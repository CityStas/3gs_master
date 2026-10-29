---
name: godot-glb-animation
description: >
  Завести GLB-модель в Godot и заставить её анимироваться: разбор GLB без Blender, headless-импорт, скрипты проверки клипов и скриншотов, prop-анимация без рига, свой риг в Blender и ретаргет библиотеки клипов. Триггеры: «модель не двигается», «AnimationPlayer пустой», «клип не находится по имени», «GLB без скелета», «ретаргет Mixamo/UAL».
agent_created: true
---

# GLB → Godot: анимация

## 0. Сначала посмотреть байты, а не картинку

Есть ли скелет и клипы — решается разбором GLB, без Blender и без Godot:

```python
import struct, json
def glb_json(p):
    d = open(p, 'rb').read()
    off = 12
    while off < len(d):
        clen, ctype = struct.unpack('<II', d[off:off+8])
        if ctype == 0x4E4F534A:          # 'JSON'
            return json.loads(d[off+8:off+8+clen])
        off += 8 + clen
j = glb_json(p)
print(len(j.get('skins', [])), len(j.get('animations', [])), j.get('asset'))
print([a['name'] for a in j.get('animations', [])])
print(j['accessors'][j['meshes'][0]['primitives'][0]['attributes']['POSITION']]['min'],
      j['accessors'][j['meshes'][0]['primitives'][0]['attributes']['POSITION']]['max'])
```

Решение по таблице:

| skins | animations | что можно |
|---|---|---|
| 0 | 0 | **только** prop-анимация (Transform3D/шейдер). Скелетная — невозможна |
| ≥1 | 0 | клипы надо писать самому (AnimationPlayer / Blender) |
| ≥1 | ≥1 | играть как есть; ретаргет на другой скелет — через BoneMap + SkeletonProfileHumanoid |

`min`/`max` POSITION дают рост и точку опоры: в Godot Y-up, если ступни не на y=0 — модель
провалится/взлетит над полом.

## 1. Проект и headless-импорт

`project.godot`:

```
config_version=5

[application]
config/name="<имя>"
run/main_scene="res://scenes/main.tscn"
config/features=PackedStringArray("4.7", "Forward Plus")
```

```bash
export APPDATA="C:\\Users\\<user>\\AppData\\Roaming"     # без него мусор в корне проекта
G="E:/Programs/distr/Godot_v4.7.2-stable_win64.exe"
"$G" --headless --path "<proj>" --import > _import.log 2>&1
```

Скобки и пробелы в имени папки (`Universal Animation Library[Standard]`) импорт не ломают.
Godot распаковывает текстуры glTF **рядом с исходником** (`<Name>_0.png` …).
В корне может появиться пустая `NVIDIA Corporation` (Vulkan pipeline cache) — удалять.

## 2. Сцена

`.tscn` руками. Инстанс GLB — обычный `PackedScene`:

```
[ext_resource type="PackedScene" path="res://path/Model.glb" id="2_m"]
...
[node name="Model" parent="." instance=ExtResource("2_m")]
```

Скрипт (HUD, перебор клипов) — минимальный:

```gdscript
extends Node3D
var _ap: AnimationPlayer
var _names: PackedStringArray

func _ready() -> void:
	_ap = find_anim_player(self)
	if _ap == null: push_error("нет AnimationPlayer"); return
	_names = _ap.get_animation_list(); _names.sort()
	print("[anim] клипов: %d" % _names.size())
	for n in _names:
		var a := _ap.get_animation(n)
		print("  %-24s len=%5.2fs loop=%d tracks=%d" % [n, a.length, a.loop_mode, a.get_track_count()])
	_ap.play(_names[0])

static func find_anim_player(root: Node) -> AnimationPlayer:
	if root is AnimationPlayer: return root
	for c in root.get_children():
		var r := find_anim_player(c)
		if r != null: return r
	return null
```

`AnimationPlayer` в импортированном GLB лежит **внутри** инстанса, а не на корне сцены —
искать рекурсивно. Треки: `tracks=56` на человеческом риге ≈ 55 костей + root.

## 3. Ловушка №1: `Transform3D(...)` в `.tscn` — это СТРОКИ

Проверено на 4.7.2: 12 чисел в `.tscn` заполняют **строки** базиса, поэтому

```
basis.x == (p0, p3, p6)
```

а `print(transform)` и `String()` показывают `[X: .., Y: .., Z: .., O: ..]` **по столбцам**.
Копипаста из `print` даёт транспонированную матрицу: камера/свет смотрят не туда, а модель
уезжает за кадр (симптом — «на скриншоте пусто, хотя позиция камеры правильная»).

**Правильный источник формата — `var_to_str()`** (тот же сериализатор, что у `.tscn`):

```gdscript
# tools/_calc_cam.gd, extends SceneTree
func _initialize() -> void:
	var cam := Camera3D.new()
	cam.fov = 38.0
	cam.look_at_from_position(Vector3(1.2, 1.1, 3.3), Vector3(0.0, 0.95, 0.0), Vector3.UP)
	print("tscn_transform = ", var_to_str(cam.transform))
	quit()
```

```bash
"$G" --headless --path "<proj>" --script res://tools/_calc_cam.gd
```

Второй симптом той же ловушки: свет «не светит», хотя `light_energy` в норме.

## 4. Ловушка №2: Godot срезает `_Loop` у имён glTF-клипов

`Idle_Loop` из файла → `Idle` в `AnimationPlayer`. При этом суффикс **управляет** loop_mode:
имя с `_Loop` → `LOOP_LINEAR`, без него → `LOOP_NONE`. Отсюда: `has_animation("Idle_Loop")`
== false, а `play("Idle_Loop")` молча ничего не делает (или падает в `push_warning`).

Терпимый резолвер имён:

```gdscript
func resolve(n: String) -> int:
	var i := _names.find(n)
	if i < 0 and n.ends_with("_Loop"): i = _names.find(n.substr(0, n.length() - 5))
	if i < 0 and not n.ends_with("_Loop"): i = _names.find(n + "_Loop")
	return i
```

Клипы без суффикса (`Death01`, `Punch_Jab`) играются один раз и замирают на последнем кадре —
для «зациклить» надо `AnimationPlayer.play(name, -1, speed)` с `Animation.loop_mode`.

## 5. Харнесс скриншотов (GPU, без человека)

Headless не рендерит — запускать **без** `--headless`, окно мигнёт.

```gdscript
# tools/shot.gd, extends Node; сцена tools/shot.tscn
ap.play(anim); ap.seek(t, true); ap.pause()   # pause() фиксирует позу
await get_tree().process_frame
await get_tree().process_frame
await RenderingServer.frame_post_draw
var img := get_viewport().get_texture().get_image()
img.save_png("res://out_shots/%s.png" % anim)
```

```bash
"$G" --path "<proj>" res://tools/shot.tscn -- --out res://out_shots \
     --shots "Idle:1.0,Walk:0.5,Punch_Jab:0.15"
```

- Аргументы — только через `OS.get_cmdline_user_args()` (после `--`).
- `|` в списке клипов ломается шеллом (rc=127) — разделитель **запятая**.
- `ap.pause()` перед кадром обязателен, иначе поза уплывает между `seek` и захватом.
- HUD-надпись обновляется вызовом метода сцены (`main.play_named(...)`), а не прямым
  `ap.play(...)` — иначе на скриншотах врёт.

### A/B «bind vs поза» — обязательный приём при отладке деформации

Сравнивать скриншоты из **разных** скриптов бессмысленно: у них разное кадрирование, и
разницу в масштабе легко принять за дефект геометрии (или наоборот). Нужен псевдоклип,
снимающий анимацию, — тогда bind и любая поза рендерятся одной камерой за один прогон:

```gdscript
# в скрипте сцены: служебный псевдоклип, не совпадающий ни с одним реальным именем
const BIND_CLIP := "__bind__"

func play_named(n: StringName) -> void:
	if str(n) == BIND_CLIP:
		_ap.stop()
		var sk := _find(self, "Skeleton3D") as Skeleton3D
		if sk != null:
			for i in sk.get_bone_count():
				sk.set_bone_pose_position(i, sk.get_bone_rest(i).origin)
				sk.set_bone_pose_rotation(i, sk.get_bone_rest(i).basis.get_rotation_quaternion())
				sk.set_bone_pose_scale(i, Vector3.ONE)
		return
	...
```

В харнессе для него надо **пропустить** обычную ветку `has_animation` / `resolve` / `seek`
(иначе `push_warning` и `continue`) и писать файл под именем `bind_t<время>.png`.

```bash
"$G" --path "<proj>" res://tools/shot.tscn -- --scene res://scenes/rigged.tscn \
     --out res://out_ab --shots "__bind__:0.0,Idle:0.8,Walk:0.5"
```

**И всегда удалять целевую папку перед прогоном** (`rm -rf out_ab`). Устаревший PNG от
прошлой версии ассета выглядит как актуальный результат — на этом легко потерять полчаса,
разбираясь с дефектом, которого уже нет.

## 6. Проба произвольного GLB (`tools/probe.gd`)

Печатает дерево, наличие `Skeleton3D` / `AnimationPlayer` / скина, AABB и снимает PNG,
**авто-кадрируя камеру** (без ручных матриц — обходит ловушку №3):

```gdscript
var center := aabb.get_center()
var radius := maxf(aabb.size.length() * 0.5, 0.001)
var dist := radius / tan(deg_to_rad(cam.fov * 0.5)) * 1.15
cam.look_at_from_position(center + Vector3(0.35, 0.28, 1.0).normalized() * dist, center, Vector3.UP)
```

```bash
"$G" --path "<proj>" res://tools/probe.tscn -- --model res://Model.glb --name probe
```

**Для любой новой сцены сначала гнать probe, а не писать матрицу камеры руками.**

## 7. Если у модели нет скелета — что реально можно

Порядок по возрастанию цены:

1. **Prop-анимация** (см. §7.1) — 15 минут, без Blender и без рига.
2. **Риг в Blender** (`E:\Programs\Blender\blender.exe`, 5.2): арматура по геометрии +
   `bpy.ops.object.parent_set(type='ARMATURE_AUTO')` (bone heat) → экспорт GLB со скелетом.
   На 500k+ вершинах bone heat считать долго; сначала decimate до ~30–50k.
3. **Ретаргет чужой библиотеки.** Нужен профиль: `Skeleton3D` → Import → `Bone Map` =
   `New BoneMap` → `profile = New SkeletonProfileHumanoid` → Reimport. Дальше клипы играются
   на любом скелете с этим BoneMap. **Пропорции решаются не этим**: чиби-модель (голова 40%
   роста, короткие руки) на гуманоидных клипах будет ломаться в суставах — сначала смотреть
   отношение `bbox.size.y / bbox.size.x` (у человека ≈ 3.8, у чиби ≈ 1.6).

### 7.1 Prop-анимация: AnimationPlayer по Transform3D пивота

Работает на любой статичной модели. Схема сцены:

```
Prop (Node3D, скрипт)
├── Camera3D            # кадр считается кодом, руками матрицу не писать (§3)
├── Sun (DirectionalLight3D)
├── Floor (MeshInstance3D, PlaneMesh)
└── Pivot (Node3D)                      # анимируем ЭТО
    ├── Model (instance GLB)            # смещён ступнями в 0
    └── Anim (AnimationPlayer)          # root_node = ".."  → Pivot
```

**Пивот — на ступнях.** Иначе вращение идёт вокруг пуза, а squash вдавливается в пол.
Смещение считать из AABB, а не хардкодить:

```gdscript
var box := _mesh_aabb(model)                       # merge get_aabb() по всем MeshInstance3D
var c := box.get_center()
model.position = Vector3(-c.x, -box.position.y, -c.z)
```

**Трек на свойство самого пивота** — путь `".:<prop>"`, потому что `root_node = ".."`:

```gdscript
func _track(a: Animation, prop: String) -> int:
	var t := a.add_track(Animation.TYPE_VALUE)
	a.track_set_path(t, NodePath(".:" + prop))     # .:position / .:rotation / .:scale
	a.track_set_interpolation_type(t, Animation.INTERPOLATION_CUBIC)
	return t
```

Клипы удобнее **генерировать кодом и сохранять в `.tres`**: тогда они сразу появляются
в Animation-панели и правятся руками, а при следующем запуске читаются с диска.

```gdscript
var path := "res://anims/%s.tres" % name
var a: Animation
if ResourceLoader.exists(path):
	a = load(path)
else:
	a = _make(name)
	a.resource_name = name
	ResourceSaver.save(a, path)                    # в debug/editor-сборке res:// пишется
var lib := _ap.get_animation_library(&"") if _ap.has_animation_library(&"") else AnimationLibrary.new()
if not _ap.has_animation_library(&""):
	_ap.add_animation_library(&"", lib)
lib.add_animation(name, a)
```

**Обязательная самопроверка привязки треков** (иначе клип «есть», но ничего не двигает):

```gdscript
_ap.play(clip)
var before := pivot.position
_ap.advance(0.4)                                   # advance() без ожидания кадров
print("selfcheck: %s -> %s  %s" % [before, pivot.position,
	("OK" if not before.is_equal_approx(pivot.position) else "НЕ ДВИГАЕТСЯ")])
_ap.stop()
```

Набор дешёвых клипов: `Idle_Bob` (позиция + микронаклон, loop), `Wobble` (качели по Z/X),
`Spin` (rotation.y 0→TAU с промежуточными ключами через 90°), `Breathe` (scale 1→1.04),
`Squash_Jump` (присед → вылет со stretch → посадка со squash, LOOP_NONE).
Loop задаётся `a.loop_mode = Animation.LOOP_LINEAR if loop else Animation.LOOP_NONE` —
на `.tres` с `loop_mode = 0` клип замирает на последнем кадре, это ожидаемо.

**Камера кадрируется по габариту КОНКРЕТНОГО клипа**, а не по статичному AABB:
статичный bbox → прыжок вылетает за кадр; общий по всем клипам → Idle получается крошечным.

```gdscript
var box := _mesh_aabb(model)
var up := 0.0; var stretch := 1.0
for t in anim.get_track_count():                       # только для нужного клипа
	var prop := str(anim.track_get_path(t)).get_slice(":", 1)
	for k in anim.track_get_key_count(t):
		var v: Variant = anim.track_get_key_value(t, k)
		if v is Vector3:
			if prop == "position": up = maxf(up, (v as Vector3).y)
			elif prop == "scale": stretch = maxf(stretch, maxf((v as Vector3).x, (v as Vector3).y))
box.size.y = box.size.y * stretch + up
# далее как в §6: dist = radius / tan(fov/2) * margin, margin ≈ 1.2
```

Кадрировать при каждой смене клипа (`play_named` / `play_index`), иначе харнесс снимет
чужой кадр.

Грабля GDScript: `var clips := [clip] if cond else _ap.get_animation_list()` не парсится —
вывод типа из Variant, а в проектах с warnings-as-errors это ошибка. Писать `var clips: Array = ...`.

Харнесс `tools/shot.gd` для этого нужен с `--scene`, а имя файла лучше делать
`<клип>_t<время>.png` — иначе два кадра одного клипа затирают друг друга:

```bash
"$G" --path "<proj>" res://tools/shot.tscn -- --scene res://scenes/prop.tscn \
     --out res://out_prop --shots "Idle_Bob:0.4,Squash_Jump:0.28,Squash_Jump:0.95"
```

## 7.2 Свой риг в Blender + ретаргет библиотеки на него

Кода нет в скилле — он в проекте: `blender/analyze_mesh.py`, `blender/silhouette.py`,
`blender/build_rig.py`, `blender/retarget.py`. Здесь — то, что нельзя вывести из логики.

### Где брать высоты суставов

**Не на глаз и не по пропорциям человека.** Сначала силуэт: срезы по Y + X-кластеризация
ширины прямо из BIN-чанка GLB (без Blender) → ортографический front/side с линейкой.
На чиби-модели (голова ~46% объёма) шея и пах на глаз промахиваются гарантированно.

### Bone heat падает на «сканах» (marching cubes, дубли вершин)

`bpy.ops.object.parent_set(type='ARMATURE_AUTO')` на выводе Trellis2/TripoSR отдаёт
«failed to find solution for one or more bones» и **100% вершин без весов**. Препроцесс
(`remove_doubles(1e-5)` + `delete_loose` + decimate до ~30k) не спасает. Свой скиннинг:

```python
# экспоненциальное ядро от расстояния точки до ОТРЕЗКА кости, top-4, нормализация
sigma = min(max(0.5 * bone_len, 0.022), 0.14)      # узкий sigma → локальнее деформация
W.append(np.exp(-((d / sigma) ** 2)))
# top-4 по весу, нормализация, квантование по 1/512, затем батчевый vg.add
```

Проверка результата — «вершин без весов = 0», иначе позы будут рвать меш.

### Импорт GLB: `disable_bone_shape=True` обязателен

Иначе импортёр добавляет в сцену `Icosphere` (кастомная форма кости, радиус 1) и он попадает
в расчёт габаритов: рост модели считается 2.0 вместо 0.92 → неверный масштаб ретаргета.
В Blender 5.2 у импортёра **нет** параметра `import_animations` (анимации тянутся всегда).

### Ретаргет: мировые матрицы + КОНСТАНТНЫЙ офсет rest→rest

Rest-позы источника и приёмника разные, поэтому переносить локальные каналы бессмысленно —
берём мировую ориентацию. Но **копировать её «как есть» — ошибка**: вместе с ориентацией
уезжает и чужой twist вокруг оси кости (roll), а у костей, чья ось совпала с опорным
вектором `align_roll`, roll вообще произвольный. Симптом: **в bind-позе меш чистый, при любой
анимации рвётся в клочья**, отдельные кости дают 180° проворот.

Правильно — один раз посчитать офсет и применять его покадрово:

```python
# один раз: dst_rest_world = src_rest_world @ off
off_rot[n] = src_rest.to_3x3().inverted() @ dst_rest.to_3x3()

# покадрово
rot = src_pose_world.to_3x3() @ off_rot[n]
```

Тогда при src-позе, равной src-rest, получаем ровно нашу rest, а переносится только мировая
дельта. Проверка на калибровочном клипе: если в библиотеке есть T-pose (в UAL это `A_TPose`),
он должен дать **0°** отклонения от нашей rest по всем костям. До фикса было 179.9°.

```python
pre      = parent_pose @ rest_rel[name]        # где кость оказалась бы в rest
desired  = Matrix.Translation(pre.translation) @ rot.to_4x4()
basis    = pre.inverted() @ desired            # локальный ключ
```

Позицию переносить только для `root`/`pelvis` и только дельтой от rest, с масштабом:

```python
scales = {"root": dst_height / src_height, "pelvis": dst_hip / src_hip}
pos = dst_root_rest + (src_m.translation - src_root_rest) * scales["root"]
```

Имена костей приёмника лучше сразу взять как у источника (`root, pelvis, spine_01..03,
neck_01, Head, clavicle/upperarm/lowerarm/hand_l|r, thigh/calf/foot/ball_l|r`) — маппинг
получается тождественным и совместим с UE-манекенными библиотеками.

**Диагностика за 10 секунд:** печатать направление кости как вектор
(`bone.matrix_local.to_3x3() @ Vector((0,1,0))`) для src_rest / src_pose / dst_rest. Векторы
читаются мгновенно, эйлеры — нет. Если src_rest_dir и dst_rest_dir не совпадают, а офсета
нет — ретаргет сломан.

### Скиннинг: top-K с мягким ядром рвёт меш

Расстояние до отрезка кости + экспоненциальное ядро + top-4 + нормировка даёт **разрывные
границы**: мягкое ядро делает много весов сопоставимыми, поэтому соседние вершины выбирают
разные наборы из 4 костей и при вращении расходятся. Симптом характерный: **одиночный сгиб
одной кости выглядит нормально, а клип с несколькими костями превращает конечности в лохмотья**.

Лечение — сгладить веса в пространстве и поднять K:

```python
def smooth_weights(co, W, radius=0.02, iterations=2, alpha=0.5):
    # соседи по РАВНОМЕРНОЙ СЕТКЕ, а не по топологии: меш из marching cubes со швами дублей,
    # рёбра ненадёжны. Для каждой вершины — усреднение W по соседям в радиусе (3x3x3 ячеек).
    ...
    out[i] = (1 - alpha) * W[i] + alpha * mean(W[neighbours])
# затем снова top-K и нормировка
```

Порядок: ядро → нормировка → сглаживание → top-K → нормировка. `k` брать 6, не 4.
Стоимость: ~20 с на 28k вершин (чистый Python + numpy, scipy в Blender нет). Размер GLB
не меняется. Флаги: `--smooth-radius 0.02 --smooth-iters 2 --topk 6 --no-smooth`.

### Decimate: не гадать, а снять две версии и положить рядом

Авто-риг на «скане» почти всегда требует decimate (668k полигонов в движок не нужны), но
ratio подбирается **по картинке, а не по числу**. Дешёвый способ решить: собрать второй риг
на другом ratio в отдельный файл, прогнать один и тот же тест поз и склеить верх/низ в одно
изображение. Порядок величин на модели ростом ~1 м (вывод Trellis2, 668k полигонов):

| ratio | полигонов | размер GLB | вид |
|---|---|---|---|
| 0.12 | 80k | 22.7 МБ | шерсть рваная, клочья иглами, рога щербатые |
| 0.30 | 200k | 30.6 МБ | шерсть гладкая, детали чистые |

Разница видна сразу, цена +31% размера — то есть **0.30 берётся почти бесплатно**, а 0.12
выбирают только из соображений веса. Учитывать: `weight_by_distance`/`smooth_weights`
работают по всем вершинам, поэтому рост ratio бьёт по времени сборки (33 с → 2 м 23 с), а не
только по размеру.

Текстуры при этом обычно весят больше меша (3× 2048² PNG = 15.7 МБ против 9.9 МБ геометрии) —
если надо ужать проект, начинать с них, а не с decimate.

### Гигиена `.godot/imported`

Кэш импорта копит записи от уже удалённых ассетов и дубли скриншотов: на этом проекте
разросся до 167 МБ / 145 файлов. Godot stale-записи сам не всегда убирает. Лечение:
`rm -rf .godot/imported` + `--import` → 107 МБ / 54 файла. Плюс `.gdignore` в каталоги со
скриншотами, иначе каждый прогон харнесса добавляет в кэш по текстуре.

### Экспорт: три ловушки подряд, все тихие

1. **Режим `ACTIONS` экспортирует только активную action + NLA-дорожки.** 43 забейканных
   клипа, лежащих в `bpy.data.actions` с `use_fake_user`, в GLB не попадут вообще.
   Каждую — в свою дорожку:

   ```python
   ad = arm.animation_data or arm.animation_data_create()
   ad.action = None
   for act in actions:
       tr = ad.nla_tracks.new(); tr.name = act.name
       st = tr.strips.new(act.name, int(act.frame_range[0]), act); st.name = act.name
       if hasattr(st, "action_slot") and len(act.slots):
           st.action_slot = act.slots[0]
       tr.mute = False
   ```

2. **Коллизия имён.** `bpy.data.actions.new("Idle_Loop")` при уже существующем `Idle_Loop`
   даёт `Idle_Loop.001` — и имя клипа в Godot уезжает. Сразу после импорта источника
   переименовать его actions в `src__<name>`, а перед экспортом удалить и объекты источника,
   и все `src__*` actions. Иначе **исходные клипы перекрывают бейк**: в GLB уедут анимации,
   нацеленные на 65 костей манекена, а наш 23-костный скелет останется без клипов.

3. **Blender 4.4+ slotted actions: у `Action` больше нет `.fcurves`** — кривые в
   `action.layers[].strips[].channelbags[].fcurves`. Нужен обходчик с фолбэком на legacy,
   иначе падает всё, что трогает `act.fcurves` (например установка интерполяции).

### Проверка: разбирать JSON-чанк, а не смотреть на размер файла

«Экспорт прошёл, 25 МБ» ничего не значит — ровно так был получен GLB, где 43 клипа целились
в чужой скелет. Критерий годности:

```python
j = glb_json(out)
assert len(j["skins"]) == 1 and len(j["meshes"]) == 1
tg = {c["target"]["node"] for a in j["animations"] for c in a["channels"]}
assert all(nodes[i]["name"] in my_bone_names for i in tg)   # 23, не 65
```

В Godot это же видно как `Skeleton3D: 2` в `tools/probe.gd` и раздутый AABB
(1.94×2.32×0.46 вместо 0.58×0.92×0.46).

Полезный счётчик после бейка: `fcurves == bones*4 + translated*3` (для 23 костей и двух
смещаемых — 98). Ноль кривых означает, что `keyframe_insert` писал не туда (частая причина —
не выставленный `animation_data.action_slot`).

### Мелочи

- `rigged/*.blend` внутри проекта Godot → Godot пытается его импортировать и вешается.
  `.blend` держать вне проекта.
- Параллельные `Edit` к одному файлу теряют правки (первая не записывается, хотя инструмент
  рапортует успех) — правки одного файла делать последовательно и сверять grep'ом.
- Дешёвый smoke-тест сцены без окна: `"$G" --headless --path <proj> --quit-after 90`.


