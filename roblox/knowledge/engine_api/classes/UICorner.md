---
name: UICorner
last_updated: 2026-10-30T19:55:53Z
inherits:
  - UIComponent
  - UIBase
  - Instance
  - Object
type: class
memory_category: Instances
summary: "UI modifier which applies deformation to corners of its parent GuiObject."
---

# Class: UICorner

> UI modifier which applies deformation to corners of its parent
> [GuiObject](/docs/reference/engine/classes/GuiObject.md).

## Description

`UICorner` is a modifier which applies deformation to corners of its parent
[GuiObject](/docs/reference/engine/classes/GuiObject.md). Input, but not descendants, will be clipped to the round
corner area. See
[UI appearance modifiers](/docs/en-us/ui/appearance-modifiers.md#corners) for
examples.

In order to keep the circular shape of round corners, each corner radius
([UDim](/docs/reference/engine/datatypes/UDim.md)) is internally calculated as follows:

- The radius of the **X** axis is always the same as the radius of **Y** axis.
- [Scale](/docs/reference/engine/datatypes/UDim.md) rounding will always apply to the **minimum**
  width or height.
- Rounded rectangles will always be in a "pill" shape if
  [CornerRadius](/docs/reference/engine/classes/UICorner.md) is set to a value that leads to a
  calculated result greater than half of the rectangle's minimum width or
  height.

Alternatively to `UICorner`, rounded corners can be accomplished using
**slices** which are suitable for decorative borders that are not simply
rounded. See [9‑Slice Design](/docs/en-us/ui/9-slice.md) for details.

Note that `UICorner` can not be applied to a [ScrollingFrame](/docs/reference/engine/classes/ScrollingFrame.md).

#### Individual Corners

Each corner has its own radius property
([TopLeftRadius](/docs/reference/engine/classes/UICorner.md),
[TopRightRadius](/docs/reference/engine/classes/UICorner.md),
[BottomRightRadius](/docs/reference/engine/classes/UICorner.md),
[BottomLeftRadius](/docs/reference/engine/classes/UICorner.md)). The
[CornerRadius](/docs/reference/engine/classes/UICorner.md) property is a convenience shorthand
that sets all four corners at once and reads from
[TopLeftRadius](/docs/reference/engine/classes/UICorner.md).

When using [styling](/docs/en-us/ui/styling.md) with `UICorner`, avoid
configuring both [CornerRadius](/docs/reference/engine/classes/UICorner.md) and the individual
corner radii in style rules at the same time, as this may produce unexpected
results.

## Properties

### Property: UICorner.BottomLeftRadius

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
  "category": "Individual Corners",
  "capabilities": [
    "UI"
  ]
}
```

This property is currently in beta. To use it, enable **New UI
Capabilities** in Studio's beta features window.

A [UDim](/docs/reference/engine/datatypes/UDim.md) property that determines the radius of the bottom-left
corner independently. Setting [CornerRadius](/docs/reference/engine/classes/UICorner.md)
overwrites all four individual corner radii to the same value.

### Property: UICorner.BottomRightRadius

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
  "category": "Individual Corners",
  "capabilities": [
    "UI"
  ]
}
```

This property is currently in beta. To use it, enable **New UI
Capabilities** in Studio's beta features window.

A [UDim](/docs/reference/engine/datatypes/UDim.md) property that determines the radius of the bottom-right
corner independently. Setting [CornerRadius](/docs/reference/engine/classes/UICorner.md)
overwrites all four individual corner radii to the same value.

### Property: UICorner.CornerRadius

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
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Appearance",
  "capabilities": [
    "UI"
  ]
}
```

A convenience [UDim](/docs/reference/engine/datatypes/UDim.md) property that acts as a shorthand for the
four individual corner radius properties. Writing to this property sets
[TopLeftRadius](/docs/reference/engine/classes/UICorner.md),
[TopRightRadius](/docs/reference/engine/classes/UICorner.md),
[BottomRightRadius](/docs/reference/engine/classes/UICorner.md), and
[BottomLeftRadius](/docs/reference/engine/classes/UICorner.md) to the same value.
Reading this property returns the value of
[TopLeftRadius](/docs/reference/engine/classes/UICorner.md).

### Property: UICorner.TopLeftRadius

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
  "category": "Individual Corners",
  "capabilities": [
    "UI"
  ]
}
```

This property is currently in beta. To use it, enable **New UI
Capabilities** in Studio's beta features window.

A [UDim](/docs/reference/engine/datatypes/UDim.md) property that determines the radius of the top-left
corner independently. Setting [CornerRadius](/docs/reference/engine/classes/UICorner.md)
overwrites all four individual corner radii to the same value.

### Property: UICorner.TopRightRadius

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
  "category": "Individual Corners",
  "capabilities": [
    "UI"
  ]
}
```

This property is currently in beta. To use it, enable **New UI
Capabilities** in Studio's beta features window.

A [UDim](/docs/reference/engine/datatypes/UDim.md) property that determines the radius of the top-right
corner independently. Setting [CornerRadius](/docs/reference/engine/classes/UICorner.md)
overwrites all four individual corner radii to the same value.

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