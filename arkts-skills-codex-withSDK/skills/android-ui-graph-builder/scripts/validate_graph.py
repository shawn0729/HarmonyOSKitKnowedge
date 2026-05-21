#!/usr/bin/env python3
"""
validate_graph.py — Cross-validate all four JSON outputs and report/fix ID inconsistencies.

Usage:
  python3 validate_graph.py <output_dir>

Reads Screen.json, Component.json, Navigation_Edge.json, Containment_Edge.json from <output_dir>.
Performs six categories of checks and outputs a detailed report.
If --fix is passed, auto-fixes what it can and rewrites the files.
"""

import json
import sys
import os
from collections import Counter


def load_json(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)


def save_json(filepath, data):
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def validate(output_dir, fix=False):
    screen_path = os.path.join(output_dir, "Screen.json")
    comp_path = os.path.join(output_dir, "Component.json")
    nav_path = os.path.join(output_dir, "Navigation_Edge.json")
    cont_path = os.path.join(output_dir, "Containment_Edge.json")

    screens = load_json(screen_path) or []
    components = load_json(comp_path) or []
    nav_edges = load_json(nav_path) or []
    cont_edges = load_json(cont_path) or []

    errors = []
    warnings = []
    fixes = []

    # ── Build ID sets ──
    screen_ids = set()
    comp_ids = set()

    # Check 1: Screen ID uniqueness
    screen_id_counts = Counter(s.get("id", "") for s in screens)
    for sid, count in screen_id_counts.items():
        if count > 1:
            errors.append(f"[DUPLICATE_SCREEN_ID] Screen ID '{sid}' appears {count} times")
        screen_ids.add(sid)

    # Check 2: Component ID uniqueness
    comp_id_counts = Counter(c.get("id", "") for c in components)
    for cid, count in comp_id_counts.items():
        if count > 1:
            errors.append(f"[DUPLICATE_COMP_ID] Component ID '{cid}' appears {count} times")
        comp_ids.add(cid)

    all_node_ids = screen_ids | comp_ids

    # Check 3: Navigation Edge references
    for i, edge in enumerate(nav_edges):
        from_id = edge.get("from", "")
        to_id = edge.get("to", "")
        src_comp = edge.get("source_component", "unknown")

        if from_id not in screen_ids:
            errors.append(f"[NAV_EDGE_{i}] 'from' references non-existent Screen: '{from_id}'")
        if to_id not in screen_ids:
            errors.append(f"[NAV_EDGE_{i}] 'to' references non-existent Screen: '{to_id}'")
        if src_comp != "unknown" and src_comp not in comp_ids:
            # Try fuzzy match
            candidates = [c for c in comp_ids if _id_similarity(src_comp, c) > 0.7]
            if candidates and fix:
                best = max(candidates, key=lambda c: _id_similarity(src_comp, c))
                fixes.append(f"[NAV_EDGE_{i}] Fixed source_component '{src_comp}' → '{best}'")
                edge["source_component"] = best
            else:
                errors.append(
                    f"[NAV_EDGE_{i}] 'source_component' references non-existent Component: '{src_comp}'"
                    + (f" (candidates: {candidates[:3]})" if candidates else "")
                )

        # Check required fields
        for field in ("trigger", "mechanism", "direction", "extras", "transition_anim", "flags", "condition"):
            if field not in edge:
                warnings.append(f"[NAV_EDGE_{i}] Missing required field: '{field}'")
                if fix:
                    if field == "extras":
                        edge[field] = {}
                    elif field == "condition":
                        edge[field] = "none"
                    else:
                        edge[field] = "unknown"
                    fixes.append(f"[NAV_EDGE_{i}] Added default for missing field '{field}'")

    # Check 4: Containment Edge references
    for i, edge in enumerate(cont_edges):
        parent_id = edge.get("parent", "")
        child_id = edge.get("child", "")

        if parent_id not in all_node_ids:
            # Try fuzzy match
            candidates = [n for n in all_node_ids if _id_similarity(parent_id, n) > 0.7]
            if candidates and fix:
                best = max(candidates, key=lambda n: _id_similarity(parent_id, n))
                fixes.append(f"[CONT_EDGE_{i}] Fixed parent '{parent_id}' → '{best}'")
                edge["parent"] = best
            else:
                errors.append(
                    f"[CONT_EDGE_{i}] 'parent' references non-existent node: '{parent_id}'"
                    + (f" (candidates: {candidates[:3]})" if candidates else "")
                )

        if child_id not in comp_ids:
            candidates = [c for c in comp_ids if _id_similarity(child_id, c) > 0.7]
            if candidates and fix:
                best = max(candidates, key=lambda c: _id_similarity(child_id, c))
                fixes.append(f"[CONT_EDGE_{i}] Fixed child '{child_id}' → '{best}'")
                edge["child"] = best
            else:
                errors.append(
                    f"[CONT_EDGE_{i}] 'child' references non-existent Component: '{child_id}'"
                    + (f" (candidates: {candidates[:3]})" if candidates else "")
                )

        # Check required fields
        for field in ("order", "source", "include_layout"):
            if field not in edge:
                warnings.append(f"[CONT_EDGE_{i}] Missing required field: '{field}'")
                if fix:
                    if field == "order":
                        edge[field] = 0
                    elif field == "source":
                        edge[field] = "direct"
                    elif field == "include_layout":
                        edge[field] = "none"
                    fixes.append(f"[CONT_EDGE_{i}] Added default for missing field '{field}'")

    # Check 5: Every Screen should have at least one Containment edge (as parent)
    screens_with_children = set()
    for edge in cont_edges:
        parent = edge.get("parent", "")
        if parent in screen_ids:
            screens_with_children.add(parent)
    orphan_screens = screen_ids - screens_with_children
    for sid in orphan_screens:
        warnings.append(f"[ORPHAN_SCREEN] Screen '{sid}' has no containment edges (no root layout connected)")

    # Check 6: Every Component should be reachable (appear as child in some containment edge)
    children_referenced = set()
    for edge in cont_edges:
        children_referenced.add(edge.get("child", ""))
    orphan_components = comp_ids - children_referenced
    for cid in orphan_components:
        # Root components connected directly from screens are OK
        warnings.append(f"[ORPHAN_COMPONENT] Component '{cid}' never appears as a child in any containment edge")

    # Check 7: Screen required fields
    screen_required = ["id", "type", "name", "package", "layout_ref", "source_file", "language",
                       "theme", "parent_activity", "menu_ref", "has_options_menu", "has_toolbar",
                       "orientation_config", "config_changes", "lifecycle_callbacks", "metadata"]
    for i, screen in enumerate(screens):
        for field in screen_required:
            if field not in screen:
                warnings.append(f"[SCREEN_{i}] Missing required field: '{field}'")
                if fix:
                    if field in ("has_options_menu", "has_toolbar"):
                        screen[field] = False
                    elif field == "lifecycle_callbacks":
                        screen[field] = []
                    elif field == "metadata":
                        screen[field] = {
                            "launch_mode": "unknown", "exported": False,
                            "intent_filters": [], "soft_input_mode": "unknown",
                            "window_flags": "unknown", "task_affinity": "unknown"
                        }
                    else:
                        screen[field] = "unknown"
                    fixes.append(f"[SCREEN_{i}] Added default for missing field '{field}'")

    # Check 8: Component required fields
    comp_required = ["id", "android_id", "class", "class_short", "is_viewgroup", "is_custom_view",
                     "source_layout", "depth", "layout_attrs", "style_attrs", "behavior_attrs",
                     "accessibility_attrs", "resource_refs", "custom_attrs"]
    for i, comp in enumerate(components):
        for field in comp_required:
            if field not in comp:
                warnings.append(f"[COMP_{i}:{comp.get('id','?')}] Missing required field: '{field}'")
                if fix:
                    if field in ("is_viewgroup", "is_custom_view"):
                        comp[field] = False
                    elif field == "depth":
                        comp[field] = 0
                    elif field in ("layout_attrs", "style_attrs", "behavior_attrs",
                                   "accessibility_attrs", "custom_attrs"):
                        comp[field] = {}
                    elif field == "resource_refs":
                        comp[field] = []
                    elif field == "android_id":
                        comp[field] = "none"
                    else:
                        comp[field] = "unknown"
                    fixes.append(f"[COMP_{i}] Added default for missing field '{field}'")

    # ── Report ──
    print("=" * 70)
    print("  Android UI Graph — Validation Report")
    print("=" * 70)
    print(f"\n  Screens:        {len(screens)}")
    print(f"  Components:     {len(components)}")
    print(f"  Nav Edges:      {len(nav_edges)}")
    print(f"  Cont Edges:     {len(cont_edges)}")
    print(f"\n  Errors:         {len(errors)}")
    print(f"  Warnings:       {len(warnings)}")
    if fix:
        print(f"  Auto-fixes:     {len(fixes)}")

    if errors:
        print(f"\n{'─' * 70}")
        print("  ERRORS (must fix — ID references broken)")
        print(f"{'─' * 70}")
        for e in errors:
            print(f"  ✗ {e}")

    if warnings:
        print(f"\n{'─' * 70}")
        print("  WARNINGS (may need attention)")
        print(f"{'─' * 70}")
        for w in warnings:
            print(f"  ⚠ {w}")

    if fixes:
        print(f"\n{'─' * 70}")
        print("  AUTO-FIXES APPLIED")
        print(f"{'─' * 70}")
        for f_ in fixes:
            print(f"  ✓ {f_}")

    if not errors and not warnings:
        print(f"\n  ✓ All checks passed. Graph is consistent.")

    print(f"\n{'=' * 70}\n")

    # ── Save if fix mode ──
    if fix and (fixes or errors):
        save_json(screen_path, screens)
        save_json(comp_path, components)
        save_json(nav_path, nav_edges)
        save_json(cont_path, cont_edges)
        print(f"  Fixed files saved to {output_dir}")

    return len(errors), len(warnings)


def _id_similarity(a, b):
    """Simple token-overlap similarity for fuzzy ID matching."""
    if not a or not b:
        return 0.0
    tokens_a = set(a.replace(":", "_").replace("#", "_").replace(".", "_").split("_"))
    tokens_b = set(b.replace(":", "_").replace("#", "_").replace(".", "_").split("_"))
    tokens_a.discard("")
    tokens_b.discard("")
    if not tokens_a or not tokens_b:
        return 0.0
    intersection = tokens_a & tokens_b
    union = tokens_a | tokens_b
    return len(intersection) / len(union)


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 validate_graph.py <output_dir> [--fix]")
        sys.exit(1)

    output_dir = sys.argv[1]
    fix = "--fix" in sys.argv

    errors, warnings = validate(output_dir, fix=fix)
    sys.exit(1 if errors > 0 else 0)


if __name__ == "__main__":
    main()
