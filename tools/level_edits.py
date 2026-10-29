#!/usr/bin/env python3
"""Наложение конверта правок на дерево уровня: `nodes` + `add` + `remove`.

Один модуль на оба сборщика (`level_build.py` для level_1, `level_apply.py` для
level_0) намеренно. Правки пишет ОДИН редактор, и две копии этой логики, разойдясь,
дали бы разное поведение на одном и том же файле — «в одной игре добавилось, в
другой нет», и искали бы это в браузере, а не в коде.

Формат конверта (`web3d/<уровень>_edit.json`):

    {
      "level": "level1.json",
      "nodes":  { "<path>": [x, y] },             # позиции
      "add":    [ {path, type, parent, props} ],  # новые узлы
      "remove": [ "<path>", ... ]                 # удалённые узлы
    }

Идемпотентность — не украшение: инструмент гоняют повторно (человек правит,
сохраняет, пересобирает, правит снова), и каждый прогон накладывает файл ЗАНОВО
на перечитанный уровень.

  * `nodes` : путь не найден -> ОТКАЗ. Устаревшая правка означает, что дерево
    переименовали, а выравнивание человека осталось висеть в пустоте: он сохранил,
    пересобрал, и правка молча исчезла. «Тихо не сработало» здесь хуже, чем
    «громко упало».
  * `remove`: узла нет -> ПРОПУСК. Это значит, что удаление уже применилось на
    прошлом прогоне. Падать здесь — требовать ручной чистки файла после каждого
    успешного запуска.
  * `add`   : узел с таким путём уже есть -> обновляем props, НЕ дублируем. Иначе
    второй прогон удвоил бы добавленное.

Порядок применения: позиции -> remove -> add. Именно такой, потому что «удалил и
добавил заново» должно кончаться добавленным: если сделать наоборот, `remove`
снёс бы только что вставленный узел.
"""
from __future__ import annotations


def collect_paths(root: dict) -> dict[str, dict]:
    """path -> узел. Поле ПЛОСКОЕ; дубль пути — отказ, а не «возьмём первый»."""
    out: dict[str, dict] = {}

    def walk(n: dict) -> None:
        p = n.get("path")
        if p:
            if p in out:
                raise SystemExit(f"уровень: путь узла не уникален: {p}")
            out[p] = n
        for c in n.get("children") or []:
            walk(c)

    walk(root)
    return out


def _find_node(root: dict, path: str):
    """Узел по пути, либо None."""
    def walk(n: dict):
        if n.get("path") == path:
            return n
        for c in n.get("children") or []:
            got = walk(c)
            if got is not None:
                return got
        return None

    return walk(root)


def _locate(root: dict, path: str):
    """(родитель, индекс) для узла `path`, либо None.

    Индекс — позиция СРЕДИ ДЕТЕЙ родителя. Он нужен, чтобы вставить добавленный
    узел РЯДОМ с образцом: порядок детей в дереве — это порядок отрисовки внутри
    слоя, и «в конец списка» значило бы «поверх всего слоя».
    """
    def walk(n: dict):
        for i, c in enumerate(n.get("children") or []):
            if c.get("path") == path:
                return n, i
            got = walk(c)
            if got:
                return got
        return None

    return walk(root)


def _remove(root: dict, path: str) -> bool:
    """Вырезать узел `path` вместе с поддеревом. False — узла не было."""
    def walk(n: dict) -> bool:
        kids = n.get("children") or []
        for i, c in enumerate(kids):
            if c.get("path") == path:
                kids.pop(i)
                return True
            if walk(c):
                return True
        return False

    return walk(root)


def _node_from_spec(spec: dict) -> dict:
    """Спек редактора -> узел уровня.

    Два формата, и оба обязаны работать. Новый несёт готовый `props` (редактор
    копирует его у узла-образца), поэтому любой тип переносится как есть — у
    `ColorRect` остаются `rect` и `color`, у `Sprite2D` — `texture`. Старый несёт
    только `position`/`scale`/`texture`; его поддерживаем, чтобы уже сохранённые
    файлы правок не перестали открываться.
    """
    path = spec.get("path")
    if not path:
        raise SystemExit(f"add: у записи нет `path`: {spec!r}")
    props = spec.get("props")
    if not isinstance(props, dict):
        props = {}
        pos = spec.get("position")
        if pos:
            props["position"] = [float(pos[0]), float(pos[1])]
        if spec.get("scale"):
            props["scale"] = [float(spec["scale"][0]), float(spec["scale"][1])]
        if spec.get("texture"):
            props["texture"] = spec["texture"]
    return {
        "name": spec.get("name") or str(path).split("/")[-1],
        "type": spec.get("type") or "Node2D",
        "path": path,
        "props": dict(props),
        "children": [],
    }


def apply(root: dict, spec: dict, label: str) -> dict:
    """Наложить конверт на дерево `root` НА МЕСТЕ. Возвращает счётчики."""
    nodes = spec.get("nodes") or {}
    adds = spec.get("add") or []
    removes = spec.get("remove") or []
    # Секция могла прийти объектом (путь -> спек) — принимаем оба вида.
    if isinstance(adds, dict):
        adds = [dict(v, path=k) for k, v in adds.items()]

    by_path = collect_paths(root)
    gone = set(removes)

    # Путь, который в этом же прогоне удаляется, устаревшим не считается: он и
    # должен отсутствовать после применения.
    stale = [p for p in nodes if p not in by_path and p not in gone]
    if stale:
        raise SystemExit(
            f"{label}: узлы не найдены в дереве — пути устарели:\n  "
            + "\n  ".join(stale)
            + f"\nДерево переименовали, а правки остались. Удалите эти записи из "
              f"web3d/{label} (или поправьте пути) — иначе выравнивание молча "
              "не применится.")

    moved = 0
    for path, val in nodes.items():
        if path in gone:
            continue
        pos = val if isinstance(val, list) else val.get("position")
        if not pos or len(pos) != 2:
            raise SystemExit(f"{label}: {path}: ожидалось [x, y], получено {val!r}")
        new = [float(pos[0]), float(pos[1])]
        if by_path[path]["props"].get("position") != new:
            moved += 1
        by_path[path]["props"]["position"] = new

    removed = 0
    for path in removes:
        if _remove(root, path):
            removed += 1

    added = 0
    updated = 0
    for spec_i in adds:
        node = _node_from_spec(spec_i)
        path = node["path"]
        existing = collect_paths(root).get(path)
        if existing is not None:
            # Идемпотентность: узел уже вставлен прошлым прогоном. Обновляем props,
            # но НЕ трогаем position, если редактор его не прислал.
            existing["props"].update(node["props"])
            updated += 1
            continue
        # Куда вставлять. Приоритет — РЯДОМ С ОБРАЗЦОМ: «добавить копию блока» и
        # должно дать копию рядом с блоком, а не в конце слоя. Если образца нет
        # (или он не найден), кладём в конец явно указанного родителя.
        parent = None
        at = None
        if spec_i.get("from"):
            loc = _locate(root, spec_i["from"])
            if loc:
                parent, at = loc[0], loc[1] + 1
        if parent is None and spec_i.get("parent"):
            parent = _find_node(root, spec_i["parent"])
        if parent is None:
            raise SystemExit(
                f"{label}: add {path}: не нашёл родителя "
                f"(parent={spec_i.get('parent')!r}, from={spec_i.get('from')!r}).\n"
                f"Укажите `parent` — путь узла-слоя, например \"Platforms\". "
                f"Без него узел некуда вставить, а молча положить его в корень "
                f"значило бы изменить порядок отрисовки всего уровня.")
        kids = parent.setdefault("children", [])
        kids.insert(len(kids) if at is None else min(at, len(kids)), node)
        added += 1

    return {"nodes": len(nodes), "moved": moved,
            "added": added, "updated": updated, "removed": removed}
