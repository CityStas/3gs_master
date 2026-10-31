---
name: UITableLayout
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
summary: "Lays out sibling UI elements and their child UI elements as rows/columns and cells in a table."
---

# Class: UITableLayout

> Lays out sibling UI elements and their child UI elements as rows/columns and
> cells in a table.

## Description

A UITableLayout lays out sibling UI elements as rows in a table. Child UI
elements (the table cells) of these rows are then arranged in columns (within
rows). Each cell within a row has the same height, and each cell within a
column has the same width.

By changing the [UIGridStyleLayout.FillDirection](/docs/reference/engine/classes/UIGridStyleLayout.md), sibling UI elements
can act as columns instead.

When applied, a UITableLayout will take control of sibling and cell elements'
[GuiObject.Size](/docs/reference/engine/classes/GuiObject.md) and [GuiObject.Position](/docs/reference/engine/classes/GuiObject.md). Changing these in the
Properties window is still possible will not produce any effect.

Dimensions of the cells in the resulting table are controlled by the parent UI
element's dimensions. Unless [UITableLayout.FillEmptySpaceColumns](/docs/reference/engine/classes/UITableLayout.md) or
[UITableLayout.FillEmptySpaceRows](/docs/reference/engine/classes/UITableLayout.md) is enabled, the cell dimensions will
be that of the parent UI element (and thus tables with more than one cell
extend outside of their parent).

Cells will continue to respect [UISizeConstraint](/docs/reference/engine/classes/UISizeConstraint.md) objects within them.
In other words, setting [UISizeConstraint.MinSize](/docs/reference/engine/classes/UISizeConstraint.md) on
[UISizeConstraints](/docs/reference/engine/classes/UISizeConstraint.md) within the header cells can
determine the size of the rest of the cells. If
[UISizeConstraint.MaxSize](/docs/reference/engine/classes/UISizeConstraint.md) restricts a cell's size from filling the
allotted space (i.e. another row/column is wider than it), it will align to
the top-left.

## Code Samples

**Build UI Table**

This code sample builds a table of 4 rows, the first having headers. It does
this using some for-loops and a `UITableLayout`. The widths of each column are
set using `UISizeConstraint`s.

```lua
local frame = script.Parent

-- Table data
local headerWidth = { 200, 80, 80 }
local headers = {
	"Name",
	"Job",
	"Cash",
}
local data = {
	{ "Bob", "Waiter", 100 },
	{ "Lisa", "Police", 200 },
	{ "George", "-", 50 },
}

-- First, build the table layout
local uiTableLayout = Instance.new("UITableLayout")
uiTableLayout.FillDirection = Enum.FillDirection.Vertical
uiTableLayout.HorizontalAlignment = Enum.HorizontalAlignment.Center
uiTableLayout.VerticalAlignment = Enum.VerticalAlignment.Center
uiTableLayout.FillEmptySpaceColumns = false
uiTableLayout.FillEmptySpaceRows = false
uiTableLayout.Padding = UDim2.new(0, 5, 0, 5)
uiTableLayout.SortOrder = Enum.SortOrder.LayoutOrder
frame.Size = UDim2.new(0, 0, 0, 40) -- The Size of the parent frame is the cell size
uiTableLayout.Parent = frame

-- Next, create column headers
local headerFrame = Instance.new("Frame")
headerFrame.Name = "Headers"
headerFrame.Parent = frame
for i = 1, #headers do
	local headerText = headers[i]
	local headerCell = Instance.new("TextLabel")
	headerCell.Text = headerText
	headerCell.Name = headerText
	headerCell.LayoutOrder = i
	headerCell.Size = UDim2.new(0, 0, 0, 24)
	headerCell.Parent = headerFrame
	local headerSize = Instance.new("UISizeConstraint")
	headerSize.MinSize = Vector2.new(headerWidth[i], 0)
	headerSize.Parent = headerCell
end

-- Finally, add data rows by iterating over each row and the columns in that row
for index, value in ipairs(data) do
	local rowData = value
	local rowFrame = Instance.new("Frame")
	rowFrame.Name = "Row" .. index
	rowFrame.Parent = frame
	for col = 1, #value do
		local cellData = rowData[col]
		local cell = Instance.new("TextLabel")
		cell.Text = cellData
		cell.Name = headers[col]
		cell.TextXAlignment = Enum.TextXAlignment.Left
		if tonumber(cellData) then -- If this cell is a number, right-align it instead
			cell.TextXAlignment = Enum.TextXAlignment.Right
		end
		cell.ClipsDescendants = true
		cell.Size = UDim2.new(0, 0, 0, 24)
		cell.Parent = rowFrame
	end
end
```

**Expected output:** When run, this code should build a table within the parent UI element. It will have 4 rows, each having data except the first which contains headers.

## Properties

### Property: UITableLayout.FillEmptySpaceColumns

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

FillEmptySpaceColumns determines whether cells' X size are set such that
the entire horizontal space of the parent UI element is used. Enabling
this is useful for making sure your table takes up a more easily
predictable amount of horizontal space (the X-axis size of the parent UI
element). It is still possible that a [UISizeConstraint](/docs/reference/engine/classes/UISizeConstraint.md) applied to
cells will cause underflow/overflow.

When enabling this property, the column widths will be approximately equal
to the parent's [GuiBase2d.AbsoluteSize](/docs/reference/engine/classes/GuiBase2d.md).X component divided by the
number of columns (not accounting for padding or other factors).

**Build UI Table**

This code sample builds a table of 4 rows, the first having headers. It does
this using some for-loops and a `UITableLayout`. The widths of each column are
set using `UISizeConstraint`s.

```lua
local frame = script.Parent

-- Table data
local headerWidth = { 200, 80, 80 }
local headers = {
	"Name",
	"Job",
	"Cash",
}
local data = {
	{ "Bob", "Waiter", 100 },
	{ "Lisa", "Police", 200 },
	{ "George", "-", 50 },
}

-- First, build the table layout
local uiTableLayout = Instance.new("UITableLayout")
uiTableLayout.FillDirection = Enum.FillDirection.Vertical
uiTableLayout.HorizontalAlignment = Enum.HorizontalAlignment.Center
uiTableLayout.VerticalAlignment = Enum.VerticalAlignment.Center
uiTableLayout.FillEmptySpaceColumns = false
uiTableLayout.FillEmptySpaceRows = false
uiTableLayout.Padding = UDim2.new(0, 5, 0, 5)
uiTableLayout.SortOrder = Enum.SortOrder.LayoutOrder
frame.Size = UDim2.new(0, 0, 0, 40) -- The Size of the parent frame is the cell size
uiTableLayout.Parent = frame

-- Next, create column headers
local headerFrame = Instance.new("Frame")
headerFrame.Name = "Headers"
headerFrame.Parent = frame
for i = 1, #headers do
	local headerText = headers[i]
	local headerCell = Instance.new("TextLabel")
	headerCell.Text = headerText
	headerCell.Name = headerText
	headerCell.LayoutOrder = i
	headerCell.Size = UDim2.new(0, 0, 0, 24)
	headerCell.Parent = headerFrame
	local headerSize = Instance.new("UISizeConstraint")
	headerSize.MinSize = Vector2.new(headerWidth[i], 0)
	headerSize.Parent = headerCell
end

-- Finally, add data rows by iterating over each row and the columns in that row
for index, value in ipairs(data) do
	local rowData = value
	local rowFrame = Instance.new("Frame")
	rowFrame.Name = "Row" .. index
	rowFrame.Parent = frame
	for col = 1, #value do
		local cellData = rowData[col]
		local cell = Instance.new("TextLabel")
		cell.Text = cellData
		cell.Name = headers[col]
		cell.TextXAlignment = Enum.TextXAlignment.Left
		if tonumber(cellData) then -- If this cell is a number, right-align it instead
			cell.TextXAlignment = Enum.TextXAlignment.Right
		end
		cell.ClipsDescendants = true
		cell.Size = UDim2.new(0, 0, 0, 24)
		cell.Parent = rowFrame
	end
end
```

**Expected output:** When run, this code should build a table within the parent UI element. It will have 4 rows, each having data except the first which contains headers.

### Property: UITableLayout.FillEmptySpaceRows

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

FillEmptySpaceRows determines whether cells' Y size are set such that the
entire vertical space of the parent UI element is used. Enabling this is
useful for making sure your table takes up a more easily predictable
amount of vertical space (the Y-axis size of the parent UI element). It is
still possible that a [UISizeConstraint](/docs/reference/engine/classes/UISizeConstraint.md) applied to cells will cause
underflow/overflow.

When enabling this property, the row heights will be approximately equal
to the parent's [GuiBase2d.AbsoluteSize](/docs/reference/engine/classes/GuiBase2d.md).Y component divided by the
number of rows (not accounting for padding or other factors).

**Build UI Table**

This code sample builds a table of 4 rows, the first having headers. It does
this using some for-loops and a `UITableLayout`. The widths of each column are
set using `UISizeConstraint`s.

```lua
local frame = script.Parent

-- Table data
local headerWidth = { 200, 80, 80 }
local headers = {
	"Name",
	"Job",
	"Cash",
}
local data = {
	{ "Bob", "Waiter", 100 },
	{ "Lisa", "Police", 200 },
	{ "George", "-", 50 },
}

-- First, build the table layout
local uiTableLayout = Instance.new("UITableLayout")
uiTableLayout.FillDirection = Enum.FillDirection.Vertical
uiTableLayout.HorizontalAlignment = Enum.HorizontalAlignment.Center
uiTableLayout.VerticalAlignment = Enum.VerticalAlignment.Center
uiTableLayout.FillEmptySpaceColumns = false
uiTableLayout.FillEmptySpaceRows = false
uiTableLayout.Padding = UDim2.new(0, 5, 0, 5)
uiTableLayout.SortOrder = Enum.SortOrder.LayoutOrder
frame.Size = UDim2.new(0, 0, 0, 40) -- The Size of the parent frame is the cell size
uiTableLayout.Parent = frame

-- Next, create column headers
local headerFrame = Instance.new("Frame")
headerFrame.Name = "Headers"
headerFrame.Parent = frame
for i = 1, #headers do
	local headerText = headers[i]
	local headerCell = Instance.new("TextLabel")
	headerCell.Text = headerText
	headerCell.Name = headerText
	headerCell.LayoutOrder = i
	headerCell.Size = UDim2.new(0, 0, 0, 24)
	headerCell.Parent = headerFrame
	local headerSize = Instance.new("UISizeConstraint")
	headerSize.MinSize = Vector2.new(headerWidth[i], 0)
	headerSize.Parent = headerCell
end

-- Finally, add data rows by iterating over each row and the columns in that row
for index, value in ipairs(data) do
	local rowData = value
	local rowFrame = Instance.new("Frame")
	rowFrame.Name = "Row" .. index
	rowFrame.Parent = frame
	for col = 1, #value do
		local cellData = rowData[col]
		local cell = Instance.new("TextLabel")
		cell.Text = cellData
		cell.Name = headers[col]
		cell.TextXAlignment = Enum.TextXAlignment.Left
		if tonumber(cellData) then -- If this cell is a number, right-align it instead
			cell.TextXAlignment = Enum.TextXAlignment.Right
		end
		cell.ClipsDescendants = true
		cell.Size = UDim2.new(0, 0, 0, 24)
		cell.Parent = rowFrame
	end
end
```

**Expected output:** When run, this code should build a table within the parent UI element. It will have 4 rows, each having data except the first which contains headers.

### Property: UITableLayout.MajorAxis

```json
{
  "type": "TableMajorAxis",
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

MajorAxis determines whether sibling UI elements are treated as rows or
columns.

**Build UI Table**

This code sample builds a table of 4 rows, the first having headers. It does
this using some for-loops and a `UITableLayout`. The widths of each column are
set using `UISizeConstraint`s.

```lua
local frame = script.Parent

-- Table data
local headerWidth = { 200, 80, 80 }
local headers = {
	"Name",
	"Job",
	"Cash",
}
local data = {
	{ "Bob", "Waiter", 100 },
	{ "Lisa", "Police", 200 },
	{ "George", "-", 50 },
}

-- First, build the table layout
local uiTableLayout = Instance.new("UITableLayout")
uiTableLayout.FillDirection = Enum.FillDirection.Vertical
uiTableLayout.HorizontalAlignment = Enum.HorizontalAlignment.Center
uiTableLayout.VerticalAlignment = Enum.VerticalAlignment.Center
uiTableLayout.FillEmptySpaceColumns = false
uiTableLayout.FillEmptySpaceRows = false
uiTableLayout.Padding = UDim2.new(0, 5, 0, 5)
uiTableLayout.SortOrder = Enum.SortOrder.LayoutOrder
frame.Size = UDim2.new(0, 0, 0, 40) -- The Size of the parent frame is the cell size
uiTableLayout.Parent = frame

-- Next, create column headers
local headerFrame = Instance.new("Frame")
headerFrame.Name = "Headers"
headerFrame.Parent = frame
for i = 1, #headers do
	local headerText = headers[i]
	local headerCell = Instance.new("TextLabel")
	headerCell.Text = headerText
	headerCell.Name = headerText
	headerCell.LayoutOrder = i
	headerCell.Size = UDim2.new(0, 0, 0, 24)
	headerCell.Parent = headerFrame
	local headerSize = Instance.new("UISizeConstraint")
	headerSize.MinSize = Vector2.new(headerWidth[i], 0)
	headerSize.Parent = headerCell
end

-- Finally, add data rows by iterating over each row and the columns in that row
for index, value in ipairs(data) do
	local rowData = value
	local rowFrame = Instance.new("Frame")
	rowFrame.Name = "Row" .. index
	rowFrame.Parent = frame
	for col = 1, #value do
		local cellData = rowData[col]
		local cell = Instance.new("TextLabel")
		cell.Text = cellData
		cell.Name = headers[col]
		cell.TextXAlignment = Enum.TextXAlignment.Left
		if tonumber(cellData) then -- If this cell is a number, right-align it instead
			cell.TextXAlignment = Enum.TextXAlignment.Right
		end
		cell.ClipsDescendants = true
		cell.Size = UDim2.new(0, 0, 0, 24)
		cell.Parent = rowFrame
	end
end
```

**Expected output:** When run, this code should build a table within the parent UI element. It will have 4 rows, each having data except the first which contains headers.

### Property: UITableLayout.Padding

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

Padding will position elements with extra space between them. This can be
done using Scale or Offset components of UDim2. Negative values can bring
elements closer together. When non-zero, the sibling UI elements may be
visible between the cells contained within them.

**Build UI Table**

This code sample builds a table of 4 rows, the first having headers. It does
this using some for-loops and a `UITableLayout`. The widths of each column are
set using `UISizeConstraint`s.

```lua
local frame = script.Parent

-- Table data
local headerWidth = { 200, 80, 80 }
local headers = {
	"Name",
	"Job",
	"Cash",
}
local data = {
	{ "Bob", "Waiter", 100 },
	{ "Lisa", "Police", 200 },
	{ "George", "-", 50 },
}

-- First, build the table layout
local uiTableLayout = Instance.new("UITableLayout")
uiTableLayout.FillDirection = Enum.FillDirection.Vertical
uiTableLayout.HorizontalAlignment = Enum.HorizontalAlignment.Center
uiTableLayout.VerticalAlignment = Enum.VerticalAlignment.Center
uiTableLayout.FillEmptySpaceColumns = false
uiTableLayout.FillEmptySpaceRows = false
uiTableLayout.Padding = UDim2.new(0, 5, 0, 5)
uiTableLayout.SortOrder = Enum.SortOrder.LayoutOrder
frame.Size = UDim2.new(0, 0, 0, 40) -- The Size of the parent frame is the cell size
uiTableLayout.Parent = frame

-- Next, create column headers
local headerFrame = Instance.new("Frame")
headerFrame.Name = "Headers"
headerFrame.Parent = frame
for i = 1, #headers do
	local headerText = headers[i]
	local headerCell = Instance.new("TextLabel")
	headerCell.Text = headerText
	headerCell.Name = headerText
	headerCell.LayoutOrder = i
	headerCell.Size = UDim2.new(0, 0, 0, 24)
	headerCell.Parent = headerFrame
	local headerSize = Instance.new("UISizeConstraint")
	headerSize.MinSize = Vector2.new(headerWidth[i], 0)
	headerSize.Parent = headerCell
end

-- Finally, add data rows by iterating over each row and the columns in that row
for index, value in ipairs(data) do
	local rowData = value
	local rowFrame = Instance.new("Frame")
	rowFrame.Name = "Row" .. index
	rowFrame.Parent = frame
	for col = 1, #value do
		local cellData = rowData[col]
		local cell = Instance.new("TextLabel")
		cell.Text = cellData
		cell.Name = headers[col]
		cell.TextXAlignment = Enum.TextXAlignment.Left
		if tonumber(cellData) then -- If this cell is a number, right-align it instead
			cell.TextXAlignment = Enum.TextXAlignment.Right
		end
		cell.ClipsDescendants = true
		cell.Size = UDim2.new(0, 0, 0, 24)
		cell.Parent = rowFrame
	end
end
```

**Expected output:** When run, this code should build a table within the parent UI element. It will have 4 rows, each having data except the first which contains headers.

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