---
name: StarterPlayer
last_updated: 2026-10-30T19:55:53Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
tags:
  - NotCreatable
  - Service
summary: "A service which allows the defaults of properties in the Player object to be set."
---

# Class: StarterPlayer

> A service which allows the defaults of properties in the [Player](/docs/reference/engine/classes/Player.md) object
> to be set.

## Description

A service which allows the defaults of properties in the [Player](/docs/reference/engine/classes/Player.md) object
to be set. When a player enters the server, each property of the player object
is set to the current value of the corresponding property in
[StarterPlayer](/docs/reference/engine/classes/StarterPlayer.md).

Additionally, you may add four objects to this service:

- A [StarterPlayerScripts](/docs/reference/engine/classes/StarterPlayerScripts.md) instance with scripts that run once for each
  player.
- A [StarterCharacterScripts](/docs/reference/engine/classes/StarterCharacterScripts.md) instance with scripts to add to each
  player's character every time they spawn.
- A [Humanoid](/docs/reference/engine/classes/Humanoid.md) instance named `StarterHumanoid` which will be used as
  the default humanoid for each player's character.
- A [Model](/docs/reference/engine/classes/Model.md) instance named `StarterCharacter` which will be used as the
  character model for all players.

## Properties

### Property: StarterPlayer.AutoJumpEnabled

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
  "category": "Mobile",
  "capabilities": [
    "Players"
  ]
}
```

This property sets whether the character will automatically jump when
hitting an obstacle on a mobile device.

This property is copied from the [StarterPlayer](/docs/reference/engine/classes/StarterPlayer.md) to a [Player](/docs/reference/engine/classes/Player.md)
when they join the game. Following that. the value of this property is
copied to [Humanoid.AutoJumpEnabled](/docs/reference/engine/classes/Humanoid.md) property of the character's
[Humanoid](/docs/reference/engine/classes/Humanoid.md) on spawn. In other words, it is possible to set the
auto-jump behavior on a per-character, per-player and per-game basis using
these three properties.

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

### Property: StarterPlayer.AvatarJointUpgrade

```json
{
  "type": "RolloutState",
  "access": "ReadOnly",
  "security": {
    "read": "RobloxScriptSecurity",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": false,
    "can_save": false
  },
  "thread_safety": "ReadSafe",
  "category": "Character",
  "capabilities": [
    "Players"
  ]
}
```

This property controls the rollout state of new
[AnimationConstraint](/docs/reference/engine/classes/AnimationConstraint.md) joints in avatars. When disabled, avatars
spawn with legacy [Motor6Ds](/docs/reference/engine/classes/Motor6D.md) connecting their limbs. When
enabled, avatars spawn with
[AnimationConstraints](/docs/reference/engine/classes/AnimationConstraint.md) and
[BallSocketConstraints](/docs/reference/engine/classes/BallSocketConstraint.md) connecting their limbs.
This makes it easier to write scripts that enable physical simulation,
like arm strength and ragdoll falling down.

### Property: StarterPlayer.CameraMaxZoomDistance

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

This property sets the maximum distance in studs the camera can be from
the character with the default cameras.

This property sets the default value of
[Player.CameraMaxZoomDistance](/docs/reference/engine/classes/Player.md) for each player who joins the game.
If this value is set to a lower value than
[StarterPlayer.CameraMinZoomDistance](/docs/reference/engine/classes/StarterPlayer.md) it will be increased to
CameraMinZoomDistance.

**Setting Camera Zoom Distance**

The example demonstrates how to set a player's camera minimum and maximum zoom
distance.

In this example, we set the [Player.CameraMinZoomDistance](/docs/reference/engine/classes/Player.md) and
[Player.CameraMaxZoomDistance](/docs/reference/engine/classes/Player.md) to set the min and max distance in studs
a player's camera can be from their character.

Note that since the example attempts to set the CameraMinZoomDistance to be
greater than the CameraMaxZoomDistance, the CameraMinZoomDistance value will
be decreased and set to the value of the max zoom distance.

To change the default min and max zoom distance values for a player when they
first enter the game, you can change the
`StarterClass.Player.CameraMinZoomDistance` and
`StarterClass.Player.CameraMaxZoomDistance` properties.

```lua
local Players = game:GetService("Players")

local player = Players.LocalPlayer

player.CameraMaxZoomDistance = 50
player.CameraMinZoomDistance = 75
```

### Property: StarterPlayer.CameraMinZoomDistance

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

This property sets the minimum distance in studs the camera can be from
the character with the default cameras.

This property sets the default value of
[Player.CameraMinZoomDistance](/docs/reference/engine/classes/Player.md) for each player who joins the game.
If this value is set to a higher value than
[StarterPlayer.CameraMaxZoomDistance](/docs/reference/engine/classes/StarterPlayer.md) it will be decreased to
CameraMaxZoomDistance.

**Setting Camera Zoom Distance**

The example demonstrates how to set a player's camera minimum and maximum zoom
distance.

In this example, we set the [Player.CameraMinZoomDistance](/docs/reference/engine/classes/Player.md) and
[Player.CameraMaxZoomDistance](/docs/reference/engine/classes/Player.md) to set the min and max distance in studs
a player's camera can be from their character.

Note that since the example attempts to set the CameraMinZoomDistance to be
greater than the CameraMaxZoomDistance, the CameraMinZoomDistance value will
be decreased and set to the value of the max zoom distance.

To change the default min and max zoom distance values for a player when they
first enter the game, you can change the
`StarterClass.Player.CameraMinZoomDistance` and
`StarterClass.Player.CameraMaxZoomDistance` properties.

```lua
local Players = game:GetService("Players")

local player = Players.LocalPlayer

player.CameraMaxZoomDistance = 50
player.CameraMinZoomDistance = 75
```

### Property: StarterPlayer.CameraMode

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

Sets the default value for [Player.CameraMode](/docs/reference/engine/classes/Player.md) for each player in
the game. The camera has two modes:

#### First Person

In first person mode, the player's camera is zoomed all the way in. Unless
there is a visible GUI present with the [GuiButton.Modal](/docs/reference/engine/classes/GuiButton.md) property
set to `true`, the mouse will be locked and the user's camera will turn as
the mouse moves.

#### Third Person

In third person mode (default), the character can be seen in the camera.
While in third person mode on Roblox:

- You may right-click and drag to rotate your camera, or use the arrow
  keys at the bottom right-hand corner of the screen.
- When you move your mouse, your camera does not change (unless you move
  the mouse to the end of the screen).
- When you press any of the arrow keys, the user's character will face in
  the corresponding arrow key's direction.
- You can zoom in and out freely.

**Playing in First Person**

This example demonstrates how to change the character's CameraMode to first
person using the LockFirstPerson value of the [CameraMode](/docs/reference/engine/enums/CameraMode.md) enum.

```lua
local Players = game:GetService("Players")

local player = Players.LocalPlayer

player.CameraMode = Enum.CameraMode.LockFirstPerson
```

### Property: StarterPlayer.CharacterBreakJointsOnDeath

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
  "category": "Character",
  "capabilities": [
    "Players"
  ]
}
```

This property determines the starting value of
[Humanoid.BreakJointsOnDeath](/docs/reference/engine/classes/Humanoid.md) for a player's
[Player.Character](/docs/reference/engine/classes/Player.md).

Note that [AvatarJointUpgrade](/docs/reference/engine/classes/StarterPlayer.md) must
be enabled for this property to take effect.

### Property: StarterPlayer.CharacterJumpHeight

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
  "category": "Character Jump Settings",
  "capabilities": [
    "Players"
  ]
}
```

This property determines the starting value of [Humanoid.JumpHeight](/docs/reference/engine/classes/Humanoid.md)
for a player's [Player.Character](/docs/reference/engine/classes/Player.md) in studs, with a default of `7.2`.

This property is only visible in the **Properties** window If
[CharacterUseJumpPower](/docs/reference/engine/classes/StarterPlayer.md) is set
to `false`, as it would not be relevant otherwise.

Since this property is only relevant for characters being spawned in the
future, changing it will not change any existing player characters.
Changes to this property will only take effect when a player respawns.

### Property: StarterPlayer.CharacterJumpPower

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
  "category": "Character Jump Settings",
  "capabilities": [
    "Players"
  ]
}
```

This property determines the starting value of [Humanoid.JumpPower](/docs/reference/engine/classes/Humanoid.md)
for a player's [Player.Character](/docs/reference/engine/classes/Player.md), with a default of `50`, minimum
of `0`, and maximum of `1000`.

This property is only visible in the **Properties** window If
[CharacterUseJumpPower](/docs/reference/engine/classes/StarterPlayer.md) is set
to `true`, as it would not be relevant otherwise.

Since this property is only relevant for characters being spawned in the
future, changing it will not change any existing player characters.
Changes to this property will only take effect when a player respawns.

### Property: StarterPlayer.CharacterMaxSlopeAngle

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
  "category": "Character",
  "capabilities": [
    "Players"
  ]
}
```

This property determines the starting value of
[Humanoid.MaxSlopeAngle](/docs/reference/engine/classes/Humanoid.md) for a player's [Player.Character](/docs/reference/engine/classes/Player.md) in
degrees. It defaults to `89`, so humanoids can climb pretty much any slope
they want by default.

Since this property is only relevant for characters being spawned in the
future, changing it will not change any existing player characters.
Changes to this property will only take effect when a player respawns.

### Property: StarterPlayer.CharacterUseJumpPower

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
  "category": "Character Jump Settings",
  "capabilities": [
    "Players"
  ]
}
```

This property determines the starting value of
[Humanoid.UseJumpPower](/docs/reference/engine/classes/Humanoid.md) for a player's [Player.Character](/docs/reference/engine/classes/Player.md).
Toggling it will change which property is visible in the **Properties**
window ([CharacterJumpHeight](/docs/reference/engine/classes/StarterPlayer.md) if
`false` or [CharacterJumpPower](/docs/reference/engine/classes/StarterPlayer.md) if
`true`). Defaults to `true`.

Since this property is only relevant for characters being spawned in the
future, changing it will not change any existing player characters.
Changes to this property will only take effect when a player respawns.

### Property: StarterPlayer.CharacterWalkSpeed

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
  "category": "Character",
  "capabilities": [
    "Players"
  ]
}
```

This property determines the starting value of [Humanoid.WalkSpeed](/docs/reference/engine/classes/Humanoid.md)
for a player's [Player.Character](/docs/reference/engine/classes/Player.md) with a default of `16`.

Since this property is only relevant for characters being spawned in the
future, changing it will not change any existing player characters.
Changes to this property will only take effect when a player respawns.

### Property: StarterPlayer.ClassicDeath

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
  "category": "Character",
  "capabilities": [
    "Players"
  ]
}
```

When enabled, the character uses the classic death behavior (joints break
apart and parts scatter). When disabled, characters spawn with
[Humanoid.BreakJointsOnDeath](/docs/reference/engine/classes/Humanoid.md) = `false`, and will ragdoll when they
die.

### Property: StarterPlayer.CreateDefaultPlayerModule

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
  "category": "Controls",
  "capabilities": [
    "Players",
    "PluginOrOpenCloud"
  ]
}
```

This property is only visible when
[Workspace.PlayerScriptsUseInputActionSystem](/docs/reference/engine/classes/Workspace.md) is enabled. When set
to `true` (default), the `PlayerModule` injection point occurs at
[StarterPlayer](/docs/reference/engine/classes/StarterPlayer.md). When set to `false`, the default camera and control
scripts will not be added to the place.

### Property: StarterPlayer.DevCameraOcclusionMode

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
and the camera subject. Applies to all players as they join the experience
and can't be changed for individual players.

The default value is [Zoom](/docs/reference/engine/enums/DevCameraOcclusionMode.md) (0). See
[DevCameraOcclusionMode](/docs/reference/engine/enums/DevCameraOcclusionMode.md) for a list of available modes.

### Property: StarterPlayer.DevComputerCameraMovementMode

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

This property lets you overwrite the player's camera mode on a computer.

If set to [UserChoice](/docs/reference/engine/enums/DevComputerCameraMovementMode.md), the player's
camera movement mode will be determined by whatever they set in the
experience's settings. Otherwise, the mode will be set based on this
property.

This property does not affect players who are not on a computer.

### Property: StarterPlayer.DevComputerMovementMode

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
  "category": "Controls",
  "capabilities": [
    "Players"
  ]
}
```

This property lets you overwrite the player's movement mode on a computer.

If set to [UserChoice](/docs/reference/engine/enums/DevComputerMovementMode.md), the player's movement
mode will be determined by whatever they set in the experience's settings.
Otherwise, the mode will be set based on this property.

This property does not affect players who are not on a computer.

### Property: StarterPlayer.DevTouchCameraMovementMode

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

This property lets you overwrite the player's camera mode on a
touch-enabled device.

If set to [UserChoice](/docs/reference/engine/enums/DevTouchCameraMovementMode.md), the player's
camera movement mode will be determined by whatever they set in the
experience's settings. Otherwise, the mode will be set based on this
property.

This property does not affect players who are not on a touch-enabled
device.

### Property: StarterPlayer.DevTouchMovementMode

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
  "category": "Controls",
  "capabilities": [
    "Players"
  ]
}
```

Lets you overwrite the player's movement mode on a touch-enabled device.

If set to [UserChoice](/docs/reference/engine/enums/DevTouchMovementMode.md), the player's movement
mode will be determined by whatever they set in the experience's settings.
Otherwise, the mode will be set based on this property.

This property does not affect players who are not on a touch-enabled
device.

### Property: StarterPlayer.EnableDynamicHeads

```json
{
  "type": "LoadDynamicHeads",
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
  "category": "Character",
  "capabilities": [
    "Players"
  ]
}
```

Sets the use of dynamic heads. When true, enables the use of avatar heads
with facial animation data.

### Property: StarterPlayer.EnableMouseLockOption

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
  "category": "Controls",
  "capabilities": [
    "Players"
  ]
}
```

This property determines if a player can toggle mouse lock by default.

Mouselock will lock the player's cursor to the center of the screen.
Moving the mouse will rotate the [Camera](/docs/reference/engine/classes/Camera.md) and [Player](/docs/reference/engine/classes/Player.md) will
move relative to the current rotation of the camera.

This property sets the value of [Player.DevEnableMouseLock](/docs/reference/engine/classes/Player.md).

Note that shift-lock related APIs are in the process of being deprecated,
so it's recommended to use [UserInputService.MouseBehavior](/docs/reference/engine/classes/UserInputService.md) instead
to lock the mouse.

**Enabling a Player's Mouse Lock**

The example demonstrates how to enable and disabled whether a player can lock
their mouse.

In this example, we set the use a while true loop to toggle the state of the
DevEnabledMouseLock property between _true_ and _false_ every 5 seconds. While
this example has little practical use, it demos how to change the property via
a `LocalScript`.

```lua
local Players = game:GetService("Players")

local player = Players.LocalPlayer

while true do
	player.DevEnableMouseLock = not player.DevEnableMouseLock
	task.wait(5)
end
```

### Property: StarterPlayer.HealthDisplayDistance

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
    "Players"
  ]
}
```

This property sets the distance in studs at which this player will see
other [Humanoid](/docs/reference/engine/classes/Humanoid.md) health bars. If set to 0, the health bars will not
be displayed. This property is set to 100 studs by default.

To change the display distance for a player once they join the game, you
can set the [Player.HealthDisplayDistance](/docs/reference/engine/classes/Player.md) property.

If a [Humanoid](/docs/reference/engine/classes/Humanoid.md) health bar is visible, you can set the display type
using [Humanoid.DisplayDistanceType](/docs/reference/engine/classes/Humanoid.md).

**Hiding Player Health and Names**

This example demonstrates how to hide other `Humanoid`'s (`Player` and NPC)
health bars and names.

This is done by setting the player's [Player.HealthDisplayDistance](/docs/reference/engine/classes/Player.md) and
[Player.NameDisplayDistance](/docs/reference/engine/classes/Player.md) properties to 0.

If you would like to display health bars and names, you set the properties to
a value greater than 0. For instance, setting the properties to 100 means that
the player will see other player's health and names up to 100 studs away.

To modify the default values for players, you can change the values of the
`StarterClass.Player.HealthDisplayDistance` and
`StarterClass.Player.NameDisplayDistance` properties.

```lua
local Players = game:GetService("Players")

local player = Players.LocalPlayer

player.HealthDisplayDistance = 0
player.NameDisplayDistance = 0
```

### Property: StarterPlayer.LoadCharacterAppearance

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
  "category": "Character",
  "capabilities": [
    "Players"
  ]
}
```

This property sets whether or not the appearance of a player's character
should be loaded.

Setting this to `false` results in the player having no clothes (including
hats), body colors, body packages or anything else related to the
appearance of the player's avatar. By default, this property is set to
`true`.

Setting this to `true` results in the player loading the appearance
corresponding to the player's [Player.CharacterAppearanceId](/docs/reference/engine/classes/Player.md).

If [Player:LoadCharacterWithHumanoidDescriptionAsync()](/docs/reference/engine/classes/Player.md) is used, it
can be advantageous to set [StarterPlayer.LoadCharacterAppearance](/docs/reference/engine/classes/StarterPlayer.md)
to false as the player's avatar is not required as all asset IDs to equip
on the character will come from the passed in [HumanoidDescription](/docs/reference/engine/classes/HumanoidDescription.md).

**Disabling a Player's Appearance**

This example demonstrates how to disable loading a player's character
appearance. Instead, the player loads as a grey model without any hats,
shirts, pants, etc.

This is useful for games using custom clothing and accessories.

Note that if the character has already spawned, this change will not take
affect until the player respawns or the [Player:LoadCharacterAsync()](/docs/reference/engine/classes/Player.md)
function is called.

```lua
local Players = game:GetService("Players")

local player = Players.LocalPlayer

player.CanLoadCharacterAppearance = false
```

### Property: StarterPlayer.LoadCharacterLayeredClothing 

```json
{
  "type": "LoadCharacterLayeredClothing",
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
  "category": "Character",
  "capabilities": [
    "Players"
  ]
}
```

Indicates whether characters spawning into an experience will have layered
clothing accessories equipped on them (Although
[Workspace.MeshPartHeadsAndAccessories](/docs/reference/engine/classes/Workspace.md) also need to be enabled in
the [Workspace](/docs/reference/engine/classes/Workspace.md)).

This property also gates the [WrapLayer.AutoSkin](/docs/reference/engine/classes/WrapLayer.md) feature. When set
to `Disabled`, the automatic skinning transfer pipeline for WrapLayers
does not run, and [WrapLayer.AutoSkin](/docs/reference/engine/classes/WrapLayer.md) has no effect. For more
information, see
[Automatic Skinning Transfer](/docs/en-us/avatar/automatic-skinning-transfer.md).

### Property: StarterPlayer.LuaCharacterController

```json
{
  "type": "CharacterControlMode",
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
  "category": "Controls",
  "capabilities": [
    "Players"
  ]
}
```

Determines which character controller implementation drives the player's
character movement. Accepts a value from [CharacterControlMode](/docs/reference/engine/enums/CharacterControlMode.md):
`Default`, `Legacy`, `NoCharacterController`, or `LuaCharacterController`.

### Property: StarterPlayer.NameDisplayDistance

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
    "Players"
  ]
}
```

Sets the distance at which this player will see other [Humanoid](/docs/reference/engine/classes/Humanoid.md)
names. If set to `0`, names are hidden. This property is set to `100`
studs by default.

To change the display distance for a player once they join the game, you
can set the [Player.NameDisplayDistance](/docs/reference/engine/classes/Player.md) property.

If a [Humanoid](/docs/reference/engine/classes/Humanoid.md) name is visible, you can set the display type using
[Humanoid.DisplayDistanceType](/docs/reference/engine/classes/Humanoid.md).

**Hiding Player Health and Names**

This example demonstrates how to hide other `Humanoid`'s (`Player` and NPC)
health bars and names.

This is done by setting the player's [Player.HealthDisplayDistance](/docs/reference/engine/classes/Player.md) and
[Player.NameDisplayDistance](/docs/reference/engine/classes/Player.md) properties to 0.

If you would like to display health bars and names, you set the properties to
a value greater than 0. For instance, setting the properties to 100 means that
the player will see other player's health and names up to 100 studs away.

To modify the default values for players, you can change the values of the
`StarterClass.Player.HealthDisplayDistance` and
`StarterClass.Player.NameDisplayDistance` properties.

```lua
local Players = game:GetService("Players")

local player = Players.LocalPlayer

player.HealthDisplayDistance = 0
player.NameDisplayDistance = 0
```

### Property: StarterPlayer.UserEmotesEnabled

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
  "category": "Character",
  "capabilities": [
    "Players"
  ]
}
```

This property determines if user-owned emotes are loaded when loading
avatars. Setting this property to `false` disables loading. Developers can
set the property in Studio directly.

When emote loading is disabled, the emotes UI will still work as long as
developers choose to use the emotes feature by adding emotes within their
game.

See also [Avatar Emotes](/docs/en-us/characters/emotes.md), an article
detailing how to control, customize, and play avatar emotes.

### Property: StarterPlayer.AllowCustomAnimations *(hidden)*

```json
{
  "type": "boolean",
  "access": "ReadOnly",
  "security": {
    "read": "None",
    "write": "RobloxScriptSecurity"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Character",
  "capabilities": [
    "Players"
  ]
}
```

This property describes the current game's permission levels regarding
custom avatar [Animations](/docs/reference/engine/classes/Animation.md) from the website.

As such, this value cannot be changed from within the game. It can only be
changed by changing the game's permission levels within the game's
setting's page on the website.

This property is not intended for use in the game.

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