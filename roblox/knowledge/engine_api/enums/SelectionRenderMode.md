---
name: SelectionRenderMode
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Controls how selected objects are highlighted in Roblox Studio."
---

# SelectionRenderMode

Controls how selected objects are highlighted in Roblox Studio.

**Type:** enum

## Description

Specifies the visual style used to highlight selected objects in Roblox
Studio. This enum is used by the `RenderMode` property, which defaults to
[SelectionRenderMode.Outlines](/docs/reference/engine/enums/SelectionRenderMode.md).

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Outlines` | 0 | Renders selected objects using an outline drawn along each object's edges. |
| `BoundingBoxes` | 1 | Renders selected objects using a bounding box drawn around each object's extents. |
| `Both` | 2 | Renders selected objects with both outlines and bounding boxes simultaneously. |