---
name: godot-ai-bridge
description: >
  Подключение к уже запущенному серверу Godot AI (godot-ai, аддон addons/godot_ai) и управление живым редактором Godot — «подключись к godot-ai», «запусти текущую сцену», «запусти Main.tscn», «покажи что сейчас в редакторе», «скриншот игры», «почему не запускается сцена», «запусти проект в Godot», а также любые задачи вида «сделай/поменяй что-то в открытой сцене Godot», «посмотри логи игры», «прочитай ошибки из редактора». Использовать, когда MCP-инструменты godot-ai недоступны в сессии (сервер не зарегистрирован в ~/.workbuddy-ai/mcp.json или MCP не перезапущен), но редактор Godot уже открыт и сервер godot-ai слушает порты. Содержит: где лежат capability-токены, как собрать минимальный streamable-http MCP-клиент на stdlib, готовый скрипт-мост, и обходные пути (прямой запуск сцены бинарником Godot), если сервер поднять не удалось.
agent_created: true
---

# Мост к Godot AI (godot-ai)

## 0. Когда это нужно

`addons/godot_ai` — это MCP-сервер **внутри живого редактора Godot**: python-процесс (FastMCP) слушает HTTP-MCP и WebSocket, а редактор подключается к нему как WS-клиент. Он даёт ~46 инструментов (`session_manage`, `editor_state`, `project_run`, `editor_screenshot`, `logs_read`, `scene_*`, `node_*`, `script_*` и т.д.).

Если в сессии нет инструментов `mcp__godot-ai__*` (сервер не прописан в `~/.workbuddy-ai/mcp.json` или MCP не перезапущен/не подтверждён), **не надо просить пользователя перезапускать сессию** — можно подключиться к уже работающему серверу напрямую по HTTP.

## 1. Карта

| Что | Где |
|---|---|
| Бинарник Godot | `E:\Programs\distr\Godot_v4.7.2-stable_win64.exe` (проверить: ярлык на рабочем столе, распарсить как UTF-16 строки) |
| PID сервера godot-ai | `%APPDATA%\Godot\app_userdata\<Project Name>\godot_ai_server.pid` |
| **HTTP-токен** (Bearer) | `%LOCALAPPDATA%\godot-ai\capabilities\http-8001.json` → поле `"http"` |
| WS-токен | тот же файл → поле `"websocket"` |
| Лог бэкенда | `%LOCALAPPDATA%\godot-ai\runtime\backend-8001.log` |
| Конфиг, который пишет плагин | `~/.codebuddy/mcp.json` (ключ `godot-ai`, `uvx godot-ai==4.1.0 attach --port 8001 --ws-port 8002`) |
| Скрипт-мост | `tools/godot_ai/_godot_ai_call.py` в проекте |
| Дамп схем инструментов | `tools/godot_ai/_godot_ai_tools.json` |

## 2. Проверка, что сервер жив

```bash
netstat -ano | grep -E ":800[12]"      # 8001 = HTTP-MCP, 8002 = WS
tasklist /FO CSV | iconv -f UTF-16LE -t UTF-8 | grep -i godot
```
Ожидаемо: `127.0.0.1:8001 LISTENING <pid>`, `127.0.0.1:8002 LISTENING <pid>`, и отдельный ESTABLISHED на 8002 — это редактор Godot (WS-клиент).

`GET http://127.0.0.1:8001/` → `401 Unauthorized`, `www-authenticate: Bearer realm="godot-ai"` — значит нужен токен из п.1.

**Сервер жив ≠ редактор подключён.** Бывает так: порт слушает, `_godot_ai_call.py` отвечает, но любой инструмент отдаёт `PLUGIN_DISCONNECTED: No active Godot session ... [connected=False, retryable=True, circuit_open=False]`, а `session_manage {"op":"list"}` возвращает `{"count":0}`. Это значит, что WS-клиент редактора отвалился (типично после `project_run`/импорта ассетов или перезагрузки плагина). Токен и клиент тут не виноваты — **не перезапускать клиент и не пересобирать мост**, ретраи не помогут. Проверить `session_manage list` (дешёвый вызов) и, если `count:0`, сначала исключить §2.1, и только потом идти в §5 — headless-тесты + свой shot-харнесс закрывают почти всё, кроме «потыкать в живом редакторе».

### 2.1. `count:0` на проекте, где аддон только скопирован — он НЕ включён

Самая частая причина на новом проекте, и она не лечится ни ретраями, ни перезапуском клиента. Скопировать `addons/godot_ai/` в проект **недостаточно**: плагин должен быть включён в `project.godot`, иначе редактор его просто не грузит и никуда не подключается.

Диагностика (редактор при этом может быть открыт и работать):

```bash
grep -a -n "editor_plugins" project.godot    # пусто => плагин не включён
```

Симптом в логе редактора, если запустить его с `--editor` и посмотреть stdout: там **нет** ни одной строки `MCP | plugin loaded` — только шапка Godot и Vulkan.

Лечение — дописать в `project.godot`:

```
[editor_plugins]

enabled=PackedStringArray("res://addons/godot_ai/plugin.cfg")
```

Грабли при этом:
- Правку делать при **закрытом** редакторе: он перезаписывает `project.godot` при выходе и может потерять секцию.
- `project_manage(op="settings_set", key="editor_plugins/enabled")` для этого не годится — инструмент явно отказывает на ключах `editor_plugins/*`. Только правка файла.
- После включения в логе появляются `MCP | plugin loaded` → `connecting to server` → `authenticated with server` → `[event] scene_changed`, а `session_manage list` отдаёт `count:1` с `readiness:"ready"`.
- Если порт 8001 уже занят другим инстансом, плагин печатает `server start blocked: Port 8001 is occupied by godot-ai vX.Y.Z; choose Replace to continue`, сам поднимает свой сервер и **меняет токен**. После этого нативный MCP-инструмент `mcp__godot-ai__*` в сессии отдаёт `Port 8001 is occupied by a process the bridge cannot adopt: status probe returned HTTP 401` — у клиента закэширован старый токен. Через `_godot_ai_call.py` всё работает (он перечитывает `capabilities/http-8001.json` каждый вызов); чтобы починить нативные инструменты, нужен перезапуск MCP-сессии.
- Запущенный редактор импортирует все PNG проекта. Скриншотные каталоги (`shots/`, `web/` и подобные) стоит закрыть пустым `.gdignore`, иначе на каждый кадр появляется `*.png.import`. Проверено: харнесс с `image.save_png("res://shots/...")` и `FileAccess.open("res://shots/report.txt", WRITE)` продолжает писать файлы при `.gdignore` внутри каталога.

## 3. Подключение через готовый скрипт

```bash
PY="C:/Users/tio/.workbuddy-ai/binaries/python/versions/3.13.12/python.exe"
cd <project>
"$PY" tools/godot_ai/_godot_ai_call.py session_manage '{"op":"list"}'
"$PY" tools/godot_ai/_godot_ai_call.py session_activate '{"session_id":"<slug>@<16hex>"}'
"$PY" tools/godot_ai/_godot_ai_call.py project_run '{"mode":"current"}'   # F6: текущая сцена
```

`session_manage(op="list")` возвращает `current_scene` (например `res://Main.tscn`), `play_state`, `readiness`, `editor_pid` — по нему видно, что открыто в редакторе **до** запуска.

### Для длинной работы — `seq.py` + `mcp_client.py`

Одиночные вызовы (`_godot_ai_call.py`) создают новую MCP-сессию на каждый процесс. После ~32 запусков сервер отдаёт `MCP_SESSION_LIMIT_REACHED`. Для реальной работы используй:

- `tools/godot_ai/mcp_client.py` — клиент с **переиспользованием** сессии (кэш id в `_mcp_session.txt`, авто-пересоздание при 404/503, `close()` через HTTP DELETE).
- `tools/godot_ai/seq.py <spec.json>` — прогон последовательности шагов за одну сессию, с реконнектом на каждом шаге. Шаги: `{"tool":..,"args":..}`, `{"eval_file":"..gd.txt"}`, `{"shot":"shots/x.png"}`, `{"sleep":1.5}`, `{"ensure_run":true}`.
- `tools/godot_ai/eval.py <file.gd.txt>` — одиночный `game_eval`.
- Скрипты-сниппеты держать как **`.gd.txt`** (не `.gd`!): иначе редактор пытается их распарсить и сыплет Parse Error в лог.

## 4. Ключевые инструменты

| Инструмент | Смысл |
|---|---|
| `session_manage {"op":"list"}` | список сессий: `session_id`, `current_scene`, `play_state` |
| `session_activate {"session_id": "..."}` | закрепить активную сессию (обязательно первым, если сессий >1) |
| `editor_state {}` | `current_scene`, `is_playing`, `readiness`, `game_capture_ready` |
| `project_run {"mode":"current"}` | **запустить текущую сцену** (аналог F6). `"main"` = главная, `"custom"` + `scene` = конкретная |
| `project_manage {"op":"stop"}` | остановить игру (нужно перед сменой сцены: `project_run` идемпотентен и не переключит) |
| `logs_read {"source":"game","count":50}` | логи игры (`plugin` / `game` / `editor`) |
| `editor_screenshot {"source":"game","max_resolution":900}` | скриншот: `game` = запущенная игра, `viewport` = редактор |
| `game_manage {"op":"get_scene_tree"}` | дерево сцены в рантайме, `input_*` — симуляция ввода |

Успешный `project_run` → `"status":"live"`, `helper_live:true`, `recent_errors:[]`.

## 5. Автономная проверка без редактора

Живая MCP-сессия мигает (`PLUGIN_DISCONNECTED`), а `Input.parse_input_event` и клики по реальному окну воспроизводятся плохо. Для «померить/посмотреть, что реально происходит» есть два независимых пути, оба без редактора.

### 5.1 Headless-пробник (детерминированно, без GPU)

```bash
APPDATA="C:\\Users\\tio\\AppData\\Roaming" \
  "/e/Programs/distr/Godot_v4.7.2-stable_win64.exe" --headless \
  --path "F:/Pets/Cursor/test/new-game-project" res://tools/debug/probe_cam.tscn
```

Готовые: `tools/debug/probe.gd` (обрыв), `probe_ui.gd` (тач), `probe_cam.gd` (мёртвая зона камеры), `probe_cam_bounds.gd` (края кадра по всей длине уровня), `probe_floor.gd` (где реально есть пол). Пролог любой пробы:

```gdscript
var main: Node = load("res://Main.tscn").instantiate()
add_child(main)
await get_tree().process_frame
await get_tree().process_frame
var end: Node = main.get_node_or_null("GameFlow/EndScreenLayer/EndOverlay")
if end != null:
    end.set("mode", "")
    (end.get("_buttons") as Array).clear()
get_tree().paused = false
```

Грабли:
- `Viewport::push_input` прогоняет координаты мыши/тача через `get_final_transform()`, а в headless окно крошечное (~20x) → синтетические события домножать: `var send: Vector2 = get_viewport().get_final_transform() * pos`.
- **`Input.parse_input_event` в headless тоже домножает `event.position`**, причём наблюдался неравномерный масштаб (x ×20 при viewport 1280x720 и окне 0x0, y ×19.47 + сдвиг). Проверять преобразование координат через реальное событие **нельзя** — только прямым вызовом обработчика: `node.call("_unhandled_input", ev)`. Отдельно оставлять дешёвую проверку «событие вообще доходит» (по побочному эффекту вроде списанного ресурса), без ассертов на координату.
- **`node.set_process(false)` ломает доставку `_unhandled_input`** — как способ «заморозить» ноду, чтобы `_process` не перезаписал её состояние, не годится.
- Луч «вниз от игрока» бьёт в сам коллайдер игрока — обязателен `q.exclude = [p.get_rid()]`.
- Телепорт + `cam.reset_smoothing()`, иначе сглаживание не успевает и замеры врут.
- Проба всегда пишет JSON в `res://` и печатает `PROBE_WRITTEN <path>` — по этой строке видно, что прогон дошёл до конца.

Грабли логических тестов (`SceneTree`-скрипты `tools/debug/test_*.gd`, возврат кода 0/1):
- **`process_frame` испускается ДО `_process` узлов.** Двух `await process_frame` мало, чтобы нода отработала один кадр — нужно три. Для `physics_frame` то же самое относительно `_physics_process`.
- **`queue_free()` срабатывает в конце кадра.** Если сцена предыдущего кейса ещё жива, `get_tree().get_first_node_in_group("player")` вернёт ЧУЖОГО игрока, и кейс будет «стрелять» в пустоту. Убирать сцену хелпером с двумя `await process_frame`.
- **Ошибка скрипта внутри `await`-корутины обрывает функцию** и она НЕ доходит до уборки. Один опечатанный `get_node` — и следующие кейсы получают грязь от предыдущего. Поэтому сначала проверять существование пути (`get_node_or_null`), а уборку ставить до ассертов там, где это возможно.
- **Финал/меню ставит `get_tree().paused = true`.** После кейса с финальным экраном обязательно `paused = false`, иначе все следующие кейсы молча не работают.
- **`EndScreenLayer` обычно не в корне `Main.tscn`**, а внутри `GameFlow` (`GameFlow/EndScreenLayer/EndOverlay`) — его создаёт `game_flow._ready()`.
- Внутри `class_name`-скрипта `static var` (например `_menu_done`) — единственный способ погасить стартовое меню в тесте: `gf.set("_menu_done", true)` до инстанса сцены.
- Детали в `_ok()` собирать из реальных значений: строка вида `"hp %d, is_alive() = %s"` с подстановкой вместо захардкоженного «false» экономит целый прогон.

### 5.2 Рендер реальных кадров (нужен GPU, `--headless` не рисует)

```bash
APPDATA="C:\\Users\\tio\\AppData\\Roaming" \
  "/e/Programs/distr/Godot_v4.7.2-stable_win64.exe" \
  --path "F:/Pets/Cursor/test/new-game-project" --resolution 1280x720 \
  res://tools/debug/shot_start.tscn
```

```gdscript
await RenderingServer.frame_post_draw
var img: Image = get_viewport().get_texture().get_image()
img.save_png("res://shots/x.png")
```

Грабли:
- После `end.set("mode","")` обязателен `(end as CanvasItem).queue_redraw()` — иначе CanvasItem держит последнюю нарисованную картинку и на скриншоте останется меню DEMO.
- **Обход кнопки START не вызывает `_set_hud(true)`** (он висит на сигнале `started`). Если игра прячет HUD на время меню — в харнессе звать `flow.call("_set_hud", true)` вручную, иначе полоска HP и счётчики на скриншоте просто отсутствуют и это выглядит как баг.
- **Телепорт игрока в зону подбора мгновенно подбирает предмет** — для кадра «предмет лежит» ставить игрока ВНЕ зоны (`Area2D` + `CollisionShape2D` дают точные границы, считать заранее).
- Позицию объекта на экране брать из `get_viewport().get_canvas_transform() * world`, а не из `Camera2D.get_screen_center_position()`: у камеры с `offset` и лимитами второе отдаёт не то, что ожидаешь, и «объект не виден» превращается в получасовую охоту на призрак. Для разглядывания — кроп нужного участка в PIL с `Image.NEAREST`.
- `Image.convert()` в 4.7 возвращает **void** (правит на месте): нельзя писать `img.get_region(r).convert(FMT)` в выражении — вернётся null, а `blit_rect` упадёт с `Condition "format != p_src->format"`. Склейку картинок делать в PIL.
- Скрипты класть как `tools/debug/*.gd` + парный `*.tscn` с одним узлом `Node` и `script = ExtResource(...)`.
- Спавн игрока берётся из `Main.tscn`, поэтому для проверки другого спавна игрока телепортировать в пробе, а не править сцену.

### 5.3 Грабли окружения
- `APPDATA` в Git Bash **пустой** → Godot создаёт `./Godot/` в корне проекта. Всегда передавать `APPDATA="C:\\Users\\tio\\AppData\\Roaming"`.
- Окно игры при запуске из bash может не находиться `EnumWindows` — для кликов есть `tools/win/click_game.py` (Win32 `mouse_event`), но рендер-скрипты надёжнее.

## 6. Как собрать мост с нуля (если скрипта нет)

Streamable-HTTP MCP на чистой stdlib — 3 шага:

1. `POST /mcp` с `Authorization: Bearer <http-токен>`, заголовками `Content-Type: application/json` и `Accept: application/json, text/event-stream`, телом `{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2024-11-05","capabilities":{},"clientInfo":{"name":"...","version":"1"}}}`.
2. Запомнить заголовок ответа `mcp-session-id`, отправить `notifications/initialized` (без `id`) с этим `Mcp-Session-Id`.
3. `tools/call` с `{"name": "<tool>", "arguments": {...}}`.

Ответы могут приходить как `text/event-stream` — парсить строки `data: {...}`. Контент инструмента лежит в `result.content[]`; картинки — блок `{"type":"image","data":"<base64>"}` (сохранять в файл, иначе утонешь в выводе).

## 7. Грабли

- **Токен меняется** при каждом старте сервера — всегда перечитывать `capabilities/http-8001.json`, не кэшировать. Есть ещё `http-8000.json` от прошлых инстансов — использовать только тот порт, который реально LISTENING.
- `http-8001.lock` может быть занят («Device or resource busy») — это нормально, читать надо `.json`, а не `.lock`.
- Сервер глушит себя по idle-таймауту (~120 с без сессии редактора) — если 8001 отвалился, значит редактор закрыт или потерял WS; поднять редактор заново.
- `tasklist` в Git Bash отдаёт UTF-16 — обязательно `| iconv -f UTF-16LE -t UTF-8`, иначе grep скажет «Binary file matches».
- PowerShell-инструмент в этой среде может вернуть пустой вывод на `Get-Process`/`Get-NetTCPConnection` — проверять порты через `netstat` в bash.
- `WScript.Shell` для разбора `.lnk` заблокирован политикой безопасности — парсить ярлык питоном, ища UTF-16 строки.
- Запускать сцену бинарником (`Godot.exe --path <project> res://Main.tscn`) — **крайний** обходной путь: он поднимает вторую копию игры в обход редактора, без game-helper, логов и debugger-моста.

## 8. Если инструменты не появились в сессии

Прописать сервер в `~/.workbuddy-ai/mcp.json` (взять точный `command`/`args` из `~/.codebuddy/mcp.json`, ключ `godot-ai`) и сказать пользователю: активируется после подтверждения («Доверять») в разделе пользовательских коннекторов и перезапуска сессии. До этого пользоваться мостом из п.3.

## 9. Web-экспорт (HTML5) и деплой в git

Проверено на Godot 4.7.2 / проекте `F:/Pets/Cursor/test/new-game-project`.

### 9.1 Пресет `export_presets.cfg`

Ключевое: `export_filter="resources"` + **явный** `export_files`, а не
`all_resources`. `all_resources` тащит все импортированные текстуры проекта
(в этом проекте 343 МБ) — у Vercel лимит 100 МБ на файл, `.pck` не пролезет.

```
[preset.0]
name="Web"
platform="Web"
runnable=true
export_filter="resources"
exclude_filter="web/*"
export_path="web/index.html"
export_files=PackedStringArray("res://Main.tscn", ...)

[preset.0.options]
variant/thread_support=false          # -> web_nothreads_release.zip, COOP/COEP не нужны
vram_texture_compression/for_desktop=true
html/export_icon=true
html/canvas_resize_policy=2
html/custom_html_shell="res://tools/web/shell.html"
progressive_web_app/enabled=false
```

Значения `export_filter` (порядок из hint в бинарнике):
`all_resources` | `scenes` | `resources` | `exclude` | `customized`.
`export_files` лежит в секции `[preset.N]`, а не в `.options`.

Что класть в `export_files`: главную сцену, `icon.svg`, все `.gd`, которые
грузятся динамически (через `load("res://...")`, а не `preload`), и все
текстуры/аудио, на которые ссылаются только строкой. Зависимости
(`ext_resource`, `preload`, атласы, кадры `SpriteFrames`) подтянутся сами.

Проверить, что реально попало в пак (без распаковки):
`re.finditer(rb"res://[A-Za-z0-9_\-/.']{3,140}", open("web/index.pck","rb").read())`.

### 9.2 Запуск экспорта

```bash
mkdir -p web    # Godot НЕ создаёт целевую папку: "Target folder does not exist"
APPDATA="C://Users//tio//AppData//Roaming" \
  "E:/Programs/distr/Godot_v4.7.2-stable_win64.exe" --headless \
  --path "F://Pets//Cursor//test//new-game-project" \
  --export-release "Web" "web/index.html"
```
`ERROR: Could not open 'user://' directory` при этом — нормальный шум.

### 9.3 Убрать заставку Godot

1. `project.godot`:
   ```
   boot_splash/show_image=false
   boot_splash/minimum_display_time=0
   boot_splash/bg_color=Color(<тот же, что default_clear_color>)
   ```
2. Свой HTML-шелл (`html/custom_html_shell`): убрать `<img id="status-splash">`
   и `<progress>`, фон `body` = цвет игры. Плейсхолдеры, которые понимает
   экспортёр: `$GODOT_URL`, `$GODOT_PROJECT_NAME`, `$GODOT_HEAD_INCLUDE`,
   `$GODOT_CONFIG`, `$GODOT_SPLASH`, `$GODOT_SPLASH_CLASSES`,
   `$GODOT_SPLASH_COLOR`, `$GODOT_THREADS_ENABLED`.
   **Грабли**: `$GODOT_URL` = `index.js`, поэтому `href="$GODOT_URL.icon.png"`
   даёт битый `index.js.icon.png`. Ссылки на иконки добавляет сам экспортёр
   при `html/export_icon=true` — в шелле их писать не надо.
3. Свой пиксельный лоадер (когда чёрный экран выглядит как «ничего не грузится»).
   Шаблон: `tools/web/shell.html`. Ключевые приёмы:
   - глифы 5x7 **скопировать из `scripts/pixel_font.gd`** (`GW=5, GH=7, GAP=1`),
     рисовать `fillRect` по `'#'`, `imageSmoothingEnabled = false` — тогда
     лоадер выглядит той же рукой, что и надписи в игре, и не нужен шрифт;
   - канвас лоадера делать DPR-aware: `width = W*dpr`, `setTransform(dpr,0,0,dpr,0,0)`;
   - фон `body` = `default_clear_color` → переход «лоадер → меню» бесшовный;
   - в конце — `statusOverlay.remove()` (не `display:none`), это единственное
     место, где кастомный шелл отличается по логике от дефолтного.

4. **Прогресс: НЕ завязываться на `onProgress`.** Это главные грабли всего
   лоадера, стоившие бага «на телефоне висит на 95%, на ПК ок».

   Что реально приходит в `onProgress(current, total)`: в `index.js` есть
   `animateProgress()`, который суммирует `loaded`/`total` по `loadingFiles`
   и вызывает `progressFunc` **только когда они изменились**, а rAF-цепочку
   останавливает, как только все файлы `done`. `total` берётся не из
   заголовка ответа, а из `fileSizes` в `GODOT_CONFIG` (запекается при
   экспорте). Следствие: любой сбой этой цепочки — rAF затроттлен на
   мобильном, fetch приостановлен при сворачивании приложения, ретрай
   обнулил `loaded` — оставляет `current/total` меньше 1 **навсегда**.

   Поэтому:
   - единственный надёжный признак готовности — **resolved `startGame()`**;
   - при `finished` цель рисования ставить ровно 1 (`goal = 1`), а не
     `min(target, 1)`: иначе `shown` сходится к застрявшему `target` и
     условие `shown >= 0.999` не выполняется никогда;
   - снятие оверлея дублировать вторым каналом на `setTimeout` — мобильные
     браузеры троттлят `requestAnimationFrame`, и цикл на rAF может просто
     не досчитать до конца;
   - до `finished` держать потолок ~92%, чтобы честные 100% до первого кадра
     не выглядели зависанием;
   - `MIN_SHOW_MS ≈ 600`, чтобы лоадер не мигал на быстром соединении.

5. **Лоадер обязан выглядеть живым.** Честный прогресс умеет замереть:
   во время компиляции wasm колбэка нет вообще (на телефоне это десятки
   секунд), а на медленном канале `target` упирается в потолок. Что делать:
   - по полосе пустить бегущий «огонёк» — и обязательно с **обратной**
     полярностью заливке (тёмное пятно на белом сегменте, светлое на пустом),
     иначе на залитых сегментах его не видно;
   - на потолке менять надпись `LOADING` → `STARTING`: это разные фазы
     (скачивание vs старт движка), и на телефоне разница в минуты;
   - если прогресс честно встал (>30 c без изменений и pck не докачан) —
     показать кнопку перезагрузки. Отличить «встал» от «идёт компиляция»
     можно по `target`: при `target >= 0.999` перезагрузка не поможет;
   - отладочный доступ `window.__ld()` (target/shown/finished) — на телефоне
     это единственный способ понять, где именно застряло.

### 9.4 Дымовой тест в браузере

`tools/web/serve.py` — статик-сервер с правильным MIME (`.wasm` →
`application/wasm`, иначе `WebAssembly.instantiateStreaming` ругается).
Запускать через `run_in_background`, иначе процесс умрёт вместе с командой.

Клик по игре из Playwright: канвас занимает всё окно, а вьюпорт 1280x720
леттербоксится внутри. Координаты экрана:
`s = min(cw/1280, ch/720)`, `ox = (cw - 1280*s)/2`, `oy = (ch - 720*s)/2`,
`screen = (ox + x*s, oy + y*s)`.

Всё в одном вызове `browser_run_code_unsafe`: `page.goto` → `waitForTimeout`
→ `page.mouse` → `page.screenshot`. Если разнести `browser_navigate` и
`browser_take_screenshot` по разным вызовам, страница может уйти в `about:blank`.

**Грабли: `page.mouse.click(x, y)` может не дойти до движка.** Одиночный
`click()` шлёт down+up одной пачкой, и кнопка в меню не срабатывает (игра
остаётся на заставке, а событие в консоли при этом видно). Надёжно работает
только разнесённая последовательность:

```js
await page.mouse.move(x, y); await page.waitForTimeout(120);
await page.mouse.down();     await page.waitForTimeout(140);
await page.mouse.up();
```

Прежде чем чинить гейм-код, проверять именно это — и заодно `elementFromPoint`
и `document.activeElement`: если в консоли видно `pointerdown target=canvas`,
а канвас в фокусе и ничем не перекрыт, значит ввод доходит и виноват тайминг.

Проверять ввод надо и мышью, и клавиатурой (`page.keyboard.down('KeyD')`) —
смена раскладки в браузере не эмулируется, но `physical_keycode`-фикс
проверяется именно так: `page.keyboard.down('KeyD')` шлёт `code: KeyD`.

**Грабли: CDP-эмуляция живёт дольше одного вызова.** `browser_run_code_unsafe`
переиспользует одну и ту же страницу между вызовами, поэтому
`Emulation.setCPUThrottlingRate` / `Network.emulateNetworkConditions`,
выставленные в мобильном тесте, **остаются в силе** в следующем прогоне, и
десктопный замер внезапно показывает 30 c вместо 2. Отлаживать надо на
**новой странице**:

```js
const fresh = await page.context().newPage();
const cdp = await page.context().newCDPSession(fresh);
await cdp.send('Emulation.setCPUThrottlingRate', { rate: 1 });
await cdp.send('Network.emulateNetworkConditions',
  { offline: false, latency: 0, downloadThroughput: -1, uploadThroughput: -1 });
```

Мобильный прогон целиком: `setUserAgentOverride` + `setDeviceMetricsOverride`
(`mobile: true`) + `setTouchEmulationEnabled` + троттлинг. На эмуляции
мобильного игра включает `touch_controls` — это же и проверка тач-управления.

Сколько реально качается: `performance.getEntriesByType('resource')` даёт
`transferSize`/`decodedBodySize` по `index.wasm` и `index.pck`. Полезно знать,
что Vercel **сжимает** их бротли (`Content-Encoding: br`,
`Transfer-Encoding: chunked`), но только на обычный GET — на `Range`-запрос
(в т.ч. `curl -I`/`-r`) сжатия нет, и по заголовкам можно ошибочно решить,
что 60 МБ уезжают в телефон несжатыми.

### 9.5 Раскладко-независимые клавиши

`keycode` в `project.godot` — символ, который выдаёт ТЕКУЩАЯ раскладка ОС.
На RU физическая A приходит как «Ф», InputMap не матчится, WASD мёртв.
Лечится переводом всех событий на `physical_keycode`:
`"keycode":0,"physical_keycode":<старый keycode>`.
Готовый идемпотентный конвертер: `tools/win/make_physical_keys.py`.
В `_input`-хоткеях (`event.keycode == KEY_X`) — то же самое, сравнивать
`physical_keycode`, а `keycode` оставлять фолбэком.

### 9.6 Деплой

`vercel.json`: `"outputDirectory": "web"` + MIME-заголовки для `.wasm`/`.pck`.
Корневой `index.html` с редиректом на `./web/index.html` — страховка, если
Vercel проигнорирует `outputDirectory`.
`.gitignore` обязательно: `.godot/`, тяжёлые исходники ассетов, `.tmp_*`,
`smoke_*`, `web/*.import`, `.workbuddy-ai/`, и **файл с креденшелами**.

#### 9.6.1 «Vercel перестал обновлять сайт» — почти всегда автор коммита

Симптом: пуш проходит, GitHub показывает коммит, а сайт не меняется. В письме
от Vercel: *«attempted to deploy a commit … but they're not a member of the
team»*. **Это не права доступа и не интеграция — это email автора коммита.**

Vercel (Deployment Authorization) резолвит email автора коммита в GitHub-аккаунт
и пускает деплой только если это участник команды. Email-заглушка вроде
`stas@example.com` (`example.com` зарезервирован) не мапится ни на кого →
деплой отклоняется. Диагностика в одну команду:

```bash
git log -1 --format="%an <%ae>"
```

Лечение — подставить noreply-адрес аккаунта. ID берётся из публичного API,
даже для приватных репозиториев:

```bash
curl -s https://api.github.com/users/<LOGIN> | grep '"id"'
# → email = <ID>+<LOGIN>@users.noreply.github.com
```

Дальше — repo-local identity + перезапись авторства всех коммитов:

```bash
git config --local user.name  "<LOGIN>"
git config --local user.email "<ID>+<LOGIN>@users.noreply.github.com"
git branch -f backup-original HEAD          # страховка, объекты те же
FILTER_BRANCH_SQUELCH_WARNING=1 git filter-branch -f --env-filter '
export GIT_AUTHOR_NAME="<LOGIN>"
export GIT_AUTHOR_EMAIL="<ID>+<LOGIN>@users.noreply.github.com"
export GIT_COMMITTER_NAME="<LOGIN>"
export GIT_COMMITTER_EMAIL="<ID>+<LOGIN>@users.noreply.github.com"
' -- --all
git push --force-with-lease=main:<прежний_SHA> origin main
```

Перезапись **не перекачивает блобы**: `filter-branch` меняет только commit-
объекты, деревья и блобы те же, поэтому пуш уходит мгновенно даже на 150 МБ репо.

**Грабли: `--force-with-lease` без аргумента падает с `stale info`**, если
локальной ссылки `refs/remotes/origin/main` нет (частый случай после пуша
из фонового процесса). Передавать lease явно: `--force-with-lease=main:<sha>`.

Проверка, что маппинг появился (для приватного репо нужен токен; в
`.git-credentials` он обычно уже лежит):

```bash
curl -s -H "Authorization: token $T" \
  https://api.github.com/repos/<OWNER>/<REPO>/commits/<SHA> | grep '"login"'
# author.login должен быть не null
```

Деплой после этого стартует за секунды — проверять так:
`curl -s https://<домен>/ | grep -c "function watchdog"` (или любой маркер
из свежего шелла). Не забыть: `git config --global user.email` тоже стоит
поправить, иначе следующие коммиты снова уедут с заглушкой.

#### 9.6.2 Что реально качается в браузер

`performance.getEntriesByType('resource')` по `index.wasm` / `index.pck`
даёт `transferSize` (по сети) и `decodedBodySize` (реально). Замеры на
Vercel для типового проекта:

| файл | raw | по сети (brotli) |
|---|---|---|
| `index.wasm` | 39.5 МБ | ~9.5 МБ (×4.1) |
| `index.pck` | 19.9 МБ | ~19.8 МБ (**не жмётся**) |

`.pck` практически не сжимается, потому что внутри уже сжатые PNG и OGG —
и именно он определяет время загрузки на телефоне. Если надо ускорить
мобильный старт, резать нужно **исходные PNG** (перевод в WebP или
уменьшение разрешения), а не крутить серверные заголовки. Vercel, кстати,
жмёт `.wasm`/`.pck` бротли только на обычный GET — на `Range`/HEAD сжатия
нет, и по `curl -I` легко ошибиться, решив, что 60 МБ уедут несжатыми.
