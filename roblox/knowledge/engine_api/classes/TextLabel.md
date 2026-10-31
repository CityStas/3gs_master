---
name: TextLabel
last_updated: 2026-10-30T19:55:53Z
inherits:
  - GuiLabel
  - GuiObject
  - GuiBase2d
  - GuiBase
  - Instance
  - Object
type: class
memory_category: Gui
summary: "A 2D user interface element that displays non-interactive text."
---

# Class: TextLabel

> A 2D user interface element that displays non-interactive text.

## Description

A [TextLabel](/docs/reference/engine/classes/TextLabel.md) renders a rectangle, like a [Frame](/docs/reference/engine/classes/Frame.md), with styled
text. The rectangle can be used to define text boundaries, text scaling
([TextScaled](/docs/reference/engine/classes/TextLabel.md)), wrapping
([TextWrapped](/docs/reference/engine/classes/TextLabel.md)), and alignment
([TextXAlignment](/docs/reference/engine/classes/TextLabel.md) and/or
[TextYAlignment](/docs/reference/engine/classes/TextLabel.md)).

This class contains properties that control the display of the text, such as
[Font](/docs/reference/engine/classes/TextLabel.md) and [TextColor3](/docs/reference/engine/classes/TextLabel.md). To
display only text and hide the background rectangle, set
[BackgroundTransparency](/docs/reference/engine/classes/TextLabel.md) to `1`.

A [UITextSizeConstraint](/docs/reference/engine/classes/UITextSizeConstraint.md) object can be used to constrain the size of
text with [TextScaled](/docs/reference/engine/classes/TextLabel.md) enabled. It is recommended
that the size of text is no lower than `9`, otherwise it may not be visible to
many users.

## Code Samples

**Game State Text**

This code sample mirrors the contents of a StringValue into a TextLabel,
updating and setting the color of the text as it changes.

```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")

-- Place a StringValue called "GameState" in the ReplicatedStorage
local vGameState = ReplicatedStorage:WaitForChild("GameState")
-- Place this code in a TextLabel
local textLabel = script.Parent

-- Some colors we'll use with TextColor3
local colorNormal = Color3.new(0, 0, 0) -- black
local colorCountdown = Color3.new(1, 0.5, 0) -- orange
local colorRound = Color3.new(0.25, 0.25, 1) -- blue

-- We'll run this function to update the TextLabel as the state of the
-- game changes.
local function update()
	-- Update the text
	textLabel.Text = "State: " .. vGameState.Value
	-- Set the color of the text based on the current game state
	if vGameState.Value == "Countdown" then
		textLabel.TextColor3 = colorCountdown
	elseif vGameState.Value == "Round" then
		textLabel.TextColor3 = colorRound
	else
		textLabel.TextColor3 = colorNormal
	end
end

-- Pattern: update once when we start and also when vGameState changes
-- We should always see the most updated GameState.
update()
vGameState.Changed:Connect(update)
```

## Properties

### Property: TextLabel.ContentText

```json
{
  "type": "string",
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
  "category": "Text",
  "capabilities": [
    "UI"
  ]
}
```

This property provides a copy of [Text](/docs/reference/engine/classes/TextLabel.md) that contains
exactly what is being rendered by the [TextLabel](/docs/reference/engine/classes/TextLabel.md). This is useful
for eliminating style tags used for [rich text](/docs/en-us/ui/rich-text.md)
markup; for example, when [RichText](/docs/reference/engine/classes/TextLabel.md) is enabled,
the [ContentText](/docs/reference/engine/classes/TextLabel.md) property shows the text as
it appears to the user.

| RichText | Text | ContentText |
| --- | --- | --- |
| `false` | <b>Hello,
 world!</b> | <b>Hello,
 world!</b> |
| `true` | <b>Hello,
 world!</b> | Hello,
 world! |

### Property: TextLabel.FontFace

```json
{
  "type": "Datatype.Font",
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
  "category": "Text",
  "capabilities": [
    "UI"
  ]
}
```

This property is similar to the [Font](/docs/reference/engine/classes/TextLabel.md) property but
allows setting fonts that don't exist in [Font](/docs/reference/engine/enums/Font.md).

This property is kept in sync with the [Font](/docs/reference/engine/classes/TextLabel.md)
property, such that when setting [FontFace](/docs/reference/engine/classes/TextLabel.md), the
font is set to the corresponding [Font](/docs/reference/engine/enums/Font.md) value or to
[Font.Unknown](/docs/reference/engine/enums/Font.md) if there are no matches.

### Property: TextLabel.LineHeight

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
  "category": "Text",
  "capabilities": [
    "UI"
  ]
}
```

Controls the height of lines as a multiple of the font's `em` square size
by scaling the spacing between lines of text in the [TextLabel](/docs/reference/engine/classes/TextLabel.md).
Valid values range from `1.0` to `3.0`, defaulting to `1.0`.

### Property: TextLabel.MaxVisibleGraphemes

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
  "category": "Text",
  "capabilities": [
    "UI"
  ]
}
```

This property controls the maximum number of graphemes (or units of text)
that are shown on the [TextLabel](/docs/reference/engine/classes/TextLabel.md). It is primarily provided as an
easy way to create a
[typewriter effect](/docs/en-us/ui/animation.md#typewriter-effect) where the
characters appear one at a time.

Changing the property does not change the position or size of the visible
graphemes; the layout will be calculated as if all graphemes are visible.

Setting the property to `-1` disables the limit and shows the entirety of
the [Text](/docs/reference/engine/classes/TextLabel.md).

### Property: TextLabel.OpenTypeFeatures

```json
{
  "type": "string",
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
  "category": "Text",
  "capabilities": [
    "UI"
  ]
}
```

This property is a comma-separated list of OpenType feature tags that are
applied when the [TextLabel](/docs/reference/engine/classes/TextLabel.md) shapes and renders its text, such as
`zero` for slashed zeros or `ss03` for a stylistic set. It defaults to an
empty string, which applies no additional features.

Each entry uses the standard OpenType feature-string syntax (for example,
`zero` or `ss03`). Only a supported subset of features is applied; a
feature that isn't supported, a malformed string, or the bracketed
partial-enabling syntax (for example, `zero[1:3]`) is rejected, and the
reason is reported through
[OpenTypeFeaturesError](/docs/reference/engine/classes/TextLabel.md).

This property supports [styling](/docs/en-us/ui/styling.md).

### Property: TextLabel.OpenTypeFeaturesError

```json
{
  "type": "string",
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
  "category": "Text",
  "capabilities": [
    "UI"
  ]
}
```

This read-only property reports the error, if any, encountered while
parsing and applying the
[OpenTypeFeatures](/docs/reference/engine/classes/TextLabel.md) string. It defaults to
an empty string, which indicates that the requested features were applied
successfully.

When a feature can't be applied, this property is set to one of the
following messages:

- `Failed to parse features.` when a feature string is malformed.
- `Unsupported feature: <tag>` when a feature isn't part of the supported
  set.
- `Partial feature enabling not supported.` when the string uses the
  bracketed range syntax.

### Property: TextLabel.RichText

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
  "category": "Text",
  "capabilities": [
    "UI"
  ]
}
```

This property determines whether the [TextLabel](/docs/reference/engine/classes/TextLabel.md) renders its text
using [rich text](/docs/en-us/ui/rich-text.md) markup to style sections of
the string in bold, italics, specific colors, and more.

To use rich text, simply include rich text formatting tags in the
[Text](/docs/reference/engine/classes/TextLabel.md) string.

### Property: TextLabel.Text

```json
{
  "type": "string",
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
  "category": "Text",
  "capabilities": [
    "UI"
  ]
}
```

This property determines the text content rendered by the
[TextLabel](/docs/reference/engine/classes/TextLabel.md). The visual properties of the string rendered to the
screen is determined by [TextColor3](/docs/reference/engine/classes/TextLabel.md),
[TextTransparency](/docs/reference/engine/classes/TextLabel.md),
[TextSize](/docs/reference/engine/classes/TextLabel.md), [Font](/docs/reference/engine/classes/TextLabel.md),
[TextScaled](/docs/reference/engine/classes/TextLabel.md),
[TextWrapped](/docs/reference/engine/classes/TextLabel.md),
[TextXAlignment](/docs/reference/engine/classes/TextLabel.md) and
[TextYAlignment](/docs/reference/engine/classes/TextLabel.md).

It is possible to render emoji such as 🔒 and other symbols which aren't
affected by the [TextColor3](/docs/reference/engine/classes/TextLabel.md) property. These
can be pasted into [Script](/docs/reference/engine/classes/Script.md) and [LocalScript](/docs/reference/engine/classes/LocalScript.md) objects, as well
as the field within the [Properties](/docs/en-us/studio/properties.md)
window.

This property may contain newline characters. Similarly, this property may
contain a tab character, but it will render as a space instead.

**Fading Banner**

This code sample creates a fading banner for a TextLabel. It fades text out,
chooses a random string (avoiding repetition), and fades back in.

```lua
local TweenService = game:GetService("TweenService")

local textLabel = script.Parent

local content = {
	"Welcome to my game!",
	"Be sure to have fun!",
	"Please give suggestions!",
	"Be nice to other players!",
	"Don't grief other players!",
	"Check out the shop!",
	"Tip: Don't die!",
}

local tweenInfo = TweenInfo.new(1, Enum.EasingStyle.Sine, Enum.EasingDirection.InOut)

local RNG = Random.new()

local fadeIn = TweenService:Create(textLabel, tweenInfo, {
	TextTransparency = 0,
})

local fadeOut = TweenService:Create(textLabel, tweenInfo, {
	TextTransparency = 1,
})

local lastIndex
while true do
	-- Step 0: Fade out before doing anything
	fadeOut:Play()
	task.wait(tweenInfo.Time)

	-- Step 1: pick content that wasn't the last displayed
	local index
	repeat
		index = RNG:NextInteger(1, #content)
	until lastIndex ~= index
	-- Make sure we don't show the same thing next time
	lastIndex = index

	-- Step 2: show the content
	textLabel.Text = content[index]
	fadeIn:Play()
	task.wait(tweenInfo.Time + 1)
end
```

**Emoji in Text**

This code sample demonstrates emoji rendering using the Text property.

```lua
local textLabel = script.Parent

local moods = {
	["happy"] = "😃",
	["sad"] = "😢",
	["neutral"] = "😐",
	["tired"] = "😫",
}

while true do
	for mood, face in pairs(moods) do
		textLabel.Text = "I am feeling " .. mood .. "! " .. face
		task.wait(1)
	end
end
```

### Property: TextLabel.TextBounds

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
  "thread_safety": "ReadSafe",
  "category": "Text",
  "capabilities": [
    "UI"
  ]
}
```

This read-only property reflects the absolute size of rendered text in
offsets, meaning that if you try to fit text into a rectangle, this
property would reflect the minimum dimensions of the rectangle you'd need
in order to fit the text.

Using [TextService:GetTextSize()](/docs/reference/engine/classes/TextService.md), you can predict what
[TextBounds](/docs/reference/engine/classes/TextLabel.md) will be given a string,
[Font](/docs/reference/engine/classes/TextLabel.md), [TextSize](/docs/reference/engine/classes/TextLabel.md), and
frame size.

**Dynamic TextBox Size**

This code sample dynamically resizes a TextLabel, TextButton or TextBox to
match the size of its TextBounds. Try changing the minimum width/height and
pasting into a LocalScript in a TextBox.

```lua
local textBox = script.Parent

-- The smallest the TextBox will go
local minWidth, minHeight = 10, 10

-- Set alignment so our text doesn't wobble a bit while we type
textBox.TextXAlignment = Enum.TextXAlignment.Left
textBox.TextYAlignment = Enum.TextYAlignment.Top

local function updateSize()
	textBox.Size = UDim2.new(0, math.max(minWidth, textBox.TextBounds.X), 0, math.max(minHeight, textBox.TextBounds.Y))
end

textBox:GetPropertyChangedSignal("TextBounds"):Connect(updateSize)
```

### Property: TextLabel.TextColor3

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
  "category": "Text",
  "capabilities": [
    "UI"
  ]
}
```

This property determines the color of all the text rendered by the
[TextLabel](/docs/reference/engine/classes/TextLabel.md) element.

**Countdown Text**

This code sample makes a TextLabel or TextButton count backwards from 10,
setting the text color as it does so.

```lua
-- Place this code in a LocalScript within a TextLabel/TextButton
local textLabel = script.Parent

-- Some colors we'll use with TextColor3
local colorNormal = Color3.new(0, 0, 0) -- black
local colorSoon = Color3.new(1, 0.5, 0.5) -- red
local colorDone = Color3.new(0.5, 1, 0.5) -- green

-- Loop infinitely
while true do
	-- Count backwards from 10 to 1
	for i = 10, 1, -1 do
		-- Set the text
		textLabel.Text = "Time: " .. i
		-- Set the color based on how much time is left
		if i > 3 then
			textLabel.TextColor3 = colorNormal
		else
			textLabel.TextColor3 = colorSoon
		end
		task.wait(1)
	end
	textLabel.Text = "GO!"
	textLabel.TextColor3 = colorDone
	task.wait(2)
end
```

### Property: TextLabel.TextDirection

```json
{
  "type": "TextDirection",
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
  "category": "Text",
  "capabilities": [
    "UI"
  ]
}
```

This property sets the base direction in which the [TextLabel](/docs/reference/engine/classes/TextLabel.md)
orders and renders its text, using a value of the [TextDirection](/docs/reference/engine/enums/TextDirection.md)
enum. It defaults to [TextDirection.Auto](/docs/reference/engine/enums/TextDirection.md), which infers the direction
from the content of [Text](/docs/reference/engine/classes/TextLabel.md) so that left-to-right and
right-to-left scripts are ordered correctly. Set it to
[TextDirection.LeftToRight](/docs/reference/engine/enums/TextDirection.md) or [TextDirection.RightToLeft](/docs/reference/engine/enums/TextDirection.md) to
force a specific direction regardless of the text content.

This property supports [styling](/docs/en-us/ui/styling.md).

### Property: TextLabel.TextFits

```json
{
  "type": "boolean",
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
  "category": "Text",
  "capabilities": [
    "UI"
  ]
}
```

This read-only property is `true` when the text rendered by the
[TextLabel](/docs/reference/engine/classes/TextLabel.md) fits entirely within the element's
[GuiBase2d.AbsoluteSize](/docs/reference/engine/classes/GuiBase2d.md), and `false` when the text is too large and
is therefore clipped or truncated. It's computed from
[TextBounds](/docs/reference/engine/classes/TextLabel.md) relative to the available space,
so it reflects the combined effect of
[TextWrapped](/docs/reference/engine/classes/TextLabel.md),
[TextTruncate](/docs/reference/engine/classes/TextLabel.md), and
[TextScaled](/docs/reference/engine/classes/TextLabel.md).

### Property: TextLabel.TextScaled

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
  "category": "Text",
  "capabilities": [
    "UI"
  ]
}
```

This property determines whether text is scaled so that it fills the
label's entire space. When enabled, [TextSize](/docs/reference/engine/classes/TextLabel.md) is
ignored and [TextWrapped](/docs/reference/engine/classes/TextLabel.md) is automatically
enabled. This property is useful for rendering text elements within
[BillboardGuis](/docs/reference/engine/classes/BillboardGui.md). When this property is used for
[on-screen UI](/docs/en-us/ui/on-screen-containers.md), it may be helpful to
use a [UITextSizeConstraint](/docs/reference/engine/classes/UITextSizeConstraint.md) to restrict the range of possible text
sizes.

##### Automatic Sizing

It's recommended that you avoid usage of
[TextScaled](/docs/reference/engine/classes/TextLabel.md) and adjust UI to take advantage of
the [AutomaticSize](/docs/reference/engine/classes/GuiObject.md) property instead. Here
are the core differences between the two properties:

- [TextScaled](/docs/reference/engine/classes/TextLabel.md) scales the content (text) to
  accommodate the UI. Without careful consideration, some text may become
  unreadable if scaled too small.

- [AutomaticSize](/docs/reference/engine/classes/GuiObject.md) resizes the UI to
  accommodate content while maintaining a consistent font size. For more
  information, see [here](/docs/en-us/ui/size-modifiers.md#automatic-sizing).

Additionally, it's recommended that you avoid applying both
[AutomaticSize](/docs/reference/engine/classes/GuiObject.md) and
[TextScaled](/docs/reference/engine/classes/TextLabel.md) and to the same [TextLabel](/docs/reference/engine/classes/TextLabel.md).
[AutomaticSize](/docs/reference/engine/classes/GuiObject.md) determines the maximum
amount of available space that a [GuiObject](/docs/reference/engine/classes/GuiObject.md) can use (in this case,
text), while [TextScaled](/docs/reference/engine/classes/TextLabel.md) uses the available
space determined by [AutomaticSize](/docs/reference/engine/classes/GuiObject.md) to scale
the font size up to the maximum font size (100) if there are no size
constraints.

### Property: TextLabel.TextSize

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
  "category": "Text",
  "capabilities": [
    "UI"
  ]
}
```

This property determines the height of one line of rendered text. The unit
is in offsets, not points (which is used in most document editing
programs). The [Font.Legacy](/docs/reference/engine/enums/Font.md) font does not hold this property.

**"Kaboom!" Text**

This code sample repeatedly tweens a TextLabel's TextSize from 5 to 100 and
fades out the text as it grows in size.

```lua
local textLabel = script.Parent

textLabel.Text = "Kaboom!"

while true do
	for size = 5, 100, 5 do
		textLabel.TextSize = size
		textLabel.TextTransparency = size / 100
		task.wait()
	end
	task.wait(1)
end
```

### Property: TextLabel.TextStrokeColor3

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
  "category": "Text",
  "capabilities": [
    "UI"
  ]
}
```

This property sets the color of the stroke, or outline, of rendered text.
Along with
[TextStrokeTransparency](/docs/reference/engine/classes/TextLabel.md), it
determines the final visual appearance of the text stroke.

As a powerful alternative which supports color gradients, see
[UIStroke](/docs/reference/engine/classes/UIStroke.md).

### Property: TextLabel.TextStrokeTransparency

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
  "category": "Text",
  "capabilities": [
    "UI"
  ]
}
```

This property sets the transparency of the stroke, or outline, of rendered
text. Along with [TextStrokeColor3](/docs/reference/engine/classes/TextLabel.md), it
determines the final visual appearance of the text stroke.

Note that text stroke is multiple renderings of the same transparency, so
this property is essentially multiplicative on itself four times over.
Therefore, it's recommended to set
[TextStrokeTransparency](/docs/reference/engine/classes/TextLabel.md) to a value
in the range of `0.75` to `1` for more a more subtle effect.

As a powerful alternative which supports color gradients, see
[UIStroke](/docs/reference/engine/classes/UIStroke.md).

**Text Highlight Oscillation**

This code sample oscillates a TextLabel's TextStrokeTransparency so that it
blinks the highlight of a text.

```lua
local textLabel = script.Parent

-- How fast the highlight ought to blink
local freq = 2

-- Set to yellow highlight color
textLabel.TextStrokeColor3 = Color3.new(1, 1, 0)

while true do
	-- math.sin oscillates from -1 to 1, so we change the range to 0 to 1:
	local transparency = math.sin(workspace.DistributedGameTime * math.pi * freq) * 0.5 + 0.5
	textLabel.TextStrokeTransparency = transparency
	task.wait()
end
```

### Property: TextLabel.TextTransparency

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
  "category": "Text",
  "capabilities": [
    "UI"
  ]
}
```

This property determines the transparency of all the text rendered by the
[TextLabel](/docs/reference/engine/classes/TextLabel.md).

### Property: TextLabel.TextTruncate

```json
{
  "type": "TextTruncate",
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
  "category": "Text",
  "capabilities": [
    "UI"
  ]
}
```

This property controls how the [TextLabel](/docs/reference/engine/classes/TextLabel.md) truncates text that is
too large to fit within the element, using a value of the
[TextTruncate](/docs/reference/engine/enums/TextTruncate.md) enum. It defaults to [TextTruncate.None](/docs/reference/engine/enums/TextTruncate.md), which
leaves text untruncated. [TextTruncate.AtEnd](/docs/reference/engine/enums/TextTruncate.md) truncates at word
boundary and replaces the overflowing graphemes with an ellipsis (`...`),
respecting word boundaries where possible, while
[TextTruncate.SplitWord](/docs/reference/engine/enums/TextTruncate.md) truncates inside a word when the line ends
in the middle of one.

This property supports [styling](/docs/en-us/ui/styling.md).

### Property: TextLabel.TextWrapped

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
  "category": "Text",
  "capabilities": [
    "UI"
  ]
}
```

When enabled, this property will render text on multiple lines within a
[TextLabel](/docs/reference/engine/classes/TextLabel.md) element's space so that
[TextBounds](/docs/reference/engine/classes/TextLabel.md) will never exceed the
[GuiBase2d.AbsoluteSize](/docs/reference/engine/classes/GuiBase2d.md) of the element. This is achieved by
breaking long lines of text into multiple lines.

Line breaks will prefer whitespace; should a long unbroken word exceed the
width of the element, that word will be broken into multiple lines.

If further line breaks would cause the vertical height of the text (the
**Y** component of [TextBounds](/docs/reference/engine/classes/TextLabel.md)) to exceed the
vertical height of the element (the **Y** component of
[GuiBase2d.AbsoluteSize](/docs/reference/engine/classes/GuiBase2d.md)), then that line will not be rendered at
all.

**Long Text Wrapping**

This code sample demonstrates TextWrap by spelling out a long chunk of text
progressively. If the text doesn't fit, it turns a different color.

```lua
local textLabel = script.Parent

-- This text wrapping demo is best shown on a 200x50 px rectangle
textLabel.Size = UDim2.new(0, 200, 0, 50)

-- Some content to spell out
local content = "Here's a long string of words that will "
	.. "eventually exceed the UI element's width "
	.. "and form line breaks. Useful for paragraphs "
	.. "that are really long."

-- A function that will spell text out two characters at a time
local function spellTheText()
	-- Iterate from 1 to the length of our content
	for i = 1, content:len() do
		-- Get a substring of our content: 1 to i
		textLabel.Text = content:sub(1, i)
		-- Color the text if it doesn't fit in our box
		if textLabel.TextFits then
			textLabel.TextColor3 = Color3.new(0, 0, 0) -- Black
		else
			textLabel.TextColor3 = Color3.new(1, 0, 0) -- Red
		end
		-- Wait a brief moment on even lengths
		if i % 2 == 0 then
			task.wait()
		end
	end
end

while true do
	-- Spell the text with scale/wrap off
	textLabel.TextWrapped = false
	textLabel.TextScaled = false
	spellTheText()
	task.wait(1)
	-- Spell the text with wrap on
	textLabel.TextWrapped = true
	textLabel.TextScaled = false
	spellTheText()
	task.wait(1)
	-- Spell the text with text scaling on
	-- Note: Text turns red (TextFits = false) once text has to be
	-- scaled down in order to fit within the UI element.
	textLabel.TextScaled = true
	-- Note: TextWrapped is enabled implicitly when TextScaled = true
	--textLabel.TextWrapped = true
	spellTheText()
	task.wait(1)
end
```

### Property: TextLabel.TextXAlignment

```json
{
  "type": "TextXAlignment",
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
  "category": "Text",
  "capabilities": [
    "UI"
  ]
}
```

This property determines the horizontal alignment of text rendered within
the object's space. It is used in conjunction with
[TextYAlignment](/docs/reference/engine/classes/TextLabel.md) to fully determine text
alignment on both axes.

Note that this property won't affect the read-only properties
[TextBounds](/docs/reference/engine/classes/TextLabel.md) and
[TextFits](/docs/reference/engine/classes/TextLabel.md).

**Text Alignment**

This code sample shows all the different text alignment combinations by
iterating over each enum item. It is meant to be placed within a TextLabel,
TextButton or TextBox.

```lua
-- Paste this in a LocalScript within a TextLabel/TextButton/TextBox
local textLabel = script.Parent

local function setAlignment(xAlign, yAlign)
	textLabel.TextXAlignment = xAlign
	textLabel.TextYAlignment = yAlign
	textLabel.Text = xAlign.Name .. " + " .. yAlign.Name
end

while true do
	-- Iterate over both TextXAlignment and TextYAlignment enum items
	for _, yAlign in pairs(Enum.TextYAlignment:GetEnumItems()) do
		for _, xAlign in pairs(Enum.TextXAlignment:GetEnumItems()) do
			setAlignment(xAlign, yAlign)
			task.wait(1)
		end
	end
end
```

### Property: TextLabel.TextYAlignment

```json
{
  "type": "TextYAlignment",
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
  "category": "Text",
  "capabilities": [
    "UI"
  ]
}
```

This property determines the vertical alignment of text rendered within
the object's space. It is used in conjunction with
[TextXAlignment](/docs/reference/engine/classes/TextLabel.md) to fully determine text
alignment on both axes.

Note that this property won't affect the read-only properties
[TextBounds](/docs/reference/engine/classes/TextLabel.md) and
[TextFits](/docs/reference/engine/classes/TextLabel.md).

### Property: TextLabel.FontSize

```json
{
  "type": "FontSize",
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
  "category": "Text",
  "capabilities": [
    "UI"
  ]
}
```

> **Deprecated:** This property is deprecated in favor of [TextSize](/docs/reference/engine/classes/TextLabel.md) which is an integer and not an enum and thus offers far more options for sizes.

This property determines the font size to be used.

### Property: TextLabel.TextWrap

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
    "can_save": false
  },
  "deprecated": true,
  "thread_safety": "ReadSafe",
  "category": "Text",
  "capabilities": [
    "UI"
  ]
}
```

> **Deprecated:** This property is simply an alias for [TextWrapped](/docs/reference/engine/classes/TextLabel.md). Use the past-tense version instead.

This property determines whether or not text should wrap at the edges of
the [TextLabel](/docs/reference/engine/classes/TextLabel.md) element's space.

### Property: TextLabel.Font *(hidden)*

```json
{
  "type": "Enum.Font",
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
  "category": "Text",
  "capabilities": [
    "UI"
  ]
}
```

This property selects one of several pre-defined fonts with which the
[TextLabel](/docs/reference/engine/classes/TextLabel.md) will render its text. Some fonts have bold, italic
and/or light variants.

With the exception of the [Font.Legacy](/docs/reference/engine/enums/Font.md) font, each font will render
text with the line height equal to the [TextSize](/docs/reference/engine/classes/TextLabel.md)
property.

The [Font.Code](/docs/reference/engine/enums/Font.md) font is the only monospace font. It has the unique
property that each character has the exact same width and height ratio of
1:2, where the width of each character is approximately half the
[TextSize](/docs/reference/engine/classes/TextLabel.md) property.

This property is kept in sync with the [FontFace](/docs/reference/engine/classes/TextLabel.md)
property.

**Show All Fonts**

This code sample renders a list of all the available fonts.

```lua
local frame = script.Parent

-- Create a TextLabel displaying each font
for _, font in pairs(Enum.Font:GetEnumItems()) do
	local textLabel = Instance.new("TextLabel")
	textLabel.Name = font.Name
	-- Set the text properties
	textLabel.Text = font.Name
	textLabel.Font = font
	-- Some rendering properties
	textLabel.TextSize = 24
	textLabel.TextXAlignment = Enum.TextXAlignment.Left
	-- Size the frame equal to the height of the text
	textLabel.Size = UDim2.new(1, 0, 0, textLabel.TextSize)
	-- Add to the parent frame
	textLabel.Parent = frame
end

-- Layout the frames in a list (if they aren't already)
if not frame:FindFirstChildOfClass("UIListLayout") then
	local uiListLayout = Instance.new("UIListLayout")
	uiListLayout.Parent = frame
end
```

**Cycle Font**

This code sample sets a parent TextLabel's Font and Text properties to all the
different fonts available.

```lua
local textLabel = script.Parent

while true do
	-- Iterate over all the different fonts
	for _, font in pairs(Enum.Font:GetEnumItems()) do
		textLabel.Font = font
		textLabel.Text = font.Name
		task.wait(1)
	end
end
```

### Property: TextLabel.LocalizedText *(hidden)*

```json
{
  "type": "string",
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
  "category": "Data",
  "capabilities": [
    "UI"
  ]
}
```

This read-only property holds the automatically-localized text that the
[TextLabel](/docs/reference/engine/classes/TextLabel.md) renders. When automatic localization is enabled through
[AutoLocalize](/docs/reference/engine/classes/GuiBase2d.md) and the label's
[Text](/docs/reference/engine/classes/TextLabel.md) matches an entry in an applicable localization
table for the player's locale, this property contains the translated
string that is actually displayed; when no translation applies, it falls
back to the label's own text. It defaults to an empty string and can't be
set from a script.

### Property: TextLabel.TextColor *(hidden)*

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
  "category": "Text",
  "capabilities": [
    "UI"
  ]
}
```

> **Deprecated:** This item has been superseded by [TextLabel.TextColor3](/docs/reference/engine/classes/TextLabel.md) which should be used in all new work.

This property determines the color of text.

## Inherited Members

### From [GuiObject](/docs/reference/engine/classes/GuiObject.md)

- **Property `Active`** (`boolean`): Determines whether this UI element sinks input.
- **Property `AnchorPoint`** (`Vector2`): Determines the origin point of a GuiObject, relative to its
- **Property `AutomaticSize`** (`AutomaticSize`): Determines whether resizing occurs based on child content.
- **Property `BackgroundColor`** (`BrickColor`): Determines the color of the GuiObject background. *(deprecated, hidden)*
- **Property `BackgroundColor3`** (`Color3`): Determines the GuiObject background color.
- **Property `BackgroundTransparency`** (`float`): Determines the transparency of the GuiObject background and
- **Property `BorderColor`** (`BrickColor`): Determines the color of the GuiObject border. *(deprecated, hidden)*
- **Property `BorderColor3`** (`Color3`): Determines the color of the GuiObject border.
- **Property `BorderMode`** (`BorderMode`): Determines in what manner the GuiObject border is laid out
- **Property `BorderSizePixel`** (`int`): Determines the pixel width of the GuiObject border.
- **Property `ClipsDescendants`** (`boolean`): Determines if descendant GuiObjects outside of the
- **Property `Draggable`** (`boolean`): Determines whether a GuiObject (and its descendants) can be *(deprecated)*
- **Property `GuiState`** (`GuiState`): Determines whether the player's mouse is being actively pressed on the
- **Property `InputSink`** (`InputSink`): Controls whether, and how, the GuiObject sinks input that occurs
- **Property `Interactable`** (`boolean`): Determines whether the GuiButton can be interacted with or not, or
- **Property `LayoutOrder`** (`int`): Controls the sort order of the GuiObject when used with a
- **Property `NextSelectionDown`** (`GuiObject`): Sets the GuiObject which will be selected when the gamepad
- **Property `NextSelectionLeft`** (`GuiObject`): Sets the GuiObject which will be selected when the gamepad
- **Property `NextSelectionRight`** (`GuiObject`): Sets the GuiObject which will be selected when the gamepad
- **Property `NextSelectionUp`** (`GuiObject`): Sets the GuiObject which will be selected when the gamepad
- **Property `Position`** (`UDim2`): Determines the pixel and scalar position of the GuiObject.
- **Property `Rotation`** (`float`): Determines the number of degrees by which the GuiObject is
- **Property `Selectable`** (`boolean`): Determine whether the GuiObject can be selected by a gamepad.
- **Property `SelectionImageObject`** (`GuiObject`): Overrides the default selection adornment used for gamepads.
- **Property `SelectionOrder`** (`int`): The order of GuiObjects selected by the gamepad UI
- **Property `Size`** (`UDim2`): Determines the pixel and scalar size of the GuiObject.
- **Property `SizeConstraint`** (`SizeConstraint`): Sets the Size axes that the GuiObject will
- **Property `Transparency`** (`float`): A mixed property of *(deprecated, hidden)*
- **Property `Visible`** (`boolean`): Determines whether the GuiObject and its descendants will be
- **Property `ZIndex`** (`int`): Determines the order in which a GuiObject renders relative to
- **Method `TweenPosition(endPosition: UDim2, easingDirection?: EasingDirection, easingStyle?: EasingStyle, time?: float, override?: boolean, callback?: Function): boolean`**: Smoothly moves a GUI to a new UDim2. *(deprecated)*
- **Method `TweenSize(endSize: UDim2, easingDirection?: EasingDirection, easingStyle?: EasingStyle, time?: float, override?: boolean, callback?: Function): boolean`**: Smoothly resizes a GuiObject to a new UDim2. *(deprecated)*
- **Method `TweenSizeAndPosition(endSize: UDim2, endPosition: UDim2, easingDirection?: EasingDirection, easingStyle?: EasingStyle, time?: float, override?: boolean, callback?: Function): boolean`**: Smoothly moves a GUI to a new size and position. *(deprecated)*
- **Event `DragBegin`**: Fired when a player begins dragging the object. *(deprecated)*
- **Event `DragStopped`**: Fired when a player stops dragging the object. *(deprecated)*
- **Event `InputBegan`**: Fired when a user begins interacting via a Human-Computer Interface device
- **Event `InputChanged`**: Fired when a user changes how they're interacting via a Human-Computer
- **Event `InputEnded`**: Fired when a user stops interacting via a Human-Computer Interface device
- **Event `MouseEnter`**: Fires when a user moves their mouse into a GUI element.
- **Event `MouseLeave`**: Fires when a user moves their mouse out of a GUI element.
- **Event `MouseMoved`**: Fires whenever a user moves their mouse while it is inside a GUI element.
- **Event `MouseWheelBackward`**: Fires when a user scrolls their mouse wheel back when the mouse is over a
- **Event `MouseWheelForward`**: Fires when a user scrolls their mouse wheel forward when the mouse is over
- **Event `SelectionGained`**: Fired when the GuiObject is being focused on with the Gamepad selector.
- **Event `SelectionLost`**: Fired when the Gamepad selector stops focusing on the GuiObject.
- **Event `TouchLongPress`**: Fires when the player starts, continues and stops long-pressing the UI
- **Event `TouchPan`**: Fires when the player moves their finger on the UI element.
- **Event `TouchPinch`**: Fires when the player performs a pinch or pull gesture using two fingers
- **Event `TouchRotate`**: Fires when the player performs a rotation gesture using two fingers on the
- **Event `TouchSwipe`**: Fires when the player performs a swipe gesture on the UI element.
- **Event `TouchTap`**: Fires when the player performs a tap gesture on the UI element.

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