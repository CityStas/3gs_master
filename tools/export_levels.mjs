#!/usr/bin/env node
/*
 * export_levels.mjs — единственный мост между игрой и студией.
 *
 * ПРОБЛЕМА, которую он решает. В проекте было ДВА уровня «по факту»:
 *   * игра грузит `web3d/levels.js` (LEVELS.canyon / LEVELS.house) — там все
 *     спрайты, параллакс, коллайдеры, пикапы, враги;
 *   * студия грузила `web3d/level.json` — отдельную заглушку из пяти
 *     ColorRect («пол, две платформы, палочка»). К игре она не имела
 *     отношения, поэтому в редакторе не было ниArt, ни слоёв, ни второго
 *     уровня, а правки не попадали в игру.
 *
 * РЕШЕНИЕ. `levels.js` остаётся ИСТОЧНИКОМ ИСТИНЫ. Скрипт разворачивает его
 * в `web3d/level_<id>.json` — тот формат, который понимает scene.js
 * (ступени Godot-like дерева узлов) — и прописывает оба уровня в манифест
 * `web3d/levels.json`. Студия показывает НАСТОЯЩУЮ геометрию, разбитую по
 * слоям как в Godot: Фон / Пол / Платформы / Декор / Объекты / Пикапы /
 * Враги / Духи / Игрок / Коллайдеры.
 *
 * Правки из студии идут не в эти файлы, а в `level_<id>_edit.json`; их
 * накладывает сама игра при старте (web3d/level_overlay.js). Поэтому
 * перегенерировать JSON после ручной правки безопасно: правки не теряются.
 *
 *     node tools/export_levels.mjs projects/three/my_game   # явный проект
 *     node tools/export_levels.mjs                          # активный проект из data/active_project.txt
 *
 * Жёстко зашитого «проекта по умолчанию» нет: в репозитории не лежит ни одной
 * игры, и скрипт одинаково работает с любым three.js-проектом, у которого
 * есть web3d/levels.js.
 *
 * Важная деталь про глубину. scene.js для КОРНЕВОГО узла считает
 * `layerDepth('Main') = -100`, а дальше прибавляет z_index каждого ребёнка.
 * Итоговый renderOrder в игре — просто `s.z`. Поэтому у каждого спрайта
 * z_index = s.z + 100: -100 (корень) + 0 (слой) + (s.z + 100) = s.z.
 * Без этой поправки арт и платформы поменялись бы местами на глазах.
 */
import fs from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';

const REPO = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');

/** Проект без аргумента берём из того же указателя, что читают лаунчеры.
 *  Проверяем и границы репозитория, и наличие levels.js: мёртвый указатель
 *  не должен молча отправить скрипт в чужой каталог. */
async function activeGame() {
  try {
    const rel = (await fs.readFile(path.join(REPO, 'data/active_project.txt'), 'utf8')).trim();
    if (!rel) return null;
    const p = path.resolve(REPO, rel);
    if (!p.startsWith(REPO + path.sep)) return null;
    if ((await fs.stat(path.join(p, 'web3d/levels.js'))).isFile()) return p;
  } catch { /* указателя нет или levels.js отсутствует */ }
  return null;
}

const picked = process.argv[2] || await activeGame();
if (!picked) {
  console.error('Укажите three.js-проект: node tools/export_levels.mjs projects/three/<имя>');
  console.error('Или задайте активный проект: dev.cmd <имя> (пишет data/active_project.txt).');
  process.exit(2);
}
const game = path.resolve(picked);
const web3d = path.join(game, 'web3d');
const { LEVELS, T, VIEW } = await import(pathToFileURL(path.join(web3d, 'levels.js')).href);

const texKey = (t) => 'res/' + t[0];
/** Имя узла: NO_EDIT в leveledit.js запрещает ровно эти имена ЦЕЛИКОМ. */
const NO_EDIT = /^(Backdrop|GameplayLayer\d*|Terrain\d*|WallLeft|WallRight|Ceiling|Strip)$/;
const safeName = (n) => (NO_EDIT.test(n) ? 'Obj_' + n : n);

function builder(id, L) {
  const textures = {};
  const meta = {};
  const groups = new Map();

  const addTex = (t) => { textures[texKey(t)] = [t[1], t[2]]; return texKey(t); };

  function put(layer, node, m) {
    if (!groups.has(layer)) groups.set(layer, []);
    groups.get(layer).push(node);
    meta[node.path] = m;
    return node;
  }

  /** Спрайт с сохранением всех полей, нужных игре при наложении правок. */
  function sprite(layer, p, t, x, y, sx = 1, sy = sx, z = 0, extra = {}) {
    const key = addTex(t);
    return put(layer, {
      type: 'Sprite2D',
      name: safeName(p),
      path: p,
      props: {
        position: [x, y],
        scale: [sx, sy],
        texture: key,
        offset: [extra.ox || 0, extra.oy || 0],
        flip_h: !!extra.flipH,
        // +100 компенсирует layerDepth('Main') = -100 в scene.js
        z_index: z + 100,
      },
      children: [],
    }, extra.meta);
  }

  // ------------------------------------------------------------- параллакс
  L.parallax.forEach((p, pi) => {
    p.sprites.forEach((s, si) => {
      sprite('Фон', `Bg_${pi}_${si}`, s.tex, s.x, s.y,
        s.sx ?? 1, s.sy ?? s.sx ?? 1, p.z,
        { flipH: s.flipH, meta: { kind: 'parallax', pi, si } });
    });
  });

  // -------------------------------------------------------------- спрайты
  L.sprites.forEach((s, i) => {
    let layer = 'Объекты';
    if (/^JumpSpot/.test(s.name)) layer = 'Платформы';
    else if (/^Island/.test(s.name)) layer = 'Пол';
    else if (/^Strip/.test(s.name)) layer = 'Пол';
    else if (/^Decor/.test(s.name)) layer = 'Декор';
    sprite(layer, s.name, s.tex, s.x, s.y, s.sx ?? 1, s.sy ?? s.sx ?? 1, s.z,
      { flipH: s.flipH, oy: s.oy || 0, meta: { kind: 'sprite', index: i } });
  });

  // ------------------------------------------------------------ коллайдеры
  L.colliders.forEach((r, i) => {
    const cx = (r.x1 + r.x2) / 2, cy = (r.y1 + r.y2) / 2;
    // В .tscn площадки-ловушки — это коллайдеры 5..8; имя должно совпадать
    // с JumpSpotN, иначе leveledit.js не свяжет пару «спрайт ↔ коллайдер».
    let p = `Collider_${i}`;
    if (id === 'canyon' && i >= 5 && i <= 8) p = `JumpSpotPlatform${i - 4}`;
    put('Коллайдеры', {
      type: 'CollisionShape2D',
      name: safeName(p),
      path: p,
      props: {
        position: [cx, cy],
        shape: { size: [r.x2 - r.x1, r.y2 - r.y1] },
        z_index: 0,
      },
      children: [],
    }, { kind: 'collider', index: i });
  });

  // Полигоны рельефа — только отладочная обводка, не правимый узел.
  (L.groundPolys || []).forEach((poly, i) => {
    const flat = [];
    for (const [x, y] of poly) flat.push(x, y);
    const n = {
      type: 'CollisionPolygon2D',
      name: `GroundPoly_${i}`,
      path: `GroundPoly_${i}`,
      props: { polygon: flat },
      children: [],
    };
    if (!groups.has('Коллайдеры')) groups.set('Коллайдеры', []);
    groups.get('Коллайдеры').push(n);
  });

  // --------------------------------------------------------------- пикапы
  L.pickups.forEach((u, i) => {
    const t = u.kind === 'ammo' ? T.ammo : T.happy;
    sprite('Пикапы', `Pickup_${i}`, t, u.x, u.y, u.sx ?? 1, u.sx ?? 1, u.z,
      { oy: u.oy || 0, meta: { kind: 'pickup', index: i } });
  });

  // ---------------------------------------------------------------- враги
  L.enemies.forEach((e, i) => {
    sprite('Враги', `Enemy_${i}`, T.enemy, e.x, e.y, 1, 1, 0,
      { meta: { kind: 'enemy', index: i } });
  });
  if (L.boss) {
    sprite('Враги', 'Boss', T.boss, L.boss.x, L.boss.y, 1, 1, 0,
      { meta: { kind: 'boss' } });
  }
  L.spirits.forEach((s, i) => {
    sprite('Духи', `Spirit_${i}`, T.wraith, s.x, s.y, 1, 1, -20,
      { meta: { kind: 'spirit', index: i } });
  });

  // ---------------------------------------------------------------- игрок
  const player = sprite('Игрок', 'Player', T.wizardIdle,
    L.spawn.x, L.spawn.y, 1, 1, 10, { meta: { kind: 'spawn' } });
  // Camera2D нужен scene.js: он читает отсюда лимиты камеры и playerStart.
  player.children.push({
    type: 'Camera2D', name: 'Camera2D', path: 'Player/Camera2D',
    props: {
      limits: { limit_left: -108, limit_top: -9999,
        limit_right: 3658, limit_bottom: 9999 },
      offset: [0, 0],
    },
    children: [],
  });

  // --------------------------------------------------------------- дерево
  // Порядок слоёв = порядок в дереве Godot, а не алфавитный.
  const LAYER_ORDER = ['Фон', 'Пол', 'Платформы', 'Декор', 'Объекты',
    'Коллайдеры', 'Пикапы', 'Враги', 'Духи', 'Игрок'];
  const children = LAYER_ORDER.filter((l) => groups.has(l)).map((l) => ({
    type: 'Node2D', name: l, path: `Layer/${l}`, props: {}, children: groups.get(l),
  }));

  return {
    project: {
      name: path.basename(game),
      viewport: [VIEW.w, VIEW.h],
      clear_color: [...L.backdrop, 1],
    },
    textures,
    frames: {},
    tree: {
      type: 'Node2D', name: 'Main', path: 'Main', props: {}, children,
    },
    // Карта «путь узла -> что именно в LEVELS надо подвинуть». Без неё игра
    // не знала бы, что Collider_7 — это седьмой прямоугольник, а JumpSpot3 —
    // третий спрайт, и правки из студии не доезжали бы до геймплея.
    studio: { id, paths: meta, textureRoot: 'res/' },
  };
}

function manifestEntry(id, L, file) {
  return {
    file,
    editable: true,
    builder: 'level_overlay',     // правки накладывает игра при старте
    title: id === 'canyon' ? 'LEVEL 1 · Каньон' : (id === 'house' ? 'LEVEL 2 · Дом' : id),
    subtitle: L.objective || '',
    objective: L.objective || '',
    door: L.door ? { x: L.door.x, y: L.door.y, half: L.door.half, gate: '' }
      : (L.gate ? { x: L.gate.x, y: L.gate.y, half: L.gate.half, gate: '' } : { x: 0, y: 0, half: 64, gate: '' }),
    fall_y: L.fallY ?? 780,
    next: L.next || '',
  };
}

const ids = Object.keys(LEVELS);
const levels = {};
for (const id of ids) {
  const file = `level_${id}.json`;
  const json = builder(id, LEVELS[id]);
  await fs.writeFile(path.join(web3d, file),
    JSON.stringify(json, null, 1) + '\n', 'utf8');
  levels[id] = manifestEntry(id, LEVELS[id], file);
  const nSprites = Object.keys(json.studio.paths).length;
  console.log(`${file}: ${nSprites} узлов, ${Object.keys(json.textures).length} текстур, ` +
    `${json.tree.children.length} слоёв`);
}

const mfPath = path.join(web3d, 'levels.json');
let mf = {};
try { mf = JSON.parse(await fs.readFile(mfPath, 'utf8')); } catch { /* нет манифеста */ }
mf._comment = 'Манифест уровней. Сгенерирован tools/export_levels.mjs из web3d/levels.js — '
  + 'это ЕДИНЫЙ источник геометрии. Правки из студии лежат в level_<id>_edit.json '
  + 'и накладываются игрой при старте (web3d/level_overlay.js).';
mf.start = ids[0];
mf.levels = levels;
await fs.writeFile(mfPath, JSON.stringify(mf, null, 1) + '\n', 'utf8');
console.log(`levels.json: ${ids.length} уровня(ей): ${ids.join(', ')}`);
