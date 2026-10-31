---
name: UIGridLayout
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
summary: "Positions sibling UI elements by filling rows using the space of the parent UI element."
---

# Class: UIGridLayout

> Positions sibling UI elements by filling rows using the space of the parent UI
> element.

## Description

A UIGridLayout (not to be confused with the abstract [UIGridStyleLayout](/docs/reference/engine/classes/UIGridStyleLayout.md)
from which this class inherits) lays out sibling UI elements in multiple rows
within the parent UI element, adding elements to a row one-by-one until the
next element would not fit. It then continues adding elements in the next row.
A UIGridLayout will take UI elements' [GuiObject.Size](/docs/reference/engine/classes/GuiObject.md) and
[GuiObject.Position](/docs/reference/engine/classes/GuiObject.md) under control. While under control, these UI
elements' properties will not be editable in the Properties window.

By default, it lays out elements in **ascending** order where lower values
take more priority over higher values, but this can be changed to use
elements' names by changing [UIListLayout.SortOrder](/docs/reference/engine/classes/UIListLayout.md) to **Name**. A
UIListLayout will automatically re-layout elements when elements are
added/removed, or if a relevant property changes:
[GuiObject.LayoutOrder](/docs/reference/engine/classes/GuiObject.md) or [Instance.Name](/docs/reference/engine/classes/Instance.md). This can be triggered
manually by calling [UIGridStyleLayout:ApplyLayout()](/docs/reference/engine/classes/UIGridStyleLayout.md), though this is
typically not necessary.

The actual cell sizes are the same for all cells. A UIGridLayout will respect
UI constraints placed with it, such as [UISizeConstraint](/docs/reference/engine/classes/UISizeConstraint.md) and
[UIAspectRatioConstraint](/docs/reference/engine/classes/UIAspectRatioConstraint.md). Elements in the layout can span multiple
cells if they have a [UISizeConstraint](/docs/reference/engine/classes/UISizeConstraint.md) with a
[MinSize](/docs/reference/engine/classes/UISizeConstraint.md) set higher than the
[CellSize](/docs/reference/engine/classes/UIGridLayout.md). It is possible to limit the number of
elements per row using [UIGridLayout.FillDirectionMaxCells](/docs/reference/engine/classes/UIGridLayout.md). If set to
1, it is possible to create a single row of elements (as each element would be
positioned in its own row).

This layout is appropriate when line breaks are OK after arbitrary cells. For
example, a set of inventory spaces is a good use of this layout. If building a
table of values in which a line break is not appropriate in the middle of
tabular data, it might be a better idea to use a [UITableLayout](/docs/reference/engine/classes/UITableLayout.md)
instead.

## Properties

### Property: UIGridLayout.AbsoluteCellCount

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
    "can_save": false
  },
  "thread_safety": "Unsafe",
  "category": "Data",
  "capabilities": [
    "UI"
  ]
}
```

Measures the maximum number of elements in each direction. Read-only.

### Property: UIGridLayout.AbsoluteCellSize

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
    "can_save": false
  },
  "thread_safety": "Unsafe",
  "category": "Data",
  "capabilities": [
    "UI"
  ]
}
```

Provides the size of each element of the grid in offsets. Read-only. Not
affected by any [UIScale](/docs/reference/engine/classes/UIScale.md), [UISizeConstraint](/docs/reference/engine/classes/UISizeConstraint.md) or
[UIAspectRatioConstraint](/docs/reference/engine/classes/UIAspectRatioConstraint.md) applied to any individual element in the
grid.

### Property: UIGridLayout.CellPadding

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

(default {0, 5},{0, 5}) Determines how much space there is between
elements in the grid. As with all UDim2s, this space can be both in a
percentage of the parent container's size and raw pixel offset.

### Property: UIGridLayout.CellSize

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

(default {0, 100},{0, 100}) Determines the size of each element in the
grid. As with all UDim2s, this size can be both in a percentage of the
parent container's size and raw pixel offset. If the element being size
has a [UIConstraint](/docs/reference/engine/classes/UIConstraint.md) then the size will be determined by the
constraint, not the grid.

### Property: UIGridLayout.FillDirectionMaxCells

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
  "category": "Behavior",
  "capabilities": [
    "UI"
  ]
}
```

FillDirectionMaxCells determines the number of cells in the grid that can
be used before continuing on the next row/column (whether this is a row or
column is dependent on [UIGridStyleLayout.FillDirection](/docs/reference/engine/classes/UIGridStyleLayout.md)). This
value must be non-negative.

- If set to zero, there is no maximum number of cells that may appear in
  one row/column except for how many can fit within the parent UI element.
- If set to one, this creates a list similar to those created by
  [UIListLayout](/docs/reference/engine/classes/UIListLayout.md).

### Property: UIGridLayout.StartCorner

```json
{
  "type": "StartCorner",
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

StartCorner ([StartCorner](/docs/reference/engine/enums/StartCorner.md)) determines from which corner the grid
starts laying out UI elements. The grid continues in the
[UIGridStyleLayout.FillDirection](/docs/reference/engine/classes/UIGridStyleLayout.md), filling elements one by one until
[UIGridLayout.FIllDirectionMaxCells](/docs/reference/engine/classes/UIGridLayout.md) cells have been laid out in
that row/column or if all the parent UI element's space has been occupied
by previous cells.

Above, the potion is the first [ImageLabel](/docs/reference/engine/classes/ImageLabel.md), followed by the gem and
the sword. The UIGridLayout is using a [StartCorner](/docs/reference/engine/enums/StartCorner.md) of BottomRight.
The [UIGridStyleLayout.FillDirection](/docs/reference/engine/classes/UIGridStyleLayout.md) is Horizontal.

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