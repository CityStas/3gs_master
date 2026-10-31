---
name: UIDragDetectorResponseStyle
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Describes how the clicked GuiObject will be treated once the desired motion has been calculated."
---

# UIDragDetectorResponseStyle

Describes how the clicked [GuiObject](/docs/reference/engine/classes/GuiObject.md) will be treated once the desired
motion has been calculated.

**Type:** enum

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Offset` | 0 | Move by the [Offset](/docs/reference/engine/datatypes/UDim.md) values of the detector's parent's [GuiObject.Position](/docs/reference/engine/classes/GuiObject.md) value. |
| `Scale` | 1 | Move by the [Scale](/docs/reference/engine/datatypes/UDim.md) values of the detector's parent's [GuiObject.Position](/docs/reference/engine/classes/GuiObject.md) value. |
| `CustomOffset` | 2 | The UI element will not move at all, but the [Offset](/docs/reference/engine/datatypes/UDim.md) values of the detector's [DragUDim2](/docs/reference/engine/classes/UIDragDetector.md) will still be updated and the detector's events will still fire, allowing you to respond to drag manipulation however you'd like. |
| `CustomScale` | 3 | The UI element will not move at all, but the [Scale](/docs/reference/engine/datatypes/UDim.md) values of the detector's [DragUDim2](/docs/reference/engine/classes/UIDragDetector.md) will still be updated and the detector's events will still fire, allowing you to respond to drag manipulation however you'd like. |