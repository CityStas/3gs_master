---
name: VideoFrame
last_updated: 2026-10-30T19:55:53Z
inherits:
  - GuiObject
  - GuiBase2d
  - GuiBase
  - Instance
  - Object
type: class
memory_category: Gui
summary: "A GUI object that renders a rectangle, like a Frame does, with a moving video image."
---

# Class: VideoFrame

> A GUI object that renders a rectangle, like a [Frame](/docs/reference/engine/classes/Frame.md) does, with a
> moving video image.

## Description

A VideoFrame renders a rectangle, like a [Frame](/docs/reference/engine/classes/Frame.md) does, with a moving
video image. The video must be from a file uploaded to the Roblox website.

The video is scaled to fit the entirety of the rectangle, but looks best when
displayed at its native resolution.

## 2D and 3D Sound

A VideoFrame placed underneath [SurfaceGui](/docs/reference/engine/classes/SurfaceGui.md) on a [BasePart](/docs/reference/engine/classes/BasePart.md) will
emit its sound from that part's [BasePart.Position](/docs/reference/engine/classes/BasePart.md).

A VideoFrame exhibits the Doppler effect, meaning its frequency and pitch
varies with the relative motion of whatever part it is attached to.

The volume of the VideoFrame will be determined by the distance between the
client's sound listener (by default the [Camera](/docs/reference/engine/classes/Camera.md) position) and the
position of the VideoFrame's part.

A VideoFrame is considered **"global"** if it is not placed underneath
SurfaceGui on a BasePart. In this case, the sound will play at the same volume
throughout the entire place.

## Code Samples

**Creating and Playing a Video**

The code sample below demonstrates how to create and play a `VideoFrame` with
some valid asset ID after the video has loaded.

```lua
local screenPart = Instance.new("Part")
screenPart.Parent = workspace

local surfaceGui = Instance.new("SurfaceGui")
surfaceGui.Parent = screenPart

local videoFrame = Instance.new("VideoFrame")
videoFrame.Parent = surfaceGui

videoFrame.Looped = true
videoFrame.Video = "rbxassetid://" -- add an asset ID to this

while not videoFrame.IsLoaded do
	task.wait()
end

videoFrame:Play()
```

## Properties

### Property: VideoFrame.IsLoaded

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
  "category": "Video",
  "capabilities": [
    "Audio",
    "UI"
  ]
}
```

This property will be true when the [VideoFrame.Video](/docs/reference/engine/classes/VideoFrame.md) has loaded
from Roblox servers and is ready to play.

### Property: VideoFrame.Looped

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
  "category": "Video",
  "capabilities": [
    "Audio",
    "UI"
  ]
}
```

This property sets whether or not the [VideoFrame.Video](/docs/reference/engine/classes/VideoFrame.md) repeats
once it has finished when it is playing.

### Property: VideoFrame.Playing

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
  "category": "Video",
  "capabilities": [
    "Audio",
    "UI"
  ]
}
```

This property indicates whether the [VideoFrame.Video](/docs/reference/engine/classes/VideoFrame.md) is currently
playing. It can be set to start or pause playback as an alternative to the
[VideoFrame:Play()](/docs/reference/engine/classes/VideoFrame.md) and [VideoFrame:Pause()](/docs/reference/engine/classes/VideoFrame.md) functions.

### Property: VideoFrame.Resolution

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
  "category": "Video",
  "capabilities": [
    "Audio",
    "UI"
  ]
}
```

This property gets the original source resolution of the
[VideoFrame.Video](/docs/reference/engine/classes/VideoFrame.md) file.

### Property: VideoFrame.RollOffMaxDistance

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
  "category": "Video",
  "capabilities": [
    "Audio",
    "UI"
  ]
}
```

The maximum distance, in studs, a client's listener can be from the
[VideoFrame](/docs/reference/engine/classes/VideoFrame.md)'s part and still hear its audio. Defaults to `10000`.

This property only affects playback when the [VideoFrame](/docs/reference/engine/classes/VideoFrame.md) is 3D, as
described in the class's "2D and 3D Sound" section; it has no effect on a
global [VideoFrame](/docs/reference/engine/classes/VideoFrame.md). How `RollOffMaxDistance` affects the
attenuation of the sound depends on the
[RollOffMode](/docs/reference/engine/classes/VideoFrame.md) property.

### Property: VideoFrame.RollOffMinDistance

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
  "category": "Video",
  "capabilities": [
    "Audio",
    "UI"
  ]
}
```

The minimum distance, in studs, at which the [VideoFrame](/docs/reference/engine/classes/VideoFrame.md)'s audio
begins to attenuate (decrease in volume). Defaults to `1`.

This property only affects playback when the [VideoFrame](/docs/reference/engine/classes/VideoFrame.md) is 3D, as
described in the class's "2D and 3D Sound" section; it has no effect on a
global [VideoFrame](/docs/reference/engine/classes/VideoFrame.md). How `RollOffMinDistance` affects the
attenuation of the sound depends on the
[RollOffMode](/docs/reference/engine/classes/VideoFrame.md) property.

### Property: VideoFrame.RollOffMode

```json
{
  "type": "RollOffMode",
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
  "category": "Video",
  "capabilities": [
    "Audio",
    "UI"
  ]
}
```

Controls how the volume of the [VideoFrame](/docs/reference/engine/classes/VideoFrame.md)'s audio attenuates
(fades out) as the distance between the listener and the video's part
changes. Defaults to [RollOffMode.Inverse](/docs/reference/engine/enums/RollOffMode.md).

This property only affects playback when the [VideoFrame](/docs/reference/engine/classes/VideoFrame.md) is 3D, as
described in the class's "2D and 3D Sound" section; it has no effect on a
global [VideoFrame](/docs/reference/engine/classes/VideoFrame.md). For details on the different modes, see
[RollOffMode](/docs/reference/engine/enums/RollOffMode.md).

### Property: VideoFrame.TimeLength

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
  "category": "Video",
  "capabilities": [
    "Audio",
    "UI"
  ]
}
```

This property indicates the length of the [VideoFrame.Video](/docs/reference/engine/classes/VideoFrame.md) in
seconds. If the video is not loaded, this value will be 0.

### Property: VideoFrame.TimePosition

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
  "category": "Video",
  "capabilities": [
    "Audio",
    "UI"
  ]
}
```

This property indicates the progress in seconds of the
[VideoFrame.Video](/docs/reference/engine/classes/VideoFrame.md). It can be changed to move the playback position
of the video both before and during playback.

### Property: VideoFrame.Video

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
  "category": "Video",
  "capabilities": [
    "Audio",
    "UI"
  ]
}
```

The content ID of the video file a [VideoFrame](/docs/reference/engine/classes/VideoFrame.md) object is associated
with. To save resources and improve performance, set this property to `""`
when the [VideoFrame](/docs/reference/engine/classes/VideoFrame.md) is not visible or in use.

**Creating and Playing a Video**

The code sample below demonstrates how to create and play a `VideoFrame` with
some valid asset ID after the video has loaded.

```lua
local screenPart = Instance.new("Part")
screenPart.Parent = workspace

local surfaceGui = Instance.new("SurfaceGui")
surfaceGui.Parent = screenPart

local videoFrame = Instance.new("VideoFrame")
videoFrame.Parent = surfaceGui

videoFrame.Looped = true
videoFrame.Video = "rbxassetid://" -- add an asset ID to this

while not videoFrame.IsLoaded do
	task.wait()
end

videoFrame:Play()
```

### Property: VideoFrame.VideoContent

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
  "category": "Video",
  "capabilities": [
    "Audio",
    "UI"
  ]
}
```

The video content a [VideoFrame](/docs/reference/engine/classes/VideoFrame.md) object is associated with. Setting
this property is equivalent to setting [Video](/docs/reference/engine/classes/VideoFrame.md), and
reading it returns a content ID equal to [Video](/docs/reference/engine/classes/VideoFrame.md).

When referencing a video by content ID, build the value with the
corresponding [Content](/docs/reference/engine/datatypes/Content.md) constructor:
[Content.fromAssetId()](/docs/reference/engine/datatypes/Content.md) for a numeric asset ID, or
[Content.fromUri()](/docs/reference/engine/datatypes/Content.md) for an `rbxassetid://` URI.

Unlike [Video](/docs/reference/engine/classes/VideoFrame.md), which only accepts a content ID
string, `VideoContent` can also hold a direct reference to a
[VideoCapture](/docs/reference/engine/classes/VideoCapture.md) object, such as one retrieved through
[CaptureService:ReadCapturesFromGalleryAsync()](/docs/reference/engine/classes/CaptureService.md). This lets a local
screen recording play back on the `VideoFrame` without first uploading it
to Roblox. Build the value with [Content.fromObject()](/docs/reference/engine/datatypes/Content.md), for
example `videoFrame.VideoContent = Content.fromObject(capture)`.

### Property: VideoFrame.Volume

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
  "category": "Video",
  "capabilities": [
    "Audio",
    "UI"
  ]
}
```

This property determines how loud the [VideoFrame.Video](/docs/reference/engine/classes/VideoFrame.md) plays back.
It can be set to a number between 0 and 100.

### Property: VideoFrame.MaximumResolution *(hidden)*

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
  "category": "Video",
  "capabilities": [
    "Audio",
    "UI",
    "InternalTest"
  ]
}
```

Internal-only. Caps the resolution the video is allowed to stream at, as
an [VideoSampleSize](/docs/reference/engine/enums/VideoSampleSize.md) rather than exact pixel dimensions.

The video may still stream below the cap on a slow connection. Defaults to
[VideoSampleSize.Full](/docs/reference/engine/enums/VideoSampleSize.md).

## Methods

### Method: VideoFrame:Pause

**Signature:** `VideoFrame:Pause(): ()`

Sets [VideoFrame.Playing](/docs/reference/engine/classes/VideoFrame.md) to `false`, pausing playback if the
[VideoFrame.Video](/docs/reference/engine/classes/VideoFrame.md) is playing.

As [VideoFrame.TimePosition](/docs/reference/engine/classes/VideoFrame.md) is not reset, when the video is resumed
it will continue from its previous position.

*Security: None · Thread Safety: Unsafe · Capabilities: Audio, UI*

**Returns:** `()`

### Method: VideoFrame:Play

**Signature:** `VideoFrame:Play(): ()`

Sets [VideoFrame.Playing](/docs/reference/engine/classes/VideoFrame.md) to `true`, playing the
[VideoFrame.Video](/docs/reference/engine/classes/VideoFrame.md) from the current [VideoFrame.TimePosition](/docs/reference/engine/classes/VideoFrame.md).
To save resources and improve performance, set the
[VideoFrame.Video](/docs/reference/engine/classes/VideoFrame.md) property to `""` when the [VideoFrame](/docs/reference/engine/classes/VideoFrame.md) is
not visible or in use.

*Security: None · Thread Safety: Unsafe · Capabilities: Audio, UI*

**Returns:** `()`

**Creating and Playing a Video**

The code sample below demonstrates how to create and play a `VideoFrame` with
some valid asset ID after the video has loaded.

```lua
local screenPart = Instance.new("Part")
screenPart.Parent = workspace

local surfaceGui = Instance.new("SurfaceGui")
surfaceGui.Parent = screenPart

local videoFrame = Instance.new("VideoFrame")
videoFrame.Parent = surfaceGui

videoFrame.Looped = true
videoFrame.Video = "rbxassetid://" -- add an asset ID to this

while not videoFrame.IsLoaded do
	task.wait()
end

videoFrame:Play()
```

## Events

### Event: VideoFrame.DidLoop

**Signature:** `VideoFrame.DidLoop(video: string)`

An event that fires whenever the [VideoFrame.Video](/docs/reference/engine/classes/VideoFrame.md) loops. Returns
the content ID of the video.

*Security: None · Capabilities: Audio, UI*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `video` | `string` | The content ID of the video that looped. |

### Event: VideoFrame.Ended

**Signature:** `VideoFrame.Ended(video: string)`

This event fires when the [VideoFrame.Video](/docs/reference/engine/classes/VideoFrame.md) has completed playback
and stopped.

*Security: None · Capabilities: Audio, UI*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `video` | `string` | The content ID of the paused that ended. |

### Event: VideoFrame.Loaded

**Signature:** `VideoFrame.Loaded(video: string)`

This event fires when the [VideoFrame.Video](/docs/reference/engine/classes/VideoFrame.md) is loaded.

*Security: None · Capabilities: Audio, UI*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `video` | `string` | The content ID of the loaded video. |

### Event: VideoFrame.Paused

**Signature:** `VideoFrame.Paused(video: string)`

This event fires whenever the [VideoFrame.Video](/docs/reference/engine/classes/VideoFrame.md) is paused using
[VideoFrame:Pause()](/docs/reference/engine/classes/VideoFrame.md) or by setting [VideoFrame.Playing](/docs/reference/engine/classes/VideoFrame.md) to
false.

*Security: None · Capabilities: Audio, UI*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `video` | `string` | The content ID of the paused video. |

### Event: VideoFrame.Played

**Signature:** `VideoFrame.Played(video: string)`

This event fires whenever the [VideoFrame.Video](/docs/reference/engine/classes/VideoFrame.md) is played using the
[VideoFrame:Play()](/docs/reference/engine/classes/VideoFrame.md) function or by setting
[VideoFrame.Playing](/docs/reference/engine/classes/VideoFrame.md) to true.

*Security: None · Capabilities: Audio, UI*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `video` | `string` | The content ID of the played video. |

## Inherited Members

### From [GuiObject](/docs/reference/engine/classes/GuiObject.md)

- **Property `Active`** (`boolean`): Determines whether this UI element sinks input.
- **Property `AnchorPoint`** (`Vector2`): Determines the origin point of a GuiObject, relative to its
- **Property `AutomaticSize`** (`AutomaticSize`): Determines whether resizing occurs based on child content.
- **Property `BackgroundColor`** (`BrickColor`): Determines the color of the GuiObject background. *(deprecated, hidden)*
- **Property `BackgroundColor3`** (`Color3`): Determines the GuiObject background color.
- **Property `BackgroundTransparency`** (`float`): Determines the transparency of the GuiObject background and
- **Property `BorderColor`** (`BrickColor`): Determines the color of the GuiObject border. *(deprecated, hidden)*
- **Property `BorderColor3`** (`Color3`): Determines the color of the GuiObject border.
- **Property `BorderMode`** (`BorderMode`): Determines in what manner the GuiObject border is laid out
- **Property `BorderSizePixel`** (`int`): Determines the pixel width of the GuiObject border.
- **Property `ClipsDescendants`** (`boolean`): Determines if descendant GuiObjects outside of the
- **Property `Draggable`** (`boolean`): Determines whether a GuiObject (and its descendants) can be *(deprecated)*
- **Property `GuiState`** (`GuiState`): Determines whether the player's mouse is being actively pressed on the
- **Property `InputSink`** (`InputSink`): Controls whether, and how, the GuiObject sinks input that occurs
- **Property `Interactable`** (`boolean`): Determines whether the GuiButton can be interacted with or not, or
- **Property `LayoutOrder`** (`int`): Controls the sort order of the GuiObject when used with a
- **Property `NextSelectionDown`** (`GuiObject`): Sets the GuiObject which will be selected when the gamepad
- **Property `NextSelectionLeft`** (`GuiObject`): Sets the GuiObject which will be selected when the gamepad
- **Property `NextSelectionRight`** (`GuiObject`): Sets the GuiObject which will be selected when the gamepad
- **Property `NextSelectionUp`** (`GuiObject`): Sets the GuiObject which will be selected when the gamepad
- **Property `Position`** (`UDim2`): Determines the pixel and scalar position of the GuiObject.
- **Property `Rotation`** (`float`): Determines the number of degrees by which the GuiObject is
- **Property `Selectable`** (`boolean`): Determine whether the GuiObject can be selected by a gamepad.
- **Property `SelectionImageObject`** (`GuiObject`): Overrides the default selection adornment used for gamepads.
- **Property `SelectionOrder`** (`int`): The order of GuiObjects selected by the gamepad UI
- **Property `Size`** (`UDim2`): Determines the pixel and scalar size of the GuiObject.
- **Property `SizeConstraint`** (`SizeConstraint`): Sets the Size axes that the GuiObject will
- **Property `Transparency`** (`float`): A mixed property of *(deprecated, hidden)*
- **Property `Visible`** (`boolean`): Determines whether the GuiObject and its descendants will be
- **Property `ZIndex`** (`int`): Determines the order in which a GuiObject renders relative to
- **Method `TweenPosition(endPosition: UDim2, easingDirection?: EasingDirection, easingStyle?: EasingStyle, time?: float, override?: boolean, callback?: Function): boolean`**: Smoothly moves a GUI to a new UDim2. *(deprecated)*
- **Method `TweenSize(endSize: UDim2, easingDirection?: EasingDirection, easingStyle?: EasingStyle, time?: float, override?: boolean, callback?: Function): boolean`**: Smoothly resizes a GuiObject to a new UDim2. *(deprecated)*
- **Method `TweenSizeAndPosition(endSize: UDim2, endPosition: UDim2, easingDirection?: EasingDirection, easingStyle?: EasingStyle, time?: float, override?: boolean, callback?: Function): boolean`**: Smoothly moves a GUI to a new size and position. *(deprecated)*
- **Event `DragBegin`**: Fired when a player begins dragging the object. *(deprecated)*
- **Event `DragStopped`**: Fired when a player stops dragging the object. *(deprecated)*
- **Event `InputBegan`**: Fired when a user begins interacting via a Human-Computer Interface device
- **Event `InputChanged`**: Fired when a user changes how they're interacting via a Human-Computer
- **Event `InputEnded`**: Fired when a user stops interacting via a Human-Computer Interface device
- **Event `MouseEnter`**: Fires when a user moves their mouse into a GUI element.
- **Event `MouseLeave`**: Fires when a user moves their mouse out of a GUI element.
- **Event `MouseMoved`**: Fires whenever a user moves their mouse while it is inside a GUI element.
- **Event `MouseWheelBackward`**: Fires when a user scrolls their mouse wheel back when the mouse is over a
- **Event `MouseWheelForward`**: Fires when a user scrolls their mouse wheel forward when the mouse is over
- **Event `SelectionGained`**: Fired when the GuiObject is being focused on with the Gamepad selector.
- **Event `SelectionLost`**: Fired when the Gamepad selector stops focusing on the GuiObject.
- **Event `TouchLongPress`**: Fires when the player starts, continues and stops long-pressing the UI
- **Event `TouchPan`**: Fires when the player moves their finger on the UI element.
- **Event `TouchPinch`**: Fires when the player performs a pinch or pull gesture using two fingers
- **Event `TouchRotate`**: Fires when the player performs a rotation gesture using two fingers on the
- **Event `TouchSwipe`**: Fires when the player performs a swipe gesture on the UI element.
- **Event `TouchTap`**: Fires when the player performs a tap gesture on the UI element.

### From [GuiBase2d](/docs/reference/engine/classes/GuiBase2d.md)

- **Property `AbsolutePosition`** (`Vector2`): Describes the actual screen position of a GuiBase2d element, in
- **Property `AbsoluteRotation`** (`float`): Describes the actual screen rotation of a GuiBase2d element, in
- **Property `AbsoluteSize`** (`Vector2`): Describes the actual screen size of a GuiBase2d element, in
- **Property `AutoLocalize`** (`boolean`): When set to `true`, localization will be applied to this GuiBase2d
- **Property `Localize`** (`boolean`): Automatically set to true when a localization table's *(deprecated, hidden)*
- **Property `RootLocalizationTable`** (`LocalizationTable`): A reference to a LocalizationTable to be used to apply automated
- **Property `SelectionBehaviorDown`** (`SelectionBehavior`): Customizes gamepad selection behavior in the down direction.
- **Property `SelectionBehaviorLeft`** (`SelectionBehavior`): Customizes gamepad selection behavior in the left direction.
- **Property `SelectionBehaviorRight`** (`SelectionBehavior`): Customizes gamepad selection behavior in the right direction.
- **Property `SelectionBehaviorUp`** (`SelectionBehavior`): Customizes gamepad selection behavior in the up direction.
- **Property `SelectionGroup`** (`boolean`): Allows customization of gamepad selection movement.
- **Event `SelectionChanged`**: Fires when the gamepad selection moves to, leaves, or changes within the

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