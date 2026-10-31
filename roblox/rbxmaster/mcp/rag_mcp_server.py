"""MCP server: hybrid search over the pinned Roblox corpus.

Same two tools as the Three.js / Godot / Unity RAG servers (`*_rag_search`, `*_rag_status`),
so the agent's habits carry over. Started by the `roblox` profile of `agent.cmd` and, in
WorkBuddy, from the shared MCP registry (`mcp/registry.json`).

Run standalone (for a smoke test):

    python -m rbxmaster.mcp.rag_mcp_server     # from the roblox/ directory
"""
from __future__ import annotations

import json
import sys
import threading
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from mcp.server.fastmcp import FastMCP  # noqa: E402

from rbxmaster import config  # noqa: E402
from rbxmaster.rag.retriever import Retriever  # noqa: E402
from rbxmaster.rag.store import IndexStore  # noqa: E402

mcp = FastMCP("rbx-rag")
_retriever: Retriever | None = None


def _get() -> Retriever:
    global _retriever
    if _retriever is None:
        _retriever = Retriever()
    return _retriever


def _preload() -> None:
    """Warm the vector matrix on a daemon thread while the agent is still booting.

    `_load_vectors()` reads the whole embedding matrix off disk; that cost otherwise lands
    on whichever `rbx_rag_search` the user runs first. Swallowing the error is correct: this
    is an optimisation, and `dense_search` reloads lazily and falls back to lexical.
    """
    try:
        _get().store.preload()
    except Exception:  # noqa: BLE001
        pass


@mcp.tool()
def rbx_rag_search(query: str, top_k: int = 8, source: str = "", path_prefix: str = "",
                   context: str = "") -> str:
    """Search the local Roblox knowledge base: the Creator Hub guides, the Engine API
    Reference (one chunk per class member), the Open Cloud reference, the curated Russian
    starter kit, the cookbook, troubleshooting and anti-patterns, plus the active Roblox
    project's own Luau indexed as source=project.

    Use it for Roblox/Luau API questions (exact class, member, event or enum names), error
    messages and "how do I do X in Roblox". It does NOT see the live Studio session - for
    that use the Roblox Studio MCP tools (`execute_luau`, `script_read`, `search_game_tree`).

    Args:
        query: natural language or an exact API/error symbol, e.g. "RemoteEvent:FireClient"
            or "DataStore request was added to queue" or "как сохранить данные игрока".
        top_k: how many passages to return (1-12).
        source: restrict to one corpus: project, curated_kb, official_docs, engine_api,
            cloud_docs, cookbook, troubleshooting, anti_patterns.
        path_prefix: restrict to paths starting with this string.
        context: restrict API hits to server, client or shared.
    """
    top_k = max(1, min(int(top_k or 8), 12))
    filters: dict = {}
    if source:
        filters["source"] = source
    if path_prefix:
        filters["path_prefix"] = path_prefix
    if context:
        filters["context"] = context
    hits = _get().search(query, top_k, filters or None)
    return json.dumps({"query": query, "count": len(hits),
                       "results": [h.to_dict() for h in hits]}, ensure_ascii=False, indent=1)


@mcp.tool()
def rbx_rag_status() -> str:
    """Report the Roblox RAG index statistics, the embedding server health and the corpus
    size on disk (so "the answer was thin" can be told apart from "the corpus is missing")."""
    store = IndexStore()
    ret = _get()
    payload = {
        "index": store.stats(),
        "embedding_server": {"url": ret.embedder.base_url, **ret.embedder.health()},
        # Non-zero means every answer so far was lexical-only, because `search()` keeps
        # answering after the dense half dies. Without this the degradation is invisible.
        "dense_failures": ret.dense_failures,
        "last_dense_error": ret.last_dense_error,
        "rerank_failures": ret.rerank_failures,
        "last_rerank_error": ret.last_rerank_error,
        "docs_version": config.RBX_VERSION,
        "studio_build": config.STUDIO_BUILD or None,
        "corpus_files": config.corpus_stats(),
    }
    store.close()
    return json.dumps(payload, ensure_ascii=False, indent=1)


def main() -> None:
    threading.Thread(target=_preload, name="vec-preload", daemon=True).start()
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
