#!/usr/bin/env python3
"""
parse_layouts.py — Deterministic XML layout parser for Android UI Graph Builder.

Parses all XML layout files referenced by screens, extracts:
  - Component nodes  → components_raw.json
  - Containment edges → containment_raw.json

Usage:
  python3 parse_layouts.py <project_root> <screen_json_path> <output_dir>

The script reads Screen.json to know which layouts to parse (layout_ref field),
then recursively parses those layouts including any <include> / <merge> / <fragment> tags.
"""

import xml.etree.ElementTree as ET
import json
import sys
import os
import re
from pathlib import Path
from collections import defaultdict

# ─── Standard widget package mapping ───
STANDARD_WIDGETS = {
    "View": "android.view.View",
    "ViewStub": "android.view.ViewStub",
    "TextureView": "android.view.TextureView",
    "SurfaceView": "android.view.SurfaceView",
    "WebView": "android.webkit.WebView",
}

WIDGET_PACKAGE = "android.widget"
VIEW_PACKAGE = "android.view"
WEBKIT_PACKAGE = "android.webkit"

VIEWGROUP_CLASSES = {
    "LinearLayout", "RelativeLayout", "FrameLayout", "TableLayout", "TableRow",
    "GridLayout", "AbsoluteLayout", "RadioGroup", "ScrollView", "HorizontalScrollView",
    "NestedScrollView", "ViewFlipper", "ViewSwitcher", "ViewAnimator",
    "ConstraintLayout", "CoordinatorLayout", "AppBarLayout", "CollapsingToolbarLayout",
    "DrawerLayout", "NavigationView", "SwipeRefreshLayout", "RecyclerView",
    "ViewPager", "ViewPager2", "CardView", "MaterialCardView",
    "BottomNavigationView", "TabLayout", "Toolbar", "MaterialToolbar",
    "TextInputLayout", "ChipGroup", "FlowLayout", "MotionLayout",
    "FragmentContainerView", "NavHostFragment",
}

# Namespaces
NS_ANDROID = "http://schemas.android.com/apk/res/android"
NS_APP = "http://schemas.android.com/apk/res-auto"
NS_TOOLS = "http://schemas.android.com/tools"

# ─── Attribute classification ───

LAYOUT_ATTR_PREFIXES = ("layout_",)
LAYOUT_ATTRS_EXTRA = {"minWidth", "minHeight", "maxWidth", "maxHeight", "orientation", "gravity"}

BEHAVIOR_ATTRS = {
    "clickable", "longClickable", "focusable", "focusableInTouchMode",
    "enabled", "selected", "activated", "visibility", "scrollbars",
    "nestedScrollingEnabled", "overScrollMode", "tag", "transitionName",
    "inputType", "imeOptions", "editable", "digits", "maxLength",
    "selectAllOnFocus", "textIsSelectable", "checked", "checkable",
    "button", "switchMinWidth", "thumbDrawable", "trackDrawable",
    "onClick", "onLongClick", "onTouch", "onFocusChange",
}

ACCESSIBILITY_ATTRS = {
    "contentDescription", "importantForAccessibility", "accessibilityLiveRegion",
    "accessibilityHeading", "accessibilityTraversalBefore", "accessibilityTraversalAfter",
    "labelFor",
}

CONSTRAINT_ATTR_PREFIX = "layout_constraint"


def resolve_class_name(tag):
    """Resolve XML tag to full class name."""
    if "." in tag:
        return tag
    if tag in STANDARD_WIDGETS:
        return STANDARD_WIDGETS[tag]
    return f"{WIDGET_PACKAGE}.{tag}"


def short_name(full_class):
    """Extract short class name."""
    return full_class.rsplit(".", 1)[-1] if "." in full_class else full_class


def is_viewgroup(class_short, full_class):
    """Heuristic: is this a ViewGroup?"""
    if class_short in VIEWGROUP_CLASSES:
        return True
    if "Layout" in class_short or "Group" in class_short or "Container" in class_short:
        return True
    if class_short in ("Toolbar", "MaterialToolbar", "TabLayout", "BottomNavigationView",
                       "NavigationView", "RecyclerView", "ViewPager", "ViewPager2",
                       "CardView", "MaterialCardView", "TextInputLayout", "ChipGroup"):
        return True
    return False


def is_custom_view(full_class, project_packages):
    """Check if the class belongs to the project (not android.*, androidx.*, com.google.*)."""
    for pkg in project_packages:
        if full_class.startswith(pkg):
            return True
    return False


def strip_ns(attr_name):
    """Remove namespace URI from attribute name."""
    if "}" in attr_name:
        return attr_name.split("}", 1)[1]
    return attr_name


def get_ns_prefix(attr_name):
    """Get namespace prefix."""
    if f"{{{NS_ANDROID}}}" in attr_name:
        return "android"
    if f"{{{NS_APP}}}" in attr_name:
        return "app"
    if f"{{{NS_TOOLS}}}" in attr_name:
        return "tools"
    return ""


def classify_attr(ns_prefix, local_name):
    """Classify an attribute into one of the four groups."""
    if ns_prefix == "tools":
        return None  # skip tools namespace

    if local_name == "id":
        return "id"
    if local_name == "style":
        return "style_attrs"

    if local_name in ACCESSIBILITY_ATTRS:
        return "accessibility_attrs"
    if local_name in BEHAVIOR_ATTRS:
        return "behavior_attrs"

    if any(local_name.startswith(p) for p in LAYOUT_ATTR_PREFIXES):
        return "layout_attrs"
    if local_name in LAYOUT_ATTRS_EXTRA:
        return "layout_attrs"

    # constraint attrs in app namespace
    if ns_prefix == "app" and local_name.startswith(CONSTRAINT_ATTR_PREFIX):
        return "layout_attrs_constraint"

    # Everything else visual → style
    return "style_attrs"


def extract_resource_ref(attr_name, value):
    """If value is a resource reference, return a resource_ref entry."""
    if not value or not value.startswith("@"):
        return None
    # e.g. @drawable/icon, @color/primary, @+id/btn (skip id)
    if value.startswith("@+id/") or value.startswith("@id/"):
        return None
    match = re.match(r"@(\w+)/(.+)", value)
    if match:
        return {
            "attr": attr_name,
            "ref": value,
            "type": match.group(1)
        }
    return None


def parse_margin_padding(attrs, prefix):
    """Parse margin or padding into {start, end, top, bottom}."""
    result = {"start": "unknown", "end": "unknown", "top": "unknown", "bottom": "unknown"}

    all_val = attrs.get(prefix, attrs.get(f"{prefix}Horizontal", None))
    if prefix in attrs:
        all_val = attrs[prefix]
        result = {"start": all_val, "end": all_val, "top": all_val, "bottom": all_val}

    if f"{prefix}Horizontal" in attrs:
        h = attrs[f"{prefix}Horizontal"]
        result["start"] = h
        result["end"] = h
    if f"{prefix}Vertical" in attrs:
        v = attrs[f"{prefix}Vertical"]
        result["top"] = v
        result["bottom"] = v

    for direction in ("start", "end", "top", "bottom", "left", "right"):
        key = f"{prefix}{direction[0].upper()}{direction[1:]}"
        if key in attrs:
            mapped = direction
            if direction == "left":
                mapped = "start"
            elif direction == "right":
                mapped = "end"
            result[mapped] = attrs[key]

    return result


def find_layout_files(project_root):
    """Find all layout XML files in the project."""
    layout_files = {}
    for root, dirs, files in os.walk(project_root):
        # Only look in res/layout* directories
        rel = os.path.relpath(root, project_root)
        parts = Path(rel).parts
        if len(parts) >= 2 and parts[-2] == "res" and parts[-1].startswith("layout"):
            for f in files:
                if f.endswith(".xml"):
                    layout_name = f.replace(".xml", "")
                    full_path = os.path.join(root, f)
                    # Prefer base layout/ over qualified layout-xxx/
                    if layout_name not in layout_files or parts[-1] == "layout":
                        layout_files[layout_name] = full_path
    return layout_files


def detect_project_packages(project_root):
    """Detect project base packages from AndroidManifest.xml or source files."""
    packages = set()
    for root, dirs, files in os.walk(project_root):
        for f in files:
            if f == "AndroidManifest.xml":
                try:
                    tree = ET.parse(os.path.join(root, f))
                    pkg = tree.getroot().get("package")
                    if pkg:
                        packages.add(pkg)
                except Exception:
                    pass
    return packages


def find_menu_files(project_root):
    """Find all menu XML files in the project (res/menu*/*.xml)."""
    menu_files = {}
    for root, dirs, files in os.walk(project_root):
        rel = os.path.relpath(root, project_root)
        parts = Path(rel).parts
        if len(parts) >= 2 and parts[-2] == "res" and parts[-1].startswith("menu"):
            for f in files:
                if f.endswith(".xml"):
                    menu_name = f.replace(".xml", "")
                    full_path = os.path.join(root, f)
                    # Prefer base menu/ over qualified menu-xxx/
                    if menu_name not in menu_files or parts[-1] == "menu":
                        menu_files[menu_name] = full_path
    return menu_files


def find_string_values(project_root):
    """Read all res/values/strings.xml files and return {name: value} dict.

    Scans all modules for strings.xml, merging results. App-module strings
    override library-module strings when names collide.
    """
    strings = {}
    app_strings = {}
    for root, dirs, files in os.walk(project_root):
        if "strings.xml" not in files:
            continue
        rel = os.path.relpath(root, project_root)
        parts = Path(rel).parts
        # Only base values/ (not values-xx/ for other locales)
        if len(parts) < 2 or parts[-1] != "values" or parts[-2] != "res":
            continue
        filepath = os.path.join(root, "strings.xml")
        try:
            tree = ET.parse(filepath)
            for elem in tree.getroot():
                if elem.tag == "string" and "name" in elem.attrib:
                    text = elem.text or ""
                    is_app_module = "app/" in rel or rel.count("/") <= 3
                    if is_app_module:
                        app_strings[elem.attrib["name"]] = text
                    elif elem.attrib["name"] not in strings:
                        strings[elem.attrib["name"]] = text
        except ET.ParseError:
            pass
    # App module strings take priority
    strings.update(app_strings)
    return strings


def find_style_values(project_root):
    """Read all res/values/styles.xml and themes.xml, return style definitions.

    Returns: {style_name: {"parent": str|None, "attrs": {attr_name: value}}}
    Handles style inheritance chains.
    """
    styles = {}
    for root, dirs, files in os.walk(project_root):
        rel = os.path.relpath(root, project_root)
        parts = Path(rel).parts
        if len(parts) < 2 or parts[-1] != "values" or parts[-2] != "res":
            continue
        for fname in files:
            if not fname.endswith(".xml"):
                continue
            # Parse styles.xml, themes.xml, and any file that might contain styles
            if not any(kw in fname for kw in ("style", "theme", "attr")):
                continue
            filepath = os.path.join(root, fname)
            try:
                tree = ET.parse(filepath)
                for elem in tree.getroot():
                    if elem.tag != "style":
                        continue
                    name = elem.attrib.get("name", "")
                    if not name:
                        continue
                    parent = elem.attrib.get("parent")
                    # Implicit parent from dot notation: "Foo.Bar" parent is "Foo"
                    if parent is None and "." in name:
                        parent = name.rsplit(".", 1)[0]
                    attrs = {}
                    for item in elem:
                        if item.tag == "item" and "name" in item.attrib:
                            attrs[item.attrib["name"]] = item.text or ""
                    styles[name] = {"parent": parent, "attrs": attrs}
            except ET.ParseError:
                pass
    return styles


def resolve_style_chain(style_name, styles_db, max_depth=10):
    """Resolve a style's full attribute set by walking the parent chain.

    Returns merged attrs dict with parent attrs overridden by child attrs.
    """
    merged = {}
    current = style_name
    depth = 0
    while current and depth < max_depth:
        entry = styles_db.get(current)
        if not entry:
            break
        # Parent attrs go first (child overrides)
        parent_attrs = dict(entry["attrs"])
        parent_attrs.update(merged)
        merged = parent_attrs
        current = entry.get("parent")
        depth += 1
    return merged


def layout_ref_to_name(layout_ref):
    """Convert R.layout.activity_main to activity_main."""
    if not layout_ref or layout_ref == "unknown":
        return None
    # Handle R.layout.xxx
    match = re.search(r"R\.layout\.(\w+)", layout_ref)
    if match:
        return match.group(1)
    # Handle plain name
    return layout_ref.replace(".xml", "")


class LayoutParser:
    def __init__(self, layout_files, project_packages, project_root):
        self.layout_files = layout_files  # name → path
        self.project_packages = project_packages
        self.project_root = project_root
        self.components = []
        self.containment = []
        self.parsed_layouts = set()
        self.id_counters = defaultdict(lambda: defaultdict(int))  # layout → class_short → count

    def gen_component_id(self, layout_name, element):
        """Generate deterministic component ID."""
        android_id = element.get(f"{{{NS_ANDROID}}}id")
        if android_id:
            id_val = android_id.replace("@+id/", "").replace("@id/", "")
            return f"comp:{layout_name}:{id_val}", android_id
        else:
            tag = element.tag
            cls = short_name(resolve_class_name(tag))
            self.id_counters[layout_name][cls] += 1
            counter = self.id_counters[layout_name][cls]
            return f"comp:{layout_name}:{cls}#{counter}", "none"

    def parse_layout(self, layout_name, depth_offset=0):
        """Parse a layout file and return the root component ID."""
        if layout_name in self.parsed_layouts:
            return None
        if layout_name not in self.layout_files:
            return None

        self.parsed_layouts.add(layout_name)
        filepath = self.layout_files[layout_name]

        try:
            tree = ET.parse(filepath)
        except ET.ParseError as e:
            print(f"  [WARN] Failed to parse {filepath}: {e}", file=sys.stderr)
            return None

        root = tree.getroot()

        # Handle <merge> — it doesn't produce a component itself
        if root.tag == "merge":
            # Return children directly; caller handles containment
            child_ids = []
            for idx, child in enumerate(root):
                if isinstance(child.tag, str):
                    cid = self._parse_element(child, layout_name, depth_offset)
                    if cid:
                        child_ids.append((cid, idx))
            return ("__merge__", child_ids)

        root_id = self._parse_element(root, layout_name, depth_offset)
        return root_id

    def _parse_element(self, element, layout_name, depth):
        """Recursively parse a single XML element."""
        if not isinstance(element.tag, str):
            return None

        tag = element.tag

        # Handle <include>
        if tag == "include":
            inc_layout_attr = element.get("layout", "")
            inc_name = inc_layout_attr.replace("@layout/", "")
            result = self.parse_layout(inc_name, depth)
            if result is None:
                return None
            if isinstance(result, tuple) and result[0] == "__merge__":
                # merge children become direct children — return special marker
                return ("__include_merge__", inc_name, result[1])
            return ("__include__", inc_name, result)

        # Handle <fragment>
        frag_class = element.get(f"{{{NS_ANDROID}}}name") or element.get("class")
        is_fragment_tag = (tag == "fragment" or tag == "FragmentContainerView"
                          or tag.endswith("FragmentContainerView")
                          or tag.endswith("NavHostFragment"))

        # Generate component
        full_class = resolve_class_name(tag)
        cls_short = short_name(full_class)
        comp_id, android_id = self.gen_component_id(layout_name, element)
        is_vg = is_viewgroup(cls_short, full_class)
        is_cv = is_custom_view(full_class, self.project_packages)

        # Classify attributes
        layout_attrs_raw = {}
        constraint_attrs = {}
        style_attrs_raw = {}
        behavior_attrs_raw = {}
        accessibility_attrs_raw = {}
        custom_attrs = {}
        resource_refs = []

        for attr_key, attr_val in element.attrib.items():
            ns_prefix = get_ns_prefix(attr_key)
            local = strip_ns(attr_key)

            if local == "id":
                continue
            if ns_prefix == "tools":
                continue

            category = classify_attr(ns_prefix, local)

            if category == "layout_attrs":
                # Strip layout_ prefix for storage
                stored_name = local
                layout_attrs_raw[stored_name] = attr_val
            elif category == "layout_attrs_constraint":
                # Remove layout_constraint prefix, convert to camelCase key
                c_name = local.replace("layout_constraint", "")
                c_name = c_name[0].lower() + c_name[1:] if c_name else local
                constraint_attrs[c_name] = attr_val
            elif category == "style_attrs":
                style_attrs_raw[local] = attr_val
            elif category == "behavior_attrs":
                behavior_attrs_raw[local] = attr_val
            elif category == "accessibility_attrs":
                accessibility_attrs_raw[local] = attr_val
            elif category is None:
                continue
            else:
                # app: namespace non-constraint → custom
                if ns_prefix == "app" and not local.startswith("layout_constraint"):
                    custom_attrs[local] = attr_val

            # Collect resource refs
            ref = extract_resource_ref(local, attr_val)
            if ref:
                resource_refs.append(ref)

        # Also check style attribute (no namespace)
        style_val = element.get("style")
        if style_val:
            style_attrs_raw["style"] = style_val
            ref = extract_resource_ref("style", style_val)
            if ref:
                resource_refs.append(ref)

        # Build layout_attrs
        layout_attrs = {
            "layout_width": layout_attrs_raw.get("layout_width", "unknown"),
            "layout_height": layout_attrs_raw.get("layout_height", "unknown"),
            "layout_margin": parse_margin_padding(layout_attrs_raw, "layout_margin"),
            "layout_padding": parse_margin_padding(
                {k.replace("padding", "layout_padding") if k.startswith("padding") else k: v
                 for k, v in {**layout_attrs_raw, **{strip_ns(k): v for k, v in element.attrib.items()
                              if "padding" in strip_ns(k)}}.items()},
                "layout_padding"
            ),
            "layout_gravity": layout_attrs_raw.get("layout_gravity", "unknown"),
            "layout_weight": layout_attrs_raw.get("layout_weight", "unknown"),
            "min_width": layout_attrs_raw.get("minWidth",
                         element.get(f"{{{NS_ANDROID}}}minWidth", "unknown")),
            "min_height": layout_attrs_raw.get("minHeight",
                          element.get(f"{{{NS_ANDROID}}}minHeight", "unknown")),
            "max_width": layout_attrs_raw.get("maxWidth",
                         element.get(f"{{{NS_ANDROID}}}maxWidth", "unknown")),
            "max_height": layout_attrs_raw.get("maxHeight",
                          element.get(f"{{{NS_ANDROID}}}maxHeight", "unknown")),
        }

        # Add container-specific attrs
        if is_vg:
            layout_attrs["orientation"] = element.get(f"{{{NS_ANDROID}}}orientation", "unknown")
            layout_attrs["gravity"] = element.get(f"{{{NS_ANDROID}}}gravity", "unknown")

        # Add constraint attrs if any
        if constraint_attrs:
            layout_attrs["constraints"] = constraint_attrs

        # Handle padding separately (it's on the view itself, not layout_)
        padding_attrs = {}
        for k, v in element.attrib.items():
            local_k = strip_ns(k)
            if local_k.startswith("padding") and get_ns_prefix(k) == "android":
                padding_attrs[local_k] = v
        if padding_attrs:
            layout_attrs["layout_padding"] = parse_margin_padding(
                {k: v for k, v in padding_attrs.items()}, "padding"
            )

        # Build component
        component = {
            "id": comp_id,
            "android_id": android_id,
            "class": full_class,
            "class_short": cls_short,
            "is_viewgroup": is_vg,
            "is_custom_view": is_cv,
            "source_layout": f"layout/{layout_name}.xml",
            "depth": depth,
            "layout_attrs": layout_attrs,
            "style_attrs": style_attrs_raw,
            "behavior_attrs": behavior_attrs_raw,
            "accessibility_attrs": accessibility_attrs_raw,
            "resource_refs": resource_refs,
            "custom_attrs": custom_attrs,
        }

        if is_fragment_tag and frag_class:
            component["_fragment_class"] = frag_class

        self.components.append(component)

        # Recurse children
        child_order = 0
        for child in element:
            if not isinstance(child.tag, str):
                continue

            child_result = self._parse_element(child, layout_name, depth + 1)

            if child_result is None:
                continue

            if isinstance(child_result, tuple):
                if child_result[0] == "__include__":
                    inc_name, inc_root_id = child_result[1], child_result[2]
                    self.containment.append({
                        "parent": comp_id,
                        "child": inc_root_id,
                        "order": child_order,
                        "source": "include",
                        "include_layout": f"layout/{inc_name}.xml"
                    })
                    child_order += 1
                elif child_result[0] == "__include_merge__":
                    inc_name, merge_children = child_result[1], child_result[2]
                    for merge_child_id, _ in merge_children:
                        self.containment.append({
                            "parent": comp_id,
                            "child": merge_child_id,
                            "order": child_order,
                            "source": "merge",
                            "include_layout": f"layout/{inc_name}.xml"
                        })
                        child_order += 1
            else:
                child_id = child_result
                source = "fragment_tag" if child.tag == "fragment" else "direct"
                self.containment.append({
                    "parent": comp_id,
                    "child": child_id,
                    "order": child_order,
                    "source": source,
                    "include_layout": "none"
                })
                child_order += 1

        return comp_id


def main():
    if len(sys.argv) < 4:
        print("Usage: python3 parse_layouts.py <project_root> <screen_json_path> <output_dir>")
        sys.exit(1)

    project_root = sys.argv[1]
    screen_json_path = sys.argv[2]
    output_dir = sys.argv[3]

    os.makedirs(output_dir, exist_ok=True)

    # Load Screen.json
    with open(screen_json_path, "r", encoding="utf-8") as f:
        screens = json.load(f)

    # Find all layout files
    layout_files = find_layout_files(project_root)
    print(f"Found {len(layout_files)} layout files in project", file=sys.stderr)

    # Detect project packages
    project_packages = detect_project_packages(project_root)
    print(f"Detected project packages: {project_packages}", file=sys.stderr)

    # Initialize parser
    parser = LayoutParser(layout_files, project_packages, project_root)

    # Parse layouts referenced by screens
    screen_layout_map = []
    for screen in screens:
        layout_name = layout_ref_to_name(screen.get("layout_ref", "unknown"))
        if layout_name and layout_name in layout_files:
            result = parser.parse_layout(layout_name)
            if result and not isinstance(result, tuple):
                screen_layout_map.append((screen["id"], result))
                # Add Screen → root containment edge
                parser.containment.insert(0, {
                    "parent": screen["id"],
                    "child": result,
                    "order": 0,
                    "source": "direct",
                    "include_layout": "none"
                })
            elif isinstance(result, tuple) and result[0] == "__merge__":
                for child_id, idx in result[1]:
                    parser.containment.insert(0, {
                        "parent": screen["id"],
                        "child": child_id,
                        "order": idx,
                        "source": "merge",
                        "include_layout": "none"
                    })
        else:
            if layout_name:
                print(f"  [WARN] Layout '{layout_name}' not found for screen {screen['id']}", file=sys.stderr)

    # Save outputs
    comp_path = os.path.join(output_dir, "components_raw.json")
    cont_path = os.path.join(output_dir, "containment_raw.json")

    with open(comp_path, "w", encoding="utf-8") as f:
        json.dump(parser.components, f, indent=2, ensure_ascii=False)

    with open(cont_path, "w", encoding="utf-8") as f:
        json.dump(parser.containment, f, indent=2, ensure_ascii=False)

    print(f"\nResults:", file=sys.stderr)
    print(f"  Components:  {len(parser.components)} → {comp_path}", file=sys.stderr)
    print(f"  Containment: {len(parser.containment)} → {cont_path}", file=sys.stderr)
    print(f"  Layouts parsed: {sorted(parser.parsed_layouts)}", file=sys.stderr)


if __name__ == "__main__":
    main()
