#!/usr/bin/env python
"""Fetch the Three.js documentation + source corpus (default tag: r186).

Why not threejs.org: the site is an SPA. `/docs/` returns *router* links
(`AnimationAction.html`) that 404 as files, and `/manual/` uses hash routing, so any
crawler collapses to the landing page. The real corpus lives in the git repo.

Corpus (all pinned to one tag so the index is reproducible):

  official_docs/
    docs/pages/*.html.md     829  markdown API reference (one page per class/namespace)
    manual/pages/*.html       60  manual chapters (HTML only upstream)
    docs/llms-full.txt             entire documentation as a single markdown file
    docs/llms.txt                  compact index
    docs/search.json               symbol index (handy for name lookups)

  official_source/
    src/**/*.js               ~700  core source, JSDoc on every public member
    examples/jsm/**/*.js      ~500  addons (OrbitControls, GLTFLoader, postprocessing, TSL)

The source trees matter more than the rendered docs for a coding agent: they carry the
exact signatures, default values and import paths of the *installed* version.

Usage:
    python tools/fetch_threejs_docs.py                 # everything, tag r186
    python tools/fetch_threejs_docs.py --only docs     # just docs/pages + manual
    python tools/fetch_threejs_docs.py --ref r187      # different tag
    python tools/fetch_threejs_docs.py --check         # report what is already on disk

Only api.github.com and raw.githubusercontent.com are contacted.
"""
from __future__ import annotations

import argparse
import json
import ssl
import sys
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from threejs import config  # noqa: E402

REPO = "mrdoob/three.js"
TREE_API = "https://api.github.com/repos/{repo}/git/trees/{ref}?recursive=1"
RAW = "https://raw.githubusercontent.com/{repo}/{ref}/{path}"
UA = {"User-Agent": "3gs-master/1.0 (+local three.js rag)"}
CTX = ssl.create_default_context()

# group -> (destination root, predicate on repo-relative path)
GROUPS = {
    "docs": (config.OFFICIAL_DOCS_DIR, lambda p: (
        (p.startswith("docs/pages/") and p.endswith(".html.md"))
        or (p.startswith("manual/pages/") and p.endswith(".html"))
    )),
    "meta": (config.OFFICIAL_DOCS_DIR, lambda p: p in {
        "docs/llms-full.txt", "docs/llms.txt", "docs/search.json",
    }),
    "source": (config.OFFICIAL_SOURCE_DIR, lambda p: (
        p.startswith("src/") and p.endswith(".js")
    )),
    "addons": (config.OFFICIAL_SOURCE_DIR, lambda p: (
        p.startswith("examples/jsm/") and p.endswith(".js")
    )),
}
MAX_FILE_BYTES = 4 * 1024 * 1024


def _get(url: str, timeout: float = 60.0) -> bytes:
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=timeout, context=CTX) as r:
        return r.read()


def _tree(ref: str) -> list[str]:
    raw = _get(TREE_API.format(repo=REPO, ref=ref))
    data = json.loads(raw.decode("utf-8"))
    if data.get("truncated"):
        print("[fetch] WARNING: GitHub tree response was truncated; corpus will be partial",
              file=sys.stderr)
    return [e["path"] for e in data.get("tree", []) if e.get("type") == "blob"]


def _plan(paths: list[str], only: set[str]) -> list[tuple[str, Path]]:
    out: list[tuple[str, Path]] = []
    for group, (dest, pred) in GROUPS.items():
        if only and group not in only:
            continue
        for p in paths:
            if pred(p):
                out.append((p, dest / p))
    return out


def _fetch_one(ref: str, item: tuple[str, Path], force: bool) -> tuple[str, str]:
    repo_path, dest = item
    if dest.exists() and not force and dest.stat().st_size > 0:
        return ("skip", repo_path)
    try:
        blob = _get(RAW.format(repo=REPO, ref=ref, path=repo_path))
    except urllib.error.HTTPError as e:
        return (f"http {e.code}", repo_path)
    except Exception as e:  # noqa: BLE001 - report and keep going
        return (f"err {e}", repo_path)
    if len(blob) > MAX_FILE_BYTES:
        return ("too-big", repo_path)
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(blob)
    return ("ok", repo_path)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--ref", default="r186", help="git tag/branch to pin (default r186)")
    ap.add_argument("--only", default="", help="comma list of: docs,meta,source,addons")
    ap.add_argument("--workers", type=int, default=8)
    ap.add_argument("--force", action="store_true", help="re-download existing files")
    ap.add_argument("--check", action="store_true", help="report disk state and exit")
    a = ap.parse_args()

    only = {x.strip() for x in a.only.split(",") if x.strip()}
    unknown = only - set(GROUPS)
    if unknown:
        print(f"[fetch] unknown --only values: {sorted(unknown)}", file=sys.stderr)
        return 2

    if a.check:
        for group, (dest, _pred) in GROUPS.items():
            n = sum(1 for f in dest.rglob("*") if f.is_file()) if dest.exists() else 0
            print(f"{group:8s} {dest}  files={n}")
        return 0

    t0 = time.time()
    print(f"[fetch] {REPO}@{a.ref}: reading tree ...", file=sys.stderr)
    paths = _tree(a.ref)
    plan = _plan(paths, only)
    if not plan:
        print("[fetch] nothing matched - wrong tag or --only?", file=sys.stderr)
        return 1
    print(f"[fetch] {len(plan)} files to fetch ({', '.join(sorted(only)) or 'all groups'})",
          file=sys.stderr)

    stats: dict[str, int] = {}
    failures: list[str] = []
    with ThreadPoolExecutor(max_workers=max(1, a.workers)) as ex:
        futs = {ex.submit(_fetch_one, a.ref, it, a.force): it for it in plan}
        done = 0
        for f in as_completed(futs):
            status, repo_path = f.result()
            stats[status] = stats.get(status, 0) + 1
            if status.startswith(("http", "err")):
                failures.append(f"{status} {repo_path}")
            done += 1
            if done % 250 == 0:
                print(f"[fetch] {done}/{len(plan)} ...", file=sys.stderr)

    print(f"[fetch] done in {time.time() - t0:.1f}s: "
          + ", ".join(f"{k}={v}" for k, v in sorted(stats.items())))
    for f in failures[:20]:
        print(f"[fetch] FAILED {f}", file=sys.stderr)
    if len(failures) > 20:
        print(f"[fetch] ... and {len(failures) - 20} more failures", file=sys.stderr)
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
