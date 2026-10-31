---
title: "Character name/health display"
url: /docs/en-us/characters/name-health-display
last_updated: 2026-10-30T19:55:38Z
description: "You can customize character UI, like name and health displays, using Class.Humanoid."
---

# Character name/health display

The `Class.Humanoid` instance is used to create character models, both for user avatars and NPCs. When a `Class.Humanoid` is present inside a `Class.Model` that contains a part named **Head**, Roblox displays a name and/or health bar above that part.

![Character display information above an in-game avatar](../assets/avatar/name-health-display/Display-Indicated.jpg)

Through various `Class.Humanoid` properties, you can modify the following:

- The [distance](#display-distance-type) from which users can see the name/health of other humanoids in relation to their own character's humanoid.
- The [display name](#override-display-names) which shows over a humanoid.
- Whether a humanoid's [health bar](#health-display-type) always appears, never appears, or only appears when the humanoid is damaged.
- Whether names and health bars are [occluded](#occlusion) (hidden) when line-of-sight between the camera and another humanoid is blocked.

> **Warning:** As noted in the introduction, character name/health display requires that the `Class.Humanoid` instance is inside a `Class.Model` and that the model contains a `Class.BasePart` named **Head**. Both objects must also be at the same level in the model's hierarchy.
## Display properties

### Display distance type

The `Class.Humanoid.DisplayDistanceType` property sets how users see the name/health of other characters in relation to their own character.

#### Viewer

When a humanoid's `Class.Humanoid.DisplayDistanceType|DisplayDistanceType` is set to `Enum.HumanoidDisplayDistanceType|HumanoidDisplayDistanceType.Viewer`, it sees the name/health of other humanoids within range of its own `Class.Humanoid.NameDisplayDistance|NameDisplayDistance` and `Class.Humanoid.HealthDisplayDistance|HealthDisplayDistance`. You can consider this the lowest priority since it is not taken into account for other humanoids configured as [subject](#subject) or [none](#none).

In the following scenario, the user's character (**Viewer**) has a larger `Class.Humanoid.NameDisplayDistance|NameDisplayDistance` than `Class.Humanoid.HealthDisplayDistance|HealthDisplayDistance`, as indicated by the circles. As a result, the user sees character names for both **Watchman** and **Octavia**, but only sees a health bar for **Watchman**.

#### Subject

When a humanoid's `Class.Humanoid.DisplayDistanceType|DisplayDistanceType` is set to `Enum.HumanoidDisplayDistanceType|HumanoidDisplayDistanceType.Subject`, it takes **full control** over its own name and health display through its `Class.Humanoid.NameDisplayDistance|NameDisplayDistance` and `Class.Humanoid.HealthDisplayDistance|HealthDisplayDistance` values. Effectively, other humanoids will only see the subject's name/health within those distances from the **subject** humanoid.

In the following scenario, both **Watchman** and **Octavia** are set to **Subject** and their `Class.Humanoid.NameDisplayDistance|NameDisplayDistance` ranges are indicated by the circles. Only the name **Octavia** is seen by the user whose character is standing inside her range but outside the **Watchman** humanoid's range.

#### None

When a humanoid's `Class.Humanoid.DisplayDistanceType|DisplayDistanceType` is set to `Enum.HumanoidDisplayDistanceType|HumanoidDisplayDistanceType.None`, its name and health bar do not appear under any circumstances. In the following scenario, both **Watchman** and **Octavia** are set to **None**, so the other character does not see their name or health even when in range.

### Health display type

The `Class.Humanoid.HealthDisplayType` property provides further control over the character's health bar visibility. The bar reflects the humanoid's `Class.Humanoid.Health|Health` as a factor of its `Class.Humanoid.MaxHealth|MaxHealth` and it changes color from green to yellow to red as the humanoid's health decreases.

#### AlwaysOn

When a humanoid's `Class.Humanoid.HealthDisplayType|HealthDisplayType` is set to `Enum.HumanoidHealthDisplayType|HumanoidHealthDisplayType.AlwaysOn`, its health bar always appears.

#### DisplayWhenDamaged

A humanoid with `Class.Humanoid.HealthDisplayType|HealthDisplayType` set to `Enum.HumanoidHealthDisplayType|HumanoidHealthDisplayType.DisplayWhenDamaged` only shows a health bar when its `Class.Humanoid.Health|Health` is less than its `Class.Humanoid.MaxHealth|MaxHealth`. In the following scenario, **Watchman** has full health and does not display a health bar, but **Octavia** is damaged by 50% and displays a yellow health bar.

#### AlwaysOff

When a humanoid's `Class.Humanoid.HealthDisplayType|HealthDisplayType` is set to `Enum.HumanoidHealthDisplayType|HumanoidHealthDisplayType.AlwaysOff`, its health bar never appears under any circumstances.

### Occlusion

Occlusion (hiding) of humanoid names behind walls or other objects is controlled by the character's `Class.Humanoid.NameOcclusion` property.

> **Warning:** Occlusion does not occur if the occluding object's `Class.BasePart.Transparency|Transparency` is higher than 0.99. Occlusion also does not occur when a humanoid is hidden behind a `Class.Model` containing a `Class.Humanoid`, such as another user's avatar character.
#### NoOcclusion

When a humanoid is hidden behind a visible object and its `Class.Humanoid.NameOcclusion|NameOcclusion` is set to `Enum.NameOcclusion|NameOcclusion.NoOcclusion`, its name and health are never occluded from viewing humanoids.

In the following scenario, both **Watchman** and **Octavia** are set to **NoOcclusion**. Although both are sufficiently hidden behind stone columns, the viewing humanoid still sees their name/health displays.

#### OccludeAll

When a humanoid is hidden behind a visible object and its `Class.Humanoid.NameOcclusion|NameOcclusion` is set to `Enum.NameOcclusion|NameOcclusion.OccludeAll`, its name and health are always occluded from viewing humanoids.

In the following scenario, both **Watchman** and **Octavia** are sufficiently hidden behind stone columns. **Watchman** is set to **OccludeAll**, so its name and health are hidden from the viewing humanoid. **Octavia**, however, is set to [NoOcclusion](#noocclusion) and her name/health remains visible to the viewing humanoid.

#### EnemyOcclusion

When a humanoid is hidden behind a visible object and its `Class.Humanoid.NameOcclusion|NameOcclusion` is set to `Enum.NameOcclusion|NameOcclusion.EnemyOcclusion`, its name and health are only occluded from enemy humanoids (players on a different `Class.Team`).

In the following scenario, both **Watchman** and **Octavia** are sufficiently hidden behind stone columns, and both are set to **EnemyOcclusion**. The viewing humanoid and **Watchman** are on the same `Class.Team`, so name/health occlusion does not occur. However, the name and health of **Octavia**, on the opposing team, are occluded.

## Modify character displays

### User avatars

To modify the name or health display for every incoming avatar in a game, connect the `Class.Players.PlayerAdded` and `Class.Player.CharacterAdded` events in a `Class.Script` and set [display properties](#display-properties) on the character's `Class.Humanoid`.

```lua
local Players = game:GetService("Players")

local function onPlayerAdded(player)
	player.CharacterAdded:Connect(function(character)
		local humanoid = character:FindFirstChildWhichIsA("Humanoid")
		if humanoid then
			-- Give each humanoid full control over its name/health display distance
			humanoid.DisplayDistanceType = Enum.HumanoidDisplayDistanceType.Subject
			-- Set name display distance to 20 studs
			humanoid.NameDisplayDistance = 20
			-- Set health bar display distance to 15 studs
			humanoid.HealthDisplayDistance = 15
			-- Only show health bar when humanoid is damaged
			humanoid.HealthDisplayType = Enum.HumanoidHealthDisplayType.DisplayWhenDamaged
		end
	end)
end

Players.PlayerAdded:Connect(onPlayerAdded)
```

You can also customize properties based on a player's `Class.Team`, such as setting all "guard" players to a generic name, and hiding the names of all "ninja" players.

```lua
local Players = game:GetService("Players")

local function onPlayerAdded(player)
	player.CharacterAdded:Connect(function(character)
		local humanoid = character:FindFirstChildWhichIsA("Humanoid")
		if humanoid then
			-- Set the name of all guards to generic "Guard"
			if player.Team.Name == "Guards" then
				humanoid.DisplayName = "Guard"
			-- Hide the name for all ninjas
			elseif player.Team.Name == "Ninjas" then
				humanoid.DisplayDistanceType = Enum.HumanoidDisplayDistanceType.None
			end
		end
	end)
end

Players.PlayerAdded:Connect(onPlayerAdded)
```

> **Info:** When a player is assigned to a `Class.Team`, their character's name appears in the same color as the team's `Class.Team.TeamColor|TeamColor`. This helps identify teammates and opposing players in team-based experiences.
### NPC characters

For NPC characters already placed in the 3D world, you can edit name/health directly on the `Class.Humanoid` object in the [Properties](/docs/en-us/studio/properties.md) window.

## Override display names

By default, a humanoid's display name matches the user's Roblox account **Display Name** which is unique and separate from their account **Username**. To show a fully custom name that's unrelated to the user's account, you can override the `Class.Humanoid.DisplayName` property.

### Set directly

You can set the `Class.Humanoid.DisplayName|DisplayName` property of any `Class.Humanoid` instance which you gain reference to through a `Class.Script`, such as the [team customization](#user-avatars) example, or directly on an [NPC](#npc-characters) character's **Humanoid** object.

### Set through user input

In some genres like roleplaying or fighting, you may want to provide a method for users to input their own character name, pet character name, etc. that's specific to the experience and isn't tied to their account display name. You can gather this input on the client side through a `Class.TextBox` name entry.

Once the input is submitted, you can pass it to the server through a [remote event](/docs/en-us/scripting/events/remote.md) and then, on the server side, listen for the remote event and assign the [filtered](/docs/en-us/ui/text-filtering.md) name to the user character's `Class.Humanoid`.

```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local changeNameEvent = ReplicatedStorage:WaitForChild("ChangeNameEvent")
changeNameEvent:FireServer("Amory")
```

```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")
local TextService = game:GetService("TextService")

-- Create remote event to receive text from client for filtering
local changeNameEvent = Instance.new("RemoteEvent")
changeNameEvent.Name = "ChangeNameEvent"
changeNameEvent.Parent = ReplicatedStorage

local function onRequestNameChange(player, newName)
	local character = player.Character
	local humanoid = character:FindFirstChildWhichIsA("Humanoid")

	local filterResult
	local success, errorMessage = pcall(function()
		filterResult = TextService:FilterStringAsync(newName, player.UserId)
	end)
	if success then
		local filteredName
		local success, errorMessage = pcall(function()
			filteredName = filterResult:GetNonChatStringForBroadcastAsync()
		end)
		if success and humanoid then
			humanoid.DisplayName = filteredName
		end
	end
end

changeNameEvent.OnServerEvent:Connect(onRequestNameChange)
```
