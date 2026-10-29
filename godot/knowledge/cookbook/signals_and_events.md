# Signals и автолоады — Godot 4.7

## Подключение сигналов

```gdscript
# Godot 4 (правильно)
button.pressed.connect(_on_button_pressed)
timer.timeout.connect(_on_timer_timeout)
area.body_entered.connect(_on_body_entered)

# с параметрами
button.pressed.connect(_on_pressed.bind(item_id))

# одноразовое
timer.timeout.connect(_on_timeout, CONNECT_ONE_SHOT)
```

```gdscript
# Godot 3 (НЕ работает в 4.x)
button.connect("pressed", self, "_on_button_pressed")
```

## Объявление и испускание

```gdscript
extends Node

signal health_changed(current: int, maximum: int)
signal died

var _health: int = 100

func take_damage(amount: int) -> void:
	_health = maxi(0, _health - amount)
	health_changed.emit(_health, 100)
	if _health == 0:
		died.emit()
```

## Автолоад-шина событий

Для развязки систем, которые не должны знать друг о друге.

```gdscript
# res://autoload/event_bus.gd  (Project Settings → Autoload → EventBus)
extends Node

signal player_died
signal score_changed(new_score: int)
signal level_completed(level_id: int)
```

Использование:

```gdscript
EventBus.score_changed.emit(1500)          # отправитель
EventBus.score_changed.connect(_on_score)  # получатель
```

Правила:
- Автолоад — **только** для действительно глобального.
- Не хранить в EventBus состояние игры; для этого отдельный `GameState`.
- Имена сигналов — прошедшее время, без префикса `on_`.

## Компоненты на сигналах

```gdscript
# health_component.gd
class_name HealthComponent
extends Node

signal changed(current: int, maximum: int)
signal depleted

@export var max_health: int = 100
var current: int

func _ready() -> void:
	current = max_health

func apply_damage(amount: int) -> void:
	if amount <= 0:
		return
	current = maxi(0, current - amount)
	changed.emit(current, max_health)
	if current == 0:
		depleted.emit()
```

Владелец:

```gdscript
@onready var health: HealthComponent = $HealthComponent

func _ready() -> void:
	health.depleted.connect(_on_health_depleted)
	health.changed.connect(_on_health_changed)
```

## Грабли

- Сигнал **не** вызовет метод, если `connect` сделан после `emit`. Порядок: подписка в
  `_ready`, эмит — по событию.
- `Callable` на метод удалённого узла остаётся живым и упадёт. При удалении узла
  с подписками — `disconnect` или проверка `is_instance_valid`.
- `await signal_name` ждёт ровно один эмит:
  ```gdscript
  await get_tree().create_timer(1.0).timeout
  ```
- `connect` на уже подключённый сигнал → ошибка `Signal is already connected`.
  Проверять `is_connected` или подключать один раз в `_ready`.
