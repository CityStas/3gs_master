---
name: AudioSpeechToText
last_updated: 2026-10-30T19:55:51Z
inherits:
  - Instance
  - Object
type: class
memory_category: Internal
summary: "Converts spoken audio into text."
---

# Class: AudioSpeechToText

> Converts spoken audio into text.

## Description

[AudioSpeechToText](/docs/reference/engine/classes/AudioSpeechToText.md) is used to convert speech audio into text. This
class provides a single **Input** pin that can be connected to other pins via
[Wires](/docs/reference/engine/classes/Wire.md).

Roblox uses the following formula to throttle requests for this API based on
the number of players in your experience:
`max requests per minute per experience = 1 + (5 * number_of_concurrent_users)`.
You can purchase additional usage using
[Extended Services](/docs/en-us/cloud-services/extended-services.md).

For more information, see
[Speech-to-text](/docs/en-us/audio/objects.md#speech-to-text).

## Code Samples

**Convert speech to text**

On character spawn, adds an [AudioSpeechToText](/docs/reference/engine/classes/AudioSpeechToText.md) instance and puts its
output into a new [TextLabel](/docs/reference/engine/classes/TextLabel.md). This script should be used in a
[LocalScript](/docs/reference/engine/classes/LocalScript.md) or a [Script](/docs/reference/engine/classes/Script.md) with
[RunContext](/docs/reference/engine/classes/BaseScript.md) set to [RunContext.Client](/docs/reference/engine/enums/RunContext.md).

```lua
local players = game:GetService("Players")
local function connect(src: Instance, dst: Instance)
	local wire = Instance.new("Wire", dst)
	wire.SourceInstance = src
	wire.TargetInstance = dst
end
local textLabel = nil
local stt = nil
local function onCharacterSpawned(player: Player, character: Model)
	local input = Instance.new("AudioDeviceInput", player)
	input.Player = player
	local audioSpeechToText = Instance.new("AudioSpeechToText", character)
	audioSpeechToText.Enabled = true
	connect(player.AudioDeviceInput, audioSpeechToText)
	local screenGui = Instance.new("ScreenGui", player.PlayerGui)
	textLabel = Instance.new("TextLabel", screenGui)
	textLabel.Text = "Hello!"
	textLabel.Size = UDim2.fromOffset(160,90)
	textLabel.Position = UDim2.fromOffset(20,20)
	textLabel.BackgroundTransparency = 0
	textLabel.FontFace.Weight = Enum.FontWeight.Bold
	textLabel.TextColor3 = Color3.new(1,1,1)
	textLabel.TextStrokeColor3 = Color3.new(0,0,0)
	textLabel.TextStrokeTransparency = 0.5
	audioSpeechToText:GetPropertyChangedSignal("Text"):Connect(function()
		if audioSpeechToText.Text ~= '' then
			print(audioSpeechToText.Text)
			textLabel.Text = audioSpeechToText.Text
			audioSpeechToText.Text = ''
		end
	end)
	stt = audioSpeechToText
end
local function onPlayerAdded(player: Player)
	if player.Character then
		onCharacterSpawned(player, player.Character)
	end
	player.CharacterAdded:Connect(function()
		onCharacterSpawned(player, player.Character)
	end)
end
players.PlayerAdded:Connect(onPlayerAdded)
for _, player in players:GetPlayers() do
	onPlayerAdded(player)
end
local vad = false
while true do
	wait(0.1)
	if stt and textLabel then
		if(stt.VoiceDetected ~= vad) then
			vad = stt.VoiceDetected
			print(vad)
			if(vad) then
				textLabel.BackgroundColor3 = Color3.new(0.7,0,0)
			else
				textLabel.BackgroundColor3 = Color3.new(0,0,0)
			end
		end
	end
end
```

## Properties

### Property: AudioSpeechToText.Enabled

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

Whether the [AudioSpeechToText](/docs/reference/engine/classes/AudioSpeechToText.md) object is enabled for processing
input audio into text.

### Property: AudioSpeechToText.Text

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
  "category": "State",
  "capabilities": [
    "Audio"
  ]
}
```

The text resulting from the conversion of speech audio.

### Property: AudioSpeechToText.VoiceDetected

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
  "category": "State",
  "capabilities": [
    "Audio"
  ]
}
```

Whether the [AudioSpeechToText](/docs/reference/engine/classes/AudioSpeechToText.md) object is detecting speech in the
incoming audio signal. [AudioSpeechToText](/docs/reference/engine/classes/AudioSpeechToText.md) records the speech audio
until it ceases or until a maximum amount of 10 seconds has been recorded.
Then it converts the recorded audio into text.

## Methods

### Method: AudioSpeechToText:GetConnectedWires

**Signature:** `AudioSpeechToText:GetConnectedWires(pin: string): List<Wire>`

Returns an array of [Wires](/docs/reference/engine/classes/Wire.md) that are connected to the specified
pin. [AudioSpeechToText](/docs/reference/engine/classes/AudioSpeechToText.md) has one "Input" pin.

*Security: None · Thread Safety: Unsafe · Capabilities: Audio*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `pin` | `string` |  | An input or output pin on this instance |

**Returns:** `List<Wire>` — An array of [Wires](/docs/reference/engine/classes/Wire.md)

### Method: AudioSpeechToText:GetInputPins

**Signature:** `AudioSpeechToText:GetInputPins(): Array`

Gets the list of pins that a [Wire](/docs/reference/engine/classes/Wire.md) can use in
[Wire.TargetName](/docs/reference/engine/classes/Wire.md) to connect to this instance via its
[Wire.TargetInstance](/docs/reference/engine/classes/Wire.md) property.

For [AudioSpeechToText](/docs/reference/engine/classes/AudioSpeechToText.md), this is `Input` only.

*Security: None · Thread Safety: Unsafe · Capabilities: Audio*

**Returns:** `Array` — An array of strings representing valid pin names.

### Method: AudioSpeechToText:GetOutputPins

**Signature:** `AudioSpeechToText:GetOutputPins(): Array`

Gets the list of pins that a [Wire](/docs/reference/engine/classes/Wire.md) can use in
[Wire.SourceName](/docs/reference/engine/classes/Wire.md) to connect to this instance via its
[Wire.SourceInstance](/docs/reference/engine/classes/Wire.md) property.

For [AudioSpeechToText](/docs/reference/engine/classes/AudioSpeechToText.md), there are none.

*Security: None · Thread Safety: Unsafe · Capabilities: Audio*

**Returns:** `Array` — An array of strings representing valid pin names.

## Events

### Event: AudioSpeechToText.WiringChanged

**Signature:** `AudioSpeechToText.WiringChanged(connected: boolean, pin: string, wire: Wire, instance: Instance)`

Event that fires after a [Wire](/docs/reference/engine/classes/Wire.md) becomes connected or disconnected,
and that [Wire](/docs/reference/engine/classes/Wire.md) is now or was previously connected to a pin on the
[AudioSpeechToText](/docs/reference/engine/classes/AudioSpeechToText.md) and to some other wirable instance.

*Security: None · Capabilities: Audio*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `connected` | `boolean` | Whether the instance got connected or disconnected. |
| `pin` | `string` | The pin on the [AudioSpeechToText](/docs/reference/engine/classes/AudioSpeechToText.md) that the [Wire](/docs/reference/engine/classes/Wire.md) targets. |
| `wire` | `Wire` | The [Wire](/docs/reference/engine/classes/Wire.md) between the [AudioSpeechToText](/docs/reference/engine/classes/AudioSpeechToText.md) and the other instance. |
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