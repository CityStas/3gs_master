---
name: RayValue
last_updated: 2026-10-30T19:55:53Z
inherits:
  - ValueBase
  - Instance
  - Object
type: class
memory_category: Instances
summary: "A container object for a single Ray."
---

# Class: RayValue

> A container object for a single Ray.

## Description

A RayValue is an object whose purpose is to store a single Ray. Similar to
CFrameValue, a RayValue's stored ray cannot be viewed or edited within the
Properties window within studio. Instead, use the Command bar to get and set
the value of these objects. For example, you can use a line like the one below
to create a new RayValue named "Value" within the [Workspace](/docs/reference/engine/classes/Workspace.md). It
creates a ray at (0, 50, 0) and it faces in the positive-X direction.

`Instance.new("RayValue").Value = Ray.new(Vector3.new(0, 50, 0), Vector3.new(10, 0, 0))`

Since there is no trivial way to edit rays within Studio, sometimes it is
better to use a CFrameValue instead (which can be changed through a part or
the camera). You can reconstruct a ray from a CFrame using
`Ray.new(cf.p, cf.lookVector * dist)`, where `cf` is a given CFrame and `dist`
is the length of the Ray you want to construct.

Like all "-Value" objects, this single value is stored in the Value property.
The Changed event for this (and other objects like it) will fire with the new
value being stored in the object, instead of a string representing the
property being changed.

## Code Samples

**Rays, RayValue and Raycasting**

This code sample demonstrates constructing a Ray, storing the Ray within a
RayValue and Raycasting to find other parts between two parts named "PartA"
and "PartB".

```lua
local partA = workspace.PartA
local partB = workspace.PartB

local origin = partA.Position
local direction = partB.Position - partA.Position
local ray = Ray.new(origin, direction)

local rayValue = Instance.new("RayValue")
rayValue.Value = ray
rayValue.Name = "PartA-to-PartB Ray"
rayValue.Parent = workspace

-- Raycast to find any parts in between PartA and PartB
local part = workspace:FindPartOnRay(ray)
if part then
	print("Hit part: " .. part:GetFullName())
else
	-- This ought to never happen, as our ray starts at PartA
	-- and points towards PartB, so we should always hit PartB
	-- or some other part.
	print("No part hit!")
end
```

## Properties

### Property: RayValue.Value

```json
{
  "type": "Ray",
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

The stored Ray.

## Events

### Event: RayValue.Changed

**Signature:** `RayValue.Changed(value: Ray)`

This event fires whenever the [RayValue.Value](/docs/reference/engine/classes/RayValue.md) property is changed.
It will run with the new value being stored in the argument object,
instead of a string representing the property being changed.

This event, like other changed events, can be used to track when an
RayValue changes and to track the different values that it may change to.

Equivalent changed events exist for similar objects, such as
[NumberValue](/docs/reference/engine/classes/NumberValue.md) and [StringValue](/docs/reference/engine/classes/StringValue.md), depending on what object type
best suits the need.

*Security: None*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `value` | `Ray` | The value after the change. |

**How to Use RayValue.Changed**

The below example, assuming all referenced objects existed, would print the
RayValue's new value each time it changed. In the example below it would print
_"{0, 0, 0}, {0.577350199, 0.577350199, 0.577350199}"_.

```lua
local value = Instance.new("RayValue")
value.Parent = workspace

value.Changed:Connect(function(NewValue)
	print(NewValue)
end)

local start = Vector3.new(0, 0, 0)
local lookAt = Vector3.new(10, 10, 10)
local ray = Ray.new(start, (lookAt - start).Unit)
value.Value = ray
```

**Expected output:** "{0, 0, 0}, {0.577350199, 0.577350199, 0.577350199}"

### Event: RayValue.changed

**Signature:** `RayValue.changed(value: Ray)`

> **Deprecated:** This event is a deprecated variant of [RayValue.Changed](/docs/reference/engine/classes/RayValue.md) which should be used instead.

*Security: None*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `value` | `Ray` |  |

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