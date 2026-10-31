---
title: "Text & image buttons"
url: /docs/en-us/ui/buttons
last_updated: 2026-10-30T19:56:02Z
description: "Buttons allow players to prompt an action."
---

# Text & image buttons

`Class.GuiButton|GuiButtons` are `Class.GuiObject|GuiObjects` that allow players to perform an action. You can customize these buttons to provide context and feedback, such as changing the visual appearance or [scripting](#script-buttons) audible feedback when a player interacts with a button.

There are two types of buttons which you can place [on‑screen](/docs/en-us/ui/on-screen-containers.md) or [in‑game](/docs/en-us/ui/in-experience-containers.md):

- A `Class.TextButton` is a rectangle with text that triggers the `Class.GuiButton.Activated|Activated` and/or `Class.GuiButton.SecondaryActivated|SecondaryActivated` event on click/tap.
- An `Class.ImageButton` is a rectangle with an image that triggers the `Class.GuiButton.Activated|Activated` and/or `Class.GuiButton.SecondaryActivated|SecondaryActivated` event on click/tap. It features additional states for swapping the image on player hover or press.

## Buttons on the screen

Buttons [on the screen](/docs/en-us/ui/on-screen-containers.md) are useful to quickly guide players to various menus or pages. To add this type of button:

1. In the [Explorer](/docs/en-us/studio/explorer.md) window, hover over `Class.StarterGui`, click the ⊕ button, and insert a `Class.ScreenGui`.
2. Hover over the new `Class.ScreenGui`, click the ⊕ button, and insert either a `Class.TextButton` or `Class.ImageButton`.

## Buttons on part faces

Buttons on a part are useful for allowing players to interact with parts. For example, you can let players step on a button to complete an action.

To add a button to the face of a part:

1. In the [Explorer](/docs/en-us/studio/explorer.md) window, hover over the **part**, click the ⊕ button, and insert a `Class.SurfaceGui`.
2. Hover over the new `Class.SurfaceGui`, click the ⊕ button, and insert either a `Class.TextButton` or `Class.ImageButton`.
  > **Warning:** If you don't see the button, try choosing a different face (`Enum.NormalId.Top|Top`, `Enum.NormalId.Bottom|Bottom`, `Enum.NormalId.Front|Front`, `Enum.NormalId.Back|Back`, `Enum.NormalId.Left|Left`, or `Enum.NormalId.Right|Right`) for the `Class.SurfaceGui.Face|Face` property of the `Class.SurfaceGui`.

## Button appearance

Both `Class.TextButton` and `Class.ImageButton` inherit from `Class.GuiObject` which contains properties like `Class.GuiObject.BackgroundColor3|BackgroundColor3`, `Class.GuiObject.Rotation|Rotation`, and `Class.GuiObject.Size|Size`. Buttons also accept the [appearance modifiers](/docs/en-us/ui/appearance-modifiers.md) common to most UI objects.

Unique to `Class.TextButton` are various properties to change its visual appearance:

- `Class.TextButton.FontFace|FontFace` — The font used to render text.
- `Class.TextButton.Text|Text` — The text string rendered on the button.
- `Class.TextButton.TextSize|TextSize` — The line height of text in offsets.
- `Class.TextButton.TextColor3|TextColor3` — Color of the rendered text.

An `Class.ImageButton` has several properties to change its visual appearance, including hover and pressed image variants to indicate a player's interaction with the button:

- `Class.ImageButton.Image|Image` — The image that displays when a player is not interacting with the `Class.ImageButton`.
- `Class.ImageButton.HoverImage|HoverImage` — The image that displays when a player is hovering their cursor over the `Class.ImageButton`.
- `Class.ImageButton.PressedImage|PressedImage` — The image that displays when a player clicks/taps the `Class.ImageButton`.

_Normal_

_Hover_

_Pressed_

## Script buttons

You can script an action when a player presses a button by connecting the button to the `Class.GuiButton.Activated` event, or to `Class.GuiButton.SecondaryActivated` for cross‑platform secondary input like right‑click on desktop and long press on mobile. For example, when you parent the following `Class.LocalScript` to a button, the button changes to a random color every time a player clicks/taps it.

```lua
local button = script.Parent
local RNG = Random.new()

local function onButtonActivated()
	-- Randomize the button color
	button.BackgroundColor3 = Color3.fromHSV(RNG:NextNumber(), 1, 1)
end

button.Activated:Connect(onButtonActivated)
```
