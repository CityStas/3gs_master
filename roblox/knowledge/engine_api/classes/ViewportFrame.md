---
name: ViewportFrame
last_updated: 2026-10-30T19:55:53Z
inherits:
  - GuiObject
  - GuiBase2d
  - GuiBase
  - Instance
  - Object
type: class
memory_category: Gui
summary: "GuiObject that renders 3D objects inside its bounds."
---

# Class: ViewportFrame

> [GuiObject](/docs/reference/engine/classes/GuiObject.md) that renders 3D objects inside its bounds.

## Description

`ViewportFrame` is a [GuiObject](/docs/reference/engine/classes/GuiObject.md) that renders 3D objects inside its
bounds, offering a way to display 3D objects in a 2D space like a
[ScreenGui](/docs/reference/engine/classes/ScreenGui.md). This object has the following caveats:

- No shadows or
  [post-processing](/docs/en-us/environment/post-processing-effects.md) effects
  are rendered.

- [Material.Neon](/docs/reference/engine/enums/Material.md) and [Material.Glass](/docs/reference/engine/enums/Material.md) materials render at the
  lowest quality.

- Nested [GuiObjects](/docs/reference/engine/classes/GuiObject.md) aren't supported.

- By default, lighting inside a `ViewportFrame` acts as if
  [Lighting.EnvironmentSpecularScale](/docs/reference/engine/classes/Lighting.md) and
  [Lighting.EnvironmentDiffuseScale](/docs/reference/engine/classes/Lighting.md) are both set to `0`, so properties
  that rely on these fields, such as [SurfaceAppearance.MetalnessMap](/docs/reference/engine/classes/SurfaceAppearance.md),
  may look different.

- This object can use a [Sky](/docs/reference/engine/classes/Sky.md) child as a cubemap for reflections, in
  which case only the [Sky](/docs/reference/engine/classes/Sky.md) object's six `Skybox[…]` properties are
  used. Assuming these properties are valid, lighting inside the
  `ViewportFrame` acts similarly to if
  [Lighting.EnvironmentSpecularScale](/docs/reference/engine/classes/Lighting.md) and
  [Lighting.EnvironmentDiffuseScale](/docs/reference/engine/classes/Lighting.md) are both set to `1`. For details,
  see [here](/docs/en-us/ui/viewport-frames.md).

## Code Samples

**ViewportFrame - Create GUI**

```lua
local Players = game:GetService("Players")

local player = Players.LocalPlayer
local playerGui = player:WaitForChild("PlayerGui")
local screenGui = Instance.new("ScreenGui")
screenGui.Parent = playerGui

local viewportFrame = Instance.new("ViewportFrame")
viewportFrame.Size = UDim2.new(0.3, 0, 0.4, 0)
viewportFrame.Position = UDim2.new(0, 15, 0, 15)
viewportFrame.BackgroundColor3 = Color3.new(0, 0, 0)
viewportFrame.BorderColor3 = Color3.new(0.6, 0.5, 0.4)
viewportFrame.BorderSizePixel = 2
viewportFrame.BackgroundTransparency = 0.25
viewportFrame.Parent = screenGui

local part = Instance.new("Part")
part.Material = Enum.Material.Concrete
part.Color = Color3.new(0.25, 0.75, 1)
part.Position = Vector3.new(0, 0, 0)
part.Parent = viewportFrame

local viewportCamera = Instance.new("Camera")
viewportFrame.CurrentCamera = viewportCamera
viewportCamera.Parent = viewportFrame

viewportCamera.CFrame = CFrame.new(Vector3.new(0, 2, 12), part.Position)
```

**ViewportFrame - Control Camera**

```lua
local Players = game:GetService("Players")

local player = Players.LocalPlayer
local playerGui = player:WaitForChild("PlayerGui")
local screenGui = Instance.new("ScreenGui")
screenGui.Parent = playerGui

local TweenService = game:GetService("TweenService")

local viewportFrame = Instance.new("ViewportFrame")
viewportFrame.Size = UDim2.new(0.3, 0, 0.4, 0)
viewportFrame.Position = UDim2.new(0, 15, 0, 15)
viewportFrame.BackgroundColor3 = Color3.new(0, 0, 0)
viewportFrame.BorderColor3 = Color3.new(0.6, 0.5, 0.4)
viewportFrame.BorderSizePixel = 2
viewportFrame.BackgroundTransparency = 0.25
viewportFrame.Parent = screenGui

local part = Instance.new("Part")
part.Material = Enum.Material.Concrete
part.Color = Color3.new(0.25, 0.75, 1)
part.Position = Vector3.new(0, 0, 0)
part.Parent = viewportFrame

local viewportCamera = Instance.new("Camera")
viewportFrame.CurrentCamera = viewportCamera
viewportCamera.Parent = viewportFrame

viewportCamera.CFrame = CFrame.new(Vector3.new(0, 2, 12), part.Position)

task.wait(2)

local cameraGoal = {
	CFrame = CFrame.new(Vector3.new(0, 6, 4), part.Position),
}

local tweenInfo = TweenInfo.new(2, Enum.EasingStyle.Quad, Enum.EasingDirection.Out)

local tween = TweenService:Create(viewportCamera, tweenInfo, cameraGoal)

tween:Play()
```

## Properties

### Property: ViewportFrame.Ambient

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
  "category": "Appearance",
  "capabilities": [
    "UI"
  ]
}
```

This property determines the lighting hue applied to the area within the
`ViewportFrame`. Defaults to
<Typography noWrap>[Color3.fromRGB(200, 200, 200)](/docs/reference/engine/datatypes/Color3.md)</Typography>
(ghost grey).

### Property: ViewportFrame.CurrentCamera

```json
{
  "type": "Camera",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": true,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Data",
  "capabilities": [
    "UI"
  ]
}
```

[Camera](/docs/reference/engine/classes/Camera.md) instance that is used to render children objects. Defaults
to `nil`.

The [Camera](/docs/reference/engine/classes/Camera.md) object does not replicate so the
[ViewportFrame.CurrentCamera](/docs/reference/engine/classes/ViewportFrame.md) won't replicate either. When you set
this property, [Camera.CFrame](/docs/reference/engine/classes/Camera.md) and [Camera.FieldOfView](/docs/reference/engine/classes/Camera.md) will
be saved and replicate with the `ViewportFrame` internally so the client
can render the frame without a [Camera](/docs/reference/engine/classes/Camera.md) object.

### Property: ViewportFrame.ImageColor3

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

This property determines how the rendered viewport image will be
colorized, allowing you to change the color without directly modifying the
rendered object. The default colorization value is <Typography
noWrap>[Color3.new(1, 1, 1)](/docs/reference/engine/datatypes/Color3.md)</Typography> (white) at which
no color modification occurs.

See also [ImageTransparency](/docs/reference/engine/classes/ViewportFrame.md) which
determines the transparency of the rendered image.

### Property: ViewportFrame.ImageTransparency

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

This property determines the transparency of the rendered viewport image,
allowing you to change the transparency without directly modifying the
rendered object. A value of `0` (default) is completely opaque and a value
of `1` is completely transparent (invisible).

See also [ImageColor3](/docs/reference/engine/classes/ViewportFrame.md) which determines
how the rendered image will be colorized.

### Property: ViewportFrame.LightColor

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
  "category": "Appearance",
  "capabilities": [
    "UI"
  ]
}
```

The color of the emitted light. Defaults to
<Typography noWrap>[Color3.fromRGB(140, 140, 140)](/docs/reference/engine/datatypes/Color3.md)</Typography>
(silver).

### Property: ViewportFrame.LightDirection

```json
{
  "type": "Vector3",
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
  "category": "Appearance",
  "capabilities": [
    "UI"
  ]
}
```

A [Vector3](/docs/reference/engine/datatypes/Vector3.md) representing the direction of the light source from
position <Typography noWrap>`(0, 0, 0)`</Typography>. Defaults to
<Typography noWrap>[Vector3.new(-1, -1, -1)](/docs/reference/engine/datatypes/Vector3.md)</Typography>.

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