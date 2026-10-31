#!/usr/bin/env python
"""Environment check for the Roblox stack: Studio, corpus, index, model servers.

    python roblox/tools/doctor.py            # full
    python roblox/tools/doctor.py --quick    # skip the index/DB read (used on agent start)
"""
from __future__ import annotations

import argparse
import json
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "roblox"))

from rbxmaster import config  # noqa: E402
from rbxmaster.luau import studio  # noqa: E402

OK = "  ok  "
BAD = " FAIL "
WARN = " warn "


def _health(url: str, timeout: float = 4.0):
    opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
    with opener.open(url, timeout=timeout) as r:
        return json.loads(r.read().decode("utf-8", "replace"))


def check_servers() -> list[tuple[str, str, str]]:
    rows = []
    for name, url in (
        ("EMBED :8081", f"http://127.0.0.1:{config.EMBED_PORT}/health"),
        ("RERANK :8083 (optional)", f"http://127.0.0.1:{config.RERANK_PORT}/health"),
    ):
        try:
            rows.append((OK, name, f"{url} -> {json.dumps(_health(url))[:100]}"))
        except Exception as e:  # noqa: BLE001
            # The reranker is optional: a missing one costs relevance, not answers, and the
            # retriever counts the failure instead of failing. A missing embedder is a
            # WARN too - the index still answers, lexical-only - but it says how to fix it.
            fix = "run: gs rerank" if "RERANK" in name else "run: gs embed"
            rows.append((WARN, name, f"{url} -> {type(e).__name__}  <- {fix}"))
    return rows


def check_studio() -> list[tuple[str, str, str]]:
    rows = []
    st = studio.status()
    rows.append((OK if st["studio_exe"] else WARN, "roblox studio",
                 st["studio_exe"] or "not found - set ROBLOX_STUDIO"))
    rows.append((OK if st["studio_mcp"] else WARN, "studio mcp",
                 st["studio_mcp"] or "StudioMCP.exe not found (needs a Studio build)"))
    running = st["studio_running"]
    rows.append((OK if running else WARN, "studio running",
                 "yes" if running else ("no" if running is False else "unknown")))
    return rows


def check_corpus(quick: bool = False) -> list[tuple[str, str, str]]:
    rows = []
    stats = config.corpus_stats()
    total = sum(stats.values())
    if total == 0:
        rows.append((BAD, "roblox corpus", "empty - run: gs roblox-fetch"))
        return rows
    detail = ", ".join(f"{k}={v}" for k, v in stats.items() if v)
    rows.append((OK if total > 1000 else WARN, "roblox corpus", f"{total} files ({detail})"))
    if quick:
        rows.append((WARN, "roblox index", "not checked (quick mode)"))
        return rows
    try:
        from rbxmaster.rag.store import IndexStore
        store = IndexStore()
        st = store.stats()
        store.close()
        healthy = st["chunks"] > 500
        rows.append((OK if healthy else WARN, "roblox index",
                     f"{st['chunks']} chunks, {st['with_vectors']} with vectors, "
                     f"{st['files']} files" + ("" if healthy else "  <- run: gs roblox-index")))
        if st["chunks"] and st["with_vectors"] < st["chunks"]:
            rows.append((WARN, "roblox vectors",
                         f"{st['chunks'] - st['with_vectors']} chunks have no embedding - "
                         f"run: gs roblox-index --vectors"))
        rows.append((OK, "roblox sources", json.dumps(st["by_source"])))
    except Exception as e:  # noqa: BLE001
        rows.append((WARN, "roblox index", f"{type(e).__name__}: {e}"))
    return rows


def check_project() -> list[tuple[str, str, str]]:
    raw = config.pointer_text()
    if not raw:
        return [(WARN, "active project", "data/active_project.txt is empty")]
    p = Path(raw)
    if not p.is_dir():
        return [(BAD, "active project", f"STALE: {raw} does not exist")]
    engine = ""
    try:
        engine = json.loads((p / "engine.json").read_text(encoding="utf-8")).get("engine", "")
    except (OSError, ValueError):
        pass
    if engine and str(engine).lower() != "roblox":
        return [(WARN, "active project", f"{p} declares engine={engine}, not roblox")]
    return [(OK, "active project", str(p))]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--quick", action="store_true")
    a = ap.parse_args()

    rows = check_studio() + check_corpus(quick=a.quick) + check_project()
    if not a.quick:
        rows += check_servers()

    width = max(len(n) for _, n, _ in rows)
    for status, name, detail in rows:
        print(f"[{status}] {name:<{width}}  {detail}")
    bad = sum(1 for s, _, _ in rows if s == BAD)
    print(f"\n{len(rows)} checks, {bad} failed")
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
