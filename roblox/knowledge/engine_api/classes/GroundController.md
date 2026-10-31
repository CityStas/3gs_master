---
name: GroundController
last_updated: 2026-10-30T19:55:52Z
inherits:
  - ControllerBase
  - Instance
  - Object
type: class
memory_category: Instances
summary: "The ControllerBase that moves a ControllerManager character while it is walking or standing on the ground."
---

# Class: GroundController

> The [ControllerBase](/docs/reference/engine/classes/ControllerBase.md) that moves a [ControllerManager](/docs/reference/engine/classes/ControllerManager.md) character
> while it is walking or standing on the ground.

## Description

[GroundController](/docs/reference/engine/classes/GroundController.md) is the [ControllerBase](/docs/reference/engine/classes/ControllerBase.md) that a
[ControllerManager](/docs/reference/engine/classes/ControllerManager.md) activates when its character is moving along or
standing on the ground. It keeps the [ControllerManager.RootPart](/docs/reference/engine/classes/ControllerManager.md)
hovering at [GroundController.GroundOffset](/docs/reference/engine/classes/GroundController.md) above the detected floor,
drives locomotion toward the manager's target velocity (ramped by
[GroundController.AccelerationTime](/docs/reference/engine/classes/GroundController.md) and
[GroundController.DecelerationTime](/docs/reference/engine/classes/GroundController.md)), keeps the root part upright, and
turns it toward the [ControllerManager.FacingDirection](/docs/reference/engine/classes/ControllerManager.md). Ground friction
comes from the floor material and this controller's
[GroundController.Friction](/docs/reference/engine/classes/GroundController.md) and [GroundController.FrictionWeight](/docs/reference/engine/classes/GroundController.md).
Parent one to a [ControllerManager](/docs/reference/engine/classes/ControllerManager.md) to supply on-ground movement; the
manager selects it through [ControllerManager.ActiveController](/docs/reference/engine/classes/ControllerManager.md) and
activates one controller at a time.

## Properties

### Property: GroundController.AccelerationTime

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
  "category": "Movement",
  "capabilities": [
    "Basic"
  ],
  "simulationAccess": true
}
```

Estimated time (in seconds) taken to reach the desired speed after walking
input begins. The character will accelerate linearly at the computed rate,
impacted by friction, so a given time may be less accurate with lower
friction.

### Property: GroundController.BalanceMaxTorque

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
  "category": "Balance",
  "capabilities": [
    "Basic"
  ],
  "simulationAccess": true
}
```

The maximum torque used to keep the [ControllerManager.RootPart](/docs/reference/engine/classes/ControllerManager.md)
aligned upright. When misaligned, this amount of torque is applied to
reach the [BalanceSpeed](/docs/reference/engine/classes/GroundController.md) and realign
the root part. A higher torque means more force is required to cause the
root part to tilt. A lower torque means it's easer for the root part to
get knocked over when running into things. This property is hidden and has
no effect when [ControllerBase.BalanceRigidityEnabled](/docs/reference/engine/classes/ControllerBase.md) is true.

### Property: GroundController.BalanceSpeed

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
  "category": "Balance",
  "capabilities": [
    "Basic"
  ],
  "simulationAccess": true
}
```

The maximum angular speed used to align the
[ControllerManager.RootPart](/docs/reference/engine/classes/ControllerManager.md) upright. A lower value means it takes
longer for the root part to recover to the upright position when
misaligned. A higher value results in a quicker recovery.

### Property: GroundController.DecelerationTime

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
  "category": "Movement",
  "capabilities": [
    "Basic"
  ],
  "simulationAccess": true
}
```

Estimated time (in seconds) taken to reach a complete stop from full speed
after walking input ends. The character will decelerate linearly at the
computed rate, impacted by friction, so a given time may be less accurate
with lower friction.

### Property: GroundController.Friction

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
  "category": "Movement",
  "capabilities": [
    "Basic"
  ],
  "simulationAccess": true
}
```

The coefficient of friction for the character at the point between it and
the ground. Determines how much force is available for locomotion or to
keep the character stationary on slopes.

### Property: GroundController.FrictionWeight

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
  "category": "Movement",
  "capabilities": [
    "Basic"
  ],
  "simulationAccess": true
}
```

Amount the character's friction is weighed against the ground friction,
equal in behavior to the
[FrictionWeight](/docs/reference/engine/datatypes/PhysicalProperties.md) data type of
[BasePart.CustomPhysicalProperties](/docs/reference/engine/classes/BasePart.md). Higher values mean more of a
part's [Friction](/docs/reference/engine/datatypes/PhysicalProperties.md) will be used.

### Property: GroundController.GroundOffset

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
  "category": "Movement",
  "capabilities": [
    "Basic"
  ],
  "simulationAccess": true
}
```

The target distance above the
[ControllerManager.GroundSensor.HitPosition](/docs/reference/engine/classes/ControllerManager.md) to keep the
[ControllerManager.RootPart](/docs/reference/engine/classes/ControllerManager.md) at. If the root part is below this
offset from the ground, a force is applied to raise up to this height. If
it's above, nothing happens.

### Property: GroundController.TurnSpeedFactor

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
  "category": "Movement",
  "capabilities": [
    "Basic"
  ],
  "simulationAccess": true
}
```

The value multiplied by the [ControllerManager.BaseTurnSpeed](/docs/reference/engine/classes/ControllerManager.md) to
determine the final target angular velocity while this controller is
active. The angular velocity is applied when turning towards the
[ControllerManager.FacingDirection.](/docs/reference/engine/classes/ControllerManager.md)

## Inherited Members

### From [ControllerBase](/docs/reference/engine/classes/ControllerBase.md)

- **Property `Active`** (`boolean`): Whether this controller is currently the active controller of its
- **Property `BalanceRigidityEnabled`** (`boolean`): Whether the controller holds its balance orientation rigidly instead of
- **Property `MoveSpeedFactor`** (`float`): The value multiplied by the ControllerManager.BaseMoveSpeed.

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