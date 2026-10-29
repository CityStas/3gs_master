/*
 * glbview.js — 3D-просмотрщик GLB для студии.
 *
 * Зачем отдельный модуль, а не три строки в студии. Просмотрщик решает свою
 * задачу: показать меш и дать на него посмотреть. Это значит камеру-орбиту,
 * свет, сетки и оверлеи (каркас, нормали, UV, вершинные цвета). Студия поверх
 * него решает другую: раскладка панелей, чат, редактор уровня. Смешать их —
 * потерять оба: просмотрщик начнёт зависеть от верстки студии, а студия
 * утонет в настройках света.
 *
 * ── Почему OrbitControls, а не свой поворот мышью ──────────────────────────
 * Свой вращатель уже есть в `scene.js` (перспективный режим), но он заточен
 * под уровень: там камера ходит вокруг точки фокуса уровня и слушается общих
 * клавиш. Вьюеру нужен зум колесом к курсору, панорама средней кнопкой и
 * damping — то есть ровно то, что в OrbitControls отлажено. Писать это заново
 * ради независимости от аддона — обменять отлаженное на своё непроверенное.
 *
 * ── Сетки (что и зачем) ────────────────────────────────────────────────────
 *   * bboxGrid — коробка по габаритам меша с шагом 1 ед. Мера размера: без неё
 *     «большой проп» и «маленький проп» в кадре неотличимы, потому что камера
 *     кадрирует по мешу. Это самая нужная сетка.
 *   * grid — мировая сетка в начале координат (Three GridHelper). Показывает,
 *     где у меша низ и стоит ли он на земле вообще.
 *   * axes — RGB-оси X/Y/Z. Отвечает на вопрос «где тут +Y», то есть куда меш
 *     смотрит вверх.
 *   * wire — каркас поверх меша. Плотность треугольников = «суп или не суп»
 *     (см. MEMORY: здоровый меш V/T ≈ 0.70).
 */
import * as THREE from '../vendor/three.module.js';
import { OrbitControls } from '../vendor/addons/controls/OrbitControls.js';
import { GLTFLoader } from '../vendor/addons/loaders/GLTFLoader.js';

/** Пересчёт габаритов меша в строку «W × H × D». */
export function sizeLine(box) {
  if (!box || box.isEmpty()) return '—';
  const s = box.getSize(new THREE.Vector3());
  return `${s.x.toFixed(2)} × ${s.y.toFixed(2)} × ${s.z.toFixed(2)}`;
}

export class GlbViewer {
  /** @param {HTMLElement} host контейнер под canvas */
  constructor(host) {
    this.host = host;
    this.renderer = new THREE.WebGLRenderer({ antialias: true, alpha: false });
    this.renderer.setPixelRatio(Math.min(devicePixelRatio, 2));
    this.renderer.outputColorSpace = THREE.SRGBColorSpace;
    // ACES-тонмаппинг: без него PBR-материалы из GLB выглядят пересвеченными
    // пятнами, и «нормально ли это» превращается в отдельный разговор. С ним
    // кадр читается как в любом вьюере, и спор идёт о модели, а не о свете.
    this.renderer.toneMapping = THREE.ACESFilmicToneMapping;
    this.renderer.toneMappingExposure = 1.0;
    host.appendChild(this.renderer.domElement);
    this.canvas = this.renderer.domElement;

    this.scene = new THREE.Scene();
    this.scene.background = new THREE.Color(0x14161c);

    this.camera = new THREE.PerspectiveCamera(42, 1, 0.05, 6000);
    this.camera.position.set(6, 4, 8);

    this.controls = new OrbitControls(this.camera, this.canvas);
    this.controls.enableDamping = true;
    this.controls.dampingFactor = 0.08;
    this.controls.zoomSpeed = 0.9;
    // Клик по модели не должен крутить камеру рывком: у OrbitControls это
    // левая кнопка, а нам она нужна под выбор меша. Крутим правой, панорама
    // средней, зум колесом.
    this.controls.mouseButtons = {
      LEFT: THREE.MOUSE.PAN, MIDDLE: THREE.MOUSE.DOLLY, RIGHT: THREE.MOUSE.ROTATE,
    };
    this.controls.touches = { ONE: THREE.TOUCH.ROTATE, TWO: THREE.TOUCH.DOLLY_PAN };

    this._buildLights();

    this.holder = new THREE.Group();     // сюда кладётся загруженная модель
    this.scene.add(this.holder);

    this.helpers = new THREE.Group();    // сетки/оверлеи — отдельно от модели
    this.scene.add(this.helpers);
    this._buildHelpers();

    this.loader = new GLTFLoader();
    this.info = null;                    // { tris, verts, meshes, mats, anims, box }
    this.modelUrl = null;
    this._raf = null;
    this._onResize = () => this.resize();
    addEventListener('resize', this._onResize);
    this.resize();
    this._loop();
  }

  _buildLights() {
    // Три источника, а не один: одна лампа спереди даёт плоский силуэт, и на
    // нём не видно ни формы, ни нормалей. Ключ + контровой + заливка — минимум,
    // на котором объём читается и без HDRI (а HDRI тянуть неоткуда: он был бы
    // ещё одним сетевым ассетом, которого может не оказаться).
    const key = new THREE.DirectionalLight(0xffffff, 2.1);
    key.position.set(5, 8, 6);
    this.scene.add(key);
    const fill = new THREE.DirectionalLight(0x9ec8ff, 0.8);
    fill.position.set(-6, 2, 4);
    this.scene.add(fill);
    const rim = new THREE.DirectionalLight(0xffd9a8, 1.0);
    rim.position.set(-3, 4, -7);
    this.scene.add(rim);
    this.scene.add(new THREE.HemisphereLight(0xbcd4ff, 0x2a2622, 0.55));
  }

  _buildHelpers() {
    this.bboxGrid = new THREE.Box3Helper(new THREE.Box3(), 0x6fd3ff);
    this.bboxGrid.visible = false;
    this.helpers.add(this.bboxGrid);

    // Миллиметровка: 20 ячеек по 1 ед. Мелкий шаг не берём — на мешах в
    // десятки единиц он превращается в серую кашу и перестаёт быть мерой.
    this.grid = new THREE.GridHelper(20, 20, 0x4a5568, 0x2b3242);
    this.grid.material.transparent = true;
    this.grid.material.opacity = 0.55;
    this.grid.visible = false;
    this.helpers.add(this.grid);

    this.axes = new THREE.AxesHelper(2.5);
    this.axes.visible = false;
    this.helpers.add(this.axes);

    // Именованные оси: цвета AxesHelper неочевидны, и без подписи «где +Y»
    // приходится вспоминать. Подписи — плоские плашки, всегда лицом к камере
    // (материал без depth-конфликта, поэтому sprite).
    this.axisLabels = new THREE.Group();
    this.axisLabels.visible = false;
    for (const [txt, col, pos] of [['X', '#ff5a5a', [2.9, 0, 0]],
      ['Y', '#5aff8a', [0, 2.9, 0]], ['Z', '#5aa8ff', [0, 0, 2.9]]]) {
      const sp = this._label(txt, col);
      sp.position.set(...pos);
      this.axisLabels.add(sp);
    }
    this.helpers.add(this.axisLabels);
  }

  _label(txt, col) {
    const c = document.createElement('canvas');
    c.width = c.height = 64;
    const g = c.getContext('2d');
    g.fillStyle = col;
    g.font = 'bold 46px monospace';
    g.textAlign = 'center';
    g.textBaseline = 'middle';
    g.fillText(txt, 32, 34);
    const t = new THREE.CanvasTexture(c);
    t.colorSpace = THREE.SRGBColorSpace;
    const m = new THREE.Sprite(new THREE.SpriteMaterial({
      map: t, transparent: true, depthTest: false, depthWrite: false,
    }));
    m.scale.setScalar(0.55);
    return m;
  }

  /** Показать/скрыть оверлей по имени тумблера. */
  setOverlay(name, on) {
    if (name === 'bboxGrid') this.bboxGrid.visible = on;
    if (name === 'grid') this.grid.visible = on;
    if (name === 'axes') { this.axes.visible = on; this.axisLabels.visible = on; }
    if (name === 'wire') {
      this._wire = on;
      this.holder.traverse((o) => {
        if (o.isMesh && o.userData._origWire !== undefined) {
          o.material.wireframe = on;
        }
      });
    }
    if (name === 'normals') this._setNormals(on);
  }

  _setNormals(on) {
    if (this._normals) { this.holder.remove(this._normals); this._normals = null; }
    if (!on) return;
    this._normals = new THREE.Group();
    const a = new THREE.Vector3(), b = new THREE.Vector3();
    const nA = new THREE.Vector3(), nB = new THREE.Vector3();
    const pa = [], pb = [];
    this.holder.traverse((o) => {
      if (!o.isMesh || !o.geometry) return;
      const g = o.geometry;
      const pos = g.attributes.position;
      const nor = g.attributes.normal;
      if (!pos || !nor) return;
      // Шаг 3: на плотном меше линия на каждый треугольник не читается —
      // получается пух, а не нормали. Треугольник как единица формы читается
      // лучше всего именно на прореженной сетке.
      const step = Math.max(1, Math.floor(pos.count / 20000));
      const len = 0.08 * (this.info ? this.info.diag : 10);
      for (let i = 0; i < pos.count; i += step * 3) {
        for (let k = 0; k < 3; k++) {
          const j = i + k;
          if (j >= pos.count) break;
          a.fromBufferAttribute(pos, j).applyMatrix4(o.matrixWorld);
          nA.fromBufferAttribute(nor, j).transformDirection(o.matrixWorld);
          b.copy(a).addScaledVector(nA, len);
          pa.push(a.x, a.y, a.z); pb.push(b.x, b.y, b.z);
        }
      }
    });
    const geo = new THREE.BufferGeometry();
    geo.setAttribute('position', new THREE.Float32BufferAttribute(pa, 3));
    const lines = new THREE.LineSegments(geo, new THREE.LineBasicMaterial({
      color: 0xffd45a, transparent: true, opacity: 0.55,
    }));
    this._normals.add(lines);
    this.holder.add(this._normals);
  }

  setVertexColors(on) {
    // Вершинные цвета не «включаются» флагом: у материала их либо имеет смысл
    // показывать, либо нет. Показываем так: если COLOR_0 есть — материал
    // начинает учитывать vertexColors (clone, чтобы не портить исходный).
    this.holder.traverse((o) => {
      if (!o.isMesh) return;
      const has = !!(o.geometry && o.geometry.attributes.color);
      if (!o.userData._matOrig) o.userData._matOrig = o.material;
      if (on && has) {
        const m = o.userData._matOrig.clone();
        m.vertexColors = true;
        o.material = m;
      } else {
        o.material = o.userData._matOrig;
      }
      o.userData._hasColor = has;
    });
    // Считаем, есть ли COLOR_0 хоть где-то: если нет — тумблер ничего не
    // меняет, и это надо сказать честно, а не оставить пользователя гадать.
    let any = false;
    this.holder.traverse((o) => { if (o.isMesh && o.geometry.attributes.color) any = true; });
    return any;
  }

  /** Загрузка модели. Возвращает сводку. */
  async load(url, onProgress) {
    this.modelUrl = url;
    // Чистим прошлую: без dispose геометрии копятся, и на 6 моделях по 100 МБ
    // вкладка съедает всю видеопамять.
    this.dispose();

    const gltf = await new Promise((res, rej) => {
      this.loader.load(url, res,
        (e) => onProgress && onProgress(e.loaded, e.total || 0), rej);
    });
    const root = gltf.scene || gltf.scenes?.[0];
    if (!root) throw new Error('в файле нет сцены');
    this.holder.add(root);
    root.updateWorldMatrix(true, true);

    // Сводка. Считаем по геометриям: индексы, если есть, иначе позиции.
    let tris = 0, verts = 0, meshes = 0;
    const mats = new Set();
    root.traverse((o) => {
      if (!o.isMesh || !o.geometry) return;
      meshes++;
      const g = o.geometry;
      const n = g.attributes.position ? g.attributes.position.count : 0;
      verts += n;
      tris += g.index ? g.index.count / 3 : n / 3;
      const m = Array.isArray(o.material) ? o.material : [o.material];
      for (const mm of m) if (mm) mats.add(mm.name || mm.uuid);
      // Запоминаем исходный wireframe, чтобы тумблер каркаса возвращал как было
      if (o.userData._origWire === undefined) o.userData._origWire = !!o.material.wireframe;
    });
    const box = new THREE.Box3().setFromObject(root);
    const size = box.getSize(new THREE.Vector3());
    this.info = {
      tris, verts, meshes, mats: mats.size,
      anims: gltf.animations ? gltf.animations.length : 0,
      box, size,
      diag: size.length() || 1,
      url,
    };
    // V/T — доля вершин на треугольник, а НЕ наоборот. Здоровый меш ≈ 0.70;
    // → 1.0 и выше означает «суп из треугольников» (каждая вершина почти не
    // делится между треугольниками, то есть геометрия перекормлена).
    //
    // Направление дроби легко перепутать, и ошибка тут молчаливая: инвертированное
    // число выглядит правдоподобно и «подтверждает» то, чего нет. Поэтому в
    // подписи панели пишем именно V / T и сравниваем с 0.70, а не с 1.4.
    this.info.vt = tris > 0 ? verts / tris : 0;

    this.bboxGrid.box.copy(box);
    this._frame(box);
    this.setOverlay('bboxGrid', this.bboxGrid.visible);
    this.setOverlay('wire', !!this._wire);
    return this.info;
  }

  /** Кадрировать камеру по габаритам. */
  _frame(box) {
    const size = box.getSize(new THREE.Vector3());
    const c = box.getCenter(new THREE.Vector3());
    const r = Math.max(size.length() * 0.5, 0.5);
    const d = r / Math.tan((this.camera.fov * Math.PI / 180) / 2) * 1.45;
    // Направление «три четверти сверху»: видно и высоту, и глубину. Строго
    // спереди меш читается как плоская картинка — ровно то, за чем сюда не идут.
    const dir = new THREE.Vector3(0.62, 0.45, 0.85).normalize();
    this.camera.position.copy(c).addScaledVector(dir, d);
    this.camera.near = Math.max(0.02, r * 0.005);
    this.camera.far = r * 40;
    this.camera.updateProjectionMatrix();
    this.controls.target.copy(c);
    this.controls.update();
    this.grid.scale.setScalar(Math.max(1, r / 10));
    this.grid.position.y = box.min.y;
  }

  resetView() { if (this.info) this._frame(this.info.box); }

  /** Пустая сцена — когда модели нет. */
  dispose() {
    if (this._normals) { this.holder.remove(this._normals); this._normals = null; }
    const doomed = [];
    this.holder.traverse((o) => {
      if (o.isMesh) {
        doomed.push(o.geometry);
        if (o.material) {
          const m = Array.isArray(o.material) ? o.material : [o.material];
          for (const mm of m) doomed.push(mm);
        }
      }
    });
    this.holder.clear();
    for (const d of doomed) d?.dispose?.();
    // текстуры, которые держали материалы, тоже отпускаем
    for (const d of doomed) {
      for (const k of ['map', 'normalMap', 'roughnessMap', 'metalnessMap',
        'aoMap', 'emissiveMap', 'alphaMap', 'sheenColorMap', 'specularMap']) {
        d?.[k]?.dispose?.();
      }
    }
    this.info = null;
  }

  resize() {
    const w = this.host.clientWidth || 1, h = this.host.clientHeight || 1;
    if (w < 2 || h < 2) return;
    // `true` — обновляем и CSS-размер холста, иначе на HiDPI (dpr > 1) буфер
    // отрисовки больше контейнера в dpr раз, и модель обрезается по краям.
    // При dpr=1 поведение прежнее.
    this.renderer.setSize(w, h, true);
    this.camera.aspect = w / h;
    this.camera.updateProjectionMatrix();
  }

  _loop() {
    const tick = () => {
      this.controls.update();
      this.renderer.render(this.scene, this.camera);
      this._raf = requestAnimationFrame(tick);
    };
    this._raf = requestAnimationFrame(tick);
  }

  stop() {
    if (this._raf) cancelAnimationFrame(this._raf);
    this._raf = null;
    removeEventListener('resize', this._onResize);
    this.dispose();
    this.renderer.dispose();
    this.canvas.remove();
  }
}
