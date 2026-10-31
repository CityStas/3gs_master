#!/usr/bin/env python
"""Fetch the Roblox documentation corpus into `roblox/knowledge/`.

Three official machine-readable sources, one per corpus:

  `docs/llms-full.txt`            every guide page, already concatenated, one
                                  `<document url=... title=...>` block per page
                                  -> knowledge/official_docs/
  `reference/engine/llms.txt`     an index of 1210 API pages, one .md each
                                  -> knowledge/engine_api/{classes,datatypes,enums,...}/
  `cloud/llms.txt`                the Open Cloud REST reference (118 pages)
                                  -> knowledge/cloud_docs/

Plus the curated Russian starter kit, copied verbatim into `knowledge/curated_kb/`.

Why the full dump for guides and per-page fetches for the API: `llms-full.txt` is one
23 MB response for 1274 pages (a single request, no rate-limit risk), while the Engine API
has no `llms-full` variant - it 404s - so those pages are fetched individually with a
small worker pool.

The dump contains the API pages too, so `fetch_guides` skips any page that `engine_api/`
already holds - otherwise every API page is indexed twice. See its docstring.

    python roblox/tools/fetch_docs.py                 # everything, incremental
    python roblox/tools/fetch_docs.py --only engine_api --limit 20   # smoke test
    python roblox/tools/fetch_docs.py --force         # re-download everything
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "roblox"))

from rbxmaster import config  # noqa: E402

UA = "3gs-roblox-corpus/1.0 (+local RAG builder)"
TIMEOUT = 90
RE_DOCUMENT = re.compile(r'<document url="([^"]+)" title="([^"]*)">\s*(.*?)</document>', re.S)
RE_LINK = re.compile(r"\]\((/docs/[^)\s]+\.md)\)")
RE_UPDATED = re.compile(r"Last updated:\s*([0-9T:\-Z]+)")


def _get(url: str, retries: int = 3) -> str:
    last: Exception | None = None
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
                return r.read().decode("utf-8", "replace")
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, OSError) as e:
            last = e
            time.sleep(1.0 + attempt * 1.5)
    raise RuntimeError(f"{url}: {type(last).__name__}: {last}")


def _slug(url: str, strip: str = "") -> str:
    """URL path -> path relative to its corpus directory, ALWAYS relative.

    Two strips happen, in this order:
      1. the site root, `/docs/` with an optional `en-us/` locale segment;
      2. the corpus root, e.g. `cloud/` or `reference/engine/` - the part that names the
         corpus rather than a topic.

    The result is forced relative. That is not cosmetic: the cloud index mixes
    `/docs/cloud/...` and `/docs/en-us/cloud/api/...` links, and before this rule the
    second form produced `/docs/en-us/cloud/api/x.md`, which `Path(dest) / that` turns into
    an ABSOLUTE path - 43 pages were written to `F:\\docs\\en-us\\...` instead of the corpus.
    """
    p = url.split("?")[0].split("#")[0]
    p = re.sub(r"^/docs/(en-us/)?", "", p)
    if strip:
        p = re.sub(strip, "", p)
    return p.lstrip("/") or "index.md"


# Документация местами приводит правдоподобные примеры секретов: живой на вид
# Slack-webhook, ключи `sk-...`, AWS-ключи. GitHub push protection блокирует пуш
# такого корпуса (и правильно делает - правило не разбирает, пример это или нет),
# а нам нужен текст, а не сам секрет. Поэтому хвост подменяется плейсхолдером при
# записи: корпус можно перекачать и запушить, не заглядывая в веб-интерфейс.
REDACTIONS = [
    (re.compile(r"(https://hooks\.slack\.com/services/)[A-Za-z0-9/]{16,}"),
     r"\1<workspace>/<channel>/<token>"),
    (re.compile(r"\b(sk-)[A-Za-z0-9]{20,}"), r"\1<redacted>"),
    (re.compile(r"\b(AKIA|ASIA)[A-Z0-9]{16}\b"), r"\1<redacted>"),
    (re.compile(r"\bgh[pousr]_[A-Za-z0-9]{20,}"), "ghp_<redacted>"),
]


def _redact(text: str) -> str:
    for rx, rep in REDACTIONS:
        text = rx.sub(rep, text)
    return text


def _target(dest: Path, url: str, strip: str) -> Path:
    """`dest/slug`, refusing anything that escapes `dest`."""
    target = (dest / _slug(url, strip)).resolve()
    root = dest.resolve()
    if target != root and not target.is_relative_to(root):
        raise RuntimeError(f"refusing to write outside the corpus: {url} -> {target}")
    return target


def _write(path: Path, text: str, force: bool) -> bool:
    if path.exists() and not force:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(_redact(text), encoding="utf-8", newline="\n")
    return True


def fetch_guides(force: bool) -> dict:
    """The whole guide corpus in one request: `docs/llms-full.txt`.

    The dump also contains every Engine API page, byte-identical to what the per-page
    fetch puts in `engine_api/`. Writing both copies indexed the same page twice: 9940
    duplicate chunks, 56% of the guides corpus, and the *worse* copy won - the guides
    chunker has no per-member `signature`/`security` metadata, yet `official_docs`
    outranks `engine_api` in SOURCE_PRIORITY. So an API page is written to guides only
    when `engine_api/` does not already have it. The pages that are NOT there - the
    section indexes `globals.md`, `libraries.md`, `overview.md`, which the API index does
    not link - still land in guides, because they are real reference content.
    """
    index = _get(config.DOCS_INDEX_URL)
    updated = (RE_UPDATED.search(index) or [None, ""])[1] if RE_UPDATED.search(index) else ""
    raw = _get(config.DOCS_FULL_URL)
    docs = RE_DOCUMENT.findall(raw)
    written = 0
    duplicates = 0
    for url, _title, body in docs:
        target = _target(config.OFFICIAL_DOCS_DIR, url, "")
        rel = target.relative_to(config.OFFICIAL_DOCS_DIR.resolve()).as_posix()
        if rel.startswith("reference/engine/"):
            twin = config.ENGINE_API_DIR / rel[len("reference/engine/"):]
            if twin.is_file():
                duplicates += 1
                continue
        if _write(target, body.strip() + "\n", force):
            written += 1
    return {"source": "official_docs", "url": config.DOCS_FULL_URL, "found": len(docs),
            "written": written, "skipped": len(docs) - written - duplicates,
            "duplicates": duplicates, "docs_updated": updated}


def _engine_pages() -> list[str]:
    index = _get(config.ENGINE_INDEX_URL)
    return sorted(set(RE_LINK.findall(index)))


def _cloud_pages() -> list[str]:
    index = _get(config.CLOUD_INDEX_URL)
    return sorted(set(RE_LINK.findall(index)))


def _fetch_pages(pages: list[str], dest: Path, force: bool, workers: int,
                 label: str, strip: str) -> dict:
    todo = []
    for url in pages:
        target = _target(dest, url, strip)
        if target.exists() and not force:
            continue
        todo.append((url, target))
    done = 0
    errors: list[str] = []
    if todo:
        with ThreadPoolExecutor(max_workers=workers) as ex:
            futs = {ex.submit(_get, config.DOCS_BASE + url): (url, target)
                    for url, target in todo}
            for i, fut in enumerate(as_completed(futs), 1):
                url, target = futs[fut]
                try:
                    text = fut.result()
                except Exception as e:  # noqa: BLE001 - one bad page must not kill the run
                    errors.append(f"{url}: {e}")
                    continue
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text(_redact(text), encoding="utf-8", newline="\n")
                done += 1
                if i % 100 == 0:
                    print(f"  {label}: {i}/{len(todo)}", file=sys.stderr, flush=True)
    return {"source": label, "found": len(pages), "written": done,
            "skipped": len(pages) - len(todo), "errors": errors[:20],
            "error_count": len(errors)}


def fetch_kb(force: bool) -> dict:
    """Copy the curated starter kit verbatim. It is the only Russian-language corpus."""
    src = config.STARTER_KIT_DIR
    if not src.is_dir():
        return {"source": "curated_kb", "found": 0, "written": 0,
                "note": f"starter kit not found: {src}"}
    written = 0
    files = sorted(src.glob("*.md"))
    for p in files:
        if _write(config.CURATED_KB_DIR / p.name, p.read_text(encoding="utf-8"), force):
            written += 1
    return {"source": "curated_kb", "found": len(files), "written": written,
            "skipped": len(files) - written}


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description="Fetch the Roblox documentation corpus.")
    ap.add_argument("--only", default="",
                    help="comma list of: official_docs, engine_api, cloud_docs, curated_kb")
    ap.add_argument("--limit", type=int, default=0, help="cap pages per source (smoke test)")
    ap.add_argument("--force", action="store_true", help="re-download existing pages")
    ap.add_argument("--workers", type=int, default=8, help="parallel page fetches")
    a = ap.parse_args(argv[1:])

    only = {x.strip() for x in a.only.split(",") if x.strip()}
    known = {"official_docs", "engine_api", "cloud_docs", "curated_kb"}
    bad = only - known
    if bad:
        print(f"unknown --only: {sorted(bad)} (known: {', '.join(sorted(known))})",
              file=sys.stderr)
        return 2

    reports = []
    if not only or "curated_kb" in only:
        print("[fetch] curated starter kit ...", flush=True)
        reports.append(fetch_kb(a.force))
    if not only or "official_docs" in only:
        print("[fetch] guides (llms-full.txt, one request) ...", flush=True)
        reports.append(fetch_guides(a.force))
    if not only or "engine_api" in only:
        pages = _engine_pages()
        if a.limit:
            pages = pages[:a.limit]
        print(f"[fetch] engine API: {len(pages)} pages ...", flush=True)
        reports.append(_fetch_pages(pages, config.ENGINE_API_DIR, a.force, a.workers,
                                    "engine_api", r"^reference/engine/"))
    if not only or "cloud_docs" in only:
        pages = _cloud_pages()
        if a.limit:
            pages = pages[:a.limit]
        print(f"[fetch] Open Cloud: {len(pages)} pages ...", flush=True)
        reports.append(_fetch_pages(pages, config.CLOUD_DOCS_DIR, a.force, a.workers,
                                    "cloud_docs", r"^cloud/"))

    meta = json.loads(config.FETCH_META.read_text(encoding="utf-8")) if config.FETCH_META.exists() else {}
    meta.setdefault("sources", {})
    meta["fetched_at"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    for r in reports:
        if r.get("docs_updated"):
            meta["docs_updated"] = r["docs_updated"]
        meta["sources"][r["source"]] = {k: v for k, v in r.items() if k != "source"}
    meta["corpus_files"] = config.corpus_stats()
    config.FETCH_META.write_text(json.dumps(meta, ensure_ascii=False, indent=1), encoding="utf-8")

    print()
    for r in reports:
        extra = f" errors={r['error_count']}" if r.get("error_count") else ""
        note = f"  ({r['note']})" if r.get("note") else ""
        print(f"  {r['source']:14s} found={r.get('found', 0)} written={r.get('written', 0)} "
              f"skipped={r.get('skipped', 0)}{extra}{note}")
    print(f"\ncorpus: {config.corpus_stats()}")
    print(f"meta  : {config.FETCH_META}")
    print("next  : gs roblox-index")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
