---
name: godot-decal-follow-body
description: >
  Прицепить эффект попадания (кровь, дырка, декаль, номер урона) к ДВИЖУЩЕМУСЯ телу в Godot 3D, чтобы он ехал вместе с ним, а не висел в воздухе на месте попадания. Использовать при жалобах «кровь остаётся на месте, а тело уже упало», «дырка от пули висит в воздухе», «декаль не едет с платформой», «номер урона отстаёт от врага», «эффект остался там, где был труп». Содержит: почему world-space эффект ломается на ригованной модели (клип смерти двигает КОСТИ, а не узел), рецепт BoneAttachment3D + выбор ближайшей кости, обязательный порядок `bone_name` до входа в дерево, граблю `Node.reparent()` который вызывает `_exit_tree` посередине и сжигает вывешенный якорь, фолбэк на `Visual` для не-ригованных целей, снятие по сигналу respawn и уборку якоря, плюс headless-пробник с замером «на сколько метров уехала декаль».
agent_created: true
---

# Декаль, которая едет вместе с телом

## 0. Симптом и почему он не лечится подгонкой координат

Игрок стреляет в NPC. Кровь появляется в точке попадания и **остаётся на месте**,
пока труп падает на пол. Выглядит как «декаль отвязалась от тела».

Причина не в координатах. Всё, что спавнится в мировых координатах
(`global_position = hit_point`), живёт в мире. Модель же умирает **анимацией**:
клип смерти двигает **кости** внутри `Skeleton3D`, а узел цели
(`AnimatableBody3D` / `CharacterBody3D`) при этом **не сдвигается ни на миллиметр**.
Проверяется одной строкой в пробнике — и это лучший аргумент в отчёте:

```
after 2.4 s: node moved 0.000 m, decal moved 1.207 m, decal y 1.20 -> 0.36
```

`node moved 0.000` — вот доказательство, что виноват не «не тот offset», а сама
привязка. Пока эффект висит на мире, ни один `offset` не поможет.

## 1. Рецепт: якорь на ближайшую кость

```gdscript
static func spawn(
	parent: Node, world_position: Vector3, world_normal: Vector3,
	kind: String = "concrete", follow: Node3D = null
) -> ImpactEffect:
	if parent == null or not parent.is_inside_tree():
		return null
	var effect := ImpactEffect.new()
	effect.name = "Impact"
	parent.add_child(effect)
	effect.global_position = world_position
	effect.setup(world_normal, kind)
	if follow != null and is_instance_valid(follow):
		effect.attach_to(follow)
	return effect


func attach_to(body: Node3D) -> void:
	var skeleton: Skeleton3D = _find_skeleton(body)
	if skeleton != null:
		var bone: int = _nearest_bone(skeleton, global_position)
		if bone >= 0:
			var anchor := BoneAttachment3D.new()
			anchor.name = "ImpactAnchor"
			# bone_name ДО входа в дерево - см. §2
			anchor.bone_name = skeleton.get_bone_name(bone)
			skeleton.add_child(anchor)
			# `_anchor` присваивать ТОЛЬКО ПОСЛЕ reparent - см. §3
			reparent(anchor, true)
			_anchor = anchor
			if body.has_signal("respawned"):
				body.connect("respawned", _on_body_respawned, CONNECT_ONE_SHOT)
			return
	# Не-ригованная цель (плита, проп): достаточно Visual, чтобы эффект
	# уехал с экрана вместе с ним.
	var visual: Node3D = body.get_node_or_null("Visual") as Node3D
	if visual != null:
		reparent(visual, true)
```

Ближайшая кость, а не «та, в которую попали»: декаль сохраняет собственный мировой
трансформ, поэтому кость нужна лишь та, которая **двигается так же**, как эта часть
тела. Искать по покою, в мировых координатах:

```gdscript
static func _nearest_bone(skeleton: Skeleton3D, world_point: Vector3) -> int:
	var best: int = -1
	var best_distance: float = INF
	var to_world: Transform3D = skeleton.global_transform
	for i in skeleton.get_bone_count():
		var at: Vector3 = to_world * skeleton.get_bone_global_pose(i).origin
		var d: float = at.distance_squared_to(world_point)
		if d < best_distance:
			best_distance = d
			best = i
	return best
```

`get_bone_global_pose()` — в локальных координатах скелета, поэтому обязателен
`global_transform` скелета. На 65 костях это десятки тысяч операций один раз на
попадание — не повод оптимизировать.

## 2. `bone_name` выставлять ДО `add_child`

`BoneAttachment3D` резолвит имя кости в индекс при входе в дерево. Имя, выставленное
после, **молча игнорируется**, `bone_idx` остаётся `-1`, и якорь висит в локальном
нуле скелета. Симптом: декаль не в точке попадания, а в ногах модели (или в её
начале координат), и ни одной ошибки в логе.

## 3. Главная грабля: `reparent()` вызывает `_exit_tree` посередине

`Node.reparent()` уводит узел из дерева и заводит обратно, то есть внутри вызова
проходит `NOTIFICATION_EXIT_TREE`. Если к этому моменту уже вывешен якорь, а в
`_exit_tree` лежит уборка («освободить якорь, чтобы не оставлять пустышку на
скелете»), то уборка снесёт **тот самый якорь, под который декаль как раз
прицепляется**.

Симптом в логе: **эффекта нет вообще** (`no impact effect spawned`), хотя выстрел
попал и урон прошёл. Объяснение: `queue_free()` на якоре отложенный, ближайший
`await get_tree().process_frame` в цикле стрельбы доходит до конца кадра — и якорь
удаляется вместе с прицепленным к нему эффектом. Декаль живёт ровно один кадр.

Лечение — **порядок двух строк**, а не отказ от уборки:

```gdscript
	skeleton.add_child(anchor)
	reparent(anchor, true)   # здесь отработает _exit_tree, _anchor ещё null
	_anchor = anchor         # вывешивать только теперь
```

Обратная сторона: если эффект уезжает на кость, **уборку якоря надо оставить в
`_exit_tree`** — якорь является РОДИТЕЛЕМ эффекта, и `queue_free()` эффекта его не
забирает. Без этого каждый выстрел по персонажу оставляет на скелете пустой
`BoneAttachment3D`:

```gdscript
func _exit_tree() -> void:
	if _anchor != null and is_instance_valid(_anchor):
		_anchor.queue_free()
		_anchor = null
```

Проверять в пробнике счётчиком: `anchors on the skeleton: 2 while wounded -> 0 after
the decals expired`. Именно `2`, а не `1`, если убийство заняло два выстрела —
считать надо **все** декали, иначе тест зелёный по недоразумению.

## 4. Пробник: замер вместо «посмотрел глазами»

Минимальная сцена строится кодом (камера + оружие + одна цель), цели
проставляется `max_health` на два попадания и `respawn_delay = 90`, чтобы труп не
встал посреди замера.

```gdscript
	# ... убить цель ...
	var decal: Node3D = _first_decal()          # группа "impact_effects"
	var p0: Vector3 = decal.global_position
	var node_at_hit: Vector3 = target.global_position
	await _wait(target.death_hold + 0.4)
	var moved: float = decal.global_position.distance_to(node_at_hit + CHEST_OFFSET)
	# VERDICT: moved > 0.30 м -> декаль едет с телом; ~0.000 -> осталась в мире
```

Запуск headless (быстро, без GPU), затем **отдельный прогон в окне** для пикселей —
цифры доказывают трансформ, но не то, что кровь видно на теле. Три кадра: попадание,
падение, на земле. Четвёртый кадр — после `death_hold`, и он обязан быть **пустым**:
это прямая проверка исходной жалобы «кровь висит, а тела уже нет».

Обязательный элемент стенда — **видимый пол** (`MeshInstance3D` + `BoxMesh` на том
же `StaticBody3D`). Без меша пола «висит в воздухе» неотличимо от «лежит на земле».

## 5. Чеклист

- [ ] `follow` протаскивается от того, кто вызвал спавн, до `attach_to`. Пропущенный
      аргумент — самая частая причина «фикс не сработал».
- [ ] Передавать **владельца урона**, а не коллайдер: попадание в голову приходит
      с голого `StaticBody3D`-хитбокса, под которым нет ни `Visual`, ни скелета.
- [ ] `bone_name` до `add_child`; `_anchor` после `reparent`.
- [ ] `respawned` → `queue_free()`: тело не должно вставать с прошлой раной.
- [ ] `_exit_tree` освобождает якорь.
- [ ] Пробник считает метры, а не «вроде норм».
- [ ] Обратная совместимость: у `spawn()` новый аргумент **по умолчанию `null`**, и
      вызов в три аргумента продолжает работать как world-space эффект.
