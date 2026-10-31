---
name: VideoPlayer
last_updated: 2026-10-30T19:55:53Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
tags:
  - NotBrowsable
summary: "Used to play video assets."
---

# Class: VideoPlayer

> Used to play video assets.

## Description

An instance for playing video assets. It can be connected to a
[VideoDisplay](/docs/reference/engine/classes/VideoDisplay.md) via a [Wire](/docs/reference/engine/classes/Wire.md) to show the video and can be connected
to audio instances via a [Wire](/docs/reference/engine/classes/Wire.md) to play the audio track.

## Code Samples

**Video Player (Server Side)**

```lua
-- This should be in a "Script" with RunContext set to "Legacy" or "Server"

-- Create what the video is displayed on
local videoScreenPart = Instance.new("Part")
videoScreenPart.Anchored = true
videoScreenPart.Size = Vector3.new(12, 6, 1)
videoScreenPart.CFrame = CFrame.new(0, 5, 0)
videoScreenPart.Parent = workspace

local videoScreenUI = Instance.new("SurfaceGui")
videoScreenUI.Parent = videoScreenPart

local videoDisplay = Instance.new("VideoDisplay")
videoDisplay.Size = UDim2.new(1, 0, 1, 0)
videoDisplay.Parent = videoScreenUI

-- Create where a video asset originates from
local videoSource = Instance.new("VideoPlayer")
videoSource.VideoContent = Content.fromUri("rbxassetid://5608359401")
videoSource.Looping = true
videoSource.Parent = videoScreenPart

-- Create where the video's audio emits from
local speakerPart = Instance.new("Part")
speakerPart.Anchored = true
speakerPart.Parent = workspace

local audioEmitter = Instance.new("AudioEmitter")
audioEmitter.Parent = speakerPart

-- Create and connect wires so that the video visually renders and emits audio
local videoWire = Instance.new("Wire")
videoWire.SourceInstance = videoSource
videoWire.TargetInstance = videoDisplay
videoWire.Parent = videoSource

local audioWire = Instance.new("Wire")
audioWire.SourceInstance = videoSource
audioWire.TargetInstance = audioEmitter
audioWire.Parent = videoSource

-- Play the video 
-- Note: Playing a video on the server does not guarantee it is loaded or synced for all clients, playing on the client is preferred
videoSource:Play()
```

**Video Player (Client Side)**

```lua
local videoSource = Instance.new("VideoPlayer")
videoSource.VideoContent = Content.fromUri("rbxassetid://5608359401")
videoSource.Parent = script.Parent

-- Play the video after it has loaded
videoSource:GetPropertyChangedSignal("IsLoaded"):Connect(function()
	if videoSource.IsLoaded then
		print("Video has loaded, starting playback in 2 seconds.")
		wait(2)
		videoSource:Play()
	end
end)

-- Load the video to have it ready when we need it
videoSource:LoadAsync()

wait(5)

-- Unload the video to save resources
videoSource:Unload()
```

## Properties

### Property: VideoPlayer.AutoLoadInStudio

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "None",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Debug",
  "capabilities": [
    "Audio",
    "UI"
  ]
}
```

By default, [VideoContent](/docs/reference/engine/classes/VideoPlayer.md) does not load
while in Studio Edit mode and shows no output when wired to
[VideoDisplay](/docs/reference/engine/classes/VideoDisplay.md) to reduce studio memory usage. Toggle this option to
load [VideoContent](/docs/reference/engine/classes/VideoPlayer.md) while in Studio Edit
mode.

### Property: VideoPlayer.AutoPlayInStudio

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "None",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Debug",
  "capabilities": [
    "Audio",
    "UI"
  ]
}
```

Plays the [VideoContent](/docs/reference/engine/classes/VideoPlayer.md) while in Studio
Edit mode. [AutoLoadInStudio](/docs/reference/engine/classes/VideoPlayer.md) must be
on for this option to show.

### Property: VideoPlayer.IsLoaded

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
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Asset",
  "capabilities": [
    "Audio",
    "UI"
  ]
}
```

This property is true when the
[VideoContent](/docs/reference/engine/classes/VideoPlayer.md) has loaded and is ready to
play.

### Property: VideoPlayer.IsPlaying

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
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Playback",
  "capabilities": [
    "Audio",
    "UI"
  ]
}
```

Denotes whether this [VideoPlayer](/docs/reference/engine/classes/VideoPlayer.md) is currently playing. This
property is read-only, but replicates. To play and pause a
[VideoPlayer](/docs/reference/engine/classes/VideoPlayer.md) at runtime, use the [Play()](/docs/reference/engine/classes/VideoPlayer.md)
and [Pause()](/docs/reference/engine/classes/VideoPlayer.md) methods.

### Property: VideoPlayer.Looping

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
    "Audio",
    "UI"
  ]
}
```

Controls whether this [VideoPlayer](/docs/reference/engine/classes/VideoPlayer.md) loops after reaching the end of
its [TimeLength](/docs/reference/engine/classes/VideoPlayer.md).

### Property: VideoPlayer.PlaybackSpeed

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
    "Audio",
    "UI"
  ]
}
```

Multiplier that controls how quickly the video plays, directly controlling
the perceived pitch of the audio track. Ranges from 0 to 1.

### Property: VideoPlayer.Resolution

```json
{
  "type": "Vector2",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Asset",
  "capabilities": [
    "Audio",
    "UI"
  ]
}
```

This property gets the original source resolution of the
[VideoContent](/docs/reference/engine/classes/VideoPlayer.md) file.

### Property: VideoPlayer.TimeLength

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
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Asset",
  "capabilities": [
    "Audio",
    "UI"
  ]
}
```

This property indicates the length of the
[VideoContent](/docs/reference/engine/classes/VideoPlayer.md) in seconds. If the video is
not loaded, this value is 0.

### Property: VideoPlayer.TimePosition

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
    "Audio",
    "UI"
  ]
}
```

This property indicates the progress in seconds of the
[VideoContent](/docs/reference/engine/classes/VideoPlayer.md). It can be changed to move
the playback position of the video both before and during playback.

### Property: VideoPlayer.VideoContent

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
    "Audio",
    "UI"
  ]
}
```

The content ID of the video file a [VideoPlayer](/docs/reference/engine/classes/VideoPlayer.md) object is
associated with. To save resources and improve performance, call the
[Unload()](/docs/reference/engine/classes/VideoPlayer.md) method to unload the
[VideoContent](/docs/reference/engine/classes/VideoPlayer.md) when the [VideoPlayer](/docs/reference/engine/classes/VideoPlayer.md)
is not visible or in use.

### Property: VideoPlayer.Volume

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
    "Audio",
    "UI"
  ]
}
```

Volume level, which is multiplied onto the output audio stream,
controlling how loudly the audio track plays. Ranges from 0 to 3.

### Property: VideoPlayer.MaximumResolution *(hidden)*

```json
{
  "type": "VideoSampleSize",
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
    "Audio",
    "UI",
    "InternalTest"
  ]
}
```

The maximum resolution, as an [VideoSampleSize](/docs/reference/engine/enums/VideoSampleSize.md) value, that the video
decoder produces when playing this [VideoPlayer](/docs/reference/engine/classes/VideoPlayer.md). Defaults to
[VideoSampleSize.Full](/docs/reference/engine/enums/VideoSampleSize.md), which doesn't limit the decoded resolution.
Lower [VideoSampleSize](/docs/reference/engine/enums/VideoSampleSize.md) values reduce the resolution the decoder
outputs, which can lower memory usage on constrained devices.

## Methods

### Method: VideoPlayer:GetConnectedWires

**Signature:** `VideoPlayer:GetConnectedWires(pin: string): List<Wire>`

Returns an array of [Wires](/docs/reference/engine/classes/Wire.md) that are connected to the specified
pin. [VideoPlayer](/docs/reference/engine/classes/VideoPlayer.md) has one "Output" pin.

*Security: None · Thread Safety: Unsafe · Capabilities: Audio, UI*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `pin` | `string` |  | An input or output pin on this instance |

**Returns:** `List<Wire>` — An array of [Wires](/docs/reference/engine/classes/Wire.md)

### Method: VideoPlayer:GetInputPins

**Signature:** `VideoPlayer:GetInputPins(): Array`

Gets the list of pins that [Wire](/docs/reference/engine/classes/Wire.md) can use in [Wire.TargetName](/docs/reference/engine/classes/Wire.md)
to connect to this instance via its [Wire.TargetInstance](/docs/reference/engine/classes/Wire.md) property.

For [VideoPlayer](/docs/reference/engine/classes/VideoPlayer.md), there are none.

*Security: None · Thread Safety: Unsafe · Capabilities: Audio, UI*

**Returns:** `Array` — An array of strings representing valid pin names.

### Method: VideoPlayer:GetOutputPins

**Signature:** `VideoPlayer:GetOutputPins(): Array`

Gets the list of pins that [Wire](/docs/reference/engine/classes/Wire.md) can use in [Wire.SourceName](/docs/reference/engine/classes/Wire.md)
to connect to this instance via its [Wire.SourceInstance](/docs/reference/engine/classes/Wire.md) property.

For [VideoPlayer](/docs/reference/engine/classes/VideoPlayer.md), this is `Output` only.

*Security: None · Thread Safety: Unsafe · Capabilities: Audio, UI*

**Returns:** `Array` — An array of strings representing valid pin names.

### Method: VideoPlayer:LoadAsync

**Signature:** `VideoPlayer:LoadAsync(): AssetFetchStatus`

[VideoContent](/docs/reference/engine/classes/VideoPlayer.md) is typically only loaded
when [Play()](/docs/reference/engine/classes/VideoPlayer.md) is called, causing some buffering
delay. This function can preload
[VideoContent](/docs/reference/engine/classes/VideoPlayer.md) so that it can be
immediately played when [Play()](/docs/reference/engine/classes/VideoPlayer.md) is called.
Loading videos can consume a significant amount of device memory.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Audio, UI*

**Returns:** `AssetFetchStatus` — An [AssetFetchStatus](/docs/reference/engine/enums/AssetFetchStatus.md) describing the outcome of the load —
[AssetFetchStatus.Success](/docs/reference/engine/enums/AssetFetchStatus.md) once the
[VideoContent](/docs/reference/engine/classes/VideoPlayer.md) has loaded, or a failure
status such as [AssetFetchStatus.Failure](/docs/reference/engine/enums/AssetFetchStatus.md) or
[AssetFetchStatus.TimedOut](/docs/reference/engine/enums/AssetFetchStatus.md) if it could not be fetched.

### Method: VideoPlayer:Pause

**Signature:** `VideoPlayer:Pause(): ()`

Pauses the [VideoPlayer](/docs/reference/engine/classes/VideoPlayer.md) wherever its
[TimePosition](/docs/reference/engine/classes/VideoPlayer.md) is. Replicates from server
to client.

*Security: None · Thread Safety: Unsafe · Capabilities: Audio, UI*

**Returns:** `()`

### Method: VideoPlayer:Play

**Signature:** `VideoPlayer:Play(): ()`

Plays the [VideoPlayer](/docs/reference/engine/classes/VideoPlayer.md) from wherever its
[TimePosition](/docs/reference/engine/classes/VideoPlayer.md) is. Replicates from server
to client. To save resources and improve performance, call the
[Unload()](/docs/reference/engine/classes/VideoPlayer.md) method to unload the
[VideoContent](/docs/reference/engine/classes/VideoPlayer.md) when the [VideoPlayer](/docs/reference/engine/classes/VideoPlayer.md)
is not visible or in use.

*Security: None · Thread Safety: Unsafe · Capabilities: Audio, UI*

**Returns:** `()`

### Method: VideoPlayer:Unload

**Signature:** `VideoPlayer:Unload(): ()`

Unloads the [VideoContent](/docs/reference/engine/classes/VideoPlayer.md) to save
resources. After calling this method, the
[IsLoaded](/docs/reference/engine/classes/VideoPlayer.md) property is false, and the
[TimePosition](/docs/reference/engine/classes/VideoPlayer.md) resets to 0. To play the
video again, the [LoadAsync()](/docs/reference/engine/classes/VideoPlayer.md) or
[Play()](/docs/reference/engine/classes/VideoPlayer.md) method must be called to reload the
video.

*Security: None · Thread Safety: Unsafe · Capabilities: Audio, UI*

**Returns:** `()`

## Events

### Event: VideoPlayer.DidEnd

**Signature:** `VideoPlayer.DidEnd()`

Fires after the [VideoPlayer](/docs/reference/engine/classes/VideoPlayer.md) has completed playback and stopped.
Note this event does **not** fire for videos with
[Looped](/docs/reference/engine/classes/VideoPlayer.md) set to `true` since it continues playing
upon reaching its end. This event also does **not** fire when the video is
stopped before playback has completed; for this, use
[VideoPlayer:GetPropertyChangedSignal()](/docs/reference/engine/classes/VideoPlayer.md) on the
[IsPlaying](/docs/reference/engine/classes/VideoPlayer.md) property.

*Security: None · Capabilities: Audio, UI*

### Event: VideoPlayer.DidLoop

**Signature:** `VideoPlayer.DidLoop()`

Event that fires after the [VideoPlayer](/docs/reference/engine/classes/VideoPlayer.md) loops. This happens when
the video reaches the end of its content. This event does **not** fire if
the video is looped manually by changing its
[TimePosition](/docs/reference/engine/classes/VideoPlayer.md).

*Security: None · Capabilities: Audio, UI*

### Event: VideoPlayer.PlayFailed

**Signature:** `VideoPlayer.PlayFailed(error: AssetFetchStatus)`

Fires when the [VideoPlayer](/docs/reference/engine/classes/VideoPlayer.md) fails to load or play its
[VideoContent](/docs/reference/engine/classes/VideoPlayer.md). The `error` parameter is an
[AssetFetchStatus](/docs/reference/engine/enums/AssetFetchStatus.md) value that describes why the content couldn't be
fetched.

*Security: None · Capabilities: Audio, UI*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `error` | `AssetFetchStatus` | An [AssetFetchStatus](/docs/reference/engine/enums/AssetFetchStatus.md) value describing why the [VideoContent](/docs/reference/engine/classes/VideoPlayer.md) failed to load. |

### Event: VideoPlayer.WiringChanged

**Signature:** `VideoPlayer.WiringChanged(connected: boolean, pin: string, wire: Wire, instance: Instance)`

Event that fires after a [Wire](/docs/reference/engine/classes/Wire.md) becomes connected or disconnected,
and that [Wire](/docs/reference/engine/classes/Wire.md) is now or was previously connected to a pin on the
[VideoPlayer](/docs/reference/engine/classes/VideoPlayer.md) and to some other wirable instance.

*Security: None · Capabilities: Audio, UI*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `connected` | `boolean` | Whether the instance was connected or disconnected. |
| `pin` | `string` | The pin on the [VideoPlayer](/docs/reference/engine/classes/VideoPlayer.md) that the [Wire](/docs/reference/engine/classes/Wire.md) targets. |
| `wire` | `Wire` | The [Wire](/docs/reference/engine/classes/Wire.md) between the [VideoPlayer](/docs/reference/engine/classes/VideoPlayer.md) and the other instance. |
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