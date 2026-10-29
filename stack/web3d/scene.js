/*
 * scene.js — построитель сцены уровня по данным level.json.
 *
 * Данные берутся из level.json (исходник — он сам; правки руками кладёт
 * tools/level_apply.py), поэтому сцена всегда соответствует файлу: меняешь
 * уровень в редакторе — сцена строится из тех же чисел.
 *
 * Система координат уровня: x вправо, y ВНИЗ (так числа в level.json читаются
 * глазами), z_index = порядок отрисовки. three.js: y вверх. Перевод делается
 * ровно в одном месте — при выставлении позиции узла: three.y = -level.y. Знак
 * scale при этом НЕ меняется: если родитель имеет scale.y = s, то в перевёрнутой
 * системе это тот же s (минус на позиции и минус на локальной координате ребёнка
 * дают плюс). Текстуры не переворачиваются: у PlaneGeometry v=1 сверху, а three
 * по умолчанию грузит текстуры с flipY=true, т.е. верх картинки оказывается
 * сверху плоскости.
 */
import * as THREE from './vendor/three.module.js';

// Размер виртуального кадра. Числа приходят из самого уровня (`project.viewport`),
// а не из константы: пока они лежали в коде, второй экземпляр мог разойтись с
// данными. Значения по умолчанию совпадают с прежними, так что уровень без
// `project` ведёт себя как раньше.
const BASE_W_DEFAULT = 1280;
const BASE_H_DEFAULT = 720;
let BASE_W = BASE_W_DEFAULT;
let BASE_H = BASE_H_DEFAULT;
const TEX_ROOT = '../';  // level.json хранит пути от корня проекта

// Глубина по z для 2.5D-режима. В ортокамере важен только порядок, но при
// включённом перспективном режиме это уже настоящий объём.
function layerDepth(name, scrollScale) {
  if (scrollScale !== undefined) return -(1 - scrollScale) * 4000;  // Parallax2D
  switch (name) {
    case 'Backdrop': return -10000;
    case 'GameplayLayer':
    case 'GameplayLayer2': return -800;
    case 'Platforms': return -600;
    case 'Props2': return -400;
    case 'Player':
    case 'EnemyLeft':
    case 'Boss': return 0;
    default: return -100;
  }
}

// Числа цвета в level.json записаны прямо в sRGB (как их видно в исходнике),
// а three по умолчанию трактует числа Color как ЛИНЕЙНЫЕ. Без
// setRGB(..., SRGBColorSpace) значение уезжает: 0.278 в файле выводится как
// 0.565 (144/255 вместо 71/255) — серый Backdrop светлеет вдвое.
function srgb(r, g, b) {
  return new THREE.Color().setRGB(r, g, b, THREE.SRGBColorSpace);
}

/** Обход дерева узлов level.json. */
export function find(node, pred) {
  if (pred(node)) return node;
  for (const c of node.children || []) {
    const r = find(c, pred);
    if (r) return r;
  }
  return null;
}

export class LevelScene {
  constructor(level) {
    this.level = level;
    // Размер виртуального кадра берём из данных уровня. Один экземпляр на всю
    // сцену: раньше это была константа модуля, и второй уровень с другим
    // viewport переопределил бы размер для уже построенной сцены.
    const vp = level.project && level.project.viewport;
    if (Array.isArray(vp) && vp.length >= 2) {
      BASE_W = vp[0];
      BASE_H = vp[1];
    } else {
      BASE_W = BASE_W_DEFAULT;
      BASE_H = BASE_H_DEFAULT;
    }
    this.textures = {};
    this.frames = {};        // "player" -> {anim: {frames, loop, speed, textures}}
    this.sprites = [];       // анимированные: {mesh, def, anim, t}
    this.parallax = [];      // {group, scaleX, repeat, base}
    this.collisions = [];    // debug-объекты
    this.camX = 0;
    this.camY = 0;
    this.viewW = BASE_W;
    this.viewH = BASE_H;
    this.showCollisions = false;
    this.parallaxOn = true;
    this.autoWalk = true;
    this.walkX = 0;
    this.clock = new THREE.Clock();
    this.ready = false;

    this.scene = new THREE.Scene();
    this.scene.background = srgb(...level.project.clear_color.slice(0, 3));

    this.root = new THREE.Group();
    this.scene.add(this.root);

    // камера: ортографическая по умолчанию (1:1 к координатам уровня),
    // перспективная — обзор
    this.orthoCam = new THREE.OrthographicCamera(-1, 1, 1, -1, 0.1, 40000);
    this.perspCam = new THREE.PerspectiveCamera(50, 1, 1, 40000);
    this.camera = this.orthoCam;
    this.mode = 'ortho';
    this.orbit = { az: 0, el: 0, dist: 2600 };
  }

  // ------------------------------------------------------------- загрузка
  async load(onProgress) {
    const mgr = new THREE.LoadingManager();
    const loader = new THREE.TextureLoader(mgr);
    const paths = Object.keys(this.level.textures);
    const total = paths.length + Object.keys(this.level.frames).length;
    let done = 0;
    const tick = () => { done++; onProgress?.(done, total); };

    await Promise.all(paths.map((p) => new Promise((res) => {
      loader.load(TEX_ROOT + p, (tex) => {
        tex.colorSpace = THREE.SRGBColorSpace;
        tex.minFilter = THREE.LinearMipmapLinearFilter;
        tex.magFilter = THREE.LinearFilter;
        tex.anisotropy = 4;
        this.textures[p] = tex;
        tick(); res();
      }, undefined, () => { tick(); res(); });
    })));

    for (const [key, anims] of Object.entries(this.level.frames)) {
      const out = {};
      for (const [name, def] of Object.entries(anims)) {
        out[name] = { ...def, textures: [] };
        for (const f of def.frames) {
          await new Promise((res) => loader.load(TEX_ROOT + f, (tex) => {
            tex.colorSpace = THREE.SRGBColorSpace;
            tex.minFilter = THREE.LinearMipmapLinearFilter;
            tex.magFilter = THREE.LinearFilter;
            out[name].textures.push(tex); res();
          }, undefined, () => res()));
        }
      }
      this.frames[key] = out;
      tick();
    }

    this.build();
    this.ready = true;
  }

  // -------------------------------------------------------------- сборка
  build() {
    // лимиты Camera2D ищем в дереве: они лежат на узле игрока
    const cam = find(this.level.tree, (n) => n.type === 'Camera2D');
    if (cam?.props?.limits) {
      const L = cam.props.limits;
      this.cameraLimits = { left: L.limit_left, top: L.limit_top,
                            right: L.limit_right, bottom: L.limit_bottom };
      this.cameraOffset = cam.props.offset || [0, 0];
    }
    const player = find(this.level.tree, (n) => n.name === 'Player' && n.props?.position);
    this.playerStart = player?.props.position || [40, 464];

    this.buildNode(this.level.tree, this.root, -100);
    this.focusX = this.playerStart[0];
    this.rawX = this.playerStart[0];
    const c = this.clampCamera(this.playerStart[0], this.playerStart[1]);
    this.camX = c[0];
    this.camY = c[1];
  }

  buildNode(node, parentObj, parentDepth, prefix = '') {
    const p = node.props || {};
    let depth = parentDepth + (p.z_index ?? 0);

    // корневые узлы задают «слой»
    if (parentObj === this.root) {
      depth = layerDepth(node.name, p.scroll_scale?.[0]);
    }

    const isParallax = node.type === 'Parallax2D';

    // Полный путь узла. Нужен там, где имя не уникально: у Player, EnemyLeft и
    // Boss ребёнок называется одинаково — «Sprite», и по имени их не различить.
    // node.path есть только у узлов, которым его проставил нормализатор уровня;
    // у прочих детей он пуст, поэтому путь достраивается по дереву.
    const path = node.path || (prefix ? prefix + '/' + node.name : node.name);

    const obj = new THREE.Group();
    obj.name = path;
    obj.userData.node = node;
    obj.userData.path = path;
    if (p.position) obj.position.set(p.position[0], -p.position[1], depth);
    else obj.position.set(0, 0, depth);
    if (p.scale) obj.scale.set(p.scale[0], p.scale[1], 1);

    parentObj.add(obj);

    if (isParallax) {
      // Контент слоя строится один раз в content, дальше размножается по
      // repeat_size — так же, как это делает Parallax2D с repeat_times.
      const s = p.scroll_scale?.[0] ?? 1;
      const sy = p.scroll_scale?.[1] ?? 0;
      const repeat = p.repeat_size?.[0] ?? 0;
      const times = p.repeat_times ?? 1;
      const content = new THREE.Group();
      obj.add(content);
      this.buildVisual(node, content, depth);
      for (const child of node.children) this.buildNode(child, content, depth, path);
      const tiles = new Map();   // k -> группа-плитка, нужна сектору 2
      if (repeat > 0) {
        for (let k = -times; k <= times; k++) {
          if (k === 0) continue;
          const tile = content.clone(true);
          tile.position.x = k * repeat;
          tile.userData.k = k;
          obj.add(tile);
          tiles.set(k, tile);
        }
      }
      this.parallax.push({ group: obj, scaleX: s, scaleY: sy, repeat, times,
                           content, tiles, name: node.name });
      return obj;
    }

    // сам узел может что-то рисовать
    this.buildVisual(node, obj, depth);

    for (const child of node.children) this.buildNode(child, obj, depth, path);

    return obj;
  }

  buildVisual(node, obj, depth) {
    const p = node.props || {};

    if (node.type === 'Sprite2D' && p.texture) {
      const tex = this.textures[p.texture];
      const size = this.level.textures[p.texture];
      if (!tex || !size) return;
      // offset — в ЛОКАЛЬНЫХ единицах спрайта, масштаб к нему применяет уже
      // сам узел (obj.scale). Предумножать здесь на s нельзя: получилось бы
      // offset * s^2. У всех спрайтов level_0 offset нулевой, поэтому правка
      // ничего не сдвигает; на новых спрайтах (враг level_1 с offset = -H/2,
      // чтобы origin был на ступнях) без неё спрайт уезжает вверх в k раз.
      const off = p.offset || [0, 0];
      const mesh = new THREE.Mesh(
        new THREE.PlaneGeometry(size[0], size[1]),
        new THREE.MeshBasicMaterial({
          map: tex, transparent: true, depthWrite: false,
          side: THREE.DoubleSide, alphaTest: 0.004,
        }));
      mesh.scale.set(p.flip_h ? -1 : 1, p.flip_v ? -1 : 1, 1);
      mesh.position.set(off[0], -off[1], 0.01);
      mesh.renderOrder = depth;
      obj.add(mesh);
      return;
    }

    if (node.type === 'AnimatedSprite2D' && p.frames) {
      const def = this.frames[p.frames];
      if (!def) return;
      const animName = p.animation || p.autoplay || Object.keys(def)[0];
      const anim = def[animName] || def[Object.keys(def)[0]];
      if (!anim || !anim.textures.length) return;
      const tex = anim.textures[0];
      const img = tex.image;
      const mesh = new THREE.Mesh(
        new THREE.PlaneGeometry(img.width, img.height),
        new THREE.MeshBasicMaterial({
          map: tex, transparent: true, depthWrite: false,
          side: THREE.DoubleSide, alphaTest: 0.004,
        }));
      const off = p.offset || [0, 0];
      mesh.position.set(off[0], -off[1], 0.01);
      mesh.renderOrder = depth;
      obj.add(mesh);
      this.sprites.push({ mesh, def, animName, t: 0, key: obj.userData.path });
      return;
    }

    if (node.type === 'ColorRect' && p.color && p.rect) {
      const [l, t, r, b] = p.rect;
      const w = r - l, h = b - t;
      const c = p.color;
      const mesh = new THREE.Mesh(
        new THREE.PlaneGeometry(w, h),
        new THREE.MeshBasicMaterial({
          color: srgb(c[0], c[1], c[2]), transparent: c[3] < 1,
          opacity: c[3], depthWrite: false,
        }));
      mesh.position.set(l + w / 2, -(t + h / 2), 0);
      mesh.renderOrder = depth;
      obj.add(mesh);
      return;
    }

    // отладочная геометрия столкновений
    if (node.type === 'CollisionShape2D' && p.shape?.size) {
      const [w, h] = p.shape.size;
      const pos = p.position || [0, 0];
      const line = new THREE.Line(
        new THREE.BufferGeometry().setFromPoints([
          new THREE.Vector3(-w / 2, -h / 2, 0), new THREE.Vector3(w / 2, -h / 2, 0),
          new THREE.Vector3(w / 2, h / 2, 0), new THREE.Vector3(-w / 2, h / 2, 0),
          new THREE.Vector3(-w / 2, -h / 2, 0),
        ]),
        new THREE.LineBasicMaterial({ color: 0x39ff88, transparent: true, opacity: 0.85,
          depthTest: false }));
      line.position.set(pos[0], -pos[1], 0.02);
      line.renderOrder = 9999;
      line.visible = this.showCollisions;
      obj.add(line);
      this.collisions.push(line);
      return;
    }

    if (node.type === 'CollisionPolygon2D' && p.polygon) {
      const pts = [];
      for (let i = 0; i + 1 < p.polygon.length; i += 2) {
        pts.push(new THREE.Vector3(p.polygon[i], -p.polygon[i + 1], 0));
      }
      if (pts.length) pts.push(pts[0].clone());
      const line = new THREE.Line(
        new THREE.BufferGeometry().setFromPoints(pts),
        new THREE.LineBasicMaterial({ color: 0xffd166, transparent: true, opacity: 0.9,
          depthTest: false }));
      line.renderOrder = 9999;
      line.visible = this.showCollisions;
      obj.add(line);
      this.collisions.push(line);
    }
  }

  // -------------------------------------------------------- сектор 2
  /**
   * Продолжение уровня новыми слоями.
   *
   * Механика: у параллакс-слоя есть content (нулевая плитка) и плитки-клоны
   * с шагом repeat_size. Чётные k оставляем как есть, нечётные подменяем на
   * новый арт — по мере ходьбы фон чередуется через один repeat. Геометрия
   * (масштаб, высота, глубина) не меняется: новый слой рисуется той же кистью,
   * что и старый, иначе стык на repeat_size будет видно.
   *
   * Материалы у клонов общие (Object3D.clone делит материал), поэтому перед
   * подменой текстуры материал клонируется — иначе перекрасились бы все плитки.
   *
   * @returns {Promise<{far:boolean, mid:boolean, gameplay:number}>}
   */
  async applySector2(spec) {
    const loader = new THREE.TextureLoader();
    const load = (rel) => new Promise((res) => {
      loader.load(TEX_ROOT + rel, (t) => {
        t.colorSpace = THREE.SRGBColorSpace;
        t.minFilter = THREE.LinearMipmapLinearFilter;
        t.magFilter = THREE.LinearFilter;
        t.anisotropy = 4;
        res(t);
      }, undefined, () => res(null));
    });
    const out = { far: false, mid: false, gameplay: 0 };

    for (const key of ['far', 'mid']) {
      const part = spec[key];
      if (!part) continue;
      const tex = await load(part.texture);
      if (!tex) continue;
      // слой ищем по scroll_scale: он однозначен (0.25 - far, 0.5 - mid),
      // а имена узлов могут поменяться.
      const layer = this.parallax.find((p) => p.scaleX === (key === 'far' ? 0.25 : 0.5));
      if (!layer) continue;
      for (const [k, tile] of layer.tiles) {
        if (k % 2 === 0) continue;
        tile.traverse((o) => {
          if (!o.isMesh) return;
          o.material = o.material.clone();
          o.material.map = tex;
          o.material.needsUpdate = true;
        });
      }
      out[key] = true;
    }

    const gp = spec.gameplay;
    if (gp) {
      const tex = await load(gp.texture);
      if (tex) {
        const img = tex.image;
        const size = this.level.textures[Object.keys(this.level.textures)
          .find((p) => p.endsWith('/gameplay_layer.png'))] || [img.width, img.height];
        for (const x of gp.slots) {
          const mesh = new THREE.Mesh(
            new THREE.PlaneGeometry(size[0], size[1]),
            new THREE.MeshBasicMaterial({ map: tex, transparent: true,
              depthWrite: false, side: THREE.DoubleSide, alphaTest: 0.004 }));
          mesh.position.set(x, -gp.y, gp.depth);
          mesh.scale.set(gp.scale[0], gp.scale[1], 1);
          mesh.renderOrder = gp.depth;
          this.root.add(mesh);
          out.gameplay++;
        }
      }
    }

    if (spec.camera_limit_right) this.cameraLimits.right = spec.camera_limit_right;
    if (spec.walk_max) this.walkMax = spec.walk_max;
    return out;
  }

  // --------------------------------------------------------------- кадры
  setCollisions(on) {
    this.showCollisions = on;
    for (const l of this.collisions) l.visible = on;
  }

  // -------------------------------------------------------- размер окна
  resize(w, h) {
    const scale = Math.min(w / BASE_W, h / BASE_H);
    this.viewW = w / scale;
    this.viewH = h / scale;
    this.orthoCam.left = -this.viewW / 2;
    this.orthoCam.right = this.viewW / 2;
    this.orthoCam.top = this.viewH / 2;
    this.orthoCam.bottom = -this.viewH / 2;
    this.orthoCam.updateProjectionMatrix();
    this.perspCam.aspect = w / h;
    this.perspCam.updateProjectionMatrix();
  }

  // -------------------------------------------------------------- камера
  /**
   * Лимиты камеры уровня (узел Camera2D в дереве).
   *
   * ВАЖНО: лимиты клампят позицию САМОГО УЗЛА камеры (для DRAG_CENTER это
   * центр кадра), а `offset` прибавляется ПОСЛЕ клампа — поэтому offset
   * способен вытолкнуть кадр за лимиты. Это прямо задокументировано в
   * Camera2D.offset ("offset can push the view past the limit").
   *
   * Проверено пробой: при любом Y игрока центр кадра равен
   * clamp(player.y, 487, 487) + (-180) = 307, т.е. видно y от -53 до 667,
   * а не 127..847, как получается при клампе уже сдвинутого кадра.
   */
  clampCamera(x, y) {
    const lim = this.cameraLimits || { left: -108, top: 127, right: 3658, bottom: 847 };
    const off = this.cameraOffset || [0, -180];
    const hw = this.viewW / 2, hh = this.viewH / 2;
    const minX = lim.left + hw, maxX = lim.right - hw;
    const minY = lim.top + hh, maxY = lim.bottom - hh;
    const cx = minX <= maxX ? Math.min(Math.max(x, minX), maxX) : (minX + maxX) / 2;
    const cy = minY <= maxY ? Math.min(Math.max(y, minY), maxY) : (minY + maxY) / 2;
    return [cx + off[0], cy + off[1]];
  }

  update(dt) {
    if (!this.ready) return;

    // --- анимации спрайтов (скорость из SpriteFrames: fps).
    // speedScale — надстройка играбельного слоя: шаг должен следовать за
    // скоростью, иначе ноги «скользят» по земле (множитель скорости кадров
    // анимации ходьбы).
    for (const s of this.sprites) {
      const a = s.def[s.animName];
      if (!a || a.textures.length < 2) continue;
      s.t += dt * a.speed * (s.speedScale ?? 1);
      const idx = Math.floor(s.t) % a.textures.length;
      const tex = a.textures[idx];
      if (s.mesh.material.map !== tex) {
        s.mesh.material.map = tex;
        s.mesh.material.needsUpdate = true;
      }
    }

    // --- камера: сглаживание -> кламп по лимитам -> offset
    if (this.autoWalk) {
      this.walkX += dt * 190;
      if (this.walkX > (this.walkMax ?? 3560)) this.walkX = 20;
    }
    const px = this.autoWalk ? this.walkX : this.focusX;
    const py = this.playerStart ? this.playerStart[1] : 464;
    const k = 1 - Math.exp(-6.0 * dt);   // position_smoothing_speed = 6.0
    this.rawX = this.rawX === undefined ? px : this.rawX + (px - this.rawX) * k;
    const target = this.clampCamera(this.rawX, py);
    this.camX = target[0];
    this.camY = target[1];

    // --- параллакс.
    // Правило слоя с scroll_scale (проверено пробой):
    //     позиция_слоя = (1 - scroll_scale) * (центр_камеры - полвьюпорта)
    // по ОБЕИМ осям. То есть scroll_scale = 1 -> слой лежит в мире как есть,
    // scroll_scale = 0 -> слой прибит к экрану, а его локальные координаты
    // становятся экранными (offset от верхнего левого угла кадра).
    // В three.y = -y_уровня, поэтому знак Y переворачивается.
    const frameL = this.camX - this.viewW / 2;
    const frameT = this.camY - this.viewH / 2;
    for (const pl of this.parallax) {
      if (!this.parallaxOn) { pl.group.position.set(0, 0, pl.group.position.z); continue; }
      pl.group.position.x = (1 - pl.scaleX) * frameL;
      pl.group.position.y = -(1 - pl.scaleY) * frameT;
    }

    // --- позиция камеры
    if (this.mode === 'ortho') {
      this.orthoCam.position.set(this.camX, -this.camY, 6000);
      this.orthoCam.lookAt(this.camX, -this.camY, 0);
    } else {
      const d = this.orbit.dist;
      const el = this.orbit.el, az = this.orbit.az;
      const cx = this.camX, cy = -this.camY;
      this.perspCam.position.set(
        cx + Math.sin(az) * Math.cos(el) * d,
        cy + Math.sin(el) * d,
        Math.cos(az) * Math.cos(el) * d);
      this.perspCam.lookAt(cx, cy, 0);
    }
  }

  setMode(mode) {
    this.mode = mode;
    this.camera = mode === 'ortho' ? this.orthoCam : this.perspCam;
    if (mode === 'persp') {
      // Дистанцию берём от ширины кадра: у уровня длина 3700 юнитов, и на
      // фиксированных 2200 в кадр влезает только середина.
      this.orbit.az = 0.42;
      this.orbit.el = 0.30;
      this.orbit.dist = Math.max(2600, this.viewW * 1.9);
    }
  }
}
