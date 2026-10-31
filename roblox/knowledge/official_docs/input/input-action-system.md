---
title: "Input Action System"
url: /docs/en-us/input/input-action-system
last_updated: 2026-10-30T19:55:44Z
description: "The cross-platform Input Action System lets you connect actions and arrange bindings across various hardware inputs at edit time."
---

# Input Action System

The cross-platform **Input Action System** lets you connect [actions](#input-actions) and arrange [bindings](#input-bindings) across various hardware inputs at edit time. Combined with [contexts](#input-contexts), you can easily configure and edit a modular input system that works on any device in any phase of play. Use cases include:

- A first-person shooter system with actions dynamically swapping in and out depending on if the player is in battle mode or spectator mode.
- A comprehensive driving system equipped with acceleration/deceleration, car boosters, and refuel stations.
- Hotkeys for an abilities system in a fighting game to swap out moves seamlessly without players missing a punch.

## Input contexts

An `Class.InputContext` is a collection of actions which holds related [input actions](#input-actions), for example `PlayContext` for in‑game character controls and `NavContext` for controls to navigate around UI menus. You can [enable/disable contexts](#context-changes) (and their corresponding actions) through their `Class.InputContext.Enabled|Enabled` property, such as to enable the `NavContext` when an inventory menu is open and then change to the `PlayContext` when the player closes the menu and returns to primary gameplay.

Even if a game may not use multiple input contexts initially, it's recommended to create a primary context at the top level of any input system, for example the `PlayContext` instance for input that occurs during gameplay.

1. **RECOMMENDED** Create a `Class.Folder` named `Inputs` inside `Class.ReplicatedStorage` to hold various input contexts.![New Folder inside ReplicatedStorage, renamed to Inputs](../assets/studio/explorer/ReplicatedStorage-Folder-Inputs.png)
2. Insert a new `Class.InputContext` into the folder and rename it to `PlayContext`.![New InputContext instance inside ReplicatedStorage, renamed to PlayContext](../assets/studio/explorer/ReplicatedStorage-InputContext.png)
3. **OPTIONAL** In the [Properties](/docs/en-us/studio/properties.md) window, set `Class.InputContext.Priority|Priority` to `2000` and enable `Class.InputContext.Sink|Sink`. A context with `Class.InputContext.Sink|Sink` enabled consumes input events for its bound `Enum.KeyCode|KeyCodes` at its priority level, blocking those inputs from reaching lower-priority contexts. This is practical for use cases like an inventory screen that should suppress specific gameplay inputs while open. In this example, `PlayContext` is given a high enough `Class.InputContext.Priority|Priority` to sink its bound inputs before the default `Class.PlayerScripts` contexts process them.![InputContext with Priority set to 2000 and Sink enabled](../assets/studio/properties/InputContext-Priority-Sink.png)

## Input actions

An `Class.InputAction` defines a gameplay action mechanic such as "Jump," "Sprint," or "Shoot." These actions are then mapped to hardware inputs using [input bindings](#input-bindings).

An `Class.InputAction` can be of several variations depending on its `Class.InputAction.Type|Type` property (`Enum.InputActionType`). The default is `Enum.InputActionType|Bool`, designed to receive `true`/`false` values from press/release of inputs such as `Enum.KeyCode.ButtonA|ButtonA`, `Enum.KeyCode.E|E`, or `Enum.KeyCode.MouseLeftButton|MouseLeftButton`.

> **Success:**`Class.InputAction` also exposes a read-only `Class.InputAction.PreferredBinding|PreferredBinding` property that returns the child `Class.InputBinding` best matching the player's current input device (keyboard/mouse, gamepad, or touch). It updates dynamically as the player's device configuration changes and is the basis for [displaying bindings](#displaying-bindings) to players.

| Input Action Type | Example Usage |
| --- | --- |
| `Enum.InputActionType\|Bool` | Triggered actions such as jump, shoot, sprint, etc. with support for pressed/released thresholds on analog inputs. |
| `Enum.InputActionType\|Direction1D` | Variable zero-to-full actions such as a car's accelerator pedal or a view scope's zoom level. |
| `Enum.InputActionType\|Direction2D` | 2D directional movement such as camera rotation, or the standard Roblox character movement. |
| `Enum.InputActionType\|Direction3D` | 3D directional movement like an airborne vehicle that can levitate up/down, accelerate/decelerate, and drift left/right. |
| `Enum.InputActionType\|ViewportPosition` | 2D viewport coordinates like mouse input, such as for custom cursors or raycasting to select world objects. |

#### Character Sprint

To test an `Class.InputAction` for simple character sprinting:

1. **RECOMMENDED** Select the top-level `Class.Workspace` object in the [Explorer](/docs/en-us/studio/explorer.md) and then, in the [Properties](/docs/en-us/studio/properties.md) window, set the `Class.Workspace.PlayerScriptsUseInputActionSystem|PlayerScriptsUseInputActionSystem` property to `Enum.RolloutState|Enabled`.
2. Create a new `Class.InputAction` inside the `PlayContext` context within `Class.ReplicatedStorage`. Rename it to `CharacterSprint` to indicate its dedicated action.![New InputAction instance inside an InputContext, renamed to CharacterSprint](../assets/studio/explorer/ReplicatedStorage-InputContext-SprintAction.png)
3. In the [Properties](/docs/en-us/studio/properties.md) window, notice that the action's `Class.InputAction.Type|Type` is `Enum.InputActionType|Bool` (default). This is a logical type for simple character sprinting as a boolean `true`/`false` action (character is either sprinting or not sprinting).![Type property of an InputAction set to Bool](../assets/studio/properties/SprintAction-Type-Bool.png)

#### Camera Rotation

To test an `Class.InputAction` for camera rotation:

1. Create a new `Class.InputAction` inside the `PlayContext` context within `Class.ReplicatedStorage`. Rename it to `CameraRotate` to indicate its dedicated action.![New InputAction instance inside an InputContext, renamed to CameraRotate](../assets/studio/explorer/ReplicatedStorage-InputContext-CameraAction.png)
2. In the [Properties](/docs/en-us/studio/properties.md) window, set the action's `Class.InputAction.Type|Type` to `Enum.InputActionType|Direction2D`. This reflects that camera rotation is a continuous 2D analog input rather than a discrete press/release.![Type property of an InputAction set to Direction2D](../assets/studio/properties/CameraAction-Type-Direction2D.png)

## Input bindings

An `Class.InputBinding` defines which hardware binding should trigger the parent `Class.InputAction`, for example a key press, gamepad button, or tap on a touch‑enabled device. For [cross‑platform](/docs/en-us/projects/cross-platform.md) compatibility, each `Class.InputAction` should have an `Class.InputBinding` for **gamepad**, **keyboard/mouse**, and **touch** as illustrated here.

** Default Bindings**

Roblox provides default input bindings for movement, camera control, and basic environment interaction — Roblox players are familiar with these controls, so you should only override them in specific cases. Also note that the **reserved** inputs cannot be overridden and will always operate with their intended purpose.

#### Roblox Reserved

| Action | Mouse/Keyboard | Gamepad | Touch |
| --- | --- | --- | --- |
| Open Roblox menu | `Esc` | `Start` button (`Enum.KeyCode\|ButtonStart`) | N/A |
| [Developer Console](/docs/en-us/studio/developer-console.md) | `F9` | N/A | N/A |
| Fullscreen mode (Windows)<br>Show desktop (Mac) | `F11` | N/A | N/A |
| Record video (Windows) | `F12` | N/A | N/A |
| Take screenshot | `PrintScreen` | N/A | N/A |

#### Character

| Action | Mouse/Keyboard | Gamepad | Touch |
| --- | --- | --- | --- |
| Move forward | `W` `↑` | Press up on primary thumbstick | Press up on virtual thumbstick |
| Move backward | `S` `↓` | Press down on primary thumbstick | Press down on virtual thumbstick |
| Move left | `A` | Press left on primary thumbstick | Press left on virtual thumbstick |
| Move right | `D` | Press right on primary thumbstick | Press right on virtual thumbstick |
| Jump | `Space` |   | Tap virtual jump button |

#### Interface / Inventory

> **Info:** The following action inputs are reserved unless you [disable the respective feature](/docs/en-us/players/disable-ui.md).

| Action | Mouse/Keyboard | Gamepad | Touch |
| --- | --- | --- | --- |
| Open text chat | `/` | N/A | N/A |
| Show/hide players list | `Tab` | N/A | N/A |
| Toggle backpack | ``` | N/A | N/A |
| Equip/unequip tools | `0`-`9` | Swap between tools using front‑left and front‑right triggers (`Enum.KeyCode.ButtonL1\|ButtonL1` and `Enum.KeyCode.ButtonR1\|ButtonR1`) | Tap on-screen tool icons |
| Use equipped tool | Click left mouse button | Back‑right trigger (`Enum.KeyCode.ButtonR2\|ButtonR2`) | Tap on screen |
| Drop equipped tool | `Backspace` | N/A | N/A |
| Toggle **UI selection** mode¹ | `\` | `Select` button (`Enum.KeyCode.ButtonSelect\|ButtonSelect`) | N/A |
| Navigate among interactive UI elements while in **UI selection** mode | `↑` `↓` `←` `→`<br>`W` `S` `A` `D` | Primary thumbstick (`Enum.KeyCode.Thumbstick1\|Thumbstick1`) or D‑pad (`Enum.KeyCode.DPadUp\|DPadUp`; `Enum.KeyCode.DPadDown\|DPadDown`; `Enum.KeyCode.DPadLeft\|DPadLeft`; `Enum.KeyCode.DPadRight\|DPadRight`) | |
| Activate an interactive UI element while in **UI selection** mode | `Enter` | Back‑right trigger (`Enum.KeyCode.ButtonR2\|ButtonR2`) | |
| Scroll up/down/left/right in selected `Class.ScrollingFrame` while in **UI selection** mode | `PageUp`<br>`PageDown`<br>`Home`<br>`End` | Secondary thumbstick (`Enum.KeyCode.Thumbstick2\|Thumbstick2`) | |

_¹ If `Class.GuiService.GuiNavigationEnabled|GuiNavigationEnabled` is enabled (default)_

#### Camera

| Action | Mouse/Keyboard | Gamepad | Touch |
| --- | --- | --- | --- |
| Move camera view around | While holding right mouse button | Move secondary thumbstick | Touch-drag around screen |
| Zoom camera in/out | Mouse scroll wheel<br>`I`/`O` | Press secondary thumbstick | Pinch in/out on screen |
| Rotate camera left or right | `←` `→` | N/A | N/A |
| Toggle mouse lock² | `Shift` | N/A | N/A |

_² If `Class.StarterPlayer.EnableMouseLockOption|EnableMouseLockOption` is enabled (default)_

The `Class.InputAction.Type|Type` assigned to the parent `Class.InputAction` directly affects which general input types (key/button/tap, analog trigger, thumbstick, etc.) are valid for child `Class.InputBinding` instances. In turn, values sent to the parent action's connected events depend on a binding's chosen input type. See [input events](#input-events) for details on the correlation between action types, bindings, and return values.

#### Character Sprint

To hook up bindings for simple character sprinting:

1. Insert a new `Class.InputBinding` into the `CharacterSprint` action and rename it to `KeyboardBinding`. Then set the binding's `Class.InputBinding.KeyCode|KeyCode` property to `Enum.KeyCode.LeftShift|LeftShift`.
2. Insert a second `Class.InputBinding` into the `CharacterSprint` action and rename it to `GamepadBinding`. Then set the binding's `Class.InputBinding.KeyCode|KeyCode` property to `Enum.KeyCode.ButtonY|ButtonY`.
3. Inside a `Class.ScreenGui` container inside `Class.StarterGui`, create an [on-screen button](/docs/en-us/ui/buttons.md), rename it to `SprintButton`, and [position/resize](/docs/en-us/ui/position-and-size.md) it as desired.
4. Insert a third `Class.InputBinding` into the `CharacterSprint` action and rename it to `TouchBinding`. Then, in the [Properties](/docs/en-us/studio/properties.md) window, link the binding's `Class.InputBinding.UIButton|UIButton` property to the `SprintButton` button you created previously inside `Class.StarterGui`.

#### Camera Rotation

To hook up bindings for camera rotation:

1. Insert a new `Class.InputBinding` into the `CameraRotate` action and rename it to `KeyboardBinding`. Leave `Class.InputBinding.KeyCode|KeyCode` empty and instead set the four composite directional properties — `Class.InputBinding.Left|Left`, `Class.InputBinding.Right|Right`, `Class.InputBinding.Up|Up`, and `Class.InputBinding.Down|Down` — to `Enum.KeyCode.Left|Left`, `Enum.KeyCode.Right|Right`, `Enum.KeyCode.Up|Up`, and `Enum.KeyCode.Down|Down` respectively.
2. Insert a second `Class.InputBinding` and rename it to `GamepadBinding`. Then set the binding's `Class.InputBinding.KeyCode|KeyCode` property to `Enum.KeyCode.Thumbstick2|Thumbstick2` (right thumbstick).
3. Insert a third `Class.InputBinding` and rename it to `MouseBinding`. Set the binding's `Class.InputBinding.KeyCode|KeyCode` property to `Enum.KeyCode.MouseDelta|MouseDelta` and its `Class.InputBinding.Scale|Scale` to `0.01`. `Enum.KeyCode.MouseDelta|MouseDelta` reports values in pixels, so the scale converts them to a reasonable rotation range.
4. Insert a fourth `Class.InputBinding` and rename it to `TouchBinding`. Set the binding's `Class.InputBinding.KeyCode|KeyCode` property to `Enum.KeyCode.TouchDelta|TouchDelta` and its `Class.InputBinding.Scale|Scale` to `0.01`. Like `Enum.KeyCode.MouseDelta|MouseDelta`, `Enum.KeyCode.TouchDelta|TouchDelta` reports values in pixels.

## Input events

The `Class.InputAction` instance has three built-in **events** to handle player input coming from `Class.InputBinding|InputBindings`.

- `Class.InputAction.Pressed|Pressed` — This event fires only when the input action's `Class.InputAction.Type|Type` is set to `Enum.InputActionType|Bool`, and only when the state transitions from `false` to `true`.
- `Class.InputAction.Released|Released` — This event fires only when the input action's `Class.InputAction.Type|Type` is set to `Enum.InputActionType|Bool`, and only when the state transitions from `true` to `false`.
- `Class.InputAction.StateChanged|StateChanged` — This event fires for all input action types whenever the state changes, except if the state attempts to transition to the same state.

Depending on the input action's `Class.InputAction.Type|Type` (`Enum.InputActionType|Bool`, `Enum.InputActionType|Direction1D`, `Enum.InputActionType|Direction2D`, `Enum.InputActionType|Direction3D`, or `Enum.InputActionType|ViewportPosition`) and the general input type coming from a child `Class.InputBinding` (key/button/tap, analog trigger, thumbstick, etc.), different values are returned to the `Class.InputAction.Pressed|Pressed`, `Class.InputAction.Released|Released`, and `Class.InputAction.StateChanged|StateChanged` event handlers. Examine the following tables to better understand the correlation.

#### Bool

The `Enum.InputActionType|Bool` type is best for triggered actions such as jump, shoot, sprint, etc. with support for pressed/released thresholds on analog inputs.

| Valid Input Types on `Class.InputBinding\|InputBindings` | Returned to the `Class.InputAction` Event(s) |
| --- | --- |
| Boolean inputs from keyboard keys or basic mouse/gamepad buttons through the binding's `Class.InputBinding.KeyCode\|KeyCode` property, or a `Class.GuiButton` press/release through the binding's `Class.InputBinding.UIButton\|UIButton` property. | <ul><li>`Class.InputAction.Pressed\|Pressed` event:<ul><li>`true` when pressed</li></ul></li><li>`Class.InputAction.Released\|Released` event:<ul><li>`true` when released</li></ul></li><li>`Class.InputAction.StateChanged\|StateChanged` event:<ul><li>`true` (pressed) or `false` (released)</li></ul></li></ul> |
| Variable input amounts from analog inputs like gamepad triggers (`Enum.KeyCode.ButtonL2\|ButtonL2`/`Enum.KeyCode.ButtonR2\|ButtonR2`) through the binding's `Class.InputBinding.KeyCode\|KeyCode` property. | <ul><li>`Class.InputAction.Pressed\|Pressed` event:<ul><li>`true` when trigger press is `>=` `Class.InputBinding.PressedThreshold\|PressedThreshold`</li></ul></li><li>`Class.InputAction.Released\|Released` event:<ul><li>`true` when trigger press is `<=` `Class.InputBinding.ReleasedThreshold\|ReleasedThreshold`</li></ul></li><li>`Class.InputAction.StateChanged\|StateChanged` event:<ul><li>`true` when trigger press is `>=` `Class.InputBinding.PressedThreshold\|PressedThreshold`</li><li>`false` when trigger press is `<=` `Class.InputBinding.ReleasedThreshold\|ReleasedThreshold`</li></ul></li></ul> |

#### Direction1D

The `Enum.InputActionType|Direction1D` type is best for variable zero‑to‑full actions such as a car's accelerator pedal or a view scope's zoom level.

| Valid Input Types on `Class.InputBinding\|InputBindings` | Returned to the `Class.InputAction` Event(s) |
| --- | --- |
| Variable input amounts from analog inputs like gamepad triggers (`Enum.KeyCode.ButtonL2\|ButtonL2`/`Enum.KeyCode.ButtonR2\|ButtonR2`) through the binding's `Class.InputBinding.KeyCode\|KeyCode`, `Class.InputBinding.Up\|Up`, and `Class.InputBinding.Down\|Down` properties. | <ul><li>`Class.InputAction.StateChanged\|StateChanged` event:<ul><li>`0` to `1` (fully released to fully pressed) through the `Class.InputBinding.KeyCode\|KeyCode` or `Class.InputBinding.Up\|Up` properties</li><li>`0` to `-1` (fully released to fully pressed) through the `Class.InputBinding.Down\|Down` property</li></ul></li></ul> |
| Boolean inputs from keyboard keys or basic mouse/gamepad buttons through the binding's `Class.InputBinding.KeyCode\|KeyCode`, `Class.InputBinding.Up\|Up`, and `Class.InputBinding.Down\|Down` properties. | <ul><li>`Class.InputAction.StateChanged\|StateChanged` event:<ul><li>`1` (pressed) or `0` (released) through the `Class.InputBinding.KeyCode\|KeyCode` or `Class.InputBinding.Up\|Up` properties</li><li>`-1` (pressed) or `0` (released) through the `Class.InputBinding.Down\|Down` property</li></ul></li></ul> |

#### Direction2D

The `Enum.InputActionType|Direction2D` type is best for 2D directional movement such as camera rotation, or the standard Roblox character movement.

| Valid Input Types on `Class.InputBinding\|InputBindings` | Returned to the `Class.InputAction` Event(s) |
| --- | --- |
| Variable input amounts from 2D analog inputs like gamepad thumbsticks (`Enum.KeyCode.Thumbstick1\|Thumbstick1`/`Enum.KeyCode.Thumbstick2\|Thumbstick2`) through the binding's `Class.InputBinding.KeyCode\|KeyCode` property. | <ul><li>`Class.InputAction.StateChanged\|StateChanged` event:<ul><li>`Datatype.Vector2` between`(-1, -1)` and`(1, 1)`</li></ul></li></ul> |
| Variable input amounts from analog inputs like gamepad triggers (`Enum.KeyCode.ButtonL2\|ButtonL2`/`Enum.KeyCode.ButtonR2\|ButtonR2`) through the binding's `Class.InputBinding.Up\|Up`, `Class.InputBinding.Down\|Down`, `Class.InputBinding.Left\|Left`, and `Class.InputBinding.Right\|Right` properties. | <ul><li>`Class.InputAction.StateChanged\|StateChanged` event:<ul><li>`Datatype.Vector2` with `Datatype.Vector2.Y\|Y` component between `0` and `1` (fully released to fully pressed) through the `Class.InputBinding.Up\|Up` property</li><li>`Datatype.Vector2` with `Datatype.Vector2.Y\|Y` component between `0` and `-1` (fully released to fully pressed) through the `Class.InputBinding.Down\|Down` property</li><li>`Datatype.Vector2` with `Datatype.Vector2.X\|X` component between `0` and `-1` (fully released to fully pressed) through the `Class.InputBinding.Left\|Left` property</li><li>`Datatype.Vector2` with `Datatype.Vector2.X\|X` component between `0` and `1` (fully released to fully pressed) through the `Class.InputBinding.Right\|Right` property</li></ul></li></ul> |
| Boolean inputs from keyboard keys or basic mouse/gamepad buttons through the binding's `Class.InputBinding.Up\|Up`, `Class.InputBinding.Down\|Down`, `Class.InputBinding.Left\|Left`, and `Class.InputBinding.Right\|Right` properties. | <ul><li>`Class.InputAction.StateChanged\|StateChanged` event:<ul><li>`Datatype.Vector2` of`(0, 1)` (pressed) or`(0, 0)` (released) through the `Class.InputBinding.Up\|Up` property</li><li>`Datatype.Vector2` of`(0, -1)` (pressed) or`(0, 0)` (released) through the `Class.InputBinding.Down\|Down` property</li><li>`Datatype.Vector2` of`(-1, 0)` (pressed) or`(0, 0)` (released) through the `Class.InputBinding.Left\|Left` property</li><li>`Datatype.Vector2` of`(1, 0)` (pressed) or`(0, 0)` (released) through the `Class.InputBinding.Right\|Right` property</li></ul></li></ul> |

#### Direction3D

The `Enum.InputActionType|Direction3D` type is best for 3D directional movement like an airborne vehicle that can levitate up/down, accelerate/decelerate, and drift left/right.

| Valid Input Types on `Class.InputBinding\|InputBindings` | Returned to the `Class.InputAction` Event(s) |
| --- | --- |
| Variable input amounts from analog inputs like gamepad triggers (`Enum.KeyCode.ButtonL2\|ButtonL2`/`Enum.KeyCode.ButtonR2\|ButtonR2`) through the binding's `Class.InputBinding.Up\|Up`, `Class.InputBinding.Down\|Down`, `Class.InputBinding.Left\|Left`, `Class.InputBinding.Right\|Right`, `Class.InputBinding.Forward\|Forward`, and `Class.InputBinding.Backward\|Backward` properties. | <ul><li>`Class.InputAction.StateChanged\|StateChanged` event:<ul><li>`Datatype.Vector3` with `Datatype.Vector3.Y\|Y` component between `0` and `1` (fully released to fully pressed) through the `Class.InputBinding.Up\|Up` property</li><li>`Datatype.Vector3` with `Datatype.Vector3.Y\|Y` component between `0` and `-1` (fully released to fully pressed) through the `Class.InputBinding.Down\|Down` property</li><li>`Datatype.Vector3` with `Datatype.Vector3.X\|X` component between `0` and `-1` (fully released to fully pressed) through the `Class.InputBinding.Left\|Left` property</li><li>`Datatype.Vector3` with `Datatype.Vector3.X\|X` component between `0` and `1` (fully released to fully pressed) through the `Class.InputBinding.Right\|Right` property</li><li>`Datatype.Vector3` with `Datatype.Vector3.Z\|Z` component between `0` and `-1` (fully released to fully pressed) through the `Class.InputBinding.Forward\|Forward` property</li><li>`Datatype.Vector3` with `Datatype.Vector3.Z\|Z` component between `0` and `1` (fully released to fully pressed) through the `Class.InputBinding.Backward\|Backward` property</li></ul></li></ul> |
| Boolean inputs from keyboard keys or basic mouse/gamepad buttons through the binding's `Class.InputBinding.Up\|Up`, `Class.InputBinding.Down\|Down`, `Class.InputBinding.Left\|Left`, `Class.InputBinding.Right\|Right`, `Class.InputBinding.Forward\|Forward`, and `Class.InputBinding.Backward\|Backward` properties. | <ul><li>`Class.InputAction.StateChanged\|StateChanged` event:<ul><li>`Datatype.Vector3` of`(0, 1, 0)` (pressed) or`(0, 0, 0)` (released) through the `Class.InputBinding.Up\|Up` property</li><li>`Datatype.Vector3` of`(0, -1, 0)` (pressed) or`(0, 0, 0)` (released) through the `Class.InputBinding.Down\|Down` property</li><li>`Datatype.Vector3` of`(-1, 0, 0)` (pressed) or`(0, 0, 0)` (released) through the `Class.InputBinding.Left\|Left` property</li><li>`Datatype.Vector3` of`(1, 0, 0)` (pressed) or`(0, 0, 0)` (released) through the `Class.InputBinding.Right\|Right` property</li><li>`Datatype.Vector3` of`(0, 0, -1)` (pressed) or`(0, 0, 0)` (released) through the `Class.InputBinding.Forward\|Forward` property</li><li>`Datatype.Vector3` of`(0, 0, 1)` (pressed) or`(0, 0, 0)` (released) through the `Class.InputBinding.Backward\|Backward` property</li></ul></li></ul> |

#### ViewportPosition

The `Enum.InputActionType|ViewportPosition` type is best for absolute 2D viewport coordinates of an input such as a mouse pointer or touch, which can be used for features like custom cursors or selecting objects.

| Valid Input Types on `Class.InputBinding\|InputBindings` | Returned to the `Class.InputAction` Event(s) |
| --- | --- |
| Variable input amounts from positional inputs such as a mouse pointer (`Enum.KeyCode.MousePosition\|MousePosition`) or touch (`Enum.KeyCode.Touch\|Touch`). | <ul><li>`Class.InputAction.StateChanged\|StateChanged` event:<ul><li>`Datatype.Vector2` between`(0, 0)` and the maximum absolute`(X, Y)` pixel size in the viewport.</li></ul></li></ul> |

#### Character Sprint

To connect events for simple character sprinting:

1. Insert a new `Class.Script` into the `CharacterSprint` tree, alongside the various input bindings. Then set its `Class.BaseScript.RunContext|RunContext` to `Enum.RunContext.Client|Client` and rename it to `OnActivate`.
2. Paste the following code into the `OnActivate` script. Note the `Class.InputAction.Pressed|Pressed` event connection on lines `13`‑`15` which doubles the character's walk speed when a sprint input binding is pressed, and the corresponding `Class.InputAction.Released|Released` event connection on lines `16`‑`18` which resets the walk speed to default when a sprint input binding is released.```lua
local Players = game:GetService("Players")

local player = Players.LocalPlayer
local character = player.Character
if not character or character.Parent == nil then
	character = player.CharacterAdded:Wait()
end
local humanoid = character:WaitForChild("Humanoid")
local defaultWalkSpeed = humanoid.WalkSpeed

local inputAction = script.Parent

inputAction.Pressed:Connect(function()
	humanoid.WalkSpeed = defaultWalkSpeed * 2
end)
inputAction.Released:Connect(function()
	humanoid.WalkSpeed = defaultWalkSpeed
end)
```
3. Playtest your game and test the character sprint action with the [bindings](#input-bindings) you chose previously: `Enum.KeyCode.LeftShift|LeftShift` for keyboard, `Enum.KeyCode.ButtonY|ButtonY` for gamepad, and the on‑screen `SprintButton` for touch‑enabled devices. Remember that you can use the [Controller Emulator](/docs/en-us/studio/testing-modes.md#controller-emulation) to test gamepad inputs directly in Roblox Studio.

#### Camera Rotation

For **continuous analog inputs** like camera rotation, `Class.InputAction.StateChanged|StateChanged` fires **once** when the state changes and does not signal until the next change, so a thumbstick held at a fixed angle only fires the event once. In these cases, poll `Class.InputAction:GetState()|GetState()` each frame and multiply by delta time for frame-rate-independent behavior.

1. Insert a new `Class.Script` into the `CameraRotate` tree, alongside the various input bindings. Then set its `Class.BaseScript.RunContext|RunContext` to `Enum.RunContext.Client|Client` and rename it to `OnInput`.
2. Paste the following code into the `OnInput` script.```lua
local RunService = game:GetService("RunService")

local CAMERA_SENSITIVITY = 1.5 -- Radians per second at action state 1

local inputAction = script.Parent
local camera = workspace.CurrentCamera
camera.CameraType = Enum.CameraType.Scriptable

RunService:BindToRenderStep("CameraRotation", Enum.RenderPriority.Camera.Value, function(dt)
	local state = inputAction:GetState()
	if state.Magnitude > 0 then
		camera.CFrame = camera.CFrame
			* CFrame.Angles(0, -state.X * CAMERA_SENSITIVITY * dt, 0)
			* CFrame.Angles(-state.Y * CAMERA_SENSITIVITY * dt, 0, 0)
	end
end)
```

## Context changes

Once you have an [input context](#input-contexts) such as `PlayContext`, you can enable/disable it during gameplay through scripting, change its `Class.InputContext.Priority|Priority` to determine which actions take precedence over others, and `Class.InputContext.Sink|Sink` inputs from being processed within contexts of lower priority.

1. To make it easier to switch contexts from other scripts, insert a new `Class.BindableEvent` into your inputs folder within `Class.ReplicatedStorage` and rename it to `ContextEvent`.
2. Create a new `Class.Script` at the same level, set its `Class.BaseScript.RunContext|RunContext` to `Enum.RunContext.Client|Client`, and rename it to `UpdateContext`.
3. Inside the `UpdateContext` script, paste the following code:```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local inputsFolder = ReplicatedStorage:WaitForChild("Inputs")
local contextEvent = inputsFolder:WaitForChild("ContextEvent")

-- Connect bindable event
contextEvent.Event:Connect(function(targetContext, enabled)
	local context = inputsFolder:FindFirstChild(targetContext)
	if context then
		context.Enabled = enabled
		print(context.Name .. ": " .. tostring(context.Enabled))
	else
		warn("InputContext not found!")
	end
end)
```
4. With the `UpdateContext` script in place, you can now update a named `Class.InputContext` by firing the bindable event, for example from a `Class.LocalScript` that powers a `Class.GuiButton` inside a `Class.ScreenGui` container.```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local inputsFolder = ReplicatedStorage:WaitForChild("Inputs")
local contextEvent = inputsFolder:WaitForChild("ContextEvent")

local button = script.Parent
button.Activated:Connect(function()
	-- Fire bindable event with target input context and enabled state
	contextEvent:Fire("PlayContext", true)
end)
```

## Displaying bindings

Once you've set up [actions](#input-actions) and [bindings](#input-bindings), you'll typically need to show players, via on‑screen [assistive hints](/docs/en-us/projects/cross-platform.md#assistive-hints), which key or button triggers each action:

#### Keyboard Input

#### Gamepad Input

The Input Action System provides two approaches:

- **RECOMMENDED** `Class.InputActionLabel` — A no-code, drag-and-drop `Class.GuiObject` that automatically displays the correct input per platform.
- **INTERMEDIATE** `Class.InputAction.PreferredBinding|PreferredBinding` — A read-only `Class.InputAction` property for creators who want full control over how bindings are displayed in custom UI.

#### InputActionLabel

> **Success:** This class/object is currently in beta. Enable it through **File** ⟩ **Beta Features** ⟩ **InputActionLabel**.

`Class.InputActionLabel` is a `Class.GuiObject` that you can insert into any `Class.ScreenGui` or `Class.SurfaceGui`. Once its `Class.InputActionLabel.InputAction|InputAction` property is set to reference an existing `Class.InputAction` instance, it automatically resolves and displays the correct keybinding for the player's current input device — no scripting required. When the player switches devices (for example, picking up a gamepad after using a keyboard) or rebinds a control, the label updates instantly.

To add an `Class.InputActionLabel`:

1. Inside a `Class.ScreenGui` container inside `Class.StarterGui`, insert an `Class.InputActionLabel` just like any other `Class.GuiObject`.
2. In the [Properties](/docs/en-us/studio/properties.md) window, set its `Class.InputActionLabel.InputAction|InputAction` property to the `Class.InputAction` instance you want to display (for example, your "Sprint" action under `Class.ReplicatedStorage`) and [position/resize](/docs/en-us/ui/position-and-size.md) it as desired.
3. When the label resolves what to show, it checks the following in order:
  1. **Custom Images** — If child `Class.InputBinding|InputBindings` have their `Class.InputBinding.DisplayImage|DisplayImage` property set, the label renders those images directly.
  2. **Platform Key Images** — Lacking custom images, the label renders platform-provided images for child `Class.InputBinding|InputBindings` through `Class.UserInputService:GetImageForKeyCode()`, if such images are available. Composite bindings with modifiers show multiple icons with `+` separators.
  3. **Custom Names** — Lacking available images, if child `Class.InputBinding|InputBindings` have their `Class.InputBinding.DisplayName|DisplayName` property set, the label renders that text using the label's style properties.
  4. **Platform Key Strings** — Lacking all of the above, the label renders platform-provided strings through `Class.UserInputService:GetStringForKeyCode()`.
  5. If no `Class.InputAction` is assigned or no child `Class.InputBinding` exists, the label renders a placeholder icon.

#### PreferredBinding

For customized use cases where you need full control over hint display (custom animations, conditional visibility, composited layouts), you can use `Class.InputAction.PreferredBinding` to query the current binding and build your own UI. `Class.InputAction.PreferredBinding|PreferredBinding` is a read-only property that returns the child `Class.InputBinding` which best matches the player's current input device.

The following two `Class.InputBinding` properties provide the custom display overrides used for `Class.InputAction.PreferredBinding|PreferredBinding`. If neither is set, fall back to platform-provided values via `Class.UserInputService:GetStringForKeyCode()|GetStringForKeyCode()` and `Class.UserInputService:GetImageForKeyCode()|GetImageForKeyCode()`.

- `Class.InputBinding.DisplayName|DisplayName` — A read/write string for custom text, for example, "Sprint."
- `Class.InputBinding.DisplayImage|DisplayImage` — A read/write `Datatype.Content` value for a custom image.

The following examples assume a client `Class.Script` parented to the `Class.InputAction` and a hint UI object (`Class.TextLabel` or `Class.ImageLabel`) inside a `Class.ScreenGui` within the player's `Class.PlayerGui`. Both connect to changes to `Class.InputAction.PreferredBinding|PreferredBinding` so that the hint refreshes whenever the player switches input devices.

```lua
local Players = game:GetService("Players")
local UserInputService = game:GetService("UserInputService")

local inputAction = script.Parent
local player = Players.LocalPlayer
local screenGui = player:WaitForChild("PlayerGui"):WaitForChild("ScreenGui")
local label = screenGui:FindFirstChildWhichIsA("TextLabel")

local function updateHintText()
	if not label then
		warn("Label UI object not found!")
		return
	end

	local binding = inputAction.PreferredBinding
	if binding and binding.DisplayName ~= "" then
		label.Text = binding.DisplayName
	elseif binding and binding.KeyCode ~= Enum.KeyCode.None then
		label.Text = UserInputService:GetStringForKeyCode(binding.KeyCode)
	else
		label.Text = ""
	end
end

inputAction:GetPropertyChangedSignal("PreferredBinding"):Connect(updateHintText)
updateHintText()
```

```lua
local Players = game:GetService("Players")
local UserInputService = game:GetService("UserInputService")

local inputAction = script.Parent
local player = Players.LocalPlayer
local screenGui = player:WaitForChild("PlayerGui"):WaitForChild("ScreenGui")
local label = screenGui:FindFirstChildWhichIsA("ImageLabel")

local function updateHintImage()
	if not label then
		warn("Label UI object not found!")
		return
	end

	local binding = inputAction.PreferredBinding
	if binding and binding.DisplayImage.SourceType ~= Enum.ContentSourceType.None then
		label.ImageContent = binding.DisplayImage
	elseif binding and binding.KeyCode ~= Enum.KeyCode.None then
		local keyImage = UserInputService:GetImageForKeyCode(binding.KeyCode)
		label.ImageContent = (keyImage ~= "") and Content.fromUri(keyImage) or Content.none
	else
		label.ImageContent = Content.none
	end
end

inputAction:GetPropertyChangedSignal("PreferredBinding"):Connect(updateHintImage)
updateHintImage()
```

## Input Action Manager

> **Success:** This tool is currently in beta. Enable it through **File** ⟩ **Beta Features** ⟩ **Input Action Manager**.

The **Input Action Manager** tool is a unified, matrix-style interface to design, audit, and scale your input architecture.

To access it, navigate to the **Window** menu in Studio and select **Input** ⟩ **Input Action Manager**. If your game already uses input [contexts](#input-contexts), [actions](#input-actions), or [bindings](#input-bindings), the manager will automatically scan the `Class.DataModel` and extract those existing instances into the editor grid. Any new input‑related instances will automatically populate into an `Inputs` folder within `Class.ReplicatedStorage`.

![Folder inside ReplicatedStorage named Inputs](../assets/studio/explorer/ReplicatedStorage-Folder-Inputs.png)

To configure an input setup for **character sprint** as outlined in the sections above:

1. **RECOMMENDED** Select the top-level `Class.Workspace` object in the [Explorer](/docs/en-us/studio/explorer.md) and then, in the [Properties](/docs/en-us/studio/properties.md) window, set the `Class.Workspace.PlayerScriptsUseInputActionSystem|PlayerScriptsUseInputActionSystem` property to `Enum.RolloutState|Enabled`.
2. Inside a `Class.ScreenGui` container inside `Class.StarterGui`, create an [on-screen button](/docs/en-us/ui/buttons.md), rename it to `SprintButton`, and [position/resize](/docs/en-us/ui/position-and-size.md) it as desired.
3. In the **Input Action Manager**, hover over the **Context** column header and click the **＋** button. Enter an appropriate name for the new context such as `PlayContext` and press `Enter`. An `Class.InputContext` of the matching name appears in `Class.ReplicatedStorage`.![New InputContext instance inside ReplicatedStorage named PlayContext](../assets/studio/explorer/ReplicatedStorage-InputContext.png)
4. Hover over the new context and click the **＋** button. From the popup menu, select `Enum.InputActionType|Bool`, enter `CharacterSprint` for the action's name, and press `Enter`. An `Class.InputAction` of the matching name appears under the context.![New InputAction instance inside an InputContext named CharacterSprint](../assets/studio/explorer/ReplicatedStorage-InputContext-SprintAction.png)
5. In the new `CharacterSprint` row, assign bindings for each input type:
  1. **Keyboard and Mouse** — Click the arrow button and select `Enum.KeyCode|LeftShift` from the picker menu.
  2. **Touch** — Click the cell and then, in the [Explorer](/docs/en-us/studio/explorer.md) hierarchy, click the `SprintButton` object that you previously inserted into the `Class.ScreenGui`.
  3. **Gamepad** — Click the arrow button and select `Enum.KeyCode|ButtonY` from the picker menu.
  > **Info:** As you assign bindings, watch for warning/error icons in the UI. Yellow warnings (**⚠**) indicate a **missing** binding for [cross‑platform](/docs/en-us/projects/cross-platform.md) compatibility, while red warnings (**⚠**) indicate a **duplicate** binding for actions within the same context.
6. Insert a new `Class.Script` into the `CharacterSprint` tree, alongside the various input bindings. Then set its `Class.BaseScript.RunContext|RunContext` to `Enum.RunContext.Client|Client` and rename it to `OnActivate`.
7. Paste the following code into the `OnActivate` script. Note the `Class.InputAction.Pressed|Pressed` event connection on lines `13`‑`15` which doubles the character's walk speed when a sprint input binding is pressed, and the corresponding `Class.InputAction.Released|Released` event connection on lines `16`‑`18` which resets the walk speed to default when a sprint input binding is released.```lua
local Players = game:GetService("Players")

local player = Players.LocalPlayer
local character = player.Character
if not character or character.Parent == nil then
	character = player.CharacterAdded:Wait()
end
local humanoid = character:WaitForChild("Humanoid")
local defaultWalkSpeed = humanoid.WalkSpeed

local inputAction = script.Parent

inputAction.Pressed:Connect(function()
	humanoid.WalkSpeed = defaultWalkSpeed * 2
end)
inputAction.Released:Connect(function()
	humanoid.WalkSpeed = defaultWalkSpeed
end)
```
