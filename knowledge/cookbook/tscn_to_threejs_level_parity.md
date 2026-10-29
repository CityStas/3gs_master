# Reusing a Godot scene as the level source for a three.js runtime

## When to use

A 2D game already exists as a Godot project (`Main.tscn` + `scripts/*.gd`) and is being
continued in three.js — either because the target is the web, or because the level is being
authored on top of the existing one. You want the *same* geometry in both, and you want to be
able to prove it.

Do not hand-port the scene. Hand-porting produces a second source of truth, and the moment
the two drift the port stops being a port.

## The pipeline

```
Main.tscn ──(tools/tscn2json.py)──> web3d/level.json ──(web3d/scene.js)──> three.js scene
```

`tscn2json.py` walks the `.tscn` text format and emits the *same tree* the scene declares:
node name, type, `path`, and the `props` that matter for rendering (position, scale,
rotation, texture, z_index, flip_h, shape, polygon, camera limits). `scene.js` builds one
`Object3D` per node, recursively, from that JSON. Nothing in the runtime reads `.tscn`.

Why a JSON intermediate rather than a loader: the JSON is diffable. `git diff` on
`level.json` shows exactly which node moved, which is how a lost node is caught.

## Preserve the coordinate system

Compute all game logic in **Godot coordinates** (y grows downward) and convert to three.js in
exactly one place — when writing a group's position:

```js
group.position.set(x, -y, 0);
```

Every constant then matches `player.gd` / `enemy.gd` line for line, and a number read in the
`.tscn` can be compared with the running game without a mental transform. Inverting y in
several places is how sign bugs become permanent.

## z_index → draw order

```js
const depth = parentDepth + (node.z_index ?? 0);
mesh.renderOrder = depth;                 // higher = drawn later = in front
```

Parallax roots need their own mapping, because their `z_index` is a layer index rather than a
scene depth, and the parallax layers of a hand-built level are often given *large negative*
`z_index` (-100, -99, -98) that would still be behind everything if taken literally.
Override them explicitly by node name:

```js
function layerDepth(name, scrollScale) { /* far/mid/gameplay → fixed depths */ }
```

## Collision: two shapes, two interpretations

`CollisionShape2D` under a `StaticBody2D` is a rectangle → an AABB. `CollisionPolygon2D` under
a `StaticBody2D` is **not** an obstacle to be navigated around — it is the terrain
*surface profile*. Build it as a heightfield by scanning columns for the minimum y among edge
intersections, and treat everything below as solid:

```js
terrainAt(x) -> surfaceY | null       // null = cliff, the only way to have a hole
```

A general polygon solver here is worse than useless: it makes the character snag on the
terrain's own interior edges and it cannot express "the ground is infinitely deep", which is
what a platformer wants. Keep AABBs for genuine walls, ceilings and platforms.

Note that `Area2D` children (hit areas, arena triggers, pickups) must be **excluded** from
solid collision. Walking the tree, propagate an `inBody` flag and only start collecting
shapes under a `StaticBody2D`.

## Order of operations in the actor step

Move **X first, then Y**, and resolve X with a step-up allowance:

```
1. X: probe the terrain across the body's width at the new x.
   - any column higher than (feet - STEP_UP)  -> wall, cancel vx
   - otherwise snap feet to the highest column within the step band
2. Y: gravity, then land on the highest surface crossed between prev_feet and feet
```

Reversed, a character walking up a slope first "stands" at the new height and then collides
with it sideways and sticks.

`STEP_UP` (≈20 px) is mandatory for a profile derived from art: the profile is a curve, not a
staircase, and without the allowance the character catches on every pixel of it.

## Make the manifest un-cacheable

`levels.json` (the level list) and the level JSON itself are **content that is edited by
hand**. A browser will happily serve the old one and you will debug a change that is not
running:

```js
await fetch(manifestUrl, { cache: 'no-cache' });
```

## Verify parity, do not assume it

- Compare the node count and per-node `z_index` between the `.tscn` and the JSON.
- Keep the parity viewer (a page that renders `level.json` with the camera and inspector)
  separate from the game page. Merging them means the viewer stops being a clean
  "does the JSON equal the scene" check and the game starts depending on debug toggles.
- **`Main.tscn` loses nodes when saved from the Godot editor.** A sibling node was dropped
  once and had to be restored in a later commit. Before editing the scene, run
  `git diff HEAD -- Main.tscn` and reconcile the node list.

## When there is no Godot scene at all

A generated level has no `.tscn`. Write a builder that emits the **same JSON shape** the
parser emits (`tools/level_build.py` in the reference project). Then `scene.js` builds both
levels with the same code and no second rendering path appears. That is the whole reason the
intermediate format is worth having.
