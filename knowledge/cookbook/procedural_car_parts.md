# Procedural replacement parts: rims, spoilers, exhaust tips, plates

## When to use

You need variant parts that are **not** in the source model - a different wheel design, a GT
wing, a titanium exhaust tip, a custom licence plate. Shipping a second GLB per variant means
N downloads and N asset pipelines. Building them from primitives costs ~100 lines, weighs
nothing, is parameterised (diameter, width, offset, wing height/pitch) and lets the UI expose
sliders instead of a fixed list.

The trade-off is honest: procedural parts look *clean and machined*, not *modelled*. For a
minimalist tech aesthetic that is a feature. For a photoreal garage you want real GLBs.

## Rule 0 - fix the local frame before writing any geometry

Every builder must produce geometry in a **documented local frame**, and the caller must know
which way is "forward", "up" and "outward". Getting this wrong costs an afternoon of
rotating-by-guesswork.

| Part | Origin | Axis convention |
|---|---|---|
| Rim | hub centre | wheel axis = **X**, outward face at **-X** |
| Spoiler | on the rear deck | **-Z** forward, **+Y** up, car width along **X** |
| Exhaust tip | at the outlet | **+Z** rearwards (cylinders rotated into Z) |
| Plate | - | textured quad, no builder needed |

For the rim, "outward at -X" matches the GLB: the left-side wheel (negative world X) has its
face at negative local X, so `if (side > 0) g.rotation.y = Math.PI` flips the right side.
One builder, two sides, no mirrored geometry.

## Rule 1 - normalise before merging

`mergeGeometries()` returns **`null`** when indexed and non-indexed inputs are mixed.
`BoxGeometry` and `CylinderGeometry` are indexed; `ExtrudeGeometry` and `ShapeGeometry` are
not. A spoiler made of box stanchions + an extruded blade hits this on the first try, and the
failure mode is a `TypeError: Cannot read properties of null (reading 'computeVertexNormals')`
several lines later. Normalise first:

```js
import { mergeGeometries } from 'three/addons/utils/BufferGeometryUtils.js';

function mergeParts(list) {
  const flat = list.map((g) => (g.index ? g.toNonIndexed() : g));
  const merged = mergeGeometries(flat, false);
  flat.forEach((g, i) => { if (g !== list[i]) g.dispose(); });   // dispose only the copies we made
  if (!merged) console.error('mergeParts failed', list.map((g) => g.type));
  return merged;
}
```

Two details:

- dispose only the *temporary* non-indexed copies, not the originals;
- a merged geometry is **non-indexed**, so `geometry.index === null`. Any tri-count or
  raycast code must fall back to `attributes.position.count / 3`. This bit a test that
  reported "трис 0" for a perfectly fine GT wing.

## Rim builder

The wheel's proportions come from the model, not from constants - pass `R` (rim radius) and
`w` (rim width) measured from the stock rim's bbox. Derive them once at load:

```js
_buildRimInfo() {
  this.rimInfo = { R: 0.086, w: 0.102 };
  const rim = this.parts.get('wheel_FL_rim');
  if (!rim || !rim.meshes.length) return;
  rim.meshes[0].geometry.computeBoundingBox();
  const b = rim.meshes[0].geometry.boundingBox;
  this.rimInfo = { R: Math.max(b.max.y, -b.min.y), w: b.max.x - b.min.x };
}
```

Core primitives - a cylinder rotated into the X axis, and a **flat disc with holes** for the
face (a `Shape` with `Path` holes, then rotated so the shape normal `+Z` maps to `+X`):

```js
const Z90 = -Math.PI / 2;

function cyl(rt, rb, h, seg, open = false) {
  const g = new THREE.CylinderGeometry(rt, rb, h, seg, 1, open);
  g.rotateZ(Z90);
  return g;
}

/** A flat disc in the YZ plane (normal along X), optional holes. */
function discFace(radius, holes = [], thickness = 0) {
  const s = new THREE.Shape();
  s.absarc(0, 0, radius, 0, Math.PI * 2, false);
  for (const h of holes) {
    const p = new THREE.Path();
    p.absarc(h.x, h.y, h.r, 0, Math.PI * 2, true);   // clockwise hole = subtracted
    s.holes.push(p);
  }
  const g = new THREE.ShapeGeometry(s, 36);
  g.rotateY(Math.PI / 2);                            // shape normal +Z -> +X
  if (thickness > 0) {
    const e = new THREE.ExtrudeGeometry(s, { depth: thickness, bevelEnabled: false, curveSegments: 36 });
    e.rotateY(Math.PI / 2);
    e.translate(-thickness, 0, 0);                   // extrude grows along +X; push it back
    g.dispose();
    return e;
  }
  return g;
}
```

Radial spokes, with an optional taper on the outer end for a machined look:

```js
function radialSpokes({ count, rInner, rOuter, thickness, width, phase = 0, taper = 1 }) {
  const out = [];
  const len = rOuter - rInner;
  for (let i = 0; i < count; i++) {
    const a = phase + (i / count) * Math.PI * 2;
    const b = new THREE.BoxGeometry(thickness, len, width);
    if (taper !== 1) {
      const pos = b.attributes.position;
      for (let v = 0; v < pos.count; v++) {
        if (pos.getY(v) > 0) {
          pos.setZ(v, pos.getZ(v) * taper);
          pos.setX(v, pos.getX(v) * (0.55 + 0.45 * taper));
        }
      }
      b.computeVertexNormals();
    }
    b.rotateX(a);
    b.translate(0, Math.cos(a) * (rInner + len / 2), Math.sin(a) * (rInner + len / 2));
    out.push(b);
  }
  return out;
}
```

Design recipes (all share the barrel + lip + spokes + centre cap skeleton):

| design | barrel | face | spokes |
|---|---|---|---|
| `stock` / `spoke5` / `watanabe` | tapered open cylinder | stepped outer lip | 6 / 5 / 8 tapered boxes |
| `mesh` | tapered barrel + stepped lip | - | **two offset 18-spoke layers** (phase `π/18`) → woven lattice |
| `deepdish` | barrel + wide outer dish | - | 6 short thick spokes, phase `π/6` |
| `steel` | plain barrel | disc with 5 punched holes | none |
| `aero` | plain barrel | flat solid disc + raised cap | none |

Assembly - merge, wrap in a mesh, wrap in a group, flip for the right side:

```js
const geo = mergeParts(parts);
parts.forEach((p) => p.dispose());
const mesh = new THREE.Mesh(geo, new THREE.MeshStandardMaterial({ color: 0xc9ced4, metalness: 0.95, roughness: 0.22 }));
mesh.name = 'rim_proc';
mesh.castShadow = true;
const g = new THREE.Group();
g.name = 'rim_assembly';
g.add(mesh);
if (side > 0) g.rotation.y = Math.PI;
return g;
```

The returned **group** is important: the caller adds it to the wheel pivot and can then scale
it (`node.scale.set(width, diameter, diameter)`) and offset it without touching the stock rim.

## Spoiler builder

The trick for the blade is `ExtrudeGeometry` + `rotateY(-π/2)`: it maps the 2D profile's `+X`
(depth along the car) onto `+Z` (rearwards) and the extrusion onto `-X` (car width). Define
the profile in the intuitive "X = forward, Y = up" plane and let the rotation do the rest:

```js
function extrudeX(shape, width) {
  const g = new THREE.ExtrudeGeometry(shape, { depth: width, bevelEnabled: false, curveSegments: 12 });
  g.rotateY(-Math.PI / 2);
  g.translate(width / 2, 0, 0);      // centre the extrusion on the car's centreline
  return g;
}
```

An airfoil profile (rounded top, flat-ish underside) reused by lip and GT wing:

```js
function airfoil(depth, thick) {
  const s = new THREE.Shape();
  s.moveTo(-depth / 2, 0);
  s.quadraticCurveTo(-depth * 0.22, thick, 0, thick);
  s.quadraticCurveTo(depth * 0.22, thick, depth / 2, 0);
  s.quadraticCurveTo(depth * 0.2, -thick * 0.45, 0, -thick * 0.45);
  s.quadraticCurveTo(-depth * 0.2, -thick * 0.45, -depth / 2, 0);
  return s;
}
```

Designs:

- **`lip`** - a small airfoil extruded across 86 % of the width, 4 mm up, 28 mm back. The
  cheapest visible change.
- **`ducktail`** - a hand-authored `Shape` (kick-up with a concave underside) extruded across
  93 % of the width. Reads as a body-integrated spoiler, not a bolt-on.
- **`gt`** - two vertical box stanchions with feet + an airfoil blade with end plates, blade
  rotated by `pitch`.
- **`swan`** - same blade, but each side is **two angled boxes** (a low forward strut and a
  high rear strut) forming a swan-neck silhouette.

```js
const blade = extrudeX(airfoil(0.165, 0.020), width * 0.98);
blade.rotateX(pitch);
blade.translate(0, h + 0.006, 0.012);
parts.push(blade);
```

Where does it mount? **Measure the deck from the body shell**, don't hardcode. Scan the shell
geometry in **world space** for the highest point behind `z > 0.28` (rear half), scored as
`y + z * 0.55` so the search prefers the rear-most high point, then measure the half-width of
the shell near that z:

```js
_buildDeckAnchor() {
  this.deck = { y: 0.42, z: 0.6, half: 0.34 };
  const shell = this.parts.get('body_shell');
  if (!shell || !shell.meshes.length) return;
  const mesh = shell.meshes[0];
  mesh.updateWorldMatrix(true, false);
  const pos = mesh.geometry.attributes.position;
  const v = new THREE.Vector3();
  let best = -1e9, bestV = null;
  for (let i = 0; i < pos.count; i++) {
    v.fromBufferAttribute(pos, i).applyMatrix4(mesh.matrixWorld);   // WORLD space
    if (v.z < 0.28) continue;
    const score = v.y + v.z * 0.55;
    if (score > best) { best = score; bestV = v.clone(); }
  }
  if (!bestV) return;
  let half = 0;
  for (let i = 0; i < pos.count; i++) {
    v.fromBufferAttribute(pos, i).applyMatrix4(mesh.matrixWorld);
    if (Math.abs(v.z - bestV.z) > 0.14) continue;
    half = Math.max(half, Math.abs(v.x));
  }
  this.deck = { y: bestV.y, z: bestV.z + 0.02, half: Math.max(half * 0.94, 0.2) };
}
```

The wing then sits at `(0, deck.y, deck.z - 0.05)` - 5 cm forward of the deck's rear edge so
it does not overhang the bumper.

**`mesh.matrixWorld` must be current.** Iterating `attributes.position` without
`applyMatrix4(mesh.matrixWorld)` gives local coordinates; the classic symptom is "the deck is
at y = 0.09" on a car whose roof is at 0.5.

## Exhaust tip builder

Cylinders rotated into Z, positioned from the stock exhaust part's **world box** so it always
meets the bumper:

```js
const mk = (radius, length, x, z, taper = 1) => {
  const c = new THREE.CylinderGeometry(radius * taper, radius, length, 20, 1, true);
  c.rotateX(Math.PI / 2);
  c.translate(x, 0, z);
  return c;
};
```

- `single` - one pipe, radius ×1.35;
- `dual` - two pipes at `x = ±r * 1.5`;
- `burnt` - a tapered pipe + a torus ring near the mouth, titanium-purple material.

Material must be `side: THREE.DoubleSide` - the pipes are open cylinders and you see their
inside walls.

```js
const b = ex.box;                                          // world box of the stock exhaust
tip.position.set(b.min.x + 0.02, (b.min.y + b.max.y) / 2, b.max.z - 0.03);
```

Both offsets matter: `+0.02` from the box's minimum X keeps it inside the bumper, `-0.03`
from `max.z` stops it floating behind the car. A tip placed at `max.z` looks detached.

## Licence plate as a CanvasTexture

Cheaper and sharper than any geometry-based text:

```js
export function plateTexture(text, style) {
  const w = 512, h = 128;
  const c = document.createElement('canvas');
  c.width = w; c.height = h;
  const x = c.getContext('2d');
  x.fillStyle = style.bg;
  x.fillRect(0, 0, w, h);
  x.strokeStyle = 'rgba(0,0,0,.35)';
  x.lineWidth = 6;
  x.strokeRect(3, 3, w - 6, h - 6);
  // ... optional JP blue strip, then centred mono text
  const tex = new THREE.CanvasTexture(c);
  tex.colorSpace = THREE.SRGBColorSpace;
  tex.anisotropy = 4;
  return tex;
}
```

Set `tex.colorSpace = THREE.SRGBColorSpace` - a `CanvasTexture` defaults to linear and the
plate renders washed out. Dispose the previous map when the text changes, and cache on
`(text, style)` so typing does not re-render a canvas every keystroke.

## Pitfalls

| Symptom | Cause |
|---|---|
| `mergeGeometries` returns `null` | Mixed indexed (Box/Cylinder) and non-indexed (Extrude/Shape) inputs |
| `Cannot read properties of null (reading 'computeVertexNormals')` | The above, surfacing later |
| Tri count reads 0 for a real mesh | Merged geometry is non-indexed; use `position.count / 3` |
| Wing mounted at the wrong height | Deck scan in local, not world space |
| Wing hangs off the back of the car | Not offset forward from the deck's rear edge |
| Rim on the right side is inside-out | Missing `rotation.y = Math.PI` for `side > 0` |
| Exhaust tip floats behind the bumper | Placed at `max.z` instead of `max.z - 0.03` |
| Plate washed out | `CanvasTexture.colorSpace` not set to sRGB |
| Rim faceted / banded under a software rasteriser | Flat-shaded boxes at low resolution; cosmetic, not a bug |
