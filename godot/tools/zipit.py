#!/usr/bin/env python
"""zipit.py - portable zip builder (Windows has no `zip`, GNU tar cannot write zip).

Usage:
    python tools/zipit.py OUT.zip PATH [PATH ...]
        [--exclude DIRNAME] [--exclude-glob PATTERN] [--root BASE] [--store]

- PATH may be a file or a directory (recursed).
- Archive member names are relative to --root (default: cwd).
- --store  skip deflate (fast, big) - use for already-compressed payloads.
- Prints a summary and returns non-zero if any member failed to read.
"""
from __future__ import annotations

import argparse
import fnmatch
import os
import sys
import time
import zipfile
from pathlib import Path

DEFAULT_SKIP_DIRS = {"__pycache__", ".pytest_cache", ".mypy_cache", ".ruff_cache"}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("out")
    ap.add_argument("paths", nargs="+")
    ap.add_argument("--exclude", action="append", default=[])
    ap.add_argument("--exclude-glob", action="append", default=[])
    ap.add_argument("--root", default=".")
    ap.add_argument("--store", action="store_true")
    ap.add_argument("--quiet", action="store_true")
    a = ap.parse_args()

    root = Path(a.root).resolve()
    out = Path(a.out).resolve()
    out.parent.mkdir(parents=True, exist_ok=True)
    skip_dirs = DEFAULT_SKIP_DIRS | set(a.exclude)
    globs = list(a.exclude_glob)
    compression = zipfile.ZIP_STORED if a.store else zipfile.ZIP_DEFLATED

    targets: list[Path] = []
    for raw in a.paths:
        p = Path(raw)
        if not p.is_absolute():
            p = (Path.cwd() / p)
        if not p.exists():
            print(f"[zipit] MISSING: {raw}", file=sys.stderr)
            continue
        targets.append(p)

    t0 = time.time()
    n_files = 0
    n_bytes = 0
    failed: list[str] = []

    with zipfile.ZipFile(out, "w", compression=compression, allowZip64=True) as z:
        for t in targets:
            if t.is_file():
                arc = t.resolve().relative_to(root).as_posix() if str(t.resolve()).startswith(str(root)) else t.name
                try:
                    z.write(t, arc)
                    n_files += 1
                    n_bytes += t.stat().st_size
                except OSError as e:
                    failed.append(f"{t}: {e}")
                continue
            for dirpath, dirnames, filenames in os.walk(t):
                dirnames[:] = [d for d in dirnames if d not in skip_dirs]
                for fn in filenames:
                    fp = Path(dirpath) / fn
                    rel = fp.resolve().relative_to(root).as_posix()
                    if any(fnmatch.fnmatch(rel, g) or fnmatch.fnmatch(fn, g) for g in globs):
                        continue
                    try:
                        z.write(fp, rel)
                        n_files += 1
                        n_bytes += fp.stat().st_size
                    except OSError as e:
                        failed.append(f"{fp}: {e}")
                    if not a.quiet and n_files % 2000 == 0:
                        print(f"[zipit] {n_files} files, {n_bytes / 1048576:.0f} MB ...", file=sys.stderr)

    size = out.stat().st_size
    print(f"[zipit] {out.name}: {n_files} files, {n_bytes / 1048576:.1f} MB raw "
          f"-> {size / 1048576:.1f} MB zip, {time.time() - t0:.1f}s")
    for f in failed:
        print(f"[zipit] FAILED {f}", file=sys.stderr)
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
