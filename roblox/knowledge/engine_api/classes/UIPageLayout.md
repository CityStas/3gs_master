---
name: UIPageLayout
last_updated: 2026-10-30T19:55:53Z
inherits:
  - UIGridStyleLayout
  - UILayout
  - UIComponent
  - UIBase
  - Instance
  - Object
type: class
memory_category: Instances
summary: "Positions sibling UI elements as full-size pages in a single row or column that users can scroll or animate through one page at a time."
---

# Class: UIPageLayout

> Positions sibling UI elements as full-size pages in a single row or column
> that users can scroll or animate through one page at a time.

## Description

Creates a paged viewing window, like the home screen of a mobile device. You
can use a UIPageLayout by parenting it to a GuiObject. The UIPageLayout will
then apply itself to all of its GuiObject siblings.

## Properties

### Property: UIPageLayout.Animated

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
  "category": "Appearance",
  "capabilities": [
    "UI"
  ]
}
```

When set to true, page transitions use the configured
[UIPageLayout.EasingStyle](/docs/reference/engine/classes/UIPageLayout.md), [UIPageLayout.EasingDirection](/docs/reference/engine/classes/UIPageLayout.md),
and [UIPageLayout.TweenTime](/docs/reference/engine/classes/UIPageLayout.md) to animate the movement between pages.
When set to false, page transitions are instantaneous. Defaults to `true`.

### Property: UIPageLayout.Circular

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
  "category": "Appearance",
  "capabilities": [
    "UI"
  ]
}
```

When set to true, navigating past the last page wraps around to the first
page, and navigating before the first page wraps to the last. Animated
transitions take the shortest rotational path around the wrap boundary.
When set to false, navigation stops at the first and last pages. Defaults
to `false`.

### Property: UIPageLayout.CurrentPage

```json
{
  "type": "GuiObject",
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
    "UI"
  ]
}
```

A read-only reference to the [GuiObject](/docs/reference/engine/classes/GuiObject.md) sibling that is currently
displayed or is the target of an in-progress animation. The layout updates
this property when pages change via [UIPageLayout:Next()](/docs/reference/engine/classes/UIPageLayout.md),
[UIPageLayout:Previous()](/docs/reference/engine/classes/UIPageLayout.md), [UIPageLayout:JumpTo()](/docs/reference/engine/classes/UIPageLayout.md),
[UIPageLayout:JumpToIndex()](/docs/reference/engine/classes/UIPageLayout.md), or through user input (touch swipe,
scroll wheel, or gamepad). If no page has been explicitly navigated to, it
defaults to the first visible [GuiObject](/docs/reference/engine/classes/GuiObject.md) sibling in layout order.

### Property: UIPageLayout.EasingDirection

```json
{
  "type": "EasingDirection",
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

Determines the direction component of the easing function applied during
animated page transitions. Combined with [UIPageLayout.EasingStyle](/docs/reference/engine/classes/UIPageLayout.md)
to form the full tween curve. Only takes effect when
[UIPageLayout.Animated](/docs/reference/engine/classes/UIPageLayout.md) is true. Defaults to
[EasingDirection.Out](/docs/reference/engine/enums/EasingDirection.md).

### Property: UIPageLayout.EasingStyle

```json
{
  "type": "EasingStyle",
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

Determines the easing curve applied during animated page transitions.
Combined with [UIPageLayout.EasingDirection](/docs/reference/engine/classes/UIPageLayout.md) to form the full tween
curve. Only takes effect when [UIPageLayout.Animated](/docs/reference/engine/classes/UIPageLayout.md) is true.
Defaults to [EasingStyle.Back](/docs/reference/engine/enums/EasingStyle.md). Assigning [EasingStyle.Bezier](/docs/reference/engine/enums/EasingStyle.md)
or [EasingStyle.Spring](/docs/reference/engine/enums/EasingStyle.md) emits a warning and leaves this property
unchanged.

### Property: UIPageLayout.GamepadInputEnabled

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
  "category": "Input",
  "capabilities": [
    "UI"
  ]
}
```

When set to true, the layout overrides sibling
[GuiObject.NextSelectionLeft](/docs/reference/engine/classes/GuiObject.md) and
[GuiObject.NextSelectionRight](/docs/reference/engine/classes/GuiObject.md) (for horizontal fill direction) or
[GuiObject.NextSelectionUp](/docs/reference/engine/classes/GuiObject.md) and [GuiObject.NextSelectionDown](/docs/reference/engine/classes/GuiObject.md)
(for vertical fill direction) so that gamepad directional navigation moves
between pages. Additionally, the L1 and R1 bumper buttons advance to the
previous and next page respectively. When false, gamepad input does not
interact with the layout. Defaults to `true`.

### Property: UIPageLayout.Padding

```json
{
  "type": "UDim",
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

Determines the amount that pages are separated from each other by. Can be
set either using scale (Percentage of parent's size in the current
direction) or offset (a static spacing value, similar to pixel size).

### Property: UIPageLayout.ScrollWheelInputEnabled

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
  "category": "Input",
  "capabilities": [
    "UI"
  ]
}
```

When set to true, mouse scroll wheel input navigates between pages.
Scrolling up moves to the previous page and scrolling down moves to the
next page. Set this to false when the scroll wheel is intended for other
interactions in the UI. Defaults to `true`.

### Property: UIPageLayout.TouchInputEnabled

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
  "category": "Input",
  "capabilities": [
    "UI"
  ]
}
```

When set to true, touch-based swipe gestures navigate between pages. Set
this to false for layouts where touch input should not trigger page
transitions, such as non-interactive displays. Defaults to `true`.

### Property: UIPageLayout.TweenTime

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
  "category": "Appearance",
  "capabilities": [
    "UI"
  ]
}
```

The duration, in seconds, of the animated transition when navigating
between pages. The value is clamped to a minimum of 0.01. Only takes
effect when [UIPageLayout.Animated](/docs/reference/engine/classes/UIPageLayout.md) is true. Defaults to `1`.

## Methods

### Method: UIPageLayout:JumpTo

**Signature:** `UIPageLayout:JumpTo(page: Instance): ()`

Navigates to a specific page within the layout. The `page` argument must
be a [GuiObject](/docs/reference/engine/classes/GuiObject.md) that is a visible sibling managed by this layout;
passing `nil` or an instance that is not part of the layout throws an
error. Sets [UIPageLayout.CurrentPage](/docs/reference/engine/classes/UIPageLayout.md) to the target and animates
the transition (or jumps instantly if [UIPageLayout.Animated](/docs/reference/engine/classes/UIPageLayout.md) is
false). When [UIPageLayout.Circular](/docs/reference/engine/classes/UIPageLayout.md) is true, the animation takes
the shortest rotational path to the target page.

*Security: None · Thread Safety: Unsafe · Capabilities: UI*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `page` | `Instance` |  | The [GuiObject](/docs/reference/engine/classes/GuiObject.md) sibling to navigate to. |

**Returns:** `()`

### Method: UIPageLayout:JumpToIndex

**Signature:** `UIPageLayout:JumpToIndex(index: int): ()`

Navigates to the page at the given zero-based `index` in layout order. If
the index is within the valid range (0 to page count minus 1), this method
behaves like [UIPageLayout:JumpTo()](/docs/reference/engine/classes/UIPageLayout.md). Out-of-bounds indices are
wrapped modulo the page count to determine the final page.

*Security: None · Thread Safety: Unsafe · Capabilities: UI*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `index` | `int` |  | The zero-based position of the target page in layout order. |

**Returns:** `()`

### Method: UIPageLayout:Next

**Signature:** `UIPageLayout:Next(): ()`

Advances [UIPageLayout.CurrentPage](/docs/reference/engine/classes/UIPageLayout.md) to the next page in layout order
and animates the transition (or jumps instantly if
[UIPageLayout.Animated](/docs/reference/engine/classes/UIPageLayout.md) is false). If the current page is already
the last page and [UIPageLayout.Circular](/docs/reference/engine/classes/UIPageLayout.md) is false, this method does
nothing. If [UIPageLayout.Circular](/docs/reference/engine/classes/UIPageLayout.md) is true, it wraps from the last
page to the first.

*Security: None · Thread Safety: Unsafe · Capabilities: UI*

**Returns:** `()`

### Method: UIPageLayout:Previous

**Signature:** `UIPageLayout:Previous(): ()`

Moves [UIPageLayout.CurrentPage](/docs/reference/engine/classes/UIPageLayout.md) to the previous page in layout
order and animates the transition (or jumps instantly if
[UIPageLayout.Animated](/docs/reference/engine/classes/UIPageLayout.md) is false). If the current page is already
the first page and [UIPageLayout.Circular](/docs/reference/engine/classes/UIPageLayout.md) is false, this method
does nothing. If [UIPageLayout.Circular](/docs/reference/engine/classes/UIPageLayout.md) is true, it wraps from the
first page to the last.

*Security: None · Thread Safety: Unsafe · Capabilities: UI*

**Returns:** `()`

## Events

### Event: UIPageLayout.PageEnter

**Signature:** `UIPageLayout.PageEnter(page: Instance)`

Fires when a sibling page's bounding rect begins intersecting the parent's
clip region, causing it to become visible and rendered. The `page`
parameter is the [GuiObject](/docs/reference/engine/classes/GuiObject.md) that entered view. This event fires on
the frame the page's visibility flips from hidden to shown, whether due to
an animated transition, a programmatic jump, or user input scrolling.

*Security: None · Capabilities: UI*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `page` | `Instance` | The [GuiObject](/docs/reference/engine/classes/GuiObject.md) that entered view. |

### Event: UIPageLayout.PageLeave

**Signature:** `UIPageLayout.PageLeave(page: Instance)`

Fires when a sibling page's bounding rect stops intersecting the parent's
clip region, causing it to become hidden and no longer rendered. The
`page` parameter is the [GuiObject](/docs/reference/engine/classes/GuiObject.md) that left view. This event fires
on the frame the page's visibility flips from shown to hidden, whether due
to an animated transition, a programmatic jump, or user input scrolling.

*Security: None · Capabilities: UI*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `page` | `Instance` | The [GuiObject](/docs/reference/engine/classes/GuiObject.md) that left view. |

### Event: UIPageLayout.Stopped

**Signature:** `UIPageLayout.Stopped(currentPage: Instance)`

Fires when a page-navigation animation reaches its target without being
interrupted by new input, and the view comes to rest. The `currentPage`
parameter is the [GuiObject](/docs/reference/engine/classes/GuiObject.md) now displayed. This event does not fire
for programmatic transitions made while [UIPageLayout.Animated](/docs/reference/engine/classes/UIPageLayout.md) is
false, since those snap to the target page instantly.

*Security: None · Capabilities: UI*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `currentPage` | `Instance` | The [GuiObject](/docs/reference/engine/classes/GuiObject.md) now displayed after the transition completed. |

## Inherited Members

### From [UIGridStyleLayout](/docs/reference/engine/classes/UIGridStyleLayout.md)

- **Property `AbsoluteContentSize`** (`Vector2`): The absolute size of space being taken up by the grid layout.
- **Property `FillDirection`** (`FillDirection`): Determines the axis in which UI objects are laid out.
- **Property `HorizontalAlignment`** (`HorizontalAlignment`): Determines the horizontal alignment of UI elements within the parent
- **Property `SortOrder`** (`SortOrder`): Determines the order in which child UI objects are placed in a layout.
- **Property `VerticalAlignment`** (`VerticalAlignment`): Determines the vertical alignment of UI elements within the parent
- **Method `ApplyLayout(): ()`**: Force re-layout of sibling UI elements. *(deprecated)*
- **Method `SetCustomSortFunction(function?: Function): ()`**: Sets the function used to determine the order of elements when SortOrder *(deprecated)*

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