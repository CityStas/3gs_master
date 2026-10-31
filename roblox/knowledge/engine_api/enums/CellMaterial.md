---
name: CellMaterial
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Material values for individual cells in the deprecated legacy voxel-based Terrain engine."
---

# CellMaterial

Material values for individual cells in the deprecated legacy voxel-based
[Terrain](/docs/reference/engine/classes/Terrain.md) engine.

**Type:** enum

## Description

Deprecated. Material values for individual cells in the legacy voxel-based
[Terrain](/docs/reference/engine/classes/Terrain.md) engine. These values were passed to the deprecated
[Terrain:SetCell()](/docs/reference/engine/classes/Terrain.md) and [Terrain:SetCells()](/docs/reference/engine/classes/Terrain.md) methods. When a
legacy place is loaded, the engine converts these cell materials to their
closest equivalents in the modern smooth terrain system. Use [Material](/docs/reference/engine/enums/Material.md)
with the current terrain APIs instead.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Empty` | 0 | Represents an air (unfilled) cell in the legacy voxel terrain; converted to air in the modern terrain system. |
| `Grass` | 1 | A green grassy cell material in the legacy voxel terrain, converted to [Material.Grass](/docs/reference/engine/enums/Material.md) in the modern terrain system. |
| `Sand` | 2 | A sandy cell material in the legacy voxel terrain, converted to [Material.Sand](/docs/reference/engine/enums/Material.md) in the modern terrain system. |
| `Brick` | 3 | A red brick cell material in the legacy voxel terrain, converted to [Material.Brick](/docs/reference/engine/enums/Material.md) in the modern terrain system. |
| `Granite` | 4 | A speckled stone cell material in the legacy voxel terrain, converted to [Material.Slate](/docs/reference/engine/enums/Material.md) in the modern terrain system. |
| `Asphalt` | 5 | A dark paved road cell material in the legacy voxel terrain, converted to [Material.Asphalt](/docs/reference/engine/enums/Material.md) in the modern terrain system. |
| `Iron` | 6 | A dark metallic cell material in the legacy voxel terrain, converted to [Material.Concrete](/docs/reference/engine/enums/Material.md) in the modern terrain system. |
| `Aluminum` | 7 | A metallic silver cell material in the legacy voxel terrain, converted to [Material.Concrete](/docs/reference/engine/enums/Material.md) in the modern terrain system. |
| `Gold` | 8 | A golden metallic cell material in the legacy voxel terrain, converted to [Material.Concrete](/docs/reference/engine/enums/Material.md) in the modern terrain system. |
| `WoodPlank` | 9 | A flat wooden plank cell material in the legacy voxel terrain, converted to [Material.WoodPlanks](/docs/reference/engine/enums/Material.md) in the modern terrain system. |
| `WoodLog` | 10 | A round wooden log cell material in the legacy voxel terrain, converted to [Material.WoodPlanks](/docs/reference/engine/enums/Material.md) in the modern terrain system. |
| `Gravel` | 11 | A loose-stone cell material in the legacy voxel terrain, converted to [Material.Asphalt](/docs/reference/engine/enums/Material.md) in the modern terrain system. |
| `CinderBlock` | 12 | A rough masonry cell material in the legacy voxel terrain, converted to [Material.Concrete](/docs/reference/engine/enums/Material.md) in the modern terrain system. |
| `MossyStone` | 13 | A weathered stone cell material in the legacy voxel terrain, converted to [Material.Pavement](/docs/reference/engine/enums/Material.md) in the modern terrain system. |
| `Cement` | 14 | A gray cement cell material in the legacy voxel terrain, converted to [Material.Concrete](/docs/reference/engine/enums/Material.md) in the modern terrain system. |
| `RedPlastic` | 15 | A red-tinted cell material in the legacy voxel terrain, converted to [Material.Sandstone](/docs/reference/engine/enums/Material.md) in the modern terrain system. |
| `BluePlastic` | 16 | A blue-tinted cell material in the legacy voxel terrain, converted to [Material.Ice](/docs/reference/engine/enums/Material.md) in the modern terrain system. |
| `Water` | 17 | A water-filled cell in the legacy voxel terrain, converted to [Material.Water](/docs/reference/engine/enums/Material.md) in the modern terrain system. |