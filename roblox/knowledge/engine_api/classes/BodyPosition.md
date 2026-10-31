---
name: BodyPosition
last_updated: 2026-10-30T19:55:52Z
inherits:
  - BodyMover
  - Instance
  - Object
type: class
memory_category: Instances
tags:
  - Deprecated
summary: "Applies a force to maintain a constant position."
---

# Class: BodyPosition

> Applies a force to maintain a constant position.

## Description

The `BodyPosition` object applies a force on an assembly such that it will
maintain a constant position in the world. The
[Position](/docs/reference/engine/classes/BodyPosition.md) property, not to be confused with
[BasePart.Position](/docs/reference/engine/classes/BasePart.md), controls the target world position. This is the
translational counterpart to a [BodyGyro](/docs/reference/engine/classes/BodyGyro.md).

If you need further control on a force applied to an object, consider using a
[BodyForce](/docs/reference/engine/classes/BodyForce.md) or [BodyThrust](/docs/reference/engine/classes/BodyThrust.md) instead.

The strength of the force applied by this object is controlled by several
factors, namely the distance to the goal position: the force is stronger when
farther away from the goal. This is amplified by [P](/docs/reference/engine/classes/BodyPosition.md)
(power). The present velocity will also dampen the force applied by this
object, and this is amplified by [D](/docs/reference/engine/classes/BodyPosition.md) (dampening). The
resulting force is then capped by [MaxForce](/docs/reference/engine/classes/BodyPosition.md). Note
the force applied on the assembly to achieve the goal position may vary on a
per-axis basis.

## Properties

### Property: BodyPosition.D

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

This property determines how much dampening will be applied to the force
used toward reaching the goal [Position](/docs/reference/engine/classes/BodyPosition.md). When
the assembly approaches the goal position it needs to decelerate,
otherwise it will move past the goal and have to stop and re-accelerate
back toward the goal. This is often creates an undesirable
"rubber‑banding" effect, avoided by applying dampening. The higher this
value is set, the greater the dampening curve becomes, or the slower the
assembly will approach the goal position.

### Property: BodyPosition.MaxForce

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
[Position](/docs/reference/engine/classes/BodyPosition.md). If an assembly isn't moving,
consider increasing this value and also check that it is not
[Anchored](/docs/reference/engine/classes/BasePart.md) or attached to any anchored assemblies.

### Property: BodyPosition.P

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
order to reach the goal [Position](/docs/reference/engine/classes/BodyPosition.md). The higher
this value, the more power will be used and the faster it will be used.
The force the [BodyPosition](/docs/reference/engine/classes/BodyPosition.md) exerts increases as the difference
between the assembly's current position and the goal position increases.
This property is multiplied to this force to either amplify or diminish
it.

### Property: BodyPosition.Position

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

This property determines the goal position towards which the
[BodyPosition](/docs/reference/engine/classes/BodyPosition.md) will apply force.

### Property: BodyPosition.maxForce

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

> **Deprecated:** This property is a deprecated variant of [BodyPosition.MaxForce](/docs/reference/engine/classes/BodyPosition.md) which should be used instead.

### Property: BodyPosition.position

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

> **Deprecated:** This is a deprecated variant of [BodyPosition.Position](/docs/reference/engine/classes/BodyPosition.md) which should be used instead.

## Methods

### Method: BodyPosition:GetLastForce

**Signature:** `BodyPosition:GetLastForce(): Vector3`

This function returns the last force in the object.

*Security: None · Thread Safety: Unsafe · Capabilities: Physics*

**Returns:** `Vector3`

### Method: BodyPosition:lastForce

**Signature:** `BodyPosition:lastForce(): Vector3`

> **Deprecated:** This property has been superseded by [BodyPosition:GetLastForce()](/docs/reference/engine/classes/BodyPosition.md) which should be used in new work instead,

The lastForce function returns the last force in the object.

*Security: None · Thread Safety: Unsafe · Capabilities: Physics*

**Returns:** `Vector3`

## Events

### Event: BodyPosition.ReachedTarget

**Signature:** `BodyPosition.ReachedTarget()`

Fired when the Parent of the BodyPosition reaches the desired
[BodyPosition.Position](/docs/reference/engine/classes/BodyPosition.md) (within .1 studs). Once this event fires it
will not fire again until [BodyPosition.Position](/docs/reference/engine/classes/BodyPosition.md) is updated.

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