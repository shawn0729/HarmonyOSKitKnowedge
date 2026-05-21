#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import html
import mimetypes
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path


IMAGE_RE = re.compile(
    r"!\[([^\]]*)\]\((https?://[^\s)]+)([ \t]+(?:\"[^\"]*\"|'[^']*'|\([^)]*\)))?\)"
)


def suffix_for(url: str, content_type: str | None) -> str:
    path = urllib.parse.urlparse(url).path
    suffix = Path(path).suffix.lower()
    if suffix in {".png", ".jpg", ".jpeg", ".gif", ".webp", ".bmp", ".svg"}:
        return suffix
    if content_type:
        guessed = mimetypes.guess_extension(content_type.split(";")[0].strip())
        if guessed:
            return ".jpg" if guessed == ".jpe" else guessed
    return ".bin"


def download(url: str, dest_without_suffix: Path, retries: int = 2) -> Path:
    request_url = html.unescape(url)
    last_error: Exception | None = None
    for attempt in range(retries + 1):
        try:
            req = urllib.request.Request(
                request_url,
                headers={
                    "User-Agent": "Mozilla/5.0 offline-markdown-images",
                    "Accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
                },
            )
            with urllib.request.urlopen(req, timeout=45) as resp:
                content_type = resp.headers.get("Content-Type")
                data = resp.read()
            suffix = suffix_for(request_url, content_type)
            dest = dest_without_suffix.with_suffix(suffix)
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes(data)
            return dest
        except Exception as exc:  # noqa: BLE001
            last_error = exc
            if attempt < retries:
                time.sleep(1 + attempt)
    raise RuntimeError(f"{last_error}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", type=Path)
    parser.add_argument("--assets-dir", type=Path, default=None)
    parser.add_argument("--report", type=Path, default=None)
    args = parser.parse_args()

    root = args.root.resolve()
    assets_dir = (args.assets_dir or root / "sources" / "_assets" / "images").resolve()
    report = args.report or root / "sources" / "_assets" / "offline-image-report.md"

    md_files = sorted(root.rglob("*.md"))
    url_to_path: dict[str, Path] = {}
    failures: list[tuple[Path, str, str]] = []
    replacements = 0

    for md_file in md_files:
        text = md_file.read_text(encoding="utf-8")
        changed = False

        def replace(match: re.Match[str]) -> str:
            nonlocal changed, replacements
            alt, url, title = match.group(1), match.group(2), match.group(3) or ""
            digest = hashlib.sha256(html.unescape(url).encode("utf-8")).hexdigest()[:24]
            dest_base = assets_dir / digest
            try:
                local_path = url_to_path.get(url)
                if local_path is None:
                    existing = sorted(dest_base.parent.glob(dest_base.name + ".*"))
                    local_path = existing[0] if existing else download(url, dest_base)
                    url_to_path[url] = local_path
                rel = Path(os.path.relpath(local_path.resolve(), md_file.parent.resolve())).as_posix()
            except Exception as exc:  # noqa: BLE001
                failures.append((md_file.relative_to(root), url, str(exc)))
                return match.group(0)

            changed = True
            replacements += 1
            return f"![{alt}]({rel}{title})"

        new_text = IMAGE_RE.sub(replace, text)
        if changed and new_text != text:
            md_file.write_text(new_text, encoding="utf-8")

    report.parent.mkdir(parents=True, exist_ok=True)
    report_lines = [
        "# Offline Image Report",
        "",
        f"- Markdown files scanned: {len(md_files)}",
        f"- Image references replaced: {replacements}",
        f"- Unique images downloaded/reused: {len(url_to_path)}",
        f"- Failures: {len(failures)}",
        "",
    ]
    if failures:
        report_lines.append("## Failures")
        report_lines.append("")
        for path, url, error in failures:
            report_lines.append(f"- `{path}`")
            report_lines.append(f"  - URL: {url}")
            report_lines.append(f"  - Error: {error}")
    report.write_text("\n".join(report_lines) + "\n", encoding="utf-8")

    print(f"scanned={len(md_files)} replaced={replacements} unique={len(url_to_path)} failures={len(failures)}")
    print(f"report={report}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
