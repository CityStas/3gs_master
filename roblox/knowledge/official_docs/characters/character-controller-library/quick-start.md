---
title: "CCL quick start"
url: /docs/en-us/characters/character-controller-library/quick-start
last_updated: 2026-10-30T19:55:38Z
description: "Traditional character abilities (run, climb, jump, swim, etc.) are easily configurable through scripting."
---

# CCL quick start

In the [Character Controller Library](/docs/en-us/characters/character-controller-library.md) (CCL), traditional character abilities (run, climb, jump, swim, etc.) are easily configurable through scripting. For custom character mechanics such as dashing, aiming, wall‑jumping, and more, see [custom abilities](/docs/en-us/characters/character-controller-library/custom-abilities.md).

## Enable CCL

The CCL is **opt-in** through Studio's [Avatar Settings](/docs/en-us/studio/avatar-settings.md) window. To enable it:

1. Enable the CCL beta through **File** ⟩ **Beta Features** ⟩ **AvatarAbilities Character Controller Library**.
2. From the **Avatar** tab, open [Avatar Settings](/docs/en-us/studio/avatar-settings.md).![Avatar Settings indicated in Studio's toolbar](../../assets/studio/general/Toolbar-Avatar-Settings.png)
3. Select the **Movement** tab on the left side of the window and, in the **Abilities** section, select **Character Controller Library**.![Character Controller Library toggle in the Avatar Settings window](../../assets/studio/general/Avatar-Settings-CCL.png)
4. All of the standard abilities like **Running**, **Jumping**, and **Climbing** are enabled by default. To disable any of them at runtime, uncheck the associated box.
  > **Warning:** It's not recommended to disable **Running**, as doing so will prevent characters from moving along the ground. Additionally, you should always keep **Getting Up** enabled if **Falling Down** is enabled, as a mismatch will allow characters to fall down (trip) but never get back up.

## Configuration

Through a script that runs from `Class.ServerScriptService`, you can experiment with the built‑in ability [attributes](#attributes). You can also modify specific [controllers](#controllers) to adjust the physical simulation of the character and its interaction with the environment, such as the character's base movement speed.

### Attributes

At runtime, CCL exposes each built-in ability as a `Class.Configuration` in the character's `Abilities` folder. This folder usually lives under `AbilityManagerActor`, but it can live directly under the character in setups without an actor. Use `AvatarAbilities.getAbilityConfigurationForCharacter()` to access an ability configuration from either setup.

Each ability contains easy-to-configure [attributes](/docs/en-us/studio/properties.md#instance-attributes) such as those noted in the table below. Some attributes correspond to legacy `Class.Humanoid` properties. This relationship identifies equivalent settings, not bidirectional synchronization. The compatibility layer copies changes from these `Class.Humanoid` properties to the corresponding ability attributes. Jumping attributes initially use the corresponding `Class.StarterPlayer` character properties.

> **Warning:** The abilities in a character's `Abilities` folder may vary, depending on which abilities you [enabled/disabled](#enable-ccl). Confirm available abilities and their valid attributes before you attempt to configure them via scripting.

| Ability | Attributes |
| --- | --- |
| `Climbing` | <ul><li>`SpeedMultiplier` — Multiplier to the `Class.ClimbController.MoveSpeedFactor` property when character is climbing.</li></ul> |
| `Crouching` | <ul><li>`SpeedMultiplier` — Multiplier to the `Class.GroundController.MoveSpeedFactor` property when character is crouching.</li></ul> |
| `Dead` | <ul><li>`BreakJointsOnDeath` — Corresponds to `Class.Humanoid.BreakJointsOnDeath`.</li><li>`Health` — Corresponds to `Class.Humanoid.Health`.</li><li>`MaxHealth` — Corresponds to `Class.Humanoid.MaxHealth`.</li><li>`RequiresNeck` — Corresponds to `Class.Humanoid.RequiresNeck`.</li></ul> |
| `FallingDown` | |
| `Freefall` | <ul><li>`SpeedMultiplier` — Multiplier to the `Class.AirController.MoveSpeedFactor` property when character is free‑falling. Note that the effect may be subtle when the character free‑falls for a very short duration.</li></ul> |
| `GettingUp` | |
| `Jumping` | <ul><li>`JumpHeight` — Corresponds to `Class.Humanoid.JumpHeight` and initializes from `Class.StarterPlayer.CharacterJumpHeight`.</li><li>`JumpPower` — Corresponds to `Class.Humanoid.JumpPower` and initializes from `Class.StarterPlayer.CharacterJumpPower`.</li><li>`UseJumpPower` — Corresponds to `Class.Humanoid.UseJumpPower` and initializes from `Class.StarterPlayer.CharacterUseJumpPower`.</li></ul> |
| `NoLocomotion` | |
| `Running` | <ul><li>`SpeedMultiplier` — Multiplier to the `Class.GroundController.MoveSpeedFactor` property when character is running.</li></ul> |
| `Sitting` | |
| `Slipping` | <ul><li>`MaxSlopeAngle` — Corresponds to `Class.Humanoid.MaxSlopeAngle`.</li></ul> |
| `Sprinting` | <ul><li>`SpeedMultiplier` — Multiplier to the `Class.GroundController.MoveSpeedFactor` and `Class.AirController.MoveSpeedFactor` properties when character is sprinting.</li></ul> |
| `Swimming` | <ul><li>`EnableFastRise` — Rise to surface more quickly by holding the jump input.</li><li>`SpeedMultiplier` — Multiplier to the `Class.SwimController.MoveSpeedFactor` property when character is swimming.</li></ul> |
| `Turning` | <ul><li>`UseLookDirectionInput` — Uses look-direction input instead of movement input to determine the character's facing direction.</li></ul> |

To set ability configurations for all characters through a script:

1. Create a new server-side `Class.Script` within `Class.ServerScriptService` and rename it to `AbilitiesScript`.
2. Copy and paste the following code into the new script. This example multiplies the base movement speed for the `Running` ability by `2`. Feel free to adjust other ability attributes such as those described in the table above.```lua
local Players = game:GetService("Players")
local AvatarAbilities = require("@rbx/AvatarAbilities")

local function waitForAbilityConfiguration(character, abilityName, timeout)
	local deadline = time() + timeout
	while character.Parent and time() < deadline do
		local ability = AvatarAbilities.getAbilityConfigurationForCharacter(character, abilityName)
		if ability then
			return ability
		end
		task.wait()
	end
	return nil
end

local function onCharacterAdded(character)
	local running = waitForAbilityConfiguration(character, "Running", 10)
	if running then
		-- Double base movement speed
		running:SetAttribute("SpeedMultiplier", 2)
	end
end

local function onPlayerAdded(player)
	if player.Character then
		onCharacterAdded(player.Character)
	end
	player.CharacterAdded:Connect(onCharacterAdded)
end

Players.PlayerAdded:Connect(onPlayerAdded)
for _, player in Players:GetPlayers() do
	onPlayerAdded(player)
end
```

### Controllers

In the CCL, a core `Class.ControllerManager` instance within the character model, alongside child controllers such as a `Class.GroundController`, handle the physical simulation of the character and its interaction with the environment. Abilities then interact with the `Class.ControllerManager` and its descendants to modify controller behaviors or switch between controllers.

Properties for the `Class.ControllerManager` and its controller descendants are summarized in the tables below, although these tables are not exhaustive; please consult the API [classes documentation](/docs/en-us/reference/engine/classes.md) for additional property options.

#### ControllerManager

| Property | Description |
| --- | --- |
| `Class.ControllerManager.BaseMoveSpeed\|BaseMoveSpeed` | The **base** linear movement speed used by all controllers. Controllers individually customize movement speed through their `MoveSpeedFactor` property. |
| `Class.ControllerManager.BaseTurnSpeed\|BaseTurnSpeed` | The **base** angular turning speed used by all controllers to align the character to face the desired direction. Some controllers individually customize turn speed through their `TurnSpeedFactor` property. |
| `Class.ControllerManager.UpDirection\|UpDirection` | `Datatype.Vector3` which indicates the upward-facing vector for the `Class.ControllerManager.RootPart`. |

#### Individual Controllers

| Controller | Properties |
| --- | --- |
| `Class.GroundController` | <ul><li>`Class.GroundController.MoveSpeedFactor\|MoveSpeedFactor` — Multiplier factor for the `Class.ControllerManager.BaseMoveSpeed` property while character is on the ground.</li><li>`Class.GroundController.AccelerationTime\|AccelerationTime` and `Class.GroundController.DecelerationTime\|DecelerationTime` — Time in seconds for character to accelerate to full speed and decelerate to full stop, respectively.</li><li>`Class.GroundController.TurnSpeedFactor\|TurnSpeedFactor` — Multiplier factor for the `Class.ControllerManager.BaseTurnSpeed` property (max angular velocity of a turn while character is on the ground).</li></ul> |
| `Class.AirController` | <ul><li>`Class.AirController.MoveSpeedFactor\|MoveSpeedFactor` — Multiplier factor for the `Class.ControllerManager.BaseMoveSpeed` property while character is in the air.</li><li>`Class.AirController.MoveMaxForce\|MoveMaxForce` and `Class.AirController.TurnMaxTorque\|TurnMaxTorque` — How quickly the character can accelerate and change direction in the air.</li><li>`Class.AirController.TurnSpeedFactor\|TurnSpeedFactor` — Multiplier factor for the `Class.ControllerManager.BaseTurnSpeed` property (max angular velocity of a turn while character is in the air).</li></ul> |
| `Class.ClimbController` | <ul><li>`Class.ClimbController.MoveSpeedFactor\|MoveSpeedFactor` — Multiplier factor for the `Class.ControllerManager.BaseMoveSpeed` property while character is climbing.</li></ul> |
| `Class.SwimController` | <ul><li>`Class.SwimController.MoveSpeedFactor\|MoveSpeedFactor` — Multiplier factor for the `Class.ControllerManager.BaseMoveSpeed` property while character is swimming.</li><li>`Class.SwimController.PitchMaxTorque\|PitchMaxTorque` — The maximum torque used to rotate on the local **X** axis to the desired pitch orientation.</li><li>`Class.SwimController.RollMaxTorque\|RollMaxTorque` — The maximum torque applied to rotate on the local **Z** axis to the desired roll orientation.</li></ul> |

To set controller configurations for all characters through a script:

1. Create a new server-side `Class.Script` within `Class.ServerScriptService` and rename it to `ControllerScript`.
2. Copy and paste the following code into the new script. This example increases ground‑based moving/turning speed as well adds a slight acceleration and deceleration time. Feel free to adjust other properties such as those described in the tables above or for each class as documented (`Class.ControllerManager`; `Class.GroundController`; `Class.AirController`; `Class.ClimbController`; `Class.SwimController`).

```lua
local Players = game:GetService("Players")
local AvatarAbilities = require("@rbx/AvatarAbilities")

local function waitForAbilityConfiguration(character, abilityName, timeout)
	local deadline = time() + timeout
	while character.Parent and time() < deadline do
		local ability = AvatarAbilities.getAbilityConfigurationForCharacter(character, abilityName)
		if ability then
			return ability
		end
		task.wait()
	end
	return nil
end

local function waitForChildOfClass(parent, className, timeout)
	local deadline = time() + timeout
	local child = parent:FindFirstChildOfClass(className)
	while not child and parent.Parent and time() < deadline do
		task.wait()
		child = parent:FindFirstChildOfClass(className)
	end
	return child
end

local function onCharacterAdded(character)
	-- Running provisions the ground controller when it registers
	if not waitForAbilityConfiguration(character, "Running", 10) then
		return
	end

	local controllerManager = waitForChildOfClass(character, "ControllerManager", 10)
	if controllerManager then
		local groundController = waitForChildOfClass(controllerManager, "GroundController", 10)
		if groundController then
			-- Double the move and turn speeds
			groundController.MoveSpeedFactor *= 2
			groundController.TurnSpeedFactor *= 2
			-- Add slight acceleration and deceleration
			groundController.AccelerationTime = 0.2
			groundController.DecelerationTime = 0.4
		end
	end
end

local function onPlayerAdded(player)
	if player.Character then
		onCharacterAdded(player.Character)
	end
	player.CharacterAdded:Connect(onCharacterAdded)
end

Players.PlayerAdded:Connect(onPlayerAdded)
for _, player in Players:GetPlayers() do
	onPlayerAdded(player)
end
```
