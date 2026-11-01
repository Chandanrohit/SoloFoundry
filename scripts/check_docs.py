#!/usr/bin/env python3
"""Check repository-local Markdown links and core editorial metadata."""

from __future__ import annotations

import json
import re
import sys
from datetime import date
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
REFERENCE_RE = re.compile(r"^\s*\[[^\]]+\]:\s*<?([^\s>]+)>?", re.MULTILINE)
REQUIRED_MATURITY_DIRS = ("10-industry-playbooks", "11-reference-architectures", "12-stack-combinations")
PLACEHOLDER_MARKERS = ("{",)


def markdown_files() -> list[Path]:
    ignored = {".git", ".docs-src", ".venv", "docs-src", "site", "node_modules", "__pycache__"}
    return [
        path
        for path in ROOT.rglob("*.md")
        if not any(part in ignored for part in path.relative_to(ROOT).parts)
        and ".github" not in path.relative_to(ROOT).parts
    ]


def target_for(source: Path, link_target: str) -> Path | None:
    target = link_target.strip().split()[0].strip("<>")
    if not target or target.upper() in {"URL", "PATH", "TODO"} or any(marker in target for marker in PLACEHOLDER_MARKERS):
        return None
    parsed = urlsplit(target)
    if parsed.scheme or parsed.netloc or target.startswith("#"):
        return None
    path_text = unquote(parsed.path)
    if not path_text:
        return None
    candidate = (source.parent / path_text).resolve()
    if candidate.is_dir():
        for index_name in ("README.md", "index.md"):
            index = candidate / index_name
            if index.is_file():
                return index
    return candidate


def check_links(files: list[Path]) -> list[str]:
    errors: list[str] = []
    for source in files:
        content = source.read_text(encoding="utf-8")
        links = [match.group(1) for match in LINK_RE.finditer(content)]
        links.extend(match.group(1) for match in REFERENCE_RE.finditer(content))
        for link in links:
            target = target_for(source, link)
            if target is None:
                continue
            if not target.exists():
                relative_source = source.relative_to(ROOT).as_posix()
                errors.append(f"{relative_source}: missing local target {link}")
    return errors


def check_maturity(files: list[Path]) -> list[str]:
    errors: list[str] = []
    for directory in REQUIRED_MATURITY_DIRS:
        for page in (ROOT / directory).rglob("*.md"):
            content = page.read_text(encoding="utf-8")
            first_lines = "\n".join(content.splitlines()[:8])
            if not re.search(r"\*\*Maturity:\*\*", first_lines):
                errors.append(f"{page.relative_to(ROOT).as_posix()}: add a Maturity label in the first eight lines")
    return errors


def check_source_register() -> list[str]:
    errors: list[str] = []
    catalog_path = ROOT / "resources" / "SOURCE_REGISTER.json"
    try:
        catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        return [f"resources/SOURCE_REGISTER.json: {error}"]

    if not isinstance(catalog, dict) or catalog.get("schema_version") != 1 or not isinstance(catalog.get("sources"), list):
        return ["resources/SOURCE_REGISTER.json: expected schema_version 1 and a sources array"]

    seen: set[str] = set()
    register_markdown = (ROOT / "resources" / "SOURCE_REGISTER.md").read_text(encoding="utf-8")
    for item in catalog["sources"]:
        if not isinstance(item, dict):
            errors.append("resources/SOURCE_REGISTER.json: every source must be an object")
            continue
        key = item.get("key", "")
        if not key or key in seen:
            errors.append(f"resources/SOURCE_REGISTER.json: missing or duplicate source key {key!r}")
        seen.add(key)
        if f"| {key} |" not in register_markdown:
            errors.append(f"source {key or '<unknown>'}: add an entry to resources/SOURCE_REGISTER.md")
        for field in ("title", "url", "scope", "last_checked", "recheck_when"):
            if not item.get(field):
                errors.append(f"source {key or '<unknown>'}: missing {field}")
        if item.get("url", "").startswith("https://") is False:
            errors.append(f"source {key or '<unknown>'}: URL must use HTTPS")
        try:
            date.fromisoformat(item.get("last_checked", ""))
        except (TypeError, ValueError):
            errors.append(f"source {key or '<unknown>'}: last_checked must be YYYY-MM-DD")
    return errors


def main() -> int:
    files = markdown_files()
    errors = check_links(files) + check_maturity(files) + check_source_register()
    if errors:
        print("Documentation checks failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"Documentation checks passed for {len(files)} Markdown files and the source register.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
