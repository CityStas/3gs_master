/*
 * launcher.js — ПУСТОЙ старт студии и выбор проекта.
 *
 * Почему это отдельный файл, а не кусок app.js:
 *   app.js -> leveledit.js / glbview.js -> `../scene.js`, `../vendor/three...`,
 *   OrbitControls, GLTFLoader. Все эти модули лежат ВНУТРИ проекта. Пока
 *   проект не выбран, серверу нечего отдать на /web3d/scene.js, граф импортов
 *   падает целиком, и показать экран выбора некому. Поэтому сначала грузится
 *   этот файл (у него НЕТ ни одного импорта), а app.js подключается
 *   динамически и ТОЛЬКО после того, как проект выбран.
 *
 * Разделение обязанностей:
 *   launcher.js  — реестр проектов, экран выбора, создание, переключение корня;
 *   app.js       — редактор (уровни, слои, инспектор, ассеты, игра);
 *   serve.py     — /__projects, /__new, /__open, /__close и статика проекта.
 *
 * Список ТОЛЬКО из projects/three/: это редактор three.js-сцен, и проекты
 * Roblox/Unity/Godot в нём были бы заведомо пустым выбором. Папки четырёх
 * движков, их RAG и pi-home-* при этом не трогаются вообще. Новый проект
 * создаётся тут же, в UI: tools/project_init.py раскладывает канонический
 * стек в новую папку projects/three/<имя>.
 */
const $ = (id) => document.getElementById(id);
const make = (tag, cls, txt) => {
  const e = document.createElement(tag);
  if (cls) e.className = cls;
  if (txt !== undefined) e.textContent = txt;
  return e;
};

const state = {
  projects: [],
  active: null,
  last: null,
  hub: true,
  engineRoot: 'projects/three',
  supported: false,   // сервер умеет /__projects
};

function log(msg) {
  const box = $('log');
  if (!box) return;
  const line = make('div', 'logline info');
  line.textContent = msg;
  box.appendChild(line);
  box.scrollTop = box.scrollHeight;
}

/** Сообщение в подвале экрана выбора (без всплывающих окон). */
let hintTimer = 0;
function flashHint(msg) {
  const hint = $('projHint');
  if (!hint) return;
  hint.textContent = msg;
  hint.style.color = 'var(--warn)';
  clearTimeout(hintTimer);
  hintTimer = setTimeout(() => { hint.style.color = ''; }, 6000);
}

/* ------------------------------------------------------------ реестр */

async function readProjects() {
  let data;
  try {
    const r = await fetch('/__projects', { cache: 'no-store' });
    if (!r.ok) throw new Error('HTTP ' + r.status);
    data = await r.json();
  } catch (e) {
    // Сервер без hub-режима (старый запуск, прямая копия serve.py в игре):
    // проект уже задан через --dir, просто грузим редактор как раньше.
    state.supported = false;
    state.hub = false;
    log('реестр проектов недоступен — обычный режим (' + e.message + ')');
    return false;
  }
  state.supported = true;
  state.projects = data.projects || [];
  state.active = data.active || null;
  state.last = data.last || null;
  state.engineRoot = (data.engineRoot || 'projects/three').replace(/\//g, '\\');
  state.hub = !state.active;
  const rootEl = $('projRoot');
  if (rootEl) rootEl.textContent = state.engineRoot;
  return true;
}

/* --------------------------------------------------------- шапка + оверлей */

function renderSelect() {
  const sel = $('projSel');
  if (!sel) return;
  sel.innerHTML = '';
  if (state.hub) {
    const o = make('option', null, '— не выбран —');
    o.value = '';
    sel.appendChild(o);
  }
  for (const p of state.projects) {
    const o = make('option', null, p.id + (p.hasLevels ? '' : '  (пустой)'));
    o.value = p.id;
    sel.appendChild(o);
  }
  // Создать проект можно и когда один уже открыт: экран выбора просто
  // показывается поверх редактора, активный проект остаётся на месте.
  const add = make('option', null, '+ Новый проект…');
  add.value = '__new__';
  sel.appendChild(add);
  sel.value = state.active || '';
  sel.onchange = () => {
    if (sel.value === '__new__') {
      sel.value = state.active || '';
      const ov = $('projOverlay');
      if (ov) ov.hidden = false;
      const inp = $('projNewName');
      if (inp) inp.focus();
      return;
    }
    if (sel.value) openProject(sel.value);
  };
}

function renderOverlay() {
  const box = $('projList');
  const ov = $('projOverlay');
  if (!box || !ov) return;
  ov.hidden = !state.hub;
  const dismiss = $('projDismiss');
  if (dismiss) dismiss.hidden = state.hub;
  box.innerHTML = '';
  if (!state.projects.length) {
    box.appendChild(make('div', 'dim',
      `В ${state.engineRoot}\\ пока нет ни одного проекта. `
      + 'Введите имя ниже — студия создаст папку и разложит полный three.js-стек.'));
    return;
  }
  // Один движок = одна группа; заголовок показывает, ОТКУДА читается список.
  box.appendChild(make('div', 'projengine', `three.js  ·  ${state.engineRoot}\\`));
  for (const p of state.projects) {
    const row = make('div', 'projrow' + (p.hasLevels ? '' : ' empty'));
    row.appendChild(make('div', 'pico', 'TH'));
    const info = make('div', 'pinfo');
    info.appendChild(make('div', 'pname', p.name));
    const bits = [p.id];
    bits.push(p.hasLevels ? `уровней: ${Math.max(0, p.levels)}`
                          : 'папка без web3d/levels.json');
    if (p.hasGame) bits.push('есть игра');
    info.appendChild(make('div', 'pmeta', bits.join('  ·  ')));
    row.appendChild(info);
    if (state.last === p.id) row.appendChild(make('span', 'plast', 'недавний'));
    row.appendChild(make('div', 'pgo', p.hasLevels ? 'Открыть ▶' : 'не инициализирован'));
    row.title = p.hasLevels
      ? `Открыть ${p.id}`
      : `${p.id}: нет web3d/levels.json — нужно разложить three.js-стек`;
    row.onclick = () => openProject(p.id);
    box.appendChild(row);
  }
  const hint = $('projHint');
  if (hint) {
    hint.textContent = `${state.projects.length} проект(ов) в ${state.engineRoot}`
      + ' · после выбора уровни, ассеты и игра инициализируются заново';
  }
}

/* -------------------------------------------------------------- действия */

async function openProject(id) {
  if (!id) return;
  // Папка в projects/three/ может быть просто пустой (создана вручную).
  // Без web3d/levels.json app.js упрётся в 404 манифеста и покажет пустой
  // «сломанный» кадр — честнее сразу объяснить, что делать.
  const p = state.projects.find((x) => x.id === id);
  if (p && !p.hasLevels) {
    flashHint(`${p.id}: нет web3d/levels.json. Разложите стек командой `
      + 'cmd\\init.cmd <папка> --engine threejs — или создайте новый проект ниже.');
    const sel = $('projSel');
    if (sel) sel.value = state.active || '';
    return;
  }
  log('открываю проект ' + id);
  try {
    const r = await fetch('/__open', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ project: id }),
    });
    const j = await r.json();
    if (!j.ok) { log('проект не открыт: ' + (j.error || r.status), 'err'); return; }
    // Перезагрузка — это и есть «полная инициализация»: уровни, оверлеи
    // правок, ассеты, iframe игры и GLB-вьюер читают корень сервера в
    // разных местах, и подменять его на лету было бы нечестно.
    location.reload();
  } catch (e) {
    log('переключение проекта: ' + e.message, 'err');
  }
}

async function closeProject() {
  try {
    const r = await fetch('/__close', { method: 'POST' });
    const j = await r.json();
    if (!j.ok) { log('не удалось закрыть проект', 'err'); return; }
    location.reload();
  } catch (e) {
    log('закрытие проекта: ' + e.message, 'err');
  }
}

/**
 * Новый проект из UI: папка в projects/three/<имя> + ПОЛНАЯ инициализация.
 * Сервер зовёт канонический tools/project_init.py (тот же, что cmd\init.cmd),
 * поэтому новый проект получает ровно тот же стек, что и остальные: vendor/,
 * scene.js, levels.json, level.json, engine.json, линтер, профиль движка.
 * Второго «скелетного» кода в студии нет и быть не должно.
 */
async function createProject() {
  const inp = $('projNewName');
  const name = (inp?.value || '').trim();
  if (!name) { flashHint('Введите имя новой папки проекта, например my_game.'); inp?.focus(); return; }
  if (!/^[A-Za-z0-9_-]+$/.test(name)) {
    flashHint('Имя папки: только латинские буквы, цифры, «_» и «-», без пробелов и путей.');
    inp?.focus();
    return;
  }
  const btn = $('projNew');
  if (btn) { btn.disabled = true; btn.textContent = 'создаю…'; }
  log(`создаю проект three/${name}`);
  try {
    const r = await fetch('/__new', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ name }),
    });
    const j = await r.json();
    if (!j.ok) {
      flashHint(j.error || 'не удалось создать проект');
      log('создание проекта: ' + (j.error || r.status), 'err');
      if (btn) { btn.disabled = false; btn.textContent = '+ Создать и открыть'; }
      return;
    }
    log('проект создан: ' + j.project + ' — открываю');
    await openProject(j.project);
  } catch (e) {
    log('создание проекта: ' + e.message, 'err');
    flashHint('создание проекта: ' + e.message);
    if (btn) { btn.disabled = false; btn.textContent = '+ Создать и открыть'; }
  }
}

function wire() {
  if ($('projClose')) $('projClose').onclick = closeProject;
  if ($('projRefresh')) $('projRefresh').onclick = async () => {
    await readProjects(); renderSelect(); renderOverlay();
  };
  if ($('projNew')) $('projNew').onclick = createProject;
  if ($('projNewName')) $('projNewName').onkeydown = (e) => {
    if (e.key === 'Enter') createProject();
  };
  if ($('projDismiss')) $('projDismiss').onclick = () => {
    if (state.active) { const ov = $('projOverlay'); if (ov) ov.hidden = true; }
  };
  window.__openProject = openProject;
  window.__closeProject = closeProject;
  window.__newProject = createProject;
  window.__projects = state;
}

/* ------------------------------------------------------------------ старт */

async function main() {
  wire();
  await readProjects();
  if (state.supported) { renderSelect(); renderOverlay(); }

  // Отладочный доступ и для пустой студии: гейты не должны зависеть от того,
  // загрузился ли тяжёлый редактор. app.js перекроет __studio/__ready сам.
  window.__studio = window.__studio || state;
  window.__ready = true;

  if (state.hub && state.supported) {
    log(`пустая студия: ${state.projects.length} проект(ов) на выбор`);
    const gp = $('gamepath');
    if (gp) gp.textContent = 'проект не выбран';
    return;                 // НЕ грузим app.js — у него нет проекта
  }
  log(state.active ? 'проект: ' + state.active : 'обычный режим, проект задан снаружи');
  try {
    await import('./app.js');
  } catch (e) {
    log('редактор не загрузился: ' + e.message, 'err');
    console.error('[launcher] app.js:', e);
  }
}

main();
