from __future__ import annotations
from dataclasses import dataclass

from .. import config
from .chunkers import Chunk
from .embedder import Embedder
from .reranker import Reranker
from .store import IndexStore

SOURCE_PRIORITY={
    "project":1.00,"rules":1.00,"official_docs":0.94,"official_source":0.92,
    "official_examples":0.90,"cookbook":0.88,"troubleshooting":0.86,"anti_patterns":0.84,
}

@dataclass
class Hit:
    id:str; score:float; chunk:Chunk; dense_rank:int|None=None; lexical_rank:int|None=None
    dense_score:float|None=None; lexical_score:float|None=None; rerank_score:float|None=None
    def to_dict(self,max_chars:int=2600):
        c=self.chunk; text=c.text if len(c.text)<=max_chars else c.text[:max_chars]+"\n... [truncated]"
        return {"score":round(self.score,5),"source":c.source,"path":c.path,"file_type":c.file_type,
                "symbol":c.symbol,"class":c.class_name,"extends":c.extends,"section":c.section,"content":text,
                "version":c.engine_version,"meta":c.meta}

class Retriever:
    def __init__(self,store=None,embedder=None,reranker=None):
        self.store=store or IndexStore(); self.embedder=embedder or Embedder()
        # None disables the second pass entirely; search() then returns exactly what it
        # returned before reranking existed.
        self.reranker=reranker if reranker is not None else (Reranker() if config.RERANK_ENABLED else None)
        # Counted, not merely swallowed: a dead embed server or reranker otherwise degrades
        # every answer silently and nothing anywhere records it.
        self.dense_failures=0; self.last_dense_error=None
        self.rerank_failures=0; self.last_rerank_error=None

    def search(self,query,top_k=None,filters=None,dense_k=None,lexical_k=None,alpha=1.0):
        top_k=top_k or config.FINAL_TOP_K; dense_k=dense_k or config.DENSE_TOP_K; lexical_k=lexical_k or config.LEXICAL_TOP_K
        dense=[]
        if alpha>0:
            try:dense=self.store.dense_search(self.embedder.embed_query(query),dense_k,filters)
            except Exception as e:
                self.dense_failures+=1; self.last_dense_error=f"{type(e).__name__}: {e}"; dense=[]
        lexical=self.store.lexical_search(query,lexical_k,filters)
        # 1-based, reporting only: to_dict() does not ship them, so the agent's prompt
        # budget is untouched and a dense/lexical mix stays visible in a debugger.
        d_rank={cid:i+1 for i,(cid,_) in enumerate(dense)}; l_rank={cid:i+1 for i,(cid,_) in enumerate(lexical)}
        d_score=dict(dense); l_score=dict(lexical)
        fused=self._rrf(dense,lexical,config.RRF_K,alpha)
        # Second pass over the fused shortlist only: the cross-encoder is O(pairs), and the
        # answer sits well inside RERANK_TOP_K - measured, a real answer was at lexical rank 46.
        order=fused[:config.RERANK_TOP_K] if self.reranker is not None else fused
        chunks=self.store.get_chunks([i for i,_ in order])
        r_score={}
        if self.reranker is not None:
            ids=[cid for cid,_ in order if cid in chunks]
            try:
                r_score=dict(zip(ids,self.reranker.rerank(query,[chunks[cid].text for cid in ids])))
                order=sorted(r_score.items(),key=lambda kv:-kv[1])
            except Exception as e:
                # A dead reranker must cost relevance, never answers.
                self.rerank_failures+=1; self.last_rerank_error=f"{type(e).__name__}: {e}"
                r_score={}; order=fused[:config.RERANK_TOP_K]
        out=[]
        for cid,score in order:
            c=chunks.get(cid)
            if c: out.append(Hit(cid,score*SOURCE_PRIORITY.get(c.source,0.9),c,
                                dense_rank=d_rank.get(cid),lexical_rank=l_rank.get(cid),
                                dense_score=d_score.get(cid),lexical_score=l_score.get(cid),
                                rerank_score=r_score.get(cid)))
        out.sort(key=lambda x:-x.score); return out[:top_k]
    @staticmethod
    def _rrf(dense,lexical,k=60,alpha=1.0):
        scores={}
        for rank,(cid,_) in enumerate(dense): scores[cid]=scores.get(cid,0)+alpha/(k+rank+1)
        for rank,(cid,_) in enumerate(lexical): scores[cid]=scores.get(cid,0)+1/(k+rank+1)
        return sorted(scores.items(),key=lambda x:-x[1])

def format_context(hits,max_total_chars=14000):
    parts=[]; used=0
    for h in hits:
        c=h.chunk; head=f"[{c.source}] {c.path}"
        if c.symbol: head+=f" :: {c.symbol}"
        body=c.text if len(c.text)<=2600 else c.text[:2600]+"\n... [truncated]"
        block=f"--- {head} ---\n{body}"
        if used+len(block)>max_total_chars: break
        parts.append(block); used+=len(block)
    return "\n\n".join(parts)
