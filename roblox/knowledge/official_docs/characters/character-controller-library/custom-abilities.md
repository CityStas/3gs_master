---
title: "Custom abilities"
url: /docs/en-us/characters/character-controller-library/custom-abilities
last_updated: 2026-10-30T19:55:38Z
description: "Custom abilities in the Character Controller Library (CCL) evaluate what a character can do, as well as enable flexible behavior composition such as a character being able to move while also aiming and crouching."
---

# Custom abilities

This guide outlines how to add a custom **dash** ability for all player characters, where activating the ability speeds the character forward in the direction it's facing, followed by a short cooldown before players can dash again.

## Enable CCL

The CCL is **opt-in** through Studio's [Avatar Settings](/docs/en-us/studio/avatar-settings.md) window. To enable it:

1. Enable the CCL beta through **File** ⟩ **Beta Features** ⟩ **AvatarAbilities Character Controller Library**.
2. From the **Avatar** tab, open [Avatar Settings](/docs/en-us/studio/avatar-settings.md).![Avatar Settings indicated in Studio's toolbar](../../assets/studio/general/Toolbar-Avatar-Settings.png)
3. Select the **Movement** tab on the left side of the window and, in the **Abilities** section, select **Character Controller Library**.![Character Controller Library toggle in the Avatar Settings window](../../assets/studio/general/Avatar-Settings-CCL.png)
4. All of the standard abilities like **Running**, **Jumping**, and **Climbing** are enabled by default. To disable any of them at runtime, uncheck the associated box.
  > **Warning:** It's not recommended to disable **Running**, as doing so will prevent characters from moving along the ground. Additionally, you should always keep **Getting Up** enabled if **Falling Down** is enabled, as a mismatch will allow characters to fall down (trip) but never get back up.

## Ability module

The first step in authoring a custom ability is to create an `AbilityDefinition` inside a `Class.ModuleScript` that can be shared between the server and client.

1. Create a `Class.ModuleScript` inside `Class.ReplicatedStorage`/`CustomAbilities` (a `Class.Folder`).
2. Rename it to `Dash` as a unique identity.
3. Paste the following supporting code into the new `Dash` script:```lua
local AvatarAbilities = require("@rbx/AvatarAbilities")

local Identifiers = AvatarAbilities.Identifiers
local Rule = AvatarAbilities.Rule
local Sensor = Identifiers.Sensor
local All, Any, Not = Rule.All, Rule.Any, Rule.Not
```

## Ability definition

The core behavior of any ability is defined through its `AbilityDefinition` (line `8`+), a Luau table that defines its identity, conditions, behavior, and lifecycle.

```lua
local AvatarAbilities = require("@rbx/AvatarAbilities")

local Identifiers = AvatarAbilities.Identifiers
local Rule = AvatarAbilities.Rule
local Sensor = Identifiers.Sensor
local All, Any, Not = Rule.All, Rule.Any, Rule.Not

local Dash: AvatarAbilities.AbilityDefinition = {
	Name = "Dash",
	Labels = { "Dashing" },
	StartsWhen = All( Sensor.Ground, Not("DashCooldown") ),
	RunsWhile = "DashWindow",
	Input = {
		InputName = "Dash",
		Mode = "Press",
		ActionSlot = 5
	},
	TimedLabels = {
		OnStart = { DashWindow = 0.2 }, -- Seconds the dash stays "active"
		OnStop = { DashCooldown = 1.0 }, -- Seconds until characters can dash again
	},
}

function Dash.OnStart(managerCtx: AvatarAbilities.ManagerContext, abilityCtx: AvatarAbilities.AbilityContext)
	local rootPart = managerCtx.AbilityOwner.PrimaryPart
	if rootPart then
		rootPart:ApplyImpulse(managerCtx.RootLookVector * 80 * rootPart.AssemblyMass)
	end
end

return Dash
```

The following table outlines every parameter in the dash ability's `AbilityDefinition` table:

| Field | Description |
| --- | --- |
| `Name` | The ability's unique identity; other abilities can reference it in conditions and conflicts. Registering two abilities with the same `Name` throws an error. For a few similar abilities, give each a different `Name` and share a common [label](/docs/en-us/characters/character-controller-library.md#labels) in `Labels`. The `Class.ModuleScript` name, not this field, determines the unique `Class.Configuration` key under the character. |
| `Labels` | A [label](/docs/en-us/characters/character-controller-library.md#labels) is a named bit in a shared world mask which acts as the coordination bus between abilities. Essentially, an active ability broadcasts its `Labels` to the world mask, while ability [conditions](/docs/en-us/characters/character-controller-library.md#conditions) (`StartsWhen` or `RunsWhile`) test the world mask and react. Abilities never call each other; they merely broadcast labels and react to labels. |
| `StartsWhen` | One or more [conditions](/docs/en-us/characters/character-controller-library.md#conditions) which are checked every frame while the ability is **inactive**; when they're all `true`, the ability can start. The notation `All()` means that **all** of the nested conditions must be `true`, specifically:<ul><li>`Sensor.Ground` — The character is standing on the ground (no air-dashing).</li><li>`Not("DashCooldown")` — The `DashCooldown` label is absent (`Not()` takes exactly one label, not a group).</li></ul> |
| `RunsWhile` | One or more [conditions](/docs/en-us/characters/character-controller-library.md#conditions) which are checked every frame while the ability is **active**; the moment they stop being `true`, the ability stops. The sole condition`RunsWhile = "DashWindow"` means the ability keeps running while the `DashWindow` label exists. `RunsWhile` holds world conditions only and input never enters it, so this field exists purely to time out the dash window on its own. See [inputs](/docs/en-us/characters/character-controller-library.md#inputs) for how `Input.Mode` (not `RunsWhile`) controls when a `Hold` or `Toggle` ability stops from its input. |
| `Input` | The [input](/docs/en-us/characters/character-controller-library.md#inputs) which triggers the ability. The CCL always adds it to `StartsWhen`.<ul><li>`InputName = "Dash"` specifies the input the ability listens to.</li><li>`Mode = "Press"` tells the ability to activate when the input is pressed.</li><li>`ActionSlot` defines the input's [action slot](#input-definition).</li></ul> |
| `TimedLabels` | Timed labels appear for a fixed number of seconds and expire on their own, independent of whether the ability is still running. `OnStart`/`OnStop` broadcast their [labels](/docs/en-us/characters/character-controller-library.md#labels) when the ability starts/stops, respectively. When the associated duration ends, the label(s) expire. |

Collectively, `StartsWhen`, `RunsWhile`, and `TimedLabels` form the dash ability's entire loop:

1. `StartsWhen = All( Sensor.Ground, Not("DashCooldown") )` — Assuming the character is on the ground and not in a dash cooldown period, `TimedLabels.OnStart` broadcasts the `DashWindow` label for `0.2` seconds.
2. `RunsWhile = "DashWindow"` keeps the dash running.
3. After `0.2` seconds, the `DashWindow` label expires, so`RunsWhile = "DashWindow"` becomes `false` and the ability stops (no need to include an `OnStop` [callback](/docs/en-us/characters/character-controller-library.md#callbacks) function).
4. `TimedLabels.OnStop` broadcasts the `DashCooldown` label for `1.0` seconds, and because `StartsWhen` contains a `Not("DashCooldown")` condition, players cannot dash again during this cooldown.
5. Once the `DashCooldown` label expires, everything resets automatically and players can attempt another dash.

Following the `AbilityDefinition` table, the `OnStart` [callback](/docs/en-us/characters/character-controller-library.md#callbacks) function runs **once** at the moment the ability activates. This is where the actual dash happens. The function's first parameter, `managerCtx`, is a `ManagerContext` object with multiple properties, including:

- `managerCtx.AbilityOwner` — The character `Class.Model`, such that `managerCtx.AbilityOwner.PrimaryPart` is the root part.
- `managerCtx.RootLookVector` — The direction the character is facing.

Dash only needs this one callback, as the impulse is applied in a single instant and the timed labels handle the rest. See [callbacks](/docs/en-us/characters/character-controller-library.md#callbacks) for info on `OnUpdate`, `OnStop`, `OnSetup`, and `OnTeardown`.

## Ability registration

Registration of custom abilities for each player character must occur on the server:

1. Place a new `Class.Script` inside `Class.ServerScriptService`.
2. Rename it to `RegisterCustomAbilities` (this script can be used to register multiple abilities in a loop).
3. Paste the following code into the script. Note that abilities are added per-character by passing the [ability module](#ability-module) as the second parameter of `addAbilityForCharacter()`, not by calling `Global.LuaGlobals.require()` on the module.

```lua
local Players = game:GetService("Players")
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local AvatarAbilities = require("@rbx/AvatarAbilities")

local CUSTOM_ABILITIES = {
	ReplicatedStorage.CustomAbilities.Dash,
	-- ...
}

local function onCharacterAdded(character: Model)
	local actor = character:WaitForChild("AbilityManagerActor", 10)
	if not actor then return end
	while not actor:IsDescendantOf(game) do actor.AncestryChanged:Wait() end

	for _, abilityModule in CUSTOM_ABILITIES do
		AvatarAbilities.addAbilityForCharacter(character, abilityModule)
	end
end

local function onPlayerAdded(player: Player)
	player.CharacterAdded:Connect(onCharacterAdded)
	if player.Character then task.spawn(onCharacterAdded, player.Character) end
end
Players.PlayerAdded:Connect(onPlayerAdded)
for _, player in Players:GetPlayers() do
	onPlayerAdded(player)
end
```

Although registration occurs on the server, ability callbacks run in both the predicted client simulation and the authoritative server simulation. Keep callback behavior deterministic so both simulations produce the same result.

## Input definition

As noted in [ability definition](#ability-definition), the `Input` definition specifies how the ability is activated. Its `ActionSlot` field defines an **action slot** which is associated with a list of `Class.InputAction|InputActions` and `Class.InputBinding|InputBindings`.

The CCL always `AND`s the generated input trigger into `StartsWhen`, and `Input.Mode` (not `RunsWhile`) controls how a `Hold` or `Toggle` ability starts and stops from that input. `RunsWhile` holds world conditions only; putting the input itself into `RunsWhile` throws an error. To make a `Hold` or `Toggle` ability outlast its input under a world condition, use `Input.OutlivesInputWhile` instead. For details and an example, see [inputs](/docs/en-us/characters/character-controller-library.md#inputs).

Several action slot input bindings are predefined by Roblox and, in the future, the [Input Action Manager](/docs/en-us/characters/input/input-action-system.md#input-action-manager) will allow you to reconfigure default input bindings for action slots as desired. Setting `ActionSlot` to `0` will choose the next available empty slot. On mobile devices, slots `1`-`7` populate to buttons on the screen (see diagram below).

| Slot | Keyboard & Mouse | Gamepad | Touch | Default Assignment |
| --- | --- | --- | --- | --- |
| `1` | `Enum.KeyCode.Space\|Space` | `Enum.KeyCode.ButtonA\|ButtonA` | ① | Jump |
| `2` | `Enum.KeyCode.LeftShift\|LeftShift` | `Enum.KeyCode.ButtonL1\|ButtonL1` | ② | Sprint |
| `3` | `Enum.KeyCode.LeftControl\|LeftControl` | `Enum.KeyCode.ButtonB\|ButtonB` | ③ | Crouch |
| `4` | `Enum.KeyCode.R\|R` | `Enum.KeyCode.ButtonX\|ButtonX` | ④ | |
| `5` | `Enum.KeyCode.MouseLeftButton\|MouseLeftButton` | `Enum.KeyCode.ButtonR2\|ButtonR2` | ⑤ | |
| `6` | `Enum.KeyCode.Q\|Q` | `Enum.KeyCode.ButtonY\|ButtonY` | ⑥ | |
| `7` | `Enum.KeyCode.X\|X` | `Enum.KeyCode.ButtonR1\|ButtonR1` | ⑦ | |
| `8` | `Enum.KeyCode.C\|C` | `Enum.KeyCode.ButtonL2\|ButtonL2` |  | |
| `9` | `Enum.KeyCode.F\|F` | `Enum.KeyCode.DPadLeft\|DPadLeft` |  | |
| `10` | `Enum.KeyCode.G\|G` | `Enum.KeyCode.DPadRight\|DPadRight` |  | |
| `11` | `Enum.KeyCode.V\|V` | `Enum.KeyCode.DPadDown\|DPadDown` |  | |
