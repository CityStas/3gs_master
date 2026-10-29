# CharacterBody3D movement — Godot 4.7

Правильный каркас управляемого 3D-персонажа.

```gdscript
extends CharacterBody3D

@export var walk_speed: float = 5.0
@export var sprint_speed: float = 8.0
@export var acceleration: float = 12.0
@export var jump_velocity: float = 4.8

func _physics_process(delta: float) -> void:
	if not is_on_floor():
		velocity += get_gravity() * delta

	if Input.is_action_just_pressed("jump") and is_on_floor():
		velocity.y = jump_velocity

	var input_dir: Vector2 = Input.get_vector("move_left", "move_right", "move_forward", "move_back")
	var direction: Vector3 = (transform.basis * Vector3(input_dir.x, 0.0, input_dir.y)).normalized()
	var target_speed: float = sprint_speed if Input.is_action_pressed("sprint") else walk_speed
	var target: Vector3 = direction * target_speed

	velocity.x = move_toward(velocity.x, target.x, acceleration * delta)
	velocity.z = move_toward(velocity.z, target.z, acceleration * delta)

	move_and_slide()
```

## Ключевые моменты

- `velocity` — **свойство** `CharacterBody3D`. `move_and_slide()` не принимает аргументов
  (в Godot 3 было `move_and_slide(velocity, Vector3.UP)`).
- `get_gravity()` возвращает гравитацию из Project Settings; можно заменить на
  `@export var gravity: float = 9.8` и `velocity.y -= gravity * delta`.
- `Input.get_vector()` уже нормализует диагонали — не нужно `normalized()` на 2D-векторе.
- `transform.basis * Vector3(...)` переводит ввод в локальные оси персонажа. Это то, что
  делает движение «относительно камеры», когда персонаж поворачивается за мышью.
- `is_on_floor()` возвращает `false` до первого `move_and_slide()`. Не проверяй его
  в `_ready()`.
- `move_toward()` даёт плавный разгон/торможение. Для мгновенного отклика — присваивание.

## Прыжок

- `velocity.y = jump_velocity` **до** `move_and_slide()`.
- Для прыжка с удержанием (variable jump height): в `_physics_process` при
  `Input.is_action_just_released("jump")` и `velocity.y > 0` умножить `velocity.y` на 0.5.
- Coyote time: сохранять `_coyote_timer` при `is_on_floor()`, обнулять при прыжке,
  разрешать прыжок пока таймер > 0.

## Трение

Не вычитать вручную. Либо `move_toward` к нулю, либо свойства `floor_friction` /
`floor_stop_on_slope` у `CharacterBody3D`.

## Чего не делать

- Не двигать через `position +=` — потеряешь коллизии.
- Не вызывать `move_and_slide()` дважды за кадр.
- Не смешивать `RigidBody3D`-подход (`apply_force`) с `CharacterBody3D`.
