---
name: UIGradient
last_updated: 2026-10-30T19:55:53Z
inherits:
  - UIComponent
  - UIBase
  - Instance
  - Object
type: class
memory_category: Instances
summary: "Applies a color and transparency gradient to the parent GuiObject."
---

# Class: UIGradient

> Applies a color and transparency gradient to the parent [GuiObject](/docs/reference/engine/classes/GuiObject.md).

## Description

`UIGradient` applies a color and transparency gradient to the parent
[GuiObject](/docs/reference/engine/classes/GuiObject.md). The appearance of the gradient is configurable through its
[Color](/docs/reference/engine/classes/UIGradient.md), [Transparency](/docs/reference/engine/classes/UIGradient.md),
[Offset](/docs/reference/engine/classes/UIGradient.md), [Rotation](/docs/reference/engine/classes/UIGradient.md),
[Scale](/docs/reference/engine/classes/UIGradient.md), [TileMode](/docs/reference/engine/classes/UIGradient.md), and
[Type](/docs/reference/engine/classes/UIGradient.md).

`UIGradient` will not apply to child or descendant
[GuiObjects](/docs/reference/engine/classes/GuiObject.md). In order to apply the same gradient to multiple
objects, you will need multiple gradient instances.

See also [appearance modifiers](/docs/en-us/ui/appearance-modifiers.md#gradient)
for more information on the `UIGradient` modifier and how it works.

#### Supported Objects

You can apply `UIGradient` modifiers to [Frame](/docs/reference/engine/classes/Frame.md), [TextLabel](/docs/reference/engine/classes/TextLabel.md),
[TextButton](/docs/reference/engine/classes/TextButton.md), [ImageLabel](/docs/reference/engine/classes/ImageLabel.md), [ImageButton](/docs/reference/engine/classes/ImageButton.md), [Path2D](/docs/reference/engine/classes/Path2D.md),
and [ViewportFrame](/docs/reference/engine/classes/ViewportFrame.md). However, [ScrollingFrame](/docs/reference/engine/classes/ScrollingFrame.md) and [TextBox](/docs/reference/engine/classes/TextBox.md)
are not currently supported.

#### Performance Considerations

In order to efficiently use a `UIGradient`, follow these principles:

- Avoid using more than 6 color stops on the [Color](/docs/reference/engine/classes/UIGradient.md)
  sequence.

- Avoid using a `UIGradient` on any object that applies a text stroke
  ([TextStrokeColor3](/docs/reference/engine/classes/TextLabel.md)), as the gradient will
  try to blend with strokes and borders, and may cause performance issues.

- Avoid setting [Color](/docs/reference/engine/classes/UIGradient.md) and
  [Transparency](/docs/reference/engine/classes/UIGradient.md) frequently: this causes the
  sequence of colors to rebuild often, which is expensive. If possible, set
  these properties only once and try to animate the
  [Offset](/docs/reference/engine/classes/UIGradient.md) or [Rotation](/docs/reference/engine/classes/UIGradient.md)
  properties to achieve a similar effect. Alternatively, you can change the
  color of the parent [GuiObject](/docs/reference/engine/classes/GuiObject.md) using such properties as
  [BackgroundColor3](/docs/reference/engine/classes/GuiObject.md),
  [ImageColor3](/docs/reference/engine/classes/ImageLabel.md), or
  [TextColor3](/docs/reference/engine/classes/TextLabel.md).

- When applying an unchanging gradient on a UI element whose state changes a
  lot, there is a tradeoff between using a `UIGradient` (processing time) and
  a static gradient image (memory).

## Properties

### Property: UIGradient.Color

```json
{
  "type": "ColorSequence",
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

This property describes the color to blend with the parent
[GuiObject](/docs/reference/engine/classes/GuiObject.md) along the provided [ColorSequence](/docs/reference/engine/datatypes/ColorSequence.md). This
property works in a similar manner to [Beam.Color](/docs/reference/engine/classes/Beam.md) or
[Trail.Color](/docs/reference/engine/classes/Trail.md), except that it applies over a distance determined by
the [Offset](/docs/reference/engine/classes/UIGradient.md) and
[Rotation](/docs/reference/engine/classes/UIGradient.md).

### Property: UIGradient.Enabled

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

Whether the gradient is enabled or not.

### Property: UIGradient.Offset

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
  "category": "Appearance",
  "capabilities": [
    "UI"
  ]
}
```

This property determines the scalar translation of the gradient from the
center of the parent [GuiObject](/docs/reference/engine/classes/GuiObject.md). It is a scalar translation,
meaning that the actual pixel offset is determined by the
[AbsoluteSize](/docs/reference/engine/classes/GuiBase2d.md) of the parent
[GuiObject](/docs/reference/engine/classes/GuiObject.md). For example, a value of `(1, 0)` shifts the gradient
horizontally to the right by a distance equal to the parent object's size.
Depending on the [Rotation](/docs/reference/engine/classes/UIGradient.md), this may cause the
gradient to be partially visible or not visible at all.

Also see [Rotation](/docs/reference/engine/classes/UIGradient.md) which also affects the
geometry of the applied gradient.

### Property: UIGradient.Rotation

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

This property determines the **clockwise** rotation in degrees of the
`UIGradient` starting from left to right. The beginning and end control
points snap to the edges of the parent [GuiObject](/docs/reference/engine/classes/GuiObject.md), but maintain the
provided rotation.

Also see [Offset](/docs/reference/engine/classes/UIGradient.md) which also affects the geometry
of the applied gradient.

### Property: UIGradient.Scale

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

This property multiplies the extent of the gradient, controlling how much
of the color/transparency sequence is visible within the parent
[GuiObject](/docs/reference/engine/classes/GuiObject.md).

- A value of `1` (default) means the full sequence spans the element
  exactly once.

- Values **less** than `1` compress the gradient so that the full sequence
  fits in a smaller region. The remaining area is determined by
  [TileMode](/docs/reference/engine/classes/UIGradient.md). Note that `Scale` is clamped to a
  minimum of `0.001` to avoid degenerate gradients.

- Values **greater** than `1` stretch the gradient beyond the element
  bounds so that only a portion of the sequence is visible.

The effect of `Scale` also depends on the gradient's
[Type](/docs/reference/engine/classes/UIGradient.md):

- [GradientType.Linear](/docs/reference/engine/enums/GradientType.md) — `Scale` affects the distance between the
  start and end control points.

- [GradientType.Radial](/docs/reference/engine/enums/GradientType.md) — `Scale` affects the radius of the radial
  gradient.

- [GradientType.Elliptical](/docs/reference/engine/enums/GradientType.md) — `Scale` affects both radii of the
  elliptical gradient.

- [GradientType.Conical](/docs/reference/engine/enums/GradientType.md) — `Scale` affects the angular sweep, clamped
  so that the sweep does not exceed a full revolution.

See also [TileMode](/docs/reference/engine/classes/UIGradient.md) which determines how the
gradient repeats when `Scale` causes it to not fill the entire element.

### Property: UIGradient.TileMode

```json
{
  "type": "GradientTileMode",
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

This property determines what happens when the gradient
[Scale](/docs/reference/engine/classes/UIGradient.md) is less than `1` or when
[Offset](/docs/reference/engine/classes/UIGradient.md) shifts the gradient so that it does not
fully cover the element. See [GradientTileMode](/docs/reference/engine/enums/GradientTileMode.md) for possible values
and their effect.

See also [Scale](/docs/reference/engine/classes/UIGradient.md) which controls how much of the
color/transparency sequence is visible.

### Property: UIGradient.Transparency

```json
{
  "type": "NumberSequence",
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

This property describes how opaque the parent UI element will be along the
provided [NumberSequence](/docs/reference/engine/datatypes/NumberSequence.md). This property works in a similar
manner to [Beam.Transparency](/docs/reference/engine/classes/Beam.md) or [Trail.Transparency](/docs/reference/engine/classes/Trail.md), except
that it applies over a distance determined by the
[Offset](/docs/reference/engine/classes/UIGradient.md) and [Rotation](/docs/reference/engine/classes/UIGradient.md).

Note that the envelope values of the
[NumberSequenceKeypoints](/docs/reference/engine/datatypes/NumberSequenceKeypoint.md) are ignored.

### Property: UIGradient.Type

```json
{
  "type": "GradientType",
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

This property determines how the gradient varies across the parent
[GuiObject](/docs/reference/engine/classes/GuiObject.md). See [GradientType](/docs/reference/engine/enums/GradientType.md) for possible values and their
effect.

See also [Scale](/docs/reference/engine/classes/UIGradient.md) which controls how much of the
color/transparency sequence is visible, and
[TileMode](/docs/reference/engine/classes/UIGradient.md) which determines repetition behavior.

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