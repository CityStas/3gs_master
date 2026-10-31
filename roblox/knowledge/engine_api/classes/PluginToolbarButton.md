---
name: PluginToolbarButton
last_updated: 2026-10-30T19:55:53Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
tags:
  - NotCreatable
summary: "A button on a PluginToolbar in the Studio ribbon, created by PluginToolbar:CreateButton(), that fires Click when pressed."
---

# Class: PluginToolbarButton

> A button on a [PluginToolbar](/docs/reference/engine/classes/PluginToolbar.md) in the Studio ribbon, created by
> [PluginToolbar:CreateButton()](/docs/reference/engine/classes/PluginToolbar.md), that fires
> [Click](/docs/reference/engine/classes/PluginToolbarButton.md) when pressed.

## Description

A `PluginToolbarButton` object is created through the
[PluginToolbar:CreateButton()](/docs/reference/engine/classes/PluginToolbar.md) function. It allows the user to initiate
a single, one-off action in Roblox Studio through the
[Click](/docs/reference/engine/classes/PluginToolbarButton.md) event. Toolbar buttons can also be
assigned a keyboard shortcut through Studio's **File**&nbsp;⟩ **Customize
Shortcuts** window.

When pressed, the [Click](/docs/reference/engine/classes/PluginToolbarButton.md) event fires. A
button will also remain in the pressed state, which may be set manually using
[SetActive()](/docs/reference/engine/classes/PluginToolbarButton.md). Upon plugin activation
([Plugin:Activate()](/docs/reference/engine/classes/Plugin.md)), buttons in all other
[PluginToolbars](/docs/reference/engine/classes/PluginToolbar.md) will be toggled off. If all buttons in a
toolbar are off, the toolbar's plugin is deactivated
([Plugin:Deactivate()](/docs/reference/engine/classes/Plugin.md)).

When the game viewport is not visible, buttons will be disabled as if their
[Enabled](/docs/reference/engine/classes/PluginToolbarButton.md) property were false. Disabled
buttons are desaturated and do not respond to user clicks. By setting
[ClickableWhenViewportHidden](/docs/reference/engine/classes/PluginToolbarButton.md)
to true, you can allow plugin buttons to remain clickable, such as during
script editing.

## Properties

### Property: PluginToolbarButton.ClickableWhenViewportHidden

```json
{
  "type": "boolean",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": true,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Appearance"
}
```

This property determines whether a [PluginToolbarButton](/docs/reference/engine/classes/PluginToolbarButton.md) may be
clicked while the 3D viewport is hidden, such as when a [Script](/docs/reference/engine/classes/Script.md) is
being edited in another tab.

Typically, this property should be enabled if an action triggered by a
plugin button's [Click](/docs/reference/engine/classes/PluginToolbarButton.md) event doesn't
occur in the 3D world ([Workspace](/docs/reference/engine/classes/Workspace.md)). For example, a button that
opens a widget should have this property as `true`, since showing a widget
is visible to the user even if the 3D view isn't visible.

### Property: PluginToolbarButton.Enabled

```json
{
  "type": "boolean",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": true,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Appearance"
}
```

This property determines whether a button is clickable in general. When
`false`, the button will be greyed out and unclickable, preventing the
user from firing the [Click](/docs/reference/engine/classes/PluginToolbarButton.md) event.
Buttons are enabled by default.

When re-enabling this property, the plugin button's state won't be
remembered from the previous state in which the user left the button in.
Instead, it will default to the last state set by
[SetActive()](/docs/reference/engine/classes/PluginToolbarButton.md) or to the inactive
state if [SetActive()](/docs/reference/engine/classes/PluginToolbarButton.md) was never
used.

Plugins should disable their buttons when the button action isn't relevant
in the current context. For example, a plugin button that assigns random
colors to selected should not be enabled when the selection contains no
parts.

See also
[ClickableWhenViewportHidden](/docs/reference/engine/classes/PluginToolbarButton.md)
which determines whether a button is clickable when the game view is
hidden (and not just in general).

**BrickColor Randomizer Plugin**

This code sample is for a studio `Plugin`. The plugin creates a
`PluginToolbarButton` which randomizes the
[BrickColor()](/docs/reference/engine/classes/BasePart.md) of each selected part using
`BrickColor.random()`. Furthermore, the button is only enabled if at least one
part is selected. It does this by detecting changes in the `Selection` using
[Selection.SelectionChanged](/docs/reference/engine/classes/Selection.md).

```lua
assert(plugin, "This script must be run as a plugin")

local Selection = game:GetService("Selection")

local toolbar = plugin:CreateToolbar("Parts")
local pluginToolbarButton = toolbar:CreateButton(
	"Randomize Colors",
	"Click this button to assign random colors to selected parts",
	"rbxassetid://5325741572" -- A rainbow
)

local function onClick()
	local selection = Selection:Get()
	for _, object in pairs(selection) do
		if object:IsA("BasePart") then
			object.BrickColor = BrickColor.random()
		end
	end
end
pluginToolbarButton.Click:Connect(onClick)

local function doesSelectionContainAPart()
	local selection = Selection:Get()
	for _, object in pairs(selection) do
		if object:IsA("BasePart") then
			return true
		end
	end
	return false
end

local function onSelectionChanged()
	pluginToolbarButton.Enabled = doesSelectionContainAPart()
end
Selection.SelectionChanged:Connect(onSelectionChanged)
onSelectionChanged()
```

### Property: PluginToolbarButton.Icon

```json
{
  "type": "ContentId",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": true,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Appearance"
}
```

This property determines which [Content](/docs/reference/engine/datatypes/Content.md) should be shown for the
button's icon in the toolbar. When this property is not set, the button
will instead use the button's text given by
[PluginToolbar:CreateButton()](/docs/reference/engine/classes/PluginToolbar.md).

### Property: PluginToolbarButton.IconContent

```json
{
  "type": "Content",
  "access": "ReadOnly",
  "security": {
    "read": "PluginSecurity",
    "write": "PluginSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Appearance"
}
```

This property sets the image content displayed as the button's icon in the
plugin toolbar. When this property is not set, the button instead displays
the text label provided when calling [PluginToolbar:CreateButton()](/docs/reference/engine/classes/PluginToolbar.md).
Only asset URIs are supported for this property.

## Methods

### Method: PluginToolbarButton:SetActive

**Signature:** `PluginToolbarButton:SetActive(active: boolean): ()`

This method can be used to manually set the active state of the plugin
button.

When the [Enabled](/docs/reference/engine/classes/PluginToolbarButton.md) property is toggled
back on, the button will either revert to the last state set by this
method or default to inactive if this method hasn't been used previously.

*Security: PluginSecurity · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `active` | `boolean` |  | Whether to set the button to its active, pressed state (`true`) or its inactive state (`false`). |

**Returns:** `()`

## Events

### Event: PluginToolbarButton.Click

**Signature:** `PluginToolbarButton.Click()`

This event fires when the [PluginToolbarButton](/docs/reference/engine/classes/PluginToolbarButton.md) is pressed and
released by the user.

See also [SetActive()](/docs/reference/engine/classes/PluginToolbarButton.md) to manually
set the state of the button.

*Security: PluginSecurity*

**PluginToolbarButton.Click**

This code sample demonstrates creating a `PluginToolbar` and a
`PluginToolbarButton` on it, then connecting a function `onClick` to the
[PluginToolbarButton.Click](/docs/reference/engine/classes/PluginToolbarButton.md) event. When pressed, the button will print
"Hello, world" to the output.

```lua
assert(plugin, "This script must be run as a plugin")

local toolbar = plugin:CreateToolbar("Hello World Plugin Toolbar")
local pluginToolbarButton =
	toolbar:CreateButton("Print Hello World", "Click this button to print Hello World!", "rbxassetid://133293265")

local function onClick()
	print("Hello, world")
end

pluginToolbarButton.Click:Connect(onClick)
```

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