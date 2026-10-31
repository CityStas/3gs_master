---
name: Plugin
last_updated: 2026-10-30T19:55:53Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
tags:
  - NotCreatable
summary: "The main object responsible for creating custom Studio widgets, toolbars, buttons, and other plugin UI elements."
---

# Class: Plugin

> The main object responsible for creating custom Studio widgets, toolbars,
> buttons, and other plugin UI elements.

## Description

`Plugin` is the main object responsible for creating custom Studio widgets,
plugin toolbars, plugin buttons, and more. The `Plugin` object can be accessed
through the [RobloxGlobals.plugin](/docs/reference/engine/globals/RobloxGlobals.md) global reference in a [Script](/docs/reference/engine/classes/Script.md)
that is executed as a plugin.

## Code Samples

**Script - Pass the Plugin Global to a ModuleScript**

The [RobloxGlobals.plugin](/docs/reference/engine/globals/RobloxGlobals.md) global reference is not passed to
[ModuleScripts](/docs/reference/engine/classes/ModuleScript.md) within the plugin. In order to use it in a
[ModuleScript](/docs/reference/engine/classes/ModuleScript.md), you must explicitly pass it as seen in the example
below.

```lua
assert(plugin, "This script must be run as a plugin!")
-- Code beyond this point will execute only if the script is run as a plugin

-- Load the module and pass the plugin reference
local pluginModule = require(script.Parent.PluginModule)
pluginModule:Initialize(plugin)

-- Verify if the plugin reference was initialized
pluginModule:CheckForPluginGlobal()
```

**ModuleScript - Receive and Store the Plugin Global**

```lua
local pluginModule = {}
local plugin -- Local plugin reference

-- Initialize the plugin reference if not already set
function pluginModule:Initialize(pluginReference: Plugin)
	if plugin ~= pluginReference then
		plugin = pluginReference
	else
		error("Plugin is already initialized")
	end
end

-- Check if the plugin reference is set and print out appropriate info
function pluginModule:CheckForPluginGlobal()
	if plugin ~= nil then
		print("Plugin reference is set!")
	else
		warn("Plugin reference is missing!")
	end
end

return pluginModule
```

## Properties

### Property: Plugin.CollisionEnabled

```json
{
  "type": "boolean",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Data"
}
```

Returns whether the user has enabled **Collisions** in Studio's toolbar.

### Property: Plugin.DisableUIDragDetectorDrags

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

If `true`, toolbars and buttons for the plugin will ignore dragging
related to a [UIDragDetector](/docs/reference/engine/classes/UIDragDetector.md) instance.

### Property: Plugin.GridSize

```json
{
  "type": "float",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Data"
}
```

Returns the grid snapping size the user has set in Studio's toolbar. Note
that this property may have slight rounding errors; for example it may be
`0.0099999997764826` for a user setting of `0.01`, or `0.4000000059604645`
for a user setting of `0.4`.

### Property: Plugin.IsDebuggable

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

Indicates whether the plugin's scripts can be debugged in Studio. This
property is not accessible through scripts.

## Methods

### Method: Plugin:Activate

**Signature:** `Plugin:Activate(exclusiveMouse: boolean): ()`

This method sets the state of the calling plugin to activated. Activating
the plugin allows mouse control through the
[GetMouse()](/docs/reference/engine/classes/Plugin.md) method.

At any given time, there are either 0 or 1 activated plugins. Activating a
plugin will deactivate all other plugins and they will receive a
[Deactivation](/docs/reference/engine/classes/Plugin.md) event.

#### See Also

- [IsActivatedWithExclusiveMouse()](/docs/reference/engine/classes/Plugin.md)
  which returns `true` if the plugin is currently active with an exclusive
  mouse, after having been activated via this method.
- [Unloading](/docs/reference/engine/classes/Plugin.md) which fires immediately before the
  plugin is unloaded or reloaded via uninstallation, deactivation, or
  updating.

*Security: PluginSecurity · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `exclusiveMouse` | `boolean` |  | A boolean specifying whether to activate the plugin with exclusive mouse. If `true`, a [PluginMouse](/docs/reference/engine/classes/PluginMouse.md) can be retrieved via [GetMouse()](/docs/reference/engine/classes/Plugin.md). |

**Returns:** `()`

### Method: Plugin:CreateDockWidgetPluginGuiAsync

**Signature:** `Plugin:CreateDockWidgetPluginGuiAsync(pluginGuiId: string, dockWidgetPluginGuiInfo: DockWidgetPluginGuiInfo): DockWidgetPluginGui`

This method creates a new [DockWidgetPluginGui](/docs/reference/engine/classes/DockWidgetPluginGui.md) from the given
[DockWidgetPluginGuiInfo](/docs/reference/engine/datatypes/DockWidgetPluginGuiInfo.md). The first parameter, `pluginGuiId`,
should be a unique and consistent string. It is used to save the state of
the widget's dock state and other internal details.

*Yields · Security: PluginSecurity · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `pluginGuiId` | `string` |  | A unique and consistent identifier used to storing the widget's dock state and other internal details. |
| `dockWidgetPluginGuiInfo` | `DockWidgetPluginGuiInfo` |  | Describes the [DockWidgetPluginGui](/docs/reference/engine/classes/DockWidgetPluginGui.md) to create (initial state, size, etc). |

**Returns:** `DockWidgetPluginGui`

**Widget GUI Text Button**

This code, when ran inside a `Plugin`, creates a `DockWidgetPluginGui` with a
simple `TextButton`.

```lua
-- Create new 'DockWidgetPluginGuiInfo' object
local widgetInfo = DockWidgetPluginGuiInfo.new(
	Enum.InitialDockState.Float, -- Widget will be initialized in floating panel
	true, -- Widget will be initially enabled
	false, -- Don't override the previous enabled state
	200, -- Default width of the floating window
	300, -- Default height of the floating window
	150, -- Minimum width of the floating window (optional)
	150 -- Minimum height of the floating window (optional)
)

-- Create new widget GUI
local testWidget = plugin:CreateDockWidgetPluginGuiAsync("TestWidget", widgetInfo)

local testButton = Instance.new("TextButton")
testButton.BorderSizePixel = 0
testButton.TextSize = 20
testButton.TextColor3 = Color3.new(1, 0.2, 0.4)
testButton.AnchorPoint = Vector2.new(0.5, 0.5)
testButton.Size = UDim2.new(1, 0, 1, 0)
testButton.Position = UDim2.new(0.5, 0, 0.5, 0)
testButton.SizeConstraint = Enum.SizeConstraint.RelativeYY
testButton.Text = "Click Me"
testButton.Parent = testWidget
```

### Method: Plugin:CreatePluginAction

**Signature:** `Plugin:CreatePluginAction(actionId: string, text: string, statusTip: string, iconName: string, allowBinding?: boolean): PluginAction`

This method creates a [PluginAction](/docs/reference/engine/classes/PluginAction.md) which represents a generic
performable action in Studio with no directly‑associated
[PluginToolbarButton](/docs/reference/engine/classes/PluginToolbarButton.md).

See also [CreatePluginMenu()](/docs/reference/engine/classes/Plugin.md) which
creates a Studio [PluginMenu](/docs/reference/engine/classes/PluginMenu.md) that can display a list of
[PluginActions](/docs/reference/engine/classes/PluginAction.md).

*Security: PluginSecurity · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `actionId` | `string` |  | Must be a unique string that identifies this PluginAction from others. |
| `text` | `string` |  | The displayed name of the action. |
| `statusTip` | `string` |  | The displayed description of the action. |
| `iconName` | `string` |  | The name of the icon used to display the plugin. |
| `allowBinding` | `boolean` | `true` | Whether the [PluginAction](/docs/reference/engine/classes/PluginAction.md) will be hidden from Studio's shortcuts view. Useful for contextual actions. Defaults to true. |

**Returns:** `PluginAction`

**Creating a PluginAction**

This code sample visualizes how to create a [PluginAction](/docs/reference/engine/classes/PluginAction.md). These must
be created using the [Plugin:CreatePluginAction()](/docs/reference/engine/classes/Plugin.md) method in order to
work.

In order to work as expected, the code block must but pasted into the Command
Bar, but only once. Consecutive attempts at executing the code in the Command
Bar will result in an error because a plugin cannot create more than one
[PluginMenu](/docs/reference/engine/classes/PluginMenu.md) with the same ID.

When the created action is bound and [Triggered](/docs/reference/engine/classes/PluginAction.md),
it outputs `Hello world!`.

```lua
local pluginAction = plugin:CreatePluginAction(
	"HelloWorldAction",
	"Hello World",
	"Prints a 'Hello world!'",
	"rbxasset://textures/sparkle.png",
	true
)
pluginAction.Name = "Test Action"

local function actionTriggered()
	print("Hello world!")
end

pluginAction.Triggered:Connect(actionTriggered)
```

### Method: Plugin:CreatePluginMenu

**Signature:** `Plugin:CreatePluginMenu(id: string, title: string, icon: string): PluginMenu`

This function creates a new [PluginMenu](/docs/reference/engine/classes/PluginMenu.md) which is a context menu
that can be shown in Studio that displays a list of
[PluginActions](/docs/reference/engine/classes/PluginAction.md) and also supports submenus.

*Security: PluginSecurity · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `id` | `string` |  | Unique ID for the menu. |
| `title` | `string` |  | The text to be displayed when used as a submenu. |
| `icon` | `string` |  | The icon to be displayed when used as a submenu. |

**Returns:** `PluginMenu`

**Creating a PluginMenu and PluginMenuAction**

This code sample visualizes how [PluginMenus](/docs/reference/engine/classes/PluginMenu.md) and
[PluginActions](/docs/reference/engine/classes/PluginAction.md) behave when created for a [Plugin](/docs/reference/engine/classes/Plugin.md).
Outside of this example, you should not parent the plugin or its functional
components to the experience's workspace.

After executing the code, changing the created [BoolValue](/docs/reference/engine/classes/BoolValue.md) in the
experience's workspace opens the plugin's menus. Selecting an action from the
menus the function connected to the trigger signal.

```lua
-- This code can be pasted into the Command Bar, but only once
local pluginMenu = plugin:CreatePluginMenu(math.random(), "Test Menu")
pluginMenu.Name = "Test Menu"

pluginMenu:AddNewAction("ActionA", "A", "rbxasset://textures/loading/robloxTiltRed.png")
pluginMenu:AddNewAction("ActionB", "B", "rbxasset://textures/loading/robloxTilt.png")

local subMenu = plugin:CreatePluginMenu(math.random(), "C", "rbxasset://textures/explosion.png")
subMenu.Name = "Sub Menu"

subMenu:AddNewAction("ActionD", "D", "rbxasset://textures/whiteCircle.png")
subMenu:AddNewAction("ActionE", "E", "rbxasset://textures/icon_ROBUX.png")

pluginMenu:AddMenu(subMenu)
pluginMenu:AddSeparator()

pluginMenu:AddNewAction("ActionF", "F", "rbxasset://textures/sparkle.png")

local toggle = Instance.new("BoolValue")
toggle.Name = "TogglePluginMenu"
toggle.Parent = workspace

local function onToggled()
	if toggle.Value then
		toggle.Value = false

		local selectedAction = pluginMenu:ShowAsync()
		if selectedAction then
			print("Selected Action:", selectedAction.Text, "with ActionId:", selectedAction.ActionId)
		else
			print("User did not select an action!")
		end
	end
end

toggle.Changed:Connect(onToggled)
```

### Method: Plugin:CreateToolbar

**Signature:** `Plugin:CreateToolbar(name: string): PluginToolbar`

This method creates a new [PluginToolbar](/docs/reference/engine/classes/PluginToolbar.md) with the given name. The
toolbar can then be used to create plugin buttons.

*Security: PluginSecurity · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `name` | `string` |  | The visible text on the toolbar, labeling the group of buttons contained within. |

**Returns:** `PluginToolbar`

**Plugin:CreateToolbar**

This code creates a toolbar with the name "ExampleToolbar".

```lua
plugin:CreateToolbar("ExampleToolbar")
```

### Method: Plugin:Deactivate

**Signature:** `Plugin:Deactivate(): ()`

Deactivates the plugin. This will disengage the associated
[PluginMouse](/docs/reference/engine/classes/PluginMouse.md) if it has been activated.

#### See Also

- [Activate()](/docs/reference/engine/classes/Plugin.md) which sets the state of the calling
  plugin to activated.
- [Deactivation](/docs/reference/engine/classes/Plugin.md) which fires when the plugin is
  deactivated.
- [Unloading](/docs/reference/engine/classes/Plugin.md) which fires immediately before the
  plugin is unloaded or reloaded via uninstallation, deactivation, or
  updating.

*Security: PluginSecurity · Thread Safety: Unsafe*

**Returns:** `()`

### Method: Plugin:GetJoinMode

**Signature:** `Plugin:GetJoinMode(): JointCreationMode`

Returns the [JointCreationMode](/docs/reference/engine/enums/JointCreationMode.md) the user has set in Studio's toolbar.

*Security: PluginSecurity · Thread Safety: Unsafe*

**Returns:** `JointCreationMode`

### Method: Plugin:GetMouse

**Signature:** `Plugin:GetMouse(): PluginMouse`

This method returns a [PluginMouse](/docs/reference/engine/classes/PluginMouse.md) that can be used while the
plugin is active through [Activate()](/docs/reference/engine/classes/Plugin.md).

*Security: PluginSecurity · Thread Safety: Unsafe*

**Returns:** `PluginMouse`

**Plugin:GetMouse**

This code would print Button 1 pressed from PluginMouse each time the mouse's
left button was clicked.

```lua
local mouse = plugin:GetMouse()

local function button1Down()
	print("Button 1 pressed from PluginMouse")
end

mouse.Button1Down:Connect(button1Down)
```

### Method: Plugin:GetSelectedRibbonTool

**Signature:** `Plugin:GetSelectedRibbonTool(): RibbonTool`

This method returns the currently selected [RibbonTool](/docs/reference/engine/enums/RibbonTool.md).

*Security: PluginSecurity · Thread Safety: Unsafe*

**Returns:** `RibbonTool`

**Plugin:GetSelectedRibbonTool**

This code must be run from a plugin. This code selects the move tool, checks
which tool is selected, then prints out to the console which tool is selected.
SelectRibbonTool will not return the value until the next frame.

```lua
plugin:SelectRibbonTool(Enum.RibbonTool.Move, UDim2.new())
task.wait() -- wait for next frame
local selectedRibbonTool = plugin:GetSelectedRibbonTool()
print("The selected RibbonTool is", selectedRibbonTool)
```

### Method: Plugin:GetSetting

**Signature:** `Plugin:GetSetting(key: string): Variant`

Retrieves a previously stored value with the given key, or `nil` if the
given key doesn't exist.

Because multiple instances of the same plugin can run simultaneously (for
example, if multiple Studio windows are open), you shouldn't depend on
this value staying the same over time. The other plugin instances can
update the setting at any time.

This call can silently fail and return `nil` if multiple instances of the
same plugin are actively reading and writing data. If your plugin expects
to write to settings frequently, you should double-check the returned
value from this call after a short while to distinguish between a setting
being temporarily unavailable and a setting not existing.

*Security: PluginSecurity · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `key` | `string` |  | The string key that was previously passed to [SetSetting()](/docs/reference/engine/classes/Plugin.md). |

**Returns:** `Variant`

**Plugin:GetSetting**

The below example would print the value saved to the key FirstTime. If the key
doesn't exist, it would print nil.

```lua
local RAN_BEFORE_KEY = "RanBefore"
local didRunBefore = plugin:GetSetting(RAN_BEFORE_KEY)

if didRunBefore then
	print("Welcome back!")
else
	plugin:SetSetting(RAN_BEFORE_KEY, true)
	print("Welcome! Thanks for installing this plugin!")
end
```

### Method: Plugin:ImportFbxAnimationAsync

**Signature:** `Plugin:ImportFbxAnimationAsync(rigModel: Instance, isR15?: boolean): Instance`

This function prompts the user to open a `.fbx` animation file that can be
loaded onto the `rigModel`, then proceeds to insert the animation as a
[KeyframeSequence](/docs/reference/engine/classes/KeyframeSequence.md) in the [Workspace](/docs/reference/engine/classes/Workspace.md).

*Yields · Security: PluginSecurity · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `rigModel` | `Instance` |  | The rig model that the imported animation will be applied to. |
| `isR15` | `boolean` | `true` | Whether the animation file should be interpreted as an R15 rig. Defaults to `true`. |

**Returns:** `Instance`

### Method: Plugin:ImportFbxRigAsync

**Signature:** `Plugin:ImportFbxRigAsync(isR15?: boolean): Instance`

Prompts the user to open a `.fbx` file, uploads the individual components
of the model as meshes, and generates a character rig for use in
animation, which is loaded into the [Workspace](/docs/reference/engine/classes/Workspace.md).

*Yields · Security: PluginSecurity · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `isR15` | `boolean` | `true` | Whether the rig file should be interpreted as R15. Defaults to `true`. |

**Returns:** `Instance`

### Method: Plugin:Intersect

**Signature:** `Plugin:Intersect(objects: Instances): Instance`

Intersects the given parts and returns the resulting
[IntersectOperation](/docs/reference/engine/classes/IntersectOperation.md).

*Security: PluginSecurity · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `objects` | `Instances` |  | The array of [BaseParts](/docs/reference/engine/classes/BasePart.md) to intersect. |

**Returns:** `Instance`

### Method: Plugin:IsActivated

**Signature:** `Plugin:IsActivated(): boolean`

This function returns true if this plugin is currently active, after
having been activated via the [Activate()](/docs/reference/engine/classes/Plugin.md)
function.

*Security: PluginSecurity · Thread Safety: Unsafe*

**Returns:** `boolean` — A boolean indicating whether the plugin is currently active.

### Method: Plugin:IsActivatedWithExclusiveMouse

**Signature:** `Plugin:IsActivatedWithExclusiveMouse(): boolean`

This function returns `true` if this plugin is currently active with an
exclusive mouse, after having been activated via the
[Activate()](/docs/reference/engine/classes/Plugin.md) function. If this returns `true`, a
[PluginMouse](/docs/reference/engine/classes/PluginMouse.md) can be retrieved via
[GetMouse()](/docs/reference/engine/classes/Plugin.md).

#### See Also

- [Deactivation](/docs/reference/engine/classes/Plugin.md) which fires when the plugin is
  deactivated.
- [Unloading](/docs/reference/engine/classes/Plugin.md) which fires immediately before the
  plugin is unloaded or reloaded via uninstallation, deactivation, or
  updating.

*Security: PluginSecurity · Thread Safety: Unsafe*

**Returns:** `boolean` — Whether this plugin is currently active with an exclusive mouse.

### Method: Plugin:Negate

**Signature:** `Plugin:Negate(objects: Instances): Instances`

Negates the given parts and returns the resulting
[NegateOperations](/docs/reference/engine/classes/NegateOperation.md).

*Security: PluginSecurity · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `objects` | `Instances` |  | The array of [BaseParts](/docs/reference/engine/classes/BasePart.md) to negate. |

**Returns:** `Instances`

### Method: Plugin:OpenWikiPage

**Signature:** `Plugin:OpenWikiPage(url: string): ()`

Opens the context help window to the wiki page that `url` links to.

*Security: PluginSecurity · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `url` | `string` |  | The URL of the wiki/documentation page to open. |

**Returns:** `()`

**Plugin:OpenWikiPage**

The following, when executed in a plugin, will open the
[BasePart API page](/docs/reference/engine/classes/BasePart.md) in the context help.

```lua
plugin:OpenWikiPage("API:Class/BasePart")
```

### Method: Plugin:PromptForExistingAssetId

**Signature:** `Plugin:PromptForExistingAssetId(assetType: string): int64`

Opens a window in Roblox Studio that prompts the user to select an
existing animation asset from the user's inventory. Pass `Animation` as
the `assetType` argument.

Returns the selected animation asset ID as an `int64`, or `-1` if the user
closes the dialog without selecting an asset. If `assetType` is not
`Animation`, this method errors.

*Yields · Security: PluginSecurity · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `assetType` | `string` |  | The asset type to browse. Only `Animation` is supported. |

**Returns:** `int64`

### Method: Plugin:PromptForExistingAssetIdAsync

**Signature:** `Plugin:PromptForExistingAssetIdAsync(assetType: string): int64`

Opens a window in Roblox Studio that prompts the user to select an
existing animation asset from the user's inventory. Pass `Animation` as
the `assetType` argument.

Returns the selected animation asset ID as an `int64`, or `-1` if the user
closes the dialog without selecting an asset. If `assetType` is not
`Animation`, this method errors.

*Yields · Security: PluginSecurity · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `assetType` | `string` |  | The asset type to browse. Only `Animation` is supported. |

**Returns:** `int64`

### Method: Plugin:PromptSaveSelectionAsync

**Signature:** `Plugin:PromptSaveSelectionAsync(suggestedFileName: string): boolean`

Prompts the user to save their current selection with the specified file
name. Returns `true` if the user did save the file.

*Yields · Security: PluginSecurity · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `suggestedFileName` | `string` |  | The default file name shown in the save dialog. Defaults to an empty string. |

**Returns:** `boolean`

### Method: Plugin:SaveSelectedToRoblox

**Signature:** `Plugin:SaveSelectedToRoblox(): ()`

Opens an upload window for the user's current selection.

*Security: PluginSecurity · Thread Safety: Unsafe*

**Returns:** `()`

### Method: Plugin:SelectRibbonTool

**Signature:** `Plugin:SelectRibbonTool(tool: RibbonTool, position: UDim2): ()`

Activates the specified Roblox Studio tool. If the tool opens a window,
the position parameter specifies where it should be shown on the screen.

An object must be selected in order for this to work correctly. Also note
that altering the scale fields of the `position` property will not affect
the dialog popups.

*Security: PluginSecurity · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `tool` | `RibbonTool` |  | The [RibbonTool](/docs/reference/engine/enums/RibbonTool.md) to activate. |
| `position` | `UDim2` |  | The [UDim2](/docs/reference/engine/datatypes/UDim2.md) screen position at which to show the tool's dialog window, if applicable. |

**Returns:** `()`

### Method: Plugin:Separate

**Signature:** `Plugin:Separate(objects: Instances): Instances`

Separates the given [UnionOperations](/docs/reference/engine/classes/UnionOperation.md) and returns the
resulting parts.

*Security: PluginSecurity · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `objects` | `Instances` |  | The array of [UnionOperations](/docs/reference/engine/classes/UnionOperation.md) to separate. |

**Returns:** `Instances`

### Method: Plugin:SetSetting

**Signature:** `Plugin:SetSetting(key: string, value: Variant): ()`

Stores a given value for later use under the given key. The value will
persist even after Roblox Studio is closed. These settings are saved in
`.json` format as a map with string keys. Arrays are automatically
converted to maps by converting the numeric keys to strings first.

Note that the `.json` format imposes additional restrictions, including
the following characters which can corrupt the settings file:

- Backslashes (`\`) in keys or values, in particular escaped quotes
  (`\"`).
- Newlines (`\n`) in keys.
- Quotes (`"`) in keys.
- Periods (`.`) in keys.

This call can silently fail if multiple instances of the same plugin are
actively reading and writing data. If your plugin expects to write to
settings frequently, you may check that the data has been properly written
by calling [GetSetting()](/docs/reference/engine/classes/Plugin.md).

*Security: PluginSecurity · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `key` | `string` |  | The string key to store the value under. |
| `value` | `Variant` |  | The value to store. Must be JSON-serializable (string, number, boolean, table, or `nil`). |

**Returns:** `()`

**Plugin:GetSetting and Plugin:SetSetting**

This code sample demonstrates use of the [Plugin:GetSetting()](/docs/reference/engine/classes/Plugin.md) and
[Plugin:SetSetting()](/docs/reference/engine/classes/Plugin.md) functions. They detect if a plugin is running for
the first time by setting a key. If the key is `true`, it prints a "welcome
back" message; otherwise it prints a "first run" message and sets the key to
`true`.

```lua
local RAN_BEFORE_KEY = "RunBefore"
local hasRunBefore = plugin:GetSetting(RAN_BEFORE_KEY)

if hasRunBefore then
	print("Welcome back!")
else
	print("Thanks for installing this plugin!")
	plugin:SetSetting(RAN_BEFORE_KEY, true)
end
```

### Method: Plugin:StartDrag

**Signature:** `Plugin:StartDrag(dragData: Dictionary): ()`

This method initiates a drag action using a dictionary of parameters. The
parameters are as follows:

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `Sender` | string | `""` | Identifies the source of the drag action to the drop target |
| `MimeType` | string | `""` | The MIME type of `Data`. |
| `Data` | string | `""` | Information about the drag action, for example what is being dragged. Should be used by the drop target. |
| `MouseIcon` | [Content](/docs/reference/engine/datatypes/Content.md) | `""` | The icon to use for the mouse cursor during the drag. If empty, uses the default cursor. |
| `DragIcon` | [Content](/docs/reference/engine/datatypes/Content.md) | `""` | An image to render under the mouse cursor during the drag. This should represent the item being dragged. |
| `HotSpot` | [Vector2](/docs/reference/engine/datatypes/Vector2.md) | [Vector2.new(0, 0)](/docs/reference/engine/datatypes/Vector2.md) | The pixel offset from the top-left where the cursor should "hold" the `DragIcon`. |

See also [PluginGui.PluginDragEntered](/docs/reference/engine/classes/PluginGui.md),
[PluginGui.PluginDragMoved](/docs/reference/engine/classes/PluginGui.md), [PluginGui.PluginDragDropped](/docs/reference/engine/classes/PluginGui.md),
and [PluginGui.PluginDragLeft](/docs/reference/engine/classes/PluginGui.md).

*Security: PluginSecurity · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `dragData` | `Dictionary` |  | A dictionary describing the drag, including fields such as `Sender`, `MimeType`, `Data`, `MouseIcon`, `DragIcon`, and `HotSpot`. |

**Returns:** `()`

**Plugin Drag and Drop**

This code sample creates two plugin widget windows: a drag source and a drop
target. In the source window, the script creates a [TextBox](/docs/reference/engine/classes/TextBox.md) and
[TextButton](/docs/reference/engine/classes/TextButton.md) to allow the user to begin a plugin drag action. The drop
target window will display the MIME type of whatever is dragged into it. If
the MIME type is `text/plain`, it will display the plain text data instead.

To run this code sample as a plugin, paste it into a [Script](/docs/reference/engine/classes/Script.md). Then,
right-click the script in the **Explorer** window and choose **Save as Local
Plugin**.

```lua
assert(plugin, "This script must be run as a Studio plugin")

local widgetInfo = DockWidgetPluginGuiInfo.new(Enum.InitialDockState.Float, true, true, 300, 200)

local dragSourceWidget = plugin:CreateDockWidgetPluginGuiAsync("Drag Source", widgetInfo)
dragSourceWidget.Title = "Drag Source"

local textBox = Instance.new("TextBox")
textBox.Parent = dragSourceWidget
textBox.Size = UDim2.new(1, 0, 0, 32)
textBox.Text = "Hello, plugin drags"

local dragButton = Instance.new("TextButton")
dragButton.Size = UDim2.new(1, 0, 1, -32)
dragButton.Position = UDim2.new(0, 0, 0, 32)
dragButton.Text = "Edit the text above, then start drag here"
dragButton.Parent = dragSourceWidget

function onMouseButton1Down()
	local dragData = {
		Sender = "SomeDragSource",
		MimeType = "text/plain",
		Data = textBox.Text,
		MouseIcon = "",
		DragIcon = "",
		HotSpot = Vector2.new(0, 0),
	}
	plugin:StartDrag(dragData)
end

dragButton.MouseButton1Down:Connect(onMouseButton1Down)

-- This widget will receive drops
local dragTargetWidget = plugin:CreateDockWidgetPluginGuiAsync("Drop Target", widgetInfo)
dragTargetWidget.Title = "Drop Target"

-- This TextLabel will display what was dropped
local textLabel = Instance.new("TextLabel")
textLabel.Size = UDim2.new(1, 0, 1, 0)
textLabel.Text = "Drop here..."
textLabel.Parent = dragTargetWidget

local function onDragDrop(dragData)
	if dragData.MimeType == "text/plain" then
		textLabel.Text = dragData.Data
	else
		textLabel.Text = dragData.MimeType
	end
end

dragTargetWidget.PluginDragDropped:Connect(onDragDrop)

dragTargetWidget.PluginDragEntered:Connect(function(_dragData)
	print("PluginDragEntered")
end)

dragTargetWidget.PluginDragLeft:Connect(function(_dragData)
	print("PluginDragLeft")
end)

dragTargetWidget.PluginDragMoved:Connect(function(_dragData)
	print("PluginDragMoved")
end)
```

### Method: Plugin:Union

**Signature:** `Plugin:Union(objects: Instances): Instance`

Unions the given parts and returns the resulting [UnionOperation](/docs/reference/engine/classes/UnionOperation.md).

*Security: PluginSecurity · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `objects` | `Instances` |  | The array of [BaseParts](/docs/reference/engine/classes/BasePart.md) to union together. |

**Returns:** `Instance`

### Method: Plugin:CreateDockWidgetPluginGui

**Signature:** `Plugin:CreateDockWidgetPluginGui(pluginGuiId: string, dockWidgetPluginGuiInfo: DockWidgetPluginGuiInfo): DockWidgetPluginGui`

> **Deprecated:** This method has been superseded by [CreateDockWidgetPluginGuiAsync()](/docs/reference/engine/classes/Plugin.md).

This method has been superseded by
[CreateDockWidgetPluginGuiAsync()](/docs/reference/engine/classes/Plugin.md).
It creates a new [DockWidgetPluginGui](/docs/reference/engine/classes/DockWidgetPluginGui.md) from the given
[DockWidgetPluginGuiInfo](/docs/reference/engine/datatypes/DockWidgetPluginGuiInfo.md).

*Yields · Security: PluginSecurity · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `pluginGuiId` | `string` |  | A unique and consistent identifier used to storing the widget's dock state and other internal details. |
| `dockWidgetPluginGuiInfo` | `DockWidgetPluginGuiInfo` |  | Describes the [DockWidgetPluginGui](/docs/reference/engine/classes/DockWidgetPluginGui.md) to create (initial state, size, etc). |

**Returns:** `DockWidgetPluginGui`

### Method: Plugin:GetStudioUserId

**Signature:** `Plugin:GetStudioUserId(): int64`

Returns the Studio user's userId if they're logged in, otherwise
returns 0.

*Security: PluginSecurity · Thread Safety: Unsafe*

**Returns:** `int64`

### Method: Plugin:ImportFbxAnimation

**Signature:** `Plugin:ImportFbxAnimation(rigModel: Instance, isR15?: boolean): Instance`

This method prompts the user to open a `.fbx` animation file that can be
loaded onto the `rigModel`, then proceeds to insert the animation as a
[KeyframeSequence](/docs/reference/engine/classes/KeyframeSequence.md) named "ImportedAnimation" in the
[Workspace](/docs/reference/engine/classes/Workspace.md). The `isR15` parameter determines whether the file is
interpreted as an R15 rig and defaults to `true`.

Returns the resulting [KeyframeSequence](/docs/reference/engine/classes/KeyframeSequence.md) instance. Errors if
`rigModel` is `nil` or if the user cancels the file dialog without
selecting a file.

*Yields · Security: PluginSecurity · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `rigModel` | `Instance` |  | The rig model that the imported animation will be applied to. |
| `isR15` | `boolean` | `true` | Whether the animation file should be interpreted as an R15 rig. Defaults to `true`. |

**Returns:** `Instance`

### Method: Plugin:ImportFbxRig

**Signature:** `Plugin:ImportFbxRig(isR15?: boolean): Instance`

> **Deprecated:** This method has been superseded by [ImportFbxRigAsync()](/docs/reference/engine/classes/Plugin.md).

This method has been superseded by
[ImportFbxRigAsync()](/docs/reference/engine/classes/Plugin.md). It prompts the
user to open a `.fbx` file, uploads the individual components of the model
as meshes, and generates a character rig for use in animation, which is
loaded into the [Workspace](/docs/reference/engine/classes/Workspace.md).

*Yields · Security: PluginSecurity · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `isR15` | `boolean` | `true` | Whether the rig file should be interpreted as R15. Defaults to `true`. |

**Returns:** `Instance`

### Method: Plugin:OpenScript

**Signature:** `Plugin:OpenScript(script: LuaSourceContainer, lineNumber?: int): ()`

Used to open the given script instance in an editor window, in Roblox
studio, at the given line. If no line is given as an argument it will
default to 1.

Prefer
[ScriptEditorService:OpenScriptDocumentAsync()](/docs/reference/engine/classes/ScriptEditorService.md),
which provides better integration with other script editor APIs and is
more extensible.

*Security: PluginSecurity · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `script` | `LuaSourceContainer` |  | The [LuaSourceContainer](/docs/reference/engine/classes/LuaSourceContainer.md) script instance to open. |
| `lineNumber` | `int` | `1` | The line number to navigate to in the editor. Defaults to `1`. |

**Returns:** `()`

**Plugin:OpenScript**

The following creates a new [Script](/docs/reference/engine/classes/Script.md) in the Workspace and opens it.

```lua
local newScript = Instance.new("Script")
newScript.Parent = workspace
plugin:OpenScript(newScript)
```

### Method: Plugin:PromptSaveSelection

**Signature:** `Plugin:PromptSaveSelection(suggestedFileName: string): boolean`

> **Deprecated:** This method has been superseded by [PromptSaveSelectionAsync()](/docs/reference/engine/classes/Plugin.md).

This method has been superseded by
[PromptSaveSelectionAsync()](/docs/reference/engine/classes/Plugin.md). It
prompts the user to save their current selection with the specified file
name and returns whether the user completed the save.

*Yields · Security: PluginSecurity · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `suggestedFileName` | `string` |  | The default file name shown in the save dialog. Defaults to an empty string. |

**Returns:** `boolean`

## Events

### Event: Plugin.Deactivation

**Signature:** `Plugin.Deactivation()`

Fired when the [Plugin](/docs/reference/engine/classes/Plugin.md) is deactivated. This occurs when either the
plugin code calls [Deactivate()](/docs/reference/engine/classes/Plugin.md), or because
some other plugin called [Activate()](/docs/reference/engine/classes/Plugin.md), which
forces all other plugins to lose their active state.

See also [Unloading](/docs/reference/engine/classes/Plugin.md) which fires immediately before
the plugin is unloaded or reloaded via uninstallation, deactivation, or
updating.

*Security: PluginSecurity*

### Event: Plugin.Unloading

**Signature:** `Plugin.Unloading()`

This event fires immediately before the [Plugin](/docs/reference/engine/classes/Plugin.md) stops running.
Plugins are unloaded when disabled, uninstalled, about to be updated, or
when the place is closing.

It enables a plugin to clean up after itself before its scripts stop
running, e.g. to remove unnecessary instances from the [DataModel](/docs/reference/engine/classes/DataModel.md).
If a plugin does not clean up properly, the old copies will remain. When
this occurs, users may be forced to close and reopen the place which is a
bad user experience.

Plugin-related instances such as
[PluginToolbarButtons](/docs/reference/engine/classes/PluginToolbarButton.md),
[DockWidgetPluginGuis](/docs/reference/engine/classes/DockWidgetPluginGui.md), and
[PluginGuis](/docs/reference/engine/classes/PluginGui.md) are automatically cleaned up when the plugin
is unloaded so there is no need to remove them.

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