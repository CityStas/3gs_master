---
name: UIGridStyleLayout
last_updated: 2026-10-30T19:55:53Z
inherits:
  - UILayout
  - UIComponent
  - UIBase
  - Instance
  - Object
type: class
memory_category: Instances
tags:
  - NotCreatable
  - NotBrowsable
summary: "The base class for grid style UI layouts."
---

# Class: UIGridStyleLayout

> The base class for grid style UI layouts.

## Properties

### Property: UIGridStyleLayout.AbsoluteContentSize

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

The **AbsoluteContentSize** property of a [UIGridStyleLayout](/docs/reference/engine/classes/UIGridStyleLayout.md)
reveals how much space the elements of the grid are taking up, including
any padding created by the grid. This property is particularly useful to
size containers of grids such as [Frames](/docs/reference/engine/classes/Frame.md) to make sure they
aren't any larger than the grid itself.

This property updates as soon as it's read. It will not fire a
[Object.Changed](/docs/reference/engine/classes/Object.md) event immediately after the UI has changed, but if
the value is read, it will become current and a [Object.Changed](/docs/reference/engine/classes/Object.md)
event will fire on the next render step.

### Property: UIGridStyleLayout.FillDirection

```json
{
  "type": "FillDirection",
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

The **FillDirection** property determines the axis in which UI elements
are laid out. [FillDirection.Horizontal](/docs/reference/engine/enums/FillDirection.md) arranges objects from left
to right, while [FillDirection.Vertical](/docs/reference/engine/enums/FillDirection.md) arranges objects from top to
bottom. To reverse elements, such as to arrange right to left, you'll need
to reverse the sorting; for example by negating the child UI objects'
[GuiObject.LayoutOrder](/docs/reference/engine/classes/GuiObject.md) values when
[UIGridStyleLayout.SortOrder](/docs/reference/engine/classes/UIGridStyleLayout.md) is set to
[SortOrder.LayoutOrder](/docs/reference/engine/enums/SortOrder.md).

### Property: UIGridStyleLayout.HorizontalAlignment

```json
{
  "type": "HorizontalAlignment",
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

The **HorizontalAlignment** property determines the **X** axis alignment
of the grid of UI elements, much like [TextLabel.TextXAlignment](/docs/reference/engine/classes/TextLabel.md)
does with [TextLabel.Text](/docs/reference/engine/classes/TextLabel.md).

### Property: UIGridStyleLayout.SortOrder

```json
{
  "type": "SortOrder",
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

The **SortOrder** property determines the order in which child UI objects
are placed in a layout.

For [SortOrder.LayoutOrder](/docs/reference/engine/enums/SortOrder.md), an ascending sort is used on the
[LayoutOrder](/docs/reference/engine/classes/GuiObject.md) property of child UI objects. If
two children share the same [LayoutOrder](/docs/reference/engine/classes/GuiObject.md),
whichever was added sooner to the parent object takes precedence.

For [SortOrder.Name](/docs/reference/engine/enums/SortOrder.md), an alphanumeric sort is used on the
[Instance.Name](/docs/reference/engine/classes/Instance.md) of the child UI objects.

### Property: UIGridStyleLayout.VerticalAlignment

```json
{
  "type": "VerticalAlignment",
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

The **VerticalAlignment** property determines the **Y** axis alignment of
the grid of UI elements, much like [TextLabel.TextYAlignment](/docs/reference/engine/classes/TextLabel.md) does
with [TextLabel.Text](/docs/reference/engine/classes/TextLabel.md).

## Methods

### Method: UIGridStyleLayout:ApplyLayout

**Signature:** `UIGridStyleLayout:ApplyLayout(): ()`

The ApplyLayout method forces sibling UI elements to be re-laid out in
case the sorting criteria may have changed (such as when
[UIGridStyleLayout.SortOrder](/docs/reference/engine/classes/UIGridStyleLayout.md) is set to Custom, and the
[UIGridStyleLayout:SetCustomSortFunction()](/docs/reference/engine/classes/UIGridStyleLayout.md) behavior changed).
Re-layouts automatically happen when UI elements are added/removed, or
their [Instance.Name](/docs/reference/engine/classes/Instance.md) or [GuiObject.LayoutOrder](/docs/reference/engine/classes/GuiObject.md) change.

The manner in which sibling UI elements are laid out is dependent on the
implementation of this abstract class. In other words, a concrete class
like [UIListLayout](/docs/reference/engine/classes/UIListLayout.md) or [UIGridLayout](/docs/reference/engine/classes/UIGridLayout.md) is responsible for the
actual element positioning.

*Security: None · Thread Safety: Unsafe · Capabilities: UI*

**Returns:** `()`

**UI Sort Order**

This code sample demonstrates sorting data using
[UIGridStyleLayout.SortOrder](/docs/reference/engine/classes/UIGridStyleLayout.md) and [GuiObject.LayoutOrder](/docs/reference/engine/classes/GuiObject.md).

```lua
-- Place in a script in a UIListLayout
local uiGridLayout = script.Parent

-- Some data to work with
local scores = {
	["Player1"] = 2048,
	["Ozzypig"] = 1337,
	["Shedletsky"] = 1250,
	["Cozecant"] = 96,
}

-- Build a scoreboard
for name, score in pairs(scores) do
	local textLabel = Instance.new("TextLabel")
	textLabel.Text = name .. ": " .. score
	textLabel.Parent = script.Parent
	textLabel.LayoutOrder = -score -- We want higher scores first, so negate for descending order
	textLabel.Name = name
	textLabel.Size = UDim2.new(0, 200, 0, 50)
	textLabel.Parent = uiGridLayout.Parent
end

while true do
	-- The name is the player's name
	uiGridLayout.SortOrder = Enum.SortOrder.Name
	uiGridLayout:ApplyLayout()
	task.wait(2)
	-- Since we set the LayoutOrder to the score, this will sort by descending score!
	uiGridLayout.SortOrder = Enum.SortOrder.LayoutOrder
	uiGridLayout:ApplyLayout()
	task.wait(2)
end
```

### Method: UIGridStyleLayout:SetCustomSortFunction

**Signature:** `UIGridStyleLayout:SetCustomSortFunction(function?: Function): ()`

> **Deprecated:** This method is deprecated in favor of using other SortOrder means, such as by Name or LayoutOrder.

This method is deprecated. Use [UIGridStyleLayout.SortOrder](/docs/reference/engine/classes/UIGridStyleLayout.md)
instead.

The function should take two arguments (each will be an [Instance](/docs/reference/engine/classes/Instance.md)
child to compare), and return true if a comes before b, otherwise return
false. In other words, use this function the same way you would use a '
function. The sorting should be deterministic, otherwise sort will fail
and fall back to name order.

*Security: None · Thread Safety: Unsafe · Capabilities: UI*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `function` | `Function` | `nil` |  |

**Returns:** `()`

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