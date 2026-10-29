#!/usr/bin/env python3
"""Проверка уровня `level*.json` против формата (`LEVEL-SCHEMA.md`).

Зачем отдельный инструмент. Ошибки формата уровня **тихие**: `scene.js` при
неизвестном свойстве просто не входит в свою ветку и ничего не рисует, а
неизвестный ключ текстуры превращается в запрос `/имя` и 404 в консоли. Ни
компилятор, ни гейт этого не видят - гейт проверяет, что страница поднялась, а
не что на ней что-то есть. В итоге «уровень собрался» и «уровень пустой»
выглядят одинаково.

Поэтому проверка отдельная и говорит человеческим языком: где, что не так и
как надо. Код возврата 1, если есть ошибки (предупреждения код не меняют).

    python tools/level_lint.py projects/games/<имя>/web3d/level.json
    python tools/level_lint.py projects/games/<имя>/web3d/level_1/level.json
    python tools/level_lint.py --warn-as-error <путь>

Проверяется только СХЕМА, а не замысел: линтер не знает, что уровень должен
быть проходимым. Смотреть глазами всё равно надо.
"""
from __future__ import annotations

import argparse
import json
import pathlib
import sys

# Типы, которые понимает scene.js::buildVisual и engine.js::World.
# Тип вне списка - не ошибка рантайма (scene.js сделает из него Group), но это
# почти всегда опечатка, поэтому считаем ошибкой: узел молча ничего не нарисует.
KNOWN_TYPES = {
    "Node2D", "StaticBody2D", "CharacterBody2D", "Area2D", "RigidBody2D",
    "Sprite2D", "AnimatedSprite2D", "ColorRect", "Parallax2D",
    "CollisionShape2D", "CollisionPolygon2D", "Camera2D", "Marker2D",
}

# Свойства, которые scene.js реально читает. Остальное он игнорирует молча,
# поэтому «свойство, которого нет в списке» - предупреждение, а не ошибка:
# движок игры может читать своё (props.role, props.fly, props.hp...).
KNOWN_PROPS = {
    "position", "scale", "z_index", "offset", "flip_h", "flip_v",
    "texture", "frames", "animation", "autoplay",
    "color", "rect", "shape", "polygon",
    "scroll_scale", "repeat_size", "repeat_times", "limits",
}

IMAGE_EXT = {".png", ".jpg", ".jpeg", ".webp", ".gif", ".bmp", ".svg"}


def image_size(path: pathlib.Path) -> list[int] | None:
    """Размер картинки из её заголовка. None, если формат не разобран.

    Размер в `textures` становится размером плоскости, поэтому «на глаз» он
    врёт молча: спрайт растягивается, и ошибки при этом нет ни в консоли, ни в
    вёрстке. PNG и JPEG читаются без библиотек - только заголовок.
    """
    try:
        with open(path, "rb") as fh:
            head = fh.read(32)
            if head[:8] == b"\x89PNG\r\n\x1a\n":
                import struct
                return list(struct.unpack(">II", head[16:24]))
            if head[:2] == b"\xff\xd8":                       # JPEG: идём по маркерам
                fh.seek(2)
                while True:
                    b = fh.read(1)
                    if not b:
                        return None
                    if b != b"\xff":
                        continue
                    marker = fh.read(1)
                    while marker == b"\xff":
                        marker = fh.read(1)
                    if marker in (b"\xc0", b"\xc1", b"\xc2", b"\xc3"):
                        fh.read(3)
                        import struct
                        h, w = struct.unpack(">HH", fh.read(4))
                        return [w, h]
                    seg = fh.read(2)
                    if len(seg) < 2:
                        return None
                    fh.seek(int.from_bytes(seg, "big") - 2, 1)
    except OSError:
        return None
    return None

# Глубина, которую scene.js::layerDepth даёт по ИМЕНИ. Применяется только к
# корневому узлу дерева - у всех остальных глубина = родитель + z_index.
LAYER_DEPTH = {
    "Backdrop": -10000, "GameplayLayer": -800, "GameplayLayer2": -800,
    "Platforms": -600, "Props2": -400,
    "Player": 0, "EnemyLeft": 0, "Boss": 0,
}

# Частые опечатки в типе: подсказка важнее списка всех типов.
TYPE_HINT = {
    "Sprite": "Похоже, нужен `Sprite2D`",
    "Node": "Похоже, нужен `Node2D`",
    "Node2d": "Похоже, нужен `Node2D`",
    "TextureRect": "Похоже, нужен `Sprite2D`",
    "ColorRectangle": "Похоже, нужен `ColorRect`",
    "StaticBody": "Похоже, нужен `StaticBody2D`",
    "CharacterBody": "Похоже, нужен `CharacterBody2D`",
    "Area": "Похоже, нужен `Area2D`",
    "Camera": "Похоже, нужен `Camera2D`",
    "ParallaxLayer": "Похоже, нужен `Parallax2D`",
    "ParallaxBackground": "Похоже, нужен `Parallax2D`",
    "CollisionShape": "Похоже, нужен `CollisionShape2D`",
    "CollisionPolygon": "Похоже, нужен `CollisionPolygon2D`",
    "Label": "типа для текста нет: надпись рисуется картинкой и типом `Sprite2D`",
    "RichTextLabel": "типа для текста нет: надпись рисуется картинкой и типом `Sprite2D`",
    "Text": "типа для текста нет: надпись рисуется картинкой и типом `Sprite2D`",
    "TileMap": "тайлмапа нет: земля и фон — это `Sprite2D` с цельной картинкой",
    "TileMapLayer": "тайлмапа нет: земля и фон — это `Sprite2D` с цельной картинкой",
    "Line2D": "линий нет; контур рисуется `CollisionPolygon2D` (он же отладочный)",
    "Polygon2D": "полигона-заливки нет; цветная фигура — это `ColorRect`",
    "Control": "UI-типов нет: элементы интерфейса — `Sprite2D` в слое с нужным именем",
    "Panel": "UI-типов нет: элементы интерфейса — `Sprite2D` в слое с нужным именем",
    "AudioStreamPlayer2D": "звук уровнем не управляется; уберите узел",
    "AudioStreamPlayer": "звук уровнем не управляется; уберите узел",
    "Timer": "таймеров в уровне нет; время считает движок игры",
    "AnimatedSprite": "Похоже, нужен `AnimatedSprite2D`",
    "Marker2d": "Похоже, нужен `Marker2D`",
}


class Report:
    def __init__(self) -> None:
        self.errors: list[tuple[str, str]] = []
        self.warns: list[tuple[str, str]] = []
        # Свойства, которых scene.js не знает, собираются в один список: по строке
        # на свойство, а не на узел. Иначе десяток узлов с props.sprite/health
        # даёт полсотни строк и топит настоящие ошибки.
        self.unknown_props: dict[str, str] = {}
        self.bad_types: set[str] = set()
        # Имена слоёв, которым имя не дало глубину (см. LAYER_DEPTH): собираем,
        # чтобы сказать это одной строкой, а не по разу на узел.
        self.layer_name_no_z: set[str] = set()

    def err(self, where: str, msg: str) -> None:
        self.errors.append((where, msg))

    def warn(self, where: str, msg: str) -> None:
        self.warns.append((where, msg))

    def note_prop(self, prop: str, label: str) -> None:
        self.unknown_props.setdefault(prop, label)


def game_root(level_path: pathlib.Path) -> pathlib.Path | None:
    """Корень игры - каталог, внутри которого лежит `web3d/`.

    Пути в `textures`/`frames` записаны от него, потому что `scene.js` грузит
    `TEX_ROOT + ключ`, где `TEX_ROOT = '../'` и страница живёт в `web3d/`.
    """
    for parent in level_path.resolve().parents:
        if (parent / "web3d").is_dir():
            return parent
    return None


def is_num(v) -> bool:
    return isinstance(v, (int, float)) and not isinstance(v, bool)


def vec2(v) -> bool:
    return isinstance(v, list) and len(v) == 2 and all(is_num(x) for x in v)


def vec4(v) -> bool:
    return isinstance(v, list) and len(v) == 4 and all(is_num(x) for x in v)


def check_textures(rep: Report, tex, root: pathlib.Path | None) -> set[str]:
    used: set[str] = set()
    if not isinstance(tex, dict):
        rep.err("textures", "должен быть объектом {\"путь\": [ширина, высота]}")
        return used
    for key, val in tex.items():
        where = f"textures[{key!r}]"
        if not isinstance(key, str) or not key:
            rep.err(where, "ключ должен быть непустой строкой")
            continue
        # Главная ошибка формата: ключ-ИМЯ вместо ключа-ПУТИ.
        if "/" not in key.replace("\\", "/") and pathlib.Path(key).suffix.lower() not in IMAGE_EXT:
            rep.err(where, (
                f"«{key}» — это имя, а не путь. Ключ обязан быть путём от КОРНЯ ИГРЫ, "
                f"например «web3d/assets/{key}.png»: scene.js грузит TEX_ROOT + ключ, "
                f"поэтому с именем запрос уйдёт на /{key} и вернёт 404."))
            continue
        if isinstance(val, dict):
            rep.err(where, (
                "значение — объект, а должно быть размером [ширина, высота] в пикселях. "
                "Полей url/repeat/offset у текстуры НЕТ: repeat и offset — свойства "
                "узлов (Parallax2D.repeat_size, Sprite2D.offset)."))
            continue
        if not vec2(val):
            rep.err(where, f"размер должен быть [ширина, высота], а не {val!r}")
            continue
        if root is not None:
            f = root / key.replace("\\", "/")
            if not f.is_file():
                rep.err(where, f"файла нет: {f}")
            else:
                real = image_size(f)
                if real and real != list(val):
                    rep.err(where, (
                        f"размер записан {list(val)}, а файл на самом деле "
                        f"{real[0]}x{real[1]}. Размер становится размером плоскости: "
                        f"с неверным спрайт растянется или сожмётся, и ошибки при "
                        f"этом не будет ни одной"))
        used.add(key)
    return used


def check_frames(rep: Report, frames, root: pathlib.Path | None) -> set[str]:
    keys: set[str] = set()
    if not isinstance(frames, dict):
        rep.err("frames", "должен быть объектом {набор: {анимация: {frames: [...]}}}")
        return keys
    for set_name, anims in frames.items():
        keys.add(set_name)
        if not isinstance(anims, dict) or not anims:
            rep.err(f"frames[{set_name!r}]", "набор без анимаций — узел не нарисуется")
            continue
        # Частая ошибка: сюда кладут описание КАРТИНКИ (url/size) вместо кадров.
        if "url" in anims or "size" in anims:
            rep.err(f"frames[{set_name!r}]", (
                "это описание ТЕКСТУРЫ (url/size), а не анимация. frames — это кадры: "
                "{набор: {анимация: {frames: [путь, путь, …]}}}. Одна неподвижная картинка "
                "живёт в блоке textures и рисуется типом Sprite2D."))
            continue
        for anim_name, anim in anims.items():
            where = f"frames[{set_name!r}][{anim_name!r}]"
            if not isinstance(anim, dict):
                rep.err(where, "анимация должна быть объектом")
                continue
            lst = anim.get("frames")
            if not isinstance(lst, list) or not lst:
                rep.err(where, "нет непустого списка `frames` — кадров нет")
                continue
            for rel in lst:
                if not isinstance(rel, str) or not rel:
                    rep.err(where, f"кадр должен быть строкой-путём, а не {rel!r}")
                    continue
                if root is not None and not (root / rel.replace("\\", "/")).is_file():
                    rep.err(where, f"кадра нет: {root / rel}")
    return keys


def check_tree(rep: Report, tree, tex_keys: set[str], frame_keys: set[str]) -> None:
    if not isinstance(tree, dict):
        rep.err("tree", "должен быть объектом-узлом")
        return
    seen: dict[str, int] = {}

    def walk(node, prefix: str, is_root: bool) -> None:
        if not isinstance(node, dict):
            rep.err(prefix or "tree", f"узел должен быть объектом, а не {type(node).__name__}")
            return
        name = node.get("name")
        typ = node.get("type")
        label = node.get("path") or (f"{prefix}/{name}" if prefix and name else name) or prefix or "?"

        for field in ("type", "name", "props", "children"):
            if field not in node:
                extra = ""
                if field == "children":
                    extra = (" — scene.js обходит детей БЕЗ фолбэка "
                             "(`for (const child of node.children)`), без поля будет TypeError")
                rep.err(label, f"нет обязательного поля `{field}`{extra}")

        if not isinstance(typ, str) or not typ:
            rep.err(label, "`type` должен быть непустой строкой")
        elif typ not in KNOWN_TYPES:
            hint = TYPE_HINT.get(typ)
            rep.err(label, f"тип `{typ}` не поддерживается" + (f". {hint}" if hint else ""))
            rep.bad_types.add(typ)

        props = node.get("props")
        if props is None:
            props = {}
        if not isinstance(props, dict):
            rep.err(label, "`props` должен быть объектом (пустой — это {})")
            props = {}

        # Уникальность адреса: студия и файл правок адресуют узел по path.
        if isinstance(node.get("path"), str):
            seen[node["path"]] = seen.get(node["path"], 0) + 1
            if seen[node["path"]] == 2:
                rep.err(label, (f"`path` = {node['path']!r} встречается больше одного раза — "
                                f"студия и level_edit.json адресуют узел по path, "
                                f"второй узел будет недоступен"))

        pos = props.get("position")
        if pos is not None and not vec2(pos):
            rep.err(label, f"props.position должен быть [x, y], а не {pos!r}")
        if "scale" in props and not vec2(props["scale"]):
            rep.err(label, f"props.scale должен быть [sx, sy], а не {props['scale']!r}")

        if typ == "Sprite2D":
            if "sprite" in props:
                rep.err(label, (
                    f"props.sprite = {props['sprite']!r} — такого свойства нет. Спрайт "
                    f"ссылается на текстуру через props.texture, а сам ключ должен быть "
                    f"путём из блока textures."))
            tex = props.get("texture")
            if tex is None:
                rep.err(label, "Sprite2D без props.texture — узел не нарисуется (и молча)")
            elif not isinstance(tex, str):
                rep.err(label, "props.texture должен быть строкой-ключом из textures")
            elif tex not in tex_keys:
                rep.err(label, (f"props.texture = {tex!r} нет в блоке textures — "
                                f"узел не нарисуется (и молча)"))
        elif typ == "AnimatedSprite2D":
            fr = props.get("frames")
            if fr is None:
                rep.err(label, "AnimatedSprite2D без props.frames — узел не нарисуется")
            elif not isinstance(fr, str):
                rep.err(label, "props.frames должен быть строкой-ключом из frames")
            elif fr not in frame_keys:
                rep.err(label, f"props.frames = {fr!r} нет в блоке frames")
        elif typ == "ColorRect":
            if not vec4(props.get("color")):
                rep.err(label, f"ColorRect: props.color = {props.get('color')!r}, нужно [r, g, b, a] 0..1")
            if not vec4(props.get("rect")):
                rep.err(label, (f"ColorRect: props.rect = {props.get('rect')!r}, нужно "
                                f"[left, top, right, bottom] в локальных координатах вокруг position"))
        elif typ == "CollisionShape2D":
            shape = props.get("shape")
            size = shape.get("size") if isinstance(shape, dict) else None
            if not vec2(size):
                rep.err(label, (f"CollisionShape2D: props.shape.size = {size!r}, нужно "
                                f"{{shape: {{size: [w, h]}}}} — полный размер, не половина"))
        elif typ == "CollisionPolygon2D":
            poly = props.get("polygon")
            if not isinstance(poly, list) or len(poly) < 6 or len(poly) % 2:
                rep.err(label, (f"CollisionPolygon2D: props.polygon — ПЛОСКИЙ массив "
                                f"[x0, y0, x1, y1, …] чётной длины (>= 3 точек), а не список пар"))
            elif not all(is_num(v) for v in poly):
                rep.err(label, "CollisionPolygon2D: props.polygon должен состоять из чисел")
        elif typ == "Parallax2D":
            # Глубина от scroll_scale применяется ТОЛЬКО к корневому узлу дерева:
            # scene.js считает её по `parentObj === this.root`, а это верно лишь
            # для самого tree. У вложенного слоя глубина = родитель + z_index.
            if not is_root and "z_index" not in props:
                rep.warn(label, ("Parallax2D не в корне дерева и без z_index: глубину от "
                                 "scroll_scale получает только корневой узел, поэтому слой "
                                 "ляжет на глубину родителя. Задайте z_index явно "
                                 "(например -100, -99, -98)"))
            ss = props.get("scroll_scale")
            if ss is not None and not vec2(ss):
                rep.err(label, f"props.scroll_scale должен быть [sx, sy], а не {ss!r}")
        elif typ == "Camera2D":
            lim = props.get("limits")
            if lim is not None:
                if not isinstance(lim, dict):
                    rep.err(label, "props.limits должен быть объектом")
                else:
                    for k in ("limit_left", "limit_top", "limit_right", "limit_bottom"):
                        if k in lim and not is_num(lim[k]):
                            rep.err(label, f"props.limits.{k} должен быть числом")

        if is_root:
            # Имя корневого узла задаёт БАЗОВУЮ глубину ВСЕГО уровня: scene.js
            # вызывает layerDepth именно на нём. Имя слоя в корне (Platforms,
            # Backdrop) утопит или поднимет всю сцену целиком.
            if name in LAYER_DEPTH:
                rep.err(label, (f"корневой узел назван {name!r}, а это имя слоя: scene.js "
                                f"считает layerDepth именно для корня, поэтому ВЕСЬ уровень "
                                f"получит глубину {LAYER_DEPTH[name]:g}. Корень принято "
                                f"называть `Main`"))
        else:
            if name in LAYER_DEPTH and "z_index" not in props:
                rep.layer_name_no_z.add(name)

        for k in props:
            if k not in KNOWN_PROPS:
                rep.note_prop(k, label)

        kids = node.get("children")
        if kids is None:
            return
        if not isinstance(kids, list):
            rep.err(label, "`children` должен быть массивом")
            return
        for child in kids:
            walk(child, label if label != "?" else "", False)

    walk(tree, "", True)


def check_project(rep: Report, proj) -> None:
    if not isinstance(proj, dict):
        rep.err("project", "должен быть объектом")
        return
    cc = proj.get("clear_color")
    if cc is None:
        rep.err("project", ("нет clear_color — scene.js читает project.clear_color.slice(0,3) "
                            "без защиты, без него падение"))
    elif not (isinstance(cc, list) and len(cc) >= 3 and all(is_num(x) for x in cc)):
        rep.err("project", f"clear_color должен быть [r, g, b, a] 0..1, а не {cc!r}")
    elif any(not (0.0 <= x <= 1.0) for x in cc[:3]):
        rep.warn("project", (f"clear_color = {cc[:3]} вне 0..1. Цвета в файле — sRGB 0..1; "
                             f"значения 0..255 дадут белый экран"))
    vp = proj.get("viewport")
    if vp is not None and not vec2(vp):
        rep.err("project", f"viewport должен быть [w, h], а не {vp!r}")
    if "backdrop_color" in proj:
        rep.warn("project", "backdrop_color нигде не читается — можно убрать")


def lint(path: pathlib.Path) -> Report:
    rep = Report()
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        rep.err(str(path), "файла нет")
        return rep
    except json.JSONDecodeError as e:
        rep.err(str(path), f"это не JSON: {e}")
        return rep
    if not isinstance(data, dict):
        rep.err(str(path), "верхний уровень должен быть объектом")
        return rep

    for key in ("project", "textures", "frames", "tree"):
        if key not in data:
            rep.err(key, (f"нет обязательного ключа `{key}`. scene.js обращается к нему "
                          f"без проверки — пустой объект {{}} тоже годится, но ключ нужен"))

    root = game_root(path)
    if root is None:
        rep.warn(str(path), "не нашёл корень игры (каталог с web3d/) — файлы ассетов не проверяю")

    check_project(rep, data.get("project"))
    tex_keys = check_textures(rep, data.get("textures"), root)
    frame_keys = check_frames(rep, data.get("frames"), root)
    check_tree(rep, data.get("tree"), tex_keys, frame_keys)

    # Никто не ссылается — не ошибка, но обычно это забытый узел или мёртвая запись.
    # Кадры анимаций тоже считаем «использованными»: level_build.py кладёт их в
    # textures ради размеров, и без этого предупреждений набегает полсотни.
    used = set()
    for anims in (data.get("frames") or {}).values():
        if isinstance(anims, dict):
            for anim in anims.values():
                if isinstance(anim, dict) and isinstance(anim.get("frames"), list):
                    used.update(x for x in anim["frames"] if isinstance(x, str))

    def collect(node):
        if not isinstance(node, dict):
            return
        p = node.get("props") if isinstance(node.get("props"), dict) else {}
        if isinstance(p.get("texture"), str):
            used.add(p["texture"])
        for c in (node.get("children") or []):
            collect(c)
    collect(data.get("tree"))
    for k in sorted(tex_keys - used):
        rep.warn(f"textures[{k!r}]", "на эту текстуру никто не ссылается")

    return rep


def main() -> int:
    ap = argparse.ArgumentParser(description="Проверка формата level*.json")
    ap.add_argument("path", help="путь к level*.json (например web3d/level.json)")
    ap.add_argument("--warn-as-error", action="store_true",
                    help="считать предупреждения ошибками")
    args = ap.parse_args()

    path = pathlib.Path(args.path)
    rep = lint(path)

    print(f"{path}")
    for where, msg in rep.errors:
        print(f"  ОШИБКА  {where}: {msg}")
    for where, msg in rep.warns:
        print(f"  предупр. {where}: {msg}")
    if rep.bad_types:
        print(f"  (scene.js понимает только эти типы: {', '.join(sorted(KNOWN_TYPES))})")
    if rep.layer_name_no_z:
        names = ", ".join(sorted(rep.layer_name_no_z))
        print(f"  предупр. имена слоёв без z_index: {names}")
        print("           глубина по имени (Backdrop -10000, Platforms -600, …) достаётся")
        print("           ТОЛЬКО корневому узлу дерева. Ваши слои — дети, поэтому порядок")
        print("           задаёт порядок в children и z_index. Проставьте z_index")
        print("           каждому слою явно")
    if rep.unknown_props:
        names = ", ".join(sorted(rep.unknown_props))
        first = rep.unknown_props[sorted(rep.unknown_props)[0]]
        print(f"  предупр. свойства, которых scene.js не знает: {names}")
        print(f"           (например, в {first}) — их поймёт только движок игры, "
              f"если знает про них")
    print()
    n_err, n_warn = len(rep.errors), len(rep.warns) + (1 if rep.unknown_props else 0)
    if not n_err and not n_warn:
        print("формат в порядке.")
    else:
        print(f"{n_err} ошибок, {n_warn} предупреждений")
    if n_err or (args.warn_as_error and n_warn):
        print("\nФормат описан в LEVEL-SCHEMA.md — раздел про тот тип узла, на который ругается линтер.")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
