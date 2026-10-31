---
title: "Spawn With Friends"
url: /docs/en-us/resources/modules/spawn-with-friends
last_updated: 2026-10-30T19:55:55Z
description: "The Spawn With Friends module automatically moves spawning players near one of their friends."
---

# Spawn With Friends

It can be challenging to locate friends in-game. The **SpawnWithFriends** [developer module](/docs/en-us/resources/modules.md) automatically moves spawning players near one of their friends present in the game. This module can also be configured to teleport a player on command instead of automatically.

> **Warning:** Before spawning occurs, in order to avoid spawning a character inside the map's geometry, the system confirms that there is enough space. Thus, this module might work better in games with large, open spaces.
## Module Usage

### Installation

To use the **SpawnWithFriends** module in a game:

1. From Studio's **Window** menu or **Home** tab toolbar, open the [Toolbox](/docs/en-us/projects/assets/toolbox.md) and select the **Creator Store** tab.
2. Make sure the **Models** sorting is selected, then click the **See All** button for **Categories**.
3. Locate and click the **Packages** tile.
4. Locate the **Spawn With Friends** module and click it, or drag-and-drop it into the 3D view.
5. In the [Explorer](/docs/en-us/studio/explorer.md) window, move the entire **SpawnWithFriends** model into `Class.ReplicatedStorage`. Upon running the game the module will begin running.

### Restricted Spawn Areas

This module may result in players spawning in restricted areas like VIP rooms, access-only spaces, etc. To prevent players from teleporting to these areas:

1. Fill the restricted area with invisible `Class.BasePart.Anchored|Anchored` blocks. Make sure `Class.BasePart.CanCollide|CanCollide`, `Class.BasePart.CanTouch|CanTouch`, and `Class.BasePart.CanQuery|CanQuery` are **disabled** for all blocks._Block filling the entire prison room to prevent players from spawning inside_
2. Using the [Tags](/docs/en-us/studio/properties.md#instance-tags) section of each block's properties, apply the tag `RestrictedSpawnArea` so that `Class.CollectionService` detects them.
3. Paste the following code into a `Class.Script` within **ServerScriptService**.```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")
local CollectionService = game:GetService("CollectionService")

local SpawnWithFriends = require(ReplicatedStorage.SpawnWithFriends)

local function validator(playerToTeleport, destinationPlayer, teleportationPoint)
	-- Iterate through all tagged parts
	for _, area in CollectionService:GetTagged("RestrictedSpawnArea") do
		local relativePosition = area.CFrame:PointToObjectSpace(teleportationPoint.Position)
		local size = area.Size
		local inXBounds = relativePosition.X < size.X / 2 and relativePosition.X > -size.X / 2
		local inZBounds = relativePosition.Z < size.Z / 2 and relativePosition.Z > -size.Z / 2
		if inXBounds and inZBounds then
			return false  -- Spawn destination is within restricted area; abort teleportation
		end
	end
	return true  -- Spawn destination doesn't overlap any restricted area; proceed with teleportation
end

SpawnWithFriends.setTeleportationValidator(validator)
```

## API Reference

### Functions

#### configure

_ configure(config: `Library.table`)_

Overrides default configuration options through the following keys/values in the `config` table. This function can only be called from a `Class.Script`.

| Key | Description | Default |
| --- | --- | --- |
| `teleportToFriendOnRespawn` | If set to `false`, teleportation to a friend will only happen manually via [teleportToRandomFriend](#teleporttorandomfriend). | true |
| `teleportDistance` | How far away players should spawn from each other, measured in studs. | 5 |
| `maxCharacterVelocity` | Characters moving faster than this value won't be picked as teleportation candidates, for instance those in moving vehicles. | 48 |
| `bypassFriendshipCheck` | If set to true, **all** players will be candidates for teleportation, not just friends. | false |
| `showLogs` | Whether or not to display log messages in the output. | false |

```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local SpawnWithFriends = require(ReplicatedStorage.SpawnWithFriends)

SpawnWithFriends.configure({
	teleportToFriendOnRespawn = true,
	teleportDistance = 5,
	maxCharacterVelocity = 48,
	bypassFriendshipCheck = false,
	showLogs = false
})
```

#### teleportToRandomFriend

_ teleportToRandomFriend(playerToTeleport: `Class.Player`): `boolean`_

Manually triggers teleportation of a player to one of their friends in the game. Returns a boolean indicating whether or not teleportation succeeded; failure to teleport can be caused by the absence of friends in the server or the inability to find an unobstructed teleportation point. This function can only be called from a `Class.Script`.

#### setTeleportationValidator

_ setTeleportationValidator(validator: `function`)_

Allows you to perform custom pre-teleportation checks by hooking up a validator callback function. The callback receives three parameters:

| Parameter | Description |
| --- | --- |
| `playerToTeleport` | Reference to the `Class.Player` that is being teleported. |
| `destinationPlayer` | Reference to the target `Class.Player` that `playerToTeleport` is being teleported to. |
| `teleportationPoint` | `Datatype.CFrame` where `playerToTeleport` is teleporting to. |

This function and its callback can only be used in a `Class.Script` and the callback returns a boolean indicating whether teleportation should proceed. For example, the `return` logic in the following validator function ensures that the spawning player and destination player are on the same team.

```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local SpawnWithFriends = require(ReplicatedStorage.SpawnWithFriends)

-- Teleports players only if they are on the same team
local function validator(playerToTeleport, destinationPlayer, teleportationPoint)
	return playerToTeleport.Team == destinationPlayer.Team
end

SpawnWithFriends.setTeleportationValidator(validator)
```
