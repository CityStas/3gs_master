---
name: AudioFilter
last_updated: 2026-10-30T19:55:51Z
inherits:
  - Instance
  - Object
type: class
memory_category: Internal
summary: "Adjusts the frequency content of audio streams."
---

# Class: AudioFilter

> Adjusts the frequency content of audio streams.

## Description

[AudioFilter](/docs/reference/engine/classes/AudioFilter.md) adjusts the frequency content of audio streams. It
provides one **Input** pin and one **Output** pin which can be connected
to/from by [Wires](/docs/reference/engine/classes/Wire.md). [AudioFilter](/docs/reference/engine/classes/AudioFilter.md) uses its
[FilterType](/docs/reference/engine/classes/AudioFilter.md), [Gain](/docs/reference/engine/classes/AudioFilter.md), and
[Q](/docs/reference/engine/classes/AudioFilter.md) properties to determine what to do around a particular
cutoff [Frequency](/docs/reference/engine/classes/AudioFilter.md).

## Code Samples

**Emitter Filtering**

An AudioFilter can be used to change the frequency content of audio streams.
In this example, an AudioFilter is used to make the AudioEmitter output more
muffled when there's a wall between it and the AudioListener.

```lua
-- This assumes the workspace contains a Part with an AudioEmitter and an AudioPlayer, and the camera has an AudioListener
local RunService = game:GetService("RunService")

local part: BasePart = workspace.Part
local camera: Camera = workspace.CurrentCamera
local audioPlayer: AudioPlayer = part.AudioPlayer
local audioEmitter: AudioEmitter = part.AudioEmitter
local audioListener: AudioListener = camera.AudioListener

local raycastParams = RaycastParams.new()
raycastParams.FilterDescendantsInstances = { audioEmitter.Parent }
raycastParams.FilterType = Enum.RaycastFilterType.Exclude

-- Create a new AudioFilter
local filter: AudioFilter = Instance.new("AudioFilter")
filter.FilterType = Enum.AudioFilterType.Lowpass12dB
filter.Frequency = 22000
filter.Q = math.sqrt(2) / 2 -- This Q value produces a flat lowpass for the 12dB slope type
filter.Parent = part

-- Put the AudioFilter between the player and the emitter
local function wireTo(source: Instance, target: Instance): Wire
	local wire = Instance.new("Wire")
	wire.SourceInstance = source
	wire.TargetInstance = target
	wire.Parent = target
end
wireTo(audioPlayer, filter)
wireTo(filter, audioEmitter)

-- Update the filter based on the positions of the emitter and listener
RunService.Heartbeat:Connect(function()
	local emitterPos: Vector3 = part.Position
	local listenerPos: Vector3 = camera.CFrame.Position

	local raycastResult = workspace:Raycast(emitterPos, (listenerPos - emitterPos), raycastParams)
	filter.Frequency = if raycastResult then 500 else 22000
end)
```

## Properties

### Property: AudioFilter.Bypass

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
  "category": "State",
  "capabilities": [
    "Audio"
  ]
}
```

If `true`, audio streams are passed-through unaffected by this effect.

### Property: AudioFilter.FilterType

```json
{
  "type": "AudioFilterType",
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

The type of frequency response curve that will be used to filter the audio
signal. Each type of curve affects the frequency content of the audio in
different ways.

### Property: AudioFilter.Frequency

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

The central frequency in hertz of the curve represented by the filter.
Generally, adjusting this value up or down corresponds to a horizontal
shift in the overall frequency curve. Ranges from 20 to 22000.

### Property: AudioFilter.Gain

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

The gain value in decibels used to determine the volume level of the curve
represented by the filter. Only applies when the
[FilterType](/docs/reference/engine/classes/AudioFilter.md) is `Peak`, `LowShelf`, or `HighShelf`.
Ranges from -30 to 30.

### Property: AudioFilter.Q

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

The quality value used to determine the slope or resonance of the curve
represented by the filter. Only applies when the
[FilterType](/docs/reference/engine/classes/AudioFilter.md) is `Peak`, `Lowpass[x]dB`, `Highpass[x]dB`,
`Bandpass`, or `Notch`. Ranges from 0.1 to 10.

For [FilterType](/docs/reference/engine/classes/AudioFilter.md) values of
[Lowpass12dB](/docs/reference/engine/enums/AudioFilterType.md) and
[Highpass12dB](/docs/reference/engine/enums/AudioFilterType.md), a **Q** value of
`sqrt(2) / 2`, or `0.707`, corresponds to a flat filter at a 12dB/octave
slope.

## Methods

### Method: AudioFilter:GetConnectedWires

**Signature:** `AudioFilter:GetConnectedWires(pin: string): List<Wire>`

Returns an array of [Wires](/docs/reference/engine/classes/Wire.md) that are connected to the specified
pin. [AudioFilter](/docs/reference/engine/classes/AudioFilter.md) has one "Input" pin and one "Output" pin.

*Security: None · Thread Safety: Unsafe · Capabilities: Audio*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `pin` | `string` |  | An input or output pin on this instance |

**Returns:** `List<Wire>` — An array of [Wires](/docs/reference/engine/classes/Wire.md)

### Method: AudioFilter:GetGainAt

**Signature:** `AudioFilter:GetGainAt(frequency: float): float`

Returns the gain value, in decibels, of the frequency response curve
represented by the filter at the given frequency, in hertz. This can be
used to sample the exact shape of the filter in key places or as a whole.

*Security: None · Thread Safety: Unsafe · Capabilities: Audio*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `frequency` | `float` |  | The frequency, in hertz, to sample. |

**Returns:** `float` — The gain value, in decibels, at the given frequency.

### Method: AudioFilter:GetInputPins

**Signature:** `AudioFilter:GetInputPins(): Array`

Gets the list of pins that [Wire](/docs/reference/engine/classes/Wire.md) can use in [Wire.TargetName](/docs/reference/engine/classes/Wire.md)
to connect to this instance via its [Wire.TargetInstance](/docs/reference/engine/classes/Wire.md) property.

For [AudioFilter](/docs/reference/engine/classes/AudioFilter.md), this is `Input` only.

*Security: None · Thread Safety: Unsafe · Capabilities: Audio*

**Returns:** `Array` — An array of strings representing valid pin names.

### Method: AudioFilter:GetOutputPins

**Signature:** `AudioFilter:GetOutputPins(): Array`

Gets the list of pins that [Wire](/docs/reference/engine/classes/Wire.md) can use in [Wire.SourceName](/docs/reference/engine/classes/Wire.md)
to connect to this instance via its [Wire.SourceInstance](/docs/reference/engine/classes/Wire.md) property.

For [AudioFilter](/docs/reference/engine/classes/AudioFilter.md), this is `Output` only.

*Security: None · Thread Safety: Unsafe · Capabilities: Audio*

**Returns:** `Array` — An array of strings representing valid pin names.

## Events

### Event: AudioFilter.WiringChanged

**Signature:** `AudioFilter.WiringChanged(connected: boolean, pin: string, wire: Wire, instance: Instance)`

Event that fires after a [Wire](/docs/reference/engine/classes/Wire.md) becomes connected or disconnected,
and that [Wire](/docs/reference/engine/classes/Wire.md) is now or was previously connected to a pin on the
[AudioFilter](/docs/reference/engine/classes/AudioFilter.md) and to some other wirable instance.

*Security: None · Capabilities: Audio*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `connected` | `boolean` | Whether the instance got connected or disconnected. |
| `pin` | `string` | The pin on the [AudioFilter](/docs/reference/engine/classes/AudioFilter.md) that the [Wire](/docs/reference/engine/classes/Wire.md) targets. |
| `wire` | `Wire` | The [Wire](/docs/reference/engine/classes/Wire.md) between the [AudioFilter](/docs/reference/engine/classes/AudioFilter.md) and the other instance. |
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