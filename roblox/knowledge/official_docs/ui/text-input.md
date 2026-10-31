---
title: "Text input fields"
url: /docs/en-us/ui/text-input
last_updated: 2026-10-30T19:56:02Z
description: "Text input fields allow users to input text from their physical or on-screen keyboard."
---

# Text input fields

A `Class.TextBox` is a rectangle that allows a user to provide text input while it's in focus. When you [script](#script-text-inputs) a `Class.TextBox`, you can use it as a search bar or an input field on a form. To help users know what type of text they should input, you can also provide a prompt through the `Class.TextBox.PlaceholderText|PlaceholderText` property.

Because these objects are `Class.GuiObject|GuiObjects`, you can customize properties such as `Class.GuiObject.BackgroundColor3|BackgroundColor3`, `Class.GuiObject.BorderMode|BorderMode`, `Class.GuiObject.Transparency|Transparency`, and `Class.GuiObject.Rotation|Rotation` to fit the aesthetics of your game.

## Create text inputs on the screen

A `Class.TextBox` on a screen is useful for things like an input field for a form.

To add a `Class.TextBox` to a screen:

1. In the **Explorer** window, select **StarterGui** and add a **ScreenGui**.
  1. Hover over StarterGui and click the ⊕ button. A contextual menu displays.
  2. Insert a **ScreenGui**.
2. Select the new **ScreenGui** and add a **TextBox**.
  1. Hover over **ScreenGui** and click the ⊕ button. A contextual menu displays.
  2. Insert a **TextBox**.

## Create text inputs on part faces

To add a `Class.TextBox` to the face of a part:

1. In the **Explorer** window, select **StarterGui** and add a **SurfaceGui**.
  1. Hover over StarterGui and click the ⊕ button. A contextual menu displays.
  2. Insert a **ScreenGui**.
2. Select the new **SurfaceGui** and add a **TextBox**.
  1. Hover over **SurfaceGui** and click the ⊕ button. A contextual menu displays.
  2. Insert a **TextBox**.
3. Adorn the **SurfaceGui** to the **part** on which you want to display the **TextBox**.
  1. In the **Properties** window, select the **Adornee** property. Your cursor changes.
  2. In the **Explorer** window, select the part.

> **Warning:** If you don't see the `Class.TextBox`, try [choosing a different face](/docs/en-us/parts/textures-decals.md#choose-a-face) in the **Face** property of the **SurfaceGui**.
## Script text inputs

Like [buttons](/docs/en-us/ui/buttons.md), you can script any action for a `Class.TextBox` object when a user interacts with it. For example, the following script connects the `Class.TextBox.FocusLost|FocusLost` event which fires when the user presses the `Enter` button or clicks outside the box. If `enterPressed` is `true`, meaning the user submitted the input instead of merely clicking outside the box, the script prints the contents of the entry to the [Output](/docs/en-us/studio/output.md) window.

```lua
local textBox = script.Parent

local function onFocusLost(enterPressed, inputObject)
	if enterPressed then
		print(textBox.Text)
	end
end

textBox.FocusLost:Connect(onFocusLost)
```

As another example, you might want to allow only numbers in a `Class.TextBox`. The following code uses the `Class.TextBox.GetPropertyChangedSignal` event to detect when the `Class.TextBox.Text` changes, such as when a user starts typing, then it uses the `Library.string.gsub()` function to disallow non‑numbers.

```lua
local textBox = script.Parent

local function allowOnlyNumbers()
	textBox.Text = string.gsub(textBox.Text, "%D", "")
end

textBox:GetPropertyChangedSignal("Text"):Connect(allowOnlyNumbers)
```

## Text filtering

Applied to various sources and inputs, [text filtering](/docs/en-us/ui/text-filtering.md) prevents users from seeing inappropriate language and personally identifiable information such as phone numbers. Roblox automatically filters common text outputs such as messages that have passed through [in-game text chat](/docs/en-us/chat/in-experience-text-chat.md), but **you are responsible for filtering any displayed text that you don't have explicit control over**, including characters/strings that users input through text inputs.

> **Error:** Because filtering is crucial for a safe environment, Roblox actively moderates the content of games to make sure they meet [community standards](https://en.help.roblox.com/hc/en-us/articles/203313410-Roblox-Community-Standards). If Roblox receives reports or automatically detects that your game doesn't apply text filtering, then the system removes the game until you add filtering.
