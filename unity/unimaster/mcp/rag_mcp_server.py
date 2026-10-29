"""MCP server: hybrid search over the pinned Unity corpus.

Same two tools as the Three.js and Godot RAG servers (`*_rag_search`, `*_rag_status`),
so the agent's habits carry over. Registered by `.pi/extensions/engine-gate.ts` only
while the active project declares `engine: unity`.

Run standalone (for a smoke test):

    python -m unimaster.mcp.rag_mcp_server     # from the unity/ directory
"""
from __future__ import annotations

import json
import sys
import threading
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from mcp.server.fastmcp import FastMCP  # noqa: E402

from unimaster import config  # noqa: E402
from unimaster.rag.retriever import Retriever  # noqa: E402
from unimaster.rag.store import IndexStore  # noqa: E402

mcp = FastMCP("unity-rag")
_retriever: Retriever | None = None


def _get() -> Retriever:
    global _retriever
    if _retriever is None:
        _retriever = Retriever()
    return _retriever


def _preload() -> None:
    """Warm the vector matrix on a daemon thread while the agent is still booting.

    `_load_vectors()` reads ~1.3 GB of BLOBs - 95 s cold, 2.9 s warm - and that cost
    otherwise lands on whichever `unity_rag_search` the user runs first. Swallowing the
    error is correct here: this is an optimisation, and `dense_search` reloads lazily and
    falls back to lexical on its own.
    """
    try:
        _get().store.preload()
    except Exception:  # noqa: BLE001
        pass


@mcp.tool()
def unity_rag_search(query: str, top_k: int = 8, source: str = "", path_prefix: str = "") -> str:
    """Search the local Unity knowledge base: the 6000.3 Manual and ScriptReference,
    UnityCsReference C#, the cookbook, recipes, troubleshooting and anti-patterns, plus
    the active Unity project's own C#/assets indexed as source=project.

    Use it for Unity API questions (exact class/member names), error messages, and
    "how do I do X in Unity" - not for local file paths (use the file tools for that).

    Args:
        query: natural language or an exact API/error symbol, e.g. "Rigidbody.AddForce" or
            "MissingReferenceException after destroying an object".
        top_k: how many passages to return (1-12).
        source: restrict to one corpus: project, official_docs, official_source,
            packages_docs, cookbook, recipes, troubleshooting, anti_patterns.
        path_prefix: restrict to paths starting with this string.
    """
    top_k = max(1, min(int(top_k or 8), 12))
    filters: dict = {}
    if source:
        filters["source"] = source
    if path_prefix:
        filters["path_prefix"] = path_prefix
    hits = _get().search(query, top_k, filters or None)
    return json.dumps({"query": query, "count": len(hits),
                       "results": [h.to_dict() for h in hits]}, ensure_ascii=False, indent=1)


@mcp.tool()
def unity_rag_status() -> str:
    """Report the Unity RAG index statistics and the embedding server health."""
    store = IndexStore()
    ret = _get()
    payload = {
        "index": store.stats(),
        "embedding_server": {"url": ret.embedder.base_url, **ret.embedder.health()},
        # Non-zero means every answer so far was lexical-only, because `search()` keeps
        # answering after the dense half dies. Without this the degradation is invisible.
        "dense_failures": ret.dense_failures,
        "last_dense_error": ret.last_dense_error,
        "unity_version": config.UNITY_VERSION,
        "editor_version": config.UNITY_EDITOR_VERSION,
        "unity_editor": str(config.UNITY_EDITOR) if config.UNITY_EDITOR else None,
    }
    store.close()
    return json.dumps(payload, ensure_ascii=False, indent=1)


def main() -> None:
    threading.Thread(target=_preload, name="vec-preload", daemon=True).start()
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
