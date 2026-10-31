---
name: Selection
last_updated: 2026-10-30T19:55:53Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
tags:
  - NotCreatable
  - Service
summary: "The Selection service controls the Instances that are selected in Roblox Studio."
---

# Class: Selection

> The Selection service controls the [Instances](/docs/reference/engine/classes/Instance.md) that are
> selected in Roblox Studio.

## Description

The Selection service controls the [Instances](/docs/reference/engine/classes/Instance.md) that are
selected in Roblox Studio.

This service is particularly useful when developing [Plugins](/docs/reference/engine/classes/Plugin.md), as
it allows the developer to access and manipulate the current selection.

Currently selected [Instances](/docs/reference/engine/classes/Instance.md) can be obtained and set using
the [Selection:Get()](/docs/reference/engine/classes/Selection.md) and [Selection:Set()](/docs/reference/engine/classes/Selection.md) functions. The
[Selection.SelectionChanged](/docs/reference/engine/classes/Selection.md) event fires whenever the current selection
changes.

For more information on using [Selection](/docs/reference/engine/classes/Selection.md) and [Plugins](/docs/reference/engine/classes/Plugin.md),
see [Plugin](/docs/reference/engine/classes/Plugin.md).

Selection is also often used in the command bar, to set hidden properties or
run functions for selected [Instances](/docs/reference/engine/classes/Instance.md).

Note this class only applies to Roblox Studio and has no applicability to
games.

## Code Samples

**Selection**

The following code sample, when used in a plugin or the command bar, will
rotate currently selected `BasePart`s.

```lua
local Selection = game:GetService("Selection")

for _, object in pairs(Selection:Get()) do
	if object:IsA("BasePart") then
		object.CFrame = object.CFrame * CFrame.Angles(0, math.pi / 2, 0)
	end
end
```

## Properties

### Property: Selection.SelectionThickness

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
  "category": "Appearance",
  "capabilities": [
    "Basic"
  ]
}
```

The thickness of the selection highlight outline drawn around selected
[Instances](/docs/reference/engine/classes/Instance.md) in Roblox Studio's viewport.

This read-only property returns the current outline thickness as a float.
The default value is `0.02`. The value is controlled by Roblox Studio and
cannot be changed through the scripting API.

This property can be read in [Plugins](/docs/reference/engine/classes/Plugin.md) to query the current
selection visualization setting, such as when drawing custom overlays that
need to match the built-in selection appearance.

## Methods

### Method: Selection:Add

**Signature:** `Selection:Add(instancesToAdd: Instances): ()`

Adds the [Instances](/docs/reference/engine/classes/Instance.md) in the given array to the current
selection. [Instances](/docs/reference/engine/classes/Instance.md) that are already selected remain
selected.

Calling this function fires the [Selection.SelectionChanged](/docs/reference/engine/classes/Selection.md) event
if any new [Instances](/docs/reference/engine/classes/Instance.md) are added to the selection.

Note this function can only be used in [Plugins](/docs/reference/engine/classes/Plugin.md) or the
command bar. For setting the selection to an entirely new set of
instances, see [Selection:Set()](/docs/reference/engine/classes/Selection.md). For removing instances from the
current selection, see [Selection:Remove()](/docs/reference/engine/classes/Selection.md).

*Security: PluginSecurity · Thread Safety: Unsafe · Capabilities: Basic*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `instancesToAdd` | `Instances` |  | An array of [Instances](/docs/reference/engine/classes/Instance.md) to add to the current selection. |

**Returns:** `()`

### Method: Selection:Get

**Signature:** `Selection:Get(): Instances`

Returns an array of currently selected [Instances](/docs/reference/engine/classes/Instance.md) in
Roblox Studio.

If no [Instances](/docs/reference/engine/classes/Instance.md) are selected, the array returned will be
empty. This function can be used in conjunction with the
[Selection.SelectionChanged](/docs/reference/engine/classes/Selection.md) event to get the selection whenever it
changes.

Note, this function can only be used in [Plugins](/docs/reference/engine/classes/Plugin.md) or the
command line.

For changing the current selection, please see [Selection:Set()](/docs/reference/engine/classes/Selection.md).

*Security: PluginSecurity · Thread Safety: Unsafe · Capabilities: Basic*

**Returns:** `Instances` — An array of currently selected [Instances](/docs/reference/engine/classes/Instance.md).

**Selection**

The following code sample, when used in a plugin or the command bar, will
rotate currently selected `BasePart`s.

```lua
local Selection = game:GetService("Selection")

for _, object in pairs(Selection:Get()) do
	if object:IsA("BasePart") then
		object.CFrame = object.CFrame * CFrame.Angles(0, math.pi / 2, 0)
	end
end
```

**Selection.SelectionChanged**

This example prints the number of selected items whenever SelectionChanged is
fired:

```lua
local selection = game:GetService("Selection")

selection.SelectionChanged:Connect(function()
	print("Selection contains " .. #selection:Get() .. " items.")
end)
```

### Method: Selection:Remove

**Signature:** `Selection:Remove(instancesToRemove: Instances): ()`

Removes the [Instances](/docs/reference/engine/classes/Instance.md) in the given array from the current
selection. [Instances](/docs/reference/engine/classes/Instance.md) that are not currently selected are
ignored.

Calling this function fires the [Selection.SelectionChanged](/docs/reference/engine/classes/Selection.md) event
if any [Instances](/docs/reference/engine/classes/Instance.md) are removed from the selection.

Note this function can only be used in [Plugins](/docs/reference/engine/classes/Plugin.md) or the
command bar. For adding instances to the current selection, see
[Selection:Add()](/docs/reference/engine/classes/Selection.md). For replacing the selection entirely, see
[Selection:Set()](/docs/reference/engine/classes/Selection.md).

*Security: PluginSecurity · Thread Safety: Unsafe · Capabilities: Basic*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `instancesToRemove` | `Instances` |  | An array of [Instances](/docs/reference/engine/classes/Instance.md) to remove from the current selection. |

**Returns:** `()`

### Method: Selection:Set

**Signature:** `Selection:Set(selection: Instances): ()`

Sets the currently selected objects in Roblox Studio to
[Instances](/docs/reference/engine/classes/Instance.md) in the given array.

Calling this function will cause the [Selection.SelectionChanged](/docs/reference/engine/classes/Selection.md)
event to fire, unless the new selection set is identical to the previous
selection.

Note this function overwrites the existing selection. However, using
[Selection:Get()](/docs/reference/engine/classes/Selection.md) an [Instance](/docs/reference/engine/classes/Instance.md) can be added to the existing
selection like so:

*Security: PluginSecurity · Thread Safety: Unsafe · Capabilities: Basic*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `selection` | `Instances` |  | An array of [Instances](/docs/reference/engine/classes/Instance.md) to set the current selection to. |

**Returns:** `()`

**Selection Set**

This code sample will select every `BasePart` in the workspace that is Bright
red.

```lua
local Selection = game:GetService("Selection")

local newSelection = {}
for _, object in pairs(workspace:GetDescendants()) do
	if object:IsA("BasePart") and object.BrickColor == BrickColor.new("Bright red") then
		table.insert(newSelection, object)
	end
end

Selection:Set(newSelection)
```

**Set**

Demonstrates [Selection:Set()](/docs/reference/engine/classes/Selection.md).

```lua
local selected = Selection:Get()
table.insert(selected, object)
Selection:Set(selected)
```

## Events

### Event: Selection.SelectionChanged

**Signature:** `Selection.SelectionChanged()`

Fires when the [Instances](/docs/reference/engine/classes/Instance.md) selected in Roblox Studio
changes.

Note this event does not give the new selection. Developers will need to
use the [Selection:Get()](/docs/reference/engine/classes/Selection.md) function to obtain the current selection.

Although this event can be used outside of plugins and the command bar, it
only applies to the selection in Roblox Studio and therefore has no
functionality outside of Studio.

To change the selection use the [Selection:Set()](/docs/reference/engine/classes/Selection.md) function.

*Security: None · Capabilities: Basic*

**Selection.SelectionChanged**

This example prints the number of selected items whenever SelectionChanged is
fired:

```lua
local selection = game:GetService("Selection")

selection.SelectionChanged:Connect(function()
	print("Selection contains " .. #selection:Get() .. " items.")
end)
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