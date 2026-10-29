"""Единая конфигурация gdmaster.

Все пути выводятся от GDM_HOME (корень установки агента), а не от cwd —
серверы MCP запускаются pi из произвольного каталога.
"""
from __future__ import annotations

import os
from pathlib import Path

# --- корень установки агента -------------------------------------------------
GDM_HOME: Path = Path(__file__).resolve().parent.parent

BIN_DIR: Path = GDM_HOME / "bin"
LLAMA_DIR: Path = BIN_DIR / "llama"
MODELS_DIR: Path = GDM_HOME / "models"
DATA_DIR: Path = GDM_HOME / "data"
QDRANT_DIR: Path = DATA_DIR / "qdrant"
SQLITE_DIR: Path = DATA_DIR / "sqlite"
CACHE_DIR: Path = DATA_DIR / "cache"
KNOWLEDGE_DIR: Path = GDM_HOME / "knowledge"
GODOT_DOCS_DIR: Path = KNOWLEDGE_DIR / "godot_docs"
COOKBOOK_DIR: Path = KNOWLEDGE_DIR / "cookbook"
TROUBLESHOOTING_DIR: Path = KNOWLEDGE_DIR / "troubleshooting"
ANTIPATTERNS_DIR: Path = KNOWLEDGE_DIR / "anti_patterns"
# Знания о внешних ассетах: источники, лицензии, manifest, политика, workflow.
# Это ЗНАНИЯ, а не возможность скачивать — сетевого инструмента в allowlist нет.
EXTERNAL_ASSETS_DIR: Path = KNOWLEDGE_DIR / "external_assets"
LOGS_DIR: Path = GDM_HOME / "logs"
TOOLS_DIR: Path = GDM_HOME / "tools"
SCRIPTS_DIR: Path = GDM_HOME / "scripts"
RUN_DIR: Path = DATA_DIR / "run"

MANIFEST_PATH: Path = DATA_DIR / "manifest.json"
LEXICAL_DB: Path = SQLITE_DIR / "lexical.db"

for _d in (
    BIN_DIR, LLAMA_DIR, MODELS_DIR, DATA_DIR, QDRANT_DIR, SQLITE_DIR,
    CACHE_DIR, KNOWLEDGE_DIR, GODOT_DOCS_DIR, COOKBOOK_DIR,
    TROUBLESHOOTING_DIR, ANTIPATTERNS_DIR, EXTERNAL_ASSETS_DIR, LOGS_DIR, RUN_DIR,
):
    _d.mkdir(parents=True, exist_ok=True)

# --- модели ------------------------------------------------------------------
LLM_GGUF: Path = MODELS_DIR / "Qwen_Qwen3.5-9B-Q4_K_M.gguf"
EMBED_GGUF: Path = MODELS_DIR / "bge-m3-q4_k_m.gguf"

LLAMA_SERVER: Path = LLAMA_DIR / "llama-server.exe"

# --- сеть (только loopback) --------------------------------------------------
LLM_HOST = os.environ.get("GDM_LLM_HOST", "127.0.0.1")
LLM_PORT = int(os.environ.get("GDM_LLM_PORT", "8080"))
EMBED_HOST = os.environ.get("GDM_EMBED_HOST", "127.0.0.1")
EMBED_PORT = int(os.environ.get("GDM_EMBED_PORT", "8081"))

LLM_BASE_URL = f"http://{LLM_HOST}:{LLM_PORT}/v1"
EMBED_BASE_URL = f"http://{EMBED_HOST}:{EMBED_PORT}"

# Кросс-энкодер-реранкер (:8083, `gs rerank`). Опционален по замыслу: если порт молчит,
# ретривер остаётся на порядке RRF и отвечает ровно как раньше.
# НЕ :8082 - там сервер зрения Qwen2.5-VL (`cmd\vlm.cmd`).
RERANK_HOST = os.environ.get("GDM_RERANK_HOST", "127.0.0.1")
RERANK_PORT = int(os.environ.get("GDM_RERANK_PORT", "8083"))
RERANK_BASE_URL = f"http://{RERANK_HOST}:{RERANK_PORT}"

# ВАЖНО: это значение должно совпадать с -c в serve-llm.cmd, contextWindow в
# pi-home/models.json и вытекающим из reserveTokens порогом компакции. pi НЕ
# спрашивает сервер — он считает порог сам, поэтому расхождение даёт компакцию
# не в тот момент. Текущая связка: 65536 / 65536 / reserveTokens 16384.
LLM_CTX = int(os.environ.get("GDM_LLM_CTX", "65536"))
LLM_NGL = os.environ.get("GDM_LLM_NGL", "999")

# --- approval policy (спека §37) ---------------------------------------------
# Удаление поддерева больше N узлов считается высокорисковой операцией
# и требует явного confirm=True от агента.
APPROVAL_SUBTREE_NODES = int(os.environ.get("GDM_APPROVAL_SUBTREE_NODES", "5"))

# --- Blender: DCC-шаг, которого у пайплайна ассетов нет -----------------------
# ComfyUI отдаёт сырой GLB и на этом останавливается. Всё, что требует настоящего
# *редактирования* меша, идёт через Blender в headless-режиме
# (`blender --background --python script.py`):
#
#   * авто-риггинг + ретаргет анимации (Kimodo / Mixamo / ARDY на наш меш)
#   * quad-ретопология и чистка UV под game-ready low-poly
#   * конвертация GLB <-> FBX <-> OBJ, упаковка GLB, проходы Draco/gltfpack
#   * перебейк текстур (albedo / normal / AO)
#   * headless-рендеры turntable для превью
#
# Blender НЕ резидентная модель и НЕ участвует в арбитраже VRAM: как Real-ESRGAN,
# он держит сотни МБ, поэтому headless-прогон может стоять рядом с ComfyUI.
# На этой машине: `E:\Programs\Blender\blender.exe` (5.2.2 LTS).
BLENDER_CANDIDATES = [
    Path(r"E:\Programs\Blender\blender.exe"),
]
BLENDER_SEARCH_ROOTS = [
    Path(r"E:\Programs\Blender"),
    Path(r"C:\Program Files\Blender Foundation"),
]
BLENDER_VERSION = os.environ.get("GDM_BLENDER_VERSION", "5.2")


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
        for hit in sorted(root.glob("blender.exe")) + sorted(root.glob("*/blender.exe")):
            if hit.is_file():
                return hit
    return None


def resolve_blender() -> "Path | None":
    """Путь к `blender.exe`, либо None. Env побеждает, но только если файл реально есть."""
    for key in ("GDM_BLENDER_EXE", "BLENDER_EXE", "BLENDER_PATH"):
        raw = os.environ.get(key)
        if raw:
            p = Path(raw)
            if p.is_file():
                return p
    return _first_blender()


BLENDER_EXE: "Path | None" = resolve_blender()
BLENDER_DIR: "Path | None" = BLENDER_EXE.parent if BLENDER_EXE else None

# --- embedding ---------------------------------------------------------------
EMBED_DIM = 1024
EMBED_BATCH = int(os.environ.get("GDM_EMBED_BATCH", "32"))
# llama-server поднимается с -c 32768 и 4 слотами -> параллельные запросы
EMBED_WORKERS = int(os.environ.get("GDM_EMBED_WORKERS", "4"))

# --- retrieval ---------------------------------------------------------------
DENSE_TOP_K = int(os.environ.get("GDM_DENSE_TOP_K", "20"))
LEXICAL_TOP_K = int(os.environ.get("GDM_LEXICAL_TOP_K", "20"))
FINAL_TOP_K = int(os.environ.get("GDM_FINAL_TOP_K", "8"))
RRF_K = 60  # константа Reciprocal Rank Fusion

# --- реранк ------------------------------------------------------------------
# TOP_K=50 не случайно: на корпусе Unity лучший чанк по запросу стоял на 46-м месте
# в лексике, и поднять его смог только кросс-энкодер — короткий список из 20 выбросил
# бы ответ ещё до того, как реранкер его увидел. MAX_CHARS обрезается потому, что
# llama.cpp отбивает одну последовательность длиннее контекста одного слота.
RERANK_ENABLED = os.environ.get("GDM_RERANK_ENABLED", "1").lower() not in ("0", "false", "no")
RERANK_TOP_K = int(os.environ.get("GDM_RERANK_TOP_K", "50"))
RERANK_MAX_CHARS = int(os.environ.get("GDM_RERANK_MAX_CHARS", "2000"))
RERANK_BATCH = int(os.environ.get("GDM_RERANK_BATCH", "32"))
RERANK_TIMEOUT = float(os.environ.get("GDM_RERANK_TIMEOUT", "60"))

# --- целевой Godot-проект ----------------------------------------------------
# GDM_HOME - это `godot/`, поэтому корень репозитория на уровень выше, а проекты
# пользователя лежат в ОБЩЕМ `projects/games/` репозитория (как у threejs и unity).
# Путь к проектам задан ещё и в `cmd/_env.cmd` (GS_GAMES) - менять синхронно.
REPO_ROOT: Path = GDM_HOME.parent
GAMES_DIR: Path = Path(os.environ.get("GDM_GAMES_DIR", REPO_ROOT / "projects" / "games"))

# **ОДИН факт - ОДИН файл.** `agent.cmd` пишет активный проект в общий
# `<repo>/data/active_project.txt` - и раньше только threejs его и читал, потому что
# godot и unity смотрели в СВОИ `godot/data/` и `unity/data/`. Эти файлы никто не
# пишет (единственный писатель - `set_active_project`, а его никто не вызывает),
# поэтому godot-агент молча не видел проект, записанный запускателем, и падал на
# "." в вызывающих. Читаем канонический файл, а свой прежний - только как legacy.
ACTIVE_PROJECT_FILE: Path = REPO_ROOT / "data" / "active_project.txt"
LEGACY_ACTIVE_PROJECT_FILE: Path = DATA_DIR / "active_project.txt"


def pointer_text() -> str:
    """Содержимое указателя активного проекта (канонический файл, затем legacy).

    Публичная: CLI-инструментам нужен ТОТ ЖЕ двухфайловый резолв, что и MCP-серверу —
    прямое чтение `ACTIVE_PROJECT_FILE` молча пропустило бы legacy-фолбэк и разошлось бы
    с сервером в том, какой проект активен.
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
    """Единственное определение «каталога Godot-проекта».

    Порядок: существующий абсолютный путь; существующий путь относительно cwd; путь
    относительно корня репозитория; голое имя в `projects/games/`.
    Env `GDM_PROJECT` / `GODOT_PROJECT_PATH` перекрывает файл активного проекта.

    **Указатель - это подсказка, а не факт.** `projects/games/` - данные пользователя:
    проекты создаются, переименовываются и удаляются, а `data/active_project.txt`
    продолжает называть старый. Поэтому подсказка разрешается на КАЖДОМ вызове и
    выдумать путь нельзя:

      * абсолютный путь возвращается как есть - это явное дело вызывающего;
      * относительный пробуется против cwd, затем корня репозитория, затем
        `projects/games/`;
      * если на диске ничего не совпало и значение пришло из УКАЗАТЕЛЯ, указатель
        устарел -> `ValueError` с его именем. Раньше здесь стоял
        `Path(raw).resolve()`, то есть путь разрешался относительно cwd процесса:
        MCP-сервер запускается pi из произвольного каталога, поэтому относительный
        указатель молча превращался в несуществующий путь у чужого каталога;
      * если ничего не совпало и значение передано ЯВНО, голое имя по-прежнему
        считается проектом, который может быть ещё не создан, а относительный путь с
        каталогами трактуется как путь от корня репозитория и НЕ приклеивается к
        `GAMES_DIR` второй раз.

    Кто обязан терпеть «проекта нет» - ловит `ValueError` (см. `godot_project_root`).
    """
    explicit = str(name_or_path or "").strip().strip('"')
    raw = explicit
    if not raw:
        raw = (os.environ.get("GDM_PROJECT") or os.environ.get("GODOT_PROJECT_PATH") or "").strip()
    from_pointer = False
    if not raw:
        raw = pointer_text()
        from_pointer = bool(raw)
    if not raw:
        raise ValueError(
            "проект не задан, и data/active_project.txt пуст. Передай project=... или "
            "запусти агента через `agent.cmd <path-to-godot-project>`."
        )
    p = Path(raw).expanduser()
    if p.is_absolute():
        # Явный абсолютный путь - дело вызывающего (проект может лежать вне
        # `projects/games/` и быть ещё не созданным). Из УКАЗАТЕЛЯ это состояние
        # системы о данных пользователя, поэтому исчезнувшую цель нужно назвать.
        if from_pointer and not p.is_dir():
            raise ValueError(
                "активный проект устарел: data/active_project.txt указывает на %r, "
                "которого нет - проект удалён или переименован. Перезапусти "
                "`dev.cmd <имя>` или `agent.cmd <проект>`." % raw
            )
        return p.resolve()
    # `is_dir`, а не `exists`: результат называется «каталог проекта», и файл с таким
    # именем не должен его подменять.
    for candidate in (Path.cwd() / p, REPO_ROOT / p, GAMES_DIR / p):
        if candidate.is_dir():
            return candidate.resolve()
    if from_pointer:
        raise ValueError(
            "активный проект устарел: data/active_project.txt указывает на %r, "
            "которого нет - проект удалён или переименован. Перезапусти "
            "`dev.cmd <имя>` или `agent.cmd <проект>`." % raw
        )
    if p.parent == Path("."):
        # Голое имя - ЕДИНСТВЕННЫЙ случай, когда GAMES_DIR правильный родитель:
        # проекта может ещё не быть, его создаст `newgame.cmd <имя>`.
        return (GAMES_DIR / p).resolve()
    return (REPO_ROOT / p).resolve()


def godot_project_root() -> Path | None:
    """Корень Godot-проекта или None.

    Приоритет: env GDM_PROJECT / GODOT_PROJECT_PATH, затем
    data/active_project.txt (его пишет agent.cmd при запуске).
    Файл нужен потому, что MCP-серверы запускаются pi как дочерние
    процессы, и прокидывать env через конфиг pi ненадёжно.

    Осталась ради вызывающих, для которых «проекта нет» - нормальное состояние
    (`runner.py` подставляет "."). Разрешение пути при этом то же самое, что у
    `resolve_project` - без него относительный указатель разрешался от cwd процесса.
    """
    try:
        return resolve_project("")
    except ValueError:
        return None


def set_active_project(path: str | Path) -> Path:
    p = Path(path).expanduser().resolve()
    ACTIVE_PROJECT_FILE.parent.mkdir(parents=True, exist_ok=True)
    ACTIVE_PROJECT_FILE.write_text(str(p), encoding="utf-8")
    return p


# --- Godot -------------------------------------------------------------------
GODOT_CANDIDATES = [
    GDM_HOME / "bin" / "godot" / "Godot_v4.7.2-stable_win64.exe",
    Path(r"E:\Programs\distr\Godot_v4.7.2-stable_win64.exe"),
    Path(r"C:\Program Files\Godot\Godot_v4.7.2-stable_win64.exe"),
]


def _resolve_godot() -> Path:
    """Первый существующий кандидат.

    env GODOT_PATH уважается, но только если файл реально есть: в этой машине
    он выставлен в несуществующий путь, и слепое доверие ломает всё.
    """
    for env_key in ("GDM_GODOT", "GODOT_PATH"):
        raw = os.environ.get(env_key)
        if raw:
            p = Path(raw)
            if p.exists():
                return p
    for p in GODOT_CANDIDATES:
        if p.exists():
            return p
    return GODOT_CANDIDATES[1]  # вернуть «эталонный» путь, чтобы ошибка была понятной


GODOT_EXE: Path = _resolve_godot()

ENGINE_VERSION = "4.7"

# --- индексируемые расширения ------------------------------------------------
PROJECT_TEXT_EXTS = {
    ".gd", ".tscn", ".tres", ".godot", ".gdshader", ".shader",
    ".md", ".json", ".cfg", ".txt", ".cs", ".gdshaderinc",
}

PROJECT_SKIP_DIRS = {
    ".git", ".import", ".godot", ".cache", "tmp", "build",
    "exports", "addons", "node_modules", "__pycache__", ".pi",
    "data", ".venv", "downloads", "models", "bin", "logs",
}

# файлы больше этого размера не индексируются
MAX_INDEX_FILE_BYTES = 512 * 1024
