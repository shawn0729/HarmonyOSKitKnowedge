#!/usr/bin/env python3
"""
synthesize_view_xml.py — Synthesize UIAutomator-compatible view.xml from Android layout XML.

When no real UIAutomator dump is available, this script parses Android layout XML files
and generates an approximate view.xml in UIAutomator dump format. The synthesized file
preserves view hierarchy and attributes but cannot provide runtime bounds coordinates.

Enhanced features:
  - Menu XML parsing: --menus flag or auto-follow app:menu attributes
  - String resolution: --resolve-strings resolves @string/ references
  - Style expansion: --resolve-styles inlines @style/ attribute values
  - app: attribute passthrough: key Material/custom attributes preserved in view.xml

Usage:
  python3 synthesize_view_xml.py <android_project_root> \
    --layouts "layout/activity_main.xml,layout/fragment_home.xml" \
    --menus "menu/home.xml,menu/queue.xml" \
    --resolve-strings --resolve-styles \
    --output spec/baseline/ui-snapshots/page_0001_MainActivity/view.xml \
    --package de.danoeh.antennapod

Reuses parsing infrastructure from parse_layouts.py (same directory).
"""

import xml.etree.ElementTree as ET
import sys
import os
import argparse
from pathlib import Path

# Import from sibling module
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from parse_layouts import (
    resolve_class_name, is_viewgroup, short_name,
    find_layout_files, find_menu_files, find_string_values, find_style_values,
    resolve_style_chain, detect_project_packages,
    NS_ANDROID, NS_APP, NS_TOOLS,
)

# Android default clickable widget types
CLICKABLE_BY_DEFAULT = {
    "Button", "ImageButton", "FloatingActionButton", "ExtendedFloatingActionButton",
    "Chip", "MaterialButton", "AppCompatButton", "ToggleButton",
}

SCROLLABLE_BY_DEFAULT = {
    "ScrollView", "HorizontalScrollView", "NestedScrollView",
    "RecyclerView", "ListView", "GridView", "ViewPager", "ViewPager2",
}

CHECKABLE_BY_DEFAULT = {
    "CheckBox", "RadioButton", "Switch", "SwitchCompat", "ToggleButton",
    "MaterialSwitch", "SwitchMaterial", "AppCompatCheckBox",
}

# Components that can carry app:menu attribute
MENU_CARRIER_CLASSES = {
    "BottomNavigationView", "NavigationView", "Toolbar", "MaterialToolbar",
    "ActionMenuView",
}

# Key app: namespace attributes to passthrough into view.xml nodes
APP_PASSTHROUGH_ATTRS = {
    "menu": "menu-ref",
    "labelVisibilityMode": "label-visibility",
    "itemPaddingTop": "item-padding-top",
    "itemPaddingBottom": "item-padding-bottom",
    "itemTextAppearanceActive": "item-text-active",
    "itemTextAppearanceInactive": "item-text-inactive",
    "layout_behavior": "behavior",
    "cardCornerRadius": "card-corner-radius",
    "cardElevation": "card-elevation",
    "cardBackgroundColor": "card-background-color",
    "navGraph": "nav-graph",
    "headerLayout": "header-layout",
    "layout_collapseMode": "collapse-mode",
    "layout_scrollFlags": "scroll-flags",
    "srcCompat": "src-compat",
    "endIconDrawable": "end-icon",
    "startIconDrawable": "start-icon",
    "fabSize": "fab-size",
    "elevation": "elevation",
    "backgroundTint": "background-tint",
    "tint": "tint",
    "rippleColor": "ripple-color",
    "strokeColor": "stroke-color",
    "strokeWidth": "stroke-width",
    "cornerRadius": "corner-radius",
}


def get_android_attr(element, attr_name, default=""):
    """Get an android: namespace attribute value."""
    return element.get(f"{{{NS_ANDROID}}}{attr_name}", default)


def get_app_attr(element, attr_name, default=""):
    """Get an app: namespace attribute value."""
    return element.get(f"{{{NS_APP}}}{attr_name}", default)


def resolve_layout_path(project_root, layout_ref, layout_files):
    """Resolve a layout reference (e.g. 'layout/activity_main.xml') to a file path."""
    # Try direct relative path from project root
    direct = os.path.join(project_root, layout_ref)
    if os.path.isfile(direct):
        return direct

    # Try under standard resource directories
    for prefix in ["app/src/main/res/", "src/main/res/"]:
        candidate = os.path.join(project_root, prefix, layout_ref)
        if os.path.isfile(candidate):
            return candidate

    # Try layout name lookup via find_layout_files cache
    layout_name = Path(layout_ref).stem
    if layout_name in layout_files:
        return layout_files[layout_name]

    return None


def resolve_menu_path(project_root, menu_ref, menu_files):
    """Resolve a menu reference (e.g. 'menu/home.xml' or '@menu/home') to a file path."""
    # Handle @menu/xxx format
    clean_ref = menu_ref.replace("@menu/", "")
    if clean_ref in menu_files:
        return menu_files[clean_ref]

    # Try direct relative path
    direct = os.path.join(project_root, menu_ref)
    if os.path.isfile(direct):
        return direct

    # Try under standard resource directories
    for prefix in ["app/src/main/res/", "src/main/res/"]:
        candidate = os.path.join(project_root, prefix, menu_ref)
        if os.path.isfile(candidate):
            return candidate

    # Try menu name lookup
    menu_name = Path(menu_ref).stem
    if menu_name in menu_files:
        return menu_files[menu_name]

    return None


class ViewXmlSynthesizer:
    """Converts Android layout XML into UIAutomator-compatible view.xml."""

    def __init__(self, project_root, package, layout_files, menu_files=None,
                 string_values=None, style_values=None,
                 resolve_strings=False, resolve_styles=False):
        self.project_root = project_root
        self.package = package
        self.layout_files = layout_files
        self.menu_files = menu_files or {}
        self.string_values = string_values or {}
        self.style_values = style_values or {}
        self.resolve_strings = resolve_strings
        self.resolve_styles = resolve_styles
        self.parsed_layouts = set()
        self.parsed_menus = set()

    def synthesize(self, layout_paths, menu_paths=None):
        """Synthesize view.xml from one or more layout files.

        Args:
            layout_paths: List of resolved file paths to layout XML files.
            menu_paths: Optional list of resolved file paths to menu XML files.

        Returns:
            ET.Element: Root <hierarchy> element in UIAutomator format.
        """
        hierarchy = ET.Element("hierarchy")
        hierarchy.set("rotation", "0")
        hierarchy.set("synthesized", "true")

        for path in layout_paths:
            layout_name = Path(path).stem
            if layout_name in self.parsed_layouts:
                continue
            self.parsed_layouts.add(layout_name)

            try:
                tree = ET.parse(path)
            except ET.ParseError as e:
                print(f"  [WARN] Failed to parse {path}: {e}", file=sys.stderr)
                continue

            root = tree.getroot()

            if root.tag == "merge":
                # Merge children directly into hierarchy
                for idx, child in enumerate(root):
                    if isinstance(child.tag, str):
                        node = self._convert_element(child, path, idx)
                        if node is not None:
                            hierarchy.append(node)
            else:
                node = self._convert_element(root, path, 0)
                if node is not None:
                    hierarchy.append(node)

        # Append explicitly requested menu files (not auto-followed from layout)
        if menu_paths:
            for path in menu_paths:
                menu_name = Path(path).stem
                if menu_name not in self.parsed_menus:
                    self._append_menu_from_file(hierarchy, path, menu_name)

        return hierarchy

    def _resolve_string(self, value):
        """Resolve @string/xxx reference to actual string value."""
        if not self.resolve_strings or not value:
            return value
        if value.startswith("@string/"):
            key = value[len("@string/"):]
            return self.string_values.get(key, value)
        return value

    def _apply_style_attrs(self, node, element):
        """Apply resolved style attributes to a node."""
        if not self.resolve_styles:
            return
        style_ref = element.get("style", "")
        if not style_ref or not style_ref.startswith("@style/"):
            return
        style_name = style_ref[len("@style/"):]
        resolved = resolve_style_chain(style_name, self.style_values)
        if resolved:
            # Store resolved style attributes in a single attribute for the converter
            # Format: "key1=val1;key2=val2"
            parts = []
            for k, v in resolved.items():
                # Resolve string refs within style values too
                v = self._resolve_string(v) if v.startswith("@string/") else v
                parts.append(f"{k}={v}")
            if parts:
                node.set("resolved-style", ";".join(parts))

    def _convert_element(self, element, source_path, index):
        """Convert a single XML element to a UIAutomator <node>."""
        if not isinstance(element.tag, str):
            return None

        tag = element.tag

        # Handle <include>
        if tag == "include":
            inc_ref = element.get("layout", "")
            inc_name = inc_ref.replace("@layout/", "")
            if inc_name in self.parsed_layouts:
                return None
            if inc_name in self.layout_files:
                self.parsed_layouts.add(inc_name)
                inc_path = self.layout_files[inc_name]
                try:
                    inc_tree = ET.parse(inc_path)
                except ET.ParseError:
                    return None
                inc_root = inc_tree.getroot()
                if inc_root.tag == "merge":
                    wrapper = ET.Element("node")
                    wrapper.set("class", "android.widget.FrameLayout")
                    wrapper.set("resource-id", "")
                    wrapper.set("text", "")
                    wrapper.set("content-desc", "")
                    wrapper.set("bounds", "")
                    self._set_default_attrs(wrapper, "FrameLayout")
                    wrapper.set("index", str(index))
                    for idx, child in enumerate(inc_root):
                        if isinstance(child.tag, str):
                            child_node = self._convert_element(child, inc_path, idx)
                            if child_node is not None:
                                wrapper.append(child_node)
                    return wrapper
                else:
                    return self._convert_element(inc_root, inc_path, index)
            return None

        # Handle <fragment> / FragmentContainerView
        frag_class = element.get(f"{{{NS_ANDROID}}}name") or element.get("class")

        # Resolve class name
        full_class = resolve_class_name(tag)
        cls_short = short_name(full_class)

        # For fragment tags, use the fragment class name
        if tag == "fragment" and frag_class:
            full_class = frag_class
            cls_short = short_name(frag_class)

        # Build <node> element
        node = ET.Element("node")
        node.set("index", str(index))
        node.set("class", full_class)

        # resource-id
        android_id = get_android_attr(element, "id")
        if android_id:
            id_val = android_id.replace("@+id/", "").replace("@id/", "")
            node.set("resource-id", f"{self.package}:id/{id_val}")
        else:
            node.set("resource-id", "")

        # text — with optional string resolution
        text_val = get_android_attr(element, "text")
        if text_val and text_val.startswith("@string/"):
            node.set("text-ref", text_val)
            node.set("text", self._resolve_string(text_val))
        else:
            node.set("text", text_val)

        # content-desc — with optional string resolution
        content_desc = get_android_attr(element, "contentDescription")
        if content_desc and content_desc.startswith("@string/"):
            node.set("content-desc", self._resolve_string(content_desc))
        else:
            node.set("content-desc", content_desc)

        # bounds — always empty for synthesized
        node.set("bounds", "")

        # Boolean attributes with Android defaults
        self._set_default_attrs(node, cls_short)

        # Override with explicit XML attributes
        for attr_name, node_attr in [
            ("clickable", "clickable"),
            ("longClickable", "long-clickable"),
            ("enabled", "enabled"),
            ("focusable", "focusable"),
            ("scrollbars", "scrollable"),
            ("checkable", "checkable"),
            ("checked", "checked"),
            ("selected", "selected"),
        ]:
            val = get_android_attr(element, attr_name)
            if val:
                node.set(node_attr, val.lower())

        # Special: scrollable from scrollbars or class type
        scrollbars = get_android_attr(element, "scrollbars")
        if scrollbars and scrollbars != "none":
            node.set("scrollable", "true")

        # Special: password detection from inputType
        input_type = get_android_attr(element, "inputType")
        node.set("password", "true" if input_type and "password" in input_type.lower() else "false")

        node.set("display-id", "0")

        # --- app: attribute passthrough ---
        for app_attr, node_attr_name in APP_PASSTHROUGH_ATTRS.items():
            val = get_app_attr(element, app_attr)
            if val:
                node.set(node_attr_name, val)

        # --- Style resolution ---
        style_ref = element.get("style", "")
        if style_ref:
            node.set("style-ref", style_ref)
        self._apply_style_attrs(node, element)

        # --- Auto-follow app:menu for menu-carrier components ---
        menu_ref = get_app_attr(element, "menu")
        if menu_ref and cls_short in MENU_CARRIER_CLASSES:
            menu_name = menu_ref.replace("@menu/", "")
            if menu_name not in self.parsed_menus and menu_name in self.menu_files:
                menu_path = self.menu_files[menu_name]
                self._append_menu_children(node, menu_path, menu_name)
        elif not menu_ref and cls_short in MENU_CARRIER_CLASSES:
            # No app:menu declared — menu is likely built dynamically in code
            # Mark this for the converter agent to handle
            node.set("menu-dynamic", "true")

        # Recurse children
        child_index = 0
        for child in element:
            if not isinstance(child.tag, str):
                continue
            # Skip <requestFocus/> and similar non-view tags
            if child.tag in ("requestFocus", "tag"):
                continue
            child_node = self._convert_element(child, source_path, child_index)
            if child_node is not None:
                node.append(child_node)
                child_index += 1

        return node

    def _append_menu_children(self, parent_node, menu_path, menu_name):
        """Parse a menu XML and append items as child nodes of parent_node."""
        self.parsed_menus.add(menu_name)
        try:
            tree = ET.parse(menu_path)
        except ET.ParseError as e:
            print(f"  [WARN] Failed to parse menu {menu_path}: {e}", file=sys.stderr)
            return

        root = tree.getroot()
        if root.tag != "menu":
            return

        self._convert_menu_children(parent_node, root, menu_name)

    def _append_menu_from_file(self, hierarchy, menu_path, menu_name):
        """Parse a standalone menu XML and append as a top-level wrapper node."""
        self.parsed_menus.add(menu_name)
        try:
            tree = ET.parse(menu_path)
        except ET.ParseError as e:
            print(f"  [WARN] Failed to parse menu {menu_path}: {e}", file=sys.stderr)
            return

        root = tree.getroot()
        if root.tag != "menu":
            return

        # Create a wrapper node for standalone menus
        wrapper = ET.Element("node")
        wrapper.set("class", "android.widget.Toolbar.Menu")
        wrapper.set("resource-id", "")
        wrapper.set("text", "")
        wrapper.set("content-desc", f"menu:{menu_name}")
        wrapper.set("bounds", "")
        wrapper.set("menu-source", f"menu/{menu_name}.xml")
        self._set_default_attrs(wrapper, "Menu")
        wrapper.set("index", "0")

        self._convert_menu_children(wrapper, root, menu_name)

        if len(wrapper) > 0:
            hierarchy.append(wrapper)

    def _convert_menu_children(self, parent_node, menu_element, menu_name):
        """Convert <item> children of a <menu> element into <node> children."""
        item_index = 0
        for child in menu_element:
            if not isinstance(child.tag, str):
                continue

            if child.tag == "item":
                item_node = self._convert_menu_item(child, menu_name, item_index)
                if item_node is not None:
                    parent_node.append(item_node)
                    item_index += 1
            elif child.tag == "group":
                # Process items inside <group>
                group_id = get_android_attr(child, "id", "")
                for group_child in child:
                    if isinstance(group_child.tag, str) and group_child.tag == "item":
                        item_node = self._convert_menu_item(group_child, menu_name, item_index)
                        if item_node is not None:
                            if group_id:
                                item_node.set("menu-group", group_id.replace("@+id/", "").replace("@id/", ""))
                            parent_node.append(item_node)
                            item_index += 1

    def _convert_menu_item(self, item_element, menu_name, index):
        """Convert a single <item> element from menu XML to a <node>."""
        node = ET.Element("node")
        node.set("index", str(index))
        node.set("class", "android.view.MenuItem")

        # resource-id from android:id
        android_id = get_android_attr(item_element, "id")
        if android_id:
            id_val = android_id.replace("@+id/", "").replace("@id/", "")
            node.set("resource-id", f"{self.package}:id/{id_val}")
        else:
            node.set("resource-id", "")

        # title → text (with string resolution)
        title = get_android_attr(item_element, "title")
        if title and title.startswith("@string/"):
            node.set("text-ref", title)
            node.set("text", self._resolve_string(title))
        else:
            node.set("text", title)

        # content-desc same as title
        node.set("content-desc", self._resolve_string(title) if title else "")

        # bounds — empty for synthesized
        node.set("bounds", "")

        # MenuItem is always clickable
        node.set("clickable", "true")
        node.set("long-clickable", "false")
        node.set("enabled", get_android_attr(item_element, "enabled", "true").lower())
        node.set("focusable", "false")
        node.set("focused", "false")
        node.set("scrollable", "false")
        node.set("checkable", get_android_attr(item_element, "checkable", "false").lower())
        node.set("checked", get_android_attr(item_element, "checked", "false").lower())
        node.set("selected", "false")
        node.set("password", "false")
        node.set("display-id", "0")

        # Menu-specific attributes
        icon = get_android_attr(item_element, "icon")
        if icon:
            node.set("icon", icon)

        # showAsAction from app: or custom: namespace
        show_as_action = get_app_attr(item_element, "showAsAction")
        if not show_as_action:
            # Try custom namespace (some projects use xmlns:custom)
            for attr_key, attr_val in item_element.attrib.items():
                if attr_key.endswith("}showAsAction"):
                    show_as_action = attr_val
                    break
        if show_as_action:
            node.set("showAsAction", show_as_action)

        # Visibility
        visible = get_android_attr(item_element, "visible", "true")
        node.set("visible", visible.lower())

        # Menu category
        menu_category = get_android_attr(item_element, "menuCategory")
        if menu_category:
            node.set("menu-category", menu_category)

        # Handle submenu (nested <menu>)
        for child in item_element:
            if isinstance(child.tag, str) and child.tag == "menu":
                self._convert_menu_children(node, child, menu_name)

        return node

    def _set_default_attrs(self, node, cls_short):
        """Set Android-default boolean attributes based on widget type."""
        node.set("clickable", "true" if cls_short in CLICKABLE_BY_DEFAULT else "false")
        node.set("long-clickable", "false")
        node.set("enabled", "true")
        node.set("focusable", "false")
        node.set("focused", "false")
        node.set("scrollable", "true" if cls_short in SCROLLABLE_BY_DEFAULT else "false")
        node.set("checkable", "true" if cls_short in CHECKABLE_BY_DEFAULT else "false")
        node.set("checked", "false")
        node.set("selected", "false")


def indent_xml(elem, level=0):
    """Add pretty-print indentation to XML tree."""
    indent = "\n" + "  " * level
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = indent + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = indent
        for child in elem:
            indent_xml(child, level + 1)
        if not child.tail or not child.tail.strip():
            child.tail = indent
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = indent


def main():
    parser = argparse.ArgumentParser(
        description="Synthesize UIAutomator-compatible view.xml from Android layout XML."
    )
    parser.add_argument("project_root", help="Android project root path")
    parser.add_argument("--layouts", required=True,
                        help="Comma-separated layout XML relative paths (from meta.json.layout_sources)")
    parser.add_argument("--menus", default="",
                        help="Comma-separated menu XML relative paths (from meta.json.menu_sources)")
    parser.add_argument("--resolve-strings", action="store_true",
                        help="Resolve @string/ references to actual text values")
    parser.add_argument("--resolve-styles", action="store_true",
                        help="Resolve @style/ references and inline style attributes")
    parser.add_argument("--output", required=True, help="Output view.xml path")
    parser.add_argument("--package", default="",
                        help="Android package name (for resource-id formatting)")

    args = parser.parse_args()

    # Find all layout files in project
    layout_files = find_layout_files(args.project_root)
    print(f"Found {len(layout_files)} layout files in project", file=sys.stderr)

    # Find all menu files in project
    menu_files = find_menu_files(args.project_root)
    print(f"Found {len(menu_files)} menu files in project", file=sys.stderr)

    # Auto-detect package if not provided
    package = args.package
    if not package:
        packages = detect_project_packages(args.project_root)
        if packages:
            package = sorted(packages)[0]
            print(f"Auto-detected package: {package}", file=sys.stderr)

    # Resolve string values if requested
    string_values = {}
    if args.resolve_strings:
        string_values = find_string_values(args.project_root)
        print(f"Loaded {len(string_values)} string values", file=sys.stderr)

    # Resolve style values if requested
    style_values = {}
    if args.resolve_styles:
        style_values = find_style_values(args.project_root)
        print(f"Loaded {len(style_values)} style definitions", file=sys.stderr)

    # Resolve layout paths
    layout_refs = [l.strip() for l in args.layouts.split(",") if l.strip()]
    resolved_layout_paths = []
    for ref in layout_refs:
        path = resolve_layout_path(args.project_root, ref, layout_files)
        if path:
            resolved_layout_paths.append(path)
            print(f"  Layout: {ref} -> {path}", file=sys.stderr)
        else:
            print(f"  [WARN] Cannot resolve layout: {ref}", file=sys.stderr)

    if not resolved_layout_paths:
        print("ERROR: No layout files could be resolved.", file=sys.stderr)
        sys.exit(1)

    # Resolve menu paths
    resolved_menu_paths = []
    if args.menus:
        menu_refs = [m.strip() for m in args.menus.split(",") if m.strip()]
        for ref in menu_refs:
            path = resolve_menu_path(args.project_root, ref, menu_files)
            if path:
                resolved_menu_paths.append(path)
                print(f"  Menu: {ref} -> {path}", file=sys.stderr)
            else:
                print(f"  [WARN] Cannot resolve menu: {ref}", file=sys.stderr)

    # Synthesize
    synthesizer = ViewXmlSynthesizer(
        args.project_root, package, layout_files, menu_files,
        string_values, style_values,
        args.resolve_strings, args.resolve_styles,
    )
    hierarchy = synthesizer.synthesize(resolved_layout_paths, resolved_menu_paths)

    # Write output
    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    indent_xml(hierarchy)
    tree = ET.ElementTree(hierarchy)
    tree.write(args.output, encoding="UTF-8", xml_declaration=True)

    # Count nodes
    node_count = len(list(hierarchy.iter("node")))
    menu_item_count = sum(1 for n in hierarchy.iter("node") if n.get("class") == "android.view.MenuItem")
    print(f"\nSynthesized view.xml: {node_count} nodes ({menu_item_count} menu items) -> {args.output}",
          file=sys.stderr)


if __name__ == "__main__":
    main()
