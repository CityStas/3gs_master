---
name: WaterForce
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "The WaterForce Enum is used to work with Terrain water cells."
---

# WaterForce

The WaterForce Enum is used to work with [Terrain](/docs/reference/engine/classes/Terrain.md) water cells.

**Type:** enum

## Items

| Name | Value | Description |
|------|-------|-------------|
| `None` | 0 | No flow force on a legacy voxel terrain water cell; the water is still. |
| `Small` | 1 | A low flow force level of a legacy voxel terrain water cell. |
| `Medium` | 2 | A moderate flow force level of a legacy voxel terrain water cell, between [WaterForce.Small](/docs/reference/engine/enums/WaterForce.md) and [WaterForce.Strong](/docs/reference/engine/enums/WaterForce.md). |
| `Strong` | 3 | A high flow force level of a legacy voxel terrain water cell, one step below [WaterForce.Max](/docs/reference/engine/enums/WaterForce.md). |
| `Max` | 4 | The maximum flow force level of a legacy voxel terrain water cell. |