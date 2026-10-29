# State machine — Godot 4.7

Паттерн конечного автомата без лишних абстракций: узел-владелец + enum состояний
для простых случаев, отдельные Node-состояния для сложных.

## Вариант 1 — enum (до ~6 состояний)

```gdscript
extends CharacterBody2D

enum State { IDLE, RUN, JUMP, ATTACK }

var state: State = State.IDLE

func _physics_process(delta: float) -> void:
	match state:
		State.IDLE:
			_state_idle(delta)
		State.RUN:
			_state_run(delta)
		State.JUMP:
			_state_jump(delta)
		State.ATTACK:
			_state_attack(delta)

func _change_state(new_state: State) -> void:
	if new_state == state:
		return
	_exit_state(state)
	state = new_state
	_enter_state(state)

func _enter_state(s: State) -> void:
	match s:
		State.ATTACK:
			$AnimationPlayer.play("attack")

func _exit_state(s: State) -> void:
	match s:
		State.ATTACK:
			pass
```

Плюс: никаких лишних узлов, всё в одном файле, легко читается.
Минус: функции всех состояний в одном скрипте.

## Вариант 2 — узлы-состояния (сложные персонажи)

```
Player (CharacterBody2D)  script: player.gd
├── StateMachine (Node)   script: state_machine.gd
│   ├── Idle (Node)       script: idle_state.gd
│   ├── Run (Node)        script: run_state.gd
│   └── Jump (Node)       script: jump_state.gd
```

```gdscript
# state_machine.gd
extends Node

var current_state: Node = null
@onready var owner_node: Node = get_parent()

func _ready() -> void:
	for child in get_children():
		child.state_machine = self
	current_state = get_child(0)
	current_state.enter()

func _physics_process(delta: float) -> void:
	if current_state:
		current_state.physics_update(delta)

func transition_to(state_name: String) -> void:
	var next: Node = get_node_or_null(state_name)
	if next == null or next == current_state:
		return
	current_state.exit()
	current_state = next
	current_state.enter()
```

```gdscript
# idle_state.gd
extends Node

var state_machine: Node
var player: CharacterBody2D

func _ready() -> void:
	player = state_machine.owner_node

func enter() -> void:
	player.get_node("AnimationPlayer").play("idle")

func physics_update(delta: float) -> void:
	if Input.get_axis("move_left", "move_right") != 0.0:
		state_machine.transition_to("Run")

func exit() -> void:
	pass
```

Плюс: каждое состояние изолировано, легко добавлять.
Минус: больше файлов, нужно аккуратно пробрасывать ссылку на владельца.

## Правило выбора

- Логика умещается в 150 строк → enum.
- Состояния имеют своё подсостояние, таймеры, анимации → узлы.

## Грабли

- **Не менять состояние прямо в `_enter_state` без защиты от рекурсии.** Лучше через
  `call_deferred("_change_state", ...)`, если переход происходит внутри `match`.
- Не забывать `_exit_state` — иначе останутся включёнными таймеры/анимации.
- `state` как `@export` в инспекторе даёт удобный дебаг, но сохраняет значение в сцену —
  при запуске игры персонаж может стартовать не в IDLE.
