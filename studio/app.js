/*
 * app.js — обвязка студии: панели, вкладки, инспектор.
 *
 * Разделение простое и намеренное:
 *   * `leveledit.js` знает про уровень (узлы, правки, слои);
 *   * `glbview.js` знает про GLB (камера, свет, оверлеи);
 *   * ЭТОТ файл знает про людей: где какая кнопка, как показать ошибку, как
 *     не дать потерять работу.
 *
 * ── Про агента ──────────────────────────────────────────────────────────────
 * Агента в студии НЕТ. Модель работает только через консольный `pi`
 * (`agent.cmd` из корня репозитория), а студия — инструмент живого просмотра и
 * ручной правки: её можно открыть в любой момент, независимо от агента, и
 * увидеть, что он изменил (уровень перечитывается кнопкой/перезагрузкой).
 * Поэтому здесь нет ни чата, ни ручки `/__ask`: браузер не может порождать
 * процессы, и держать полусервер-полуагент в странице незачем.
 */
import { LevelEditor, THREE } from './leveledit.js';
import { GlbViewer, sizeLine } from './glbview.js';

const $ = (id) => document.getElementById(id);
const el = (tag, cls, txt) => {
  const e = document.createElement(tag);
  if (cls) e.className = cls;
  if (txt !== undefined) e.textContent = txt;
  return e;
};

/* ============================================================ состояние */

const S = {
  manifest: null,
  levels: [],
  level: null,
  ed: null,
  viewer: null,
  assets: { images: [], glbs: [] },
  tab: 'level',
  dirty: false,
};

function log(msg, kind = 'info') {
  const box = $('log');
  const line = el('div', 'logline ' + kind);
  line.textContent = msg;
  box.appendChild(line);
  box.scrollTop = box.scrollHeight;
  while (box.children.length > 400) box.removeChild(box.firstChild);
}

/* ============================================================ уровень */

async function loadManifest() {
  // Манифест лежит РЯДОМ со студией, а не двумя уровнями выше: браузер считает
  // относительный путь от URL СТРАНИЦЫ (`/web3d/studio.html`), а не от URL
  // модуля. Здесь легко ошибиться, а симптом обманчив — 404 рядом с рабочим
  // редактором читается как «манифест сломан», хотя достаточно было одного `..`.
  S.manifest = await (await fetch('./levels.json', { cache: 'no-cache' })).json();
  S.levels = Object.entries(S.manifest.levels).map(([id, d]) => ({ id, ...d }));
  const sel = $('levelSel');
  sel.innerHTML = '';
  for (const l of S.levels) {
    const o = el('option', null, `${l.title || l.id}  —  ${l.file}`);
    o.value = l.id;
    // «Нередактируемый» уровень не прячем из списка, а помечаем: он открывается
    // на просмотр, и это нужный сценарий («посмотреть, как собрано»). Прятать —
    // значит заставлять человека гадать, почему уровня нет.
    if (!l.editable) o.textContent += '  (только просмотр)';
    sel.appendChild(o);
  }
  // Стартуем с САМОГО БОГАТОГО уровня из редактируемых, а не с первого по
  // списку. Манифест начинается с `start` (level_0), но level_0 исторически
  // беден адресуемыми узлами — открыть его первым значит показать пустой
  // список и пустой кадр, то есть «редактор не работает».
  const editable = S.levels.filter((l) => l.editable);
  sel.value = (editable[editable.length - 1] || S.levels[0]).id;
}

/* ------------------------------------------------- проверка формата уровня */
/* Зачем отдельная кнопка. Агент регулярно отчитывается «уровень создан», и это
   ПРАВДА: файл написан, схема верна. Но если он сослался на текстуры и кадры
   анимации, которых на диске нет, — в сцене не нарисуется НИЧЕГО, а консоль
   получит 404. Разница между «создан» и «работает» видна только прогоном, и
   вердикт обязан быть в студии, а не только в логе агента. */
async function lintLevel() {
  const btn = $('lintBtn');
  if (!btn || !S.level) return null;
  btn.className = 'lint';
  btn.textContent = 'формат: проверяю…';
  try {
    const r = await fetch('/__lint?level=' + encodeURIComponent(S.level.id));
    const j = await r.json();
    const lines = (j.out || '').split('\n').filter((l) => l.trim());
    const errs = lines.filter((l) => l.includes('ОШИБКА'));
    btn.className = 'lint ' + (j.ok ? 'ok' : 'bad');
    btn.textContent = j.ok ? 'формат: в порядке' : `формат: ${errs.length} ошибок`;
    btn.title = j.ok
      ? 'Формат уровня в порядке — файлы на месте'
      : 'Уровень не заработает: нажмите, чтобы увидеть ошибки в журнале';
    if (!j.ok) {
      log(`линтер: ${j.file || S.level.file} — ошибок ${errs.length}`, 'err');
      for (const l of errs.slice(0, 40)) log('  ' + l.trim(), 'err');
      if (errs.length > 40) log(`  … и ещё ${errs.length - 40}`, 'err');
    }
    return j;
  } catch (e) {
    btn.className = 'lint';
    btn.textContent = 'формат: не проверить';
    btn.title = e.message;
    log('линтер недоступен: ' + e.message, 'warn');
    return null;
  }
}

async function openLevel(id) {
  const def = S.levels.find((l) => l.id === id);
  if (!def) return;
  if (S.ed && S.dirty && !confirm('Есть несохранённые правки. Открыть другой уровень и потерять их?')) return;
  S.level = def;
  if (S.ed) S.ed.dispose();
  const host = $('cvLevel');
  host.innerHTML = '';
  S.ed = new LevelEditor(host, {
    onReady: () => { log(`уровень ${def.id} открыт (${S.ed.editable.length} правимых узлов)`); },
    onChange: () => { S.dirty = true; $('saveBtn').classList.add('hot'); renderTree(); },
    onSelect: (path, info) => renderInspector(info),
    onLayers: (list) => renderLayers(list),
    onView: () => renderView(),
    onLog: (m) => log(m),
  });
  await S.ed.load(def.file, def);
  S.ed.dirty = false;
  S.dirty = false;
  $('saveBtn').classList.remove('hot');
  $('editableWarn').style.display = def.editable ? 'none' : '';
  $('saveBtn').disabled = !def.editable;
  $('levelFileMini').textContent = def.file;
  renderTree();
  renderLayers(S.ed.layerList());
  renderInspector(null);
  renderView();
  S.ed.start();
  // Вердикт линтера — сразу при открытии, а не по кнопке: иначе человек
  // видит пустой кадр и не знает, что причина в отсутствующих ассетах.
  lintLevel();
}

/* ------------------------------------------------------------- дерево */

function renderTree() {
  const box = $('tree');
  box.innerHTML = '';
  if (!S.ed) return;
  const q = ($('treeFilter').value || '').toLowerCase();
  const root = el('div', 'tnode');
  root.appendChild(el('div', 'tname root', `Main — ${S.level.file}`));
  const groups = new Map();
  for (const e of S.ed.editable) {
    const lay = S.ed._layerOf(e.obj);
    if (!groups.has(lay)) groups.set(lay, []);
    groups.get(lay).push(e);
  }
  for (const lay of S.ed.layerOrder) {
    const items = groups.get(lay) || [];
    const g = el('div', 'tgroup');
    const h = el('div', 'tname grp', `${lay}  (${items.length})`);
    g.appendChild(h);
    let n = 0;
    for (const e of items) {
      if (q && !e.path.toLowerCase().includes(q)) continue;
      n++;
      const row = el('div', 'n' + (S.ed.sel === e.path ? ' sel' : '') +
        (e.added ? ' added' : '') + (S.ed.edits[e.path] ? ' edited' : ''));
      row.textContent = e.path;
      row.dataset.path = e.path;
      row.onclick = () => {
        S.ed.select(e.path);
        focusPath(e.path);
      };
      row.ondblclick = () => zoomToPath(e.path);
      g.appendChild(row);
    }
    if (n === 0 && q) return;
    root.appendChild(g);
  }
  box.appendChild(root);
}

function focusPath(path) {
  const obj = S.ed.objByPath.get(path);
  if (!obj) return;
  // Панораму ставим так, чтобы узел оказался в центре: без этого выбор в списке
  // меняет выделение, но человек не понимает, что выделилось — узел за кадром.
  const p = S.ed.levelPos(path);
  if (!p) return;
  S.ed.pan.x = p[0];
  S.ed.pan.y = p[1];
  S.ed.applyView();
}

function zoomToPath(path) {
  const e = S.ed.editableByPath.get(path);
  if (!e) return;
  const sc = Math.abs(e.obj.scale.x) || 1;
  S.ed.zoom = Math.max(0.1, Math.min(4, 1.2 / Math.max(0.2, sc)));
  focusPath(path);
  S.ed._applyOrthoZoom();
}

/* ----------------------------------------------------------- инспектор */

function renderInspector(info) {
  const box = $('insp');
  box.innerHTML = '';
  if (!S.ed) return;
  if (!info) {
    box.appendChild(el('div', 'dim', 'Ничего не выбрано. Клик по объекту в кадре или строке списка.'));
    return;
  }
  const row = (k, v, cls) => {
    const r = el('div', 'irow ' + (cls || ''));
    r.appendChild(el('span', 'ik', k));
    r.appendChild(el('span', 'iv', v));
    box.appendChild(r);
    return r;
  };
  row('путь', info.path, 'mono');
  row('тип', info.type || '—');
  row('слой', info.layer);

  // Позиция — ЕДИНСТВЕННОЕ правимое поле. Редактируем через те же setPos, что и
  // мышью: иначе клавиатура и мышь пишут в правки разными путями, и undo
  // начинает «прыгать» на один шаг.
  const pr = el('div', 'irow');
  pr.appendChild(el('span', 'ik', 'позиция X Y'));
  const wrap = el('span', 'iv');
  const ix = el('input', 'num'); ix.type = 'number'; ix.step = '0.5'; ix.value = info.pos[0];
  const iy = el('input', 'num'); iy.type = 'number'; iy.step = '0.5'; iy.value = info.pos[1];
  const commit = () => S.ed.moveTo(info.path, parseFloat(ix.value) || 0, parseFloat(iy.value) || 0);
  ix.onchange = commit; iy.onchange = commit;
  wrap.appendChild(ix); wrap.appendChild(iy);
  pr.appendChild(wrap);
  box.appendChild(pr);

  row('масштаб', `${info.scale[0]} × ${info.scale[1]}  (только чтение)`);
  row('глубина', `${info.depth}  (renderOrder`, 'dim');
  row('z_index', String(info.zIndex));
  if (info.links) row('пара', info.links, 'link');
  if (info.locked) box.appendChild(el('div', 'warn', 'Слой служебный: его позиция вычисляется, а не задаётся.'));
  if (info.added) box.appendChild(el('div', 'warn',
    'Узел добавлен в студии. Сборщик пока читает из файла правок только позиции — ' +
    'см. лог: добавление в level1.json ещё не поддержано.'));

  const acts = el('div', 'iacts');
  const b1 = el('button', null, 'Вернуть этот узел');
  b1.onclick = () => {
    if (S.ed.orig[info.path]) S.ed.setPos(info.path, S.ed.orig[info.path][0], S.ed.orig[info.path][1]);
  };
  const b2 = el('button', 'danger', 'Удалить узел');
  b2.onclick = () => removeNode(info.path);
  acts.appendChild(b1); acts.appendChild(b2);
  box.appendChild(acts);
}

/* ------------------------------------------------------------- слои */

function renderLayers(list) {
  const box = $('layers');
  box.innerHTML = '';
  for (const l of list) {
    const r = el('div', 'lrow');
    const eye = el('button', 'icn' + (l.visible ? ' on' : ''), l.visible ? '◉' : '◌');
    eye.title = 'Видимость слоя';
    eye.onclick = () => S.ed.setLayerVisible(l.name, !l.visible);
    const lock = el('button', 'icn' + (l.locked ? ' on' : ''), l.locked ? '🔒' : '🔓');
    lock.title = 'Заморозить слой (запрет правки)';
    lock.onclick = () => S.ed.setLayerLocked(l.name, !l.locked);
    const name = el('span', 'lname', l.name);
    const cnt = el('span', 'lcnt', String(l.count));
    r.appendChild(eye); r.appendChild(lock); r.appendChild(name); r.appendChild(cnt);
    // Параллакс-слоям добавляем свой тумблер: их позиция вычисляется, и
    // «показать/скрыть, чтобы посмотреть, что под ними» — единственная
    // осмысленная операция.
    const isPar = /Backdrop|Parallax|Far|Mid/.test(l.name);
    if (isPar) {
      const tag = el('span', 'ltag', 'par');
      tag.title = 'Слой параллакса: позиция вычисляется из камеры';
      r.appendChild(tag);
    }
    box.appendChild(r);
  }
}

function renderView() {
  if (!S.ed) return;
  $('viewInfo').textContent =
    `${S.ed.mode.toUpperCase()} · zoom ${S.ed.zoom.toFixed(2)} · ` +
    `pan ${Math.round(S.ed.pan.x)}, ${Math.round(S.ed.pan.y)}`;
}

/* ====================================================== добавление узла */

/**
 * Добавление узла. Конверт: `add: [{path, type, parent, props, from}]`.
 *
 * `props` копируется у узла-образца ЦЕЛИКОМ, а не собирается из position/scale.
 * Так переносится любой тип: у `ColorRect` остаются `rect` и `color` (без них
 * узел невидим), у `Sprite2D` — `texture`. Собрать props «по типу» значило бы
 * вести здесь вторую таблицу того, что нужно каждому типу, и она разошлась бы
 * со `scene.js`.
 *
 * `parent` — путь узла-слоя, куда вставлять. Без него `tools/level_edits.py`
 * откажется: положить узел в корень «на глазок» значит изменить порядок
 * отрисовки всего уровня.
 */
function addNode(type, srcPath) {
  if (!S.ed) return;
  const src = S.ed.editableByPath.get(srcPath);
  if (!src) return;
  const n = Math.floor(Math.random() * 9000 + 1000);
  const base = srcPath.replace(/\d+$/, '');
  const path = `${base}${n}`;
  // Позицию ставим ПО ЦЕНТРУ ВИДА: добавлять «где-то там» — значит гарантировать
  // «не вижу, что добавилось».
  const position = [Math.round(S.ed.pan.x), Math.round(S.ed.pan.y)];
  const spec = {
    path, type: src.node.type,
    parent: src.parent || null,
    from: srcPath,
    props: { ...(src.node.props || {}), position },
  };
  const e = S.ed._spawnLocal(spec);
  if (!e) { log(`не нашёл шаблон типа ${src.node.type}`, 'err'); return; }
  // Копия шаблона нуждается в уникальном path внутри дерева THREE: иначе
  // _groupOf в движке вернёт первый попавшийся узел, и «добавили» превратится
  // в «сдвинули существующий».
  e.obj.name = path;
  S.ed.added.push(spec);
  S.dirty = true;
  log(`+ ${path} (из ${srcPath}, тип ${src.node.type})`
      + (spec.parent ? ` в слой ${spec.parent}` : ' — родитель не определён, сборка откажет'), 
      spec.parent ? 'info' : 'warn');
  renderTree();
  S.ed.select(path);
}

function removeNode(path) {
  if (!S.ed) return;
  const e = S.ed.editableByPath.get(path);
  if (!e) return;
  if (!confirm(`Удалить «${path}»? Из файла правок узел уйдёт сразу, из уровня — после «Пересобрать».`)) return;
  e.obj.visible = false;
  if (!S.ed.removed.includes(path)) S.ed.removed.push(path);
  // Если это был добавленный здесь узел — достаточно убрать его из `add`,
  // иначе останется «удалить то, чего в уровне и не было».
  const i = S.ed.added.findIndex((a) => a.path === path);
  if (i >= 0) { S.ed.added.splice(i, 1); S.ed.editable = S.ed.editable.filter((x) => x.path !== path); }
  S.ed.rebuildPickable();
  S.dirty = true;
  log(`− ${path} — уйдёт из уровня при пересборке`, 'warn');
  if (S.ed.sel === path) S.ed.select(null);
  renderTree();
}

/* ======================================================== ассеты/GLB */

/**
 * Путь ассета -> URL, который отдаёт serve.py.
 *
 * Два случая, и они разные по устройству:
 *   * файл В КАТАЛОГЕ ИГРЫ - это обычная статика. Студия лежит на два уровня
 *     глубже (`web3d/studio/`), поэтому поднимаемся на два;
 *   * файл ВНЕ каталога игры (`ext:3d/nova.glb`) - это ручка `/__ext/<имя>/...`.
 *     Обходить это «относительным путём» нельзя: браузер за пределы корня
 *     сервера не выйдет, и файл просто не загрузится.
 */
function assetUrl(p) {
  if (p.startsWith('ext:')) {
    const rest = p.slice(4);
    const i = rest.indexOf('/');
    return '/__ext/' + rest.slice(0, i) + '/' + rest.slice(i + 1)
      .split('/').map(encodeURIComponent).join('/');
  }
  return '../../' + p.split('/').map(encodeURIComponent).join('/');
}

async function loadAssets() {
  const r = await fetch('/__assets');
  if (!r.ok) throw new Error('HTTP ' + r.status);
  S.assets = await r.json();
  renderAssets();
  // Каталог игры приходит от сервера, а не выводится из URL: страница лежит в
  // `web3d/`, и по её адресу имени игры не видно. Это единственное место, где
  // видно, ЧЬИ данные открыты, — поэтому показываем всегда.
  const gp = $('gamepath');
  if (gp && S.assets.game) {
    gp.innerHTML = '';
    gp.appendChild(document.createTextNode('каталог: '));
    gp.appendChild(el('b', null, S.assets.game));
  }
  log(`ассеты: ${S.assets.images.length} картинок, ${S.assets.glbs.length} GLB`
      + (S.assets.game ? ` · каталог ${S.assets.game}` : ''));
}

function renderAssets() {
  const grid = $('assetGrid');
  grid.innerHTML = '';
  const q = ($('assetFilter').value || '').toLowerCase();
  const list = S.assets.images.filter((a) => !q || a.path.toLowerCase().includes(q));
  $('assetCount').textContent = `${list.length} / ${S.assets.images.length}`;
  const frag = document.createDocumentFragment();
  for (const a of list.slice(0, 600)) {
    const c = el('div', 'card');
    const img = el('img');
    // `decoding="async"` + `loading="lazy"` не роскошь: в каталоге есть PNG по
    // 1.5 МБ (кадры персонажей), и без этого 500 карточек в одной сетке
    // забивают декодер и вкладка «Картинки» на секунды превращается в пустую
    // сетку серых плашек — хотя файлы в порядке.
    img.loading = 'lazy';
    img.decoding = 'async';
    img.src = assetUrl(a.path);
    img.onerror = () => { c.classList.add('bad'); };
    c.appendChild(img);
    c.appendChild(el('div', 'cap', a.path.split('/').pop()));
    c.title = `${a.path}\n${(a.bytes / 1024).toFixed(0)} KB`;
    c.onclick = () => {
      $('previewBig').innerHTML = '';
      const big = el('img');
      big.src = assetUrl(a.path);
      $('previewBig').appendChild(big);
      $('previewInfo').textContent = `${a.path}  ·  ${(a.bytes / 1024).toFixed(0)} KB`;
      showTab('preview');
    };
    frag.appendChild(c);
  }
  if (!S.assets.images.length) {
    grid.appendChild(el('div', 'dim', 'Пусто. Ассеты ищутся в Shrooms/, assets/, shots/.'));
  }
  grid.appendChild(frag);

  const gl = $('glbList');
  gl.innerHTML = '';
  for (const a of S.assets.glbs) {
    const r = el('div', 'glrow');
    r.appendChild(el('span', 'glname', a.path));
    r.appendChild(el('span', 'glsz', (a.bytes / 1048576).toFixed(1) + ' MB'));
    r.onclick = () => openGlb(a.path);
    gl.appendChild(r);
  }
  if (!S.assets.glbs.length) {
    gl.appendChild(el('div', 'dim',
      'GLB не найдено. Просмотрщик ищет *.glb в каталоге игры; ' +
      'модели репозитория лежат в assets/3d/.'));
  }
}

async function openGlb(path) {
  showTab('glb');
  const host = $('cvGlb');
  const meta = $('glbMeta');
  meta.innerHTML = '';
  meta.appendChild(el('div', 'dim', 'Загрузка ' + path + ' …'));
  if (S.viewer) S.viewer.dispose();
  else S.viewer = new GlbViewer(host);
  try {
    const t0 = performance.now();
    // GLB-модели репозитория весят 40..130 МБ, поэтому прогресс обязателен:
    // без него 130 МБ выглядят как «повисло» и пользователь жмёт ещё раз.
    const info = await S.viewer.load(assetUrl(path), (loaded, total) => {
      meta.textContent = total
        ? `Загрузка ${(loaded / 1048576).toFixed(1)} / ${(total / 1048576).toFixed(1)} MB`
        : `Загрузка ${(loaded / 1048576).toFixed(1)} MB`;
    });
    const ms = (performance.now() - t0).toFixed(0);
    meta.innerHTML = '';
    const rows = [
      ['файл', path],
      ['размер', `${sizeLine(info.box)}  ед.`],
      ['треугольников', info.tris.toLocaleString()],
      ['вершин', info.verts.toLocaleString()],
      ['V / T', info.vt.toFixed(3) + (info.vt > 0.95 ? '  ← похоже на суп из треугольников' : '  (норм ≈ 0.70)')],
      ['мешей / материалов', `${info.meshes} / ${info.mats}`],
      ['анимаций', String(info.anims)],
      ['загрузка', ms + ' мс'],
    ];
    for (const [k, v] of rows) {
      const r = el('div', 'irow');
      r.appendChild(el('span', 'ik', k));
      r.appendChild(el('span', 'iv', v));
      meta.appendChild(r);
    }
    if (!S.viewer.setVertexColors(false)) {
      meta.appendChild(el('div', 'warn', 'В меше нет COLOR_0 — тумблер вершинных цветов ничего не меняет.'));
    }
    log(`GLB ${path}: ${info.tris.toLocaleString()} треуг., ${ms} мс`);
    showTab('glb');
    S.viewer.resize();
  } catch (e) {
    meta.innerHTML = '';
    meta.appendChild(el('div', 'warn', 'Не загрузилось: ' + e.message));
    log(`GLB ${path}: ${e.message}`, 'err');
  }
}

/* ============================================================= вкладки */

function showTab(name) {
  S.tab = name;
  for (const t of document.querySelectorAll('.tab')) {
    t.classList.toggle('on', t.dataset.tab === name);
  }
  for (const p of document.querySelectorAll('.pane')) {
    const on = p.dataset.pane === name;
    p.classList.toggle('on', on);
    // Скрытая панель имеет нулевой размер, и рендерер рисует в 0x0. Поэтому
    // размеры пересчитываем В МОМЕНТ показа, а не при создании.
    if (on) {
      if (name === 'level' && S.ed) { S.ed.resize(); S.ed.applyView(); }
      if (name === 'glb' && S.viewer) S.viewer.resize();
    }
  }
  renderView();
}

/* ============================================================== запуск */

async function boot() {
  // Глобальные ссылки для отладки и для гейта: без них проверить студию
  // снаружи нечем, а «проверять глазами» здесь не работает — это тот же урок,
  // что и у run_editor.js.
  window.__studio = S;
  window.__log = log;
  // Открытие GLB наружу: гейту нужен вход в вьюер, а клик по списку требует
  // прокрутки и попадания в элемент. Именованная функция — честнее, чем
  // «гейт эмулирует клик и надеется, что попал».
  window.__studioOpenGlb = (p) => openGlb(p);
  window.__studioTab = (t) => showTab(t);
  // Наведение камеры на узел: снаружи это нужно и гейту, и съёмке кадров.
  // Через `ed.select` этого не сделать — выделение не двигает камеру, а узел
  // в кадре обязан оказаться, иначе проверка меряет пустоту.
  window.__studioFocus = (p) => zoomToPath(p);

  for (const t of document.querySelectorAll('.tab')) {
    t.onclick = () => showTab(t.dataset.tab);
  }

  // Вкладка «Игра»: iframe на страницу игры с того же сервера. Адрес берётся
  // относительно корня сервера (он и отдаёт каталог игры), поэтому страница
  // видит свои ассеты по тем же путям, что и при открытии напрямую.
  const openGame = () => {
    let page = ($('gamePage').value || '').trim().replace(/^\/+/, '');
    if (!page || page.includes('..')) {
      $('gameInfo').textContent = 'укажите имя страницы без «..»';
      return;
    }
    $('gameFrame').src = '/' + page;
    $('gameInfo').textContent = 'открыто: /' + page;
  };
  $('gameOpen').onclick = openGame;
  $('gamePage').onkeydown = (e) => { if (e.key === 'Enter') openGame(); };

  // Подставляем страницу игры, которая РЕАЛЬНО есть в каталоге, вместо
  // зашитого `ninja.html` (он остался от другого проекта и у всех прочих
  // давал 404). Порядок — от самой «играбельной» к самой простой: play.html
  // — готовая игра, index.html — как её зовут в большинстве игр.
  // Подставляем страницу игры, которая РЕАЛЬНО есть, вместо зашитого
  // `ninja.html` (он остался от другого проекта и у всех прочих давал 404).
  //
  // ВАЖНО про путь: сервер отдаёт КАТАЛОГ ИГРЫ как корень, поэтому страница
  // живёт на `/web3d/play.html`, а не на `/projects/games/<игра>/web3d/...`.
  // Полный путь из подписи «каталог: …» брать нельзя — это 404.
  const guessGamePage = async () => {
    for (const cand of ['web3d/play.html', 'web3d/index.html', 'index.html']) {
      try {
        const r = await fetch('/' + cand, { method: 'HEAD' });
        if (r.ok) { $('gamePage').value = cand; return; }
      } catch { /* пробуем следующий */ }
    }
  };
  setTimeout(guessGamePage, 700);

  $('levelSel').onchange = (e) => openLevel(e.target.value);
  $('treeFilter').oninput = renderTree;
  $('assetFilter').oninput = renderAssets;

  // Кнопки уровня
  $('mode2d').onclick = () => setMode('2d');
  $('mode3d').onclick = () => setMode('3d');
  $('zin').onclick = () => { if (S.ed) { S.ed.zoom = Math.min(4, S.ed.zoom * 1.25); S.ed._applyOrthoZoom(); renderView(); } };
  $('zout').onclick = () => { if (S.ed) { S.ed.zoom = Math.max(0.05, S.ed.zoom / 1.25); S.ed._applyOrthoZoom(); renderView(); } };
  $('fit').onclick = () => fitLevel();
  $('toggleCol').onclick = (e) => {
    if (!S.ed) return;
    S.ed.setCollisions(!S.ed.showCollisions);
    e.target.classList.toggle('on', S.ed.showCollisions);
  };
  $('togglePar').onclick = (e) => {
    if (!S.ed) return;
    const on = !S.ed.showParallax;
    S.ed.setParallaxVisible(on);
    e.target.classList.toggle('on', on);
  };
  $('undoBtn').onclick = () => { if (S.ed && S.ed.undo()) renderTree(); };
  $('revBtn').onclick = () => {
    if (S.ed && confirm('Сбросить все правки этого уровня?')) { S.ed.revertAll(); renderTree(); renderInspector(null); }
  };
  $('lintBtn').onclick = lintLevel;
  $('saveBtn').onclick = async () => {
    if (!S.ed) return;
    try {
      await S.ed.saveEdits();
      S.ed.dirty = false; S.dirty = false;
      $('saveBtn').classList.remove('hot');
      renderTree();
      lintLevel();
    } catch (e) { log('сохранение: ' + e.message, 'err'); }
  };
  $('buildBtn').onclick = async () => {
    if (!S.ed) return;
    if (S.dirty && !confirm('Есть несохранённые правки — пересборка их не увидит. Сохранить и пересобрать?')) return;
    if (S.dirty) { await S.ed.saveEdits(); S.dirty = false; $('saveBtn').classList.remove('hot'); }
    $('buildBtn').disabled = true;
    log('пересборка уровня…');
    try { await S.ed.rebuild(); renderTree(); }
    catch (e) { log('сборка: ' + e.message, 'err'); }
    finally { $('buildBtn').disabled = false; lintLevel(); }
  };

  // Добавление: тип берём из текущего выделения — «сделай ещё такую же» это
  // 99% случаев, а пустой выбор типа оставил бы человека без подсказки.
  $('addBtn').onclick = () => {
    if (!S.ed) return;
    if (!S.ed.sel) { log('сначала выберите узел-образец в кадре или списке', 'err'); return; }
    addNode(null, S.ed.sel);
  };
  $('delBtn').onclick = () => { if (S.ed && S.ed.sel) removeNode(S.ed.sel); };

  // GLB
  for (const id of ['bboxGrid', 'grid', 'axes', 'wire', 'normals', 'vcol']) {
    const cb = $(id);
    if (!cb) continue;
    cb.onchange = () => {
      if (!S.viewer) return;
      if (id === 'vcol') {
        const ok = S.viewer.setVertexColors(cb.checked);
        if (cb.checked && !ok) log('в меше нет COLOR_0', 'warn');
      } else S.viewer.setOverlay(id, cb.checked);
    };
  }
  $('glbReset').onclick = () => S.viewer && S.viewer.resetView();
  $('glbFile').onchange = (e) => {
    const f = e.target.files[0];
    if (!f || !S.viewer) return;
    const url = URL.createObjectURL(f);
    S.viewer.load(url).then((info) => {
      const meta = $('glbMeta');
      meta.innerHTML = '';
      for (const [k, v] of [['файл', f.name], ['размер', sizeLine(info.box)],
        ['треугольников', info.tris.toLocaleString()], ['вершин', info.verts.toLocaleString()],
        ['V / T', info.vt.toFixed(3)]]) {
        const r = el('div', 'irow');
        r.appendChild(el('span', 'ik', k)); r.appendChild(el('span', 'iv', v));
        meta.appendChild(r);
      }
    }).catch((err) => log('локальный GLB: ' + err.message, 'err'));
  };

  addEventListener('resize', () => {
    if (S.ed) S.ed.resize();
    if (S.viewer) S.viewer.resize();
  });

  $('sideToggle').onclick = toggleSide;
  uiBoot();
  addEventListener('keydown', (e) => {
    if (e.ctrlKey && e.code === 'KeyB') { e.preventDefault(); toggleSide(); }
  });

  try {
    await loadManifest();
    await openLevel($('levelSel').value);
  } catch (e) {
    log('уровень не открылся: ' + e.message, 'err');
  }
  try { await loadAssets(); }
  catch (e) { log('ассеты: ' + e.message, 'err'); }

  showTab('level');
  window.__ready = true;
}

function setMode(m) {
  if (!S.ed) return;
  S.ed.setMode(m);
  $('mode2d').classList.toggle('on', m === '2d');
  $('mode3d').classList.toggle('on', m === '3d');
  renderView();
}

function fitLevel() {
  if (!S.ed) return;
  // Габариты корня сцены — это габариты уровня. Кадрируем по ним, а не по
  // «примерно 0.3»: разный уровень имеет разную длину, и один зум на всех
  // либо показывает половину, либо превращает уровень в нитку.
  const b = new THREE.Box3().setFromObject(S.ed.gs.root);
  if (b.isEmpty()) return;
  const size = b.getSize(new THREE.Vector3());
  const c = b.getCenter(new THREE.Vector3());
  const host = $('cvLevel');
  const zx = host.clientWidth / Math.max(1, size.x);
  const zy = host.clientHeight / Math.max(1, size.y);
  S.ed.zoom = Math.max(0.05, Math.min(4, Math.min(zx, zy) * 0.92));
  S.ed.pan.x = c.x;
  S.ed.pan.y = -c.y;
  S.ed.applyView();
  renderView();
}

// --------------------------------------------------------------- масштаб UI
// Весь интерфейс в rem (см. studio.html), поэтому одна переменная `--ui-size`
// на <html> меняет его целиком: подписи, кнопки, дерево, лог. По умолчанию она
// текучая — clamp(13px, 0.42vw + 8.4px, 19px), то есть на большом мониторе
// интерфейс крупнее сам, без браузерного зума. Кнопки A−/A+ фиксируют её
// вручную, и выбор переживает перезагрузку страницы.
const UI_KEY = 'studio.uiSize';
const UI_BASE = 13;   // база, от которой считаются проценты на кнопке
const UI_MIN = 11;
const UI_MAX = 28;

/** Текущий размер корневого шрифта в px — он и есть масштаб интерфейса. */
function uiCurrent() {
  return parseFloat(getComputedStyle(document.documentElement).fontSize) || UI_BASE;
}

/** `px === null` — вернуть текучую величину из CSS (сброс к автомату). */
function uiApply(px) {
  const root = document.documentElement;
  if (px == null) root.style.removeProperty('--ui-size');
  else root.style.setProperty('--ui-size', px + 'px');
  uiLabel();
  // Раскладка целиком в rem, поэтому после смены масштаба её надо пересобрать:
  // обработчики `resize` пересчитают и холсты, и ширины панелей (их clamp в rem).
  dispatchEvent(new Event('resize'));
}

function uiLabel() {
  const btn = $('uiLabel');
  if (!btn) return;
  const px = uiCurrent();
  btn.textContent = Math.round((px / UI_BASE) * 100) + '%';
  btn.title = 'Размер текста ' + px.toFixed(1) + ' px. Клик — вернуть автомат';
}

function uiStep(dir) {
  const next = Math.max(UI_MIN, Math.min(UI_MAX, Math.round(uiCurrent() + dir)));
  try { localStorage.setItem(UI_KEY, String(next)); } catch { /* приватный режим */ }
  uiApply(next);
}

function uiBoot() {
  const minus = $('uiMinus'), plus = $('uiPlus'), lbl = $('uiLabel');
  if (!minus || !plus || !lbl) return;
  let saved = null;
  try {
    const raw = localStorage.getItem(UI_KEY);
    if (raw != null) saved = parseFloat(raw);
  } catch { /* приватный режим: настройка просто не сохранится */ }
  if (Number.isFinite(saved)) uiApply(saved);
  else uiLabel();
  minus.onclick = () => uiStep(-1);
  plus.onclick = () => uiStep(1);
  lbl.onclick = () => {
    try { localStorage.removeItem(UI_KEY); } catch { /* приватный режим */ }
    uiApply(null);
  };
  // Текучая величина зависит от ширины окна — при ресайзе обновляем подпись.
  // Сами холсты пересчитывает обработчик resize из boot().
  addEventListener('resize', uiLabel);
}

function toggleSide() {
  const app = document.getElementById('app');
  app.classList.toggle('hide-side');
  if (S.ed) S.ed.resize();
  if (S.viewer) S.viewer.resize();
}

boot();
