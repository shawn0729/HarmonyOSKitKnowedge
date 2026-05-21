#!/usr/bin/env python3
"""
merge_components.py — Merge script-parsed raw components with LLM-enriched attributes.

The deterministic parser (parse_layouts.py) produces reliable:
  - Component IDs (no counter errors)
  - Containment edges (structurally correct parent-child)
  - Basic attributes extracted from XML

The LLM may produce additional semantic attributes (e.g., from code analysis).
This script merges them, always preferring the parser's IDs and structure.

Usage:
  python3 merge_components.py <raw_dir> <llm_dir> <final_output_dir>

Where:
  <raw_dir>          — directory containing components_raw.json, containment_raw.json
  <llm_dir>          — directory containing LLM-generated Component.json, Containment_Edge.json
                       (may also have Navigation_Edge.json, Screen.json to copy)
  <final_output_dir> — where to write the final four JSON files
"""

import json
import sys
import os
from collections import defaultdict


def load_json(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)


def save_json(filepath, data):
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def deep_merge(base, overlay):
    """Merge overlay into base. Base wins for ID/structural fields; overlay fills unknowns."""
    result = dict(base)
    for key, val in overlay.items():
        if key not in result:
            result[key] = val
        elif isinstance(val, dict) and isinstance(result[key], dict):
            result[key] = deep_merge(result[key], val)
        elif result[key] == "unknown" and val != "unknown":
            result[key] = val
        elif isinstance(result[key], list) and isinstance(val, list):
            # For resource_refs, merge by attr name
            if key == "resource_refs":
                existing_attrs = {r.get("attr") for r in result[key]}
                for item in val:
                    if item.get("attr") not in existing_attrs:
                        result[key].append(item)
            # For other lists, prefer longer
            elif len(val) > len(result[key]):
                result[key] = val
    return result


def build_id_map(components):
    """Build a map from various ID forms to component dict."""
    id_map = {}
    for comp in components:
        cid = comp.get("id", "")
        id_map[cid] = comp
        # Also index by android_id for cross-matching
        aid = comp.get("android_id", "none")
        if aid != "none":
            id_map[f"_aid:{aid}"] = comp
    return id_map


def match_llm_to_raw(llm_comp, raw_id_map):
    """Try to find the matching raw component for an LLM-generated component."""
    # Exact ID match
    lid = llm_comp.get("id", "")
    if lid in raw_id_map:
        return raw_id_map[lid]

    # Match by android_id
    laid = llm_comp.get("android_id", "none")
    if laid != "none":
        key = f"_aid:{laid}"
        if key in raw_id_map:
            return raw_id_map[key]

    # Match by source_layout + class_short + approximate position
    for rid, raw in raw_id_map.items():
        if not rid.startswith("comp:"):
            continue
        if (raw.get("source_layout") == llm_comp.get("source_layout") and
            raw.get("class_short") == llm_comp.get("class_short") and
            raw.get("depth") == llm_comp.get("depth")):
            return raw

    return None


def main():
    if len(sys.argv) < 4:
        print("Usage: python3 merge_components.py <raw_dir> <llm_dir> <final_output_dir>")
        sys.exit(1)

    raw_dir = sys.argv[1]
    llm_dir = sys.argv[2]
    final_dir = sys.argv[3]
    os.makedirs(final_dir, exist_ok=True)

    # Load raw (from parser)
    raw_components = load_json(os.path.join(raw_dir, "components_raw.json")) or []
    raw_containment = load_json(os.path.join(raw_dir, "containment_raw.json")) or []

    # Load LLM outputs
    llm_components = load_json(os.path.join(llm_dir, "Component.json")) or []
    llm_containment = load_json(os.path.join(llm_dir, "Containment_Edge.json")) or []
    llm_screens = load_json(os.path.join(llm_dir, "Screen.json")) or []
    llm_nav = load_json(os.path.join(llm_dir, "Navigation_Edge.json")) or []

    raw_id_map = build_id_map(raw_components)

    # Strategy: raw components are the structural truth.
    # Enrich them with any extra attributes from LLM.
    if llm_components:
        enriched_count = 0
        for llm_comp in llm_components:
            raw_match = match_llm_to_raw(llm_comp, raw_id_map)
            if raw_match:
                # Merge LLM extras into raw
                idx = raw_components.index(raw_match)
                raw_components[idx] = deep_merge(raw_match, llm_comp)
                enriched_count += 1
        print(f"Enriched {enriched_count}/{len(llm_components)} LLM components with raw data",
              file=sys.stderr)

    # Fix Navigation edge source_component IDs to match raw component IDs
    raw_comp_ids = {c["id"] for c in raw_components}
    raw_by_android_id = {}
    for c in raw_components:
        aid = c.get("android_id", "none")
        if aid != "none":
            # Extract just the id part: @+id/btn_login → btn_login
            clean_aid = aid.replace("@+id/", "").replace("@id/", "")
            raw_by_android_id[clean_aid] = c["id"]

    nav_fixes = 0
    for edge in llm_nav:
        src = edge.get("source_component", "unknown")
        if src != "unknown" and src not in raw_comp_ids:
            # Try to find by android_id suffix
            parts = src.split(":")
            if len(parts) >= 3:
                id_part = parts[-1]
                if id_part in raw_by_android_id:
                    edge["source_component"] = raw_by_android_id[id_part]
                    nav_fixes += 1

    if nav_fixes:
        print(f"Fixed {nav_fixes} navigation edge source_component IDs", file=sys.stderr)

    # Save final outputs
    save_json(os.path.join(final_dir, "Screen.json"), llm_screens)
    save_json(os.path.join(final_dir, "Component.json"), raw_components)
    save_json(os.path.join(final_dir, "Containment_Edge.json"), raw_containment)
    save_json(os.path.join(final_dir, "Navigation_Edge.json"), llm_nav)

    print(f"\nFinal output:", file=sys.stderr)
    print(f"  Screens:     {len(llm_screens)}", file=sys.stderr)
    print(f"  Components:  {len(raw_components)} (parser-authoritative)", file=sys.stderr)
    print(f"  Containment: {len(raw_containment)} (parser-authoritative)", file=sys.stderr)
    print(f"  Navigation:  {len(llm_nav)} (LLM-generated, IDs reconciled)", file=sys.stderr)


if __name__ == "__main__":
    main()
