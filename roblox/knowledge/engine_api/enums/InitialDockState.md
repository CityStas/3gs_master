---
name: InitialDockState
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Describes the initial docking state of a DockWidgetPluginGui."
---

# InitialDockState

Describes the initial docking state of a [DockWidgetPluginGui](/docs/reference/engine/classes/DockWidgetPluginGui.md).

**Type:** enum

## Description

Specifies where a [DockWidgetPluginGui](/docs/reference/engine/classes/DockWidgetPluginGui.md) is initially positioned in
Roblox Studio when it is created for the first time. The value is supplied as
the `initialDockState` field of [DockWidgetPluginGuiInfo](/docs/reference/engine/datatypes/DockWidgetPluginGuiInfo.md), which is
passed to [Plugin:CreateDockWidgetPluginGuiAsync()](/docs/reference/engine/classes/Plugin.md). If Roblox Studio
has a saved layout entry for the plugin widget, that saved layout takes
precedence and this value is ignored;
[DockWidgetPluginGui.HostWidgetWasRestored](/docs/reference/engine/classes/DockWidgetPluginGui.md) is `true` in that case.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `Top` | 0 | The widget will appear docked above the game screen. |
| `Bottom` | 1 | The widget will appear docked below the game screen. |
| `Left` | 2 | The widget will appear docked to the left of the game screen. |
| `Right` | 3 | The widget will appear docked to the right of the game screen. |
| `Float` | 4 | The widget will not be docked to any side of the game screen, and instead can be freely dragged around. |