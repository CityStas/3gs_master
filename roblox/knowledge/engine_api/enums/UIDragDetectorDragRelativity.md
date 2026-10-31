---
name: UIDragDetectorDragRelativity
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Used with DragDetector to set the paradigm which defines the relativity of inputs/outputs from a custom drag function."
---

# UIDragDetectorDragRelativity

Used with [DragDetector](/docs/reference/engine/classes/DragDetector.md) to set the paradigm which defines the
relativity of inputs/outputs from a custom drag function.

**Type:** enum

## Description

Used with [DragDetector](/docs/reference/engine/classes/DragDetector.md) to set the paradigm which defines the
relativity of inputs/outputs from a custom drag function registered through
[SetDragStyleFunction()](/docs/reference/engine/classes/UIDragDetector.md) or
[AddConstraintFunction()](/docs/reference/engine/classes/UIDragDetector.md).

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Absolute` | 0 | Designates the input and return values as the absolute target position/rotation in the space defined by [DragSpace](/docs/reference/engine/classes/UIDragDetector.md). |
| `Relative` | 1 | Designates the input and return values as the change from the current position/rotation in the space defined by [DragSpace](/docs/reference/engine/classes/UIDragDetector.md). |