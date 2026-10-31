---
name: RibbonTool
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Identifies a Studio ribbon toolbar tool, used with Plugin:GetSelectedRibbonTool() and Plugin:SelectRibbonTool()."
---

# RibbonTool

Identifies a Studio ribbon toolbar tool, used with
[Plugin:GetSelectedRibbonTool()](/docs/reference/engine/classes/Plugin.md) and [Plugin:SelectRibbonTool()](/docs/reference/engine/classes/Plugin.md).

**Type:** enum

## Description

[RibbonTool](/docs/reference/engine/enums/RibbonTool.md) represents the set of built-in tools available on the Roblox
Studio ribbon toolbar. Values from this enum are returned by
[Plugin:GetSelectedRibbonTool()](/docs/reference/engine/classes/Plugin.md) to identify which tool is currently
active, and passed to [Plugin:SelectRibbonTool()](/docs/reference/engine/classes/Plugin.md) to programmatically
activate a tool from a plugin script.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Select` | 0 | The **Select** tool, which selects objects in the viewport. |
| `Scale` | 1 | The **Scale** tool, which resizes selected parts along their axes. |
| `Rotate` | 2 | The **Rotate** tool, which rotates selected parts around the three primary axes. |
| `Move` | 3 | The **Move** tool, which translates selected parts along the three primary axes. |
| `Transform` | 4 | The **Transform** tool, which provides combined move, scale, and rotate handles in a single gizmo. |
| `ColorPicker` | 5 | The **Color** tool, which opens the color picker to paint the color of selected parts. |
| `MaterialPicker` | 6 | Deprecated ribbon **Color**/**Material** picker tool; use **Material Manager** instead. |
| `Group` | 7 | The **Group** tool, which groups the selected objects into a [Model](/docs/reference/engine/classes/Model.md). |
| `Ungroup` | 8 | The **Ungroup** tool, which dissolves a selected Model and promotes its children to the parent container. |
| `None` | 9 | Represents no ribbon tool being active. |
| `PivotEditor` | 10 | The **Edit Pivot** tool, which repositions the pivot point of selected parts or models. |