"""Single configuration for the Unity stack.

Every path is derived from `UNIM_HOME` (the `unity/` folder that holds this package),
never from cwd - the MCP servers are started by pi from an arbitrary directory, and a
relative path there resolves to the wrong tree.

The three numbers that must agree (see docs/ARCHITECTURE.md "Контекстное
бюджетирование") are owned by the shared llama.cpp servers, not by this stack: the
Unity profile reuses the same `:8080` LLM and `:8081` embeddings as Three and Godot.
"""
from __future__ import annotations

import os
import re
from pathlib import Path

# --- install root ------------------------------------------------------------
UNIM_HOME: Path = Path(__file__).resolve().parent.parent          # .../3GS_Master/unity
REPO_ROOT: Path = UNIM_HOME.parent                                 # .../3GS_Master

BIN_DIR: Path = UNIM_HOME / "bin"
DATA_DIR: Path = UNIM_HOME / "data"
SQLITE_DIR: Path = DATA_DIR / "sqlite"
CACHE_DIR: Path = DATA_DIR / "cache"
RUN_DIR: Path = DATA_DIR / "run"
LOGS_DIR: Path = UNIM_HOME / "logs"
TOOLS_DIR: Path = UNIM_HOME / "tools"

KNOWLEDGE_DIR: Path = UNIM_HOME / "knowledge"
OFFICIAL_DOCS_DIR: Path = KNOWLEDGE_DIR / "official_docs"          # Manual + ScriptReference (HTML)
OFFICIAL_SOURCE_DIR: Path = KNOWLEDGE_DIR / "official_source"      # UnityCsReference (C#)
PACKAGES_DOCS_DIR: Path = KNOWLEDGE_DIR / "packages_docs"          # package manuals (HTML)
COOKBOOK_DIR: Path = KNOWLEDGE_DIR / "cookbook"
RECIPES_DIR: Path = KNOWLEDGE_DIR / "recipes"
TROUBLESHOOTING_DIR: Path = KNOWLEDGE_DIR / "troubleshooting"
ANTIPATTERNS_DIR: Path = KNOWLEDGE_DIR / "anti_patterns"

LEXICAL_DB: Path = SQLITE_DIR / "lexical.db"
# ACTIVE_PROJECT_FILE is defined further down, next to GAMES_DIR ("the Unity project
# the agent is pointed at"): it is SHARED system state, not a per-stack file.

for _d in (DATA_DIR, SQLITE_DIR, CACHE_DIR, RUN_DIR, LOGS_DIR, KNOWLEDGE_DIR,
           OFFICIAL_DOCS_DIR, OFFICIAL_SOURCE_DIR, PACKAGES_DOCS_DIR,
           COOKBOOK_DIR, RECIPES_DIR, TROUBLESHOOTING_DIR, ANTIPATTERNS_DIR):
    _d.mkdir(parents=True, exist_ok=True)

# --- pinned engine version ---------------------------------------------------
# The corpus and the `unity_version` stamped on every chunk come from here. Bumping
# it invalidates every chunk header -> run `unity-index.cmd --force`.
#
# `UNITY_DOC_VERSION` is the *documentation* version path on docs.unity3d.com; the
# editor build is `UNITY_EDITOR_VERSION`. They track each other but are not the same
# string (docs use the "6000.3" line, the editor a full "6000.3.26f1" build).
UNITY_DOC_VERSION = os.environ.get("UNITY_DOC_VERSION", "6000.3")
UNITY_EDITOR_VERSION = os.environ.get("UNITY_EDITOR_VERSION", "6000.3.26f1")
UNITY_VERSION = UNITY_DOC_VERSION

DOCS_BASE = os.environ.get(
    "UNITY_DOCS_BASE", f"https://docs.unity3d.com/{UNITY_DOC_VERSION}/Documentation")
# UnityCsReference branch matching the docs line (Unity publishes `6000.3` branches).
UNITY_CSREF_REF = os.environ.get("UNITY_CSREF_REF", "6000.3")

# --- local llama.cpp servers (shared with the Three.js / Godot stacks) -------
LLM_HOST = os.environ.get("UNIM_LLM_HOST", "127.0.0.1")
LLM_PORT = int(os.environ.get("UNIM_LLM_PORT", "8080"))
LLM_BASE_URL = f"http://{LLM_HOST}:{LLM_PORT}/v1"
EMBED_HOST = os.environ.get("UNIM_EMBED_HOST", "127.0.0.1")
EMBED_PORT = int(os.environ.get("UNIM_EMBED_PORT", "8081"))
EMBED_BASE_URL = f"http://{EMBED_HOST}:{EMBED_PORT}"
EMBED_DIM = int(os.environ.get("UNIM_EMBED_DIM", "1024"))       # bge-m3
EMBED_BATCH = int(os.environ.get("UNIM_EMBED_BATCH", "32"))
EMBED_WORKERS = int(os.environ.get("UNIM_EMBED_WORKERS", "4"))
# Cross-encoder reranker (:8083, `gs rerank`). Optional by design: if the port is
# silent the retriever keeps the RRF order and answers exactly as it did before.
# NOT :8082 - that is the Qwen2.5-VL vision server (`cmd\vlm.cmd`).
RERANK_HOST = os.environ.get("UNIM_RERANK_HOST", "127.0.0.1")
RERANK_PORT = int(os.environ.get("UNIM_RERANK_PORT", "8083"))
RERANK_BASE_URL = f"http://{RERANK_HOST}:{RERANK_PORT}"

# --- retrieval ---------------------------------------------------------------
DENSE_TOP_K = int(os.environ.get("UNIM_DENSE_TOP_K", "20"))
LEXICAL_TOP_K = int(os.environ.get("UNIM_LEXICAL_TOP_K", "20"))
FINAL_TOP_K = int(os.environ.get("UNIM_FINAL_TOP_K", "8"))
RRF_K = int(os.environ.get("UNIM_RRF_K", "60"))
# Reranking. TOP_K=50 is deliberate: measured on this corpus, the best chunk for
# "how do I add force to a rigidbody every frame" sat at lexical rank 46 and only the
# cross-encoder lifted it to 5 - a shortlist of 20 would have discarded the answer
# before the reranker ever saw it. MAX_CHARS is clipped because llama.cpp rejects a
# single sequence longer than one slot's context (`-c 8192 -np 4` = 2048 per slot).
RERANK_ENABLED = os.environ.get("UNIM_RERANK_ENABLED", "1").lower() not in ("0", "false", "no")
RERANK_TOP_K = int(os.environ.get("UNIM_RERANK_TOP_K", "50"))
RERANK_MAX_CHARS = int(os.environ.get("UNIM_RERANK_MAX_CHARS", "2000"))
RERANK_BATCH = int(os.environ.get("UNIM_RERANK_BATCH", "32"))
RERANK_TIMEOUT = float(os.environ.get("UNIM_RERANK_TIMEOUT", "60"))
MAX_INDEX_FILE_BYTES = int(os.environ.get("UNIM_MAX_INDEX_FILE_BYTES", str(1024 * 1024)))

# --- Unity toolchain ---------------------------------------------------------
# The editor is what compiles C# and runs `-executeMethod`; the CLI (`unity.exe`
# 1.0.0-beta) is a separate binary that drives Hub installs, projects and the
# editor bridge. They are found independently and either may be missing.
UNITY_EDITOR_CANDIDATES = [
    # Unity Hub keeps editors under `<hub>\Unity\Editors\<version>\Editor\Unity.exe`
    # (this machine: E:\Programs\Unity Hub\Unity\Editors\6000.3.26f1\...).
    Path(r"E:\Programs\Unity Hub\Unity\Editors") / UNITY_EDITOR_VERSION / "Editor" / "Unity.exe",
    Path(r"C:\Program Files\Unity\Hub\Editor") / UNITY_EDITOR_VERSION / "Editor" / "Unity.exe",
]
UNITY_EDITOR_SEARCH_ROOTS = [
    Path(r"E:\Programs\Unity Hub\Unity\Editors"),
    Path(r"C:\Program Files\Unity\Hub\Editor"),
]
UNITY_CLI_CANDIDATES = [
    Path(os.environ.get("LOCALAPPDATA", r"C:\Users\Public")) / "Unity" / "bin" / "unity.exe",
    Path(r"E:\Programs\Unity Hub\resources\unity.exe"),
]
# Hub's editor install root, for `unity editors default <ver>` hints.
UNITY_EDITORS_INSTALL_ROOT = Path(
    os.environ.get("UNITY_EDITORS_ROOT", r"E:\Programs\Unity Hub\Unity\Editors"))


def _first_existing(paths) -> Path | None:
    for p in paths:
        try:
            if p.exists():
                return p
        except OSError:
            continue
    return None


def _scan_editor(root: Path) -> Path | None:
    """Highest `<version>/Editor/Unity.exe` under an editors root."""
    if not root or not root.exists():
        return None
    best: tuple[tuple[int, ...], Path] | None = None
    for exe in root.glob("*/Editor/Unity.exe"):
        ver = exe.parent.parent.name
        nums = tuple(int(x) for x in re.findall(r"\d+", ver)[:4]) or (0,)
        if best is None or nums > best[0]:
            best = (nums, exe)
    return best[1] if best else None


def resolve_unity_editor() -> Path | None:
    """Path to `Unity.exe` (the editor), or None.

    Env `UNITY_EDITOR` / `UNITY_PATH` win, but only when the file actually exists -
    this machine has a stale `GODOT_PATH`-style variable pointing at a deleted build,
    and blindly trusting it breaks everything downstream.
    """
    for key in ("UNITY_EDITOR", "UNITY_PATH", "UNIM_UNITY"):
        raw = os.environ.get(key)
        if raw:
            p = Path(raw)
            if p.is_file():
                return p
    found = _first_existing(UNITY_EDITOR_CANDIDATES)
    if found:
        return found
    return _scan_editor(UNITY_EDITORS_INSTALL_ROOT) or _scan_editor(UNITY_EDITOR_SEARCH_ROOTS[1])


def resolve_unity_cli() -> Path | None:
    """Path to the standalone Unity CLI (`unity.exe` 1.0.0-beta), or None."""
    for key in ("UNITY_CLI", "UNIM_UNITY_CLI"):
        raw = os.environ.get(key)
        if raw:
            p = Path(raw)
            if p.is_file():
                return p
    return _first_existing(UNITY_CLI_CANDIDATES)


UNITY_EDITOR: Path | None = resolve_unity_editor()
UNITY_CLI: Path | None = resolve_unity_cli()

# --- Blender: DCC-шаг, которого у пайплайна ассетов нет -----------------------
# ComfyUI отдаёт сырой GLB и на этом останавливается. Всё, что требует настоящего
# *редактирования* меша, идёт через Blender в headless-режиме
# (`blender --background --python script.py`): авто-риггинг + ретаргет анимации
# (Kimodo / Mixamo / ARDY), quad-ретопология и чистка UV, конвертация
# GLB <-> FBX <-> OBJ, перебейк текстур, headless-рендеры превью.
#
# Blender НЕ резидентная модель и НЕ участвует в арбитраже VRAM: как Real-ESRGAN,
# держит сотни МБ, поэтому headless-прогон может стоять рядом с ComfyUI.
# На этой машине: `E:\Programs\Blender\blender.exe` (5.2.2 LTS).
BLENDER_CANDIDATES = [
    Path(r"E:\Programs\Blender\blender.exe"),
]
BLENDER_SEARCH_ROOTS = [
    Path(r"E:\Programs\Blender"),
    Path(r"C:\Program Files\Blender Foundation"),
]
BLENDER_VERSION = os.environ.get("UNIM_BLENDER_VERSION", "5.2")


def _first_blender() -> Path | None:
    found = _first_existing(BLENDER_CANDIDATES)
    if found:
        return found
    for root in BLENDER_SEARCH_ROOTS:
        if not root.is_dir():
            continue
        for hit in sorted(root.glob("blender.exe")) + sorted(root.glob("*/blender.exe")):
            if hit.is_file():
                return hit
    return None


def resolve_blender() -> Path | None:
    """Путь к `blender.exe`, либо None. Env побеждает, но только если файл реально есть."""
    for key in ("UNIM_BLENDER_EXE", "BLENDER_EXE", "BLENDER_PATH"):
        raw = os.environ.get(key)
        if raw:
            p = Path(raw)
            if p.is_file():
                return p
    return _first_blender()


BLENDER_EXE: Path | None = resolve_blender()
BLENDER_DIR: Path | None = BLENDER_EXE.parent if BLENDER_EXE else None

# --- the Unity project the agent is pointed at --------------------------------
# **One fact, one file.** `agent.cmd <project>` writes the active project to the
# SHARED `<repo>/data/active_project.txt`; the MCP servers read it back so a tool call
# that names only `project="MyGame"` lands in the same tree the agent is editing.
#
# This used to point at `unity/data/active_project.txt`, which nothing ever writes
# (the only writer is `set_active_project`, and no caller invokes it) - so a Unity
# agent silently failed to see the project the launcher had just recorded, fell back
# to "." and reported "active_project.txt is empty" while the canonical file in fact
# held a path. Godot had the identical defect and was fixed the same way: read the
# canonical file, keep the old per-stack path only as a legacy fallback.
GAMES_DIR: Path = REPO_ROOT / "projects" / "games"
ACTIVE_PROJECT_FILE: Path = REPO_ROOT / "data" / "active_project.txt"
LEGACY_ACTIVE_PROJECT_FILE: Path = DATA_DIR / "active_project.txt"


def pointer_text() -> str:
    """The active-project pointer's contents (canonical file, then legacy).

    Public because `tools/index.py` needs the SAME two-file resolution when it adopts
    the active project; reading `ACTIVE_PROJECT_FILE` directly would silently skip the
    legacy fallback and make the CLI disagree with the MCP server about which project
    is active.
    """
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
    """The one definition of "the Unity project directory".

    Accepts, in order: an existing absolute path; an existing path relative to cwd;
    a path relative to the repo root; a bare name under `projects/games/`.
    Env `UNITY_PROJECT` / `UNIM_PROJECT` overrides the active-project file.

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
        still assumed to be a game that may not exist yet, while a relative path that
        already carries directories is treated as repo-relative and is NOT joined onto
        `GAMES_DIR` a second time.

    Callers that must tolerate "no project" catch `ValueError` (`unity/tools/doctor.py`).
    """
    explicit = str(name_or_path or "").strip().strip('"')
    raw = explicit
    if not raw:
        raw = (os.environ.get("UNITY_PROJECT") or os.environ.get("UNIM_PROJECT") or "").strip()
    from_pointer = False
    if not raw:
        raw = pointer_text()
        from_pointer = bool(raw)
    if not raw:
        raise ValueError(
            "no project given, and data/active_project.txt is empty. Pass project=..., "
            "or start the agent with `agent.cmd <path-to-unity-project>`."
        )
    p = Path(raw).expanduser()
    if p.is_absolute():
        # An explicit absolute path is the caller's business - it may be a project
        # outside `projects/games/` that is about to be created. From the POINTER it is
        # system state about user data, so a vanished target has to be reported.
        if from_pointer and not p.is_dir():
            raise ValueError(
                "the active project is stale: data/active_project.txt points at %r, "
                "which does not exist - the project was deleted or renamed. Re-run "
                "`dev.cmd <name>` or `agent.cmd <project>` to point the system at a "
                "live project." % raw
            )
        return p.resolve()
    # `is_dir`, not `exists`: the result is called "the project directory", and a file
    # that happens to carry the name must not shadow it.
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
        # A bare name is the ONE case where GAMES_DIR is the right parent: the project
        # may legitimately not exist yet.
        return (GAMES_DIR / p).resolve()
    return (REPO_ROOT / p).resolve()


def set_active_project(path: str | Path) -> Path:
    p = Path(path).expanduser().resolve()
    ACTIVE_PROJECT_FILE.parent.mkdir(parents=True, exist_ok=True)
    ACTIVE_PROJECT_FILE.write_text(str(p), encoding="utf-8")
    return p


# --- what gets indexed -------------------------------------------------------
# Source corpora are narrow on purpose; `project` keeps the wide Unity set.
PROJECT_TEXT_EXTS = {
    ".cs", ".shader", ".compute", ".cginc", ".hlsl", ".glsl",
    ".asmdef", ".asmref", ".json", ".md", ".txt",
    ".uxml", ".uss", ".unity", ".prefab", ".asset", ".mat", ".controller",
    ".yaml", ".yml", ".xml", ".meta",
}
PROJECT_SKIP_DIRS = {
    ".git", ".vs", ".idea", "Library", "Temp", "Obj", "obj", "Logs", "UserSettings",
    "Build", "Builds", "build", "node_modules", "__pycache__", ".venv", ".pi",
    "data", "models", "bin", "downloads", ".unim", ".gdmaster_backups",
    ".workbuddy-ai", "PackageCache",
}

# Chunk headers carry the version so a stale hit is visible in the result.
UNITY_FRAMEWORK_TAG = "unity"
