---
name: LinearVelocity
last_updated: 2026-10-30T19:55:52Z
inherits:
  - Constraint
  - Instance
  - Object
type: class
memory_category: BaseParts
summary: "Applies force on an assembly to maintain a constant linear velocity."
---

# Class: LinearVelocity

> Applies force on an assembly to maintain a constant linear velocity.

## Description

The `LinearVelocity` constraint applies force on an assembly to maintain a
**constant** linear velocity. It can be set to apply force along a
[Vector3](/docs/reference/engine/datatypes/Vector3.md), line, or 2D&nbsp;plane. Alternatively:

- If you want to control the amount of force applied, use a
  [VectorForce](/docs/reference/engine/classes/VectorForce.md) constraint.
- If you only need **initial** linear velocity, set the
  [AssemblyLinearVelocity](/docs/reference/engine/classes/BasePart.md) property
  directly on the assembly.

When configuring this constraint, it may be helpful to study
[Roblox Units](/docs/en-us/physics/units.md) to understand how Roblox units
compare to metric units.

#### Relativity

Application of velocity can be controlled through the constraint's
[RelativeTo](/docs/reference/engine/classes/LinearVelocity.md) property. If set to
[World](/docs/reference/engine/enums/ActuatorRelativeTo.md), force will be applied in world coordinates,
independent of the parent or attachment orientations. If set to
[Attachment0](/docs/reference/engine/enums/ActuatorRelativeTo.md) or
[Attachment1](/docs/reference/engine/enums/ActuatorRelativeTo.md), force will be applied relative to
[Attachment0](/docs/reference/engine/classes/Constraint.md) or
[Attachment1](/docs/reference/engine/classes/Constraint.md) respectively.

## Properties

### Property: LinearVelocity.ForceLimitMode

```json
{
  "type": "ForceLimitMode",
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
  "category": "Limits",
  "capabilities": [
    "Physics"
  ],
  "simulationAccess": true
}
```

Determines how the constraint force will be limited. When set to
[Magnitude](/docs/reference/engine/enums/ForceLimitMode.md), the constraint force will have a
magnitude less than [MaxForce](/docs/reference/engine/classes/LinearVelocity.md). When set to
[PerAxis](/docs/reference/engine/enums/ForceLimitMode.md), the force along each axis will be less than
the corresponding value in
[MaxAxesForce](/docs/reference/engine/classes/LinearVelocity.md) when
[VelocityConstraintMode](/docs/reference/engine/classes/LinearVelocity.md) is
[Vector](/docs/reference/engine/enums/VelocityConstraintMode.md) or the corresponding value in
[MaxPlanarAxesForce](/docs/reference/engine/classes/LinearVelocity.md) when
[VelocityConstraintMode](/docs/reference/engine/classes/LinearVelocity.md) is
[Plane](/docs/reference/engine/enums/VelocityConstraintMode.md). Only used when
[ForceLimitsEnabled](/docs/reference/engine/classes/LinearVelocity.md) is `true`.

### Property: LinearVelocity.ForceLimitsEnabled

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
  "category": "Mode",
  "capabilities": [
    "Physics"
  ],
  "simulationAccess": true
}
```

Determines if the constraint force will be limited or if the physics
solver can apply an unlimited force to achieve the target velocity. When
enabled, the constraint force is limited based on
[ForceLimitMode](/docs/reference/engine/classes/LinearVelocity.md). When disabled, the
physics solver will always apply a force that is large enough to achieve
the target velocity.

### Property: LinearVelocity.LineDirection

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
  "category": "Line",
  "capabilities": [
    "Physics"
  ],
  "simulationAccess": true
}
```

The normalized [Vector3](/docs/reference/engine/datatypes/Vector3.md) direction for constraining the velocity
along a line, when
[VelocityConstraintMode](/docs/reference/engine/classes/LinearVelocity.md) is
set to [Line](/docs/reference/engine/enums/VelocityConstraintMode.md).

### Property: LinearVelocity.LineVelocity

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
  "category": "Line",
  "capabilities": [
    "Physics"
  ],
  "simulationAccess": true
}
```

Float value of the velocity when
[VelocityConstraintMode](/docs/reference/engine/classes/LinearVelocity.md) is
set to [Line](/docs/reference/engine/enums/VelocityConstraintMode.md).

### Property: LinearVelocity.MaxAxesForce

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
  "category": "Limits",
  "capabilities": [
    "Physics"
  ],
  "simulationAccess": true
}
```

Maximum force along each axis that the constraint can apply to achieve the
target velocity. Only used if
[ForceLimitsEnabled](/docs/reference/engine/classes/LinearVelocity.md) is `true`,
[ForceLimitMode](/docs/reference/engine/classes/LinearVelocity.md) is
[PerAxis](/docs/reference/engine/enums/ForceLimitMode.md), and
[VelocityConstraintMode](/docs/reference/engine/classes/LinearVelocity.md) is
[Vector](/docs/reference/engine/enums/VelocityConstraintMode.md). The axes used to apply the limit
correspond to the [RelativeTo](/docs/reference/engine/classes/LinearVelocity.md) property.

### Property: LinearVelocity.MaxForce

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
  "category": "Limits",
  "capabilities": [
    "Physics"
  ],
  "simulationAccess": true
}
```

Maximum magnitude of the force vector the constraint can apply. Only used
if [ForceLimitsEnabled](/docs/reference/engine/classes/LinearVelocity.md) is `true`
and [ForceLimitMode](/docs/reference/engine/classes/LinearVelocity.md) is
[Magnitude](/docs/reference/engine/enums/ForceLimitMode.md).

### Property: LinearVelocity.MaxPlanarAxesForce

```json
{
  "type": "Vector2",
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
  "category": "Limits",
  "capabilities": [
    "Physics"
  ],
  "simulationAccess": true
}
```

Maximum force along each axis that the constraint can apply to achieve the
plane velocity. Only used if
[ForceLimitsEnabled](/docs/reference/engine/classes/LinearVelocity.md) is `true`,
[ForceLimitMode](/docs/reference/engine/classes/LinearVelocity.md) is
[PerAxis](/docs/reference/engine/enums/ForceLimitMode.md), and
[VelocityConstraintMode](/docs/reference/engine/classes/LinearVelocity.md) is
[Plane](/docs/reference/engine/enums/VelocityConstraintMode.md). The axes used to apply the limit
correspond to the [RelativeTo](/docs/reference/engine/classes/LinearVelocity.md) property.

### Property: LinearVelocity.PlaneVelocity

```json
{
  "type": "Vector2",
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
  "category": "Plane",
  "capabilities": [
    "Physics"
  ],
  "simulationAccess": true
}
```

[Vector2](/docs/reference/engine/datatypes/Vector2.md) value of the velocity in each tangent direction of the
plane, when
[VelocityConstraintMode](/docs/reference/engine/classes/LinearVelocity.md) is
set to [Plane](/docs/reference/engine/enums/VelocityConstraintMode.md).

### Property: LinearVelocity.PrimaryTangentAxis

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
  "category": "Plane",
  "capabilities": [
    "Physics"
  ],
  "simulationAccess": true
}
```

The primary axis in the plane, when
[VelocityConstraintMode](/docs/reference/engine/classes/LinearVelocity.md) is
set to [Plane](/docs/reference/engine/enums/VelocityConstraintMode.md). Value depends on the value of
[RelativeTo](/docs/reference/engine/classes/LinearVelocity.md) as follows:

- If [RelativeTo](/docs/reference/engine/classes/LinearVelocity.md) is set to
  [Attachment0](/docs/reference/engine/enums/ActuatorRelativeTo.md), this axis is the
  [Axis](/docs/reference/engine/classes/Attachment.md) of
  [Attachment0](/docs/reference/engine/classes/Constraint.md).
- If [RelativeTo](/docs/reference/engine/classes/LinearVelocity.md) is set to
  [Attachment1](/docs/reference/engine/enums/ActuatorRelativeTo.md), this axis is the
  [Axis](/docs/reference/engine/classes/Attachment.md) of
  [Attachment1](/docs/reference/engine/classes/Constraint.md).
- If [RelativeTo](/docs/reference/engine/classes/LinearVelocity.md) is set to
  [World](/docs/reference/engine/enums/ActuatorRelativeTo.md), this value must be specified in the
  world space.

### Property: LinearVelocity.ReactionForceEnabled

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
  "category": "Mode",
  "capabilities": [
    "Physics"
  ],
  "simulationAccess": true
}
```

Determines whether the constraint applies an equal and opposite reaction
force to the assembly of [Attachment1](/docs/reference/engine/classes/Constraint.md).
Defaults to `true`. This reaction force is relevant when
[RelativeTo](/docs/reference/engine/classes/LinearVelocity.md) is
[ActuatorRelativeTo.Attachment1](/docs/reference/engine/enums/ActuatorRelativeTo.md) — the mode in which the constraint
drives the `Attachment0` assembly's velocity relative to the `Attachment1`
assembly. Because `RelativeTo` defaults to
[ActuatorRelativeTo.World](/docs/reference/engine/enums/ActuatorRelativeTo.md), this property is typically only
meaningful once `RelativeTo` is set to `Attachment1`.

When enabled in that mode, the constraint applies the reaction force to
the `Attachment1` assembly, coupling the two assemblies. When disabled,
the constraint applies force only to the `Attachment0` assembly; the
`Attachment1` assembly receives no reaction force, though its pose and
velocity are still read as the reference frame for the target velocity.

### Property: LinearVelocity.RelativeTo

```json
{
  "type": "ActuatorRelativeTo",
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
  "category": "Mode",
  "capabilities": [
    "Physics"
  ],
  "simulationAccess": true
}
```

Sets the [ActuatorRelativeTo](/docs/reference/engine/enums/ActuatorRelativeTo.md) property for the constraint.

### Property: LinearVelocity.SecondaryTangentAxis

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
  "category": "Plane",
  "capabilities": [
    "Physics"
  ],
  "simulationAccess": true
}
```

The secondary axis in the plane, when
[VelocityConstraintMode](/docs/reference/engine/classes/LinearVelocity.md) is
set to [Plane](/docs/reference/engine/enums/VelocityConstraintMode.md). Value depends on the value of
[RelativeTo](/docs/reference/engine/classes/LinearVelocity.md) as follows:

- If [RelativeTo](/docs/reference/engine/classes/LinearVelocity.md) is set to
  [Attachment0](/docs/reference/engine/enums/ActuatorRelativeTo.md), this axis is the
  [SecondaryAxis](/docs/reference/engine/classes/Attachment.md) of
  [Attachment0](/docs/reference/engine/classes/Constraint.md).
- If [RelativeTo](/docs/reference/engine/classes/LinearVelocity.md) is set to
  [Attachment1](/docs/reference/engine/enums/ActuatorRelativeTo.md), this axis is the
  [SecondaryAxis](/docs/reference/engine/classes/Attachment.md) of
  [Attachment1](/docs/reference/engine/classes/Constraint.md).
- If [RelativeTo](/docs/reference/engine/classes/LinearVelocity.md) is set to
  [World](/docs/reference/engine/enums/ActuatorRelativeTo.md), this value must be specified in the
  world space.

### Property: LinearVelocity.VectorVelocity

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
  "category": "Vector",
  "capabilities": [
    "Physics"
  ],
  "simulationAccess": true
}
```

[Vector3](/docs/reference/engine/datatypes/Vector3.md) velocity value when
[VelocityConstraintMode](/docs/reference/engine/classes/LinearVelocity.md) is
set to [Vector](/docs/reference/engine/enums/VelocityConstraintMode.md).

### Property: LinearVelocity.VelocityConstraintMode

```json
{
  "type": "VelocityConstraintMode",
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
  "category": "Mode",
  "capabilities": [
    "Physics"
  ],
  "simulationAccess": true
}
```

The mode of the constraint: [Line](/docs/reference/engine/enums/VelocityConstraintMode.md),
[Plane](/docs/reference/engine/enums/VelocityConstraintMode.md), or
[Vector](/docs/reference/engine/enums/VelocityConstraintMode.md). Default is
[Vector](/docs/reference/engine/enums/VelocityConstraintMode.md).

## Inherited Members

### From [Constraint](/docs/reference/engine/classes/Constraint.md)

- **Property `Active`** (`boolean`): Indicates if the constraint is currently active in the world.
- **Property `Attachment0`** (`Attachment`): The Attachment that is connected to
- **Property `Attachment1`** (`Attachment`): The Attachment that is connected to
- **Property `Color`** (`BrickColor`): The color of the constraint.
- **Property `Enabled`** (`boolean`): Toggles whether or not the constraint is enabled.
- **Property `Visible`** (`boolean`): Toggles the constraint's visibility.
- **Method `GetDebugAppliedForce(bodyId: int): Vector3`**:  *(deprecated)*
- **Method `GetDebugAppliedTorque(bodyId: int): Vector3`**:  *(deprecated)*

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