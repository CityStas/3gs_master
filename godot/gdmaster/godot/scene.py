"""Чтение и мутация .tscn.

Мутации выполняются не текстовой правкой, а самой Godot: генерируется
SceneTree-скрипт, который инстанцирует сцену, меняет дерево и сохраняет
PackedScene через ResourceSaver. Так .tscn остаётся валидным by construction.
"""
from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from pathlib import Path

from .paths import resolve, res_path, normalize
from .runner import GodotRunner
from ..rag.chunkers import _tscn_sections


@dataclass
class SceneNode:
    name: str
    type: str
    path: str
    parent: str
    script: str = ""
    properties: dict = field(default_factory=dict)
    children: list["SceneNode"] = field(default_factory=list)

    def flat(self) -> list["SceneNode"]:
        out = [self]
        for c in self.children:
            out.extend(c.flat())
        return out


def read_scene(scene_path: str, project_root: Path) -> dict:
    p = resolve(scene_path, project_root, must_exist=True)
    text = p.read_text(encoding="utf-8", errors="replace")
    sections = _tscn_sections(text)

    ext_res: dict[str, tuple[str, str]] = {}
    raw_nodes: list[tuple[str, str, str, dict, str]] = []
    for tag, attrs, body in sections:
        if tag == "ext_resource":
            ext_res[attrs.get("id", "")] = (attrs.get("type", ""), attrs.get("path", ""))
        elif tag == "node":
            name = attrs.get("name", "?")
            ntype = attrs.get("type", "")
            inst = attrs.get("instance", "")
            parent = attrs.get("parent", "")
            full = name if parent in ("", ".") else f"{parent}/{name}"
            full = re.sub(r"^\./", "", full)
            props: dict[str, str] = {}
            script = ""
            for b in body:
                m = re.match(r"^([A-Za-z_][\w/]*)\s*=\s*(.+)$", b.strip())
                if not m:
                    continue
                k, v = m.group(1), m.group(2)
                if k == "script":
                    rid = re.search(r'ExtResource\("([^"]+)"\)', v)
                    if rid:
                        script = ext_res.get(rid.group(1), ("", ""))[1]
                    continue
                props[k] = v
            raw_nodes.append((full, ntype or (f"[instance {inst}]" if inst else "Node"), parent, props, script))

    # построить дерево.
    # В формате Godot 4 у корневого [node] нет атрибута parent вообще,
    # а у детей он равен "." или пути родителя. Различать "" и "." обязательно.
    by_path: dict[str, SceneNode] = {}
    root_node: SceneNode | None = None
    for full, ntype, parent, props, script in raw_nodes:
        node = SceneNode(name=full.rsplit("/", 1)[-1], type=ntype, path=full,
                         parent=parent or ".", script=script, properties=props)
        by_path[full] = node
        if parent == "" and root_node is None:
            root_node = node
    if root_node is None and raw_nodes:
        root_node = by_path[raw_nodes[0][0]]

    for full, ntype, parent, props, script in raw_nodes:
        node = by_path[full]
        if node is root_node:
            continue
        if parent in ("", "."):
            root_node.children.append(node)
        elif parent in by_path:
            by_path[parent].children.append(node)
        else:
            root_node.children.append(node)

    def ser(n: SceneNode) -> dict:
        return {
            "name": n.name, "type": n.type, "path": n.path,
            "script": n.script, "properties": n.properties,
            "children": [ser(c) for c in n.children],
        }

    return {
        "scene": res_path(scene_path, project_root),
        "file": str(p),
        "node_count": len(raw_nodes),
        "root": ser(root_node) if root_node else None,
        "flat": [{"path": n.path, "type": n.type, "script": n.script,
                  "property_count": len(n.properties)} for n in (root_node.flat() if root_node else [])],
    }


# --------------------------------------------------------------------------
# GDScript-литералы
# --------------------------------------------------------------------------

_GD_EXPR_RE = re.compile(
    # [A-Za-z0-9]+ — в именах есть цифры: PackedInt32Array, PackedVector3Array.
    # С [A-Za-z]+ такие выражения не распознавались и уезжали в GDScript
    # СТРОКОЙ ("PackedInt32Array()"), то есть свойство получало текст.
    r"^(Vector[234](i)?|Vector[234]i|Color|NodePath|Rect2|Transform[23]D|Basis|Quaternion|AABB|Plane|"
    r"Callable|RID|StringName|Packed[A-Za-z0-9]+Array|Array|Dictionary|Object)\s*[\(\[]")
_INT_LITERAL_RE = re.compile(r"(?<![\w.])(\d+)(?![\w.])")
_STR_SPAN_RE = re.compile(r'"(?:[^"\\]|\\.)*"|\'(?:[^\'\\]|\\.)*\'')

#: Конструкторы, которые принимают ТОЛЬКО целые. Приводить в них литералы к
#: float нельзя: Vector2i(3.0, 4.0) — такая же ошибка компиляции, только с
#: другой стороны. Проверяется по имени сразу после открывающей скобки.
_INT_ONLY_HEADS = frozenset({
    "Vector2i", "Vector3i", "Vector4i",
    "PackedByteArray", "PackedInt32Array", "PackedInt64Array",
})


def _floatify_int_literals(expr: str) -> str:
    """Целые литералы внутри готового выражения Godot -> вещественные.

    Нужно, потому что конструкторы некоторых встроенных типов не принимают
    целые: `Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 5, -5)` — это ошибка
    КОМПИЛЯЦИИ GDScript («No constructor of "Transform3D" matches the signature
    "Transform3D(int, int, ...)"»), а не тихая конверсия. Модель пишет такие
    выражения естественно, и раньше вызов падал с невнятным Parse Error.
    Для Vector3/Color/... целые допустимы, так что приведение безопасно.

    Строковые литералы не трогаем: `Callable(obj, "run2")` должен остаться как есть.
    Целочисленные конструкторы (Vector2i, PackedInt32Array, ...) пропускаем целиком.
    """
    head = expr.split("(", 1)[0].split("[", 1)[0].strip()
    if head in _INT_ONLY_HEADS:
        return expr
    out: list[str] = []
    pos = 0
    for m in _STR_SPAN_RE.finditer(expr):
        out.append(_INT_LITERAL_RE.sub(r"\1.0", expr[pos:m.start()]))
        out.append(m.group(0))
        pos = m.end()
    out.append(_INT_LITERAL_RE.sub(r"\1.0", expr[pos:]))
    return "".join(out)


_NUM_ARG_RE = re.compile(r"^[+-]?(?:\d+\.?\d*|\.\d+)(?:[eE][+-]?\d+)?$")
_CALL_RE = re.compile(r"^([A-Za-z_][A-Za-z0-9_]*)\s*\(([^()]*)\)$")


def _split_numeric_args(expr: str):
    """(имя, [аргументы]) если expr — вызов с аргументами только из чисел."""
    m = _CALL_RE.match(expr)
    if not m:
        return None, None
    head, inner = m.group(1), m.group(2)
    if not inner.strip():
        return head, []
    parts = [p.strip() for p in inner.split(",")]
    if not all(_NUM_ARG_RE.match(p) for p in parts):
        return None, None
    return head, parts


def _rewrite_unsupported_ctor(s: str) -> str | None:
    """Переписать конструктор, которого в GDScript нет, в равносильный.

    `Transform3D(12 чисел)` и `Transform2D(6 чисел)` — это формат
    СЕРИАЛИЗАЦИИ .tscn/.tres, а не конструкторы GDScript. Проверено на
    Godot 4.7.2: обе формы дают ошибку компиляции «No constructor of
    "Transform3D" matches the signature "Transform3D(float, ...)"».
    Модель, начитавшись .tscn, пишет именно так, и вызов падает с Parse
    Error, по которому причина не видна (на прогоне — 4 итерации подряд).
    Существующие формы: Transform3D(Basis, Vector3), Transform2D(Vector2,
    Vector2, Vector2). Соответствие осей проверено round-trip'ом в Godot.
    """
    head, nums = _split_numeric_args(s)
    if head == "Transform3D" and nums is not None and len(nums) == 12:
        axes = ", ".join("Vector3(%s)" % ", ".join(nums[i:i + 3]) for i in (0, 3, 6))
        return f"Transform3D(Basis({axes}), Vector3({', '.join(nums[9:12])}))"
    if head == "Transform2D" and nums is not None and len(nums) == 6:
        axes = ", ".join("Vector2(%s)" % ", ".join(nums[i:i + 2]) for i in (0, 2, 4))
        return f"Transform2D({axes})"
    return None


def to_gd_literal(value) -> str:
    """JSON-значение -> выражение GDScript."""
    if value is None:
        return "null"
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (int, float)):
        return repr(value)
    if isinstance(value, str):
        s = value.strip()
        # уже готовое выражение Godot (Vector3(...), Color(...), NodePath(".."))
        if _GD_EXPR_RE.match(s):
            return _rewrite_unsupported_ctor(s) or _floatify_int_literals(s)
        if s in ("null", "true", "false", "inf", "-inf", "nan"):
            return s
        return json.dumps(value, ensure_ascii=False)
    if isinstance(value, list):
        return "[" + ", ".join(to_gd_literal(v) for v in value) + "]"
    if isinstance(value, dict):
        return "{" + ", ".join(f"{json.dumps(str(k))}: {to_gd_literal(v)}" for k, v in value.items()) + "}"
    return json.dumps(str(value), ensure_ascii=False)


def _q(s: str) -> str:
    """Строковый литерал GDScript."""
    return json.dumps(s, ensure_ascii=False)


def _node_lookup(var_name: str, node_path: str, root_expr: str = "__root") -> list[str]:
    """Строки GDScript, кладущие узел в var_name (или null, если не найден).

    Корень сцены адресуется как "", "." или "root" — в GDScript нет литерала
    кортежа, поэтому проверка идёт явными сравнениями. Плюс принимается
    СОБСТВЕННОЕ ИМЯ корня: godot_scene_tree отдаёт путь корня как его имя
    (например "Main3D"), и модель закономерно повторяет этот путь в других
    инструментах. Без этой ветки она получает «узел не найден: Main3D» по
    пути, который ей же и показал соседний инструмент (замерено на прогоне).
    """
    p = _q(node_path)
    return [
        f"var {var_name}: Node = {root_expr}",
        f"if {p} != \"\" and {p} != \".\" and {p} != \"root\" and {p} != String({root_expr}.name):",
        f"\t{var_name} = {root_expr}.get_node_or_null({p})",
    ]


def _op_script(runner: GodotRunner, scene_path: str, body_lines: list[str],
               timeout: float = 60.0) -> dict:
    rel = normalize(scene_path, runner.project_root)
    prelude = [
        f'var __scene_path: String = "res://{rel}"',
        "var __ps: PackedScene = load(__scene_path)",
        "if __ps == null:",
        '\t__res["error"] = "не удалось загрузить сцену: " + __scene_path',
        "\treturn",
        "var __root: Node = __ps.instantiate()",
        "if __root == null:",
        '\t__res["error"] = "не удалось инстанцировать сцену"',
        "\treturn",
    ]
    epilogue = [
        "var __new_ps := PackedScene.new()",
        "var __pack_err := __new_ps.pack(__root)",
        "if __pack_err != OK:",
        '\t__res["error"] = "pack() вернул код %d" % __pack_err',
        "\treturn",
        "var __save_err := ResourceSaver.save(__new_ps, __scene_path)",
        "if __save_err != OK:",
        '\t__res["error"] = "ResourceSaver.save вернул код %d" % __save_err',
        "\treturn",
        '__res["saved"] = true',
        '__res["scene"] = __scene_path',
        "__root.free()",
    ]
    res, payload = runner.exec_tree_script("\n".join(prelude + body_lines + epilogue), timeout=timeout)
    # Успех определяется результатом операции, а не шумом Godot в stdout:
    # пустой payload без "error" = операция прошла.
    if payload and "error" not in payload:
        payload["godot_ok"] = res.ok
        payload["godot_exit_code"] = res.exit_code
        return payload
    if not payload:
        payload = {"error": "; ".join(res.errors[:5]) or
                            f"Godot завершился с кодом {res.exit_code} и не записал результат"}
    payload["godot_ok"] = res.ok
    return payload


def add_node(runner: GodotRunner, scene_path: str, parent_path: str, node_type: str,
             node_name: str, properties: dict | None = None) -> dict:
    """Добавить узел в сцену.

    Две проверки типа стоят ДО `ClassDB.instantiate`, и это не формальность.
    Модель регулярно путает узел и ресурс: на прогоне она трижды позвала
    `add_node(node_type="StandardMaterial3D")` и получила сырую ошибку
    типизации GDScript («Trying to assign value of type 'StandardMaterial3D'
    to a variable of type 'Node'») — по ней непонятно, что делать. То же с
    несуществующими классами (`Scene3D`). Поэтому:

      * класс не существует      -> «неизвестный тип» + подсказка проверить имя;
      * класс есть, но не Node   -> «это РЕСУРС, а не узел» + как поступить.
    """
    props = properties or {}
    body = _node_lookup("__parent", parent_path)
    body += [
        "if __parent == null:",
        '\t__res["error"] = "родительский узел не найден: ' + parent_path + '"',
        "\treturn",
        f'if __parent.get_node_or_null({_q(node_name)}) != null:',
        '\t__res["error"] = "узел с именем ' + node_name + ' уже существует"',
        "\treturn",
        # node_type — либо имя класса Godot, либо путь к сцене (.gltf/.glb/.tscn).
        # Второй случай закрывает дыру, из-за которой модель уходила писать
        # .tscn руками: скачанный .gltf — это PackedScene, а не Mesh, и через
        # ClassDB его не создать. На прогоне из-за этого модель 15 раз
        # переписывала Main.tscn текстом и получала «Parse Error» без причины.
        f"var __t: String = {_q(node_type)}",
        "var __n: Node = null",
        'if __t.begins_with("res://") or __t.ends_with(".gltf") or __t.ends_with(".glb")'
        ' or __t.ends_with(".tscn") or __t.ends_with(".scn"):',
        "\tvar __ipath: String = __t",
        '\tif not __ipath.begins_with("res://"):',
        '\t\t__ipath = "res://" + __ipath',
        "\tif not ResourceLoader.exists(__ipath):",
        # Файл может лежать в проекте, но ещё не быть импортированным: только что
        # установленный .gltf Godot не видит до прохода импорта. Различаем эти
        # два случая — иначе модель ищет ошибку в пути, которого нет.
        "\t\tif FileAccess.file_exists(ProjectSettings.globalize_path(__ipath)):",
        '\t\t\t__res["error"] = __ipath + " есть на диске, но ещё не импортирован Godot. '
        'Вызови godot_check_project (он делает импорт), затем повтори."',
        "\t\telse:",
        '\t\t\t__res["error"] = "сцена не найдена: " + __ipath',
        "\t\treturn",
        "\tvar __ipack = load(__ipath)",
        "\tif __ipack == null:",
        '\t\t__res["error"] = "не удалось загрузить сцену: " + __ipath',
        "\t\treturn",
        "\tif not (__ipack is PackedScene):",
        '\t\t__res["error"] = __ipath + " — это не сцена (PackedScene), а " + type_string(typeof(__ipack))'
        ' + ". Инстанцировать как узел нельзя; для .tres-ресурсов используй godot_scene_set_property."',
        "\t\treturn",
        "\t__n = __ipack.instantiate()",
        "\tif __n == null:",
        '\t\t__res["error"] = "не удалось инстанцировать сцену: " + __ipath',
        "\t\treturn",
        '\t__res["instance_of"] = __ipath',
        "else:",
        "\tif not ClassDB.class_exists(__t):",
        '\t\t__res["error"] = "неизвестный тип: " + __t + " — такого класса в Godot нет. '
        'Проверь имя (например Node3D, MeshInstance3D, Camera3D)."',
        "\t\treturn",
        '\tif __t != "Node" and not ClassDB.is_parent_class(__t, "Node"):',
        '\t\t__res["error"] = __t + " — это РЕСУРС, а не узел, поэтому его нельзя добавить в сцену. '
        'Ресурсы создаются отдельно и назначаются через свойство '
        '(например godot_scene_set_property с material_override = путь к .tres)."',
        "\t\treturn",
        "\t__n = ClassDB.instantiate(__t)",
        "\tif __n == null:",
        '\t\t__res["error"] = "не удалось создать узел типа " + __t',
        "\t\treturn",
        f"__n.name = {_q(node_name)}",
        "__parent.add_child(__n)",
        "__n.owner = __root",
    ]
    for k, v in props.items():
        body += [
            f"if __n.get({_q(k)}) == null and not __n.has_method({_q(k)}):",
            f'\t__res.set({_q("warn_" + k)}, {_q(f"свойство {k} не найдено у {node_type}")})',
            f"__n.set({_q(k)}, {to_gd_literal(v)})",
        ]
    body.append('__res["node_path"] = str(__root.get_path_to(__n))')
    return _op_script(runner, scene_path, body)


def remove_node(runner: GodotRunner, scene_path: str, node_path: str) -> dict:
    body = _node_lookup("__n", node_path)
    body += [
        "if __n == null:",
        '\t__res["error"] = "узел не найден: ' + node_path + '"',
        "\treturn",
        "if __n == __root:",
        '\t__res["error"] = "нельзя удалить корень сцены"',
        "\treturn",
        '__res["removed"] = str(__n.name)',
        "__n.get_parent().remove_child(__n)",
        "__n.queue_free()",
    ]
    return _op_script(runner, scene_path, body)


def set_property(runner: GodotRunner, scene_path: str, node_path: str,
                 property_name: str, value) -> dict:
    """Установить свойство узла.

    Отдельная забота — ЧТО отвечать при промахе. Раньше инструмент говорил
    только «нет свойства X», и модель уходила в rag_search, чтобы узнать имя,
    тратя два шага на каждую попытку (замерено на прогоне: 4 таких промаха,
    `color` вместо `light_color`, `look_at` как свойство). Поэтому при промахе
    ответ несёт две подсказки:

      * «это метод, а не свойство» — если имя есть среди методов узла
        (`look_at`, `rotate_y` — их нельзя задать через свойство);
      * список ПОХОЖИХ свойств самого узла (`get_property_list()`), чтобы
        правильное имя находилось за один шаг, без похода в RAG.
    """
    body = _node_lookup("__n", node_path)
    body += [
        "if __n == null:",
        '\t__res["error"] = "узел не найден: ' + node_path + '"',
        "\treturn",
        "var __ok: bool = false",
        "for __p in __n.get_property_list():",
        f"\tif String(__p.get(\"name\", \"\")) == {_q(property_name)}:",
        "\t\t__ok = true",
        "\t\tbreak",
        "if not __ok:",
        f"\tvar __want: String = {_q(property_name)}",
        '\tvar __msg: String = "у узла %s (%s) нет свойства %s" % [__n.name, __n.get_class(), __want]',
        "\tif __n.has_method(__want):",
        '\t\t__msg += ". Это МЕТОД, а не свойство — через godot_scene_set_property его задать нельзя, вызывай из скрипта (.gd)."',
        "\tvar __cands: Array = []",
        "\tfor __p2 in __n.get_property_list():",
        '\t\tvar __nm: String = String(__p2.get("name", ""))',
        '\t\tif __nm.length() < 3 or __nm.begins_with("_") or __nm == __want:',
        "\t\t\tcontinue",
        "\t\tif __cands.size() >= 12:",
        "\t\t\tbreak",
        "\t\tif __nm.findn(__want) >= 0 or __want.findn(__nm) >= 0:",
        "\t\t\t__cands.append(__nm)",
        "\tif __cands.size() > 0:",
        '\t\t__msg += ". Похожие свойства: " + ", ".join(__cands)',
        '\t\t__res["similar_properties"] = __cands',
        "\t__res[\"error\"] = __msg",
        "\treturn",
        f"var __v = {to_gd_literal(value)}",
        # Ресурс, заданный строкой-путём, надо ЗАГРУЗИТЬ: Object.set() строку
        # в Resource-свойство не грузит. Замерено на прогоне: модель звала
        # set_property("Floor/FloorMesh", "material_override", "res://materials/floor.tres")
        # и получала ok:true при value "<Object#null>" — то есть молча ничего.
        # Молчаливый успех хуже отказа: модель считает работу сделанной.
        'if typeof(__v) == TYPE_STRING and String(__v).begins_with("res://"):',
        "\tvar __rp: String = String(__v)",
        "\tif not ResourceLoader.exists(__rp):",
        "\t\tif FileAccess.file_exists(ProjectSettings.globalize_path(__rp)):",
        '\t\t\t__res["error"] = __rp + " есть на диске, но ещё не импортирован Godot. '
        'Вызови godot_check_project (он делает импорт), затем повтори."',
        "\t\telse:",
        '\t\t\t__res["error"] = "ресурс не найден: " + __rp',
        "\t\treturn",
        "\tvar __rl = load(__rp)",
        "\tif __rl == null:",
        '\t\t__res["error"] = "не удалось загрузить ресурс: " + __rp',
        "\t\treturn",
        "\t__v = __rl",
        f"__n.set({_q(property_name)}, __v)",
        f"var __got = __n.get({_q(property_name)})",
        '__res["value"] = str(__got)',
        # set() на несовместимом типе ничего не делает и не жалуется. Поэтому
        # проверяем результат и говорим правду вместо бодрого ok:true.
        "if __v != null and __got == null:",
        "\tvar __tn: String = type_string(typeof(__v))",
        '\tvar __msg2: String = "свойство %s осталось пустым: значение типа %s не подошло." % ['
        f"{_q(property_name)}, __tn]",
        "\tif __v is PackedScene:",
        '\t\t__msg2 += " Это PackedScene (готовая сцена), а не значение-ресурс. Чтобы поставить .gltf/.tscn в проект, добавь узел-инстанс: godot_scene_add_node с node_type = путь к этой сцене."',
        '\t__res["warning"] = __msg2',
    ]
    return _op_script(runner, scene_path, body)


def attach_script(runner: GodotRunner, scene_path: str, node_path: str, script_path: str) -> dict:
    rel_script = normalize(script_path, runner.project_root)
    body = _node_lookup("__n", node_path)
    body += [
        "if __n == null:",
        '\t__res["error"] = "узел не найден: ' + node_path + '"',
        "\treturn",
        f'var __s: Script = load("res://{rel_script}")',
        "if __s == null:",
        '\t__res["error"] = "не удалось загрузить скрипт res://' + rel_script + '"',
        "\treturn",
        "__n.set_script(__s)",
        '__res["script"] = "res://' + rel_script + '"',
    ]
    return _op_script(runner, scene_path, body)


def connect_signal(runner: GodotRunner, scene_path: str, node_path: str, signal_name: str,
                   target_path: str, method: str) -> dict:
    body = _node_lookup("__n", node_path)
    body += _node_lookup("__t", target_path)
    body += [
        "if __n == null or __t == null:",
        '\t__res["error"] = "источник или цель сигнала не найдены"',
        "\treturn",
        f"if not __n.has_signal({_q(signal_name)}):",
        f'\t__res["error"] = "нет сигнала %s у %s" % [{_q(signal_name)}, __n.get_class()]',
        "\treturn",
        f"if not __t.has_method({_q(method)}):",
        f'\t__res["error"] = "у цели нет метода %s" % {_q(method)}',
        "\treturn",
        f"var __e: int = __n.connect({_q(signal_name)}, Callable(__t, {_q(method)}))",
        "if __e != OK:",
        '\t__res["error"] = "connect вернул код %d" % __e',
        "\treturn",
        '__res["connected"] = true',
    ]
    return _op_script(runner, scene_path, body)


_EXTRES_DECL_RE = re.compile(r'\[ext_resource\b[^\]]*?\bid\s*=\s*"([^"]+)"')
_EXTRES_REF_RE = re.compile(r'\bExtResource\(\s*"([^"]+)"\s*\)')
_SUBRES_DECL_RE = re.compile(r'\[sub_resource\b[^\]]*?\bid\s*=\s*"([^"]+)"')
_SUBRES_REF_RE = re.compile(r'\bSubResource\(\s*"([^"]+)"\s*\)')


def explain_tscn_parse_error(text: str) -> list[str]:
    """Назвать причину, по которой Godot не читает .tscn.

    Godot на битый .tscn говорит только «Parse Error» и номер строки. По
    такому сообщению причину не восстановить, и модель уходит перебирать
    кавычки: на прогоне — 15 итераций write_script/validate/read_file подряд,
    каждая следующая догадка («в .tscn нужны одинарные кавычки», «ExtResource
    требует путь без res://») была неверной. Поэтому проверяем ровно те
    правила формата, которые нарушаются чаще всего: ссылка на ресурс без
    объявления.
    """
    hints: list[str] = []

    declared_ext = set(_EXTRES_DECL_RE.findall(text))
    used_ext = set(_EXTRES_REF_RE.findall(text))
    missing_ext = sorted(used_ext - declared_ext)
    if missing_ext:
        hints.append(
            "Есть ссылки ExtResource(...) без объявления [ext_resource ...]. "
            "Godot требует сначала объявить ресурс, а в ссылке указывать его id, "
            "а не путь. Не объявлено: "
            + ", ".join(f'"{m}"' for m in missing_ext[:5])
            + '. Правильно: [ext_resource type="PackedScene" '
              'path="res://assets/external/pack/model.gltf" id="1_model"] '
              'и затем mesh = ExtResource("1_model").'
        )
    if used_ext and not declared_ext:
        hints.append(
            "Секции [ext_resource] в файле нет вообще. Это признак ручной записи "
            ".tscn текстом — так делать не нужно: Godot пишет сцены сам. "
            "Используй godot_scene_add_node с node_type = путь к .gltf/.tscn, "
            "тогда ext_resource проставит движок."
        )

    declared_sub = set(_SUBRES_DECL_RE.findall(text))
    used_sub = set(_SUBRES_REF_RE.findall(text))
    missing_sub = sorted(used_sub - declared_sub)
    if missing_sub:
        hints.append(
            "Есть ссылки SubResource(...) без объявления [sub_resource ...]. "
            "Не объявлено: " + ", ".join(f'"{m}"' for m in missing_sub[:5])
        )
    return hints


def validate_scene(runner: GodotRunner, scene_path: str, timeout: float = 45.0) -> dict:
    """Проверить, что .tscn действительно загружается и инстанцируется.

    Нужно потому, что `.tscn` можно записать и текстом (godot_write_script), а
    синтаксическая проверка GDScript такую сцену не ловит: битый текст молча
    ломает загрузку уже в рантайме. Здесь сцена реально грузится движком.
    Сцена НЕ сохраняется — это read-only проверка.
    """
    rel = normalize(scene_path, runner.project_root)
    script = "\n".join([
        f'var __scene_path: String = "res://{rel}"',
        "var __ps: PackedScene = load(__scene_path)",
        "if __ps == null:",
        '\t__res["error"] = "сцена не загружается (битый .tscn): " + __scene_path',
        "\treturn",
        "var __root: Node = __ps.instantiate()",
        "if __root == null:",
        '\t__res["error"] = "сцена не инстанцируется: " + __scene_path',
        "\treturn",
        "var __n: int = 1",
        "var __stack: Array = [__root]",
        # Сцена может грузиться без единой ошибки и при этом ничего не рисовать:
        # mesh, которому присвоили .gltf (PackedScene), молча остаётся null.
        # На прогоне модель именно так и отчиталась об успехе — сцена валидна,
        # запускается с 0 ошибок, а все четыре MeshInstance3D пустые.
        "var __empty_mesh: Array = []",
        "var __empty_shape: Array = []",
        "while __stack.size() > 0:",
        "\tvar __c: Node = __stack.pop_back()",
        "\tif __c is MeshInstance3D and __c.mesh == null:",
        "\t\t__empty_mesh.append(str(__root.get_path_to(__c)))",
        "\tif __c is CollisionShape3D and __c.shape == null:",
        "\t\t__empty_shape.append(str(__root.get_path_to(__c)))",
        "\tfor __ch in __c.get_children():",
        "\t\t__n += 1",
        "\t\t__stack.append(__ch)",
        '__res["ok"] = true',
        "__res[\"scene\"] = __scene_path",
        "__res[\"root_name\"] = str(__root.name)",
        "__res[\"root_type\"] = __root.get_class()",
        "__res[\"node_count\"] = __n",
        "if __empty_mesh.size() > 0:",
        '\t__res["empty_meshes"] = __empty_mesh',
        "if __empty_shape.size() > 0:",
        '\t__res["empty_shapes"] = __empty_shape',
        "__root.free()",
    ])
    res, payload = runner.exec_tree_script(script, timeout=timeout)
    if not payload:
        payload = {"error": "; ".join(res.errors[:5]) or
                            f"Godot завершился с кодом {res.exit_code} и не записал результат"}
    payload["godot_ok"] = res.ok
    payload["godot_exit_code"] = res.exit_code
    if res.errors:
        payload.setdefault("engine_errors", res.errors[:5])
    # Godot сказал «Parse Error» и номер строки — этого мало, чтобы починить.
    # Читаем файл сами и называем нарушенное правило формата.
    if not payload.get("ok"):
        try:
            text = (runner.project_root / rel).read_text(encoding="utf-8", errors="replace")
        except OSError:
            text = ""
        hints = explain_tscn_parse_error(text) if text else []
        if hints:
            payload["hints"] = hints
            payload["hint"] = " ".join(hints)
    else:
        # Сцена грузится — но это ещё не значит, что она что-то показывает.
        warns: list[str] = []
        empty_mesh = payload.get("empty_meshes") or []
        if empty_mesh:
            warns.append(
                "MeshInstance3D без меша (ничего не нарисует): " + ", ".join(empty_mesh[:8])
                + ". Частая причина — в свойство mesh записан .gltf: это PackedScene, а не Mesh, "
                  "и присваивание молча не срабатывает. .gltf ставится как узел: "
                  "godot_scene_add_node с node_type = путь к .gltf."
            )
        empty_shape = payload.get("empty_shapes") or []
        if empty_shape:
            warns.append(
                "CollisionShape3D без shape (коллизии не будет): " + ", ".join(empty_shape[:8])
                + ". Задай godot_scene_set_property с shape = путь к .tres, либо SubResource через "
                  "допустимую ручную правку .tscn."
            )
        if warns:
            payload["warnings"] = warns
    return payload


def create_scene(runner: GodotRunner, scene_path: str, root_type: str = "Node2D",
                 root_name: str = "Root") -> dict:
    rel = normalize(scene_path, runner.project_root)
    target = runner.project_root / rel
    if target.exists():
        return {"error": f"файл уже существует: res://{rel}"}
    target.parent.mkdir(parents=True, exist_ok=True)
    body = [
        f"var __root_new: Node = ClassDB.instantiate({_q(root_type)})",
        "if __root_new == null:",
        '\t__res["error"] = "неизвестный тип: ' + root_type + '"',
        "\treturn",
        f"__root_new.name = {_q(root_name)}",
        "var __ps2 := PackedScene.new()",
        "var __e2 := __ps2.pack(__root_new)",
        "if __e2 != OK:",
        '\t__res["error"] = "pack вернул %d" % __e2',
        "\treturn",
        f'var __se := ResourceSaver.save(__ps2, "res://{rel}")',
        "if __se != OK:",
        '\t__res["error"] = "save вернул %d" % __se',
        "\treturn",
        '__res["saved"] = true',
        f'__res["scene"] = "res://{rel}"',
        "__root_new.free()",
    ]
    res, payload = runner.exec_tree_script("\n".join(body))
    if payload and "error" not in payload:
        payload["godot_ok"] = res.ok
        return payload
    if not payload:
        payload = {"error": "; ".join(res.errors[:3]) or
                            f"Godot завершился с кодом {res.exit_code} и не записал результат"}
    return payload
