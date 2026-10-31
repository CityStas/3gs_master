---
name: HingeConstraint
last_updated: 2026-10-30T19:55:52Z
inherits:
  - Constraint
  - Instance
  - Object
type: class
memory_category: BaseParts
summary: "Constrains its attachments to rotate about a single axis."
---

# Class: HingeConstraint

> Constrains its attachments to rotate about a single axis.

## Description

A **HingeConstraint** allows two [Attachments](/docs/reference/engine/classes/Attachment.md) to rotate
about one axis, constraining the two [Attachments](/docs/reference/engine/classes/Attachment.md) so that
they both occupy the same position and that their **X** axes point in the same
direction.

Note that if this constraint attaches one part (**A**) to another part (**B**)
that is anchored or connected to an anchored part (**Z**), part **A** will not
be locally simulated when interacting with a player.

When configuring this constraint, it may be helpful to study
[Roblox Units](/docs/en-us/physics/units.md) to understand how Roblox units
compare to metric units.

#### Angular Power

Hinges can be configured to actuate rotation. If a hinge's
[ActuatorType](/docs/reference/engine/classes/HingeConstraint.md) is set to
[Motor](/docs/reference/engine/enums/ActuatorType.md), it attempts to rotate the attachments with the goal
of reaching its [AngularVelocity](/docs/reference/engine/classes/HingeConstraint.md). You
can further control this rotation through both
[MotorMaxAcceleration](/docs/reference/engine/classes/HingeConstraint.md) and
[MotorMaxTorque](/docs/reference/engine/classes/HingeConstraint.md). If a hinge's
[ActuatorType](/docs/reference/engine/classes/HingeConstraint.md) is set to
[Servo](/docs/reference/engine/enums/ActuatorType.md), it attempts to rotate to an angle specified by
[TargetAngle](/docs/reference/engine/classes/HingeConstraint.md). This rotation is controlled
by both [AngularSpeed](/docs/reference/engine/classes/HingeConstraint.md) and
[ServoMaxTorque](/docs/reference/engine/classes/HingeConstraint.md).

#### Limits

You can set limits to restrict the rotation of a hinge, useful for mechanisms
like doors which should only swing open or closed within a set range. Enabling
the [LimitsEnabled](/docs/reference/engine/classes/HingeConstraint.md) property exposes the
[LowerAngle](/docs/reference/engine/classes/HingeConstraint.md) and
[UpperAngle](/docs/reference/engine/classes/HingeConstraint.md) limits, as well as
[Restitution](/docs/reference/engine/classes/HingeConstraint.md) which defines the elasticity
of the attachments when they reach either limit.

## Properties

### Property: HingeConstraint.ActuatorType

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
  "category": "Hinge",
  "capabilities": [
    "Physics"
  ],
  "simulationAccess": true
}
```

Sets whether the rotation of the [HingeConstraint](/docs/reference/engine/classes/HingeConstraint.md) is actuated and,
if so, what kind of actuation.

- If [ActuatorType](/docs/reference/engine/classes/HingeConstraint.md) is set to
  [Motor](/docs/reference/engine/enums/ActuatorType.md), the hinge will attempt to rotate the
  attachments with the goal of reaching
  [AngularVelocity](/docs/reference/engine/classes/HingeConstraint.md). This rotation
  is limited by both
  [MotorMaxAcceleration](/docs/reference/engine/classes/HingeConstraint.md) and
  [MotorMaxTorque](/docs/reference/engine/classes/HingeConstraint.md).
- If [ActuatorType](/docs/reference/engine/classes/HingeConstraint.md) is set to
  [Servo](/docs/reference/engine/enums/ActuatorType.md), the hinge will attempt to rotate to an angle
  specified by [TargetAngle](/docs/reference/engine/classes/HingeConstraint.md). This
  rotation is limited by both
  [AngularSpeed](/docs/reference/engine/classes/HingeConstraint.md) and
  [ServoMaxTorque](/docs/reference/engine/classes/HingeConstraint.md).

Note that both actuated and free spinning rotation can be limited by
setting [LimitsEnabled](/docs/reference/engine/classes/HingeConstraint.md) to true.

### Property: HingeConstraint.AngularResponsiveness

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

This property specifies the sharpness of the servo motor in reaching the
[TargetAngle](/docs/reference/engine/classes/HingeConstraint.md), when
[ActuatorType](/docs/reference/engine/classes/HingeConstraint.md) is set to
[Servo](/docs/reference/engine/enums/ActuatorType.md). Larger values correspond to a faster response
and smaller values results in more damping and a slower response.

### Property: HingeConstraint.AngularSpeed

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

The desired angular speed a [HingeConstraint](/docs/reference/engine/classes/HingeConstraint.md) with
[ActuatorType](/docs/reference/engine/classes/HingeConstraint.md) set to
[Servo](/docs/reference/engine/enums/ActuatorType.md) will attempt to maintain while rotating towards
its [TargetAngle](/docs/reference/engine/classes/HingeConstraint.md). Measured in
radians/second.

### Property: HingeConstraint.AngularVelocity

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

The angular velocity a [HingeConstraint](/docs/reference/engine/classes/HingeConstraint.md) with
[ActuatorType](/docs/reference/engine/classes/HingeConstraint.md) set to
[Motor](/docs/reference/engine/enums/ActuatorType.md) will attempt to achieve. Measured in
radians/second.

### Property: HingeConstraint.CurrentAngle

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

The current angle of the [HingeConstraint](/docs/reference/engine/classes/HingeConstraint.md). This angle is calculated
by measuring the angle separation of the **Y** axes of the
[Attachments](/docs/reference/engine/classes/Attachment.md).

### Property: HingeConstraint.LimitsEnabled

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
  "category": "Hinge",
  "capabilities": [
    "Physics"
  ],
  "simulationAccess": true
}
```

Sets whether the [HingeConstraint](/docs/reference/engine/classes/HingeConstraint.md) will limit the range of rotation.
If enabled, the constraint will only allow the
[CurrentAngle](/docs/reference/engine/classes/HingeConstraint.md) to be between
[LowerAngle](/docs/reference/engine/classes/HingeConstraint.md) and
[UpperAngle](/docs/reference/engine/classes/HingeConstraint.md). If the [Attachment](/docs/reference/engine/classes/Attachment.md)
reach the end of the limited range of rotation then they will stop
rotating. If [Restitution](/docs/reference/engine/classes/HingeConstraint.md) is greater
than 0 then the attachments will bounce when they hit the ends of the
limited range.

### Property: HingeConstraint.LowerAngle

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

The minimum rotation angle the [HingeConstraint](/docs/reference/engine/classes/HingeConstraint.md) will allow if
[LimitsEnabled](/docs/reference/engine/classes/HingeConstraint.md) is true. Measured in
degrees.

### Property: HingeConstraint.MotorMaxAcceleration

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

The maximum angular acceleration a [HingeConstraint](/docs/reference/engine/classes/HingeConstraint.md) with
[ActuatorType](/docs/reference/engine/classes/HingeConstraint.md) set to
[Motor](/docs/reference/engine/enums/ActuatorType.md) can apply to achieve its
[AngularVelocity](/docs/reference/engine/classes/HingeConstraint.md). Measured in
radians/second&sup2;.

### Property: HingeConstraint.MotorMaxTorque

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

The maximum torque a [HingeConstraint](/docs/reference/engine/classes/HingeConstraint.md) with
[ActuatorType](/docs/reference/engine/classes/HingeConstraint.md) set to
[Motor](/docs/reference/engine/enums/ActuatorType.md) can apply when trying to reach its desired
[AngularVelocity](/docs/reference/engine/classes/HingeConstraint.md).

### Property: HingeConstraint.Radius

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

The visualized radius of the [HingeConstraint](/docs/reference/engine/classes/HingeConstraint.md).

### Property: HingeConstraint.Restitution

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

How elastic [Attachment](/docs/reference/engine/classes/Attachment.md) connected by a [HingeConstraint](/docs/reference/engine/classes/HingeConstraint.md) will
be when they reach the end of the range when
[LimitsEnabled](/docs/reference/engine/classes/HingeConstraint.md) is true. Constrained
between 0 and 1.

### Property: HingeConstraint.ServoMaxTorque

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

The maximum torque a [HingeConstraint](/docs/reference/engine/classes/HingeConstraint.md) with
[ActuatorType](/docs/reference/engine/classes/HingeConstraint.md) set to
[Servo](/docs/reference/engine/enums/ActuatorType.md) can apply when trying to reach its desired
[TargetAngle](/docs/reference/engine/classes/HingeConstraint.md).

### Property: HingeConstraint.TargetAngle

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

The target angle a [HingeConstraint](/docs/reference/engine/classes/HingeConstraint.md) will attempt to rotate to if
its [ActuatorType](/docs/reference/engine/classes/HingeConstraint.md) is set to
[Servo](/docs/reference/engine/enums/ActuatorType.md). Measured in degrees.

### Property: HingeConstraint.UpperAngle

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

The maximum rotation angle the [HingeConstraint](/docs/reference/engine/classes/HingeConstraint.md) will allow if
[LimitsEnabled](/docs/reference/engine/classes/HingeConstraint.md) is true. Measured in
degrees.

### Property: HingeConstraint.SoftlockServoUponReachingTarget

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