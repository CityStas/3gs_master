---
name: UIDragDetectorDragStyle
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Used with UIDragDetector as the paradigm to generate proposed motion, given a stream of input position vectors."
---

# UIDragDetectorDragStyle

Used with [UIDragDetector](/docs/reference/engine/classes/UIDragDetector.md) as the paradigm to generate proposed motion,
given a stream of input position vectors.

**Type:** enum

## Items

| Name | Value | Description |
|------|-------|-------------|
| `TranslatePlane` | 0 | 2D motion in the plane of the [LayerCollector](/docs/reference/engine/classes/LayerCollector.md). |
| `TranslateLine` | 1 | 1D motion along the detector's [DragAxis](/docs/reference/engine/classes/UIDragDetector.md). |
| `Rotate` | 2 | By default, rotation about the absolute center position of the detector's parent [GuiObject](/docs/reference/engine/classes/GuiObject.md). If [ReferenceUIInstance](/docs/reference/engine/classes/UIDragDetector.md) is set, rotation happens about that instance's absolute center position. |
| `Scriptable` | 3 | Calculates desired motion via a custom function provided through [SetDragStyleFunction()](/docs/reference/engine/classes/UIDragDetector.md). |