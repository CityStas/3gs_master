#!/usr/bin/env python
"""Build / refresh the Three.js RAG index (data/sqlite/lexical.db).

Incremental: a file is re-chunked only when its mtime+size changed, and only when its
SHA-256 actually differs. Stale revisions of a changed file are deleted by the indexer.

    python tools/index.py                       # everything, incremental
    python tools/index.py --force               # full rebuild (required after a version bump)
    python tools/index.py --only official_docs  # one source
    python tools/index.py --project C:/path/to/three-project
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from threejs.rag.indexer import Indexer, SOURCE_BY_DIR  # noqa: E402


def main() -> int:
    p = argparse.ArgumentParser(description="Index the Three.js corpus.")
    p.add_argument("--project", type=Path, help="also index a Three.js project tree as source=project")
    p.add_argument("--only", default="", help="comma list of: " + ", ".join(SOURCE_BY_DIR) + ",project")
    p.add_argument("--force", action="store_true", help="re-chunk everything, ignoring mtime/sha")
    a = p.parse_args()

    only = {x.strip() for x in a.only.split(",") if x.strip()} or None
    if only:
        known = set(SOURCE_BY_DIR) | {"project"}
        bad = only - known
        if bad:
            print(f"unknown --only: {sorted(bad)}", file=sys.stderr)
            return 2

    idx = Indexer()
    reports = idx.run(a.project, a.force, only)
    total = 0
    print()
    for r in reports:
        print(" ", r.line())
        total += r.chunks
    st = idx.store.stats()
    print(f"\nindexed this run: {total} chunks")
    print(f"index now       : {st['chunks']} chunks, {st['with_vectors']} with vectors, "
          f"{st['files']} files tracked")
    print(f"db              : {st['db']}")
    print(f"by source       : {st['by_source']}")
    print(f"by file_type    : {st['by_type']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
