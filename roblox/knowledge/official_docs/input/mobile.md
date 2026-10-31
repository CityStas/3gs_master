---
title: "Mobile input"
url: /docs/en-us/input/mobile
last_updated: 2026-10-30T19:55:44Z
description: "Explains Roblox support for mobile devices."
---

# Mobile input

The majority of Roblox sessions are played on mobile devices, so it's important to consider the mobile [device orientation](#device-orientation) and other [cross‑platform](/docs/en-us/projects/cross-platform.md) factors when designing a game for a wide audience.

To simplify cross‑platform inputs, including player interaction with virtual buttons, Roblox provides the [Input Action System](/docs/en-us/input/input-action-system.md) to define **actions** such as "jump," "sprint," or "shoot" and set up **bindings** for multiple hardware inputs to drive those actions.

Roblox also supports native mobile features like [haptic feedback](#haptic-feedback), touch gestures such as `Class.UserInputService.TouchSwipe|TouchSwipe` and `Class.UserInputService.TouchPinch|TouchPinch`, or accelerometer and gyroscope functionality on `Class.UserInputService.AccelerometerEnabled|AccelerometerEnabled` and `Class.UserInputService.GyroscopeEnabled|GyroscopeEnabled` devices.

## Input type detection

In cross‑platform development, it's important that you determine and respond to the `Class.UserInputService.PreferredInput|PreferredInput` type a player is using, normally to ensure that [UI elements](/docs/en-us/ui.md#ui-objects) like on-screen buttons and menus work elegantly and support interaction across devices.

For example, a touch-enabled device assumes touch is the default input and that touch-buttons may appear for actions, but a player may choose to connect a bluetooth gamepad. In this case, touch remains a valid input, but you can assume the player wants to switch to the connected gamepad as the **primary** input type and possibly use touch as a backup input for on-screen UI.

See [input type detection](/docs/en-us/input.md#input-type-detection) for more information.

## Device orientation

By default, Roblox games run in **landscape** mode, allowing the game to switch between landscape "left" and landscape "right" as the player's device rotates. However, games can be locked to a particular orientation if desired.

There are five different orientation modes, including two sensor-based modes and three locked modes.¹ Each of these can be set as the **default** orientation through `Class.StarterGui.ScreenOrientation`, accessible through Studio's [Properties](/docs/en-us/studio/properties.md) window.

| Sensor Modes |
| --- |
| `Enum.ScreenOrientation\|LandscapeSensor` | The default Roblox setting in which the game always appears in landscape mode (no portrait mode) and the device detects its physical orientation to ensure the game view is always oriented upward. |
| `Enum.ScreenOrientation\|Sensor` | The device detects its physical orientation to ensure the game view is always oriented upward, switching between landscape and portrait mode as needed. |
| Locked Modes |
| `Enum.ScreenOrientation\|LandscapeLeft` | On devices with a virtual home/nav bar, its touch region is at the bottom of the display. On devices with a physical home button, the home button is to the left of the display. |
| `Enum.ScreenOrientation\|LandscapeRight` | On devices with a virtual home/nav bar, its touch region is at the bottom of the display. On devices with a physical home button, the home button is to the right of the display. |
| `Enum.ScreenOrientation\|Portrait` | On devices with a virtual home/nav bar, its touch region is at the bottom of the display. On devices with a physical home button, the home button is below the display. |

_¹ Roblox does not include a "portrait upside-down" mode since many devices do not natively support that orientation_

Beyond the default `Class.StarterGui.ScreenOrientation` property, you can change orientation during gameplay through `Class.PlayerGui.ScreenOrientation`. This can be useful when a game needs to enforce an orientation, such as locking the view to `Enum.ScreenOrientation|Portrait` for a minigame.

The following code in a `Class.LocalScript` sets the screen orientation to portrait after a short delay:

```lua
local Players = game:GetService("Players")

local player = Players.LocalPlayer
local playerGui = player.PlayerGui

task.wait(5)

playerGui.ScreenOrientation = Enum.ScreenOrientation.Portrait
```

Finally, you can detect changes to screen orientation during gameplay by listening to value changes on the `Class.PlayerGui.CurrentScreenOrientation` property.

```lua
local Players = game:GetService("Players")

local player = Players.LocalPlayer
local playerGui = player.PlayerGui

local function onOrientationChange()
	print("Orientation changed to", playerGui.ScreenOrientation)
end

playerGui:GetPropertyChangedSignal("ScreenOrientation"):Connect(onOrientationChange)
```

## Haptic feedback

Most mobile devices have motors built in to provide haptic feedback. Adding rumbles and vibrations can greatly enhance a player's experience and provide subtle feedback beyond visuals or audio.

Roblox supports haptics for haptic-capable devices including most iPhone, Pixel, and Samsung Galaxy devices. Haptic feedback is managed through `Class.HapticEffect` instances which can be set to a specific `Class.HapticEffect.Type|Type` such as `Enum.HapticEffectType|GameplayCollision` or `Enum.HapticEffectType|UIClick`.

Once a `Class.HapticEffect` is in place, you can initiate it through the `Class.HapticEffect:Play()|Play()` method, for instance:

```lua
local Workspace = game:GetService("Workspace")

local effect = Instance.new("HapticEffect")
effect.Type = Enum.HapticEffectType.GameplayExplosion
effect.Parent = Workspace

-- Play the haptic effect
effect:Play()
```
