---
name: Player
last_updated: 2026-10-30T19:55:53Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
summary: "An object that represents a presently connected client to the experience."
---

# Class: Player

> An object that represents a presently connected client to the experience.

## Description

A `Player` object is a client that is currently connected. These objects are
added to the [Players](/docs/reference/engine/classes/Players.md) service when a new player connects, then removed
when they eventually disconnect from the server.

The [Instance.Name](/docs/reference/engine/classes/Instance.md) property reflects the player's username. When saving
information about a player, you should use their [UserId](/docs/reference/engine/classes/Player.md)
since it is possible that a player can change their username.

There are several similar methods in the [Players](/docs/reference/engine/classes/Players.md) service for working
with Player objects. Use these over their respective [Instance](/docs/reference/engine/classes/Instance.md) methods:

- You can get a table of current `Player` objects using
  [Players:GetPlayers()](/docs/reference/engine/classes/Players.md); again, use this instead of
  [Instance:GetChildren()](/docs/reference/engine/classes/Instance.md).
- To detect the addition of `Player` objects, it is recommended to use the
  [Players.PlayerAdded](/docs/reference/engine/classes/Players.md) event (instead of [Instance.ChildAdded](/docs/reference/engine/classes/Instance.md) on
  the [Players](/docs/reference/engine/classes/Players.md) service).
- Similarly, you can detect the removal of `Player` objects using
  [Players.PlayerRemoving](/docs/reference/engine/classes/Players.md), which fires just **before** the `Player` is
  removed (instead of [Instance.ChildRemoved](/docs/reference/engine/classes/Instance.md) which fires after). This
  is important if you are saving information about the player that might be
  removed or cleaned up on removal.

## Properties

### Property: Player.AccountAge

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
    "Players"
  ]
}
```

This property describes how long ago a player's account was registered in
days. It is set using the [SetAccountAge()](/docs/reference/engine/classes/Player.md)
method, which cannot be accessed by scripts.

### Property: Player.AgeChecked

```json
{
  "type": "AgeCheckStatus",
  "access": "ReadOnly",
  "security": {
    "read": "None",
    "write": "RobloxEngineSecurity"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Data",
  "capabilities": [
    "Players"
  ]
}
```

This read-only property holds an [AgeCheckStatus](/docs/reference/engine/enums/AgeCheckStatus.md) value indicating
whether the player has completed age verification. The default value is
[AgeCheckStatus.Unchecked](/docs/reference/engine/enums/AgeCheckStatus.md). It transitions to
[AgeCheckStatus.Checked](/docs/reference/engine/enums/AgeCheckStatus.md) when the player passes age verification
through the [Player:PromptAgeCheck()](/docs/reference/engine/classes/Player.md) flow.

This property is set by the server and cannot be changed by scripts.

### Property: Player.AutoJumpEnabled

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
    "Players"
  ]
}
```

This property determines whether the [Character](/docs/reference/engine/classes/Player.md) of
a [Player](/docs/reference/engine/classes/Player.md) using a mobile device will automatically jump when they
hit an obstacle. This can make levels more navigable while on a mobile
device.

When the player joins the experience, the
[StarterPlayer.AutoJumpEnabled](/docs/reference/engine/classes/StarterPlayer.md) value determines the initial state
of this property. Then, this property determines the value of the
[Humanoid.AutoJumpEnabled](/docs/reference/engine/classes/Humanoid.md) property of the
[Character](/docs/reference/engine/classes/Player.md) on spawn. In other words, it is
possible to set the auto-jump behavior on a per-character, per-player, and
per-experience basis using these three properties.

**Auto-Jump Toggle**

This code sample is meant for a TextButton. It allows the player to toggle the
auto-jumping behavior while on a mobile device.

```lua
local Players = game:GetService("Players")

local player = Players.LocalPlayer
local button = script.Parent

local function update()
	-- Update button text
	if player.AutoJumpEnabled then
		button.Text = "Auto-Jump is ON"
	else
		button.Text = "Auto-Jump is OFF"
	end
	-- Reflect the property in the player's character, if they have one
	if player.Character then
		local human = player.Character:FindFirstChild("Humanoid")
		if human then
			human.AutoJumpEnabled = player.AutoJumpEnabled
		end
	end
end

local function onActivated()
	-- Toggle auto-jump
	player.AutoJumpEnabled = not player.AutoJumpEnabled
	-- Update everything else
	update()
end

button.Activated:Connect(onActivated)
update()
```

### Property: Player.CameraMaxZoomDistance

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
  "category": "Camera",
  "capabilities": [
    "Players"
  ]
}
```

This property sets the maximum distance the player's camera is allowed to
zoom out, in studs.

The default value of this property is set by
[StarterPlayer.CameraMaxZoomDistance](/docs/reference/engine/classes/StarterPlayer.md). If this value is set to a
lower value than
[CameraMinZoomDistance](/docs/reference/engine/classes/Player.md), it will be
increased to [CameraMinZoomDistance](/docs/reference/engine/classes/Player.md).

### Property: Player.CameraMinZoomDistance

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
  "category": "Camera",
  "capabilities": [
    "Players"
  ]
}
```

This property sets the minimum distance the player's camera is allowed to
zoom in, in studs.

The default value of this property is set by
[StarterPlayer.CameraMinZoomDistance](/docs/reference/engine/classes/StarterPlayer.md). If this value is set to a
higher value than
[CameraMaxZoomDistance](/docs/reference/engine/classes/Player.md), it will be
decreased to [CameraMaxZoomDistance](/docs/reference/engine/classes/Player.md).

### Property: Player.CameraMode

```json
{
  "type": "CameraMode",
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
  "category": "Camera",
  "capabilities": [
    "Players"
  ]
}
```

This property sets the player's camera mode, defaulting to third person.

#### Third Person

In the default third person mode ([CameraMode.Classic](/docs/reference/engine/enums/CameraMode.md)), the
character can be seen in the camera. While in this mode, the default
behavior is:

- Players can right-click and drag (mouse), tap and drag (mobile), use the
  secondary thumbstick (gamepad), or press the left/right arrows
  (keyboard) to rotate the camera around their character.
- When a player moves their character, it faces in the corresponding
  movement direction.
- Players can zoom in and out freely, even to first person on full zoom
  in.

#### First Person

In first person mode ([CameraMode.LockFirstPerson](/docs/reference/engine/enums/CameraMode.md)), the player's
camera is zoomed all the way in. Unless there is a visible GUI present
with the [GuiButton.Modal](/docs/reference/engine/classes/GuiButton.md) property set to `true`, moving the mouse,
tap-dragging on mobile, or using the secondary thumbstick on a gamepad
will rotate the camera around the character.

**Playing in First Person**

This example demonstrates how to change the character's CameraMode to first
person using the LockFirstPerson value of the [CameraMode](/docs/reference/engine/enums/CameraMode.md) enum.

```lua
local Players = game:GetService("Players")

local player = Players.LocalPlayer

player.CameraMode = Enum.CameraMode.LockFirstPerson
```

### Property: Player.CanLoadCharacterAppearance

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
  "category": "Behavior",
  "capabilities": [
    "Players"
  ]
}
```

This property determines whether the character's appearance will be loaded
when the player spawns. The default value of this property is set by
[StarterPlayer.LoadPlayerAppearance](/docs/reference/engine/classes/StarterPlayer.md).

- If `true`, the character will load the appearance of the player
  corresponding to the player's
  [CharacterAppearanceId](/docs/reference/engine/classes/Player.md).

- If `false`, the player will spawn with a default appearance.

Attempting to set the property after the character has spawned will not
change the character; you must call
[LoadCharacterAsync()](/docs/reference/engine/classes/Player.md) to load the new
appearance.

### Property: Player.Character

```json
{
  "type": "Model",
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
    "Players"
  ]
}
```

This property contains a reference to a [Model](/docs/reference/engine/classes/Model.md) containing a
[Humanoid](/docs/reference/engine/classes/Humanoid.md), body parts, scripts, and other objects required for
simulating the player's avatar in-experience. The model is parented to the
[Workspace](/docs/reference/engine/classes/Workspace.md) but it may be moved. It is automatically loaded when
[Players.CharacterAutoLoads](/docs/reference/engine/classes/Players.md) is `true` and it can be manually loaded
otherwise using [LoadCharacterAsync()](/docs/reference/engine/classes/Player.md).

Initially this property is `nil` and it is set when the player's character
first spawns. Use the [CharacterAdded](/docs/reference/engine/classes/Player.md) event
to detect when a player's character properly loads, and the
[CharacterRemoving](/docs/reference/engine/classes/Player.md) event to detect when
the character is about to despawn. Avoid using
[Object:GetPropertyChangedSignal()](/docs/reference/engine/classes/Object.md) on this property.

Note that [LocalScripts](/docs/reference/engine/classes/LocalScript.md) that are cloned from
[StarterGui](/docs/reference/engine/classes/StarterGui.md) or [StarterPack](/docs/reference/engine/classes/StarterPack.md) into a player's
[PlayerGui](/docs/reference/engine/classes/PlayerGui.md) or [Backpack](/docs/reference/engine/classes/Backpack.md) respectively are often run before
the old character model is replaced, so [Player.Character](/docs/reference/engine/classes/Player.md) may refer
to the old model whose [Parent](/docs/reference/engine/classes/Instance.md) property is `nil`.
Therefore, in a [LocalScript](/docs/reference/engine/classes/LocalScript.md) under [StarterGui](/docs/reference/engine/classes/StarterGui.md) or
[StarterPack](/docs/reference/engine/classes/StarterPack.md), it is advisable to make sure the parent of
`Character` is not `nil` before using it, for example:

**Character**

Demonstrates [Player.Character](/docs/reference/engine/classes/Player.md).

```lua
local Players = game:GetService("Players")
local player = Players.LocalPlayer

local character = player.Character
if not character or character.Parent == nil then
	character = player.CharacterAdded:Wait()
end
```

### Property: Player.CharacterAppearanceId

```json
{
  "type": "int64",
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
    "Players"
  ]
}
```

This property determines the user ID of the account whose character
appearance is used for a player's [Character](/docs/reference/engine/classes/Player.md). By
default, this property is the [UserId](/docs/reference/engine/classes/Player.md), which uses the
player's avatar as they have created it on Roblox.

Changing this property to the user ID of another account will cause the
player to spawn with that account's appearance.

You can also toggle whether or not a player's character appearance is
loaded in experience by changing the
[StarterPlayer.LoadCharacterAppearance](/docs/reference/engine/classes/StarterPlayer.md) property.

### Property: Player.DevCameraOcclusionMode

```json
{
  "type": "DevCameraOcclusionMode",
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
  "category": "Camera",
  "capabilities": [
    "Players"
  ]
}
```

Defines how the default camera scripts handle objects between the camera
and the camera subject. Set by
[StarterPlayer.DevCameraOcclusionMode](/docs/reference/engine/classes/StarterPlayer.md) and can't be changed for
individual players.

The default value is [Zoom](/docs/reference/engine/enums/DevCameraOcclusionMode.md). See
[DevCameraOcclusionMode](/docs/reference/engine/enums/DevCameraOcclusionMode.md) for a list of available modes.

### Property: Player.DevComputerCameraMode

```json
{
  "type": "DevComputerCameraMovementMode",
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
  "category": "Camera",
  "capabilities": [
    "Players"
  ]
}
```

This property determines the manner in which a player moves their camera
when using a device with a mouse and keyboard. This property cannot be set
using a [LocalScript](/docs/reference/engine/classes/LocalScript.md) (it must be set on the server using a
[Script](/docs/reference/engine/classes/Script.md)).

The default value of this property is determined by
[StarterPlayer.DevComputerCameraMovementMode](/docs/reference/engine/classes/StarterPlayer.md).

This property doesn't affect players using a
[TouchEnabled](/docs/reference/engine/classes/UserInputService.md) device. See
[DevTouchCameraMode](/docs/reference/engine/classes/Player.md) instead.

### Property: Player.DevComputerMovementMode

```json
{
  "type": "DevComputerMovementMode",
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
  "category": "Control",
  "capabilities": [
    "Players"
  ]
}
```

This property determines the manner in which a player moves their
character when using a device with a mouse and keyboard. This property
cannot be set using a [LocalScript](/docs/reference/engine/classes/LocalScript.md) (it must be set on the server
using a [Script](/docs/reference/engine/classes/Script.md)).

The default value of this property is determined by
[StarterPlayer.DevComputerMovementMode](/docs/reference/engine/classes/StarterPlayer.md).

This property doesn't affect players using a
[TouchEnabled](/docs/reference/engine/classes/UserInputService.md) device. See
[DevTouchMovementMode](/docs/reference/engine/classes/Player.md) instead.

### Property: Player.DevEnableMouseLock

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
  "category": "Camera",
  "capabilities": [
    "Players"
  ]
}
```

This property determines if a player is able to toggle mouse lock by
pressing <kbd>Shift</kbd>. A player can disable the mouse lock switch in
the experience's settings during play. By default, this property is set to
the value of [StarterPlayer.EnableMouseLockOption](/docs/reference/engine/classes/StarterPlayer.md). This can be set
server-side during runtime by using a [Script](/docs/reference/engine/classes/Script.md). It can not be set
client-side.

When mouse lock is enabled, the player's cursor is locked to the center of
the screen. Moving the mouse will orbit the camera around the player's
[Character](/docs/reference/engine/classes/Player.md), and the character will face the same
direction as the [Camera](/docs/reference/engine/classes/Camera.md). It also offsets the camera view just over
the right shoulder of the player's character.

### Property: Player.DevTouchCameraMode

```json
{
  "type": "DevTouchCameraMovementMode",
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
  "category": "Camera",
  "capabilities": [
    "Players"
  ]
}
```

This property determines the manner in which a player moves their camera
when using a [TouchEnabled](/docs/reference/engine/classes/UserInputService.md) device.
This property cannot be set using a [LocalScript](/docs/reference/engine/classes/LocalScript.md) (it must be set on
the server using a [Script](/docs/reference/engine/classes/Script.md)).

The default value of this property is determined by
[StarterPlayer.DevTouchCameraMovementMode](/docs/reference/engine/classes/StarterPlayer.md).

This property doesn't affect players who aren't using a
[TouchEnabled](/docs/reference/engine/classes/UserInputService.md) device. See
[DevComputerCameraMode](/docs/reference/engine/classes/Player.md) instead.

### Property: Player.DevTouchMovementMode

```json
{
  "type": "DevTouchMovementMode",
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
  "category": "Control",
  "capabilities": [
    "Players"
  ]
}
```

This property determines the manner in which a player moves their
character when using a [TouchEnabled](/docs/reference/engine/classes/UserInputService.md)
device. This property cannot be set using a [LocalScript](/docs/reference/engine/classes/LocalScript.md) (it must
be set on the server using a [Script](/docs/reference/engine/classes/Script.md)).

The default value of this property is determined by
[StarterPlayer.DevTouchMovementMode](/docs/reference/engine/classes/StarterPlayer.md).

This property doesn't affect players who aren't using a
[TouchEnabled](/docs/reference/engine/classes/UserInputService.md) device. See
[DevComputerMovementMode](/docs/reference/engine/classes/Player.md) instead.

### Property: Player.DisplayName

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
  "category": "Data",
  "capabilities": [
    "Players"
  ]
}
```

This property contains the display name of the authenticated user
associated with the [Player](/docs/reference/engine/classes/Player.md) object. Unlike
[UserId](/docs/reference/engine/classes/Player.md), display names are non-unique names a player
displays to others.

#### Usage Notes

- Since display names are non-unique, it's possible for two players in a
  single instance to have identical names. If you need a globally unique
  identifier for a player, use [UserId](/docs/reference/engine/classes/Player.md) instead.

- Characters generated with
  [LoadCharacterAsync()](/docs/reference/engine/classes/Player.md) or by the
  Roblox engine will have their [Humanoid.DisplayName](/docs/reference/engine/classes/Humanoid.md) property
  assigned to the [Player.DisplayName](/docs/reference/engine/classes/Player.md) property.

- Display names may have unicode characters in the string. See
  [UTF-8](/docs/reference/engine/globals/utf8.md) for more information on how to work with strings
  with unicode characters.

### Property: Player.FollowUserId

```json
{
  "type": "int64",
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
    "Players"
  ]
}
```

This property contains the [UserId](/docs/reference/engine/classes/Player.md) of the user that a
player followed into the experience, or `0` if the player did not follow
anyone in. This property is useful for alerting players who have been
followed by another player into the experience.

You can get the name of the player followed using this user ID and the
[Players:GetNameFromUserIdAsync()](/docs/reference/engine/classes/Players.md) method.

**Followed Alert**

This code sample alerts players if a new player follows the local player into
the game. Place this in a [LocalScript](/docs/reference/engine/classes/LocalScript.md) in [StarterPlayerScripts](/docs/reference/engine/classes/StarterPlayerScripts.md).

```lua
local Players = game:GetService("Players")

local player = Players.LocalPlayer

local screenGui = Instance.new("ScreenGui")
screenGui.Parent = player:WaitForChild("PlayerGui")

local function onPlayerAdded(newPlayer)
	if newPlayer.FollowUserId == player.UserId then
		local textLabel = Instance.new("TextLabel")
		textLabel.Parent = screenGui
		textLabel.Text = "You were followed to this game by " .. newPlayer.Name .. "!"
		task.delay(3, function()
			if textLabel then
				textLabel:Destroy()
			end
		end)
	end
end

Players.PlayerAdded:Connect(onPlayerAdded)
```

### Property: Player.FrustumStreaming

```json
{
  "type": "FrustumStreamingMode",
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
    "Players"
  ]
}
```

This property controls the engine's instance streaming behavior for the
camera view of the given player. [Enabled](/docs/reference/engine/enums/FrustumStreamingMode.md) means
the player will always stream their camera view.
[Automatic](/docs/reference/engine/enums/FrustumStreamingMode.md) means the engine will decide to
stream the camera view based on the player's capability (based on the
bandwidth, device memory, etc.) and gameplay suitability.
[Disabled](/docs/reference/engine/enums/FrustumStreamingMode.md) means the player will never stream
their camera view. [Default](/docs/reference/engine/enums/FrustumStreamingMode.md) currently behaves
the same as [Disabled](/docs/reference/engine/enums/FrustumStreamingMode.md).

### Property: Player.HasRobloxSubscription

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "None",
    "write": "RobloxEngineSecurity"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Data",
  "capabilities": [
    "Players"
  ]
}
```

This read-only property is `true` when the player has an active Roblox
subscription (the flagship Roblox membership), and `false` otherwise. It
is set by the server and cannot be changed by scripts.

Use this property instead of [Player.MembershipType](/docs/reference/engine/classes/Player.md) to check for
the Roblox subscription.

**Check Roblox Subscription Status**

The following example checks whether a player has an active
[Roblox subscription](https://create.roblox.com/docs/production/monetization/roblox-plus)
and grants them a benefit if so.

```lua
local Players = game:GetService("Players")

local player = Players.LocalPlayer

if player.HasRobloxSubscription then
	-- Grant subscriber-exclusive content or perks
end
```

### Property: Player.HasVerifiedBadge

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
  "category": "Data",
  "capabilities": [
    "Players"
  ]
}
```

This property indicates if the player has a **Verified** badge.

### Property: Player.HealthDisplayDistance

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
  "category": "Camera",
  "capabilities": [
    "Players"
  ]
}
```

This property sets the distance in studs at which this player will see
other [Humanoid](/docs/reference/engine/classes/Humanoid.md) health bars. If set to `0`, the health bars will
not be displayed. This property is set to
[StarterPlayer.HealthDisplayDistance](/docs/reference/engine/classes/StarterPlayer.md) by default.

If a humanoid's health bar is visible, you can set the display type using
[Humanoid.DisplayDistanceType](/docs/reference/engine/classes/Humanoid.md).

### Property: Player.InputLatency

```json
{
  "type": "int",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxEngineSecurity",
    "write": "RobloxEngineSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Data",
  "capabilities": [
    "Players"
  ]
}
```

Latency used by the Server Authority netcode system. This property is not
accessible through scripts.

### Property: Player.MembershipType

```json
{
  "type": "MembershipType",
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
    "Players"
  ]
}
```

This property can only be read from to determine membership (it cannot be
set to another membership type). It holds a [MembershipType](/docs/reference/engine/enums/MembershipType.md) enum of
the account's membership type.

**Check Player Membership Status**

The following example checks whether a player has
[Premium](https://www.roblox.com/premium/membership) membership.

```lua
local Players = game:GetService("Players")

local player = Players.LocalPlayer

if player.MembershipType == Enum.MembershipType.Premium then
	-- Take some action specifically for Premium members
end
```

### Property: Player.NameDisplayDistance

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
  "category": "Camera",
  "capabilities": [
    "Players"
  ]
}
```

This property sets the distance in studs at which this player will see
other [Humanoid](/docs/reference/engine/classes/Humanoid.md) names. If the property is set to `0`, names are
hidden. This property is set to [StarterPlayer.NameDisplayDistance](/docs/reference/engine/classes/StarterPlayer.md)
by default.

If a humanoid's name is visible, you can set the display type using
[Humanoid.DisplayDistanceType](/docs/reference/engine/classes/Humanoid.md).

### Property: Player.Neutral

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
  "category": "Team",
  "capabilities": [
    "Players"
  ]
}
```

This property determines whether the player is on a specific team.

- When `true`, the player is not on a specific team. This also means that
  the [Team](/docs/reference/engine/classes/Player.md) property will be `nil` and the
  [TeamColor](/docs/reference/engine/classes/Player.md) will be white.

- When `false`, the player is on a specific team. The
  [Team](/docs/reference/engine/classes/Player.md) property will correspond to the [Team](/docs/reference/engine/classes/Team.md)
  that the player is on, as will the [TeamColor](/docs/reference/engine/classes/Player.md).

### Property: Player.ReplicationFocus

```json
{
  "type": "Instance",
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
    "Players"
  ]
}
```

This property sets the part to focus replication around a player.
Different Roblox systems that communicate over the network (such as
physics, streaming, etc.) replicate at different rates depending on how
close objects are to the replication focus.

When this property is `nil`, it reverts to its default behavior which is
to treat the local player's character's
[PrimaryPart](/docs/reference/engine/classes/Model.md) as the replication focus.

This property should only be set on the server with a [Script](/docs/reference/engine/classes/Script.md), not
a [LocalScript](/docs/reference/engine/classes/LocalScript.md). Note that this property does not change or update
network ownership of parts.

### Property: Player.RespawnLocation

```json
{
  "type": "SpawnLocation",
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
    "Players"
  ]
}
```

If set, the player will respawn at the given [SpawnLocation](/docs/reference/engine/classes/SpawnLocation.md) which
must meet the following criteria:

- Descendant of [Workspace](/docs/reference/engine/classes/Workspace.md).

- The [SpawnLocation.TeamColor](/docs/reference/engine/classes/SpawnLocation.md) property is set to the player's
  [TeamColor](/docs/reference/engine/classes/Player.md) or the [SpawnLocation.Neutral](/docs/reference/engine/classes/SpawnLocation.md)
  property is set to `true`.

#### Alternatives

- A [Player](/docs/reference/engine/classes/Player.md) will spawn from [SpawnLocations](/docs/reference/engine/classes/SpawnLocation.md)
  belonging to their team. In some cases it may be simpler to change the
  player's [Team](/docs/reference/engine/classes/Player.md) instead.
- Implement your own custom spawn logic using [PVInstance:PivotTo()](/docs/reference/engine/classes/PVInstance.md)
  to manually move the [Character](/docs/reference/engine/classes/Player.md).

**Change Spawn on Touch**

This code sample will set the player to always respawn from the last
SpawnLocation they touched. New players will respawn from the SpawnLocation
named 'FirstSpawn' until they touch a different SpawnLocation.

This is an alternative to using the AllowTeamChangeOnTouch property to switch
SpawnLocations and does not require Teams.

```lua
local Players = game:GetService("Players")

local function addSpawn(spawnLocation)
	-- listen for the spawn being touched
	spawnLocation.Touched:Connect(function(hit)
		local character = hit:FindFirstAncestorOfClass("Model")
		if character then
			local player = Players:GetPlayerFromCharacter(character)
			if player and player.RespawnLocation ~= spawnLocation then
				local humanoid = character:FindFirstChildOfClass("Humanoid")
				-- make sure the character isn't dead
				if humanoid and humanoid:GetState() ~= Enum.HumanoidStateType.Dead then
					print("spawn set")
					player.RespawnLocation = spawnLocation
				end
			end
		end
	end)
end

local firstSpawn

-- look through the workspace for spawns
for _, descendant in pairs(workspace:GetDescendants()) do
	if descendant:IsA("SpawnLocation") then
		if descendant.Name == "FirstSpawn" then
			firstSpawn = descendant
		end
		addSpawn(descendant)
	end
end

local function playerAdded(player)
	player.RespawnLocation = firstSpawn
end

-- listen for new players
Players.PlayerAdded:Connect(playerAdded)

-- go through existing players
for _, player in pairs(Players:GetPlayers()) do
	playerAdded(player)
end
```

### Property: Player.Team

```json
{
  "type": "Team",
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
  "category": "Team",
  "capabilities": [
    "Players"
  ]
}
```

This property is a reference to a [Team](/docs/reference/engine/classes/Team.md) object within the
[Teams](/docs/reference/engine/classes/Teams.md) service. If the player isn't on a team or has an invalid
[TeamColor](/docs/reference/engine/classes/Player.md), this property is `nil`. When this
property is set, the player has joined the [Team](/docs/reference/engine/classes/Team.md) and the
[Team.PlayerAdded](/docs/reference/engine/classes/Team.md) event fires on the associated team. Similarly,
[Team.PlayerRemoved](/docs/reference/engine/classes/Team.md) fires when the property is unset from a certain
[Team](/docs/reference/engine/classes/Team.md).

### Property: Player.TeamColor

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
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Team",
  "capabilities": [
    "Players"
  ]
}
```

This property determines which [Team](/docs/reference/engine/classes/Team.md) a player is associated with
according to that team's [Team.TeamColor](/docs/reference/engine/classes/Team.md). If no [Team](/docs/reference/engine/classes/Team.md) object
has the associated [BrickColor](/docs/reference/engine/datatypes/BrickColor.md), the player will not be
associated with a team.

It's often a better idea to set [Player.Team](/docs/reference/engine/classes/Player.md) to the respective
[Team](/docs/reference/engine/classes/Team.md) instead of using this property. Setting this property often
leads to repetition of the same [BrickColor](/docs/reference/engine/datatypes/BrickColor.md) value for a certain
team across many scripts.

### Property: Player.ThirdPartyTextChatRestrictionStatus

```json
{
  "type": "ChatRestrictionStatus",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": false,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Data",
  "capabilities": [
    "Players"
  ]
}
```

This read-only property holds the [ChatRestrictionStatus](/docs/reference/engine/enums/ChatRestrictionStatus.md) that a
third-party platform (for example, a console platform's parental or
communication settings) reports for the player's text chat. The default
value is [ChatRestrictionStatus.Unknown](/docs/reference/engine/enums/ChatRestrictionStatus.md).

This property cannot be set from scripts.

### Property: Player.User

```json
{
  "type": "User",
  "access": "ReadOnly",
  "security": {
    "read": "None",
    "write": "RobloxEngineSecurity"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Data",
  "capabilities": [
    "Players"
  ]
}
```

A read-only [User](/docs/reference/engine/datatypes/User.md) value that represents this player's
domain-scoped identity within the current experience. The [User](/docs/reference/engine/datatypes/User.md)
encapsulates the player's domain user ID alongside the domain type and
domain ID, providing an unambiguous identifier that carries its context.

Use this property as the standard way to identify users in new code.
Engine APIs that accept user ID parameters also accept [User](/docs/reference/engine/datatypes/User.md)
values directly.

**User**

Demonstrates [Player.User](/docs/reference/engine/classes/Player.md).

```lua
local Players = game:GetService("Players")

Players.PlayerAdded:Connect(function(player)
    local user = player.User
    print("Domain user ID:", user.Id)
    print("Domain type:", user.DomainType)
    print("Domain ID:", user.DomainId)
end)
```

### Property: Player.UserId

```json
{
  "type": "int64",
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
    "Players"
  ]
}
```

This property contains a read-only integer that **uniquely and
consistently** identifies the user's account on Roblox. Unlike the
player's [DisplayName](/docs/reference/engine/classes/Player.md) which may change, this
value will never change for the same account.

This property is essential when saving/loading player data using
[GlobalDataStores](/docs/reference/engine/classes/GlobalDataStore.md).

**Player.UserId**

The below example would print the UserId of every user who entered a game.

```lua
local Players = game:GetService("Players")

local function onPlayerAdded(player)
	print(player.UserId)
end

Players.PlayerAdded:Connect(onPlayerAdded)
```

**Data Store to Leaderboard**

This code sample retrieves a player's saved gold from a data store and puts
the returned value onto the leaderboard. Note that this sample does not save
players' gold&nbsp;&mdash; it only loads it.

```lua
local Players = game:GetService("Players")
local DataStoreService = game:GetService("DataStoreService")

local goldDataStore = DataStoreService:GetDataStore("Gold")

local STARTING_GOLD = 100

local function onPlayerAdded(player)
	local playerKey = "Player_" .. player.UserId

	local leaderstats = Instance.new("IntValue")
	leaderstats.Name = "leaderstats"

	local gold = Instance.new("IntValue")
	gold.Name = "Gold"
	gold.Parent = leaderstats

	local success, result = pcall(function()
		return goldDataStore:GetAsync(playerKey) or STARTING_GOLD
	end)
	if success then
		gold.Value = result
	else
		-- Failed to retrieve data
		warn(result)
	end

	leaderstats.Parent = player
end

Players.PlayerAdded:Connect(onPlayerAdded)
```

### Property: Player.CharacterAppearance

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
  "deprecated": true,
  "thread_safety": "ReadSafe",
  "category": "Data",
  "capabilities": [
    "Players"
  ]
}
```

> **Deprecated:** This item is deprecated. Do not use it for new work.

This property indicates the URL of the asset containing the character's
appearance, clothing, and gear. It is automatically set by Roblox to load
your avatar's appearance when you join an experience.

Attempting to set the property after the character has spawned will not
change the character, you must call
[LoadCharacterAsync()](/docs/reference/engine/classes/Player.md) to load the new
appearance.

### Property: Player.userId

```json
{
  "type": "int64",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "deprecated": true,
  "thread_safety": "ReadSafe",
  "category": "Data",
  "capabilities": [
    "Players"
  ]
}
```

> **Deprecated:** This property is a deprecated variant of [Player.UserId](/docs/reference/engine/classes/Player.md) which should be used instead.

### Property: Player.DataComplexity *(hidden)*

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
  "deprecated": true,
  "thread_safety": "ReadSafe",
  "category": "Data",
  "capabilities": [
    "Players"
  ]
}
```

> **Deprecated:** This item is deprecated, as it may have been used for a now obsolete data persistence method. Please save and load player data using [DataStoreService](/docs/reference/engine/classes/DataStoreService.md) for new work.

This property was once used by an ancient data persistence method to
indicate the total amount of data currently being stored in the player's
cache on the current place.

#### Notes

- Booleans and numbers cost 1 data complexity unit.
- Strings cost their length divided by 100 in data complexity units.
- Instances cost their DataCost in data complexity units.
- Saving the default value (0 for numbers, false for booleans, "" for
  strings and `nil` for Instances) removes the key from the DataComplexity
  count.
- If, when using the SaveBoolean, SaveString, SaveNumber or SaveInstance
  functions, the DataComplexity for the player goes over the limit
  (currently 45000 units, defined by DataComplexityLimit), the function
  throws an error, the value is not saved, and any previous value of the
  key that was being saved to is deleted.

### Property: Player.DataReady *(hidden)*

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
  "deprecated": true,
  "thread_safety": "ReadSafe",
  "category": "Data",
  "capabilities": [
    "Players"
  ]
}
```

> **Deprecated:** This item is deprecated, as it may have been used for a now obsolete data persistence method. Please save and load player data using [DataStoreService](/docs/reference/engine/classes/DataStoreService.md) for new work.

This property was once used by an ancient data persistence method to
indicate when the player's data is available to load. Becomes true when
data is available.

### Property: Player.DeviceTrustLevel *(hidden)*

```json
{
  "type": "PlayerDeviceTrustLevel",
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
    "Players",
    "Consequences"
  ]
}
```

This read-only property holds the [PlayerDeviceTrustLevel](/docs/reference/engine/enums/PlayerDeviceTrustLevel.md) of the
player's device, as outlined in
[device trust](/docs/en-us/scripting/security/device-trust.md). Use it on the
server to restrict sensitive features, such as trading or ranked play, to
players on trusted devices.

Every player starts at [PlayerDeviceTrustLevel.Pending](/docs/reference/engine/enums/PlayerDeviceTrustLevel.md) and the
property changes once when the trust level becomes available. This happens
after [Players.PlayerAdded](/docs/reference/engine/classes/Players.md) fires and before
[IntegrityService.EvaluatePlayerDeviceTrust](/docs/reference/engine/classes/IntegrityService.md) is called. If Roblox
can't finish checking a device, the property might stay at
[Pending](/docs/reference/engine/enums/PlayerDeviceTrustLevel.md) for the whole session.
Roblox doesn't check devices in Studio, so the property always stays at
[Pending](/docs/reference/engine/enums/PlayerDeviceTrustLevel.md) during playtests, a level
which should never be trusted enough for sensitive features.

Only the server and the player's own client can read the player's trust
level. Every other client sees
[Pending](/docs/reference/engine/enums/PlayerDeviceTrustLevel.md), so make trust decisions on
the server.

The device trust level describes the player's device, not the player or
their account. **It doesn't tell you whether a player is cheating.** For
code samples, see
[device trust](/docs/en-us/scripting/security/device-trust.md).

### Property: Player.GameplayPaused *(hidden)*

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "None",
    "write": "NotAccessibleSecurity"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Behavior",
  "capabilities": [
    "Players"
  ]
}
```

This property indicates if the player is currently in a pause state in a
place with [StreamingEnabled](/docs/reference/engine/classes/Workspace.md) activated.
It is set on the client but replicated to the server.

#### See Also

- [Workspace.StreamingEnabled](/docs/reference/engine/classes/Workspace.md) which controls whether content
  streaming is enabled
- [Workspace.StreamingIntegrityMode](/docs/reference/engine/classes/Workspace.md) and
  [StreamingIntegrityMode](/docs/reference/engine/enums/StreamingIntegrityMode.md) for more details on when gameplay is
  paused.

### Property: Player.LocaleId *(hidden)*

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
  "category": "Data",
  "capabilities": [
    "Players"
  ]
}
```

This property shows the locale ID that the local player has set for their
Roblox account. It holds a string with the two letter code, for example
`en-us`.

See also [LocalizationService.RobloxLocaleId](/docs/reference/engine/classes/LocalizationService.md), the locale ID used
for localizing internal content. This can be a different value when the
player's account locale isn't supported for internal content localization.

### Property: Player.PartyId *(hidden)*

```json
{
  "type": "string",
  "access": "ReadOnly",
  "security": {
    "read": "None",
    "write": "RobloxEngineSecurity"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Data",
  "capabilities": [
    "Players"
  ]
}
```

A read-only string identifying the party the player currently belongs to
within the experience. If the player is not in a party, this value is an
empty string.

This property is essential for integrating with the Roblox Party feature.
Use it in combination with [SocialService:GetPlayersByPartyId()](/docs/reference/engine/classes/SocialService.md) and
[SocialService:GetPartyAsync()](/docs/reference/engine/classes/SocialService.md) to access information about a
player's party and its members.

To test this service in your experience, use the
[Party Simulator](/docs/en-us/studio/testing-modes.md#party-simulation) in
Roblox Studio or publish the experience and play it in the Roblox
application.

**Player.PartyId**

This example checks the [Player.PartyId](/docs/reference/engine/classes/Player.md) of a [Player](/docs/reference/engine/classes/Player.md) when they
join the experience. If the player is in a party, it outputs the
[Player.PartyId](/docs/reference/engine/classes/Player.md); otherwise, it outputs that the player is not in a
party.

```lua
local Players = game:GetService("Players")

Players.PlayerAdded:Connect(function(player)
	local partyId = player.PartyId

	if partyId ~= "" then
		print("Player is in a party with ID: " .. partyId)
	else
		print("Player is not in a party")
	end

	player:GetPropertyChangedSignal("PartyId"):Connect(function()
		if player.PartyId ~= "" then
			print("Player joined party with ID: " .. player.PartyId)
		else
			print("Player left party")
		end
	end)
end)
```

## Methods

### Method: Player:AddReplicationFocus

**Signature:** `Player:AddReplicationFocus(part: BasePart): ()`

This method adds an additional replication focus for the player in order
to trigger streaming around the location of the specified `part`. In this
manner, streaming can occur around multiple locations, not just the
location of [Player.ReplicationFocus](/docs/reference/engine/classes/Player.md). This has no effect in
experiences that are not streaming enabled.

Additional foci will use the same values of
[Workspace.StreamingMinRadius](/docs/reference/engine/classes/Workspace.md) and
[Workspace.StreamingTargetRadius](/docs/reference/engine/classes/Workspace.md) as are used by the primary focus.

This method should only be called on the server. It has no effect when
called from a [LocalScript](/docs/reference/engine/classes/LocalScript.md).

*Security: None · Thread Safety: Unsafe · Capabilities: Players*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `part` | `BasePart` |  | The [BasePart](/docs/reference/engine/classes/BasePart.md) to use as a new replication focus. |

**Returns:** `()`

### Method: Player:ClearCachedAvatarAppearance

**Signature:** `Player:ClearCachedAvatarAppearance(): ()`

This method clears the cached avatar appearance for the player. The next
time [LoadCharacterAsync()](/docs/reference/engine/classes/Player.md) is called
with the player's default platform appearance, a fresh version will be
fetched from the backend instead of using the cached version.

Avatar appearance is cached after the first load to improve respawn
latency and reduce backend load; most players do not change their avatar
mid-session. Call this method when you want to reflect a change the player
has made to their avatar outside of the experience, for example to
implement a custom refresh button that mirrors the behavior of the default
in-experience menu.

*Security: None · Thread Safety: Unsafe · Capabilities: AvatarAppearance, Players*

**Returns:** `()`

### Method: Player:ClearCharacterAppearance

**Signature:** `Player:ClearCharacterAppearance(): ()`

This method removes all [Accessory](/docs/reference/engine/classes/Accessory.md), [Shirt](/docs/reference/engine/classes/Shirt.md), [Pants](/docs/reference/engine/classes/Pants.md),
[CharacterMesh](/docs/reference/engine/classes/CharacterMesh.md), and [BodyColors](/docs/reference/engine/classes/BodyColors.md) from the given player's
[Character](/docs/reference/engine/classes/Player.md). In addition, it also removes the
T-Shirt [Decal](/docs/reference/engine/classes/Decal.md) on the player's torso. The character's body part
colors and face will remain unchanged. This method does nothing if the
player does not have a [Character](/docs/reference/engine/classes/Player.md).

*Security: None · Thread Safety: Unsafe · Capabilities: Players*

**Returns:** `()`

**How to Clear a Character's Appearance**

```lua
local Players = game:GetService("Players")

local player = Players.LocalPlayer

local character = player.Character or player.CharacterAdded:Wait()

local function onChildRemoved(child)
	print(child.ClassName, "removed from character")
end

character.ChildRemoved:Connect(onChildRemoved)

player:ClearCharacterAppearance()
--> BodyColors removed from character
--> ShirtGraphic removed from character
--> Shirt removed from character
--> Pants removed from character
--> CharacterMesh removed from character
--> Hat removed from character
--> Shirt removed from character
```

### Method: Player:DistanceFromCharacter

**Signature:** `Player:DistanceFromCharacter(point: Vector3): float`

This method returns the distance between the character's head and the
given [Vector3](/docs/reference/engine/datatypes/Vector3.md) point, or `0` if the player has no
[Character](/docs/reference/engine/classes/Player.md).

This is useful when determining the distance between a player and another
object or location in experience.

If you would like to determine the distance between two non-player
instances or positions, you can use the following:

*Security: None · Thread Safety: Unsafe · Capabilities: Players*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `point` | `Vector3` |  | The location from which player's distance to is being measured. |

**Returns:** `float` — The distance in studs between the player and the location.

**Measuring the Distance Between a Player and a Position**

This example demonstrates how to measure the distance between a player's
[Player.Character](/docs/reference/engine/classes/Player.md) and another location.

This code will print the distance of each player's character from the origin
(0, 0, 0):

```lua
local Players = game:GetService("Players")

for _, player in pairs(Players:GetPlayers()) do
	print(player:DistanceFromCharacter(Vector3.new(0, 0, 0)))
end
```

**Distance From Character**

Demonstrates [Player:DistanceFromCharacter()](/docs/reference/engine/classes/Player.md).

```lua
local position1 = Vector3.new(0, 0, 0)
local position2 = Vector3.new(0, 10, 0)

local distance = (position1 - position2).Magnitude
```

### Method: Player:GetCameraState

**Signature:** `Player:GetCameraState(): CameraState`

Returns a dictionary containing information about the player's current
camera state. This method requires
[Server Authority](/docs/en-us/projects/server-authority.md) to be enabled in
the game. The dictionary contains the following fields:

| Key | Value Type | Description |
| --- | --- | --- |
| `CFrame` | [CFrame](/docs/reference/engine/datatypes/CFrame.md) | The current [CFrame](/docs/reference/engine/classes/Camera.md) of the player's camera. |
| `FieldOfView` | number | The current [FieldOfView](/docs/reference/engine/classes/Camera.md) of the player's camera in degrees. |
| `ViewportSize` | [Vector2](/docs/reference/engine/datatypes/Vector2.md) | The current [ViewportSize](/docs/reference/engine/classes/Camera.md) of the player's camera in pixels. |

On the client, this method can only be called on the
[Players.LocalPlayer](/docs/reference/engine/classes/Players.md). On the server, it can be called on any
[Player](/docs/reference/engine/classes/Player.md) object to retrieve their replicated camera state. Typical
server-side uses include aim and look-direction logic in
server-authoritative gameplay, and camera-aware content streaming.

The `CFrame` field is replicated as part of the player's input stream,
meaning it is synchronized with other inputs such as movement and actions.
The `FieldOfView` and `ViewportSize` fields use standard client-to-server
property replication which is not synchronized with input and may update
at a different cadence.

*Security: None · Thread Safety: Safe · Capabilities: Players · Simulation Access: true*

**Returns:** `CameraState` — A dictionary containing [CFrame](/docs/reference/engine/classes/Camera.md),
[FieldOfView](/docs/reference/engine/classes/Camera.md), and
[ViewportSize](/docs/reference/engine/classes/Camera.md) values.

**Get Camera State**

Demonstrates [Player:GetCameraState()](/docs/reference/engine/classes/Player.md).

```lua
local Players = game:GetService("Players")

local player = Players.LocalPlayer
local cameraState = player:GetCameraState()

print(cameraState.CFrame)
print(cameraState.FieldOfView)
print(cameraState.ViewportSize)
```

### Method: Player:GetFriendsOnlineAsync

**Signature:** `Player:GetFriendsOnlineAsync(maxFriends?: int): Array`

This function returns a dictionary array of online friends, using a 30
second cache. In the returned array, some fields are only present for
certain location types; for example, `PlaceId` won't be present when
`LocationType` is `0` (mobile website).

| Name | Type | Description |
| --- | --- | --- |
| `VisitorId` | number | The [UserId](/docs/reference/engine/classes/Player.md) of the friend. |
| `UserName` | string | The username of the friend. |
| `DisplayName` | string | The [DisplayName](/docs/reference/engine/classes/Player.md) of the friend. |
| `LastOnline` | string | When the friend was last online. |
| `IsOnline` | boolean | If the friend is currently online. |
| `LastLocation` | string | The name of the friend's current location. |
| `PlaceId` | number | The place ID of the friend's last location. |
| `GameId` | string | The [DataModel.JobId](/docs/reference/engine/classes/DataModel.md) of the friend's last location. |
| `LocationType` | number | The location type of the friend's last location. |

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Players, Social*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `maxFriends` | `int` | `200` | The maximum number of online friends to return. |

**Returns:** `Array` — A dictionary of online friends (see the table above).

**Get a List of Online Connections**

This example demonstrates how to get a dictionary of a player's online
friends. It returns the maximum number of friends specified by the argument,
or 200 if an argument is not provided.

```lua
local Players = game:GetService("Players")

local player = Players.LocalPlayer

local success, result = pcall(player.GetFriendsOnlineAsync, player, 10)

if success then
	for _, friend in pairs(result) do
		print(friend.UserName)
	end
else
	warn("Failed to get online players: " .. result)
end
```

### Method: Player:GetFriendsWhoPlayedAsync

**Signature:** `Player:GetFriendsWhoPlayedAsync(): Array`

Returns an array of user IDs of any friends who have previously played
this game. For example, if a player has had two friends play the game, the
method might return `{1111111111, 2222222222}`. If no friends have played
this game, the method returns an empty array (`{}`).

This is particularly useful for friend leaderboards: by narrowing
DataStore lookups to only friends who have actually played the experience,
you avoid fetching scores for the entire friends list and reduce the risk
of hitting DataStore rate limits.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Players, Social*

**Returns:** `Array` — An array of user IDs.

### Method: Player:GetJoinData

**Signature:** `Player:GetJoinData(): Dictionary`

Returns a dictionary containing information describing how the player
joins the experience. The dictionary contains any of the following fields:

| Key | Value Type | Description |
| --- | --- | --- |
| `SourceGameId` | number | The [DataModel.GameId](/docs/reference/engine/classes/DataModel.md) of the experience the `Player` teleported from. Only present if the player teleports to the current experience and if a server calls the teleport function. |
| `SourcePlaceId` | number | The [DataModel.PlaceId](/docs/reference/engine/classes/DataModel.md) of the place the `Player` teleported from. Only present if the player teleports to the current place and a server calls the teleport function. |
| `ReferredByPlayerId` | number | The [UserId](/docs/reference/engine/classes/Player.md) of the player who invited the current player to the experience. Use this data to identify the referrer and trigger reward logic. |
| `Members` | array | An array containing the [UserId](/docs/reference/engine/classes/Player.md) numbers of the users teleported alongside the player. Only present if the player teleported as part of a group. |
| `TeleportData` | variant | Reflects the `teleportData` specified in the original teleport. Useful for sharing information between servers the player teleports to. Only present if `teleportData` was specified and a server calls the teleport function. |
| `LaunchData` | string | A plain or JSON encoded string that contains launch data specified in a [share link](/docs/en-us/production/promotion/share-links.md) or [ExperienceInviteOptions.LaunchData](/docs/reference/engine/classes/ExperienceInviteOptions.md). |
| `GameJoinContext` | dictionary | A dictionary that includes relevant information based on the context of the join. It contains the following keys:

<ul><li>`JoinSource`: [JoinSource](/docs/reference/engine/enums/JoinSource.md)</li><li>`ItemType`: optional [AvatarItemType](/docs/reference/engine/enums/AvatarItemType.md)</li><li>`AssetId`: optional `string`</li><li>`OutfitId`: optional `string`</li><li>`AssetType`: optional [AssetType](/docs/reference/engine/enums/AssetType.md)</li></ul> |

If a server initiates the player's teleport, the dictionary that this
method returns includes the player's teleport data. The
[GetJoinData()](/docs/reference/engine/classes/Player.md) method can only be used to
fetch teleport data on the server. To fetch the data on the client, use
[TeleportService:GetLocalPlayerTeleportData()](/docs/reference/engine/classes/TeleportService.md).

Unlike [TeleportService:GetLocalPlayerTeleportData()](/docs/reference/engine/classes/TeleportService.md),
[GetJoinData()](/docs/reference/engine/classes/Player.md) only provides teleport data
that meets the following security criteria:

- It's guaranteed to have been sent by a Roblox server in the past 48
  hours.
- It's guaranteed to have been sent with this [Player](/docs/reference/engine/classes/Player.md).
- The `SourcePlaceId` and `SourceGameId` are guaranteed to be the place
  and universe the data was sent from. This means you can verify the
  teleport data came from an approved place.

As this data is transmitted by the client, it can still potentially be
abused by an exploiter. Sensitive data such as player currency should be
transmitted via a secure solution like
[Memory Stores](/docs/en-us/cloud-services/memory-stores.md).

*Security: None · Thread Safety: Unsafe · Capabilities: Players*

**Returns:** `Dictionary` — A dictionary containing PlaceId and UserId values (see table in
description).

**Tracking Traffic Sources**

The following example tracks sources of traffic for analytics. By creating
URLs with unique launch data for each social platform, you can determine the
most popular traffic sources. The sample checks the source against a list of
possible samples and discards any invalid sources because users can modify the
launch data.

```lua
local DataStoreService = game:GetService("DataStoreService")
local Players = game:GetService("Players")

local analyticsStore = DataStoreService:GetDataStore("Analytics")

local ALLOWED_SOURCES = {
	"twitter",
	"youtube",
	"discord",
}

local function onPlayerAdded(player)
	local source = player:GetJoinData().LaunchData
	-- check if the provided source is valid
	if source and table.find(ALLOWED_SOURCES, source) then
		-- update the data store to track the source popularity
		local success, result = pcall(analyticsStore.IncrementAsync, analyticsStore, source)

		if success then
			print(player.Name, "joined from", source, "- total:", result)
		else
			warn("Failed to record join source: " .. result)
		end
	end
end

Players.PlayerAdded:Connect(onPlayerAdded)
```

**Referral URL Generator**

The following example generates a URL with the user's ID used as launch data.
It then displays the URL in a read-only text box that makes it easy for the
user to copy and share the link with their friends. When a user joins the game
using a referral link, you can use the launch data to reward the referrer.

```lua
local Players = game:GetService("Players")

local player = Players.LocalPlayer

local DIRECT_JOIN_URL = "https://www.roblox.com/games/start?placeId=%d&launchData=%s"

local textBox = script.Parent

local function generateReferralURL(player)
	return DIRECT_JOIN_URL:format(game.PlaceId, player.UserId)
end

local function highlightAll()
	if -- avoid recursive property updates
		textBox:IsFocused() and not (textBox.SelectionStart == 1 and textBox.CursorPosition == #textBox.Text + 1)
	then
		textBox.SelectionStart = 1
		textBox.CursorPosition = #textBox.Text + 1
	end
end

textBox.Focused:Connect(highlightAll)
textBox:GetPropertyChangedSignal("SelectionStart"):Connect(highlightAll)
textBox:GetPropertyChangedSignal("CursorPosition"):Connect(highlightAll)

textBox.TextEditable = false
textBox.ClearTextOnFocus = false

textBox.Text = generateReferralURL(player)
```

**Using a Table as Launch Data**

The following example is a function that converts a table into a string you
can use as launch data. The provided data is JSON encoded, checked for valid
character length, and escaped with percent signs.

```lua
local HttpService = game:GetService("HttpService")

local DATA_CHARACTER_LIMIT = 200

local function encodeTableAsLaunchData(data)
	-- convert the table to a string
	local jsonEncodedData = HttpService:JSONEncode(data)

	if #jsonEncodedData <= DATA_CHARACTER_LIMIT then
		-- escape potentially invalid characters, such as spaces
		local urlEncodedData = HttpService:UrlEncode(jsonEncodedData)
		return true, urlEncodedData
	else
		-- report character limit error
		return false, ("Encoded table exceeds %d character limit"):format(DATA_CHARACTER_LIMIT)
	end
end

local sampleData = {
	joinMessage = "Hello!",
	urlCreationDate = os.time(),
	magicNumbers = {
		534,
		1337,
		746733573,
	},
}

local success, encodedData = encodeTableAsLaunchData(sampleData)

if success then
	print(encodedData)
else
	warn("failed to encode launch data: " .. encodedData)
end
```

**Decoding JSON Launch Data**

The following example attempts to decode launch data, using `pcall` to prevent
an error in case the data is corrupt.

```lua
local HttpService = game:GetService("HttpService")
local Players = game:GetService("Players")

local function onPlayerAdded(player)
	local launchData = player:GetJoinData().LaunchData
	if launchData then
		-- attempt to decode the data
		local success, result = pcall(HttpService.JSONDecode, HttpService, launchData)
		if success then
			print(player.Name, "joined with data:", result)
		else
			-- this is probably due to the user messing with the URL
			warn("Failed to parse launch data:" .. result)
		end
	end
end

Players.PlayerAdded:Connect(onPlayerAdded)
```

**Server TeleportData Example**

The following code sample is an example of how teleport data can be retrieved
on the server using [Player:GetJoinData()](/docs/reference/engine/classes/Player.md). This code, when ran in a
`Script` in `ServerScriptService`, will listen for new `Player|Players`
joining the game. When they join it will retrieve their teleport data
(verifying it came from a valid place) to find their current level.

```lua
local Players = game:GetService("Players")

local approvedPlaceIds = { 1 } -- insert approved PlaceIds here

local function isPlaceIdApproved(placeId)
	for _, id in pairs(approvedPlaceIds) do
		if id == placeId then
			return true
		end
	end
	return false
end

local function onPlayerAdded(player)
	local joinData = player:GetJoinData()

	-- verify this data was sent by an approved place
	if isPlaceIdApproved(joinData.SourcePlaceId) then
		local teleportData = joinData.TeleportData
		if teleportData then
			local currentLevel = teleportData.currentLevel
			print(player.Name .. " is on level " .. currentLevel)
		end
	end
end

Players.PlayerAdded:Connect(onPlayerAdded)
```

### Method: Player:GetMouse

**Signature:** `Player:GetMouse(): Mouse`

This method returns the [Mouse](/docs/reference/engine/classes/Mouse.md) being used by the client. The
player's mouse instance can be used to track user mouse input including
left and right mouse button clicks and movement and location.

Note that [UserInputService](/docs/reference/engine/classes/UserInputService.md) provides additional methods,
properties, and events to track user input, especially for devices that do
not use a mouse.

*Security: None · Thread Safety: Unsafe · Capabilities: Input, Players*

**Returns:** `Mouse` — The player's [Mouse](/docs/reference/engine/classes/Mouse.md) instance.

### Method: Player:GetNetworkPing

**Signature:** `Player:GetNetworkPing(): float`

Returns the round-trip, isolated network latency of the player in seconds.
"Ping" is a measurement of the time taken for data to be sent from the
client to the server, then back again. It doesn't involve data
deserialization or processing.

For client-side [LocalScripts](/docs/reference/engine/classes/LocalScript.md), this function can only
be called on the [Players.LocalPlayer](/docs/reference/engine/classes/Players.md). This function is useful in
identifying and debugging issues that occur in high network latency
scenarios. It's also useful for masking latency, such as adjusting the
speed of throwing animations for projectiles.

*Security: None · Thread Safety: Safe · Capabilities: Players*

**Returns:** `float` — The round-trip network latency of the player in seconds.

### Method: Player:HasAppearanceLoaded

**Signature:** `Player:HasAppearanceLoaded(): boolean`

This method returns whether or not the appearance of the player's
[Character](/docs/reference/engine/classes/Player.md) has loaded. Appearance includes items
such as the player's [Shirt](/docs/reference/engine/classes/Shirt.md), [Pants](/docs/reference/engine/classes/Pants.md), and
[Accessories](/docs/reference/engine/classes/Accessory.md).

This is useful when determining whether a player's appearance has loaded
after they first join the experience, which can be tracked using the
[Players.PlayerAdded](/docs/reference/engine/classes/Players.md) event.

*Security: None · Thread Safety: Unsafe · Capabilities: Players*

**Returns:** `boolean` — A boolean indicating whether or not the appearance of the player's
character has loaded.

**Check if a Player's Appearance Has Loaded**

This example prints the result of [Player:HasAppearanceLoaded()](/docs/reference/engine/classes/Player.md) after a
player joins the game until the player's appearance has loaded.

```lua
local Players = game:GetService("Players")

local function onPlayerAdded(player)
	local loaded = player:HasAppearanceLoaded()
	print(loaded)

	while not loaded do
		loaded = player:HasAppearanceLoaded()
		print(loaded)
		task.wait()
	end
end

Players.PlayerAdded:Connect(onPlayerAdded)
```

### Method: Player:IsFriendsWithAsync

**Signature:** `Player:IsFriendsWithAsync(userId: User): boolean`

This method sends a request to Roblox asking whether a player is a friend
of another user, given the [UserId](/docs/reference/engine/classes/Player.md) of that user. This
method caches results so multiple calls on the same player with the same
`userId` may not yield the most up-to-date result.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Players, Social*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `userId` | `User` |  | The [Player.UserId](/docs/reference/engine/classes/Player.md) of the specified player. |

**Returns:** `boolean` — A boolean indicating whether a player is a friend of the specified
user.

### Method: Player:IsInGroupAsync

**Signature:** `Player:IsInGroupAsync(groupId: int64): boolean`

This method sends a request to Roblox asking whether a player is a member
of a group, given the ID of that group.

This call may not yield the most up-to-date information. If a player
leaves a group while they are in the experience, `IsInGroupAsync()` will
still think they're in that group until they leave. However, this does not
happen when used with a [LocalScript](/docs/reference/engine/classes/LocalScript.md) because the method caches
results, so multiple calls of `IsInGroupAsync()` on the same player with
the same group ID will yield the same result as when the method was first
called with the given group ID. The caching behavior is on a per-peer
basis: a server does not share the same cache as a client.

When a player joins a group in-experience due to a call to
[GroupService:PromptJoinAsync()](/docs/reference/engine/classes/GroupService.md), any cached value for that player
will be cleared on the client where the prompt was shown.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Players, Groups*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `groupId` | `int64` |  | The group ID of the specified group. |

**Returns:** `boolean` — A boolean indicating whether the player is in the specified group.

### Method: Player:IsVerified

**Signature:** `Player:IsVerified(level?: VerifiedLevel): boolean`

Returns a boolean value indicating whether the player meets the specified
[VerifiedLevel](/docs/reference/engine/enums/VerifiedLevel.md). When `level` is omitted, this method defaults to
[VerifiedLevel.Low](/docs/reference/engine/enums/VerifiedLevel.md). Note that this is a distinct check from the
verified badge.

Verification uses concrete, real-world signals, including, but not limited
to, phone number or government ID verification.

When implementing `IsVerified`, exercise caution to ensure that the
implementation does not inadvertently block all unverified users.

Note that the method can only be called on the backend server. Calling it
client-side results in an error. Additionally, this method will always
return `false` in Studio.

*Security: None · Thread Safety: Unsafe · Capabilities: Players*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `level` | `VerifiedLevel` | `Low` | The verification level to check. Defaults to [VerifiedLevel.Low](/docs/reference/engine/enums/VerifiedLevel.md). |

**Returns:** `boolean` — A boolean indicating whether the player meets the specified
verification level.

**Using IsVerified**

The following example prints "true" if the player is verified.

```lua
local Players = game:GetService("Players")

local function onPlayerAdded(player)
	print(player:IsVerified())
end

for _, player in pairs(Players:GetPlayers()) do
	onPlayerAdded(player)
end
Players.PlayerAdded:Connect(onPlayerAdded)
```

### Method: Player:Kick

**Signature:** `Player:Kick(message: string): ()`

This method allows an experience to gracefully disconnect a client and
optionally provide a message to the disconnected user. This is useful for
moderating abusive users. You should only allow specific users whom you
trust to trigger this method on other users.

Calling this method on a [Player](/docs/reference/engine/classes/Player.md) with no arguments disconnects the
user from the server and provides a default notice message. Calling this
method on a [Player](/docs/reference/engine/classes/Player.md) along with a string as the first argument
replaces the default message with the provided string.

When you call this method from the server, the custom message can be at
most 500 bytes long. If the message is longer, it's discarded and the user
sees the default notice message instead. The limit is measured in bytes,
not characters, so messages that contain multibyte characters such as
emoji or non-Latin text reach the limit sooner.

When using this method from a [LocalScript](/docs/reference/engine/classes/LocalScript.md), only the local user's
client can be kicked.

*Security: None · Thread Safety: Unsafe · Capabilities: Players, Consequences*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `message` | `string` |  | The message to show the user upon kicking. When called from the server, messages longer than 500 bytes are not shown. |

**Returns:** `()`

### Method: Player:LoadCharacterAsync

**Signature:** `Player:LoadCharacterAsync(): ()`

This method creates a new character for the player, removing the old one.
It also clears the player's [Backpack](/docs/reference/engine/classes/Backpack.md) and [PlayerGui](/docs/reference/engine/classes/PlayerGui.md). This
is useful in cases where you want to reload the character without killing
the player, such as when you want to load a new character appearance after
changing the player's
[CharacterAppearance](/docs/reference/engine/classes/Player.md).

When reloading a [Player](/docs/reference/engine/classes/Player.md) with their default platform appearance
applied, a cached version of their appearance will be loaded. The cached
version is cleared whenever the player's appearance is updated using
[AvatarEditorService](/docs/reference/engine/classes/AvatarEditorService.md) or when the player manually resets via the
in-experience menu. To programmatically clear this cache, call
[ClearCachedAvatarAppearance()](/docs/reference/engine/classes/Player.md)
before calling `LoadCharacterAsync()`.

After calling `LoadCharacterAsync()` for an individual player, it is not
recommended to call it again for the same player until after that player's
[CharacterAppearanceLoaded](/docs/reference/engine/classes/Player.md) event
has fired.

#### Character Loading Event Order

Calling the `LoadCharacterAsync()` method on any `Player` fires events in
the following order:

1. [Player.Character](/docs/reference/engine/classes/Player.md) sets, automatically removing old character.
2. [Player.CharacterAdded](/docs/reference/engine/classes/Player.md) fires.
3. [Object.Changed](/docs/reference/engine/classes/Object.md) fires on the [Player](/docs/reference/engine/classes/Player.md) with a value of
   `Character`.
4. The character appearance initializes.
5. [Player.CharacterAppearanceLoaded](/docs/reference/engine/classes/Player.md) fires.
6. The character's [Parent](/docs/reference/engine/classes/Instance.md) sets to the
   [DataModel](/docs/reference/engine/classes/DataModel.md).
7. The character rig builds and scales.
8. The character moves to the spawn location.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Players*

**Returns:** `()`

**Turn Off Auto-Loading and Simulate Character Respawn**

This script turns off auto-loading and simulates character respawning.

```lua
local Players = game:GetService("Players")

local RESPAWN_DELAY = 5

Players.CharacterAutoLoads = false

local function onPlayerAdded(player)
	local function onCharacterAdded(character)
		local humanoid = character:WaitForChild("Humanoid")

		local function onDied()
			task.wait(RESPAWN_DELAY)
			player:LoadCharacterAsync()
		end

		humanoid.Died:Connect(onDied)
	end

	player.CharacterAdded:Connect(onCharacterAdded)

	player:LoadCharacterAsync()
end

Players.PlayerAdded:Connect(onPlayerAdded)
```

### Method: Player:LoadCharacterWithHumanoidDescriptionAsync

**Signature:** `Player:LoadCharacterWithHumanoidDescriptionAsync(humanoidDescription: HumanoidDescription, assetTypeVerification?: AssetTypeVerification): ()`

This method spawns a player character with everything equipped in the
passed in [HumanoidDescription](/docs/reference/engine/classes/HumanoidDescription.md).

After calling this method for an individual player, it is not recommended
to call it again for the same player until after that player's
[CharacterAppearanceLoaded](/docs/reference/engine/classes/Player.md) event
has fired.

See also
[HumanoidDescription System](/docs/en-us/characters/appearance.md#humanoiddescription),
an article which explains the humanoid description system in greater
detail and provides several scripting examples.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Players*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `humanoidDescription` | `HumanoidDescription` |  | A [HumanoidDescription](/docs/reference/engine/classes/HumanoidDescription.md) containing traits like body parts/colors, body scaling, accessories, clothing, and animations that will be equipped to the loaded character. |
| `assetTypeVerification` | `AssetTypeVerification` | `Default` | The asset type verification mode. |

**Returns:** `()`

**Spawn Characters With HumanoidDescription**

To create a `HumanoidDescription` and then spawn a character with that
description applied, add a `Script` (not a `LocalScript`) to the workspace and
add this code to it.

```lua
local Players = game:GetService("Players")

Players.CharacterAutoLoads = false

local function onPlayerAdded(player)
	local humanoidDescription = Instance.new("HumanoidDescription")
	humanoidDescription.HatAccessory = "2551510151,2535600138"
	humanoidDescription.BodyTypeScale = 0.1
	humanoidDescription.ClimbAnimation = 619521311
	humanoidDescription.Face = 86487700
	humanoidDescription.GraphicTShirt = 1711661
	humanoidDescription.HeadColor = Color3.new(0, 1, 0)
	player:LoadCharacterWithHumanoidDescriptionAsync(humanoidDescription)
end

Players.PlayerAdded:Connect(onPlayerAdded)
```

### Method: Player:Move

**Signature:** `Player:Move(walkDirection: Vector3, relativeToCamera?: boolean): ()`

This method causes the player's character to walk in the given direction
until stopped, or interrupted by the player (by using their controls).

This is useful when scripting NPC [Humanoids](/docs/reference/engine/classes/Humanoid.md) that move
around a map but are not controlled by an actual player's input.

Note that the function's second argument indicates whether the provided
[Vector3](/docs/reference/engine/datatypes/Vector3.md) should move the player relative to world coordinates
(`false`) or the player's [Camera](/docs/reference/engine/classes/Camera.md) (`true`).

*Security: None · Thread Safety: Unsafe · Capabilities: Players*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `walkDirection` | `Vector3` |  | The Vector3 direction that the player should move. |
| `relativeToCamera` | `boolean` | `false` | A boolean indicating whether the player should move relative to the player's camera. |

**Returns:** `()`

**Moving the Player relative to their Camera**

Demonstrates moving a player relative to their camera's position using
[Player:Move()](/docs/reference/engine/classes/Player.md).

The script first waits for the player's Character and Humanoid to load, as
both are required before calling [Player:Move()](/docs/reference/engine/classes/Player.md). Otherwise a warning
will display in the Output.

```lua
local Players = game:GetService("Players")
local localPlayer = Players.LocalPlayer

-- Wait for the player's character and humanoid, which must exist before calling :Move()
local character = localPlayer.Character or localPlayer.CharacterAdded:Wait()
character:WaitForChild("Humanoid")

-- The player will move until they are 50 studs away from the camera's position at the time of running
localPlayer:Move(Vector3.new(0, 0, -50), true)
```

### Method: Player:PromptAgeCheck

**Signature:** `Player:PromptAgeCheck(): ()`

This method requests that the player be shown the age verification prompt.
When called from a [LocalScript](/docs/reference/engine/classes/LocalScript.md), it must target the
[Players.LocalPlayer](/docs/reference/engine/classes/Players.md); when called from a server [Script](/docs/reference/engine/classes/Script.md), it
can target any [Player](/docs/reference/engine/classes/Player.md). Repeated calls for the same player within a
short cooldown window are silently ignored.

On success, the `PromptAgeCheckRequested` event fires on the target
player's client. When the player passes verification, their
[Player.AgeChecked](/docs/reference/engine/classes/Player.md) property transitions to
[AgeCheckStatus.Checked](/docs/reference/engine/enums/AgeCheckStatus.md).

*Security: None · Thread Safety: Unsafe · Capabilities: Players*

**Returns:** `()`

### Method: Player:RemoveReplicationFocus

**Signature:** `Player:RemoveReplicationFocus(part: BasePart): ()`

This method removes a replication focus previously added by
[AddReplicationFocus()](/docs/reference/engine/classes/Player.md). Has no effect
in experiences that are not streaming enabled.

This method should only be called on the server. It has no effect when
called from a [LocalScript](/docs/reference/engine/classes/LocalScript.md).

*Security: None · Thread Safety: Unsafe · Capabilities: Players*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `part` | `BasePart` |  | The [BasePart](/docs/reference/engine/classes/BasePart.md) to remove as a replication focus. |

**Returns:** `()`

### Method: Player:RequestStreamAroundAsync

**Signature:** `Player:RequestStreamAroundAsync(position: Vector3, timeOut?: double): ()`

For experiences where
[instance streaming](/docs/en-us/workspace/streaming.md) is enabled,
requests that the server stream to the player regions (parts and terrain)
around the specified **X**, **Y**, **Z** location in the 3D world. It is
useful if the experience knows that the player's [CFrame](/docs/reference/engine/datatypes/CFrame.md) will be
set to the specified location in the near future. Without providing the
location with this call, the player may not have streamed in content for
the destination, resulting in a streaming pause or other undesirable
behavior.

The effect of this call will be temporary and there are no guarantees of
what will be streamed in around the specified location. Client memory
limits and network conditions may impact what will be available on the
client.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Players*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `position` | `Vector3` |  | World location where streaming is requested. |
| `timeOut` | `double` | `0` | Optional timeout for the request, the maximum duration that the engine attempts to stream regions around the `position` parameter before abandoning the request. If you don't specify a value, the timeout is effectively infinite. However, if the client is low on memory, the engine abandons all streaming requests, even those that are still within the timeout duration. |

**Returns:** `()`

### Method: Player:SetAccountAge

**Signature:** `Player:SetAccountAge(accountAge: int): ()`

This method sets the [AccountAge](/docs/reference/engine/classes/Player.md) of the player in
days, meaning the age of the account itself relative to when it was first
created.

*Security: PluginSecurity · Thread Safety: Unsafe · Capabilities: Players*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `accountAge` | `int` |  | The age of the account in days. |

**Returns:** `()`

### Method: Player:SetSuperSafeChat

**Signature:** `Player:SetSuperSafeChat(value: boolean): ()`

This method sets whether or not the player sees chat filtered by
[TextService:FilterStringAsync()](/docs/reference/engine/classes/TextService.md) rather than normal chats.

```lua
local Players = game:GetService("Players")

local player = Players.LocalPlayer
player:SetSuperSafeChat(true)
```

Regardless of whether a player has filtered chat enabled, all chat should
be filtered by [TextService](/docs/reference/engine/classes/TextService.md) when broadcast to other players or on
the player's own screen. [TextService:FilterStringAsync()](/docs/reference/engine/classes/TextService.md) returns a
[TextFilterResult](/docs/reference/engine/classes/TextFilterResult.md) object that can be filtered differently according
to the message's intended use.

*Security: PluginSecurity · Thread Safety: Unsafe · Capabilities: Players*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `value` | `boolean` |  | A boolean indicating whether or not the player sees filtered chat. |

**Returns:** `()`

### Method: Player:GetFriendsOnline

**Signature:** `Player:GetFriendsOnline(maxFriends?: int): Array`

> **Deprecated:** This method has been superseded by [GetFriendsOnlineAsync()](/docs/reference/engine/classes/Player.md).

This method returns an array describing the
[LocalPlayer](/docs/reference/engine/classes/Players.md)'s currently online friends, up to
a maximum of `maxFriends` entries. It can only be called on the
[Players.LocalPlayer](/docs/reference/engine/classes/Players.md); calling it on any other [Player](/docs/reference/engine/classes/Player.md) raises
an error. No more than 200 friends are ever returned, and requesting more
logs a warning.

This method has been superseded by
[GetFriendsOnlineAsync()](/docs/reference/engine/classes/Player.md), which
shares the same behavior and return format. See that method for the full
description of the returned dictionary array.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Players, Social*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `maxFriends` | `int` | `200` | The maximum number of online friends to return. |

**Returns:** `Array` — A dictionary of online friends (see the table above).

**Get a List of Online Connections**

This example demonstrates how to get a dictionary of a player's online
friends. It returns the maximum number of friends specified by the argument,
or 200 if an argument is not provided.

```lua
local Players = game:GetService("Players")

local player = Players.LocalPlayer

local success, result = pcall(player.GetFriendsOnlineAsync, player, 10)

if success then
	for _, friend in pairs(result) do
		print(friend.UserName)
	end
else
	warn("Failed to get online players: " .. result)
end
```

### Method: Player:GetRankInGroup

**Signature:** `Player:GetRankInGroup(groupId: int64): int`

> **Deprecated:** This method has been superseded by [GetRankInGroupAsync()](/docs/reference/engine/classes/Player.md).

Only public roles are considered.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Players, Groups*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `groupId` | `int64` |  | The `groupId` of the specified group. |

**Returns:** `int` — The player's rank in the group.

**How to Check a Player's Rank in a Group**

The code below will check if a player that has entered the game has a rank
equal to 255, in a group with an ID of 2. If they are, it will print "Player
is the owner of the group, 'LOL'!", otherwise "Player is NOT the owner of the
group, 'LOL'!" will be printed to the output.

```lua
local Players = game:GetService("Players")

local function onPlayerAdded(player)
	if player:GetRankInGroupAsync(2) == 255 then
		print("Player is the owner of the group, 'LOL'!")
	else
		print("Player is NOT the owner of the group, 'LOL'!")
	end
end

Players.PlayerAdded:Connect(onPlayerAdded)
```

### Method: Player:GetRankInGroupAsync

**Signature:** `Player:GetRankInGroupAsync(groupId: int64): int`

> **Deprecated:** This method returns only the rank value of the member's highest public role. Use [GroupService:GetRolesInGroupAsync()](/docs/reference/engine/classes/GroupService.md) instead, which returns all public roles.

This method returns the player's rank in the group as an integer between
`0` and `255`, where `0` is a non-member and `255` is the group's owner.
Only public roles are considered.

This call may not yield the most up-to-date information. If a player
leaves a group while they are in the experience, `GetRankInGroupAsync()`
will still think they're in that group until they leave. However, this
does not happen when used with a [LocalScript](/docs/reference/engine/classes/LocalScript.md) because the method
caches results, so multiple calls of `GetRankInGroupAsync()` on the same
player with the same group ID will yield the same result as when the
method was first called with the given group ID. The caching behavior is
on a per-peer basis: a server does not share the same cache as a client.

When a player joins a group in-experience due to a call to
[GroupService:PromptJoinAsync()](/docs/reference/engine/classes/GroupService.md), any cached value for that player
will be cleared on the client where the prompt was shown.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Players, Groups*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `groupId` | `int64` |  | The `groupId` of the specified group. |

**Returns:** `int` — The player's rank in the group.

**How to Check a Player's Rank in a Group**

The code below will check if a player that has entered the game has a rank
equal to 255, in a group with an ID of 2. If they are, it will print "Player
is the owner of the group, 'LOL'!", otherwise "Player is NOT the owner of the
group, 'LOL'!" will be printed to the output.

```lua
local Players = game:GetService("Players")

local function onPlayerAdded(player)
	if player:GetRankInGroupAsync(2) == 255 then
		print("Player is the owner of the group, 'LOL'!")
	else
		print("Player is NOT the owner of the group, 'LOL'!")
	end
end

Players.PlayerAdded:Connect(onPlayerAdded)
```

### Method: Player:GetRoleInGroup

**Signature:** `Player:GetRoleInGroup(groupId: int64): string`

> **Deprecated:** This method has been superseded by [GetRoleInGroup()](/docs/reference/engine/classes/Player.md).

Only public roles are considered.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Players, Groups*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `groupId` | `int64` |  | The group ID of the specified group. |

**Returns:** `string` — The player's role in the specified group, or `Guest` if the player is
not a member.

**How to Check a Player's Role in a Group**

The code below will print the name of the rank that the player is currently a
part of, in a specific group. In this instance we're checking what rank the
player is within a group which has a group ID of 2.

```lua
local Players = game:GetService("Players")

local function onPlayerAdded(player)
	print("Player is ranked as '", player:GetRoleInGroupAsync(2), "' in group, 'LOL'!")
end

Players.PlayerAdded:Connect(onPlayerAdded)
```

### Method: Player:GetRoleInGroupAsync

**Signature:** `Player:GetRoleInGroupAsync(groupId: int64): string`

> **Deprecated:** This method returns only the member's highest public role. Use [GroupService:GetRolesInGroupAsync()](/docs/reference/engine/classes/GroupService.md) instead, which returns all public roles.

This method returns the player's role in the group as a string, or `Guest`
if the player isn't part of the group. Only public roles are considered.

This call may not yield the most up-to-date information. If a player
leaves a group while they are in the experience, `GetRoleInGroupAsync()`
will still think they're in that group until they leave. However, this
does not happen when used with a [LocalScript](/docs/reference/engine/classes/LocalScript.md) because the method
caches results, so multiple calls of `GetRoleInGroupAsync()` on the same
player with the same group ID will yield the same result as when the
method was first called with the given group ID. The caching behavior is
on a per-peer basis: a server does not share the same cache as a client.

When a player joins a group in-experience due to a call to
[GroupService:PromptJoinAsync()](/docs/reference/engine/classes/GroupService.md), any cached value for that player
will be cleared on the client where the prompt was shown.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Players, Groups*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `groupId` | `int64` |  | The group ID of the specified group. |

**Returns:** `string` — The player's role in the specified group, or `Guest` if the player is
not a member.

**How to Check a Player's Role in a Group**

The code below will print the name of the rank that the player is currently a
part of, in a specific group. In this instance we're checking what rank the
player is within a group which has a group ID of 2.

```lua
local Players = game:GetService("Players")

local function onPlayerAdded(player)
	print("Player is ranked as '", player:GetRoleInGroupAsync(2), "' in group, 'LOL'!")
end

Players.PlayerAdded:Connect(onPlayerAdded)
```

### Method: Player:IsBestFriendsWith

**Signature:** `Player:IsBestFriendsWith(userId: User): boolean`

> **Deprecated:** This function is obsolete because the "best friends" feature was removed. Use [Player:IsFriendsWithAsync()](/docs/reference/engine/classes/Player.md) instead.

This function was once used to return whether a player is best friends
with the specified user, but the feature has since been removed.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Players*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `userId` | `User` |  | The [Player.UserId](/docs/reference/engine/classes/Player.md) of the user to check friendship with. |

**Returns:** `boolean` — A boolean indicating whether the player is friends with the specified
user.

### Method: Player:IsFriendsWith

**Signature:** `Player:IsFriendsWith(userId: User): boolean`

> **Deprecated:** This method has been superseded by the [Player:IsFriendsWithAsync()](/docs/reference/engine/classes/Player.md) method which should be used for new work.

This method sends a request to Roblox asking whether the player is a
friend of the user with the given [UserId](/docs/reference/engine/classes/Player.md). Results
are cached, so multiple calls on the same player with the same `userId`
may not reflect the most up-to-date friendship status.

This method has been superseded by
[IsFriendsWithAsync()](/docs/reference/engine/classes/Player.md), which shares the
same behavior and should be used for new work.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Players, Social*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `userId` | `User` |  | The [Player.UserId](/docs/reference/engine/classes/Player.md) of the specified player. |

**Returns:** `boolean` — A boolean indicating whether a player is a friend of the specified
user.

**How to Check if a Player is a Connection**

The below example would print whether or not a recently added player is
friends with Gordonrox24.

```lua
local Players = game:GetService("Players")

local function onPlayerAdded(player)
	if player:IsFriendsWithAsync(146569) then
		print(player.Name .. " is connections with gordonrox24!")
	end
end

Players.PlayerAdded:Connect(onPlayerAdded)
```

### Method: Player:isFriendsWith

**Signature:** `Player:isFriendsWith(userId: User): boolean`

> **Deprecated:** This method has been superseded by the [Player:IsFriendsWithAsync()](/docs/reference/engine/classes/Player.md) method which should be used for new work.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Players*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `userId` | `User` |  |  |

**Returns:** `boolean`

### Method: Player:IsInGroup

**Signature:** `Player:IsInGroup(groupId: int64): boolean`

> **Deprecated:** This method has been superseded by [IsInGroupAsync()](/docs/reference/engine/classes/Player.md).

This method sends a request to Roblox asking whether the player is a
member of the group with the given ID.

This method has been superseded by
[IsInGroupAsync()](/docs/reference/engine/classes/Player.md), which shares the same
behavior (including its per-peer result caching) and should be used for
new work.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Players, Groups*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `groupId` | `int64` |  | The group ID of the specified group. |

**Returns:** `boolean` — A boolean indicating whether the player is in the specified group.

### Method: Player:LoadBoolean

**Signature:** `Player:LoadBoolean(key: string): boolean`

> **Deprecated:** This item is deprecated, as it may have been used for a now obsolete data persistence method. Please save and load player data using [DataStoreService](/docs/reference/engine/classes/DataStoreService.md) for new work.

This function returns a boolean value that was previously saved to the
player with [Player:SaveBoolean()](/docs/reference/engine/classes/Player.md) with the same key. Returns false
if the key doesn't exist, not `nil`.

*Security: None · Thread Safety: Unsafe · Capabilities: Players*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `key` | `string` |  | The string key under which the boolean was previously saved. |

**Returns:** `boolean` — The saved boolean value, or `false` if the key does not exist.

### Method: Player:loadBoolean

**Signature:** `Player:loadBoolean(key: string): boolean`

> **Deprecated:** This deprecated function is a variant of [Player:LoadBoolean()](/docs/reference/engine/classes/Player.md) which has also been deprecated. Neither function should be used in new work.

*Security: None · Thread Safety: Unsafe · Capabilities: Players*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `key` | `string` |  |  |

**Returns:** `boolean`

### Method: Player:LoadCharacter

**Signature:** `Player:LoadCharacter(): ()`

> **Deprecated:** This method has been superseded by [LoadCharacterAsync()](/docs/reference/engine/classes/Player.md).

This method creates a new [Character](/docs/reference/engine/classes/Player.md) for the
player, removing the old one, and also clears the player's
[Backpack](/docs/reference/engine/classes/Backpack.md) and [PlayerGui](/docs/reference/engine/classes/PlayerGui.md). It can only be called on the
server.

This method has been superseded by
[LoadCharacterAsync()](/docs/reference/engine/classes/Player.md), which shares the
same character-loading behavior and should be used for new work.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Players*

**Returns:** `()`

**Turn Off Auto-Loading and Simulate Character Respawn**

This script turns off auto-loading and simulates character respawning.

```lua
local Players = game:GetService("Players")

local RESPAWN_DELAY = 5

Players.CharacterAutoLoads = false

local function onPlayerAdded(player)
	local function onCharacterAdded(character)
		local humanoid = character:WaitForChild("Humanoid")

		local function onDied()
			task.wait(RESPAWN_DELAY)
			player:LoadCharacterAsync()
		end

		humanoid.Died:Connect(onDied)
	end

	player.CharacterAdded:Connect(onCharacterAdded)

	player:LoadCharacterAsync()
end

Players.PlayerAdded:Connect(onPlayerAdded)
```

### Method: Player:LoadCharacterAppearance

**Signature:** `Player:LoadCharacterAppearance(assetInstance: Instance): ()`

> **Deprecated:** This method is deprecated. Do not use it for new work.

The LoadCharacterAppearance [Player](/docs/reference/engine/classes/Player.md) function places the given
instance either in the player's [Player.Character](/docs/reference/engine/classes/Player.md), head, or
[StarterGear](/docs/reference/engine/classes/StarterGear.md) based on the instance's class.

This is useful when giving a player's character an asset from the Roblox
catalog, such as a hat or piece of gear.

It is similar to [Player:LoadCharacterAsync()](/docs/reference/engine/classes/Player.md), except it does not
reload the entire character instance, StarterGear, or [PlayerGui](/docs/reference/engine/classes/PlayerGui.md).

Note:

- [Accessory](/docs/reference/engine/classes/Accessory.md), [Shirt](/docs/reference/engine/classes/Shirt.md), [ShirtGraphic](/docs/reference/engine/classes/ShirtGraphic.md),
  [CharacterMesh](/docs/reference/engine/classes/CharacterMesh.md), [BodyColors](/docs/reference/engine/classes/BodyColors.md), and [Accoutrement](/docs/reference/engine/classes/Accoutrement.md) are
  parented to the player's character.
- [Decal](/docs/reference/engine/classes/Decal.md), [FileMesh](/docs/reference/engine/classes/FileMesh.md), [SpecialMesh](/docs/reference/engine/classes/SpecialMesh.md), [BlockMesh](/docs/reference/engine/classes/BlockMesh.md),
  [CylinderMesh](/docs/reference/engine/classes/CylinderMesh.md), and [Texture](/docs/reference/engine/classes/Texture.md) are parented to the
  character's head.
- [Tool](/docs/reference/engine/classes/Tool.md) is parented to the player's [StarterGear](/docs/reference/engine/classes/StarterGear.md).
- All other classes are ignored.

*Security: None · Thread Safety: Unsafe · Capabilities: AvatarAppearance, Players*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `assetInstance` | `Instance` |  | An instance of the asset being loaded, which can be obtained using the [InsertService:LoadAsset()](/docs/reference/engine/classes/InsertService.md) function. |

**Returns:** `()`

**Player:LoadCharacterAppearance**

This script gives any Hat/Gear/Face/Body Part to a player once they chat the
URL of the asset.

```lua
local Players = game:GetService("Players")
local InsertService = game:GetService("InsertService")

local function onPlayerAdded(player)
	local function onChatted(message)
		local assetId = message:match("id=(%d+)")
		if assetId then
			local model = InsertService:LoadAsset(assetId)
			for _, child in pairs(model:GetChildren()) do
				player:LoadCharacterAppearance(child)
			end
		end
	end

	player.Chatted:Connect(onChatted)
end

Players.PlayerAdded:Connect(onPlayerAdded)
```

### Method: Player:LoadCharacterWithHumanoidDescription

**Signature:** `Player:LoadCharacterWithHumanoidDescription(humanoidDescription: HumanoidDescription, assetTypeVerification?: AssetTypeVerification): ()`

> **Deprecated:** This method has been superseded by [LoadCharacterWithHumanoidDescriptionAsync()](/docs/reference/engine/classes/Player.md).

This method spawns a player character with everything equipped in the
passed-in [HumanoidDescription](/docs/reference/engine/classes/HumanoidDescription.md), such as body parts, colors, body
scaling, accessories, clothing, and animations. A `nil` description raises
an error, and a description that contains duplicate costume assets or
duplicate body parts logs a warning before the character loads.

This method has been superseded by
[LoadCharacterWithHumanoidDescriptionAsync()](/docs/reference/engine/classes/Player.md),
which shares the same behavior and should be used for new work.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Players*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `humanoidDescription` | `HumanoidDescription` |  | A [HumanoidDescription](/docs/reference/engine/classes/HumanoidDescription.md) containing traits like body parts/colors, body scaling, accessories, clothing, and animations that will be equipped to the loaded character. |
| `assetTypeVerification` | `AssetTypeVerification` | `Default` | The asset type verification mode. |

**Returns:** `()`

**Spawn Characters With HumanoidDescription**

To create a `HumanoidDescription` and then spawn a character with that
description applied, add a `Script` (not a `LocalScript`) to the workspace and
add this code to it.

```lua
local Players = game:GetService("Players")

Players.CharacterAutoLoads = false

local function onPlayerAdded(player)
	local humanoidDescription = Instance.new("HumanoidDescription")
	humanoidDescription.HatAccessory = "2551510151,2535600138"
	humanoidDescription.BodyTypeScale = 0.1
	humanoidDescription.ClimbAnimation = 619521311
	humanoidDescription.Face = 86487700
	humanoidDescription.GraphicTShirt = 1711661
	humanoidDescription.HeadColor = Color3.new(0, 1, 0)
	player:LoadCharacterWithHumanoidDescriptionAsync(humanoidDescription)
end

Players.PlayerAdded:Connect(onPlayerAdded)
```

### Method: Player:LoadInstance

**Signature:** `Player:LoadInstance(key: string): Instance`

> **Deprecated:** This item is deprecated, as it may have been used for a now obsolete data persistence method. Please save and load player data using [DataStoreService](/docs/reference/engine/classes/DataStoreService.md) for new work.

This function returns an instance that was previously saved to the player
with [Player:SaveInstance()](/docs/reference/engine/classes/Player.md) with the same key. Returns `nil` if the
key doesn't exist.

*Security: None · Thread Safety: Unsafe · Capabilities: Players*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `key` | `string` |  | The string key under which the instance was previously saved. |

**Returns:** `Instance` — The saved [Instance](/docs/reference/engine/classes/Instance.md), or `nil` if the key does not exist.

**Player:LoadInstance**

The below example would reparent the saved instance to Workspace.

```lua
local Players = game:GetService("Players")

local function onPlayerAdded(player)
	if player:WaitForDataReady() then
		local model = player:LoadInstance("Model")
		model.Parent = workspace
	end
end

Players.PlayerAdded:Connect(onPlayerAdded)
```

### Method: Player:loadInstance

**Signature:** `Player:loadInstance(key: string): Instance`

> **Deprecated:** This deprecated function is a variant of [Player:LoadInstance()](/docs/reference/engine/classes/Player.md) which has also been deprecated. Neither function should be used in new work.

*Security: None · Thread Safety: Unsafe · Capabilities: Players*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `key` | `string` |  |  |

**Returns:** `Instance`

### Method: Player:LoadNumber

**Signature:** `Player:LoadNumber(key: string): double`

> **Deprecated:** This item is deprecated, as it may have been used for a now obsolete data persistence method. Please save and load player data using [DataStoreService](/docs/reference/engine/classes/DataStoreService.md) for new work.

This function was once used by an ancient data persistence method to
return a number value that was previously saved to the player with
[Player:SaveNumber()](/docs/reference/engine/classes/Player.md) with the same key. Returns 0 if the key
doesn't exist, not `nil`.

*Security: None · Thread Safety: Unsafe · Capabilities: Players*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `key` | `string` |  | The string key under which the number was previously saved. |

**Returns:** `double` — The saved number value, or `0` if the key does not exist.

**Player:LoadNumber**

The below would print the value of the player's TotalPlays.

```lua
local Players = game:GetService("Players")

local function onPlayerAdded(player)
	if player:WaitForDataReady() then
		print(player:LoadNumber("TotalPlays"))
	end
end

Players.PlayerAdded:Connect(onPlayerAdded)
```

### Method: Player:loadNumber

**Signature:** `Player:loadNumber(key: string): double`

> **Deprecated:** This deprecated function is a variant of [Player:LoadNumber()](/docs/reference/engine/classes/Player.md) which has also been deprecated. Neither function should be used in new work.

*Security: None · Thread Safety: Unsafe · Capabilities: Players*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `key` | `string` |  |  |

**Returns:** `double`

### Method: Player:LoadString

**Signature:** `Player:LoadString(key: string): string`

> **Deprecated:** This item is deprecated, as it may have been used for a now obsolete data persistence method. Please save and load player data using [DataStoreService](/docs/reference/engine/classes/DataStoreService.md) for new work.

This function returns a string value that was previously saved to the
player with [Player:SaveString()](/docs/reference/engine/classes/Player.md) with the same key. Returns an
empty string ("") if the key doesn't exist, not `nil`.

*Security: None · Thread Safety: Unsafe · Capabilities: Players*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `key` | `string` |  | The string key under which the string was previously saved. |

**Returns:** `string` — The saved string value, or an empty string if the key does not exist.

**Player:LoadString**

The below example would print the value of the previously saved key
"TheirName".

```lua
game.Players.PlayerAdded:Connect(function(Player)
	if Player:WaitForDataReady() then
		print(Player:LoadString("TheirName"))
	end
end)
```

### Method: Player:loadString

**Signature:** `Player:loadString(key: string): string`

> **Deprecated:** This function is a deprecated variant of [Player:LoadString()](/docs/reference/engine/classes/Player.md) which has also been deprecated. Neither function should be used in new work.

*Security: None · Thread Safety: Unsafe · Capabilities: Players*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `key` | `string` |  |  |

**Returns:** `string`

### Method: Player:SaveBoolean

**Signature:** `Player:SaveBoolean(key: string, value: boolean): ()`

> **Deprecated:** This item is deprecated, as it may have been used for a now obsolete data persistence method. Please save and load player data using [DataStoreService](/docs/reference/engine/classes/DataStoreService.md) for new work.

This function is used to save a boolean value that can be loaded again at
a later time using [Player:LoadBoolean()](/docs/reference/engine/classes/Player.md).

*Security: None · Thread Safety: Unsafe · Capabilities: Players*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `key` | `string` |  | The string key to associate with the saved boolean value. |
| `value` | `boolean` |  | The boolean value to save. |

**Returns:** `()`

**Player:SaveBoolean**

The below example would save a boolean to the player with a key of "HasPlayed"
and a value of true.

```lua
game.Players.PlayerAdded:Connect(function(Player)
	if Player:WaitForDataReady() then
		Player:SaveBoolean("HasPlayed", true)
	end
end)
```

### Method: Player:saveBoolean

**Signature:** `Player:saveBoolean(key: string, value: boolean): ()`

> **Deprecated:** This function is a deprecated variant of [Player:SaveBoolean()](/docs/reference/engine/classes/Player.md) which has also been deprecated. Neither function should be used in new work.

*Security: None · Thread Safety: Unsafe · Capabilities: Players*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `key` | `string` |  |  |
| `value` | `boolean` |  |  |

**Returns:** `()`

### Method: Player:SaveInstance

**Signature:** `Player:SaveInstance(key: string, value: Instance): ()`

> **Deprecated:** This item is deprecated, as it may have been used for a now obsolete data persistence method. Please save and load player data using [DataStoreService](/docs/reference/engine/classes/DataStoreService.md) for new work.

This function was once used by an ancient data persistence method to save
an instance which can be loaded again at a later time using
[Player:LoadInstance()](/docs/reference/engine/classes/Player.md)..

*Security: None · Thread Safety: Unsafe · Capabilities: Players*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `key` | `string` |  | The string key to associate with the saved instance. |
| `value` | `Instance` |  | The [Instance](/docs/reference/engine/classes/Instance.md) to save. |

**Returns:** `()`

**Player:SaveInstance**

The below code will save 'Model', a descendant of Workspace, to the player
each time they join the game. To access this instance again, we would need to
index it by it's key, 'Model', as defined in the first argument of this
method.

```lua
game.Players.PlayerAdded:Connect(function(Player)
	Player:WaitForDataReady()
	Player:SaveInstance("Model", game.Workspace.Model)
end)
```

### Method: Player:saveInstance

**Signature:** `Player:saveInstance(key: string, value: Instance): ()`

> **Deprecated:** This function is a deprecated variant of [Player:SaveInstance()](/docs/reference/engine/classes/Player.md) which has also been deprecated. Neither function should be used in new work.

*Security: None · Thread Safety: Unsafe · Capabilities: Players*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `key` | `string` |  |  |
| `value` | `Instance` |  |  |

**Returns:** `()`

### Method: Player:SaveNumber

**Signature:** `Player:SaveNumber(key: string, value: double): ()`

> **Deprecated:** This item is deprecated, as it may have been used for a now obsolete data persistence method. Please save and load player data using [DataStoreService](/docs/reference/engine/classes/DataStoreService.md) for new work.

This function was once used by an ancient data persistence method to save
a number value that can be loaded again at a later time using
[Player:LoadNumber()](/docs/reference/engine/classes/Player.md).

*Security: None · Thread Safety: Unsafe · Capabilities: Players*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `key` | `string` |  | The string key to associate with the saved number value. |
| `value` | `double` |  | The number value to save. |

**Returns:** `()`

**Player:SaveNumber**

The below example would save a number to the player with a key of "TotalPlays"
and add one to the value each time.

```lua
game.Players.PlayerAdded:Connect(function(Player)
	if Player:WaitForDataReady() then
		local OldValue = Player:SaveNumber("TotalPlays")
		Player:SaveNumber("TotalPlays", OldValue + 1)
	end
end)
```

### Method: Player:saveNumber

**Signature:** `Player:saveNumber(key: string, value: double): ()`

> **Deprecated:** This function is a deprecated variant of [Player:SaveNumber()](/docs/reference/engine/classes/Player.md) which has also been deprecated. Neither function should be used in new work.

*Security: None · Thread Safety: Unsafe · Capabilities: Players*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `key` | `string` |  |  |
| `value` | `double` |  |  |

**Returns:** `()`

### Method: Player:SaveString

**Signature:** `Player:SaveString(key: string, value: string): ()`

> **Deprecated:** This item is deprecated, as it may have been used for a now obsolete data persistence method. Please save and load player data using [DataStoreService](/docs/reference/engine/classes/DataStoreService.md) for new work.

This function was once used by an ancient data persistence method to save
a string value that can be loaded again at a later time using
[Player:LoadString()](/docs/reference/engine/classes/Player.md).

*Security: None · Thread Safety: Unsafe · Capabilities: Players*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `key` | `string` |  | The string key to associate with the saved string value. |
| `value` | `string` |  | The string value to save. |

**Returns:** `()`

**Player:SaveString**

The below example would save a string to the player with a key of "TheirName"
and a value of their current name. If you printed it, it would print their
name.

```lua
local Players = game:GetService("Players")

local function onPlayerAdded(player)
	if player:WaitForDataReady() then
		player:SaveString("TheirName", player.Name)
	end
end

Players.PlayerAdded:Connect(onPlayerAdded)
```

### Method: Player:saveString

**Signature:** `Player:saveString(key: string, value: string): ()`

> **Deprecated:** This function is a deprecated variant of [Player:SaveString()](/docs/reference/engine/classes/Player.md) which has also been deprecated. Neither function should be used in new work.

*Security: None · Thread Safety: Unsafe · Capabilities: Players*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `key` | `string` |  |  |
| `value` | `string` |  |  |

**Returns:** `()`

### Method: Player:WaitForDataReady

**Signature:** `Player:WaitForDataReady(): boolean`

> **Deprecated:** This item is deprecated, as it may have been used for a now obsolete data persistence method. Please save and load player data using [DataStoreService](/docs/reference/engine/classes/DataStoreService.md) for new work.

This function is used to pause the script until the player's data is
available to manipulate, or until a certain amount of time has elapsed
without fetching the player's data

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Players*

**Returns:** `boolean` — A boolean indicating whether the player's data loaded successfully.

### Method: Player:waitForDataReady

**Signature:** `Player:waitForDataReady(): boolean`

> **Deprecated:** This function is a deprecated variant of [Player:WaitForDataReady()](/docs/reference/engine/classes/Player.md) which has also been deprecated. Neither function should be used in new work.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Players*

**Returns:** `boolean`

## Events

### Event: Player.CharacterAdded

**Signature:** `Player.CharacterAdded(character: Model)`

This event fires when a player's character spawns or respawns. It fires
soon after setting [Character](/docs/reference/engine/classes/Player.md) to a non-`nil` value
or calling [LoadCharacterAsync()](/docs/reference/engine/classes/Player.md), which
is before the character is parented to the [Workspace](/docs/reference/engine/classes/Workspace.md).

This can be used alongside the
[CharacterRemoving](/docs/reference/engine/classes/Player.md) event which fires right
before a player's character is about to be removed, typically after death.
As such, both of these events can potentially fire many times as players
die then respawn in a place.

Note that the [Humanoid](/docs/reference/engine/classes/Humanoid.md) and its default body parts (head, torso,
and limbs) will exist on the server when this event fires, but clothing
items like [Hats](/docs/reference/engine/classes/Hat.md), [Shirts](/docs/reference/engine/classes/Shirt.md), and [Pants](/docs/reference/engine/classes/Pants.md) might
take a few seconds to be added to the character. The parts will also take
time to replicate to clients. Connect [Instance.ChildAdded](/docs/reference/engine/classes/Instance.md) on the
added character to detect these, or wait for the
[CharacterAppearanceLoaded](/docs/reference/engine/classes/Player.md) event
to be sure the character has everything equipped.

If you instead need to track when a player joins/leaves the experience,
use the events [Players.PlayerAdded](/docs/reference/engine/classes/Players.md) and
[Players.PlayerRemoving](/docs/reference/engine/classes/Players.md).

*Security: None · Capabilities: Players*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `character` | `Model` | An instance of the character that spawned/respawned. |

**Detecting Player Spawns and Despawns**

This code sample demonstrates the usage of [Players.PlayerAdded](/docs/reference/engine/classes/Players.md),
[Player.CharacterAdded](/docs/reference/engine/classes/Player.md) and [Player.CharacterRemoving](/docs/reference/engine/classes/Player.md) in order to
detect the spawning and despawning of players' characters. You can use this as
a boilerplate script to make changes to players' characters as they spawn,
such as changing [Humanoid.WalkSpeed](/docs/reference/engine/classes/Humanoid.md).

```lua
local Players = game:GetService("Players")

local function onCharacterAdded(character)
	print(character.Name .. " has spawned")
end

local function onCharacterRemoving(character)
	print(character.Name .. " is despawning")
end

local function onPlayerAdded(player)
	player.CharacterAdded:Connect(onCharacterAdded)
	player.CharacterRemoving:Connect(onCharacterRemoving)
end

Players.PlayerAdded:Connect(onPlayerAdded)
```

**Expected output:** Player1 has spawned
Player1 is despawning

**Accessory Remover**

This code sample automatically removes `Accessory` objects like hats from the
`Player`'s character when they respawn. Warning: this includes hair, so this
script may cause acute baldness.

When the [Character()](/docs/reference/engine/classes/Player.md) is
[added](/docs/reference/engine/classes/Player.md), we wait for [RunService.Stepped](/docs/reference/engine/classes/RunService.md) to
fire once (using the `wait` function of events). This is so the accessory
removal logic runs one frame after the character spawns. A warning can appear
if you delete accessories too quickly after the player spawns, so waiting one
frame will avoid that.

```lua
local Players = game:GetService("Players")
local RunService = game:GetService("RunService")

local function destroyAccessory(object)
	if object:IsA("Hat") or object:IsA("Accessory") then
		object:Destroy()
	end
end

local function onCharacterAdded(character)
	-- Wait a brief moment before removing accessories to avoid the
	-- "Something unexpectedly set ___ parent to NULL" warning
	RunService.Stepped:Wait()
	-- Check for any existing accessories in the player's character
	for _, child in pairs(character:GetChildren()) do
		destroyAccessory(child)
	end
	-- Hats may be added to the character a moment after
	-- CharacterAdded fires, so we listen for those using ChildAdded
	character.ChildAdded:Connect(destroyAccessory)
end

local function onPlayerAdded(player)
	player.CharacterAdded:Connect(onCharacterAdded)
end

Players.PlayerAdded:Connect(onPlayerAdded)
```

### Event: Player.CharacterAppearanceLoaded

**Signature:** `Player.CharacterAppearanceLoaded(character: Model)`

This event fires when the full appearance of a
[Character](/docs/reference/engine/classes/Player.md) has been inserted. It only fires on the
server.

A [Character](/docs/reference/engine/classes/Player.md) generally has a range of objects
modifying its appearance, including [Accoutrements](/docs/reference/engine/classes/Accoutrement.md),
[Shirts](/docs/reference/engine/classes/Shirt.md), [Pants](/docs/reference/engine/classes/Pants.md) and
[CharacterMeshes](/docs/reference/engine/classes/CharacterMesh.md). This event will fire when all such
objects have been inserted into the character.

For custom character implementations, such as using a character model
named `StarterCharacter` inside [StarterPlayer](/docs/reference/engine/classes/StarterPlayer.md), use
[CharacterAdded](/docs/reference/engine/classes/Player.md) and handle your own
accessories.

One use for this event is to ensure all accessories have loaded before
destroying them. See below for an example of this.

*Security: None · Capabilities: Players*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `character` | `Model` | The [Player.Character](/docs/reference/engine/classes/Player.md) [Model](/docs/reference/engine/classes/Model.md). |

**Remove Accessories After Loading**

This code sample will wait for accessories to fully load, print out how many
there are, and then destroy them all.

```lua
local Players = game:GetService("Players")

local function onPlayerAddedAsync(player)
	local connection = player.CharacterAppearanceLoaded:Connect(function(character)
		-- All accessories have loaded at this point
		local humanoid = character:FindFirstChildOfClass("Humanoid")
		local numAccessories = #humanoid:GetAccessories()
		print(("Destroying %d accessories for %s"):format(numAccessories, player.Name))
		humanoid:RemoveAccessories()
	end)

	-- Make sure we disconnect our connection to the player after they leave
	-- to allow the player to get garbage collected
	player.AncestryChanged:Wait()
	connection:Disconnect()
end

for _, player in Players:GetPlayers() do
	task.spawn(onPlayerAddedAsync, player)
end
Players.PlayerAdded:Connect(onPlayerAddedAsync)
```

### Event: Player.CharacterRemoving

**Signature:** `Player.CharacterRemoving(character: Model)`

This event fires right before a player's
[Character](/docs/reference/engine/classes/Player.md) is removed, such as when the player is
respawning. This can be used alongside the
[CharacterAdded](/docs/reference/engine/classes/Player.md) event which fires when a
player's character spawns or respawns.

If you instead need to track when a player joins/leaves the experience,
use the events [Players.PlayerAdded](/docs/reference/engine/classes/Players.md) and
[Players.PlayerRemoving](/docs/reference/engine/classes/Players.md).

*Security: None · Capabilities: Players*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `character` | `Model` | An instance of the character that is being removed. |

**Detecting Player Spawns and Despawns**

This code sample demonstrates the usage of [Players.PlayerAdded](/docs/reference/engine/classes/Players.md),
[Player.CharacterAdded](/docs/reference/engine/classes/Player.md) and [Player.CharacterRemoving](/docs/reference/engine/classes/Player.md) in order to
detect the spawning and despawning of players' characters. You can use this as
a boilerplate script to make changes to players' characters as they spawn,
such as changing [Humanoid.WalkSpeed](/docs/reference/engine/classes/Humanoid.md).

```lua
local Players = game:GetService("Players")

local function onCharacterAdded(character)
	print(character.Name .. " has spawned")
end

local function onCharacterRemoving(character)
	print(character.Name .. " is despawning")
end

local function onPlayerAdded(player)
	player.CharacterAdded:Connect(onCharacterAdded)
	player.CharacterRemoving:Connect(onCharacterRemoving)
end

Players.PlayerAdded:Connect(onPlayerAdded)
```

**Expected output:** Player1 has spawned
Player1 is despawning

### Event: Player.Chatted

**Signature:** `Player.Chatted(message: string, recipient: Player)`

This event fires when a [Player](/docs/reference/engine/classes/Player.md) types a message and presses
<kbd>Enter</kbd> in Roblox's provided chat bar. This is done using some
Luau bindings by the default chat script. You can prevent players from
chatting by using [StarterGui:SetCoreGuiEnabled()](/docs/reference/engine/classes/StarterGui.md) and setting
[CoreGuiType.Chat](/docs/reference/engine/enums/CoreGuiType.md) to `false`.

*Security: None · Capabilities: Chat, Players*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `message` | `string` | The content of the message the player typed in chat. |
| `recipient` | `Player` | **Deprecated.** For whisper messages, this was the Player who was the intended target of the chat message. |

### Event: Player.Idled

**Signature:** `Player.Idled(time: double)`

This event fires approximately two minutes after the engine classifies the
player as idle. Time is the number of seconds that have elapsed since that
point. The event continues to fire every 30 seconds for as long as the
player remains idle.

Once the player becomes active again, `Idled` stops firing and the elapsed
idle time resets. There is no separate event for the transition back to
activity. If the player goes idle again later, `Idled` waits the same ~2
minutes before firing again.

This event only fires in client scripts, not server scripts; use a
[RemoteEvent](/docs/reference/engine/classes/RemoteEvent.md) to notify the server of idle players.

Roblox automatically disconnects players that have been idle for at least
20 minutes, so this event is useful for warning players that they will be
disconnected soon, disconnecting players prior to those 20 minutes, or
other away from keyboard (AFK) features.

To track how often automatic disconnects occur, try correlating this event
with occurrences of [Players.PlayerRemoving](/docs/reference/engine/classes/Players.md).

*Security: None · Capabilities: Players*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `time` | `double` | The time in seconds the player has been idle. |

### Event: Player.OnTeleport

**Signature:** `Player.OnTeleport(teleportState: TeleportState, placeId: int64, spawnName: string)`

This event fires when the [TeleportState](/docs/reference/engine/enums/TeleportState.md) of a player changes. This
event is useful for detecting whether a teleportation was successful.

*Security: None · Capabilities: Players, Teleport*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `teleportState` | `TeleportState` | The new [TeleportState](/docs/reference/engine/enums/TeleportState.md) of the [Player](/docs/reference/engine/classes/Player.md). |
| `placeId` | `int64` | The ID of the place the [Player](/docs/reference/engine/classes/Player.md) is being teleported to. |
| `spawnName` | `string` | The name of the spawn to teleport to, if [TeleportService:TeleportToSpawnByName()](/docs/reference/engine/classes/TeleportService.md) has been used. |

**Player.OnTeleport**

This example prints which stage of a teleport a player is at, as well as
printing if the teleport was a failure.

```lua
local Players = game:GetService("Players")

Players.PlayerAdded:Connect(function(player)
	local playerOnTeleport = player
	player.OnTeleport:Connect(function(teleportState, _placeId, _spawnName)
		if teleportState == Enum.TeleportState.Started then
			print("Teleport started (" .. playerOnTeleport.Name .. ")")
		elseif teleportState == Enum.TeleportState.WaitingForServer then
			print("Teleport waiting for server (" .. playerOnTeleport.Name .. ")")
		elseif teleportState == Enum.TeleportState.InProgress then
			print("Teleport in progress (" .. playerOnTeleport.Name .. ")")
		elseif teleportState == Enum.TeleportState.Failed then
			print("Teleport failed! (" .. playerOnTeleport.Name .. ")")
		end
	end)
end)
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