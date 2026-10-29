"""Godot-only MCP-сервер: собственный, узкий tool surface.

Почему свой, а не hybridindie/godot-mcp (193 инструмента):
локальная 9B-модель деградирует на большом tool surface — растёт доля
невалидных вызовов. Здесь ~16 инструментов, каждый с точной семантикой,
project-scoped и с audit log. Всё, что делает мутации, проходит через
сам Godot (headless SceneTree-скрипты), а не через текстовую правку .tscn.

Границы (жёсткие):
  * любой путь нормализуется и обязан лежать внутри корня Godot-проекта;
  * запись разрешена только для Godot-текстовых расширений;
  * никакого shell, сети, чтения вне проекта.
"""
from __future__ import annotations

import json
import re
import shutil
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from mcp.server.fastmcp import FastMCP  # noqa: E402

from gdmaster import config  # noqa: E402
from gdmaster.godot import play as gplay  # noqa: E402
from gdmaster.godot import project_settings as gproj  # noqa: E402
from gdmaster.godot import scene as gscene  # noqa: E402
from gdmaster.godot.lint import lint_gdscript  # noqa: E402
from gdmaster.godot.paths import (  # noqa: E402
    PathDenied, WRITABLE_EXTS, guard_extension, normalize, project_root, res_path, resolve,
)
from gdmaster.godot.runner import GodotRunner  # noqa: E402
from gdmaster.rag.chunkers import chunk_gdscript  # noqa: E402

mcp = FastMCP("godot")

BACKUP_DIR = ".gdmaster_backups"
AUDIT_LOG = config.LOGS_DIR / "godot_mcp_audit.jsonl"


def _audit(tool: str, args: dict, result: str, ok: bool) -> None:
    try:
        with AUDIT_LOG.open("a", encoding="utf-8") as f:
            f.write(json.dumps({
                "ts": time.time(), "tool": tool, "ok": ok,
                "args": {k: (v if len(str(v)) < 400 else str(v)[:400] + "...") for k, v in args.items()},
                "result": result[:400],
            }, ensure_ascii=False) + "\n")
    except OSError:
        pass


def _err(msg: str, **extra) -> str:
    """Ответ об ошибке. Дополнительные поля доезжают до модели.

    Поля вроде `similar_properties` — не украшение: именно по ним модель
    находит правильное имя свойства за один шаг вместо похода в RAG. Поэтому
    `**extra` тут обязателен, иначе подсказка теряется по дороге.
    """
    return json.dumps({"ok": False, "error": msg, **extra},
                      ensure_ascii=False, indent=1)


def _ok(**kw) -> str:
    return json.dumps({"ok": True, **kw}, ensure_ascii=False, indent=1)


def _attach_lint(payload: dict, script_path: str) -> None:
    """Дописать в payload разбор на API Godot 3.

    Парсер (`--check-only`) проверяет синтаксис, а не существование методов,
    поэтому `preload(...).instance()` проходит валидацию и падает в рантайме.
    Находки кладём и отдельным полем `lint`, и строками в уже существующий
    `warnings` — модель читает warnings даже когда игнорирует новые поля.
    """
    try:
        target = resolve(script_path, must_exist=False)
        if not target.is_file():
            return
        findings = lint_gdscript(target.read_text(encoding="utf-8", errors="replace"))
    except Exception:
        return
    if not findings:
        return
    payload["lint"] = findings
    lines = [f"godot3-api line {f['line']}: {f['message']} -> {f['fix']}" for f in findings]
    payload["warnings"] = lines + list(payload.get("warnings") or [])
    payload["lint_hint"] = (
        "Найдено API Godot 3. Парсер его не ловит — это ошибка РАНТАЙМА. "
        "Исправь, затем godot_validate() и godot_run_scene() заново."
    )


_EXT_RESOURCE_RE = re.compile(r"^\[ext_resource\b([^\]]*)\]", re.MULTILINE)
_ATTR_RE = re.compile(r'(\w+)\s*=\s*"([^"]*)"')


def _scene_script_paths(scene_path: str) -> list[str]:
    """Вытащить из .tscn пути скриптов, привязанных к его узлам.

    Нужно, чтобы линт Godot 3 срабатывал там, где модель реально смотрит:
    она почти всегда валидирует СЦЕНУ, а не каждый скрипт по отдельности.
    Без этого `.instance()` в привязанном скрипте проходит мимо проверки.
    """
    try:
        target = resolve(scene_path, must_exist=False)
        text = target.read_text(encoding="utf-8", errors="replace")
    except Exception:
        return []
    out: list[str] = []
    for m in _EXT_RESOURCE_RE.finditer(text):
        attrs = dict(_ATTR_RE.findall(m.group(1)))
        if attrs.get("type") != "Script":
            continue
        path = attrs.get("path") or ""
        if path.startswith("res://"):
            out.append(path[len("res://"):])
    return out


def _attach_scene_lint(payload: dict, scene_path: str) -> None:
    """Пролинтовать скрипты, привязанные к сцене, и подшить находки в payload."""
    findings: list[dict] = []
    for rel in _scene_script_paths(scene_path):
        try:
            text = resolve(rel, must_exist=False).read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        for f in lint_gdscript(text):
            findings.append({**f, "script": f"res://{rel}"})
    if not findings:
        return
    payload["lint"] = findings
    lines = [f"godot3-api {f['script']}:{f['line']}: {f['message']} -> {f['fix']}"
             for f in findings]
    payload["warnings"] = lines + list(payload.get("warnings") or [])
    payload["lint_hint"] = (
        "Найдено API Godot 3 в скриптах этой сцены. Парсер его не ловит — это "
        "ошибка РАНТАЙМА. Исправь и провалидируй сцену заново."
    )


def _runner() -> GodotRunner:
    return GodotRunner(project_root=project_root())


def _backup(path: Path) -> str:
    root = project_root()
    rel = path.relative_to(root)
    base = root / BACKUP_DIR / rel
    base.parent.mkdir(parents=True, exist_ok=True)
    (root / BACKUP_DIR / ".gdignore").write_text("", encoding="utf-8")
    stamp = time.strftime("%Y%m%d-%H%M%S")
    dst = base.with_suffix(base.suffix + f".{stamp}.bak")
    # несколько мутаций в одну секунду не должны затирать друг друга
    i = 1
    while dst.exists():
        dst = base.with_suffix(base.suffix + f".{stamp}-{i}.bak")
        i += 1
    shutil.copy2(path, dst)
    return res_path(str(dst.relative_to(root)).replace("\\", "/"), root)


def _backup_scene(scene_path: str) -> str:
    """Бэкап .tscn перед мутацией. Ошибка бэкапа не должна блокировать работу."""
    try:
        p = resolve(scene_path, must_exist=True)
        return _backup(p)
    except (PathDenied, OSError):
        return ""


def _subtree_size(scene_path: str, node_path: str) -> int:
    """Сколько узлов будет удалено вместе с node_path (включая сам узел).

    Считается по .tscn, без запуска Godot. -1, если сцену прочитать не удалось.
    """
    try:
        tree = gscene.read_scene(scene_path, project_root())
    except (PathDenied, OSError):
        return -1
    target = node_path.strip("/").replace("\\", "/")
    if target in (".", "root", ""):
        target = ""
    prefix = (target + "/") if target else ""
    n = 0
    for node in tree.get("flat", []):
        p = str(node.get("path", ""))
        if target == "" or p == target or p.startswith(prefix):
            n += 1
    return n


# ==========================================================================
# ИНСПЕКЦИЯ (read-only)
# ==========================================================================

@mcp.tool()
def godot_project_info() -> str:
    """Паспорт текущего Godot-проекта: имя, версия движка, главная сцена,
    автолоады, входные действия, состав файлов.

    Вызывай первым при любой содержательной задаче, чтобы понять структуру.
    """
    try:
        root = project_root()
    except PathDenied as e:
        return _err(str(e))
    info: dict = {"project_root": str(root), "exists": root.exists()}
    pg = root / "project.godot"
    if pg.exists():
        text = pg.read_text(encoding="utf-8", errors="replace")
        section = ""
        settings: dict = {}
        autoloads: dict = {}
        for line in text.splitlines():
            s = line.strip()
            m = re.match(r"^\[(.+)\]$", s)
            if m:
                section = m.group(1)
                continue
            m = re.match(r"^([A-Za-z0-9_/\.]+)\s*=\s*(.+)$", s)
            if not m:
                continue
            k, v = m.group(1), m.group(2)
            if section == "autoload":
                autoloads[k] = v
            elif section == "input":
                settings.setdefault("input_actions", []).append(k)
            else:
                settings[f"{section}/{k}" if section else k] = v
        info["config_version"] = settings.get("config_version")
        info["features"] = settings.get("application/config/features")
        info["main_scene"] = settings.get("application/run/main_scene")
        info["project_name"] = settings.get("application/config/name")
        info["autoloads"] = autoloads
        info["input_actions"] = settings.get("input_actions", [])
        info["rendering_method"] = settings.get("rendering/renderer/rendering_method")
    counts = {"gd": 0, "tscn": 0, "tres": 0, "other": 0}
    scenes: list[str] = []
    if root.exists():
        for p in root.rglob("*"):
            if not p.is_file() or any(part in config.PROJECT_SKIP_DIRS for part in p.parts):
                continue
            if p.suffix == ".gd":
                counts["gd"] += 1
            elif p.suffix == ".tscn":
                counts["tscn"] += 1
                scenes.append(res_path(str(p.relative_to(root)), root))
            elif p.suffix == ".tres":
                counts["tres"] += 1
            else:
                counts["other"] += 1
    info["file_counts"] = counts
    info["scenes"] = sorted(scenes)[:60]
    info["godot_exe"] = str(config.GODOT_EXE)
    info["engine_version_target"] = config.ENGINE_VERSION
    return _ok(**info)


@mcp.tool()
def godot_list_files(kind: str = "all", glob: str = "") -> str:
    """Список файлов проекта.

    Args:
        kind: "all" | "gd" (скрипты) | "tscn" (сцены) | "tres" (ресурсы) | "dirs".
        glob: необязательная маска, например "player/*" или "*.gd".
    """
    try:
        root = project_root()
    except PathDenied as e:
        return _err(str(e))
    exts = {"gd": {".gd"}, "tscn": {".tscn"}, "tres": {".tres"}}
    out: list[str] = []
    for p in sorted(root.rglob("*")):
        rel = p.relative_to(root).as_posix()
        if any(part in config.PROJECT_SKIP_DIRS for part in p.parts):
            continue
        if kind == "dirs":
            if p.is_dir():
                out.append(rel + "/")
            continue
        if not p.is_file():
            continue
        if kind in exts and p.suffix.lower() not in exts[kind]:
            continue
        if glob and not Path(rel).match(glob):
            continue
        out.append(rel)
    return _ok(count=len(out), files=out[:400], truncated=len(out) > 400)


@mcp.tool()
def godot_read_file(path: str) -> str:
    """Прочитать текстовый файл проекта (скрипт, сцена, ресурс, конфиг)."""
    try:
        p = resolve(path, must_exist=True)
    except PathDenied as e:
        return _err(str(e))
    if p.suffix.lower() not in WRITABLE_EXTS | {".xml", ".csv", ".import"}:
        return _err(f"чтение {p.suffix} не поддерживается (бинарный файл?)")
    try:
        text = p.read_text(encoding="utf-8", errors="replace")
    except OSError as e:
        return _err(f"не удалось прочитать: {e}")
    return _ok(path=res_path(path), lines=text.count("\n") + 1, content=text[:60000])


@mcp.tool()
def godot_scene_tree(scene_path: str) -> str:
    """Дерево узлов сцены: имена, типы, прикреплённые скрипты, свойства.

    Args:
        scene_path: путь к .tscn, например "res://Main.tscn" или "Main.tscn".
    """
    try:
        root = project_root()
        data = gscene.read_scene(scene_path, root)
    except PathDenied as e:
        return _err(str(e))
    except Exception as e:  # noqa: BLE001
        return _err(f"не удалось разобрать сцену: {e}")
    return _ok(**data)


@mcp.tool()
def godot_script_symbols(script_path: str) -> str:
    """Символы GDScript-файла: class_name, extends, сигналы, экспорты,
    переменные, константы, функции с сигнатурами.

    Args:
        script_path: путь к .gd.
    """
    try:
        p = resolve(script_path, must_exist=True)
    except PathDenied as e:
        return _err(str(e))
    if p.suffix.lower() != ".gd":
        return _err("ожидался .gd файл")
    text = p.read_text(encoding="utf-8", errors="replace")
    chunks = chunk_gdscript(text, normalize(script_path), "project")

    class_name = ""
    extends = ""
    m = re.search(r"^class_name\s+([A-Za-z_]\w*)", text, re.M)
    if m:
        class_name = m.group(1)
    m = re.search(r"^extends\s+([A-Za-z_][\w\.]*)", text, re.M)
    if m:
        extends = m.group(1)

    functions = []
    for fm in re.finditer(r"^([ \t]*)func\s+([A-Za-z_]\w*)\s*(\([^)]*\))\s*(->\s*[^:\n]+)?\s*:",
                          text, re.M):
        line = text[:fm.start()].count("\n") + 1
        functions.append({
            "name": fm.group(2), "args": fm.group(3).strip(),
            "returns": (fm.group(4) or "").replace("->", "").strip() or "void",
            "line": line,
        })
    signals = [{"name": s.group(1), "args": (s.group(2) or "()")}
               for s in re.finditer(r"^\s*signal\s+([A-Za-z_]\w*)\s*(\([^)]*\))?", text, re.M)]
    exports = [{"name": v.group(3), "type": v.group(4) or "Variant", "line": text[:v.start()].count("\n") + 1}
               for v in re.finditer(r"^([ \t]*)(@export[^\n]*?)?\s*(?:@onready\s+)?var\s+([A-Za-z_]\w*)\s*(?::\s*([A-Za-z_][\w\.\[\]]*))?",
                                    text, re.M)
               if (v.group(2) or "").strip().startswith("@export")]
    return _ok(
        path=res_path(script_path), class_name=class_name, extends=extends,
        lines=text.count("\n") + 1, functions=functions, signals=signals,
        exported_variables=exports,
        chunk_summary=[{"symbol": c.symbol, "section": c.section} for c in chunks],
    )


@mcp.tool()
def godot_find_symbol(name: str, kind: str = "any") -> str:
    """Найти символ в проекте: имя функции, класса, узла или строку в файлах.

    Args:
        name: что искать, например "player", "take_damage", "CharacterBody3D".
        kind: "any" | "gd" (только скрипты) | "tscn" (только сцены) | "text".
    """
    try:
        root = project_root()
    except PathDenied as e:
        return _err(str(e))
    exts = {".gd"} if kind == "gd" else ({".tscn"} if kind == "tscn" else None)
    pat = re.compile(re.escape(name), re.I)
    hits: list[dict] = []
    for p in root.rglob("*"):
        if not p.is_file() or any(part in config.PROJECT_SKIP_DIRS for part in p.parts):
            continue
        if exts and p.suffix.lower() not in exts:
            continue
        if not exts and p.suffix.lower() not in config.PROJECT_TEXT_EXTS:
            continue
        try:
            if p.stat().st_size > config.MAX_INDEX_FILE_BYTES:
                continue
            text = p.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        for i, line in enumerate(text.splitlines(), 1):
            if pat.search(line):
                hits.append({"path": res_path(str(p.relative_to(root)), root),
                             "line": i, "text": line.strip()[:200]})
                if len(hits) >= 60:
                    break
        if len(hits) >= 60:
            break
    return _ok(query=name, count=len(hits), hits=hits, truncated=len(hits) >= 60)


# ==========================================================================
# МУТАЦИИ
# ==========================================================================

@mcp.tool()
def godot_write_script(path: str, content: str, reason: str = "") -> str:
    """Создать или полностью перезаписать текстовый файл проекта (обычно .gd).

    Делает резервную копию предыдущей версии. Для правки существующего кода
    предпочитай godot_patch_script — минимальное изменение безопаснее.

    Args:
        path: путь, например "player/player.gd".
        content: полное новое содержимое файла.
        reason: зачем (идёт в audit log и в отчёт).
    """
    try:
        rel = guard_extension(path, WRITABLE_EXTS)
        p = resolve(rel)
    except PathDenied as e:
        return _err(str(e))
    backup = ""
    if p.exists():
        backup = _backup(p)
    p.parent.mkdir(parents=True, exist_ok=True)
    try:
        p.write_text(content, encoding="utf-8", newline="\n")
    except OSError as e:
        return _err(f"запись не удалась: {e}")
    _audit("godot_write_script", {"path": rel, "reason": reason, "bytes": len(content)},
           f"written {rel}", True)
    extra: dict = {}
    if rel.lower().endswith(".tscn"):
        # Ручная запись .tscn почти всегда даёт файл, который Godot не читает:
        # ссылки ExtResource(...) должны совпадать с секциями [ext_resource],
        # а модель проставляет путь вместо id. На прогоне это дало 15 итераций
        # write_script → validate → read_file подряд. Не запрещаем (запрет
        # упёрся бы в тупик, если сцену надо починить точечно), но говорим прямо.
        extra["warning"] = (
            ".tscn записан текстом. Godot читает такой файл только если ссылки "
            "ExtResource(\"id\") совпадают с секциями [ext_resource ... id=\"id\"] — "
            "вручную это почти всегда расходится, и сцена не загрузится. "
            "Сцены собирай инструментами: godot_scene_create / godot_scene_add_node "
            "(node_type = путь к .gltf или .tscn — инстанцирует готовую сцену) / "
            "godot_scene_set_property. Тогда файл пишет сама Godot."
        )
    return _ok(path=res_path(rel), bytes=len(content), backup=backup,
               next_step="Проверь: godot_validate", **extra)


@mcp.tool()
def godot_patch_script(path: str, old_text: str, new_text: str, reason: str = "") -> str:
    """Точечная замена фрагмента в файле проекта (минимальное изменение).

    `old_text` должен встречаться в файле ровно один раз — иначе правка
    отклоняется, чтобы не задеть лишнее.

    Args:
        path: путь к файлу.
        old_text: точный существующий фрагмент.
        new_text: чем заменить.
        reason: зачем.
    """
    try:
        rel = guard_extension(path, WRITABLE_EXTS)
        p = resolve(rel, must_exist=True)
    except PathDenied as e:
        return _err(str(e))
    text = p.read_text(encoding="utf-8", errors="replace")
    n = text.count(old_text)
    if n == 0:
        return _err("old_text не найден в файле. Прочитай файл и повтори с точным фрагментом.")
    if n > 1:
        return _err(f"old_text встречается {n} раз — расширь фрагмент до уникального.")
    backup = _backup(p)
    p.write_text(text.replace(old_text, new_text, 1), encoding="utf-8", newline="\n")
    _audit("godot_patch_script", {"path": rel, "reason": reason},
           f"patched {rel} ({len(old_text)}->{len(new_text)} bytes)", True)
    return _ok(path=res_path(rel), backup=backup, next_step="Проверь: godot_validate")


@mcp.tool()
def godot_scene_create(scene_path: str, root_type: str = "Node2D", root_name: str = "Root") -> str:
    """Создать новую сцену с указанным корневым узлом.

    Args:
        scene_path: путь новой сцены, например "levels/level_02.tscn".
        root_type: тип корневого узла Godot, например "Node2D", "Node3D", "Control".
        root_name: имя корневого узла.
    """
    try:
        r = _runner()
        backup = _backup_scene(scene_path) if resolve(scene_path).exists() else ""
        res = gscene.create_scene(r, scene_path, root_type, root_name)
    except PathDenied as e:
        return _err(str(e))
    _audit("godot_scene_create", {"scene_path": scene_path, "root_type": root_type},
           json.dumps(res, ensure_ascii=False)[:300], "error" not in res)
    return _err(res["error"]) if "error" in res else _ok(backup=backup, **res)


@mcp.tool()
def godot_scene_add_node(scene_path: str, parent_path: str, node_type: str,
                         node_name: str, properties: dict | None = None) -> str:
    """Добавить узел в сцену.

    Это единственный правильный способ добавлять объекты в .tscn — файл пишет
    сама Godot. Не записывай .tscn текстом через godot_write_script: такой файл
    ломается на загрузке («Parse Error»), потому что ссылки на внешние ресурсы
    (ExtResource) должны совпадать с секциями [ext_resource], а вручную это
    почти всегда расходится.

    Args:
        scene_path: путь к .tscn.
        parent_path: путь родителя от корня сцены ("." = корень), например "Player" или "UI/HUD".
        node_type: тип узла Godot, например "Camera3D", "Timer", "Label", "Area3D".
            Либо путь к готовой сцене — тогда она инстанцируется как узел:
            "assets/external/polyhaven-Barrel_01/Barrel_01_2k.gltf" или
            "res://props/crate.tscn". Так ставится скачанный ассет.
            ВАЖНО: перед этим нужен godot_check_project (импорт ресурсов), иначе
            Godot ещё не видит установленный .gltf и вернёт «есть на диске, но
            ещё не импортирован».
        node_name: имя нового узла (уникальное среди детей родителя).
        properties: необязательные свойства, например {"position": "Vector3(0, 2, 0)", "text": "HP"}.
            Строки вида Vector3(...)/Color(...) подставляются как выражения Godot.
    """
    try:
        r = _runner()
        backup = _backup_scene(scene_path)
        res = gscene.add_node(r, scene_path, parent_path, node_type, node_name, properties)
    except PathDenied as e:
        return _err(str(e))
    _audit("godot_scene_add_node",
           {"scene": scene_path, "parent": parent_path, "type": node_type, "name": node_name},
           json.dumps(res, ensure_ascii=False)[:300], "error" not in res)
    if "error" in res:
        extra = {k: v for k, v in res.items() if k != "error"}
        return _err(res["error"], **extra)
    return _ok(backup=backup, **res)


@mcp.tool()
def godot_scene_remove_node(scene_path: str, node_path: str, confirm: bool = False) -> str:
    """Удалить узел (со всеми детьми) из сцены.

    Перед удалением создаётся резервная копия .tscn в .gdmaster_backups/.
    Удаление поддерева больше APPROVAL_SUBTREE_NODES узлов требует confirm=True
    (политика approval, спека §37).

    Args:
        scene_path: путь к .tscn.
        node_path: путь узла от корня сцены, например "Player/Camera3D".
        confirm: подтверждение для удаления большого поддерева.
    """
    size = _subtree_size(scene_path, node_path)
    limit = config.APPROVAL_SUBTREE_NODES
    if size < 0:
        return _err(f"сцена не читается, удаление отклонено: {scene_path}")
    if size > limit and not confirm:
        _audit("godot_scene_remove_node",
               {"scene": scene_path, "node": node_path, "subtree": size, "approved": False},
               "APPROVAL_REQUIRED", False)
        return _err(
            f"APPROVAL_REQUIRED: узел '{node_path}' тянет за собой {size} узлов "
            f"(порог {limit}). Это высокорисковая операция. Если удаление действительно "
            f"нужно — вызови инструмент повторно с confirm=true."
        )
    try:
        r = _runner()
        backup = _backup_scene(scene_path)
        res = gscene.remove_node(r, scene_path, node_path)
    except PathDenied as e:
        return _err(str(e))
    _audit("godot_scene_remove_node",
           {"scene": scene_path, "node": node_path, "subtree": size, "approved": True},
           json.dumps(res, ensure_ascii=False)[:300], "error" not in res)
    return _err(res["error"]) if "error" in res else _ok(subtree_removed=size, backup=backup, **res)


@mcp.tool()
def godot_scene_set_property(scene_path: str, node_path: str, property: str, value) -> str:
    """Установить свойство узла в сцене.

    Args:
        scene_path: путь к .tscn.
        node_path: путь узла от корня ("." = корень).
        property: имя свойства, например "position", "text", "modulate".
        value: значение. Строки вида "Vector3(0, 1, 0)", "Color(1,0,0)" трактуются
            как выражения Godot; обычные строки/числа — как литералы.
            Строка, начинающаяся с "res://", ЗАГРУЖАЕТСЯ как ресурс и
            назначается объектом — так ставится материал:
            property="material_override", value="res://materials/floor.tres".
            Для меша из .gltf это не сработает: .gltf — это PackedScene, а не
            Mesh. Его ставят как узел через godot_scene_add_node (node_type =
            путь к .gltf).
    """
    try:
        r = _runner()
        backup = _backup_scene(scene_path)
        res = gscene.set_property(r, scene_path, node_path, property, value)
    except PathDenied as e:
        return _err(str(e))
    _audit("godot_scene_set_property",
           {"scene": scene_path, "node": node_path, "property": property, "value": value},
           json.dumps(res, ensure_ascii=False)[:300], "error" not in res)
    if "error" in res:
        # similar_properties доезжает до модели: без него подсказка бесполезна
        extra = {k: v for k, v in res.items() if k != "error"}
        return _err(res["error"], **extra)
    return _ok(backup=backup, **res)


@mcp.tool()
def godot_scene_attach_script(scene_path: str, node_path: str, script_path: str) -> str:
    """Прикрепить GDScript к узлу сцены.

    Args:
        scene_path: путь к .tscn.
        node_path: путь узла от корня.
        script_path: путь к .gd, например "player/player.gd".
    """
    try:
        r = _runner()
        backup = _backup_scene(scene_path)
        res = gscene.attach_script(r, scene_path, node_path, script_path)
    except PathDenied as e:
        return _err(str(e))
    _audit("godot_scene_attach_script",
           {"scene": scene_path, "node": node_path, "script": script_path},
           json.dumps(res, ensure_ascii=False)[:300], "error" not in res)
    return _err(res["error"]) if "error" in res else _ok(backup=backup, **res)


@mcp.tool()
def godot_scene_connect_signal(scene_path: str, node_path: str, signal_name: str,
                               target_path: str, method: str) -> str:
    """Соединить сигнал узла с методом другого узла (в редакторе, не в коде).

    Args:
        scene_path: путь к .tscn.
        node_path: узел-источник сигнала.
        signal_name: имя сигнала, например "pressed", "body_entered".
        target_path: узел, на котором вызывается метод.
        method: имя метода-обработчика.
    """
    try:
        r = _runner()
        backup = _backup_scene(scene_path)
        res = gscene.connect_signal(r, scene_path, node_path, signal_name, target_path, method)
    except PathDenied as e:
        return _err(str(e))
    _audit("godot_scene_connect_signal",
           {"scene": scene_path, "node": node_path, "signal": signal_name,
            "target": target_path, "method": method},
           json.dumps(res, ensure_ascii=False)[:300], "error" not in res)
    return _err(res["error"]) if "error" in res else _ok(backup=backup, **res)


# ==========================================================================
# НАСТРОЙКИ ПРОЕКТА
# ==========================================================================

@mcp.tool()
def godot_input_action_add(action: str, keys: list[str], deadzone: float = 0.5) -> str:
    """Добавить или перезаписать действие в InputMap проекта.

    Файл project.godot пишет сама Godot (ProjectSettings.save()), поэтому формат
    гарантированно корректный, а остальные настройки проекта сохраняются.

    НЕ пытайся править секцию [input] через godot_write_script: там
    сериализованные объекты InputEventKey/InputEventMouseButton, ручной формат
    вида [action(name="...")] Godot молча игнорирует и действие не появляется.

    Args:
        action: имя действия, например "ui_sprint" или "jump".
        keys: список клавиш, например ["Shift"] или ["Ctrl", "mouse_left"].
            Имена разбирает сама Godot: "Shift", "Space", "W", "Escape", "F1",
            а также "mouse_left", "mouse_right", "mouse_middle".
        deadzone: мёртвая зона, по умолчанию 0.5.
    """
    try:
        r = _runner()
        p = resolve("project.godot", must_exist=True)
        backup = _backup(p)
        res = gproj.add_input_action(r, action, keys, deadzone)
    except PathDenied as e:
        return _err(str(e))
    _audit("godot_input_action_add", {"action": action, "keys": keys},
           json.dumps(res, ensure_ascii=False)[:300], "error" not in res)
    return _err(res["error"]) if "error" in res else _ok(backup=backup, **res)


@mcp.tool()
def godot_project_init(project_name: str = "", renderer: str = "forward_plus",
                       main_scene: str = "") -> str:
    """Развернуть текущую папку в рабочий Godot-проект и назначить главную сцену.

    Нужен, когда проекта ещё НЕТ: Godot сам проект из пустой папки не создаёт,
    поэтому без этого инструмента первый же шаг задачи («сделай уровень в пустой
    папке») невыполним.

    Идемпотентен: если `project.godot` уже существует — проект не пересоздаётся,
    но `main_scene` (если задан) будет назначен. Поэтому вызывай его повторно,
    когда нужно поменять главную сцену.

    Args:
        project_name: имя проекта. Пусто = имя папки.
        renderer: "forward_plus" (по умолчанию), "mobile" или "gl_compatibility".
            Для простого 2D хватает любого; gl_compatibility самый нетребовательный.
        main_scene: путь к .tscn, который станет главной сценой. Сцена должна уже
            существовать. Без главной сцены проект не запускается «просто F5».
    """
    try:
        r = _runner()
        res = gproj.init_project(r, project_name, renderer, main_scene)
    except PathDenied as e:
        return _err(str(e))
    ok = bool(res.get("ok"))
    _audit("godot_project_init",
           {"project_name": project_name, "renderer": renderer, "main_scene": main_scene},
           json.dumps(res, ensure_ascii=False)[:300], ok)
    return json.dumps(res, ensure_ascii=False, indent=1)


# ==========================================================================
# ВАЛИДАЦИЯ И RUNTIME
# ==========================================================================

@mcp.tool()
def godot_validate(script_path: str = "") -> str:
    """Проверить GDScript на ошибки парсинга или .tscn на загружаемость.

    Args:
        script_path: путь к .gd (парсинг) или к .tscn (реальная загрузка движком).
            Если пусто — проверяются весь проект: headless-запуск на 30 кадров.
    """
    try:
        r = _runner()
        if script_path:
            if script_path.lower().endswith(".tscn"):
                payload = gscene.validate_scene(r, script_path)
                payload["checked"] = res_path(script_path)
                _attach_scene_lint(payload, script_path)
                ok = bool(payload.get("ok"))
                _audit("godot_validate", {"scene": script_path},
                       json.dumps(payload, ensure_ascii=False)[:300], ok)
                return json.dumps(payload, ensure_ascii=False, indent=1)
            res = r.check_script(script_path)
            payload = res.to_dict()
            payload["checked"] = res_path(script_path)
            _attach_lint(payload, script_path)
            _audit("godot_validate", {"script": script_path}, json.dumps(payload)[:300], res.ok)
            return json.dumps(payload, ensure_ascii=False, indent=1)
        # все скрипты: быстрый проход по одному процессу на скрипт не нужен —
        # запускаем проект headless и собираем ошибки парсинга из вывода
        res = r.run_scene(None, quit_after_frames=30)
        payload = res.to_dict()
        payload["checked"] = "весь проект (headless import + запуск 30 кадров)"
        _audit("godot_validate", {"script": "all"}, json.dumps(payload)[:300], res.ok)
        return json.dumps(payload, ensure_ascii=False, indent=1)
    except PathDenied as e:
        return _err(str(e))


@mcp.tool()
def godot_run_scene(scene_path: str = "", frames: int = 180, timeout: float = 90.0) -> str:
    """Запустить сцену в Godot headless и вернуть ошибки рантайма.

    Это основной способ проверить, что изменение реально работает.
    Успешная запись файла — НЕ доказательство работоспособности.

    Args:
        scene_path: путь к .tscn. Пусто = главная сцена проекта.
        frames: сколько кадров прогнать перед остановкой (по умолчанию 180 ≈ 3 с).
        timeout: жёсткий лимит в секундах.
    """
    try:
        r = _runner()
        res = r.run_scene(scene_path or None, quit_after_frames=max(10, int(frames)),
                          timeout=float(timeout))
    except PathDenied as e:
        return _err(str(e))
    payload = res.to_dict()
    payload["scene"] = res_path(scene_path) if scene_path else "(main scene)"
    payload["verdict"] = ("OK: ошибок рантайма не обнаружено" if res.ok
                          else "FAILED: см. errors")
    _audit("godot_run_scene", {"scene": scene_path, "frames": frames},
           json.dumps(payload)[:300], res.ok)
    return json.dumps(payload, ensure_ascii=False, indent=1)


@mcp.tool()
def godot_play_scene(scene_path: str = "", wait: float = 6.0) -> str:
    """Открыть сцену в НАСТОЯЩЕМ ОКНЕ игры на экране пользователя.

    Используй, когда пользователь просит «запусти», «покажи», «продемонстрируй»
    сцену или игру, «хочу посмотреть». `godot_run_scene` окна НЕ открывает —
    он только читает ошибки из консоли. Этот инструмент действительно показывает
    игру человеку.

    Процесс отсоединённый: игра живёт, пока пользователь сам не закроет окно,
    и не умирает вместе с агентом. Повторный вызов закрывает предыдущее окно.
    В ответе `window_opened`/`window_title` — подтверждение, что окно реально
    появилось, а не просто «процесс запустился».

    Args:
        scene_path: путь к .tscn. Пусто = главная сцена проекта.
        wait: сколько секунд ждать появления окна перед отчётом.
    """
    try:
        payload = gplay.play_scene(scene_path, wait=float(wait))
    except PathDenied as e:
        return _err(str(e))
    _audit("godot_play_scene", {"scene": scene_path, "wait": wait},
           json.dumps(payload, ensure_ascii=False)[:300], bool(payload.get("ok")))
    return json.dumps(payload, ensure_ascii=False, indent=1)


@mcp.tool()
def godot_stop_play() -> str:
    """Закрыть окно игры, открытое `godot_play_scene`.

    Безопасно вызывать, когда ничего не запущено. Используй, когда пользователь
    просит закрыть игру, или когда её нужно перезапустить начисто.
    """
    payload = gplay.stop_play()
    _audit("godot_stop_play", {}, json.dumps(payload, ensure_ascii=False)[:300],
           bool(payload.get("ok")))
    return json.dumps(payload, ensure_ascii=False, indent=1)


@mcp.tool()
def godot_check_project(timeout: float = 300.0) -> str:
    """Полная проверка проекта: переимпорт ресурсов и разбор ошибок Godot.

    Долгая операция. Запускай после добавления новых файлов/ресурсов,
    если сцены не подхватывают изменения.
    """
    try:
        r = _runner()
        res = r.import_assets(timeout=timeout)
    except PathDenied as e:
        return _err(str(e))
    payload = res.to_dict()
    payload["verdict"] = "OK" if res.ok else "есть ошибки (см. errors)"
    return json.dumps(payload, ensure_ascii=False, indent=1)


def main() -> None:
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
