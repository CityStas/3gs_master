---
name: AudioEmitter
last_updated: 2026-10-30T19:55:51Z
inherits:
  - Instance
  - Object
type: class
memory_category: Internal
summary: "Emits audio streams into the world."
---

# Class: AudioEmitter

> Emits audio streams into the world.

## Description

[AudioEmitter](/docs/reference/engine/classes/AudioEmitter.md) emits audio streams into the world. It provides a single
**Input** pin that can be connected to by one or more [Wires](/docs/reference/engine/classes/Wire.md). Any
streams wired to an [AudioEmitter](/docs/reference/engine/classes/AudioEmitter.md) get broadcasted into the world from
the emitter's parent's position. If the parent is an [Attachment](/docs/reference/engine/classes/Attachment.md),
[Camera](/docs/reference/engine/classes/Camera.md), or [PVInstance](/docs/reference/engine/classes/PVInstance.md), the parent's world-position will be
used. If the parent is not one of these classes, the [AudioEmitter](/docs/reference/engine/classes/AudioEmitter.md) is
effectively silent.

[AudioEmitters](/docs/reference/engine/classes/AudioEmitter.md) are heard by
[AudioListeners](/docs/reference/engine/classes/AudioListener.md) in order to implement 3D spatialization.

## Code Samples

**Playing one asset from multiple 3d locations at once**

```lua
local part1: BasePart = workspace.Speakers.Left
local part2: BasePart = workspace.Speakers.Right
local player: AudioPlayer = workspace.AudioPlayer

local leftEmitter = Instance.new("AudioEmitter")
local rightEmitter = Instance.new("AudioEmitter")
local toLeft = Instance.new("Wire")
local toRight = Instance.new("Wire")

leftEmitter.Parent = part1
rightEmitter.Parent = part2

toLeft.Parent = leftEmitter
toLeft.SourceInstance = player
toLeft.TargetInstance = leftEmitter

toRight.Parent = rightEmitter
toRight.SourceInstance = player
toRight.TargetInstance = rightEmitter

player:Play()
```

## Properties

### Property: AudioEmitter.AcousticSimulationEnabled

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

Determines whether sound from this [AudioEmitter](/docs/reference/engine/classes/AudioEmitter.md) shoud
automatically implement features of acoustic simulation, such as occlusion
(being muffled through walls), diffraction (bending around corners), and
reverberation (echoing off of walls), when being heard by an
[AudioListener](/docs/reference/engine/classes/AudioListener.md). Note that the [AudioListener](/docs/reference/engine/classes/AudioListener.md)
also needs its
[AcousticSimulationEnabled](/docs/reference/engine/classes/AudioListener.md)
property set to `true` for the effects to occur.

### Property: AudioEmitter.AngleAttenuation

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
  "category": "Emission",
  "capabilities": [
    "Audio"
  ]
}
```

Represents a volume-over-angle curve that affects how loudly a
[AudioListener](/docs/reference/engine/classes/AudioListener.md) will hear the [AudioEmitter](/docs/reference/engine/classes/AudioEmitter.md), based on the
angle between them and the [LookVector](/docs/reference/engine/datatypes/CFrame.md)
associated with the [AudioEmitter](/docs/reference/engine/classes/AudioEmitter.md).

This property is internal and can't be accessed by scripts; it exists to
support replication. See
[SetAngleAttenuation()](/docs/reference/engine/classes/AudioEmitter.md) for usage
details.

### Property: AudioEmitter.AudioInteractionGroup

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

If an [AudioEmitter](/docs/reference/engine/classes/AudioEmitter.md) and an [AudioListener](/docs/reference/engine/classes/AudioListener.md) share an
interaction group, then the listener is capable of hearing the emitter.

### Property: AudioEmitter.DistanceAttenuation

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
  "category": "Emission",
  "capabilities": [
    "Audio"
  ]
}
```

Represents a volume-over-distance curve that affects how loudly a
[AudioListener](/docs/reference/engine/classes/AudioListener.md) will hear the [AudioEmitter](/docs/reference/engine/classes/AudioEmitter.md), based on the
distance between them.

This property is internal and can't be accessed by scripts; it exists to
support replication. See
[SetDistanceAttenuation()](/docs/reference/engine/classes/AudioEmitter.md) for
usage details.

### Property: AudioEmitter.DistanceAttenuationBounds

```json
{
  "type": "NumberRange",
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
  "category": "Emission",
  "capabilities": [
    "Audio"
  ]
}
```

Specifies the [NumberRange](/docs/reference/engine/datatypes/NumberRange.md) that defines the minimum and maximum
distances for the distance attenuation preset selected by
[DistanceAttenuationMode](/docs/reference/engine/classes/AudioEmitter.md). The
emitter is at full volume when a [AudioListener](/docs/reference/engine/classes/AudioListener.md) is within the
minimum distance and fully attenuated at or beyond the maximum distance.
The attenuation curve between these bounds is determined by the chosen
[DistanceAttenuationMode](/docs/reference/engine/enums/DistanceAttenuationMode.md).

Defaults to a [NumberRange](/docs/reference/engine/datatypes/NumberRange.md) of `[4, 10000]`. This property is
only used when
[DistanceAttenuationMode](/docs/reference/engine/classes/AudioEmitter.md) is
set to a preset other than [DistanceAttenuationMode.Custom](/docs/reference/engine/enums/DistanceAttenuationMode.md).

### Property: AudioEmitter.DistanceAttenuationMode

```json
{
  "type": "DistanceAttenuationMode",
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
  "category": "Emission",
  "capabilities": [
    "Audio"
  ]
}
```

Determines which formula is used to roll off the perceived volume of this
[AudioEmitter](/docs/reference/engine/classes/AudioEmitter.md) as the distance from a [AudioListener](/docs/reference/engine/classes/AudioListener.md)
increases, via [DistanceAttenuationMode](/docs/reference/engine/enums/DistanceAttenuationMode.md).

When set to any value other than [DistanceAttenuationMode.Custom](/docs/reference/engine/enums/DistanceAttenuationMode.md),
[DistanceAttenuationBounds](/docs/reference/engine/classes/AudioEmitter.md)
defines the minimum and maximum distances for the rolloff, and the custom
curve set by
[SetDistanceAttenuation()](/docs/reference/engine/classes/AudioEmitter.md) is
ignored. Defaults to [DistanceAttenuationMode.Custom](/docs/reference/engine/enums/DistanceAttenuationMode.md).

### Property: AudioEmitter.PositionInstance

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
  "category": "Emission",
  "capabilities": [
    "Audio"
  ]
}
```

This property is only functional when
[PositionType](/docs/reference/engine/classes/AudioEmitter.md) is set to
[EmitterPositionType.Instance](/docs/reference/engine/enums/EmitterPositionType.md). In that scenario, this property
determines which [Instance](/docs/reference/engine/classes/Instance.md) will be used to determine the position
of spatial audio emitted by the [AudioEmitter](/docs/reference/engine/classes/AudioEmitter.md) to be heard by
[AudioListeners](/docs/reference/engine/classes/AudioListener.md).

If set to an instance without a position or `nil`, the
[AudioEmitter](/docs/reference/engine/classes/AudioEmitter.md) will not be heard.

### Property: AudioEmitter.PositionType

```json
{
  "type": "EmitterPositionType",
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
  "category": "Emission",
  "capabilities": [
    "Audio"
  ]
}
```

The method by which the [AudioEmitter](/docs/reference/engine/classes/AudioEmitter.md) determines its 3D location
(the point from which audio can be heard by any nearby
[AudioListeners](/docs/reference/engine/classes/AudioListener.md)). Defaults to
[EmitterPositionType.Parent](/docs/reference/engine/enums/EmitterPositionType.md).

### Property: AudioEmitter.SimulationFidelity

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
[AudioEmitter](/docs/reference/engine/classes/AudioEmitter.md), similar to [MeshPart.CollisionFidelity](/docs/reference/engine/classes/MeshPart.md) or
[MeshPart.RenderFidelity](/docs/reference/engine/classes/MeshPart.md).

[AudioEmitters](/docs/reference/engine/classes/AudioEmitter.md) and
[AudioListeners](/docs/reference/engine/classes/AudioListener.md) which disagree on the necessary level
of detail will use the less-detailed option.

## Methods

### Method: AudioEmitter:GetAngleAttenuation

**Signature:** `AudioEmitter:GetAngleAttenuation(): Dictionary`

Returns a table mapping angle to volume. Keys are numbers between `0` and
`180` (inclusive), while values are numbers between `0` and `1`
(inclusive) describing how volume attenuates depending on direction. This
method returns an empty table if the default angle attenuation curve is
being used.

*Security: None · Thread Safety: Unsafe · Capabilities: Audio*

**Returns:** `Dictionary` — Table mapping angle to volume, as described above.

### Method: AudioEmitter:GetAudibilityFor

**Signature:** `AudioEmitter:GetAudibilityFor(listener: AudioListener): float`

Calculates how audible this emitter is for a particular
[AudioListener](/docs/reference/engine/classes/AudioListener.md). The resulting volume, ranging from `0` to `1`,
accounts for distance and angle attenuation on both the emitter and
listener.

*Security: None · Thread Safety: Unsafe · Capabilities: Audio*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `listener` | `AudioListener` |  | The [AudioListener](/docs/reference/engine/classes/AudioListener.md) to calculate audibility for. |

**Returns:** `float` — A number between `0` and `1` representing the combined volume after
distance and angle attenuation.

### Method: AudioEmitter:GetConnectedWires

**Signature:** `AudioEmitter:GetConnectedWires(pin: string): List<Wire>`

Returns an array of [Wires](/docs/reference/engine/classes/Wire.md) that are connected to the specified
pin. [AudioEmitter](/docs/reference/engine/classes/AudioEmitter.md) has one "Input" pin.

*Security: None · Thread Safety: Unsafe · Capabilities: Audio*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `pin` | `string` |  | An input or output pin on this instance |

**Returns:** `List<Wire>` — An array of [Wires](/docs/reference/engine/classes/Wire.md)

### Method: AudioEmitter:GetDistanceAttenuation

**Signature:** `AudioEmitter:GetDistanceAttenuation(): Dictionary`

Returns a table mapping distance to volume. Keys are numbers greater than
or equal to 0, while values are numbers between 0 and 1 (inclusive)
describing how volume attenuates over distance. This method returns an
empty table if the default distance attenuation curve is being used.

Note that this method always returns the custom curve set by
[SetDistanceAttenuation()](/docs/reference/engine/classes/AudioEmitter.md),
regardless of the current
[DistanceAttenuationMode](/docs/reference/engine/classes/AudioEmitter.md)
setting. When a preset mode is active, the custom curve is not used for
attenuation and this return value may not reflect the active rolloff
behavior.

*Security: None · Thread Safety: Unsafe · Capabilities: Audio*

**Returns:** `Dictionary` — A table mapping distance to volume, as described above.

### Method: AudioEmitter:GetInputPins

**Signature:** `AudioEmitter:GetInputPins(): Array`

Gets the list of pins that [Wire](/docs/reference/engine/classes/Wire.md) can use in [Wire.TargetName](/docs/reference/engine/classes/Wire.md)
to connect to this instance via its [Wire.TargetInstance](/docs/reference/engine/classes/Wire.md) property.

For [AudioEmitter](/docs/reference/engine/classes/AudioEmitter.md), this is `Input` only.

*Security: None · Thread Safety: Unsafe · Capabilities: Audio*

**Returns:** `Array` — An array of strings representing valid pin names.

### Method: AudioEmitter:GetInteractingListeners

**Signature:** `AudioEmitter:GetInteractingListeners(): List<AudioListener>`

Returns an array of [AudioListeners](/docs/reference/engine/classes/AudioListener.md) that share an
[AudioInteractionGroup](/docs/reference/engine/classes/AudioEmitter.md) with the
emitter.

*Security: None · Thread Safety: Unsafe · Capabilities: Audio*

**Returns:** `List<AudioListener>` — An array of [AudioListeners](/docs/reference/engine/classes/AudioListener.md).

### Method: AudioEmitter:GetOutputPins

**Signature:** `AudioEmitter:GetOutputPins(): Array`

Gets the list of pins that [Wire](/docs/reference/engine/classes/Wire.md) can use in [Wire.SourceName](/docs/reference/engine/classes/Wire.md)
to connect to this instance via its [Wire.SourceInstance](/docs/reference/engine/classes/Wire.md) property.

For [AudioEmitter](/docs/reference/engine/classes/AudioEmitter.md), there are none.

*Security: None · Thread Safety: Unsafe · Capabilities: Audio*

**Returns:** `Array` — An array of strings representing valid pin names.

### Method: AudioEmitter:SetAngleAttenuation

**Signature:** `AudioEmitter:SetAngleAttenuation(curve: Dictionary): ()`

Sets a volume-over-angle curve that affects how loudly a
[AudioListener](/docs/reference/engine/classes/AudioListener.md) will hear the [AudioEmitter](/docs/reference/engine/classes/AudioEmitter.md), based on the
angle between them and the [LookVector](/docs/reference/engine/datatypes/CFrame.md)
associated with the [AudioEmitter](/docs/reference/engine/classes/AudioEmitter.md). Use this to model directional
audio sources — for example, making an avatar's voice project more
strongly in front of them, or having a monster's growl serve as a gameplay
cue that it is facing the player.

The curve is represented by a table mapping angle keys to volume values.
Keys are expected to be unique numbers between `0` and `180` (inclusive),
while values are expected to be numbers between `0` and `1` (inclusive).
Tables containing up to 400 key-value pairs are supported.

The volume of the [AudioEmitter](/docs/reference/engine/classes/AudioEmitter.md) from the perspective of a
[AudioListener](/docs/reference/engine/classes/AudioListener.md) at an angle `a` is determined by linearly
interpolating between the volume levels for the points on the curve whose
angle values are directly above and below `a`. If there is either no point
below `a` or no point above `a`, the volume level of the other point is
chosen. Essentially, the curve is a sequence of points connected by
straight lines, and beyond its left and right endpoints the curve extends
outward at their respective volume levels.

This volume will be multiplied with the volumes from all other attenuation
curves (including the ones on the receiving [AudioListener](/docs/reference/engine/classes/AudioListener.md)) to
obtain the final audibility.

If the table is empty or `nil`, the [AudioEmitter](/docs/reference/engine/classes/AudioEmitter.md) defaults to using
an angle attenuation curve with the constant volume value of `1`.

*Security: None · Thread Safety: Unsafe · Capabilities: Audio*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `curve` | `Dictionary` |  | A table mapping angle to volume. Keys are numbers between `0` and `180`, values are numbers between `0` and `1`. |

**Returns:** `()`

### Method: AudioEmitter:SetDistanceAttenuation

**Signature:** `AudioEmitter:SetDistanceAttenuation(curve: Dictionary): ()`

Sets a volume-over-distance curve that affects how loudly a
[AudioListener](/docs/reference/engine/classes/AudioListener.md) will hear the [AudioEmitter](/docs/reference/engine/classes/AudioEmitter.md), based on the
distance between them. This curve is only used for attenuation when
[DistanceAttenuationMode](/docs/reference/engine/classes/AudioEmitter.md) is
set to [DistanceAttenuationMode.Custom](/docs/reference/engine/enums/DistanceAttenuationMode.md).

The curve is represented by a table mapping distance keys to volume
values. Keys are expected to be unique numbers greater than or equal to 0,
while values are expected to be numbers between 0 and 1 (inclusive).
Tables containing up to 400 key-value pairs are supported.

The volume of the [AudioEmitter](/docs/reference/engine/classes/AudioEmitter.md) from the perspective of a
[AudioListener](/docs/reference/engine/classes/AudioListener.md) at a distance `d` is determined by linearly
interpolating between the volume levels for the points on the curve whose
distance values are directly above and below `d`. If there is either no
point below `d` or no point above `d`, the volume level of the other point
is chosen. Essentially, the curve is a sequence of points connected by
straight lines, and beyond its left and right endpoints the curve extends
outward infinitely at their respective volume levels.

This volume will be multiplied with the volumes from all other attenuation
curves (including the ones on the receiving [AudioListener](/docs/reference/engine/classes/AudioListener.md)) to
obtain the final audibility.

If the table is empty or `nil`, the [AudioEmitter](/docs/reference/engine/classes/AudioEmitter.md) defaults to using
a distance attenuation curve determined by the inverse-square law.

*Security: None · Thread Safety: Unsafe · Capabilities: Audio*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `curve` | `Dictionary` |  | A table mapping distance to volume. Keys are numbers greater than or equal to `0`, values are numbers between `0` and `1`. |

**Returns:** `()`

**Custom Distance Attenuation**

```lua
local Players = game:GetService("Players")

local emitterPart = Instance.new("Part")
emitterPart.Anchored = true
emitterPart.Position = Vector3.new(0, 0, 0)
emitterPart.Parent = workspace

local emitter: AudioEmitter = Instance.new("AudioEmitter")
emitter.Parent = emitterPart

local curve = {}
curve[10] = 1 -- Within a distance of 10 studs, listeners hear this emitter at full volume
curve[100] = 0.4 -- At a distance of 100 studs, listeners hear this emitter at 40% volume
curve[300] = 0 -- At any distance farther than 300 studs, listeners cannot hear this emitter
emitter:SetDistanceAttenuation(curve)

-- Replicate the rolloff curve from the old voice implementation
-- Default voice without the new audio API uses quadratic rolloff ranging from 7 to 80 studs
local MIN_DISTANCE = 7
local MAX_DISTANCE = 80
local CURVE_STEP_SIZE = 2

local voiceCurve = {}
for i = MIN_DISTANCE, MAX_DISTANCE, CURVE_STEP_SIZE do
	voiceCurve[i] = ((i - MIN_DISTANCE) - (MAX_DISTANCE - MIN_DISTANCE)) ^ 2 / (MAX_DISTANCE - MIN_DISTANCE) ^ 2
end
voiceCurve[MAX_DISTANCE] = 0

local function setVoiceCurve(character)
	local voiceEmitter: AudioEmitter = character:WaitForChild("AudioEmitter")
	voiceEmitter:SetDistanceAttenuation(voiceCurve)
end

for _, player in Players:GetPlayers() do
	if player.Character then
		setVoiceCurve(player.Character)
	end
	player.CharacterAdded:Connect(setVoiceCurve)
end
```

## Events

### Event: AudioEmitter.WiringChanged

**Signature:** `AudioEmitter.WiringChanged(connected: boolean, pin: string, wire: Wire, instance: Instance)`

Event that fires after a [Wire](/docs/reference/engine/classes/Wire.md) becomes connected or disconnected,
and that [Wire](/docs/reference/engine/classes/Wire.md) is now or was previously connected to a pin on the
[AudioEmitter](/docs/reference/engine/classes/AudioEmitter.md) and to some other wirable instance.

*Security: None · Capabilities: Audio*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `connected` | `boolean` | Whether the instance got connected or disconnected. |
| `pin` | `string` | The pin on the [AudioEmitter](/docs/reference/engine/classes/AudioEmitter.md) that the [Wire](/docs/reference/engine/classes/Wire.md) targets. |
| `wire` | `Wire` | The [Wire](/docs/reference/engine/classes/Wire.md) between the [AudioEmitter](/docs/reference/engine/classes/AudioEmitter.md) and the other instance. |
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