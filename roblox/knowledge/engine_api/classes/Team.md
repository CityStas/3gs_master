---
name: Team
last_updated: 2026-10-30T19:55:53Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
summary: "The Team class represents a faction in a Roblox place. The only valid parent for a Team is in the Teams service."
---

# Class: Team

> The [Team](/docs/reference/engine/classes/Team.md) class represents a faction in a Roblox place. The only valid
> parent for a Team is in the [Teams](/docs/reference/engine/classes/Teams.md) service.

## Description

The [Team](/docs/reference/engine/classes/Team.md) class represents a faction in a Roblox place. The only valid
parent for a Team is in the [Teams](/docs/reference/engine/classes/Teams.md) service. Teams offer a range of
features that are useful to developers that can be divided into two rough
groups:

- Features that work 'out of the box'
- Features developers can program into their game.

**Built-in Team Behavior**

The following functionality of Teams exists by default and does not require
the developer to program any custom behavior.

- When part of a Team, the name above a player's character [Model](/docs/reference/engine/classes/Model.md) will
  be colored to the [Team.TeamColor](/docs/reference/engine/classes/Team.md)
- Changing [Player.TeamColor](/docs/reference/engine/classes/Player.md) will cause [Player.Team](/docs/reference/engine/classes/Player.md) to switch
  to the Team with the corresponding [Team.TeamColor](/docs/reference/engine/classes/Team.md)
- When using the default player list users will be grouped and displayed
  together as a team
- Setting [Player.Neutral](/docs/reference/engine/classes/Player.md) to true will cause the [Player](/docs/reference/engine/classes/Player.md) to be
  disassociated with the team, but it will not change [Player.Team](/docs/reference/engine/classes/Player.md) or
  [Player.TeamColor](/docs/reference/engine/classes/Player.md)
- When a [Player](/docs/reference/engine/classes/Player.md) joins a game, they will be allocated to the team with
  [Team.AutoAssignable](/docs/reference/engine/classes/Team.md) set to true that has the fewest players. If no
  auto assignable team is available, [Player.Neutral](/docs/reference/engine/classes/Player.md) will be set to
  true
- When [SpawnLocation.Neutral](/docs/reference/engine/classes/SpawnLocation.md) is set to false, only players whose
  [Player.TeamColor](/docs/reference/engine/classes/Player.md) matches [SpawnLocation.TeamColor](/docs/reference/engine/classes/SpawnLocation.md) can spawn
  on that [SpawnLocation](/docs/reference/engine/classes/SpawnLocation.md)
- When [SpawnLocation.AllowTeamChangeOnTouch](/docs/reference/engine/classes/SpawnLocation.md) is set to true, a player's
  [Player.TeamColor](/docs/reference/engine/classes/Player.md) will change to [SpawnLocation.TeamColor](/docs/reference/engine/classes/SpawnLocation.md) when
  their character touches the [SpawnLocation](/docs/reference/engine/classes/SpawnLocation.md)

**Optional Extended Team Behaviors**

Many developers chose to add the following features to teams in their own
code.

- Implement checks in weapon code to prevent friendly fire.
- Implement checks in doors or other features that allow only certain teams to
  use them
- Periodically reassign teams to maintain team balance

## Code Samples

**Simple Team Rebalance**

This code sample includes a simple example of how to re-balance teams. When
Team.AutoAssignable is set to true players will be added to Teams in a
balanced fashion. However as Players leave the game this can lead to
unbalanced teams as players are not reallocated. This code keeps track of the
number of players in each team and, when players leave will check to see if
the teams need re-balancing.

```lua
local Teams = game:GetService("Teams")

-- create two teams
local redTeam = Instance.new("Team")
redTeam.TeamColor = BrickColor.new("Bright red")
redTeam.AutoAssignable = true
redTeam.Name = "Red Team"
redTeam.Parent = Teams

local blueTeam = Instance.new("Team")
blueTeam.TeamColor = BrickColor.new("Bright blue")
blueTeam.AutoAssignable = true
blueTeam.Name = "Blue Team"
blueTeam.Parent = Teams

-- start counting the number of players on each team
local numberRed, numberBlue = 0, 0

local function playerAdded(team)
	-- increase the team's count by 1
	if team == redTeam then
		numberRed = numberRed + 1
	elseif team == blueTeam then
		numberBlue = numberBlue + 1
	end
end

local function playerRemoved(team)
	-- decrease the team's count by 1
	if team == redTeam then
		numberRed = numberRed - 1
	elseif team == blueTeam then
		numberBlue = numberBlue - 1
	end

	-- check if the teams are unbalanced
	local bigTeam, smallTeam = nil, nil
	if (numberRed - numberBlue) > 2 then
		bigTeam = redTeam
		smallTeam = blueTeam
	elseif (numberBlue - numberRed) > 2 then
		bigTeam = blueTeam
		smallTeam = redTeam
	end

	if bigTeam then
		-- pick a random player
		local playerList = bigTeam:GetPlayers()
		local player = playerList[math.random(1, #playerList)]

		-- check the player exists
		if player then
			-- change the player's team
			player.TeamColor = smallTeam.TeamColor
			-- respawn the player
			player:LoadCharacterAsync()
		end
	end
end

-- listen for players being added / removed
blueTeam.PlayerAdded:Connect(function(_player)
	playerAdded(blueTeam)
end)

blueTeam.PlayerRemoved:Connect(function(_player)
	playerRemoved(blueTeam)
end)

redTeam.PlayerAdded:Connect(function(_player)
	playerAdded(redTeam)
end)

redTeam.PlayerRemoved:Connect(function(_player)
	playerRemoved(redTeam)
end)
```

**Team Kill Check**

This code sample includes a quick function that can be added to weapons in a
place to prevent them from team killing. It will return false when the two
players are on different teams or if either of them is neutral.

```lua
local Players = game:GetService("Players")

function checkTeamKill(playerAttack, playerVictim)
	if playerAttack.Team ~= playerVictim.Team or playerAttack.Neutral or playerVictim.Neutral then
		return false
	end
	return true
end

local players = Players:GetPlayers()

checkTeamKill(players[1], players[2])
```

**Team Only Door**

The following code sample will create a door in the Workspace that can only be
walked through by Players on the Bright red team.

```lua
local Players = game:GetService("Players")

local door = Instance.new("Part")
door.Anchored = true
door.Size = Vector3.new(7, 10, 1)
door.Position = Vector3.new(0, 5, 0)
door.Parent = workspace

local debounce = false

door.Touched:Connect(function(hit)
	if not debounce then
		debounce = true
		if hit then
			local player = Players:GetPlayerFromCharacter(hit.Parent)
			if player and player.TeamColor == BrickColor.new("Bright red") then
				door.Transparency = 0.5
				door.CanCollide = false
				task.wait(3)
				door.Transparency = 0
				door.CanCollide = true
			end
		end
		task.wait(0.5)
		debounce = false
	end
end)
```

**Team Rebalance with Party Integration**

This code sample demonstrates how to assign players to [Teams](/docs/reference/engine/classes/Team.md)
based on their [Player.PartyId](/docs/reference/engine/classes/Player.md) using the
[SocialService:GetPlayersByPartyId()](/docs/reference/engine/classes/SocialService.md) method. When a player joins the
experience, the script checks whether they're part of a party. If so, it
attempts to assign them to the same team as other party members. If no match
is found or the player isn't in a party, they're placed on the team with fewer
members to maintain balance.

```lua
local Teams = game:GetService("Teams")
local Players = game:GetService("Players")
local SocialService = game:GetService("SocialService")

local redTeam = Instance.new("Team")
redTeam.Name = "Red Team"
redTeam.TeamColor = BrickColor.Red()
redTeam.AutoAssignable = false
redTeam.Parent = Teams

local blueTeam = Instance.new("Team")
blueTeam.Name = "Blue Team"
blueTeam.TeamColor = BrickColor.Blue()
blueTeam.AutoAssignable = false
blueTeam.Parent = Teams

local function assignPlayerToTeam(player)
	local partyId = player.PartyId

	if partyId == "" then
		assignBalancedTeam(player)
		return
	end

	local teams = { redTeam, blueTeam }
	local matchingTeam = nil
	local partyPlayers = SocialService:GetPlayersByPartyId(partyId)

	for _, partyPlayer in partyPlayers do
		if partyPlayer ~= player and table.find(teams, partyPlayer.Team) then
			matchingTeam = partyPlayer.Team
			break
		end
	end

	if matchingTeam then
		player.Team = matchingTeam
		player.TeamColor = matchingTeam.TeamColor
	else
		assignBalancedTeam(player)
	end
end

function assignBalancedTeam(player)
	local redCount = #redTeam:GetPlayers()
	local blueCount = #blueTeam:GetPlayers()
	local chosenTeam = redCount <= blueCount and redTeam or blueTeam

	player.Team = chosenTeam
	player.TeamColor = chosenTeam.TeamColor
end

local function groupPlayersByParty()
	local seenPartyIds = {}
	local groupedPlayers = {}

	for _, player in Players:GetPlayers() do
		if player.PartyId == "" then
			table.insert(groupedPlayers, { player })
		elseif not table.find(seenPartyIds, player.PartyId) then
			table.insert(seenPartyIds, player.PartyId)

			local partyPlayers = SocialService:GetPlayersByPartyId(player.PartyId)
			table.insert(groupedPlayers, partyPlayers)
		end
	end

	return groupedPlayers
end

-- Call this function to rebalance teams
local function rebalanceTeams()
	local groups = groupPlayersByParty()

	table.sort(groups, function(a, b)
		return #a > #b
	end)

	for _, player in Players:GetPlayers() do
		player.Team = nil
	end

	for _, group in groups do
		local redCount = #redTeam:GetPlayers()
		local blueCount = #blueTeam:GetPlayers()

		local bestTeam
		if redCount <= blueCount then
			bestTeam = redTeam
		else
			bestTeam = blueTeam
		end

		for _, player in group do
			player.Team = bestTeam
			player.TeamColor = bestTeam.TeamColor
		end
	end

	for _, player in Players:GetPlayers() do
		player:LoadCharacterAsync()
	end
end

Players.PlayerAdded:Connect(function(player)
	assignPlayerToTeam(player)

	player:LoadCharacterAsync()

	player:GetPropertyChangedSignal("PartyId"):Connect(function()
		if player.PartyId ~= "" then
			assignPlayerToTeam(player)
		end
	end)
end)
```

## Properties

### Property: Team.AutoAssignable

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

This property determines whether [Players](/docs/reference/engine/classes/Player.md) will be
automatically placed onto the [Team](/docs/reference/engine/classes/Team.md) when joining. If multiple teams
have this property set to true, Roblox will attempt to even the teams out
when [Players](/docs/reference/engine/classes/Player.md) are added.

When a [Player](/docs/reference/engine/classes/Player.md) joins a game they will be assigned to the
[Team](/docs/reference/engine/classes/Team.md) with [Team.AutoAssignable](/docs/reference/engine/classes/Team.md) set to true that has the
fewest players. If no such team is available, [Player.Neutral](/docs/reference/engine/classes/Player.md) will
be set to true.

Note while using this property will help even out teams when players are
added, it will not do anything when players are removed. For this reason
developers may wish to implement their own team balancing system.

**Simple Team Rebalance**

This code sample includes a simple example of how to re-balance teams. When
Team.AutoAssignable is set to true players will be added to Teams in a
balanced fashion. However as Players leave the game this can lead to
unbalanced teams as players are not reallocated. This code keeps track of the
number of players in each team and, when players leave will check to see if
the teams need re-balancing.

```lua
local Teams = game:GetService("Teams")

-- create two teams
local redTeam = Instance.new("Team")
redTeam.TeamColor = BrickColor.new("Bright red")
redTeam.AutoAssignable = true
redTeam.Name = "Red Team"
redTeam.Parent = Teams

local blueTeam = Instance.new("Team")
blueTeam.TeamColor = BrickColor.new("Bright blue")
blueTeam.AutoAssignable = true
blueTeam.Name = "Blue Team"
blueTeam.Parent = Teams

-- start counting the number of players on each team
local numberRed, numberBlue = 0, 0

local function playerAdded(team)
	-- increase the team's count by 1
	if team == redTeam then
		numberRed = numberRed + 1
	elseif team == blueTeam then
		numberBlue = numberBlue + 1
	end
end

local function playerRemoved(team)
	-- decrease the team's count by 1
	if team == redTeam then
		numberRed = numberRed - 1
	elseif team == blueTeam then
		numberBlue = numberBlue - 1
	end

	-- check if the teams are unbalanced
	local bigTeam, smallTeam = nil, nil
	if (numberRed - numberBlue) > 2 then
		bigTeam = redTeam
		smallTeam = blueTeam
	elseif (numberBlue - numberRed) > 2 then
		bigTeam = blueTeam
		smallTeam = redTeam
	end

	if bigTeam then
		-- pick a random player
		local playerList = bigTeam:GetPlayers()
		local player = playerList[math.random(1, #playerList)]

		-- check the player exists
		if player then
			-- change the player's team
			player.TeamColor = smallTeam.TeamColor
			-- respawn the player
			player:LoadCharacterAsync()
		end
	end
end

-- listen for players being added / removed
blueTeam.PlayerAdded:Connect(function(_player)
	playerAdded(blueTeam)
end)

blueTeam.PlayerRemoved:Connect(function(_player)
	playerRemoved(blueTeam)
end)

redTeam.PlayerAdded:Connect(function(_player)
	playerAdded(redTeam)
end)

redTeam.PlayerRemoved:Connect(function(_player)
	playerRemoved(redTeam)
end)
```

### Property: Team.TeamColor

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
  "category": "Data",
  "capabilities": [
    "Players"
  ]
}
```

This property sets the color of the [Team](/docs/reference/engine/classes/Team.md). Determines the
[Player.TeamColor](/docs/reference/engine/classes/Player.md) property of players who are a member of the team.

A lot of Roblox's default team functionality is based on the team color,
rather than the name or object. For example,
[SpawnLocations](/docs/reference/engine/classes/SpawnLocation.md) can be assigned to a team via
[SpawnLocation.TeamColor](/docs/reference/engine/classes/SpawnLocation.md). For this reason it is recommended that
developers ensure each [Team](/docs/reference/engine/classes/Team.md) has a unique TeamColor.

Any player which is a part of a team will have their name color changed to
the team's TeamColor property. They will also be put underneath the team
heading on the player list.

**Team Only Door**

The following code sample will create a door in the Workspace that can only be
walked through by Players on the Bright red team.

```lua
local Players = game:GetService("Players")

local door = Instance.new("Part")
door.Anchored = true
door.Size = Vector3.new(7, 10, 1)
door.Position = Vector3.new(0, 5, 0)
door.Parent = workspace

local debounce = false

door.Touched:Connect(function(hit)
	if not debounce then
		debounce = true
		if hit then
			local player = Players:GetPlayerFromCharacter(hit.Parent)
			if player and player.TeamColor == BrickColor.new("Bright red") then
				door.Transparency = 0.5
				door.CanCollide = false
				task.wait(3)
				door.Transparency = 0
				door.CanCollide = true
			end
		end
		task.wait(0.5)
		debounce = false
	end
end)
```

### Property: Team.AutoColorCharacters

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

> **Deprecated:** This property is deprecated and no longer functions, it should not be used for new work.

Historically set whether or not [Player](/docs/reference/engine/classes/Player.md) character models on a team
would be colored to [Team.TeamColor](/docs/reference/engine/classes/Team.md).

Developers are advised not to use this property as the script which
changed the team colors has since been removed from the default character.
This property is deprecated and should not be used for new work.

### Property: Team.Score

```json
{
  "type": "int",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": true,
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

> **Deprecated:** This property is deprecated and should not be used in new work. For more information on how to handle leaderboards and scoring please see [this tutorial](/docs/en-us/players/leaderboards.md).

This property can be used to store an integer value associated with the
team. This property offers no additional functionality and is not used by
any game services.

This property is deprecated and should not be used by developers for new
work.

## Methods

### Method: Team:GetPlayers

**Signature:** `Team:GetPlayers(): List<Player>`

Returns a list of [Players](/docs/reference/engine/classes/Player.md) who are assigned to the
[Team](/docs/reference/engine/classes/Team.md). A [Player](/docs/reference/engine/classes/Player.md) is considered assigned if their
[Player.Team](/docs/reference/engine/classes/Player.md) property is equal to the [Team](/docs/reference/engine/classes/Team.md) and
[Player.Neutral](/docs/reference/engine/classes/Player.md) is false.

This function has a number of potential uses, including counting the
number of players on a [Team](/docs/reference/engine/classes/Team.md) or giving every [Player](/docs/reference/engine/classes/Player.md) on a
[Team](/docs/reference/engine/classes/Team.md) a [Tool](/docs/reference/engine/classes/Tool.md).

*Security: None · Thread Safety: Safe · Capabilities: Players*

**Returns:** `List<Player>` — An array of [Players](/docs/reference/engine/classes/Player.md) in the [Team](/docs/reference/engine/classes/Team.md).

**Teams GetTeams**

The example below prints the number of players on each Team.

```lua
local Teams = game:GetService("Teams")

local teams = Teams:GetTeams()

for _, team in pairs(teams) do
	local players = team:GetPlayers()
	print("Team", team.Name, "has", #players, "players")
end
```

## Events

### Event: Team.PlayerAdded

**Signature:** `Team.PlayerAdded(player: Player)`

Fires whenever a [Player](/docs/reference/engine/classes/Player.md) is assigned to the [Team](/docs/reference/engine/classes/Team.md). A player
is considered assigned if their [Player.Team](/docs/reference/engine/classes/Player.md) property is equal to
the [Team](/docs/reference/engine/classes/Team.md) and [Player.Neutral](/docs/reference/engine/classes/Player.md) is false.

This event is team specific and will only fire when a [Player](/docs/reference/engine/classes/Player.md)
joints the specific [Team](/docs/reference/engine/classes/Team.md). Any function connected to this event
will be passed the [Player](/docs/reference/engine/classes/Player.md) object of the player who joined the
team. For example:

    Team.PlayerAdded:Connect(function(player)
    	print(player.Name.." has joined the team")
    end)

*Security: None · Capabilities: Players*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `player` | `Player` | The [Player](/docs/reference/engine/classes/Player.md) that was added. |

**Simple Team Rebalance**

This code sample includes a simple example of how to re-balance teams. When
Team.AutoAssignable is set to true players will be added to Teams in a
balanced fashion. However as Players leave the game this can lead to
unbalanced teams as players are not reallocated. This code keeps track of the
number of players in each team and, when players leave will check to see if
the teams need re-balancing.

```lua
local Teams = game:GetService("Teams")

-- create two teams
local redTeam = Instance.new("Team")
redTeam.TeamColor = BrickColor.new("Bright red")
redTeam.AutoAssignable = true
redTeam.Name = "Red Team"
redTeam.Parent = Teams

local blueTeam = Instance.new("Team")
blueTeam.TeamColor = BrickColor.new("Bright blue")
blueTeam.AutoAssignable = true
blueTeam.Name = "Blue Team"
blueTeam.Parent = Teams

-- start counting the number of players on each team
local numberRed, numberBlue = 0, 0

local function playerAdded(team)
	-- increase the team's count by 1
	if team == redTeam then
		numberRed = numberRed + 1
	elseif team == blueTeam then
		numberBlue = numberBlue + 1
	end
end

local function playerRemoved(team)
	-- decrease the team's count by 1
	if team == redTeam then
		numberRed = numberRed - 1
	elseif team == blueTeam then
		numberBlue = numberBlue - 1
	end

	-- check if the teams are unbalanced
	local bigTeam, smallTeam = nil, nil
	if (numberRed - numberBlue) > 2 then
		bigTeam = redTeam
		smallTeam = blueTeam
	elseif (numberBlue - numberRed) > 2 then
		bigTeam = blueTeam
		smallTeam = redTeam
	end

	if bigTeam then
		-- pick a random player
		local playerList = bigTeam:GetPlayers()
		local player = playerList[math.random(1, #playerList)]

		-- check the player exists
		if player then
			-- change the player's team
			player.TeamColor = smallTeam.TeamColor
			-- respawn the player
			player:LoadCharacterAsync()
		end
	end
end

-- listen for players being added / removed
blueTeam.PlayerAdded:Connect(function(_player)
	playerAdded(blueTeam)
end)

blueTeam.PlayerRemoved:Connect(function(_player)
	playerRemoved(blueTeam)
end)

redTeam.PlayerAdded:Connect(function(_player)
	playerAdded(redTeam)
end)

redTeam.PlayerRemoved:Connect(function(_player)
	playerRemoved(redTeam)
end)
```

### Event: Team.PlayerRemoved

**Signature:** `Team.PlayerRemoved(player: Player)`

Fires whenever a [Player](/docs/reference/engine/classes/Player.md) is removed from a [Team](/docs/reference/engine/classes/Team.md). This can
be due to the [Player](/docs/reference/engine/classes/Player.md) leaving the game, [Player.Neutral](/docs/reference/engine/classes/Player.md)
being set to true or the [Player](/docs/reference/engine/classes/Player.md) joining a different team.

This event is team specific and will only fire when a [Player](/docs/reference/engine/classes/Player.md)
leaves the specific [Team](/docs/reference/engine/classes/Team.md). Any function connected to this event
will be passed the [Player](/docs/reference/engine/classes/Player.md) object of the player who left the team.
For example:

    Team.PlayerRemoved:Connect(function(player)
    	print(player.Name.." has left the team")
    end)

*Security: None · Capabilities: Players*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `player` | `Player` | The [Player](/docs/reference/engine/classes/Player.md) removed. |

**Simple Team Rebalance**

This code sample includes a simple example of how to re-balance teams. When
Team.AutoAssignable is set to true players will be added to Teams in a
balanced fashion. However as Players leave the game this can lead to
unbalanced teams as players are not reallocated. This code keeps track of the
number of players in each team and, when players leave will check to see if
the teams need re-balancing.

```lua
local Teams = game:GetService("Teams")

-- create two teams
local redTeam = Instance.new("Team")
redTeam.TeamColor = BrickColor.new("Bright red")
redTeam.AutoAssignable = true
redTeam.Name = "Red Team"
redTeam.Parent = Teams

local blueTeam = Instance.new("Team")
blueTeam.TeamColor = BrickColor.new("Bright blue")
blueTeam.AutoAssignable = true
blueTeam.Name = "Blue Team"
blueTeam.Parent = Teams

-- start counting the number of players on each team
local numberRed, numberBlue = 0, 0

local function playerAdded(team)
	-- increase the team's count by 1
	if team == redTeam then
		numberRed = numberRed + 1
	elseif team == blueTeam then
		numberBlue = numberBlue + 1
	end
end

local function playerRemoved(team)
	-- decrease the team's count by 1
	if team == redTeam then
		numberRed = numberRed - 1
	elseif team == blueTeam then
		numberBlue = numberBlue - 1
	end

	-- check if the teams are unbalanced
	local bigTeam, smallTeam = nil, nil
	if (numberRed - numberBlue) > 2 then
		bigTeam = redTeam
		smallTeam = blueTeam
	elseif (numberBlue - numberRed) > 2 then
		bigTeam = blueTeam
		smallTeam = redTeam
	end

	if bigTeam then
		-- pick a random player
		local playerList = bigTeam:GetPlayers()
		local player = playerList[math.random(1, #playerList)]

		-- check the player exists
		if player then
			-- change the player's team
			player.TeamColor = smallTeam.TeamColor
			-- respawn the player
			player:LoadCharacterAsync()
		end
	end
end

-- listen for players being added / removed
blueTeam.PlayerAdded:Connect(function(_player)
	playerAdded(blueTeam)
end)

blueTeam.PlayerRemoved:Connect(function(_player)
	playerRemoved(blueTeam)
end)

redTeam.PlayerAdded:Connect(function(_player)
	playerAdded(redTeam)
end)

redTeam.PlayerRemoved:Connect(function(_player)
	playerRemoved(redTeam)
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