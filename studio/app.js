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
  sector: 0,          // -1 = весь уровень (Fit)
  sectors: [],
  edZoom: 0.7,        // читаемый зум «на один экран игры»
};

function log(msg, kind = 'info') {
  const box = $('log');
  const line = el('div', 'logline ' + kind);
  line.textContent = msg;
  box.appendChild(line);
  box.scrollTop = box.scrollHeight;
  while (box.children.length > 400) box.removeChild(box.firstChild);
}

/* Выбор проекта живёт в launcher.js, а не здесь: app.js тянет за собой
 * scene.js и three.js из КАТАЛОГА ИГРЫ, поэтому в пустой студии его нельзя
 * грузить вообще. launcher.js показываёт список и импортирует этот файл
 * только после POST /__open. См. комментарий в launcher.js.
 */

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
    // В списке — только человеческое имя: файл показан чипом рядом и в
    // статус-строке, дублировать его в каждой строке незачем.
    const o = el('option', null, `${l.title || l.id}`);
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
    onChange: () => { S.dirty = true; $('saveBtn').classList.add('hot'); renderTree(); updateStatus(); },
    onSelect: (path, info) => { renderInspector(info); renderLayers(S.ed.layerList()); renderTree(); },
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
  // Имя файла уровня — всегда на виду: в тулбаре чипом и в статус-строке.
  const lt = $('levelTag');
  if (lt) { lt.textContent = def.file; lt.style.display = ''; }
  renderTree();
  renderLayers(S.ed.layerList());
  renderInspector(null);
  renderView();
  updateStatus();
  S.ed.start();
  // Не оставляем Fit «на весь уровень»: по умолчанию камера стоит на первом
  // участке в масштабе одного экрана, как в Godot.
  S.sector = 0;
  computeSectors();
  gotoSector(0);
  // Вердикт линтера — сразу при открытии, а не по кнопке: иначе человек
  // видит пустой кадр и не знает, что причина в отсутствующих ассетах.
  lintLevel();
}

/* ------------------------------------------------------------- дерево */

/* Цвета маркеров слоёв. Раньше дерево было монохромным, и глаз не цеплялся
   за границу слоя: строки шли сплошняком. Цвет повторяет порядок слоёв в
   дереве (см. renderLayers), поэтому «красный» в дереве и в списке слоёв —
   один и тот же слой. */
const LAYER_COLORS = ['#e2584c', '#e8a35c', '#79b8f2', '#59d99a',
  '#c792ea', '#ffd166', '#66d9e8', '#f78fb3'];

function layerColor(name) {
  const i = S.ed ? S.ed.layerOrder.indexOf(name) : -1;
  return LAYER_COLORS[(i < 0 ? 0 : i) % LAYER_COLORS.length];
}

function renderTree() {
  const box = $('tree');
  box.innerHTML = '';
  if (!S.ed) return;
  const q = ($('treeFilter').value || '').toLowerCase();
  const root = el('div', 'tnode');
  const head = el('div', 'tname root');
  head.appendChild(el('span', null, `Main — ${S.level.file}`));
  root.appendChild(head);
  const groups = new Map();
  for (const e of S.ed.editable) {
    const lay = S.ed._layerOf(e.obj);
    if (!groups.has(lay)) groups.set(lay, []);
    groups.get(lay).push(e);
  }
  let shown = 0;
  for (const lay of S.ed.layerOrder) {
    const items = groups.get(lay) || [];
    const g = el('div', 'tgroup');
    g.style.setProperty('--dot', layerColor(lay));
    // Заголовок слоя — тоже «выбиратель» слоя: клик подсвечивает все его узлы
    // и разрешает тащить их разом, как группу в Godot.
    const h = el('div', 'tname grp' + (S.ed.activeLayer === lay ? ' on' : ''));
    h.appendChild(el('span', null, lay));
    h.appendChild(el('span', 'lcnt', String(items.length)));
    h.title = 'Клик — выбрать слой целиком (сдвинуть все узлы сразу)';
    h.onclick = () => selectLayerToggle(lay);
    g.appendChild(h);
    for (const e of items) {
      if (q && !e.path.toLowerCase().includes(q)) continue;
      shown++;
      const row = el('div', 'n' + (S.ed.sel === e.path ? ' sel' : '') +
        (e.added ? ' added' : '') + (S.ed.edits[e.path] ? ' edited' : ''));
      row.appendChild(el('span', null, e.path));
      row.dataset.path = e.path;
      row.style.setProperty('--dot', layerColor(lay));
      row.onclick = () => {
        S.ed.select(e.path);
        focusPath(e.path);
      };
      row.ondblclick = () => zoomToPath(e.path);
      g.appendChild(row);
    }
    // `continue`, а не `return`: пустой слой при активном фильтре не должен
    // обрывать отрисовку всех СЛЕДУЮЩИХ слоёв.
    if (!items.length && q) continue;
    root.appendChild(g);
  }
  box.appendChild(root);
  const cnt = $('treeCount');
  if (cnt) cnt.textContent = q ? `${shown} / ${S.ed.editable.length}` : String(S.ed.editable.length);
  updateStatus();
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
  const kind = $('inspKind');
  if (!S.ed) return;
  if (kind) kind.textContent = info ? (info.type === 'layer' ? 'слой' : (info.type || 'узел')) : '—';
  if (!info) {
    // Пустой инспектор — не «ничего не выбрано», а справка: в редакторе это
    // единственное место, где человек узнаёт, что вообще можно делать.
    const e = el('div', 'empty');
    e.appendChild(el('h5', null, 'Ничего не выбрано'));
    const rows = [
      ['ЛКМ', 'выбрать узел в кадре'],
      ['ЛКМ + тащить', 'сдвинуть узел (или весь слой)'],
      ['↑ ↓ ← →', 'сдвиг на 1 · Shift — на 10'],
      ['Двойной клик', 'приблизить к узлу'],
      ['Ctrl+Z', 'отменить правку'],
      ['Ctrl+B', 'свернуть панели'],
    ];
    for (const [k, v] of rows) {
      const r = el('div', 'er');
      r.appendChild(el('kbd', null, k));
      r.appendChild(el('span', null, v));
      e.appendChild(r);
    }
    box.appendChild(e);
    updateHud();
    return;
  }
  // Строка «ключ — значение» (объявлена до веток, иначе TDZ при вызове в
  // ветке слоя, которая идёт выше объявления).
  const row = (k, v, cls) => {
    const r = el('div', 'irow ' + (cls || ''));
    r.appendChild(el('span', 'ik', k));
    r.appendChild(el('span', 'iv', v));
    box.appendChild(r);
    return r;
  };
  // Выбран СЛОЙ целиком (Godot-режим «перетащить группу»).
  if (info.type === 'layer') {
    box.appendChild(el('div', 'dim', `Слой: ${info.layer}`));
    row('узлов в слое', String(info.count));
    row('видимость', info.visible ? 'включена' : 'скрыт');
    row('заморозка', info.locked ? 'заблокирован' : 'правится');
    const acts = el('div', 'iacts');
    const bVis = el('button', info.visible ? 'on' : '', info.visible ? 'Скрыть слой' : 'Показать слой');
    bVis.onclick = () => { S.ed.setLayerVisible(info.layer, !info.visible); renderLayers(S.ed.layerList()); renderInspector(S.ed.layerInfo(info.layer)); };
    const bLock = el('button', info.locked ? 'on' : '', info.locked ? 'Разморозить' : 'Заморозить');
    bLock.onclick = () => { S.ed.setLayerLocked(info.layer, !info.locked); renderLayers(S.ed.layerList()); renderInspector(S.ed.layerInfo(info.layer)); };
    acts.appendChild(bVis); acts.appendChild(bLock);
    box.appendChild(acts);
    box.appendChild(el('div', 'warn',
      'Слой активен: перетащите в кадре или стрелками ←→↑↓, чтобы сдвинуть ВСЕ узлы слоя сразу. ' +
      'Shift — шаг 10. Клик по отдельному узлу в кадре/дереве вернёт правку одного узла.'));
    const bClear = el('button', '', 'Снять выделение слоя');
    bClear.onclick = () => { S.ed.clearLayer(); renderLayers(S.ed.layerList()); renderTree(); renderInspector(null); };
    box.appendChild(bClear);
    updateHud();
    return;
  }
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
  updateHud();
}

/* ------------------------------------------------------------- слои */

function renderLayers(list) {
  const box = $('layers');
  box.innerHTML = '';
  for (const l of list) {
    const r = el('div', 'lrow' + (l.active ? ' active' : ''));
    r.style.setProperty('--dot', layerColor(l.name));
    r.dataset.layer = l.name;
    r.title = 'Клик — выбрать слой целиком (сдвинуть все узлы сразу). Глаз — видимость, замок — запрет правки.';
    const dot = el('span', 'ldot');
    const eye = el('button', 'icn' + (l.visible ? ' on' : ''), l.visible ? '◉' : '◌');
    eye.title = 'Видимость слоя';
    eye.onclick = (e) => { e.stopPropagation(); S.ed.setLayerVisible(l.name, !l.visible); };
    const lock = el('button', 'icn' + (l.locked ? ' on' : ''), l.locked ? '🔒' : '🔓');
    lock.title = 'Заморозить слой (запрет правки)';
    lock.onclick = (e) => { e.stopPropagation(); S.ed.setLayerLocked(l.name, !l.locked); };
    const name = el('span', 'lname', l.name);
    const cnt = el('span', 'lcnt', String(l.count));
    r.appendChild(dot); r.appendChild(eye); r.appendChild(lock); r.appendChild(name); r.appendChild(cnt);
    // Параллакс-слоям — метка: их позиция вычисляется из камеры, двигать нельзя.
    const isPar = /Backdrop|Parallax|Far|Mid/.test(l.name);
    if (isPar) {
      const tag = el('span', 'ltag', 'par');
      tag.title = 'Слой параллакса: позиция вычисляется из камеры';
      r.appendChild(tag);
    }
    r.onclick = () => selectLayerToggle(l.name);
    box.appendChild(r);
  }
  updateStatus();
}

/** Клик по слою в панели «Слои»: выбрать слой целиком (как в Godot выбрать
 *  группу) или снять выделение, если он уже активен. */
function selectLayerToggle(name) {
  if (!S.ed) return;
  if (S.ed.activeLayer === name) S.ed.clearLayer();
  else S.ed.selectLayer(name);
  renderLayers(S.ed.layerList());
  renderTree();
}

function renderView() {
  if (!S.ed) return;
  const host = $('cvLevel');
  const vw = host.clientWidth / Math.max(0.001, S.ed.zoom);
  const x0 = Math.round(S.ed.pan.x - vw / 2), x1 = Math.round(S.ed.pan.x + vw / 2);
  const v = `${S.ed.mode.toUpperCase()} · zoom ${S.ed.zoom.toFixed(2)} · ` +
    `панорама ${Math.round(S.ed.pan.x)}, ${Math.round(S.ed.pan.y)} · ` +
    `x ${x0}..${x1}`;
  const vi = $('viewInfo');
  if (vi) vi.textContent = v;
  const sv = $('stView');
  if (sv) sv.textContent = v;
  updateHud();
}

/* ------------------------------------------------------------ статус/HUD */

/** Статус-строка: то, что в редакторе читают боковым зрением — что открыто,
 *  сколько узлов, есть ли несохранённое. */
function updateStatus() {
  const ed = S.ed;
  const nodes = ed ? ed.editable.length : 0;
  const layers = ed ? ed.layerOrder.length : 0;
  const edits = ed ? Object.keys(ed.edits || {}).length : 0;
  const set = (id, v) => { const e = $(id); if (e) e.textContent = v; };
  set('stNodes', String(nodes));
  set('stLayers', String(layers));
  set('stEdits', String(edits));
  set('editCount', String(edits));
  set('stLevel', S.level ? (S.level.title || S.level.id) : '—');
  set('stFile', S.level ? S.level.file : '');
  const st = $('stState');
  if (st) st.textContent = S.dirty ? 'есть правки' : 'готово';
  const dot = $('stDot');
  if (dot) dot.classList.toggle('busy', !!S.dirty);
  const dt = $('dirtyTag');
  if (dt) {
    dt.textContent = S.dirty ? 'не сохранено' : 'сохранено';
    dt.classList.toggle('hot', !!S.dirty);
  }
}

/** HUD кадра: режим, координаты выделенного узла, подпись выбора. */
function updateHud() {
  const set = (id, v) => { const e = $(id); if (e) e.textContent = v; };
  const ed = S.ed;
  const vm = $('vmode');
  if (vm && ed) vm.textContent = ed.mode === '3d' ? 'PERSP' : 'ORTHO';
  if (!ed) { set('hudTool', 'select'); set('hudX', '—'); set('hudY', '—'); return; }
  const info = ed.sel ? ed.infoOf(ed.sel) : null;
  if (info) {
    set('hudTool', 'move');
    set('hudX', String(info.pos[0]));
    set('hudY', String(info.pos[1]));
    set('hudSel', info.path);
  } else if (ed.activeLayer) {
    set('hudTool', 'move layer');
    set('hudX', '—');
    set('hudY', '—');
    set('hudSel', 'слой: ' + ed.activeLayer);
  } else {
    set('hudTool', 'select');
    set('hudX', '—');
    set('hudY', '—');
    set('hudSel', 'ничего не выбрано');
  }
}

/* ================================================ участки уровня (секторы) */

/**
 * Уровень шириной ~3700 px при Fit превращается в тонкую полоску: «открыл
 * редактор — ничего не видно». Godot так не работает: там камера стоит на
 * ОДНОМ экране, а по уровню ходят. Поэтому по умолчанию показываем участок
 * ~1 экран игры с читаемым зумом, аFit остаётся отдельной кнопкой.
 */
function computeSectors() {
  const ed = S.ed;
  if (!ed) return;
  const host = $('cvLevel');
  S.edZoom = Math.max(0.35, Math.min(1.1,
    Math.min(host.clientHeight / 780, host.clientWidth / 1450)));
  let min = Infinity, max = -Infinity;
  for (const e of ed.editable) {
    const p = ed.levelPos(e.path);
    if (!p) continue;
    if (p[0] < min) min = p[0];
    if (p[0] > max) max = p[0];
  }
  if (!isFinite(min)) { min = 0; max = 1280; }
  const step = Math.max(900, Math.round((host.clientWidth / S.edZoom) * 0.9));
  // Первый участок начинаем с нуля, а не с «минус одного шага»: отрицательные
  // x есть у фона и стен, и без этого сектор 1 показывал бы пустоту левее
  // уровня — ровно та же жалоба «открыл и вижу кусок ниоткуда».
  const start = Math.max(0, Math.floor(min / step) * step);
  const n = Math.max(1, Math.ceil((max + 200 - start) / step));
  S.sectors = Array.from({ length: n }, (_, i) => ({
    start: start + i * step, end: start + (i + 1) * step,
  }));
  updateSectorSel();
}

function updateSectorSel() {
  const sel = $('secSel');
  if (!sel) return;
  sel.innerHTML = '';
  const all = el('option', null, 'весь уровень');
  all.value = '-1';
  sel.appendChild(all);
  S.sectors.forEach((s, i) => {
    const o = el('option', null, `участок ${i + 1} · x ${Math.round(s.start)}–${Math.round(s.end)}`);
    o.value = String(i);
    sel.appendChild(o);
  });
  sel.value = String(S.sector);
}

function gotoSector(i) {
  const ed = S.ed;
  if (!ed) return;
  if (i === -1) { S.sector = -1; fitLevel(); updateSectorSel(); return; }
  if (!S.sectors.length) computeSectors();
  S.sector = Math.max(0, Math.min(S.sectors.length - 1, i));
  const s = S.sectors[S.sector];
  ed.zoom = S.edZoom;
  ed.pan.x = (s.start + s.end) / 2;
  ed.pan.y = 360;                     // центр виртуального кадра 1280×720
  ed.applyView();
  updateSectorSel();
}

/* ====================================================== добавление узла */

/**
 * Добавить объект «ещё такой же»: копируем ТЕКСТУРУ выделенного узла, а не
 * весь THREE-объект. Клонировать объект нельзя — у площадки внутри лежит
 * коллайдер-подсветка и настроенный renderOrder, и «копия» начинала бы жить
 * своей жизнью, никак не попадая в файл правок.
 *
 * Источник правды — specs в `add`: студия показывает узел сразу, игра читает
 * тот же specs при старте (web3d/level_overlay.js).
 */
async function addNode(type, srcPath) {
  if (!S.ed) return;
  const src = S.ed.editableByPath.get(srcPath);
  if (!src) return;
  const tex = (src.node.props || {}).texture;
  if (!tex) { log('у узла нет текстуры — выберите ассет в библиотеке', 'err'); return; }
  const pos = [Math.round(S.ed.pan.x), Math.round(S.ed.pan.y)];
  const p = await S.ed.addAsset({ path: tex }, pos);
  if (p) { renderTree(); renderLayers(S.ed.layerList()); updateStatus(); }
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
    // забивают декодер и вкладка «Картинки» превращается в сетку серых плашек.
    img.loading = 'lazy';
    img.decoding = 'async';
    img.src = assetUrl(a.path);
    img.onerror = () => { c.classList.add('bad'); };
    c.appendChild(img);
    c.appendChild(el('div', 'cap', a.path.split('/').pop()));
    c.title = `${a.path}\n${(a.bytes / 1024).toFixed(0)} KB`;
    c.onclick = () => openImage(a);
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
  renderLevelAssets();
}

/** Картинка на весь экран во вкладке «Картинки». */
function openImage(a) {
  const big = $('previewBig');
  big.innerHTML = '';
  const img = el('img');
  img.src = assetUrl(a.path);
  big.appendChild(img);
  $('previewInfo').textContent = `${a.path}  ·  ${(a.bytes / 1024).toFixed(0)} KB`;
  showTab('preview');
}

/**
 * Клик по ассету в нижней библиотеке = ПОЛОЖИТЬ ЕГО В УРОВЕНЬ.
 * Раньше клик просто открывал превью картинки, и «добавить платформу» было
 * невозможно в принципе. Теперь объект появляется в центре вида (или в
 * активном слое), сразу выделяется и тащится мышью; Shift+клик оставляет
 * старое поведение — посмотреть картинку крупно.
 */
async function placeAsset(a) {
  if (!S.ed) return;
  const pos = [S.ed.pan.x, S.ed.pan.y];
  const p = await S.ed.addAsset(a, pos);
  if (!p) { log(`ассет не добавлен: ${a.path}`, 'err'); return; }
  S.dirty = true;
  $('saveBtn').classList.add('hot');
  renderTree();
  renderLayers(S.ed.layerList());
  updateStatus();
}

/**
 * Нижняя библиотека ассетов (как ASSET LIBRARY в редакторе уровней).
 *
 * Показывает картинки каталога игры плотной сеткой. Это не дубль вкладки
 * «Картинки»: здесь библиотека всегда под рукой, пока правишь уровень, и
 * открывает превью одним кликом, не уводя из сцены насовсем.
 */
function renderLevelAssets() {
  const grid = $('lvAssetGrid');
  if (!grid) return;
  const q = (($('lvAssetFilter') || {}).value || '').toLowerCase();
  const all = S.assets.images || [];
  const list = all.filter((a) => !q || a.path.toLowerCase().includes(q));
  const cnt = $('lvAssetCount');
  if (cnt) cnt.textContent = `${list.length} / ${all.length}`;
  grid.innerHTML = '';
  const frag = document.createDocumentFragment();
  for (const a of list.slice(0, 400)) {
    const card = el('div', 'acard');
    const img = el('img');
    img.loading = 'lazy';
    img.decoding = 'async';
    img.src = assetUrl(a.path);
    img.onerror = () => card.classList.add('bad');
    card.appendChild(img);
    card.appendChild(el('div', 'cap', a.path.split('/').pop()));
    card.appendChild(el('div', 'sub', a.path.split('/').slice(0, -1).join('/') || '—'));
    card.title = `${a.path}\n${(a.bytes / 1024).toFixed(0)} KB — клик: добавить в уровень, Shift+клик: посмотреть`;
    card.onclick = (ev) => { if (ev.shiftKey) openImage(a); else placeAsset(a); };
    frag.appendChild(card);
  }
  grid.appendChild(frag);
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

  // Вкладки левой панели «Объекты / Слои». Обе показывают одно состояние с
  // разных сторон: дерево — иерархию, список слоёв — видимость и замок.
  for (const t of document.querySelectorAll('.ptab')) {
    t.onclick = () => {
      for (const x of document.querySelectorAll('.ptab')) x.classList.toggle('on', x === t);
      const isTree = t.dataset.ptab === 'tree';
      const pt = $('paneTree'), pl = $('paneLayers');
      if (pt) pt.hidden = !isTree;
      if (pl) pl.hidden = isTree;
      const filt = $('treeFilter');
      if (filt) filt.parentElement.style.display = isTree ? '' : 'none';
    };
  }

  // Журнал — выдвижной ящик: держать 120 px под лог в редакторе нельзя.
  const lg = $('logbox');
  const setLog = (open) => {
    if (!lg) return;
    lg.classList.toggle('open', open);
    const b = $('logToggle');
    if (b) b.textContent = open ? 'Журнал ▾' : 'Журнал ▴';
  };
  if ($('logToggle')) $('logToggle').onclick = () => setLog(!lg.classList.contains('open'));
  if ($('logClose')) $('logClose').onclick = () => setLog(false);

  // Нижняя библиотека ассетов.
  if ($('lvAssetFilter')) $('lvAssetFilter').oninput = renderLevelAssets;
  if ($('lvAssetAll')) $('lvAssetAll').onclick = () => showTab('preview');

  // Сворачиваемые секции боковой панели: клик по заголовку складывает секцию
  // (как группы в Godot). При 6 секциях это держит нужное под рукой, не уходя
  // в длинный скролл. ▾ в заголовке — индикатор раскрытия.
  for (const h of document.querySelectorAll('.pane[data-pane="level"] .side .sec > h4')) {
    const f = document.createElement('span');
    f.className = 'fold';
    f.textContent = '▾';
    h.prepend(f);
    h.addEventListener('click', () => h.parentElement.classList.toggle('collapsed'));
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
    // Раньше здесь были HEAD-запросы к трём кандидатам. У НОВОГО проекта
    // нет ещё ни одной страницы игры, и все три промаха давали 404 в консоли
    // — то есть «чисто созданный проект» выглядел как падение. Сервер теперь
    // отвечает на /__gamepage одним 200 и говорит, что реально лежит на диске.
    try {
      const r = await fetch('/__gamepage', { cache: 'no-store' });
      if (r.ok) {
        const j = await r.json();
        if (j.page) $('gamePage').value = j.page;
        else if ($('gameInfo')) $('gameInfo').textContent =
          'у проекта ещё нет страницы игры — это нормально для нового проекта';
        return;
      }
    } catch { /* старый сервер без ручки — проверяем ниже */ }
    for (const cand of ['index.html', 'play.html', 'web3d/play.html']) {
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
  $('fit').onclick = () => { S.sector = -1; fitLevel(); updateSectorSel(); };
  $('secSel').onchange = (e) => gotoSector(parseInt(e.target.value, 10));
  $('secPrev').onclick = () => gotoSector((S.sector < 0 ? 0 : S.sector) - 1);
  $('secNext').onclick = () => gotoSector((S.sector < 0 ? -1 : S.sector) + 1);
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
    // «Пересобрать» больше не зовёт python-сборщик: уровни генерируются из
    // levels.js, а правки накладывает САМА ИГРА при старте. Поэтому достаточно
    // сохранить оверлей и перезапустить iframe — человек сразу видит результат.
    try {
      await S.ed.saveEdits();
      S.ed.dirty = false; S.dirty = false;
      $('saveBtn').classList.remove('hot');
      const f = $('gameFrame');
      if (f.src) f.src = f.src;
      else { $('gamePage').value = 'index.html'; $('gameOpen').click(); }
      showTab('game');
      log('правки сохранены — игра перезапущена с ними');
    } catch (e) { log('применение: ' + e.message, 'err'); }
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
    if (S.ed) { S.ed.resize(); if (S.sectors.length) computeSectors(); }
    if (S.viewer) S.viewer.resize();
  });

  $('sideToggle').onclick = toggleSide;
  uiBoot();
  addEventListener('keydown', (e) => {
    if (e.ctrlKey && e.code === 'KeyB') { e.preventDefault(); toggleSide(); }
  });

  // Сюда мы попадаем ТОЛЬКО когда проект уже выбран (launcher.js), поэтому
  // levels.json, scene.js и вендор three.js гарантированно доступны.
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
