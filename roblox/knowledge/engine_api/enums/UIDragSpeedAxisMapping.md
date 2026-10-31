---
name: UIDragSpeedAxisMapping
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Used with UIDragDetector.UIDragSpeedAxisMapping to determine the **X**/**Y** dimension dragging speeds."
---

# UIDragSpeedAxisMapping

Used with [UIDragDetector.UIDragSpeedAxisMapping](/docs/reference/engine/classes/UIDragDetector.md) to determine the
**X**/**Y** dimension dragging speeds.

**Type:** enum

## Description

Used with [UIDragDetector.UIDragSpeedAxisMapping](/docs/reference/engine/classes/UIDragDetector.md) to determine the
**X**/**Y** dimension dragging speeds, based on the detector's
[SelectionModeDragSpeed](/docs/reference/engine/classes/UIDragDetector.md).

## Items

| Name | Value | Description |
|------|-------|-------------|
| `XY` | 0 | Default setting for a detector's [UIDragSpeedAxisMapping](/docs/reference/engine/classes/UIDragDetector.md) where the **X** and **Y** axis speeds are based off the **X** and **Y** [Scale](/docs/reference/engine/datatypes/UDim.md)/[Offset](/docs/reference/engine/datatypes/UDim.md) values respectively. |
| `XX` | 1 | Both the **X** and **Y** axis speeds are based off the **X** axis for [Scale](/docs/reference/engine/datatypes/UDim.md), while the [Offset](/docs/reference/engine/datatypes/UDim.md) values still apply to their respective axis. |
| `YY` | 2 | Both the **X** and **Y** axis speeds are based off the **Y** axis for [Scale](/docs/reference/engine/datatypes/UDim.md), while the [Offset](/docs/reference/engine/datatypes/UDim.md) values still apply to their respective axis. |