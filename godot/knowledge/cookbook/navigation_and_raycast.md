# Navigation и Raycast — Godot 4.7

## NavigationAgent3D

```gdscript
extends CharacterBody3D

@export var speed: float = 3.5
@onready var agent: NavigationAgent3D = $NavigationAgent3D

func _ready() -> void:
	# Навигационный меш строится в первом физическом кадре.
	# Без ожидания первый путь будет пустым.
	await get_tree().physics_frame
	agent.path_desired_distance = 0.5
	agent.target_desired_distance = 0.5

func set_target(target: Node3D) -> void:
	agent.target_position = target.global_position

func _physics_process(delta: float) -> void:
	if agent.is_navigation_finished():
		velocity = Vector3.ZERO
		move_and_slide()
		return

	var next: Vector3 = agent.get_next_path_position()
	var direction: Vector3 = global_position.direction_to(next)
	direction.y = 0.0

	velocity.x = direction.x * speed
	velocity.z = direction.z * speed
	if not is_on_floor():
		velocity += get_gravity() * delta

	move_and_slide()
```

### Требования

- В сцене должен быть `NavigationRegion3D` с запечённым `NavigationMesh`.
- `NavigationAgent3D` — **ребёнок** персонажа.
- Без запечённой навигации `get_next_path_position()` вернёт текущую позицию и агент
  не сдвинется. Это не баг кода.

### 2D

`NavigationRegion2D` + `NavigationAgent2D`, логика идентична.

## RayCast3D

### Узел (обновляется каждый физический кадр)

```gdscript
@onready var ray: RayCast3D = $RayCast3D

func _physics_process(_delta: float) -> void:
	if ray.is_colliding():
		var hit: Node = ray.get_collider()
		var point: Vector3 = ray.get_collision_point()
		var normal: Vector3 = ray.get_collision_normal()
```

`RayCast3D` направлен по **-Z** локальной оси. Разворачивать через `rotation` или
`target_position`.

### Разовый луч (PhysicsDirectSpaceState3D)

```gdscript
func cast_ray(from: Vector3, to: Vector3, exclude: Array[RID] = []) -> Dictionary:
	var space := get_world_3d().direct_space_state
	var query := PhysicsRayQueryParameters3D.create(from, to)
	query.exclude = exclude
	query.collision_mask = 0xFFFFFFFF
	return space.intersect_ray(query)
```

Возвращает `{}` при промахе или `{"position", "normal", "collider", "collider_id", "rid", "shape"}`.

### Луч вниз от игрока

```gdscript
func ground_distance() -> float:
	var from: Vector3 = global_position
	var to: Vector3 = from + Vector3.DOWN * 5.0
	# Исключить собственный коллайдер — иначе луч попадёт в себя.
	var hit: Dictionary = cast_ray(from, to, [get_rid()])
	if hit.is_empty():
		return INF
	return from.distance_to(hit["position"])
```

## Грабли

- **`get_rid()`** у `CharacterBody3D` — RID физического тела. Без исключения луч
  попадёт в собственный коллайдер и `ground_distance()` вернёт 0.
- `PhysicsRayQueryParameters3D.create()` — статический метод; не конструировать вручную.
- `intersect_ray` вызывать **только** из `_physics_process` или после
  `await get_tree().physics_frame` — иначе `Can't change this state while flushing queries`.
- `NavigationAgent3D.target_position` — **глобальная** позиция, не локальная.
- При смене сцены уровень нужно перезапекать или использовать `NavigationRegion3D.bake_navigation_mesh()`.
