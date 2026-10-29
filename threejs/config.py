from __future__ import annotations

import os
from pathlib import Path

THREE_RAG_HOME = Path(os.environ.get("THREE_RAG_HOME", Path(__file__).resolve().parent.parent)).resolve()
DATA_DIR = THREE_RAG_HOME / "data"
SQLITE_DIR = DATA_DIR / "sqlite"
KNOWLEDGE_DIR = THREE_RAG_HOME / "knowledge"
OFFICIAL_DOCS_DIR = KNOWLEDGE_DIR / "official_docs"
OFFICIAL_SOURCE_DIR = KNOWLEDGE_DIR / "official_source"
COOKBOOK_DIR = KNOWLEDGE_DIR / "cookbook"
TROUBLESHOOTING_DIR = KNOWLEDGE_DIR / "troubleshooting"
ANTIPATTERNS_DIR = KNOWLEDGE_DIR / "anti_patterns"
RULES_DIR = KNOWLEDGE_DIR / "rules"
LOGS_DIR = THREE_RAG_HOME / "logs"
LEXICAL_DB = SQLITE_DIR / "lexical.db"

# --- generated-asset store (text -> image -> 3D -> three.js) ---------------------
# Every artefact produced by the ComfyUI pipeline lands here under a slug derived from
# the request, never under a ComfyUI template name like `ComfyUI_00007_.glb`.
ASSETS_DIR = Path(os.environ.get("THREE_ASSETS_DIR", THREE_RAG_HOME / "assets"))
ASSET_IMAGE_DIR = ASSETS_DIR / "images"
ASSET_MASK_DIR = ASSETS_DIR / "masks"
ASSET_3D_DIR = ASSETS_DIR / "3d"
ASSET_SPLAT_DIR = ASSETS_DIR / "splats"
ASSET_PREVIEW_DIR = ASSETS_DIR / "previews"
# Projects live in `projects/games` - the launchers read the same layout from
# `cmd/_env.cmd` (GS_GAMES). Both places move together.
GAMES_DIR = Path(os.environ.get("THREE_GAMES_DIR", THREE_RAG_HOME / "projects" / "games"))
ACTIVE_PROJECT_FILE = DATA_DIR / "active_project.txt"

# The `assets/` store above is the scratch pile for one-off probes. A game wants its
# files inside its own tree, so the pipeline can be rooted anywhere:
# `AssetPipeline(root=<project>/public/assets)` writes the same images/ masks/ 3d/
# layout under that root. One table, two roots.
ASSET_SUBDIR = {
    "image": "images", "mask": "masks", "mesh": "3d", "splat": "splats",
    "preview": "previews", "file": "3d",
}
# Default asset home inside a project. Vite serves `public/` at the site root, so a
# runtime fetch of `/assets/<name>.png` resolves with no bundler involvement.
PROJECT_ASSET_ROOT = os.environ.get("THREE_PROJECT_ASSET_ROOT", "public/assets")

# --- serialised generation ------------------------------------------------------
# One GPU, one resident model. `assets/scheduler.py` produces a pack into
# `gen-staging/<run>/` and only moves it into the project once the run has finished,
# so a failed run cannot leave half-written files in the game's asset tree.
GEN_STAGING_DIR = DATA_DIR / "gen-staging"
GEN_LOCK_FILE = DATA_DIR / "gen.lock"
GEN_STATUS_FILE = DATA_DIR / "gen-status.json"
GENERATE_LOG = LOGS_DIR / "generate.log"

for d in (DATA_DIR, SQLITE_DIR, KNOWLEDGE_DIR, OFFICIAL_DOCS_DIR, OFFICIAL_SOURCE_DIR,
          COOKBOOK_DIR, TROUBLESHOOTING_DIR, ANTIPATTERNS_DIR, RULES_DIR, LOGS_DIR,
          ASSET_IMAGE_DIR, ASSET_MASK_DIR, ASSET_3D_DIR, ASSET_SPLAT_DIR,
          ASSET_PREVIEW_DIR, GAMES_DIR, GEN_STAGING_DIR):
    d.mkdir(parents=True, exist_ok=True)


def resolve_project(name_or_path: str | Path = "") -> Path:
    """The one definition of "the project directory".

    `agent.cmd <project>` writes the path to `data/active_project.txt`; the MCP servers
    and the generation scheduler read it back, so a tool call that says only
    `project="new_local_game"` lands in the same place the agent is editing.

    Accepts, in order: an existing absolute path; an existing path relative to the
    current directory; a path relative to the repo root; a bare name under
    `projects/games/`.

    **A pointer is a hint, never a fact.** `projects/games/` is user data: games get
    created, renamed and deleted while `data/active_project.txt` still names the old one.
    So this function resolves the hint on EVERY call and refuses to invent a path:

      * an absolute path is returned as-is - that is the caller's explicit business;
      * a relative one is tried against cwd, then the repo root, then `projects/games/`;
      * if nothing on disk matches and the value came from the POINTER, that pointer is
        stale -> `ValueError` naming it. Previously this fell through to
        `GAMES_DIR / raw`, which for a repo-relative `raw` produced
        `projects/games/projects/games/<name>` - a path that can never exist, returned
        silently, so every caller failed later with an error about the wrong directory;
      * if nothing matches and the caller passed the value EXPLICITLY, a bare name is
        still assumed to be a game that may not exist yet (`newgame.cmd`), while a
        relative path that already carries directories is treated as repo-relative and
        is NOT joined onto `GAMES_DIR` a second time.

    Callers that must tolerate "no project" catch `ValueError` (see `tools/pagecheck.py`,
    `unity/tools/doctor.py`, `pipeline.locate_input`).
    """
    explicit = str(name_or_path or "").strip().strip('"')
    raw = explicit
    from_pointer = False
    if not raw and ACTIVE_PROJECT_FILE.exists():
        raw = ACTIVE_PROJECT_FILE.read_text(encoding="utf-8", errors="replace").strip()
        from_pointer = bool(raw)
    if not raw:
        raise ValueError(
            "no project given, and data/active_project.txt is empty. Pass project=..., "
            "or start the agent with `agent.cmd <path-to-threejs-project>`."
        )
    p = Path(raw).expanduser()
    if p.is_absolute():
        # An explicit absolute path is the caller's business - it may be a project
        # outside `projects/games/` that is about to be created. From the POINTER it is
        # system state about user data, so a vanished target has to be reported.
        if from_pointer and not p.is_dir():
            raise ValueError(
                "the active project is stale: data/active_project.txt points at %r, "
                "which does not exist - the game was deleted or renamed. Re-run "
                "`dev.cmd <name>` or `agent.cmd <project>` to point the system at a "
                "live project." % raw
            )
        return p.resolve()
    # `is_dir`, not `exists`: the result is called "the project directory", and a file
    # that happens to carry the name must not shadow it.
    for candidate in (Path.cwd() / p, THREE_RAG_HOME / p, GAMES_DIR / p):
        if candidate.is_dir():
            return candidate.resolve()
    if from_pointer:
        raise ValueError(
            "the active project is stale: data/active_project.txt points at %r, which "
            "does not exist - the game was deleted or renamed. Re-run `dev.cmd <name>` "
            "or `agent.cmd <project>` to point the system at a live project." % raw
        )
    if p.parent == Path("."):
        # A bare name is the ONE case where GAMES_DIR is the right parent: the project
        # may legitimately not exist yet and be created by `newgame.cmd <name>`.
        return (GAMES_DIR / p).resolve()
    return (THREE_RAG_HOME / p).resolve()


# Pinned to the npm dist-tag verified on 2026-10-07 (registry.npmjs.org/three/latest).
# Bumping this invalidates every chunk header -> run `index.cmd --force`.
THREE_VERSION = os.environ.get("THREE_VERSION", "0.186.1")
LLM_HOST = os.environ.get("THREE_LLM_HOST", "127.0.0.1")
LLM_PORT = int(os.environ.get("THREE_LLM_PORT", "8080"))
LLM_BASE_URL = f"http://{LLM_HOST}:{LLM_PORT}/v1"
EMBED_HOST = os.environ.get("THREE_EMBED_HOST", "127.0.0.1")
EMBED_PORT = int(os.environ.get("THREE_EMBED_PORT", "8081"))
EMBED_BASE_URL = f"http://{EMBED_HOST}:{EMBED_PORT}"
EMBED_DIM = int(os.environ.get("THREE_EMBED_DIM", "1024"))
EMBED_BATCH = int(os.environ.get("THREE_EMBED_BATCH", "32"))
EMBED_WORKERS = int(os.environ.get("THREE_EMBED_WORKERS", "4"))
# Cross-encoder reranker (:8083, `gs rerank`). Optional by design: if the port is
# silent the retriever keeps the RRF order and answers as it did before.
# NOT :8082 - that is the Qwen2.5-VL vision server (`cmd\vlm.cmd`).
RERANK_HOST = os.environ.get("THREE_RERANK_HOST", "127.0.0.1")
RERANK_PORT = int(os.environ.get("THREE_RERANK_PORT", "8083"))
RERANK_BASE_URL = f"http://{RERANK_HOST}:{RERANK_PORT}"

# ComfyUI sidecar (image / background-removal / image-to-3D backend).
# Lives under models/text_image_3D/ - the local text -> image -> 3D generation stack.
# It sat at the repo root until 2026-10-12; `THREE_TEXT_IMAGE_3D_DIR` still overrides.
COMFY_HOST = os.environ.get("THREE_COMFY_HOST", "127.0.0.1")
COMFY_PORT = int(os.environ.get("THREE_COMFY_PORT", "8188"))
COMFY_BASE_URL = f"http://{COMFY_HOST}:{COMFY_PORT}"
TEXT_IMAGE_3D_DIR = Path(os.environ.get(
    "THREE_TEXT_IMAGE_3D_DIR", THREE_RAG_HOME / "models" / "text_image_3D"
))
COMFY_ROOT = Path(os.environ.get(
    "THREE_COMFY_ROOT",
    os.environ.get("HC_COMFY_ROOT", TEXT_IMAGE_3D_DIR / "3d_gen" / "3d_comfy" / "ComfyUI-Easy-Install"),
))

# Which third-party node packs ComfyUI is allowed to load.
#
# Every node our workflows use is *native* (`comfy_extras/nodes_trellis2.py`,
# `nodes_triposplat.py`, `nodes_moge.py`, `nodes_bg_removal.py`, ...) - verified by
# resolving all 100+ class_types in `assets/workflows/*.json` against the core
# registry. The single exception is `UnetLoaderGGUF` in the Qwen-Image graphs.
#
# Leaving the other 25 packs enabled costs ~250 s of imports on every cold start
# (ComfyUI-Trellis2 118 s, ComfyUI-Easy-Use 60 s, comfyui-easy-sam3 13 s, ...),
# which is what pushed a 3D job past its 420 s startup budget. `--disable-all-custom-nodes`
# plus this whitelist takes the start down to a torch import and a CUDA init.
#
# A pack that is genuinely needed again shows up as a loud ComfyUI 400 naming the
# missing class, not as a silent misrender - so widening this is a one-line fix.
#
# `THREE_COMFY_CUSTOM_NODES=*` (or `all`) restores the legacy "load every pack"
# behaviour for the case where someone's install genuinely needs the rest.
_COMFY_CUSTOM_NODES_RAW = os.environ.get("THREE_COMFY_CUSTOM_NODES", "ComfyUI-GGUF").strip()
COMFY_CUSTOM_NODES: tuple[str, ...] | None = (
    None if _COMFY_CUSTOM_NODES_RAW in ("*", "all")
    else tuple(n.strip() for n in _COMFY_CUSTOM_NODES_RAW.split(",") if n.strip())
)

# z-image-turbo via stable-diffusion.cpp (`bin/sd-vulkan/`) - the fast text-to-image
# engine. Six-to-ten step distilled model: ~20 s warm against ~12 min for the ComfyUI
# Qwen-Image path, at 3.8 GB of VRAM instead of 8.9 GB, because its text encoder runs
# on the CPU. ComfyUI stays the fallback for what z-image cannot do (prompt-faithful
# lettering, BiRefNet cut-outs, image-to-3D).
SD_HOST = os.environ.get("THREE_SD_HOST", "127.0.0.1")
SD_PORT = int(os.environ.get("THREE_SD_PORT", "8687"))
SD_BASE_URL = f"http://{SD_HOST}:{SD_PORT}"
SD_BIN_DIR = Path(os.environ.get("THREE_SD_BIN_DIR", THREE_RAG_HOME / "bin" / "sd-vulkan"))
SD_MODEL_DIR = Path(os.environ.get("THREE_SD_MODEL_DIR",
                                   THREE_RAG_HOME / "models" / "image" / "z-image-turbo"))

# Real-ESRGAN (ncnn/Vulkan) - upscales a finished picture instead of making the
# diffusion model draw it large. Holds a few hundred MB, so it is not part of the
# resident-model arbitration.
ESRGAN_DIR = Path(os.environ.get("THREE_ESRGAN_DIR",
                                 THREE_RAG_HOME / "bin" / "Real-ESRGAN-ncnn-vulkan"))

# --- Blender - the DCC step the asset pipeline does not own ----------------------
# ComfyUI hands back a raw GLB and stops there. Everything that needs an actual
# *edit* of that mesh runs through Blender in headless mode
# (`blender --background --python script.py`):
#
#   * auto-rigging + animation retarget (Kimodo / Mixamo / ARDY motion onto our mesh)
#   * quad retopology and UV cleanup for game-ready low-poly
#   * GLB <-> FBX <-> OBJ conversion, GLB packing, Draco/gltfpack passes
#   * texture rebake (albedo / normal / AO), normal-map fixes
#   * headless turntable renders for `assets/previews/`
#
# Blender is NOT a resident model and NOT part of the VRAM arbitration: like
# Real-ESRGAN it holds a few hundred MB, so a headless run can sit next to ComfyUI.
# Present on this machine at `E:\Programs\Blender\blender.exe` (5.2.2 LTS).
BLENDER_CANDIDATES = [
    Path(r"E:\Programs\Blender\blender.exe"),
]
BLENDER_SEARCH_ROOTS = [
    Path(r"E:\Programs\Blender"),
    Path(r"C:\Program Files\Blender Foundation"),
]
BLENDER_VERSION = os.environ.get("THREE_BLENDER_VERSION", "5.2")


def _first_blender() -> "Path | None":
    for p in BLENDER_CANDIDATES:
        try:
            if p.is_file():
                return p
        except OSError:
            continue
    for root in BLENDER_SEARCH_ROOTS:
        try:
            if not root.is_dir():
                continue
        except OSError:
            continue
        # Flat install (`...\Blender\blender.exe`) or Hub/version layout
        # (`...\Blender Foundation\Blender 5.2\blender.exe`).
        for hit in sorted(root.glob("blender.exe")) + sorted(root.glob("*/blender.exe")):
            if hit.is_file():
                return hit
    return None


def resolve_blender() -> "Path | None":
    """Path to `blender.exe`, or None.

    Env wins, but only when the file actually exists - a stale variable pointing at a
    deleted build must not shadow a working install (same rule as the Unity editor).
    """
    for key in ("THREE_BLENDER_EXE", "BLENDER_EXE", "BLENDER_PATH"):
        raw = os.environ.get(key)
        if raw:
            p = Path(raw)
            if p.is_file():
                return p
    return _first_blender()


BLENDER_EXE: "Path | None" = resolve_blender()
BLENDER_DIR: "Path | None" = BLENDER_EXE.parent if BLENDER_EXE else None

DENSE_TOP_K = int(os.environ.get("THREE_DENSE_TOP_K", "20"))
LEXICAL_TOP_K = int(os.environ.get("THREE_LEXICAL_TOP_K", "20"))
FINAL_TOP_K = int(os.environ.get("THREE_FINAL_TOP_K", "8"))
RRF_K = int(os.environ.get("THREE_RRF_K", "60"))
# Reranking. TOP_K=50 is deliberate: on the Unity corpus a query's best chunk sat at
# lexical rank 46 and only the reranker could lift it, so a shortlist of 20 would have
# thrown the answer away before the cross-encoder ever saw it. MAX_CHARS is clipped
# because llama.cpp rejects a single sequence longer than one slot's context.
RERANK_ENABLED = os.environ.get("THREE_RERANK_ENABLED", "1").lower() not in ("0", "false", "no")
RERANK_TOP_K = int(os.environ.get("THREE_RERANK_TOP_K", "50"))
RERANK_MAX_CHARS = int(os.environ.get("THREE_RERANK_MAX_CHARS", "2000"))
RERANK_BATCH = int(os.environ.get("THREE_RERANK_BATCH", "32"))
RERANK_TIMEOUT = float(os.environ.get("THREE_RERANK_TIMEOUT", "60"))
MAX_INDEX_FILE_BYTES = int(os.environ.get("THREE_MAX_INDEX_FILE_BYTES", str(1024 * 1024)))

PROJECT_TEXT_EXTS = {
    ".js", ".mjs", ".cjs", ".ts", ".tsx", ".jsx",
    ".html", ".htm", ".css", ".scss", ".sass", ".json", ".json5",
    ".md", ".txt", ".glsl", ".vert", ".frag", ".wgsl", ".shader",
    ".yaml", ".yml", ".xml", ".svg", ".vue", ".svelte",
}

PROJECT_SKIP_DIRS = {
    ".git", "node_modules", "dist", "build", ".vite", ".cache", ".turbo",
    "coverage", ".next", ".nuxt", ".output", "vendor", "downloads",
    "models", "data", "logs", ".three-rag", ".pi", "__pycache__", ".venv",
}
