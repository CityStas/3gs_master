---
name: TerrainAcquisitionMethod
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Describes how terrain in a place was originally created or last substantially modified."
---

# TerrainAcquisitionMethod

Describes how terrain in a place was originally created or last substantially
modified.

**Type:** enum

## Description

Describes how the terrain in a place was originally created or last
substantially modified. This value is stored on the `AcquisitionMethod`
property of [Terrain](/docs/reference/engine/classes/Terrain.md) and is updated automatically by the engine
whenever terrain changes.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `None` | 0 | No terrain is present, or terrain acquisition method has not been recorded. |
| `Legacy` | 1 | Terrain was deserialized from a place file that predates acquisition-method tracking. |
| `Template` | 2 | Terrain was loaded from a Studio place template. |
| `Generate` | 3 | Terrain was created using the Studio terrain generator. |
| `Import` | 4 | Terrain was created by importing a heightmap or colormap image via the Studio terrain importer. |
| `Convert` | 5 | Terrain was created by converting legacy smooth terrain from an older place format. |
| `EditAddTool` | 6 | Terrain was created or last modified using the Studio terrain editor's Add tool. |
| `EditSeaLevelTool` | 7 | Terrain was created or last modified using the Studio terrain editor's Sea Level tool. |
| `EditReplaceTool` | 8 | Terrain was created or last modified using the Studio terrain editor's Replace tool. |
| `RegionFillTool` | 9 | Terrain was created or last modified using the Studio terrain editor's Fill region tool. |
| `RegionPasteTool` | 10 | Terrain was created or last modified by pasting a previously copied terrain region in the Studio terrain editor. |
| `Other` | 11 | Terrain was created or modified by an untracked method, such as a third-party plugin. |