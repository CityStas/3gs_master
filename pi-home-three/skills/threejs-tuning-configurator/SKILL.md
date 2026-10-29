---
name: threejs-tuning-configurator
description: "GTA-style garage and part configurator on a loaded glTF: detach each part in the browser, explode views, swap variants, tune a vehicle or prop. Use when the task is to take a model apart, build a garage, or tune a car. Covers Blender pre-split, pivots, spring-damper detach, ghost holograms, variant swap and MSAA EffectComposer pitfalls. Русские триггеры: «разобрать модель на детали», «гараж», «конфигуратор машины», «менять детали», «тюнинг»."
---

# Vehicle / prop Tuning Configurator

Use when the task is "detach each part of a model in the browser, swap parts, tune it" -
a GTA-style garage / configurator built on a loaded glTF.

## Retrieval order

1. `knowledge/cookbook/blender_split_parts_to_glb.md` - how the asset must be prepared
   (split by material, explicit pivots, hinge derivation, dedup, GLB + manifest export).
2. `knowledge/cookbook/threejs_part_configurator.md` - the runtime: part registry,
   spring-damper detach/explode, ghost holograms, variant swap, MSAA `EffectComposer`.
3. `knowledge/cookbook/procedural_car_parts.md` - variant parts built from primitives
   (rims, spoilers, exhaust tips, plates) and their local-frame conventions.

## Non-negotiables

- The split happens in Blender **before** export. Never split a monolithic mesh at runtime.
- One node per part, origin rebased to the pivot. Pivot = hub centre for wheels, rear-top
  edge for pop-up headlight pods.
- `new EffectComposer(renderer)` alone creates a non-multisampled target → dashed panel
  seams. Always pass a `WebGLRenderTarget({ samples: 4 })`.
- `mergeGeometries` returns `null` for mixed indexed/non-indexed input; normalise with
  `toNonIndexed()` first.
- World-space measurements require `updateMatrixWorld(true)` and
  `applyMatrix4(mesh.matrixWorld)`. Local bboxes are the source of most placement bugs.
- Dispose swapped-out geometry. A garage UI cycles variants hundreds of times per session.
- Verify with a deterministic `settle()` hook, not wall-clock frames - software rasterisers
  run too slowly for the spring integrator to converge.

## Verification

Assert on semantic state (pop-up angle in radians, `detached` count, `procRims.size`,
wing bbox above the deck) and on `gl.readPixels` coverage. Screenshots are for humans,
assertions are for CI. A scene that throws in the render loop still screenshots clean.
