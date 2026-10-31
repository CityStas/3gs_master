---
name: ModelLevelOfDetail
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Controls the level of detail for Models in experiences with instance streaming enabled."
---

# ModelLevelOfDetail

Controls the level of detail for [Models](/docs/reference/engine/classes/Model.md) in experiences with
instance streaming enabled.

**Type:** enum

## Description

Controls the level of detail for [Models](/docs/reference/engine/classes/Model.md) in experiences with
instance [streaming](/docs/en-us/workspace/streaming.md) enabled. Composite
or imposter meshes do not support physics, collision detection, or raycasting.

| _Original model_ | _Lightweight SLIM mesh_ | _Low-res "imposter" mesh_ |
| --- | --- | --- |

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Automatic` | 0 | Default behavior, currently equivalent to `Disabled`. |
| `StreamingMesh` | 1 | A lower resolution "imposter" mesh (colored, coarse mesh that wraps around all child parts of the model) renders outside the streaming radius. Does not support textures. |
| `Disabled` | 2 | A lower resolution mesh will not be displayed. |
| `SLIM` | 4 | A **SLIM** model (Scalable Lightweight Interactive Model) renders a composite of all child parts at progressively lower resolutions at distances based on the streaming radius. Greatly improves visual quality over `StreamingMesh`. |