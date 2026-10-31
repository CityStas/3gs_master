---
name: DeveloperMemoryTag
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "A memory tracking category."
---

# DeveloperMemoryTag

A memory tracking category.

**Type:** enum

## Description

A list of memory categories, and a description of what they are allocated to.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Internal` | 0 | General data that doesn't have any categorization. This could be due to either internal reasons, or because it simply isn't being tracked categorically. |
| `HttpCache` | 1 | A cache of HTTP responses. |
| `Instances` | 2 | All the Instances present in memory. |
| `Signals` | 3 | Events, signals, connections, etc. |
| `LuaHeap` | 4 | All of the data in Luau, including everything happening in core scripts, built-in data types, etc. |
| `Script` | 5 | All memory being manipulated and referenced by scripts. |
| `PhysicsCollision` | 6 | Collision detection in the [Workspace](/docs/reference/engine/classes/Workspace.md). |
| `BaseParts` | 7 | 3D parts used for simulation. |
| `GraphicsSolidModels` | 8 | Rendering solid models (stuff made with Union, Negate, etc.). |
| `GraphicsMeshParts` | 10 | Rendering of mesh parts. |
| `GraphicsParticles` | 11 | Rendering of particles from ParticleEmitters. |
| `GraphicsParts` | 12 | Rendering of regular parts. |
| `GraphicsSpatialHash` | 13 | Spatial hash lookup tables of the game world that are used for rendering. |
| `GraphicsTerrain` | 14 | Rendering of terrain geometry. |
| `GraphicsTexture` | 15 | Rendering of textures in the game world. |
| `GraphicsTextureCharacter` | 16 | Rendering of texture composition maps that are generated for Humanoids. |
| `Sounds` | 17 | Data of sounds in-game. |
| `StreamingSounds` | 18 | Playback of sounds in-game. |
| `TerrainVoxels` | 19 | Occupancy/Material data of the Terrain. |
| `Gui` | 21 | Gui element data and rendering. |
| `Animation` | 22 | Playback of Animations on Humanoids and AnimationControllers. |
| `Navigation` | 23 | Pathfinding for Humanoids via the PathfindingService. |
| `GeometryCSG` | 24 | Geometry mesh data for CSG objects such as [UnionOperation](/docs/reference/engine/classes/UnionOperation.md) and [PartOperation](/docs/reference/engine/classes/PartOperation.md). |
| `GraphicsSlimModels` | 25 | Rendering memory for SLIM (streamed level-of-detail instance mesh) model data. |