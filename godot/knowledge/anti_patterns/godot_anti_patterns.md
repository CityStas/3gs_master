# Anti-patterns — Godot 4.7

Список того, что агент НЕ должен писать. Каждый пункт — реальная ошибка,  
которая выглядит рабочей.

## Синтаксис Godot 3 в Godot 4

```gdscript
# ПЛОХО
extends KinematicBody2D
var sprite = Sprite.new()
func _ready():
    yield(get_tree().create_timer(1.0), "timeout")
    connect("pressed", self, "_on_pressed")
    export(int) var speed = 5
    onready var node = $Node
```

```gdscript
# ХОРОШО
extends CharacterBody2D
var sprite := Sprite2D.new()
func _ready() -> void:
    await get_tree().create_timer(1.0).timeout
    pressed.connect(_on_pressed)
    @export var speed: int = 5
    @onready var node: Node = $Node
```

## Обращение к узлам

```gdscript
# ПЛОХО — поиск в дереве каждый кадр
func _process(delta):
    get_node("../../UI/Label").text = str(score)
```

```gdscript
# ХОРОШО — один раз, через сигнал
@onready var score_label: Label = %ScoreLabel   # % = уникальное имя узла

func _ready() -> void:
    EventBus.score_changed.connect(_on_score_changed)

func _on_score_changed(value: int) -> void:
    score_label.text = str(value)
```

## Аллокации в кадре

```gdscript
# ПЛОХО
func _process(delta):
    var dir = Vector3(0, 0, 0)          # аллокация каждый кадр
    for e in get_tree().get_nodes_in_group("enemies"):
        var d = global_position.distance_to(e.global_position)
```

```gdscript
# ХОРОШО — кэш группы, обновление раз в N кадров
var _enemies: Array[Node] = []
var _tick: int = 0

func _ready() -> void:
    _enemies = get_tree().get_nodes_in_group("enemies")

func _physics_process(delta: float) -> void:
    _tick += 1
    if _tick % 10 != 0:
        return
    # ... тяжёлая работа раз в 10 физических кадров
```

## Прочее

| Антипаттерн                                        | Почему плохо                                     |
| -------------------------------------------------- | ------------------------------------------------ |
| `queue_free()` вместо пула для пуль/партиклов      | аллокации и фризы                                |
| `load()` в `_process`                              | диск/парсинг каждый кадр                         |
| `print()` в `_process`                             | вывод тормозит больше, чем кажется               |
| Правка `.tscn` текстовым редактором                | ломает `owner`, uid, формат                      |
| Один скрипт на 1000+ строк                         | нечитаемо, конфликты                             |
| Глубокая иерархия с `get_node("../../../..")`      | хрупко, ломается при реорганизации               |
| Глобальное состояние в статических переменных      | не сбрасывается между запусками                  |
| `@export` для рантайм-состояния (например `state`) | сохраняется в сцену, стартует не так             |
| `await` внутри `_process`                          | непредсказуемая частота                          |
| `Input.is_action_pressed` для разовых действий     | нужен `is_action_just_pressed`                   |
| Изменение физики из колбэка физики                 | `Can't change this state while flushing queries` |
| `visible = false` для «выключить логику»           | `_process` продолжает работать                   |
| Обращение к `global_position` в `_ready()`         | трансформ не финализирован                       |
| Изменение `scale` у `CollisionShape3D`             | коллизия рассинхронизируется с мешем             |
| Создание `Theme` на каждый `Control`               | дублирование ресурсов                            |

## Отдельно про агента

- **Не переписывать файл целиком ради одной правки.** Только точечный патч.
- **Не переименовывать** существующие члены и узлы: `.tscn` ссылается на них по имени.
- **Не «улучшать» попутно.** Запрошено X — делается X.
- **Не объявлять задачу выполненной без `godot_run_scene()` с `ok: true`.**
