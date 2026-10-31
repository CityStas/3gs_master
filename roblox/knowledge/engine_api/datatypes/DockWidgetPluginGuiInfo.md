---
name: DockWidgetPluginGuiInfo
last_updated: 2026-10-30T19:55:54Z
type: datatype
summary: "Describes details for a DockWidgetPluginGui."
---

# DockWidgetPluginGuiInfo

Describes details for a [DockWidgetPluginGui](/docs/reference/engine/classes/DockWidgetPluginGui.md).

**Type:** datatype

## Description

The [DockWidgetPluginGuiInfo](/docs/reference/engine/datatypes/DockWidgetPluginGuiInfo.md) data type describes details for a
[DockWidgetPluginGui](/docs/reference/engine/classes/DockWidgetPluginGui.md). This data type is used when constructing a
[PluginGui](/docs/reference/engine/classes/PluginGui.md) via the plugin's
[Plugin:CreateDockWidgetPluginGuiAsync()](/docs/reference/engine/classes/Plugin.md) method.

## Constructors

### DockWidgetPluginGuiInfo.new

**Signature:** `DockWidgetPluginGuiInfo.new(InitialDockState?: InitialDockState, InitialEnabled?: bool, InitialEnabledShouldOverrideRestore?: bool, FloatingXSize?: number, FloatingYSize?: number, MinWidth?: number, MinHeight?: number)`

The main constructor function for the [DockWidgetPluginGuiInfo](/docs/reference/engine/datatypes/DockWidgetPluginGuiInfo.md).

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `InitialDockState` | `InitialDockState` | `Enum.InitialDockState.Right` |  |
| `InitialEnabled` | `bool` | `false` |  |
| `InitialEnabledShouldOverrideRestore` | `bool` | `false` |  |
| `FloatingXSize` | `number` | `0` |  |
| `FloatingYSize` | `number` | `0` |  |
| `MinWidth` | `number` | `0` |  |
| `MinHeight` | `number` | `0` |  |

## Properties

### DockWidgetPluginGuiInfo.InitialEnabled

**Type:** `bool`

The initial enabled state of a [PluginGui](/docs/reference/engine/classes/PluginGui.md) created using this
[DockWidgetPluginGuiInfo](/docs/reference/engine/datatypes/DockWidgetPluginGuiInfo.md). If a [PluginGui](/docs/reference/engine/classes/PluginGui.md) with the same
''pluginGuiId'' has previously been created in an earlier session of
Roblox Studio, then it will reload that saved enabled state (unless
`InitialEnabledShouldOverrideRestore` is true).

### DockWidgetPluginGuiInfo.InitialEnabledShouldOverrideRestore

**Type:** `bool`

If true, the value of `InitialEnabled` will override the previously saved
enabled state of a [PluginGui](/docs/reference/engine/classes/PluginGui.md) being created with this
[DockWidgetPluginGuiInfo](/docs/reference/engine/datatypes/DockWidgetPluginGuiInfo.md). The previously saved enabled state is
loaded based on the `pluginGuiId` argument of
[Plugin:CreateDockWidgetPluginGuiAsync()](/docs/reference/engine/classes/Plugin.md).

### DockWidgetPluginGuiInfo.FloatingXSize

**Type:** `number`

The initial pixel width of a [PluginGui](/docs/reference/engine/classes/PluginGui.md) created using this
[DockWidgetPluginGuiInfo](/docs/reference/engine/datatypes/DockWidgetPluginGuiInfo.md), when the [InitialDockState](/docs/reference/engine/enums/InitialDockState.md) is
set to `Float`.

### DockWidgetPluginGuiInfo.FloatingYSize

**Type:** `number`

The initial pixel height of a [PluginGui](/docs/reference/engine/classes/PluginGui.md) created using this
[DockWidgetPluginGuiInfo](/docs/reference/engine/datatypes/DockWidgetPluginGuiInfo.md), when the [InitialDockState](/docs/reference/engine/enums/InitialDockState.md) is
set to `Float`.

### DockWidgetPluginGuiInfo.MinWidth

**Type:** `number`

The minimum width of a [PluginGui](/docs/reference/engine/classes/PluginGui.md) created using this
[DockWidgetPluginGuiInfo](/docs/reference/engine/datatypes/DockWidgetPluginGuiInfo.md), in pixels.

Each platform has its own absolute minimum that Roblox will enforce. These
variations exist to account for the contents of the title bar (which
varies by platform) when the widget is floating. For example, on a Mac,
the width can never be less than ~80 pixels to accommodate the
close/minimize/maximize buttons.

### DockWidgetPluginGuiInfo.MinHeight

**Type:** `number`

The minimum height of a [PluginGui](/docs/reference/engine/classes/PluginGui.md) created using this
[DockWidgetPluginGuiInfo](/docs/reference/engine/datatypes/DockWidgetPluginGuiInfo.md), in pixels.