---
name: ImageButton
last_updated: 2026-10-30T19:55:52Z
inherits:
  - GuiButton
  - GuiObject
  - GuiBase2d
  - GuiBase
  - Instance
  - Object
type: class
memory_category: Gui
summary: "A 2D user interface element that displays an interactive image."
---

# Class: ImageButton

> A 2D user interface element that displays an interactive image.

## Description

An [ImageButton](/docs/reference/engine/classes/ImageButton.md) behaves similarly to an [ImageLabel](/docs/reference/engine/classes/ImageLabel.md) in regards
to rendering, with the additional behaviors of a [GuiButton](/docs/reference/engine/classes/GuiButton.md).

## Properties

### Property: ImageButton.HoverImage

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
  "category": "Image",
  "capabilities": [
    "UI"
  ]
}
```

A texture ID that will be used when the [ImageButton](/docs/reference/engine/classes/ImageButton.md) is being
hovered.

### Property: ImageButton.HoverImageContent

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
  "category": "Image",
  "capabilities": [
    "UI"
  ]
}
```

An image-type Content that can be set as an [ImageButton](/docs/reference/engine/classes/ImageButton.md) property.
When the button is hovered, it will render this image. Only asset URIs are
supported for this property.

### Property: ImageButton.Image

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
  "category": "Image",
  "capabilities": [
    "UI"
  ]
}
```

This property is a content-type property that should hold the asset ID of
a decal or image uploaded to Roblox. It functions identically to
[Decal.Texture](/docs/reference/engine/classes/Decal.md) with regards to loading the image from Roblox. The
rendered image will be colorized using
[ImageColor3](/docs/reference/engine/classes/ImageButton.md).

Note that it is possible to make the image render as tiled, scaled to fit,
or 9-sliced by adjusting the [ScaleType](/docs/reference/engine/classes/ImageButton.md)
property.

**Image Hover Lock**

This code sample causes an ImageLabel/ImageButton to display a red padlock.
When the mouse is hovered, it changes to a green unlocked padlock.

```lua
local imageLabel = script.Parent

-- The images in this example are 64x64
imageLabel.Size = UDim2.new(0, 64, 0, 64)

local function unlock()
	imageLabel.Image = "rbxassetid://284402785" -- Unlocked padlock (64x64)
	imageLabel.ImageColor3 = Color3.new(0, 0.5, 0) -- Dark green
end

local function lock()
	imageLabel.Image = "rbxassetid://284402752" -- Locked padlock (64x64)
	imageLabel.ImageColor3 = Color3.new(0.5, 0, 0) -- Dark red
end

-- Connect events; our default state is locked
imageLabel.MouseEnter:Connect(unlock)
imageLabel.MouseLeave:Connect(lock)
lock()
```

### Property: ImageButton.ImageColor3

```json
{
  "type": "Color3",
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
  "category": "Image",
  "capabilities": [
    "UI"
  ]
}
```

This property determines how an image is colorized. When set to white, no
colorization occurs. This property is very useful for reusing image
assets: If the source image is completely white with transparency, you can
set the entire color of the image at once with this property.

**Image Hover Lock**

This code sample causes an ImageLabel/ImageButton to display a red padlock.
When the mouse is hovered, it changes to a green unlocked padlock.

```lua
local imageLabel = script.Parent

-- The images in this example are 64x64
imageLabel.Size = UDim2.new(0, 64, 0, 64)

local function unlock()
	imageLabel.Image = "rbxassetid://284402785" -- Unlocked padlock (64x64)
	imageLabel.ImageColor3 = Color3.new(0, 0.5, 0) -- Dark green
end

local function lock()
	imageLabel.Image = "rbxassetid://284402752" -- Locked padlock (64x64)
	imageLabel.ImageColor3 = Color3.new(0.5, 0, 0) -- Dark red
end

-- Connect events; our default state is locked
imageLabel.MouseEnter:Connect(unlock)
imageLabel.MouseLeave:Connect(lock)
lock()
```

### Property: ImageButton.ImageContent

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
  "category": "Image",
  "capabilities": [
    "UI"
  ]
}
```

This property should hold an
[asset URI](/docs/en-us/projects/assets.md#asset-uris) or a reference
to an [EditableImage](/docs/reference/engine/classes/EditableImage.md) object. The asset URI can reference a decal or
image uploaded to Roblox. It functions identically to
[Decal.Texture](/docs/reference/engine/classes/Decal.md) with regards to loading the image.

The rendered image will be colorized using
[ImageColor3](/docs/reference/engine/classes/ImageButton.md). It is possible to make the
image render as tiled, scaled to fit, or 9‑sliced by adjusting the
[ScaleType](/docs/reference/engine/classes/ImageButton.md) property.

### Property: ImageButton.ImageRectOffset

```json
{
  "type": "Vector2",
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
  "category": "Image",
  "capabilities": [
    "UI"
  ]
}
```

This property determines the pixel offset (from the top-left) of the image
area to be displayed, allowing for the partial display of an image in
conjunction with [ImageRectSize](/docs/reference/engine/classes/ImageButton.md).

**Image Animation using Spritesheet**

This code sample uses ImageRectOffset/ImageRectSize in order to play an
animation of a man throwing a punch

```lua
-- Place this in an ImageLabel/ImageButton with size 256x256
local imageLabel = script.Parent

-- The following image is 1024x1024 with 12 frames (256x256)
-- The frames play an animation of a man throwing a punch
imageLabel.Image = "rbxassetid://848623155"
imageLabel.ImageRectSize = Vector2.new(256, 256)

-- The order of the frames to be displayed (left-to-right, then top-to-bottom)
local frames = {
	Vector2.new(0, 0),
	Vector2.new(1, 0),
	Vector2.new(2, 0),
	Vector2.new(3, 0),
	Vector2.new(0, 1),
	Vector2.new(1, 1),
	Vector2.new(2, 1),
	Vector2.new(3, 1),
	Vector2.new(0, 2),
	Vector2.new(1, 2),
	Vector2.new(2, 2),
	Vector2.new(3, 2),
}

-- Animate the frames one at a time in a loop
while true do
	for _, frame in ipairs(frames) do
		imageLabel.ImageRectOffset = frame * imageLabel.ImageRectSize
		task.wait(0.1)
	end
end
```

### Property: ImageButton.ImageRectSize

```json
{
  "type": "Vector2",
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
  "category": "Image",
  "capabilities": [
    "UI"
  ]
}
```

This property determines the pixel size of the image area to be displayed,
allowing for the partial display of an image in conjunction with
[ImageRectOffset](/docs/reference/engine/classes/ImageButton.md). If either dimension
is set to `0`, the entire image is displayed instead.

**Image Animation using Spritesheet**

This code sample uses ImageRectOffset/ImageRectSize in order to play an
animation of a man throwing a punch

```lua
-- Place this in an ImageLabel/ImageButton with size 256x256
local imageLabel = script.Parent

-- The following image is 1024x1024 with 12 frames (256x256)
-- The frames play an animation of a man throwing a punch
imageLabel.Image = "rbxassetid://848623155"
imageLabel.ImageRectSize = Vector2.new(256, 256)

-- The order of the frames to be displayed (left-to-right, then top-to-bottom)
local frames = {
	Vector2.new(0, 0),
	Vector2.new(1, 0),
	Vector2.new(2, 0),
	Vector2.new(3, 0),
	Vector2.new(0, 1),
	Vector2.new(1, 1),
	Vector2.new(2, 1),
	Vector2.new(3, 1),
	Vector2.new(0, 2),
	Vector2.new(1, 2),
	Vector2.new(2, 2),
	Vector2.new(3, 2),
}

-- Animate the frames one at a time in a loop
while true do
	for _, frame in ipairs(frames) do
		imageLabel.ImageRectOffset = frame * imageLabel.ImageRectSize
		task.wait(0.1)
	end
end
```

### Property: ImageButton.ImageTransparency

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
  "category": "Image",
  "capabilities": [
    "UI"
  ]
}
```

This property determines the alpha of the element's rendered image. A
value of `0` is completely opaque and a value of `1` is completely
transparent (invisible). This property behaves similarly to
[GuiObject.BackgroundTransparency](/docs/reference/engine/classes/GuiObject.md) or [BasePart.Transparency](/docs/reference/engine/classes/BasePart.md).

If you disable image rendering by setting
[ImageTransparency](/docs/reference/engine/classes/ImageButton.md) to `1`, it will
result in a plain rectangle that can be used as a button. However, it may
be better to use a blank [TextButton](/docs/reference/engine/classes/TextButton.md) instead.

### Property: ImageButton.IsLoaded

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
  "category": "Image",
  "capabilities": [
    "UI"
  ]
}
```

This property indicates if the [Image](/docs/reference/engine/classes/ImageButton.md) property
has finished loading from Roblox. Images declined by moderation will never
load.

**Image Load Time**

This code sample measures how long an ImageLabel or ImageButton takes to load
an image. If the image was already loaded, this will be 0.

```lua
local imageLabel = script.Parent

local startTime = workspace.DistributedGameTime

-- Wait for the image to load
while not imageLabel.IsLoaded do
	task.wait()
end

-- Measure and display how long it took to load
local deltaTime = workspace.DistributedGameTime - startTime
print(("Image loaded in %.3f seconds"):format(deltaTime))
```

### Property: ImageButton.PressedImage

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
  "category": "Image",
  "capabilities": [
    "UI"
  ]
}
```

A texture ID that can be set as an [ImageButton](/docs/reference/engine/classes/ImageButton.md) property. When the
button is pressed, it will render this image.

### Property: ImageButton.PressedImageContent

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
  "category": "Image",
  "capabilities": [
    "UI"
  ]
}
```

An image-type Content that can be set as an [ImageButton](/docs/reference/engine/classes/ImageButton.md) property.
When the button is pressed, it will render this image. Only asset URIs are
supported for this property.

### Property: ImageButton.ResampleMode

```json
{
  "type": "ResamplerMode",
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
  "category": "Image",
  "capabilities": [
    "UI"
  ]
}
```

Determines how the image looks when it is scaled. By default, the image
smooths out the texture when displayed either larger or smaller than its
size in texture memory. In contrast,
[Enum.ResamplerMode.Pixelated](/docs/reference/engine/enums/ResamplerMode.md) preserves the
sharp edges of the image pixels.

### Property: ImageButton.ScaleType

```json
{
  "type": "ScaleType",
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
  "category": "Image",
  "capabilities": [
    "UI"
  ]
}
```

This property determines in what way the [Image](/docs/reference/engine/classes/ImageButton.md)
property is rendered when the UI element's absolute size differs from the
source image's size.

By default, this property is
[Enum.ScaleType.Stretch](/docs/reference/engine/enums/ScaleType.md) which will simply
stretch/compact the image dimensions so it fits the UI element's space
exactly. Since transparent pixels are set to black when uploading to
Roblox, transparent images should apply alpha blending to avoid a blackish
outline around scaled images.

For [ScaleType.Slice](/docs/reference/engine/enums/ScaleType.md), when scaling up, the corners will remain the
source image size. The edges of the image will stretch to the width/height
of the image. Finally, the center of the image will stretch to fill the
center area of the image. To learn more about 9‑sliced images, see
[UI 9‑Slice Design](/docs/en-us/ui/9-slice.md).

For [ScaleType.Tile](/docs/reference/engine/enums/ScaleType.md), the size of each image tile is determined by
the [TileSize](/docs/reference/engine/classes/ImageButton.md) property.

### Property: ImageButton.SliceCenter

```json
{
  "type": "Rect",
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
  "category": "Image",
  "capabilities": [
    "UI"
  ]
}
```

This property sets the slice boundaries of a 9-sliced image when
[ScaleType](/docs/reference/engine/classes/ImageButton.md) is set to
[Enum.ScaleType.Slice](/docs/reference/engine/enums/ScaleType.md).

To learn more about 9‑sliced images, see
[UI 9‑Slice Design](/docs/en-us/ui/9-slice.md).

### Property: ImageButton.SliceScale

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
  "category": "Image",
  "capabilities": [
    "UI"
  ]
}
```

Scales the 9-slice edges by the specified ratio. This means that the edges
around the 9‑slice will grow as if you'd uploaded a new version of the
texture upscaled. Defaults to `1.0`.

As a multiplier for the borders of a 9-slice, it is useful for reusing one
rounded corner image for multiple radii.

See also [ScaleType](/docs/reference/engine/classes/ImageButton.md) which determines how an
image will scale if displayed in a UI element whose size differs from the
source image.

### Property: ImageButton.TileSize

```json
{
  "type": "UDim2",
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
  "category": "Image",
  "capabilities": [
    "UI"
  ]
}
```

Sets the tiling size of the [ImageButton](/docs/reference/engine/classes/ImageButton.md) starting at the upper-left
corner of the image. The default [UDim2](/docs/reference/engine/datatypes/UDim2.md) values are <Typography
noWrap>`1, 0, 1, 0`</Typography>; the scale components of the
[UDim2](/docs/reference/engine/datatypes/UDim2.md) will scale the tile based on the size of the
[ImageButton](/docs/reference/engine/classes/ImageButton.md) while the offset components are in raw pixels. For
example, a scale of `0.5` means the tile will be half the size of the
[ImageButton](/docs/reference/engine/classes/ImageButton.md) in the corresponding axis.

This property is only active if the
[ScaleType](/docs/reference/engine/classes/ImageButton.md) property is set to
[ScaleType.Tile](/docs/reference/engine/enums/ScaleType.md).

## Inherited Members

### From [GuiButton](/docs/reference/engine/classes/GuiButton.md)

- **Property `AutoButtonColor`** (`boolean`): Determines whether the button automatically changes color when the mouse
- **Property `HoverHapticEffect`** (`HapticEffect`): A HapticEffect instance that will play when the GuiButton
- **Property `Modal`** (`boolean`): If `true` while the GUI element is visible, the mouse will not be locked
- **Property `PressHapticEffect`** (`HapticEffect`): A HapticEffect instance that will play when the GuiButton
- **Property `Selected`** (`boolean`): A boolean property which indicates whether the object has been selected.
- **Property `Style`** (`ButtonStyle`): Sets the style of the GuiButton based on a list of pre-determined
- **Event `Activated`**: Fires when the button is activated.
- **Event `MouseButton1Click`**: Fires when the user's mouse fully left clicks the GuiButton.
- **Event `MouseButton1Down`**: Fires when the user presses their left mouse button down on the
- **Event `MouseButton1Up`**: Fires when the user releases their left mouse button off of the
- **Event `MouseButton2Click`**: Fires when the user's mouse fully right clicks the GuiButton.
- **Event `MouseButton2Down`**: Fires when the user presses their right mouse button down on the
- **Event `MouseButton2Up`**: Fires when the user releases their right mouse button off of the
- **Event `SecondaryActivated`**: Fires when the button's "secondary" input is activated.

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