---
name: TextBox
last_updated: 2026-10-30T19:55:53Z
inherits:
  - GuiObject
  - GuiBase2d
  - GuiBase
  - Instance
  - Object
type: class
memory_category: Gui
summary: "A 2D user interface element that displays player-editable text."
---

# Class: TextBox

> A 2D user interface element that displays player-editable text.

## Description

A `TextBox` allows the player to provide text input. It behaves similarly to a
[TextButton](/docs/reference/engine/classes/TextButton.md), except that a single `TextBox` can be put in focus by
clicking, tapping, or gamepad selection. While in focus, the player can use a
keyboard to change the [Text](/docs/reference/engine/classes/TextBox.md) property.

- If there is no text, the [PlaceholderText](/docs/reference/engine/classes/TextBox.md)
  will be visible. This is useful prompting players of the kind or format of
  data they should input.
- By default, the [ClearTextOnFocus](/docs/reference/engine/classes/TextBox.md) property
  is enabled and ensures there is no existing text when a `TextBox` is
  focused. This may not be desirable for text that should be editable by the
  player.
- The [MultiLine](/docs/reference/engine/classes/TextBox.md) property allows players to enter
  multiple lines of text with newline characters (`\n`).

#### Focus State

It is possible to detect and change the focus state of a `TextBox`:

- You can use [CaptureFocus](/docs/reference/engine/classes/TextBox.md) when a dialogue
  appears so that the player doesn't have to click on a `TextBox` when it
  becomes available; you can use [ContextActionService:BindAction()](/docs/reference/engine/classes/ContextActionService.md) to
  bind a certain key to focus a `TextBox` using this function. When a
  `TextBox` comes into focus, the [Focused](/docs/reference/engine/classes/TextBox.md) event fires.
- You can detect if a certain `TextBox` is in focus by using
  [IsFocused](/docs/reference/engine/classes/TextBox.md). Alternatively,
  [UserInputService:GetFocusedTextBox()](/docs/reference/engine/classes/UserInputService.md) can be used to check if any
  `TextBox` is in focus.
- When the player is done inputting text, the
  [FocusLost](/docs/reference/engine/classes/TextBox.md) event fires, indicating if the player
  pressed <kbd>Enter</kbd> to submit text along with the [InputObject](/docs/reference/engine/classes/InputObject.md)
  that caused the loss of focus. When using on-screen keyboards on mobile and
  console,
  [ReturnPressedFromOnScreenKeyboard](/docs/reference/engine/classes/TextBox.md)
  may also fire.
- If some more important matter comes up during gameplay, you can
  [ReleaseFocus](/docs/reference/engine/classes/TextBox.md) of the `TextBox` so that a
  player's keyboard input returns to your game.

#### Text Editing

A `TextBox` supports text selection through its
[CursorPosition](/docs/reference/engine/classes/TextBox.md) and
[SelectionStart](/docs/reference/engine/classes/TextBox.md) properties. Using
[GetPropertyChangedSignal](/docs/reference/engine/classes/Object.md), you can
detect when a selection changes. Additionally, it is possible for players to
copy and paste text within a TextBox, enabling basic clipboard support. When
the cursor moves outside the visible area while typing or navigating, the
`TextBox` automatically scrolls its viewport to keep the cursor in view.

**Text Filtering Notice** Games that facilitate player-to-player communication
using text, such as custom chat or nametags, must properly filter such text
using [TextService:FilterStringAsync()](/docs/reference/engine/classes/TextService.md) or
[Chat:FilterStringAsync()](/docs/reference/engine/classes/Chat.md). If this is not properly done, your game may
receive moderation action.

## Code Samples

**TextBox Secret Word**

This code sample creates a password-like interface for a TextBox, giving
visual feedback on the player's input.

```lua
-- Place this code in a LocalScript inside a TextBox
local textBox = script.Parent

local secretWord = "roblox"
local colorNormal = Color3.new(1, 1, 1) -- white
local colorWrong = Color3.new(1, 0, 0) -- red
local colorCorrect = Color3.new(0, 1, 0) -- green

-- Initialize the state of the textBox
textBox.ClearTextOnFocus = true
textBox.Text = ""
textBox.Font = Enum.Font.Code
textBox.PlaceholderText = "What is the secret word?"
textBox.BackgroundColor3 = colorNormal

local function onFocused()
	textBox.BackgroundColor3 = colorNormal
end

local function onFocusLost(enterPressed, _inputObject)
	if enterPressed then
		local guess = textBox.Text
		if guess == secretWord then
			textBox.Text = "ACCESS GRANTED"
			textBox.BackgroundColor3 = colorCorrect
		else
			textBox.Text = "ACCESS DENIED"
			textBox.BackgroundColor3 = colorWrong
		end
	else
		-- The player stopped editing without pressing Enter
		textBox.Text = ""
		textBox.BackgroundColor3 = colorNormal
	end
end

textBox.FocusLost:Connect(onFocusLost)
textBox.Focused:Connect(onFocused)
```

## Properties

### Property: TextBox.ClearTextOnFocus

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

Determines whether clicking on the `TextBox` will clear its
[TextBox.Text](/docs/reference/engine/classes/TextBox.md) property

### Property: TextBox.ContentText

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

This property provides a copy of [Text](/docs/reference/engine/classes/TextBox.md) that contains
exactly what is being rendered by the [TextBox](/docs/reference/engine/classes/TextBox.md). This is useful for
eliminating style tags used for [rich text](/docs/en-us/ui/rich-text.md)
markup; for example, when [RichText](/docs/reference/engine/classes/TextBox.md) is enabled,
the [ContentText](/docs/reference/engine/classes/TextBox.md) property shows the text as it
appears to the user.

| RichText | Text | ContentText |
| --- | --- | --- |
| `false` | <b>Hello,
 world!</b> | <b>Hello,
 world!</b> |
| `true` | <b>Hello,
 world!</b> | Hello,
 world! |

### Property: TextBox.CursorPosition

```json
{
  "type": "int",
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

This property determines the offset of the text cursor in bytes, or `-1`
if the `TextBox` is not currently being edited. A value of `1` represents
the position before the first byte in the [Text](/docs/reference/engine/classes/TextBox.md)
property. When used in conjunction with the
[SelectionStart](/docs/reference/engine/classes/TextBox.md) property, it is possible to
both get and set selected text within a `TextBox`.

Note that the units of this property are **bytes** and that many unicode
characters such as emoji are longer than 1 byte. For instance, if a player
types in "Hello👋" ("Hello" immediately followed by the waving hand sign),
the cursor position would be `10`, not `7`, since the emoji uses 4 bytes.

**TextBox Selections**

This code sample demonstrates reading the current selection of a `TextBox`
using [CursorPosition](/docs/reference/engine/classes/TextBox.md) and
[SelectionStart](/docs/reference/engine/classes/TextBox.md).

```lua
local textBox = script.Parent

local function showSelection()
	if textBox.CursorPosition == -1 or textBox.SelectionStart == -1 then
		print("No selection")
	else
		local selectedText = string.sub(
			textBox.Text,
			math.min(textBox.CursorPosition, textBox.SelectionStart),
			math.max(textBox.CursorPosition, textBox.SelectionStart)
		)
		print('The selection is:"', selectedText, '"')
	end
end

textBox:GetPropertyChangedSignal("CursorPosition"):Connect(showSelection)
textBox:GetPropertyChangedSignal("SelectionStart"):Connect(showSelection)
```

### Property: TextBox.FontFace

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

This property is similar to the [Font](/docs/reference/engine/classes/TextBox.md) property but
allows setting fonts that don't exist in [Font](/docs/reference/engine/enums/Font.md).

This property is kept in sync with the [TextBox.Font](/docs/reference/engine/classes/TextBox.md) property. When
setting `FontFace`, the [Font](/docs/reference/engine/classes/TextBox.md) property is set to the
corresponding enum value, or to [Font.Unknown](/docs/reference/engine/enums/Font.md) if there are no
matches.

### Property: TextBox.LineHeight

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

Controls the height of lines, as a multiple of the font's em square size,
by scaling the spacing between lines of text in the `TextBox`. Valid
values range from `1.0` (default) to `3.0`.

### Property: TextBox.MaxVisibleGraphemes

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
that are shown on the `TextBox`, regardless of whether it's showing the
[PlaceholderText](/docs/reference/engine/classes/TextBox.md) or
[Text](/docs/reference/engine/classes/TextBox.md).

Changing the property does not change the position or size of the visible
graphemes; the layout will be calculated as if all graphemes are visible.

Setting the property to `-1` disables the limit and shows the entirety of
the [Text](/docs/reference/engine/classes/TextBox.md).

### Property: TextBox.MultiLine

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

When set to `true`, text inside a `TextBox` is able to move onto multiple
lines. This also enables players to use the <kbd>Enter</kbd> key to move
onto a new line.

### Property: TextBox.OpenTypeFeatures

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

Comma-separated list of OpenType feature tags applied when the
[TextBox](/docs/reference/engine/classes/TextBox.md) shapes and renders its text, such as `zero` for slashed
zeros or `ss03` for a stylistic set. Defaults to an empty string (no
additional features).

Each entry uses standard OpenType feature-string syntax (for example,
`zero` or `ss03`). Only a supported subset is applied; an unsupported
feature, malformed string, or bracketed partial-enabling syntax (for
example, `zero[1:3]`) is rejected, with the reason in
[OpenTypeFeaturesError](/docs/reference/engine/classes/TextBox.md).

Supports [styling](/docs/en-us/ui/styling.md).

### Property: TextBox.OpenTypeFeaturesError

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

Read-only error, if any, from parsing and applying
[OpenTypeFeatures](/docs/reference/engine/classes/TextBox.md). Defaults to an empty
string when the requested features applied successfully.

An error is produced when:

- The feature string is malformed and cannot be parsed.
- A requested feature is not in the supported set.
- A bracketed range syntax is used (partial feature enabling is not
  supported).

### Property: TextBox.PlaceholderColor3

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

Sets the text color that gets used when no text has been entered into the
`TextBox`.

### Property: TextBox.PlaceholderText

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

Sets the text that gets displayed when no text has been entered into the
`TextBox`.

### Property: TextBox.RichText

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

This property determines whether the `TextBox` renders the
[Text](/docs/reference/engine/classes/TextBox.md) string using
[rich text](/docs/en-us/ui/rich-text.md) formatting. Rich text uses simple
markup tags to style sections of the string in bold, italics, specific
colors, and more.

Note that when the `TextBox` has this property enabled and the box gains
focus, the player will be able to edit and interact with the complete XML
string, including all of the formatting tags. When focus is lost, the text
will automatically parse and render the tags as rich text.

### Property: TextBox.SelectionStart

```json
{
  "type": "int",
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

Determines the starting position of a text selection, or `-1` if the
`TextBox` has no range of selected text. This property uses the same
positioning logic as [CursorPosition](/docs/reference/engine/classes/TextBox.md).
`SelectionStart` will be greater than
[CursorPosition](/docs/reference/engine/classes/TextBox.md) if the cursor is at the
beginning of a selection, and less than
[CursorPosition](/docs/reference/engine/classes/TextBox.md) if the cursor is at the end.

**TextBox Selections**

This code sample demonstrates reading the current selection of a `TextBox`
using [CursorPosition](/docs/reference/engine/classes/TextBox.md) and
[SelectionStart](/docs/reference/engine/classes/TextBox.md).

```lua
local textBox = script.Parent

local function showSelection()
	if textBox.CursorPosition == -1 or textBox.SelectionStart == -1 then
		print("No selection")
	else
		local selectedText = string.sub(
			textBox.Text,
			math.min(textBox.CursorPosition, textBox.SelectionStart),
			math.max(textBox.CursorPosition, textBox.SelectionStart)
		)
		print('The selection is:"', selectedText, '"')
	end
end

textBox:GetPropertyChangedSignal("CursorPosition"):Connect(showSelection)
textBox:GetPropertyChangedSignal("SelectionStart"):Connect(showSelection)
```

### Property: TextBox.ShowNativeInput

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

If set to `true`, input native to the platform is used instead of Roblox's
built-in keyboard.

### Property: TextBox.Text

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

This property determines the text content rendered by the `TextBox`
element. The visual properties of the string rendered to the screen is
determined by [TextColor3](/docs/reference/engine/classes/TextBox.md),
[TextTransparency](/docs/reference/engine/classes/TextBox.md),
[TextSize](/docs/reference/engine/classes/TextBox.md), [FontFace](/docs/reference/engine/classes/TextBox.md), and
other properties.

It is possible to render emoji such as 👋 and other symbols. These special
symbols aren't affected by the [TextColor3](/docs/reference/engine/classes/TextBox.md)
property.

This property may contain newline characters, but it is not possible to
type newline characters within the **Properties** window. Similarly, this
property may contain a tab character, but it will render as a space
instead.

### Property: TextBox.TextBounds

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
offsets. In other words, if you were to try to fit text into a rectangle,
this property would reflect the minimum dimensions of the rectangle you
would need in order to fit the text.

Using [TextService:GetTextSize()](/docs/reference/engine/classes/TextService.md), you can predict what `TextBounds`
will be on a `TextLabel` given a string, [Font](/docs/reference/engine/classes/TextBox.md),
[TextSize](/docs/reference/engine/classes/TextBox.md) and frame size.

### Property: TextBox.TextColor3

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

This property determines the color of non-placeholder text rendered by the
`TextBox`. Text is rendered after the text stroke.

**Vowel Detector**

This code sample, when placed within a TextBox, will turn the text color red
if the typed string contains no vowels (A, E, I, O or U).

```lua
local textBox = script.Parent

local function hasVowels(str)
	return str:lower():find("[aeiou]")
end

local function onTextChanged()
	local text = textBox.Text
	-- Check for vowels
	if hasVowels(text) then
		textBox.TextColor3 = Color3.new(0, 0, 0) -- Black
	else
		textBox.TextColor3 = Color3.new(1, 0, 0) -- Red
	end
end

textBox:GetPropertyChangedSignal("Text"):Connect(onTextChanged)
```

### Property: TextBox.TextDirection

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

[TextDirection](/docs/reference/engine/enums/TextDirection.md) in which the [TextBox](/docs/reference/engine/classes/TextBox.md) renders its text.
Defaults to [TextDirection.Auto](/docs/reference/engine/enums/TextDirection.md), which picks direction from the text
content so right-to-left scripts render right-to-left.
[TextDirection.LeftToRight](/docs/reference/engine/enums/TextDirection.md) and [TextDirection.RightToLeft](/docs/reference/engine/enums/TextDirection.md)
force left-to-right or right-to-left rendering.

Supports [styling](/docs/en-us/ui/styling.md).

### Property: TextBox.TextEditable

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

This property determines whether the player can change the
[Text](/docs/reference/engine/classes/TextBox.md) through input. It is recommended to disable
[ClearTextOnFocus](/docs/reference/engine/classes/TextBox.md) when this property is
disabled, otherwise the text can be cleared on-focus.

### Property: TextBox.TextFits

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

Whether the text fits within the constraints of the `TextBox`.

### Property: TextBox.TextScaled

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

This property determines whether text is scaled so that it fills the box's
entire space. When enabled, [TextSize](/docs/reference/engine/classes/TextBox.md) is ignored
and [TextWrapped](/docs/reference/engine/classes/TextBox.md) is automatically enabled. When
this property is used for on-screen UI, it may be helpful to use a
[UITextSizeConstraint](/docs/reference/engine/classes/UITextSizeConstraint.md) to restrict the range of possible text sizes.

See [TextLabel.TextScaled](/docs/reference/engine/classes/TextLabel.md) for additional recommendations when using
this property.

### Property: TextBox.TextSize

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

This property determines the height in offsets of one line of rendered
text. The unit is in offsets, not points as in many document editing
programs.

### Property: TextBox.TextStrokeColor3

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

This property sets the color of the stroke (outline) of the rendered text.
This property and
[TextStrokeTransparency](/docs/reference/engine/classes/TextBox.md) determine
the visual appearance of the text stroke.

### Property: TextBox.TextStrokeTransparency

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

This property sets the transparency of the stroke (outline) of the
rendered text. This property and
[TextStrokeColor3](/docs/reference/engine/classes/TextBox.md) determine the visual
appearance of the text stroke.

Since text stroke is simply multiple renderings of the same transparency,
this property is essentially multiplicative on itself four times over; for
example a `TextStrokeTransparency` of `0.5` appears about the same as
[TextTransparency](/docs/reference/engine/classes/TextBox.md) of `0.0625`, or `0.5^4`.

### Property: TextBox.TextTransparency

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
`TextBox`.

### Property: TextBox.TextTruncate

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

Controls the truncation of the text displayed in the `TextBox`.

### Property: TextBox.TextWrapped

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
`TextBox` element's space so that [TextBounds](/docs/reference/engine/classes/TextBox.md)
will never exceed the [GuiBase2d.AbsoluteSize](/docs/reference/engine/classes/GuiBase2d.md) of the element.

This is achieved by breaking long lines of text into multiple lines. Line
breaks will prefer whitespace; should a long unbroken word exceed the
width of the element, that word will be broken into multiple lines.

If further line breaks would cause the vertical height of the text (the
**Y** component of [TextBox.TextBounds](/docs/reference/engine/classes/TextBox.md)) to exceed the vertical
height of the element (the **Y** component of
[GuiBase2d.AbsoluteSize](/docs/reference/engine/classes/GuiBase2d.md)), then that line will not be rendered at
all.

### Property: TextBox.TextXAlignment

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
the `TextBox` element's space. It can be used in conjunction with
[TextYAlignment](/docs/reference/engine/classes/TextBox.md) to fully determine text
alignment on both axes.

This property does not affect the read-only properties
[TextBounds](/docs/reference/engine/classes/TextBox.md) and
[TextFits](/docs/reference/engine/classes/TextBox.md).

### Property: TextBox.TextYAlignment

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
the `TextBox` element's space. It can be used in conjunction with
[TextXAlignment](/docs/reference/engine/classes/TextBox.md) to fully determine text
alignment on both axes.

This property does not affect the read-only properties
[TextBounds](/docs/reference/engine/classes/TextBox.md) and
[TextFits](/docs/reference/engine/classes/TextBox.md).

### Property: TextBox.FontSize

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

> **Deprecated:** This item has been superseded by [TextBox.TextSize](/docs/reference/engine/classes/TextBox.md) which should be used in all new work.

This property determines the font size of a `TextBox` object.

### Property: TextBox.TextWrap

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

> **Deprecated:** This item has been superseded by [TextBox.TextWrapped](/docs/reference/engine/classes/TextBox.md) which should be used in all new work.

### Property: TextBox.Font *(hidden)*

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

This property selects one of several pre-defined [Font](/docs/reference/engine/enums/Font.md) fonts with
which the UI element will render its text. Some fonts have bold, italic,
and/or light variants.

This property is kept in sync with the [TextBox.FontFace](/docs/reference/engine/classes/TextBox.md) property.
When setting `Font`, the [FontFace](/docs/reference/engine/classes/TextBox.md) property will
be set to [Font.fromEnum(value)](/docs/reference/engine/datatypes/Font.md).

### Property: TextBox.TextColor *(hidden)*

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

> **Deprecated:** This item has been superseded by [TextBox.TextColor3](/docs/reference/engine/classes/TextBox.md) which should be used in all new work.

## Methods

### Method: TextBox:CaptureFocus

**Signature:** `TextBox:CaptureFocus(): ()`

Forces the client to focus on the `TextBox`.

*Security: None · Thread Safety: Unsafe · Capabilities: UI*

**Returns:** `()`

**Capture TextBox Focus**

This code sample causes the client to focus on the parent [TextBox](/docs/reference/engine/classes/TextBox.md) when
the player presses the <kbd>Q</kbd> key.

```lua
local UserInputService = game:GetService("UserInputService")

local textBox = script.Parent

local input = UserInputService.InputBegan:Connect(function(input, processed)
	if input.KeyCode == Enum.KeyCode.Q then
		textBox:CaptureFocus()
	end
end)
```

### Method: TextBox:IsFocused

**Signature:** `TextBox:IsFocused(): boolean`

Returns `true` if the `TextBox` is focused or `false` if it is not.

*Security: None · Thread Safety: Unsafe · Capabilities: UI*

**Returns:** `boolean` — Returns `true` if the `TextBox` is focused or `false` if it is not.

### Method: TextBox:ReleaseFocus

**Signature:** `TextBox:ReleaseFocus(submitted?: boolean): ()`

Forces the client to unfocus the `TextBox`. The `submitted` parameter lets
you override the `enterPressed` parameter in the [TextBox.FocusLost](/docs/reference/engine/classes/TextBox.md)
event.

*Security: None · Thread Safety: Unsafe · Capabilities: UI*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `submitted` | `boolean` | `false` | Whether the [TextBox.FocusLost](/docs/reference/engine/classes/TextBox.md) event's `enterPressed` parameter reports `true`, as if the player pressed Enter to submit text. Defaults to `false`. |

**Returns:** `()`

**Release TextBox Focus**

This code sample causes the client to release focus on the parent
[TextBox](/docs/reference/engine/classes/TextBox.md) (if focused) when the player presses the <kbd>Escape</kbd>
key.

```lua
local UserInputService = game:GetService("UserInputService")

local textBox = script.Parent

local input = UserInputService.InputBegan:Connect(function(input, processed)
	if input.KeyCode == Enum.KeyCode.Escape and textBox.IsFocused then
		textBox:ReleaseFocus()
	end
end)
```

## Events

### Event: TextBox.Focused

**Signature:** `TextBox.Focused()`

This event fires when the `TextBox` gains focus, typically when a player
clicks/taps on the `TextBox` to begin text entry. Also fires if `TextBox`
focus is forced through [CaptureFocus()](/docs/reference/engine/classes/TextBox.md).

This event can be used alongside [FocusLost](/docs/reference/engine/classes/TextBox.md) to
track when a `TextBox` both gains and loses focus.

*Security: None · Capabilities: UI*

**TextBox Focus**

This example shows how to connect the [TextBox.Focused](/docs/reference/engine/classes/TextBox.md) and
[TextBox.FocusLost](/docs/reference/engine/classes/TextBox.md) events.

```lua
local textBox = script.Parent

textBox.Focused:Connect(function()
	print("Focused!")
end)

textBox.FocusLost:Connect(function()
	print("Focus lost!")
end)
```

### Event: TextBox.FocusLost

**Signature:** `TextBox.FocusLost(enterPressed: boolean, inputThatCausedFocusLoss: InputObject)`

This event fires when the `TextBox` loses its focus, typically when a
player clicks/taps outside of it or presses <kbd>Enter</kbd>. Also fires
if `TextBox` focus release is forced through
[ReleaseFocus()](/docs/reference/engine/classes/TextBox.md).

This event can be used alongside [FocusLost](/docs/reference/engine/classes/TextBox.md) to
track when a `TextBox` both gains and loses focus.

*Security: None · Capabilities: UI*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `enterPressed` | `boolean` | A boolean indicating whether the client pressed <kbd>Enter</kbd> to lose focus (`true`) or not (`false`). |
| `inputThatCausedFocusLoss` | `InputObject` | An [InputObject](/docs/reference/engine/classes/InputObject.md) instance indicating the type of input that caused the `TextBox` to lose focus. |

**TextBox Focus**

This example shows how to connect the [TextBox.Focused](/docs/reference/engine/classes/TextBox.md) and
[TextBox.FocusLost](/docs/reference/engine/classes/TextBox.md) events.

```lua
local textBox = script.Parent

textBox.Focused:Connect(function()
	print("Focused!")
end)

textBox.FocusLost:Connect(function()
	print("Focus lost!")
end)
```

**FocusLost**

This example works when placed in a [LocalScript](/docs/reference/engine/classes/LocalScript.md) that is the child of a
TextBox. When the TextBox loses focus, the example prints either:

1. "Player pressed Enter" - if the TextBox lost focus because the player
   pressed the Enter key. **_or_**
2. "Player pressed InputObject._KeyCode_" - where "_KeyCode_" is the
   [InputObject](/docs/reference/engine/classes/InputObject.md) KeyCode property of the input that caused the TextBox
   to lose focus. For example, pressing the Escape (esc) key to exit TextBox
   focus returns an InputObject instance with the KeyCode
   'InputObject.Escape'.

```lua
local textBox = script.Parent

local function onFocusLost(enterPressed, inputThatCausedFocusLost)
	if enterPressed then
		print("Player pressed Enter")
	else
		print("Player pressed", inputThatCausedFocusLost.KeyCode)
	end
end

textBox.FocusLost:Connect(onFocusLost)
```

**TextBox.FocusLost1**

The example shown below will print "Focus was lost because enter was pressed!"
whenever the TextBox loses focus as a result of the enter key being pressed.

```lua
local gui = script.Parent
local textBox = gui.TextBox

local function focusLost(enterPressed)
	if enterPressed then
		print("Focus was lost because enter was pressed!")
	else
		print("Focus was lost without enter being pressed")
	end
end

textBox.FocusLost:Connect(focusLost)
```

### Event: TextBox.ReturnPressedFromOnScreenKeyboard

**Signature:** `TextBox.ReturnPressedFromOnScreenKeyboard()`

On mobile and console, this event fires when the `TextBox` is focused and
the player presses the on-screen keyboard's return/enter button.

*Security: None · Capabilities: UI*

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