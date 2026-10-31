---
name: UIDragDetectorDragSpace
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Used with DragDetector to set the paradigm which defines the space of inputs/outputs from a custom drag function."
---

# UIDragDetectorDragSpace

Used with [DragDetector](/docs/reference/engine/classes/DragDetector.md) to set the paradigm which defines the space of
inputs/outputs from a custom drag function.

**Type:** enum

## Description

Used with [DragDetector](/docs/reference/engine/classes/DragDetector.md) to set the paradigm which defines the space of
inputs/outputs from a custom drag function registered through
[SetDragStyleFunction()](/docs/reference/engine/classes/UIDragDetector.md) or
[AddConstraintFunction()](/docs/reference/engine/classes/UIDragDetector.md).

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Parent` | 0 | Designates the input and return values' space as the local space of the detector's parent [GuiObject](/docs/reference/engine/classes/GuiObject.md). |
| `LayerCollector` | 1 | Designates the input and return values' space as that of the [LayerCollector](/docs/reference/engine/classes/LayerCollector.md). |
| `Reference` | 2 | Designates the input and return values' space as that of the [ReferenceUIInstance](/docs/reference/engine/classes/UIDragDetector.md). For [DragRelativity](/docs/reference/engine/classes/UIDragDetector.md) and [DragUDim2](/docs/reference/engine/classes/UIDragDetector.md) purposes, the `(0, 0)` origin is the absolute center position of the [ReferenceUIInstance](/docs/reference/engine/classes/UIDragDetector.md).  If [ReferenceUIInstance](/docs/reference/engine/classes/UIDragDetector.md) is not `nil`, this will behave the same as **Parent**. |