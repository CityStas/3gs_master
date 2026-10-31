---
name: CylindricalConstraint
last_updated: 2026-10-30T19:55:52Z
inherits:
  - SlidingBallConstraint
  - Constraint
  - Instance
  - Object
type: class
memory_category: BaseParts
summary: "Constrains two attachments on two parts to have a relative linear and rotational motion."
---

# Class: CylindricalConstraint

> Constrains two attachments on two parts to have a relative linear and
> rotational motion.

## Description

A **CylindricalConstraint** allows its attachments to slide along one axis and
rotate about another axis. It can be thought of like a combination of a
[PrismaticConstraint](/docs/reference/engine/classes/PrismaticConstraint.md) and a [HingeConstraint](/docs/reference/engine/classes/HingeConstraint.md). The sliding axis is
determined by the **X** axis of the constraint's
[Attachment0](/docs/reference/engine/classes/Constraint.md). The rotation axis is centered at
the constraint's [Attachment1](/docs/reference/engine/classes/Constraint.md) and is angled off
of the sliding constraint by the constraint's
[InclinationAngle](/docs/reference/engine/classes/CylindricalConstraint.md).

This constraint, along with a [SpringConstraint](/docs/reference/engine/classes/SpringConstraint.md), is ideal for building
vehicle suspension.

Note that if this constraint attaches one part (**A**) to another part (**B**)
that is anchored or connected to an anchored part (**Z**), part **A** will not
be locally simulated when interacting with a player.

When configuring this constraint, it may be helpful to study
[Roblox Units](/docs/en-us/physics/units.md) to understand how Roblox units
compare to metric units.

#### Angular Power

If a cylindrical's
[AngularActuatorType](/docs/reference/engine/classes/CylindricalConstraint.md) is set
to [Motor](/docs/reference/engine/enums/ActuatorType.md), it attempts to rotate the attachments with the
goal of reaching its
[AngularVelocity](/docs/reference/engine/classes/CylindricalConstraint.md). You can further
control this rotation through both
[MotorMaxAngularAcceleration](/docs/reference/engine/classes/CylindricalConstraint.md)
and [MotorMaxTorque](/docs/reference/engine/classes/CylindricalConstraint.md). If a
cylindrical's
[AngularActuatorType](/docs/reference/engine/classes/CylindricalConstraint.md) is set
to [Servo](/docs/reference/engine/enums/ActuatorType.md), it attempts to rotate to an angle specified by
[TargetAngle](/docs/reference/engine/classes/CylindricalConstraint.md). This rotation is
controlled by [AngularSpeed](/docs/reference/engine/classes/CylindricalConstraint.md),
[AngularResponsiveness](/docs/reference/engine/classes/CylindricalConstraint.md), and
[ServoMaxTorque](/docs/reference/engine/classes/CylindricalConstraint.md).

#### Linear Power

If a cylindrical's [ActuatorType](/docs/reference/engine/classes/CylindricalConstraint.md) is set to
[Motor](/docs/reference/engine/enums/ActuatorType.md), it attempts to translate the attachments with the
goal of reaching [Velocity](/docs/reference/engine/classes/CylindricalConstraint.md). You can further
control this translation through both
[MotorMaxAcceleration](/docs/reference/engine/classes/CylindricalConstraint.md) and
[MotorMaxForce](/docs/reference/engine/classes/CylindricalConstraint.md). If a cylindrical's
[ActuatorType](/docs/reference/engine/classes/CylindricalConstraint.md) is set to
[Servo](/docs/reference/engine/enums/ActuatorType.md), it attempts to translate the attachments to a set
separation specified by [TargetPosition](/docs/reference/engine/classes/CylindricalConstraint.md). This
translation is controlled by [Speed](/docs/reference/engine/classes/CylindricalConstraint.md),
[LinearResponsiveness](/docs/reference/engine/classes/CylindricalConstraint.md), and
[ServoMaxForce](/docs/reference/engine/classes/CylindricalConstraint.md).

#### Limits

You can set limits to restrict both the **sliding range** and **rotation** of
a cylindrical constraint. Enabling the
[LimitsEnabled](/docs/reference/engine/classes/CylindricalConstraint.md) property exposes the
[LowerLimit](/docs/reference/engine/classes/CylindricalConstraint.md) and
[UpperLimit](/docs/reference/engine/classes/CylindricalConstraint.md) values, as well as
[Restitution](/docs/reference/engine/classes/CylindricalConstraint.md) which defines the elasticity of the
attachments when they reach either limit. Enabling the
[AngularLimitsEnabled](/docs/reference/engine/classes/CylindricalConstraint.md)
property exposes the [LowerAngle](/docs/reference/engine/classes/CylindricalConstraint.md) and
[UpperAngle](/docs/reference/engine/classes/CylindricalConstraint.md) limits, as well as
[AngularRestitution](/docs/reference/engine/classes/CylindricalConstraint.md) which
defines the elasticity of the attachments when they reach either limit.

#### Inclination Angle

[InclinationAngle](/docs/reference/engine/classes/CylindricalConstraint.md) defines the
direction of the rotation axis as an angle from the **X** axis in the **XY**
plane of [Attachment0](/docs/reference/engine/classes/Constraint.md), from
-180&nbsp;to&nbsp;180. This lets you tilt the rotating element without
changing the sliding axis.

## Properties

### Property: CylindricalConstraint.AngularActuatorType

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
  "category": "Cylinder",
  "capabilities": [
    "Physics"
  ],
  "simulationAccess": true
}
```

If a cylindrical's
[AngularActuatorType](/docs/reference/engine/classes/CylindricalConstraint.md) is
set to [Motor](/docs/reference/engine/enums/ActuatorType.md), it attempts to rotate the attachments
with the goal of reaching its
[AngularVelocity](/docs/reference/engine/classes/CylindricalConstraint.md). You can
further control this rotation through both
[MotorMaxAngularAcceleration](/docs/reference/engine/classes/CylindricalConstraint.md)
and [MotorMaxTorque](/docs/reference/engine/classes/CylindricalConstraint.md).

If a cylindrical's
[AngularActuatorType](/docs/reference/engine/classes/CylindricalConstraint.md) is
set to [Servo](/docs/reference/engine/enums/ActuatorType.md), it attempts to rotate to an angle
specified by [TargetAngle](/docs/reference/engine/classes/CylindricalConstraint.md). This
rotation is controlled by
[AngularSpeed](/docs/reference/engine/classes/CylindricalConstraint.md),
[AngularResponsiveness](/docs/reference/engine/classes/CylindricalConstraint.md),
and [ServoMaxTorque](/docs/reference/engine/classes/CylindricalConstraint.md).

### Property: CylindricalConstraint.AngularLimitsEnabled

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
  "category": "Cylinder",
  "capabilities": [
    "Physics"
  ],
  "simulationAccess": true
}
```

Enables the angular limits around the rotation axis.

### Property: CylindricalConstraint.AngularResponsiveness

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
  "category": "AngularServo",
  "capabilities": [
    "Physics"
  ],
  "simulationAccess": true
}
```

This property specifies the sharpness of the angular servo motor in
reaching the [TargetAngle](/docs/reference/engine/classes/CylindricalConstraint.md), when
[AngularActuatorType](/docs/reference/engine/classes/CylindricalConstraint.md) is
set to [Servo](/docs/reference/engine/enums/ActuatorType.md). Larger values correspond to a faster
response and smaller values results in more damping and a slower response.

### Property: CylindricalConstraint.AngularRestitution

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
  "category": "AngularLimits",
  "capabilities": [
    "Physics"
  ],
  "simulationAccess": true
}
```

Restitution of the two limits, or how elastic they are. Constrained
between 0 and 1.

### Property: CylindricalConstraint.AngularSpeed

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
  "category": "AngularServo",
  "capabilities": [
    "Physics"
  ],
  "simulationAccess": true
}
```

Target angular speed. This value is unsigned as the servo will always move
toward its target. In radians per second.

### Property: CylindricalConstraint.AngularVelocity

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
  "category": "AngularMotor",
  "capabilities": [
    "Physics"
  ],
  "simulationAccess": true
}
```

The target angular velocity of the motor in radians per second around the
rotation axis.

### Property: CylindricalConstraint.CurrentAngle

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

Signed angle (in degrees) between the reference axis and the secondary
axis of [Attachment1](/docs/reference/engine/classes/Constraint.md) around the rotation
axis. Valid range between -180 and 180.

### Property: CylindricalConstraint.InclinationAngle

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
  "category": "Cylinder",
  "capabilities": [
    "Physics"
  ],
  "simulationAccess": true
}
```

Direction of the rotation axis as an angle from the **X** axis in the
**XY** plane of [Attachment0](/docs/reference/engine/classes/Constraint.md). Valid range
between -180 and 180.

### Property: CylindricalConstraint.LowerAngle

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
  "category": "AngularLimits",
  "capabilities": [
    "Physics"
  ],
  "simulationAccess": true
}
```

Lower limit for the angle (in degrees) between the reference axis and the
SecondaryAxis of [Attachment1](/docs/reference/engine/classes/Constraint.md) around the
rotation axis. Valid range between -180 and 180.

### Property: CylindricalConstraint.MotorMaxAngularAcceleration

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
  "category": "AngularMotor",
  "capabilities": [
    "Physics"
  ],
  "simulationAccess": true
}
```

The maximum angular acceleration of the motor in radians per second
squared.

### Property: CylindricalConstraint.MotorMaxTorque

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
  "category": "AngularMotor",
  "capabilities": [
    "Physics"
  ],
  "simulationAccess": true
}
```

The maximum torque the motor can apply to achieve the target angular
velocity. Units are mass&nbsp;&times;&nbsp;studs&sup2;/second&sup2;.

### Property: CylindricalConstraint.RotationAxisVisible

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
  "category": "Appearance",
  "capabilities": [
    "Physics"
  ]
}
```

Enable the visibility of the rotation axis.

### Property: CylindricalConstraint.ServoMaxTorque

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
  "category": "AngularServo",
  "capabilities": [
    "Physics"
  ],
  "simulationAccess": true
}
```

Maximum torque the servo motor can apply. Units are
mass&nbsp;&times;&nbsp;studs&sup2;/second&sup2;.

### Property: CylindricalConstraint.TargetAngle

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
  "category": "AngularServo",
  "capabilities": [
    "Physics"
  ],
  "simulationAccess": true
}
```

Target angle (in degrees) between the reference axis and the secondary
axis of [Attachment1](/docs/reference/engine/classes/Constraint.md) around the rotation
axis. Valid range between -180 and 180.

### Property: CylindricalConstraint.UpperAngle

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
  "category": "AngularLimits",
  "capabilities": [
    "Physics"
  ],
  "simulationAccess": true
}
```

Upper limit for the angle (in degrees) between the reference axis and the
secondary axis of [Attachment1](/docs/reference/engine/classes/Constraint.md) around the
rotation axis. Valid range between -180 and 180.

### Property: CylindricalConstraint.WorldRotationAxis

```json
{
  "type": "Vector3",
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

The unit vector direction of the rotation axis in world coordinates.

### Property: CylindricalConstraint.SoftlockAngularServoUponReachingTarget

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
  "category": "AngularServo",
  "capabilities": [
    "Physics"
  ],
  "simulationAccess": true
}
```

> **Deprecated:** This property should not be used in new work.

## Inherited Members

### From [SlidingBallConstraint](/docs/reference/engine/classes/SlidingBallConstraint.md)

- **Property `ActuatorType`** (`ActuatorType`): Sets whether the translation of the SlidingBallConstraint is
- **Property `CurrentPosition`** (`float`): The current offset between the constraint's
- **Property `LimitsEnabled`** (`boolean`): Sets whether the SlidingBallConstraint will limit the range of
- **Property `LinearResponsiveness`** (`float`): Specifies the "sharpness" of the linear servo motor in reaching the
- **Property `LowerLimit`** (`float`): The lower positional limit along the **X** axis of
- **Property `MotorMaxAcceleration`** (`float`): The constraint's maximum acceleration when
- **Property `MotorMaxForce`** (`float`): The constraint's maximum force when
- **Property `Restitution`** (`float`): The elasticity of the constraint's Attachments when
- **Property `ServoMaxForce`** (`float`): The constraint's maximum force when
- **Property `Size`** (`float`): The constraint's visualized size.
- **Property `SoftlockServoUponReachingTarget`** (`boolean`):  *(deprecated)*
- **Property `Speed`** (`float`): The constraint's desired speed when
- **Property `TargetPosition`** (`float`): The constraint's attempted target position when
- **Property `UpperLimit`** (`float`): The upper positional limit along the **X** axis of
- **Property `Velocity`** (`float`): The constraint's attempted velocity when

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