---
name: UserInputType
last_updated: 2026-10-30T19:55:54Z
type: enum
summary: "Describes the type of a user input event."
---

# UserInputType

Describes the type of a user input event.

**Type:** enum

## Description

The **UserInputType** enum describes the kind of input being performed (mouse,
keyboard, gamepad, touch, etc). This enum is used by the
[InputObject.UserInputType](/docs/reference/engine/classes/InputObject.md) property of the same name, as well as
various [UserInputService](/docs/reference/engine/classes/UserInputService.md) and [GuiObject](/docs/reference/engine/classes/GuiObject.md) events.

## Items

| Name | Value | Description |
|------|-------|-------------|
| `MouseButton1` | 0 | The left mouse button. |
| `MouseButton2` | 1 | The right mouse button. |
| `MouseButton3` | 2 | The middle mouse button. |
| `MouseWheel` | 3 | The mouse wheel. |
| `MouseMovement` | 4 | Movement of the mouse. Fires changed events each time the player's cursor position changes and when the move enters/leaves the game window. |
| `Touch` | 7 | A tap on the screen from a mobile device. |
| `Keyboard` | 8 | Key press on a keyboard. |
| `Focus` | 9 | The client regaining focus of the Roblox window. |
| `Accelerometer` | 10 | The accelerometer of a mobile device. |
| `Gyro` | 11 | The Gyroscope of a mobile device. |
| `Gamepad1` | 12 | Input from the 1st plugged in Gamepad. |
| `Gamepad2` | 13 | Input from the 2nd plugged in Gamepad. |
| `Gamepad3` | 14 | Input from the 3rd plugged in Gamepad. |
| `Gamepad4` | 15 | Input from the 4th plugged in Gamepad. |
| `Gamepad5` | 16 | Input from the 5th plugged in Gamepad. |
| `Gamepad6` | 17 | Input from the 6th plugged in Gamepad. |
| `Gamepad7` | 18 | Input from the 7th plugged in Gamepad. |
| `Gamepad8` | 19 | Input from the 8th plugged in Gamepad. |
| `TextInput` | 20 | Input of Text into a text-based [GuiObject](/docs/reference/engine/classes/GuiObject.md). Normally this is only a [TextBox](/docs/reference/engine/classes/TextBox.md). |
| `InputMethod` | 21 | Text input from an input method editor (IME). [InputObjects](/docs/reference/engine/classes/InputObject.md) with this type aren't currently fired. |
| `None` | 22 | Unknown UserInputType. |