---
name: ControllerManager
last_updated: 2026-10-30T19:55:52Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
summary: "Manages simulated motion control for its assigned ControllerManager.RootPart ."
---

# Class: ControllerManager

> Manages simulated motion control for its assigned
> [ControllerManager.RootPart](/docs/reference/engine/classes/ControllerManager.md) .

## Description

The [ControllerManager](/docs/reference/engine/classes/ControllerManager.md) instance manages simulated motion control for
its assigned [ControllerManager.RootPart](/docs/reference/engine/classes/ControllerManager.md). It can be used to build a
physics-based character controller.

## Properties

### Property: ControllerManager.ActiveController

```json
{
  "type": "ControllerBase",
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
    "AvatarBehavior"
  ],
  "simulationAccess": true
}
```

The [ControllerBase](/docs/reference/engine/classes/ControllerBase.md) that is set to be activated on the character.
It does not guarantee that the specified [ControllerBase](/docs/reference/engine/classes/ControllerBase.md) is, in
fact, active. If the [ControllerBase](/docs/reference/engine/classes/ControllerBase.md) cannot be activated for
whatever reason, such as being outside of the character's
[WorldRoot](/docs/reference/engine/classes/WorldRoot.md) or no [Part](/docs/reference/engine/classes/Part.md) being found to use as the floor for a
[GroundController](/docs/reference/engine/classes/GroundController.md), it will remain set and the
[ControllerManager](/docs/reference/engine/classes/ControllerManager.md) will attempt to activate it in the next frame.
This property can be set to `nil` to disable the physics controller.

### Property: ControllerManager.BaseMoveSpeed

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
  "category": "Behavior",
  "capabilities": [
    "AvatarBehavior"
  ],
  "simulationAccess": true
}
```

The base linear movement speed used by all controllers. Controllers
individually customize speed by setting the
[ControllerBase.MoveSpeedFactor](/docs/reference/engine/classes/ControllerBase.md) property.

### Property: ControllerManager.BaseTurnSpeed

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
  "category": "Behavior",
  "capabilities": [
    "AvatarBehavior"
  ],
  "simulationAccess": true
}
```

The base angular turning speed used by all controllers to align the
character to face the desired direction.

### Property: ControllerManager.ClimbSensor

```json
{
  "type": "ControllerSensor",
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
    "AvatarBehavior"
  ],
  "simulationAccess": true
}
```

A reference to the sensor data used while a [ClimbController](/docs/reference/engine/classes/ClimbController.md) is
active. A [ClimbController](/docs/reference/engine/classes/ClimbController.md) will use the
[ControllerPartSensor.HitPart](/docs/reference/engine/classes/ControllerPartSensor.md),
[ControllerPartSensor.HitFrame](/docs/reference/engine/classes/ControllerPartSensor.md), and
[ControllerPartSensor.HitNormal](/docs/reference/engine/classes/ControllerPartSensor.md) for climb movement computations.
Typically a [ControllerPartSensor](/docs/reference/engine/classes/ControllerPartSensor.md) set to [SensorMode.Ladder](/docs/reference/engine/enums/SensorMode.md)
is used here. Otherwise, you can override the sensor's outputs to direct
what sensor data you want the [ClimbController](/docs/reference/engine/classes/ClimbController.md) to use.

### Property: ControllerManager.FacingDirection

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
  "category": "Input",
  "capabilities": [
    "AvatarBehavior"
  ],
  "simulationAccess": true
}
```

The unit vector describing the desired direction to face. Aligns the
[LookVector](/docs/reference/engine/datatypes/CFrame.md) of the
[ControllerManager.RootPart](/docs/reference/engine/classes/ControllerManager.md) to this. Any [Vector3](/docs/reference/engine/datatypes/Vector3.md)
assigned will be automatically unitized.

### Property: ControllerManager.GroundSensor

```json
{
  "type": "ControllerSensor",
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
    "AvatarBehavior"
  ],
  "simulationAccess": true
}
```

A reference to the sensor data used while a [GroundController](/docs/reference/engine/classes/GroundController.md) is
active. A [GroundController](/docs/reference/engine/classes/GroundController.md) will use the
[ControllerPartSensor.HitPart](/docs/reference/engine/classes/ControllerPartSensor.md),
[ControllerPartSensor.HitFrame](/docs/reference/engine/classes/ControllerPartSensor.md), and
[ControllerPartSensor.HitNormal](/docs/reference/engine/classes/ControllerPartSensor.md) for ground movement computations.
Typically a [ControllerPartSensor](/docs/reference/engine/classes/ControllerPartSensor.md) set to [SensorMode.Floor](/docs/reference/engine/enums/SensorMode.md) is
used here. Otherwise, you can override the sensor's outputs to direct what
sensor data you want the [GroundController](/docs/reference/engine/classes/GroundController.md) to use.

### Property: ControllerManager.MovingDirection

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
  "category": "Input",
  "capabilities": [
    "AvatarBehavior"
  ],
  "simulationAccess": true
}
```

The vector describing the desired direction to move in, with a magnitude
between 0 and 1. This is multiplied by
[BaseMoveSpeed](/docs/reference/engine/classes/ControllerManager.md) to determine a final
target move velocity. The [RootPart](/docs/reference/engine/classes/ControllerManager.md) will
attempt to move in this direction based on the rules defined by the
[ActiveController](/docs/reference/engine/classes/ControllerManager.md).

### Property: ControllerManager.RootPart

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
  "category": "Behavior",
  "capabilities": [
    "AvatarBehavior"
  ],
  "simulationAccess": true
}
```

The [BasePart](/docs/reference/engine/classes/BasePart.md) where the controller's forces and torques are
applied. With a typical [Humanoid](/docs/reference/engine/classes/Humanoid.md)-based character, the
[Humanoid.RootPart](/docs/reference/engine/classes/Humanoid.md) is assigned as the
[ControllerManager.RootPart](/docs/reference/engine/classes/ControllerManager.md).

### Property: ControllerManager.UpDirection

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
  "category": "Input",
  "capabilities": [
    "AvatarBehavior"
  ],
  "simulationAccess": true
}
```

The unit vector describing the up direction for the character, which
defaults to `(0, 1, 0)` (world up). Controllers under this
[ControllerManager](/docs/reference/engine/classes/ControllerManager.md) use it to keep the
[RootPart](/docs/reference/engine/classes/ControllerManager.md) upright and to orient
direction-dependent forces. For example, a [GroundController](/docs/reference/engine/classes/GroundController.md)
applies levitation and balancing forces along this direction, while an
[AirController](/docs/reference/engine/classes/AirController.md) and [SwimController](/docs/reference/engine/classes/SwimController.md) align the character to
it. Any [Vector3](/docs/reference/engine/datatypes/Vector3.md) assigned is automatically unitized; a zero,
`NaN`, or infinite value is ignored.

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