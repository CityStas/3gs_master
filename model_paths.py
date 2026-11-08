#!/usr/bin/env python
"""Where the weights live - ONE definition, and no drive letters in it.

Why this file exists
--------------------
The weights are ~65 GB, so they are NOT in git: a clone gets code and nothing else.
That makes "where do the models live" a property of the MACHINE, not of the repo.
Before this file, that property was hardcoded in five places with two different
drives (`E:\\Programs\\LocalLLM\\Models` in `cmd/_env.cmd` and
`tools/llm_models.py`, `<repo>/models` in four stack configs and three `.cmd`
launchers). On any other machine at least one of them pointed at nothing.

The contract now
----------------
    GS_MODELS_ROOT    this project's root (wins)
    LOCAL_LLM_MODELS  the SHARED root - a neutral name other local-model tools read
                      too, so one folder of weights serves several apps
    GS_LLM_MODELS_DIR extra roots for CHAT models only, `;`-separated (optional)

Default is repo-relative on purpose: `git clone` + `gs models fetch` works on any
drive letter without editing a single file. A machine that keeps its weights on a
bigger disk sets one variable (`setx LOCAL_LLM_MODELS D://AI//Models`) or puts one
line in `local.env.cmd` (not tracked, see `local.env.example.cmd`), and every
consumer follows - the four stack configs, the llama.cpp router, `vlm.cmd`,
`sd-image.cmd`. No other project is named anywhere in this file.

Layout inside the root
----------------------
    llm/                     chat GGUFs for the router (:8080)
    vlm/Qwen2.5-VL-7B/       vision model + mmproj
    image/z-image-turbo/     diffusion + VAE + text encoder (sd-server, :8687)
    text_image_3D/           ComfyUI install and its 3D models (~45 GB)
    *.gguf at the root       the 9B chat default, bge-m3 embedder, bge reranker

Everything here is *resolved*, never assumed: `find()` walks the roots, and the
named helpers fall back to a glob when the canonical filename changed upstream.

    python model_paths.py               # human-readable report
    python model_paths.py --json        # machine-readable
    python model_paths.py --models-root # just the root (for .cmd / shell)
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

#: Repo root, derived from this file - never from cwd (MCP servers start anywhere).
#: This module sits in the repo root next to `project_layout.py`, so `parent` - not
#: `parents[1]` like the modules under `tools/`.
REPO = Path(__file__).resolve().parent

#: Canonical names. A missing file is reported by `report()`, not raised: half a
#: stack is a normal state (you may only need the RAG today).
DEFAULT_CHAT = "Qwen_Qwen3.5-9B-Q4_K_M.gguf"
EMBED_NAME = "bge-m3-q4_k_m.gguf"
RERANK_NAME = "bge-reranker-v2-m3-Q8_0.gguf"
VLM_DIR = "vlm/Qwen2.5-VL-7B"
VLM_MODEL_GLOB = "Qwen2.5-VL-7B-Instruct-Q4_K_M.gguf"
VLM_MMPROJ_GLOB = "mmproj-Qwen2.5-VL-7B-Instruct-Q8_0.gguf"
SD_DIR = "image/z-image-turbo"
SD_DIFF_GLOB = "z_image_turbo-Q4_K.gguf"
SD_VAE_GLOB = "ae.safetensors"
SD_TE_GLOB = "Qwen3-4B-Instruct-2507-Q4_K_M.gguf"
COMFY_DIR = "text_image_3D/3d_gen/3d_comfy/ComfyUI-Easy-Install"


def _local_env() -> dict[str, str]:
    """`local.env.cmd` parsed for the few variables that decide paths.

    Why parse batch at all: `cmd\\_env.cmd` sources that file, so batch sees the
    machine's paths; a Python entry point started directly (`python
    tools/llm_models.py`, an MCP server spawned by pi) inherits nothing. Without
    this, `python tools/llm_models.py` on a machine with `GS_LLM_MODELS_DIR` set
    would silently see fewer models than `cmd\\models.cmd` does - the exact class
    of drift this module exists to remove.

    Deliberately dumb: only `set "NAME=value"` / `set NAME=value`, only the names
    in `_LOCAL_KEYS`, comments and conditionals ignored. Nothing here executes.
    """
    f = REPO / "local.env.cmd"
    if not f.is_file():
        return {}
    out: dict[str, str] = {}
    try:
        text = f.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return {}
    for line in text.splitlines():
        line = line.strip()
        if not line or line.lower().startswith("rem") or line.startswith("::"):
            continue
        if line.lower().startswith("if "):
            continue
        if line.lower().startswith("set "):
            line = line[4:].strip()
        else:
            continue
        if line.startswith('"') and "=" in line:
            name, _, value = line[1:].partition("=")
            value = value.rstrip('"')
        elif "=" in line:
            name, _, value = line.partition("=")
        else:
            continue
        name = name.strip()
        if name.upper() not in _LOCAL_KEYS:
            continue
        out[name.upper()] = value.strip()
    return out


#: Variables `local.env.cmd` is allowed to set for the Python side. Everything
#: else in that file is batch-only (and `cmd\_env.cmd` still applies it there).
_LOCAL_KEYS = {
    "GS_MODELS_ROOT", "GS_LLM_MODELS_DIR", "BLENDER_EXE", "UNITY_EDITOR",
    "UNITY_CLI", "ROBLOX_STUDIO_MCP", "THREE_COMFY_ROOT", "THREE_TEXT_IMAGE_3D_DIR",
    "LOCAL_LLM_MODELS",
}

_LOCAL_CACHE: dict[str, str] | None = None


def _local(key: str) -> str:
    global _LOCAL_CACHE
    if _LOCAL_CACHE is None:
        _LOCAL_CACHE = _local_env()
    return _LOCAL_CACHE.get(key.upper(), "")


def _env_path(name: str) -> Path | None:
    """env var, then `local.env.cmd`, then nothing. Empty string is "not set"."""
    raw = (os.environ.get(name) or "").strip().strip('"') or _local(name)
    if not raw:
        return None
    return Path(raw).expanduser().resolve()


def models_root() -> Path:
    """The weights root. Order: `GS_MODELS_ROOT` -> `LOCAL_LLM_MODELS` -> `<repo>/models`.

    `LOCAL_LLM_MODELS` is the point of the whole exercise: it is a NEUTRAL name that
    this project does not own, so any other local-model tool (hc_local_ai_image_3D,
    a ComfyUI install, a second agent) can read the same variable and share one
    folder of weights without either project knowing the other exists. Set it once:

        setx LOCAL_LLM_MODELS "D:\\AI\\Models"

    `GS_MODELS_ROOT` still wins, because a machine that needs THIS project pointed
    somewhere specific should not have to fight a global default.
    """
    return (_env_path("GS_MODELS_ROOT")
            or _env_path("LOCAL_LLM_MODELS")
            or (REPO / "models"))


def llm_roots() -> list[Path]:
    """Roots scanned for CHAT GGUFs: the models root, then `GS_LLM_MODELS_DIR`.

    The extra roots are for alternative 9B builds kept outside the project
    (`E:\\Programs\\LocalLLM\\Models` on this machine). They are chat-only on
    purpose: embedding/rerank/VLM/3D must live in the models root, otherwise
    "which corpus is my RAG built from" stops having an answer.
    """
    out = [models_root()]
    raw = ((os.environ.get("GS_LLM_MODELS_DIR") or "").strip()
           or _local("GS_LLM_MODELS_DIR"))
    for part in raw.split(";"):
        part = part.strip().strip('"')
        if not part:
            continue
        p = Path(part).expanduser()
        if p not in out:
            out.append(p)
    return out


def path(*parts: str) -> Path:
    """`models_root()/parts...` - the canonical location, whether it exists or not."""
    return models_root().joinpath(*parts)


def find(*parts: str) -> Path | None:
    """First existing `root/parts...` across `llm_roots()`."""
    for root in llm_roots():
        candidate = root.joinpath(*parts)
        if candidate.is_file():
            return candidate
    return None


def _find_in(directory: Path, pattern: str) -> Path | None:
    """Exact name first, then a glob - upstream renames a quant, we still boot."""
    exact = directory / pattern
    if exact.is_file():
        return exact
    if any(ch in pattern for ch in "*?["):
        hits = sorted(directory.glob(pattern)) if directory.is_dir() else []
        return hits[0] if hits else None
    hits = sorted(directory.glob(pattern)) if directory.is_dir() else []
    return hits[0] if hits else None


def chat_gguf() -> Path | None:
    """The default chat model the router prefers (first one found)."""
    return find(DEFAULT_CHAT) or find("llm", DEFAULT_CHAT)


def embed_gguf() -> Path | None:
    return find(EMBED_NAME)


def rerank_gguf() -> Path | None:
    return find(RERANK_NAME)


def vlm_files() -> tuple[Path | None, Path | None]:
    """(model, mmproj) of the vision server; `vlm.cmd` needs both or neither."""
    d = path(VLM_DIR)
    return _find_in(d, VLM_MODEL_GLOB), _find_in(d, VLM_MMPROJ_GLOB)


def sd_files() -> tuple[Path | None, Path | None, Path | None]:
    """(diffusion, vae, text-encoder) of z-image-turbo (`sd-image.cmd`)."""
    d = path(SD_DIR)
    return _find_in(d, SD_DIFF_GLOB), _find_in(d, SD_VAE_GLOB), _find_in(d, SD_TE_GLOB)


def comfy_root() -> Path:
    """ComfyUI install. ~45 GB of the models root; env wins, then the canonical path."""
    for var in ("THREE_COMFY_ROOT", "HC_COMFY_ROOT", "HC_COMFY_ROOT_3D"):
        p = _env_path(var)
        if p:
            return p
    return path(COMFY_DIR)


def text_image_3d_dir() -> Path:
    p = _env_path("THREE_TEXT_IMAGE_3D_DIR")
    return p or path("text_image_3D")


def report() -> dict:
    """What is here and what is not - the shape `gs doctor` and `--json` print."""
    vlm, mmproj = vlm_files()
    diff, vae, te = sd_files()
    comfy = comfy_root()

    def row(p: Path | None) -> dict:
        if p is None:
            return {"path": None, "exists": False, "gb": None}
        try:
            gb = round(p.stat().st_size / 1e9, 2) if p.is_file() else None
        except OSError:
            gb = None
        return {"path": str(p), "exists": p.exists(), "gb": gb}

    return {
        "models_root": str(models_root()),
        "llm_roots": [str(p) for p in llm_roots()],
        "chat": row(chat_gguf()),
        "embed": row(embed_gguf()),
        "rerank": row(rerank_gguf()),
        "vlm_model": row(vlm),
        "vlm_mmproj": row(mmproj),
        "sd_diffusion": row(diff),
        "sd_vae": row(vae),
        "sd_text_encoder": row(te),
        "comfy": row(comfy),
    }


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description="where the model weights live")
    ap.add_argument("--models-root", action="store_true", help="print the root only")
    ap.add_argument("--llm-roots", action="store_true", help="print every chat root, one per line")
    ap.add_argument("--json", action="store_true", help="machine-readable report")
    a = ap.parse_args(argv[1:])

    if a.models_root:
        print(models_root())
        return 0
    if a.llm_roots:
        for p in llm_roots():
            print(p)
        return 0

    r = report()
    if a.json:
        print(json.dumps(r, indent=2, ensure_ascii=False))
        return 0

    print(f"models root : {r['models_root']}")
    extra = r["llm_roots"][1:]
    print(f"chat roots  : {len(r['llm_roots'])}" + (f"  (+{', '.join(extra)})" if extra else ""))
    print()
    rows = [
        ("chat", r["chat"]), ("embed", r["embed"]), ("rerank", r["rerank"]),
        ("vlm", r["vlm_model"]), ("vlm mmproj", r["vlm_mmproj"]),
        ("sd diffusion", r["sd_diffusion"]), ("sd vae", r["sd_vae"]),
        ("sd text enc", r["sd_text_encoder"]), ("comfyui", r["comfy"]),
    ]
    for label, row_ in rows:
        if row_["path"] is None:
            print(f"  {label:<14} MISSING (no file found)")
        elif row_["exists"]:
            size = f"{row_['gb']} GB" if row_["gb"] is not None else "dir"
            print(f"  {label:<14} ok       {size:<9} {row_['path']}")
        else:
            print(f"  {label:<14} MISSING  {row_['path']}")
    missing = [lbl for lbl, row_ in rows if not row_["exists"]]
    return 0 if not missing else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
