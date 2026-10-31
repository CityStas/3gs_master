---
name: BasePlayerGui
last_updated: 2026-10-30T19:55:52Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
tags:
  - NotCreatable
summary: "`BasePlayerGui` is an abstract class which the GUI drawing storage classes inherit from."
---

# Class: BasePlayerGui

> `BasePlayerGui` is an abstract class which the GUI drawing storage classes
> inherit from.

## Description

`BasePlayerGui` is an abstract class that all GUI drawing storage classes
inherit from.

## Methods

### Method: BasePlayerGui:GetGuiObjectsAtPosition

**Signature:** `BasePlayerGui:GetGuiObjectsAtPosition(x: int, y: int): Instances`

Takes a screen position and returns a list of all the [GuiObject](/docs/reference/engine/classes/GuiObject.md)
instances which are occupying that screen position, sorted in the order
they appear on screen from top to bottom as the first and last index,
respectively. The main use case is to get GUI objects under the player's
mouse or touch inputs to allow for selection or highlighting.

Since the child classes of [BasePlayerGui](/docs/reference/engine/classes/BasePlayerGui.md) inherit this function, it
can be fired by container classes such as [PlayerGui](/docs/reference/engine/classes/PlayerGui.md) and
[StarterGui](/docs/reference/engine/classes/StarterGui.md).

*Security: None · Thread Safety: Unsafe · Capabilities: UI*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `x` | `int` |  | The **X** position on the screen relative to the top-left corner after the GUI inset is applied (see [GuiService:GetGuiInset()](/docs/reference/engine/classes/GuiService.md)). |
| `y` | `int` |  | The **Y** position on the screen relative to the top-left corner after the GUI inset is applied (see [GuiService:GetGuiInset()](/docs/reference/engine/classes/GuiService.md)). |

**Returns:** `Instances` — A table of the [GuiObject](/docs/reference/engine/classes/GuiObject.md) instances that occupy the given
screen space.

**Selecting GUIs at a Position**

All GUIs returned by [BasePlayerGui:GetGuiObjectsAtPosition()](/docs/reference/engine/classes/BasePlayerGui.md) are
'cloned' by the `highlightAsFrame()` local function, which creates a `Frame`
GUI positioned on top of the specified GUI that is semi-transparent and the
same [GuiBase2d.AbsoluteSize](/docs/reference/engine/classes/GuiBase2d.md) and [GuiBase2d.AbsolutePosition](/docs/reference/engine/classes/GuiBase2d.md).

These highlights are added to the HighlightsContainer `ScreenGui` in the
Highlight folder of the player's PlayerGui folder. Both are created by the
code sample. All highlight GUIs are [Instance:Destroy()](/docs/reference/engine/classes/Instance.md)ed every time
`highlightGui()` executes.

Note that HighlightContainer's [ScreenGui.DisplayOrder](/docs/reference/engine/classes/ScreenGui.md) is 99999, a
large number, so that it is unlikely any other GUI will render on top of the
highlight GUIs.

```lua
local UserInputService = game:GetService("UserInputService")
local Players = game:GetService("Players")

local player = Players.LocalPlayer

local playerGui = player:WaitForChild("PlayerGui")

-- Create a Folder and ScreenGui to contain the highlight Frames
local highlights = Instance.new("Folder")
highlights.Name = "Highlights"
highlights.Parent = playerGui

local highlightsContainer = Instance.new("ScreenGui")
highlightsContainer.Name = "Container"
highlightsContainer.Parent = highlights
highlightsContainer.DisplayOrder = 99999

-- Creates a semi-transparent yellow Frame on top of the gui with the same AbsoluteSize and AbsolutePosition
local function highlightAsFrame(gui)
	local highlight = Instance.new("Frame")
	highlight.Name = "Highlight"
	highlight.Parent = highlightsContainer
	highlight.Size = UDim2.new(0, gui.AbsoluteSize.X, 0, gui.AbsoluteSize.Y)
	highlight.Position = UDim2.new(0, gui.AbsolutePosition.X, 0, gui.AbsolutePosition.Y)
	highlight.BackgroundColor3 = Color3.fromRGB(255, 255, 10) -- Yellow
	highlight.BackgroundTransparency = 0.75
	highlight.BorderSizePixel = 0
	highlight.LayoutOrder = gui.LayoutOrder - 1
end

-- Use GetGuiObjectsAtPosition to get and highlight all GuiObjects at the input's position
local function highlightGui(input, _gameProcessed)
	local pos = input.Position
	local guisAtPosition = playerGui:GetGuiObjectsAtPosition(pos.X, pos.Y)

	highlightsContainer:ClearAllChildren()

	for _, gui in ipairs(guisAtPosition) do
		if gui:IsA("GuiObject") then
			highlightAsFrame(gui)
		end
	end
end

-- Fire highlightGui on InputBegan if input is of type MouseButton1 of Touch
local function InputBegan(input, gameProcessed)
	local inputType = input.UserInputType
	local touch = Enum.UserInputType.Touch
	local mouse1 = Enum.UserInputType.MouseButton1
	if inputType == touch or inputType == mouse1 then
		highlightGui(input, gameProcessed)
	end
end

UserInputService.InputBegan:Connect(InputBegan)
```

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