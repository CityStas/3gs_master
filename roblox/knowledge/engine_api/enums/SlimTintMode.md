---
name: SlimTintMode
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Determines the color-coding mode used by the SLIM debug tint overlay in the Developer Console."
---

# SlimTintMode

Determines the color-coding mode used by the SLIM debug tint overlay in the
Developer Console.

**Type:** enum

## Description

Determines the color-coding mode used by the SLIM debug tint overlay. Select a
mode via the **DebugVisualizations** panel in the Developer Console to
color-code meshes by different criteria.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `None` | 0 | No tint is applied. Meshes render with their normal appearance. |
| `LevelOfDetail` | 1 | Colors each mesh by its current level of detail. Blue is the coarsest, red the finest, and every rank in between maps to a fixed color. A given color always means the same LOD rank across every mesh, with the exception that each mesh's own highest available LOD is always shown red. |
| `DataModelState` | 5 | Colors SLIM models by whether their DataModel instances are streamed in or out. Green indicates streamed in (full DataModel present); yellow indicates streamed out (a placeholder). Both are still rendered via SLIM. |
| `TranscoderStatus` | 6 | Colors each SLIM model by its [SlimTranscoderStatus](/docs/reference/engine/enums/SlimTranscoderStatus.md). Follow the link to see which color maps to each status. |