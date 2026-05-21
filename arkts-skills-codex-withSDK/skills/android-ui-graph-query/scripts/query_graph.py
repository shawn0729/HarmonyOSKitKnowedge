#!/usr/bin/env python3
"""
query_graph.py — Android UI Graph query engine.

Loads the four JSON files and supports multiple query modes designed for
Android→HarmonyOS migration context extraction.

Usage:
  python3 query_graph.py <graph_dir> <command> [args...]

Commands:

  screen <screen_id_or_name>
      Full context for one screen: attributes, component tree, navigation in/out.

  component <component_id_or_android_id>
      Full context for one component: attributes, children, parent chain, siblings.

  screen_list
      List all screens with type and layout_ref.

  component_list <screen_id_or_name>
      List all components belonging to a screen (flat list with depth).

  tree <screen_id_or_name>
      Visual indented tree of the screen's component hierarchy.

  navigation <screen_id_or_name>
      All navigation edges from/to a screen.

  migration_context <screen_id_or_name>
      THE MAIN COMMAND for migration: produces a complete, self-contained context
      document with everything needed to rewrite this screen in HarmonyOS ArkUI.

  migration_component <component_id_or_android_id>
      Component-level migration context: full attributes, children subtree,
      parent context, sibling context.

  search <keyword>
      Search across all nodes by class name, android_id, or layout file.

All output is JSON printed to stdout. Human-readable summaries go to stderr.
"""

import json
import sys
import os
from collections import defaultdict


class GraphStore:
    """In-memory graph store with indexed lookups."""

    def __init__(self, graph_dir):
        self.screens = self._load(os.path.join(graph_dir, "Screen.json"))
        self.components = self._load(os.path.join(graph_dir, "Component.json"))
        self.nav_edges = self._load(os.path.join(graph_dir, "Navigation_Edge.json"))
        self.cont_edges = self._load(os.path.join(graph_dir, "Containment_Edge.json"))
        self._build_indexes()

    def _load(self, path):
        if not os.path.exists(path):
            print(f"[WARN] File not found: {path}", file=sys.stderr)
            return []
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    def _build_indexes(self):
        # Screen indexes
        self.screen_by_id = {s["id"]: s for s in self.screens}
        self.screen_by_name = {}
        for s in self.screens:
            self.screen_by_name[s["name"]] = s
            self.screen_by_name[s["name"].lower()] = s

        # Component indexes
        self.comp_by_id = {c["id"]: c for c in self.components}
        self.comp_by_android_id = {}
        for c in self.components:
            aid = c.get("android_id", "none")
            if aid != "none":
                clean = aid.replace("@+id/", "").replace("@id/", "")
                self.comp_by_android_id[clean] = c
                self.comp_by_android_id[aid] = c

        # Containment indexes
        self.children_of = defaultdict(list)   # parent_id → [(child_id, order, source, include_layout)]
        self.parent_of = {}                     # child_id → (parent_id, order, source)
        for e in self.cont_edges:
            self.children_of[e["parent"]].append({
                "child": e["child"],
                "order": e.get("order", 0),
                "source": e.get("source", "direct"),
                "include_layout": e.get("include_layout", "none")
            })
            self.parent_of[e["child"]] = {
                "parent": e["parent"],
                "order": e.get("order", 0),
                "source": e.get("source", "direct")
            }
        # Sort children by order
        for pid in self.children_of:
            self.children_of[pid].sort(key=lambda x: x["order"])

        # Navigation indexes
        self.nav_from = defaultdict(list)   # screen_id → [edge]
        self.nav_to = defaultdict(list)     # screen_id → [edge]
        for e in self.nav_edges:
            self.nav_from[e["from"]].append(e)
            self.nav_to[e["to"]].append(e)

        # Components by source_layout
        self.comp_by_layout = defaultdict(list)
        for c in self.components:
            self.comp_by_layout[c.get("source_layout", "")].append(c)

    def resolve_screen(self, identifier):
        """Resolve a screen by ID, name, or partial match."""
        if identifier in self.screen_by_id:
            return self.screen_by_id[identifier]
        if identifier in self.screen_by_name:
            return self.screen_by_name[identifier]
        low = identifier.lower()
        if low in self.screen_by_name:
            return self.screen_by_name[low]
        # Partial match
        for sid, s in self.screen_by_id.items():
            if identifier in sid or identifier in s.get("name", ""):
                return s
        return None

    def resolve_component(self, identifier):
        """Resolve a component by ID, android_id, or partial match."""
        if identifier in self.comp_by_id:
            return self.comp_by_id[identifier]
        if identifier in self.comp_by_android_id:
            return self.comp_by_android_id[identifier]
        clean = identifier.replace("@+id/", "").replace("@id/", "")
        if clean in self.comp_by_android_id:
            return self.comp_by_android_id[clean]
        # Partial match
        for cid, c in self.comp_by_id.items():
            if identifier in cid:
                return c
        return None

    def get_subtree(self, node_id, max_depth=50):
        """Get the full component subtree under a node (BFS)."""
        result = []
        queue = [(node_id, 0)]
        visited = set()
        while queue:
            nid, depth = queue.pop(0)
            if nid in visited or depth > max_depth:
                continue
            visited.add(nid)
            children = self.children_of.get(nid, [])
            for child_info in children:
                cid = child_info["child"]
                comp = self.comp_by_id.get(cid)
                if comp:
                    result.append({
                        "component": comp,
                        "parent_id": nid,
                        "order": child_info["order"],
                        "source": child_info["source"],
                        "include_layout": child_info["include_layout"],
                        "relative_depth": depth
                    })
                    queue.append((cid, depth + 1))
        return result

    def get_parent_chain(self, comp_id):
        """Walk up from a component to the screen root."""
        chain = []
        current = comp_id
        visited = set()
        while current in self.parent_of and current not in visited:
            visited.add(current)
            info = self.parent_of[current]
            parent_id = info["parent"]
            parent_node = self.comp_by_id.get(parent_id) or self.screen_by_id.get(parent_id)
            chain.append({
                "id": parent_id,
                "type": "screen" if parent_id in self.screen_by_id else "component",
                "node": parent_node,
                "child_order": info["order"],
                "containment_source": info["source"]
            })
            current = parent_id
        return chain

    def get_siblings(self, comp_id):
        """Get sibling components (same parent, excluding self)."""
        if comp_id not in self.parent_of:
            return []
        parent_id = self.parent_of[comp_id]["parent"]
        siblings = []
        for child_info in self.children_of.get(parent_id, []):
            if child_info["child"] != comp_id:
                comp = self.comp_by_id.get(child_info["child"])
                if comp:
                    siblings.append({
                        "component": comp,
                        "order": child_info["order"]
                    })
        return siblings

    def get_screen_root_components(self, screen_id):
        """Get the direct root component(s) of a screen."""
        return self.children_of.get(screen_id, [])


# ─── Command implementations ───

def cmd_screen(store, identifier):
    """Full screen context."""
    screen = store.resolve_screen(identifier)
    if not screen:
        return {"error": f"Screen not found: {identifier}"}

    sid = screen["id"]
    roots = store.get_screen_root_components(sid)
    root_comps = []
    for r in roots:
        comp = store.comp_by_id.get(r["child"])
        if comp:
            root_comps.append(comp)

    # Count total components
    subtree = store.get_subtree(sid)

    return {
        "screen": screen,
        "root_components": root_comps,
        "total_components": len(subtree),
        "navigation_outgoing": store.nav_from.get(sid, []),
        "navigation_incoming": store.nav_to.get(sid, []),
    }


def cmd_component(store, identifier):
    """Full component context."""
    comp = store.resolve_component(identifier)
    if not comp:
        return {"error": f"Component not found: {identifier}"}

    cid = comp["id"]
    children_info = store.children_of.get(cid, [])
    direct_children = []
    for ch in children_info:
        child_comp = store.comp_by_id.get(ch["child"])
        if child_comp:
            direct_children.append({
                "component": child_comp,
                "order": ch["order"],
                "source": ch["source"]
            })

    parent_chain = store.get_parent_chain(cid)
    siblings = store.get_siblings(cid)

    return {
        "component": comp,
        "direct_children": direct_children,
        "total_descendants": len(store.get_subtree(cid)),
        "parent_chain": parent_chain,
        "siblings": siblings,
    }


def cmd_screen_list(store):
    """List all screens."""
    result = []
    for s in store.screens:
        result.append({
            "id": s["id"],
            "name": s["name"],
            "type": s["type"],
            "layout_ref": s.get("layout_ref", "unknown"),
            "nav_out_count": len(store.nav_from.get(s["id"], [])),
            "nav_in_count": len(store.nav_to.get(s["id"], [])),
            "component_count": len(store.get_subtree(s["id"])),
        })
    return result


def cmd_component_list(store, screen_identifier):
    """Flat list of all components in a screen."""
    screen = store.resolve_screen(screen_identifier)
    if not screen:
        return {"error": f"Screen not found: {screen_identifier}"}

    subtree = store.get_subtree(screen["id"])
    result = []
    for item in subtree:
        c = item["component"]
        result.append({
            "id": c["id"],
            "android_id": c.get("android_id", "none"),
            "class_short": c["class_short"],
            "depth": c.get("depth", 0),
            "is_viewgroup": c.get("is_viewgroup", False),
            "parent_id": item["parent_id"],
        })
    return result


def cmd_tree(store, screen_identifier):
    """Indented tree representation."""
    screen = store.resolve_screen(screen_identifier)
    if not screen:
        return {"error": f"Screen not found: {screen_identifier}"}

    lines = [f"📱 {screen['name']} ({screen['type']})"]

    def _walk(node_id, indent):
        children = store.children_of.get(node_id, [])
        for i, ch in enumerate(children):
            comp = store.comp_by_id.get(ch["child"])
            if not comp:
                continue
            is_last = (i == len(children) - 1)
            prefix = "└── " if is_last else "├── "
            aid = comp.get("android_id", "none")
            aid_str = f" #{aid.replace('@+id/', '').replace('@id/', '')}" if aid != "none" else ""
            src = f" [{ch['source']}]" if ch["source"] != "direct" else ""
            lines.append(f"{indent}{prefix}{comp['class_short']}{aid_str}{src}")
            next_indent = indent + ("    " if is_last else "│   ")
            _walk(ch["child"], next_indent)

    _walk(screen["id"], "  ")
    return {"tree": "\n".join(lines)}


def cmd_navigation(store, screen_identifier):
    """Navigation edges for a screen."""
    screen = store.resolve_screen(screen_identifier)
    if not screen:
        return {"error": f"Screen not found: {screen_identifier}"}

    sid = screen["id"]
    return {
        "screen": {"id": sid, "name": screen["name"]},
        "outgoing": store.nav_from.get(sid, []),
        "incoming": store.nav_to.get(sid, []),
    }


def cmd_migration_context(store, screen_identifier):
    """
    THE MAIN COMMAND: Complete migration context for one screen.
    Produces everything needed to rewrite this screen in HarmonyOS ArkUI.
    """
    screen = store.resolve_screen(screen_identifier)
    if not screen:
        return {"error": f"Screen not found: {screen_identifier}"}

    sid = screen["id"]

    # 1. Screen metadata
    screen_meta = dict(screen)

    # 2. Full component tree with all attributes
    subtree = store.get_subtree(sid)
    component_tree = []
    for item in subtree:
        comp = dict(item["component"])
        comp["_tree_info"] = {
            "parent_id": item["parent_id"],
            "order": item["order"],
            "source": item["source"],
            "include_layout": item["include_layout"],
            "relative_depth": item["relative_depth"],
        }
        component_tree.append(comp)

    # 3. Navigation context (what screens can this screen jump to / be jumped from)
    outgoing = []
    for edge in store.nav_from.get(sid, []):
        target_screen = store.screen_by_id.get(edge["to"])
        outgoing.append({
            "edge": edge,
            "target_screen_summary": {
                "id": edge["to"],
                "name": target_screen["name"] if target_screen else "unknown",
                "type": target_screen["type"] if target_screen else "unknown",
            } if target_screen else None
        })

    incoming = []
    for edge in store.nav_to.get(sid, []):
        source_screen = store.screen_by_id.get(edge["from"])
        incoming.append({
            "edge": edge,
            "source_screen_summary": {
                "id": edge["from"],
                "name": source_screen["name"] if source_screen else "unknown",
                "type": source_screen["type"] if source_screen else "unknown",
            } if source_screen else None
        })

    # 4. Resource inventory (all unique resources referenced by this screen's components)
    resource_inventory = {}
    for item in subtree:
        for ref in item["component"].get("resource_refs", []):
            key = ref.get("ref", "")
            if key and key != "unknown":
                if key not in resource_inventory:
                    resource_inventory[key] = {
                        "ref": key,
                        "type": ref.get("type", "unknown"),
                        "used_by": []
                    }
                resource_inventory[key]["used_by"].append({
                    "component_id": item["component"]["id"],
                    "attribute": ref.get("attr", "")
                })

    # 5. Layout structure summary (for understanding the layout approach)
    root_comps = store.get_screen_root_components(sid)
    layout_summary = {
        "root_container": None,
        "max_depth": 0,
        "total_components": len(component_tree),
        "viewgroup_count": 0,
        "leaf_count": 0,
        "component_type_counts": {},
        "has_include": False,
        "has_fragment_tag": False,
        "has_dynamic_content": False,
        "constraint_layout_used": False,
        "recycler_view_used": False,
    }

    for item in subtree:
        comp = item["component"]
        cs = comp["class_short"]
        layout_summary["component_type_counts"][cs] = layout_summary["component_type_counts"].get(cs, 0) + 1
        if comp.get("is_viewgroup"):
            layout_summary["viewgroup_count"] += 1
        else:
            layout_summary["leaf_count"] += 1
        d = comp.get("depth", 0)
        if d > layout_summary["max_depth"]:
            layout_summary["max_depth"] = d
        if "ConstraintLayout" in cs:
            layout_summary["constraint_layout_used"] = True
        if "RecyclerView" in cs:
            layout_summary["recycler_view_used"] = True
        if item["source"] == "include":
            layout_summary["has_include"] = True
        if item["source"] == "fragment_tag":
            layout_summary["has_fragment_tag"] = True
        if item["source"] == "dynamic":
            layout_summary["has_dynamic_content"] = True

    if root_comps:
        rc = store.comp_by_id.get(root_comps[0]["child"])
        if rc:
            layout_summary["root_container"] = {
                "class": rc["class"],
                "class_short": rc["class_short"]
            }

    # 6. Host activity context (for Fragment/Dialog)
    host_activity = None
    if screen.get("parent_activity") and screen["parent_activity"] != "none":
        ha = store.screen_by_id.get(screen["parent_activity"])
        if ha:
            host_activity = {
                "id": ha["id"],
                "name": ha["name"],
                "type": ha["type"],
                "layout_ref": ha.get("layout_ref", "unknown"),
            }

    # 7. Child screens (Fragments/Dialogs hosted by this Activity)
    child_screens = []
    for s in store.screens:
        if s.get("parent_activity") == sid:
            child_screens.append({
                "id": s["id"],
                "name": s["name"],
                "type": s["type"],
            })

    return {
        "screen": screen_meta,
        "layout_summary": layout_summary,
        "component_tree": component_tree,
        "resource_inventory": list(resource_inventory.values()),
        "navigation": {
            "outgoing": outgoing,
            "incoming": incoming,
        },
        "host_activity": host_activity,
        "child_screens": child_screens,
    }


def cmd_migration_component(store, identifier):
    """
    Component-level migration context.
    Full attributes + children subtree + parent context + sibling context.
    """
    comp = store.resolve_component(identifier)
    if not comp:
        return {"error": f"Component not found: {identifier}"}

    cid = comp["id"]

    # 1. Full component data
    component_data = dict(comp)

    # 2. Children subtree with all attributes
    subtree = store.get_subtree(cid)
    children_tree = []
    for item in subtree:
        child = dict(item["component"])
        child["_tree_info"] = {
            "parent_id": item["parent_id"],
            "order": item["order"],
            "source": item["source"],
            "relative_depth": item["relative_depth"],
        }
        children_tree.append(child)

    # 3. Parent chain (up to screen)
    parent_chain = store.get_parent_chain(cid)
    parent_context = []
    for p in parent_chain:
        node = p["node"]
        if node:
            parent_context.append({
                "id": p["id"],
                "type": p["type"],
                "class_short": node.get("class_short", node.get("name", "?")),
                "layout_attrs": node.get("layout_attrs", {}),
                "child_order": p["child_order"],
            })

    # 4. Siblings (same parent) with their attributes
    siblings = store.get_siblings(cid)
    sibling_context = []
    for s in siblings:
        sc = s["component"]
        sibling_context.append({
            "id": sc["id"],
            "class_short": sc["class_short"],
            "android_id": sc.get("android_id", "none"),
            "order": s["order"],
            "layout_attrs": sc.get("layout_attrs", {}),
            "style_attrs": sc.get("style_attrs", {}),
        })

    # 5. Resource inventory for this component and descendants
    resource_inventory = {}
    all_comps = [comp] + [item["component"] for item in subtree]
    for c in all_comps:
        for ref in c.get("resource_refs", []):
            key = ref.get("ref", "")
            if key and key != "unknown":
                if key not in resource_inventory:
                    resource_inventory[key] = {
                        "ref": key,
                        "type": ref.get("type", "unknown"),
                        "used_by": []
                    }
                resource_inventory[key]["used_by"].append(c["id"])

    # 6. Navigation edges triggered by this component
    triggered_navigations = []
    for edge in store.nav_edges:
        if edge.get("source_component") == cid:
            triggered_navigations.append(edge)

    return {
        "component": component_data,
        "children_tree": children_tree,
        "parent_context": parent_context,
        "sibling_context": sibling_context,
        "resource_inventory": list(resource_inventory.values()),
        "triggered_navigations": triggered_navigations,
    }


def cmd_search(store, keyword):
    """Search across all nodes."""
    keyword_lower = keyword.lower()
    results = {"screens": [], "components": []}

    for s in store.screens:
        if (keyword_lower in s.get("name", "").lower() or
            keyword_lower in s.get("id", "").lower() or
            keyword_lower in s.get("package", "").lower() or
            keyword_lower in s.get("layout_ref", "").lower()):
            results["screens"].append({
                "id": s["id"], "name": s["name"], "type": s["type"]
            })

    for c in store.components:
        if (keyword_lower in c.get("id", "").lower() or
            keyword_lower in c.get("android_id", "").lower() or
            keyword_lower in c.get("class", "").lower() or
            keyword_lower in c.get("class_short", "").lower() or
            keyword_lower in c.get("source_layout", "").lower()):
            results["components"].append({
                "id": c["id"],
                "android_id": c.get("android_id", "none"),
                "class_short": c["class_short"],
                "source_layout": c.get("source_layout", ""),
            })

    return results


def main():
    if len(sys.argv) < 3:
        print(__doc__, file=sys.stderr)
        sys.exit(1)

    graph_dir = sys.argv[1]
    command = sys.argv[2]
    args = sys.argv[3:]

    store = GraphStore(graph_dir)

    commands = {
        "screen": lambda: cmd_screen(store, args[0]) if args else {"error": "Missing screen identifier"},
        "component": lambda: cmd_component(store, args[0]) if args else {"error": "Missing component identifier"},
        "screen_list": lambda: cmd_screen_list(store),
        "component_list": lambda: cmd_component_list(store, args[0]) if args else {"error": "Missing screen identifier"},
        "tree": lambda: cmd_tree(store, args[0]) if args else {"error": "Missing screen identifier"},
        "navigation": lambda: cmd_navigation(store, args[0]) if args else {"error": "Missing screen identifier"},
        "migration_context": lambda: cmd_migration_context(store, args[0]) if args else {"error": "Missing screen identifier"},
        "migration_component": lambda: cmd_migration_component(store, args[0]) if args else {"error": "Missing component identifier"},
        "search": lambda: cmd_search(store, args[0]) if args else {"error": "Missing keyword"},
    }

    if command not in commands:
        print(f"Unknown command: {command}", file=sys.stderr)
        print(f"Available: {', '.join(commands.keys())}", file=sys.stderr)
        sys.exit(1)

    result = commands[command]()

    # Print tree to stderr for human readability
    if command == "tree" and "tree" in result:
        print(result["tree"], file=sys.stderr)

    # JSON to stdout
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
