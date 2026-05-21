#!/usr/bin/env python3
from __future__ import annotations

import argparse
import os
import re
import shutil
from pathlib import Path

from PIL import Image


MARKDOWN_GIF_RE = re.compile(r"(!\[[^\]]*\]\()([^) \t\n]+\.gif)((?:[ \t]+[^)]*)?\))", re.IGNORECASE)
HTML_GIF_RE = re.compile(r"(<img\b[^>]*?\bsrc=[\"'])([^\"']+\.gif)([\"'][^>]*>)", re.IGNORECASE)


def convert_first_frame(gif_path: Path, webp_path: Path, quality: int) -> None:
    with Image.open(gif_path) as image:
        image.seek(0)
        frame = image.convert("RGBA")
        webp_path.parent.mkdir(parents=True, exist_ok=True)
        frame.save(webp_path, format="WEBP", quality=quality, method=6)


def rewrite_markdown_refs(sources_root: Path) -> int:
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

        new_text = MARKDOWN_GIF_RE.sub(replace_markdown, text)
        new_text = HTML_GIF_RE.sub(replace_html, new_text)
        if new_text != text:
            md_path.write_text(new_text, encoding="utf-8")
    return replacements


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--skill-root", type=Path, default=Path("skills/harmonyos-development"))
    parser.add_argument("--backup-dir", type=Path, default=Path("original-images"))
    parser.add_argument("--quality", type=int, default=80)
    parser.add_argument("--keep-assets-gif", action="store_true")
    args = parser.parse_args()

    skill_root = args.skill_root.resolve()
    images_dir = skill_root / "sources" / "_assets" / "images"
    sources_root = skill_root / "sources"
    backup_dir = args.backup_dir.resolve()

    gif_paths = sorted(images_dir.glob("*.gif"))
    backup_dir.mkdir(parents=True, exist_ok=True)

    converted = 0
    backed_up = 0
    removed = 0
    original_bytes = 0
    webp_bytes = 0
    failures: list[tuple[Path, str]] = []

    for gif_path in gif_paths:
        backup_path = backup_dir / gif_path.name
        webp_path = gif_path.with_suffix(".webp")
        try:
            original_bytes += gif_path.stat().st_size
            if not backup_path.exists():
                shutil.copy2(gif_path, backup_path)
                backed_up += 1
            elif backup_path.stat().st_size != gif_path.stat().st_size:
                raise RuntimeError(f"backup exists with different size: {backup_path}")

            convert_first_frame(gif_path, webp_path, args.quality)
            converted += 1
            webp_bytes += webp_path.stat().st_size

            if not args.keep_assets_gif:
                gif_path.unlink()
                removed += 1
        except Exception as exc:  # noqa: BLE001
            failures.append((gif_path, str(exc)))

    replacements = rewrite_markdown_refs(sources_root)

    report = skill_root / "sources" / "_assets" / "gif-first-frame-webp-report.md"
    report_lines = [
        "# GIF First Frame WebP Report",
        "",
        f"- GIF files found: {len(gif_paths)}",
        f"- GIF files backed up: {backed_up}",
        f"- GIF files converted: {converted}",
        f"- GIF files removed from assets: {removed}",
        f"- Markdown/HTML references updated: {replacements}",
        f"- Original GIF bytes processed: {original_bytes}",
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

    print(f"gifs={len(gif_paths)} backed_up={backed_up} converted={converted} removed={removed} refs={replacements} failures={len(failures)}")
    print(f"original_mb={original_bytes/1024/1024:.2f} webp_mb={webp_bytes/1024/1024:.2f}")
    print(f"backup={backup_dir}")
    print(f"report={report}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
