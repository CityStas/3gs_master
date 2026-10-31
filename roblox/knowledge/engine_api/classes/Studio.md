---
name: Studio
last_updated: 2026-10-30T19:55:53Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
tags:
  - NotCreatable
  - Service
  - NotReplicated
summary: "Represents Roblox Studio's script editor settings."
---

# Class: Studio

> Represents Roblox Studio's script editor settings.

## Description

The Studio object is a settings object that is exclusive to Roblox Studio. It
can be found in Roblox Studio's settings under the Studio tab.

## Properties

### Property: Studio."function" Color

```json
{
  "type": "Color3",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Script Editor Colors"
}
```

Sets the color of the `function` keyword in the script editor. This must
be set in Studio Settings > Studio tab.

### Property: Studio."local" Color

```json
{
  "type": "Color3",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Script Editor Colors"
}
```

Sets the color of the `local` keyword in the script editor. This must be
set in Studio Settings > Studio tab.

### Property: Studio."nil" Color

```json
{
  "type": "Color3",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Script Editor Colors"
}
```

Sets the color of the `nil` keyword in the script editor. This must be set
in Studio Settings > Studio tab.

### Property: Studio."self" Color

```json
{
  "type": "Color3",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Script Editor Colors"
}
```

Sets the color of the `self` keyword in the script editor. This must be
set in Studio Settings > Studio tab.

### Property: Studio."TODO" Color

```json
{
  "type": "Color3",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Script Editor Colors"
}
```

Sets the color of TODO comments in the script editor. This must be set in
Studio Settings > Studio tab.

### Property: Studio.ActionOnStopSync

```json
{
  "type": "ActionOnStopSync",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Directories"
}
```

Sets the action Studio takes when stopping file sync. This must be set in
Studio Settings > Studio tab.

### Property: Studio.Active Color

```json
{
  "type": "Color3",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Tools"
}
```

Sets the color of active UI elements in Studio. This must be set in Studio
Settings > Studio tab.

### Property: Studio.Active Hover Over Color

```json
{
  "type": "Color3",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Tools"
}
```

Sets the color of active UI elements when hovered in Studio. This must be
set in Studio Settings > Studio tab.

### Property: Studio.Always Save Script Changes

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "General"
}
```

If set to true, Roblox Studio will attempt to transfer script changes that
were made during a Play Solo session to the opened place.

### Property: Studio.Animate Hover Over

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Tools"
}
```

If set to true, the hover selection box that is shown when mousing over
selectable objects in the [Workspace](/docs/reference/engine/classes/Workspace.md) will flash between
`Hover Over Color` and `Select Color` based on the `Hover Animate Speed`.

### Property: Studio.Auto Clean Empty Line

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Script Editor"
}
```

Controls whether trailing whitespace is automatically removed from empty
lines in the script editor. This must be set in Studio Settings > Studio
tab.

### Property: Studio.Auto Closing Brackets

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Script Editor"
}
```

Controls whether the script editor automatically inserts a matching
closing bracket. This must be set in Studio Settings > Studio tab.

### Property: Studio.Auto Closing Quotes

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Script Editor"
}
```

Controls whether the script editor automatically inserts a matching
closing quote. This must be set in Studio Settings > Studio tab.

### Property: Studio.Auto Delete Closing Brackets and Quotes

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Script Editor"
}
```

Controls whether deleting an opening bracket or quote also removes its
closing counterpart. This must be set in Studio Settings > Studio tab.

### Property: Studio.Auto Indent Rule

```json
{
  "type": "AutoIndentRule",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Script Editor"
}
```

Sets the rule used to determine automatic indentation in the script
editor. This must be set in Studio Settings > Studio tab.

### Property: Studio.Auto-Recovery Enabled

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Auto-Recovery"
}
```

Controls whether Studio automatically saves recovery files at a set
interval. This must be set in Studio Settings > Studio tab.

### Property: Studio.Auto-Recovery Interval (Minutes)

```json
{
  "type": "int",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Auto-Recovery"
}
```

Sets the interval in minutes at which Studio saves auto-recovery files.
This must be set in Studio Settings > Studio tab.

### Property: Studio.AutocompleteAcceptanceBehavior

```json
{
  "type": "CompletionAcceptanceBehavior",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Script Editor"
}
```

Sets the key used to accept autocomplete suggestions in the script editor.
This must be set in Studio Settings > Studio tab.

### Property: Studio.Automatically trigger AI Code Completion

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Script Editor"
}
```

Controls whether AI code completion suggestions trigger automatically
while typing. This must be set in Studio Settings > Studio tab.

### Property: Studio.AutoResumeSyncOnPlaceOpen

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxEngineSecurity",
    "write": "RobloxEngineSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Directories"
}
```

Controls whether file sync resumes automatically when a place is opened.
This must be set in Studio Settings > Studio tab.

### Property: Studio.AutoUpdateEnabled

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Updates"
}
```

Controls whether Studio updates itself automatically when a new version is
available. This must be set in Studio Settings > Studio tab.

### Property: Studio.Background Color

```json
{
  "type": "Color3",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Script Editor Colors"
}
```

Specifies the background color of Roblox Studio's script editor.

### Property: Studio.Basic Objects Display Mode

```json
{
  "type": "ListDisplayMode",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "General"
}
```

Sets the scrolling mode of the `Advanced Objects` tab in Roblox Studio.

### Property: Studio.Bool Color

```json
{
  "type": "Color3",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Script Editor Colors"
}
```

Sets the color of boolean literals in the script editor. This must be set
in Studio Settings > Studio tab.

### Property: Studio.Bracket Color

```json
{
  "type": "Color3",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Script Editor Colors"
}
```

Sets the color of brackets in the script editor. This must be set in
Studio Settings > Studio tab.

### Property: Studio.Built-in Function Color

```json
{
  "type": "Color3",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Script Editor Colors"
}
```

Sets the color of built-in functions and keywords in the script editor.

### Property: Studio.Camera Mouse Wheel Speed

```json
{
  "type": "float",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Camera"
}
```

Sets how many studs the camera will move forward or backwards when using
the mouse wheel.

### Property: Studio.Camera Pan Speed

```json
{
  "type": "float",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Camera"
}
```

Sets the speed of camera panning in Studio. This must be set in Studio
Settings > Studio tab.

### Property: Studio.Camera Shift Speed

```json
{
  "type": "float",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Camera"
}
```

Sets the speed in studs/sec that the camera moves while holding down Shift
with the movement keys.

### Property: Studio.Camera Speed

```json
{
  "type": "float",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Camera"
}
```

Sets the speed in studs/sec that the camera moves when movement keys are
pressed.

### Property: Studio.Camera Speed Adjust Binding

```json
{
  "type": "CameraSpeedAdjustBinding",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Camera"
}
```

Sets the mouse button used to adjust the camera speed in Studio. This must
be set in Studio Settings > Studio tab.

### Property: Studio.Camera Zoom to Mouse Position

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Camera"
}
```

Controls whether the camera zooms toward the mouse cursor position. This
must be set in Studio Settings > Studio tab.

### Property: Studio.CameraNavigationModel

```json
{
  "type": "CameraNavigationModel",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Camera"
}
```

Sets the navigation model used for camera movement in Studio. This must be
set in Studio Settings > Studio tab.

### Property: Studio.CameraShiftFactor

```json
{
  "type": "float",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Camera"
}
```

Sets the speed multiplier applied to camera movement when Shift is held.
This must be set in Studio Settings > Studio tab.

### Property: Studio.CameraTweenFocus

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Camera"
}
```

Controls whether the camera smoothly tweens when refocusing on a selected
object. This must be set in Studio Settings > Studio tab.

### Property: Studio.Clear Output On Start

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Output"
}
```

If set to true, the output will be automatically cleared when game
sessions are switched.

### Property: Studio.CommandBarEnterExec

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Script Editor"
}
```

Controls whether pressing Enter immediately executes the command bar
input. This must be set in Studio Settings > Studio tab.

### Property: Studio.CommandBarFont

```json
{
  "type": "QFont",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Script Editor"
}
```

Sets the font used in the Studio command bar. This must be set in Studio
Settings > Studio tab.

### Property: Studio.CommandBarLocalState

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Lua Debugger"
}
```

Controls whether the command bar retains its input state between sessions.
This must be set in Studio Settings > Studio tab.

### Property: Studio.Comment Color

```json
{
  "type": "Color3",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Script Editor Colors"
}
```

Specifies the color of comments in Roblox Studio's script editor.

### Property: Studio.Current Line Highlight Color

```json
{
  "type": "Color3",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Script Editor Colors"
}
```

Sets the color of the current line highlight in the script editor. This
must be set in Studio Settings > Studio tab.

### Property: Studio.Debugger Current Line Color

```json
{
  "type": "Color3",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Script Editor Colors"
}
```

Sets the color of the current debugger line in the script editor. This
must be set in Studio Settings > Studio tab.

### Property: Studio.Debugger Error Line Color

```json
{
  "type": "Color3",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Script Editor Colors"
}
```

Sets the color of debugger error lines in the script editor. This must be
set in Studio Settings > Studio tab.

### Property: Studio.DefaultInstancesDir

```json
{
  "type": "QDir",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxEngineSecurity",
    "write": "RobloxEngineSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Directories"
}
```

Sets the default directory where Studio saves instance files. This must be
set in Studio Settings > Studio tab.

### Property: Studio.DefaultScriptSyncFileType

```json
{
  "type": "DefaultScriptSyncFileType",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Directories"
}
```

Sets the default file type used when syncing scripts to the file system.
This must be set in Studio Settings > Studio tab.

### Property: Studio.DeprecatedObjectsShown

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Browsing"
}
```

If set to true, deprecated objects will be shown in the Advanced Objects
window, as well as the Object Browser.

### Property: Studio.DisplayLanguage

```json
{
  "type": "string",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "General"
}
```

Sets the display language used by the Studio interface. This must be set
in Studio Settings > Studio tab.

### Property: Studio.DraggerActiveColor

```json
{
  "type": "Color3",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Data"
}
```

Sets the color of the active dragger handle in Studio. This must be set in
Studio Settings > Studio tab.

### Property: Studio.DraggerLengthFactor

```json
{
  "type": "float",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Data"
}
```

Sets the length scale factor of dragger handles in Studio. This must be
set in Studio Settings > Studio tab.

### Property: Studio.DraggerMajorGridIncrement

```json
{
  "type": "int",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Data"
}
```

Sets the major grid increment used when snapping with the dragger. This
must be set in Studio Settings > Studio tab.

### Property: Studio.DraggerMaxSoftSnaps

```json
{
  "type": "int",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Data"
}
```

Sets the maximum number of soft snap points shown by the dragger. This
must be set in Studio Settings > Studio tab.

### Property: Studio.DraggerPassiveColor

```json
{
  "type": "Color3",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Data"
}
```

Sets the color of inactive dragger handles in Studio. This must be set in
Studio Settings > Studio tab.

### Property: Studio.DraggerScaleFactor

```json
{
  "type": "float",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Data"
}
```

Sets the scale factor controlling the overall size of dragger handles.
This must be set in Studio Settings > Studio tab.

### Property: Studio.DraggerShowAxisTicks

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Data"
}
```

Controls whether tick marks are shown on dragger axis lines. This must be
set in Studio Settings > Studio tab.

### Property: Studio.DraggerShowHoverRuler

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Data"
}
```

Controls whether a ruler is shown when hovering near the dragger. This
must be set in Studio Settings > Studio tab.

### Property: Studio.DraggerShowMeasurement

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Data"
}
```

Controls whether distance measurements are shown while dragging. This must
be set in Studio Settings > Studio tab.

### Property: Studio.DraggerShowNegativeAxes

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Data"
}
```

Controls whether negative axis handles are shown on the dragger. This must
be set in Studio Settings > Studio tab.

### Property: Studio.DraggerShowPlanes

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Data"
}
```

Controls whether planar translation handles are shown on the dragger. This
must be set in Studio Settings > Studio tab.

### Property: Studio.DraggerShowTargetSnap

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Data"
}
```

Controls whether the target snap indicator is shown on the dragger. This
must be set in Studio Settings > Studio tab.

### Property: Studio.DraggerShowTrackball

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Data"
}
```

Controls whether the trackball handle is shown on the rotation dragger.
This must be set in Studio Settings > Studio tab.

### Property: Studio.DraggerShowWhileDragging

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Data"
}
```

Controls whether dragger handles remain visible while actively dragging.
This must be set in Studio Settings > Studio tab.

### Property: Studio.DraggerSoftSnapMarginFactor

```json
{
  "type": "float",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Data"
}
```

Sets the margin factor used to determine proximity for soft snapping. This
must be set in Studio Settings > Studio tab.

### Property: Studio.DraggerSummonMarginFactor

```json
{
  "type": "float",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Data"
}
```

Sets the margin factor used to summon the dragger near a surface. This
must be set in Studio Settings > Studio tab.

### Property: Studio.DraggerTiltRotateDuration

```json
{
  "type": "float",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Data"
}
```

Sets the duration in seconds of the tilt rotation animation in the
dragger. This must be set in Studio Settings > Studio tab.

### Property: Studio.Enable Autocomplete

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Script Editor"
}
```

When set to true, the script editor and command bar will show an
autocomplete menu while writing.

### Property: Studio.Enable Autocomplete Doc View

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Script Editor"
}
```

Controls whether documentation is shown alongside autocomplete
suggestions. This must be set in Studio Settings > Studio tab.

### Property: Studio.Enable CoreScript Debugger

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Advanced"
}
```

Controls whether the CoreScript debugger is available in Studio. This must
be set in Studio Settings > Studio tab.

### Property: Studio.Enable Http Sandboxing

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Advanced"
}
```

Controls whether HTTP requests from plugins are sandboxed. This must be
set in Studio Settings > Studio tab.

### Property: Studio.Enable Internal Beta Features

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Advanced"
}
```

Controls whether internal beta features are accessible in Studio. This
must be set in Studio Settings > Studio tab.

### Property: Studio.Enable Internal Features

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Advanced"
}
```

Controls whether internal developer features are accessible in Studio.
This must be set in Studio Settings > Studio tab.

### Property: Studio.Enable Script Analysis

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Script Editor"
}
```

Controls whether the script editor performs real-time Luau script
analysis. This must be set in Studio Settings > Studio tab.

### Property: Studio.Enable Scrollbar Markers

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Script Editor"
}
```

Controls whether error and warning markers are shown on the script editor
scrollbar. This must be set in Studio Settings > Studio tab.

### Property: Studio.Enable Signature Help

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Script Editor"
}
```

Controls whether function signature help popups are shown while typing.
This must be set in Studio Settings > Studio tab.

### Property: Studio.Enable Signature Help Doc View

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Script Editor"
}
```

Controls whether documentation is shown alongside signature help popups.
This must be set in Studio Settings > Studio tab.

### Property: Studio.Enable Temporary Tabs

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Script Editor"
}
```

Controls whether opening a script creates a temporary tab that is replaced
on the next open. This must be set in Studio Settings > Studio tab.

### Property: Studio.Enable Temporary Tabs In Explorer

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Script Editor"
}
```

Controls whether clicking a script in the Explorer opens it in a temporary
tab. This must be set in Studio Settings > Studio tab.

### Property: Studio.Enable Type Hover

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Script Editor"
}
```

Controls whether hovering over an identifier shows its inferred type. This
must be set in Studio Settings > Studio tab.

### Property: Studio.EnableCodeAssist

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Script Editor"
}
```

Controls whether AI-powered code assist features are enabled in the script
editor. This must be set in Studio Settings > Studio tab.

### Property: Studio.EnableFindOnType

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Data"
}
```

Controls whether the Find bar activates when typing in the script editor.
This must be set in Studio Settings > Studio tab.

### Property: Studio.EnableIndentationRulers

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Script Editor"
}
```

Controls whether indentation ruler lines are shown in the script editor.
This must be set in Studio Settings > Studio tab.

### Property: Studio.EnableSelectionTooltips

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Script Editor"
}
```

Controls whether tooltips are shown when hovering over selected objects.
This must be set in Studio Settings > Studio tab.

### Property: Studio.EnableStudioStreaming

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Streaming"
}
```

Controls whether Studio streaming mode is enabled. This must be set in
Studio Settings > Studio tab.

### Property: Studio.Error Color

```json
{
  "type": "Color3",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Script Editor Colors"
}
```

Specifies the color of the wavy underline shown when malformed code is
detected in the script editor.

### Property: Studio.ExternalEditorMode

```json
{
  "type": "ExternalEditorMode",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Directories"
}
```

Sets the mode used when opening scripts in an external editor. This must
be set in Studio Settings > Studio tab.

### Property: Studio.ExternalEditorSelection

```json
{
  "type": "QDir",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Directories"
}
```

Sets which external editor Studio opens scripts with. This must be set in
Studio Settings > Studio tab.

### Property: Studio.Find Selection Background Color

```json
{
  "type": "Color3",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Script Editor Colors"
}
```

Sets the highlight color of matches in the script editor's Find Selection
operation (Ctrl+F).

### Property: Studio.Font

```json
{
  "type": "QFont",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Script Editor"
}
```

Specifies the font used in the script editor.

### Property: Studio.Format On Paste

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Script Editor"
}
```

Controls whether pasted code is automatically formatted in the script
editor. This must be set in Studio Settings > Studio tab.

### Property: Studio.Format On Type

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Script Editor"
}
```

Controls whether code is automatically formatted as you type in the script
editor. This must be set in Studio Settings > Studio tab.

### Property: Studio.Function Name Color

```json
{
  "type": "Color3",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Script Editor Colors"
}
```

Sets the color of function names in the script editor. This must be set in
Studio Settings > Studio tab.

### Property: Studio.Highlight Current Line

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Script Editor"
}
```

Controls whether the current line is highlighted in the script editor.
This must be set in Studio Settings > Studio tab.

### Property: Studio.Highlight Occurances

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Script Editor"
}
```

Controls whether other occurrences of the word under the cursor are
highlighted. This must be set in Studio Settings > Studio tab.

### Property: Studio.HintColor

```json
{
  "type": "Color3",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Script Editor Colors"
}
```

Sets the color of hint diagnostics in the script editor. This must be set
in Studio Settings > Studio tab.

### Property: Studio.Hover Animate Speed

```json
{
  "type": "HoverAnimateSpeed",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Tools"
}
```

Specifies how frequently the hover animation flashes when the mouse is
hovering over a selectable object in the [Workspace](/docs/reference/engine/classes/Workspace.md).

### Property: Studio.Hover Box Thickness

```json
{
  "type": "float",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxEngineSecurity",
    "write": "RobloxEngineSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Tools"
}
```

Sets the thickness of the selection box shown when hovering over objects.
This must be set in Studio Settings > Studio tab.

### Property: Studio.Hover Line Thickness

```json
{
  "type": "int",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxEngineSecurity",
    "write": "RobloxEngineSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Tools"
}
```

Sets the line thickness of the hover selection box. This must be set in
Studio Settings > Studio tab.

### Property: Studio.Hover Over Color

```json
{
  "type": "Color3",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Tools"
}
```

Specifies the color that the hover selection box uses.

### Property: Studio.IconOverrideDir

```json
{
  "type": "QDir",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Directories"
}
```

Sets the directory Studio uses to load icon overrides. This must be set in
Studio Settings > Studio tab.

### Property: Studio.Indent Using Spaces

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Script Editor"
}
```

Controls whether the script editor uses spaces instead of tabs for
indentation. This must be set in Studio Settings > Studio tab.

### Property: Studio.IndentationRulerColor

```json
{
  "type": "Color3",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Script Editor Colors"
}
```

Sets the color of indentation rulers in the script editor. This must be
set in Studio Settings > Studio tab.

### Property: Studio.InformationColor

```json
{
  "type": "Color3",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Script Editor Colors"
}
```

Sets the color of information diagnostics in the script editor. This must
be set in Studio Settings > Studio tab.

### Property: Studio.Keyword Color

```json
{
  "type": "Color3",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Script Editor Colors"
}
```

Sets the text color of built-in Luau keywords.

### Property: Studio.LargeFileLineCountThreshold

```json
{
  "type": "int",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Script Editor"
}
```

Sets the line count at which a script is treated as a large file by the
script editor. This must be set in Studio Settings > Studio tab.

### Property: Studio.LargeFileThreshold

```json
{
  "type": "int",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Script Editor"
}
```

Sets the byte size at which a script is treated as a large file by the
script editor. This must be set in Studio Settings > Studio tab.

### Property: Studio.Line Thickness

```json
{
  "type": "float",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Primary Part"
}
```

Sets the thickness of the [Model.PrimaryPart](/docs/reference/engine/classes/Model.md) selection adornee.
This value is constrained between 0 and 0.05.

### Property: Studio.LoadAllBuiltinPluginsInRunModes

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Data"
}
```

Controls whether all built-in plugins are loaded when using run modes.
This must be set in Studio Settings > Studio tab.

### Property: Studio.LoadInternalPlugins

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxEngineSecurity",
    "write": "RobloxEngineSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Data"
}
```

Controls whether internal Roblox plugins are loaded in Studio. This must
be set in Studio Settings > Studio tab.

### Property: Studio.LoadUserPluginsInRunModes

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Data"
}
```

Controls whether user-installed plugins are loaded when using run modes.
This must be set in Studio Settings > Studio tab.

### Property: Studio.LocalAssetsFolder

```json
{
  "type": "QDir",
  "access": "ReadOnly",
  "security": {
    "read": "None",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Directories"
}
```

Sets the local folder Studio uses for local asset storage. This must be
set in Studio Settings > Studio tab.

### Property: Studio.LuaDebuggerEnabled

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Lua Debugger"
}
```

Specifies whether or not the Lua Debugger feature is enabled.

### Property: Studio.Luau Keyword Color

```json
{
  "type": "Color3",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Script Editor Colors"
}
```

Sets the color of Luau-specific keywords in the script editor. This must
be set in Studio Settings > Studio tab.

### Property: Studio.Main Volume

```json
{
  "type": "float",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Audio"
}
```

Sets the main audio playback volume in Studio. This must be set in Studio
Settings > Studio tab.

### Property: Studio.Matching Word Background Color

```json
{
  "type": "Color3",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Script Editor Colors"
}
```

Sets the highlight color of double-clicked variables in the script editor.

### Property: Studio.MaxFindReplaceAllResults

```json
{
  "type": "int",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Data"
}
```

Sets the maximum number of results returned by the Find All operation.
This must be set in Studio Settings > Studio tab.

### Property: Studio.Maximum Output Lines

```json
{
  "type": "int",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Output"
}
```

The maximum number of lines that can be displayed in the output.

### Property: Studio.Menu Item Background Color

```json
{
  "type": "Color3",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Script Editor Colors"
}
```

Sets the background color of menu items in Studio. This must be set in
Studio Settings > Studio tab.

### Property: Studio.Method Color

```json
{
  "type": "Color3",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Script Editor Colors"
}
```

Sets the color of method names in the script editor. This must be set in
Studio Settings > Studio tab.

### Property: Studio.Number Color

```json
{
  "type": "Color3",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Script Editor Colors"
}
```

Specifies the color of numbers in Roblox Studio's script editor.

### Property: Studio.Only Play Audio from Window in Focus

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Audio"
}
```

If set to true, audio being played will only be heard if the game window
is being focused on.

### Property: Studio.Operator Color

```json
{
  "type": "Color3",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Script Editor Colors"
}
```

Sets the text color of operator characters in the script editor.

### Property: Studio.Output Font

```json
{
  "type": "QFont",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Output"
}
```

Specifies the font used by the output.

### Property: Studio.Output Layout Mode

```json
{
  "type": "OutputLayoutMode",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Output"
}
```

Sets the layout mode of the output.

### Property: Studio.PermissionLevelShown

```json
{
  "type": "PermissionLevelShown",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Browsing"
}
```

Sets the highest permission level that APIs have to have in order to be
shown in the Object Browser. See [PermissionLevelShown](/docs/reference/engine/enums/PermissionLevelShown.md) for more
info.

### Property: Studio.Physical Draggers Select Scope By Default

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Tools"
}
```

Controls whether physical draggers default to selecting within the current
scope. This must be set in Studio Settings > Studio tab.

### Property: Studio.Pivot Snap To Geometry Color

```json
{
  "type": "Color3",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxEngineSecurity",
    "write": "RobloxEngineSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Tools"
}
```

Sets the color of the pivot snap-to-geometry indicator in Studio. This
must be set in Studio Settings > Studio tab.

### Property: Studio.PluginDebuggingEnabled

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Lua Debugger"
}
```

Controls whether plugin script debugging is enabled in Studio. This must
be set in Studio Settings > Studio tab.

### Property: Studio.PluginsDir

```json
{
  "type": "QDir",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Directories"
}
```

The directory where local plugins are stored.

### Property: Studio.PreferredTextSize

```json
{
  "type": "PreferredTextSize",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "General"
}
```

Sets the preferred font size in the script editor. This must be set in
Studio Settings > Studio tab.

### Property: Studio.Primary Text Color

```json
{
  "type": "Color3",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Script Editor Colors"
}
```

Sets the primary text color in Studio. This must be set in Studio
Settings > Studio tab.

### Property: Studio.Property Color

```json
{
  "type": "Color3",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Script Editor Colors"
}
```

Sets the color of property names in the script editor. This must be set in
Studio Settings > Studio tab.

### Property: Studio.ReloadBuiltinPluginsOnChange

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxEngineSecurity",
    "write": "RobloxEngineSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Directories"
}
```

Controls whether built-in plugins are automatically reloaded when their
files change. This must be set in Studio Settings > Studio tab.

### Property: Studio.ReloadLocalPluginsOnChange

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxEngineSecurity",
    "write": "RobloxEngineSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Directories"
}
```

Controls whether local plugins are automatically reloaded when their files
change. This must be set in Studio Settings > Studio tab.

### Property: Studio.Respect Studio shortcuts when game has focus

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Advanced"
}
```

When set to true, Roblox Studio shortcuts will take priority over inputs
being captured in the game window.

### Property: Studio.Ruler Color

```json
{
  "type": "Color3",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Script Editor Colors"
}
```

Sets the color of the column ruler in the script editor. This must be set
in Studio Settings > Studio tab.

### Property: Studio.Rulers

```json
{
  "type": "string",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Script Editor"
}
```

Sets the column positions at which vertical ruler lines are drawn in the
script editor. This must be set in Studio Settings > Studio tab.

### Property: Studio.RuntimeUndoBehavior

```json
{
  "type": "RuntimeUndoBehavior",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Undo"
}
```

Sets how Studio handles undo operations during runtime playback. This must
be set in Studio Settings > Studio tab.

### Property: Studio.Script Editor Color Preset

```json
{
  "type": "StudioScriptEditorColorPresets",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Script Editor Colors"
}
```

Sets the color preset applied to the script editor. This must be set in
Studio Settings > Studio tab.

### Property: Studio.Script Editor Scrollbar Background Color

```json
{
  "type": "Color3",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Script Editor Colors"
}
```

Sets the background color of the script editor scrollbar in Studio. This
must be set in Studio Settings > Studio tab.

### Property: Studio.Script Editor Scrollbar Handle Color

```json
{
  "type": "Color3",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Script Editor Colors"
}
```

Sets the handle color of the script editor scrollbar in Studio. This must
be set in Studio Settings > Studio tab.

### Property: Studio.ScriptTimeoutLength

```json
{
  "type": "int",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Lua Debugger"
}
```

The time (in seconds) a script can wait to be resumed before timing out.

### Property: Studio.Scroll Past Last Line

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Script Editor"
}
```

Controls whether the script editor allows scrolling below the last line.
This must be set in Studio Settings > Studio tab.

### Property: Studio.Secondary Text Color

```json
{
  "type": "Color3",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Script Editor Colors"
}
```

Sets the secondary text color in Studio. This must be set in Studio
Settings > Studio tab.

### Property: Studio.Select Color

```json
{
  "type": "Color3",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Tools"
}
```

The color of the selection box used with object selections in the
[Workspace](/docs/reference/engine/classes/Workspace.md)

### Property: Studio.Select/Hover Color

```json
{
  "type": "Color3",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Primary Part"
}
```

Sets the color of the [Model.PrimaryPart](/docs/reference/engine/classes/Model.md) selection box.

### Property: Studio.Selected Menu Item Background Color

```json
{
  "type": "Color3",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Script Editor Colors"
}
```

Sets the background color of selected menu items in Studio. This must be
set in Studio Settings > Studio tab.

### Property: Studio.Selected Text Color

```json
{
  "type": "Color3",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Script Editor Colors"
}
```

Sets the color of selected text in Studio. This must be set in Studio
Settings > Studio tab.

### Property: Studio.Selection Background Color

```json
{
  "type": "Color3",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Script Editor Colors"
}
```

Sets the background color of selected text in the script editor.

### Property: Studio.Selection Box Thickness

```json
{
  "type": "float",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxEngineSecurity",
    "write": "RobloxEngineSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Tools"
}
```

Sets the thickness of the selection box around selected objects. This must
be set in Studio Settings > Studio tab.

### Property: Studio.Selection Color

```json
{
  "type": "Color3",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Script Editor Colors"
}
```

Sets the text color of selected text in the script editor.

### Property: Studio.Selection Line Thickness

```json
{
  "type": "int",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxEngineSecurity",
    "write": "RobloxEngineSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Tools"
}
```

Sets the line thickness of the selection box around selected objects. This
must be set in Studio Settings > Studio tab.

### Property: Studio.Set Pivot of Imported Parts

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Advanced"
}
```

Sets whether the pivot point is repositioned when parts are imported. This
must be set in Studio Settings > Studio tab.

### Property: Studio.Show Core GUI in Explorer while Playing

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Explorer"
}
```

If set to true, the [CoreGui](/docs/reference/engine/classes/CoreGui.md) will be visible in the Explorer while
the game is running.

### Property: Studio.Show Diagnostics Bar

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Advanced"
}
```

If set to true, basic diagnostic information is shown in the bottom right.

### Property: Studio.Show FileSyncService

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Explorer"
}
```

Controls whether FileSyncService is shown in the Explorer panel. This must
be set in Studio Settings > Studio tab.

### Property: Studio.Show Hidden Objects in Explorer

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Explorer"
}
```

Controls whether hidden objects are visible in the Explorer panel. This
must be set in Studio Settings > Studio tab.

### Property: Studio.Show Hover Over

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Tools"
}
```

If set to true, hovering over an object in the [Workspace](/docs/reference/engine/classes/Workspace.md) will show
a selection box.

### Property: Studio.Show Light Guides

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Visualization"
}
```

Controls whether light guide visualizations are shown in the viewport.
This must be set in Studio Settings > Studio tab.

### Property: Studio.Show Navigation Labels

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Visualization"
}
```

Controls whether navigation mesh region labels are shown in the viewport.
This must be set in Studio Settings > Studio tab.

### Property: Studio.Show Navigation Mesh

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Visualization"
}
```

When set to true, the navigation mesh used by the
[PathfindingService](/docs/reference/engine/classes/PathfindingService.md) will be visualized.

### Property: Studio.Show Pathfinding Links

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Visualization"
}
```

Controls whether PathfindingLink visualizations are shown in the viewport.
This must be set in Studio Settings > Studio tab.

### Property: Studio.Show Plugin GUI Service in Explorer

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Explorer"
}
```

When set to true, the [PluginGuiService](/docs/reference/engine/classes/PluginGuiService.md) will be shown in Roblox
Studio's explorer.

### Property: Studio.Show plus button on hover in Explorer

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Explorer"
}
```

Controls whether a plus button appears when hovering over items in the
Explorer. This must be set in Studio Settings > Studio tab.

### Property: Studio.Show Singly Selected Attachment Parent Frame

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Visualization"
}
```

Controls whether the parent part frame is shown when a single attachment
is selected. This must be set in Studio Settings > Studio tab.

### Property: Studio.Show Whitespace

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Script Editor"
}
```

Controls whether whitespace characters are shown as visible glyphs in the
script editor. This must be set in Studio Settings > Studio tab.

### Property: Studio.ShowCorePackagesInExplorer

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Explorer"
}
```

Controls whether core packages are shown in the Explorer panel. This must
be set in Studio Settings > Studio tab.

### Property: Studio.Skip Closing Brackets and Quotes

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Script Editor"
}
```

Controls whether the cursor skips over a typed closing bracket or quote if
one already exists. This must be set in Studio Settings > Studio tab.

### Property: Studio.String Color

```json
{
  "type": "Color3",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Script Editor Colors"
}
```

Specifies the color of strings in the script editor.

### Property: Studio.Tab Width

```json
{
  "type": "int",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Script Editor"
}
```

Specifies how many spaces are used to represent a tab in the script
editor.

### Property: Studio.Text Color

```json
{
  "type": "Color3",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Script Editor Colors"
}
```

Specifies the color of normal text in the script editor.

### Property: Studio.Text Wrapping

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Script Editor"
}
```

If set to true, text in the script editor will be wrapped.

### Property: Studio.Theme

```json
{
  "type": "StudioTheme",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "General"
}
```

The Theme property is used to get/set the current [StudioTheme](/docs/reference/engine/classes/StudioTheme.md) used
by [Studio](/docs/reference/engine/classes/Studio.md).

This is intended for use within [Plugins](/docs/reference/engine/classes/Plugin.md), but will also
execute in the Command Line. You can access the function via:

```lua
settings().Studio.Theme
```

For instance, if you would like to print the current Studio theme:

```lua
print("The current Studio theme is:", settings().Studio.Theme)
```

### Property: Studio.TypeColor

```json
{
  "type": "Color3",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Script Editor Colors"
}
```

Sets the color of type annotations in the script editor. This must be set
in Studio Settings > Studio tab.

### Property: Studio.Use Bounding Box Move Handles

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Tools"
}
```

Controls whether move handles are placed at the bounding box edges instead
of the pivot. This must be set in Studio Settings > Studio tab.

### Property: Studio.UseDefaultExternalEditor

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Directories"
}
```

Controls whether Studio uses the system's default application to open
scripts externally. This must be set in Studio Settings > Studio tab.

### Property: Studio.VAxisColor

```json
{
  "type": "Color3",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Data"
}
```

Sets the color of the V axis handle in Studio's draggers. This must be set
in Studio Settings > Studio tab.

### Property: Studio.Warning Color

```json
{
  "type": "Color3",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Script Editor Colors"
}
```

Specifies the color of the wavy underline shown when the script analyzer
picks up a problem that should be addressed in the script editor.

### Property: Studio.Whitespace Color

```json
{
  "type": "Color3",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Script Editor Colors"
}
```

Sets the color of visible whitespace characters in the script editor. This
must be set in Studio Settings > Studio tab.

### Property: Studio.XAxisColor

```json
{
  "type": "Color3",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Data"
}
```

Sets the color of the X axis handle in Studio's draggers. This must be set
in Studio Settings > Studio tab.

### Property: Studio.YAxisColor

```json
{
  "type": "Color3",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Data"
}
```

Sets the color of the Y axis handle in Studio's draggers. This must be set
in Studio Settings > Studio tab.

### Property: Studio.ZAxisColor

```json
{
  "type": "Color3",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Data"
}
```

Sets the color of the Z axis handle in Studio's draggers. This must be set
in Studio Settings > Studio tab.

### Property: Studio.LuaDebuggerEnabledAtStartup *(hidden)*

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Lua Debugger"
}
```

Controls whether the Lua debugger is enabled when Studio starts. This must
be set in Studio Settings > Studio tab.

### Property: Studio.UI Theme *(hidden)*

```json
{
  "type": "UITheme",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": false,
    "can_save": true
  },
  "deprecated": true,
  "thread_safety": "ReadSafe",
  "category": "General"
}
```

Specifies the color scheme of Roblox Studio.

## Methods

### Method: Studio:GetAvailableThemes

**Signature:** `Studio:GetAvailableThemes(): Array`

The **GetAvailableThemes()** function returns a list of
[StudioThemes](/docs/reference/engine/classes/StudioTheme.md) available in [Studio](/docs/reference/engine/classes/Studio.md). You can
access the function via:

*Security: PluginSecurity · Thread Safety: Unsafe*

**Returns:** `Array` — A list of themes available in Studio.

**Output Studio Themes**

The code below retrieves an array of all available themes and then iterates
through them.

```lua
local themes = settings().Studio:GetAvailableThemes()

for _, theme in pairs(themes) do
	print(theme)
end
```

**Get Available Themes**

Demonstrates [Studio:GetAvailableThemes()](/docs/reference/engine/classes/Studio.md).

```lua
settings().Studio:GetAvailableThemes()
```

## Events

### Event: Studio.ThemeChanged

**Signature:** `Studio.ThemeChanged()`

The **ThemeChanged** event fires when Studio's [Theme](/docs/reference/engine/classes/Studio.md)
changes. The best use of this event is to get the colors from the theme
that changed and update your plugin's UI accordingly.

*Security: PluginSecurity*

## Inherited Members

### From [Instance](/docs/reference/engine/classes/Instance.md)

- **Property `Archivable`** (`boolean`): Determines if an Instance and its descendants can be cloned using
- **Property `archivable`** (`boolean`):  *(deprecated, hidden)*
- **Property `Capabilities`** (`SecurityCapabilities`): The set of capabilities allowed to be used for scripts inside this
- **Property `IsInSandbox`** (`boolean`): Indicates whether the instance is inside a sandboxed container.
- **Property `Name`** (`string`): A non-unique identifier of the Instance.
- **Property `Parent`** (`Instance`): Determines the hierarchical parent of the Instance.
- **Property `PredictionMode`** (`PredictionMode`): Reflects the client-side prediction mode applied to the instance under
- **Property `RobloxLocked`** (`boolean`): A deprecated property that used to protect CoreGui objects. *(hidden)*
- **Property `Sandboxed`** (`boolean`): When enabled, the instance can only access abilities in its `Capabilities`
- **Property `UniqueId`** (`UniqueId`): A unique identifier for the instance.
- **Method `AddTag(tag: string): ()`**: Applies a tag to the instance.
- **Method `children(): Instances`**: Returns an array of the object's children. *(deprecated)*
- **Method `ClearAllChildren(): ()`**: This method destroys all of an instance's children.
- **Method `Clone(): Instance`**: Create a copy of an instance and all its descendants, ignoring instances
- **Method `clone(): Instance`**:  *(deprecated)*
- **Method `Destroy(): ()`**: Sets the Instance.Parent property to `nil`, locks the
- **Method `destroy(): ()`**:  *(deprecated)*
- **Method `FindFirstAncestor(name: string): Instance?`**: Returns the first ancestor of the Instance whose
- **Method `FindFirstAncestorOfClass(className: string): Instance?`**: Returns the first ancestor of the Instance whose
- **Method `FindFirstAncestorWhichIsA(className: string): Instance?`**: Returns the first ancestor of the Instance for whom
- **Method `FindFirstChild(name: string, recursive?: boolean): Instance?`**: Returns the first child of the Instance found with the given name.
- **Method `findFirstChild(name: string, recursive?: boolean): Instance`**:  *(deprecated)*
- **Method `FindFirstChildOfClass(className: string): Instance?`**: Returns the first child of the Instance whose
- **Method `FindFirstChildWhichIsA(className: string, recursive?: boolean): Instance?`**: Returns the first child of the Instance for whom
- **Method `FindFirstDescendant(name: string): Instance?`**: Returns the first descendant found with the given Instance.Name.
- **Method `GetActor(): Actor?`**: Returns the Actor associated with the Instance, if any.
- **Method `GetAttribute(attribute: string): Variant`**: Returns the value which has been assigned to the given attribute name.
- **Method `GetAttributeChangedSignal(attribute: string): RBXScriptSignal`**: Returns an event that fires when the given attribute changes.
- **Method `GetAttributes(): Dictionary`**: Returns a dictionary of the instance's attributes.
- **Method `GetChildren(): Instances`**: Returns an array containing all of the instance's children.
- **Method `getChildren(): Instances`**:  *(deprecated)*
- **Method `GetDebugId(scopeLength?: int): string`**: Returns a coded string of the debug ID used internally by Roblox.
- **Method `GetDescendants(): Instances`**: Returns an array containing all of the descendants of the instance.
- **Method `GetFullName(): string`**: Returns a string describing the instance's ancestry.
- **Method `GetStyled(name: string, selector: string?): Variant`**: Returns the styled or explicitly modified value of the specified property,
- **Method `GetStyledPropertyChangedSignal(property: string): RBXScriptSignal`**: Returns an event that fires when the given style property changes on the
- **Method `GetTags(): Array`**: Gets an array of all tags applied to the instance.
- **Method `HasTag(tag: string): boolean`**: Check whether the instance has a given tag.
- **Method `IsAncestorOf(descendant: Instance): boolean`**: Returns true if an Instance is an ancestor of the given
- **Method `IsDescendantOf(ancestor: Instance): boolean`**: Returns `true` if an Instance is a descendant of the given
- **Method `isDescendantOf(ancestor: Instance): boolean`**:  *(deprecated)*
- **Method `IsPropertyModified(property: string): boolean`**: Returns `true` if the value stored in the specified property is not equal
- **Method `QueryDescendants(selector: string): Instances`**: Returns an array containing all descendants of the instance that match the
- **Method `Remove(): ()`**: Sets the object's `Parent` to `nil`, and does the same for all its *(deprecated)*
- **Method `remove(): ()`**:  *(deprecated)*
- **Method `RemoveTag(tag: string): ()`**: Removes a tag from the instance.
- **Method `ResetPropertyToDefault(property: string): ()`**: Resets a property to its default value.
- **Method `SetAttribute(attribute: string, value: Variant): ()`**: Sets the attribute with the given name to the given value.
- **Method `WaitForChild(childName: string, timeOut: double): Instance`**: Returns the child of the Instance with the given name. If the
- **Event `AncestryChanged`**: Fires when the Instance.Parent property of this object or one of
- **Event `AttributeChanged`**: Fires whenever an attribute is changed on the Instance.
- **Event `ChildAdded`**: Fires after an object is parented to this Instance.
- **Event `childAdded`**:  *(deprecated)*
- **Event `ChildRemoved`**: Fires after a child is removed from this Instance.
- **Event `DescendantAdded`**: Fires after a descendant is added to the Instance.
- **Event `DescendantRemoving`**: Fires immediately before a descendant of the Instance is removed.
- **Event `Destroying`**: Fires immediately before (or is deferred until after) the instance is
- **Event `StyledPropertiesChanged`**: Fires whenever any style property is changed on the instance, including

### From [Object](/docs/reference/engine/classes/Object.md)

- **Property `ClassName`** (`string`): A read-only string representing the class this Object belongs to.
- **Property `className`** (`string`):  *(deprecated)*
- **Method `GetPropertyChangedSignal(property: string): RBXScriptSignal`**: Get an event that fires when a given property of the object changes.
- **Method `IsA(className: string): boolean`**: Returns true if an object's class matches or inherits from a given class.
- **Method `isA(className: string): boolean`**:  *(deprecated)*
- **Event `Changed`**: Fires immediately after a property of the object changes, with some