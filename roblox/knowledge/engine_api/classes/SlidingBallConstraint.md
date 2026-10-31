---
name: SlidingBallConstraint
last_updated: 2026-10-30T19:55:53Z
inherits:
  - Constraint
  - Instance
  - Object
type: class
memory_category: BaseParts
tags:
  - NotCreatable
summary: "The base class for constraints that allow their attachments to slide along an axis."
---

# Class: SlidingBallConstraint

> The base class for constraints that allow their attachments to slide along an
> axis.

## Description

**SlidingBallConstraint** is the base class for constraints that allow their
attachments to slide along an axis, including [PrismaticConstraint](/docs/reference/engine/classes/PrismaticConstraint.md) and
[CylindricalConstraint](/docs/reference/engine/classes/CylindricalConstraint.md). The base class does not restrict rotation.
[PrismaticConstraint](/docs/reference/engine/classes/PrismaticConstraint.md) prevents rotation, while
[CylindricalConstraint](/docs/reference/engine/classes/CylindricalConstraint.md) allows rotation about an axis.

When configuring this constraint, it may be helpful to study
[Roblox Units](/docs/en-us/physics/units.md) to understand how Roblox units
compare to metric units.

#### Linear Power

If this constraint's [ActuatorType](/docs/reference/engine/classes/SlidingBallConstraint.md) is set to
[Motor](/docs/reference/engine/enums/ActuatorType.md), it attempts to translate the attachments with the
goal of reaching [Velocity](/docs/reference/engine/classes/SlidingBallConstraint.md). You can further
control this translation through both
[MotorMaxAcceleration](/docs/reference/engine/classes/SlidingBallConstraint.md) and
[MotorMaxForce](/docs/reference/engine/classes/SlidingBallConstraint.md).

If this constraint's [ActuatorType](/docs/reference/engine/classes/SlidingBallConstraint.md) is set to
[Servo](/docs/reference/engine/enums/ActuatorType.md), it attempts to translate the attachments to a set
separation specified by [TargetPosition](/docs/reference/engine/classes/SlidingBallConstraint.md). This
translation is controlled by [Speed](/docs/reference/engine/classes/SlidingBallConstraint.md),
[LinearResponsiveness](/docs/reference/engine/classes/SlidingBallConstraint.md), and
[ServoMaxForce](/docs/reference/engine/classes/SlidingBallConstraint.md).

#### Limits

You can set **limits** to restrict this constraint's sliding range. Enabling
the [LimitsEnabled](/docs/reference/engine/classes/SlidingBallConstraint.md) property exposes the
[LowerLimit](/docs/reference/engine/classes/SlidingBallConstraint.md) and
[UpperLimit](/docs/reference/engine/classes/SlidingBallConstraint.md) values, as well as
[Restitution](/docs/reference/engine/classes/SlidingBallConstraint.md) which defines the elasticity of the
attachments when they reach either limit.

## Properties

### Property: SlidingBallConstraint.ActuatorType

```json
{
  "type": "ActuatorType",
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
  "category": "Slider",
  "capabilities": [
    "Physics"
  ],
  "simulationAccess": true
}
```

Sets whether the translation of the [SlidingBallConstraint](/docs/reference/engine/classes/SlidingBallConstraint.md) is
actuated and, if so, what kind of actuation.

- If [ActuatorType](/docs/reference/engine/classes/SlidingBallConstraint.md) is set to
  [None](/docs/reference/engine/enums/ActuatorType.md), the joint can slide freely.

- If [ActuatorType](/docs/reference/engine/classes/SlidingBallConstraint.md) is set to
  [Motor](/docs/reference/engine/enums/ActuatorType.md), it attempts to translate the attachments with
  the goal of reaching [Velocity](/docs/reference/engine/classes/SlidingBallConstraint.md). You can
  further control this translation through both
  [MotorMaxAcceleration](/docs/reference/engine/classes/SlidingBallConstraint.md) and
  [MotorMaxForce](/docs/reference/engine/classes/SlidingBallConstraint.md).

- If this constraint's [ActuatorType](/docs/reference/engine/classes/SlidingBallConstraint.md) is set
  to [Servo](/docs/reference/engine/enums/ActuatorType.md), it attempts to translate the attachments
  to a set separation specified by
  [TargetPosition](/docs/reference/engine/classes/SlidingBallConstraint.md). This translation is
  controlled by [Speed](/docs/reference/engine/classes/SlidingBallConstraint.md),
  [LinearResponsiveness](/docs/reference/engine/classes/SlidingBallConstraint.md), and
  [ServoMaxForce](/docs/reference/engine/classes/SlidingBallConstraint.md).

### Property: SlidingBallConstraint.CurrentPosition

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
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Derived",
  "capabilities": [
    "Physics"
  ],
  "simulationAccess": true
}
```

The current offset between the constraint's
[Attachments](/docs/reference/engine/classes/Attachment.md).

### Property: SlidingBallConstraint.LimitsEnabled

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
  "category": "Slider",
  "capabilities": [
    "Physics"
  ],
  "simulationAccess": true
}
```

Sets whether the [SlidingBallConstraint](/docs/reference/engine/classes/SlidingBallConstraint.md) will limit the range of
translation. If true, this property exposes the
[LowerLimit](/docs/reference/engine/classes/SlidingBallConstraint.md) and
[UpperLimit](/docs/reference/engine/classes/SlidingBallConstraint.md) values, as well as
[Restitution](/docs/reference/engine/classes/SlidingBallConstraint.md) which defines the elasticity of
the attachments when they reach either limit.

### Property: SlidingBallConstraint.LinearResponsiveness

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
  "category": "Servo",
  "capabilities": [
    "Physics"
  ],
  "simulationAccess": true
}
```

Specifies the "sharpness" of the linear servo motor in reaching the
[TargetPosition](/docs/reference/engine/classes/SlidingBallConstraint.md) when the
derived classes' actuator type is set to [Servo](/docs/reference/engine/enums/ActuatorType.md). Larger
values correspond to faster a response and smaller values results in more
damping and a slower response.

### Property: SlidingBallConstraint.LowerLimit

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

The lower positional limit along the **X** axis of
[Attachment0](/docs/reference/engine/classes/Constraint.md) if
[LimitsEnabled](/docs/reference/engine/classes/SlidingBallConstraint.md) is true.

### Property: SlidingBallConstraint.MotorMaxAcceleration

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
  "category": "Motor",
  "capabilities": [
    "Physics"
  ],
  "simulationAccess": true
}
```

The constraint's maximum acceleration when
[ActuatorType](/docs/reference/engine/classes/SlidingBallConstraint.md) is set to
[Motor](/docs/reference/engine/enums/ActuatorType.md), as the constraint attempts to reach its desired
[Velocity](/docs/reference/engine/classes/SlidingBallConstraint.md).

### Property: SlidingBallConstraint.MotorMaxForce

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
  "category": "Motor",
  "capabilities": [
    "Physics"
  ],
  "simulationAccess": true
}
```

The constraint's maximum force when
[ActuatorType](/docs/reference/engine/classes/SlidingBallConstraint.md) is set to
[Motor](/docs/reference/engine/enums/ActuatorType.md), as the constraint attempts to reach its desired
[Velocity](/docs/reference/engine/classes/SlidingBallConstraint.md).

### Property: SlidingBallConstraint.Restitution

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

The elasticity of the constraint's [Attachments](/docs/reference/engine/classes/Attachment.md) when
they reach the end of the range specified by
[UpperLimit](/docs/reference/engine/classes/SlidingBallConstraint.md) and
[LowerLimit](/docs/reference/engine/classes/SlidingBallConstraint.md), assuming
[LimitsEnabled](/docs/reference/engine/classes/SlidingBallConstraint.md) is set to true.
The valid range is between 0&ndash;1.

### Property: SlidingBallConstraint.ServoMaxForce

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
  "category": "Servo",
  "capabilities": [
    "Physics"
  ],
  "simulationAccess": true
}
```

The constraint's maximum force when
[ActuatorType](/docs/reference/engine/classes/SlidingBallConstraint.md) is set to
[Servo](/docs/reference/engine/enums/ActuatorType.md), as the constraint attempts to reach its desired
[Speed](/docs/reference/engine/classes/SlidingBallConstraint.md).

### Property: SlidingBallConstraint.Size

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
  "category": "Appearance",
  "capabilities": [
    "Physics"
  ],
  "simulationAccess": true
}
```

The constraint's visualized size.

### Property: SlidingBallConstraint.Speed

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
  "category": "Servo",
  "capabilities": [
    "Physics"
  ],
  "simulationAccess": true
}
```

The constraint's desired speed when
[ActuatorType](/docs/reference/engine/classes/SlidingBallConstraint.md) is set to
[Servo](/docs/reference/engine/enums/ActuatorType.md), as the constraint translates towards its
[TargetPosition](/docs/reference/engine/classes/SlidingBallConstraint.md). Measured in
studs per second.

### Property: SlidingBallConstraint.TargetPosition

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
  "category": "Servo",
  "capabilities": [
    "Physics"
  ],
  "simulationAccess": true
}
```

The constraint's attempted target position when
[ActuatorType](/docs/reference/engine/classes/SlidingBallConstraint.md) is set to
[Servo](/docs/reference/engine/enums/ActuatorType.md) Measured in studs.

### Property: SlidingBallConstraint.UpperLimit

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

The upper positional limit along the **X** axis of
[Attachment0](/docs/reference/engine/classes/Constraint.md) if
[LimitsEnabled](/docs/reference/engine/classes/SlidingBallConstraint.md) is true.

### Property: SlidingBallConstraint.Velocity

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
  "category": "Motor",
  "capabilities": [
    "Physics"
  ],
  "simulationAccess": true
}
```

The constraint's attempted velocity when
[ActuatorType](/docs/reference/engine/classes/SlidingBallConstraint.md) is set to
[Motor](/docs/reference/engine/enums/ActuatorType.md). Measured in studs per second.

### Property: SlidingBallConstraint.SoftlockServoUponReachingTarget

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
  "deprecated": true,
  "thread_safety": "ReadSafe",
  "category": "Servo",
  "capabilities": [
    "Physics"
  ],
  "simulationAccess": true
}
```

> **Deprecated:** This property should not be used in new work.

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