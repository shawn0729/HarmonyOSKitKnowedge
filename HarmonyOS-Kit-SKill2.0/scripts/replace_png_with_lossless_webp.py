#!/usr/bin/env python3
from __future__ import annotations

import argparse
import os
import re
import shutil
from pathlib import Path

from PIL import Image


MARKDOWN_PNG_RE = re.compile(r"(!\[[^\]]*\]\()([^) \t\n]+\.png)((?:[ \t]+[^)]*)?\))", re.IGNORECASE)
HTML_PNG_RE = re.compile(r"(<img\b[^>]*?\bsrc=[\"'])([^\"']+\.png)([\"'][^>]*>)", re.IGNORECASE)


def convert_lossless_webp(png_path: Path, webp_path: Path) -> None:
    with Image.open(png_path) as image:
        webp_path.parent.mkdir(parents=True, exist_ok=True)
        image.save(webp_path, format="WEBP", lossless=True, method=6)


def rewrite_png_refs(sources_root: Path) -> int:
    replacements = 0
    for md_path in sorted(sources_root.rglob("*.md")):
        text = md_path.read_text(encoding="utf-8")

        def replace_markdown(match: re.Match[str]) -> str:
            nonlocal replacements
            target = match.group(2)
            target_path = (md_path.parent / target).resolve()
            webp_path = target_path.with_suffix(".webp")
            if not webp_path.exists():
                return match.group(0)
            replacements += 1
            return f"{match.group(1)}{target[:-4]}.webp{match.group(3)}"

        def replace_html(match: re.Match[str]) -> str:
            nonlocal replacements
            target = match.group(2)
            target_path = (md_path.parent / target).resolve()
            webp_path = target_path.with_suffix(".webp")
            if not webp_path.exists():
                return match.group(0)
            replacements += 1
            return f"{match.group(1)}{target[:-4]}.webp{match.group(3)}"

        new_text = MARKDOWN_PNG_RE.sub(replace_markdown, text)
        new_text = HTML_PNG_RE.sub(replace_html, new_text)
        if new_text != text:
            md_path.write_text(new_text, encoding="utf-8")
    return replacements


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--skill-root", type=Path, default=Path("skills/harmonyos-development"))
    parser.add_argument("--backup-dir", type=Path, default=Path("original-images"))
    parser.add_argument("--keep-assets-png", action="store_true")
    args = parser.parse_args()

    skill_root = args.skill_root.resolve()
    images_dir = skill_root / "sources" / "_assets" / "images"
    sources_root = skill_root / "sources"
    backup_dir = args.backup_dir.resolve()

    png_paths = sorted(images_dir.glob("*.png"))
    backup_dir.mkdir(parents=True, exist_ok=True)

    converted = 0
    backed_up = 0
    removed = 0
    original_bytes = 0
    webp_bytes = 0
    failures: list[tuple[Path, str]] = []

    for png_path in png_paths:
        backup_path = backup_dir / png_path.name
        webp_path = png_path.with_suffix(".webp")
        try:
            original_bytes += png_path.stat().st_size
            if not backup_path.exists():
                shutil.copy2(png_path, backup_path)
                backed_up += 1
            elif backup_path.stat().st_size != png_path.stat().st_size:
                raise RuntimeError(f"backup exists with different size: {backup_path}")

            convert_lossless_webp(png_path, webp_path)
            converted += 1
            webp_bytes += webp_path.stat().st_size

            if not args.keep_assets_png:
                png_path.unlink()
                removed += 1
        except Exception as exc:  # noqa: BLE001
            failures.append((png_path, str(exc)))

    replacements = rewrite_png_refs(sources_root)

    report = skill_root / "sources" / "_assets" / "png-lossless-webp-report.md"
    report_lines = [
        "# PNG Lossless WebP Report",
        "",
        f"- PNG files found: {len(png_paths)}",
        f"- PNG files backed up: {backed_up}",
        f"- PNG files converted: {converted}",
        f"- PNG files removed from assets: {removed}",
        f"- Markdown/HTML references updated: {replacements}",
        f"- Original PNG bytes processed: {original_bytes}",
        f"- Generated WebP bytes: {webp_bytes}",
        f"- Backup directory: `{os.path.relpath(backup_dir, skill_root.parent.parent)}`",
        f"- Failures: {len(failures)}",
        "",
    ]
    if failures:
        report_lines.extend(["## Failures", ""])
        for path, error in failures:
            report_lines.append(f"- `{path}`: {error}")
    report.write_text("\n".join(report_lines) + "\n", encoding="utf-8")

    print(f"pngs={len(png_paths)} backed_up={backed_up} converted={converted} removed={removed} refs={replacements} failures={len(failures)}")
    print(f"original_mb={original_bytes/1024/1024:.2f} webp_mb={webp_bytes/1024/1024:.2f}")
    print(f"backup={backup_dir}")
    print(f"report={report}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
