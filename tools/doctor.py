#!/usr/bin/env python
"""Environment check for the 3GS_Master Three.js agent.

Verifies, in order: python venv, local servers (LLM :8080, embeddings :8081, reranker
:8083 - optional), corpus on
disk, RAG index health, ComfyUI sidecar (:8188), the Blender DCC step, the agent-reach
research layer and the generated-asset store.

    python tools/doctor.py
"""
from __future__ import annotations

import json
import re
import shutil
import subprocess
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from threejs import config  # noqa: E402

OK = "  ok  "
BAD = " FAIL "
WARN = " warn "


def _http_json(url: str, timeout: float = 5.0):
    req = urllib.request.Request(url, headers={"User-Agent": "3gs-doctor"})
    opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
    with opener.open(req, timeout=timeout) as r:
        return json.loads(r.read().decode("utf-8", "replace"))


def _lock_holder() -> dict:
    if not config.GEN_LOCK_FILE.exists():
        return {}
    try:
        return json.loads(config.GEN_LOCK_FILE.read_text(encoding="utf-8"))
    except Exception:  # noqa: BLE001
        return {}


def check_servers() -> list[tuple[str, str, str]]:
    rows = []
    for name, url in (
        ("LLM   llama.cpp", f"http://127.0.0.1:{config.LLM_PORT}/v1/models"),
        ("EMBED llama.cpp", f"http://127.0.0.1:{config.EMBED_PORT}/health"),
    ):
        try:
            data = _http_json(url)
            detail = json.dumps(data)[:110]
            rows.append((OK, name, f"{url} -> {detail}"))
        except Exception as e:  # noqa: BLE001
            # A generation run stops the LLM on purpose and restarts it when it is done.
            # Reporting that as a failure would abort an `&&` chain and read as a broken
            # install, when the machine is in fact doing exactly what it should.
            if "LLM" in name and _lock_holder():
                rows.append((WARN, name, f"{url} -> stopped: a generation run is in progress "
                                         f"(pid {_lock_holder().get('pid')})"))
            else:
                rows.append((BAD, name, f"{url} -> {type(e).__name__}: {e}"))
    # The reranker is optional, so a missing one is a WARN and never a BAD: it costs
    # relevance, not answers, and the retrievers count the failure instead of failing.
    # Reported at all because a silent reranker is otherwise invisible - search keeps
    # working, just worse, and nothing else in the doctor would say so.
    rurl = f"http://127.0.0.1:{config.RERANK_PORT}/health"
    try:
        rows.append((OK, "RERANK llama.cpp", f"{rurl} -> {json.dumps(_http_json(rurl))[:110]}"))
    except Exception as e:  # noqa: BLE001
        rows.append((WARN, "RERANK llama.cpp (optional)",
                     f"{rurl} -> {type(e).__name__}: {e}  <- run: gs rerank"))
    return rows


def check_corpus() -> list[tuple[str, str, str]]:
    rows = []
    for label, d in (
        ("official_docs", config.OFFICIAL_DOCS_DIR),
        ("official_source", config.OFFICIAL_SOURCE_DIR),
        ("cookbook", config.COOKBOOK_DIR),
        ("rules", config.RULES_DIR),
        ("troubleshooting", config.TROUBLESHOOTING_DIR),
        ("anti_patterns", config.ANTIPATTERNS_DIR),
    ):
        n = sum(1 for f in d.rglob("*") if f.is_file()) if d.exists() else 0
        mark = OK if n else WARN
        hint = "" if n else "  <- run: python tools/fetch_threejs_docs.py"
        rows.append((mark, f"corpus {label}", f"{n} files  ({d}){hint}"))
    return rows


def check_index() -> list[tuple[str, str, str]]:
    rows = []
    if not config.LEXICAL_DB.exists():
        rows.append((BAD, "index", f"{config.LEXICAL_DB} missing - run: python tools/index.py"))
        return rows
    try:
        from threejs.rag.store import IndexStore

        st = IndexStore().stats()
        mark = OK if st["chunks"] > 500 else WARN
        rows.append((mark, "index", f"{st['chunks']} chunks, {st['with_vectors']} vectors, "
                                   f"{st['files']} files, {config.LEXICAL_DB.stat().st_size / 1048576:.1f} MB"))
        rows.append((OK, "index sources", json.dumps(st["by_source"], ensure_ascii=False)))
    except Exception as e:  # noqa: BLE001
        rows.append((BAD, "index", f"{type(e).__name__}: {e}"))
    return rows


def check_comfy() -> list[tuple[str, str, str]]:
    rows = []
    try:
        _http_json(f"{config.COMFY_BASE_URL}/system_stats")
        rows.append((OK, "ComfyUI sidecar", f"{config.COMFY_BASE_URL} -> up"))
    except Exception as e:  # noqa: BLE001
        rows.append((WARN, "ComfyUI sidecar",
                     f"{config.COMFY_BASE_URL} -> {type(e).__name__} "
                     f"(start: models\\text_image_3D\\3d_gen\\3d_comfy\\ComfyUI-Easy-Install\\Start ComfyUI.bat)"))
    root = config.COMFY_ROOT
    present = (root / "python_embeded" / "python.exe").exists() and (root / "ComfyUI" / "main.py").exists()
    rows.append((OK if present else BAD, "ComfyUI install", f"{root}" if present else f"not found at {root}"))
    return rows


def check_gpu() -> list[tuple[str, str, str]]:
    """Who holds the card.

    The whole scheduler exists to keep this at one resident model: with the 9B and
    ComfyUI both up, a 512x512 four-step image took 725 s and only 426 MiB of VRAM was
    free. Nothing else in this script would notice that.
    """
    rows = []
    from threejs.assets.hardware import vram

    reading = vram()
    if reading:
        rows.append((OK, "GPU", f"{reading['used_mb']} MiB used / {reading['free_mb']} MiB free "
                                f"of {reading['total_mb']} MiB"))
    else:
        rows.append((WARN, "GPU", "nvidia-smi unavailable - VRAM cannot be verified"))

    def up(url: str) -> bool:
        try:
            _http_json(url, timeout=3.0)
            return True
        except Exception:  # noqa: BLE001
            return False

    llm = up(f"http://127.0.0.1:{config.LLM_PORT}/v1/models")
    comfy = up(f"{config.COMFY_BASE_URL}/system_stats")
    if llm and comfy:
        rows.append((WARN, "GPU ownership",
                     "both llama-server :8080 and ComfyUI :8188 are resident - generation "
                     "will be slow. Use cmd/gen.cmd / asset_generate_pack (which stops the LLM "
                     "first) rather than starting ComfyUI by hand."))
    else:
        holder = "llama-server :8080" if llm else ("ComfyUI :8188" if comfy else "nothing")
        rows.append((OK, "GPU ownership", f"resident: {holder}"))

    holder = _lock_holder()
    if holder:
        rows.append((WARN, "gen lock", f"held by pid {holder.get('pid')} - a generation is in "
                                       f"progress; see logs\\generate.log"))
    return rows


def check_unity(quick: bool = False) -> list[tuple[str, str, str]]:
    """The Unity stack (`unity/`) is a sibling of the Three.js stack and shares the servers.

    Everything here is `warn` when absent: a machine that only does Three.js must not fail
    doctor because Unity was never set up. The Unity editor is the one row that is `FAIL`
    only when the stack is otherwise present but the editor cannot be found.

    `quick=True` skips the corpus walk and the index stats: `rglob("*")` по каталогу
    официальной документации Unity идёт минутами, а строка эта всё равно `warn`.
    """
    rows = []
    unity_home = ROOT / "unity"
    if not unity_home.is_dir():
        rows.append((WARN, "unity stack", f"{unity_home} missing"))
        return rows
    try:
        sys.path.insert(0, str(unity_home))
        from unimaster import config as ucfg  # noqa: PLC0415

        rows.append((OK if ucfg.UNITY_EDITOR else WARN, "unity editor",
                     str(ucfg.UNITY_EDITOR) if ucfg.UNITY_EDITOR else
                     "not found - set UNITY_EDITOR or install an editor"))
        rows.append((OK if ucfg.UNITY_CLI else WARN, "unity cli",
                     str(ucfg.UNITY_CLI) if ucfg.UNITY_CLI else "not found (optional)"))
        if quick:
            rows.append((WARN, "unity corpus", "not walked (quick mode)"))
            rows.append((WARN, "unity index", "not checked (quick mode)"))
            return rows
        corpus = sum(1 for d in (ucfg.OFFICIAL_DOCS_DIR, ucfg.OFFICIAL_SOURCE_DIR,
                                 ucfg.COOKBOOK_DIR, ucfg.RECIPES_DIR,
                                 ucfg.TROUBLESHOOTING_DIR, ucfg.ANTIPATTERNS_DIR)
                     if d.exists() for _ in d.rglob("*") if _.is_file())
        rows.append((OK if corpus > 100 else WARN, "unity corpus",
                     f"{corpus} files  (fetch: gs unity-fetch)"))
        if ucfg.LEXICAL_DB.exists():
            from unimaster.rag.store import IndexStore  # noqa: PLC0415

            st = IndexStore().stats()
            rows.append((OK if st["chunks"] > 500 else WARN, "unity index",
                         f"{st['chunks']} chunks, {st['with_vectors']} vectors, "
                         f"{ucfg.LEXICAL_DB.stat().st_size / 1048576:.1f} MB"))
        else:
            rows.append((WARN, "unity index", "missing - run: gs unity-index"))
    except Exception as e:  # noqa: BLE001
        rows.append((WARN, "unity stack", f"{type(e).__name__}: {e}"))
    return rows


def check_blender() -> list[tuple[str, str, str]]:
    """Blender is the DCC step the asset pipeline shells out to.

    Everything ComfyUI cannot do to a mesh - auto-rigging + animation retarget,
    quad retopology, UV cleanup, GLB/FBX conversion, headless preview renders - runs
    as `blender --background --python`. It is optional for pure image/3D generation,
    so a missing Blender is a `warn`, never a `FAIL`.
    """
    rows = []
    exe = getattr(config, "BLENDER_EXE", None)
    if exe and Path(exe).is_file():
        ver = ""
        try:
            out = subprocess.run([str(exe), "--version"], capture_output=True, text=True, timeout=20)
            ver = (out.stdout or "").splitlines()[0].strip() if out.stdout else ""
        except Exception:  # noqa: BLE001
            ver = "(version check failed)"
        rows.append((OK, "blender", f"{exe}  {ver}".rstrip()))
    else:
        rows.append((WARN, "blender",
                     "not found - set BLENDER_EXE or install Blender "
                     "(animation/rigging/retopo/GLB conversion will be unavailable)"))
    return rows


def check_agent_reach() -> list[tuple[str, str, str]]:
    """agent-reach is the research front end the agent uses to look things up.

    It is a capability layer over upstream CLIs (`yt-dlp`, `gh`, ...), not a library,
    so the check is "does the launcher resolve" rather than "does it import". The
    launcher lives in its own venv and reaches the shell through PATH; a terminal
    opened before that PATH entry was added will not see it, which is the usual
    reason a channel that works from a fresh prompt reports as missing.

    Optional for generation, so a missing agent-reach is a `warn`, never a `FAIL`.
    """
    rows = []
    exe = shutil.which("agent-reach")
    if not exe:
        fallback = Path.home() / ".agent-reach-venv" / "Scripts" / "agent-reach.exe"
        if fallback.is_file():
            rows.append((WARN, "agent-reach",
                         f"installed at {fallback} but not on PATH - open a new terminal "
                         "(or run: agent-reach doctor)"))
            return rows
        rows.append((WARN, "agent-reach",
                     "not found - install it for web/YouTube/GitHub research "
                     "(see ASSET-POLICY.md, research channels)"))
        return rows

    ver = ""
    try:
        out = subprocess.run([exe, "doctor"], capture_output=True, text=True, timeout=90,
                             encoding="utf-8", errors="replace")
        text = (out.stdout or "") + (out.stderr or "")
        # agent-reach prints "状态：N/16 个渠道可用" - surface the count, not the prose.
        match = re.search(r"(\d+)\s*/\s*(\d+)", text)
        if match:
            ver = f"{match.group(1)}/{match.group(2)} channels up"
        else:
            ver = "(doctor produced no channel count)"
    except Exception:  # noqa: BLE001
        ver = "(doctor check failed)"
    rows.append((OK, "agent-reach", f"{exe}  {ver}".rstrip()))
    return rows


def main() -> int:
    # --quick: пропустить проверки, которые ходят в сеть/поднимают процессы и могут
    # висеть минутами (agent-reach doctor: 90 с, Blender --version: 20 с, ComfyUI).
    # agent.cmd зовёт doctor на КАЖДОМ запуске, поэтому там нужен быстрый режим:
    # иначе старт пилота ждёт внешние сервисы, которые к запуску отношения не имеют.
    quick = "--quick" in sys.argv[1:]
    print(f"3GS_Master doctor{' (quick)' if quick else ''}\n  root        : {ROOT}")
    print(f"  three.js    : {config.THREE_VERSION}")
    print(f"  assets dir  : {config.ASSETS_DIR}")
    print()
    rows = check_servers() + check_gpu() + check_corpus() + check_index()
    if not quick:
        rows = rows + check_comfy() + check_blender() + check_agent_reach()
    rows = rows + check_unity(quick=quick)
    fails = 0
    for mark, label, detail in rows:
        if mark == BAD:
            fails += 1
        print(f"[{mark}] {label:20s} {detail}")
    if quick:
        print("\n(quick mode: comfy / blender / agent-reach not probed)")
    print()
    print("FAILURES:" if fails else "all required checks passed.", fails if fails else "")
    return 1 if fails else 0


if __name__ == "__main__":
    raise SystemExit(main())
