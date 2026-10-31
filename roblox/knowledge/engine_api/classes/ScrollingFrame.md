---
name: ScrollingFrame
last_updated: 2026-10-30T19:55:53Z
inherits:
  - GuiObject
  - GuiBase2d
  - GuiBase
  - Instance
  - Object
type: class
memory_category: Gui
summary: "`ScrollingFrame` is a special Frame type with built-in scrolling interactivity and different ways to customize how the scrolling works."
---

# Class: ScrollingFrame

> `ScrollingFrame` is a special [Frame](/docs/reference/engine/classes/Frame.md) type with built-in scrolling
> interactivity and different ways to customize how the scrolling works.

## Description

`ScrollingFrame` is a special [Frame](/docs/reference/engine/classes/Frame.md) type with built-in scrolling
interactivity and different ways to customize how the scrolling works.

![Example ScrollingFrame on the screen containing a tabbed category bar and a list of magical items for the player to consider purchasing.](/assets/ui/ui-objects/ScrollingFrame-Example.jpg)

## Properties

### Property: ScrollingFrame.AbsoluteCanvasSize

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
    "can_save": true
  },
  "thread_safety": "Unsafe",
  "category": "Scrolling",
  "capabilities": [
    "UI"
  ]
}
```

The size of the area that is scrollable, in offsets. This property is set
to the maximum of the [CanvasSize](/docs/reference/engine/classes/ScrollingFrame.md)
property and the size of the children if
[AutomaticCanvasSize](/docs/reference/engine/classes/ScrollingFrame.md) is set to
something other than [AutomaticSize.None](/docs/reference/engine/enums/AutomaticSize.md).

### Property: ScrollingFrame.AbsoluteWindowSize

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
    "can_save": true
  },
  "thread_safety": "Unsafe",
  "category": "Scrolling",
  "capabilities": [
    "UI"
  ]
}
```

The size of the frame, in offsets, without the scroll bars. This read-only
property represents the visible content area of the `ScrollingFrame`: the
frame's [AbsoluteSize](/docs/reference/engine/classes/GuiBase2d.md) minus the space
occupied by any currently visible scroll bar gutters
([ScrollBarThickness](/docs/reference/engine/classes/ScrollingFrame.md)). If no
scroll bars are visible, this equals the frame's absolute size.

### Property: ScrollingFrame.AutomaticCanvasSize

```json
{
  "type": "AutomaticSize",
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
  "category": "Scrolling",
  "capabilities": [
    "UI"
  ]
}
```

This property is used to automatically size parent UI objects based on the
size of its descendants. You can use this property to dynamically add text
and other content to a `ScrollingFrame` at edit or run time and the size
will adjust to fit that content.

When this property is set to an [AutomaticSize](/docs/reference/engine/enums/AutomaticSize.md) value other than
[None](/docs/reference/engine/enums/AutomaticSize.md),
[AbsoluteCanvasSize](/docs/reference/engine/classes/ScrollingFrame.md) may resize
depending on its child content.

### Property: ScrollingFrame.BottomImage

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
  "category": "Scrolling",
  "capabilities": [
    "UI"
  ]
}
```

Image that displays on the bottom of a vertical scroll bar, or the right
of a horizontal scroll bar (rotated 90&deg; counterclockwise for a
horizontal scroll bar).

![Diagram showing the three image asset elements which construct a scrolling frame's scroll bar.](/assets/ui/ui-objects/ScrollingFrame-Scroll-Bar-Elements.png)

### Property: ScrollingFrame.BottomImageContent

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
  "category": "Scrolling",
  "capabilities": [
    "UI"
  ]
}
```

Image that displays on the bottom of a vertical scroll bar, or the right
of a horizontal scroll bar (rotated 90&deg; counterclockwise for a
horizontal scroll bar). Only supports asset URIs as textures.

![Diagram showing the three image asset elements which construct a scrolling frame's scroll bar.](/assets/ui/ui-objects/ScrollingFrame-Scroll-Bar-Elements.png)

### Property: ScrollingFrame.CanvasPosition

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
  "category": "Scrolling",
  "capabilities": [
    "UI"
  ]
}
```

Reflects the **current** positional offset of the canvas within the frame,
in pixels, and sets the position of scroll bars accordingly. Note that
this property doesn't do anything if scroll bars aren't visible.

### Property: ScrollingFrame.CanvasSize

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
  "category": "Scrolling",
  "capabilities": [
    "UI"
  ]
}
```

Determines the size of the scrollable area. For an adaptive alternative
based on the overall size of children within the `ScrollingFrame`,
consider using
[AutomaticCanvasSize](/docs/reference/engine/classes/ScrollingFrame.md).

### Property: ScrollingFrame.ElasticBehavior

```json
{
  "type": "ElasticBehavior",
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
  "category": "Scrolling",
  "capabilities": [
    "UI"
  ]
}
```

This property determines if and when elastic scrolling is allowed on
touch‑enabled devices. Defaults to [WhenScrollable](/docs/reference/engine/enums/ElasticBehavior.md).

### Property: ScrollingFrame.HorizontalScrollBarInset

```json
{
  "type": "ScrollBarInset",
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
  "category": "Scrolling",
  "capabilities": [
    "UI"
  ]
}
```

Indicates whether the scrollable canvas is inset by
[ScrollBarThickness](/docs/reference/engine/classes/ScrollingFrame.md) to account
for the horizontal scroll bar. Because the horizontal scroll bar occupies
space along the bottom edge, this inset reduces the canvas height.
Defaults to [ScrollBarInset.None](/docs/reference/engine/enums/ScrollBarInset.md).

- [None](/docs/reference/engine/enums/ScrollBarInset.md) — the canvas is never inset; content may be
  obscured behind the horizontal scroll bar when it is visible.
- [ScrollBar](/docs/reference/engine/enums/ScrollBarInset.md) — the canvas is inset only while the
  horizontal scroll bar is visible.
- [Always](/docs/reference/engine/enums/ScrollBarInset.md) — the canvas is always inset regardless of
  whether the horizontal scroll bar is visible.

### Property: ScrollingFrame.MidImage

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
  "category": "Scrolling",
  "capabilities": [
    "UI"
  ]
}
```

Image which spans the area between
[TopImage](/docs/reference/engine/classes/ScrollingFrame.md) and
[BottomImage](/docs/reference/engine/classes/ScrollingFrame.md) (rotated 90&deg;
counterclockwise for a horizontal scroll bar). This image automatically
scales to fill the space between the cap segments.

![Diagram showing the three image asset elements which construct a scrolling frame's scroll bar.](/assets/ui/ui-objects/ScrollingFrame-Scroll-Bar-Elements.png)

### Property: ScrollingFrame.MidImageContent

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
  "category": "Scrolling",
  "capabilities": [
    "UI"
  ]
}
```

Image which spans the area between
[TopImageContent](/docs/reference/engine/classes/ScrollingFrame.md) and
[BottomImageContent](/docs/reference/engine/classes/ScrollingFrame.md) (rotated
90&deg; counterclockwise for a horizontal scroll bar). This image
automatically scales to fill the space between the cap segments. Only
supports asset URIs as textures.

![Diagram showing the three image asset elements which construct a scrolling frame's scroll bar.](/assets/ui/ui-objects/ScrollingFrame-Scroll-Bar-Elements.png)

### Property: ScrollingFrame.ScrollBarImageColor3

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
  "category": "Scrolling",
  "capabilities": [
    "UI"
  ]
}
```

Determines how the scroll bar images
([TopImage](/docs/reference/engine/classes/ScrollingFrame.md),
[MidImage](/docs/reference/engine/classes/ScrollingFrame.md),
[BottomImage](/docs/reference/engine/classes/ScrollingFrame.md)) are colorized. When set to
white, no colorization occurs. This property is useful for reusing image
assets; if the source images are completely white with transparency, you
can set the color of the entire scroll bar at once.

### Property: ScrollingFrame.ScrollBarImageTransparency

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
  "category": "Scrolling",
  "capabilities": [
    "UI"
  ]
}
```

Determines the opacity of the scroll bar images
([TopImage](/docs/reference/engine/classes/ScrollingFrame.md),
[MidImage](/docs/reference/engine/classes/ScrollingFrame.md),
[BottomImage](/docs/reference/engine/classes/ScrollingFrame.md)). A value of `0` is
completely opaque and a value of `1` is completely transparent
(invisible).

### Property: ScrollingFrame.ScrollBarThickness

```json
{
  "type": "int",
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
  "category": "Scrolling",
  "capabilities": [
    "UI"
  ]
}
```

Thickness of the scroll bar in pixels; applies to both horizontal and
vertical scroll bars. If set to `0`, no scroll bars are rendered.

### Property: ScrollingFrame.ScrollingDirection

```json
{
  "type": "ScrollingDirection",
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
  "category": "Scrolling",
  "capabilities": [
    "UI"
  ]
}
```

This property determines the direction(s) in which scrolling is allowed.
If scrolling is disallowed in a direction, the associated scroll bar will
not appear. Defaults to [ScrollingDirection.XY](/docs/reference/engine/enums/ScrollingDirection.md).

### Property: ScrollingFrame.ScrollingEnabled

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
  "category": "Scrolling",
  "capabilities": [
    "UI"
  ]
}
```

Determines whether scrolling is allowed on the frame. If `false`, no
scroll bars will be rendered.

### Property: ScrollingFrame.TopImage

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
  "category": "Scrolling",
  "capabilities": [
    "UI"
  ]
}
```

Image which displays on the top of a vertical scroll bar, or the left of a
horizontal scroll bar (rotated 90&deg; counterclockwise for a horizontal
scroll bar).

![Diagram showing the three image asset elements which construct a scrolling frame's scroll bar.](/assets/ui/ui-objects/ScrollingFrame-Scroll-Bar-Elements.png)

### Property: ScrollingFrame.TopImageContent

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
  "category": "Scrolling",
  "capabilities": [
    "UI"
  ]
}
```

Image which displays on the top of a vertical scroll bar, or the left of a
horizontal scroll bar (rotated 90&deg; counterclockwise for a horizontal
scroll bar). Only supports asset URIs as textures. Defaults to the
built-in scroll bar top cap texture
(`rbxasset://textures/ui/Scroll/scroll-top.png`).

![Diagram showing the three image asset elements which construct a scrolling frame's scroll bar.](/assets/ui/ui-objects/ScrollingFrame-Scroll-Bar-Elements.png)

### Property: ScrollingFrame.VerticalScrollBarInset

```json
{
  "type": "ScrollBarInset",
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
  "category": "Scrolling",
  "capabilities": [
    "UI"
  ]
}
```

Indicates whether the scrollable canvas is inset by
[ScrollBarThickness](/docs/reference/engine/classes/ScrollingFrame.md) to account
for the vertical scroll bar. Because the vertical scroll bar occupies
space along a side edge, this inset reduces the canvas width. Defaults to
[ScrollBarInset.None](/docs/reference/engine/enums/ScrollBarInset.md).

- [None](/docs/reference/engine/enums/ScrollBarInset.md) — the canvas is never inset; content may be
  obscured behind the vertical scroll bar when it is visible.
- [ScrollBar](/docs/reference/engine/enums/ScrollBarInset.md) — the canvas is inset only while the
  vertical scroll bar is visible.
- [Always](/docs/reference/engine/enums/ScrollBarInset.md) — the canvas is always inset regardless of
  whether the vertical scroll bar is visible.

### Property: ScrollingFrame.VerticalScrollBarPosition

```json
{
  "type": "VerticalScrollBarPosition",
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
  "category": "Scrolling",
  "capabilities": [
    "UI"
  ]
}
```

Indicates whether the vertical scroll bar is positioned to the left or
right of the canvas. Defaults to [VerticalScrollBarPosition.Right](/docs/reference/engine/enums/VerticalScrollBarPosition.md).

## Methods

### Method: ScrollingFrame:GetScrollVelocity

**Signature:** `ScrollingFrame:GetScrollVelocity(): Vector2`

Returns a [Vector2](/docs/reference/engine/datatypes/Vector2.md) representing the current inertial scroll
velocity after the user stops their input, for example lifts their finger
off the `ScrollingFrame` on a touch-enabled device.

Note that this method may only produce noticable data on an actual device
or in an emulated scenario from Studio's **Device&nbsp;Emulator**.

*Security: None · Thread Safety: Unsafe · Capabilities: UI*

**Returns:** `Vector2` — The current inertial scroll velocity in pixels per second on each
axis, or `(0, 0)` if the frame is not coasting.

### Method: ScrollingFrame:ResetScrollVelocity

**Signature:** `ScrollingFrame:ResetScrollVelocity(): ()`

Resets the inertial scroll velocity of the `ScrollingFrame` to `0` on both
axes.

*Security: None · Thread Safety: Unsafe · Capabilities: UI*

**Returns:** `()`

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