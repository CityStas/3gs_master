---
name: ControllerPartSensor
last_updated: 2026-10-30T19:55:52Z
inherits:
  - ControllerSensor
  - SensorBase
  - Instance
  - Object
type: class
memory_category: Instances
summary: "A SensorBase that outputs data about another BasePart based on Humanoid floor and ladder detection logic."
---

# Class: ControllerPartSensor

> A [SensorBase](/docs/reference/engine/classes/SensorBase.md) that outputs data about another [BasePart](/docs/reference/engine/classes/BasePart.md) based on
> [Humanoid](/docs/reference/engine/classes/Humanoid.md) floor and ladder detection logic.

## Description

A [SensorBase](/docs/reference/engine/classes/SensorBase.md) that outputs data about another [BasePart](/docs/reference/engine/classes/BasePart.md) based on
[Humanoid](/docs/reference/engine/classes/Humanoid.md) floor and ladder detection logic. It is primarily used for
sending data to a character controller. Using a [ControllerPartSensor](/docs/reference/engine/classes/ControllerPartSensor.md)
allows you to detect [BaseParts](/docs/reference/engine/classes/BasePart.md) in the same manner as the
[Humanoid](/docs/reference/engine/classes/Humanoid.md) uses for detecting floors and ladders.

## Properties

### Property: ControllerPartSensor.HitFrame

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
  "category": "Output",
  "capabilities": [
    "Basic"
  ],
  "simulationAccess": true
}
```

The position in world space where the sensor hit the
[ControllerPartSensor.SensedPart](/docs/reference/engine/classes/ControllerPartSensor.md).

### Property: ControllerPartSensor.HitNormal

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
  "category": "Output",
  "capabilities": [
    "Basic"
  ],
  "simulationAccess": true
}
```

The surface normal at the position where the sensor hit the SensedPart.

### Property: ControllerPartSensor.LadderSearchHeight

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
  "category": "Input",
  "capabilities": [
    "Basic"
  ],
  "simulationAccess": true
}
```

Top of the vertical extent the sensor scans for a climbable ladder, in
studs relative to the sensor's parent [BasePart](/docs/reference/engine/classes/BasePart.md). Together with
[ControllerPartSensor.LadderSearchOffset](/docs/reference/engine/classes/ControllerPartSensor.md), it defines the height
range: the region extends upward to `LadderSearchHeight` minus
`LadderSearchOffset`.

Defaults to `6`; clamped to non-negative values.

Only affects sensing when [ControllerPartSensor.SensorMode](/docs/reference/engine/classes/ControllerPartSensor.md) is a
ladder mode such as [SensorMode.Ladder](/docs/reference/engine/enums/SensorMode.md). Because `SensorMode`
defaults to [SensorMode.Floor](/docs/reference/engine/enums/SensorMode.md), this has no effect until `SensorMode`
is changed.

### Property: ControllerPartSensor.LadderSearchOffset

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
  "category": "Input",
  "capabilities": [
    "Basic"
  ],
  "simulationAccess": true
}
```

Downward offset, in studs relative to the parent [BasePart](/docs/reference/engine/classes/BasePart.md), that
positions the vertical extent scanned for a climbable ladder. Behaves like
a hip-height offset: increasing it lowers both the bottom and top of the
searched region, and scales the rung-spacing tolerance used to decide
whether a surface is climbable.

Defaults to `5`; clamped to non-negative values.

Only affects sensing when [ControllerPartSensor.SensorMode](/docs/reference/engine/classes/ControllerPartSensor.md) is a
ladder mode such as [SensorMode.Ladder](/docs/reference/engine/enums/SensorMode.md). Because `SensorMode`
defaults to [SensorMode.Floor](/docs/reference/engine/enums/SensorMode.md), this has no effect until `SensorMode`
is changed.

### Property: ControllerPartSensor.SearchDistance

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
  "category": "Input",
  "capabilities": [
    "Basic"
  ],
  "simulationAccess": true
}
```

The distance from the sensor's parent [BasePart](/docs/reference/engine/classes/BasePart.md) to use when sensing
other parts.

### Property: ControllerPartSensor.SensedMaterial

```json
{
  "type": "Material",
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
    "Basic"
  ],
  "simulationAccess": true
}
```

Surface [Material](/docs/reference/engine/enums/Material.md) of the part the sensor currently detects, matching
the material [Humanoid](/docs/reference/engine/classes/Humanoid.md) floor and ladder detection report for the
same contact. Updated as an output alongside
[ControllerPartSensor.SensedPart](/docs/reference/engine/classes/ControllerPartSensor.md),
[ControllerPartSensor.HitFrame](/docs/reference/engine/classes/ControllerPartSensor.md), and
[ControllerPartSensor.HitNormal](/docs/reference/engine/classes/ControllerPartSensor.md) each time the sensor senses.

Defaults to [Material.Air](/docs/reference/engine/enums/Material.md).

### Property: ControllerPartSensor.SensedPart

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
  "category": "Output",
  "capabilities": [
    "Basic"
  ],
  "simulationAccess": true
}
```

A reference to the [BasePart](/docs/reference/engine/classes/BasePart.md) hit by the sensor.

### Property: ControllerPartSensor.SensorMode

```json
{
  "type": "SensorMode",
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
    "Basic"
  ],
  "simulationAccess": true
}
```

Determines what behavior this [SensorBase](/docs/reference/engine/classes/SensorBase.md) uses when sensing other
parts.

A setting of [SensorMode.Ladder](/docs/reference/engine/enums/SensorMode.md) performs the same ladder detection
logic used by a [Humanoid](/docs/reference/engine/classes/Humanoid.md) to populate sensor output. It currently
always senses along the forward vector of its parent [BasePart](/docs/reference/engine/classes/BasePart.md).

A setting of [SensorMode.Floor](/docs/reference/engine/enums/SensorMode.md) performs the same floor detection
logic used by a [Humanoid](/docs/reference/engine/classes/Humanoid.md) to populate sensor output. It currently
always senses along the negative up vector of the world.

## Inherited Members

### From [SensorBase](/docs/reference/engine/classes/SensorBase.md)

- **Property `UpdateType`** (`SensorUpdateType`): Determines how the sensor will update its output data.
- **Method `Sense(): ()`**: Recomputes the sensor's output properties immediately. *(deprecated)*
- **Event `OnSensorOutputChanged`**: Fires when one of the sensor's output properties changes value.

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