# Part configurator: detach, explode, swap parts of a loaded GLB

## When to use

A GLB arrives as N named nodes (see `blender_split_parts_to_glb.md`). You want a
GTA-style garage in the browser: click a part to detach it, slide an "explode" control to
pull the whole car apart, swap a part for a procedural or second-GLB variant, keep a ghost
of the original in place.

The three things that make this work and are easy to get wrong:

1. a **part registry** built from the manifest, not from a hardcoded node list;
2. **spring-damper** animation instead of lerps (parts must not arrive in lockstep);
3. a **multisampled EffectComposer** target - without it every panel seam sparkles.

## 1. Part registry

The GLB gives you nodes; the manifest gives you meaning. Join them by node name.

```js
async load(glbUrl, manifestUrl) {
  const gltf = await new GLTFLoader().loadAsync(glbUrl);
  this.model = gltf.scene;
  this.root.add(this.model);

  this.manifest = await fetch(manifestUrl).then((r) => r.json());
  this.manifestById = new Map(this.manifest.parts.map((p) => [p.id, p]));

  this._upgradeMaterials();
  this.model.updateMatrixWorld(true);
  this._measureBox();
  this._registerParts();
  this._buildChassis();
  return this;
}
```

`_registerParts` walks the model, and for every node whose name is in the manifest builds a
record holding **both** local and world-space boxes - local for the UI thumbnail, world for
explode direction:

```js
const world = new THREE.Box3();
for (const m of meshes) {
  m.geometry.computeBoundingBox();
  world.union(m.geometry.boundingBox.clone().applyMatrix4(m.matrixWorld));
}

this.parts.set(o.name, {
  id: o.name, node: o, role: rec.role, material: rec.material, kind: rec.kind,
  swap: rec.swap, parentId: rec.parent || null, meshes,
  isPivot: pivotIds.has(o.name),
  rest: o.position.clone(), restRot: o.rotation.clone(),
  worldPos: world.getCenter(new THREE.Vector3()),
  pos: new THREE.Vector3(), vel: new THREE.Vector3(),
  rot: new THREE.Euler(), rotVel: new THREE.Vector3(),
  tPos: new THREE.Vector3(), tRot: new THREE.Euler(),
  dir: new THREE.Vector3(), detached: false, removed: false, hidden: false,
  ghost: null, opacity: 1, tOpacity: 1,
});
```

**World-space bounding boxes need `updateMatrixWorld(true)` first**, and every vertex must be
transformed with `applyMatrix4(m.matrixWorld)`. Reading `geometry.boundingBox` alone gives
local coordinates - a common source of "the deck is at y = 0.09" style bugs where the part
is actually 0.4 m up in the world.

### Explode direction

Default: radially away from the car's centre. Override per part when "radially away" is
visually wrong (glass should rise, exhaust should go back, mirrors should go sideways):

```js
export const EXPLODE_OVERRIDE = {
  body_shell:    [0, 0, 0],      // the anchor - never moves
  glass:         [0, 1.0, 0.10],
  interior:      [0, 1.0, -0.05],
  trim:          [0, 0.35, 0.95],
  body_lower:    [0, -0.15, 0.99],
  exhaust:       [-0.35, 0.05, 0.94],
  mirrors:       [1, 0.35, -0.15],
  tail_lights:   [0, 0.15, 1],
  front_markers: [0, 0.15, -1],
};

for (const p of this.parts.values()) {
  const ov = EXPLODE_OVERRIDE[p.id];
  if (ov) { p.dir.fromArray(ov).normalize(); continue; }
  if (p.isPivot) continue;
  const w = p.worldPos.clone().sub(this.center);
  w.y = Math.max(w.y, 0.09);       // never let a part slide straight through the floor
  p.dir.copy(w).normalize();
}
```

### The chassis group - and the nested-child trap

Every movable part is `attach()`ed to a `chassis` group so that ride-height / body-lift
adjustments move the whole shell without touching the wheels. Two rules:

- **skip wheels** - they must stay anchored to the ground;
- **skip nested children whose parent is itself a registered part** - a headlight pod is a
  parent node with `housing`/`lens`/`cover` children. If you `attach()` the children to the
  chassis, they stop riding along when the pod rotates, and their world bbox collapses to
  the origin.

```js
_buildChassis() {
  this.chassis = new THREE.Group();
  this.chassis.name = 'chassis';
  this.model.add(this.chassis);
  for (const p of this.parts.values()) {
    if (p.id.startsWith('wheel_')) continue;
    if (p.parentId && this.parts.has(p.parentId)) continue;   // nested -> ride the pivot
    this.chassis.attach(p.node);
    p.rest = p.node.position.clone();       // re-read rest AFTER attach
    p.restRot = p.node.rotation.clone();
  }
}
```

`Object3D.attach()` preserves world transform, so the local `position` changes. Re-reading
`rest`/`restRot` after the attach is mandatory; otherwise the first `update()` snaps every
part back to its pre-attach local transform.

## 2. Spring-damper animation

A lerp makes every part arrive at the same time - it reads as a slideshow. A critically-ish
damped spring gives the mechanical, weighty feel that sells the effect:

```js
const SPRING_K = 150;
const SPRING_C = 17;
const EXPLODE_DIST = 0.78;
const DETACH_DIST  = 0.44;
const REMOVE_DIST  = 0.95;

update(dt) {
  const k = SPRING_K, c = SPRING_C;
  const d = Math.min(dt, 1 / 30);          // clamp: a tab-switch dt spike must not explode the sim
  const target = this._tmp;
  for (const p of this.parts.values()) {
    if (p.isPivot) continue;
    target.copy(p.dir).multiplyScalar(EXPLODE_DIST * this.explode);
    if (p.detached) target.copy(p.dir).multiplyScalar(Math.max(DETACH_DIST, EXPLODE_DIST * this.explode));
    if (p.removed)  target.copy(p.dir).multiplyScalar(REMOVE_DIST);
    target.add(p.tPos);

    p.vel.x += (target.x - p.pos.x) * k * d;
    p.vel.y += (target.y - p.pos.y) * k * d;
    p.vel.z += (target.z - p.pos.z) * k * d;
    p.vel.multiplyScalar(Math.max(0, 1 - c * d));
    p.pos.addScaledVector(p.vel, d);
    p.node.position.copy(p.rest).add(p.pos);

    const rv = p.rotVel, r = p.rot;
    rv.x += (p.tRot.x - r.x) * k * d;
    rv.y += (p.tRot.y - r.y) * k * d;
    rv.z += (p.tRot.z - r.z) * k * d;
    rv.multiplyScalar(Math.max(0, 1 - c * d));
    r.x += rv.x * d; r.y += rv.y * d; r.z += rv.z * d;
    p.node.rotation.set(p.restRot.x + r.x, p.restRot.y + r.y, p.restRot.z + r.z);
  }
}
```

Notes:

- `p.rotVel` must be a **`THREE.Vector3`**, not a `THREE.Euler` - `Euler` has no
  `multiplyScalar`.
- `Math.max(0, 1 - c * d)` is the damping term. With `c = 17` and `d = 1/60` it is 0.717.
- The damping is **frame-rate dependent** by construction. At 20 FPS (software rasteriser)
  `1 - c*d` goes negative and gets clamped to 0, killing all damping and the part never
  converges. For headless verification do not rely on wall-clock frames - see §6.

## 3. Detach + ghost hologram

When a part detaches it should leave a translucent hologram of itself at the rest pose, so
the user sees *where* it came from. Clone the node, swap every material for one additive
basic material, pin it to the rest transform, hide it until needed:

```js
_ensureGhost(p) {
  if (p.ghost) return;
  const g = p.node.clone(true);
  const gm = new THREE.MeshBasicMaterial({
    color: ACCENT, transparent: true, opacity: 0.085,
    blending: THREE.AdditiveBlending, depthWrite: false, side: THREE.DoubleSide,
  });
  g.traverse((o) => { if (isMesh(o)) { o.material = gm; o.castShadow = false; o.receiveShadow = false; } });
  g.position.copy(p.rest);
  g.rotation.copy(p.restRot);
  g.visible = false;
  g.name = 'ghost_' + p.id;
  p.node.parent.add(g);
  p.ghost = g;
}
```

Clone **before** any transform is applied, and parent the ghost to the same parent as the
original. `depthWrite: false` + additive blending is what makes it read as a hologram rather
than a grey copy. Opacity 0.085 is the sweet spot; above ~0.15 it starts competing with the
part itself.

Detach also tilts the part so it reads as "loose" rather than "floating":

```js
setDetached(id, on) {
  const p = this.parts.get(id);
  if (!p || p.isPivot) return;
  p.detached = on;
  if (on) {
    const axis = new THREE.Vector3().crossVectors(p.dir, new THREE.Vector3(0, 1, 0));
    if (axis.lengthSq() < 1e-4) axis.set(1, 0, 0);
    axis.normalize().multiplyScalar(0.18);          // ~10°
    p.tRot.set(axis.x, axis.y, axis.z);
    this._ensureGhost(p);
    if (p.ghost) p.ghost.visible = true;
  } else if (!p.removed) {
    p.tPos.set(0, 0, 0);
    p.tRot.set(0, 0, 0);
    if (p.ghost) p.ghost.visible = false;
  }
}
```

## 4. Swapping a part for a variant

Two mechanisms, use both:

- **Replace by opacity** - the stock mesh of a part fades out (`setPartRemoved(id, true)`)
  while the procedural variant fades in. No ghost, no offset; the part stays in place.
- **Replace by node swap** - remove the old procedural group from the pivot, build the new
  one, add it back. Cache by a `userData.design` key so re-selecting the same variant is a
  no-op.

```js
const existing = this.procRims.get(key);
if (design === 'stock') {
  if (existing) { node.remove(existing); existing.traverse((o) => { if (o.isMesh) o.geometry.dispose(); }); this.procRims.delete(key); }
  this.car.setPartRemoved('wheel_' + key + '_rim', false);
} else {
  this.car.setPartRemoved('wheel_' + key + '_rim', true);
  let g = existing;
  if (!g || g.userData.design !== design) {
    if (g) { node.remove(g); g.traverse((o) => { if (o.isMesh) o.geometry.dispose(); }); }
    g = buildRim({ design, R, w, side });
    g.userData.design = design;
    node.add(g);
    this.procRims.set(key, g);
  }
}
```

**Dispose the geometry** when removing a variant. A garage UI lets the user cycle designs
hundreds of times per session; leaking a few hundred KB per cycle ends in a GPU memory
warning after a few minutes.

Opacity-based replacement must respect the material's *original* transparency, so keep the
base values in `userData` at material-creation time:

```js
mat.userData.base = { transparent: mat.transparent, opacity: mat.opacity, depthWrite: mat.depthWrite };

_applyOpacity(p) {
  for (const m of p.meshes) {
    const b = m.material.userData.base;
    const o = b.opacity * p.opacity * (p.xray || 1);
    m.material.opacity = o;
    m.material.transparent = b.transparent || o < 0.995;
    m.material.depthWrite = o > 0.995 ? b.depthWrite : false;
    m.material.needsUpdate = true;
  }
  if (p.opacity < 0.02 && p.removed) p.node.visible = false;
  else if (!p.hidden) p.node.visible = true;
}
```

`depthWrite: false` whenever the part is translucent, otherwise it occludes the parts behind
it. This is also how X-ray mode works: force `xray = 0.13` on the shell materials only.

## 5. Materials: rebuild, don't reuse

The glTF materials are `MeshStandardMaterial` with whatever the exporter produced. Rebuild
them from the manifest's PBR table so the configurator controls have something to talk to,
and keep a `name → [materials]` index so a slider can address "all Paint materials" at once:

```js
_upgradeMaterials() {
  this.model.traverse((o) => {
    if (!isMesh(o)) return;
    const src = Array.isArray(o.material) ? o.material[0] : o.material;
    const name = src?.name || 'Material';
    const mat = matFactory(name);         // per-name material recipe
    mat.name = name;
    mat.side = src ? src.side : THREE.FrontSide;
    mat.userData.base = { transparent: mat.transparent, opacity: mat.opacity, depthWrite: mat.depthWrite };
    mat.userData.em0 = mat.emissive ? mat.emissive.getHex() : null;
    mat.userData.emI0 = mat.emissiveIntensity ?? 0;
    o.material = mat;
    o.castShadow = true;
    o.receiveShadow = true;
    if (!this.materials.has(name)) this.materials.set(name, []);
    this.materials.get(name).push(mat);
  });
}
```

Two material details that matter for a car body:

- **`polygonOffset` on the dark trim materials.** Converted models have decals, grilles and
  window trim modelled as separate surfaces *coplanar* with the paint. Without
  `polygonOffset: true, polygonOffsetFactor: -1..-2` they flicker through the body.
- **`MeshPhysicalMaterial` + `clearcoat` for paint.** `metalness 0.24 / roughness 0.24 /
  clearcoat 1.0 / clearcoatRoughness 0.05` is the "showroom gloss" recipe. Metallic flake
  is faked with `sheen`.

```js
case 'Paint': return new THREE.MeshPhysicalMaterial({
  color: 0xf2f3f5, metalness: 0.24, roughness: 0.24,
  clearcoat: 1, clearcoatRoughness: 0.05, envMapIntensity: 0.85 });
case 'SecondPaint': return new THREE.MeshPhysicalMaterial({
  color: 0x0e0f11, metalness: 0.25, roughness: 0.34, clearcoat: 0.9, clearcoatRoughness: 0.08,
  polygonOffset: true, polygonOffsetFactor: -1, polygonOffsetUnits: -1 });
case 'Black': return new THREE.MeshStandardMaterial({
  color: 0x17181b, metalness: 0.15, roughness: 0.62,
  polygonOffset: true, polygonOffsetFactor: -2, polygonOffsetUnits: -2 });
```

## 6. The MSAA EffectComposer recipe (critical)

**`new EffectComposer(renderer)` creates its own render target with `samples: 0`.** The
renderer's `antialias: true` then does nothing, because you are no longer rendering to the
canvas - you are rendering to a plain texture. The visible symptom is not "jagged edges": it
is **dashed, dashed-looking panel seams and window trim**, because a 1-pixel coplanar gap
between two panels turns into a dotted line once MSAA is gone.

Pass a multisampled target explicitly:

```js
const buf = this.renderer.getDrawingBufferSize(new THREE.Vector2());
const rt = new THREE.WebGLRenderTarget(buf.x, buf.y, { type: THREE.HalfFloatType, samples: 4 });
this.composer = new EffectComposer(this.renderer, rt);
this.composer.setPixelRatio(Math.min(devicePixelRatio, 2));
this.composer.addPass(new RenderPass(this.scene, this.camera));
this.composer.addPass(new UnrealBloomPass(new THREE.Vector2(1, 1), 0.22, 0.55, 1.0));
this.composer.addPass(new OutputPass());
```

Then resize **all three** in `resize()`:

```js
resize() {
  const w = innerWidth, h = innerHeight;
  this.camera.aspect = w / h;
  this.camera.updateProjectionMatrix();
  this.renderer.setSize(w, h, false);
  this.composer.setSize(w, h);
  this.bloom.setSize(w, h);
}
```

Debugging note: to prove the artefact is MSAA and not the geometry, temporarily swap all
materials to `MeshBasicMaterial` (flat) and `MeshNormalMaterial` (normal). If the seams
persist in both, it is a sampling/resolution problem, not a shading problem. Screenshot a
tight crop around one seam (window trim, a door edge) - the full-car shot hides it.

Bloom is the other easy way to ruin a studio look: `strength 0.42, threshold 0.8` blows out
a white car into a glowing blob. `0.22 / 0.55 / 1.0` keeps emissive lights readable while
leaving the paint alone.

## 7. Deterministic verification hook

Software rasterisers (SwiftShader, llvmpipe) run at 15-25 FPS, which is below the threshold
where the spring damping breaks down (§2). Never assert on wall-clock animation. Expose a
hook that steps the simulation deterministically, and drive it from the test:

```js
window.__scene = {
  ready: true, THREE, car, studio, tuning, state,
  set: (patch) => change(patch),
  click: (id) => partClick(id),
  stats: () => Tuning.stats(state),
  /** Advance the part animation deterministically (60 Hz) without waiting on rAF. */
  settle: (seconds = 1) => { const n = Math.round(seconds * 60); for (let i = 0; i < n; i++) car.update(1 / 60); },
  info: () => ({ /* explode, popup angle, detached count, camera, mesh count */ }),
  coverage: (bg = [6, 7, 10], tol = 26) => { /* readPixels + count non-background pixels */ },
};
```

`coverage()` via `gl.readPixels` answers "did anything actually render?" - a scene that
throws inside the render loop still screenshots as a clean background. Assert on it:

```js
const cov = await page.evaluate(() => window.__scene.coverage());
if (cov.ratio < 0.10) throw new Error('car covers only ' + (cov.ratio * 100).toFixed(1) + '% of frame');
```

Assert on **semantic state**, not pixels: pop-up angle ≈ 0.8727 rad for 50°, `rootY > 0`
when the wheel diameter is increased, `detached === N`, `procRims.size === 4`,
`spoiler` non-null and its world bbox above the deck. Screenshots are for humans; assertions
are for CI.

## Pitfalls

| Symptom | Cause |
|---|---|
| Dashed seams / dotted window trim | `EffectComposer` without an MSAA render target |
| Part snaps to origin on first frame | `rest` read before `attach()` |
| Headlight lens left behind when the pod opens | Nested child not skipped in `_buildChassis` |
| `rv.multiplyScalar is not a function` | `rotVel` was an `Euler`; use `Vector3` |
| Detach distance wrong in CI | Wall-clock frames under SwiftShader; use a deterministic `settle()` |
| Variant leaks GPU memory | Geometry not disposed when swapping |
| Decals flicker through the body | Missing `polygonOffset` on trim materials |
| Exploded part slides through the floor | Explode direction not clamped (`w.y = Math.max(w.y, 0.09)`) |
| Ghost hologram occludes the car | `depthWrite: false` missing on the ghost material |
| White paint blows out to a blob | Bloom strength/threshold too high; exposure too high |
