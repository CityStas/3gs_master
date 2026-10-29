"""Правка ProjectSettings (project.godot) самой Godot, а не текстом.

Зачем отдельный модуль: `project.godot` — INI-подобный файл, но секция `[input]`
хранит сериализованные объекты `InputEventKey`/`InputEventMouseButton` в формате,
который невозможно угадать. Модель, дописывающая `[input]` вручную, стабильно
изобретает несуществующий синтаксис (`[input_map]`, `[action(name=...)]`) — Godot
такие секции молча игнорирует, и действие просто не появляется в InputMap.

Здесь настройка ставится через `ProjectSettings.set_setting()` и сохраняется
`ProjectSettings.save()`, то есть файл пишет движок. Существующие настройки
сохраняются: `save()` выгружает все ProjectSettings, а не только новую.
"""
from __future__ import annotations

import json
from pathlib import Path

from .. import config
from .paths import PathDenied, res_path, resolve
from .runner import GodotRunner

# Минимальный валидный project.godot.
#
# Godot сам проект из ПУСТОЙ папки не создаёт — проверено: ни `--editor --quit`,
# ни `--import` на пустом каталоге не делают ничего (`--import` лишь отвечает
# «Can't run project: no main scene defined»). Поэтому файл пишем сами, а дальше
# движок его принимает и разворачивает в полноценный проект при первом импорте:
# появляется `.godot/`, скан файловой системы, глобальные имена классов.
MINIMAL_PROJECT = """\
; Engine configuration file.
; Written by gdmaster (godot_project_init), then rewritten by Godot on first import.
config_version=5

[application]

config/name="{name}"
config/features=PackedStringArray("{version}", "{renderer}")
"""

RENDERERS = {
    "forward_plus": "Forward Plus",
    "mobile": "Mobile",
    "gl_compatibility": "GL Compatibility",
}

# Клавиши мыши, которые можно передать в add_input_action.
MOUSE_BUTTONS = {
    "mouse_left": "MOUSE_BUTTON_LEFT",
    "mouse_right": "MOUSE_BUTTON_RIGHT",
    "mouse_middle": "MOUSE_BUTTON_MIDDLE",
    "mouse_wheel_up": "MOUSE_BUTTON_WHEEL_UP",
    "mouse_wheel_down": "MOUSE_BUTTON_WHEEL_DOWN",
}


def add_input_action(runner: GodotRunner, action: str, keys: list[str],
                     deadzone: float = 0.5, timeout: float = 60.0) -> dict:
    """Добавить или перезаписать действие InputMap.

    action: имя действия, например "ui_sprint".
    keys:   список клавиш/кнопок. Имена клавиш разбирает сама Godot
            (`OS.find_keycode_from_string`), поэтому подходят "Shift", "Space",
            "W", "Escape", "F1", а также "mouse_left" и т.п.
    """
    action = (action or "").strip()
    if not action:
        return {"error": "имя действия пустое"}
    if not keys:
        return {"error": "нужен хотя бы один ключ/кнопка"}
    if "/" in action or "\\" in action:
        return {"error": f"недопустимое имя действия: {action}"}

    # Значения — это ИМЕНА констант Godot, они подставляются в GDScript как есть
    # (не строки), иначе button_index получит 0 вместо MOUSE_BUTTON_LEFT.
    mouse_literal = "{ " + ", ".join(f'"{k}": {v}' for k, v in MOUSE_BUTTONS.items()) + " }"
    script = "\n".join([
        f"var __action: String = {json.dumps(action)}",
        f"var __keys: Array = {json.dumps(list(keys), ensure_ascii=False)}",
        f"var __deadzone: float = {float(deadzone)}",
        f"var __mouse: Dictionary = {mouse_literal}",
        "var __events: Array = []",
        "for __k in __keys:",
        "\tvar __s: String = str(__k)",
        "\tif __mouse.has(__s):",
        "\t\tvar __mb := InputEventMouseButton.new()",
        "\t\t__mb.button_index = __mouse[__s]",
        "\t\t__events.append(__mb)",
        "\t\tcontinue",
        "\tvar __kc: int = OS.find_keycode_from_string(__s)",
        "\tif __kc == 0:",
        '\t\t__res["error"] = "неизвестная клавиша: " + __s',
        "\t\treturn",
        "\tvar __ev := InputEventKey.new()",
        "\t__ev.physical_keycode = __kc",
        "\t__events.append(__ev)",
        'ProjectSettings.set_setting("input/" + __action, {"deadzone": __deadzone, "events": __events})',
        "var __err: int = ProjectSettings.save()",
        "if __err != OK:",
        '\t__res["error"] = "ProjectSettings.save() вернул код %d" % __err',
        "\treturn",
        '__res["ok"] = true',
        '__res["action"] = __action',
        '__res["keys"] = __keys',
        '__res["deadzone"] = __deadzone',
        '__res["project_file"] = ProjectSettings.globalize_path("res://project.godot")',
    ])
    res, payload = runner.exec_tree_script(script, timeout=timeout)
    if not payload:
        payload = {"error": "; ".join(res.errors[:5]) or
                            f"Godot завершился с кодом {res.exit_code} и не записал результат"}
    payload["godot_ok"] = res.ok
    payload["godot_exit_code"] = res.exit_code
    return payload


def set_main_scene(runner: GodotRunner, scene_path: str, timeout: float = 60.0) -> dict:
    """Назначить главную сцену проекта (`application/run/main_scene`).

    Без неё проект нельзя запустить «просто нажав F5» и не работает
    `godot_play_scene()` без аргумента. Пишет опять же Godot, а не текст.
    """
    target = resolve(scene_path, runner.project_root, must_exist=True)
    if target.suffix.lower() != ".tscn":
        return {"error": f"главная сцена должна быть .tscn, получено: {scene_path}"}
    rel = res_path(scene_path, runner.project_root)
    script = "\n".join([
        f"var __scene: String = {json.dumps(rel)}",
        'ProjectSettings.set_setting("application/run/main_scene", __scene)',
        "var __err: int = ProjectSettings.save()",
        "if __err != OK:",
        '\t__res["error"] = "ProjectSettings.save() вернул код %d" % __err',
        "\treturn",
        '__res["ok"] = true',
        '__res["main_scene"] = str(ProjectSettings.get_setting("application/run/main_scene", ""))',
        '__res["project_file"] = ProjectSettings.globalize_path("res://project.godot")',
    ])
    res, payload = runner.exec_tree_script(script, timeout=timeout)
    if not payload:
        payload = {"error": "; ".join(res.errors[:5]) or
                            f"Godot завершился с кодом {res.exit_code} и не записал результат"}
    payload["godot_ok"] = res.ok
    return payload


def init_project(runner: GodotRunner, project_name: str = "", renderer: str = "forward_plus",
                 main_scene: str = "", timeout: float = 240.0) -> dict:
    """Развернуть папку в рабочий Godot-проект и, если задано, назначить главную сцену.

    Идемпотентна: если `project.godot` уже есть — ничего не пересоздаёт, только
    (при `main_scene`) назначает главную сцену.
    """
    root = Path(runner.project_root)
    pg = root / "project.godot"
    payload: dict = {"project": str(root), "created": False}

    if pg.exists():
        payload["message"] = "project.godot уже есть — проект не пересоздавали"
    else:
        key = (renderer or "forward_plus").strip().lower()
        render = RENDERERS.get(key)
        if render is None:
            return {"ok": False,
                    "error": f"неизвестный рендерер {renderer!r}; допустимо: "
                             f"{', '.join(sorted(RENDERERS))}"}
        name = (project_name or "").strip() or root.name
        existing = sorted(p.name for p in root.iterdir()) if root.exists() else []
        try:
            root.mkdir(parents=True, exist_ok=True)
            pg.write_text(MINIMAL_PROJECT.format(name=name, version=config.ENGINE_VERSION,
                                                 renderer=render), encoding="utf-8")
        except OSError as e:
            return {"ok": False, "error": f"не удалось записать project.godot: {e}"}

        res = runner.import_assets(timeout=timeout)
        expanded = pg.exists() and (root / ".godot").exists()
        payload.update({
            "created": True,
            "project_name": name,
            "renderer": render,
            "project_file": str(pg),
            "engine": config.ENGINE_VERSION,
            "seconds": round(res.seconds, 2),
            "godot_ok": res.ok,
            "godot_exit_code": res.exit_code,
        })
        if existing:
            payload["pre_existing_files"] = existing[:20]
        if not expanded:
            payload["ok"] = False
            payload["error"] = ("проект не развернулся: " +
                                ("; ".join(res.errors[:5]) or
                                 f"Godot завершился с кодом {res.exit_code}"))
            payload["stdout"] = res.stdout[-2000:]
            return payload

    if main_scene:
        ms = set_main_scene(runner, main_scene)
        payload["main_scene"] = ms
        if not ms.get("ok"):
            payload["ok"] = False
            payload["error"] = ms.get("error") or "не удалось назначить главную сцену"
            return payload

    payload.setdefault("ok", True)
    if payload["created"] and not main_scene:
        payload["next"] = ("Проект создан, но главная сцена не задана: "
                           "`godot_play_scene()` без аргумента её не найдёт. "
                           "Создай сцену и вызови godot_project_init(main_scene=\"...\").")
    return payload
