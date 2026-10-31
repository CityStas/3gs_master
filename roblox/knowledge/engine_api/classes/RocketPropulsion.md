---
name: RocketPropulsion
last_updated: 2026-10-30T19:55:53Z
inherits:
  - BodyMover
  - Instance
  - Object
type: class
memory_category: Instances
tags:
  - Deprecated
summary: "Applies a force so that an assembly follows and faces a target part."
---

# Class: RocketPropulsion

> Applies a force so that an assembly follows and faces a target part.

## Description

The `RocketPropulsion` object applies force on an assembly so that it both
**follows** and **faces** a target. It acts like a hybrid of
[BodyPosition](/docs/reference/engine/classes/BodyPosition.md) and [BodyGyro](/docs/reference/engine/classes/BodyGyro.md). Unlike other
[BodyMovers](/docs/reference/engine/classes/BodyMover.md), `RocketPropulsion` must be instructed to begin
applying or stopping force via [Fire()](/docs/reference/engine/classes/RocketPropulsion.md) or
[Abort()](/docs/reference/engine/classes/RocketPropulsion.md) respectively.

You can detect when the assembly reaches its target using the
[ReachedTarget](/docs/reference/engine/classes/RocketPropulsion.md) event which fires once
the assembly is within the [TargetRadius](/docs/reference/engine/classes/RocketPropulsion.md)
of the [Target](/docs/reference/engine/classes/RocketPropulsion.md) part.

## Properties

### Property: RocketPropulsion.CartoonFactor

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

This property determines the tendency of the assembly to face the
[Target](/docs/reference/engine/classes/RocketPropulsion.md). By default, this property is set
to `0.7`. If set to `0`, the assembly will make no effort to face the
target.

### Property: RocketPropulsion.MaxSpeed

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
  "category": "Thrust",
  "capabilities": [
    "Physics"
  ]
}
```

This property determines the upper limit of the velocity at which the
assembly will move toward the [Target](/docs/reference/engine/classes/RocketPropulsion.md).

### Property: RocketPropulsion.MaxThrust

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
  "category": "Thrust",
  "capabilities": [
    "Physics"
  ]
}
```

This property determines the upper limit of the thrust that may be exerted
to move the assembly. Assemblies that have high mass will require more
thrust in order to remain airborne and thus track the
[Target](/docs/reference/engine/classes/RocketPropulsion.md).

### Property: RocketPropulsion.MaxTorque

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
  "category": "Turn",
  "capabilities": [
    "Physics"
  ]
}
```

This property determines the upper limit on the amount of torque that may
be exerted in order to rotate the assembly towards the
[Target](/docs/reference/engine/classes/RocketPropulsion.md). It functions similarly to
[BodyGyro.MaxTorque](/docs/reference/engine/classes/BodyGyro.md).

### Property: RocketPropulsion.Target

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
  "category": "Goals",
  "capabilities": [
    "Physics"
  ]
}
```

This property determines the object towards which the `RocketPropulsion`
will exert force/torque. If set to `nil`, the
[TargetOffset](/docs/reference/engine/classes/RocketPropulsion.md) will be used instead.

### Property: RocketPropulsion.TargetOffset

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

This property determines the world offset from the
[Target](/docs/reference/engine/classes/RocketPropulsion.md). It is especially useful when
[Target](/docs/reference/engine/classes/RocketPropulsion.md) is set to `nil`, since this
property then acts as the target position.

### Property: RocketPropulsion.TargetRadius

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

This property determines the maximum distance from the
[Target](/docs/reference/engine/classes/RocketPropulsion.md) at which the assembly must be in
order for [ReachedTarget](/docs/reference/engine/classes/RocketPropulsion.md) to be
fired. It does not affect the exerted forces in any way.

### Property: RocketPropulsion.ThrustD

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
  "category": "Thrust",
  "capabilities": [
    "Physics"
  ]
}
```

This property is used to dampen the velocity of the assembly in order to
prevent it from overshooting the [Target](/docs/reference/engine/classes/RocketPropulsion.md)
and causing a "rubber‑banding" effect. It behaves similarly to
[BodyPosition.D](/docs/reference/engine/classes/BodyPosition.md).

### Property: RocketPropulsion.ThrustP

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
  "category": "Thrust",
  "capabilities": [
    "Physics"
  ]
}
```

This property determines how much power is used while applying force in
order to reach the [Target](/docs/reference/engine/classes/RocketPropulsion.md) position. The
higher this value, the more power will be used and the faster it will be
used. This property works similarly to [BodyPosition.P](/docs/reference/engine/classes/BodyPosition.md).

### Property: RocketPropulsion.TurnD

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
  "category": "Turn",
  "capabilities": [
    "Physics"
  ]
}
```

This property specifies how much dampening will be applied to the torque
used to face the [Target](/docs/reference/engine/classes/RocketPropulsion.md). When the assembly
approaches the goal orientation, it needs to decelerate, otherwise it will
rotate past the goal and have to stop and re-accelerate back toward the
goal. This often creates an undesirable "rubber‑banding" effect, avoided
by applying dampening. The higher this value is set, the greater the
dampening curve becomes, or the slower the part will approach the goal
orientation.

### Property: RocketPropulsion.TurnP

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
  "category": "Turn",
  "capabilities": [
    "Physics"
  ]
}
```

This property determines how much power is used while applying torque in
order to face the [Target](/docs/reference/engine/classes/RocketPropulsion.md). The higher this
value, the more power will be used and the faster it will be used.

## Methods

### Method: RocketPropulsion:Abort

**Signature:** `RocketPropulsion:Abort(): ()`

Causes the assembly to stop moving toward its
[Target](/docs/reference/engine/classes/RocketPropulsion.md).

*Security: None · Thread Safety: Unsafe · Capabilities: Physics*

**Returns:** `()`

### Method: RocketPropulsion:Fire

**Signature:** `RocketPropulsion:Fire(): ()`

Causes the assembly to start moving toward its
[Target](/docs/reference/engine/classes/RocketPropulsion.md).

*Security: None · Thread Safety: Unsafe · Capabilities: Physics*

**Returns:** `()`

### Method: RocketPropulsion:fire

**Signature:** `RocketPropulsion:fire(): ()`

> **Deprecated:** This function is a deprecated variant of [RocketPropulsion:Fire()](/docs/reference/engine/classes/RocketPropulsion.md) which should be used instead.

*Security: None · Thread Safety: Unsafe · Capabilities: Physics*

**Returns:** `()`

## Events

### Event: RocketPropulsion.ReachedTarget

**Signature:** `RocketPropulsion.ReachedTarget()`

Fires when the assembly comes within
[TargetRadius](/docs/reference/engine/classes/RocketPropulsion.md) of the
[Target](/docs/reference/engine/classes/RocketPropulsion.md).

*Security: None · Capabilities: Physics*

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