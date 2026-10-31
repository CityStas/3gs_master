---
name: BodyVelocity
last_updated: 2026-10-30T19:55:52Z
inherits:
  - BodyMover
  - Instance
  - Object
type: class
memory_category: Instances
tags:
  - Deprecated
summary: "Applies a force to maintain a constant velocity."
---

# Class: BodyVelocity

> Applies a force to maintain a constant velocity.

## Description

The `BodyVelocity` object applies a force on an assembly such that it will
maintain a constant velocity. The [Velocity](/docs/reference/engine/classes/BodyVelocity.md)
property, not to be confused with [BasePart.AssemblyLinearVelocity](/docs/reference/engine/classes/BasePart.md),
controls the goal velocity.

[BodyVelocity](/docs/reference/engine/classes/BodyVelocity.md) is the linear counterpart to [BodyAngularVelocity](/docs/reference/engine/classes/BodyAngularVelocity.md).
If you need the assembly to move toward a goal position, use
[BodyPosition](/docs/reference/engine/classes/BodyPosition.md) instead. If you need further control on a force applied
to an object, consider using a [BodyForce](/docs/reference/engine/classes/BodyForce.md) or [BodyThrust](/docs/reference/engine/classes/BodyThrust.md)
instead.

The strength of the force applied by this object is controlled by several
factors, namely the difference between the assembly's current velocity and the
goal velocity. This is multiplied by [P](/docs/reference/engine/classes/BodyVelocity.md) (power) to
either amplify or diminish it. The resulting force is then capped by
[MaxForce](/docs/reference/engine/classes/BodyVelocity.md).

## Properties

### Property: BodyVelocity.MaxForce

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
  "category": "Goals",
  "capabilities": [
    "Physics"
  ]
}
```

This property determines the limit on the amount of force that may be
applied on each axis in reaching the goal
[Velocity](/docs/reference/engine/classes/BodyVelocity.md). If an assembly isn't moving,
consider increasing this value and also check that it is not
[Anchored](/docs/reference/engine/classes/BasePart.md) or attached to any anchored assemblies.

### Property: BodyVelocity.P

```json
{
  "type": "float",
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
  "category": "Goals",
  "capabilities": [
    "Physics"
  ]
}
```

This property determines how much power is used while applying force in
order to reach the goal [Velocity](/docs/reference/engine/classes/BodyVelocity.md). The higher
this value, the more power will be used and the faster it will be used.
The force the [BodyVelocity](/docs/reference/engine/classes/BodyVelocity.md) exerts increases as the difference
between the assembly's current velocity and the goal velocity increases.
This property is multiplied to this force to either amplify or diminish
it.

### Property: BodyVelocity.Velocity

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
  "category": "Goals",
  "capabilities": [
    "Physics"
  ]
}
```

This property (not to be confused with [BasePart.Velocity](/docs/reference/engine/classes/BasePart.md))
determines the target velocity towards which force will be exerted. It is
specified relative to the world, not the assembly.

### Property: BodyVelocity.maxForce

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
    "can_save": false
  },
  "deprecated": true,
  "thread_safety": "ReadSafe",
  "category": "Goals",
  "capabilities": [
    "Physics"
  ]
}
```

> **Deprecated:** This property is a deprecated variant of [BodyVelocity.MaxForce](/docs/reference/engine/classes/BodyVelocity.md) which should be used instead.

### Property: BodyVelocity.velocity

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
    "can_save": false
  },
  "deprecated": true,
  "thread_safety": "ReadSafe",
  "category": "Goals",
  "capabilities": [
    "Physics"
  ]
}
```

> **Deprecated:** This property is a deprecated variant of [BodyVelocity.Velocity](/docs/reference/engine/classes/BodyVelocity.md) which should be used instead.

## Methods

### Method: BodyVelocity:GetLastForce

**Signature:** `BodyVelocity:GetLastForce(): Vector3`

This method is not implemented and it will always return the `0` vector.
You are advised to use [AlignPosition](/docs/reference/engine/classes/AlignPosition.md) instead.

*Security: None · Thread Safety: Unsafe · Capabilities: Physics*

**Returns:** `Vector3`

### Method: BodyVelocity:lastForce

**Signature:** `BodyVelocity:lastForce(): Vector3`

Returns the last force in the object.

*Security: None · Thread Safety: Unsafe · Capabilities: Physics*

**Returns:** `Vector3`

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