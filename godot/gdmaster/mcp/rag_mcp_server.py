"""RAG MCP-сервер.

Модели отдаются только два инструмента: `rag_search` и `rag_status`.
Остальное (reindex, get_document) доступно как CLI, но не как capability LLM —
это осознанное сужение tool surface (§18 спеки).
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from mcp.server.fastmcp import FastMCP  # noqa: E402

from gdmaster.rag.retriever import Retriever, format_context  # noqa: E402
from gdmaster.rag.store import IndexStore  # noqa: E402

mcp = FastMCP("godot-rag")

_retriever: Retriever | None = None


def _get() -> Retriever:
    global _retriever
    if _retriever is None:
        _retriever = Retriever()
    return _retriever


@mcp.tool()
def rag_search(query: str, top_k: int = 8, source: str = "", path_prefix: str = "") -> str:
    """Поиск по локальной базе знаний Godot 4.7 и по текущему проекту.

    Используй, когда нужно уточнить Godot API, сигнатуру метода, имя свойства
    или поведение узла, а также чтобы найти код/сцены в текущем проекте.

    Args:
        query: запрос. Лучше всего работают точные Godot-символы,
            например "CharacterBody3D move_and_slide" или "AnimationTree state machine".
        top_k: сколько passages вернуть (1-12, по умолчанию 8).
        source: фильтр источника: "official_docs" (документация движка),
            "project" (файлы текущего проекта), "cookbook" (готовые паттерны),
            "troubleshooting", "anti_patterns". Пусто = все источники.
        path_prefix: фильтр по пути, например "res://player/" или "player/".
    """
    top_k = max(1, min(int(top_k or 8), 12))
    filters: dict = {}
    if source:
        filters["source"] = source
    if path_prefix:
        filters["path_prefix"] = path_prefix.replace("res://", "")
    hits = _get().search(query, top_k=top_k, filters=filters or None)
    if not hits:
        return json.dumps(
            {"results": [], "note": "Ничего не найдено. Попробуй другие термины или "
                                    "проверь rag_status."},
            ensure_ascii=False, indent=1)
    payload = {
        "query": query,
        "count": len(hits),
        "results": [h.to_dict() for h in hits],
    }
    return json.dumps(payload, ensure_ascii=False, indent=1)


@mcp.tool()
def rag_status() -> str:
    """Состояние локального индекса знаний: сколько чанков, файлов, источников.

    Вызывай, если rag_search возвращает пусто или данные выглядят устаревшими.
    """
    store = IndexStore()
    stats = store.stats()
    emb = _get().embedder.health()
    payload = {
        "index": stats,
        "embedding_server": {"url": _get().embedder.base_url, **emb},
        "hint": "Если embedding_server.status != ok — запусти serve-embed.cmd и "
                "переиндексируй (index.cmd).",
    }
    store.close()
    return json.dumps(payload, ensure_ascii=False, indent=1)


def main() -> None:
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
