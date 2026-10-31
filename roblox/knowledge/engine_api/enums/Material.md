---
name: Material
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Materials used for parts and/or terrain."
---

# Material

Materials used for parts and/or terrain.

**Type:** enum

## Description

The following base materials are used for [parts](/docs/en-us/parts.md)
and/or [terrain](/docs/en-us/parts/terrain.md). See the
[Materials](/docs/en-us/parts/materials.md) guide for more details on using and
modifying materials.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Plastic` | 256 | Applies to [BasePart](/docs/reference/engine/classes/BasePart.md) only. |
| `SmoothPlastic` | 272 | Applies to [BasePart](/docs/reference/engine/classes/BasePart.md) only. |
| `Neon` | 288 | Applies to [BasePart](/docs/reference/engine/classes/BasePart.md) only. |
| `Wood` | 512 | Applies to [BasePart](/docs/reference/engine/classes/BasePart.md) only. |
| `WoodPlanks` | 528 | Applies to [BasePart](/docs/reference/engine/classes/BasePart.md) and [Terrain](/docs/reference/engine/classes/Terrain.md). |
| `Marble` | 784 | Applies to [BasePart](/docs/reference/engine/classes/BasePart.md) only. |
| `Basalt` | 788 | Applies to [BasePart](/docs/reference/engine/classes/BasePart.md) and [Terrain](/docs/reference/engine/classes/Terrain.md). |
| `Slate` | 800 | Applies to [BasePart](/docs/reference/engine/classes/BasePart.md) and [Terrain](/docs/reference/engine/classes/Terrain.md). |
| `CrackedLava` | 804 | Applies to [BasePart](/docs/reference/engine/classes/BasePart.md) and [Terrain](/docs/reference/engine/classes/Terrain.md). |
| `Concrete` | 816 | Applies to [BasePart](/docs/reference/engine/classes/BasePart.md) and [Terrain](/docs/reference/engine/classes/Terrain.md). |
| `Limestone` | 820 | Applies to [BasePart](/docs/reference/engine/classes/BasePart.md) and [Terrain](/docs/reference/engine/classes/Terrain.md). |
| `Granite` | 832 | Applies to [BasePart](/docs/reference/engine/classes/BasePart.md) only. |
| `Pavement` | 836 | Applies to [BasePart](/docs/reference/engine/classes/BasePart.md) and [Terrain](/docs/reference/engine/classes/Terrain.md). |
| `Brick` | 848 | Applies to [BasePart](/docs/reference/engine/classes/BasePart.md) and [Terrain](/docs/reference/engine/classes/Terrain.md). |
| `Pebble` | 864 | Applies to [BasePart](/docs/reference/engine/classes/BasePart.md) only. |
| `Cobblestone` | 880 | Applies to [BasePart](/docs/reference/engine/classes/BasePart.md) and [Terrain](/docs/reference/engine/classes/Terrain.md). |
| `Rock` | 896 | Applies to [BasePart](/docs/reference/engine/classes/BasePart.md) and [Terrain](/docs/reference/engine/classes/Terrain.md). |
| `Sandstone` | 912 | Applies to [BasePart](/docs/reference/engine/classes/BasePart.md) and [Terrain](/docs/reference/engine/classes/Terrain.md). |
| `CorrodedMetal` | 1040 | Applies to [BasePart](/docs/reference/engine/classes/BasePart.md) only. |
| `DiamondPlate` | 1056 | Applies to [BasePart](/docs/reference/engine/classes/BasePart.md) only. |
| `Foil` | 1072 | Applies to [BasePart](/docs/reference/engine/classes/BasePart.md) only. |
| `Metal` | 1088 | Applies to [BasePart](/docs/reference/engine/classes/BasePart.md) only. |
| `Grass` | 1280 | Applies to [BasePart](/docs/reference/engine/classes/BasePart.md) and [Terrain](/docs/reference/engine/classes/Terrain.md). |
| `LeafyGrass` | 1284 | Applies to [BasePart](/docs/reference/engine/classes/BasePart.md) and [Terrain](/docs/reference/engine/classes/Terrain.md). |
| `Sand` | 1296 | Applies to [BasePart](/docs/reference/engine/classes/BasePart.md) and [Terrain](/docs/reference/engine/classes/Terrain.md). |
| `Fabric` | 1312 | Applies to [BasePart](/docs/reference/engine/classes/BasePart.md) only. |
| `Snow` | 1328 | Applies to [BasePart](/docs/reference/engine/classes/BasePart.md) and [Terrain](/docs/reference/engine/classes/Terrain.md). |
| `Mud` | 1344 | Applies to [BasePart](/docs/reference/engine/classes/BasePart.md) and [Terrain](/docs/reference/engine/classes/Terrain.md). |
| `Ground` | 1360 | Applies to [BasePart](/docs/reference/engine/classes/BasePart.md) and [Terrain](/docs/reference/engine/classes/Terrain.md). |
| `Asphalt` | 1376 | Applies to [BasePart](/docs/reference/engine/classes/BasePart.md) and [Terrain](/docs/reference/engine/classes/Terrain.md). |
| `Salt` | 1392 | Applies to [BasePart](/docs/reference/engine/classes/BasePart.md) and [Terrain](/docs/reference/engine/classes/Terrain.md). |
| `Ice` | 1536 | Applies to [BasePart](/docs/reference/engine/classes/BasePart.md) and [Terrain](/docs/reference/engine/classes/Terrain.md). |
| `Glacier` | 1552 | Applies to [BasePart](/docs/reference/engine/classes/BasePart.md) and [Terrain](/docs/reference/engine/classes/Terrain.md). |
| `Glass` | 1568 | Applies to [BasePart](/docs/reference/engine/classes/BasePart.md) only. Note that refraction of light through this material is not supported on mobile devices due to computational limitations. |
| `ForceField` | 1584 | Must be used on a [MeshPart](/docs/reference/engine/classes/MeshPart.md) with UVs laid out to cover much of the 0:1 UV space or more (larger is better). The [MeshPart](/docs/reference/engine/classes/MeshPart.md) must also have a texture applied to its [TextureID](/docs/reference/engine/classes/MeshPart.md), and that texture image must have a wide value range since the material displays the range from dark/black to light/white values. Obtain [this model](https://create.roblox.com/store/asset/15507769146/ForceFieldMesh) for a functional example. |
| `Air` | 1792 | Applies to [Terrain](/docs/reference/engine/classes/Terrain.md) only. |
| `Water` | 2048 | Applies to [Terrain](/docs/reference/engine/classes/Terrain.md) only. |
| `Cardboard` | 2304 | Applies to [BasePart](/docs/reference/engine/classes/BasePart.md) only. |
| `Carpet` | 2305 | Applies to [BasePart](/docs/reference/engine/classes/BasePart.md) only. |
| `CeramicTiles` | 2306 | Applies to [BasePart](/docs/reference/engine/classes/BasePart.md) only. |
| `ClayRoofTiles` | 2307 | Applies to [BasePart](/docs/reference/engine/classes/BasePart.md) only. |
| `RoofShingles` | 2308 | Applies to [BasePart](/docs/reference/engine/classes/BasePart.md) only. |
| `Leather` | 2309 | Applies to [BasePart](/docs/reference/engine/classes/BasePart.md) only. |
| `Plaster` | 2310 | Applies to [BasePart](/docs/reference/engine/classes/BasePart.md) only. |
| `Rubber` | 2311 | Applies to [BasePart](/docs/reference/engine/classes/BasePart.md) only. |