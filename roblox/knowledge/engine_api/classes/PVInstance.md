---
name: PVInstance
last_updated: 2026-10-30T19:55:52Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
tags:
  - NotCreatable
  - NotBrowsable
summary: "Abstract class for all objects that have a physical location in the world."
---

# Class: PVInstance

> Abstract class for all objects that have a physical location in the world.

## Description

A [PVInstance](/docs/reference/engine/classes/PVInstance.md) is an abstract class that cannot be created. It is the
base for all objects that have a physical location in the world.

## Properties

### Property: PVInstance.Origin

```json
{
  "type": "CFrame",
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
  "category": "Transform"
}
```

Editor-only property, shown in the Studio Properties window as **Origin
Position** and **Origin Orientation** under **Transform**. Its value is
the world-space [CFrame](/docs/reference/engine/datatypes/CFrame.md) of the instance's pivot; reading it
returns the same [CFrame](/docs/reference/engine/datatypes/CFrame.md) as [PVInstance:GetPivot()](/docs/reference/engine/classes/PVInstance.md). It
has no stored value of its own and always reflects the current pivot.

Setting it from the Properties window moves the whole instance so its
pivot lands at the new [CFrame](/docs/reference/engine/datatypes/CFrame.md), much like
[PVInstance:PivotTo()](/docs/reference/engine/classes/PVInstance.md). Editing through the Properties window
temporarily disables [WeldConstraints](/docs/reference/engine/classes/WeldConstraint.md) to other
objects for the move; `PivotTo` does not modify joints.

Not available to scripts; use [PVInstance:GetPivot()](/docs/reference/engine/classes/PVInstance.md) and
[PVInstance:PivotTo()](/docs/reference/engine/classes/PVInstance.md) at runtime instead.

### Property: PVInstance.Pivot Offset

```json
{
  "type": "CFrame",
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
  "category": "Pivot"
}
```

Editor-only property, shown in the Studio Properties window as **Pivot
Position** and **Pivot Orientation** under **Pivot**. It is the
[CFrame](/docs/reference/engine/datatypes/CFrame.md) of the pivot relative to the instance's own frame.

Changing it from the Properties window moves the pivot relative to the
instance while leaving the instance in place, unlike `Origin`, which moves
the whole instance. For a [BasePart](/docs/reference/engine/classes/BasePart.md), the offset defaults to the
identity [CFrame](/docs/reference/engine/datatypes/CFrame.md), so the pivot coincides with the part's center.
For a [Model](/docs/reference/engine/classes/Model.md), this property appears only when the model has a
[PrimaryPart](/docs/reference/engine/classes/Model.md); it then reflects and edits that
part's [PivotOffset](/docs/reference/engine/classes/BasePart.md), and
[Model:GetPivot()](/docs/reference/engine/classes/Model.md) aliases the primary part's pivot.

Not available to scripts; scripts read and write the equivalent through
the concrete class, such as [BasePart.PivotOffset](/docs/reference/engine/classes/BasePart.md).

## Methods

### Method: PVInstance:GetPivot

**Signature:** `PVInstance:GetPivot(): CFrame`

This function gets the pivot of a [PVInstance](/docs/reference/engine/classes/PVInstance.md). This is often used
with [PVInstance:PivotTo()](/docs/reference/engine/classes/PVInstance.md) to move a model.

[Models](/docs/reference/engine/classes/Model.md) and [BaseParts](/docs/reference/engine/classes/BasePart.md) are both
[PVInstances](/docs/reference/engine/classes/PVInstance.md) ("Position Velocity Instances") and so both
have this function.

*Security: None · Thread Safety: Safe · Simulation Access: true*

**Returns:** `CFrame` — The world-space [CFrame](/docs/reference/engine/datatypes/CFrame.md) of the instance's pivot.

**Simple Character Teleportation**

This code sample is a simple teleport script that moves your character
10&nbsp;studs forwards in the direction you're currently facing when you press
the <kbd>F</kbd> key. It does so by getting the current pivot with
[PVInstance:GetPivot()](/docs/reference/engine/classes/PVInstance.md) and calling `PVInstance|PivotTo` to move the
character forwards.

```lua
-- This code should be placed in a LocalScript under StarterPlayerScripts
local Players = game:GetService("Players")
local ContextActionService = game:GetService("ContextActionService")

local player = Players.LocalPlayer

local function doTeleport(_actionName, inputState, _inputObject)
	local character = player.Character
	if character and character.Parent and inputState == Enum.UserInputState.Begin then
		-- Move the character 10 studs forwards in the direction they're facing
		local currentPivot = character:GetPivot()
		character:PivotTo(currentPivot * CFrame.new(0, 0, -10))
	end
end

ContextActionService:BindAction("Teleport", doTeleport, true, Enum.KeyCode.F)
```

### Method: PVInstance:PivotTo

**Signature:** `PVInstance:PivotTo(targetCFrame: CFrame): ()`

Transforms the [PVInstance](/docs/reference/engine/classes/PVInstance.md) along with all of its descendant
[PVInstances](/docs/reference/engine/classes/PVInstance.md) such that the pivot is now located at the
specified [CFrame](/docs/reference/engine/datatypes/CFrame.md). This is the primary function that should be
used to move [Models](/docs/reference/engine/classes/Model.md) via scripting.

[BaseParts](/docs/reference/engine/classes/BasePart.md) are moved in this way by having their
[CFrame](/docs/reference/engine/datatypes/CFrame.md) transformed by the necessary offset.
[Models](/docs/reference/engine/classes/Model.md) are moved in this way by having their
[Model.WorldPivot](/docs/reference/engine/classes/Model.md) transformed by the necessary offset.

Note that for efficiency purposes, [Object.Changed](/docs/reference/engine/classes/Object.md) events are not
fired for [Position](/docs/reference/engine/classes/BasePart.md) and
[Orientation](/docs/reference/engine/classes/BasePart.md) of [BaseParts](/docs/reference/engine/classes/BasePart.md)
moved in this way; they are only fired for [CFrame](/docs/reference/engine/datatypes/CFrame.md).

When calling [PivotTo](/docs/reference/engine/classes/PVInstance.md) on [Models](/docs/reference/engine/classes/Model.md),
the offsets of the descendant parts and models are cached, such that
subsequent calls to [PivotTo](/docs/reference/engine/classes/PVInstance.md) on the same model
do not accumulate floating point drift between the parts making up the
model.

[Models](/docs/reference/engine/classes/Model.md) and [BaseParts](/docs/reference/engine/classes/BasePart.md) are both
[PVInstances](/docs/reference/engine/classes/PVInstance.md) ("Position Velocity Instances") and so both
have this function.

*Security: None · Thread Safety: Unsafe · Simulation Access: true*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `targetCFrame` | `CFrame` |  | The [CFrame](/docs/reference/engine/datatypes/CFrame.md) that the [PVInstance](/docs/reference/engine/classes/PVInstance.md) pivot should equal after moving it. |

**Returns:** `()`

**Simple Character Teleportation**

This code sample is a simple teleport script that moves your character
10&nbsp;studs forwards in the direction you're currently facing when you press
the <kbd>F</kbd> key. It does so by getting the current pivot with
[PVInstance:GetPivot()](/docs/reference/engine/classes/PVInstance.md) and calling `PVInstance|PivotTo` to move the
character forwards.

```lua
-- This code should be placed in a LocalScript under StarterPlayerScripts
local Players = game:GetService("Players")
local ContextActionService = game:GetService("ContextActionService")

local player = Players.LocalPlayer

local function doTeleport(_actionName, inputState, _inputObject)
	local character = player.Character
	if character and character.Parent and inputState == Enum.UserInputState.Begin then
		-- Move the character 10 studs forwards in the direction they're facing
		local currentPivot = character:GetPivot()
		character:PivotTo(currentPivot * CFrame.new(0, 0, -10))
	end
end

ContextActionService:BindAction("Teleport", doTeleport, true, Enum.KeyCode.F)
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