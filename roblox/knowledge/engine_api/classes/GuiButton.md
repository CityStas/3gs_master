---
name: GuiButton
last_updated: 2026-10-30T19:55:52Z
inherits:
  - GuiObject
  - GuiBase2d
  - GuiBase
  - Instance
  - Object
type: class
memory_category: Gui
tags:
  - NotCreatable
  - NotBrowsable
summary: "An abstract class for interactive 2D user interface elements."
---

# Class: GuiButton

> An abstract class for interactive 2D user interface elements.

## Description

[GuiButton](/docs/reference/engine/classes/GuiButton.md) is an abstract class that inherits from [GuiObject](/docs/reference/engine/classes/GuiObject.md).
It is the base class for the interactive, clickable [ImageButton](/docs/reference/engine/classes/ImageButton.md) and
[TextButton](/docs/reference/engine/classes/TextButton.md) objects. This class also defines several properties for
interactive behavior, namely [AutoButtonColor](/docs/reference/engine/classes/GuiButton.md)
and [Modal](/docs/reference/engine/classes/GuiButton.md).

The most important event of a [GuiButton](/docs/reference/engine/classes/GuiButton.md) is
[Activated](/docs/reference/engine/classes/GuiButton.md), a **multi-platform event** that fires
when the button is activated. When using a mouse, this means clicking the
button and releasing with the cursor still over the UI object. For touch, the
same applies but with a touch instead of button press. Finally, for gamepads,
[Activated](/docs/reference/engine/classes/GuiButton.md) fires if a [GuiButton](/docs/reference/engine/classes/GuiButton.md) is selected
when the **A** button is pressed and released. In short, this event is very
useful for multi-platform user interface programming as it provides a nice
general interface for a single user input.

## Properties

### Property: GuiButton.AutoButtonColor

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
  "category": "Data",
  "capabilities": [
    "UI"
  ]
}
```

This property determines whether the button automatically changes color
when the user's [Mouse](/docs/reference/engine/classes/Mouse.md) hovers over or clicks on it. If `true`, the
button will automatically change color when the mouse hovers over or
clicks on it. If `false`, the button will not change.

If you would like to customize how a button changes when the user's mouse
hovers over or clicks on it, consider using an [ImageButton](/docs/reference/engine/classes/ImageButton.md) and
changing the element's [HoverImage](/docs/reference/engine/classes/ImageButton.md) and
[PressedImage](/docs/reference/engine/classes/ImageButton.md).

Please note that this property will not have an effect on an
[ImageButton](/docs/reference/engine/classes/ImageButton.md) if its [Image](/docs/reference/engine/classes/ImageButton.md) property is set
to an image. Additionally, this property will not affect an
[ImageButton](/docs/reference/engine/classes/ImageButton.md) on mouse hover when its
[HoverImage](/docs/reference/engine/classes/ImageButton.md) is not `nil`, nor on mouse click
if its [PressedImage](/docs/reference/engine/classes/ImageButton.md) is not `nil`.

### Property: GuiButton.HoverHapticEffect

```json
{
  "type": "HapticEffect",
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
  "category": "Haptic",
  "capabilities": [
    "UI"
  ]
}
```

A [HapticEffect](/docs/reference/engine/classes/HapticEffect.md) that the engine plays the first time the pointer
moves over the button, when the button transitions from its idle state to
its hover state. Assign a [HapticEffect](/docs/reference/engine/classes/HapticEffect.md) to give hover feedback (for
example, a light effect on gamepad or mobile); leave it unset for no hover
haptics.

The effect plays through the standard [HapticService](/docs/reference/engine/classes/HapticService.md) mixer, so
whether the player actually feels vibration depends on their device and
haptic settings. This property defaults to `nil` (no effect).

### Property: GuiButton.Modal

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
  "category": "Data",
  "capabilities": [
    "UI"
  ]
}
```

If `true` while the GUI element is visible, the mouse will not be locked
unless the right mouse button is down.

### Property: GuiButton.PressHapticEffect

```json
{
  "type": "HapticEffect",
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
  "category": "Haptic",
  "capabilities": [
    "UI"
  ]
}
```

A [HapticEffect](/docs/reference/engine/classes/HapticEffect.md) that the engine plays when the button enters its
pressed state. Assign a [HapticEffect](/docs/reference/engine/classes/HapticEffect.md) to give press or click
feedback; leave it unset for no press haptics.

The effect plays through the standard [HapticService](/docs/reference/engine/classes/HapticService.md) mixer, so
whether the player actually feels vibration depends on their device and
haptic settings. This property defaults to `nil` (no effect).

### Property: GuiButton.Selected

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
  "category": "Selection",
  "capabilities": [
    "UI"
  ]
}
```

When set to `true`, the button renders in a highlighted "selected" state
instead of its normal idle appearance. This property defaults to `false`,
and the engine never changes it automatically; set it yourself to mark a
button as selected.

`Selected` only has a visual effect on the legacy [ButtonStyle](/docs/reference/engine/enums/ButtonStyle.md)
presets (the `Roblox*` styles) with
[AutoButtonColor](/docs/reference/engine/classes/GuiButton.md) enabled, where it swaps
in the button's highlighted image. It has no effect under the default
[Style](/docs/reference/engine/classes/GuiButton.md) of `Custom`. It is unrelated to gamepad and
controller UI navigation; the currently focused element is tracked
separately by [SelectedObject](/docs/reference/engine/classes/GuiService.md).

### Property: GuiButton.Style

```json
{
  "type": "ButtonStyle",
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
  "category": "Data",
  "capabilities": [
    "UI"
  ]
}
```

Sets the button's overall appearance from a fixed set of
[ButtonStyle](/docs/reference/engine/enums/ButtonStyle.md) presets. The default value is `Custom`, which applies
no built-in styling and lets you control the button's appearance entirely
through properties such as
[BackgroundColor3](/docs/reference/engine/classes/GuiObject.md) and, for an
[ImageButton](/docs/reference/engine/classes/ImageButton.md), its images.

A legacy method of applying a fixed set of Roblox-themed button styles.
The remaining presets (`RobloxButton`, `RobloxButtonDefault`,
`RobloxRoundButton`, `RobloxRoundDefaultButton`, and
`RobloxRoundDropdownButton`) render Roblox-themed button art. New
interfaces should keep `Custom` and style the button directly. This
property defaults to [ButtonStyle.Custom](/docs/reference/engine/enums/ButtonStyle.md).

## Events

### Event: GuiButton.Activated

**Signature:** `GuiButton.Activated(inputObject: InputObject, clickCount: int)`

Fires when a left click press-and-release is detected on desktop, touch
release is detected on mobile, or **A**/cross is activated in UI
navigation mode on console. The first time this method is called,
`clickCount` will start at `0`.

As this event doesn't fire on the server, it should only be used in a
[LocalScript](/docs/reference/engine/classes/LocalScript.md), or in a [Script](/docs/reference/engine/classes/Script.md) with
[RunContext](/docs/reference/engine/classes/Script.md) of [RunContext.Client](/docs/reference/engine/enums/RunContext.md).

*Security: None · Capabilities: UI*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `inputObject` | `InputObject` | An [InputObject](/docs/reference/engine/classes/InputObject.md) representing the user input that activated the button. |
| `clickCount` | `int` | The number of consecutive rapid activations, starting at 0 for the first activation and incrementing with each subsequent activation within quick succession of the previous one. |

### Event: GuiButton.MouseButton1Click

**Signature:** `GuiButton.MouseButton1Click()`

This event fires when the user's mouse fully left clicks the
[GuiButton](/docs/reference/engine/classes/GuiButton.md).

In regards to clicking, the mouse must be in bounds of the
[GuiButton](/docs/reference/engine/classes/GuiButton.md) and the mouse button must be pressed down and up again
before this event fires. If the mouse leaves the bounds of the
[GuiButton](/docs/reference/engine/classes/GuiButton.md) and is released, the event will not fire. If you would
like to avoid this limitation, you can use
[MouseButton1Down](/docs/reference/engine/classes/GuiButton.md) and
[MouseButton1Up](/docs/reference/engine/classes/GuiButton.md); these events are similar
but will fire whenever the user presses their left mouse button down or
up, respectively.

*Security: None · Capabilities: UI*

### Event: GuiButton.MouseButton1Down

**Signature:** `GuiButton.MouseButton1Down(x: int, y: int)`

This event fires when the user presses their left mouse button down on the
[GuiButton](/docs/reference/engine/classes/GuiButton.md).

For an event requiring the user to press **and** release their left mouse
on a [GuiButton](/docs/reference/engine/classes/GuiButton.md) in order for the event to fire, consider using
[MouseButton1Click](/docs/reference/engine/classes/GuiButton.md).

*Security: None · Capabilities: UI*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `x` | `int` | The mouse's **X** screen coordinate in pixels. |
| `y` | `int` | The mouse's **Y** screen coordinate in pixels. |

### Event: GuiButton.MouseButton1Up

**Signature:** `GuiButton.MouseButton1Up(x: int, y: int)`

This event fires when the user releases their left mouse button off of the
[GuiButton](/docs/reference/engine/classes/GuiButton.md).

For an event requiring the user to press **and** release their left mouse
on a [GuiButton](/docs/reference/engine/classes/GuiButton.md) in order for the event to fire, consider using
[MouseButton1Click](/docs/reference/engine/classes/GuiButton.md).

*Security: None · Capabilities: UI*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `x` | `int` | The mouse's **X** screen coordinate in pixels. |
| `y` | `int` | The mouse's **Y** screen coordinate in pixels. |

### Event: GuiButton.MouseButton2Click

**Signature:** `GuiButton.MouseButton2Click()`

This event fires when the user's mouse fully right clicks the
[GuiButton](/docs/reference/engine/classes/GuiButton.md).

In regards to clicking, the mouse must be in bounds of the
[GuiButton](/docs/reference/engine/classes/GuiButton.md) and the mouse button must be pressed down and up again
before this event fires. If the mouse leaves the bounds of the
[GuiButton](/docs/reference/engine/classes/GuiButton.md) and is released, the event will not fire. If you would
like to avoid this limitation, you can use
[MouseButton2Down](/docs/reference/engine/classes/GuiButton.md) and
[MouseButton2Up](/docs/reference/engine/classes/GuiButton.md); these events are similar
but will fire whenever the user presses their right mouse button down or
up, respectively.

*Security: None · Capabilities: UI*

### Event: GuiButton.MouseButton2Down

**Signature:** `GuiButton.MouseButton2Down(x: int, y: int)`

This event fires when the user presses their right mouse button down on
the [GuiButton](/docs/reference/engine/classes/GuiButton.md).

For an event requiring the user to press **and** release their right mouse
on a [GuiButton](/docs/reference/engine/classes/GuiButton.md) in order for the event to fire, consider using
[MouseButton2Click](/docs/reference/engine/classes/GuiButton.md).

*Security: None · Capabilities: UI*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `x` | `int` | The mouse's **X** screen coordinate in pixels. |
| `y` | `int` | The mouse's **Y** screen coordinate in pixels. |

### Event: GuiButton.MouseButton2Up

**Signature:** `GuiButton.MouseButton2Up(x: int, y: int)`

This event fires when the user releases their right mouse button off of
the [GuiButton](/docs/reference/engine/classes/GuiButton.md).

For an event requiring the user to press **and** release their right mouse
on a [GuiButton](/docs/reference/engine/classes/GuiButton.md) in order for the event to fire, consider using
[MouseButton2Click](/docs/reference/engine/classes/GuiButton.md).

*Security: None · Capabilities: UI*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `x` | `int` | The mouse's **X** screen coordinate in pixels. |
| `y` | `int` | The mouse's **Y** screen coordinate in pixels. |

### Event: GuiButton.SecondaryActivated

**Signature:** `GuiButton.SecondaryActivated(inputObject: InputObject)`

Fires when a right-click press-and-release is detected from a mouse, long
press is detected on a touch input, `R3` is detected from a gamepad, or
<kbd>Alt</kbd><kbd>Enter</kbd> is detected in UI navigation mode using
keyboard.

*Security: None · Capabilities: UI*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `inputObject` | `InputObject` | The input object representing the alternate activation action. |

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