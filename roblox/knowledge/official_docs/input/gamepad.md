---
title: "Gamepad input"
url: /docs/en-us/input/gamepad
last_updated: 2026-10-30T19:55:43Z
description: "Explains how to accept input from USB gamepads, such as Xbox and PlayStation controllers."
---

# Gamepad input

Roblox accepts input from gamepads such as Xbox and PlayStation controllers. To simplify [cross‑platform](/docs/en-us/projects/cross-platform.md) inputs, including gamepads, Roblox provides the [Input Action System](/docs/en-us/input/input-action-system.md) to define **actions** such as "jump," "sprint," or "shoot" and set up **bindings** for multiple hardware inputs to drive those actions.

When binding gamepad inputs, see [common control schemas](#common-control-schemas) to create a consistent gamepad experience for players. After inputs are set, you can enhance the player's experience by including [haptic feedback](#haptic-feedback) on supported controllers.

As you build out support for gamepads, remember to test frequently using a connected gamepad or the [Controller Emulator](#controller-emulation) in Studio.

## Input type detection

In cross‑platform development, it's important that you determine and respond to the `Class.UserInputService.PreferredInput|PreferredInput` type a player is using, normally to ensure that [UI elements](/docs/en-us/ui.md#ui-objects) like on-screen buttons and menus work elegantly and support interaction across devices.

For example, a console assumes that gamepads are the default input, but a player on PC or laptop may also choose to connect a bluetooth gamepad. In this case, mouse/keyboard remains a valid input for that player, but you can assume they want to switch to the connected gamepad as the **primary** input type.

See [input type detection](/docs/en-us/input.md#input-type-detection) for more information.

> **Info:** For alternative gamepad detection methods, see the `Class.UserInputService.GamepadEnabled` property and the `Class.UserInputService.GamepadConnected|GamepadConnected`/`Class.UserInputService.GamepadDisconnected|GamepadDisconnected` events.
## Common control schemas

When considering specific control bindings for the [Input Action System](/docs/en-us/input/input-action-system.md), it's best to establish consistency across different games. The following input bindings will help players immediately feel familiar and comfortable with gamepad controls.

| Input | Common use cases |
| --- | --- |
| `Enum.KeyCode\|ButtonA` | Accepts player prompts or GUI selections. Alternatively used for primary actions such as jumping. |
| `Enum.KeyCode\|ButtonB` | Cancels player prompts or GUI selections. Alternatively used for secondary actions such as a dodge, roll, or sprint. |
| `Enum.KeyCode\|Thumbstick1` | Generally associated with character movement. |
| `Enum.KeyCode\|Thumbstick2` | Generally associated with camera movement. |
| `Enum.KeyCode\|ButtonL2`, `Enum.KeyCode\|ButtonR2` | Generally used for primary actions, such as shooting. |
| `Enum.KeyCode\|ButtonL1`, `Enum.KeyCode\|ButtonR1`, `Enum.KeyCode\|ButtonX`, `Enum.KeyCode\|ButtonY` | Secondary actions such as reloading, targeting, or accessing an inventory or minimap. |

#### Xbox

#### PlayStation

## Haptic feedback

Many gamepad controllers have motors built in to provide haptic feedback. Adding rumbles and vibrations can greatly enhance a player's experience and provide subtle feedback beyond visuals or audio.

Roblox supports haptics for PlayStation gamepads, Xbox gamepads, and the Quest Touch controller. Haptic feedback is managed through `Class.HapticEffect` instances which can be set to a specific `Class.HapticEffect.Type|Type` such as `Enum.HapticEffectType|GameplayCollision` or `Enum.HapticEffectType|UIClick`.

Once a `Class.HapticEffect` is in place, you can initiate it through the `Class.HapticEffect:Play()|Play()` method, for instance:

```lua
local Workspace = game:GetService("Workspace")

local effect = Instance.new("HapticEffect")
effect.Type = Enum.HapticEffectType.GameplayExplosion
effect.Parent = Workspace

-- Play the haptic effect
effect:Play()
```

## Controller emulation

Use [Controller Emulator](/docs/en-us/studio/controller-emulator.md) to test gamepad input directly in Studio without a physical controller connected. It shows a picture of the emulated device and lights up its controls as input arrives, which helps confirm that your `Class.UserInputService` handlers and [Input Action System](/docs/en-us/input/input-action-system.md) bindings react the way you expect.
