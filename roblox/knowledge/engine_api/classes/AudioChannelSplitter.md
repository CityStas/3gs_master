---
name: AudioChannelSplitter
last_updated: 2026-10-30T19:55:51Z
inherits:
  - Instance
  - Object
type: class
memory_category: Internal
summary: "Splits an audio stream into component channels so that each can be processed independently."
---

# Class: AudioChannelSplitter

> Splits an audio stream into component channels so that each can be processed
> independently.

## Description

[AudioChannelSplitter](/docs/reference/engine/classes/AudioChannelSplitter.md) splits an audio stream into component channels so
that each can be processed independently. It provides one **Input** pin, one
combined **Output** pin, as well as the following secondary output pins, all
of which can be connected to/from by [Wires](/docs/reference/engine/classes/Wire.md): **Left**, **Right**,
**Center**, **SurroundLeft**, **SurroundRight**, **Sub**, **BackLeft**,
**BackRight**, **TopLeft**, **TopRight**, **TopBackLeft**, and
**TopBackRight**.

![Diagram showing position of all potential channels.](/assets/engine-api/enums/AudioChannelLayout/Surround_7_1_4.jpg)

## Code Samples

**Splitting & Mixing Channels**

```lua
local Workspace = game:GetService("Workspace")

local function wireUp(source: Instance, target: Instance, sourceName: string?, targetName: string?)
	local wire = Instance.new("Wire", source)
	wire.SourceInstance = source
	wire.TargetInstance = target

	if sourceName then
		wire.SourceName = sourceName
	end
	if targetName then
		wire.TargetName = targetName
	end

	return wire
end

local listener = Instance.new("AudioListener")
listener.Parent = Workspace.CurrentCamera
local output = Instance.new("AudioDeviceOutput")
output.Parent = Workspace

local splitter = Instance.new("AudioChannelSplitter")
splitter.Parent = Workspace
local mixer = Instance.new("AudioChannelMixer")
mixer.Parent = Workspace

-- Send what the listener hears to a splitter and send a mix to the final output
wireUp(listener, splitter)
wireUp(mixer, output)

-- Set up both the splitter and mixer to use a quadrophonic layout
splitter.Layout = Enum.AudioChannelLayout.Quad
mixer.Layout = Enum.AudioChannelLayout.Quad

-- Give each of the four channels its own pitch shifter
local frontLeft = Instance.new("AudioPitchShifter")
frontLeft.Name = "Front Left"
frontLeft.Pitch = 1.25
frontLeft.Parent = Workspace
local backLeft = Instance.new("AudioPitchShifter")
backLeft.Name = "Back Left"
backLeft.Pitch = 0.5
backLeft.Parent = Workspace
local frontRight = Instance.new("AudioPitchShifter")
frontRight.Name = "Front Right"
frontRight.Pitch = 1.5
frontRight.Parent = Workspace
local backRight = Instance.new("AudioPitchShifter")
backRight.Name = "Back Right"
backRight.Pitch = 0.75
backRight.Parent = Workspace

wireUp(splitter, frontLeft, "Left")
wireUp(splitter, backLeft, "BackLeft")
wireUp(splitter, frontRight, "Right")
wireUp(splitter, backRight, "BackRight")

wireUp(frontLeft, mixer, nil, "Left")
wireUp(backLeft, mixer, nil, "BackLeft")
wireUp(frontRight, mixer, nil, "Right")
wireUp(backRight, mixer, nil, "BackRight")

-- Configure a part to emit audio
local part = Instance.new("Part")
part.Shape = Enum.PartType.Ball
part.Size = Vector3.new(4, 4, 4)
part.Material = Enum.Material.SmoothPlastic
part.CastShadow = false
part.Position = Vector3.new(0, 4, -12)
part.Anchored = true
part.Parent = Workspace

local analyzer = Instance.new("AudioAnalyzer")
analyzer.Parent = part
local emitter = Instance.new("AudioEmitter")
emitter.Parent = part
local assetPlayer = Instance.new("AudioPlayer")
assetPlayer.Looping = true
assetPlayer.Asset = "rbxassetid://97799489309320"
assetPlayer.Parent = emitter

wireUp(assetPlayer, emitter)
wireUp(assetPlayer, analyzer)

-- Start playing the audio
assetPlayer:Play()

-- Adjust the part's color as the audio plays
while true do
	local peak = math.sqrt(analyzer.PeakLevel)
	part.Color = Color3.new(peak, peak, peak)
	task.wait()
end
```

## Properties

### Property: AudioChannelSplitter.Layout

```json
{
  "type": "AudioChannelLayout",
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

Controls the input channel layout to be split from. When changed, all
audio streams prior to this channel splitter's input may need to be
up-mixed (widened to at least as many channels as the input requires).

The **Output** pin produces a copy of the stream wired to **Input** but,
depending on the value of [AudioChannelSplitter.Layout](/docs/reference/engine/classes/AudioChannelSplitter.md):

- For [Mono](/docs/reference/engine/enums/AudioChannelLayout.md), the **Center** pin produces an
  audio stream.
- For [Stereo](/docs/reference/engine/enums/AudioChannelLayout.md), the **Left** and **Right**
  pins produce audio streams.
- For [Quad](/docs/reference/engine/enums/AudioChannelLayout.md), the **Left**, **Right**,
  **BackLeft**, and **BackRight** pins produce audio streams.
- [Surround_5](/docs/reference/engine/enums/AudioChannelLayout.md) is the same as `Quad`,
  plus **Center** produces an audio stream.
- [Surround_5_1](/docs/reference/engine/enums/AudioChannelLayout.md) is the same as
  `Surround_5`, plus **Sub** produces an audio stream.
- [Surround_7_1](/docs/reference/engine/enums/AudioChannelLayout.md) is the same as
  `Surround_5_1`, plus **SurroundLeft** and **SurroundRight** produce
  audio streams.
- For [Surround_7_1_4](/docs/reference/engine/enums/AudioChannelLayout.md), all
  secondary output pins produce audio streams.

## Methods

### Method: AudioChannelSplitter:GetConnectedWires

**Signature:** `AudioChannelSplitter:GetConnectedWires(pin: string): List<Wire>`

Returns an array of [Wires](/docs/reference/engine/classes/Wire.md) that are connected to the specified
pin. For [AudioChannelSplitter](/docs/reference/engine/classes/AudioChannelSplitter.md), this can be one "Input" pin or a
number of output pins - see [AudioChannelSplitter.GetInputPins](/docs/reference/engine/classes/AudioChannelSplitter.md) for
a full list.

*Security: None · Thread Safety: Unsafe · Capabilities: Audio*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `pin` | `string` |  | An input or output pin on this instance |

**Returns:** `List<Wire>` — An array of [Wires](/docs/reference/engine/classes/Wire.md)

### Method: AudioChannelSplitter:GetInputPins

**Signature:** `AudioChannelSplitter:GetInputPins(): Array`

Gets the list of pins that [Wire](/docs/reference/engine/classes/Wire.md) can use in [Wire.TargetName](/docs/reference/engine/classes/Wire.md)
to connect to this instance via its [Wire.TargetInstance](/docs/reference/engine/classes/Wire.md) property.

For [AudioChannelSplitter](/docs/reference/engine/classes/AudioChannelSplitter.md), this is `Input` only.

*Security: None · Thread Safety: Unsafe · Capabilities: Audio*

**Returns:** `Array` — An array of strings representing valid pin names.

### Method: AudioChannelSplitter:GetOutputPins

**Signature:** `AudioChannelSplitter:GetOutputPins(): Array`

Gets the list of pins that [Wire](/docs/reference/engine/classes/Wire.md) can use in [Wire.SourceName](/docs/reference/engine/classes/Wire.md)
to connect to this instance via its [Wire.SourceInstance](/docs/reference/engine/classes/Wire.md) property.

For [AudioChannelSplitter](/docs/reference/engine/classes/AudioChannelSplitter.md), these are:

- `"Output"`
- `"Left"`
- `"Right"`
- `"Center"`
- `"SurroundLeft"`
- `"SurroundRight"`
- `"BackLeft"`
- `"BackRight"`
- `"Sub"`
- `"TopLeft"`
- `"TopRight"`
- `"TopBackLeft"`
- `"TopBackRight"`

*Security: None · Thread Safety: Unsafe · Capabilities: Audio*

**Returns:** `Array` — An array of strings representing valid pin names.

## Events

### Event: AudioChannelSplitter.WiringChanged

**Signature:** `AudioChannelSplitter.WiringChanged(connected: boolean, pin: string, wire: Wire, instance: Instance)`

Event that fires after a [Wire](/docs/reference/engine/classes/Wire.md) becomes connected or disconnected,
and that [Wire](/docs/reference/engine/classes/Wire.md) is now or was previously connected to a pin on the
[AudioChannelSplitter](/docs/reference/engine/classes/AudioChannelSplitter.md) and to some other wirable instance.

*Security: None · Capabilities: Audio*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `connected` | `boolean` | Whether the instance got connected or disconnected. |
| `pin` | `string` | The pin on the [AudioChannelSplitter](/docs/reference/engine/classes/AudioChannelSplitter.md) that the [Wire](/docs/reference/engine/classes/Wire.md) targets. |
| `wire` | `Wire` | The [Wire](/docs/reference/engine/classes/Wire.md) between the [AudioChannelSplitter](/docs/reference/engine/classes/AudioChannelSplitter.md) and the other instance. |
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