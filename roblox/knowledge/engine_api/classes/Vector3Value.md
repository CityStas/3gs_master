---
name: Vector3Value
last_updated: 2026-10-30T19:55:53Z
inherits:
  - ValueBase
  - Instance
  - Object
type: class
memory_category: Instances
summary: "A container object for a single Vector3 value."
---

# Class: Vector3Value

> A container object for a single Vector3 value.

## Description

A Vector3Value simply holds a Vector3 as a value. This value can be used for
scripts to communicate, for objects to move to a preset location, etc.

## Code Samples

**Teleporter Part**

This code sample causes a Part to teleport any players that touch it to a
specific position defined by a "TeleportPosition" Vector3Value.

```lua
-- Paste me in a Script inside a Part
local part = script.Parent

local teleportPosition = part.TeleportPosition

local function onTouch(otherPart)
	-- First, find the HumanoidRootPart. If we can't find it, exit.
	local hrp = otherPart.Parent:FindFirstChild("HumanoidRootPart")
	if not hrp then
		return
	end

	-- Now teleport by setting the CFrame to one created from
	-- the stored TeleportPosition
	hrp.CFrame = CFrame.new(teleportPosition.Value)
end

part.Touched:Connect(onTouch)
```

**Storing Vector2 inside Vector3Value**

This code sample demonstrates how it is possible to store a Vector2 within a
Vector3Value by converting a Vector2 into a Vector3 with a dummy Z value.
Similarly, you can load it by reconstructing the Vector2 from the X and Y
axes.

```lua
local vector3Value = Instance.new("Vector3Value")

-- Store a Vector2 in a Vector3
local vector2 = Vector2.new(42, 70)
vector3Value.Value = Vector3.new(vector2.X, vector2.Y, 0) -- The Z value is ignored

-- Load a Vector2 from a Vector3
vector2 = Vector2.new(vector3Value.Value.X, vector3Value.Value.Y)

print(vector2)
```

## Properties

### Property: Vector3Value.Value

```json
{
  "type": "Vector3",
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
  "simulationAccess": true
}
```

The stored [Vector3](/docs/reference/engine/datatypes/Vector3.md).

## Events

### Event: Vector3Value.Changed

**Signature:** `Vector3Value.Changed(value: Vector3)`

Fired whenever the [Vector3Value.Value](/docs/reference/engine/classes/Vector3Value.md) of the [Vector3Value](/docs/reference/engine/classes/Vector3Value.md)
is changed. It will run with the new value being stored in the argument
object, instead of a string representing the property being changed.

This event, like other changed events, can be used to track when an
Vector3Value changes and to track the different values that it may change
to.

For instance, this may be useful in games that rely on Vector3Values to
track positions in the game world.

Equivalent changed events exist for similar objects, such as
[NumberValue](/docs/reference/engine/classes/NumberValue.md) and [StringValue](/docs/reference/engine/classes/StringValue.md), depending on what object type
best suits the need.

*Security: None*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `value` | `Vector3` | The new value after the change. |

**How to Use Vector3Value.Changed**

The below example, assuming all referenced objects existed, would print the
Vector3Value's new value each time it changed. In the example below it would
print _"10,10,10"_.

```lua
local value = Instance.new("Vector3Value")
value.Parent = workspace

value.Changed:Connect(function(NewValue)
	print(NewValue)
end)

value.Value = Vector3.new(10, 10, 10)
```

**Expected output:** "10,10,10"

### Event: Vector3Value.changed

**Signature:** `Vector3Value.changed(value: Vector3)`

> **Deprecated:** This deprecated event is a variant of [Vector3Value.Changed](/docs/reference/engine/classes/Vector3Value.md) which should be used instead.

*Security: None*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `value` | `Vector3` |  |

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