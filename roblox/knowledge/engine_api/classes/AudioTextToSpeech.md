---
name: AudioTextToSpeech
last_updated: 2026-10-30T19:55:51Z
inherits:
  - Instance
  - Object
type: class
memory_category: Internal
summary: "Plays text as speech audio."
---

# Class: AudioTextToSpeech

> Plays text as speech audio.

## Description

[AudioTextToSpeech](/docs/reference/engine/classes/AudioTextToSpeech.md) is used to play text as speech audio. It provides a
single **Output** pin which can be connected to other pins via
[Wires](/docs/reference/engine/classes/Wire.md).

Roblox uses the following formula to throttle requests for this API based on
the number of players in your experience:
`max requests per minute per experience = 1 + (6 * number_of_concurrent_users)`.
You can purchase additional usage using
[Extended Services](/docs/en-us/cloud-services/extended-services.md).

There is also a client-side throttle of 4 requests per second per user.

For a more in-depth look, see
[Text-to-speech](/docs/en-us/audio/objects.md#text-to-speech).

## Code Samples

**Outputting Text as Speech**

```lua
local audioTextToSpeech: AudioTextToSpeech = Instance.new("AudioTextToSpeech")
audioTextToSpeech.Parent = workspace
audioTextToSpeech.Text = "Hello! Converting text into speech is fun!"
audioTextToSpeech.VoiceId = "1"

local deviceOutput = Instance.new("AudioDeviceOutput")
deviceOutput.Parent = workspace

local wire = Instance.new("Wire")
wire.Parent = workspace

wire.SourceInstance = audioTextToSpeech
wire.TargetInstance = deviceOutput

local count = 0

local connection = nil
connection = audioTextToSpeech.Ended:Connect(function()
	audioTextToSpeech.Text = "I can count to " .. count .. " because I am very smart"
	audioTextToSpeech.VoiceId = "2"
	audioTextToSpeech.TimePosition = 0
	audioTextToSpeech:Play()

	count += 1

	if count > 10 then
		connection:Disconnect()
	end
end)

audioTextToSpeech:Play()
```

## Properties

### Property: AudioTextToSpeech.AutoLocalize

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

When set to `true`, [AudioTextToSpeech.Text](/docs/reference/engine/classes/AudioTextToSpeech.md) is automatically
translated into the player's language and routed to the most appropriate
[AudioTextToSpeech.VoiceId](/docs/reference/engine/classes/AudioTextToSpeech.md). For example, if a female voice ID is
used in English, Roblox routes to a female voice for other languages.

Text-to-speech currently supports automatic translation between the
following languages:

- Arabic
- Chinese (Mandarin)
- English
- French
- German
- Hindi
- Italian
- Japanese
- Korean
- Portuguese
- Spanish

Defaults to `true`.

### Property: AudioTextToSpeech.IsLoaded

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

Denotes whether the [AudioTextToSpeech](/docs/reference/engine/classes/AudioTextToSpeech.md) object is loaded, buffered,
and ready to play. Although uncommon, [AudioTextToSpeech](/docs/reference/engine/classes/AudioTextToSpeech.md) objects
may have their assets unloaded at runtime if there is extreme memory
pressure, in which case [IsLoaded](/docs/reference/engine/classes/AudioTextToSpeech.md) will
become false.

### Property: AudioTextToSpeech.IsPlaying

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

Denotes whether the [AudioTextToSpeech](/docs/reference/engine/classes/AudioTextToSpeech.md) object is currently playing.
This property is read-only, but replicates. To play and stop an
[AudioTextToSpeech](/docs/reference/engine/classes/AudioTextToSpeech.md) object at runtime, use the
[Play()](/docs/reference/engine/classes/AudioTextToSpeech.md) and
[Pause()](/docs/reference/engine/classes/AudioTextToSpeech.md) methods.

### Property: AudioTextToSpeech.Looping

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

Controls whether the [AudioTextToSpeech](/docs/reference/engine/classes/AudioTextToSpeech.md) object loops when exceeding
the end of its [TimeLength](/docs/reference/engine/classes/AudioTextToSpeech.md).

### Property: AudioTextToSpeech.Pitch

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
  "category": "Asset",
  "capabilities": [
    "Audio"
  ]
}
```

A value in musical semitones. The pitch of the generated speech audio is
shifted from its default value by `AudioTextToSpeech.Pitch` semitones.
Ranges from -12.0 to 12.0.

### Property: AudioTextToSpeech.PlaybackSpeed

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
  "category": "Playback",
  "capabilities": [
    "Audio"
  ]
}
```

Multiplier controlling how quickly the speech audio will be played,
directly controlling its perceived pitch. Ranges from 0 to 20.

### Property: AudioTextToSpeech.Speed

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
  "category": "Asset",
  "capabilities": [
    "Audio"
  ]
}
```

Multiplier controlling the speed of the generated speech audio. Ranges
from 0.5 to 2.0.

### Property: AudioTextToSpeech.Text

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
  "category": "Asset",
  "capabilities": [
    "Audio"
  ]
}
```

The text to be converted into speech audio by [AudioTextToSpeech](/docs/reference/engine/classes/AudioTextToSpeech.md).
The text has a maximum length of 300 characters.

### Property: AudioTextToSpeech.TimeLength

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

Denotes the generated speech audio in seconds.

### Property: AudioTextToSpeech.TimePosition

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
generated speech audio, in seconds.

### Property: AudioTextToSpeech.VoiceId

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
  "category": "Asset",
  "capabilities": [
    "Audio"
  ]
}
```

The voice style to be used by [AudioTextToSpeech](/docs/reference/engine/classes/AudioTextToSpeech.md). A list of
available voices and their corresponding VoiceIds can be found in the
[list of artificial voices](/docs/en-us/audio/objects.md#list-of-artificial-voices).

Roblox automatically translates [AudioTextToSpeech.Text](/docs/reference/engine/classes/AudioTextToSpeech.md) into the
player's language and routes it to an appropriate voice when
[AudioTextToSpeech.AutoLocalize](/docs/reference/engine/classes/AudioTextToSpeech.md) is `true`.

### Property: AudioTextToSpeech.Volume

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
how loudly the generated speech audio will be played. Ranges from 0 to 3.

## Methods

### Method: AudioTextToSpeech:GetConnectedWires

**Signature:** `AudioTextToSpeech:GetConnectedWires(pin: string): List<Wire>`

Returns an array of [Wires](/docs/reference/engine/classes/Wire.md) that are connected to the specified
pin. [AudioTextToSpeech](/docs/reference/engine/classes/AudioTextToSpeech.md) has one "Output" pin.

*Security: None · Thread Safety: Unsafe · Capabilities: Audio*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `pin` | `string` |  | An input or output pin on this instance |

**Returns:** `List<Wire>` — An array of [Wires](/docs/reference/engine/classes/Wire.md)

### Method: AudioTextToSpeech:GetInputPins

**Signature:** `AudioTextToSpeech:GetInputPins(): Array`

Gets the list of pins that a [Wire](/docs/reference/engine/classes/Wire.md) can use in
[Wire.TargetName](/docs/reference/engine/classes/Wire.md) to connect to this instance via its
[Wire.TargetInstance](/docs/reference/engine/classes/Wire.md) property.

For [AudioTextToSpeech](/docs/reference/engine/classes/AudioTextToSpeech.md), there are none.

*Security: None · Thread Safety: Unsafe · Capabilities: Audio*

**Returns:** `Array` — An array of strings representing valid pin names.

### Method: AudioTextToSpeech:GetOutputPins

**Signature:** `AudioTextToSpeech:GetOutputPins(): Array`

Gets the list of pins that a [Wire](/docs/reference/engine/classes/Wire.md) can use in
[Wire.SourceName](/docs/reference/engine/classes/Wire.md) to connect to this instance via its
[Wire.SourceInstance](/docs/reference/engine/classes/Wire.md) property.

For [AudioTextToSpeech](/docs/reference/engine/classes/AudioTextToSpeech.md), this is `Output` only.

*Security: None · Thread Safety: Unsafe · Capabilities: Audio*

**Returns:** `Array` — An array of strings representing valid pin names.

### Method: AudioTextToSpeech:GetWaveformAsync

**Signature:** `AudioTextToSpeech:GetWaveformAsync(timeRange: NumberRange, samples: int): Array`

Returns a sampling of the waveform data for the generated text-to-speech
audio. This can be used to check the volume of the audio over the course
of its duration without playing it.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Audio*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `timeRange` | `NumberRange` |  | The start and end time (in seconds) of the segment to read. |
| `samples` | `int` |  | The number of samples to return for the specified range. |

**Returns:** `Array` — A table of `samples` numbers ranging between -1 and 1 representing the
sampled waveform,

### Method: AudioTextToSpeech:LoadAsync

**Signature:** `AudioTextToSpeech:LoadAsync(): AssetFetchStatus`

A blocking call that begins the generation of speech audio based on the
current parameters. It will yield until the speech generation either
completes or fails. Status is returned by an AssetFetchStatus value.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Audio*

**Returns:** `AssetFetchStatus` — An [AssetFetchStatus](/docs/reference/engine/enums/AssetFetchStatus.md) — [Success](/docs/reference/engine/enums/AssetFetchStatus.md)
once the speech audio has been generated, or
[Failure](/docs/reference/engine/enums/AssetFetchStatus.md) if generation could not be
completed.

### Method: AudioTextToSpeech:Pause

**Signature:** `AudioTextToSpeech:Pause(): ()`

Pauses the [AudioTextToSpeech](/docs/reference/engine/classes/AudioTextToSpeech.md) object wherever its
[TimePosition](/docs/reference/engine/classes/AudioTextToSpeech.md) is. Replicates from
server to client.

*Security: None · Thread Safety: Unsafe · Capabilities: Audio*

**Returns:** `()`

### Method: AudioTextToSpeech:Play

**Signature:** `AudioTextToSpeech:Play(): ()`

Plays the [AudioTextToSpeech](/docs/reference/engine/classes/AudioTextToSpeech.md) from wherever its
[TimePosition](/docs/reference/engine/classes/AudioTextToSpeech.md) is. Replicates from
server to client.

*Security: None · Thread Safety: Unsafe · Capabilities: Audio*

**Returns:** `()`

### Method: AudioTextToSpeech:Unload

**Signature:** `AudioTextToSpeech:Unload(): ()`

Frees resources by unloading the generated speech audio.

*Security: None · Thread Safety: Unsafe · Capabilities: Audio*

**Returns:** `()`

## Events

### Event: AudioTextToSpeech.Ended

**Signature:** `AudioTextToSpeech.Ended()`

Fires after the [AudioTextToSpeech](/docs/reference/engine/classes/AudioTextToSpeech.md) object has completed playback
and paused. Note this event will **not** fire for audio with
[Looped](/docs/reference/engine/classes/AudioTextToSpeech.md) set to `true` since it continues
playing upon reaching its end. This event will also **not** fire when the
audio is paused before playback has completed; for this, use
[AudioTextToSpeech:GetPropertyChangedSignal()](/docs/reference/engine/classes/AudioTextToSpeech.md) on the
[IsPlaying](/docs/reference/engine/classes/AudioTextToSpeech.md) property.

This event may be used to destroy an [AudioTextToSpeech](/docs/reference/engine/classes/AudioTextToSpeech.md) object when
it has completed playback.

*Security: None · Capabilities: Audio*

### Event: AudioTextToSpeech.Looped

**Signature:** `AudioTextToSpeech.Looped()`

Event that fires after the [AudioTextToSpeech](/docs/reference/engine/classes/AudioTextToSpeech.md) object loops. This
happens when the audio reaches the end of its content and
[Looping](/docs/reference/engine/classes/AudioTextToSpeech.md) is `true`.

This event does **not** fire if the audio is looped manually by changing
its [TimePosition](/docs/reference/engine/classes/AudioTextToSpeech.md).

*Security: None · Capabilities: Audio*

### Event: AudioTextToSpeech.WiringChanged

**Signature:** `AudioTextToSpeech.WiringChanged(connected: boolean, pin: string, wire: Wire, instance: Instance)`

Event that fires after a [Wire](/docs/reference/engine/classes/Wire.md) becomes connected or disconnected,
and that [Wire](/docs/reference/engine/classes/Wire.md) is now or was previously connected to a pin on the
[AudioTextToSpeech](/docs/reference/engine/classes/AudioTextToSpeech.md) and to some other wirable instance.

*Security: None · Capabilities: Audio*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `connected` | `boolean` | Whether the instance got connected or disconnected. |
| `pin` | `string` | The pin on the [AudioTextToSpeech](/docs/reference/engine/classes/AudioTextToSpeech.md) that the [Wire](/docs/reference/engine/classes/Wire.md) targets. |
| `wire` | `Wire` | The [Wire](/docs/reference/engine/classes/Wire.md) between the [AudioTextToSpeech](/docs/reference/engine/classes/AudioTextToSpeech.md) and the other instance. |
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