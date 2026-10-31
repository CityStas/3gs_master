---
name: UIListLayout
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
summary: "Positions sibling UI elements in rows or columns within the parent UI container."
---

# Class: UIListLayout

> Positions sibling UI elements in rows or columns within the parent UI
> container.

## Description

A [UIListLayout](/docs/reference/engine/classes/UIListLayout.md) positions sibling UI elements in rows or columns within
the parent UI container, based on the
[FillDirection](/docs/reference/engine/classes/UIListLayout.md). The
[Position](/docs/reference/engine/classes/GuiObject.md) and [Rotation](/docs/reference/engine/classes/GuiObject.md)
properties of each sibling [GuiObject](/docs/reference/engine/classes/GuiObject.md) are either ignored or overridden
by the list layout, while each sibling retains its defined
[Size](/docs/reference/engine/classes/GuiObject.md) unless the layout is configured to utilize a flex
layout. See [List and Flex Layouts](/docs/en-us/ui/list-flex-layouts.md) for
further information.

![UIListLayouts illustrating FillDirection of either horizontal
or vertical.](../../../assets/engine-api/classes/UIListLayout/FillDirection.png)

To control the layout order of siblings, set
[SortOrder](/docs/reference/engine/classes/UIListLayout.md) to either [SortOrder.Name](/docs/reference/engine/enums/SortOrder.md) or
[SortOrder.LayoutOrder](/docs/reference/engine/enums/SortOrder.md), then rename siblings in alphanumerical order or
set their [LayoutOrder](/docs/reference/engine/classes/GuiObject.md) value, respectively.
[UIListLayout](/docs/reference/engine/classes/UIListLayout.md) will automatically re‑layout elements when elements are
added/removed, or if a sibling's [Name](/docs/reference/engine/classes/Instance.md) or
[LayoutOrder](/docs/reference/engine/classes/GuiObject.md) changes.

![List layout examples illustrating numerical LayoutOrder
sorting or alphanumerical Name sorting.](../../../assets/engine-api/classes/UIListLayout/SortOrder.png)

Padding between siblings is controlled through the
[Padding](/docs/reference/engine/classes/UIListLayout.md) property, and wrapping within the parent
container's bounds through the [Wraps](/docs/reference/engine/classes/UIListLayout.md) boolean.
Alignment of siblings within the parent container is controlled through
[HorizontalAlignment](/docs/reference/engine/classes/UIListLayout.md) and
[VerticalAlignment](/docs/reference/engine/classes/UIListLayout.md) unless the layout is
configured to utilize a
[flex layout](/docs/en-us/ui/list-flex-layouts.md#flex-layouts).

Note that there are performance implications of using a
[flex‑enabled](/docs/en-us/ui/list-flex-layouts.md#flex-layouts) list layout,
since extra calculations are needed to calculate flex basis sizes, flexed
sizes, and line wrapping. Flex is enabled on a [UIListLayout](/docs/reference/engine/classes/UIListLayout.md) when the
following properties are set, or if any [GuiObject](/docs/reference/engine/classes/GuiObject.md) sibling has a
[UIFlexItem](/docs/reference/engine/classes/UIFlexItem.md) parented to it:

- [HorizontalFlex](/docs/reference/engine/classes/UIListLayout.md) and/or
  [VerticalFlex](/docs/reference/engine/classes/UIListLayout.md) are **not** set to
  [UIFlexAlignment.None](/docs/reference/engine/enums/UIFlexAlignment.md).
- [ItemLineAlignment](/docs/reference/engine/classes/UIListLayout.md) is **not** set to
  [ItemLineAlignment.Automatic](/docs/reference/engine/enums/ItemLineAlignment.md).
- [Wraps](/docs/reference/engine/classes/UIListLayout.md) is `true`.

## Properties

### Property: UIListLayout.HorizontalFlex

```json
{
  "type": "UIFlexAlignment",
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
  "category": "Alignment",
  "capabilities": [
    "UI"
  ]
}
```

When the list layout's [FillDirection](/docs/reference/engine/classes/UIListLayout.md) is
set to [FillDirection.Horizontal](/docs/reference/engine/enums/FillDirection.md), the
[HorizontalFlex](/docs/reference/engine/classes/UIListLayout.md) property specifies how
to distribute extra horizontal space in the parent container.

| Setting | Sibling Behavior |
| --- | --- |
| [None](/docs/reference/engine/enums/UIFlexAlignment.md) | No flex behavior; siblings maintain their defined width. |
| [Fill](/docs/reference/engine/enums/UIFlexAlignment.md) | Siblings resize horizontally to fill the entire parent container, overriding their defined width. The number of siblings in a row remain unchanged; for example, if three siblings fit horizontally within the container's width under the [None](/docs/reference/engine/enums/UIFlexAlignment.md) setting, those three siblings will resize to fill the entire width. |
| [SpaceAround](/docs/reference/engine/enums/UIFlexAlignment.md) | Siblings maintain their defined width. Equal spacing is added on both sides of each sibling. |
| [SpaceBetween](/docs/reference/engine/enums/UIFlexAlignment.md) | Siblings maintain their defined width. Equal spacing is added **between** siblings, but no additional space is added **around** siblings. |
| [SpaceEvenly](/docs/reference/engine/enums/UIFlexAlignment.md) | Siblings maintain their defined width. Equal spacing is added both **between** and **around** siblings. |

![UIListLayout examples showing how each HorizontalFlex option affects the size and spacing of sibling UI objects.](../../../assets/engine-api/classes/UIListLayout/HorizontalFlex-Options.png)

##### Cross-Direction Behavior

In **vertical** list layouts
([FillDirection](/docs/reference/engine/classes/UIListLayout.md) set to
[FillDirection.Vertical](/docs/reference/engine/enums/FillDirection.md)), the
[HorizontalFlex](/docs/reference/engine/classes/UIListLayout.md) property specifies how
to distribute the siblings across the **horizontal cross‑direction**. In
such layouts, a setting of [UIFlexAlignment.Fill](/docs/reference/engine/enums/UIFlexAlignment.md) makes the siblings
fill the entire horizontal space while vertical spacing adheres to
[VerticalFlex](/docs/reference/engine/classes/UIListLayout.md).

![Diagram showing how HorizontalFlex affects the horizontal size of sibling UI objects when the UIListLayout fill direction is set to vertical.](../../../assets/engine-api/classes/UIListLayout/HorizontalFlex-Cross-Direction.png)

##### AutomaticSize Interaction

If [GuiObject.AutomaticSize](/docs/reference/engine/classes/GuiObject.md) is enabled for a child of the
[UIListLayout](/docs/reference/engine/classes/UIListLayout.md) in the
[FillDirection](/docs/reference/engine/classes/UIListLayout.md), it is interpreted as
"automatic flex basis" and it defines the size of the [GuiObject](/docs/reference/engine/classes/GuiObject.md)
from which it can grow or shrink.

If [GuiObject.AutomaticSize](/docs/reference/engine/classes/GuiObject.md) is enabled for a child of the
[UIListLayout](/docs/reference/engine/classes/UIListLayout.md) in the **cross‑direction**, it is interpreted as
"automatic cross size" and it defines the minimum size needed to contain
all the child's content in the cross‑direction.

### Property: UIListLayout.ItemLineAlignment

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
  "category": "Alignment",
  "capabilities": [
    "UI"
  ]
}
```

In a [flex layout](/docs/en-us/ui/list-flex-layouts.md#flex-layouts), defines
the **cross-directional** alignment of siblings within a line. See
[ItemLineAlignment](/docs/reference/engine/enums/ItemLineAlignment.md) for visual examples.

| Setting | Sibling Behavior |
| --- | --- |
| [Automatic](/docs/reference/engine/enums/ItemLineAlignment.md) | Aligns the layout's siblings or the specific [UIFlexItem](/docs/reference/engine/classes/UIFlexItem.md) parent to the layout's [HorizontalAlignment](/docs/reference/engine/classes/UIListLayout.md) or [VerticalAlignment](/docs/reference/engine/classes/UIListLayout.md), depending on its [FillDirection](/docs/reference/engine/classes/UIListLayout.md). |
| [Start](/docs/reference/engine/enums/ItemLineAlignment.md) | Aligns the layout's siblings or the specific [UIFlexItem](/docs/reference/engine/classes/UIFlexItem.md) parent to the line's **top** in a horizontal fill or the line's **left** in a vertical fill. |
| [Center](/docs/reference/engine/enums/ItemLineAlignment.md) | Aligns the layout's siblings or the specific [UIFlexItem](/docs/reference/engine/classes/UIFlexItem.md) parent to the line's **center** in either a horizontal or vertical fill. |
| [End](/docs/reference/engine/enums/ItemLineAlignment.md) | Aligns the layout's siblings or the specific [UIFlexItem](/docs/reference/engine/classes/UIFlexItem.md) parent to the line's **bottom** in a horizontal fill or the line's **right** in a vertical fill. |
| [Stretch](/docs/reference/engine/enums/ItemLineAlignment.md) | Stretches the layout's siblings or the specific [UIFlexItem](/docs/reference/engine/classes/UIFlexItem.md) parent to fill the entire cross‑direction of the line in either a horizontal or vertical fill. |

![Examples of options for ItemLineAlignment in a horizontal fill direction.](../../../assets/engine-api/classes/UIListLayout/ItemLineAlignment.png)

### Property: UIListLayout.Padding

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

Determines the amount of free space between each element, set to either a
scale (percentage of the parent's size in the current direction) or an
offset (static spacing value similar to pixel size).

### Property: UIListLayout.VerticalFlex

```json
{
  "type": "UIFlexAlignment",
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
  "category": "Alignment",
  "capabilities": [
    "UI"
  ]
}
```

When the list layout's [FillDirection](/docs/reference/engine/classes/UIListLayout.md) is
set to [FillDirection.Vertical](/docs/reference/engine/enums/FillDirection.md), the
[VerticalFlex](/docs/reference/engine/classes/UIListLayout.md) property specifies how to
distribute extra vertical space in the parent container.

| Setting | Sibling Behavior |
| --- | --- |
| [None](/docs/reference/engine/enums/UIFlexAlignment.md) | No flex behavior; siblings maintain their defined height. |
| [Fill](/docs/reference/engine/enums/UIFlexAlignment.md) | Siblings resize vertically to fill the entire parent container, overriding their defined height. The number of siblings in a column remain unchanged; for example, if three siblings fit vertically within the container's height under the [None](/docs/reference/engine/enums/UIFlexAlignment.md) setting, those three siblings will resize to fill the entire height. |
| [SpaceAround](/docs/reference/engine/enums/UIFlexAlignment.md) | Siblings maintain their defined height. Equal spacing is added on both sides of each sibling. |
| [SpaceBetween](/docs/reference/engine/enums/UIFlexAlignment.md) | Siblings maintain their defined height. Equal spacing is added **between** siblings, but no additional space is added **around** siblings. |
| [SpaceEvenly](/docs/reference/engine/enums/UIFlexAlignment.md) | Siblings maintain their defined height. Equal spacing is added both **between** and **around** siblings. |

![UIListLayout examples showing how each VerticalFlex option affects the size and spacing of sibling UI objects.](../../../assets/engine-api/classes/UIListLayout/VerticalFlex-Options.png)

##### Cross-Direction Behavior

In **horizontal** list layouts
([FillDirection](/docs/reference/engine/classes/UIListLayout.md) set to
[FillDirection.Horizontal](/docs/reference/engine/enums/FillDirection.md)), the
[VerticalFlex](/docs/reference/engine/classes/UIListLayout.md) property specifies how to
distribute the siblings across the **vertical cross direction**. In such
layouts, a setting of [UIFlexAlignment.Fill](/docs/reference/engine/enums/UIFlexAlignment.md) makes the siblings fill
the entire vertical space while horizontal spacing adheres to
[HorizontalFlex](/docs/reference/engine/classes/UIListLayout.md).

![Diagram showing how VerticalFlex affects the vertical size of sibling UI objects when the UIListLayout fill direction is set to horizontal.](../../../assets/engine-api/classes/UIListLayout/VerticalFlex-Cross-Direction.png)

##### AutomaticSize Interaction

If [GuiObject.AutomaticSize](/docs/reference/engine/classes/GuiObject.md) is enabled for a child of the
[UIListLayout](/docs/reference/engine/classes/UIListLayout.md) in the
[FillDirection](/docs/reference/engine/classes/UIListLayout.md), it is interpreted as
"automatic flex basis" and it defines the size of the [GuiObject](/docs/reference/engine/classes/GuiObject.md)
from which it can grow or shrink.

If [GuiObject.AutomaticSize](/docs/reference/engine/classes/GuiObject.md) is enabled for a child of the
[UIListLayout](/docs/reference/engine/classes/UIListLayout.md) in the **cross‑direction**, it is interpreted as
"automatic cross size" and it defines the minimum size needed to contain
all the child's content in the cross‑direction.

### Property: UIListLayout.Wraps

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
  "category": "Behavior",
  "capabilities": [
    "UI"
  ]
}
```

Controls whether siblings within the parent container wrap to another line
when their default size exceeds the width/height of the container's
bounds.

![Diagram showing how Wraps affects how siblings are distributed within the parent container's bounds.](../../../assets/engine-api/classes/UIListLayout/Wraps.png)

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