from __future__ import annotations
import json,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[2]))
from mcp.server.fastmcp import FastMCP
from threejs.rag.retriever import Retriever
from threejs.rag.store import IndexStore

mcp=FastMCP("threejs-rag")
_retriever=None

def _get():
    global _retriever
    if _retriever is None:_retriever=Retriever()
    return _retriever

@mcp.tool()
def threejs_rag_search(query:str,top_k:int=8,source:str="",path_prefix:str="")->str:
    """Search local Three.js docs and the current project's indexed JS/TS/web code."""
    top_k=max(1,min(int(top_k or 8),12)); filters={}
    if source: filters["source"]=source
    if path_prefix: filters["path_prefix"]=path_prefix
    hits=_get().search(query,top_k,filters or None)
    return json.dumps({"query":query,"count":len(hits),"results":[h.to_dict() for h in hits]},ensure_ascii=False,indent=1)

@mcp.tool()
def threejs_rag_status()->str:
    """Return Three.js RAG index statistics and embedding server health."""
    store=IndexStore(); payload={"index":store.stats(),"embedding_server":{"url":_get().embedder.base_url,**_get().embedder.health()},"three_version":__import__('threejs.config',fromlist=['THREE_VERSION']).THREE_VERSION}; store.close(); return json.dumps(payload,ensure_ascii=False,indent=1)

def main(): mcp.run(transport="stdio")
if __name__=="__main__": main()
