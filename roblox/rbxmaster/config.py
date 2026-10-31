"""Single configuration for the Roblox stack.

Every path is derived from `RBX_HOME` (the `roblox/` folder that holds this package),
never from cwd - the MCP servers are started by pi from an arbitrary directory, and a
relative path there resolves to the wrong tree.

The local model servers (`:8080` LLM, `:8081` embeddings, `:8083` reranker) are shared
with the Three.js / Godot / Unity stacks: this profile adds a corpus, not a runtime.
"""
from __future__ import annotations

import json
import os
import re
from pathlib import Path

# --- install root ------------------------------------------------------------
RBX_HOME: Path = Path(__file__).resolve().parent.parent            # .../3GS_Master/roblox
REPO_ROOT: Path = RBX_HOME.parent                                  # .../3GS_Master

DATA_DIR: Path = RBX_HOME / "data"
SQLITE_DIR: Path = DATA_DIR / "sqlite"
CACHE_DIR: Path = DATA_DIR / "cache"
RUN_DIR: Path = DATA_DIR / "run"
LOGS_DIR: Path = RBX_HOME / "logs"
TOOLS_DIR: Path = RBX_HOME / "tools"

KNOWLEDGE_DIR: Path = RBX_HOME / "knowledge"
# Guides, tutorials, platform concepts: split out of `llms-full.txt`.
OFFICIAL_DOCS_DIR: Path = KNOWLEDGE_DIR / "official_docs"
# Engine API Reference: one .md per class / datatype / enum / library (1210 pages).
ENGINE_API_DIR: Path = KNOWLEDGE_DIR / "engine_api"
# Open Cloud REST reference (`cloud/llms.txt`).
CLOUD_DOCS_DIR: Path = KNOWLEDGE_DIR / "cloud_docs"
# The curated Russian-language starter kit (Roblox_RAG_Starter_Kit), copied verbatim.
CURATED_KB_DIR: Path = KNOWLEDGE_DIR / "curated_kb"
COOKBOOK_DIR: Path = KNOWLEDGE_DIR / "cookbook"
TROUBLESHOOTING_DIR: Path = KNOWLEDGE_DIR / "troubleshooting"
ANTIPATTERNS_DIR: Path = KNOWLEDGE_DIR / "anti_patterns"
META_DIR: Path = KNOWLEDGE_DIR / "_meta"

STARTER_KIT_DIR: Path = REPO_ROOT / "Roblox_RAG_Starter_Kit"

LEXICAL_DB: Path = SQLITE_DIR / "lexical.db"
# Provenance of the last fetch: source URLs, timestamps, page counts, index hashes.
FETCH_META: Path = META_DIR / "fetch.json"

for _d in (DATA_DIR, SQLITE_DIR, CACHE_DIR, RUN_DIR, LOGS_DIR, KNOWLEDGE_DIR,
           OFFICIAL_DOCS_DIR, ENGINE_API_DIR, CLOUD_DOCS_DIR, CURATED_KB_DIR,
           COOKBOOK_DIR, TROUBLESHOOTING_DIR, ANTIPATTERNS_DIR, META_DIR):
    _d.mkdir(parents=True, exist_ok=True)

# --- pinned corpus version ---------------------------------------------------
# Roblox has no semantic platform version: the documentation is a rolling site and the
# Studio build is `version-<hash>`. So the "version" stamped on every chunk is the date
# the docs index was published (it carries `<!-- Last updated: ... -->`), plus the local
# Studio build hash when it can be resolved. A stale hit is then visible in the result.
DOCS_INDEX_URL = "https://create.roblox.com/docs/llms.txt"
DOCS_FULL_URL = "https://create.roblox.com/docs/llms-full.txt"
ENGINE_INDEX_URL = "https://create.roblox.com/docs/reference/engine/llms.txt"
CLOUD_INDEX_URL = "https://create.roblox.com/docs/cloud/llms.txt"
DOCS_BASE = "https://create.roblox.com"


def _fetch_meta() -> dict:
    try:
        return json.loads(FETCH_META.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}


_META = _fetch_meta()
# `2026-10-30T19:55:53Z` -> `2026-10-30`; falls back to a literal that says "unknown".
DOCS_VERSION = str(_META.get("docs_updated") or "").split("T")[0] or "unknown"
RBX_VERSION = os.environ.get("RBX_DOCS_VERSION", DOCS_VERSION)

# --- Roblox Studio -----------------------------------------------------------
# Studio installs per-user under `app/Versions/version-<hash>/` and the public build
# lands in `C:\Program Files\Roblox\Versions\version-<hash>/`. Either may be the newest.
STUDIO_EXE_NAME = "RobloxStudioBeta.exe"
STUDIO_MCP_EXE_NAME = "StudioMCP.exe"
STUDIO_CANDIDATES = [
    Path(r"E:\Programs\Roblox Studio\app\Versions"),
    Path(os.environ.get("LOCALAPPDATA", r"C:\Users\Public")) / "Roblox" / "Versions",
    Path(r"C:\Program Files\Roblox\Versions"),
    Path(r"C:\Program Files (x86)\Roblox\Versions"),
]
# The launcher Roblox itself documents (`cmd.exe /c %LOCALAPPDATA%\Roblox\mcp.bat`).
STUDIO_MCP_BAT = Path(os.environ.get("LOCALAPPDATA", r"C:\Users\Public")) / "Roblox" / "mcp.bat"


def _version_key(p: Path) -> tuple:
    """`version-7062aec9dbe74b14` -> sortable key.

    The hash is not numeric and not ordered, so recency comes from the directory mtime;
    the hash is only a tiebreaker that keeps the sort stable.
    """
    try:
        mtime = p.stat().st_mtime
    except OSError:
        mtime = 0.0
    return (mtime, p.name)


def _scan_studio(roots) -> Path | None:
    best: tuple[tuple, Path] | None = None
    for root in roots:
        try:
            if not root.is_dir():
                continue
        except OSError:
            continue
        for ver in root.glob("version-*"):
            exe = ver / STUDIO_EXE_NAME
            if not exe.is_file():
                continue
            key = _version_key(ver)
            if best is None or key > best[0]:
                best = (key, exe)
    return best[1] if best else None


def resolve_studio() -> Path | None:
    """Path to `RobloxStudioBeta.exe`, or None.

    Env wins, but only when the file actually exists - a stale variable pointing at a
    deleted build must not become "the editor is installed".
    """
    for key in ("ROBLOX_STUDIO", "RBX_STUDIO", "RBX_STUDIO_EXE"):
        raw = os.environ.get(key)
        if raw:
            p = Path(raw)
            if p.is_file():
                return p
    return _scan_studio(STUDIO_CANDIDATES)


def resolve_studio_mcp() -> Path | None:
    """Path to `StudioMCP.exe` (the built-in Studio MCP server binary), or None.

    Preferred order: the copy next to the resolved Studio build, then the documented
    `mcp.bat` launcher (a `.bat`, which needs `cmd.exe /c`), then any build on disk.
    """
    for key in ("ROBLOX_STUDIO_MCP", "RBX_STUDIO_MCP"):
        raw = os.environ.get(key)
        if raw:
            p = Path(raw)
            if p.is_file():
                return p
    studio = resolve_studio()
    if studio:
        sibling = studio.parent / STUDIO_MCP_EXE_NAME
        if sibling.is_file():
            return sibling
    if STUDIO_MCP_BAT.is_file():
        return STUDIO_MCP_BAT
    for root in STUDIO_CANDIDATES:
        try:
            for hit in sorted(root.glob(f"version-*/{STUDIO_MCP_EXE_NAME}")):
                if hit.is_file():
                    return hit
        except OSError:
            continue
    return None


def studio_build() -> str:
    """`version-<hash>` of the resolved Studio, or "" when Studio is not installed."""
    studio = resolve_studio()
    return studio.parent.name if studio else ""


STUDIO_EXE: Path | None = resolve_studio()
STUDIO_MCP: Path | None = resolve_studio_mcp()
STUDIO_BUILD = studio_build()

# --- local llama.cpp servers (shared with the Three.js / Godot / Unity stacks) -
LLM_HOST = os.environ.get("RBX_LLM_HOST", "127.0.0.1")
LLM_PORT = int(os.environ.get("RBX_LLM_PORT", "8080"))
LLM_BASE_URL = f"http://{LLM_HOST}:{LLM_PORT}/v1"
EMBED_HOST = os.environ.get("RBX_EMBED_HOST", "127.0.0.1")
EMBED_PORT = int(os.environ.get("RBX_EMBED_PORT", "8081"))
EMBED_BASE_URL = f"http://{EMBED_HOST}:{EMBED_PORT}"
EMBED_DIM = int(os.environ.get("RBX_EMBED_DIM", "1024"))          # bge-m3
EMBED_BATCH = int(os.environ.get("RBX_EMBED_BATCH", "32"))
EMBED_WORKERS = int(os.environ.get("RBX_EMBED_WORKERS", "4"))
# Cross-encoder reranker (:8083, `gs rerank`). Optional by design: if the port is
# silent the retriever keeps the RRF order and answers exactly as it did before.
# NOT :8082 - that is the Qwen2.5-VL vision server (`cmd\vlm.cmd`).
RERANK_HOST = os.environ.get("RBX_RERANK_HOST", "127.0.0.1")
RERANK_PORT = int(os.environ.get("RBX_RERANK_PORT", "8083"))
RERANK_BASE_URL = f"http://{RERANK_HOST}:{RERANK_PORT}"

# --- retrieval ---------------------------------------------------------------
DENSE_TOP_K = int(os.environ.get("RBX_DENSE_TOP_K", "20"))
LEXICAL_TOP_K = int(os.environ.get("RBX_LEXICAL_TOP_K", "20"))
FINAL_TOP_K = int(os.environ.get("RBX_FINAL_TOP_K", "8"))
RRF_K = int(os.environ.get("RBX_RRF_K", "60"))
# Deep shortlist on purpose: an exact API name such as `SetNetworkOwner` often sits far
# down the lexical list because the page mentions a dozen other members, and only the
# cross-encoder lifts the right member chunk to the top.
RERANK_ENABLED = os.environ.get("RBX_RERANK_ENABLED", "1").lower() not in ("0", "false", "no")
RERANK_TOP_K = int(os.environ.get("RBX_RERANK_TOP_K", "50"))
RERANK_MAX_CHARS = int(os.environ.get("RBX_RERANK_MAX_CHARS", "2000"))
RERANK_BATCH = int(os.environ.get("RBX_RERANK_BATCH", "32"))
RERANK_TIMEOUT = float(os.environ.get("RBX_RERANK_TIMEOUT", "60"))
MAX_INDEX_FILE_BYTES = int(os.environ.get("RBX_MAX_INDEX_FILE_BYTES", str(1024 * 1024)))

# --- the project the agent is pointed at --------------------------------------
# **One fact, one file.** `agent.cmd <project>` writes the active project to the SHARED
# `<repo>/data/active_project.txt`; the MCP servers read it back so a tool call that
# names only `project="MyGame"` lands in the same tree the agent is editing.
GAMES_DIR: Path = REPO_ROOT / "projects" / "games"
ACTIVE_PROJECT_FILE: Path = REPO_ROOT / "data" / "active_project.txt"
LEGACY_ACTIVE_PROJECT_FILE: Path = DATA_DIR / "active_project.txt"


def pointer_text() -> str:
    """The active-project pointer's contents (canonical file, then legacy)."""
    for f in (ACTIVE_PROJECT_FILE, LEGACY_ACTIVE_PROJECT_FILE):
        try:
            if f.exists():
                text = f.read_text(encoding="utf-8", errors="replace").strip()
                if text:
                    return text
        except OSError:
            continue
    return ""


def resolve_project(name_or_path: str | Path = "") -> Path:
    """The one definition of "the Roblox project directory".

    Accepts, in order: an existing absolute path; an existing path relative to cwd;
    a path relative to the repo root; a bare name under `projects/games/`.
    Env `ROBLOX_PROJECT` / `RBX_PROJECT` overrides the active-project file.

    A pointer is a hint, never a fact: `projects/games/` is user data, so a dead pointer
    raises instead of being resolved into a path that is not on disk.
    """
    explicit = str(name_or_path or "").strip().strip('"')
    raw = explicit
    if not raw:
        raw = (os.environ.get("ROBLOX_PROJECT") or os.environ.get("RBX_PROJECT") or "").strip()
    from_pointer = False
    if not raw:
        raw = pointer_text()
        from_pointer = bool(raw)
    if not raw:
        raise ValueError(
            "no project given, and data/active_project.txt is empty. Pass project=..., "
            "or start the agent with `agent.cmd <path-to-roblox-project>`."
        )
    p = Path(raw).expanduser()
    if p.is_absolute():
        if from_pointer and not p.is_dir():
            raise ValueError(
                "the active project is stale: data/active_project.txt points at %r, "
                "which does not exist - the project was deleted or renamed. Re-run "
                "`dev.cmd <name>` or `agent.cmd <project>` to point the system at a "
                "live project." % raw
            )
        return p.resolve()
    for candidate in (Path.cwd() / p, REPO_ROOT / p, GAMES_DIR / p):
        if candidate.is_dir():
            return candidate.resolve()
    if from_pointer:
        raise ValueError(
            "the active project is stale: data/active_project.txt points at %r, which "
            "does not exist - the project was deleted or renamed. Re-run `dev.cmd <name>` "
            "or `agent.cmd <project>` to point the system at a live project." % raw
        )
    if p.parent == Path("."):
        return (GAMES_DIR / p).resolve()
    return (REPO_ROOT / p).resolve()


def set_active_project(path: str | Path) -> Path:
    p = Path(path).expanduser().resolve()
    ACTIVE_PROJECT_FILE.parent.mkdir(parents=True, exist_ok=True)
    ACTIVE_PROJECT_FILE.write_text(str(p), encoding="utf-8")
    return p


# --- what gets indexed -------------------------------------------------------
# Luau source, Rojo project files, Wally/Rokit manifests, places and models.
PROJECT_TEXT_EXTS = {
    ".luau", ".lua", ".md", ".txt",
    ".json", ".jsonc", ".toml", ".yaml", ".yml", ".xml",
    ".rbxlx", ".rbxmx", ".rbxmk",
}
PROJECT_SKIP_DIRS = {
    ".git", ".vs", ".idea", "node_modules", "__pycache__", ".venv", ".pi",
    "data", "models", "bin", "logs", "downloads", ".workbuddy-ai",
    # Wally's vendored dependencies: source, but not *our* source - it would drown the
    # project corpus in third-party modules the RAG already has better docs for.
    "Packages", "ServerPackages", "DevPackages",
    ".rbxmaster_backups",
}

# Chunk headers carry the version so a stale hit is visible in the result.
RBX_FRAMEWORK_TAG = "roblox"


def corpus_stats() -> dict:
    """File counts per corpus directory - used by doctor and by `rbx_rag_status`."""
    out = {}
    for name, root in SOURCE_DIRS.items():
        try:
            out[name] = sum(1 for p in root.rglob("*") if p.is_file())
        except OSError:
            out[name] = 0
    return out


SOURCE_DIRS = {
    "official_docs": OFFICIAL_DOCS_DIR,
    "engine_api": ENGINE_API_DIR,
    "cloud_docs": CLOUD_DOCS_DIR,
    "curated_kb": CURATED_KB_DIR,
    "cookbook": COOKBOOK_DIR,
    "troubleshooting": TROUBLESHOOTING_DIR,
    "anti_patterns": ANTIPATTERNS_DIR,
}


def _engine_from_project(path: Path | None) -> str:
    if not path:
        return ""
    try:
        return json.loads((path / "engine.json").read_text(encoding="utf-8")).get("engine", "")
    except (OSError, ValueError):
        return ""


ENGINE_OF_ACTIVE_PROJECT = _engine_from_project(
    Path(pointer_text()).resolve() if pointer_text() else None)
