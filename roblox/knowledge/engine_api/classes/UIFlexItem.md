---
name: UIFlexItem
last_updated: 2026-10-30T19:55:53Z
inherits:
  - UIComponent
  - UIBase
  - Instance
  - Object
type: class
memory_category: Instances
summary: "Defines flex behavior for a GuiObject within a UIListLayout."
---

# Class: UIFlexItem

> Defines flex behavior for a [GuiObject](/docs/reference/engine/classes/GuiObject.md) within a [UIListLayout](/docs/reference/engine/classes/UIListLayout.md).

## Description

The [UIFlexItem](/docs/reference/engine/classes/UIFlexItem.md) object defines flex behavior for its parent
[GuiObject](/docs/reference/engine/classes/GuiObject.md) under the control of a [UIListLayout](/docs/reference/engine/classes/UIListLayout.md). The defined
flex behavior overrides that of the controlling [UIListLayout](/docs/reference/engine/classes/UIListLayout.md), letting
you configure flex behavior on a per‑object basis where necessary.

![Example of UIFlexItem applied to a specific GuiObject under control of a UIListLayout.](../../../assets/ui/ui-objects/UIFlexItem-Example.png)

![Example hierarchy of a UIFlexItem parented to a GuiObject under control of a UIListLayout.](../../../assets/ui/ui-objects/UIFlexItem-Hierarchy.png)

## Properties

### Property: UIFlexItem.FlexMode

```json
{
  "type": "UIFlexMode",
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

[UIFlexMode](/docs/reference/engine/enums/UIFlexMode.md) value which defines how the parent [GuiObject](/docs/reference/engine/classes/GuiObject.md)
grows or shrinks with available space in the
[flex layout](/docs/en-us/ui/list-flex-layouts.md#flex-layouts) container.

When the container's size is **larger** than the flex line's combined
basis size, a value of [UIFlexMode.Grow](/docs/reference/engine/enums/UIFlexMode.md) sets an effective `1:0`
grow‑shrink ratio on the parent [GuiObject](/docs/reference/engine/classes/GuiObject.md). Objects set to
[UIFlexMode.Grow](/docs/reference/engine/enums/UIFlexMode.md) never shrink below their basis size, so overflow
may occur if the container becomes smaller than the line's combined basis
size.

![Diagram showing two items in a line with FlexMode set to Grow.](../../../assets/engine-api/classes/UIListLayout/FlexMode-Grow.png)

When the container's size is **smaller** than the flex line's combined
basis size and the controlling [UIListLayout](/docs/reference/engine/classes/UIListLayout.md) is **not** set to wrap
(resulting in overflow), a value of [UIFlexMode.Shrink](/docs/reference/engine/enums/UIFlexMode.md) sets an
effective `0:1` grow‑shrink ratio on the parent [GuiObject](/docs/reference/engine/classes/GuiObject.md). Objects
set to [UIFlexMode.Shrink](/docs/reference/engine/enums/UIFlexMode.md) never grow above their basis size, so
underflow may occur if the container becomes larger than the line's
combined basis size.

![Diagram showing two items in a line with FlexMode set to Shrink.](../../../assets/engine-api/classes/UIListLayout/FlexMode-Shrink.png)

When the container's size is either larger or smaller than the flex line's
combined basis size, a value of [UIFlexMode.Fill](/docs/reference/engine/enums/UIFlexMode.md) sets an effective
`1:1` grow‑shrink ratio on the parent [GuiObject](/docs/reference/engine/classes/GuiObject.md). This setting
ensures the flex line always fills the container, even if the container
size changes.

![Diagram showing two items in a line with FlexMode set to Fill.](../../../assets/engine-api/classes/UIListLayout/FlexMode-Fill.png)

For fine-tuned layouts, a value of [UIFlexMode.Custom](/docs/reference/engine/enums/UIFlexMode.md) enables the
[GrowRatio](/docs/reference/engine/classes/UIFlexItem.md) and
[ShrinkRatio](/docs/reference/engine/classes/UIFlexItem.md) properties, allowing for
relative growth or shrinking of the object in a ratio compared to other
flex objects also under control of a [UIFlexItem](/docs/reference/engine/classes/UIFlexItem.md).

### Property: UIFlexItem.GrowRatio

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

If there is free space in the flex line, this property determines the
amount the parent [GuiObject](/docs/reference/engine/classes/GuiObject.md) grows relative to other flex items in
the line. Applies only if [FlexMode](/docs/reference/engine/classes/UIFlexItem.md) is set to
[UIFlexMode.Custom](/docs/reference/engine/enums/UIFlexMode.md).

### Property: UIFlexItem.ItemLineAlignment

```json
{
  "type": "ItemLineAlignment",
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

Cross-axis alignment of the specific parent [GuiObject](/docs/reference/engine/classes/GuiObject.md) within the
flex line. See [UIListLayout.ItemLineAlignment](/docs/reference/engine/classes/UIListLayout.md) for details.

### Property: UIFlexItem.ShrinkRatio

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

If there is overflow in the flex line, this property determines the amount
the parent [GuiObject](/docs/reference/engine/classes/GuiObject.md) shrinks relative to other flex items in the
line. Applies only if [FlexMode](/docs/reference/engine/classes/UIFlexItem.md) is set to
[UIFlexMode.Custom](/docs/reference/engine/enums/UIFlexMode.md).

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