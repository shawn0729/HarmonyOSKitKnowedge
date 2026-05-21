#!/usr/bin/env python3
"""
synthesize_meta_json.py — Deterministic meta.json synthesizer for a2h pipeline.

Extracts deterministic fields from Android source code and XML resources,
reducing LLM dependency for meta.json generation. Supports two modes:
  - scaffold: Generate meta.json skeleton from scratch (deterministic fields only)
  - enrich:   Read existing meta.json, verify/supplement deterministic fields

Usage:
  # Scaffold mode: generate skeleton before LLM analysis
  python3 synthesize_meta_json.py $ANDROID_SRC \
    --activity de.danoeh.antennapod.activity.MainActivity \
    --page-id page_0001_MainActivity \
    --output spec/baseline/ui-snapshots/page_0001_MainActivity/meta.json \
    --mode scaffold \
    --package de.danoeh.antennapod

  # Enrich mode: merge into existing meta.json after LLM analysis
  python3 synthesize_meta_json.py $ANDROID_SRC \
    --activity de.danoeh.antennapod.activity.MainActivity \
    --page-id page_0001_MainActivity \
    --output spec/baseline/ui-snapshots/page_0001_MainActivity/meta.json \
    --mode enrich \
    --existing spec/baseline/ui-snapshots/page_0001_MainActivity/meta.json \
    --view-xml spec/baseline/ui-snapshots/page_0001_MainActivity/view.xml \
    --package de.danoeh.antennapod

Reuses parsing infrastructure from parse_layouts.py (same directory).
"""

import xml.etree.ElementTree as ET
import json
import sys
import os
import re
import argparse
from pathlib import Path

# Import from sibling modules
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from parse_layouts import (
    find_layout_files, find_menu_files, find_string_values,
    detect_project_packages,
    NS_ANDROID, NS_APP,
)
from synthesize_view_xml import CLICKABLE_BY_DEFAULT, MENU_CARRIER_CLASSES


# ─── Regex patterns ───

# Layout binding patterns
RE_SET_CONTENT_VIEW = re.compile(r'setContentView\s*\(\s*R\.layout\.(\w+)')
RE_INFLATE_LAYOUT = re.compile(r'\.inflate\s*\(\s*R\.layout\.(\w+)')
RE_BINDING_INFLATE = re.compile(r'(\w+)Binding\.inflate')
RE_PREF_RESOURCE = re.compile(r'addPreferencesFromResource\s*\(\s*R\.xml\.(\w+)')

# Menu binding patterns
RE_MENU_REF = re.compile(r'R\.menu\.(\w+)')

# Fragment TAG patterns
RE_TAG_JAVA = re.compile(
    r'(?:public|private|protected)?\s*static\s+final\s+String\s+TAG\s*=\s*"([^"]+)"'
)
RE_TAG_KOTLIN = re.compile(r'const\s+val\s+TAG\s*=\s*"([^"]+)"')
RE_CLASS_DECL = re.compile(r'(?:public\s+)?(?:abstract\s+)?class\s+(\w+)')
RE_KOTLIN_CLASS = re.compile(r'(?:abstract\s+)?class\s+(\w+)')

# Navigation patterns
RE_INTENT_TARGET = re.compile(
    r'Intent\s*\([^,]+,\s*(\w+)(?:\.class|::class(?:\.java)?)'
)
RE_LOAD_FRAGMENT = re.compile(
    r'(?:loadFragment|replace)\s*\([^,]*,?\s*(?:new\s+)?([A-Z]\w{2,})(?:\s*\(\)|\.TAG|\.class)'
)
RE_NAV_NAVIGATE = re.compile(r'navigate\s*\(\s*R\.id\.(\w+)')

# Adapter patterns
RE_ADAPTER_REF = re.compile(r'(?:new\s+|=\s*new\s+|:\s*)(\w+Adapter)\s*[(<]')
RE_ON_CREATE_VH = re.compile(r'onCreateViewHolder\s*\(')

# Style reference in layout XML
RE_STYLE_REF_XML = re.compile(r'@style/([^\s"]+)')


# ─── Fields classification ───

# Fields that the script always overwrites (more reliable than LLM)
OVERWRITE_FIELDS = {
    "layout_sources", "menu_sources", "fragment_tags",
    "style_sources", "recycler_item_layouts",
}

# Fields that preserve LLM values in enrich mode
LLM_ONLY_FIELDS = {
    "label", "confidence", "dynamic_menus", "bottom_sheet_config",
    "navigation_mode", "came_from", "trigger_element", "click_path",
}

# Fields that merge script + LLM data
MERGE_FIELDS = {
    "clickable_elements", "navigation_targets",
}


# ─── SourceLocator ───

class SourceLocator:
    """Finds and caches Java/Kotlin source files in an Android project."""

    def __init__(self, project_root):
        self.project_root = project_root
        self._index_simple = {}   # {SimpleClassName: [abs_path, ...]}
        self._index_fqn = {}      # {fully.qualified.Name: abs_path}
        self._content_cache = {}  # {abs_path: content}
        self._build_index()

    def _build_index(self):
        """Walk project once, build class-name-to-path indices."""
        for root, dirs, files in os.walk(self.project_root):
            # Skip build/test/generated directories
            dirs[:] = [d for d in dirs if d not in (
                "build", ".gradle", ".idea", "test", "androidTest",
                "generated", "intermediates", "node_modules",
            )]
            for f in files:
                if not (f.endswith(".java") or f.endswith(".kt")):
                    continue
                abs_path = os.path.join(root, f)
                simple_name = f.rsplit(".", 1)[0]

                # Index by simple class name
                if simple_name not in self._index_simple:
                    self._index_simple[simple_name] = []
                self._index_simple[simple_name].append(abs_path)

                # Index by FQN derived from path
                rel = os.path.relpath(abs_path, self.project_root)
                # Extract package from path: */src/main/java/com/example/Foo.java
                for marker in ("src/main/java/", "src/main/kotlin/"):
                    idx = rel.find(marker)
                    if idx >= 0:
                        pkg_path = rel[idx + len(marker):]
                        fqn = pkg_path.replace(os.sep, ".").replace("/", ".")
                        fqn = fqn.rsplit(".", 1)[0]  # strip .java/.kt
                        self._index_fqn[fqn] = abs_path
                        break

    def find_source(self, fqn_or_simple):
        """Find source file for a fully-qualified or simple class name."""
        # Try FQN first
        if fqn_or_simple in self._index_fqn:
            return self._index_fqn[fqn_or_simple]

        # Try simple name
        simple = fqn_or_simple.rsplit(".", 1)[-1]
        paths = self._index_simple.get(simple, [])
        if len(paths) == 1:
            return paths[0]
        if len(paths) > 1:
            # Prefer path matching the FQN structure
            fqn_parts = fqn_or_simple.replace(".", os.sep)
            for p in paths:
                if fqn_parts in p:
                    return p
            return paths[0]  # fallback to first match
        return None

    def read_source(self, path):
        """Read and cache file content."""
        if path not in self._content_cache:
            try:
                with open(path, "r", encoding="utf-8") as f:
                    self._content_cache[path] = f.read()
            except (IOError, UnicodeDecodeError):
                self._content_cache[path] = ""
        return self._content_cache[path]

    def all_source_files(self):
        """Yield all (simple_name, abs_path) pairs."""
        for name, paths in self._index_simple.items():
            for p in paths:
                yield name, p


# ─── Extractors ───

def _binding_to_layout(binding_name):
    """Convert ViewBinding class name to layout name.
    ActivityMainBinding -> activity_main
    FragmentHomeBinding -> fragment_home
    """
    name = binding_name
    if name.endswith("Binding"):
        name = name[:-7]
    # CamelCase to snake_case
    result = re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()
    return result


def _collect_includes(layout_path, layout_files, visited=None):
    """Recursively collect <include> referenced layout paths."""
    if visited is None:
        visited = set()
    if layout_path in visited:
        return []
    visited.add(layout_path)

    results = []
    try:
        tree = ET.parse(layout_path)
    except (ET.ParseError, IOError):
        return results

    for elem in tree.iter():
        # <include layout="@layout/xxx">
        layout_ref = elem.get("layout", "")
        if not layout_ref:
            layout_ref = elem.get(f"{{{NS_ANDROID}}}layout", "")
        if layout_ref.startswith("@layout/"):
            inc_name = layout_ref.split("/", 1)[1]
            if inc_name in layout_files:
                inc_path = layout_files[inc_name]
                results.append(inc_path)
                results.extend(_collect_includes(inc_path, layout_files, visited))
    return results


def extract_layout_sources(source_content, layout_files, project_root):
    """Extract layout file paths from Activity/Fragment source code.

    Returns list of relative paths (relative to project_root).
    """
    layout_names = set()

    # R.layout.xxx references
    for m in RE_SET_CONTENT_VIEW.finditer(source_content):
        layout_names.add(m.group(1))
    for m in RE_INFLATE_LAYOUT.finditer(source_content):
        layout_names.add(m.group(1))

    # ViewBinding: XxxBinding.inflate -> layout name
    for m in RE_BINDING_INFLATE.finditer(source_content):
        layout_name = _binding_to_layout(m.group(1))
        layout_names.add(layout_name)

    # PreferenceFragment: addPreferencesFromResource(R.xml.xxx)
    for m in RE_PREF_RESOURCE.finditer(source_content):
        layout_names.add(f"xml/{m.group(1)}")  # mark as xml resource

    # Resolve names to paths and collect includes
    all_paths = set()
    for name in layout_names:
        if name.startswith("xml/"):
            # Search for xml resource files
            xml_name = name[4:]
            for root, dirs, files in os.walk(project_root):
                rel = os.path.relpath(root, project_root)
                parts = Path(rel).parts
                if len(parts) >= 2 and parts[-2] == "res" and parts[-1].startswith("xml"):
                    for f in files:
                        if f == f"{xml_name}.xml":
                            all_paths.add(os.path.join(root, f))
        elif name in layout_files:
            path = layout_files[name]
            all_paths.add(path)
            # Recursively collect includes
            for inc_path in _collect_includes(path, layout_files):
                all_paths.add(inc_path)

    # Convert to relative paths and validate
    result = []
    for abs_path in sorted(all_paths):
        rel_path = os.path.relpath(abs_path, project_root)
        if os.path.isfile(abs_path):
            result.append(rel_path)
        else:
            print(f"  [WARN] Layout path not found: {rel_path}", file=sys.stderr)

    return result


def extract_menu_sources(source_content, layout_paths, menu_files, project_root):
    """Extract menu XML file paths from source code and layout XMLs.

    Returns list of relative paths.
    """
    menu_names = set()

    # R.menu.xxx in source code
    for m in RE_MENU_REF.finditer(source_content):
        menu_names.add(m.group(1))

    # app:menu="@menu/xxx" in layout XMLs
    for layout_path in layout_paths:
        abs_path = os.path.join(project_root, layout_path) if not os.path.isabs(layout_path) else layout_path
        try:
            tree = ET.parse(abs_path)
            for elem in tree.iter():
                menu_attr = elem.get(f"{{{NS_APP}}}menu", "")
                if menu_attr.startswith("@menu/"):
                    menu_names.add(menu_attr.split("/", 1)[1])
        except (ET.ParseError, IOError):
            pass

    # Resolve to file paths
    result = []
    for name in sorted(menu_names):
        if name in menu_files:
            rel_path = os.path.relpath(menu_files[name], project_root)
            result.append(rel_path)
        else:
            print(f"  [WARN] Menu '{name}' not found in project", file=sys.stderr)

    return result


def extract_fragment_tags(source_locator):
    """Extract Fragment TAG constants from all source files.

    Returns {ClassName: TAG_value} mapping.
    Only includes classes that look like Fragment/Activity/View subclasses.
    """
    tags = {}
    for simple_name, abs_path in source_locator.all_source_files():
        content = source_locator.read_source(abs_path)
        if not content:
            continue

        # Find TAG constant
        tag_value = None
        for m in RE_TAG_JAVA.finditer(content):
            tag_value = m.group(1)
            break
        if tag_value is None:
            for m in RE_TAG_KOTLIN.finditer(content):
                tag_value = m.group(1)
                break

        if tag_value is None:
            continue

        # Use filename as class name (most reliable)
        class_name = simple_name  # filename without extension

        # Validate: class name must start with uppercase and be at least 3 chars
        if not class_name or len(class_name) < 3 or not class_name[0].isupper():
            continue

        tags[class_name] = tag_value

    return tags


def extract_style_sources(layout_paths, project_root):
    """Extract style/theme file paths referenced by layout XMLs.

    Returns list of relative paths.
    """
    style_names = set()
    style_file_index = {}  # {style_name: rel_path_to_defining_file}

    # Collect style references from layout XMLs
    for layout_path in layout_paths:
        abs_path = os.path.join(project_root, layout_path) if not os.path.isabs(layout_path) else layout_path
        try:
            tree = ET.parse(abs_path)
            for elem in tree.iter():
                # style="@style/xxx"
                style_val = elem.get("style", "")
                if style_val.startswith("@style/"):
                    style_names.add(style_val[7:])
                # Also check app:itemTextAppearanceActive etc.
                for attr_val in elem.attrib.values():
                    if isinstance(attr_val, str) and attr_val.startswith("@style/"):
                        style_names.add(attr_val[7:])
        except (ET.ParseError, IOError):
            pass

    # Build index: {style_name: file_path} from all values/ dirs
    all_style_files = set()
    for root, dirs, files in os.walk(project_root):
        rel = os.path.relpath(root, project_root)
        parts = Path(rel).parts
        if len(parts) < 2 or parts[-2] != "res":
            continue
        if not parts[-1].startswith("values"):
            continue
        for fname in files:
            if not fname.endswith(".xml"):
                continue
            abs_file = os.path.join(root, fname)
            rel_file = os.path.relpath(abs_file, project_root)
            is_style_file = any(kw in fname for kw in ("style", "theme", "color"))

            # Add "standard trio" unconditionally
            if fname in ("styles.xml", "themes.xml", "colors.xml"):
                all_style_files.add(rel_file)

            # Parse for style definitions
            if any(kw in fname for kw in ("style", "theme")):
                try:
                    tree = ET.parse(abs_file)
                    for elem in tree.getroot():
                        if elem.tag == "style" and "name" in elem.attrib:
                            style_file_index[elem.attrib["name"]] = rel_file
                except (ET.ParseError, IOError):
                    pass

    # Add files that define referenced styles
    for name in style_names:
        if name in style_file_index:
            all_style_files.add(style_file_index[name])

    return sorted(all_style_files)


def extract_recycler_item_layouts(source_content, source_locator, layout_files, project_root):
    """Extract RecyclerView adapter item layouts.

    Returns [{"adapter": "XxxAdapter", "layouts": ["layout_name", ...]}]
    """
    results = []

    # Find adapter class references in the source
    adapter_names = set()
    for m in RE_ADAPTER_REF.finditer(source_content):
        adapter_names.add(m.group(1))

    # Also check for inner class adapter definitions
    for m in re.finditer(r'class\s+(\w+Adapter)\s', source_content):
        adapter_names.add(m.group(1))

    for adapter_name in sorted(adapter_names):
        # Find adapter source file
        adapter_path = source_locator.find_source(adapter_name)
        if adapter_path is None:
            continue

        adapter_content = source_locator.read_source(adapter_path)
        if not adapter_content:
            continue

        # Extract layouts from onCreateViewHolder method body
        layouts = set()
        vh_match = RE_ON_CREATE_VH.search(adapter_content)
        if vh_match:
            method_body = _extract_method_body(adapter_content, vh_match.start())
            for m in RE_INFLATE_LAYOUT.finditer(method_body):
                layouts.add(m.group(1))
            # Also catch R.layout.xxx without .inflate prefix
            for m in re.finditer(r'R\.layout\.(\w+)', method_body):
                layouts.add(m.group(1))

        if layouts:
            results.append({
                "adapter": adapter_name,
                "layouts": sorted(layouts),
            })

    return results


def _extract_method_body(source, start_pos):
    """Extract method body by counting braces from the first { after start_pos."""
    brace_start = source.find("{", start_pos)
    if brace_start < 0:
        return ""

    depth = 0
    i = brace_start
    while i < len(source):
        ch = source[i]
        if ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                return source[brace_start:i + 1]
        elif ch == '"':
            # Skip string literals
            i += 1
            while i < len(source) and source[i] != '"':
                if source[i] == '\\':
                    i += 1
                i += 1
        elif ch == '/' and i + 1 < len(source):
            if source[i + 1] == '/':
                # Skip line comment
                while i < len(source) and source[i] != '\n':
                    i += 1
            elif source[i + 1] == '*':
                # Skip block comment
                i += 2
                while i + 1 < len(source) and not (source[i] == '*' and source[i + 1] == '/'):
                    i += 1
                i += 1
        i += 1
    return source[brace_start:]


def extract_clickable_elements(view_xml_path, layout_paths=None, project_root=None):
    """Extract clickable elements from synthesized view.xml.

    Falls back to layout XML scanning if view.xml is not available.
    Returns [{"class": "Button", "resource_id": "btn_xxx", "text": "...", "content_desc": "..."}]
    """
    results = []

    if view_xml_path and os.path.isfile(view_xml_path):
        # Parse view.xml
        try:
            tree = ET.parse(view_xml_path)
            for node in tree.iter("node"):
                if node.get("clickable") != "true":
                    continue
                cls = node.get("class", "")
                short_cls = cls.rsplit(".", 1)[-1] if "." in cls else cls
                res_id = node.get("resource-id", "")
                # Strip package prefix from resource-id
                if ":" in res_id:
                    res_id = res_id.split("/", 1)[-1] if "/" in res_id else res_id.split(":", 1)[-1]
                elif "/" in res_id:
                    res_id = res_id.split("/", 1)[-1]

                results.append({
                    "class": short_cls,
                    "resource_id": res_id,
                    "text": node.get("text", ""),
                    "content_desc": node.get("content-desc", ""),
                })
        except (ET.ParseError, IOError) as e:
            print(f"  [WARN] Failed to parse view.xml: {e}", file=sys.stderr)

    elif layout_paths and project_root:
        # Fallback: scan layout XMLs
        for layout_path in layout_paths:
            abs_path = os.path.join(project_root, layout_path) if not os.path.isabs(layout_path) else layout_path
            try:
                tree = ET.parse(abs_path)
                for elem in tree.iter():
                    tag = elem.tag
                    if tag in ("include", "merge", "requestFocus"):
                        continue

                    short_cls = tag.rsplit(".", 1)[-1] if "." in tag else tag
                    is_clickable = (
                        elem.get(f"{{{NS_ANDROID}}}clickable") == "true"
                        or short_cls in CLICKABLE_BY_DEFAULT
                    )
                    if not is_clickable:
                        continue

                    res_id_raw = elem.get(f"{{{NS_ANDROID}}}id", "")
                    res_id = res_id_raw.replace("@+id/", "").replace("@id/", "")

                    results.append({
                        "class": short_cls,
                        "resource_id": res_id,
                        "text": elem.get(f"{{{NS_ANDROID}}}text", ""),
                        "content_desc": elem.get(f"{{{NS_ANDROID}}}contentDescription", ""),
                    })
            except (ET.ParseError, IOError):
                pass

    return results


def extract_navigation_targets(source_content):
    """Extract navigation targets from Activity/Fragment source code.

    Returns {"trigger_or_target_id": "TargetClassName"} mapping.
    """
    targets = {}

    # Intent-based Activity jumps
    for m in RE_INTENT_TARGET.finditer(source_content):
        target_class = m.group(1)
        # Try to find nearby R.id reference as trigger
        context_before = source_content[max(0, m.start() - 200):m.start()]
        trigger_match = re.search(r'R\.id\.(\w+)', context_before)
        trigger = trigger_match.group(1) if trigger_match else f"intent_{target_class.lower()}"
        targets[trigger] = target_class

    # Fragment loading via ClassName.TAG pattern
    # e.g., loadFragment(HomeFragment.TAG, null)
    for m in re.finditer(r'loadFragment\s*\(\s*([A-Z]\w{2,})\.TAG', source_content):
        target_class = m.group(1)
        targets[f"fragment_{target_class}"] = target_class

    # Fragment transaction replace with ClassName.TAG
    # e.g., transaction.replace(R.id.xxx, fragment, NavDrawerFragment.TAG)
    for m in re.finditer(
        r'\.replace\s*\(\s*R\.id\.(\w+)\s*,\s*\w+\s*,\s*([A-Z]\w{2,})\.TAG',
        source_content
    ):
        container_id = m.group(1)
        target_class = m.group(2)
        targets[container_id] = target_class

    # Navigation Component
    for m in RE_NAV_NAVIGATE.finditer(source_content):
        action_id = m.group(1)
        targets[action_id] = f"nav_action_{action_id}"

    return targets


# ─── MetaSynthesizer ───

class MetaSynthesizer:
    """Orchestrates all extractors to produce a meta.json dict."""

    def __init__(self, project_root, activity_fqn, page_id, package,
                 view_xml_path=None,
                 layout_files=None, menu_files=None):
        self.project_root = project_root
        self.activity_fqn = activity_fqn
        self.page_id = page_id
        self.package = package
        self.view_xml_path = view_xml_path
        self.layout_files = layout_files or {}
        self.menu_files = menu_files or {}
        self.source_locator = SourceLocator(project_root)

        # Locate and read the activity source
        self.activity_source_path = self.source_locator.find_source(activity_fqn)
        self.activity_source = ""
        if self.activity_source_path:
            self.activity_source = self.source_locator.read_source(self.activity_source_path)
            print(f"Found activity source: {os.path.relpath(self.activity_source_path, project_root)}",
                  file=sys.stderr)
        else:
            print(f"  [WARN] Activity source not found: {activity_fqn}", file=sys.stderr)

    def _run_extractors(self):
        """Run all extractors and return their results."""
        results = {}

        # 1. layout_sources
        try:
            results["layout_sources"] = extract_layout_sources(
                self.activity_source, self.layout_files, self.project_root
            )
            print(f"Extracting layout_sources... found {len(results['layout_sources'])}",
                  file=sys.stderr)
        except Exception as e:
            print(f"  [WARN] extract_layout_sources failed: {e}", file=sys.stderr)
            results["layout_sources"] = []

        # 2. menu_sources (depends on layout_sources)
        try:
            results["menu_sources"] = extract_menu_sources(
                self.activity_source, results["layout_sources"],
                self.menu_files, self.project_root
            )
            print(f"Extracting menu_sources... found {len(results['menu_sources'])}",
                  file=sys.stderr)
        except Exception as e:
            print(f"  [WARN] extract_menu_sources failed: {e}", file=sys.stderr)
            results["menu_sources"] = []

        # 3. fragment_tags (global scan)
        try:
            results["fragment_tags"] = extract_fragment_tags(self.source_locator)
            print(f"Extracting fragment_tags... found {len(results['fragment_tags'])}",
                  file=sys.stderr)
        except Exception as e:
            print(f"  [WARN] extract_fragment_tags failed: {e}", file=sys.stderr)
            results["fragment_tags"] = {}

        # 4. style_sources (depends on layout_sources)
        try:
            results["style_sources"] = extract_style_sources(
                results["layout_sources"], self.project_root
            )
            print(f"Extracting style_sources... found {len(results['style_sources'])}",
                  file=sys.stderr)
        except Exception as e:
            print(f"  [WARN] extract_style_sources failed: {e}", file=sys.stderr)
            results["style_sources"] = []

        # 5. recycler_item_layouts
        try:
            results["recycler_item_layouts"] = extract_recycler_item_layouts(
                self.activity_source, self.source_locator,
                self.layout_files, self.project_root
            )
            print(f"Extracting recycler_item_layouts... found {len(results['recycler_item_layouts'])}",
                  file=sys.stderr)
        except Exception as e:
            print(f"  [WARN] extract_recycler_item_layouts failed: {e}", file=sys.stderr)
            results["recycler_item_layouts"] = []

        # 6. clickable_elements
        try:
            results["clickable_elements"] = extract_clickable_elements(
                self.view_xml_path, results["layout_sources"], self.project_root
            )
            print(f"Extracting clickable_elements... found {len(results['clickable_elements'])}",
                  file=sys.stderr)
        except Exception as e:
            print(f"  [WARN] extract_clickable_elements failed: {e}", file=sys.stderr)
            results["clickable_elements"] = []

        # 7. navigation_targets
        try:
            results["navigation_targets"] = extract_navigation_targets(self.activity_source)
            print(f"Extracting navigation_targets... found {len(results['navigation_targets'])} (partial confidence)",
                  file=sys.stderr)
        except Exception as e:
            print(f"  [WARN] extract_navigation_targets failed: {e}", file=sys.stderr)
            results["navigation_targets"] = {}

        return results

    def scaffold(self):
        """Generate meta.json skeleton from scratch (deterministic fields only).

        LLM-only fields are set to default placeholders.
        """
        extracted = self._run_extractors()

        meta = {
            # Identity
            "page_id": self.page_id,
            "label": "",                    # LLM fills
            "activity": self.activity_fqn,
            # Quality
            "confidence": "medium",         # LLM can override
            "auto_generated": True,
            "view_xml_synthesized": False,
            # Deterministic fields
            "layout_sources": extracted["layout_sources"],
            "style_sources": extracted["style_sources"],
            "menu_sources": extracted["menu_sources"],
            "fragment_tags": extracted["fragment_tags"],
            "recycler_item_layouts": extracted["recycler_item_layouts"],
            # Mixed fields
            "navigation_targets": extracted["navigation_targets"],
            "clickable_elements": extracted["clickable_elements"],
            # LLM-only fields (defaults)
            "dynamic_menus": {},
            "bottom_sheet_config": {},
            "navigation_mode": "UNKNOWN",
            "came_from": None,
            "trigger_element": None,
            "click_path": [],
        }

        return meta

    def enrich(self, existing):
        """Read existing meta.json, verify/supplement deterministic fields.

        Rules:
        - OVERWRITE_FIELDS: script always overwrites (more reliable)
        - LLM_ONLY_FIELDS: preserve existing values
        - MERGE_FIELDS: script as base + LLM additions that don't conflict
        """
        extracted = self._run_extractors()

        result = dict(existing)

        # Always set identity fields
        result["page_id"] = self.page_id
        result["activity"] = self.activity_fqn
        result["auto_generated"] = existing.get("auto_generated", True)

        # Overwrite deterministic fields
        for field in OVERWRITE_FIELDS:
            if field in extracted:
                result[field] = extracted[field]

        # Preserve LLM-only fields (use existing or default)
        for field in LLM_ONLY_FIELDS:
            if field not in result:
                defaults = {
                    "label": "",
                    "confidence": "medium",
                    "dynamic_menus": {},
                    "bottom_sheet_config": {},
                    "navigation_mode": "UNKNOWN",
                    "came_from": None,
                    "trigger_element": None,
                    "click_path": [],
                }
                result[field] = defaults.get(field)

        # Merge clickable_elements: use script output, add LLM extras
        script_clickables = extracted.get("clickable_elements", [])
        existing_clickables = existing.get("clickable_elements", [])
        script_ids = {e.get("resource_id") for e in script_clickables if e.get("resource_id")}
        merged_clickables = list(script_clickables)
        for ec in existing_clickables:
            if ec.get("resource_id") and ec["resource_id"] not in script_ids:
                merged_clickables.append(ec)
        result["clickable_elements"] = merged_clickables

        # Merge navigation_targets: script as base + LLM additions
        script_nav = extracted.get("navigation_targets", {})
        existing_nav = existing.get("navigation_targets", {})
        merged_nav = dict(script_nav)
        for k, v in existing_nav.items():
            if k not in merged_nav:
                merged_nav[k] = v
        result["navigation_targets"] = merged_nav

        # Ensure all schema fields exist
        schema_defaults = {
            "view_xml_synthesized": False,
            "layout_sources": [],
            "style_sources": [],
            "menu_sources": [],
            "fragment_tags": {},
            "recycler_item_layouts": [],
            "navigation_targets": {},
            "clickable_elements": [],
            "dynamic_menus": {},
            "bottom_sheet_config": {},
            "navigation_mode": "UNKNOWN",
            "came_from": None,
            "trigger_element": None,
            "click_path": [],
        }
        for field, default in schema_defaults.items():
            if field not in result:
                result[field] = default

        return result


# ─── CLI ───

def main():
    parser = argparse.ArgumentParser(
        description="Synthesize meta.json from Android source code and XML resources."
    )
    parser.add_argument("project_root",
                        help="Android project root path ($ANDROID_SRC)")
    parser.add_argument("--activity", required=True,
                        help="Fully qualified Activity/Fragment class name")
    parser.add_argument("--page-id", required=True,
                        help="Page ID (e.g., page_0001_MainActivity)")
    parser.add_argument("--output", required=True,
                        help="Output meta.json path")
    parser.add_argument("--mode", choices=["scaffold", "enrich"], default="scaffold",
                        help="scaffold: generate from scratch; enrich: merge into existing")
    parser.add_argument("--existing", default=None,
                        help="Path to existing meta.json (required for enrich mode)")
    parser.add_argument("--view-xml", default=None,
                        help="Path to synthesized view.xml (for clickable_elements extraction)")
    parser.add_argument("--package", default="",
                        help="Android package name")
    parser.add_argument("--dry-run", action="store_true",
                        help="Output to stdout without writing file")

    args = parser.parse_args()

    if args.mode == "enrich" and not args.existing:
        print("Error: --existing is required for enrich mode", file=sys.stderr)
        sys.exit(1)

    project_root = os.path.abspath(args.project_root)
    if not os.path.isdir(project_root):
        print(f"Error: Project root not found: {project_root}", file=sys.stderr)
        sys.exit(1)

    print(f"Mode: {args.mode}", file=sys.stderr)
    print(f"Activity: {args.activity}", file=sys.stderr)
    print(f"Page ID: {args.page_id}", file=sys.stderr)

    # Discover resources
    layout_files = find_layout_files(project_root)
    menu_files = find_menu_files(project_root)
    print(f"Found {len(layout_files)} layout files in project", file=sys.stderr)
    print(f"Found {len(menu_files)} menu files in project", file=sys.stderr)

    # Auto-detect package if not provided
    package = args.package
    if not package:
        packages = detect_project_packages(project_root)
        if packages:
            package = sorted(packages, key=len)[0]
            print(f"Auto-detected package: {package}", file=sys.stderr)

    # Initialize synthesizer
    synthesizer = MetaSynthesizer(
        project_root=project_root,
        activity_fqn=args.activity,
        page_id=args.page_id,
        package=package,
        view_xml_path=args.view_xml,
        layout_files=layout_files,
        menu_files=menu_files,
    )

    # Run
    if args.mode == "scaffold":
        result = synthesizer.scaffold()
    else:
        # Load existing meta.json
        try:
            with open(args.existing, "r", encoding="utf-8") as f:
                existing = json.load(f)
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error reading existing meta.json: {e}", file=sys.stderr)
            sys.exit(1)
        result = synthesizer.enrich(existing)

    # Output
    output_json = json.dumps(result, indent=2, ensure_ascii=False)

    if args.dry_run:
        print(output_json)
    else:
        output_path = args.output
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(output_json)
            f.write("\n")
        print(f"\nSynthesized meta.json ({len(result)} fields) -> {output_path}",
              file=sys.stderr)

    sys.exit(0)


if __name__ == "__main__":
    main()
