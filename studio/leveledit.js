/*
 * leveledit.js — визуальный редактор уровня для студии.
 *
 * Это НАСЛЕДНИК `web3d/editor.html`, а не второй редактор рядом с ним. Тот файл
 * был целой страницей: он сам грузил манифест, сам строил сцену, сам рисовал
 * себе UI. Здесь та же логика вынесена в класс, чтобы студия могла положить её
 * в свою панель. Правила расстановки при этом НЕ переписаны — они взяты как
 * есть, потому что каждое из них стоило потерянной работы:
 *
 *   * адрес узла — ПОЛЕ `path`, и оно ПЛОСКОЕ (`JumpSpot3`, не
 *     `Props/JumpSpot3`). Именно его scene.js кладёт в userData.path;
 *   * правки живут в отдельном `<level>_edit.json` рядом с уровнем, потому что
 *     `level1.json` собирается заново из таблиц арта, и любая правка «в файле»
 *     исчезла бы при первой же пересборке;
 *   * слои параллакса, полосы арта, стены и `Ceiling` не правятся, и запрет
 *     распространяется на ВСЁ поддерево узла (позиция слоя параллакса
 *     ВЫЧИСЛЯЕТСЯ из камеры — подвинуть её руками нельзя, она тут же вернётся);
 *   * `scale` только для чтения: размер коллайдера выводится как
 *     текстура × scale, то есть поле, которое меняет вид и не сохраняется,
 *     — это худший вид обмана в редакторе.
 *
 * ── Что добавлено против editor.html ───────────────────────────────────────
 *   1. ДОБАВЛЕНИЕ и УДАЛЕНИЕ узлов. В старом редакторе их не было вовсе.
 *      Домен — тоже файл правок: у него появились секции `add` и `remove`
 *      (см. `toOverlay`). Сборщик их пока не читает — см. ПРЕДУПРЕЖДЕНИЕ в
 *      `_applyLocal`, почему это честно сказано, а не сделано молча.
 *   2. Слои как список: видимость, заморозка (заблокировать от мыши), выбор
 *      «активного» слоя для новых узлов.
 *   3. Точки платформы в стиле Godot: узел площадки тянут за точку «стояния»,
 *      а коллайдер площадки идёт за ним ПАРОЙ (это правило было и раньше — оно
 *      и есть «ходьба соблюдается»).
 */
import * as THREE from '../vendor/three.module.js';
import { LevelScene } from '../scene.js';

/**
 * Re-export: студии нужны те же КЛАССЫ three, а не «ещё одна копия модуля».
 * Если app.js импортирует `three.module.js` сам, браузер отдаст тот же URL и
 * модуль будет один — но полагаться на это в коде, который читают люди, хуже,
 * чем сказать явно: «Box3 бери отсюда».
 */
export { THREE };

/** Слои, которые не правятся: их позиция не принадлежит человеку. */
const NO_EDIT = /^(Backdrop|GameplayLayer\d*|Terrain\d*|WallLeft|WallRight|Ceiling|Strip)$/;

export class LevelEditor {
  /**
   * @param {HTMLElement} host
   * @param {object} opts { onChange, onSelect, onLog }
   */
  constructor(host, opts = {}) {
    this.host = host;
    this.opts = opts;
    this.cb = opts;

    this.renderer = new THREE.WebGLRenderer({ antialias: false });
    this.renderer.setPixelRatio(Math.min(devicePixelRatio, 2));
    this.renderer.outputColorSpace = THREE.SRGBColorSpace;
    host.appendChild(this.renderer.domElement);
    this.canvas = this.renderer.domElement;
    this.canvas.style.display = 'block';

    this.mode = '2d';                 // 2d | 3d
    this.zoom = 0.32;
    this.pan = new THREE.Vector2(0, 0);
    this.orbit = { yaw: 0.6, pitch: 0.45, dist: 2600, target: new THREE.Vector3() };

    this.edits = {};                  // снятые и ещё не сохранённые правки
    this.orig = {};                   // исходные позиции (для undo/REVERT)
    this.history = [];
    this.sel = null;
    this.activeLayer = null;
    this.layers = new Map();          // path -> { visible, locked }
    this.pickable = [];
    this.links = new Map();           // JumpSpotN -> JumpSpotPlatformN

    this.showParallax = false;
    this.showCollisions = false;

    this._bindPointer();
    this._bindKeys();
    this._raf = null;
  }

  /* --------------------------------------------------------------- загрузка */

  async load(levelFile, def = {}) {
    this.levelFile = levelFile;
    this.def = def;
    // Каталог СТРАНИЦЫ, а не модуля: `import.meta.url` здесь дал бы
    // `web3d/studio/`, и уровень искался бы не там. Студия — это
    // `web3d/studio.html`, и уровень лежит рядом с ней.
    const dir = location.pathname.replace(/[^/]*$/, '');
    this.editFile = (dir + levelFile.replace(/\.json$/, '_edit.json')).replace(/^\/+/, '');
    this.levelPath = (dir + levelFile).replace(/^\/+/, '');

    const json = await (await fetch('./' + levelFile, { cache: 'no-cache' })).json();
    if (this.gs) { this.gs.scene.clear(); this.gs = null; }
    this.gs = new LevelScene(json);
    await this.gs.load(() => {});
    this.gs.autoWalk = false;
    this.gs.setCollisions(this.showCollisions);
    this.gs.cameraLimits = { left: -700, top: -700, right: 4300, bottom: 1500 };

    this._collect();
    this._buildLayers();
    await this.loadEdits();
    this.resize();
    this.applyView();
    // Кадрируем по уровню СРАЗУ. Иначе первый кадр показывает угол мира: зум
    // по умолчанию (0.32) и панорама (0,0) — это верхний левый угол, где у
    // уровня пустота. «Открыл редактор, а там ничего» — худшее первое
    // впечатление, и лечится оно одной строкой.
    this.fit();
    if (this.cb.onReady) this.cb.onReady(this);
  }

  /**
   * Показать весь уровень: зум и панорама по габаритам сцены.
   *
   * Габариты считаем по ПРАВИМЫМ узлам, а не по корню сцены. В корне лежит
   * `Backdrop` — ColorRect размером 8437×4813, который заведомо больше
   * геймплея (он накрывает кадр с запасом под параллакс и движение камеры).
   * Подгон по корню даёт кадр, где уровень — крошка в центре пустого
   * прямоугольника: «Fit» отрабатывает, а смотреть не на что.
   */
  fit() {
    const b = new THREE.Box3();
    const tmp = new THREE.Box3();
    for (const e of this.editable) {
      tmp.setFromObject(e.obj);
      if (!tmp.isEmpty()) b.union(tmp);
    }
    if (b.isEmpty()) b.setFromObject(this.gs.root);
    if (b.isEmpty()) return;
    const size = b.getSize(new THREE.Vector3());
    const c = b.getCenter(new THREE.Vector3());
    const w = this.canvas.clientWidth || 1200, h = this.canvas.clientHeight || 700;
    const zx = w / Math.max(1, size.x), zy = h / Math.max(1, size.y);
    this.zoom = Math.max(0.02, Math.min(4, Math.min(zx, zy) * 0.88));
    this.pan.x = c.x;
    this.pan.y = -c.y;
    this.applyView();
    this.resize();
  }

  /** Узлы, которые человек вправе двигать. */
  _collect() {
    this.editable = [];
    this.objByPath = new Map();
    const self = this;

    // Обход по СВЯЗИ, а не по индексу. Соблазн взять `obj.children[i]` и
    // сопоставить с `node.children[i]` велик, и он же — источник тихой поломки:
    // Parallax2D вставляет в группу ПРОМЕЖУТОЧНЫЙ узел `content` (и ещё плитки
    // `repeat_times`), из-за которого дети группы сдвигаются относительно детей
    // узла. Обход по индексу после этого промахивается мимо ВСЕГО поддерева —
    // редактор показывает ноль узлов и пустой кадр, без единой ошибки.
    // Поэтому идём по объектам и берём узел из `userData.node`: scene.js
    // кладёт его каждому объекту, и эта связь устойчива к любым вставкам.
    // `parentPath` — путь узла-РОДИТЕЛЯ в дереве уровня. Нужен добавлению: новый
    // узел вставляется рядом с образцом, а «рядом» без родителя не выразить.
    // Берём именно путь УЗЛА, а не имя three-объекта: у слоя параллакса дети
    // лежат внутри промежуточной группы `content`, и её имя в дереве уровня
    // ничего не значит.
    (function walk(obj, skip, parentPath) {
      const node = obj.userData && obj.userData.node;
      if (node) {
        const path = node.path || obj.userData.path;
        const isForbidden = skip || NO_EDIT.test(node.name || '');
        const isLayer = node.type === 'Parallax2D';
        if (obj.name && node.path) self.objByPath.set(node.path, obj);
        const p = node.props || {};
        if (!isForbidden && !isLayer && path && p.position) {
          self.editable.push({ path, obj, node, parent: parentPath || null });
        }
        for (const child of obj.children) {
          walk(child, isForbidden || isLayer, path);
        }
      } else {
        // Группа без узла (`content` слоя параллакса) — её дети принадлежат
        // тому же узлу, поэтому идём внутрь с тем же флагом запрета и тем же
        // родителем.
        for (const child of obj.children) walk(child, skip, parentPath);
      }
    })(this.gs.root, false);

    this.orig = {};
    for (const e of this.editable) {
      // Уровневые координаты: three.y = -level.y (единственное место перевода).
      this.orig[e.path] = [e.obj.position.x, -e.obj.position.y];
    }
    this.editableByPath = new Map(this.editable.map((e) => [e.path, e]));
    // Кэш для _layerOf: пересобирается при каждом _collect (смена уровня), иначе
    // слои считались бы по узлам ПРЕДЫДУЩЕГО уровня.
    this._editableSet = new Set(this.editable.map((e) => e.obj));

    // Площадка и её коллайдер — ПАРА, и двигаются вместе. В дереве они сёстры
    // (не родитель/ребёнок), поэтому связь ищется по имени: `JumpSpot3` ↔
    // `JumpSpotPlatform3`.
    this.links = new Map();
    for (const e of this.editable) {
      const m = /^JumpSpot(\d+)$/.exec(e.path);
      if (!m) continue;
      const partner = `JumpSpotPlatform${m[1]}`;
      if (this.editableByPath.has(partner)) {
        this.links.set(e.path, partner);
        this.links.set(partner, e.path);
      }
    }
    this.rebuildPickable();
  }

  _buildLayers() {
    this.layers.clear();
    const seen = [];
    for (const e of this.editable) {
      const com = this._layerOf(e.obj);
      if (!this.layers.has(com)) {
        this.layers.set(com, { visible: true, locked: false, count: 0 });
        seen.push(com);
      }
      this.layers.get(com).count++;
    }
    // Порядок слоёв — порядок В ДЕРЕВЕ, а не по алфавиту. Слои рисуются друг
    // над другом в порядке обхода, и алфавитный список читается как случайный:
    // человек ищет «Props», а видит список, где первым идёт AmmoPickup1150.
    const order = [];
    const seenSet = new Set();
    for (const e of this.editable) {
      const com = this._layerOf(e.obj);
      if (!seenSet.has(com)) { seenSet.add(com); order.push(com); }
    }
    this.layerOrder = order;
  }

  /**
   * Слой узла — имя БЛИЖАЙШЕЙ группы-контейнера, внутри которой он лежит.
   *
   * Почему не «верхний исключённый предок»: у `level_1` промежуточных контейнеров
   * почти нет, и такой обход возвращал бы самого узла — каждый ассет становился
   * бы отдельным «слоем». Список слоёв превращался бы в копию списка узлов, и
   * тумблер видимости переставал что-либо значить.
   *
   * Слой = БЛИЖАЙШИЙ узел-группа вверх по дереву. Для `JumpSpot3` это `Props`;
   * для его ребёнка-коллайдера — тоже `Props` (у самого площадочного узла нет
   * детей-контейнеров, и подниматься надо ЧЕРЕЗ него); для `Player` — `Main`.
   *
   * Ключевая тонкость: узел, который САМ правится (`JumpSpot3`, `Player`),
   * слоем не становится — иначе площадка и её коллайдер попали бы в разные
   * слои, и «скрыть слой» разрывало бы пару.
   */
  _layerOf(obj) {
    // Идём вверх по РОДИТЕЛЯМ, пропуская промежуточные группы без узла
    // (`content` параллакса). Первый узел, который сам НЕ является правимым
    // объектом, — и есть слой.
    let o = obj.parent;
    const editableSet = this._editableSet || (this._editableSet = new Set(
      this.editable.map((e) => e.obj)));
    while (o && o !== this.gs.root) {
      const nd = o.userData && o.userData.node;
      if (nd && !editableSet.has(o)) return nd.name || (nd.path || 'Main');
      o = o.parent;
    }
    return 'Main';
  }

  rebuildPickable() {
    this.pickable = [];
    for (const e of this.editable) {
      const lay = this.layers.get(this._layerOf(e.obj));
      if (lay && !lay.visible) continue;
      e.obj.traverse((o) => { if (o.isMesh || o.isSprite) this.pickable.push(o); });
    }
    this._pickRoot = new Map();
    for (const e of this.editable) {
      e.obj.traverse((o) => this._pickRoot.set(o, e.path));
    }
  }

  /* -------------------------------------------------------------- правки */

  async loadEdits() {
    const r = await fetch('/__edits?file=' + this.editFile + '&t=' + Date.now());
    const j = await r.json();
    this.edits = {};
    for (const [path, val] of Object.entries(j.nodes || {})) {
      const pos = Array.isArray(val) ? val : val.position;
      if (pos) this.edits[path] = [pos[0], pos[1]];
    }
    this.added = j.add || [];
    this.removed = j.remove || [];
    // Наложение на сцену: позиции.
    for (const [path, pos] of Object.entries(this.edits)) this._applyLocal(path, pos);
    for (const a of this.added) this._spawnLocal(a);
    for (const rm of this.removed) this.hideLocal(rm, true);
    if (this.cb.onChange) this.cb.onChange(this);
  }

  /** Собрать конверт правок. `add`/`remove` — расширение формата. */
  toOverlay() {
    return {
      level: this.levelFile,
      nodes: Object.fromEntries(Object.entries(this.edits).map(
        ([k, v]) => [k, [round(v[0]), round(v[1])]])),
      ...(this.added && this.added.length ? { add: this.added } : {}),
      ...(this.removed && this.removed.length ? { remove: this.removed } : {}),
    };
  }

  async saveEdits() {
    const r = await fetch('/__save?file=' + this.editFile, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(this.toOverlay()),
    });
    const j = await r.json();
    if (this.cb.onLog) {
      this.cb.onLog(`saved ${j.path} (${j.bytes} b)`);
      if (j.path !== this.editFile) {
        this.cb.onLog(`!! ${j.path} != ${this.editFile} — правки уехали не туда`);
      }
    }
    return j;
  }

  async rebuild() {
    const lvl = (this.def && this.def.id) || (this.levelFile === 'level.json' ? 'level_0' : 'level_1');
    const r = await fetch('/__build?level=' + encodeURIComponent(lvl), { method: 'POST' });
    const j = await r.json();
    if (this.cb.onLog) this.cb.onLog(`build ${lvl}: ${j.ok ? 'OK' : 'FAIL'} (${j.tool})`);
    if (!j.ok && this.cb.onLog) this.cb.onLog(j.out.trim().split('\n').slice(-14).join('\n'));
    return j;
  }

  /**
   * Наложить позицию на объект. `alsoPartner` — двигать ли площадку и её
   * коллайдер вместе.
   *
   * При ЗАГРУЗКЕ правок партнёр включается: в файле может лежать только один
   * путь из пары (так писал старый редактор), и без этого платформа осталась бы
   * на месте. При ДВИЖЕНИИ мышью партнёр выключен: setPos и так перебирает оба
   * и уже посчитал каждому своё приращение.
   */
  _applyLocal(path, pos, alsoPartner = true) {
    const e = this.editableByPath.get(path);
    if (!e) return;
    e.obj.position.x = pos[0];
    e.obj.position.y = -pos[1];
    if (alsoPartner && this.links.has(path)) {
      const p = this.editableByPath.get(this.links.get(path));
      if (p) { p.obj.position.x = pos[0]; p.obj.position.y = -pos[1]; }
    }
  }

  /**
   * Локальная копия добавляемого узла.
   *
   * Это ТОЛЬКО показ в текущей сессии: в `level.json` узел попадает не отсюда, а
   * через файл правок — секцию `add` разбирает `tools/level_edits.py` при
   * пересборке. Копия нужна, чтобы человек увидел, что добавил, не дожидаясь
   * сборки; расхождение с ней не страшно, потому что источник правды — файл.
   */
  _spawnLocal(spec) {
    // Позиция приходит либо в новом `props` (вместе с остальными свойствами
    // узла), либо в старом плоском `position`. Второй вид надо принимать: файлы
    // правок, сохранённые до появления `props`, обязаны открываться.
    const props = spec.props || {};
    const pos = props.position || spec.position;
    const scale = props.scale || spec.scale;
    if (!pos) return null;
    const clone = this._templateFor(spec.type, spec.texture || props.texture);
    if (!clone) return null;
    clone.name = spec.path;
    if (scale) clone.scale.set(scale[0], scale[1], 1);
    clone.position.set(pos[0], -pos[1], this._depthFor(spec));
    this.gs.root.add(clone);
    const e = { path: spec.path, obj: clone, added: true, parent: spec.parent || null,
      node: { path: spec.path, type: spec.type,
              props: spec.props || { position: spec.position } } };
    this.editable.push(e);
    this.editableByPath.set(spec.path, e);
    this.orig[spec.path] = spec.position.slice();
    this.objByPath.set(spec.path, clone);
    this.rebuildPickable();
    return e;
  }

  _templateFor(type, texKey) {
    // Шаблон ищем по уже существующему узлу ТОГО ЖЕ типа: его материал, его
    // текстура, его размер. Собрать узел «с нуля» нельзя — у него нет
    // текстуры, а текстура без имени файла это узел, который в игре будет
    // невидим (или хуже: 404 в консоли, а его читают гейты).
    const src = this.editable.find((e) => (e.node.type || '') === type
      && (!texKey || (e.node.props || {}).texture === texKey))
      || this.editable.find((e) => (e.node.type || '') === type);
    if (!src) return null;
    const clone = src.obj.clone(true);
    // clone(true) тащит детей — их оставляем: у площадки это может быть
    // коллайдер-подсветка, и без него узел «без тела».
    return clone;
  }

  _depthFor(spec) {
    // Глубина = renderOrder родителя; новый узел кладём туда же, где его
    // шаблон. Придумывать число нельзя: сдвинешь поддерево — узел всплывёт
    // поверх того, что должен перекрывать.
    const e = this.editable.find((x) => (x.node.type || '') === spec.type);
    return e ? e.obj.position.z : -100;
  }

  /** Локально спрятать/показать удалённый узел. */
  hideLocal(path, hidden) {
    const e = this.editableByPath.get(path);
    if (e) e.obj.visible = !hidden;
    return !!e;
  }

  /* --------------------------------------------------------------- выбор */

  select(path, opts = {}) {
    if (this.sel && this.objByPath.get(this.sel)) this._setHl(this.sel, false);
    this.sel = path || null;
    if (this.sel) this._setHl(this.sel, true);
    if (this.cb.onSelect) this.cb.onSelect(this.sel, this.infoOf(this.sel), opts);
    return this.sel;
  }

  _setHl(path, on) {
    const obj = this.objByPath.get(path);
    if (!obj) return;
    obj.traverse((o) => {
      if (!o.isMesh && !o.isSprite) return;
      if (!o.userData._hlOrig) o.userData._hlOrig = [];
      if (on) {
        const mats = Array.isArray(o.material) ? o.material : [o.material];
        const copy = mats.map((m) => {
          const c = m.clone();
          c.color = new THREE.Color(0xffd45a);
          return c;
        });
        o.userData._hlOrig.push(o.material);
        o.material = Array.isArray(o.material) ? copy : copy[0];
      } else if (o.userData._hlOrig.length) {
        o.material = o.userData._hlOrig.pop();
      }
    });
  }

  infoOf(path) {
    if (!path) return null;
    const e = this.editableByPath.get(path);
    if (!e) return null;
    const pos = this.edits[path] || this.orig[path] || this.levelPos(path);
    const sc = e.obj.scale;
    const isLayerLike = NO_EDIT.test(e.path) || (e.obj.userData.node || {}).type === 'Parallax2D';
    return {
      path, type: e.node.type, pos: [round(pos[0]), round(pos[1])],
      scale: [round(sc.x, 3), round(sc.y, 3)],
      depth: this._renderOrder(e.obj),
      rawDepth: e.obj.position.z,
      zIndex: (e.node.props || {}).z_index ?? 0,
      layer: this._layerOf(e.obj),
      locked: isLayerLike,
      edited: !!this.edits[path],
      added: !!e.added,
      links: this.links.has(path) ? this.links.get(path) : null,
      dirty: this.dirty,
    };
  }

  _renderOrder(o) { return o.renderOrder; }

  /* -------------------------------------------------------- перемещение */

  levelPos(path) {
    const e = this.editableByPath.get(path);
    if (!e) return null;
    return [e.obj.position.x, -e.obj.position.y];
  }

  setPos(path, x, y, record = true) {
    const e = this.editableByPath.get(path);
    if (!e) return;
    const lay = this.layers.get(this._layerOf(e.obj));
    if (lay && lay.locked) return;
    if (NO_EDIT.test(path)) return;

    // ПАРА. Площадка и её коллайдер двигаются вместе — это и есть «ходьба
    // соблюдается»: площадка, уехавшая без коллайдера, на вид та же, а встать
    // на неё нельзя.
    //
    // Двигаем ПРИРАЩЕНИЕМ, а не «поставить обеим ту же координату». Это
    // принципиально: у площадки `JumpSpot3` и её коллайдера `JumpSpotPlatform3`
    // координаты в уровне РАЗНЫЕ (спрайт и коробка стоят по-разному), и общая
    // координата раздавила бы эту разницу. Приращение её сохраняет — и
    // одновременно гарантирует, что относительное смещение не поплывёт.
    const from = this.levelPos(path);
    const dx = x - from[0], dy = y - from[1];
    if (dx === 0 && dy === 0) return;

    const partner = this.links.get(path);
    const targets = partner ? [path, partner] : [path];

    if (record) this.history.push(this._snap(targets));
    for (const t of targets) {
      const t0 = this.editableByPath.get(t);
      if (!t0) continue;
      const p0 = this.levelPos(t);
      const np = [round(p0[0] + dx), round(p0[1] + dy)];
      this.edits[t] = np;
      this._applyLocal(t, np, false);
    }
    this.dirty = true;
    if (this.cb.onChange) this.cb.onChange(this);
    if (this.cb.onSelect && this.sel && targets.includes(this.sel)) {
      this.cb.onSelect(this.sel, this.infoOf(this.sel));
    }
  }

  moveBy(path, dx, dy) {
    const p = this.levelPos(path);
    if (!p) return;
    this.setPos(path, round(p[0] + dx), round(p[1] + dy));
  }

  moveTo(path, x, y) { this.setPos(path, round(x), round(y)); }

  /**
   * Отмена одного ШАГА. Шаг — это одно движение мышью, а оно пишет два пути
   * (площадку и её пару). Поэтому история хранит НЕ позиции, а кадры состояния:
   * каждый push — снимок всех правок «до» этого шага, вместе с их путями.
   * Так отмена восстанавливает согласованный набор, и площадка с платформой не
   * могут разъехаться на полшага.
   */
  undo() {
    const snap = this.history.pop();
    if (!snap) return false;
    // `alsoPartner=false` — ОБЯЗАТЕЛЬНО. В снимке лежат оба пути пары, и
    // каждый восстанавливается в СВОЮ позицию. Если бы каждый тянул за собой
    // партнёра, последний в обходе затёр бы первого, и undo «вернул» бы оба
    // узла в одну точку — то есть сломал бы ровно то, что чинит.
    for (const [path, pos] of Object.entries(snap)) {
      if (pos === null) delete this.edits[path];
      else this.edits[path] = pos;
      this._applyLocal(path, pos || this.orig[path] || [0, 0], false);
    }
    this.dirty = this.history.length > 0;
    if (this.cb.onChange) this.cb.onChange(this);
    if (this.cb.onSelect && this.sel) this.cb.onSelect(this.sel, this.infoOf(this.sel));
    return true;
  }

  /** Снимок правок по списку путей — «до» для следующего шага. */
  _snap(paths) {
    const out = {};
    for (const p of paths) out[p] = this.edits[p] ? this.edits[p].slice() : null;
    return out;
  }

  revertAll() {
    for (const [path, pos] of Object.entries(this.orig)) {
      if (this.edits[path]) this._applyLocal(path, pos);
    }
    this.edits = {};
    this.added = [];
    for (const rm of this.removed || []) this.hideLocal(rm, false);
    this.removed = [];
    this.history.length = 0;
    this.dirty = false;
    this.rebuildPickable();
    if (this.cb.onChange) this.cb.onChange(this);
  }

  /* ------------------------------------------------------------- слои */

  setLayerVisible(name, on) {
    const l = this.layers.get(name);
    if (!l) return;
    l.visible = on;
    for (const e of this.editable) {
      if (this._layerOf(e.obj) === name) e.obj.visible = on;
    }
    this.rebuildPickable();
    if (this.cb.onLayers) this.cb.onLayers(this.layerList());
  }

  setLayerLocked(name, on) {
    const l = this.layers.get(name);
    if (!l) return;
    l.locked = on;
    if (this.cb.onLayers) this.cb.onLayers(this.layerList());
  }

  layerList() {
    return this.layerOrder.map((n) => ({
      name: n, ...this.layers.get(n),
      active: n === this.activeLayer,
    }));
  }

  /** Видимость поддерева параллакса (для 2D-фона). */
  setParallaxVisible(on) {
    this.showParallax = on;
    this.gs.root.traverse((o) => {
      const nd = o.userData.node;
      if (nd && nd.type === 'Parallax2D') o.visible = on;
    });
  }

  setCollisions(on) {
    this.showCollisions = on;
    this.gs.setCollisions(on);
  }

  /* --------------------------------------------------------- камера/вид */

  applyView() {
    if (this.mode === '2d') {
      this.gs.setMode('ortho');
      // ВАЖНО: позицию ортокамеры задаёт САМ scene.js в update() — из
      // camX/camY, которые считаются из focusX и клампятся лимитами. Значит
      // писать `camera.position` отсюда бессмысленно: следующий кадр это
      // затрёт. Управляем через те входы, которые scene.js читает: focusX и
      // rawX (rawX — «уже сглаженное» значение, его выставляем, чтобы панорама
      // не плыла за курсором).
      this.gs.rawX = this.pan.x;
      this.gs.focusX = this.pan.x;
      this.gs.playerStart = [this.pan.x, this.pan.y];
      this.gs.update(0.0001);
    } else {
      this.gs.setMode('persp');
    }
    this._applyOrthoZoom();
    if (this.cb.onView) this.cb.onView(this);
  }

  _applyOrthoZoom() {
    const cam = this.gs.orthoCam;
    const w = this.canvas.clientWidth || 1, h = this.canvas.clientHeight || 1;
    const vw = w / this.zoom, vh = h / this.zoom;
    cam.left = -vw / 2; cam.right = vw / 2;
    cam.top = vh / 2; cam.bottom = -vh / 2;
    cam.updateProjectionMatrix();
    // viewW/viewH тоже правим: из них scene.js считает параллакс и кламп
    // камеры. Не синхронизировать — значит получить кадр, где фон уехал, а
    // земля нет (или наоборот), и «редактор врёт» на пустом месте.
    this.gs.viewW = vw;
    this.gs.viewH = vh;
  }

  setMode(m) {
    this.mode = m === '3d' ? '3d' : '2d';
    this.applyView();
  }

  /** Экран -> уровень (плоскость z выбранного объекта). */
  worldAt(ev, zLevel = 0) {
    const r = this.canvas.getBoundingClientRect();
    const sx = ev.clientX - r.left, sy = ev.clientY - r.top;
    const w = r.width || 1, h = r.height || 1;
    if (this.mode === '2d') {
      const vw = w / this.zoom, vh = h / this.zoom;
      const x = this.pan.x + (sx / w - 0.5) * vw;
      const y = this.pan.y + (sy / h - 0.5) * vh;
      return { x: round(x), y: round(y) };
    }
    // 3D: луч в орбитальную камеру, пересечение с плоскостью z = zLevel.
    if (!this.gs || !this.gs.camera) return null;
    const ray = new THREE.Raycaster();
    const ndc = new THREE.Vector2((sx / w) * 2 - 1, -(sy / h) * 2 + 1);
    ray.setFromCamera(ndc, this.gs.camera);
    const plane = new THREE.Plane(new THREE.Vector3(0, 0, 1), -zLevel);
    const hit = new THREE.Vector3();
    if (!ray.ray.intersectPlane(plane, hit)) return null;
    return { x: round(hit.x), y: round(-hit.y) };
  }

  pickAt(ev) {
    // Указатель приходит с момента конструктора (_bindPointer), а сцена
    // появляется только после await fetch в load(). До этого - не падаем.
    if (!this.gs || !this.gs.camera) return null;
    const r = this.canvas.getBoundingClientRect();
    const ndc = new THREE.Vector2(
      ((ev.clientX - r.left) / r.width) * 2 - 1,
      -((ev.clientY - r.top) / r.height) * 2 + 1);
    const ray = new THREE.Raycaster();
    ray.setFromCamera(ndc, this.gs.camera);
    const hits = ray.intersectObjects(this.pickable, true);
    for (const h of hits) {
      const p = this._pickRoot.get(h.object);
      if (p) {
        const lay = this.layers.get(this._layerOf(this.objByPath.get(p) || h.object));
        if (lay && !lay.visible) continue;
        return p;
      }
    }
    return null;
  }

  /* --------------------------------------------------------------- ввод */

  _bindPointer() {
    let drag = null, moved = false;
    const down = (ev) => {
      if (ev.button !== 0) return;
      if (this.mode === '3d') return;   // в 3D мышь принадлежит орбите
      const path = this.pickAt(ev);
      if (!path) { this.select(null); return; }
      this.select(path);
      const e = this.editableByPath.get(path);
      const start = this.worldAt(ev, e ? e.obj.position.z : 0);
      drag = { path, start, orig: this.levelPos(path) };
      moved = false;
      this.canvas.style.cursor = 'grabbing';
    };
    const move = (ev) => {
      if (!drag) {
        const p = this.pickAt(ev);
        this.canvas.style.cursor = p ? 'grab' : 'default';
        return;
      }
      // Кнопка уже отпущена, а `pointerup` мы не увидели — сбрасываем захват.
      //
      // `pointerup` висит на window, и это правильно (drag должен переживать
      // выход курсора за холст), но событие приходит не всегда: отпускание за
      // пределами окна, alt-tab, переключение приложения, синтетическое событие
      // из автоматизации. Тогда `drag` остаётся живым навсегда, и КАЖДОЕ
      // следующее движение мыши тянет выбранный узел — без нажатой кнопки.
      // Уровень при этом «сам» разъезжается, а правки уходят в
      // `<level>_edit.json` при первом же «Сохранить». `buttons === 0` — это
      // ровно «ни одна кнопка не нажата», так что живое перетаскивание
      // (buttons === 1) не задевается.
      if (ev.buttons === 0) {
        drag = null;
        this.canvas.style.cursor = 'default';
        return;
      }
      const cur = this.worldAt(ev, this.editableByPath.get(drag.path).obj.position.z);
      if (!cur) return;
      const dx = cur.x - drag.start.x, dy = cur.y - drag.start.y;
      if (!moved && Math.abs(dx) + Math.abs(dy) < 1) return;
      if (!moved) {
        // Снимок «до» берём ОДИН раз — на первом реальном сдвиге. Дальше шаги
        // тянутся без записи в историю, и весь перетаскивания — это один шаг
        // отмены, а не сотня.
        const e0 = this.editableByPath.get(drag.path);
        const partner = this.links.get(drag.path);
        this.history.push(this._snap(partner ? [drag.path, partner] : [drag.path]));
        moved = true;
      }
      this.setPos(drag.path, round(drag.orig[0] + dx), round(drag.orig[1] + dy), false);
    };
    const up = () => { drag = null; this.canvas.style.cursor = 'default'; };
    this.canvas.addEventListener('pointerdown', down);
    addEventListener('pointermove', move);
    addEventListener('pointerup', up);
    // `pointercancel` браузер шлёт, когда жест забрал кто-то другой (тач-скролл,
    // системный жест, потеря фокуса). Без него захват тоже оставался живым.
    addEventListener('pointercancel', up);
    addEventListener('blur', up);
    // Колесо — зум к курсору в 2D; в 3D им владеет OrbitControls.
    // Ctrl+колесо НЕ перехватываем: это браузерный зум, и он нужен как
    // штатный способ увеличить весь интерфейс (мелкий текст на большом
    // мониторе). Раньше preventDefault стоял безусловно, и Ctrl+колесо над
    // кадром молча уходило в зум уровня — со стороны выглядело как «зум
    // сломан». Для зума кадра есть колесо без Ctrl и кнопки ＋ / －.
    this.canvas.addEventListener('wheel', (ev) => {
      if (this.mode !== '2d' || ev.ctrlKey) return;
      ev.preventDefault();
      const before = this.worldAt(ev);
      this.zoom = Math.max(0.05, Math.min(4, this.zoom * (ev.deltaY < 0 ? 1.12 : 1 / 1.12)));
      this._applyOrthoZoom();
      const after = this.worldAt(ev);
      this.pan.x += before.x - after.x;
      this.pan.y += before.y - after.y;
      this.applyView();
    }, { passive: false });
    // Средняя кнопка / пробел+мышь — панорама.
    this.canvas.addEventListener('pointerdown', (ev) => {
      if (ev.button !== 1) return;
      ev.preventDefault();
      const p0 = { x: ev.clientX, y: ev.clientY, px: this.pan.x, py: this.pan.y };
      const mv = (e2) => {
        this.pan.x = p0.px - (e2.clientX - p0.x) / this.zoom;
        this.pan.y = p0.py - (e2.clientY - p0.y) / this.zoom;
        this.applyView();
      };
      const stop = () => {
        removeEventListener('pointermove', mv);
        removeEventListener('pointerup', stop);
      };
      addEventListener('pointermove', mv);
      addEventListener('pointerup', stop);
    });

    // --- 3D: орбита вокруг точки уровня. Своя, а не OrbitControls: камера здесь
    // живёт в scene.js, и подсунуть ей второй контроллер значит получить двух
    // хозяев у одной матрицы. Поэтому вращаем свои yaw/pitch/dist, а позицию
    // камеры собирает start() по тем же числам.
    let orb = null;
    const odown = (ev) => {
      if (this.mode !== '3d' || ev.button !== 0) return;
      orb = { x: ev.clientX, y: ev.clientY, yaw: this.orbit.yaw, pitch: this.orbit.pitch };
      this.canvas.style.cursor = 'grabbing';
    };
    const omove = (ev) => {
      if (!orb) return;
      this.orbit.yaw = orb.yaw + (ev.clientX - orb.x) * 0.006;
      this.orbit.pitch = Math.max(-1.35, Math.min(1.35,
        orb.pitch - (ev.clientY - orb.y) * 0.006));
    };
    const oup = () => { orb = null; this.canvas.style.cursor = 'default'; };
    this.canvas.addEventListener('pointerdown', odown);
    addEventListener('pointermove', omove);
    addEventListener('pointerup', oup);
    // Зум в 3D — дистанция орбиты. Знак тот же, что у зума в 2D: «от себя =
    // приблизить» — иначе две панели одного редактора ведут себя по-разному.
    // Ctrl+колесо, как и в 2D, отдаём браузеру (браузерный зум).
    this.canvas.addEventListener('wheel', (ev) => {
      if (this.mode !== '3d' || ev.ctrlKey) return;
      ev.preventDefault();
      this.orbit.dist = Math.max(120, Math.min(14000,
        this.orbit.dist * (ev.deltaY < 0 ? 1 / 1.12 : 1.12)));
    }, { passive: false });
  }

  _bindKeys() {
    this._keys = (ev) => {
      if (ev.target && /INPUT|TEXTAREA/.test(ev.target.tagName)) return;
      const step = ev.shiftKey ? 10 : 1;
      if (ev.code === 'KeyZ' && (ev.ctrlKey || ev.metaKey)) { ev.preventDefault(); this.undo(); return; }
      if (!this.sel) return;
      const d = { ArrowLeft: [-1, 0], ArrowRight: [1, 0], ArrowUp: [0, -1], ArrowDown: [0, 1] }[ev.code];
      if (!d) return;
      ev.preventDefault();
      this.moveBy(this.sel, d[0] * step, d[1] * step);
    };
    addEventListener('keydown', this._keys);
  }

  /* --------------------------------------------------------------- рендер */

  start() {
    // Точка обзора орбиты — середина уровня по габаритам: она одна для всего
    // уровня и не зависит от того, куда человек утащил панораму в 2D. Иначе
    // переключение 2D->3D давало бы вид «в никуда» из свежесдвинутого места.
    const b = new THREE.Box3().setFromObject(this.gs.root);
    if (!b.isEmpty()) {
      const c = b.getCenter(new THREE.Vector3());
      this.orbit.target.set(c.x, c.y, -50);
    }
    const tick = () => {
      if (this.mode === '3d') {
        const c = this.gs.camera;
        const t = this.orbit.target;
        const p = this.orbit;
        c.position.set(
          t.x + p.dist * Math.cos(p.pitch) * Math.sin(p.yaw),
          t.y + p.dist * Math.sin(p.pitch),
          t.z + p.dist * Math.cos(p.pitch) * Math.cos(p.yaw));
        c.lookAt(t);
      }
      this.gs.update(0.016);
      this.renderer.render(this.gs.scene, this.gs.camera);
      this._raf = requestAnimationFrame(tick);
    };
    this._raf = requestAnimationFrame(tick);
  }

  resize() {
    const w = this.host.clientWidth || 1, h = this.host.clientHeight || 1;
    if (w < 2 || h < 2) return;
    // Третий аргумент — `true`, то есть «обнови и CSS-размер холста». С `false`
    // three менял только буфер отрисовки (w*dpr), а стиль оставлял прежним, и
    // холст рисовался в своих ВНУТРЕННИХ пикселях. На экране с dpr=1 это
    // незаметно, но на HiDPI (dpr 1.25/1.5/2) холст становился в dpr раз
    // больше контейнера: сцену обрезало, а картинка выглядела «приближенной»
    // без причины. Здесь размеры хоста и буфера совпадают, так что `true`
    // ничего не меняет на dpr=1 и лечит HiDPI.
    this.renderer.setSize(w, h, true);
    // LevelScene.resize пересчитывает свою проекцию «как в игре» (fit 1280x720),
    // то есть ЗАТИРАЕТ наш зум. Поэтому зум применяем ПОСЛЕ него, а не до:
    // иначе после каждого изменения размеров панели кадр возвращался бы к
    // игровому масштабу, и панорама «терялась» без причины.
    this.gs.resize(w, h);
    this._applyOrthoZoom();
    this.gs.update(0.0001);
  }

  dispose() {
    if (this._raf) cancelAnimationFrame(this._raf);
    removeEventListener('keydown', this._keys);
    this.renderer.dispose();
    this.canvas.remove();
  }
}

function round(v, n = 1) {
  const k = 10 ** n;
  return Math.round(v * k) / k;
}
