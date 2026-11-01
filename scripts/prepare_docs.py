#!/usr/bin/env python3
"""Mirror repository content into MkDocs' required child docs directory."""

from __future__ import annotations

import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS_DIR = ROOT / ".docs-src"
IGNORED = {
    ".git",
    ".github",
    ".docs-src",
    ".venv",
    "node_modules",
    "scripts",
    "site",
    "tests",
    "__pycache__",
    "mkdocs.yml",
}


def main() -> None:
    if DOCS_DIR.exists():
        shutil.rmtree(DOCS_DIR)
    shutil.copytree(
        ROOT,
        DOCS_DIR,
        ignore=lambda _directory, names: {name for name in names if name in IGNORED},
    )
    print(f"Prepared documentation sources in {DOCS_DIR.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
