---
name: AudioListener
last_updated: 2026-10-30T19:55:51Z
inherits:
  - Instance
  - Object
type: class
memory_category: Internal
summary: "Records an audio stream from its surrounding AudioEmitters in the 3D world."
---

# Class: AudioListener

> Records an audio stream from its surrounding
> [AudioEmitters](/docs/reference/engine/classes/AudioEmitter.md) in the 3D world.

## Description

[AudioListener](/docs/reference/engine/classes/AudioListener.md) records an audio stream from its surrounding
[AudioEmitters](/docs/reference/engine/classes/AudioEmitter.md) in the 3D world. It provides a single
**Output** pin which can be connected to other pins via [Wires](/docs/reference/engine/classes/Wire.md). If
the parent is an [Attachment](/docs/reference/engine/classes/Attachment.md), [Camera](/docs/reference/engine/classes/Camera.md), or [PVInstance](/docs/reference/engine/classes/PVInstance.md),
the parent's world [CFrame](/docs/reference/engine/datatypes/CFrame.md) will be used for listening. If the parent
is not one of these classes, the [AudioListener](/docs/reference/engine/classes/AudioListener.md) effectively hears
nothing.

## Code Samples

**Camera Listener**

```lua
local listener = Instance.new("AudioListener")
local output = Instance.new("AudioDeviceOutput")
local wire = Instance.new("Wire")

listener.Parent = workspace.Camera
wire.Parent = listener
output.Parent = wire

wire.SourceInstance = listener
wire.TargetInstance = output
```

## Properties

### Property: AudioListener.AcousticSimulationEnabled

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
  "category": "Simulation",
  "capabilities": [
    "Audio"
  ]
}
```

Determines whether sound being heard by this [AudioListener](/docs/reference/engine/classes/AudioListener.md) shoud
automatically implement features of acoustic simulation, such as occlusion
(being muffled through walls), diffraction (bending around corners), and
reverberation (echoing off of walls), when being sourced from an
[AudioEmitter](/docs/reference/engine/classes/AudioEmitter.md). Note that the [AudioEmitter](/docs/reference/engine/classes/AudioEmitter.md) also
needs its
[AcousticSimulationEnabled](/docs/reference/engine/classes/AudioEmitter.md)
property set to `true` for the effects to occur.

### Property: AudioListener.AngleAttenuation

```json
{
  "type": "BinaryString",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxEngineSecurity",
    "write": "RobloxEngineSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Listening",
  "capabilities": [
    "Audio"
  ]
}
```

Represents a volume-over-angle curve that affects how loudly a
[AudioListener](/docs/reference/engine/classes/AudioListener.md) will hear the [AudioEmitter](/docs/reference/engine/classes/AudioEmitter.md), based on the
angle between them and the [LookVector](/docs/reference/engine/datatypes/CFrame.md)
associated with the [AudioListener](/docs/reference/engine/classes/AudioListener.md).

This property is internal and can't be accessed by scripts; it exists to
support replication. See
[SetAngleAttenuation()](/docs/reference/engine/classes/AudioListener.md) for
usage details.

### Property: AudioListener.AudioInteractionGroup

```json
{
  "type": "string",
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
  "category": "Interactions",
  "capabilities": [
    "Audio"
  ]
}
```

Controls which [AudioEmitters](/docs/reference/engine/classes/AudioEmitter.md) are audible to this
[AudioListener](/docs/reference/engine/classes/AudioListener.md). Emitters that share an interaction group can be
heard by this Listener.

### Property: AudioListener.DistanceAttenuation

```json
{
  "type": "BinaryString",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxEngineSecurity",
    "write": "RobloxEngineSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Listening",
  "capabilities": [
    "Audio"
  ]
}
```

Represents a volume-over-distance curve that affects how loudly the
[AudioListener](/docs/reference/engine/classes/AudioListener.md) hears any [AudioEmitters](/docs/reference/engine/classes/AudioEmitter.md), based
on the distance between them.

This property is internal and can't be accessed by scripts; it exists to
support replication. See
[SetDistanceAttenuation()](/docs/reference/engine/classes/AudioListener.md)
for usage details.

### Property: AudioListener.PositionInstance

```json
{
  "type": "Instance",
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
  "category": "Listening",
  "capabilities": [
    "Audio"
  ]
}
```

This property is only functional when
[PositionType](/docs/reference/engine/classes/AudioListener.md) is set to
[ListenerPositionType.Instance](/docs/reference/engine/enums/ListenerPositionType.md). In that scenario, this property
determines which [Instance](/docs/reference/engine/classes/Instance.md) will be used to determine the position
of the [AudioListener](/docs/reference/engine/classes/AudioListener.md) when hearing spatial audio from
[AudioEmitters](/docs/reference/engine/classes/AudioEmitter.md).

If set to an instance without a position or `nil`, the
[AudioListener](/docs/reference/engine/classes/AudioListener.md) will not hear anything.

### Property: AudioListener.PositionType

```json
{
  "type": "ListenerPositionType",
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
  "category": "Listening",
  "capabilities": [
    "Audio"
  ]
}
```

The method by which the [AudioListener](/docs/reference/engine/classes/AudioListener.md) determines its 3D location
(the point from which any nearby [AudioEmitters](/docs/reference/engine/classes/AudioEmitter.md) can be
heard). Defaults to [ListenerPositionType.Parent](/docs/reference/engine/enums/ListenerPositionType.md).

### Property: AudioListener.SimulationFidelity

```json
{
  "type": "AudioSimulationFidelity",
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
  "category": "Simulation",
  "capabilities": [
    "Audio"
  ]
}
```

Controls how detailed the audio simulation should be for this
[AudioListener](/docs/reference/engine/classes/AudioListener.md), similar to [MeshPart.CollisionFidelity](/docs/reference/engine/classes/MeshPart.md) or
[MeshPart.RenderFidelity](/docs/reference/engine/classes/MeshPart.md).

[AudioListeners](/docs/reference/engine/classes/AudioListener.md) and
[AudioEmitters](/docs/reference/engine/classes/AudioEmitter.md) which disagree on the necessary level
of detail will use the less-detailed option.

## Methods

### Method: AudioListener:GetAngleAttenuation

**Signature:** `AudioListener:GetAngleAttenuation(): Dictionary`

Returns a table mapping angle to volume. Keys are numbers between `0` and
`180` (inclusive), while values are numbers between `0` and `1`
(inclusive) describing how volume attenuates depending on direction. This
method returns an empty table if the default angle attenuation curve is
being used.

*Security: None · Thread Safety: Unsafe · Capabilities: Audio*

**Returns:** `Dictionary` — Table mapping angle to volume, as described above.

### Method: AudioListener:GetAudibilityFor

**Signature:** `AudioListener:GetAudibilityFor(emitter: AudioEmitter): float`

Calculates how audible an [AudioEmitter](/docs/reference/engine/classes/AudioEmitter.md) is for this listener. The
resulting volume, ranging from `0` to `1`, accounts for distance and angle
attenuation on both the emitter and listener. Use this to drive game logic
that depends on perceived loudness, such as proximity UI indicators or
mechanics that scale with how clearly a sound source is heard.

*Security: None · Thread Safety: Unsafe · Capabilities: Audio*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `emitter` | `AudioEmitter` |  | The [AudioEmitter](/docs/reference/engine/classes/AudioEmitter.md) whose audibility should be calculated relative to this listener. |

**Returns:** `float` — A number between 0 and 1 representing the combined volume after
distance and angle attenuation from both the emitter and listener.

### Method: AudioListener:GetConnectedWires

**Signature:** `AudioListener:GetConnectedWires(pin: string): List<Wire>`

Returns an array of [Wires](/docs/reference/engine/classes/Wire.md) that are connected to the specified
pin. [AudioListener](/docs/reference/engine/classes/AudioListener.md) has one "Output" pin.

*Security: None · Thread Safety: Unsafe · Capabilities: Audio*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `pin` | `string` |  | An input or output pin on this instance |

**Returns:** `List<Wire>` — An array of [Wires](/docs/reference/engine/classes/Wire.md)

### Method: AudioListener:GetDistanceAttenuation

**Signature:** `AudioListener:GetDistanceAttenuation(): Dictionary`

Returns a table mapping distance to volume. Keys are numbers greater than
or equal to 0, while values are numbers between 0 and 1 (inclusive)
describing how volume attenuates over distance. This method returns an
empty table if the default distance attenuation curve is being used.

*Security: None · Thread Safety: Unsafe · Capabilities: Audio*

**Returns:** `Dictionary` — A table mapping distance keys to volume values, or an empty table if
the default curve is being used.

### Method: AudioListener:GetInputPins

**Signature:** `AudioListener:GetInputPins(): Array`

Gets the list of pins that [Wire](/docs/reference/engine/classes/Wire.md) can use in [Wire.TargetName](/docs/reference/engine/classes/Wire.md)
to connect to this instance via its [Wire.TargetInstance](/docs/reference/engine/classes/Wire.md) property.

For [AudioListener](/docs/reference/engine/classes/AudioListener.md), there are none.

*Security: None · Thread Safety: Unsafe · Capabilities: Audio*

**Returns:** `Array` — An array of strings representing valid pin names.

### Method: AudioListener:GetInteractingEmitters

**Signature:** `AudioListener:GetInteractingEmitters(): List<AudioEmitter>`

Returns an array of [AudioEmitters](/docs/reference/engine/classes/AudioEmitter.md) that share an
[AudioInteractionGroup](/docs/reference/engine/classes/AudioListener.md) with the
listener.

*Security: None · Thread Safety: Unsafe · Capabilities: Audio*

**Returns:** `List<AudioEmitter>` — An array of [AudioEmitters](/docs/reference/engine/classes/AudioEmitter.md) that share an
[AudioInteractionGroup](/docs/reference/engine/classes/AudioListener.md) with
this listener.

### Method: AudioListener:GetOutputPins

**Signature:** `AudioListener:GetOutputPins(): Array`

Gets the list of pins that [Wire](/docs/reference/engine/classes/Wire.md) can use in [Wire.SourceName](/docs/reference/engine/classes/Wire.md)
to connect to this instance via its [Wire.SourceInstance](/docs/reference/engine/classes/Wire.md) property.

For [AudioListener](/docs/reference/engine/classes/AudioListener.md), this is `Output` only.

*Security: None · Thread Safety: Unsafe · Capabilities: Audio*

**Returns:** `Array` — An array of strings representing valid pin names.

### Method: AudioListener:SetAngleAttenuation

**Signature:** `AudioListener:SetAngleAttenuation(curve: Dictionary): ()`

Sets a volume-over-angle curve that affects how loudly a
[AudioListener](/docs/reference/engine/classes/AudioListener.md) will hear the [AudioEmitter](/docs/reference/engine/classes/AudioEmitter.md), based on the
angle between them and the [LookVector](/docs/reference/engine/datatypes/CFrame.md)
associated with the [AudioListener](/docs/reference/engine/classes/AudioListener.md).

The curve is represented by a table mapping angle keys to volume values.
Keys are expected to be unique numbers between `0` and `180` (inclusive),
while values are expected to be numbers between `0` and `1` (inclusive).
Tables containing up to 400 key-value pairs are supported.

The volume of a [AudioEmitter](/docs/reference/engine/classes/AudioEmitter.md) from the perspective of the
[AudioListener](/docs/reference/engine/classes/AudioListener.md) at an angle `a` is determined by linearly
interpolating between the volume levels for the points on the curve whose
angle values are directly above and below `a`. If there is either no point
below `a` or no point above `a`, the volume level of the other point is
chosen. Essentially, the curve is a sequence of points connected by
straight lines, and beyond its left and right endpoints the curve extends
outward at their respective volume levels.

This volume will be multiplied with the volumes from all other attenuation
curves (including the ones on the sending [AudioEmitter](/docs/reference/engine/classes/AudioEmitter.md)) to obtain
the final audibility.

If the table is empty or `nil`, the [AudioListener](/docs/reference/engine/classes/AudioListener.md) defaults to
using an angle attenuation curve with the constant volume value of `1`.

*Security: None · Thread Safety: Unsafe · Capabilities: Audio*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `curve` | `Dictionary` |  | A table mapping angle keys (0 to 180) to volume values (0 to 1), or an empty/nil table to use the default constant volume of 1. |

**Returns:** `()`

**Camera Listener**

```lua
local Workspace = game:GetService("Workspace")

local currentCamera = Workspace.CurrentCamera

local listener = Instance.new("AudioListener")
listener.Parent = currentCamera
local wire = Instance.new("Wire")
wire.Parent = listener
local output = Instance.new("AudioDeviceOutput")
output.Parent = wire

listener:SetAngleAttenuation({
	[0] = 1, -- Emitters directly in front of the listener will be full volume
	[180] = 0.5 -- Emitters directly behind the listener will be half volume
})

wire.SourceInstance = listener
wire.TargetInstance = output
```

### Method: AudioListener:SetDistanceAttenuation

**Signature:** `AudioListener:SetDistanceAttenuation(curve: Dictionary): ()`

Sets a volume-over-distance curve that affects how loudly the
[AudioListener](/docs/reference/engine/classes/AudioListener.md) will hear any [AudioEmitters](/docs/reference/engine/classes/AudioEmitter.md),
based on the distance between them. This is useful when you want a
particular listener to have an extended or shortened hearing range — for
example, a character with enhanced hearing — without modifying the
emitting [AudioEmitter](/docs/reference/engine/classes/AudioEmitter.md) or separating emitters and listeners into
different interaction groups.

The curve is represented by a table mapping distance keys to volume
values. Keys are expected to be unique numbers greater than or equal to 0,
while values are expected to be numbers between 0 and 1 (inclusive).
Tables containing up to 400 key-value pairs are supported.

The volume of a [AudioEmitter](/docs/reference/engine/classes/AudioEmitter.md) from the perspective of the
[AudioListener](/docs/reference/engine/classes/AudioListener.md) at a distance `d` is determined by linearly
interpolating between the volume levels for the points on the curve whose
distance values are directly above and below `d`. If there is either no
point below `d` or no point above `d`, the volume level of the other point
is chosen. Essentially, the curve is a sequence of points connected by
straight lines, and beyond its left and right endpoints the curve extends
outward infinitely at their respective volume levels.

This volume will be multiplied with the volumes from all other attenuation
curves (including the ones on the sending [AudioEmitter](/docs/reference/engine/classes/AudioEmitter.md)) to obtain
the final audibility.

If the table is empty or `nil`, the [AudioListener](/docs/reference/engine/classes/AudioListener.md) defaults to
applying a constant volume of 1 everywhere.

*Security: None · Thread Safety: Unsafe · Capabilities: Audio*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `curve` | `Dictionary` |  | A table mapping distance keys (greater than or equal to 0) to volume values (0 to 1), or an empty/nil table to use the default constant volume of 1 everywhere. |

**Returns:** `()`

## Events

### Event: AudioListener.WiringChanged

**Signature:** `AudioListener.WiringChanged(connected: boolean, pin: string, wire: Wire, instance: Instance)`

Event that fires after a [Wire](/docs/reference/engine/classes/Wire.md) becomes connected or disconnected,
and that [Wire](/docs/reference/engine/classes/Wire.md) is now or was previously connected to a pin on the
[AudioListener](/docs/reference/engine/classes/AudioListener.md) and to some other wirable instance.

*Security: None · Capabilities: Audio*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `connected` | `boolean` | Whether the instance got connected or disconnected. |
| `pin` | `string` | The pin on the [AudioListener](/docs/reference/engine/classes/AudioListener.md) that the [Wire](/docs/reference/engine/classes/Wire.md) targets. |
| `wire` | `Wire` | The [Wire](/docs/reference/engine/classes/Wire.md) between the [AudioListener](/docs/reference/engine/classes/AudioListener.md) and the other instance. |
| `instance` | `Instance` | The other instance that is or was connected through the [Wire](/docs/reference/engine/classes/Wire.md). |

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