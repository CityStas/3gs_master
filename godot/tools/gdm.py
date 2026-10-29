"""gdmaster CLI: doctor / status / index / search / serve / tools.

Примеры:
    .venv\\Scripts\\python.exe tools\\gdm.py doctor
    .venv\\Scripts\\python.exe tools\\gdm.py index --project F:\\path\\to\\godot-project
    .venv\\Scripts\\python.exe tools\\gdm.py search "CharacterBody3D move_and_slide" --source official_docs
"""
from __future__ import annotations

import argparse
import json
import os
import socket
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from gdmaster import config  # noqa: E402


def _p(*a) -> None:
    print(*a, flush=True)


def _port_open(host: str, port: int, timeout: float = 0.4) -> bool:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(timeout)
        return s.connect_ex((host, port)) == 0


# --------------------------------------------------------------------------
def cmd_doctor(args) -> int:
    ok = True
    _p("== gdmaster doctor ==\n")

    _p(f"GDM_HOME      : {config.GDM_HOME}")
    _p(f"venv python   : {sys.executable}")
    _p(f"Godot exe     : {config.GODOT_EXE}  [{'OK' if config.GODOT_EXE.exists() else 'НЕТ'}]")
    if not config.GODOT_EXE.exists():
        ok = False

    proj = config.godot_project_root()
    _p(f"Godot project : {proj}  [{'OK' if proj and proj.exists() else 'НЕ ЗАДАН'}]")
    _p("")

    _p("-- файлы --")
    for label, path in (("llama-server", config.LLAMA_SERVER),
                        ("LLM gguf", config.LLM_GGUF),
                        ("embed gguf", config.EMBED_GGUF)):
        state = "OK" if path.exists() else "НЕТ"
        size = f"{path.stat().st_size/1e9:.2f} GB" if path.exists() else "-"
        if not path.exists():
            ok = False
        _p(f"{label:<13}: {state:<4} {size:>9}  {path}")
    _p("")

    _p("-- сервисы --")
    for label, host, port in (("LLM llama-server", config.LLM_HOST, config.LLM_PORT),
                              ("embed server", config.EMBED_HOST, config.EMBED_PORT)):
        up = _port_open(host, port)
        _p(f"{label:<17}: {'UP' if up else 'DOWN'}  http://{host}:{port}")
    _p("")

    _p("-- индекс --")
    try:
        from gdmaster.rag.store import IndexStore
        st = IndexStore().stats()
        _p(f"chunks={st['chunks']} files={st['files']} with_vectors={st['with_vectors']}")
        _p(f"by_source={st['by_source']}")
        if st["chunks"] == 0:
            _p("  ! индекс пуст — запусти index")
    except Exception as e:  # noqa: BLE001
        _p(f"  ! ошибка чтения индекса: {e}")
        ok = False
    _p("")

    _p("-- MCP --")
    gw = config.GDM_HOME / "gdmaster" / "mcp" / "policy_gateway.py"
    _p(f"policy gateway: {'OK' if gw.exists() else 'НЕТ'}")
    _p(f"audit log     : {config.LOGS_DIR / 'policy_audit.jsonl'}")
    _p("")
    _p("== " + ("ВСЁ ОК" if ok else "ЕСТЬ ПРОБЛЕМЫ") + " ==")
    return 0 if ok else 1


def cmd_status(args) -> int:
    from gdmaster.rag.store import IndexStore
    from gdmaster.rag.embedder import Embedder
    st = IndexStore().stats()
    emb = Embedder().health()
    out = {
        "index": st,
        "llm_server": {"url": config.LLM_BASE_URL, "up": _port_open(config.LLM_HOST, config.LLM_PORT)},
        "embed_server": {"url": config.EMBED_BASE_URL, "up": _port_open(config.EMBED_HOST, config.EMBED_PORT), **emb},
        "project": str(config.godot_project_root() or ""),
    }
    _p(json.dumps(out, ensure_ascii=False, indent=1))
    return 0


def cmd_index(args) -> int:
    from gdmaster.rag.indexer import Indexer
    from gdmaster.rag.store import IndexStore
    store = IndexStore()
    if args.reset:
        _p("Сброс индекса...")
        store.close()
        for f in (config.LEXICAL_DB, Path(str(config.LEXICAL_DB) + "-wal"), Path(str(config.LEXICAL_DB) + "-shm")):
            if f.exists():
                f.unlink()
        store = IndexStore()
    project = Path(args.project).resolve() if args.project else config.godot_project_root()
    if project:
        os.environ["GDM_PROJECT"] = str(project)
    only = args.only.split(",") if args.only else None
    idx = Indexer(store=store)
    rep = idx.run(project_root=project, force=args.full, only=only)
    _p(json.dumps(rep, ensure_ascii=False, indent=1))
    return 0


def cmd_search(args) -> int:
    from gdmaster.rag.retriever import Retriever
    r = Retriever()
    filters = {}
    if args.source:
        filters["source"] = args.source
    if args.path_prefix:
        filters["path_prefix"] = args.path_prefix
    hits = r.search(args.query, top_k=args.top_k, filters=filters or None,
                    alpha=0.0 if args.lexical_only else 1.0)
    if not hits:
        _p("Ничего не найдено.")
        return 1
    for i, h in enumerate(hits, 1):
        c = h.chunk
        _p(f"\n[{i}] score={h.score:.4f}  {c.source}  {c.path}")
        _p(f"    symbol={c.symbol}  section={c.section}  type={c.file_type}")
        body = c.text.strip().splitlines()
        for ln in body[:8]:
            _p("    | " + ln[:160])
        if len(body) > 8:
            _p(f"    | ... (+{len(body)-8} строк)")
    return 0


def cmd_serve(args) -> int:
    if not config.LLAMA_SERVER.exists():
        _p(f"Нет llama-server: {config.LLAMA_SERVER}")
        return 1
    if args.which == "llm":
        cmd = [
            str(config.LLAMA_SERVER), "-m", str(config.LLM_GGUF),
            "--host", config.LLM_HOST, "--port", str(config.LLM_PORT),
            "--jinja", "-c", str(config.LLM_CTX), "-ngl", str(config.LLM_NGL),
            "-fa", "on", "-np", "1", "--no-webui",
            "--temp", "0.6", "--top-p", "0.95", "--top-k", "20",
        ]
    else:
        cmd = [
            str(config.LLAMA_SERVER), "-m", str(config.EMBED_GGUF),
            "--host", config.EMBED_HOST, "--port", str(config.EMBED_PORT),
            "--embedding", "--pooling", os.environ.get("GDM_EMBED_POOLING", "cls"),
            "-c", "8192", "-ngl", os.environ.get("GDM_EMBED_NGL", "0"),
            "-b", "8192", "-ub", "8192", "--no-webui",
        ]
    _p("$ " + " ".join(cmd))
    return subprocess.call(cmd, cwd=str(config.GDM_HOME))


def cmd_tools(args) -> int:
    """Показать реальный tool surface, который увидит модель (через gateway)."""
    import anyio
    from gdmaster.mcp.policy_gateway import ALLOWED_TOOLS, Gateway

    async def run():
        gw = Gateway()
        await gw.start()
        try:
            _p(f"Gateway отдаёт модели {len(gw.tools)} инструментов "
               f"(allowlist={len(ALLOWED_TOOLS)}):\n")
            for t in sorted(gw.tools, key=lambda x: x.name):
                desc = (t.description or "").strip().splitlines()[0][:110]
                _p(f"  {t.name:<28} {desc}")
            if gw.startup_errors:
                _p("\nОшибки запуска дочерних серверов:")
                for e in gw.startup_errors:
                    _p("  ! " + e)
        finally:
            await gw.stop()

    anyio.run(run)
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(prog="gdm")
    sub = ap.add_subparsers(dest="cmd", required=True)

    sub.add_parser("doctor").set_defaults(func=cmd_doctor)
    sub.add_parser("status").set_defaults(func=cmd_status)

    p = sub.add_parser("index")
    p.add_argument("--project", default="")
    p.add_argument("--full", action="store_true", help="переиндексировать всё, игнорируя sha256")
    p.add_argument("--reset", action="store_true", help="удалить индекс и собрать заново")
    p.add_argument("--only", default="", help="official_docs,project,cookbook,troubleshooting,anti_patterns")
    p.set_defaults(func=cmd_index)

    p = sub.add_parser("search")
    p.add_argument("query")
    p.add_argument("--top-k", type=int, default=8)
    p.add_argument("--source", default="")
    p.add_argument("--path-prefix", default="")
    p.add_argument("--lexical-only", action="store_true")
    p.set_defaults(func=cmd_search)

    p = sub.add_parser("serve")
    p.add_argument("which", choices=["llm", "embed"])
    p.set_defaults(func=cmd_serve)

    sub.add_parser("tools").set_defaults(func=cmd_tools)

    args = ap.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
