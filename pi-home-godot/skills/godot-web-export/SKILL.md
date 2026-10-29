---
name: godot-web-export
description: >
  Веб-сборка Godot под деплой: рендерер, вес pck, загрузочная шторка, медленный старт из-за шейдеров. Триггеры: «сделай веб версию», «залью на vercel», «чёрный экран в браузере», «лоадер висит», «сборка весит слишком много», «игра не стартует на сайте, а локально работает».
agent_created: true
---

# Godot web-export: сборка, деплой, вес, загрузочная шторка

Вынесено из скилла `godot-headless-assets`, где это были §18-23. Нумерация здесь
своя, с единицы; ссылки вида «§9» ведут в `godot-headless-assets` (там это смоук
web-сборки в Playwright).

## 1. Веб-сборка под деплой: рендерер, размер, MIME

Проект Bubble Peaks (Godot 4.7.2, Forward+ на десктопе) собирался в `web_ver/`
для показа на Vercel. Пайплайн §5 и §9 из `godot-headless-assets` работает, но всплыли четыре вещи, которых
там нет.

### 1.1 `gl_compatibility` обязателен, иначе чёрный экран

Forward+ требует Vulkan, которого в браузере нет. Правки только для веб-таргета
(десктоп остаётся на Forward+):

```ini
; project.godot
renderer/rendering_method.web="gl_compatibility"
anti_aliasing/quality/screen_space_aa.web=0
```

Вторая строка — не косметика: FXAA живёт только в Forward+/Mobile, под
Compatibility настройка мертва, и Godot **на каждом старте** пишет
`WARNING: Screen-space AA is only available when using the Forward+ or Mobile
renderer`. MSAA 4x на WebGL2 работает, кромки не страдают.

Признак успеха в консоли браузера:
`OpenGL ES 3.0 (WebGL 2.0) - Compatibility` + `Build configuration: Emscripten
4.0.20, single-threaded, no GDExtension support`.

### 1.2 `thread_support=false` избавляет от COOP/COEP на хостинге

```ini
; export_presets.cfg
variant/thread_support=false
```

Выбирается шаблон `web_nothreads_release.zip`, **SharedArrayBuffer не нужен**,
значит Vercel не придётся заставлять отдавать `Cross-Origin-Opener-Policy:
same-origin` и `Cross-Origin-Embedder-Policy: require-corp`. Для деплоя на
статик-хостинг это главный аргумент за однопоточный вариант: многопоточный без
этих заголовков падает на старте.

### 1.2.1 Secure Context — отдельное требование, и HTTP его не даёт

**Симптом, который легко принять за битую сборку:**

```
Error
The following features required to run Godot projects on the Web are missing:
Secure Context - Check web server configuration (use HTTPS)
```

Сборка при этом цела: `canvas` в DOM есть, консоль чистая, `index.pck` отдаётся 200.
Шелл Godot делает **жёсткий гейт** по `window.isSecureContext` ещё до инициализации
движка — это не про COOP/COEP и не про `thread_support`. По http-ориджину (не
`localhost`) `isSecureContext === false`, и игра не стартует никогда.

Ловушка при отладке: **`http://localhost` и `http://127.0.0.1` — secure context**,
поэтому локально всё работает, а на боевом домене по http — нет. Разница вылезает
только после деплоя.

A/B-харнесс, который это различает за один прогон (один и тот же сайт по http и по
https, `ignoreHTTPSErrors: true` на контексте, в iframe читаем `isSecureContext`
и `document.body.innerText`):

```bash
# _preview/demo-https.js в проекте портфолио
PW_DIR="C:/Users/tio/AppData/Local/npm-cache/_npx/9833c18b2d85bc59" \
  ONLY_BASE="^https" WAIT_MS=40000 node _preview/demo-https.js
# http:  secure=false, ac=[],      bufs=0, body="Error The following features ..."
# https: secure=true,  ac=['running'], bufs>=1, body=""
```

**Важно:** https с **невалидным** сертификатом (fallback `CN=*.github.io` на своём
домене) — это тоже secure context, если пользователь прошёл интерстишл. То есть
`https://свой-домен/` → «Advanced → Proceed» → игра запускается. Это рабочий
обход, пока не выпущен сертификат; проверяется тем же харнессом с
`ignoreHTTPSErrors: true`.

Что делать, если по http обязаны остаться: единственный чистый вариант — отдельный
https-ориджин (второй хостинг/поддомен), а не патч шелла. Патч
`isSecureContext` в сгенерированном `.js` снимает гейт, но тогда движок идёт по
пути, который этот гейт закрывает, — не рекомендуется.

### 1.3 Размер PCK: `all_resources` + `exclude_filter`

`export_filter="all_resources"` пакует **все** импортированные файлы. Обход
зависимостей Godot бесполезен, если игра собирает путь в рантайме:

```gdscript
# так Godot не видит зависимость и не выкинет ассет
static func scene(dir: String, name: String) -> PackedScene:
	return load(dir + name + ".gltf")
```

Поэтому мёртвые ассеты вырезать вручную. Вспомогательный скрипт: разобрать
списки пулов из кода регуляркой, собрать из `*.gltf` карту «текстура -> кто её
использует», и считать файл мёртвым, только если **все** ссылающиеся модели
не используются. Так нашлись 4 текстуры на 19.4 MB; `Leaves_TwistedTree.png`
при этом оказался живым — его тянет `Bush_Common.gltf`.

**ГЛАВНАЯ ЛОВУШКА: шаблон `exclude_filter` матчит и середину строки, а якоря
нет.** `DeadTree_*` **не** матчит `Bark_DeadTree.png`. Первая попытка
`"…DeadTree_*, …TwistedTree_*"` сэкономила 3.2 MB вместо 19.4. Рабочий набор:

```ini
exclude_filter="*.log, tools/*, web_ver/*, \
assets/models/nature_quaternius/DeadTree_*, \
assets/models/nature_quaternius/TwistedTree_*, \
assets/models/nature_quaternius/Bark_DeadTree*, \
assets/models/nature_quaternius/Bark_TwistedTree*"
```

PCK 68.3 -> **48.28 MB**. Проверка: `index.pck` не должен расти между
одинаковыми экспортами — рост означает, что в пак попало что-то новое.

**ЛОВУШКА 2: Godot импортирует любой PNG внутри проекта.** Playwright с
**относительным** именем файла пишет скриншот в корень проекта, а не в
`.playwright-mcp/`. Два таких PNG добавили в PCK 0.87 MB и осиротевшие
`*.png.import`. Скриншоты складывать в папку под `exclude_filter` и
`.gitignore` (например `tools/debug/shots/`), а если PNG уже попал в корень —
удалять вместе с его `.import`.

### 1.4 MIME и кэш на хостинге

`web_ver/vercel.json` (аналог — `_headers`/`.htaccess`):

```json
{ "headers": [
  { "source": "/index.wasm", "headers": [
    { "key": "Content-Type", "value": "application/wasm" },
    { "key": "Cache-Control", "value": "public, max-age=3600" } ] },
  { "source": "/index.pck", "headers": [
    { "key": "Content-Type", "value": "application/octet-stream" },
    { "key": "Cache-Control", "value": "public, max-age=3600" } ] },
  { "source": "/index.html", "headers": [
    { "key": "Cache-Control", "value": "no-cache" } ] }
] }
```

Настройки Vercel: preset **Other**, build-команды нет, output/root — `web_ver`;
или разово `npx vercel deploy web_ver --prod --yes`.

Локально тот же контракт воспроизводит свой статик (§9 в `godot-headless-assets`) — **Windows
`http.server` отдаёт `.wasm` как `application/octet-stream`** и ломает
`WebAssembly.instantiateStreaming`. Своя карта MIME обязательна, плюс
`Cache-Control: no-store`, чтобы не отлаживать старый PCK.

### 1.5 Что чистить перед экспортом

- `web_ver/.gdignore` — иначе Godot импортирует собственную сборку.
- Папка сборки в `.gitignore` **не** нужна, если её отдаёт хостинг из репозитория
  (Bubble Peaks пушит `web_ver/` целиком, ~86 MB).
- Логи `_c*.log` и `*.log` — в `.gitignore`, но **не** в `exclude_filter`
  (они и так не ассеты; в фильтре держать `*.log` на случай, если лог лежит
  внутри проекта).

### 1.6 Итоговый чек-лист

```bash
godot --headless --editor --quit > _c.log 2>&1          # 0 ERROR/WARNING
grep -ciE "screen-space aa" _c.log                        # 0
godot --headless --export-release "Web" web_ver/index.html
ls -l web_ver/index.pck web_ver/index.wasm                # размер не вырос
python tools/serve_web.py                                 # 127.0.0.1:8137
# Playwright: титульник -> клик -> HUD, 0 ошибок шейдеров в консоли
```

### 1.7 Как доказать, что деплой реально ушёл (без токена Vercel)

Вердикт Vercel висит статусом на коммите, но `GET /repos/<o>/<r>/commits/<sha>/status`
для **приватного** репозитория отдаёт `404 Not Found` без токена, а `gh` в песочнице
может быть не установлен. Проверять надо иначе — и этого достаточно:

```bash
git ls-remote origin refs/heads/main     # == git rev-parse HEAD  -> пуш долетел
curl -s https://<site>/ | grep -c DOWNLOAD_SHARE   # >0 -> на сайте новый лоадер
curl -sI https://<site>/index.pck | grep -i content-length   # == размер локального pck
```

Третий тест — самый полезный: `Content-Length` живого `.pck` совпадает с
`ls -l web_ver/index.pck` байт в байт, значит Vercel пересобрал и отдаёт именно
твою сборку, а не закэшированную предыдущую. `Age: 0` в тех же заголовках
подтверждает, что ответ пришёл не из edge-кэша.

Помни про `Cache-Control: public, max-age=3600` на `.pck`/`.wasm`: браузер
пользователя может час отдавать старый файл. Перед проверкой — hard refresh.

**Косметическая грабля песочницы:** `git push` работает, но ref трекинга не
появляется — `mkdir -p .git/refs/remotes/origin` возвращает `0`, а каталога
после этого нет, `git update-ref refs/remotes/origin/main <sha>` тоже молчит, и
`git status` навсегда пишет `[gone]`. Это не признак неудачного пуша (проверяй
через `ls-remote`), на машине пользователя ref создастся сам.

## 2. Доказать, что пост-эффект вообще что-то делает (A/B по кадрам)

Вопрос «эффект работает?» решается не чтением кода, а выключением эффекта и
сравнением кадров. В проекте Bubble Peaks так проверяли glow, тонмаппинг и туман.

### 2.1 Харнесс `tools/debug/shot.gd` (Bubble Peaks)

`extends Node`, грузит `res://scenes/main.tscn`, ставит свободную камеру и пишет
PNG. Интерфейс:

```bash
godot --path . res://tools/debug/shot.tscn -- \
    --scene=res://scenes/main.tscn --call=begin \
    --player=146,27,9 \
    --shots='146,33,30|146,27,0' \
    --frames=3 --size=1280x720 --prefix=naf --out=res://tools/debug/shots
```

- `--call=begin` **обязателен** для съёмки геймплея. Без него снимается титульник:
  оверлей перекрывает кадр, а камера двигается «за» ним, и все кадры выходят
  одинаковыми независимо от `--shots`. На этом легко построить ложный вывод.
- `--player=x,y,z` телепортирует игрока и его camera rig — так снимают арену, не
  проходя уровень.
- `--frames=N` — сколько кадров подождать до снимка. Для сравнения рендереров
  ставить **3**: мир успевает прогреться, но анимации ещё не расходятся.
- `--shots` — `;`-список `camX,camY,camZ|lookX,lookY,lookZ`.

**ГЛАВНАЯ ЛОВУШКА: `|` в `--shots` — это пайп для bash.** Без кавычек получаешь
`rc=127` и пустой лог, причём выглядит как «Godot не запустился». Всегда через
переменную:

```bash
S='--scene=res://scenes/main.tscn --call=begin --shots=146,33,30|146,27,0'
"$GODOT" --path . res://tools/debug/shot.tscn -- $S --prefix=naf
```

### 2.2 Метрика: MAD по каналу L

numpy в окружении может отсутствовать — считать через PIL:

```python
from PIL import Image, ImageChops
def mad(pa, pb):
    h = ImageChops.difference(Image.open(pa).convert('RGB'),
                              Image.open(pb).convert('RGB')).convert('L').histogram()
    n = sum(h)
    return sum(k*c for k, c in enumerate(h))/n, sum(c for k,c in enumerate(h) if k > 32)/n*100
```

`MAD` — средняя абсолютная разница (0..255), второе число — доля пикселей,
разошедшихся сильнее чем на 32. Читать **вместе**: смена тонмаппинга дала
`MAD 8.5` при `>32 = 0.10 %` (ровный сдвиг всей картинки), а смена рендерера —
`MAD 27` при `>32 = 48 %` (реально другая картинка). По одной только MAD эти
случаи не различить.

### 2.3 Схема A/B на эффект

1. Снять эталон.
2. Временно выключить одну строку в `main.gd` (`env.glow_enabled = false`).
3. Снять тот же кадр.
4. **Вернуть файл и проверить `git diff --stat <файл>` — должно быть пусто.**
   Всегда делать `cp файл файл.bak` до правки и удалять `.bak` после.

Пример результата: `glow ВКЛ` против `glow ВЫКЛ` в Forward+ дал `MAD 0.48`.
Значит при `glow_intensity=0.35`, `glow_hdr_threshold=1.25`, `glow_bloom=0.04`
эффект не виден вообще. Полезно: вместо спора «настроен ли glow» есть число.

### 2.4 Десктопный `gl_compatibility` — ГОДНЫЙ proxy для веба

**ИСПРАВЛЕНО 2026-09-20.** Раньше здесь было написано обратное, и это была
ошибка, построенная на трёх пикселях неба с одного ракурса. Правильный замер
(одинаковая камера, одинаковое разрешение 1280x720, MAD по каналу L):

| сцена | Forward+ против браузера | Forward+ против десктопного Compatibility |
|---|---|---|
| Зона 2 | MAD 24.72 / >32 31.5 % | MAD 24.68 / >32 31.5 % |
| Арена | MAD 27.22 / >32 47.6 % | MAD 27.19 / >32 47.6 % |

Совпадение до сотых: **браузер и десктопный Compatibility дают одну и ту же
картинку**. Значит итерировать веб-вид можно быстрыми десктопными рендерами
(12 с), а в браузер лезть только за финальным подтверждением.

**Урок про методику, а не про рендерер:** вывод о «разных рендерерах» был сделан
по выборке из трёх пикселей на кадре с другим ракурсом. Сравнивать картинки
можно только при **идентичной камере**; при разных ракурсах разница камеры
маскируется под разницу рендерера. Как получить идентичную камеру в браузере —
§3.

### 2.5 Что реально расходится (Bubble Peaks, Forward+ против Compatibility)

- **Небо**: в Forward+ розово-лавандовый градиент, в Compatibility плоское
  серо-синее. HDR-панорама (`.hdr`, значения >1.0) пишется в LDR-буфер RGBA8 и
  обрезается, поэтому яркое небо выходит темнее.
- **Ambient проседает**: при `ambient_light_source = AMBIENT_SOURCE_SKY` и
  `sky_contribution = 0.62` свет берётся от неба, а небо темнее -> темнее вся
  сцена. Внешне читается как «обесцвеченные текстуры», хотя текстуры целы.
- **Тени жёстче**: PCSS не поддерживается, `soft_shadow_filter_quality`
  игнорируется.
- Растительность, почва, панели, персонаж — идентичны.

Чем это **не** лечится (проверено): glow (`MAD 0.48` между вкл/выкл при
`intensity 0.35`, `hdr_threshold 1.25`) и смена тонмаппинга (LINEAR даёт 26.89
против 26.89 у FILMIC). Лечится подъёмом яркости неба под веб:
`pano.energy_multiplier` 0.85 -> ~1.6 под `OS.has_feature("web")`.

## 3. Снять из браузера то, что нельзя пройти руками: временный пробник

Боевая веб-сборка всегда стартует со спавна, поэтому поздние зоны в браузере
сфотографировать нечем. Решение — **одноразовый экспорт с подменённой главной
сценой**. Пробник лежит вне `tools/` (иначе его вырежет `exclude_filter`).

### 3.1 Шаги

```bash
mkdir -p _probe _webprobe && printf '' > _webprobe/.gdignore   # выход сборки не импортировать
cp project.godot _project.godot.bak
sed -i 's|^run/main_scene=.*|run/main_scene="res://_probe/webprobe.tscn"|' project.godot
godot --headless --editor --quit                     # 0 ERROR, проверить скрипт
godot --headless --export-release "Web" _webprobe/index.html
cp _project.godot.bak project.godot && rm -f _project.godot.bak
git diff --stat project.godot                        # ОБЯЗАТЕЛЬНО пусто
```

Дальше свой статик на `_webprobe/` (свой MIME-мап, §9 в `godot-headless-assets`) и Playwright.

### 3.2 Пробник: аргументы через query string

`OS.get_cmdline_args()` в вебе пуст, но `JavaScriptBridge` читает адресную строку:

```gdscript
func _param(key: String) -> String:
	for token in _query().lstrip("?").split("&", false):
		var kv := token.split("=", true, 1)
		if kv.size() == 2 and kv[0].to_lower() == key:
			return kv[1]
	return ""

func _query() -> String:
	if not OS.has_feature("web"):
		return ""
	return str(JavaScriptBridge.eval("window.location.search", true))
```

Что стоит завести в пробнике:

- `?cam=x,y,z&look=x,y,z` — **свободная камера ровно как в `shot.gd --shots`**
  (`fov 60`, `near 0.05`, `far 800`, `look_at(..., Vector3.UP)`, `make_current()`).
  Без этого сравнить браузер с десктопом нельзя: follow-камера в двух прогонах
  встаёт по-разному, и разница камеры маскируется под разницу рендерера.
- `?zone2` / `?arena` — телепорт игрока, если нужен персонаж в кадре.
- Ждать `1.5 с` после `begin()` до перемещений, иначе интро перебьёт.

### 3.3 Ловушка: размер вьюпорта

`browser_take_screenshot` снимает **текущий вьюпорт**, а не 1280x720 по
умолчанию. На одном прогоне кадр вышел `1920x897` вместо `1280x720`, и сравнение
с десктопным кадром дало мусорные `MAD 66`. Перед съёмкой всегда:

```
browser_resize(1280, 720)  ->  browser_navigate(url)  ->  wait  ->  screenshot
```

и в скрипте сравнения проверять `A.size == B.size`, иначе печатать
`SIZE MISMATCH` и выходить, а не считать MAD.

### 3.4 `?mute` для веба

**`index.html?--mute` до игры не доходит** — веб-шелл не пробрасывает query
string в аргументы движка (проверено: 0 упоминаний `muted` в консоли). Поэтому
флаг надо принять явно:

```gdscript
func _mute_arg_sources() -> Array:
	var sources: Array = [OS.get_cmdline_args(), OS.get_cmdline_user_args()]
	if OS.has_feature("web"):
		sources.append(_web_query_args())
	return sources

func _web_query_args() -> PackedStringArray:
	var raw: Variant = JavaScriptBridge.eval("window.location.search", true)
	var out := PackedStringArray()
	for token in str(raw).lstrip("?").split("&", false):
		if token != "":
			out.append(token)
	return out
```

Признак успеха в консоли браузера: `[Sfx] muted (--mute)`.

### 3.5 Консоль Playwright надёжнее, чем инструмент

Страница между вызовами MCP сбрасывается в `about:blank`, и
`browser_console_messages` возвращает 0 сообщений. Логи при этом лежат на диске:

```bash
f=$(ls -t .playwright-mcp/console-*.log | head -1)
grep -iE "muted|Godot Engine|ERROR" "$f"
```

Оттуда же видно баннер (`OpenGL ES 3.0 (WebGL 2.0) - Compatibility`,
`Emscripten ... single-threaded`) — быстрый способ подтвердить, что сборка
поднялась именно в Compatibility.

## 4. Своя загрузочная шторка вместо стоковой Godot (custom HTML shell)

Стоковый шелл красит загрузку в плоский `#242424` с голым `<progress>` и
снимает её в тот момент, когда разрешился `startGame()` — **до** `_ready()`
главной сцены. То есть пока строится уровень, игрок смотрит в чёрное окно.

### 4.1 Пресет и плейсхолдеры

```ini
# export_presets.cfg
html/custom_html_shell="res://tools/web/shell.html"
```

`index.html` пересобирается из этого файла на **каждом** экспорте — править
`web_ver/index.html` бессмысленно. Доступные подстановки (достаются из бинаря
Godot: `grep -a -o '\$GODOT_[A-Z_]*' Godot_v*.exe | sort -u`):

`$GODOT_CONFIG`, `$GODOT_HEAD_INCLUDE`, `$GODOT_PROJECT_NAME`, `$GODOT_SPLASH`,
`$GODOT_SPLASH_CLASSES`, `$GODOT_SPLASH_COLOR`, `$GODOT_THREADS_ENABLED`,
`$GODOT_URL`.

`$GODOT_SPLASH` подставляется как **имя файла**, а не как тег: в web-экспорте
boot splash выгружается рядом как `index.png`, поэтому `<img src="$GODOT_SPLASH">`
работает без правок.

### 4.2 Шторку снимает игра, а не шелл

`startGame().then(...)` в стоковом шелле — неверный момент. Правильный сигнал
даёт сама игра, когда первые кадры уже на экране:

```gdscript
# main.gd, в _ready() после сборки уровня
if OS.has_feature("web"):
    _dismiss_web_loader()

func _dismiss_web_loader() -> void:
    await get_tree().process_frame
    await RenderingServer.frame_post_draw
    await RenderingServer.frame_post_draw   # два кадра: на первом компилятся шейдеры
    JavaScriptBridge.eval("window.bubblePeaksLoaderDone && window.bubblePeaksLoaderDone();", true)
```

В шелле `setStatusMode('hidden')` надо превратить в no-op (иначе стоковый
`startGame().then()` всё равно спрячет шторку), а `.then()` оставить только как
страховку: `setTimeout(window.bubblePeaksLoaderDone, 60000)`.

### 4.3 Геометрию лоадера считать от дизайн-базы, а не от vw

Если на шторке тот же логотип, что и на титульном экране, размер надо взять
**точно**, иначе кроссфейд читается как двойная экспозиция. Титул рисуется в
дизайн-пространстве Godot, а оно масштабируется:

```ini
# project.godot
window/size/viewport_width=1600
window/size/viewport_height=900
window/stretch/mode="canvas_items"
window/stretch/aspect="expand"
```

Значит масштаб = `min(vw / 1600, vh / 900)`. В CSS это одна переменная:

```css
:root { --godot-scale: min(100vw / 1600, 100vh / 900); }
#status-splash { width: calc(var(--godot-scale) * 834.7); }  /* 880 * 1881/1983 */
```

Логотип на титуле занимает `1881` из `1983` px исходника (обрезанные поля), а
`index.png` — уже обрезанная копия, поэтому ширина содержимого = `880 * 1881/1983`.
Центрировать так же: `position: absolute; left/top: 50%; transform: translate(-50%,-50%)`,
и «дыхание» держать той же амплитуды/периода, что в `hud.gd` (`±3.5 %`, `2π/2.2`).

Проверка — не глазом, а bbox'ом по кадрам:

```python
# bbox розовых пикселей в полосе логотипа; сравнивать loader vs title card
r, g, b = px[x, y]
if r > 205 and g < 160 and (r - g) > 70: ...
```

До правки: лоадер 785 px против титула 686 px (разница 14 %). После: 643..691
у обоих — расхождение только от фазы «дыхания».

### 4.4 Сфотографировать полосу прогресса

На localhost сборка грузится быстрее, чем успевает прийти скриншот: полоса уже
на 100 %. Нужен сервер, который **цедит `.pck`** (остальное отдаёт как есть):

```python
def copyfile(self, source, outputfile):
    if not self.path.endswith(".pck"):
        return super().copyfile(source, outputfile)
    while True:
        block = source.read(96 * 1024)
        if not block: break
        outputfile.write(block); outputfile.flush(); time.sleep(0.05)
```

Content-Length при этом остаётся корректным, поэтому `onProgress` в шелле
считает проценты как в бою. Так снимаются кадры 49 % / 55 % / 98 % и видно, что
полоса реально едет, а не просто стоит на 100 %.

**Порты:** песочница режет часть портов (`WinError 10013`). Проверено: `8000` и
`8137` открываются, `8001` — нет. Если сервер не поднимается, менять порт, а не
искать ошибку в коде.

### 4.5 Прогресс обязан быть двухфазным, иначе шкала врёт

Жалоба звучит как «шкала ещё не загрузилась, а уже 100 %». Причина не в шкале,
а в том, что `onProgress` описывает **только байты**: `animateProgress()` в
`index.js` суммирует `loaded/total` по всем файлам, которые шли через
`preloader` (wasm + pck, `total` — сумма их размеров из `fileSizes`). А после
последнего байта остаётся:

1. инстанцирование wasm (стриминговая компиляция добирает хвост),
2. `copyToFS` — весь pck копируется в MEMFS,
3. `callMain` -> движок грузит `--main-pack` и строит сцену,
4. `main.gd::_ready()` строит уровень целиком (у Bubble Peaks — вся геометрия),
5. `_dismiss_web_loader()` ждёт **два** нарисованных кадра (на первом компилятся
   шейдеры) и только тогда дёргает `window.bubblePeaksLoaderDone`.

Всё это время байтовый прогресс уже 100 %. Второй, более мелкий источник
рассинхрона: у полосы стоял `transition: width .18s linear`, а текст обновлялся
мгновенно — при крупном чанке «100 %» появлялось раньше, чем полоса доезжала.

Рабочая схема:

```js
const DOWNLOAD_SHARE = 88;   // байты владеют 0..88 %
const BOOT_CEIL = 99;        // потолок догона
const CREEP_TAU = 4.0;       // с; постоянная времени

let target = 0, shown = 0, bootStart = 0;

// onProgress: монотонно и с клампом
const bytes = Math.min(1, current / total) * DOWNLOAD_SHARE;
if (bytes > target) target = bytes;
if (bootStart === 0 && current >= total) bootStart = performance.now();

// rAF: и ширина, и текст — из одного сглаженного числа
function tick(now) {
  if (bootStart > 0) {
    const t = (now - bootStart) / 1000;
    const creep = DOWNLOAD_SHARE + (BOOT_CEIL - DOWNLOAD_SHARE) * (1 - Math.exp(-t / CREEP_TAU));
    if (creep > target) target = creep;
  }
  shown += (target - shown) * (1 - Math.exp(-dt / 0.22));
  statusFill.style.width = shown + '%';
  statusPct.textContent = Math.floor(shown) + '%';   // floor, не round
  rafId = requestAnimationFrame(tick);
}

// bubblePeaksLoaderDone: только здесь 100 % становится правдой
target = 100; shown = 100; draw(); statusOverlay.style.opacity = '0';
```

Ключевые детали, каждая из которых была багом в первой версии:

- `bootStart` ставить по `current >= total`, **не** по `.then()` от `startGame()`:
  инстанцирование wasm и копирование pck лежат именно между ними.
- у `#status-fill` **убрать** `transition: width` — иначе CSS анимирует полосу
  позади уже обновлённого текста, и они расходятся.
- `Math.floor`, не `Math.round`: округление печатает «100 %» на 99.6 % догона.
- догон нужен асимптотический (`1 - exp`), а не линейный: он никогда не
  упирается в потолок и продолжает шевелиться, пока идёт долгий бут.
- `displayFailureNotice` должен глушить rAF-цикл флагом (`failed = true`),
  иначе тикер продолжает перерисовывать полосу, которой уже нет на экране.

### 4.6 Проверить лоадер без браузера: node-харнесс на экспортированном HTML

Браузерной автоматизации на Windows нет, а тайминги лоадера глазами не
проверяются. Инлайн-скрипт из `web_ver/index.html` исполняется в node с
подменёнными DOM/часами:

```js
const html = fs.readFileSync('web_ver/index.html', 'utf8');
const blocks = [...html.matchAll(/<script(?![^>]*src=)[^>]*>([\s\S]*?)<\/script>/g)];
const js = blocks[blocks.length - 1][1];          // последний = свой, не index.js

let fakeNow = 0; const frames = [];
const el = () => ({ style: {}, textContent: '', lastChild: null,
                    appendChild() {}, removeChild() {} });
const nodes = { 'status': el(), 'status-bar': el(), 'status-fill': el(),
                'status-pct': el(), 'status-notice': el() };
const windowStub = { requestAnimationFrame: (cb) => frames.push(cb), setTimeout: () => 0 };

function Engine() {}
Engine.getMissingFeatures = () => [];
Engine.prototype.startGame = function (o) {
  onProgress = o.onProgress;
  return new Promise((res) => { startResolve = res; });
};

new Function('window', 'document', 'Engine', 'performance',
             'requestAnimationFrame', 'console', js)(
  windowStub,
  { getElementById: (id) => nodes[id], createElement: () => ({}), createTextNode: () => ({}) },
  Engine, { now: () => fakeNow }, windowStub.requestAnimationFrame, console);
```

Драйвер: `step(ms)` увеличивает `fakeNow` и вызывает все накопленные кадры,
микрозадачи прогонять `await Promise.resolve()`. Сценарий — 100 событий
`onProgress` по 40 мс, затем 6 с «бутфейза» кадров, затем `startResolve()` +
`window.bubblePeaksLoaderDone()`. Инварианты, которые надо проверять:

- `text <= width` на каждом кадре (текст не впереди полосы);
- текст монотонен;
- до `bubblePeaksLoaderDone` **строго** `< 100 %`;
- после 6 с бутфейза `> 95 %` (догон не стоит);
- после `loaderDone` ровно 100 % и больше не меняется.

Готовый харнесс лежит в проекте как `tools/web/loader_test.js`
(`node tools/web/loader_test.js` из корня). Он читает **экспортированный**
`index.html`, поэтому проверяет артефакт, а не исходник шелла.

## 5. PNG в корне проекта уезжает в релизный PCK

`export_filter="all_resources"` пакует **все** ресурсы, а PNG в корне — ресурс:
Godot его импортирует и кладёт в пак. Скриншоты браузерных тестов пишутся
именно в корень (`browser_take_screenshot` с относительным путём), поэтому
пять кадров на 2 МБ молча добавили **1.6 МБ** к веб-сборке.

Лечение — каталог под `.gdignore`, как для сборок и пробников:

```bash
mkdir -p _shots && printf '' > _shots/.gdignore
# дальше в Playwright: filename: "_shots/loader_mid.png"
```

Как поймать, если уже случилось:

```bash
grep -ac "_shots\|_web_" web_ver/index.pck        # 0 = чисто
grep -aoE "[A-Za-z0-9_./-]+\.png" web_ver/index.pck | sort -u   # что реально в паке
```

Правило: **два экспорта подряд без правок должны давать одинаковый размер**
(`ls -l web_ver/index.pck`). Если размер «плавает» — в дерево попал файл,
который не должен был. Если размер стабильно вырос после правки, не относящейся
к ассетам, — искать новый PNG/ресурс в корне.

## 6. Сколько `.pck` весит НА САМОМ ДЕЛЕ

Размер `index.pck` на диске — не то, что скачивает игрок. Vercel (как и любой
приличный хостинг) отдаёт его с brotli, и соотношение по ассетам разное в разы:

```bash
curl -sI -H 'Accept-Encoding: br' https://<site>/index.wasm | grep -i content-encoding
curl -s  -H 'Accept-Encoding: br' https://<site>/index.pck  | wc -c   # реальные байты
```

Замер на реальном проекте: `wasm` 39.5 МБ -> 9.55 МБ, `pck` 46.5 МБ -> 24.0 МБ,
итого ~33.5 МБ по сети. Обрати внимание: `-o /dev/null` в песочнице отдаёт
`size_download 0` и `exit 23` — мерить через `| wc -c`.

Скачиваются они **параллельно** и без нашей помощи: `startGame()` — это
`Promise.all([this.init(exe), this.preloadFile(pack, pack)])`. То есть
«распараллелить загрузку» — не рычаг, рычаг — уменьшить байты.

Разбор пака: `scripts/pck_report.py <pck> --top 20 --zlib`. Колонка `zlib` —
прокси того, сколько ассет стоит по сети:

```
      raw      zlib   ratio  name
    8.00M     2.50M   31.3%  ...puresky_2k.hdr...ctex      <- HDR жмётся
    5.33M     4.12M   77.3%  ...Bark_NormalTree_Normal...s3tc.ctex   <- дорого
    5.33M     0.05M    1.0%  ...Leaf_Pine_C...s3tc.ctex   <- почти бесплатно
```

Сортировать по zlib, а не по размеру: block-compressed текстуры (S3TC/BPTC) и
OGG лежат около 100 % (то есть в паке и по сети весят одинаково), а плоские
атласы — 1..20 %. Отсюда приоритет: сначала нормал-мапы и «шумные» текстуры,
потом всё остальное.

Что искать в паке, чего Godot не умеет:

- `export_filter="all_resources"` тащит **все** импортированные ресурсы проекта,
  включая те, чьи модели вычеркнуты из экспорта. Классика: `TwistedTree_*`
  в `exclude_filter`, а `Bark_TwistedTree.png` всё равно в паке — потому что
  исключается модель, а не текстура.
- если пути к моделям собираются в рантайме (`"res://.../%s.gltf" % name`),
  dependency-walker слеп полностью, и «мёртвое» надо искать самому: сверять
  таблицу файлов пака с текстом проекта (`assets/`, `scripts/`, `scenes/`,
  `shaders/`, плюс `.gltf`/`.mtl`, потому что текстуры названы внутри них).
  Готовый пример — `tools/pck_usage.py --exclude` в проекте Bubble Peaks: он
  печатает готовые шаблоны для `exclude_filter`.
- `boot_logo`/splash из `exclude_filter` **не убирается** (движок грузит его как
  исходник через `Image::load_from_file`) — экономить надо на самом файле.

Порядок действий, который окупается: (1) выкинуть мёртвое, (2) посмотреть на
колонку zlib, (3) только потом трогать разрешение текстур и битрейт аудио — это
уже правка арта, и её надо согласовывать, а не делать молча.

## 7. Пропорции окна: рамка 16:9 и телефон в портрете

Симптом: на телефоне в портрете «слои игры разъехались вниз по всей высоте
экрана». На кадре 390x844 видно полосу неба сверху, огромное серое поле в
середине, полосы уровня ниже, а HUD и тач-кнопки — по краям ЭКРАНА, а не рамки.

### 7.1 Причина

`html/canvas_resize_policy=2` (канвас = окно) + `window/stretch/aspect="expand"`.
В `Window::_update_viewport_size()` (scene/main/window.cpp) ветка выбирается по
`viewport_aspect` против `video_mode_aspect`, и при окне ВЫШЕ базы EXPAND идёт
в «will stretch horizontally»: `viewport_size.x = desired.x`,
`viewport_size.y = desired.x / video_mode_aspect`. Для базы 1280x720 и окна
390x844 это **1280x2770**. Камера упирается в `limit_top`/`limit_bottom` (у
уровня это 127/847) и встаёт в середине рамки, поэтому уровень уезжает в
середину кадра, а сверху и снизу торчит фоновая подложка.

Обратный случай (окно ШИРЕ базы) работает правильно и трогать его нельзя:
EXPAND даёт `viewport_size.x = desired.y * video_mode_aspect`, то есть рамка
целиком плюс больше мира по бокам.

### 7.2 Решение: рамка = канвас, размер задаёт shell

Не двигать аспект в рантайме и не ставить `aspect="keep"` глобально — вместо
этого отдать размер канваса своему скрипту в шелле (§4), а движку сказать
читать его:

```ini
# export_presets.cfg
html/canvas_resize_policy=0      ; None: размер канваса - наш
```

```js
// в shell.html, ДО <script src="$GODOT_URL">
function fitCanvas() {
	const w = innerWidth, h = innerHeight, RATIO = 16 / 9;
	const bw = w;                              // ширина всегда вся
	const bh = (w / h >= RATIO) ? h : w / RATIO;   // выше рамки - полоса 16:9
	const dpr = devicePixelRatio || 1;
	canvas.width = Math.round(bw * dpr);       // буфер под физический экран
	canvas.height = Math.round(bh * dpr);
	canvas.style.width = bw + 'px';            // и та же рамка в css-пикселях
	canvas.style.height = bh + 'px';
}
fitCanvas();
addEventListener('resize', fitCanvas);
addEventListener('orientationchange', fitCanvas);
```

```css
#canvas { position: absolute; left: 50%; top: 50%; transform: translate(-50%, -50%); }
```

Поля вокруг полосы заливает фон `body` — держать его равным
`environment/defaults/default_clear_color`, тогда шва не видно.

Почему это работает без перезагрузки при повороте: в `web/index.js` **нет**
слушателей `resize`/`orientationchange`, о смене размера движок узнаёт опросом
из wasm (`_godot_js_display_size_update` -> `GodotDisplayScreen.updateSize()`), а
при policy 0 ветка `noResize` берёт `canvas.width/height` как `desired_size`,
зовёт `_updateGL()` и возвращает 1 -> wasm переставляет размер окна ->
`_update_viewport_size()`. Вьюпорт всегда совпадает с рамкой, растягивать
нечего, а `get_viewport_rect()` равен 1280x720 — HUD и тач-управление
раскладываются по рамке, а не по экрану.

### 7.3 Что НЕ работает (проверено)

- **Смена `content_scale_aspect` в рантайме из GDScript.** Аспект применяется
  (`KEEP` -> `get_visible_rect()` ровно 1280x720, `EXPAND` -> расширенный), но
  **переход** EXPAND -> KEEP на ходу рендерится как stretch-to-fill: полосы не
  появляются, картинку нелинейно сжимает (канвас 780x1688 при вьюпорте 1280x720
  -> масштаб 0.609 по X и 2.34 по Y). На старте та же смена из `_ready()`
  леттербоксит правильно — ломается именно переход.
- **`aspect="keep"` в `project.godot` целиком.** Портрет лечит, но ландшафт
  телефона (844x390, 2.16) превращает в 693x390 с полосами по бокам — регресс
  на рабочем случае.
- **`canvas_resize_policy=1` + растягивание канваса через CSS.** Буфер был бы
  1280x720, а на 390 css-пикселей его раздувал бы браузер: мыло и рябь на
  детальной отрисовке.

### 7.4 Как проверять

Headless-проба пропорции не ловит (dummy-драйвер), размер pck тоже ничего не
говорит — только живой браузер. Два харнесса (Playwright из
`@playwright/mcp`, `channel: 'chrome'`, `--use-gl=angle --use-angle=swiftshader
--enable-unsafe-swiftshader`):

- `check_rotate.js` — печатает `innerWidth`, `canvas.width/height`, `style` и
  `getBoundingClientRect()` на серии размеров, включая повороты. Так видно,
  доехал ли новый размер до движка.
- `shot_mobile.js` — кадры меню/игры/ходьбы в портрете, ландшафте, на десктопе
  и после поворота.

**Клик по кнопке внутри игры считать от РАМКИ, а не от окна** (когда рамка
леттербоксится, окно и игровое пространство расходятся):

```js
const bandH = Math.min(h, w * 9 / 16), bandTop = (h - bandH) * 0.5, scale = bandH / 720;
await page.mouse.click(w * 0.5, bandTop + 0.62 * bandH + 28.5 * scale);
```

Ещё грабля: меню Godot-игры может слушать **только** `InputEventMouseButton` —
`keyboard.press('Enter')` его не закрывает, и на всех кадрах остаётся титульник
(выглядит как «игра не стартовала»). Проверять по кадру, а не по отсутствию
ошибок.

Матрица, которую стоит прогнать после правки пропорций: портрет 390x844 (свежая
загрузка и поворот из ландшафта), ландшафт 844x390, 1280x720, 1920x900 (шире
рамки — полей быть не должно) и 1024x768 (выше рамки — полоса 16:9 по центру).

## 8. Почему веб-сборка грузится 30-70 с: синхронная линковка шейдеров

Симптом: клик по Demo -> шторка висит десятки секунд, полоса прогресса при этом
замирает на месте (её двигает `requestAnimationFrame`, а он встал). Скачивание
и разбор `pck` тут ни при чём: 47 МБ с localhost — 0.4 с, с CDN — 1-2 с.

Замер делается `_preview/bp-where.js` в проекте портфолио. Он оборачивает
**все** методы WebGL2 на инстансе контекста (через
`HTMLCanvasElement.prototype.getContext` — Emscripten кэширует методы на
инстансе, хук на прототипе не ловит ничего), ставит `setInterval(16)` как
heartbeat для поиска окон блокировки главного потока и отдаёт результат на
локальный сервер.

Ловушки харнесса, каждая из которых уже стоила прогона:

- **в WebGL метод называется `getProgramParameter`, а не `getProgramiv`** (это
  имя из C-API). Хук на `getProgramiv` даёт 0 вызовов и уводит диагноз в сторону.
- `navigator.sendBeacon` **молча режет payload > 64 КБ** — а тут 105 программ с
  наборами `#define`. Отдавать обычным `fetch('/__probe', {method:'POST', ...})`.
- `page.evaluate` внутри окна блокировки отваливается по таймауту и возвращает
  `null`, поэтому «проба» должна уходить из страницы сама, а не вычитываться
  снаружи.
- Chrome наследует `http_proxy`/`https_proxy` из окружения песочницы и ползёт
  на 0.2 МБ/с. Запускать с `--no-proxy-server`, иначе меряешь прокси, а не игру.

Что он показывает на реальной сборке (Bubble Peaks, Chrome + ANGLE/D3D11,
RTX 2060 SUPER), 50 с загрузки:

```
getProgramParameter   вызовов 208   сумма 47.45 с   макс 11.10 с
getShaderParameter    вызовов 208   сумма  0.50 с
linkProgram           вызовов 105   сумма  0.00 с   <- вот это важно
окна блокировки главного потока: 0.35 с  +49.82 с   <- один сплошной блок
```

`linkProgram` стоит ноль: ANGLE планирует компиляцию HLSL->D3D на воркере и
**джойнит её в первом же запросе статуса**. То есть все 47 с — это
`glGetProgramiv(prog, GL_LINK_STATUS)`, по ~0.3-1.8 с на программу.

Итог двух правок на Bubble Peaks: **50.85 -> 19.90 с** холодной загрузки
(27.89 после CPU-частиц, 24.44 после нормализации материалов, 19.90 после
принудительных осей), 105 -> ~90 программ, худший одиночный вызов 11.10 -> 1.72 с.

**Но сначала выяснить, холодная это загрузка или уже прогретая.** Chrome кладёт
скомпилированные программы и в GPU-процесс, и **на диск профиля** — переживает
перезапуск браузера. Замер: 26.8 -> 2.7 -> 2.6 с в одной сессии
(`bp-warm.js`), 30.5 -> 3.2 -> 3.2 с при перезапуске Chrome между прогонами на
одном профиле (`bp-persist.js`). То есть 20 с платит только **первый в жизни
заход на этой машине**; повторные визиты уже ~3 с. Харнесс без
`launchPersistentContext` каждый раз стартует с пустым профилем, поэтому и
показывает холодную цифру — это то, что видит новый посетитель, но не то, что
видит вернувшийся.

### 8.1 Что НЕ работает

- **Батчить линковки JS-шимом нельзя.** Godot сразу после `linkProgram` зовёт
  `getProgramiv(LINK_STATUS)`, а затем `getProgramiv(ACTIVE_UNIFORMS)` и
  `getActiveUniform` для рефлексии. Любой из этих вызовов в ANGLE джойнит
  линковку. Отложить джойн можно только соврав про статус, а соврать про
  `ACTIVE_UNIFORMS` нельзя — Godot построит пустой кэш юниформов и материал
  перестанет настраиваться. `KHR_parallel_shader_compile` рекламируется
  (`extParallel: true`), но GLES3-бэкенд Godot его не использует.
- Переупорядочить сборку уровня, спрятать компиляцию за асинхронный прогрев —
  тоже нет: компиляция синхронная, а главный поток — единственный.

Рычаг ровно один: **уменьшить число уникальных специализаций шейдера**.

### 8.2 Откуда берутся специализации

Godot компилирует отдельную программу на каждое сочетание флагов. Считать
надо так (`_preview/bp-programs.js` + `_preview/define-diff.js`): хук собирает
`#define` из `shaderSource` и раскладывает по группам. На Bubble Peaks вышло
105 программ, и варьируются:

| ось | что это | кто ставит |
|---|---|---|
| `MODE_RENDER_DEPTH` | отдельная программа на shadow pass | `cast_shadow` у `GeometryInstance3D` |
| `ALPHA_SCISSOR_USED` | `transparency = ALPHA_SCISSOR` | материалы импортированных GLTF |
| `COLOR_USED` | у меша есть COLOR | `StandardMaterial3D` + вершины модели |
| `NORMAL_MAP_USED`, `MODE_UNSHADED`, `LIGHT_RIM_USED`, `DO_SIDE_CHECK` | флаги материала | то же |
| `USE_INSTANCING` | MultiMesh / частицы | `MultiMeshInstance3D`, `CPUParticles3D` |

То есть 165 импортированных моделей со своими `StandardMaterial3D` дают
комбинаторный взрыв: `shadow × scissor × color × normal × ...`.

**Осторожно с атрибуцией по группам.** Классификатор «`stdmat` = в исходнике
есть `albedo_texture`» ловит ВСЕ `StandardMaterial3D` проекта, а не только
материалы моделей: в ту же корзину попадают `Vfx.fx_material` (частицы и
вспышки) и `_film_material` у пузырей. Из 12.1 с этой группы ~2.6 с
принадлежали `fx_material`, и без разбора по флагам легко починить не то.
Поэтому решающий шаг — выгрузить по каждой дорогой программе её флаги:

```js
const has=(p,n)=>p.fd.includes(n)||p.vd.includes(n)?"1":".";
// COLOR_USED / DO_SIDE_CHECK / ALPHA_SCISSOR_USED / NORMAL_MAP_USED /
// USE_INSTANCING / MODE_RENDER_DEPTH / APPLY_TONEMAPPING / BASE_PASS
```

Материалы моделей после нормализации видны как `COLOR_USED + DO_SIDE_CHECK +
ALPHA_SCISSOR_USED` одновременно (шаблон ставит `vertex_color_use_as_albedo`).
Программы без `COLOR_USED` — чужие.

Ещё две ловушки самого харнесса `bp-programs.js`: группировка читала
`p.defines` и `p.flags`, которых в записи нет (запись кладёт `p.fd` и `p.key`),
и из-за этого все 91 программа сваливались в одну группу `undefined`; а
`sendBeacon` молча обрезает тело > 64 КБ — для 100+ программ нужен `fetch`.

### 8.3 Главный и самый дешёвый рычаг: GPU-частицы -> CPU-частицы

`GPUParticles3D` на GLES3 считает симуляцию в вершинном шейдере через
**transform feedback**, и godot'овский `particles.glsl` разворачивается в
**~33 000 символов GLSL**. Одна такая программа компилировалась 9-11 с, шесть
вариантов стоили **22 с из 47**. В `define-diff` они видны как группа с
`vertLen > 8000` и `fragLen < 4000` (огромный вершинник, крошечный фрагмент) и
`#define DISABLE_VELOCITY` / `MODE_3D`.

`CPUParticles3D` считает частицы на CPU и рисует через `MultiMesh` — процессного
шейдера у него **нет вообще**. Маппинг свойств 1:1, кроме трёх мест:

```
GPUParticles3D                         CPUParticles3D
p.draw_pass_1 = quad                  p.mesh = quad
p.process_material = ParticleProcessMaterial   -> свойства прямо на узле:
   mat.emission_shape/sphere_radius/ring_*         p.emission_shape/...
   mat.scale_min / scale_max                       p.scale_amount_min / _max
   mat.color_ramp = GradientTexture1D              p.color_ramp = Gradient
mat.turbulence_*                      <- НЕ поддерживается (убрать)
```

Типизация GDScript проверяет имена свойств на этапе парсинга, поэтому
`--export-release` падает сразу, если свойство названо неверно — отдельная
проверка не нужна.

Результат на Bubble Peaks: 105 -> 99 программ, худший одиночный вызов
11.1 -> 1.76 с, клик->снятие лоадера 50.85 -> 27.89 с.

### 8.4 Главный рычаг для моделей: один материал + принудительные оси

Считать надо **уникальные программы, а не материалы**: один вариант шейдера
стоит ~1.1-1.8 с, а программа, чей HLSL уже скомпилирован (ANGLE кэширует по
исходнику), — 0.04-0.17 с. На Bubble Peaks 12 дорогих программ давали 14.5 с
из 16.3 с, остальные ~79 почти бесплатны. То есть бороться надо только с
числом **уникальных** вариантов.

Что сработало (проверено, 22 -> 4 программы, 12.1 -> 4.5 с):

1. **Снять с импортированных моделей их собственные материалы.** В `Nature.pick()`
   (единственная точка инстанцирования, куда сходятся все — `tree()`, `grass()`,
   `dress_island()`) вызвать `set_surface_override_material` на каждый сюрфейс и
   повесить общий шаблон. Переносятся только `albedo_texture`, `albedo_color` и
   `normal_texture` — это uniform'ы и программ не добавляют.
2. **Принудительно включить вырез альфы и двусторонность у ВСЕХ моделей.** Вот
   это и схлопывает счётчик: оставленные как оси, они дают
   `2 (scissor) x 2 (two-sided) x 2 (normal) = 8` комбинаций, а рендерер
   удваивает их инстансными вариантами. Принудительные первые два оставляют
   единственной осью карту нормалей -> 4 программы на весь набор.
   Визуально бесплатно: `ALPHA_SCISSOR` отбрасывает только тексели с альфой
   < 0.5 (а `alphaMode: BLEND` в наборах Quaternius/KayKit не встречается
   вовсе — 48 моделей листвы уже объявляют `MASK`), двусторонность уже стоит
   у 88 из 173 моделей, остальные — замкнутые тела, у которых задние грани и
   так проигрывают тест глубины.

Проверять перед правкой, что все модели идут через одну точку:
`grep -rn "instantiate()\|\.gltf" --include=*.gd scripts/` — если
`ps.instantiate()` встречается в двух местах, второй путь материалы не получит.

### 8.4a Что НЕ работает (проверено, не тратить время)

* **`cast_shadow = OFF` у мелких пропов.** Ось `MODE_RENDER_DEPTH` выглядит
  страшно (31 программа), но стоит **0.60 с** — depth-шейдер компилируется
  быстро. Правка арта ради 0.6 с не окупается. (В прошлой редакции этот пункт
  стоял как «рычаг №2» — замер это опроверг.)
* **Выравнивание `transparency` без выравнивания `cull_mode`.** Одна ось из
  двух ничего не даёт: 2 x 2 всё равно 4 комбинации.
* **`m.specular = ...` на `StandardMaterial3D`.** Это имя из Godot 3: оно уходит
  в remap-путь `BaseMaterial3D::_set`, печатает
  `WARNING: Godot 3.x SpatialMaterial remapped parameter not found: specular`
  и значение **теряет**. Правильное имя — **`metallic_specular`**. Ловится
  только чтением консоли в браузере (`_preview/bp-shot.js` собирает её), в
  логе экспорта этого нет.
* **Ось `USE_INSTANCING`** ставит сам рендерер (MultiMesh у облачного моря и у
  `CPUParticles3D`), материалом на неё повлиять нельзя. В замере она удваивала
  почти каждую группу — принять как данность.
* Трогать `wasm`/`pck` (0.4-2 с) и «распараллеливать загрузку» (Godot и так
  качает через `Promise.all`).

### 8.4b Как доказать, что правка не изменила картинку

Скриншот до/после сравнивать **только после замера шумового пола**: снять одну
и ту же сборку дважды и посчитать разницу. На Bubble Peaks два прогона одной
сборки расходятся на 3.3 % пикселей (облака дрейфуют, частицы живут, камера
встаёт чуть иначе) — то есть разница 1.8 % между «до» и «после» **меньше
шума** и ничего не доказывает. Без этого контроля легко принять дрожание
анимации за регрессию арта.

```bash
# 1) два прогона ОДНОЙ сборки -> шумовой пол
PW_DIR=... node _preview/bp-shot.js && cp _preview/shot-play.png _cmp/a.png
PW_DIR=... node _preview/bp-shot.js && cp _preview/shot-play.png _cmp/b.png
# 2) разница в % пикселей с порогом 8 и максимум канала
```

### 8.5 Экспорт и деплой после правки

```bash
GODOT=/e/Programs/distr/Godot_v4.7.2-stable_win64.exe
"$GODOT" --headless --path 'F:/Pets/Projects/games/bubble_peaks_3d' --export-release Web
grep -in "error\|Parse Error\|SCRIPT ERROR" _exp_load.log   # пусто = скрипты целы
```

`fileSizes` в `index.html` **пересобирает сам экспорт** — руками править не надо,
надо только не забыть скопировать `index.html` вместе с `index.pck`. Копировать
надо девять файлов (`index.html`, `index.js`, `index.pck`, `index.wasm`,
`index.png`, `index.icon.png`, `index.apple-touch-icon.png` и два
`index.audio*.worklet.js`); после копирования `git status` в репозитории сайта
покажет изменёнными ровно `index.html` и `index.pck`, остальное совпадает
побайтно.

Проверка после деплоя (страница сайта отдаёт новый `fileSizes`, а не только
локальный файл):

```bash
curl -sk https://<домен>/games/<игра>/index.html | grep -o '"fileSizes":{[^}]*}'
curl -skI https://<домен>/games/<игра>/index.pck | grep -i content-length
```

И финальный замер «как у игрока» — `_preview/bp-verbose.js` (прогон через
страницу портфолио с кликом по карточке), а не прямой заход на URL игры.
