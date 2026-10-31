---
name: UIStroke
last_updated: 2026-10-30T19:55:53Z
inherits:
  - UIComponent
  - UIBase
  - Instance
  - Object
type: class
memory_category: Instances
summary: "Applies an outline to text or a UI border."
---

# Class: UIStroke

> Applies an outline to text or a UI border.

## Description

[UIStroke](/docs/reference/engine/classes/UIStroke.md) applies an outline to text or a UI border. Some properties
may require enabling the
[Improved UIStrokes beta](https://devforum.roblox.com/t/studio-beta-uistroke-improvements-scaling-offsets-and-more/3958036).

Key features include:

- Adjust the [Color](/docs/reference/engine/classes/UIStroke.md) and
  [Thickness](/docs/reference/engine/classes/UIStroke.md) of the stroke outline.
- Change the stroke [Transparency](/docs/reference/engine/classes/UIStroke.md) independently
  from the text or UI object.
- Choose the [LineJoinMode](/docs/reference/engine/classes/UIStroke.md) of the stroke (round,
  bevel, or miter).
- Specify the [BorderStrokePosition](/docs/reference/engine/classes/UIStroke.md) on
  its parent's border and/or an additional
  [BorderOffset](/docs/reference/engine/classes/UIStroke.md) to the stroke's position.
- Add a gradient to the stroke via the [UIGradient](/docs/reference/engine/classes/UIGradient.md) instance.
- Use [rich text](/docs/en-us/ui/rich-text.md) tags to add stroke to inline text
  segments.

For more details on the [UIStroke](/docs/reference/engine/classes/UIStroke.md) object, see
[Appearance Modifiers](/docs/en-us/ui/appearance-modifiers.md).

## Properties

### Property: UIStroke.ApplyStrokeMode

```json
{
  "type": "ApplyStrokeMode",
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

When a [UIStroke](/docs/reference/engine/classes/UIStroke.md) instance is applied to a text object, this
property determines whether to apply the stroke to the object's border
instead of the text itself.

_`ApplyStrokeMode` = [Contextual](/docs/reference/engine/enums/ApplyStrokeMode.md)_
_`ApplyStrokeMode` = [Border](/docs/reference/engine/enums/ApplyStrokeMode.md)_

### Property: UIStroke.BorderOffset

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

This property specifies an additional offset ([UDim](/docs/reference/engine/datatypes/UDim.md)) to the
stroke's position, relative to the parent's minimum height or width.

_`BorderOffset` = `(0.15, 0)`_
_`BorderOffset` = `(0, -16)`_

### Property: UIStroke.BorderStrokePosition

```json
{
  "type": "BorderStrokePosition",
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

This property determines the stroke's position on its parent's border as
an [BorderStrokePosition](/docs/reference/engine/enums/BorderStrokePosition.md) value.

_`BorderStrokePosition` = [Center](/docs/reference/engine/enums/BorderStrokePosition.md)_
_`BorderStrokePosition` = [Inner](/docs/reference/engine/enums/BorderStrokePosition.md)_
_`BorderStrokePosition` = [Outer](/docs/reference/engine/enums/BorderStrokePosition.md)_

### Property: UIStroke.Color

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

Determines the [UIStroke](/docs/reference/engine/classes/UIStroke.md) color. You can also insert a
[UIGradient](/docs/reference/engine/classes/UIGradient.md) instance as a child to create gradient strokes.

_`Color` = `(0, 95, 225)`_
_`UIStroke` with [UIGradient](/docs/reference/engine/classes/UIGradient.md) child_

### Property: UIStroke.Enabled

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

This property determines whether the [UIStroke](/docs/reference/engine/classes/UIStroke.md) is visible. When set
to `false`, the stroke will not be rendered. Defaults to `true`.

### Property: UIStroke.LineJoinMode

```json
{
  "type": "LineJoinMode",
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

This property determines how corners are interpreted. It accepts an
[LineJoinMode](/docs/reference/engine/enums/LineJoinMode.md) value of either [Round](/docs/reference/engine/enums/LineJoinMode.md)
(default), [Bevel](/docs/reference/engine/enums/LineJoinMode.md), or
[Miter](/docs/reference/engine/enums/LineJoinMode.md).

_`LineJoinMode` = [Round](/docs/reference/engine/enums/LineJoinMode.md)_
_`LineJoinMode` = [Bevel](/docs/reference/engine/enums/LineJoinMode.md)_
_`LineJoinMode` = [Miter](/docs/reference/engine/enums/LineJoinMode.md)_

### Property: UIStroke.StrokeSizingMode

```json
{
  "type": "StrokeSizingMode",
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

This property determines whether the stroke's
[Thickness](/docs/reference/engine/classes/UIStroke.md) will be measured in pixels or be
scaled relative to the parent. See [StrokeSizingMode](/docs/reference/engine/enums/StrokeSizingMode.md) for further
details.

### Property: UIStroke.Thickness

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

This property determines the stroke's thickness, measured in pixels
(default) or scaled relative to the parent, depending on
[StrokeSizingMode](/docs/reference/engine/classes/UIStroke.md).

_`Thickness` = `4`_
_`Thickness` = `12`_

Be mindful of [tweening](/docs/en-us/ui/animation.md) this [UIStroke](/docs/reference/engine/classes/UIStroke.md)
property when applied to text objects. This renders and stores many glyph
sizes each frame, potentially causing performance issues or text
flickering.

### Property: UIStroke.Transparency

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

This property sets the stroke opacity independently of the parent object's
[BackgroundTransparency](/docs/reference/engine/classes/GuiObject.md) or
[TextTransparency](/docs/reference/engine/classes/TextLabel.md). This allows you to
render text and borders that are "hollow" (consisting of only an outline).

_`Transparency` = `0.5`  ·  [TextLabel.TextTransparency](/docs/reference/engine/classes/TextLabel.md) = `0`_
_`Transparency` = `0`  ·  [TextLabel.TextTransparency](/docs/reference/engine/classes/TextLabel.md) = `1`_

### Property: UIStroke.ZIndex

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
  "category": "Appearance",
  "capabilities": [
    "UI"
  ]
}
```

This property determines the order in which the stroke renders relative to
sibling [UIStroke](/docs/reference/engine/classes/UIStroke.md) instances. Those with a lower `ZIndex` render
under (behind) those with a higher `ZIndex`.

Note that the rendering order for [UIStroke](/docs/reference/engine/classes/UIStroke.md) instances with the same
`ZIndex` is undefined. Do not apply multiple [UIStroke](/docs/reference/engine/classes/UIStroke.md) instances
with the same `ZIndex` if their rendering order matters.

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