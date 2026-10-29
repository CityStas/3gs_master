#!/usr/bin/env python
"""Build / refresh the Unity RAG index (unity/data/sqlite/lexical.db).

Incremental: a file is re-chunked only when its mtime+size changed, and only when its
SHA-256 actually differs. Stale revisions of a changed file are deleted by the indexer.

    python unity/tools/index.py                        # everything, incremental
    python unity/tools/index.py --force                # full rebuild (needed after a version bump)
    python unity/tools/index.py --vectors              # only fill in missing vectors
    python unity/tools/index.py --only official_docs   # one corpus
    python unity/tools/index.py --project C:/path/to/MyUnityGame
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "unity"))

from unimaster import config  # noqa: E402
from unimaster.rag.indexer import SOURCE_BY_DIR, Indexer  # noqa: E402


def main() -> int:
    p = argparse.ArgumentParser(description="Index the Unity corpus.")
    p.add_argument("--project", type=Path,
                   help="also index a Unity project tree as source=project")
    p.add_argument("--only", default="",
                   help="comma list of: " + ", ".join(SOURCE_BY_DIR) + ",project")
    p.add_argument("--force", action="store_true",
                   help="re-chunk everything, ignoring mtime/sha")
    p.add_argument("--vectors", action="store_true",
                   help="only embed chunks that have no vector (repair after an "
                        "embedding outage); no re-chunking")
    a = p.parse_args()

    only = {x.strip() for x in a.only.split(",") if x.strip()} or None
    if only:
        known = set(SOURCE_BY_DIR) | {"project"}
        bad = only - known
        if bad:
            print(f"unknown --only: {sorted(bad)}", file=sys.stderr)
            return 2

    if a.project is None:
        raw = config.pointer_text()
        if raw:
            candidate = Path(raw)
            if candidate.is_dir() and (candidate / "Assets").is_dir():
                a.project = candidate

    idx = Indexer()
    if a.vectors:
        # Repair mode: the corpus is already chunked, only the missing vectors are filled.
        # This is the cheap fix for "index built while :8081 was down".
        reports = [idx.repair_vectors()]
    else:
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
    print(f"unity version   : {config.UNITY_VERSION}")
    print(f"by source       : {st['by_source']}")
    print(f"by file_type    : {st['by_type']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
