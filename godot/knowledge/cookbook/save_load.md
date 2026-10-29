# Save / load — Godot 4.7

## Что сохранять

Только **состояние**, не сцены. Сцены — это ассеты, их пересоздаёт движок.
Сохраняем: позиции, HP, инвентарь, прогресс, настройки.

## Формат

`user://save_01.json` — читаемо, отлаживаемо, версионируемо.

```gdscript
# save_manager.gd  (autoload)
extends Node

const SAVE_PATH := "user://save_01.json"
const SAVE_VERSION := 1

func save_game(data: Dictionary) -> bool:
	data["version"] = SAVE_VERSION
	data["saved_at"] = Time.get_datetime_string_from_system()
	var file := FileAccess.open(SAVE_PATH, FileAccess.WRITE)
	if file == null:
		push_error("Не удалось открыть файл для записи: %s" % FileAccess.get_open_error())
		return false
	file.store_string(JSON.stringify(data, "\t"))
	file.close()
	return true

func load_game() -> Dictionary:
	if not FileAccess.file_exists(SAVE_PATH):
		return {}
	var file := FileAccess.open(SAVE_PATH, FileAccess.READ)
	if file == null:
		return {}
	var text := file.get_as_text()
	file.close()
	var parsed: Variant = JSON.parse_string(text)
	if typeof(parsed) != TYPE_DICTIONARY:
		push_error("Повреждённый файл сохранения")
		return {}
	var data: Dictionary = parsed
	if int(data.get("version", 0)) > SAVE_VERSION:
		push_warning("Сохранение из более новой версии игры")
		return {}
	return data
```

## Сбор состояния

```gdscript
func collect_state() -> Dictionary:
	return {
		"player": {
			"position": [player.global_position.x, player.global_position.y, player.global_position.z],
			"health": player.get_node("HealthComponent").current,
		},
		"progress": {
			"level": GameState.current_level,
			"score": GameState.score,
		},
	}
```

Восстановление:

```gdscript
func apply_state(data: Dictionary) -> void:
	var p: Dictionary = data.get("player", {})
	var pos: Array = p.get("position", [0, 0, 0])
	player.global_position = Vector3(pos[0], pos[1], pos[2])
	player.get_node("HealthComponent").current = int(p.get("health", 100))
```

## Правила

- **`user://`**, не `res://` — в экспортированной игре `res://` только для чтения.
- Сохранять примитивы и массивы примитивов. `Vector3` в JSON превратится в строку —
  лучше `[x, y, z]` явно.
- Всегда писать поле `version` — иначе первое же изменение структуры сломает старые сейвы.
- Не сохранять `Object`/`Node` ссылки — только данные.
- Записывать во временный файл и переименовывать — защита от обрыва записи:
  ```gdscript
  var tmp := SAVE_PATH + ".tmp"
  # ... запись в tmp ...
  DirAccess.rename_absolute(ProjectSettings.globalize_path(tmp),
                            ProjectSettings.globalize_path(SAVE_PATH))
  ```

## Настройки (отдельно от сейва)

```gdscript
# settings.cfg — ConfigFile удобнее для настроек
var cfg := ConfigFile.new()
cfg.set_value("audio", "master", 0.8)
cfg.save("user://settings.cfg")
```

`ConfigFile` сохраняет типы нативно и не требует ручной сериализации.

## Грабли

- `JSON.stringify` не умеет `Vector3`, `Color`, `NodePath` — конвертировать вручную.
- `JSON.parse_string` возвращает `null` при ошибке, а не бросает исключение — проверять.
- `FileAccess.open` возвращает `null` при ошибке; проверять, а не использовать вслепую.
- Загрузка сейва в `_ready()` сцены — плохая идея: дочерние узлы ещё не готовы.
  Загружать и применять после `await get_tree().process_frame` или из меню.
