---
name: SelectionBehavior
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Customization options for gamepad selection when GuiBase2d.SelectionGroup is true."
---

# SelectionBehavior

Customization options for gamepad selection when
[GuiBase2d.SelectionGroup](/docs/reference/engine/classes/GuiBase2d.md) is true.

**Type:** enum

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Escape` | 0 | Prioritizes GuiObjects within the same SelectionGroup but allows the selection to move to other outside GuiObjects if no suitable button is found. |
| `Stop` | 1 | Constrains gamepad selection to the SelectionGroup. |