---
name: DragDetectorResponseStyle
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Describes how the clicked object will be treated once the desired motion has been calculated."
---

# DragDetectorResponseStyle

Describes how the clicked object will be treated once the desired motion has
been calculated.

**Type:** enum

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Geometric` | 0 | For an [Anchored](/docs/reference/engine/classes/BasePart.md) object both inside the running experience and in Studio edit mode, the position/orientation of the object will be updated to exactly reflect the proposed motion. For an unanchored object, behavior is the same as for an anchored object; however, in a running experience, the object will be anchored at the start of the drag and restored to unanchored upon drag release. |
| `Physical` | 1 | An [Anchored](/docs/reference/engine/classes/BasePart.md) object will default to **Geometric** behavior as it is not affected by forces. An unanchored object will be moved by constraint forces that attempt to bring it to the desired position and/or orientation given by the proposed motion. |
| `Custom` | 2 | The object will not move at all, but [DragFrame](/docs/reference/engine/classes/DragDetector.md) will still be updated and you can respond to drag manipulation however you'd like. |