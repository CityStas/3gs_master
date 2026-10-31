---
name: JointInstance
last_updated: 2026-10-30T19:55:52Z
inherits:
  - Instance
  - Object
type: class
memory_category: BaseParts
tags:
  - NotCreatable
summary: "The base class for joints."
---

# Class: JointInstance

> The base class for joints.

## Description

`JointInstance` is the base class for joints such as [Welds](/docs/reference/engine/classes/Weld.md) and
[Motors](/docs/reference/engine/classes/Motor.md).

[Weld](/docs/reference/engine/classes/Weld.md), [WeldConstraint](/docs/reference/engine/classes/WeldConstraint.md), [Motor](/docs/reference/engine/classes/Motor.md), and [Motor6D](/docs/reference/engine/classes/Motor6D.md) all
combine multiple parts into the same
[assembly](/docs/en-us/physics/assemblies.md). Every assembly has a root part
([BasePart:GetRootPart()](/docs/reference/engine/classes/BasePart.md)) and when
[C0](/docs/reference/engine/classes/JointInstance.md)/[C1](/docs/reference/engine/classes/JointInstance.md) of a
[JointInstance](/docs/reference/engine/classes/JointInstance.md) is modified, the root part will stay where it was.

Welds do not have any directionality. You can imagine rigid joints forming a
tree branching down from the root part. All the parts down the tree from root
will move, and their welded "children" in this tree will move with them.

## Properties

### Property: JointInstance.Active

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
  "category": "Behavior",
  "capabilities": [
    "Physics"
  ]
}
```

This property determines if the joint is currently active in the world.

If the [JointInstance](/docs/reference/engine/classes/JointInstance.md) is not in [Workspace](/docs/reference/engine/classes/Workspace.md) or
[JointsService](/docs/reference/engine/classes/JointsService.md), or one of its parts is not in [Workspace](/docs/reference/engine/classes/Workspace.md),
the joint will be inactive.

Rigid joints like [Weld](/docs/reference/engine/classes/Weld.md), [Snap](/docs/reference/engine/classes/Snap.md), [WeldConstraint](/docs/reference/engine/classes/WeldConstraint.md),
[Motor](/docs/reference/engine/classes/Motor.md), or [Motor6D](/docs/reference/engine/classes/Motor6D.md) may also be disabled due to conflicts
with other rigid joints, such as joints between the same two parts or
indirect cycles in the weld graph. Joints disabled this way may be
re-enabled later when another joint or part is added or removed.

### Property: JointInstance.C0

```json
{
  "type": "CFrame",
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
    "Physics"
  ]
}
```

`C0` is the position aspect of the orientation between two parts in a
weld. [Part0](/docs/reference/engine/classes/JointInstance.md) and
[Part1](/docs/reference/engine/classes/JointInstance.md) move accordingly to this value, which
denotes their respective positions.

When animating a [Motor6D](/docs/reference/engine/classes/Motor6D.md), it's recommended to tween its
[Transform](/docs/reference/engine/classes/Motor6D.md) property instead of `C0`.

### Property: JointInstance.C1

```json
{
  "type": "CFrame",
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
    "Physics"
  ]
}
```

This property is subtracted from the [C0](/docs/reference/engine/classes/JointInstance.md) property
to create an offset point for [Part1](/docs/reference/engine/classes/JointInstance.md).

When animating a [Motor6D](/docs/reference/engine/classes/Motor6D.md), it's recommended to tween its
[Transform](/docs/reference/engine/classes/Motor6D.md) property instead of `C1`.

### Property: JointInstance.Enabled

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
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Behavior",
  "capabilities": [
    "Physics"
  ]
}
```

This property sets whether the joint is active or not.

When this property is set to `true` and the joint's
[Part0](/docs/reference/engine/classes/JointInstance.md) and [Part1](/docs/reference/engine/classes/JointInstance.md)
properties are set, the joint will ensure that its two parts will be
connected and behave according to joint type.

See also [Active](/docs/reference/engine/classes/JointInstance.md) which determines if the joint
is currently active in the world.

### Property: JointInstance.Part0

```json
{
  "type": "BasePart",
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
    "Physics"
  ]
}
```

This property indicates the first [BasePart](/docs/reference/engine/classes/BasePart.md) that the joint
connects.

### Property: JointInstance.Part1

```json
{
  "type": "BasePart",
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
    "Physics"
  ]
}
```

This property indicates the second [BasePart](/docs/reference/engine/classes/BasePart.md) that the joint
connects.

### Property: JointInstance.part1 *(hidden)*

```json
{
  "type": "BasePart",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "deprecated": true,
  "thread_safety": "ReadSafe",
  "category": "Data",
  "capabilities": [
    "Physics"
  ]
}
```

> **Deprecated:** This deprecated property is a variant of [Part1](/docs/reference/engine/classes/JointInstance.md) which should be used instead.

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