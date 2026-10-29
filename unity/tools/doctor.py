#!/usr/bin/env python
"""Environment check for the Unity stack.

    python unity/tools/doctor.py

Exits 1 if a *required* check fails. The shared llama.cpp servers are required (the
index needs :8081, the agent needs :8080); the Unity editor is reported but its absence
is not fatal - RAG questions can still be answered without it.
"""
from __future__ import annotations

import json
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "unity"))

from unimaster import config  # noqa: E402

OK, BAD, WARN = "  ok  ", " FAIL ", " warn "


def _http_json(url: str, timeout: float = 5.0):
    req = urllib.request.Request(url, headers={"User-Agent": "3gs-doctor"})
    opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
    with opener.open(req, timeout=timeout) as r:
        return json.loads(r.read().decode("utf-8", "replace"))


def check_servers() -> list[tuple[str, str, str]]:
    rows = []
    for name, url in (
        ("LLM   llama.cpp", f"http://127.0.0.1:{config.LLM_PORT}/v1/models"),
        ("EMBED llama.cpp", f"http://127.0.0.1:{config.EMBED_PORT}/health"),
    ):
        try:
            detail = json.dumps(_http_json(url))[:100]
            rows.append((OK, name, f"{url} -> {detail}"))
        except Exception as e:  # noqa: BLE001
            rows.append((BAD, name, f"{url} -> {type(e).__name__}: {e}"))
    return rows


def check_corpus() -> list[tuple[str, str, str]]:
    rows = []
    for label, d, hint in (
        ("docs Manual", config.OFFICIAL_DOCS_DIR / "Manual", "fetch_docs.py"),
        ("docs ScriptReference", config.OFFICIAL_DOCS_DIR / "ScriptReference", "fetch_docs.py"),
        ("source C#", config.OFFICIAL_SOURCE_DIR, "fetch_docs.py --with-source"),
        ("packages_docs", config.PACKAGES_DOCS_DIR, "fetch_docs.py (package manuals)"),
        ("cookbook", config.COOKBOOK_DIR, "shipped"),
        ("recipes", config.RECIPES_DIR, "shipped"),
        ("troubleshooting", config.TROUBLESHOOTING_DIR, "shipped"),
        ("anti_patterns", config.ANTIPATTERNS_DIR, "shipped"),
    ):
        n = sum(1 for f in d.rglob("*") if f.is_file()) if d.exists() else 0
        mark = OK if n else WARN
        extra = "" if n else f"  <- run: python unity/tools/{hint}"
        rows.append((mark, f"corpus {label}", f"{n} files{extra}"))
    return rows


def check_index() -> list[tuple[str, str, str]]:
    rows = []
    if not config.LEXICAL_DB.exists():
        rows.append((WARN, "index", f"{config.LEXICAL_DB} missing - run: "
                                  f"python unity/tools/index.py"))
        return rows
    try:
        from unimaster.rag.store import IndexStore

        st = IndexStore().stats()
        mark = OK if st["chunks"] > 500 else WARN
        rows.append((mark, "index", f"{st['chunks']} chunks, {st['with_vectors']} vectors, "
                                   f"{st['files']} files, "
                                   f"{config.LEXICAL_DB.stat().st_size / 1048576:.1f} MB"))
        rows.append((OK, "index sources", json.dumps(st["by_source"], ensure_ascii=False)))
    except Exception as e:  # noqa: BLE001
        rows.append((BAD, "index", f"{type(e).__name__}: {e}"))
    return rows


def check_toolchain() -> list[tuple[str, str, str]]:
    rows = []
    rows.append((OK if config.UNITY_EDITOR else BAD, "Unity editor",
                 str(config.UNITY_EDITOR) if config.UNITY_EDITOR else
                 f"not found - install an editor or set UNITY_EDITOR "
                 f"(looked under {config.UNITY_EDITORS_INSTALL_ROOT})"))
    rows.append((OK if config.UNITY_CLI else WARN, "Unity CLI",
                 str(config.UNITY_CLI) if config.UNITY_CLI else
                 "not found (optional: batch commands, editor bridge)"))
    try:
        project = config.resolve_project("")
        rows.append((OK, "active project", str(project)))
        rows.append((OK if (project / "Assets").is_dir() else WARN, "  Assets/",
                     "present" if (project / "Assets").is_dir() else "missing"))
    except Exception as e:  # noqa: BLE001
        rows.append((WARN, "active project", f"{e}"))
    return rows


def main() -> int:
    print(f"Unity stack doctor\n  root        : {config.UNIM_HOME}")
    print(f"  docs version: {config.UNITY_DOC_VERSION}  (editor {config.UNITY_EDITOR_VERSION})")
    print()
    rows = check_servers() + check_toolchain() + check_corpus() + check_index()
    fails = 0
    for mark, label, detail in rows:
        if mark == BAD:
            fails += 1
        print(f"[{mark}] {label:22s} {detail}")
    print()
    print(f"FAILURES: {fails}" if fails else "all required checks passed.")
    return 1 if fails else 0


if __name__ == "__main__":
    raise SystemExit(main())
