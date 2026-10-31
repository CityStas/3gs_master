---
name: HapticEffect
last_updated: 2026-10-30T19:55:52Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
summary: "An object that provides waveform-based haptic feedback (vibrations and rumbles) on supported controllers and mobile devices."
---

# Class: HapticEffect

> An object that provides waveform-based haptic feedback (vibrations and
> rumbles) on supported controllers and mobile devices.

## Description

Modern controllers and devices have motors built‑in to provide haptic
feedback. Adding rumbles and vibrations can provide subtle feedback that is
hard to convey through visuals or audio.

Roblox supports haptics for the following devices:

- Android and iOS phones supporting haptics including most iPhone, Pixel, and
  Samsung Galaxy devices
- PlayStation gamepads
- Xbox gamepads
- Quest Touch controller

## Properties

### Property: HapticEffect.Looped

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
  "category": "Data",
  "capabilities": [
    "Input"
  ]
}
```

Whether the haptic effect loops continuously.

**Looped**

Demonstrates [HapticEffect.Looped](/docs/reference/engine/classes/HapticEffect.md).

```lua
local Workspace = game:GetService("Workspace")

local effect = Instance.new("HapticEffect")
effect.Type = Enum.HapticEffectType.GameplayExplosion
effect.Looped = true
effect.Parent = Workspace

-- Start the haptic effect
effect:Play()
-- After two seconds, stop the effect
task.wait(2)
effect:Stop()
```

### Property: HapticEffect.Position

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
  "category": "Data",
  "capabilities": [
    "Input"
  ]
}
```

Along with [Radius](/docs/reference/engine/classes/HapticEffect.md), specifies the impact
position relative to the input device and, effectively, how broadly that
impact effects nearby motors. Note that some gamepads do not have both
"small" and "large" motors, and that "gamepad large left/right" is not
supported on PC.

**Position**

Demonstrates [HapticEffect.Position](/docs/reference/engine/classes/HapticEffect.md).

```lua
local Workspace = game:GetService("Workspace")

local effect = Instance.new("HapticEffect")

-- Set the position and radius of impact
effect.Position = Vector3.new(0.5, 0.5, 0)
effect.Radius = 1
effect.Parent = Workspace

effect:Play()
```

### Property: HapticEffect.Radius

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
  "category": "Data",
  "capabilities": [
    "Input"
  ]
}
```

Along with [Position](/docs/reference/engine/classes/HapticEffect.md), specifies the impact
radius relative to the input device and, effectively, how broadly that
impact effects nearby motors. Note that some gamepads do not have both
"small" and "large" motors, and that "gamepad large left/right" is not
supported on PC.

**Radius**

Demonstrates [HapticEffect.Radius](/docs/reference/engine/classes/HapticEffect.md).

```lua
local Workspace = game:GetService("Workspace")

local effect = Instance.new("HapticEffect")

-- Set the position and radius of impact
effect.Position = Vector3.new(0.5, 0.5, 0)
effect.Radius = 1
effect.Parent = Workspace

-- Play the haptic effect
effect:Play()
```

### Property: HapticEffect.Type

```json
{
  "type": "HapticEffectType",
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
    "Input"
  ]
}
```

The haptic type, such as [HapticEffectType.GameplayCollision](/docs/reference/engine/enums/HapticEffectType.md) for a
large immediate rumble that dies down quickly. The
[HapticEffectType.Custom](/docs/reference/engine/enums/HapticEffectType.md) value lets you specify a haptic with custom
waveform keys defined through
[SetWaveformKeys()](/docs/reference/engine/classes/HapticEffect.md) and read back
with [GetWaveformKeys()](/docs/reference/engine/classes/HapticEffect.md).

## Methods

### Method: HapticEffect:Play

**Signature:** `HapticEffect:Play(): ()`

Plays the haptic effect.

*Security: None · Thread Safety: Unsafe · Capabilities: Input*

**Returns:** `()`

**Play**

Demonstrates [HapticEffect:Play()](/docs/reference/engine/classes/HapticEffect.md).

```lua
local Workspace = game:GetService("Workspace")

local effect = Instance.new("HapticEffect")
effect.Type = Enum.HapticEffectType.GameplayExplosion
effect.Parent = Workspace

-- Play the haptic effect
effect:Play()
```

### Method: HapticEffect:SetWaveformKeys

**Signature:** `HapticEffect:SetWaveformKeys(keys: Array): ()`

This method lets you define a custom waveform as a table and apply it to
the haptic. It takes an array of [FloatCurveKey](/docs/reference/engine/datatypes/FloatCurveKey.md) objects, each
constructed with three arguments: **time** in milliseconds, **value**
ranging from `0` (no haptic) to `1` (full intensity), and an
[KeyInterpolationMode](/docs/reference/engine/enums/KeyInterpolationMode.md) that controls how the curve interpolates.
between keys.

*Security: None · Thread Safety: Unsafe · Capabilities: Input*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `keys` | `Array` |  | An array of [FloatCurveKey](/docs/reference/engine/datatypes/FloatCurveKey.md) objects defining the custom haptic waveform, where each key specifies a time in milliseconds, an intensity value from 0 (no haptic) to 1 (full intensity), and an [KeyInterpolationMode](/docs/reference/engine/enums/KeyInterpolationMode.md) for interpolation between keys. |

**Returns:** `()`

**Set Waveform Keys**

Demonstrates [HapticEffect:SetWaveformKeys()](/docs/reference/engine/classes/HapticEffect.md).

```lua
local Workspace = game:GetService("Workspace")

local effect = Instance.new("HapticEffect")

-- Set effect type to custom in order to define a waveform
effect.Type = Enum.HapticEffectType.Custom
effect.Parent = Workspace

-- Define the custom waveform curve through a table of FloatCurveKeys
-- Time values are in milliseconds; values range from 0 (no haptic) to 1 (full intensity)
local rampUpWaveform = {
	FloatCurveKey.new(0, 0.3, Enum.KeyInterpolationMode.Linear),
	FloatCurveKey.new(100, 0.4, Enum.KeyInterpolationMode.Linear),
	FloatCurveKey.new(300, 0.8, Enum.KeyInterpolationMode.Linear),
	FloatCurveKey.new(400, 1.0, Enum.KeyInterpolationMode.Linear)
}

-- Set waveform through the effect's method
effect:SetWaveformKeys(rampUpWaveform)
```

### Method: HapticEffect:Stop

**Signature:** `HapticEffect:Stop(): ()`

Stops the haptic effect.

*Security: None · Thread Safety: Unsafe · Capabilities: Input*

**Returns:** `()`

**Stop**

Demonstrates [HapticEffect:Stop()](/docs/reference/engine/classes/HapticEffect.md).

```lua
local Workspace = game:GetService("Workspace")

local effect = Instance.new("HapticEffect")
effect.Type = Enum.HapticEffectType.GameplayExplosion
effect.Looped = true
effect.Parent = Workspace

-- Start the haptic effect
effect:Play()
-- After two seconds, stop the effect
task.wait(2)
effect:Stop()
```

## Events

### Event: HapticEffect.Ended

**Signature:** `HapticEffect.Ended()`

Fires when the [HapticEffect](/docs/reference/engine/classes/HapticEffect.md) has completed playback and stopped.
Note this event will **not** fire for haptics with
[Looped](/docs/reference/engine/classes/HapticEffect.md) set to `true` since they continue
playing upon reaching the end. This event will also **not** fire when the
haptic is stopped before playback has completed.

This event is often used to destroy an [HapticEffect](/docs/reference/engine/classes/HapticEffect.md) when it has
completed playback.

*Security: None · Capabilities: Input*

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