---
name: AudioEqualizer
last_updated: 2026-10-30T19:55:51Z
inherits:
  - Instance
  - Object
type: class
memory_category: Internal
summary: "Adjusts the frequency content of audio streams."
---

# Class: AudioEqualizer

> Adjusts the frequency content of audio streams.

## Description

[AudioEqualizer](/docs/reference/engine/classes/AudioEqualizer.md) adjusts the frequency content of audio streams. It
provides one **Input** pin and one **Output** pin which can be connected
to/from by [Wires](/docs/reference/engine/classes/Wire.md). [AudioEqualizer](/docs/reference/engine/classes/AudioEqualizer.md) has 3 frequency bands
whose gain values can be controlled, and the crossover points between bands
can be moved.

## Code Samples

**Listener Equalization**

An AudioEqualizer can be used to change the frequency content of audio
streams. This can be done before emission, or after listening, and can be used
to implement your own, custom RollOff logic! In this example, we use an
AudioEqualizer to make an AudioPlayer's high frequencies more muffled as the
AudioListener looks away from the AudioEmitter. We also reduce both the low
and high frequencies as the listener gets further away.

```lua
local function wireUp(source: Instance, target: Instance): Wire
	local wire = Instance.new("Wire")
	wire.Parent = target
	wire.SourceInstance = source
	wire.TargetInstance = target
	return wire
end

local function getCFrameFrom(inst: Instance): CFrame?
	local parent = inst.Parent
	if not parent then
		return nil
	elseif parent:IsA("Model") then
		return parent.WorldPivot
	elseif parent:IsA("BasePart") then
		return parent.CFrame
	elseif parent:IsA("Attachment") then
		return parent.WorldCFrame
	elseif parent:IsA("Camera") then
		return parent.CFrame
	else
		return nil
	end
end

local function rescale(value: number, oldRange: NumberRange, newRange: NumberRange): number
	local clamped = math.clamp(value, oldRange.Min, oldRange.Max)
	local normalized = clamped - oldRange.Min / (oldRange.Max - oldRange.Min)
	return normalized * (newRange.Max - newRange.Min) + newRange.Min
end

local assetPlayer = Instance.new("AudioPlayer")
assetPlayer.AssetId = "rbxassetid://142376088"
assetPlayer.Parent = workspace

local equalizer = Instance.new("AudioEqualizer")
equalizer.MidRange = NumberRange.new(400, 3000)
equalizer.Parent = workspace

local emitterPart = Instance.new("Part")
emitterPart.Anchored = true
emitterPart.Position = Vector3.new(0, 5, 0)
emitterPart.Parent = workspace

local emitter = Instance.new("AudioEmitter")
emitter.Parent = emitterPart

local listener = Instance.new("AudioListener")
listener.Parent = workspace.CurrentCamera

local output = Instance.new("AudioDeviceOutput")
output.Parent = workspace

wireUp(assetPlayer, equalizer)
wireUp(equalizer, emitter)
wireUp(listener, output)

assetPlayer.Looping = true
assetPlayer:Play()

while true do
	local emitterFrame = getCFrameFrom(emitter)
	local listenerFrame = getCFrameFrom(listener)
	if emitterFrame and listenerFrame then
		local towardEmitter = emitterFrame.Position - listenerFrame.Position
		local look = towardEmitter.Unit:Dot(listenerFrame.LookVector) -- ranges from [-1, 1]
		look = rescale(look, NumberRange.new(-1, 1), NumberRange.new(-20, 0))

		local distance = math.max(towardEmitter.Magnitude, 1)
		local rolloff = 1 / distance -- ranges from [0, 1]
		rolloff = rescale(rolloff, NumberRange.new(0, 1), NumberRange.new(-10, 10))

		equalizer.HighGain = look + rolloff
		equalizer.LowGain = rolloff
	end
	task.wait()
end
```

## Properties

### Property: AudioEqualizer.Bypass

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

### Property: AudioEqualizer.HighGain

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

Gain value, in decibels, to be applied to the frequency content of the
highest band in the equalizer. Ranges from -80 to 10.

### Property: AudioEqualizer.LowGain

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

Gain value, in decibels, to be applied to the frequency content of the
lowest band in the equalizer. Ranges from -80 to 10.

### Property: AudioEqualizer.MidGain

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

Gain value, in decibels, to be applied to the frequency content of the
middle band in the equalizer. Ranges from -80 to 10.

### Property: AudioEqualizer.MidRange

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
  "category": "State",
  "capabilities": [
    "Audio"
  ]
}
```

The frequency range in hertz of the band influenced by
[MidGain](/docs/reference/engine/classes/AudioEqualizer.md). The lower value of the range
determines the crossover frequency between the low and mid bands. The
higher value of the range determines the crossover frequency between the
mid and high bands. Both crossover frequencies range from 200 to 20,000.

## Methods

### Method: AudioEqualizer:GetConnectedWires

**Signature:** `AudioEqualizer:GetConnectedWires(pin: string): List<Wire>`

Returns an array of [Wires](/docs/reference/engine/classes/Wire.md) that are connected to the specified
pin. [AudioEqualizer](/docs/reference/engine/classes/AudioEqualizer.md) has one "Input" pin and one "Output" pin.

*Security: None · Thread Safety: Unsafe · Capabilities: Audio*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `pin` | `string` |  | An input or output pin on this instance |

**Returns:** `List<Wire>` — An array of [Wires](/docs/reference/engine/classes/Wire.md)

### Method: AudioEqualizer:GetInputPins

**Signature:** `AudioEqualizer:GetInputPins(): Array`

Gets the list of pins that [Wire](/docs/reference/engine/classes/Wire.md) can use in [Wire.TargetName](/docs/reference/engine/classes/Wire.md)
to connect to this instance via its [Wire.TargetInstance](/docs/reference/engine/classes/Wire.md) property.

For [AudioEqualizer](/docs/reference/engine/classes/AudioEqualizer.md), this is `Input` only.

*Security: None · Thread Safety: Unsafe · Capabilities: Audio*

**Returns:** `Array` — An array of strings representing valid pin names.

### Method: AudioEqualizer:GetOutputPins

**Signature:** `AudioEqualizer:GetOutputPins(): Array`

Gets the list of pins that [Wire](/docs/reference/engine/classes/Wire.md) can use in [Wire.SourceName](/docs/reference/engine/classes/Wire.md)
to connect to this instance via its [Wire.SourceInstance](/docs/reference/engine/classes/Wire.md) property.

For [AudioEqualizer](/docs/reference/engine/classes/AudioEqualizer.md), this is `Output` only.

*Security: None · Thread Safety: Unsafe · Capabilities: Audio*

**Returns:** `Array` — An array of strings representing valid pin names.

## Events

### Event: AudioEqualizer.WiringChanged

**Signature:** `AudioEqualizer.WiringChanged(connected: boolean, pin: string, wire: Wire, instance: Instance)`

Event that fires after a [Wire](/docs/reference/engine/classes/Wire.md) becomes connected or disconnected,
and that [Wire](/docs/reference/engine/classes/Wire.md) is now or was previously connected to a pin on the
[AudioEqualizer](/docs/reference/engine/classes/AudioEqualizer.md) and to some other wirable instance.

*Security: None · Capabilities: Audio*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `connected` | `boolean` | Whether the instance got connected or disconnected. |
| `pin` | `string` | The pin on the [AudioEqualizer](/docs/reference/engine/classes/AudioEqualizer.md) that the [Wire](/docs/reference/engine/classes/Wire.md) targets. |
| `wire` | `Wire` | The [Wire](/docs/reference/engine/classes/Wire.md) between the [AudioEqualizer](/docs/reference/engine/classes/AudioEqualizer.md) and the other instance. |
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