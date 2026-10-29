# Object pooling — Godot 4.7

Пул для пуль, частиц, врагов и любого объекта, который создаётся/удаляется часто.

## Почему

`instantiate()` + `queue_free()` в цикле — это аллокации и фризы. Пул переиспользует
готовые инстансы: `set_active(false)` вместо удаления.

## Реализация

```gdscript
# object_pool.gd
class_name ObjectPool
extends Node

@export var scene: PackedScene
@export var initial_size: int = 20
@export var max_size: int = 200

var _available: Array[Node] = []
var _active: Array[Node] = []

func _ready() -> void:
	for i in initial_size:
		_available.append(_create())

func _create() -> Node:
	var node: Node = scene.instantiate()
	node.set("pool", self)
	node.process_mode = Node.PROCESS_MODE_DISABLED
	add_child(node)
	node.hide()
	return node

func spawn(position: Vector3, rotation_y: float = 0.0) -> Node:
	var node: Node
	if _available.is_empty():
		if _active.size() >= max_size:
			return null
		node = _create()
	else:
		node = _available.pop_back()

	_active.append(node)
	node.global_position = position
	if node is Node3D:
		node.rotation.y = rotation_y
	node.process_mode = Node.PROCESS_MODE_INHERIT
	if node is CanvasItem:
		node.show()
	if node.has_method("activate"):
		node.call("activate")
	return node

func release(node: Node) -> void:
	if not _active.has(node):
		return
	_active.erase(node)
	node.process_mode = Node.PROCESS_MODE_DISABLED
	if node is CanvasItem:
		node.hide()
	if node.has_method("deactivate"):
		node.call("deactivate")
	_available.append(node)
```

## Объект пула

```gdscript
extends Area3D

var pool: ObjectPool
@export var lifetime: float = 3.0
var _timer: float = 0.0

func activate() -> void:
	_timer = lifetime
	monitoring = true

func deactivate() -> void:
	monitoring = false

func _physics_process(delta: float) -> void:
	_timer -= delta
	if _timer <= 0.0:
		pool.release(self)
```

## Правила

- **`queue_free()` не вызывать.** Только `release()`.
- `process_mode = PROCESS_MODE_DISABLED` для неактивных — они не тратят `_process`.
- При `release` сбрасывать всё, что могло измениться: `monitoring`, `visible`,
  `rotation`, `velocity`, счётчики. Иначе объект «приедет» с прошлого раза.
- Не использовать пул для объектов, которые живут долго и редко создаются.

## Грабли

- `hide()` на `Node3D` не существует — это `CanvasItem`. Для 3D использовать
  `visible = false` (есть у `Node3D` через `GeometryInstance3D`/`Node3D.visible`).
- `_active.has(node)` — линейный поиск. Для сотен объектов держать `Dictionary` id→node.
- Если объект сам себя освобождает через `queue_free()`, пул получит мёртвую ссылку.
