"""unimaster - Unity-only local RAG stack for the 3GS_Master agent.

Mirror of the Godot stack (`godot/gdmaster`) and the Three.js stack (`threejs/`):
a pinned documentation corpus, a hybrid (dense + BM25) index, and MCP servers that
give the local 9B agent a *small* Unity tool surface.

Nothing here talks to the network at query time. The corpus is fetched once by
`unity/tools/fetch_docs.py` and then lives on disk.
"""

__all__ = ["config"]
