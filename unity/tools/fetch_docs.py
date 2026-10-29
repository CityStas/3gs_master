#!/usr/bin/env python
"""Fetch the Unity documentation corpus (pinned to one version).

Why the TOC and not a crawler: docs.unity3d.com ships a machine-readable table of
contents per section (`<section>/docdata/toc.json`), so the full page list is one
request instead of a crawl that has to guess links. Every page is then a plain
`<link>.html` download - no SPA, no hash routing.

Corpus (all pinned to `UNITY_DOC_VERSION`, default 6000.3):

  official_docs/
    Manual/*.html            ~2800  user manual chapters
    ScriptReference/*.html   ~4200  API reference, one page per class/namespace
    _toc/                    the raw toc.json files, so the index is reproducible

  packages_docs/                   (--only packages)
    <package>/{manual,api}/*.html  UPM package manuals + API (Input System,
                                   Addressables, AI Navigation, URP, Cinemachine, ...)

  official_source/                 (--with-source)
    Runtime/**/*.cs          UnityCsReference - the actual managed API source,
    Editor/**/*.cs           which is what a coding agent needs for exact signatures

The source tree matters more than the rendered pages for a coding agent: it carries the
real attributes, default values and overloads of the *installed* version.

Usage:
    python unity/tools/fetch_docs.py                     # Manual + ScriptReference
    python unity/tools/fetch_docs.py --with-source       # + UnityCsReference C#
    python unity/tools/fetch_docs.py --only packages     # UPM package docs only
    python unity/tools/fetch_docs.py --only manual       # one section
    python unity/tools/fetch_docs.py --limit 50          # smoke test
    python unity/tools/fetch_docs.py --check             # what is already on disk
    python unity/tools/fetch_docs.py --version 6000.0    # a different docs line

Only docs.unity3d.com, api.github.com and raw.githubusercontent.com are contacted.
"""
from __future__ import annotations

import argparse
import json
import re
import ssl
import sys
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]          # repo root
sys.path.insert(0, str(ROOT / "unity"))

from unimaster import config  # noqa: E402

UA = {"User-Agent": "3gs-master/1.0 (+local unity rag)"}
CTX = ssl.create_default_context()
MAX_FILE_BYTES = 4 * 1024 * 1024
SECTIONS = {"manual": "Manual", "scriptref": "ScriptReference"}

# ---------------------------------------------------------------------------
# UPM package docs.
#
# The Manual covers the engine core; everything shipped as a package (Input System,
# Addressables, AI Navigation, URP, Cinemachine, ...) documents itself separately under
# `docs.unity3d.com/Packages/<name>@<version>/`. A coding agent that only has the
# Manual will confidently write `Input.GetAxis` in a project whose manifest pins the
# new Input System - the single most common Unity API mistake. These are the packages
# a game project actually depends on, in rough order of how often they matter.
#
# Two things differ from the Manual/ScriptReference sections, both discovered by probing:
#
#   * package docs have **no `docdata/toc.json`** - the sidebar lives in `<section>/toc.html`
#     as plain `<a href="Page.html">` links;
#   * there is **no `@latest` alias** - the URL needs a concrete version.
#
# The version therefore comes from Unity's own npm-style registry
# (`https://packages.unity.com/<name>` -> `dist-tags.latest`), trimmed to `major.minor`,
# because that is the form the docs site actually serves (`@1.20`, not `@1.20.1`).
# The pinned value below is only a fallback for when the registry is unreachable.
# ---------------------------------------------------------------------------
PACKAGES: dict[str, str] = {
    "com.unity.inputsystem": "1.14",
    "com.unity.render-pipelines.universal": "17.0",
    "com.unity.addressables": "2.6",
    "com.unity.ai.navigation": "2.0",
    "com.unity.cinemachine": "3.1",
    "com.unity.textmeshpro": "3.0",
    "com.unity.timeline": "1.8",
    "com.unity.animation.rigging": "1.3",
    "com.unity.probuilder": "6.0",
    "com.unity.netcode.gameobjects": "2.0",
    "com.unity.test-framework": "1.4",
    "com.unity.burst": "1.8",
    "com.unity.collections": "2.5",
    "com.unity.entities": "1.3",
    "com.unity.2d.animation": "11.0",
    "com.unity.2d.tilemap.extras": "5.0",
    "com.unity.xr.interaction.toolkit": "3.0",
    "com.unity.recorder": "5.0",
    "com.unity.formats.fbx": "5.0",
    "com.unity.cloud.gltfast": "6.0",
    "com.unity.localization": "1.5",
}
PACKAGE_SECTIONS = ("manual", "api")
PACKAGES_REGISTRY = "https://packages.unity.com/{pkg}"
PACKAGES_BASE = "https://docs.unity3d.com/Packages"
RE_TOC_LINK = re.compile(r'href="([^"#?]+\.html)"')

# docs.unity3d.com throttles aggressively: a burst of 8 parallel workers got 2225 of
# 2827 Manual pages rejected with HTTP 429. So every request now backs off on 429/503
# instead of giving up, and the default concurrency stays low.
RETRY_CODES = {429, 500, 502, 503, 504}
RETRY_TRIES = 6
RETRY_BASE = 1.5
RETRY_CAP = 30.0

# Backing off *after* a 429 is the fallback; staying under the limit in the first place is
# cheaper. A small per-request delay per worker keeps the sustained rate below the
# threshold, which matters most for the ScriptReference section (~4200 pages) where a
# throttled crawl would otherwise take hours.
REQUEST_DELAY = 0.0  # seconds, set from --delay

CSREF_REPO = "Unity-Technologies/UnityCsReference"
CSREF_TREE = "https://api.github.com/repos/{repo}/git/trees/{ref}?recursive=1"
CSREF_RAW = "https://raw.githubusercontent.com/{repo}/{ref}/{path}"
# `Modules/` is not optional: it holds 3712 of the repo's 5774 C# files and is where the
# engine API an agent actually calls lives - Rigidbody, Transform, NavMeshAgent, Animator,
# SpriteRenderer, AudioSource. Taking only Runtime/ + Editor/ (2012 files) yields a corpus
# with no physics, no animation and no navigation, which is exactly what a first attempt
# did. `External/` (third-party) and `Tools/` are deliberately excluded.
CSREF_PREFIXES = ("Runtime/", "Editor/", "Modules/")
CSREF_SKIP = ("Runtime/GraphView/", "Modules/GraphView/")


def _get(url: str, timeout: float = 60.0) -> bytes:
    """One request, no retry. Used for toc.json, where a failure is fatal anyway."""
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=timeout, context=CTX) as r:
        return r.read()


def _get_retry(url: str, timeout: float = 60.0) -> bytes:
    """Same as `_get`, but waits out 429/5xx instead of dropping the page.

    Retry-After is honoured when the server sends it; otherwise the delay grows
    exponentially with a cap, so a throttling burst decays instead of escalating.
    """
    delay = RETRY_BASE
    last: Exception | None = None
    for attempt in range(RETRY_TRIES):
        try:
            return _get(url, timeout)
        except urllib.error.HTTPError as e:
            last = e
            if e.code not in RETRY_CODES:
                raise
            wait = delay
            ra = e.headers.get("Retry-After") if e.headers else None
            if ra:
                try:
                    wait = min(float(ra), RETRY_CAP)
                except ValueError:
                    pass
        except Exception as e:  # noqa: BLE001  (connection reset, timeout, ...)
            last = e
            wait = delay
        if attempt < RETRY_TRIES - 1:
            time.sleep(wait)
        delay = min(delay * 2, RETRY_CAP)
    raise last if last else RuntimeError("retry loop fell through")


def _toc(base: str, section: str) -> list[str]:
    raw = _get_retry(f"{base}/{section}/docdata/toc.json")
    data = json.loads(raw.decode("utf-8-sig"))
    out: list[str] = []

    def walk(node):
        if not node:
            return
        children = node.get("children")
        if children:
            for c in children:
                walk(c)
            return
        link = node.get("link")
        if link and link != "null":
            out.append(link)

    walk(data)
    return out


def _save_toc(base: str, section: str, toc_dir: Path) -> None:
    toc_dir.mkdir(parents=True, exist_ok=True)
    try:
        (toc_dir / f"{section}.toc.json").write_bytes(
            _get(f"{base}/{section}/docdata/toc.json"))
    except Exception as e:  # noqa: BLE001
        print(f"[fetch] WARNING: could not save {section} toc: {e}", file=sys.stderr)


def _fetch_page(url: str, dest: Path, force: bool) -> str:
    if dest.exists() and not force and dest.stat().st_size > 0:
        return "skip"
    if REQUEST_DELAY:
        time.sleep(REQUEST_DELAY)
    try:
        blob = _get_retry(url)
    except urllib.error.HTTPError as e:
        return f"http {e.code}"
    except Exception as e:  # noqa: BLE001
        return f"err {e}"
    if len(blob) > MAX_FILE_BYTES:
        return "too-big"
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(blob)
    return "ok"


def _run(plan: list[tuple[str, Path]], workers: int, force: bool, label: str) -> int:
    if not plan:
        print(f"[fetch] {label}: nothing to do", file=sys.stderr)
        return 0
    stats: dict[str, int] = {}
    failures: list[str] = []
    t0 = time.time()
    with ThreadPoolExecutor(max_workers=max(1, workers)) as ex:
        futs = {ex.submit(_fetch_page, url, dest, force): (url, dest) for url, dest in plan}
        done = 0
        for f in as_completed(futs):
            status = f.result()
            stats[status] = stats.get(status, 0) + 1
            if status.startswith(("http", "err")):
                failures.append(f"{status} {futs[f][1].name}")
            done += 1
            if done % 250 == 0:
                print(f"[fetch] {label}: {done}/{len(plan)} ...", file=sys.stderr)
    print(f"[fetch] {label}: {len(plan)} files in {time.time() - t0:.1f}s - "
          + ", ".join(f"{k}={v}" for k, v in sorted(stats.items())))
    for f in failures[:15]:
        print(f"[fetch]   FAILED {f}", file=sys.stderr)
    if len(failures) > 15:
        print(f"[fetch]   ... and {len(failures) - 15} more", file=sys.stderr)
    return len(failures)


def _pkg_toc(pkg: str, ver: str, section: str) -> list[str]:
    """Page links from `<section>/toc.html`. Package docs ship no `toc.json`."""
    html = _get_retry(f"{PACKAGES_BASE}/{pkg}@{ver}/{section}/toc.html").decode(
        "utf-8", "replace")
    out: list[str] = []
    seen: set[str] = set()
    for href in RE_TOC_LINK.findall(html):
        if href.startswith(("http://", "https://", "/", "../", "#")):
            continue          # external or parent-relative (index.html, changelog, ...)
        if href in seen:
            continue
        seen.add(href)
        out.append(href[:-5])  # drop ".html" - the caller re-appends it
    return out


def _pkg_version(pkg: str, pinned: str) -> str:
    """The version the docs site actually serves, from Unity's package registry.

    `dist-tags.latest` is a full semver (`1.20.1`) but the docs site is versioned by
    `major.minor` (`@1.20`), so both are candidates. Pre-release tags (`7.0.0-exp.1`)
    are trimmed the same way.
    """
    latest = ""
    try:
        data = json.loads(_get_retry(PACKAGES_REGISTRY.format(pkg=pkg)).decode("utf-8"))
        latest = (data.get("dist-tags") or {}).get("latest", "") or ""
    except Exception:  # noqa: BLE001  (offline, unknown package -> pinned fallback)
        latest = ""
    cands = []
    for v in (latest, pinned):
        if not v:
            continue
        base = v.split("-")[0]              # 7.0.0-exp.1 -> 7.0.0
        parts = base.split(".")
        if len(parts) >= 2:
            cands.append(".".join(parts[:2]))   # 1.20.1 -> 1.20
        cands.append(base)
        cands.append(v)
    for v in dict.fromkeys(cands):          # dedupe, keep order
        try:
            _get_retry(f"{PACKAGES_BASE}/{pkg}@{v}/manual/toc.html")
            return v
        except Exception:  # noqa: BLE001
            continue
    return ""


def fetch_packages(force: bool, workers: int, limit: int) -> int:
    """Fetch UPM package manuals + API from `docs.unity3d.com/Packages/<name>@<ver>/`."""
    failures = 0
    toc_dir = config.PACKAGES_DOCS_DIR / "_toc"
    toc_dir.mkdir(parents=True, exist_ok=True)

    for pkg, pinned in PACKAGES.items():
        ver = _pkg_version(pkg, pinned)
        if not ver:
            print(f"[fetch] WARNING: no docs for {pkg} (registry latest and @{pinned} both "
                  f"unavailable)", file=sys.stderr)
            failures += 1
            continue

        got_any = False
        for section in PACKAGE_SECTIONS:
            try:
                links = _pkg_toc(pkg, ver, section)
            except Exception:  # noqa: BLE001  (many packages ship no `api/` toc)
                continue
            if not links:
                continue
            got_any = True
            (toc_dir / f"{pkg}@{ver}").mkdir(parents=True, exist_ok=True)
            try:
                (toc_dir / f"{pkg}@{ver}" / f"{section}.toc.html").write_bytes(
                    _get_retry(f"{PACKAGES_BASE}/{pkg}@{ver}/{section}/toc.html"))
            except Exception:  # noqa: BLE001
                pass
            if limit:
                links = links[:limit]
            out = config.PACKAGES_DOCS_DIR / pkg / section
            plan = [(f"{PACKAGES_BASE}/{pkg}@{ver}/{section}/{link}.html",
                     out / f"{link}.html") for link in links]
            failures += _run(plan, workers, force, f"packages_docs/{pkg}/{section}")
        if not got_any:
            print(f"[fetch] WARNING: {pkg}@{ver} had no readable toc.html", file=sys.stderr)
            failures += 1
    return failures


def fetch_csref(ref: str, force: bool, workers: int, limit: int) -> int:
    print(f"[fetch] {CSREF_REPO}@{ref}: reading tree ...", file=sys.stderr)
    try:
        data = json.loads(_get(CSREF_TREE.format(repo=CSREF_REPO, ref=ref)).decode("utf-8"))
    except Exception as e:  # noqa: BLE001
        print(f"[fetch] ERROR: cannot read {CSREF_REPO}@{ref}: {e}", file=sys.stderr)
        return 1
    if data.get("truncated"):
        print("[fetch] WARNING: GitHub tree truncated; corpus will be partial", file=sys.stderr)
    paths = [e["path"] for e in data.get("tree", [])
             if e.get("type") == "blob" and e["path"].endswith(".cs")
             and e["path"].startswith(CSREF_PREFIXES)
             and not e["path"].startswith(CSREF_SKIP)]
    if limit:
        paths = paths[:limit]
    plan = [(CSREF_RAW.format(repo=CSREF_REPO, ref=ref, path=p),
             config.OFFICIAL_SOURCE_DIR / p) for p in paths]
    return _run(plan, workers, force, "official_source")


def main() -> int:
    ap = argparse.ArgumentParser(description="Fetch the pinned Unity documentation corpus.")
    ap.add_argument("--version", default=config.UNITY_DOC_VERSION,
                    help="docs version path, e.g. 6000.3 or 6000.0")
    ap.add_argument("--only", default="", help="comma list of: manual,scriptref,packages,source")
    ap.add_argument("--with-source", action="store_true",
                    help="also fetch UnityCsReference C# (official_source)")
    ap.add_argument("--ref", default="", help="UnityCsReference git ref (default: the docs line)")
    ap.add_argument("--workers", type=int, default=4,
                    help="parallel downloads; keep low, docs.unity3d.com rate-limits")
    ap.add_argument("--delay", type=float, default=0.0,
                    help="seconds to wait before each request, per worker (throttle)")
    ap.add_argument("--limit", type=int, default=0, help="cap files per group (smoke test)")
    ap.add_argument("--force", action="store_true", help="re-download existing files")
    ap.add_argument("--check", action="store_true", help="report disk state and exit")
    a = ap.parse_args()

    global REQUEST_DELAY
    REQUEST_DELAY = max(0.0, a.delay)

    base = f"https://docs.unity3d.com/{a.version}/Documentation"
    only = {x.strip() for x in a.only.split(",") if x.strip()}
    unknown = only - {"manual", "scriptref", "packages", "source"}
    if unknown:
        print(f"[fetch] unknown --only values: {sorted(unknown)}", file=sys.stderr)
        return 2

    if a.check:
        for label, d in (("official_docs/Manual", config.OFFICIAL_DOCS_DIR / "Manual"),
                         ("official_docs/ScriptReference",
                          config.OFFICIAL_DOCS_DIR / "ScriptReference"),
                         ("official_source", config.OFFICIAL_SOURCE_DIR),
                         ("packages_docs", config.PACKAGES_DOCS_DIR),
                         ("cookbook", config.COOKBOOK_DIR),
                         ("recipes", config.RECIPES_DIR),
                         ("troubleshooting", config.TROUBLESHOOTING_DIR),
                         ("anti_patterns", config.ANTIPATTERNS_DIR)):
            n = sum(1 for f in d.rglob("*") if f.is_file()) if d.exists() else 0
            print(f"{label:32s} files={n}")
        return 0

    failures = 0
    want_docs = (not only) or bool(only & {"manual", "scriptref", "packages"})
    if want_docs:
        toc_dir = config.OFFICIAL_DOCS_DIR / "_toc"
        for key, section in SECTIONS.items():
            if only and key not in only:
                continue
            print(f"[fetch] {section}: reading toc ...", file=sys.stderr)
            try:
                links = _toc(base, section)
            except Exception as e:  # noqa: BLE001
                print(f"[fetch] ERROR: cannot read {section} toc: {e}", file=sys.stderr)
                failures += 1
                continue
            _save_toc(base, section, toc_dir)
            if a.limit:
                links = links[:a.limit]
            plan = [(f"{base}/{section}/{link}.html",
                     config.OFFICIAL_DOCS_DIR / section / f"{link}.html") for link in links]
            failures += _run(plan, a.workers, a.force, f"official_docs/{section}")

    if (not only) or "packages" in only:
        failures += fetch_packages(a.force, a.workers, a.limit)

    if a.with_source or "source" in only:
        ref = a.ref or config.UNITY_CSREF_REF
        failures += fetch_csref(ref, a.force, a.workers, a.limit)

    print("[fetch] done. Build the index with: python unity/tools/index.py", file=sys.stderr)
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
