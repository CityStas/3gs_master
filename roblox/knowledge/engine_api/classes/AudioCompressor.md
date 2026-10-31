---
name: AudioCompressor
last_updated: 2026-10-30T19:55:51Z
inherits:
  - Instance
  - Object
type: class
memory_category: Internal
summary: "Adjusts the dynamic range of input streams."
---

# Class: AudioCompressor

> Adjusts the dynamic range of input streams.

## Description

[AudioCompressor](/docs/reference/engine/classes/AudioCompressor.md) adjusts the dynamic range of audio streams. Any
momentary bursts of loudness will be clamped down according to the
compressor's properties.

[AudioCompressor](/docs/reference/engine/classes/AudioCompressor.md) provides **Input** and **Sidechain** pins that can be
targeted by [Wire.TargetName](/docs/reference/engine/classes/Wire.md), and an **Output** pin that can be used by
[Wire.SourceName](/docs/reference/engine/classes/Wire.md).

## Code Samples

**Sidechain Compression**

By using Sidechain compression, the background ambience can be ducked around
an explosion

```lua
local deviceOutput: AudioDeviceOutput = Instance.new("AudioDeviceOutput")
deviceOutput.Parent = workspace
local explosionPlayer: AudioPlayer = Instance.new("AudioPlayer")
explosionPlayer.Parent = workspace
explosionPlayer.AssetId = "rbxassetid://1835333184"

local ambiencePlayer = Instance.new("AudioPlayer")
ambiencePlayer.AssetId = "rbxassetid://9112854440"
local compressor = Instance.new("AudioCompressor")
local wireToCompressor = Instance.new("Wire")
local wireToSidechain = Instance.new("Wire")
local wireToOutput = Instance.new("Wire")

ambiencePlayer.Parent = workspace
compressor.Parent = workspace
wireToCompressor.Parent = workspace
wireToSidechain.Parent = workspace
wireToOutput.Parent = workspace

wireToCompressor.SourceInstance = ambiencePlayer
wireToCompressor.TargetInstance = compressor

wireToSidechain.SourceInstance = explosionPlayer
wireToSidechain.TargetInstance = compressor
wireToSidechain.TargetName = "Sidechain"

wireToOutput.SourceInstance = compressor
wireToOutput.TargetInstance = deviceOutput

ambiencePlayer:Play()
```

## Properties

### Property: AudioCompressor.Attack

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

Time, in seconds, denoting how quickly the compressor will clamp down on
volume after it surpasses [Threshold](/docs/reference/engine/classes/AudioCompressor.md).
Ranges from 0.0001 to 0.5.

### Property: AudioCompressor.Bypass

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

### Property: AudioCompressor.MakeupGain

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

Gain value to be applied after compression, in decibels. After limiting
the dynamic range, the resulting stream may be very quiet and this
property can be used to compensate. Ranges from -30 to 30.

### Property: AudioCompressor.Ratio

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

Ratio of input volume to output volume, to be applied when surpassing
[Threshold](/docs/reference/engine/classes/AudioCompressor.md). For example, a value of 2
will cut the amount by which the input stream exceeds the threshold in
half whenever the input stream does so. Ranges from 1 to 50.

### Property: AudioCompressor.Release

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

Time, in seconds, denoting how quickly the compressor will unclamp after
its stream volume dips back below
[Threshold](/docs/reference/engine/classes/AudioCompressor.md). Ranges from 0.01 to 5.

### Property: AudioCompressor.Threshold

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

Gain value at which the compressor will start to modify the input stream,
in decibels, with a range of -60 to 0. When the input stream's volume
surpasses [Threshold](/docs/reference/engine/classes/AudioCompressor.md), the compressor will
take [Attack](/docs/reference/engine/classes/AudioCompressor.md) seconds to kick in. When the
input stream's volume recedes below
[Threshold](/docs/reference/engine/classes/AudioCompressor.md), the compressor will take
[Release](/docs/reference/engine/classes/AudioCompressor.md) seconds to stop acting.

If any [Wires](/docs/reference/engine/classes/Wire.md) are connected to the **Sidechain** pin of the
compressor, this threshold analyzes those streams instead of the **Input**
streams; this can be used to duck the volume of one stream in response to
another.

## Methods

### Method: AudioCompressor:GetConnectedWires

**Signature:** `AudioCompressor:GetConnectedWires(pin: string): List<Wire>`

Returns an array of [Wires](/docs/reference/engine/classes/Wire.md) that are connected to the specified
pin. [AudioCompressor](/docs/reference/engine/classes/AudioCompressor.md) has one "Input" pin, one "Sidechain" pin, and
one "Output" pin.

*Security: None · Thread Safety: Unsafe · Capabilities: Audio*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `pin` | `string` |  | An input or output pin on this instance |

**Returns:** `List<Wire>` — An array of [Wires](/docs/reference/engine/classes/Wire.md)

### Method: AudioCompressor:GetInputPins

**Signature:** `AudioCompressor:GetInputPins(): Array`

Gets the list of pins that [Wire](/docs/reference/engine/classes/Wire.md) can use in [Wire.TargetName](/docs/reference/engine/classes/Wire.md)
to connect to this instance via its [Wire.TargetInstance](/docs/reference/engine/classes/Wire.md) property.

For [AudioCompressor](/docs/reference/engine/classes/AudioCompressor.md), these are:

- `Input`
- `Sidechain`

*Security: None · Thread Safety: Unsafe · Capabilities: Audio*

**Returns:** `Array` — An array of strings representing valid pin names.

### Method: AudioCompressor:GetOutputPins

**Signature:** `AudioCompressor:GetOutputPins(): Array`

Gets the list of pins that [Wire](/docs/reference/engine/classes/Wire.md) can use in [Wire.SourceName](/docs/reference/engine/classes/Wire.md)
to connect to this instance via its [Wire.SourceInstance](/docs/reference/engine/classes/Wire.md) property.

For [AudioCompressor](/docs/reference/engine/classes/AudioCompressor.md), this is `Output` only.

*Security: None · Thread Safety: Unsafe · Capabilities: Audio*

**Returns:** `Array` — An array of strings representing valid pin names.

## Events

### Event: AudioCompressor.WiringChanged

**Signature:** `AudioCompressor.WiringChanged(connected: boolean, pin: string, wire: Wire, instance: Instance)`

Event that fires after a [Wire](/docs/reference/engine/classes/Wire.md) becomes connected or disconnected,
and that [Wire](/docs/reference/engine/classes/Wire.md) is now or was previously connected to a pin on the
[AudioCompressor](/docs/reference/engine/classes/AudioCompressor.md) and to some other wirable instance.

*Security: None · Capabilities: Audio*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `connected` | `boolean` | Whether the instance got connected or disconnected. |
| `pin` | `string` | The pin on the [AudioCompressor](/docs/reference/engine/classes/AudioCompressor.md) that the [Wire](/docs/reference/engine/classes/Wire.md) targets. |
| `wire` | `Wire` | The [Wire](/docs/reference/engine/classes/Wire.md) between the [AudioCompressor](/docs/reference/engine/classes/AudioCompressor.md) and the other instance. |
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