# 3D hero header: real geometry, camera dolly on scroll, grade chain

## When to use

A landing page whose first screen is a WebGL scene: the camera orbits a few degrees with the
mouse, dollies forward as the page scrolls, the scene blurs and fades away, and the content
below takes over. Reference implementation: the WebDesign Master lesson "Создание красивого
3D сайта на Three.js" (`youtube.com/watch?v=go01B9Xd0HM`), rebuilt for **three.js r186** with
locally generated assets.

The lesson ships one 70 MB `scene.glb` (a cave with a wizard) and does everything on top of
it. Copying that shape of solution means you need a 3D asset before you can start. The
alternative, used here, is **real geometry built in code** plus one generated mesh for the
hero. Read both routes before choosing:

| Route | Cost | Depth quality | When |
|---|---|---|---|
| One generated GLB scene | 17–18 min per asset, 40 MB at default `faces_3d` | real geometry, real lights, real shadows | the camera flies through the scene, or props are seen from many angles |
| Procedural geometry + one generated character | minutes of code, ~2–5 MB total | real geometry, real lights, real shadows, full art direction control | a hero shot of architecture: a building, a room, a street |

**Image planes are not on this list.** Stacked billboards produce parallax, but the light
never lands on them, nothing casts a shadow, and the result reads as a collage the moment the
camera moves. If the brief says "3D", the answer is meshes.

## Procedural architecture: one extruded wall, not a box with decals

A facade needs openings you can see through. `BoxGeometry` cannot have holes, and faking them
with dark decals dies under any camera motion. Use a `Shape` with `Path` holes and
`ExtrudeGeometry`:

```js
const shape = new THREE.Shape();
shape.moveTo(-W / 2, 0); shape.lineTo(W / 2, 0);
shape.lineTo(W / 2, H); shape.lineTo(-W / 2, H);
shape.closePath();

for (let f = 0; f < floors; f++) {
  for (let b = 0; b < bays; b++) {
    const cx = -W / 2 + bayW * (b + 0.5);
    const cy = f * floorH + floorH * 0.56;
    const hole = new THREE.Path();
    hole.moveTo(cx - winW / 2, cy - winH / 2);
    hole.lineTo(cx - winW / 2, cy + winH / 2);
    hole.lineTo(cx + winW / 2, cy + winH / 2);
    hole.lineTo(cx + winW / 2, cy - winH / 2);
    hole.closePath();
    shape.holes.push(hole);
  }
}

const wall = new THREE.Mesh(
  new THREE.ExtrudeGeometry(shape, { depth: 0.55, bevelEnabled: false, curveSegments: 1 }),
  wallMat
);
```

Notes that cost time if missed:

- `ExtrudeGeometry` UVs for the front face are the **shape's own x/y coordinates**, not 0..1.
  A 26 m wall with `map.repeat = 0.16` gets ~4 texture tiles; with the default repeat it gets
  26 tiles and looks like noise.
- The hole walls are real geometry, so the opening has visible thickness (a reveal) from any
  angle. That reveal is most of what makes the wall read as a wall.
- `bevelEnabled: false` — bevels on a wall are 4× the triangles for a chamfer nobody sees.
- The shell behind the wall must exist, or you look straight through the building into the
  sky. A `BoxGeometry` with `side: THREE.BackSide` and a near-black material is enough; add
  interior floor slabs at each level so the openings have depth.

## The albedo trap (this is why procedural scenes look like mud)

`MeshStandardMaterial` multiplies `map` × `color`. A grey concrete canvas at 138/255 is 0.25
in linear space; a "concrete" tint of `0xa8a094` is 0.4. The product is 0.1 — darker than
coal, and no amount of light fixes it. The first render of this scene was a brown void for
exactly this reason.

Rule: **the texture carries the value, the tint stays near white.** `0xf2efe9` on the same
texture gives 0.22, which is right for concrete, and the light can do its job.

Same class of bug, other symptoms:

- **Flat lit elevation looks like cardboard.** Bake a vertical grime gradient into vertex
  colours — dark at the base, clean at the parapet — and enable `vertexColors` on a cloned
  material. Costs nothing at runtime, and it is the difference between "wall" and "poster".

  ```js
  const k = THREE.MathUtils.clamp(0.34 + 0.66 * Math.pow(pos.getY(i) / H, 0.5), 0, 1);
  ```

- **170 identical rocks read as one blob.** `InstancedMesh.setColorAt` with a per-instance
  grey multiplier (0.55–1.2) breaks the uniformity for free. Remember `instanceColor` is
  multiplied by `material.color`, so the base tint must already be the mid value.

## Lighting rig for a night exterior

Four lights, in this order of importance:

1. **Hemisphere** (`sky 0x8ea6c0`, `ground 0x1c1712`, intensity ~1.0) — cold ambient in the
   shadows. Without it, every shadow is black and the frame has no colour separation.
2. **Key directional**, warm, ~1.2 — the only shadow caster. `shadow.mapSize 2048`,
   `bias -0.0009`, and a shadow camera box sized to the visible block, not the whole scene.
3. **Back directional**, warm, ~1.1, pointing at the camera — separates the silhouette from
   the sky.
4. **Interior point lights** (the practicals): one per lit window, `intensity 8–12`,
   `distance ~18`, `decay 2`. They are what makes the window holes read as rooms.

Emissive planes (`MeshBasicMaterial` with a gradient canvas) are cheaper than lights for the
doorway itself; a bloom pass then picks them up. The gradient matters — a flat colour turns
into a white blob under `UnrealBloomPass`.

## Camera: orbit by mouse, dolly by scroll

No `OrbitControls`. Two inputs summed into a target position, then damped — the damping is
what makes the motion feel expensive.

```js
const ang = mouse.x * 0.10;                       // radians at |mouse.x| = 1
const radius = R - (R - Rmin) * p;                // p = scroll / innerHeight, 0..1
camera.position.lerp(new THREE.Vector3(
  look.x + side + Math.sin(ang) * radius,         // `side` turns the elevation into a 3/4 view
  eyeY + mouse.y * 0.28 + p * 0.5,
  look.z + Math.cos(ang) * radius
), 0.075);
camera.lookAt(look);
```

- `cos`/`sin` of one angle = orbit on a circle. Above ~0.2 rad the near objects swing out of
  frame; 0.08–0.12 is the usable range for a foreground subject 4–5 m from the camera.
- `lookAt` a **fixed** point every frame, after the lerp. Aiming at the moving target makes
  the whole frame sway, which reads as a bug.
- A constant `side` offset (camera off the look axis) is what turns a flat elevation into a
  three-quarter view. It costs one number and buys the entire sense of volume.
- Dolly range: 1.5–2.5 m over one screen. More, and the near subject doubles in size and
  leaves the frame; less, and the push is invisible.

Screen height of a subject: `h / (2·d·tan(fov/2))`. At `fov 55` that is `h / (0.976·d)` — a
1.85 m person at 4.5 m is 42 % of the frame. Design the layout from this number instead of
nudging the camera until it looks right.

## Fade and blur on the way out

Values are pushed into CSS custom properties; CSS does the compositing. Cheaper than a
`BokehPass` and it degrades to a plain fade:

```js
const out = Math.max(0, (p - 0.3) / 0.7);
root.style.setProperty('--scene-blur', `${(out * 7).toFixed(2)}px`);
root.style.setProperty('--scene-op', (1 - out * 0.92).toFixed(3));
```

`filter: blur()` on a full-screen canvas is the most expensive thing on the page. Cap it at
6–8 px and start it late (`p > 0.3`).

Native scroll plus a damped camera is indistinguishable from Lenis in feel, and it keeps the
keyboard, the trackpad and `scrollIntoView` working. Reach for a smooth-scroll library only
when the whole page must move as one transformed layer.

## Grade chain, in the order it must be applied

1. `outputColorSpace = SRGBColorSpace`, `toneMapping = ACESFilmicToneMapping`,
   `toneMappingExposure 1.2–1.4`, `powerPreference: 'high-performance'`,
   `pixelRatio = min(devicePixelRatio, 2)`.
2. One fog colour feeds both `scene.background` and `scene.fog`; mismatch shows a seam at the
   horizon.
3. CSS overlay: radial vignette + bottom gradient + `backdrop-filter` if you want a tint.
   This is where the "filmic" look comes from, and it costs nothing.
4. Composer: FXAA, bloom, vignette, output.
5. SVG `feTurbulence` grain at 3–6 % over everything.

**`renderer.physicallyCorrectLights` does not exist in r186.** It was removed; lights are
physical by default. Code copied from r15x lessons that sets it is a silent no-op (the
property is ignored), and any code that then compensates with huge intensities is fighting a
setting it no longer controls.

## Postprocessing on r186

`antialias` on the renderer does nothing once a composer exists, and the edges come back as
stairs. Chain:

```js
import { EffectComposer } from 'three/addons/postprocessing/EffectComposer.js';
import { RenderPass } from 'three/addons/postprocessing/RenderPass.js';
import { FXAAPass } from 'three/addons/postprocessing/FXAAPass.js';
import { UnrealBloomPass } from 'three/addons/postprocessing/UnrealBloomPass.js';
import { ShaderPass } from 'three/addons/postprocessing/ShaderPass.js';
import { VignetteShader } from 'three/addons/shaders/VignetteShader.js';
import { OutputPass } from 'three/addons/postprocessing/OutputPass.js';

composer.addPass(new RenderPass(scene, camera));
composer.addPass(new FXAAPass());                     // r186: its own pass, no manual resolution
composer.addPass(new UnrealBloomPass(new THREE.Vector2(w, h), 0.42, 0.75, 0.78));
const vig = new ShaderPass(VignetteShader);
vig.uniforms.offset.value = 1.0;
vig.uniforms.darkness.value = 1.12;
composer.addPass(vig);
composer.addPass(new OutputPass());                   // MUST be last
```

`OutputPass` does sRGB conversion **and** tone mapping. Drop it and the frame goes dark or
double-graded. Anything added after it works on an already-encoded image.

**Vendor gap.** `vendor/three/addons/` here ships only `controls`, `loaders`, `utils`. The
postprocessing chain is not there — copy it from
`knowledge/official_source/examples/jsm/{postprocessing,shaders}`, which is pinned to the same
r186 as the runtime:

```bash
SRC=knowledge/official_source/examples/jsm
cp $SRC/postprocessing/{EffectComposer,Pass,ShaderPass,MaskPass,RenderPass,OutputPass,FXAAPass,UnrealBloomPass}.js vendor/three/addons/postprocessing/
cp $SRC/shaders/{CopyShader,OutputShader,FXAAShader,VignetteShader,LuminosityHighPassShader}.js vendor/three/addons/shaders/
```

Taking them from another `node_modules/three` (e.g. the r185 copy inside `Mesh2Motion/`) is
the one thing not to do: the failure mode is a black frame, not an error.

## Gotchas, each one observed

- **Canvas `top: -1px`** — kills the 1 px seam under the canvas that appears once the page
  scrolls.
- **Plane `far` too large** costs depth precision and clips interiors; tune it to just past
  the last object (a compact exterior needs 200–400, not 1000).
- **`fov 55–60`** is the comfortable header range. 35 flattens the parallax, 90 fisheyes the
  frame edges.
- **A 3/4 view needs a real side wall.** A facade with nothing on its edges ends in mid-air
  the moment the camera leaves dead centre. Two perpendicular boxes and a roof slab fix it.
- **Keep a clear corridor to the light source.** A rubble field generated with uniform random
  placement will bury the doorway, which is the only thing the eye can land on. Exclude the
  corridor in the placement loop (`if (Math.abs(x) < 3.6 && z < front + 12) continue;`) and
  count the placed instances instead of `continue`-ing inside a fixed `for` — an unset
  instance matrix is identity, and the leftovers pile up at the origin.
- **Text belongs in HTML.** Signage rendered into generated art is gibberish, and a DOM
  headline stays sharp under the canvas blur.
- **Preloader must wait for the GLB**, not for `load`. `LoadingManager.onProgress` covers both
  textures and the mesh; `onLoad` fires once for the whole manager.
- **Normalise a generated mesh** before placing it: `Box3` → scale to the intended real
  height → re-measure → put `min.y` on the ground and centre x/z. Image-to-3D output arrives
  at an arbitrary scale and origin, and "the character is a 40 m giant floating in the sky"
  is the default, not an edge case.

## Making a procedural ruin read as a ruin

A facade built from `Shape` + holes is geometrically correct and still looks like a new build.
Four additions, all cheap, do most of the work:

- **Break the parapet, don't decorate it.** A 26 m straight top edge is the single line that
  reads "recent construction". Cut whole top-floor bays out of the *outline* (skip their window
  holes as well, or the hole ends up outside the boundary and earcut fails) and step the rest of
  the profile in courses — masonry comes off in blocks, so quantise the dip
  (`drop = t > 0.72 ? 2.3 : t > 0.4 ? 1.5 : t > 0.15 ? 0.7 : 0.3`). A smooth triangular notch
  reads as a design decision, not damage.
- **Soot above every opening.** One 32×128 canvas gradient on an `InstancedMesh` of quads:
  transparent at the top, `rgba(9,7,5,.78)` at the bottom, `destination-out` horizontal falloff
  so the quad edges never show, plus a few `destination-out` vertical fingers so it streaks
  instead of veiling. Clamp the plume height to the local wall top or it hangs in the sky.
  Keep `opacity ≤ 0.6` — above that it reads as fog on the wall.
- **Boarded-up windows.** Two or three `box()` planks per opening, slight random tilt
  (`±0.09 rad`), placed at `wallZ + depth + 0.05`. Nothing else says "people tried to keep
  something in" this cheaply.
- **Per-vertex vertical grime** on the wall: `k = 0.24 + 0.76 * pow(y / H, 0.62)`, then write it
  into a `color` attribute with `vertexColors = true`. Without it the elevation is flat
  cardboard; with it the base is dark and the parapet catches the last light.

## A sky plate needs its horizon placed, not just loaded

A `MeshBasicMaterial` plane at 100 units with `fog: false` is the cheapest backdrop, but the
image's own horizon lands wherever the plane centre is. With the camera at 1.7 m and the roof
at 10 m / 28 units away, everything below `y ≈ 1.7 + d·tan(16.5°)` is hidden behind the building:
a plate centred at `y = 16` at `z = -96` puts its sun, its skyline and its smoke *behind the
facade*, and only the empty haze strip at the top of the image is ever visible.

Rule of thumb: put the plate centre where the image's horizon should project — for a low sun
above a 10 m roof, `y ≈ 36` at 96 units — and size it to cover the frustum at that distance
(`half-height ≥ d·tan(fov/2)`), or the top of the frame falls back to `scene.background`.

## r186 API removals that fail silently

- `THREE.Clock` is deprecated (console warning only). Use `THREE.Timer` or, simplest, two
  `performance.now()` timestamps — the loop keeps working on every revision.
- `THREE.PCFSoftShadowMap` **was removed**: the renderer logs
  `PCFSoftShadowMap has been removed. Using PCFShadowMap instead.` and quietly switches. Set
  `PCFShadowMap` yourself so the shadow bias you tuned is the one that actually applies.
- `physicallyCorrectLights` is gone — light intensities are physical now, no flag to set.
