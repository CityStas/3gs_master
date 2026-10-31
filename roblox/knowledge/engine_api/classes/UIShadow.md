---
name: UIShadow
last_updated: 2026-10-30T19:55:53Z
inherits:
  - UIComponent
  - UIBase
  - Instance
  - Object
type: class
memory_category: Instances
summary: "Renders configurable shape or text shadows for the parent UI instance."
---

# Class: UIShadow

> Renders configurable shape or text shadows for the parent UI instance.

## Description

`UIShadow` renders a shadow for its parent UI instance. Key features include:

- Adjust the shadow's blurriness with [BlurRadius](/docs/reference/engine/classes/UIShadow.md).
- Adjust the shadow's color and transparency with [Color](/docs/reference/engine/classes/UIShadow.md)
  and [Transparency](/docs/reference/engine/classes/UIShadow.md).
- Adjust the shadow's position and size relative to the parent with
  [Offset](/docs/reference/engine/classes/UIShadow.md) and [Spread](/docs/reference/engine/classes/UIShadow.md).
- Add multiple shadows under the same parent and adjust their render order
  with [ZIndex](/docs/reference/engine/classes/UIShadow.md).
- Add a shadow to the text in [TextLabel](/docs/reference/engine/classes/TextLabel.md), [TextButton](/docs/reference/engine/classes/TextButton.md), or
  [TextBox](/docs/reference/engine/classes/TextBox.md) with [Mode](/docs/reference/engine/classes/UIShadow.md).
- Add an inset shadow with [Inset](/docs/reference/engine/classes/UIShadow.md).
- Hide the part of the shadow directly behind the parent with
  [ShowBehindParent](/docs/reference/engine/classes/UIShadow.md).
- Apply a gradient to a shadow's color with a child [UIGradient](/docs/reference/engine/classes/UIGradient.md).
- If the parent is rotated with [GuiObject.Rotation](/docs/reference/engine/classes/GuiObject.md), the shadow will
  also be rotated.
- If the parent has round corners with [UICorner](/docs/reference/engine/classes/UICorner.md), the shadow will also
  have round corners.

#### Limitations

- `UIShadow` does not support [Path2D](/docs/reference/engine/classes/Path2D.md).
- You cannot apply textures to a `UIShadow`.

## Properties

### Property: UIShadow.BlurRadius

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

This property determines the shadow's blurriness. A larger value makes the
shadow's edges appear softer.

Note that the scale factor of this [UDim](/docs/reference/engine/datatypes/UDim.md) property is relative to
the parent's width or height, whichever is shorter. This property must
also be non-negative; a negative value will be treated as `0`.

### Property: UIShadow.Color

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

This property determines the shadow's color.

### Property: UIShadow.Enabled

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

This property determines whether the `UIShadow` is visible. Default is
`true`.

### Property: UIShadow.Inset

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

When `true`, the shadow appears on top of and inside the parent. When
`false`, the shadow appears behind the parent.

Defaults to `false`. This property has no effect when
[Mode](/docs/reference/engine/classes/UIShadow.md) is [ApplyShadowMode.Text](/docs/reference/engine/enums/ApplyShadowMode.md).

### Property: UIShadow.Mode

```json
{
  "type": "ApplyShadowMode",
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

Determines whether the shadow applies to the parent's shape or text.
Defaults to [ApplyShadowMode.Shape](/docs/reference/engine/enums/ApplyShadowMode.md), which renders a shadow for the
parent's rectangular area.

[ApplyShadowMode.Text](/docs/reference/engine/enums/ApplyShadowMode.md) renders a shadow for text in a
[TextLabel](/docs/reference/engine/classes/TextLabel.md), [TextButton](/docs/reference/engine/classes/TextButton.md), or [TextBox](/docs/reference/engine/classes/TextBox.md). On other
classes, text mode renders no shadow.

[Shape](/docs/reference/engine/enums/ApplyShadowMode.md) mode and
[Text](/docs/reference/engine/enums/ApplyShadowMode.md) mode shadows can coexist under the same
parent.

The following properties have no effect in text mode:

- [Spread](/docs/reference/engine/classes/UIShadow.md)
- [Inset](/docs/reference/engine/classes/UIShadow.md)
- [ShowBehindParent](/docs/reference/engine/classes/UIShadow.md)

### Property: UIShadow.Offset

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
  "category": "Appearance",
  "capabilities": [
    "UI"
  ]
}
```

This property moves the shadow relative to the parent's position. The X
scale factor is relative to the parent's width, and the Y scale factor is
relative to the parent's height.

### Property: UIShadow.ShowBehindParent

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

When `true`, the entire shadow is rendered. When `false`, the parent's
shape masks the portion of the shadow directly behind it. Disabling this
property prevents a shadow from obscuring content behind a transparent
parent.

Defaults to `true`. This property has no effect when
[Mode](/docs/reference/engine/classes/UIShadow.md) is [ApplyShadowMode.Text](/docs/reference/engine/enums/ApplyShadowMode.md) or
[Inset](/docs/reference/engine/classes/UIShadow.md) is `true`.

### Property: UIShadow.Spread

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
  "category": "Appearance",
  "capabilities": [
    "UI"
  ]
}
```

This property expands or shrinks the shadow relative to the parent's size.
The X scale factor is relative to the parent's width, and the Y scale
factor is relative to the parent's height. Properties that are relative to
the parent's size, such as the scale factors of
[BlurRadius](/docs/reference/engine/classes/UIShadow.md) and [Offset](/docs/reference/engine/classes/UIShadow.md),
are not affected by `Spread`.

This property has no effect when [Mode](/docs/reference/engine/classes/UIShadow.md) is
[ApplyShadowMode.Text](/docs/reference/engine/enums/ApplyShadowMode.md).

When [Inset](/docs/reference/engine/classes/UIShadow.md) is `true`, positive `Spread` values
expand the shadow toward the center of the parent instead of outward.

### Property: UIShadow.Transparency

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

This property sets the shadow's transparency, with `0` being fully opaque
and `1` being fully transparent.

### Property: UIShadow.ZIndex

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

If a UI instance has multiple shadows, they are rendered in order of
increasing `ZIndex`. Since all shadows are rendered below the parent
instance, `ZIndex` can only be negative.

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