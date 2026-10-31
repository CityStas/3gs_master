---
name: AudioRecorder
last_updated: 2026-10-30T19:55:51Z
inherits:
  - Instance
  - Object
type: class
memory_category: Internal
tags:
  - NotBrowsable
summary: "Records audio streams in-experience."
---

# Class: AudioRecorder

> Records audio streams in-experience.

## Description

**This API is in development and is not available yet.**

`AudioRecorder` records audio streams in-experience with a fixed time limit of
60 seconds. The results can be loaded into an [AudioPlayer](/docs/reference/engine/classes/AudioPlayer.md) for
playback.

At this time, [AudioDeviceInput](/docs/reference/engine/classes/AudioDeviceInput.md) cannot be recorded. The
[GetUnrecordableInstancesAsync()](/docs/reference/engine/classes/AudioRecorder.md)
method can be used to check specifically which instances aren't recordable.

## Code Samples

**Audio Recorder**

```lua
local Workspace = game:GetService("Workspace")

local audioRecorder = Instance.new("AudioRecorder")
audioRecorder.Parent = Workspace

local audioPlayer = Instance.new("AudioPlayer")
audioPlayer.Asset = "rbxassetid://5829815715"
audioPlayer.Volume = 0.8
audioPlayer.Parent = Workspace

-- Wire AudioPlayer into the AudioRecorder
local wire1 = Instance.new("Wire")
wire1.SourceInstance = audioPlayer
wire1.TargetInstance = audioRecorder
wire1.Parent = audioRecorder

-- There is no exact way to determine when audio buffer enters in to trigger the recording properly
-- Recording will have pre-head empty silence compared to the original asset
audioPlayer:Play()
audioRecorder:RecordAsync() -- Start recording the AudioPlayer
print("Recording...")
task.wait(5)
audioRecorder:Stop() -- Stop recording
print("Stopped recording!")
audioPlayer:Stop()
audioPlayer.TimePosition = 0

-- Create output to listen the results
local audioOutput = Instance.new("AudioDeviceOutput")
audioOutput.Parent = Workspace
local wire2 = Instance.new("Wire")
wire2.SourceInstance = audioPlayer
wire2.TargetInstance = audioOutput
wire2.Parent = audioOutput

-- Get the recorded content and play it in the AudioPlayer
local resultUri = audioRecorder:GetTemporaryContent().Uri
audioPlayer.Asset = resultUri

if not audioPlayer.IsReady then
	audioPlayer:GetPropertyChangedSignal("IsReady"):Wait()
end

audioPlayer:Play()
```

## Properties

### Property: AudioRecorder.IsRecording

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "None",
    "write": "RobloxEngineSecurity"
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

Returns whether the `AudioRecorder` is currently recording.

### Property: AudioRecorder.TimeLength

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
  "category": "Data",
  "capabilities": [
    "Audio"
  ]
}
```

Returns the current length of the recording in seconds.

## Methods

### Method: AudioRecorder:CanRecordAsync

**Signature:** `AudioRecorder:CanRecordAsync(): boolean`

Returns whether the `AudioRecorder` can currently record. For instance,
this will return `false` if the current recording data has reached the
recording time limit. To clear the recording, use
[Clear()](/docs/reference/engine/classes/AudioRecorder.md).

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Audio*

**Returns:** `boolean` — `true` if recording is possible, `false` otherwise.

### Method: AudioRecorder:Clear

**Signature:** `AudioRecorder:Clear(): ()`

Clears out the recording from the `AudioRecorder`.

*Security: None · Thread Safety: Unsafe · Capabilities: Audio*

**Returns:** `()`

### Method: AudioRecorder:GetConnectedWires

**Signature:** `AudioRecorder:GetConnectedWires(pin: string): List<Wire>`

Returns an array of [Wires](/docs/reference/engine/classes/Wire.md) that are connected to the specified
pin. [AudioRecorder](/docs/reference/engine/classes/AudioRecorder.md) has one "Input" pin.

*Security: None · Thread Safety: Unsafe · Capabilities: Audio*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `pin` | `string` |  | An input or output pin on this instance |

**Returns:** `List<Wire>` — An array of [Wires](/docs/reference/engine/classes/Wire.md)

### Method: AudioRecorder:GetInputPins

**Signature:** `AudioRecorder:GetInputPins(): Array`

Gets the list of pins that [Wire](/docs/reference/engine/classes/Wire.md) can use in [Wire.TargetName](/docs/reference/engine/classes/Wire.md)
to connect to this instance via its [Wire.TargetInstance](/docs/reference/engine/classes/Wire.md) property.

For [AudioRecorder](/docs/reference/engine/classes/AudioRecorder.md), this is `Input` only.

*Security: None · Thread Safety: Unsafe · Capabilities: Audio*

**Returns:** `Array` — An array of strings representing valid pin names.

### Method: AudioRecorder:GetOutputPins

**Signature:** `AudioRecorder:GetOutputPins(): Array`

Gets the list of pins that [Wire](/docs/reference/engine/classes/Wire.md) can use in [Wire.SourceName](/docs/reference/engine/classes/Wire.md)
to connect to this instance via its [Wire.SourceInstance](/docs/reference/engine/classes/Wire.md) property.

For [AudioRecorder](/docs/reference/engine/classes/AudioRecorder.md), there are none.

*Security: None · Thread Safety: Unsafe · Capabilities: Audio*

**Returns:** `Array` — An array of strings representing valid pin names.

### Method: AudioRecorder:GetTemporaryContent

**Signature:** `AudioRecorder:GetTemporaryContent(): Content`

Returns recorded content that can be played back with [AudioPlayer](/docs/reference/engine/classes/AudioPlayer.md).
The content retrieved from this method is only valid in the current
session.

*Security: None · Thread Safety: Unsafe · Capabilities: Audio*

**Returns:** `Content` — A temporary `Content` ID that can be used with [AudioPlayer](/docs/reference/engine/classes/AudioPlayer.md).

### Method: AudioRecorder:GetUnrecordableInstancesAsync

**Signature:** `AudioRecorder:GetUnrecordableInstancesAsync(): List<Instance>`

Traverses the audio graph, starting from this recorder's inputs, to find
unrecordable instances. Currently, [AudioDeviceInput](/docs/reference/engine/classes/AudioDeviceInput.md) is not
recordable.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Audio*

**Returns:** `List<Instance>` — A table of [Instances](/docs/reference/engine/classes/Instance.md) that are not recordable.

### Method: AudioRecorder:RecordAsync

**Signature:** `AudioRecorder:RecordAsync(): ()`

Starts recording audio. If
[CanRecordAsync()](/docs/reference/engine/classes/AudioRecorder.md) returns `true`,
recording begins. If recording cannot begin, this method produces an
error.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Audio*

**Returns:** `()`

### Method: AudioRecorder:Stop

**Signature:** `AudioRecorder:Stop(): ()`

Stops recording audio.

*Security: None · Thread Safety: Unsafe · Capabilities: Audio*

**Returns:** `()`

## Events

### Event: AudioRecorder.WiringChanged

**Signature:** `AudioRecorder.WiringChanged(connected: boolean, pin: string, wire: Wire, instance: Instance)`

Event that fires after a [Wire](/docs/reference/engine/classes/Wire.md) becomes connected or disconnected,
and that [Wire](/docs/reference/engine/classes/Wire.md) is now or was previously connected to a pin on the
[AudioRecorder](/docs/reference/engine/classes/AudioRecorder.md) and to some other wirable instance.

*Security: None · Capabilities: Audio*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `connected` | `boolean` | Whether the instance got connected or disconnected. |
| `pin` | `string` | The pin on the [AudioRecorder](/docs/reference/engine/classes/AudioRecorder.md) that the [Wire](/docs/reference/engine/classes/Wire.md) targets. |
| `wire` | `Wire` | The [Wire](/docs/reference/engine/classes/Wire.md) between the [AudioRecorder](/docs/reference/engine/classes/AudioRecorder.md) and the other instance. |
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