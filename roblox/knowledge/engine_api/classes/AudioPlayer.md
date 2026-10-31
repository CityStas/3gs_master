---
name: AudioPlayer
last_updated: 2026-10-30T19:55:51Z
inherits:
  - Instance
  - Object
type: class
memory_category: Internal
summary: "Used to play audio assets."
---

# Class: AudioPlayer

> Used to play audio assets.

## Description

[AudioPlayer](/docs/reference/engine/classes/AudioPlayer.md) is used to play audio assets. It provides a single
**Output** pin which can be connected to other pins via [Wires](/docs/reference/engine/classes/Wire.md).

## Code Samples

**Outputting Audio to Device**

```lua
local audioPlayer: AudioPlayer = Instance.new("AudioPlayer")
audioPlayer.Parent = workspace
audioPlayer.AssetId = "rbxassetid://9112854440"

local deviceOutput = Instance.new("AudioDeviceOutput")
deviceOutput.Parent = workspace

local wire = Instance.new("Wire")
wire.Parent = workspace

wire.SourceInstance = audioPlayer
wire.TargetInstance = deviceOutput

audioPlayer:Play()
```

## Properties

### Property: AudioPlayer.Asset

```json
{
  "type": "ContentId",
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
  "category": "Asset",
  "capabilities": [
    "Audio"
  ]
}
```

The asset to be loaded into the [AudioPlayer](/docs/reference/engine/classes/AudioPlayer.md). If
[AutoLoad](/docs/reference/engine/classes/AudioPlayer.md) is `true`, the asset loads
immediately once this property is assigned. When loading is complete,
[IsReady](/docs/reference/engine/classes/AudioPlayer.md) becomes `true`.

### Property: AudioPlayer.AudioContent

```json
{
  "type": "Content",
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
  "category": "Asset",
  "capabilities": [
    "Audio"
  ]
}
```

The audio content to be loaded into the [AudioPlayer](/docs/reference/engine/classes/AudioPlayer.md). If
[AutoLoad](/docs/reference/engine/classes/AudioPlayer.md) is `true`, the asset loads
immediately once this property is assigned. When loading is complete,
[IsReady](/docs/reference/engine/classes/AudioPlayer.md) becomes `true`.

### Property: AudioPlayer.AutoLoad

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
  "category": "Asset",
  "capabilities": [
    "Audio"
  ]
}
```

Controls whether [Asset](/docs/reference/engine/classes/AudioPlayer.md) loads automatically once
assigned. If `false`, the asset will load upon the first attempt to play.

### Property: AudioPlayer.AutoPlay

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
  "category": "Playback",
  "capabilities": [
    "Audio"
  ]
}
```

Denotes whether this [AudioPlayer](/docs/reference/engine/classes/AudioPlayer.md) starts playing as soon as it
enters the [DataModel](/docs/reference/engine/classes/DataModel.md) for the first time. This only applies to
[AudioPlayers](/docs/reference/engine/classes/AudioPlayer.md) that are created or deserialized locally,
and does not apply to [AudioPlayers](/docs/reference/engine/classes/AudioPlayer.md) generated via
replication. This property is primarily used at edit time in Studio to
have an [AudioPlayer](/docs/reference/engine/classes/AudioPlayer.md) begin when entering a play session.

### Property: AudioPlayer.IsPlaying

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "None",
    "write": "RobloxEngineSecurity"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Playback",
  "capabilities": [
    "Audio"
  ]
}
```

Denotes whether this [AudioPlayer](/docs/reference/engine/classes/AudioPlayer.md) is currently playing or planning
to play. This property is read-only, but replicates. To play and stop an
[AudioPlayer](/docs/reference/engine/classes/AudioPlayer.md) at runtime, use the [Play()](/docs/reference/engine/classes/AudioPlayer.md)
and [Stop()](/docs/reference/engine/classes/AudioPlayer.md) methods.

### Property: AudioPlayer.IsReady

```json
{
  "type": "boolean",
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
  "category": "Asset",
  "capabilities": [
    "Audio"
  ]
}
```

Denotes whether this [AudioPlayer](/docs/reference/engine/classes/AudioPlayer.md) is loaded, buffered, and ready to
play. Although uncommon, [AudioPlayers](/docs/reference/engine/classes/AudioPlayer.md) may have their
assets unloaded at runtime if there is extreme memory pressure, in which
case [IsReady](/docs/reference/engine/classes/AudioPlayer.md) will become false.

### Property: AudioPlayer.Looping

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
  "category": "Playback",
  "capabilities": [
    "Audio"
  ]
}
```

Controls whether this [AudioPlayer](/docs/reference/engine/classes/AudioPlayer.md) loops when exceeding the end of
its [TimeLength](/docs/reference/engine/classes/AudioPlayer.md),
[LoopRegion](/docs/reference/engine/classes/AudioPlayer.md), or
[PlaybackRegion](/docs/reference/engine/classes/AudioPlayer.md).

### Property: AudioPlayer.LoopRegion

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
  "category": "Regions",
  "capabilities": [
    "Audio"
  ]
}
```

A range, in seconds, denoting a desired loop start and loop end within the
[PlaybackRegion](/docs/reference/engine/classes/AudioPlayer.md) of this
[AudioPlayer](/docs/reference/engine/classes/AudioPlayer.md).

If the [LoopRegion](/docs/reference/engine/classes/AudioPlayer.md) minimum is **greater**
than the [PlaybackRegion](/docs/reference/engine/classes/AudioPlayer.md) minimum, the
loop starts from the [LoopRegion](/docs/reference/engine/classes/AudioPlayer.md) minimum.

If the [LoopRegion](/docs/reference/engine/classes/AudioPlayer.md) minimum is **less** than
the [PlaybackRegion](/docs/reference/engine/classes/AudioPlayer.md) minimum, the loop
starts from the [PlaybackRegion](/docs/reference/engine/classes/AudioPlayer.md) minimum.

If the [LoopRegion](/docs/reference/engine/classes/AudioPlayer.md) maximum is **greater**
than the [PlaybackRegion](/docs/reference/engine/classes/AudioPlayer.md) maximum, the
loop ends at the [PlaybackRegion](/docs/reference/engine/classes/AudioPlayer.md)
maximum.

If the [LoopRegion](/docs/reference/engine/classes/AudioPlayer.md) maximum is **less** than
the [PlaybackRegion](/docs/reference/engine/classes/AudioPlayer.md) maximum, the loop
ends at exactly the [LoopRegion](/docs/reference/engine/classes/AudioPlayer.md) maximum.

If the [LoopRegion](/docs/reference/engine/classes/AudioPlayer.md) minimum **equals** the
[LoopRegion](/docs/reference/engine/classes/AudioPlayer.md) maximum, the [AudioPlayer](/docs/reference/engine/classes/AudioPlayer.md)
uses the [PlaybackRegion](/docs/reference/engine/classes/AudioPlayer.md) property
instead.

### Property: AudioPlayer.PlaybackRegion

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
  "category": "Regions",
  "capabilities": [
    "Audio"
  ]
}
```

Range in seconds denoting a desired start time (minimum) and stop time
(maximum) within the [TimeLength](/docs/reference/engine/classes/AudioPlayer.md).

If the [PlaybackRegion](/docs/reference/engine/classes/AudioPlayer.md) minimum is
**greater** than 0, the sound begins playing from the
[PlaybackRegion](/docs/reference/engine/classes/AudioPlayer.md) minimum time.

If the [PlaybackRegion](/docs/reference/engine/classes/AudioPlayer.md) minimum is
**less** than 0, the sound begins playing from 0.

If the [PlaybackRegion](/docs/reference/engine/classes/AudioPlayer.md) maximum is
**greater** than the [TimeLength](/docs/reference/engine/classes/AudioPlayer.md), the sound
stops at [TimeLength](/docs/reference/engine/classes/AudioPlayer.md).

If the [PlaybackRegion](/docs/reference/engine/classes/AudioPlayer.md) maximum is
**less** than the [TimeLength](/docs/reference/engine/classes/AudioPlayer.md), the sound
stops at exactly the [PlaybackRegion](/docs/reference/engine/classes/AudioPlayer.md)
maximum.

If the [PlaybackRegion](/docs/reference/engine/classes/AudioPlayer.md) minimum
**equals** the [PlaybackRegion](/docs/reference/engine/classes/AudioPlayer.md) maximum,
the sound plays in its entirety.

### Property: AudioPlayer.PlaybackSpeed

```json
{
  "type": "double",
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
  "category": "Playback",
  "capabilities": [
    "Audio"
  ]
}
```

Multiplier controlling how quickly the asset will be played, directly
controlling its perceived pitch. Ranges from 0 to 20.

### Property: AudioPlayer.TimeLength

```json
{
  "type": "double",
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
  "category": "Asset",
  "capabilities": [
    "Audio"
  ]
}
```

Denotes the length of the loaded [Asset](/docs/reference/engine/classes/AudioPlayer.md) in
seconds.

### Property: AudioPlayer.TimePosition

```json
{
  "type": "double",
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
  "category": "Playback",
  "capabilities": [
    "Audio"
  ]
}
```

Tracks and controls the current position of the playhead within the
[Asset](/docs/reference/engine/classes/AudioPlayer.md), in seconds.

### Property: AudioPlayer.Volume

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
  "category": "State",
  "capabilities": [
    "Audio"
  ]
}
```

Volume level which is multiplied onto the output audio stream, controlling
how loudly the asset will be played. Ranges from 0 to 10.

### Property: AudioPlayer.AssetId *(hidden)*

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
    "can_save": false
  },
  "deprecated": true,
  "thread_safety": "ReadSafe",
  "category": "Asset",
  "capabilities": [
    "Audio"
  ]
}
```

> **Deprecated:** This property is deprecated; use [Asset](/docs/reference/engine/classes/AudioPlayer.md) instead.

The asset to be loaded into the [AudioPlayer](/docs/reference/engine/classes/AudioPlayer.md). If
[AutoLoad](/docs/reference/engine/classes/AudioPlayer.md) is `true`, the asset loads
immediately once this property is assigned. When loading is complete,
[IsReady](/docs/reference/engine/classes/AudioPlayer.md) becomes `true`.

## Methods

### Method: AudioPlayer:Cancel

**Signature:** `AudioPlayer:Cancel(actionId: int64?): boolean`

Attempts to cancel a [Play()](/docs/reference/engine/classes/AudioPlayer.md) or
[Stop()](/docs/reference/engine/classes/AudioPlayer.md) command that was scheduled to occur at a
future time. When [Play()](/docs/reference/engine/classes/AudioPlayer.md) or
[Stop()](/docs/reference/engine/classes/AudioPlayer.md) is called with an `atTime` argument, the
action is scheduled against
[GetMixerTime()](/docs/reference/engine/classes/SoundService.md) and the call returns a
unique `actionId`. Passing that `actionId` to this method prevents the
scheduled action from taking effect.

Returns `true` if the pending action was found and successfully cancelled.
Returns `false` if the action has already occurred, was never scheduled,
or the supplied `actionId` does not correspond to a pending action.

*Security: None · Thread Safety: Unsafe · Capabilities: Audio*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `actionId` | `int64?` |  | The unique-ID of a pre-planned `Play` or `Stop` command. |

**Returns:** `boolean` — Whether the cancellation was successful. Returns false if the action
has already occurred, or otherwise does not exist.

### Method: AudioPlayer:GetConnectedWires

**Signature:** `AudioPlayer:GetConnectedWires(pin: string): List<Wire>`

Returns an array of [Wires](/docs/reference/engine/classes/Wire.md) that are connected to the specified
pin. [AudioPlayer](/docs/reference/engine/classes/AudioPlayer.md) has one "Output" pin.

*Security: None · Thread Safety: Unsafe · Capabilities: Audio*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `pin` | `string` |  | An input or output pin on this instance |

**Returns:** `List<Wire>` — An array of [Wires](/docs/reference/engine/classes/Wire.md)

### Method: AudioPlayer:GetInputPins

**Signature:** `AudioPlayer:GetInputPins(): Array`

Gets the list of pins that [Wire](/docs/reference/engine/classes/Wire.md) can use in [Wire.TargetName](/docs/reference/engine/classes/Wire.md)
to connect to this instance via its [Wire.TargetInstance](/docs/reference/engine/classes/Wire.md) property.

For [AudioPlayer](/docs/reference/engine/classes/AudioPlayer.md), there are none.

*Security: None · Thread Safety: Unsafe · Capabilities: Audio*

**Returns:** `Array` — An array of strings representing valid pin names.

### Method: AudioPlayer:GetOutputPins

**Signature:** `AudioPlayer:GetOutputPins(): Array`

Gets the list of pins that [Wire](/docs/reference/engine/classes/Wire.md) can use in [Wire.SourceName](/docs/reference/engine/classes/Wire.md)
to connect to this instance via its [Wire.SourceInstance](/docs/reference/engine/classes/Wire.md) property.

For [AudioPlayer](/docs/reference/engine/classes/AudioPlayer.md), this is `Output` only.

*Security: None · Thread Safety: Unsafe · Capabilities: Audio*

**Returns:** `Array` — An array of strings representing valid pin names.

### Method: AudioPlayer:GetWaveformAsync

**Signature:** `AudioPlayer:GetWaveformAsync(timeRange: NumberRange, samples: int): Array`

Returns a sampling of the waveform data for the loaded
[Asset](/docs/reference/engine/classes/AudioPlayer.md), allowing you to check the volume of an
asset over its full duration without playing it. Unlike
[AudioAnalyzer](/docs/reference/engine/classes/AudioAnalyzer.md), which measures volume levels of a live audio stream
in real time, this method analyzes the asset ahead of time, making it
suitable for waverform visualization or logic that needs audio content
before playback begins.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Audio*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `timeRange` | `NumberRange` |  | The start and end time (in seconds) of the segment to read. |
| `samples` | `int` |  | The number of samples to return for the specified range. |

**Returns:** `Array` — A table of `samples` numbers ranging between -1 and 1 representing the
sampled waveform, or an empty table if a waveform could not be read.

### Method: AudioPlayer:Play

**Signature:** `AudioPlayer:Play(atTime: double?): int64?`

Plays the [AudioPlayer](/docs/reference/engine/classes/AudioPlayer.md) from wherever its
[TimePosition](/docs/reference/engine/classes/AudioPlayer.md) is. Replicates from server
to client. When `atTime` is provided, the action is scheduled against
[GetMixerTime()](/docs/reference/engine/classes/SoundService.md) for sample-accurate,
framerate-independent timing — useful for rhythm games or any scenario
where audio changes must align precisely with a beat.

*Security: None · Thread Safety: Unsafe · Capabilities: Audio*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `atTime` | `double?` |  | A specific time, based on [GetMixerTime](/docs/reference/engine/classes/SoundService.md), that this `AudioPlayer` should begin playing at. |

**Returns:** `int64?` — If `atTime` was provided, a unique ID, which can be passed to
[Cancel()](/docs/reference/engine/classes/AudioPlayer.md).

### Method: AudioPlayer:Stop

**Signature:** `AudioPlayer:Stop(atTime: double?): int64?`

Stops the [AudioPlayer](/docs/reference/engine/classes/AudioPlayer.md) wherever its
[TimePosition](/docs/reference/engine/classes/AudioPlayer.md) is. Replicates from server
to client. When `atTime` is provided, the action is scheduled against
[GetMixerTime()](/docs/reference/engine/classes/SoundService.md) for sample-accurate,
framerate-independent timing, enabling precise beat-synchronized stops or
track transitions.

*Security: None · Thread Safety: Unsafe · Capabilities: Audio*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `atTime` | `double?` |  | A specific time, based on [GetMixerTime](/docs/reference/engine/classes/SoundService.md), that this `AudioPlayer` should stop playing at. |

**Returns:** `int64?` — If `atTime` was provided, a unique ID, which can be passed to
[Cancel()](/docs/reference/engine/classes/AudioPlayer.md).

## Events

### Event: AudioPlayer.Ended

**Signature:** `AudioPlayer.Ended()`

Fires after the [AudioPlayer](/docs/reference/engine/classes/AudioPlayer.md) has completed playback and stopped.
Note this event will **not** fire for audio with
[Looping](/docs/reference/engine/classes/AudioPlayer.md) set to `true` since it continues
playing upon reaching its end. This event will also **not** fire when the
audio is stopped before playback has completed; for this, use
[AudioPlayer:GetPropertyChangedSignal()](/docs/reference/engine/classes/AudioPlayer.md) on the
[IsPlaying](/docs/reference/engine/classes/AudioPlayer.md) property.

This event is often used to destroy an [AudioPlayer](/docs/reference/engine/classes/AudioPlayer.md) when it has
completed playback.

*Security: None · Capabilities: Audio*

### Event: AudioPlayer.Looped

**Signature:** `AudioPlayer.Looped()`

Event that fires after the [AudioPlayer](/docs/reference/engine/classes/AudioPlayer.md) loops. This happens when
the audio reaches the end of its content (or the end of the
[LoopRegion](/docs/reference/engine/classes/AudioPlayer.md) if it is active) and
[Looping](/docs/reference/engine/classes/AudioPlayer.md) is `true`.

This event does **not** fire if the audio is looped manually by changing
its [TimePosition](/docs/reference/engine/classes/AudioPlayer.md).

*Security: None · Capabilities: Audio*

### Event: AudioPlayer.WiringChanged

**Signature:** `AudioPlayer.WiringChanged(connected: boolean, pin: string, wire: Wire, instance: Instance)`

Event that fires after a [Wire](/docs/reference/engine/classes/Wire.md) becomes connected or disconnected,
and that [Wire](/docs/reference/engine/classes/Wire.md) is now or was previously connected to a pin on the
[AudioPlayer](/docs/reference/engine/classes/AudioPlayer.md) and to some other wirable instance.

*Security: None · Capabilities: Audio*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `connected` | `boolean` | Whether the instance got connected or disconnected. |
| `pin` | `string` | The pin on the [AudioPlayer](/docs/reference/engine/classes/AudioPlayer.md) that the [Wire](/docs/reference/engine/classes/Wire.md) targets. |
| `wire` | `Wire` | The [Wire](/docs/reference/engine/classes/Wire.md) between the [AudioPlayer](/docs/reference/engine/classes/AudioPlayer.md) and the other instance. |
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