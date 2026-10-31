---
name: TerrainFace
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Identifies which face direction of a terrain voxel a TerrainDetail object overrides."
---

# TerrainFace

Identifies which face direction of a terrain voxel a [TerrainDetail](/docs/reference/engine/classes/TerrainDetail.md)
object overrides.

**Type:** enum

## Description

Identifies which face direction of a terrain voxel a [TerrainDetail](/docs/reference/engine/classes/TerrainDetail.md)
object targets. Terrain renders its top (+Y), side (horizontal), and bottom
(-Y) faces independently; this enum lets each [TerrainDetail](/docs/reference/engine/classes/TerrainDetail.md) child of a
[MaterialVariant](/docs/reference/engine/classes/MaterialVariant.md) declare which of those three surfaces it overrides.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Top` | 0 | The top (+Y) face of a terrain voxel. |
| `Side` | 1 | The horizontal (side) faces of a terrain voxel, perpendicular to the Y axis. |
| `Bottom` | 2 | The bottom (-Y) face of a terrain voxel. |