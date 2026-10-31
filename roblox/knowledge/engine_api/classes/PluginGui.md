---
name: PluginGui
last_updated: 2026-10-30T19:55:53Z
inherits:
  - LayerCollector
  - GuiBase2d
  - GuiBase
  - Instance
  - Object
type: class
memory_category: Instances
tags:
  - NotCreatable
  - NotReplicated
summary: "An abstract base class for GUIs that display GuiObjects in Roblox Studio widgets."
---

# Class: PluginGui

> An abstract base class for GUIs that display [GuiObjects](/docs/reference/engine/classes/GuiObject.md) in
> Roblox Studio widgets.

## Description

PluginGui is an abstract class for GUIs that allow the display of
[GuiObjects](/docs/reference/engine/classes/GuiObject.md) in various Roblox Studio widgets. As of right
now, the only available PluginGui type is [DockWidgetPluginGui](/docs/reference/engine/classes/DockWidgetPluginGui.md), but
there may be more in the future!

## Properties

### Property: PluginGui.Title

```json
{
  "type": "string",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Data",
  "capabilities": [
    "UI"
  ]
}
```

The title that is displayed above the contents of the [PluginGui](/docs/reference/engine/classes/PluginGui.md).
Defaults to empty string.

## Methods

### Method: PluginGui:BindToClose

**Signature:** `PluginGui:BindToClose(function?: Function): ()`

This method binds a function that runs when the user clicks the close
button of the [PluginGui](/docs/reference/engine/classes/PluginGui.md). The widget closes and its
[Enabled](/docs/reference/engine/classes/LayerCollector.md) property becomes `false` even when
a function is bound, so the function can't prevent or delay closing. Use
it to perform tasks such as saving work when the widget closes.

For example, the following code saves work when the user closes the
widget:

```lua
local function saveWork()
	-- Save the user's work here.
end

pluginGui:BindToClose(function()
	saveWork()
end)
```

Call `BindToClose()` without an argument to unbind the current function:

```lua
pluginGui:BindToClose()
```

See also:

- [Plugin:CreateDockWidgetPluginGuiAsync()](/docs/reference/engine/classes/Plugin.md) to create a
  [PluginGui](/docs/reference/engine/classes/PluginGui.md)
- [DataModel:BindToClose()](/docs/reference/engine/classes/DataModel.md), which can be used to bind a function to
  the game ending and should not be confused with this function

*Security: None · Thread Safety: Unsafe · Capabilities: UI*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `function` | `Function` | `nil` | The function to bind the close button to. If no function is specified then any previously specified function will be unbound. |

**Returns:** `()`

### Method: PluginGui:GetRelativeMousePosition

**Signature:** `PluginGui:GetRelativeMousePosition(): Vector2`

GetRelativeMousePosition returns the position of the mouse relative to the
top-left corner of the [PluginGui](/docs/reference/engine/classes/PluginGui.md). The returned value changes only
if a mouse input began on the PluginGui, or if the mouse is presently
hovering over the window.

*Security: PluginSecurity · Thread Safety: Unsafe · Capabilities: UI*

**Returns:** `Vector2` — The screen position of the mouse relative to the PluginGui in pixels.

**PluginGui:GetRelativeMousePosition**

```lua
local RunService = game:GetService("RunService")

local widgetInfo = DockWidgetPluginGuiInfo.new(
	Enum.InitialDockState.Float,
	true,
	false, -- Enabled state, override
	200,
	300, -- Size
	150,
	150 -- Minimum size
)

local testWidget = plugin:CreateDockWidgetPluginGuiAsync("TestWidget", widgetInfo)

function update()
	local v2 = testWidget:GetRelativeMousePosition()
	testWidget.Title = ("(%d, %d)"):format(v2.x, v2.y)
end

RunService.Stepped:Connect(update)

update()
```

## Events

### Event: PluginGui.PluginDragDropped

**Signature:** `PluginGui.PluginDragDropped(dragData: Dictionary)`

**PluginDragDropped** fires when the user releases their mouse over a
[PluginGui](/docs/reference/engine/classes/PluginGui.md) during a drag operation started by
[Plugin:StartDrag()](/docs/reference/engine/classes/Plugin.md).

See also:

- [PluginGui.PluginDragEntered](/docs/reference/engine/classes/PluginGui.md)
- [PluginGui.PluginDragLeft](/docs/reference/engine/classes/PluginGui.md)
- [PluginGui.PluginDragMoved](/docs/reference/engine/classes/PluginGui.md)

*Security: PluginSecurity · Capabilities: UI*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `dragData` | `Dictionary` | A copy of the data originally passed to [Plugin:StartDrag()](/docs/reference/engine/classes/Plugin.md). |

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

### Event: PluginGui.PluginDragEntered

**Signature:** `PluginGui.PluginDragEntered(dragData: Dictionary)`

**PluginDragEntered** fires when the user's mouse enters the
[PluginGui](/docs/reference/engine/classes/PluginGui.md) during a drag operation started by
[Plugin:StartDrag()](/docs/reference/engine/classes/Plugin.md).

This event is useful for displaying a "Drop Here" UI on PluginGuis where a
drag operation can be dropped. Such a UI should be hidden when either
[PluginDragLeft](/docs/reference/engine/classes/PluginGui.md) or
[PluginDragDropped](/docs/reference/engine/classes/PluginGui.md) fire.

See also:

- [PluginGui.PluginDragLeft](/docs/reference/engine/classes/PluginGui.md)
- [PluginGui.PluginDragMoved](/docs/reference/engine/classes/PluginGui.md)
- [PluginGui.PluginDragDropped](/docs/reference/engine/classes/PluginGui.md)

*Security: PluginSecurity · Capabilities: UI*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `dragData` | `Dictionary` | A copy of the data originally passed to [Plugin:StartDrag()](/docs/reference/engine/classes/Plugin.md). |

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

### Event: PluginGui.PluginDragLeft

**Signature:** `PluginGui.PluginDragLeft(dragData: Dictionary)`

**PluginDragLeft** fires when the user's mouse leaves a [PluginGui](/docs/reference/engine/classes/PluginGui.md)
during a drag operation started by [Plugin:StartDrag()](/docs/reference/engine/classes/Plugin.md).

This event and [PluginDragDropped](/docs/reference/engine/classes/PluginGui.md) are
useful for hiding a "Drop Here" UI on PluginGuis where a drag operation
can be dropped. Such a UI should be shown when either
[PluginDragEntered](/docs/reference/engine/classes/PluginGui.md) fires.

See also:

- [PluginGui.PluginDragEntered](/docs/reference/engine/classes/PluginGui.md)
- [PluginGui.PluginDragMoved](/docs/reference/engine/classes/PluginGui.md)
- [PluginGui.PluginDragDropped](/docs/reference/engine/classes/PluginGui.md)

*Security: PluginSecurity · Capabilities: UI*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `dragData` | `Dictionary` | A copy of the data originally passed to [Plugin:StartDrag()](/docs/reference/engine/classes/Plugin.md). |

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

### Event: PluginGui.PluginDragMoved

**Signature:** `PluginGui.PluginDragMoved(dragData: Dictionary)`

**PluginDragMoved** fires when the user's mouse moves within a
[PluginGui](/docs/reference/engine/classes/PluginGui.md) during a drag operation started by
[Plugin:StartDrag()](/docs/reference/engine/classes/Plugin.md).

See also:

- [PluginGui.PluginDragEntered](/docs/reference/engine/classes/PluginGui.md)
- [PluginGui.PluginDragLeft](/docs/reference/engine/classes/PluginGui.md)
- [PluginGui.PluginDragDropped](/docs/reference/engine/classes/PluginGui.md)

*Security: PluginSecurity · Capabilities: UI*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `dragData` | `Dictionary` | A copy of the data originally passed to [Plugin:StartDrag()](/docs/reference/engine/classes/Plugin.md). |

### Event: PluginGui.WindowFocused

**Signature:** `PluginGui.WindowFocused()`

**WindowFocused** fires immediately when the user starts interacting with
the PluginGui's window, usually by clicking on it. This functions works
similarly to the similarly-named [UserInputService.WindowFocused](/docs/reference/engine/classes/UserInputService.md)
event. It fires before any [GuiObject.InputBegan](/docs/reference/engine/classes/GuiObject.md) events related to
mouse buttons.

If another [PluginGui](/docs/reference/engine/classes/PluginGui.md) is in focus and the user focuses this
PluginGui, then this event fires after the other's
[WindowFocusReleased](/docs/reference/engine/classes/PluginGui.md) event. However,
if the main game window was in focus, this event fires **after**
[UserInputService.WindowFocusReleased](/docs/reference/engine/classes/UserInputService.md).

*Security: PluginSecurity · Capabilities: UI*

**Detecting PluginGui Focus State**

This code sample demonstrates how the focus state of a `PluginGui` can be
tracked using the [WindowFocused()](/docs/reference/engine/classes/PluginGui.md) and
[WindowFocusReleased()](/docs/reference/engine/classes/PluginGui.md) events. It changes
the [Title()](/docs/reference/engine/classes/PluginGui.md) as the focus state changes.

```lua
local info = DockWidgetPluginGuiInfo.new(Enum.InitialDockState.Float, true, true, 200, 50, 1, 1)

local widget = plugin:CreateDockWidgetPluginGuiAsync("TestWidget", info)

local function onFocusReleased()
	widget.Title = "I'm not in focus :("
end

local function onFocused()
	widget.Title = "I'm in focus :D"
end

widget.WindowFocusReleased:Connect(onFocusReleased)

widget.WindowFocused:Connect(onFocused)
```

### Event: PluginGui.WindowFocusReleased

**Signature:** `PluginGui.WindowFocusReleased()`

**WindowFocusReleased** fires immediately when the user stops interacting
with the PluginGui's window, usually by clicking on something not in the
window. This functions works similarly to the similarly-named
[UserInputService.WindowFocusReleased](/docs/reference/engine/classes/UserInputService.md) event.

If focus is moving to another [PluginGui](/docs/reference/engine/classes/PluginGui.md) while the user had this
PluginGui in focus, then this event fires before the other's
[WindowFocused](/docs/reference/engine/classes/PluginGui.md) event. However, if the main
game window is being put in focus, this event fires **after**
[UserInputService.WindowFocused](/docs/reference/engine/classes/UserInputService.md).

*Security: PluginSecurity · Capabilities: UI*

**Detecting PluginGui Focus State**

This code sample demonstrates how the focus state of a `PluginGui` can be
tracked using the [WindowFocused()](/docs/reference/engine/classes/PluginGui.md) and
[WindowFocusReleased()](/docs/reference/engine/classes/PluginGui.md) events. It changes
the [Title()](/docs/reference/engine/classes/PluginGui.md) as the focus state changes.

```lua
local info = DockWidgetPluginGuiInfo.new(Enum.InitialDockState.Float, true, true, 200, 50, 1, 1)

local widget = plugin:CreateDockWidgetPluginGuiAsync("TestWidget", info)

local function onFocusReleased()
	widget.Title = "I'm not in focus :("
end

local function onFocused()
	widget.Title = "I'm in focus :D"
end

widget.WindowFocusReleased:Connect(onFocusReleased)

widget.WindowFocused:Connect(onFocused)
```

## Inherited Members

### From [LayerCollector](/docs/reference/engine/classes/LayerCollector.md)

- **Property `Enabled`** (`boolean`): Toggles the visibility of this LayerCollector.
- **Property `ResetOnSpawn`** (`boolean`): Determines if the LayerCollector resets (deletes itself and
- **Property `ZIndexBehavior`** (`ZIndexBehavior`): Controls how GuiObject.ZIndex behaves on all descendants of this
- **Method `GetLayoutNodeTree(): Dictionary`**:  *(deprecated)*

### From [GuiBase2d](/docs/reference/engine/classes/GuiBase2d.md)

- **Property `AbsolutePosition`** (`Vector2`): Describes the actual screen position of a GuiBase2d element, in
- **Property `AbsoluteRotation`** (`float`): Describes the actual screen rotation of a GuiBase2d element, in
- **Property `AbsoluteSize`** (`Vector2`): Describes the actual screen size of a GuiBase2d element, in
- **Property `AutoLocalize`** (`boolean`): When set to `true`, localization will be applied to this GuiBase2d
- **Property `Localize`** (`boolean`): Automatically set to true when a localization table's *(deprecated, hidden)*
- **Property `RootLocalizationTable`** (`LocalizationTable`): A reference to a LocalizationTable to be used to apply automated
- **Property `SelectionBehaviorDown`** (`SelectionBehavior`): Customizes gamepad selection behavior in the down direction.
- **Property `SelectionBehaviorLeft`** (`SelectionBehavior`): Customizes gamepad selection behavior in the left direction.
- **Property `SelectionBehaviorRight`** (`SelectionBehavior`): Customizes gamepad selection behavior in the right direction.
- **Property `SelectionBehaviorUp`** (`SelectionBehavior`): Customizes gamepad selection behavior in the up direction.
- **Property `SelectionGroup`** (`boolean`): Allows customization of gamepad selection movement.
- **Event `SelectionChanged`**: Fires when the gamepad selection moves to, leaves, or changes within the

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