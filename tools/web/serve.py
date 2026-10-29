"""Локальный статик-сервер для веб-рантайма игры (three.js).

Зачем свой, а не `python -m http.server`: он обслуживает не только статику.
Здесь же живут три служебные ручки:
`POST /__save` (записать файл правок), `POST /__build` (пересобрать уровень
нужным инструментом).
Все три запускает СЕРВЕР, а не страница: дочерний процесс из среды редактора
породить нельзя, `spawnSync` падает с EBUSY, а браузер и вовсе не умеет.

Плюс mimetypes на Windows не знает .wasm и отдаёт его как
application/octet-stream, из-за чего браузер отказывается от
`WebAssembly.instantiateStreaming`. Поэтому словарь EXTRA ниже.

Корень по умолчанию - КАТАЛОГ ИГРЫ, а не подкаталог. Раньше стояло `web`, и
запуск без флагов давал сервер, который не отдаёт вообще ничего из
веб-рантайма: редактор и level.json живут в `web3d/`, а `/web3d/...` на таком
корне - 404. Ошибка выглядела как «редактор сломался», хотя сервер был жив и
послушно печатал `serving ...\\web`. Теперь по умолчанию каталог игры, и
`--dir` нужен только чтобы отдать что-то другое.

usage: python serve.py [--dir .] [--port 8777]
"""
import argparse
import functools
import http.server
import json
import os
import pathlib
import queue
import re
import shutil
import socket
import socketserver
import subprocess
import sys
import threading
import time

EXTRA = {
    ".wasm": "application/wasm",
    ".pck": "application/octet-stream",
    ".js": "text/javascript; charset=utf-8",
    ".mjs": "text/javascript; charset=utf-8",
    ".ogg": "audio/ogg",
    ".png": "image/png",
    ".json": "application/json",
    ".worklet.js": "text/javascript; charset=utf-8",
    ".glb": "model/gltf-binary",
    ".gltf": "model/gltf+json",
}

# Внешние каталоги ассетов (вне корня сервера) - «ссылки по имени».
# Зачем: GLB-модели и сгенерированные арты лежат в КОРНЕ РЕПОЗИТОРИЯ
# (`assets/3d`, `assets/images`, `assets/previews`), а сервер отдаёт каталог
# ИГРЫ. Отдавать корень репозитория целиком нельзя: тогда `--dir` перестаёт
# быть каталогом игры и рушится проверка выше. Поэтому внешние корни
# подмешиваются ТОЧЕЧНО: сопоставление «имя -> реальный путь», и `/__ext/<имя>/...`
# отдаёт файл оттуда. Панель ассетов получает пути вида `ext:3d/nova.glb`.
EXT_ROOTS: dict[str, pathlib.Path] = {}

# Общий каталог студии (`<репозиторий>/studio`). ОДИН на все игры: страница и её
# скрипты. Игра владеет только ДАННЫМИ (`web3d/level*.json`, `web3d/assets`,
# `web3d/levels.json`) и игровым рантаймом (`scene.js`, `engine.js`, `vendor/`).
#
# Зачем: оболочка студии - это то, что правят чаще всего. Пока она копировалась
# в каждую игру, любая правка интерфейса требовала обойти все игры, и «сто игр»
# означали сто копий одного файла. Теперь правка здесь видна сразу всем.
STUDIO_DIR: pathlib.Path | None = None


def studio_target(rel: str):
    """Куда отдать URL `rel` (путь БЕЗ ведущего слэша) — из общего каталога студии.

    Подменяется ТОЛЬКО оболочка: страница и её скрипты. URL при этом не меняется
    (`/web3d/studio.html`), поэтому все относительные пути внутри страницы
    остаются верными: `./vendor/three.module.js` и `../scene.js` уходят в каталог
    ИГРЫ, а не в общий. Именно поэтому вендор и `scene.js` можно не трогать.
    """
    if STUDIO_DIR is None:
        return None
    if rel == "web3d/studio.html":
        return STUDIO_DIR / "studio.html"
    pref = "web3d/studio/"
    if rel.startswith(pref):
        tail = rel[len(pref):]
        # `..` отбиваем здесь же: путь склеивается с общим каталогом, и
        # `web3d/studio/../../..` иначе вывел бы наружу.
        if not tail or ".." in tail.split("/"):
            return None
        return STUDIO_DIR / tail
    return None


def find_repo_root(start):
    """Корень репозитория 3GS_Master по каталогу игры.

    Ищем ПО ПРИЗНАКУ (`pi-home/settings.json` + `agent.cmd`), а не отсчётом
    `..`: сервер поднимается и с `--dir`, и тогда арифметика уровней врёт
    молча — агент запустился бы с чужим конфигом, то есть без MCP и с
    глобальным провайдером. Симптом был бы «агент отвечает не то», без единой
    ошибки в логе.

    Кандидаты, в этом порядке:
      0. `GS_REPO` из окружения. Нужен игре ВНЕ репозитория: там ни `--dir`, ни
         путь самого serve.py не ведут к корню (игра лежит на другом диске), и
         без явного указания чат отваливался бы с 500 «не нашёл корень».
         Лаунчер, который знает корень, просто выставляет переменную.
      1. каталог, который отдаёт сервер (`--dir`). Так работает игра ВНУТРИ
         репозитория;
      2. каталог самого serve.py. Это спасает случай «игра лежит вне
         репозитория, а запускают канонический сервер из репозитория».
    """
    cands = []
    env = os.environ.get("GS_REPO")
    if env:
        # resolve() обязателен: лаунчер новой игры отдаёт корень как
        # `projects\games\<имя>\..\..`, и без нормализации `parents` у такого пути
        # перечисляет несуществующие каталоги (`projects\games\<имя>\pi-home`), а
        # настоящий корень теряется в середине списка.
        cands.append(pathlib.Path(env).expanduser().resolve())
    cands.append(pathlib.Path(start).resolve())
    cands.append(pathlib.Path(__file__).resolve().parent)
    for base in cands:
        for d in (base, *base.parents):
            if ((d / "pi-home" / "settings.json").is_file()
                    and (d / "agent.cmd").is_file()):
                return d
    return None


class Handler(http.server.SimpleHTTPRequestHandler):
    def guess_type(self, path):
        p = str(path).lower()
        for ext, mime in EXTRA.items():
            if p.endswith(ext):
                return mime
        return super().guess_type(path)

    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def log_message(self, fmt, *args):
        print("[serve]", fmt % args, flush=True)

    # ------------------------------------------------------- запись правок
    # ЕДИНСТВЕННОЕ место во всём стенде, которое пишет на диск. Нужно редактору
    # расстановки (`web3d/editor.html`): он накапливает сдвиги узлов и шлёт их
    # сюда - браузер сам файл записать не может, а качать через загрузку неудобно
    # и теряет предыдущие правки.
    #
    # Правила жёсткие, потому что это запись, а не чтение:
    #   * только POST и только на /__save;
    #   * имя - относительный путь из сегментов `<имя>.json`, ASCII, без '..',
    #     без ведущего слэша, без бэкслэшей и пробелов;
    #   * итоговый путь обязан лежать ВНУТРИ --dir (проверка по resolve, а не по
    #     строке: '..\\' и симлинк ловятся одинаково);
    #   * тело обязано быть JSON-объектом.
    #
    # ПОДКАТАЛОГ РАЗРЕШЁН НЕ ДЛЯ УДОБСТВА, А ЧТОБЫ УБИТЬ КЛАСС ОШИБОК. Редактор
    # лежит в web3d/, и правки обязаны лежать рядом с тем level1.json, который
    # они правят. Пока имя файла было голым (`level1_edit.json`), сервер писал
    # его в СВОЙ корень (каталог игры), а tools/level_build.py читал
    # web3d/level1_edit.json - и «Сохранить и пересобрать» молча теряло работу:
    # редактор отчитывался об успехе, сборка печатала «правок руками: нет».
    # Ни одного отказа, ни одной ошибки в консоли - просто выравнивание исчезало.
    # Поэтому URL теперь называет ТОТ ЖЕ путь, что и сборщик, а ответ /__save
    # возвращает фактически записанный путь, чтобы расхождение было видно сразу.
    def _safe_json_name(self, name):
        seg = r"[A-Za-z0-9_.-]+"
        if not re.fullmatch(seg + r"(/" + seg + r")*\.json", name) or ".." in name:
            return None
        root = pathlib.Path(self.directory).resolve()
        dest = (root / name).resolve()
        # `dest.parent == root` - файл прямо в корне, `root in dest.parents` -
        # в подкаталоге. Вместе это «строго внутри корня».
        return dest if dest.parent == root or root in dest.parents else None

    def _level_flags(self, lvl):
        """Запись уровня из `web3d/levels.json`. Пусто, если манифеста нет.

        Манифест — единственное место, где сказано, ЧЕМ уровень собирается
        (поле `builder`) и можно ли его править руками (`editable`). Читаем его,
        а не гадаем по имени уровня: имя придумывает агент.
        """
        try:
            man = json.loads((pathlib.Path(self.directory).resolve()
                              / "web3d" / "levels.json").read_text(encoding="utf-8"))
        except (OSError, ValueError):
            return {}
        lv = (man.get("levels") or {}).get(lvl)
        return lv if isinstance(lv, dict) else {}

    def _build_tool(self, game, lvl):
        """Какой инструмент пересобирает этот уровень.

        Порядок решения:
          1. явное `builder` в манифесте (`"level_apply"` / `"level_build"`);
          2. `level_build.py`, если он у игры ЕСТЬ и уровень не `level_0`
             (у ded_space `level_0` — родной исходник, `level_1` собирается
             из таблиц арта);
          3. `level_apply.py` — наложение правок, есть у любой игры;
          4. тот из двух, что найдётся.
        """
        flags = self._level_flags(lvl)
        tools = game / "tools"
        want = flags.get("builder")
        if isinstance(want, str) and want:
            cand = tools / (want if want.endswith(".py") else want + ".py")
            if cand.is_file():
                return cand
        build, apply_ = tools / "level_build.py", tools / "level_apply.py"
        if build.is_file() and lvl != "level_0":
            return build
        if apply_.is_file():
            return apply_
        return build if build.is_file() else None

    def _lint(self, lvl):
        """`/__lint` — прогон линтера формата уровня.

        Отдельная ручка, потому что «уровень создан» и «уровень работает» —
        разные вещи, и вторая проверяется только запуском. Линтер ловит ровно
        тот класс ошибок, который не падает и не рисуется: ссылку на файл,
        которого нет, неизвестный тип узла, `textures` с ключом-именем. Без
        этой ручки агент отчитывался «уровень готов», а в сцене было пусто.
        """
        flags = self._level_flags(lvl)
        name = flags.get("file") or "level.json"
        game = pathlib.Path(self.directory).resolve()
        repo = find_repo_root(game)
        # Линтер универсальный: он живёт в `tools/` репозитория, но у игры может
        # лежать своя копия — берём её первой, если есть.
        cands = [game / "tools" / "level_lint.py"]
        if repo:
            cands.append(repo / "tools" / "level_lint.py")
        script = next((c for c in cands if c.is_file()), None)
        if script is None:
            self.send_error(500, "нет tools/level_lint.py")
            return
        target = f"web3d/{name}"
        p = subprocess.run([sys.executable, str(script), target],
                           cwd=str(game), capture_output=True, text=True,
                           encoding="utf-8")
        self._send_json({"ok": p.returncode == 0, "code": p.returncode,
                         "level": lvl, "file": target,
                         "out": (p.stdout or "") + (p.stderr or "")})

    def _send_json(self, obj, code=200):
        out = json.dumps(obj, ensure_ascii=False).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(out)))
        self.end_headers()
        self.wfile.write(out)

    def _read_body(self):
        """Тело запроса. Понимает и Content-Length, и chunked.

        Почему не только Content-Length: клиент, который пишет тело отдельными
        `write()` и лишь потом `end()` (так делает node), шлёт
        `Transfer-Encoding: chunked` и Content-Length НЕ ставит вообще. Код,
        читавший ровно Content-Length байт, читал ноль и отвечал 400 «bad json»
        на полностью корректный запрос. Ошибка была почти невидимой: первое
        сохранение делал браузер (fetch ставит Content-Length сам) и оно
        проходило, а все следующие - скрипт прогона, и они молча не доезжали,
        выглядя потом как «сборка не увидела правок».
        """
        if "chunked" in (self.headers.get("Transfer-Encoding") or "").lower():
            buf = bytearray()
            while True:
                size = int(self.rfile.readline(65536).split(b";")[0].strip()
                           or b"0", 16)
                if size == 0:
                    self.rfile.readline(65536)          # CRLF после последнего
                    break
                buf += self.rfile.read(size)
                self.rfile.read(2)                      # CRLF после чанка
            return bytes(buf)
        n = int(self.headers.get("Content-Length") or 0)
        return self.rfile.read(n) if n > 0 else b""

    def translate_path(self, path):
        """URL -> файл. Единственная точка, где решается, ОТКУДА отдать файл.

        И статика, и `send_head` идут через неё, поэтому подменять что-то ещё не
        нужно. Оболочка студии берётся из общего каталога, всё остальное — из
        каталога игры.

        Подменяем ТОЛЬКО если общий файл существует. У старой игры может лежать
        своя копия студии: тогда она останется рабочей, и это лучше, чем 404 на
        страницу из-за того, что общий каталог не нашли.
        """
        from urllib.parse import urlparse, unquote
        rel = unquote(urlparse(path).path).lstrip("/")
        hit = studio_target(rel)
        if hit is not None and hit.is_file():
            return str(hit)
        return super().translate_path(path)

    def do_GET(self):
        from urllib.parse import urlparse, parse_qs
        u = urlparse(self.path)
        # Список ассетов для рабочей области студии: картинки (превью генерации)
        # и GLB (3D-просмотрщик). Отдельная ручка, а не обход каталога из
        # браузера: у статики нет листинга, а гадать имена нельзя - файл,
        # которого нет, даёт 404 в консоли, и гейты читают это как падение.
        #
        # Отдаём ОТНОСИТЕЛЬНЫЕ пути от корня сервера: их можно сразу подставить
        # в <img src> / fetch, не зная, откуда открыта страница.
        if u.path == "/__assets":
            root = pathlib.Path(self.directory).resolve()
            imgs, glbs = [], []

            def add(rel, size):
                if size <= 0:
                    return
                (glbs if rel.suffix.lower() == ".glb" else imgs).append(
                    {"path": rel.as_posix(), "bytes": size})

            def scan(sub, exts, limit=4000):
                d = root / sub
                if not d.is_dir():
                    return
                n = 0
                for p in sorted(d.rglob("*")):
                    if n >= limit:
                        break
                    if not p.is_file() or p.suffix.lower() not in exts:
                        continue
                    try:
                        size = p.stat().st_size
                    except OSError:
                        continue
                    if size == 0:
                        continue
                    add(p.relative_to(root), size)
                    n += 1

            def scan_ext(name, d, exts, limit=2000):
                """То же, но с меткой `ext:<name>/<отн. путь>`.

                Метка — это адресуемость: путь обязан быть однозначным, иначе
                `assets/3d` из корня репозитория и `assets/3d` из каталога игры
                (если появится) стали бы одним и тем же ключом.
                """
                if not d.is_dir():
                    return
                n = 0
                for p in sorted(d.rglob("*")):
                    if n >= limit:
                        break
                    if not p.is_file() or p.suffix.lower() not in exts:
                        continue
                    try:
                        size = p.stat().st_size
                    except OSError:
                        continue
                    if size == 0:
                        continue
                    rel = pathlib.Path("ext:" + name) / p.relative_to(d)
                    (glbs if p.suffix.lower() == ".glb" else imgs).append(
                        {"path": rel.as_posix(), "bytes": size})
                    n += 1

            # Сначала то, чем игра реально живёт, потом остальное. Порядок в
            # списке - это порядок в панели, и он должен читаться как «начни
            # отсюда», а не как «отсортируй по алфавиту 400 PNG».
            scan("Shrooms", {".png"}, limit=800)
            scan("assets", {".png", ".jpg", ".jpeg", ".webp"}, limit=1200)
            scan("shots", {".png"}, limit=200)
            scan(".", {".png", ".jpg", ".jpeg", ".webp", ".glb"}, limit=1200)
            # Внешние корни репозитория (см. EXT_ROOTS).
            for nm, d in EXT_ROOTS.items():
                scan_ext(nm, d, {".glb", ".gltf", ".png", ".jpg", ".jpeg", ".webp"})
            # дедуп: файл мог попасть и в точечном скане, и в общем
            seen, uniq = set(), []
            for it in imgs:
                if it["path"] in seen:
                    continue
                seen.add(it["path"])
                uniq.append(it)
            # `game` - каталог проекта относительно репозитория (`projects/games/<имя>`).
            # Нужен странице, чтобы показать в чате, ГДЕ работает агент: без
            # этого единственным источником правды оставался текст промпта, и
            # на новой игре чат молча правил ded_space.
            _repo = find_repo_root(root)
            try:
                game = root.relative_to(_repo).as_posix() if _repo else root.name
            except ValueError:
                game = root.name
            self._send_json({"images": uniq, "glbs": glbs, "root": str(root),
                             "game": game})
            return
        # Чтение файла правок. Отдельный эндпоинт, а не статика, ровно по одной
        # причине: отсутствие файла - это НОРМА (уровень без ручных правок), а
        # статика на отсутствующий файл отвечает 404, и браузер печатает это в
        # консоль как ошибку. Прогон читает консоль, и «норма» выглядела бы как
        # падение. Здесь отсутствие файла - это 200 и пустой список правок.
        if u.path == "/__edits":
            name = (parse_qs(u.query).get("file") or [""])[0]
            dest = self._safe_json_name(name)
            if dest is None:
                self.send_error(400, "file must be <name>.json")
                return
            if dest.is_file():
                self._send_json(json.loads(dest.read_text(encoding="utf-8")))
            else:
                self._send_json({"nodes": {}})
            return
        # Проверка формата уровня. См. `_lint`: «создан» и «работает» — разное,
        # и второе видно только прогоном линтера.
        if u.path == "/__lint":
            self._lint((parse_qs(u.query).get("level") or [""])[0])
            return
        # Файл из внешнего корня: `/__ext/<имя>/<относительный путь>`.
        # Проверка «строго внутри своего корня» - та же, что у записи правок:
        # `..` и симлинк ловятся одним resolve, а не сравнением строк.
        if u.path.startswith("/__ext/"):
            rel = u.path[len("/__ext/"):]
            name, _, tail = rel.partition("/")
            base = EXT_ROOTS.get(name)
            if base is None or not tail:
                self.send_error(404, f"нет внешнего корня {name!r}")
                return
            base = base.resolve()
            dest = (base / tail).resolve()
            if not (dest == base or base in dest.parents) or not dest.is_file():
                self.send_error(404, "нет файла")
                return
            data = dest.read_bytes()
            self.send_response(200)
            self.send_header("Content-Type", self.guess_type(str(dest)))
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)
            return
        super().do_GET()

    def do_POST(self):
        from urllib.parse import urlparse, parse_qs
        u = urlparse(self.path)
        if u.path == "/__build":
            # Пересборка уровня. Нужна редактору («Сохранить и пересобрать») и
            # гейту: правка расстановки живёт в отдельном файле, и «доехала ли
            # она до уровня» проверяется только запуском инструмента. Запускает
            # СЕРВЕР, а не страница: страница не может, а node в этой среде не
            # может породить процесс вообще (spawnSync -> EBUSY на чём угодно,
            # включая cmd). sys.executable - тот же питон, что поднял сервер.
            #
            # Инструмент выбираем по СМЫСЛУ уровня, а НЕ по его имени:
            #   * `level_apply.py` - уровень и есть исходник (`level.json`),
            #     накладываем только правки;
            #   * `level_build.py` - уровень СОБИРАЕТСЯ из таблиц арта.
            # Раньше стояло `{"level_0": "level_apply.py"}.get(lvl, "level_build.py")`,
            # то есть ЛЮБОЕ другое имя уровня тянуло сборщик. Агент вправе назвать
            # уровень как угодно - и на игре без `level_build.py` (у новой игры его
            # нет) «Сохранить и пересобрать» падало с 500 «нет tools/level_build.py»,
            # хотя накладывать было что.
            lvl = (parse_qs(u.query).get("level") or [""])[0]
            game = pathlib.Path(self.directory).resolve()
            script = self._build_tool(game, lvl)
            if script is None:
                self.send_error(
                    500, "нет ни tools/level_apply.py, ни tools/level_build.py")
                return
            p = subprocess.run([sys.executable, str(script)],
                               cwd=str(script.parents[1]),
                               capture_output=True, text=True, encoding="utf-8")
            self._send_json({"ok": p.returncode == 0, "code": p.returncode,
                             "tool": script.name,
                             "out": (p.stdout or "") + (p.stderr or "")})
            return
        if u.path != "/__save":
            self.send_error(404, "only /__save and /__build")
            return
        name = (parse_qs(u.query).get("file") or [""])[0]
        dest = self._safe_json_name(name)
        if dest is None:
            self.send_error(400, "file must be <name>.json")
            return
        try:
            data = json.loads(self._read_body().decode("utf-8"))
        except Exception as e:                      # noqa: BLE001
            self.send_error(400, f"bad json: {e}")
            return
        if not isinstance(data, dict):
            self.send_error(400, "top level must be an object")
            return
        dest.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n",
                        encoding="utf-8")
        # Путь возвращаем ОТНОСИТЕЛЬНО корня - ровно в том виде, в каком его
        # должен читать сборщик. Гейт сверяет это поле со своим ожиданием, и
        # «файл уехал не туда» перестаёт быть невидимым.
        rel = dest.relative_to(pathlib.Path(self.directory).resolve()).as_posix()
        print(f"[serve] saved {dest} ({dest.stat().st_size} b)", flush=True)
        self._send_json({"ok": True, "file": name, "path": rel,
                         "bytes": dest.stat().st_size})


class Server(socketserver.ThreadingTCPServer):
    allow_reuse_address = True
    daemon_threads = True
    # Очередь accept. По умолчанию socketserver ставит 5, и этого НЕ ХВАТАЕТ:
    # страница тянет ~60 текстур разом, Chrome открывает их пачкой, и всё, что
    # не влезло в очередь, получает ERR_CONNECTION_REFUSED - а это в отчёте
    # прогона выглядит как ошибка консоли, то есть как падение гейта. Гейт при
    # этом падал не из-за игры: у прогона с 21 отказом симуляция прошла целиком,
    # а часть текстур не загрузилась. Ошибка была в стенде.
    request_queue_size = 128

    def handle_error(self, request, client_address):
        """Обрыв клиента - это норма, а не ошибка сервера.

        Браузер штатно рвёт соединение: закрыли вкладку, отменили запрос,
        пересобрали web/ прямо во время выдачи. Без этого socketserver печатает
        полный traceback ConnectionResetError на каждый такой случай, и в логе
        отладки настоящие ошибки тонут в шуме.
        """
        exc = sys.exc_info()[1]
        if isinstance(exc, (ConnectionResetError, ConnectionAbortedError,
                            BrokenPipeError)):
            return
        super().handle_error(request, client_address)


def main() -> None:
    ap = argparse.ArgumentParser()
    # Корень по умолчанию считаем ОТ САМОГО СКРИПТА, а не от текущего каталога:
    # serve.py лежит в tools/web/, значит каталог игры - на два уровня выше. Так
    # команда без флагов работает и из корня игры, и откуда угодно ещё. Дефолт
    # `web` раньше давал сервер, который не отдаёт ничего из веб-рантайма.
    game_dir = pathlib.Path(__file__).resolve().parents[2]
    ap.add_argument("--dir", default=str(game_dir))
    ap.add_argument("--port", type=int, default=8777)
    ap.add_argument("--bind", default="127.0.0.1")    # Внешние корни ассетов: `имя=путь`, можно несколько раз. По умолчанию
    # подключаем то, что есть в репозитории, - модели и сгенерированные арты.
    # Дефолт нужен, чтобы студия показывала GLB сразу, без флагов: пустая
    # панель «Доступные GLB» выглядит как поломка, а не как «забыли --assets».
    ap.add_argument("--assets", action="append", default=[],
                    metavar="ИМЯ=ПУТЬ",
                    help="внешний каталог ассетов (можно несколько раз)")
    a = ap.parse_args()
    root = pathlib.Path(a.dir).resolve()
    # Корень РЕПОЗИТОРИЯ для внешних каталогов ассетов. Считаем его тем же
    # поиском по признаку (find_repo_root), а НЕ арифметикой `game_dir.parents[1]`:
    # у игры вне репозитория арифметика даёт соседний каталог, `EXT_ROOTS`
    # остаётся пустым, и панель ассетов молча показывает одни PNG без единого
    # GLB. Ошибка тихая и потому неприятная — ровно как с прежним дефолтом `web`.
    repo = find_repo_root(root) or game_dir.parents[1]
    # Общий каталог студии: страница и её скрипты, ОДНИ на все игры. См.
    # `studio_target`. Если каталога нет (репозиторий старее этой правки), или в
    # нём нет страницы, остаётся прежнее поведение — студия из самой игры.
    global STUDIO_DIR
    STUDIO_DIR = repo / "studio"
    if not (STUDIO_DIR / "studio.html").is_file():
        STUDIO_DIR = None
    for spec in (a.assets or [f"3d={repo / 'assets' / '3d'}",
                              f"images={repo / 'assets' / 'images'}",
                              f"previews={repo / 'assets' / 'previews'}"]):
        if "=" not in spec:
            sys.exit(f"--assets: ожидалось ИМЯ=ПУТЬ, получено {spec!r}")
        nm, _, p = spec.partition("=")
        d = pathlib.Path(p)
        if d.is_dir():
            EXT_ROOTS[nm] = d.resolve()
    # Проверяем, что корень — действительно каталог игры, а не что попало. Без
    # этого опечатка или устаревший дефолт даёт «сервер жив, но страниц нет», и
    # искать причину приходится в браузере. Признак берём тот, что не зависит от
    # уровня: веб-рантайм и сборщик уровня.
    # Признак «это каталог игры» берём по МАНИФЕСТУ уровней, а не по
    # `tools/level_build.py`. Сборщик есть только у level_1 в ded_space, а
    # `web3d/levels.json` есть у любой игры формата 3GS — в том числе у новой,
    # где сборщика ещё нет вовсе. С прежней проверкой новая игра не могла даже
    # поднять сервер: `--dir <несуществующий>` падал на старте, и это выглядело как
    # «студия не работает на новом проекте».
    # Строгость сохранена: `--dir <игра>/web3d` по-прежнему падает, потому что
    # там нет `web3d/levels.json` — а именно эту ошибку проверка и ловила.
    manifest = root / "web3d" / "levels.json"
    if not manifest.is_file():
        sys.exit(f"{root}: не похоже на каталог игры - нет web3d/levels.json.\n"
                 f"Запускайте из корня игры или укажите --dir <каталог игры> "
                 f"(не `web`: веб-рантайм лежит в web3d/).\n"
                 f"Новая игра: newgame.cmd <имя> создаёт скелет.")
    handler = functools.partial(Handler, directory=str(root))
    # Windows разрешает ВТОРОЙ bind на тот же порт при allow_reuse_address, и
    # тогда два сервера начинают ДЕЛИТЬ соединения: часть запросов уходит
    # старому (без новых эндпоинтов) и отвечает 404/501, часть - новому. Симптом
    # плавающий и выглядит как «гейт иногда падает сам по себе»; на этом уже
    # потеряно полчаса. Проверяем порт ДО bind.
    probe = socket.socket()
    probe.settimeout(0.3)
    if probe.connect_ex((a.bind, a.port)) == 0:
        print(f"!!! порт {a.port} УЖЕ ЗАНЯТ: два сервера будут делить соединения, "
              f"и часть запросов уйдёт старому. Убейте его или возьмите другой "
              f"порт.", flush=True)
    probe.close()
    with Server((a.bind, a.port), handler) as httpd:
        print(f"serving {root} on http://{a.bind}:{a.port}/", flush=True)
        if EXT_ROOTS:
            for nm, d in EXT_ROOTS.items():
                print(f"  ext:{nm} -> {d}", flush=True)
        else:
            print("  внешних каталогов ассетов нет (GLB в панели не появятся)",
                  flush=True)
        httpd.serve_forever()


if __name__ == "__main__":
    main()
