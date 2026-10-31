---
name: GuiObject
last_updated: 2026-10-30T19:55:52Z
inherits:
  - GuiBase2d
  - GuiBase
  - Instance
  - Object
type: class
memory_category: Gui
tags:
  - NotCreatable
  - NotBrowsable
summary: "An abstract class for all 2D user interface objects."
---

# Class: GuiObject

> An abstract class for all 2D user interface objects.

## Description

[GuiObject](/docs/reference/engine/classes/GuiObject.md) is an abstract class (much like [BasePart](/docs/reference/engine/classes/BasePart.md)) for a 2D
user interface object. It defines all the properties relating to the display
of a graphical user interface (GUI) object such as [Size](/docs/reference/engine/classes/GuiObject.md)
and [Position](/docs/reference/engine/classes/GuiObject.md). It also has some useful read‑only
properties like [AbsolutePosition](/docs/reference/engine/classes/GuiObject.md),
[AbsoluteSize](/docs/reference/engine/classes/GuiObject.md), and
[AbsoluteRotation](/docs/reference/engine/classes/GuiObject.md).

To manipulate the layout of GUI objects in special ways, you can use a layout
structure such as [list/flex](/docs/en-us/ui/list-flex-layouts.md) or
[grid](/docs/en-us/ui/grid-table-layouts.md), and you can style them beyond their
core properties through
[appearance modifiers](/docs/en-us/ui/appearance-modifiers.md).

Although it's possible to detect mouse button events on any GUI object using
[InputBegan](/docs/reference/engine/classes/GuiObject.md) and
[InputEnded](/docs/reference/engine/classes/GuiObject.md), only [ImageButton](/docs/reference/engine/classes/ImageButton.md) and
[TextButton](/docs/reference/engine/classes/TextButton.md) have convenient dedicated events such as
[Activated](/docs/reference/engine/classes/TextButton.md) to detect click/press.

## Properties

### Property: GuiObject.Active

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

This property determines whether the [GuiObject](/docs/reference/engine/classes/GuiObject.md) will sink input to
3D space, such as underlying models with a [ClickDetector](/docs/reference/engine/classes/ClickDetector.md) class
like [DragDetector](/docs/reference/engine/classes/DragDetector.md).

For [GuiButton](/docs/reference/engine/classes/GuiButton.md) objects ([ImageButton](/docs/reference/engine/classes/ImageButton.md) and
[TextButton](/docs/reference/engine/classes/TextButton.md)), this property determines whether
[Activated](/docs/reference/engine/classes/GuiButton.md) fires
([AutoButtonColor](/docs/reference/engine/classes/GuiButton.md) will still work for
those as well). The events [InputBegan](/docs/reference/engine/classes/GuiObject.md),
[InputChanged](/docs/reference/engine/classes/GuiObject.md), and
[InputEnded](/docs/reference/engine/classes/GuiObject.md) work as normal no matter the value
of this property.

**TextButton Active Debounce**

This code sample demonstrates the usage of the Active property as a debounce
for the Activated event.

```lua
-- Place this LocalScript within a TextButton (or ImageButton)
local textButton = script.Parent

textButton.Text = "Click me"
textButton.Active = true

local function onActivated()
	-- This acts like a debounce
	textButton.Active = false

	-- Count backwards from 5
	for i = 5, 1, -1 do
		textButton.Text = "Time: " .. i
		task.wait(1)
	end
	textButton.Text = "Click me"

	textButton.Active = true
end

textButton.Activated:Connect(onActivated)
```

### Property: GuiObject.AnchorPoint

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
  "category": "Data",
  "capabilities": [
    "UI"
  ]
}
```

This property determines the origin point of a [GuiObject](/docs/reference/engine/classes/GuiObject.md), relative
to its absolute size. The origin point determines from where the element
is positioned (through [GuiObject.Position](/docs/reference/engine/classes/GuiObject.md)) and from which the
rendered [GuiObject.Size](/docs/reference/engine/classes/GuiObject.md) expands.

See [here](/docs/en-us/ui/position-and-size.md#anchorpoint) for illustrated
diagrams and details.

**AnchorPoint Demo**

This code sample moves a UI element to different sides of the parent element.
It starts at the top-left and ends at the bottom-right. Paste into a
LocalScript in a Frame, within a ScreenGui.

```lua
local guiObject = script.Parent

while true do
	-- Top-left
	guiObject.AnchorPoint = Vector2.new(0, 0)
	guiObject.Position = UDim2.new(0, 0, 0, 0)
	task.wait(1)
	-- Top
	guiObject.AnchorPoint = Vector2.new(0.5, 0)
	guiObject.Position = UDim2.new(0.5, 0, 0, 0)
	task.wait(1)
	-- Top-right
	guiObject.AnchorPoint = Vector2.new(1, 0)
	guiObject.Position = UDim2.new(1, 0, 0, 0)
	task.wait(1)
	-- Left
	guiObject.AnchorPoint = Vector2.new(0, 0.5)
	guiObject.Position = UDim2.new(0, 0, 0.5, 0)
	task.wait(1)
	-- Dead center
	guiObject.AnchorPoint = Vector2.new(0.5, 0.5)
	guiObject.Position = UDim2.new(0.5, 0, 0.5, 0)
	task.wait(1)
	-- Right
	guiObject.AnchorPoint = Vector2.new(1, 0.5)
	guiObject.Position = UDim2.new(1, 0, 0.5, 0)
	task.wait(1)
	-- Bottom-left
	guiObject.AnchorPoint = Vector2.new(0, 1)
	guiObject.Position = UDim2.new(0, 0, 1, 0)
	task.wait(1)
	-- Bottom
	guiObject.AnchorPoint = Vector2.new(0.5, 1)
	guiObject.Position = UDim2.new(0.5, 0, 1, 0)
	task.wait(1)
	-- Bottom-right
	guiObject.AnchorPoint = Vector2.new(1, 1)
	guiObject.Position = UDim2.new(1, 0, 1, 0)
	task.wait(1)
end
```

### Property: GuiObject.AutomaticSize

```json
{
  "type": "AutomaticSize",
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

This property is used to automatically size parent UI objects based on the
size of its descendants. You can use this property to dynamically add text
and other content to a UI object at edit or run time, and the size will
adjust to fit that content.

When [AutomaticSize](/docs/reference/engine/classes/GuiObject.md) is set to an
[AutomaticSize](/docs/reference/engine/enums/AutomaticSize.md) value to anything other than
[None](/docs/reference/engine/enums/AutomaticSize.md), this UI object may resize depending on its
child content.

For more information on how to use this property and how it works, please
see [here](/docs/en-us/ui/size-modifiers.md#automatic-sizing).

**LocalScript in a ScreenGui**

The following script creates an automatically-sized parent frame with
a`UIListLayout`, then it inserts several automatically-sized `TextLabel`
objects. Note how the parent `UIListLayout` automatically resizes to fit its
child content and the labels automatically resize to fit their text content.
This script can be parented to a `ScreenGui`.

```lua
-- Array of text labels/fonts/sizes to output
local labelArray = {
	{ text = "Lorem", font = Enum.Font.Creepster, size = 50 },
	{ text = "ipsum", font = Enum.Font.IndieFlower, size = 35 },
	{ text = "dolor", font = Enum.Font.Antique, size = 55 },
	{ text = "sit", font = Enum.Font.SpecialElite, size = 65 },
	{ text = "amet", font = Enum.Font.FredokaOne, size = 40 },
}

-- Create an automatically-sized parent frame
local parentFrame = Instance.new("Frame")
parentFrame.AutomaticSize = Enum.AutomaticSize.XY
parentFrame.BackgroundColor3 = Color3.fromRGB(90, 90, 90)
parentFrame.Size = UDim2.fromOffset(25, 100)
parentFrame.Position = UDim2.fromScale(0.1, 0.1)
parentFrame.Parent = script.Parent

-- Add a list layout
local listLayout = Instance.new("UIListLayout")
listLayout.Padding = UDim.new(0, 5)
listLayout.Parent = parentFrame

-- Set rounded corners and padding for visual aesthetics
local roundedCornerParent = Instance.new("UICorner")
roundedCornerParent.Parent = parentFrame
local uiPaddingParent = Instance.new("UIPadding")
uiPaddingParent.PaddingTop = UDim.new(0, 5)
uiPaddingParent.PaddingLeft = UDim.new(0, 5)
uiPaddingParent.PaddingRight = UDim.new(0, 5)
uiPaddingParent.PaddingBottom = UDim.new(0, 5)
uiPaddingParent.Parent = parentFrame

for i = 1, #labelArray do
	-- Create an automatically-sized text label from array
	local childLabel = Instance.new("TextLabel")
	childLabel.AutomaticSize = Enum.AutomaticSize.XY
	childLabel.Size = UDim2.fromOffset(75, 15)
	childLabel.Text = labelArray[i]["text"]
	childLabel.Font = labelArray[i]["font"]
	childLabel.TextSize = labelArray[i]["size"]
	childLabel.TextColor3 = Color3.new(1, 1, 1)
	childLabel.Parent = parentFrame

	-- Visual aesthetics
	local roundedCorner = Instance.new("UICorner")
	roundedCorner.Parent = childLabel
	local uiPadding = Instance.new("UIPadding")
	uiPadding.PaddingTop = UDim.new(0, 5)
	uiPadding.PaddingLeft = UDim.new(0, 5)
	uiPadding.PaddingRight = UDim.new(0, 5)
	uiPadding.PaddingBottom = UDim.new(0, 5)
	uiPadding.Parent = childLabel

	task.wait(2)
end
```

### Property: GuiObject.BackgroundColor3

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
  "category": "Data",
  "capabilities": [
    "UI"
  ]
}
```

This property determines the color of a [GuiObject](/docs/reference/engine/classes/GuiObject.md) background (the
fill color). If your element contains text, such as a [TextBox](/docs/reference/engine/classes/TextBox.md),
[TextButton](/docs/reference/engine/classes/TextButton.md), or [TextLabel](/docs/reference/engine/classes/TextLabel.md), make sure the color of your
background contrasts the text's color.

Another property that determines the visual properties of the background
is [GuiObject.BackgroundTransparency](/docs/reference/engine/classes/GuiObject.md); if this is set to `1`,
neither the background nor the border will render.

See also [BorderColor3](/docs/reference/engine/classes/GuiObject.md).

**Rainbow Frame**

This code sample causes a parent Frame to loop through all colors of the
rainbow using Color3.fromHSV.

```lua
-- Put this code in a LocalScript in a Frame
local frame = script.Parent

while true do
	for hue = 0, 255, 4 do
		-- HSV = hue, saturation, value
		-- If we loop from 0 to 1 repeatedly, we get a rainbow!
		frame.BorderColor3 = Color3.fromHSV(hue / 256, 1, 1)
		frame.BackgroundColor3 = Color3.fromHSV(hue / 256, 0.5, 0.8)
		task.wait()
	end
end
```

### Property: GuiObject.BackgroundTransparency

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
  "category": "Data",
  "capabilities": [
    "UI"
  ]
}
```

This property determines the transparency of the [GuiObject](/docs/reference/engine/classes/GuiObject.md)
background and border. It does not, however, determine the transparency of
text if the GUI is a [TextBox](/docs/reference/engine/classes/TextBox.md), [TextButton](/docs/reference/engine/classes/TextButton.md), or
[TextLabel](/docs/reference/engine/classes/TextLabel.md); text transparency is determined
[TextBox.TextTransparency](/docs/reference/engine/classes/TextBox.md), [TextButton.TextTransparency](/docs/reference/engine/classes/TextButton.md), and
[TextLabel.TextTransparency](/docs/reference/engine/classes/TextLabel.md) respectively.

If this property is set to `1`, neither the background nor the border will
render and the GUI background will be completely transparent.

### Property: GuiObject.BorderColor3

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
  "category": "Data",
  "capabilities": [
    "UI"
  ]
}
```

Determines the color of the [GuiObject](/docs/reference/engine/classes/GuiObject.md) rectangular border (also
known as the stroke color). This is separate from the object's
[GuiObject.BackgroundColor3](/docs/reference/engine/classes/GuiObject.md). You will not be able to see the
object's border if its [GuiObject.BorderSizePixel](/docs/reference/engine/classes/GuiObject.md) property is set
to `0`.

Note that the [UIStroke](/docs/reference/engine/classes/UIStroke.md) component allows for more advanced border
effects.

**Button Highlight**

This code sample causes the border of a parent GuiObject to highlight when the
user hovers their mouse over the element.

```lua
-- Put me inside some GuiObject, preferrably an ImageButton/TextButton
local button = script.Parent

local function onEnter()
	button.BorderSizePixel = 2
	button.BorderColor3 = Color3.new(1, 1, 0) -- Yellow
end

local function onLeave()
	button.BorderSizePixel = 1
	button.BorderColor3 = Color3.new(0, 0, 0) -- Black
end

-- Connect events
button.MouseEnter:Connect(onEnter)
button.MouseLeave:Connect(onLeave)
-- Our default state is "not hovered"
onLeave()
```

### Property: GuiObject.BorderMode

```json
{
  "type": "BorderMode",
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

This property determines in what manner the [GuiObject](/docs/reference/engine/classes/GuiObject.md) border is
laid out relative to its dimensions using the enum of the same name,
[BorderMode](/docs/reference/engine/enums/BorderMode.md).

Note that [UIStroke](/docs/reference/engine/classes/UIStroke.md) can override this property and allow for more
advanced border effects.

### Property: GuiObject.BorderSizePixel

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
  "category": "Data",
  "capabilities": [
    "UI"
  ]
}
```

This property determines how wide the [GuiObject](/docs/reference/engine/classes/GuiObject.md) border renders, in
pixels. Setting this to 0 disables the border altogether.

Note that [UIStroke](/docs/reference/engine/classes/UIStroke.md) can override this property and allow for more
advanced border effects.

**Button Highlight**

This code sample causes the border of a parent GuiObject to highlight when the
user hovers their mouse over the element.

```lua
-- Put me inside some GuiObject, preferrably an ImageButton/TextButton
local button = script.Parent

local function onEnter()
	button.BorderSizePixel = 2
	button.BorderColor3 = Color3.new(1, 1, 0) -- Yellow
end

local function onLeave()
	button.BorderSizePixel = 1
	button.BorderColor3 = Color3.new(0, 0, 0) -- Black
end

-- Connect events
button.MouseEnter:Connect(onEnter)
button.MouseLeave:Connect(onLeave)
-- Our default state is "not hovered"
onLeave()
```

### Property: GuiObject.ClipsDescendants

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

This property determines if the [GuiObject](/docs/reference/engine/classes/GuiObject.md) will clip (make
invisible) any portion of descendant GUI elements that would otherwise
render outside the bounds of the rectangle.

#### Rotation Behavior

When [StarterGui.ClipsDescendantsSupportsRotation](/docs/reference/engine/classes/StarterGui.md) is enabled,
clipping works correctly for rotated shapes. However, clipping **by**
rotated shapes (when the clipping parent itself is rotated) or by rounded
corners ([UICorner](/docs/reference/engine/classes/UICorner.md)) is not supported.

When [StarterGui.ClipsDescendantsSupportsRotation](/docs/reference/engine/classes/StarterGui.md) is **not**
enabled and this [GuiObject](/docs/reference/engine/classes/GuiObject.md) or any ancestor [GuiObject](/docs/reference/engine/classes/GuiObject.md) has a
**non‑zero** [Rotation](/docs/reference/engine/classes/GuiObject.md), this property is
**ignored** and descendant GUI elements will render regardless of this
property's value.

### Property: GuiObject.GuiState

```json
{
  "type": "GuiState",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": false,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "State",
  "capabilities": [
    "UI"
  ]
}
```

When the player's finger is being tapped and held on the
[GuiObject](/docs/reference/engine/classes/GuiObject.md), the [GuiState](/docs/reference/engine/classes/GuiObject.md) of the
[GuiObject](/docs/reference/engine/classes/GuiObject.md) will be set to [Press](/docs/reference/engine/enums/GuiState.md). Similarly,
When the player's finger is being released from the [GuiObject](/docs/reference/engine/classes/GuiObject.md), the
[GuiState](/docs/reference/engine/classes/GuiObject.md) of the [GuiObject](/docs/reference/engine/classes/GuiObject.md) will be set
to [Idle](/docs/reference/engine/enums/GuiState.md), and when
[Interactable](/docs/reference/engine/classes/GuiObject.md) is turned off on the
[GuiObject](/docs/reference/engine/classes/GuiObject.md), the [GuiState](/docs/reference/engine/classes/GuiState.md) of the [GuiObject](/docs/reference/engine/classes/GuiObject.md) will be
set to [NonInteractable](/docs/reference/engine/enums/GuiState.md).

### Property: GuiObject.InputSink

```json
{
  "type": "InputSink",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Data",
  "capabilities": [
    "UI"
  ]
}
```

Controls whether, and to what degree, the [GuiObject](/docs/reference/engine/classes/GuiObject.md) sinks input
that occurs over it, using [InputSink](/docs/reference/engine/enums/InputSink.md). Sinking input prevents it
from passing through to objects behind the element, including 3D objects
in the world such as those with a [ClickDetector](/docs/reference/engine/classes/ClickDetector.md) or
[DragDetector](/docs/reference/engine/classes/DragDetector.md). It defaults to [InputSink.None](/docs/reference/engine/enums/InputSink.md), except on
[GuiButton](/docs/reference/engine/classes/GuiButton.md) objects ([ImageButton](/docs/reference/engine/classes/ImageButton.md) and [TextButton](/docs/reference/engine/classes/TextButton.md)),
where it defaults to [InputSink.Activate](/docs/reference/engine/enums/InputSink.md).

- [InputSink.None](/docs/reference/engine/enums/InputSink.md) — the object does not sink input on its own.
- [InputSink.Activate](/docs/reference/engine/enums/InputSink.md) — the object sinks the mouse-button and touch
  press/release input used to activate it, but lets other input (such as
  mouse movement) pass through.
- [InputSink.All](/docs/reference/engine/enums/InputSink.md) — the object sinks all input that occurs over it.

This property is a more granular successor to the boolean
[Active](/docs/reference/engine/classes/GuiObject.md) property, which can only sink all input or
none. The [InputBegan](/docs/reference/engine/classes/GuiObject.md),
[InputChanged](/docs/reference/engine/classes/GuiObject.md), and
[InputEnded](/docs/reference/engine/classes/GuiObject.md) events fire regardless of this
property's value.

### Property: GuiObject.Interactable

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

Determines whether the [GuiButton](/docs/reference/engine/classes/GuiButton.md) can be interacted with or not, or
if the [GuiState](/docs/reference/engine/enums/GuiState.md) of the [GuiObject](/docs/reference/engine/classes/GuiObject.md) is changing or
not.

On a [GuiButton](/docs/reference/engine/classes/GuiButton.md):

- When the [Interactable](/docs/reference/engine/classes/GuiObject.md) setting on the
  [GuiButton](/docs/reference/engine/classes/GuiButton.md) is set to `false`, the [GuiButton](/docs/reference/engine/classes/GuiButton.md) will no
  longer be able to be pressed or clicked, and the
  [GuiState](/docs/reference/engine/classes/GuiObject.md) will be constantly set to
  [NonInteractable](/docs/reference/engine/enums/GuiState.md).
- When the [Interactable](/docs/reference/engine/classes/GuiObject.md) setting on the
  [GuiButton](/docs/reference/engine/classes/GuiButton.md) is set to `true`, the [GuiButton](/docs/reference/engine/classes/GuiButton.md) will behave
  normally again and the [GuiState](/docs/reference/engine/classes/GuiObject.md) will behave
  normally.

On a [GuiObject](/docs/reference/engine/classes/GuiObject.md):

- When the [Interactable](/docs/reference/engine/classes/GuiObject.md) setting on the
  [GuiButton](/docs/reference/engine/classes/GuiButton.md) is set to `false`, the
  [GuiState](/docs/reference/engine/classes/GuiObject.md) will be constantly set to
  [NonInteractable](/docs/reference/engine/enums/GuiState.md).
- When the [Interactable](/docs/reference/engine/classes/GuiObject.md) setting on the
  [GuiButton](/docs/reference/engine/classes/GuiButton.md) is set to `true`, the
  [GuiState](/docs/reference/engine/classes/GuiObject.md) will behave normally again.

### Property: GuiObject.LayoutOrder

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
  "category": "Data",
  "capabilities": [
    "UI"
  ]
}
```

This property controls the sorting order of the [GuiObject](/docs/reference/engine/classes/GuiObject.md) when
using a [UIGridStyleLayout](/docs/reference/engine/classes/UIGridStyleLayout.md) (such as [UIListLayout](/docs/reference/engine/classes/UIListLayout.md) or
[UIPageLayout](/docs/reference/engine/classes/UIPageLayout.md)) with [SortOrder](/docs/reference/engine/classes/UIGridStyleLayout.md)
set to [SortOrder.LayoutOrder](/docs/reference/engine/enums/SortOrder.md). It has no functionality if the object
does not have a sibling UI layout structure.

[GuiObjects](/docs/reference/engine/classes/GuiObject.md) are sorted in ascending order where lower
values take priority over higher values. Objects with equal values fall
back to the order they were added in.

If you are unsure if you'll need to add an element between two existing
elements in the future, it's a good practice to use multiples of `100`
(`0`, `100`, `200`, etc.). This ensures a large gap of layout order values
which you can use for elements ordered in-between other elements.

See also [ZIndex](/docs/reference/engine/classes/GuiObject.md) which determines the object's
**rendering** order instead of sorting order.

### Property: GuiObject.NextSelectionDown

```json
{
  "type": "GuiObject",
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
  "category": "Selection",
  "capabilities": [
    "UI"
  ]
}
```

This property sets the [GuiObject](/docs/reference/engine/classes/GuiObject.md) selected when the user moves the
[gamepad](/docs/en-us/input/gamepad.md) selector downward. If this property
is empty, moving the gamepad downward will not change the selected GUI.

Moving the gamepad selector downward sets the
[GuiService.SelectedObject](/docs/reference/engine/classes/GuiService.md) to this object unless the GUI is not
[Selectable](/docs/reference/engine/classes/GuiObject.md). Note that this property can be
set to a GUI element even if it is not
[Selectable](/docs/reference/engine/classes/GuiObject.md), so you should ensure that the
value of a GUI's selectable property matches your expected behavior.

See also [NextSelectionUp](/docs/reference/engine/classes/GuiObject.md),
[NextSelectionLeft](/docs/reference/engine/classes/GuiObject.md), and
[NextSelectionRight](/docs/reference/engine/classes/GuiObject.md).

**Creating a Gamepad Selection Grid**

This example demonstrates how to enable Gamepad navigation through a grid of
`GuiObject|GUI` elements without manually having to connect the
[GuiObject.NextSelectionUp](/docs/reference/engine/classes/GuiObject.md), [GuiObject.NextSelectionDown](/docs/reference/engine/classes/GuiObject.md), and
`GuiObject|NextSelectionRight`, and [GuiObject.NextSelectionLeft](/docs/reference/engine/classes/GuiObject.md)
properties for every element in the grid.

Note that this code sample assumes your `UIGridLayout` is sorted by
[name](/docs/reference/engine/classes/UIGridLayout.md), where elements are named in successive
numerical order.

The code relies on this to set the NextSelection properties for all
`GuiObjects` in the same level as the UIGridLayout. In our example, the
UIGridLayoutObject and GUI elements within the grid are all children of a
`Frame` named _"Container"_. The code
[gets the children](/docs/reference/engine/classes/Instance.md) of _"Container"_ and loops
through each child. Children that are not GuiObjects are ignored. For each GUI
element, the code attempts to assigned the NextSelection properties using the
following logic:

1. Starting with 1, the name of all GUI elements match their position in the
   grid
2. Left: The item to the left will always be numbered 1 less than the current
   element
3. Right: The item to the left will always be numbered 1 more than the current
   element
4. Up: The item above (up) will always be number of GUIs in a row 1 less than
   the current element
5. Down: The item below (down) will always be the number of GUIs in a row more
   than the current element This logic also allows for the GUI elements at the
   begging and end of rows (excluding the first and last element) to wrap
   around to the next and previous rows. If an element doesn't exist to the
   left, right, up, or down, the NextSelection will remain nil and moving the
   Gamepad selector in the direction will not change the selected GUI.

This example also contains code to test the grid using the arrow keys (Up,
Down, Left, Right) of your keyboard instead of a gamepad, just in case you
don't have a gamepad to test with. This portion of code initially selects the
element named _"1"_ by assigning it to the [GuiService.SelectedObject](/docs/reference/engine/classes/GuiService.md)
property.

```lua
-- Setup the Gamepad selection grid using the code below
local container = script.Parent:FindFirstChild("Container")
local grid = container:GetChildren()
local rowSize = container:FindFirstChild("UIGridLayout").FillDirectionMaxCells

for _, gui in pairs(grid) do
	if gui:IsA("GuiObject") then
		local pos = gui.Name

		-- Left edge
		gui.NextSelectionLeft = container:FindFirstChild(pos - 1)
		-- Right edge
		gui.NextSelectionRight = container:FindFirstChild(pos + 1)
		-- Above
		gui.NextSelectionUp = container:FindFirstChild(pos - rowSize)
		-- Below
		gui.NextSelectionDown = container:FindFirstChild(pos + rowSize)
	end
end

-- Test the Gamepad selection grid using the code below
local GuiService = game:GetService("GuiService")
local UserInputService = game:GetService("UserInputService")

GuiService.SelectedObject = container:FindFirstChild("1")

function updateSelection(input)
	if input.UserInputType == Enum.UserInputType.Keyboard then
		local key = input.KeyCode

		local selectedObject = GuiService.SelectedObject
		if not selectedObject then
			return
		end

		if key == Enum.KeyCode.Up then
			if not selectedObject.NextSelectionUp then
				GuiService.SelectedObject = selectedObject
			end
		elseif key == Enum.KeyCode.Down then
			if not selectedObject.NextSelectionDown then
				GuiService.SelectedObject = selectedObject
			end
		elseif key == Enum.KeyCode.Left then
			if not selectedObject.NextSelectionLeft then
				GuiService.SelectedObject = selectedObject
			end
		elseif key == Enum.KeyCode.Right then
			if not selectedObject.NextSelectionRight then
				GuiService.SelectedObject = selectedObject
			end
		end
	end
end

UserInputService.InputBegan:Connect(updateSelection)
```

### Property: GuiObject.NextSelectionLeft

```json
{
  "type": "GuiObject",
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
  "category": "Selection",
  "capabilities": [
    "UI"
  ]
}
```

This property sets the [GuiObject](/docs/reference/engine/classes/GuiObject.md) selected when the user moves the
[gamepad](/docs/en-us/input/gamepad.md) selector to the left. If this
property is empty, moving the gamepad to the left will not change the
selected GUI.

Moving the gamepad selector to the left sets the
[GuiService.SelectedObject](/docs/reference/engine/classes/GuiService.md) to this object unless the GUI is not
[Selectable](/docs/reference/engine/classes/GuiObject.md). Note that this property can be
set to a GUI element even if it is not
[Selectable](/docs/reference/engine/classes/GuiObject.md), so you should ensure that the
value of a GUI's selectable property matches your expected behavior.

See also [NextSelectionUp](/docs/reference/engine/classes/GuiObject.md),
[NextSelectionDown](/docs/reference/engine/classes/GuiObject.md), and
[NextSelectionRight](/docs/reference/engine/classes/GuiObject.md).

**Creating a Gamepad Selection Grid**

This example demonstrates how to enable Gamepad navigation through a grid of
`GuiObject|GUI` elements without manually having to connect the
[GuiObject.NextSelectionUp](/docs/reference/engine/classes/GuiObject.md), [GuiObject.NextSelectionDown](/docs/reference/engine/classes/GuiObject.md), and
`GuiObject|NextSelectionRight`, and [GuiObject.NextSelectionLeft](/docs/reference/engine/classes/GuiObject.md)
properties for every element in the grid.

Note that this code sample assumes your `UIGridLayout` is sorted by
[name](/docs/reference/engine/classes/UIGridLayout.md), where elements are named in successive
numerical order.

The code relies on this to set the NextSelection properties for all
`GuiObjects` in the same level as the UIGridLayout. In our example, the
UIGridLayoutObject and GUI elements within the grid are all children of a
`Frame` named _"Container"_. The code
[gets the children](/docs/reference/engine/classes/Instance.md) of _"Container"_ and loops
through each child. Children that are not GuiObjects are ignored. For each GUI
element, the code attempts to assigned the NextSelection properties using the
following logic:

1. Starting with 1, the name of all GUI elements match their position in the
   grid
2. Left: The item to the left will always be numbered 1 less than the current
   element
3. Right: The item to the left will always be numbered 1 more than the current
   element
4. Up: The item above (up) will always be number of GUIs in a row 1 less than
   the current element
5. Down: The item below (down) will always be the number of GUIs in a row more
   than the current element This logic also allows for the GUI elements at the
   begging and end of rows (excluding the first and last element) to wrap
   around to the next and previous rows. If an element doesn't exist to the
   left, right, up, or down, the NextSelection will remain nil and moving the
   Gamepad selector in the direction will not change the selected GUI.

This example also contains code to test the grid using the arrow keys (Up,
Down, Left, Right) of your keyboard instead of a gamepad, just in case you
don't have a gamepad to test with. This portion of code initially selects the
element named _"1"_ by assigning it to the [GuiService.SelectedObject](/docs/reference/engine/classes/GuiService.md)
property.

```lua
-- Setup the Gamepad selection grid using the code below
local container = script.Parent:FindFirstChild("Container")
local grid = container:GetChildren()
local rowSize = container:FindFirstChild("UIGridLayout").FillDirectionMaxCells

for _, gui in pairs(grid) do
	if gui:IsA("GuiObject") then
		local pos = gui.Name

		-- Left edge
		gui.NextSelectionLeft = container:FindFirstChild(pos - 1)
		-- Right edge
		gui.NextSelectionRight = container:FindFirstChild(pos + 1)
		-- Above
		gui.NextSelectionUp = container:FindFirstChild(pos - rowSize)
		-- Below
		gui.NextSelectionDown = container:FindFirstChild(pos + rowSize)
	end
end

-- Test the Gamepad selection grid using the code below
local GuiService = game:GetService("GuiService")
local UserInputService = game:GetService("UserInputService")

GuiService.SelectedObject = container:FindFirstChild("1")

function updateSelection(input)
	if input.UserInputType == Enum.UserInputType.Keyboard then
		local key = input.KeyCode

		local selectedObject = GuiService.SelectedObject
		if not selectedObject then
			return
		end

		if key == Enum.KeyCode.Up then
			if not selectedObject.NextSelectionUp then
				GuiService.SelectedObject = selectedObject
			end
		elseif key == Enum.KeyCode.Down then
			if not selectedObject.NextSelectionDown then
				GuiService.SelectedObject = selectedObject
			end
		elseif key == Enum.KeyCode.Left then
			if not selectedObject.NextSelectionLeft then
				GuiService.SelectedObject = selectedObject
			end
		elseif key == Enum.KeyCode.Right then
			if not selectedObject.NextSelectionRight then
				GuiService.SelectedObject = selectedObject
			end
		end
	end
end

UserInputService.InputBegan:Connect(updateSelection)
```

### Property: GuiObject.NextSelectionRight

```json
{
  "type": "GuiObject",
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
  "category": "Selection",
  "capabilities": [
    "UI"
  ]
}
```

This property sets the [GuiObject](/docs/reference/engine/classes/GuiObject.md) selected when the user moves the
[gamepad](/docs/en-us/input/gamepad.md) selector to the right. If this
property is empty, moving the gamepad to the right will not change the
selected GUI.

Moving the gamepad selector to the right sets the
[GuiService.SelectedObject](/docs/reference/engine/classes/GuiService.md) to this object unless the GUI is not
[Selectable](/docs/reference/engine/classes/GuiObject.md). Note that this property can be
set to a GUI element even if it is not
[Selectable](/docs/reference/engine/classes/GuiObject.md), so you should ensure that the
value of a GUI's selectable property matches your expected behavior.

See also [NextSelectionUp](/docs/reference/engine/classes/GuiObject.md),
[NextSelectionDown](/docs/reference/engine/classes/GuiObject.md), and
[NextSelectionLeft](/docs/reference/engine/classes/GuiObject.md).

**Creating a Gamepad Selection Grid**

This example demonstrates how to enable Gamepad navigation through a grid of
`GuiObject|GUI` elements without manually having to connect the
[GuiObject.NextSelectionUp](/docs/reference/engine/classes/GuiObject.md), [GuiObject.NextSelectionDown](/docs/reference/engine/classes/GuiObject.md), and
`GuiObject|NextSelectionRight`, and [GuiObject.NextSelectionLeft](/docs/reference/engine/classes/GuiObject.md)
properties for every element in the grid.

Note that this code sample assumes your `UIGridLayout` is sorted by
[name](/docs/reference/engine/classes/UIGridLayout.md), where elements are named in successive
numerical order.

The code relies on this to set the NextSelection properties for all
`GuiObjects` in the same level as the UIGridLayout. In our example, the
UIGridLayoutObject and GUI elements within the grid are all children of a
`Frame` named _"Container"_. The code
[gets the children](/docs/reference/engine/classes/Instance.md) of _"Container"_ and loops
through each child. Children that are not GuiObjects are ignored. For each GUI
element, the code attempts to assigned the NextSelection properties using the
following logic:

1. Starting with 1, the name of all GUI elements match their position in the
   grid
2. Left: The item to the left will always be numbered 1 less than the current
   element
3. Right: The item to the left will always be numbered 1 more than the current
   element
4. Up: The item above (up) will always be number of GUIs in a row 1 less than
   the current element
5. Down: The item below (down) will always be the number of GUIs in a row more
   than the current element This logic also allows for the GUI elements at the
   begging and end of rows (excluding the first and last element) to wrap
   around to the next and previous rows. If an element doesn't exist to the
   left, right, up, or down, the NextSelection will remain nil and moving the
   Gamepad selector in the direction will not change the selected GUI.

This example also contains code to test the grid using the arrow keys (Up,
Down, Left, Right) of your keyboard instead of a gamepad, just in case you
don't have a gamepad to test with. This portion of code initially selects the
element named _"1"_ by assigning it to the [GuiService.SelectedObject](/docs/reference/engine/classes/GuiService.md)
property.

```lua
-- Setup the Gamepad selection grid using the code below
local container = script.Parent:FindFirstChild("Container")
local grid = container:GetChildren()
local rowSize = container:FindFirstChild("UIGridLayout").FillDirectionMaxCells

for _, gui in pairs(grid) do
	if gui:IsA("GuiObject") then
		local pos = gui.Name

		-- Left edge
		gui.NextSelectionLeft = container:FindFirstChild(pos - 1)
		-- Right edge
		gui.NextSelectionRight = container:FindFirstChild(pos + 1)
		-- Above
		gui.NextSelectionUp = container:FindFirstChild(pos - rowSize)
		-- Below
		gui.NextSelectionDown = container:FindFirstChild(pos + rowSize)
	end
end

-- Test the Gamepad selection grid using the code below
local GuiService = game:GetService("GuiService")
local UserInputService = game:GetService("UserInputService")

GuiService.SelectedObject = container:FindFirstChild("1")

function updateSelection(input)
	if input.UserInputType == Enum.UserInputType.Keyboard then
		local key = input.KeyCode

		local selectedObject = GuiService.SelectedObject
		if not selectedObject then
			return
		end

		if key == Enum.KeyCode.Up then
			if not selectedObject.NextSelectionUp then
				GuiService.SelectedObject = selectedObject
			end
		elseif key == Enum.KeyCode.Down then
			if not selectedObject.NextSelectionDown then
				GuiService.SelectedObject = selectedObject
			end
		elseif key == Enum.KeyCode.Left then
			if not selectedObject.NextSelectionLeft then
				GuiService.SelectedObject = selectedObject
			end
		elseif key == Enum.KeyCode.Right then
			if not selectedObject.NextSelectionRight then
				GuiService.SelectedObject = selectedObject
			end
		end
	end
end

UserInputService.InputBegan:Connect(updateSelection)
```

### Property: GuiObject.NextSelectionUp

```json
{
  "type": "GuiObject",
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
  "category": "Selection",
  "capabilities": [
    "UI"
  ]
}
```

This property sets the [GuiObject](/docs/reference/engine/classes/GuiObject.md) selected when the user moves the
[gamepad](/docs/en-us/input/gamepad.md) selector upward. If this property is
empty, moving the gamepad upward will not change the selected GUI.

Moving the gamepad selector upward sets the
[GuiService.SelectedObject](/docs/reference/engine/classes/GuiService.md) to this object unless the GUI is not
[Selectable](/docs/reference/engine/classes/GuiObject.md). Note that this property can be
set to a GUI element even if it is not
[Selectable](/docs/reference/engine/classes/GuiObject.md), so you should ensure that the
value of a GUI's selectable property matches your expected behavior.

See also [NextSelectionDown](/docs/reference/engine/classes/GuiObject.md),
[NextSelectionLeft](/docs/reference/engine/classes/GuiObject.md),
[NextSelectionRight](/docs/reference/engine/classes/GuiObject.md).

**Creating a Gamepad Selection Grid**

This example demonstrates how to enable Gamepad navigation through a grid of
`GuiObject|GUI` elements without manually having to connect the
[GuiObject.NextSelectionUp](/docs/reference/engine/classes/GuiObject.md), [GuiObject.NextSelectionDown](/docs/reference/engine/classes/GuiObject.md), and
`GuiObject|NextSelectionRight`, and [GuiObject.NextSelectionLeft](/docs/reference/engine/classes/GuiObject.md)
properties for every element in the grid.

Note that this code sample assumes your `UIGridLayout` is sorted by
[name](/docs/reference/engine/classes/UIGridLayout.md), where elements are named in successive
numerical order.

The code relies on this to set the NextSelection properties for all
`GuiObjects` in the same level as the UIGridLayout. In our example, the
UIGridLayoutObject and GUI elements within the grid are all children of a
`Frame` named _"Container"_. The code
[gets the children](/docs/reference/engine/classes/Instance.md) of _"Container"_ and loops
through each child. Children that are not GuiObjects are ignored. For each GUI
element, the code attempts to assigned the NextSelection properties using the
following logic:

1. Starting with 1, the name of all GUI elements match their position in the
   grid
2. Left: The item to the left will always be numbered 1 less than the current
   element
3. Right: The item to the left will always be numbered 1 more than the current
   element
4. Up: The item above (up) will always be number of GUIs in a row 1 less than
   the current element
5. Down: The item below (down) will always be the number of GUIs in a row more
   than the current element This logic also allows for the GUI elements at the
   begging and end of rows (excluding the first and last element) to wrap
   around to the next and previous rows. If an element doesn't exist to the
   left, right, up, or down, the NextSelection will remain nil and moving the
   Gamepad selector in the direction will not change the selected GUI.

This example also contains code to test the grid using the arrow keys (Up,
Down, Left, Right) of your keyboard instead of a gamepad, just in case you
don't have a gamepad to test with. This portion of code initially selects the
element named _"1"_ by assigning it to the [GuiService.SelectedObject](/docs/reference/engine/classes/GuiService.md)
property.

```lua
-- Setup the Gamepad selection grid using the code below
local container = script.Parent:FindFirstChild("Container")
local grid = container:GetChildren()
local rowSize = container:FindFirstChild("UIGridLayout").FillDirectionMaxCells

for _, gui in pairs(grid) do
	if gui:IsA("GuiObject") then
		local pos = gui.Name

		-- Left edge
		gui.NextSelectionLeft = container:FindFirstChild(pos - 1)
		-- Right edge
		gui.NextSelectionRight = container:FindFirstChild(pos + 1)
		-- Above
		gui.NextSelectionUp = container:FindFirstChild(pos - rowSize)
		-- Below
		gui.NextSelectionDown = container:FindFirstChild(pos + rowSize)
	end
end

-- Test the Gamepad selection grid using the code below
local GuiService = game:GetService("GuiService")
local UserInputService = game:GetService("UserInputService")

GuiService.SelectedObject = container:FindFirstChild("1")

function updateSelection(input)
	if input.UserInputType == Enum.UserInputType.Keyboard then
		local key = input.KeyCode

		local selectedObject = GuiService.SelectedObject
		if not selectedObject then
			return
		end

		if key == Enum.KeyCode.Up then
			if not selectedObject.NextSelectionUp then
				GuiService.SelectedObject = selectedObject
			end
		elseif key == Enum.KeyCode.Down then
			if not selectedObject.NextSelectionDown then
				GuiService.SelectedObject = selectedObject
			end
		elseif key == Enum.KeyCode.Left then
			if not selectedObject.NextSelectionLeft then
				GuiService.SelectedObject = selectedObject
			end
		elseif key == Enum.KeyCode.Right then
			if not selectedObject.NextSelectionRight then
				GuiService.SelectedObject = selectedObject
			end
		end
	end
end

UserInputService.InputBegan:Connect(updateSelection)
```

### Property: GuiObject.Position

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
  "category": "Data",
  "capabilities": [
    "UI"
  ]
}
```

This property determines the [GuiObject](/docs/reference/engine/classes/GuiObject.md) pixel and scalar position
using a [UDim2](/docs/reference/engine/datatypes/UDim2.md). Position is centered around the object's
[GuiObject.AnchorPoint](/docs/reference/engine/classes/GuiObject.md).

The scalar position is relative to the size of the parent GUI element, if
any.

The pixel portions of the [UDim2](/docs/reference/engine/datatypes/UDim2.md) value are the same regardless
of the parent GUI's size. The values represent the position of the object
in pixels. An object's actual pixel position can be read from the
[GuiBase2d.AbsolutePosition](/docs/reference/engine/classes/GuiBase2d.md) property.

### Property: GuiObject.Rotation

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
  "category": "Data",
  "capabilities": [
    "UI"
  ]
}
```

This property determines the number of degrees by which the
[GuiObject](/docs/reference/engine/classes/GuiObject.md) is rotated. Rotation is relative to the **center** of
the object, **not** the [AnchorPoint](/docs/reference/engine/classes/GuiObject.md), meaning
you cannot change the point of rotation. Additionally, this property is
not compatible with [ClipsDescendants](/docs/reference/engine/classes/GuiObject.md).

### Property: GuiObject.Selectable

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
  "category": "Selection",
  "capabilities": [
    "UI"
  ]
}
```

This property determines whether the [GuiObject](/docs/reference/engine/classes/GuiObject.md) can be selected
when navigating GUIs using a gamepad.

If this property is `true`, a GUI can be selected. Selecting a GUI also
sets the [GuiService.SelectedObject](/docs/reference/engine/classes/GuiService.md) property to that object.

When this is `false`, the GUI cannot be selected. However, setting this to
`false` when a GUI is selected will not deselect it nor change the value
of the [GuiService.SelectedObject](/docs/reference/engine/classes/GuiService.md) property.

Add [GuiObject.SelectionGained](/docs/reference/engine/classes/GuiObject.md) and [GuiObject.SelectionLost](/docs/reference/engine/classes/GuiObject.md)
will not fire for the element. To deselect a GuiObject, you must change
the [GuiService.SelectedObject](/docs/reference/engine/classes/GuiService.md) property.

This property is useful if a GUI is connected to several GUIs via
properties such as this [GuiObject.NextSelectionUp](/docs/reference/engine/classes/GuiObject.md),
[GuiObject.NextSelectionDown](/docs/reference/engine/classes/GuiObject.md), [NextSelectionRight](/docs/reference/engine/classes/GuiObject.md),
or [NextSelectionLeft](/docs/reference/engine/classes/GuiObject.md). Rather than change all of the
properties so that the Gamepad cannot select the GUI, you can disable its
Selectable property to temporarily prevent it from being selected. Then,
when you want the gamepad selector to be able to select the GUI, simply
re-enable its selectable property.

**Limiting TextBox Selection**

The example below offers a simple demonstration on how to use the
[GuiObject.Selectable](/docs/reference/engine/classes/GuiObject.md) property to limit when a GUI element can be
selected by the Gamepad navigator.

When a `TextBox` has gains focus, it can be selected. However, when a TextBox
loses focus it can no longer be selected.

Although this is a simple demonstration, the property can also be used to
prevent the navigator from selecting UI elements that exist for cosmetic
rather than functional purposes. For instance, while the buttons on a menu
screen should be selectable, the title image should not be.

```lua
local GuiService = game:GetService("GuiService")

local textBox = script.Parent

local function gainFocus()
	textBox.Selectable = true
	GuiService.SelectedObject = textBox
end

local function loseFocus(_enterPressed, _inputObject)
	GuiService.SelectedObject = nil
	textBox.Selectable = false
end

-- The FocusLost and FocusGained event will fire because the textBox
-- is of type TextBox
textBox.Focused:Connect(gainFocus)
textBox.FocusLost:Connect(loseFocus)
```

### Property: GuiObject.SelectionImageObject

```json
{
  "type": "GuiObject",
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

This property overrides the default selection adornment used for gamepads.

Note that the chosen
[SelectionImageObject](/docs/reference/engine/classes/GuiObject.md) overlays the
selected [GuiObject](/docs/reference/engine/classes/GuiObject.md) with the [Size](/docs/reference/engine/classes/GuiObject.md) of the
image. For best results, you should size the custom `SelectionImageObject`
via the scale [UDim2](/docs/reference/engine/datatypes/UDim2.md) values to help ensure that the object
scales properly over the selected element.

Changing the [SelectionImageObject](/docs/reference/engine/classes/GuiObject.md)
for a [GuiObject](/docs/reference/engine/classes/GuiObject.md) element only affects that element. To affect all
of a user's GUI elements, set the [PlayerGui.SelectionImageObject](/docs/reference/engine/classes/PlayerGui.md)
property.

To determine or set which GUI element is selected by the user, you can use
the [GuiService.SelectedObject](/docs/reference/engine/classes/GuiService.md) property. The player uses the
gamepad to select different GUI elements, invoking the
[NextSelectionUp](/docs/reference/engine/classes/GuiObject.md),
[NextSelectionDown](/docs/reference/engine/classes/GuiObject.md),
[NextSelectionLeft](/docs/reference/engine/classes/GuiObject.md), and
[NextSelectionRight](/docs/reference/engine/classes/GuiObject.md) events.

### Property: GuiObject.SelectionOrder

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
  "category": "Selection",
  "capabilities": [
    "UI"
  ]
}
```

GuiObjects with a lower SelectionOrder are selected earlier than
GuiObjects with a higher SelectionOrder when starting the gamepad
selection or calling [GuiService:Select()](/docs/reference/engine/classes/GuiService.md) on an ancestor. This
property does not affect directional navigation. Default value is 0.

### Property: GuiObject.Size

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
  "category": "Data",
  "capabilities": [
    "UI"
  ]
}
```

This property determines the [GuiObject](/docs/reference/engine/classes/GuiObject.md) scalar and pixel size using
a [UDim2](/docs/reference/engine/datatypes/UDim2.md).

The scalar size is relative to the size of the parent GUI element, if any.

The pixel portions of the [UDim2](/docs/reference/engine/datatypes/UDim2.md) value are the same regardless
of the parent GUI's size. The values represent the size of the object in
pixels. An object's actual pixel size can be read from the
[GuiBase2d.AbsoluteSize](/docs/reference/engine/classes/GuiBase2d.md) property.

If the [GuiObject](/docs/reference/engine/classes/GuiObject.md) has a parent, its size along each axis is also
influenced by the parent's
[SizeConstraint](/docs/reference/engine/classes/GuiObject.md).

**Health Bar**

This code sample allows you to create a simple color-changing health bar using
two nested Frames. Paste this into a LocalScript on the inner frame.

```lua
local Players = game:GetService("Players")

local player = Players.LocalPlayer

-- Paste script into a LocalScript that is
-- parented to a Frame within a Frame
local frame = script.Parent
local container = frame.Parent
container.BackgroundColor3 = Color3.new(0, 0, 0) -- black

-- This function is called when the humanoid's health changes
local function onHealthChanged()
	local human = player.Character.Humanoid
	local percent = human.Health / human.MaxHealth
	-- Change the size of the inner bar
	frame.Size = UDim2.new(percent, 0, 1, 0)
	-- Change the color of the health bar
	if percent < 0.1 then
		frame.BackgroundColor3 = Color3.new(1, 0, 0) -- black
	elseif percent < 0.4 then
		frame.BackgroundColor3 = Color3.new(1, 1, 0) -- yellow
	else
		frame.BackgroundColor3 = Color3.new(0, 1, 0) -- green
	end
end

-- This function runs is called the player spawns in
local function onCharacterAdded(character)
	local human = character:WaitForChild("Humanoid")
	-- Pattern: update once now, then any time the health changes
	human.HealthChanged:Connect(onHealthChanged)
	onHealthChanged()
end

-- Connect our spawn listener; call it if already spawned
player.CharacterAdded:Connect(onCharacterAdded)
if player.Character then
	onCharacterAdded(player.Character)
end
```

### Property: GuiObject.SizeConstraint

```json
{
  "type": "SizeConstraint",
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

This property sets the [Size](/docs/reference/engine/classes/GuiObject.md) axes that the
[GuiObject](/docs/reference/engine/classes/GuiObject.md) will be based on, relative to the size of its parent.

This property is useful for creating GUI objects that are meant to scale
with either the width **or** height of a parent object, but not both,
effectively preserving the aspect ratio of the object.

### Property: GuiObject.Visible

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

This property whether the [GuiObject](/docs/reference/engine/classes/GuiObject.md) and its descendants will be
rendered.

The rendering of individual components of a [GuiObject](/docs/reference/engine/classes/GuiObject.md) can be
controlled individually through transparency properties such as
[GuiObject.BackgroundTransparency](/docs/reference/engine/classes/GuiObject.md),
[TextLabel.TextTransparency](/docs/reference/engine/classes/TextLabel.md) and
[ImageLabel.ImageTransparency](/docs/reference/engine/classes/ImageLabel.md).

When this property is `false`, the [GuiObject](/docs/reference/engine/classes/GuiObject.md) will be ignored by
layout structures such as [UIListLayout](/docs/reference/engine/classes/UIListLayout.md), [UIGridLayout](/docs/reference/engine/classes/UIGridLayout.md), and
[UITableLayout](/docs/reference/engine/classes/UITableLayout.md). In other words, the space that the element would
otherwise occupy in the layout is used by other elements instead.

**UI Window**

This code sample adds open/close functionality to a Window UI. Paste as a
LocalScript that is a sibling of a Frame named Window, a
TextButton/ImageButton named Window, and a TextButton/ImageButton within the
Window called Close.

```lua
local gui = script.Parent
local window = gui:WaitForChild("Window")
local toggleButton = gui:WaitForChild("ToggleWindow")
local closeButton = window:WaitForChild("Close")

local function toggleWindowVisbility()
	-- Flip a boolean using the `not` keyword
	window.Visible = not window.Visible
end

toggleButton.Activated:Connect(toggleWindowVisbility)
closeButton.Activated:Connect(toggleWindowVisbility)
```

### Property: GuiObject.ZIndex

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
  "category": "Data",
  "capabilities": [
    "UI"
  ]
}
```

This property determines the order in which a [GuiObject](/docs/reference/engine/classes/GuiObject.md) renders
relative to others.

By default, [GuiObjects](/docs/reference/engine/classes/GuiObject.md) render in ascending priority
order where those with lower [ZIndex](/docs/reference/engine/classes/GuiObject.md) values are
rendered under those with higher values. You can change the render order
within a [ScreenGui](/docs/reference/engine/classes/ScreenGui.md), [SurfaceGui](/docs/reference/engine/classes/SurfaceGui.md), or [BillboardGui](/docs/reference/engine/classes/BillboardGui.md) by
changing the value of its
[ZIndexBehavior](/docs/reference/engine/classes/LayerCollector.md).

If you are unsure if you'll need to add an element between two existing
elements in the future, it's a good practice to use multiples of `100`
(`0`, `100`, `200`, etc.). This ensures a large gap of render order values
which you can use for elements layered in-between other elements.

See also [LayoutOrder](/docs/reference/engine/classes/GuiObject.md) which controls the
**sorting** order of a [GuiObject](/docs/reference/engine/classes/GuiObject.md) when used with a layout structure
such as [UIListLayout](/docs/reference/engine/classes/UIListLayout.md) or [UIGridLayout](/docs/reference/engine/classes/UIGridLayout.md).

### Property: GuiObject.Draggable

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
  "deprecated": true,
  "thread_safety": "ReadSafe",
  "category": "Behavior",
  "capabilities": [
    "UI"
  ]
}
```

> **Deprecated:** This property is deprecated. Use [UIDragDetector](/docs/reference/engine/classes/UIDragDetector.md) instead, as it supports more input types and can be better customized.

This indicates whether a [GuiObject](/docs/reference/engine/classes/GuiObject.md) (and its descendants) can be
dragged around the screen.

### Property: GuiObject.BackgroundColor *(hidden)*

```json
{
  "type": "BrickColor",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": true,
    "can_save": false
  },
  "deprecated": true,
  "thread_safety": "ReadSafe",
  "category": "Data",
  "capabilities": [
    "UI"
  ]
}
```

> **Deprecated:** This property is deprecated in favor of the [Color3](/docs/reference/engine/datatypes/Color3.md) property [GuiObject.BackgroundColor3](/docs/reference/engine/classes/GuiObject.md), which should be used in new work instead.

Determines the color of the [GuiObject](/docs/reference/engine/classes/GuiObject.md) background.

### Property: GuiObject.BorderColor *(hidden)*

```json
{
  "type": "BrickColor",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": true,
    "can_save": false
  },
  "deprecated": true,
  "thread_safety": "ReadSafe",
  "category": "Data",
  "capabilities": [
    "UI"
  ]
}
```

> **Deprecated:** This property is deprecated in favor of the [Color3](/docs/reference/engine/datatypes/Color3.md) property BorderColor3, which should be used in new work instead.

Determines the color of the [GuiObject](/docs/reference/engine/classes/GuiObject.md) border.

### Property: GuiObject.Transparency *(hidden)*

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
    "can_save": false
  },
  "deprecated": true,
  "thread_safety": "ReadSafe",
  "category": "Data",
  "capabilities": [
    "UI"
  ]
}
```

> **Deprecated:** This property is deprecated and indexing it will return [BackgroundTransparency](/docs/reference/engine/classes/GuiObject.md).

A mixed property of
[BackgroundTransparency](/docs/reference/engine/classes/GuiObject.md) and
[TextTransparency](/docs/reference/engine/classes/TextLabel.md).

## Methods

### Method: GuiObject:TweenPosition

**Signature:** `GuiObject:TweenPosition(endPosition: UDim2, easingDirection?: EasingDirection, easingStyle?: EasingStyle, time?: float, override?: boolean, callback?: Function): boolean`

> **Deprecated:** This function is deprecated in favor of using [TweenService](/docs/reference/engine/classes/TweenService.md), which allows for better customization using an object-oriented and event-based approach.  - The `easingDirection`, `easingStyle`, and `time` parameters are handled   by a [TweenInfo](/docs/reference/engine/datatypes/TweenInfo.md) - The `override` parameter is no longer relevant; tweens always override   previous tweens on the same property. - The `callback` parameter is better suited by the [Tween.Completed](/docs/reference/engine/classes/Tween.md)   event. The [PlaybackState](/docs/reference/engine/enums/PlaybackState.md) enum passed by that event provides a   more detailed description of the tween's completion state.

Smoothly moves a GUI to a new [UDim2](/docs/reference/engine/datatypes/UDim2.md) position in the specified
time using the specified [EasingDirection](/docs/reference/engine/enums/EasingDirection.md) and [EasingStyle](/docs/reference/engine/enums/EasingStyle.md).
This method raises an error if `easingStyle` is [EasingStyle.Bezier](/docs/reference/engine/enums/EasingStyle.md)
or [EasingStyle.Spring](/docs/reference/engine/enums/EasingStyle.md).

This function will return whether the tween will play. It will not play if
another tween is acting on the [GuiObject](/docs/reference/engine/classes/GuiObject.md) and the override
parameter is `false`.

See also [GuiObject:TweenSize()](/docs/reference/engine/classes/GuiObject.md) and
[GuiObject:TweenSizeAndPosition()](/docs/reference/engine/classes/GuiObject.md).

*Security: None · Thread Safety: Unsafe · Capabilities: UI*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `endPosition` | `UDim2` |  | Where the GUI should move to. |
| `easingDirection` | `EasingDirection` | `Out` | The direction in which to ease the GUI to the _endPosition_. |
| `easingStyle` | `EasingStyle` | `Quad` | The style in which to ease the GUI to the _endPosition_. |
| `time` | `float` | `1` | How long, in seconds, the tween should take to complete. |
| `override` | `boolean` | `false` | Whether the tween will override an in-progress tween. |
| `callback` | `Function` | `nil` | A callback function to execute when the tween completes. |

**Returns:** `boolean` — Whether the tween will play.

**Tween a GUI's Position**

This code sample demonstrates a more involved usage of TweenPosition by
detecting when the tween completes/cancels by defining a callback function. It
also prints whether the tween will play.

```lua
local START_POSITION = UDim2.new(0, 0, 0, 0)
local GOAL_POSITION = UDim2.new(1, 0, 1, 0)

local guiObject = script.Parent

local function callback(state)
	if state == Enum.TweenStatus.Completed then
		print("The tween completed uninterrupted")
	elseif state == Enum.TweenStatus.Canceled then
		print("Another tween cancelled this one")
	end
end

-- Initialize the GuiObject position, then start the tween:
guiObject.Position = START_POSITION

local willPlay = guiObject:TweenPosition(
	GOAL_POSITION, -- Final position the tween should reach
	Enum.EasingDirection.In, -- Direction of the easing
	Enum.EasingStyle.Sine, -- Kind of easing to apply
	2, -- Duration of the tween in seconds
	true, -- Whether in-progress tweens are interrupted
	callback -- Function to be callled when on completion/cancelation
)

if willPlay then
	print("The tween will play")
else
	print("The tween will not play")
end
```

### Method: GuiObject:TweenSize

**Signature:** `GuiObject:TweenSize(endSize: UDim2, easingDirection?: EasingDirection, easingStyle?: EasingStyle, time?: float, override?: boolean, callback?: Function): boolean`

> **Deprecated:** This function is deprecated in favor of using [TweenService](/docs/reference/engine/classes/TweenService.md), which allows for better customization using an object-oriented and event-based approach.  - The `easingDirection`, `easingStyle`, and `time` parameters are handled   by a [TweenInfo](/docs/reference/engine/datatypes/TweenInfo.md) - The `override` parameter is no longer relevant; tweens always override   previous tweens on the same property. - The `callback` parameter is better suited by the [Tween.Completed](/docs/reference/engine/classes/Tween.md)   event. The [PlaybackState](/docs/reference/engine/enums/PlaybackState.md) enum passed by that event provides a   more detailed description of the tween's completion state.

Smoothly resizes a [GuiObject](/docs/reference/engine/classes/GuiObject.md) to a new [UDim2](/docs/reference/engine/datatypes/UDim2.md) in the
specified time using the specified [EasingDirection](/docs/reference/engine/enums/EasingDirection.md) and
[EasingStyle](/docs/reference/engine/enums/EasingStyle.md). This method raises an error if `easingStyle` is
[EasingStyle.Bezier](/docs/reference/engine/enums/EasingStyle.md) or [EasingStyle.Spring](/docs/reference/engine/enums/EasingStyle.md).

This function will return whether the tween will play. Normally this will
always return `true`, but it will return `false` if another tween is
active and override is set to `false`.

See also [GuiObject:TweenSize()](/docs/reference/engine/classes/GuiObject.md) and
[GuiObject:TweenSizeAndPosition()](/docs/reference/engine/classes/GuiObject.md).

*Security: None · Thread Safety: Unsafe · Capabilities: UI*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `endSize` | `UDim2` |  | The size that the GUI should resize. |
| `easingDirection` | `EasingDirection` | `Out` | The direction in which to ease the GUI to the _endSize_. |
| `easingStyle` | `EasingStyle` | `Quad` | The style in which to ease the GUI to the _endSize_. |
| `time` | `float` | `1` | How long, in seconds, the tween should take to complete. |
| `override` | `boolean` | `false` | Whether the tween will override an in-progress tween. |
| `callback` | `Function` | `nil` | A callback function to execute when the tween completes. |

**Returns:** `boolean` — Whether the tween will play.

**Tween a GuiObject's Size**

This code sample demonstrates the usage of the [GuiObject:TweenSize()](/docs/reference/engine/classes/GuiObject.md)
function. It initiates an animation on the parent's [GuiObject.Size](/docs/reference/engine/classes/GuiObject.md)
property to `UDim2.new(0.5, 0, 0.5, 0)`, which is half the `GuiObject`'s
parent size on both axes.

Additionally, it demonstrates how the callback parameter can be used to detect
when the tween stops (whether it was cancelled by another tween or completed).

```lua
local guiObject = script.Parent

local function callback(didComplete)
	if didComplete then
		print("The tween completed successfully")
	else
		print("The tween was cancelled")
	end
end

local willTween = guiObject:TweenSize(
	UDim2.new(0.5, 0, 0.5, 0), -- endSize (required)
	Enum.EasingDirection.In, -- easingDirection (default Out)
	Enum.EasingStyle.Sine, -- easingStyle (default Quad)
	2, -- time (default: 1)
	true, -- should this tween override ones in-progress? (default: false)
	callback -- a function to call when the tween completes (default: nil)
)

if willTween then
	print("The GuiObject will tween")
else
	print("The GuiObject will not tween")
end
```

**Expected output:** The GuiObject will tween
The tween was completed successfully

### Method: GuiObject:TweenSizeAndPosition

**Signature:** `GuiObject:TweenSizeAndPosition(endSize: UDim2, endPosition: UDim2, easingDirection?: EasingDirection, easingStyle?: EasingStyle, time?: float, override?: boolean, callback?: Function): boolean`

> **Deprecated:** This function is deprecated in favor of using [TweenService](/docs/reference/engine/classes/TweenService.md), which allows for better customization using an object-oriented and event-based approach.  - The `easingDirection`, `easingStyle`, and `time` parameters are handled   by a [TweenInfo](/docs/reference/engine/datatypes/TweenInfo.md) - The `override` parameter is no longer relevant; tweens always override   previous tweens on the same property. - The `callback` parameter is better suited by the [Tween.Completed](/docs/reference/engine/classes/Tween.md)   event. The [PlaybackState](/docs/reference/engine/enums/PlaybackState.md) enum passed by that event provides a   more detailed description of the tween's completion state.

Smoothly resizes and moves a GUI to a new [UDim2](/docs/reference/engine/datatypes/UDim2.md) size and
position in the specified time using the specified [EasingDirection](/docs/reference/engine/enums/EasingDirection.md)
and [EasingStyle](/docs/reference/engine/enums/EasingStyle.md). This method raises an error if `easingStyle` is
[EasingStyle.Bezier](/docs/reference/engine/enums/EasingStyle.md) or [EasingStyle.Spring](/docs/reference/engine/enums/EasingStyle.md).

This function will return whether the tween will play. Normally this will
always return `true`, but it will return `false` if another tween is
active and override is set to `false`.

See also [GuiObject:TweenSize()](/docs/reference/engine/classes/GuiObject.md) and
[GuiObject:TweenSizeAndPosition()](/docs/reference/engine/classes/GuiObject.md).

*Security: None · Thread Safety: Unsafe · Capabilities: UI*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `endSize` | `UDim2` |  | The size that the GUI should resize. |
| `endPosition` | `UDim2` |  | Where the GUI should move to. |
| `easingDirection` | `EasingDirection` | `Out` | The direction in which to ease the GUI to the _endSize_ and _endPosition_. |
| `easingStyle` | `EasingStyle` | `Quad` | The style in which to ease the GUI to the _endSize_ and _endPosition_. |
| `time` | `float` | `1` | How long, in seconds, the tween should take to complete. |
| `override` | `boolean` | `false` | Whether the tween will override an in-progress tween. |
| `callback` | `Function` | `nil` | A callback function to execute when the tween completes. |

**Returns:** `boolean` — Whether the tween will play.

**Tween a GUI's Size and Position**

The below example would tween a [Frame](/docs/reference/engine/classes/Frame.md) to the top left of the parent's
size and resize it down to 0.

```lua
local frame = script.Parent.Frame
frame:TweenSizeAndPosition(UDim2.new(0, 0, 0, 0), UDim2.new(0, 0, 0, 0))
```

## Events

### Event: GuiObject.InputBegan

**Signature:** `GuiObject.InputBegan(input: InputObject)`

This event fires when a user begins interacting with the [GuiObject](/docs/reference/engine/classes/GuiObject.md)
via a Human-Computer Interface device (Mouse button down, touch begin,
keyboard button down, etc).

The [UserInputService](/docs/reference/engine/classes/UserInputService.md) has a similarly named event that is not
restricted to a specific UI element: [UserInputService.InputBegan](/docs/reference/engine/classes/UserInputService.md).

This event will always fire regardless of game state.

See also [GuiObject.InputEnded](/docs/reference/engine/classes/GuiObject.md) and [GuiObject.InputChanged](/docs/reference/engine/classes/GuiObject.md).

*Security: None · Capabilities: UI*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `input` | `InputObject` | An [InputObject](/docs/reference/engine/classes/InputObject.md), which contains useful data for querying user input such as the [type of input](/docs/reference/engine/enums/UserInputType.md), [state of input](/docs/reference/engine/enums/UserInputState.md), and [screen coordinates of the input](/docs/reference/engine/classes/InputObject.md). |

**Tracking the Beginning of Input on a GuiObject**

The following example demonstrates one of many usage examples of handling user
input from InputBegan depending on its type.

In order for this to work as expected, it must be placed in a `LocalScript`
and a child of _gui_.

```lua
-- In order to use the InputBegan event, you must specify the GuiObject
local gui = script.Parent

-- A sample function providing multiple usage cases for various types of user input
local function inputBegan(input)
	if input.UserInputType == Enum.UserInputType.Keyboard then
		print("A key is being pushed down! Key:", input.KeyCode)
	elseif input.UserInputType == Enum.UserInputType.MouseButton1 then
		print("The left mouse button has been pressed down at", input.Position)
	elseif input.UserInputType == Enum.UserInputType.MouseButton2 then
		print("The right mouse button has been pressed down at", input.Position)
	elseif input.UserInputType == Enum.UserInputType.Touch then
		print("A touchscreen input has started at", input.Position)
	elseif input.UserInputType == Enum.UserInputType.Gamepad1 then
		print("A button is being pressed on a gamepad! Button:", input.KeyCode)
	end
end

gui.InputBegan:Connect(inputBegan)
```

### Event: GuiObject.InputChanged

**Signature:** `GuiObject.InputChanged(input: InputObject)`

This event fires when a user changes how they're interacting via a
Human-Computer Interface device (Mouse button down, touch begin, keyboard
button down, etc).

The [UserInputService](/docs/reference/engine/classes/UserInputService.md) has a similarly named event that is not
restricted to a specific UI element:
[UserInputService.InputChanged](/docs/reference/engine/classes/UserInputService.md).

This event will always fire regardless of game state.

See also [GuiObject.InputBegan](/docs/reference/engine/classes/GuiObject.md) and [GuiObject.InputEnded](/docs/reference/engine/classes/GuiObject.md).

*Security: None · Capabilities: UI*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `input` | `InputObject` | An [InputObject](/docs/reference/engine/classes/InputObject.md), which contains useful data for querying user input such as the [type of input](/docs/reference/engine/enums/UserInputType.md), [state of input](/docs/reference/engine/enums/UserInputState.md), and [screen coordinates of the input](/docs/reference/engine/classes/InputObject.md). |

**GuiObject InputChanged Demo**

The following example demonstrates one of many usage examples of handling user
input from InputChanged depending on its type.

In order for this to work as expected, it must be placed in a `LocalScript`
and a child of _gui_.

```lua
local UserInputService = game:GetService("UserInputService")

local gui = script.Parent

local function printMovement(input)
	print("Position:", input.Position)
	print("Movement Delta:", input.Delta)
end

local function inputChanged(input)
	if input.UserInputType == Enum.UserInputType.MouseMovement then
		print("The mouse has been moved!")
		printMovement(input)
	elseif input.UserInputType == Enum.UserInputType.MouseWheel then
		print("The mouse wheel has been scrolled!")
		print("Wheel Movement:", input.Position.Z)
	elseif input.UserInputType == Enum.UserInputType.Gamepad1 then
		if input.KeyCode == Enum.KeyCode.Thumbstick1 then
			print("The left thumbstick has been moved!")
			printMovement(input)
		elseif input.KeyCode == Enum.KeyCode.Thumbstick2 then
			print("The right thumbstick has been moved!")
			printMovement(input)
		elseif input.KeyCode == Enum.KeyCode.ButtonL2 then
			print("The pressure being applied to the left trigger has changed!")
			print("Pressure:", input.Position.Z)
		elseif input.KeyCode == Enum.KeyCode.ButtonR2 then
			print("The pressure being applied to the right trigger has changed!")
			print("Pressure:", input.Position.Z)
		end
	elseif input.UserInputType == Enum.UserInputType.Touch then
		print("The user's finger is moving on the screen!")
		printMovement(input)
	elseif input.UserInputType == Enum.UserInputType.Gyro then
		local _rotInput, rotCFrame = UserInputService:GetDeviceRotation()
		local rotX, rotY, rotZ = rotCFrame:toEulerAnglesXYZ()
		local rot = Vector3.new(math.deg(rotX), math.deg(rotY), math.deg(rotZ))
		print("The rotation of the user's mobile device has been changed!")
		print("Position", rotCFrame.p)
		print("Rotation:", rot)
	elseif input.UserInputType == Enum.UserInputType.Accelerometer then
		print("The acceleration of the user's mobile device has been changed!")
		printMovement(input)
	end
end

gui.InputChanged:Connect(inputChanged)
```

### Event: GuiObject.InputEnded

**Signature:** `GuiObject.InputEnded(input: InputObject)`

The InputEnded event fires when a user stops interacting via a
Human-Computer Interface device (Mouse button down, touch begin, keyboard
button down, etc).

The [UserInputService](/docs/reference/engine/classes/UserInputService.md) has a similarly named event that is not
restricted to a specific UI element: [UserInputService.InputEnded](/docs/reference/engine/classes/UserInputService.md).

This event will always fire regardless of game state.

See also [GuiObject.InputBegan](/docs/reference/engine/classes/GuiObject.md) and [GuiObject.InputChanged](/docs/reference/engine/classes/GuiObject.md).

*Security: None · Capabilities: UI*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `input` | `InputObject` | An [InputObject](/docs/reference/engine/classes/InputObject.md), which contains useful data for querying user input such as the [UserInputType](/docs/reference/engine/enums/UserInputType.md), [UserInputState](/docs/reference/engine/enums/UserInputState.md), and [InputObject.Position](/docs/reference/engine/classes/InputObject.md). |

**Tracking the End of Input on a GuiObject**

The following example demonstrates one of many usage examples of handling user
input from InputEnded depending on its type.

In order for this to work as expected, it must be placed in a `LocalScript`
and a child of _gui_.

```lua
-- In order to use the InputChanged event, you must specify a GuiObject
local gui = script.Parent

-- A sample function providing multiple usage cases for various types of user input
local function inputEnded(input)
	if input.UserInputType == Enum.UserInputType.Keyboard then
		print("A key has been released! Key:", input.KeyCode)
	elseif input.UserInputType == Enum.UserInputType.MouseButton1 then
		print("The left mouse button has been released at", input.Position)
	elseif input.UserInputType == Enum.UserInputType.MouseButton2 then
		print("The right mouse button has been released at", input.Position)
	elseif input.UserInputType == Enum.UserInputType.Touch then
		print("A touchscreen input has been released at", input.Position)
	elseif input.UserInputType == Enum.UserInputType.Gamepad1 then
		print("A button has been released on a gamepad! Button:", input.KeyCode)
	end
end

gui.InputEnded:Connect(inputEnded)
```

### Event: GuiObject.MouseEnter

**Signature:** `GuiObject.MouseEnter(x: int, y: int)`

The MouseEnter event fires when a user moves their mouse into a
[GuiObject](/docs/reference/engine/classes/GuiObject.md) element.

Please do not rely on the `x` and `y` arguments passed by this event as a
fool-proof way to determine where the user's mouse is when it enters a
GUI. These coordinates may vary even when the mouse enters the GUI via the
same edge - particularly when the mouse enters the element quickly. This
is due to the fact the coordinates indicate the position of the mouse when
the event fires rather than the exact moment the mouse enters the GUI.

This event fires even when the GUI element renders beneath another
element.

If you would like to track when a user's mouse leaves a GUI element, you
can use the [GuiObject.MouseLeave](/docs/reference/engine/classes/GuiObject.md) event.

##### See Also

- [GuiObject.MouseLeave](/docs/reference/engine/classes/GuiObject.md)
- [GuiObject.MouseMoved](/docs/reference/engine/classes/GuiObject.md)
- [GuiObject.MouseWheelForward](/docs/reference/engine/classes/GuiObject.md)
- [GuiObject.MouseWheelBackward](/docs/reference/engine/classes/GuiObject.md)

*Security: None · Capabilities: UI*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `x` | `int` | The mouse's **X** screen coordinate in pixels, relative to the top left corner of the screen. |
| `y` | `int` | The mouse's **Y** screen coordinate in pixels, relative to the top left corner of the screen. |

**Printing where a Mouse Enters a GuiObject**

The following example prints the mouse location, in pixels, when it enters GUI
element.

```lua
local guiObject = script.Parent
guiObject.MouseEnter:Connect(function(x, y)
	print("The user's mouse cursor has entered the GuiObject at position", x, ",", y)
end)
```

### Event: GuiObject.MouseLeave

**Signature:** `GuiObject.MouseLeave(x: int, y: int)`

The MouseLeave event fires when a user moves their mouse out of a
[GuiObject](/docs/reference/engine/classes/GuiObject.md) element.

Please do not rely on the `x` and `y` arguments passed by this event as a
fool-proof way to determine where the user's mouse is when it leaves a
GUI. These coordinates may vary even when the mouse leaves the GUI via the
same edge - particularly when the mouse leaves the element quickly. This
is due to the fact the coordinates indicate the position of the mouse when
the event fires rather than the exact moment the mouse leaves the GUI.

This event fires even when the GUI element renders beneath another
element.

##### See Also

- [GuiObject.MouseEnter](/docs/reference/engine/classes/GuiObject.md)
- [GuiObject.MouseMoved](/docs/reference/engine/classes/GuiObject.md)
- [GuiObject.MouseWheelForward](/docs/reference/engine/classes/GuiObject.md)
- [GuiObject.MouseWheelBackward](/docs/reference/engine/classes/GuiObject.md)

*Security: None · Capabilities: UI*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `x` | `int` | The mouse's **X** screen coordinate in pixels, relative to the top left corner of the screen. |
| `y` | `int` | The mouse's **Y** screen coordinate in pixels, relative to the top left corner of the screen. |

### Event: GuiObject.MouseMoved

**Signature:** `GuiObject.MouseMoved(x: int, y: int)`

Fires whenever a user moves their mouse while it is inside a
[GuiObject](/docs/reference/engine/classes/GuiObject.md) element. It is similar to [Mouse.Move](/docs/reference/engine/classes/Mouse.md), which
fires regardless whether the user's mouse is over a GUI element.

Note, this event fires when the mouse's position is updated, therefore it
will fire repeatedly while being moved.

The `x` and `y` arguments indicate the updated screen coordinates of the
user's mouse in pixels. These can be useful to determine the mouse's
location on the GUI, screen, and delta since the mouse's previous position
if it is being tracked in a global variable.

The code below demonstrates how to determine the [Vector2](/docs/reference/engine/datatypes/Vector2.md) offset
of the user's mouse relative to a GUI element.
[AbsolutePosition](/docs/reference/engine/classes/GuiObject.md) is measured inside the
screen's GUI inset, while the `x` and `y` arguments of this event are
screen coordinates that include it, so the sample calls
[GetGuiInset()](/docs/reference/engine/classes/GuiService.md) to reconcile the two spaces
instead of assuming a fixed inset size.

```lua
local Players = game:GetService("Players")
local GuiService = game:GetService("GuiService")

local CustomScrollingFrame = script.Parent
local SubFrame = CustomScrollingFrame:FindFirstChild("SubFrame")

local mouse = Players.LocalPlayer:GetMouse()

local function getPosition(X, Y)
	local topLeftInset = GuiService:GetGuiInset()

	local gui_X = CustomScrollingFrame.AbsolutePosition.X
	local gui_Y = CustomScrollingFrame.AbsolutePosition.Y

	local pos = Vector2.new(math.abs(X - gui_X), math.abs(Y - gui_Y - topLeftInset.Y))
	print(pos)
end

CustomScrollingFrame.MouseMoved:Connect(getPosition)
```

Note that this event may not fire exactly when the user's mouse enters or
exits a GUI element. Therefore, the `x` and `y` arguments may not match up
perfectly to the coordinates of the GUI's edges.

##### See Also

- [GuiObject.MouseEnter](/docs/reference/engine/classes/GuiObject.md)
- [GuiObject.MouseLeave](/docs/reference/engine/classes/GuiObject.md)
- [GuiObject.MouseWheelForward](/docs/reference/engine/classes/GuiObject.md)
- [GuiObject.MouseWheelBackward](/docs/reference/engine/classes/GuiObject.md)

*Security: None · Capabilities: UI*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `x` | `int` | The mouse's **X** screen coordinate in pixels, relative to the top left corner of the screen. |
| `y` | `int` | The mouse's **Y** screen coordinate in pixels, relative to the top left corner of the screen. |

### Event: GuiObject.MouseWheelBackward

**Signature:** `GuiObject.MouseWheelBackward(x: int, y: int)`

The WheelBackward event fires when a user scrolls their mouse wheel back
when the mouse is over a [GuiObject](/docs/reference/engine/classes/GuiObject.md) element. It is similar to
[Mouse.WheelBackward](/docs/reference/engine/classes/Mouse.md), which fires regardless whether the user's
mouse is over a GUI element.

This event fires merely as an indicator of the wheel's backward movement.
This means that the `x` and `y` mouse coordinate arguments don't change as
a result of this event. These coordinates only change when the mouse
moves, which can be tracked by the [GuiObject.MouseMoved](/docs/reference/engine/classes/GuiObject.md) event.

##### See Also

- [GuiObject.MouseEnter](/docs/reference/engine/classes/GuiObject.md)
- [GuiObject.MouseLeave](/docs/reference/engine/classes/GuiObject.md)
- [GuiObject.MouseMoved](/docs/reference/engine/classes/GuiObject.md)
- [GuiObject.MouseWheelForward](/docs/reference/engine/classes/GuiObject.md)

*Security: None · Capabilities: UI*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `x` | `int` | The mouse's **X** screen coordinate in pixels, relative to the top left corner of the screen. |
| `y` | `int` | The mouse's **Y** screen coordinate in pixels, relative to the top left corner of the screen. |

### Event: GuiObject.MouseWheelForward

**Signature:** `GuiObject.MouseWheelForward(x: int, y: int)`

The WheelForward event fires when a user scrolls their mouse wheel forward
when the mouse is over a [GuiObject](/docs/reference/engine/classes/GuiObject.md) element. It is similar to
[Mouse.WheelForward](/docs/reference/engine/classes/Mouse.md), which fires regardless whether the user's
mouse is over a GUI element.

This event fires merely as an indicator of the wheel's forward movement.
This means that the **X** and **Y** mouse coordinate arguments do not
change as a result of this event. These coordinates only change when the
mouse moves, which can be tracked by the [GuiObject.MouseMoved](/docs/reference/engine/classes/GuiObject.md)
event.

##### See Also

- [GuiObject.MouseEnter](/docs/reference/engine/classes/GuiObject.md)
- [GuiObject.MouseLeave](/docs/reference/engine/classes/GuiObject.md)
- [GuiObject.MouseMoved](/docs/reference/engine/classes/GuiObject.md)
- [GuiObject.MouseWheelBackward](/docs/reference/engine/classes/GuiObject.md)

*Security: None · Capabilities: UI*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `x` | `int` | The mouse's **X** screen coordinate in pixels, relative to the top left corner of the screen. |
| `y` | `int` | The **Y** coordinate of the user's mouse. |

### Event: GuiObject.SelectionGained

**Signature:** `GuiObject.SelectionGained()`

This event fires when the Gamepad selector starts focusing on the
[GuiObject](/docs/reference/engine/classes/GuiObject.md).

If you want to check from the Gamepad select stops focusing on the GUI
element, you can use the [GuiObject.SelectionLost](/docs/reference/engine/classes/GuiObject.md) event.

When a GUI gains selection focus, the value of the
[SelectedObject](/docs/reference/engine/classes/GuiService.md) property also changes to
the that gains selection. To determine which GUI gained selection, check
the value of this property.

*Security: None · Capabilities: UI*

**Handling GUI Selection Gained**

The following example prints a message when the user selects the object with a
gamepad.

In order for this to work as expected, it must be placed in a `LocalScript`
and a child of _gui_.

```lua
local guiObject = script.Parent

local function selectionGained()
	print("The user has selected this button with a gamepad.")
end

guiObject.SelectionGained:Connect(selectionGained)
```

### Event: GuiObject.SelectionLost

**Signature:** `GuiObject.SelectionLost()`

This event fires when the Gamepad selector stops focusing on the
[GuiObject](/docs/reference/engine/classes/GuiObject.md).

If you want to check from the Gamepad select starts focusing on the GUI
element, you can use the [GuiObject.SelectionGained](/docs/reference/engine/classes/GuiObject.md) event.

When a GUI loses selection focus, the value of the
[SelectionObject](/docs/reference/engine/classes/GuiService.md) property changes either
to `nil` or to the GUI element that gains selection focus. To determine
which GUI gained selection, or if no GUI is selected, check the value of
this property.

*Security: None · Capabilities: UI*

**Handling GUI Selection Lost**

The following example prints a message when the element has its focus lost on
a gamepad.

In order for this to work as expected, it must be placed in a `LocalScript`
and a child of _gui_.

```lua
local guiObject = script.Parent

local function selectionLost()
	print("The user no longer has this selected with their gamepad.")
end

guiObject.SelectionLost:Connect(selectionLost)
```

### Event: GuiObject.TouchLongPress

**Signature:** `GuiObject.TouchLongPress(touchPositions: Array, state: UserInputState)`

This event fires after a brief moment when the player holds their finger
on the UI element using a touch-enabled device. It fires with a table of
[Vector2](/docs/reference/engine/datatypes/Vector2.md) that describe the relative screen positions of the
fingers involved in the gesture. In addition, it fires multiple times:
[UserInputState.Begin](/docs/reference/engine/enums/UserInputState.md) after a brief delay,
[UserInputState.Change](/docs/reference/engine/enums/UserInputState.md) if the player moves their finger during the
gesture, and finally [UserInputState.End](/docs/reference/engine/enums/UserInputState.md). The delay is platform
dependent; in Studio it is a little longer than one second.

*Security: None · Capabilities: UI*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `touchPositions` | `Array` | An array of [Vector2](/docs/reference/engine/datatypes/Vector2.md) that describe the **relative** positions of the fingers involved in the gesture. |
| `state` | `UserInputState` | A [UserInputState](/docs/reference/engine/enums/UserInputState.md) that describes the state of the gesture:  - Begin fires once at the beginning of the gesture (after the brief   delay) - Change fires if the player moves their finger while pressing down - End fires once at the end of the gesture when they release their   finger. |

**Move UI Element with TouchLongPress**

This code sample allows the player to manipulate the screen position of some
UI element, like a `Frame`, by holding down on the UI element for a brief
moment. Then, the player moves their finger and releases. During the gesture
the Frame is colored blue with a white outline.

```lua
local frame = script.Parent
frame.Active = true

local dragging = false
local basePosition
local startTouchPosition
local borderColor3
local backgroundColor3

local function onTouchLongPress(touchPositions, state)
	if state == Enum.UserInputState.Begin and not dragging then
		-- Start a drag
		dragging = true
		basePosition = frame.Position
		startTouchPosition = touchPositions[1]
		-- Color the frame to indicate the drag is happening
		borderColor3 = frame.BorderColor3
		backgroundColor3 = frame.BackgroundColor3
		frame.BorderColor3 = Color3.new(1, 1, 1) -- White
		frame.BackgroundColor3 = Color3.new(0, 0, 1) -- Blue
	elseif state == Enum.UserInputState.Change then
		local touchPosition = touchPositions[1]
		local deltaPosition =
			UDim2.new(0, touchPosition.X - startTouchPosition.X, 0, touchPosition.Y - startTouchPosition.Y)
		frame.Position = basePosition + deltaPosition
	elseif state == Enum.UserInputState.End and dragging then
		-- Stop the drag
		dragging = false
		frame.BorderColor3 = borderColor3
		frame.BackgroundColor3 = backgroundColor3
	end
end

frame.TouchLongPress:Connect(onTouchLongPress)
```

**Expected output:** When the player hold their finger down on the Frame, it should turn blue to indicate the beginning of a TouchLongPress gesture. Moving their finger should move the Frame accordingly. Releasing it will return the Frame to its original color.

### Event: GuiObject.TouchPan

**Signature:** `GuiObject.TouchPan(touchPositions: Array, totalTranslation: Vector2, velocity: Vector2, state: UserInputState)`

This event fires when the player moves their finger on the UI element
using a touch-enabled device. It fires shortly before
[GuiObject.TouchSwipe](/docs/reference/engine/classes/GuiObject.md) would, and does not fire with
[GuiObject.TouchTap](/docs/reference/engine/classes/GuiObject.md). This event is useful for allowing the player
to manipulate the position of UI elements on the screen.

This event fires with a table of [Vector2](/docs/reference/engine/datatypes/Vector2.md) that describe the
relative screen positions of the fingers involved in the gesture. In
addition, it fires multiple times: [UserInputState.Begin](/docs/reference/engine/enums/UserInputState.md) after a
brief delay, [UserInputState.Change](/docs/reference/engine/enums/UserInputState.md) when the player moves their
finger during the gesture, and finally with [UserInputState.End](/docs/reference/engine/enums/UserInputState.md).

*Security: None · Capabilities: UI*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `touchPositions` | `Array` | A Luau array of [Vector2](/docs/reference/engine/datatypes/Vector2.md) objects, each indicating the position of all the fingers involved in the gesture. |
| `totalTranslation` | `Vector2` | Indicates how far the pan gesture has gone from its starting point. |
| `velocity` | `Vector2` | Indicates how quickly the gesture is being performed in each dimension. |
| `state` | `UserInputState` | Indicates the [UserInputState](/docs/reference/engine/enums/UserInputState.md) of the gesture. |

**Panning UI Element**

This code sample is meant to be placed in a `LocalScript` within an inner
`Frame` that is inside an outer `Frame`, or other `GuiObject`. It allows the
player to manipulate the position of the inner frame by moving their finger on
the outer frame.

```lua
local innerFrame = script.Parent
local outerFrame = innerFrame.Parent
outerFrame.BackgroundTransparency = 0.75
outerFrame.Active = true
outerFrame.Size = UDim2.new(1, 0, 1, 0)
outerFrame.Position = UDim2.new(0, 0, 0, 0)
outerFrame.AnchorPoint = Vector2.new(0, 0)
outerFrame.ClipsDescendants = true

local dragging = false
local basePosition

local function onTouchPan(_touchPositions, totalTranslation, _velocity, state)
	if state == Enum.UserInputState.Begin and not dragging then
		dragging = true
		basePosition = innerFrame.Position
		outerFrame.BackgroundTransparency = 0.25
	elseif state == Enum.UserInputState.Change then
		innerFrame.Position = basePosition + UDim2.new(0, totalTranslation.X, 0, totalTranslation.Y)
	elseif state == Enum.UserInputState.End and dragging then
		dragging = false
		outerFrame.BackgroundTransparency = 0.75
	end
end

outerFrame.TouchPan:Connect(onTouchPan)
```

**Expected output:** When the player begins moving their finger on the outer frame, the inner frame should move with their finger.

### Event: GuiObject.TouchPinch

**Signature:** `GuiObject.TouchPinch(touchPositions: Array, scale: float, velocity: float, state: UserInputState)`

This event fires when the player uses two fingers to make a pinch or pull
gesture on the UI element using a touch-enabled device. A **pinch**
happens when two or more fingers move closer together, and a **pull**
happens when they move apart. This event fires in conjunction with
[GuiObject.TouchPan](/docs/reference/engine/classes/GuiObject.md). This event is useful for allowing the player
to manipulate the scale (size) of UI elements on the screen, and is most
often used for zooming features.

This event fires with a table of [Vector2](/docs/reference/engine/datatypes/Vector2.md) that describe the
relative screen positions of the fingers involved in the gesture. In
addition, it fires multiple times: [UserInputState.Begin](/docs/reference/engine/enums/UserInputState.md) after a
brief delay, [UserInputState.Change](/docs/reference/engine/enums/UserInputState.md) when the player moves a finger
during the gesture, and finally with [UserInputState.End](/docs/reference/engine/enums/UserInputState.md). It should
be noted that the scale should be used **multiplicatively**.

*Security: None · Capabilities: UI*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `touchPositions` | `Array` | A Luau array of [Vector2](/docs/reference/engine/datatypes/Vector2.md) objects, each indicating the position of all the fingers involved in the pinch gesture. |
| `scale` | `float` | A float that indicates the difference from the beginning of the pinch gesture. |
| `velocity` | `float` | A float indicating how quickly the pinch gesture is happening. |
| `state` | `UserInputState` | Indicates the [UserInputState](/docs/reference/engine/enums/UserInputState.md) of the gesture. |

**Pinch/Pull Scaling**

This code sample is meant for a `LocalScript` within an inner `Frame` that is
inside an outer `Frame`, or other `GuiObject`. It allows the player to scale
the inner frame by performing a [GuiObject.TouchPinch](/docs/reference/engine/classes/GuiObject.md) gesture on the
outer frame.

```lua
local innerFrame = script.Parent
local outerFrame = innerFrame.Parent
outerFrame.BackgroundTransparency = 0.75
outerFrame.Active = true
outerFrame.Size = UDim2.new(1, 0, 1, 0)
outerFrame.Position = UDim2.new(0, 0, 0, 0)
outerFrame.AnchorPoint = Vector2.new(0, 0)
outerFrame.ClipsDescendants = true

local dragging = false
local uiScale = Instance.new("UIScale")
uiScale.Parent = innerFrame
local baseScale

local function onTouchPinch(_touchPositions, scale, _velocity, state)
	if state == Enum.UserInputState.Begin and not dragging then
		dragging = true
		baseScale = uiScale.Scale
		outerFrame.BackgroundTransparency = 0.25
	elseif state == Enum.UserInputState.Change then
		uiScale.Scale = baseScale * scale -- Notice the multiplication here
	elseif state == Enum.UserInputState.End and dragging then
		dragging = false
		outerFrame.BackgroundTransparency = 0.75
	end
end

outerFrame.TouchPinch:Connect(onTouchPinch)
```

**Expected output:** When the player performs a pinch gesture, the inner frame should get smaller. When the player performs a pull gesture, the inner frame should get bigger. Note that if the inner frame renders text, there may be text rendering issues using a `UIScale`.

### Event: GuiObject.TouchRotate

**Signature:** `GuiObject.TouchRotate(touchPositions: Array, rotation: float, velocity: float, state: UserInputState)`

This event fires when the player uses two fingers to make a pinch or pull
gesture on the UI element using a touch-enabled device. Rotation occurs
when the angle of the line between two fingers changes. This event fires
in conjunction with [GuiObject.TouchPan](/docs/reference/engine/classes/GuiObject.md). This event is useful for
allowing the player to manipulate the rotation of UI elements on the
screen.

This event fires with a table of [Vector2](/docs/reference/engine/datatypes/Vector2.md) that describe the
relative screen positions of the fingers involved in the gesture. In
addition, it fires multiple times: [UserInputState.Begin](/docs/reference/engine/enums/UserInputState.md) after a
brief delay, [UserInputState.Change](/docs/reference/engine/enums/UserInputState.md) when the player moves a finger
during the gesture, and finally with [UserInputState.End](/docs/reference/engine/enums/UserInputState.md).

*Security: None · Capabilities: UI*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `touchPositions` | `Array` | A Luau array of [Vector2](/docs/reference/engine/datatypes/Vector2.md) objects, each indicating the position of all the fingers involved in the gesture. |
| `rotation` | `float` | A float indicating how much the rotation has gone from the start of the gesture. |
| `velocity` | `float` | A float that indicates how quickly the gesture is being performed. |
| `state` | `UserInputState` | Indicates the [UserInputState](/docs/reference/engine/enums/UserInputState.md) of the gesture. |

**Touch Rotation**

This code sample is meant for a `LocalScript` within an inner `Frame` that is
inside an outer `Frame`, or other `GuiObject`. It allows the player to rotate
the inner frame by performing a [GuiObject.TouchRotate](/docs/reference/engine/classes/GuiObject.md) gesture on the
outer frame.

```lua
local innerFrame = script.Parent
local outerFrame = innerFrame.Parent
outerFrame.BackgroundTransparency = 0.75
outerFrame.Active = true
outerFrame.Size = UDim2.new(1, 0, 1, 0)
outerFrame.Position = UDim2.new(0, 0, 0, 0)
outerFrame.AnchorPoint = Vector2.new(0, 0)
outerFrame.ClipsDescendants = true

local dragging = false
local baseRotation = innerFrame.Rotation

local function onTouchRotate(_touchPositions, rotation, _velocity, state)
	if state == Enum.UserInputState.Begin and not dragging then
		dragging = true
		baseRotation = innerFrame.Rotation
		outerFrame.BackgroundTransparency = 0.25
	elseif state == Enum.UserInputState.Change then
		innerFrame.Rotation = baseRotation + rotation
	elseif state == Enum.UserInputState.End and dragging then
		dragging = false
		outerFrame.BackgroundTransparency = 0.75
	end
end

outerFrame.TouchRotate:Connect(onTouchRotate)
```

**Expected output:** When the player rotates two fingers on the outer frame, the inner frame should rotate accordingly.

### Event: GuiObject.TouchSwipe

**Signature:** `GuiObject.TouchSwipe(swipeDirection: SwipeDirection, numberOfTouches: int)`

This event fires when the player performs a swipe gesture on the UI
element using a touch-enabled device. It fires with the direction of the
gesture (Up, Down, Left or Right) and the number of touch points involved
in the gesture. Swipe gestures are often used to change tabs in mobile
UIs.

*Security: None · Capabilities: UI*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `swipeDirection` | `SwipeDirection` | A [SwipeDirection](/docs/reference/engine/enums/SwipeDirection.md) indicating the direction of the swipe gesture (Up, Down, Left or Right). |
| `numberOfTouches` | `int` | The number of touch points involved in the gesture (usually 1). |

**Bouncing Color Picker**

This code sample will cause a `Frame` (or other `GuiObject`) to bounce when a
swipe gesture is performed on a touch-enabled device (or Studio's emulator).
Horizontal swipes will change the hue of the
[GuiObject.BackgroundColor3](/docs/reference/engine/classes/GuiObject.md), while vertical swipes will change the
saturation.

```lua
local frame = script.Parent
frame.Active = true

-- How far the frame should bounce on a successful swipe
local BOUNCE_DISTANCE = 50

-- Current state of the frame
local basePosition = frame.Position
local hue = 0
local saturation = 128

local function updateColor()
	frame.BackgroundColor3 = Color3.fromHSV(hue / 256, saturation / 256, 1)
end

local function onTouchSwipe(swipeDir, _touchCount)
	-- Change the BackgroundColor3 based on the swipe direction
	local deltaPos
	if swipeDir == Enum.SwipeDirection.Right then
		deltaPos = UDim2.new(0, BOUNCE_DISTANCE, 0, 0)
		hue = (hue + 16) % 255
	elseif swipeDir == Enum.SwipeDirection.Left then
		deltaPos = UDim2.new(0, -BOUNCE_DISTANCE, 0, 0)
		hue = (hue - 16) % 255
	elseif swipeDir == Enum.SwipeDirection.Up then
		deltaPos = UDim2.new(0, 0, 0, -BOUNCE_DISTANCE)
		saturation = (saturation + 16) % 255
	elseif swipeDir == Enum.SwipeDirection.Down then
		deltaPos = UDim2.new(0, 0, 0, BOUNCE_DISTANCE)
		saturation = (saturation - 16) % 255
	else
		deltaPos = UDim2.new()
	end
	-- Update the color and bounce the frame a little
	updateColor()
	frame.Position = basePosition + deltaPos
	frame:TweenPosition(basePosition, Enum.EasingDirection.Out, Enum.EasingStyle.Bounce, 0.7, true)
end

frame.TouchSwipe:Connect(onTouchSwipe)
updateColor()
```

**Expected output:** The Frame will bounce and change color in a direction when you perform a swipe gesture on it using a touch-enabled device (or Studio's emulator).

### Event: GuiObject.TouchTap

**Signature:** `GuiObject.TouchTap(touchPositions: Array)`

This event fires when the player performs a tap gesture on the UI element
using a touch-enabled device. A tap is a quick single touch without any
movement involved (a longer press would fire
[GuiObject.TouchLongPress](/docs/reference/engine/classes/GuiObject.md), and moving during the touch would fire
[GuiObject.TouchPan](/docs/reference/engine/classes/GuiObject.md) and/or [GuiObject.TouchSwipe](/docs/reference/engine/classes/GuiObject.md)). It fires
with a table of [Vector2](/docs/reference/engine/datatypes/Vector2.md) objects that describe the relative
positions of the fingers involved in the gesture.

*Security: None · Capabilities: UI*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `touchPositions` | `Array` | An array of [Vector2](/docs/reference/engine/datatypes/Vector2.md) that describe the **relative** positions of the fingers involved in the gesture. |

**Tap Transparency Toggle**

This code sample will toggle the [GuiObject.BackgroundTransparency](/docs/reference/engine/classes/GuiObject.md) of a
UI element, like a `Frame`, when it is tapped on a touch-enabled device.

```lua
local frame = script.Parent
frame.Active = true

local function onTouchTap()
	-- Toggle background transparency
	if frame.BackgroundTransparency > 0 then
		frame.BackgroundTransparency = 0
	else
		frame.BackgroundTransparency = 0.75
	end
end

frame.TouchTap:Connect(onTouchTap)
```

**Expected output:** Upon briefly tapping the UI element, it should toggle the BackgroundTransparency.

### Event: GuiObject.DragBegin

**Signature:** `GuiObject.DragBegin(initialPosition: UDim2)`

> **Deprecated:** This property is deprecated. Use [UIDragDetector](/docs/reference/engine/classes/UIDragDetector.md) instead, as it supports more input types and can be better customized.

This event fires when a player begins dragging the object.

See also [GuiObject.DragStopped](/docs/reference/engine/classes/GuiObject.md).

*Security: None · Capabilities: UI*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `initialPosition` | `UDim2` | A [UDim2](/docs/reference/engine/datatypes/UDim2.md) value of the position of the [GuiObject](/docs/reference/engine/classes/GuiObject.md) before any drag operation began. |

**(Deprecated) Print the Position of a GUI When Dragging Begins**

The below example assumes it's within a GuiObject such as a `TextButton`, and
that the [GuiObject.Draggable](/docs/reference/engine/classes/GuiObject.md) property is set to true. It will print
the UDim2 of where the player started dragging the object from.

```lua
script.Parent.DragBegin:Connect(function(udim2)
	local x = udim2.X
	local y = udim2.Y

	local xScale = x.Scale
	local xOffset = x.Offset

	local yScale = y.Scale
	local yOffset = y.Offset

	print(
		("The player started dragging the object at UDim2.new(%f, %d, %f, %d)"):format(xScale, xOffset, yScale, yOffset)
	)
end)
```

### Event: GuiObject.DragStopped

**Signature:** `GuiObject.DragStopped(x: int, y: int)`

> **Deprecated:** This property is deprecated. Use [UIDragDetector](/docs/reference/engine/classes/UIDragDetector.md) instead, as it supports more input types and can be better customized.

This event fires when a player stops dragging the object.

See also [GuiObject.DragBegin](/docs/reference/engine/classes/GuiObject.md).

*Security: None · Capabilities: UI*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `x` | `int` | The mouse's **X** screen location in pixels, relative to the top left corner of the screen. |
| `y` | `int` | The mouse's **Y** screen location in pixels, relative to the top left corner of the screen. |

**(Deprecated) Print the Position of a GUI When Dragging Stops**

The below example assumes it's within a GuiObject such as a `TextButton`, and
that the [GuiObject.Draggable](/docs/reference/engine/classes/GuiObject.md) property is set to true. It will print
the X and Y of where the player stopped dragging the GUI. For example, if the
player were to stop dragging the object at 189, 180 the below would print The
player stopped dragging the GuiObject at (189, 180)

```lua
script.Parent.DragStopped:Connect(function(x, Y)
	print(("The player stopped dragging the GuiObject at (%i, %i)"):format(x, Y))
end)
```

## Inherited Members

### From [GuiBase2d](/docs/reference/engine/classes/GuiBase2d.md)

- **Property `AbsolutePosition`** (`Vector2`): Describes the actual screen position of a GuiBase2d element, in
- **Property `AbsoluteRotation`** (`float`): Describes the actual screen rotation of a GuiBase2d element, in
- **Property `AbsoluteSize`** (`Vector2`): Describes the actual screen size of a GuiBase2d element, in
- **Property `AutoLocalize`** (`boolean`): When set to `true`, localization will be applied to this GuiBase2d
- **Property `Localize`** (`boolean`): Automatically set to true when a localization table's *(deprecated, hidden)*
- **Property `RootLocalizationTable`** (`LocalizationTable`): A reference to a LocalizationTable to be used to apply automated
- **Property `SelectionBehaviorDown`** (`SelectionBehavior`): Customizes gamepad selection behavior in the down direction.
- **Property `SelectionBehaviorLeft`** (`SelectionBehavior`): Customizes gamepad selection behavior in the left direction.
- **Property `SelectionBehaviorRight`** (`SelectionBehavior`): Customizes gamepad selection behavior in the right direction.
- **Property `SelectionBehaviorUp`** (`SelectionBehavior`): Customizes gamepad selection behavior in the up direction.
- **Property `SelectionGroup`** (`boolean`): Allows customization of gamepad selection movement.
- **Event `SelectionChanged`**: Fires when the gamepad selection moves to, leaves, or changes within the

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