---
name: UIDragDetectorBoundingBehavior
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Used with UIDragDetector to determine bounding behavior of the dragged UI object when UIDragDetector.BoundingUI is set."
---

# UIDragDetectorBoundingBehavior

Used with [UIDragDetector](/docs/reference/engine/classes/UIDragDetector.md) to determine bounding behavior of the dragged
UI object when [UIDragDetector.BoundingUI](/docs/reference/engine/classes/UIDragDetector.md) is set.

**Type:** enum

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Automatic` | 0 | Mimics **EntireObject** behavior for a UI object that's entirely contained by the [BoundingUI](/docs/reference/engine/classes/UIDragDetector.md), or else **HitPoint** for a UI object that's partially outside the [BoundingUI](/docs/reference/engine/classes/UIDragDetector.md). |
| `EntireObject` | 1 | Bounds the entire dragged UI object within the [BoundingUI](/docs/reference/engine/classes/UIDragDetector.md). |
| `HitPoint` | 2 | Bounds the dragged UI only by the exact hit/grab point and its respective position after translation/rotation. |