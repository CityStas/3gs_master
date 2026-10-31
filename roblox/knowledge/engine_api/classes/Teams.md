---
name: Teams
last_updated: 2026-10-30T19:55:53Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
tags:
  - NotCreatable
  - Service
summary: "The Teams service holds a game's Team objects. Team objects must be parented to the Teams service."
---

# Class: Teams

> The Teams service holds a game's [Team](/docs/reference/engine/classes/Team.md) objects. [Team](/docs/reference/engine/classes/Team.md) objects
> must be parented to the Teams service.

## Description

The Teams service holds a game's [Team](/docs/reference/engine/classes/Team.md) objects. [Team](/docs/reference/engine/classes/Team.md) objects
must be parented to the Teams service.

Teams offer a range of features that are useful to developers. These can
broadly be divided into features that work out-of-the-box and features
developers can program into their game.

**Built-in team behavior** The following functionality of Teams exists by
default and does not require the developer to program any custom behavior.

- When part of a Team, the name above a player's character [Model](/docs/reference/engine/classes/Model.md) will
  be colored to the [Team.TeamColor](/docs/reference/engine/classes/Team.md)
- Changing [Player.TeamColor](/docs/reference/engine/classes/Player.md) will cause [Player.Team](/docs/reference/engine/classes/Player.md) switch to
  the Team with the corresponding [Team.TeamColor](/docs/reference/engine/classes/Team.md)
- When using the default player list users will be grouped and displayed by
  team
- Setting [Player.Neutral](/docs/reference/engine/classes/Player.md) to true will cause the [Player](/docs/reference/engine/classes/Player.md) to be
  dis-associated with the team, but will not change [Player.Team](/docs/reference/engine/classes/Player.md) or
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

**Optional extended team behavior** Many developers chose to add the following
features to teams in their own code.

- Implement checks for team in weapon code to prevent team killing
- Implement doors or other features that only certain teams can use
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

## Methods

### Method: Teams:GetTeams

**Signature:** `Teams:GetTeams(): List<Team>`

The GetTeam function returns a table containing the game's [Team](/docs/reference/engine/classes/Team.md)
objects.

Note this will only return Team objects that are directly parented to the
[Teams](/docs/reference/engine/classes/Teams.md) service. For this reason it is recommended developers only
parent [Team](/docs/reference/engine/classes/Team.md) objects to the [Teams](/docs/reference/engine/classes/Teams.md) service and not to other
[Instances](/docs/reference/engine/classes/Instance.md) (or to each other).

*Security: None · Thread Safety: Unsafe · Capabilities: Players*

**Returns:** `List<Team>` — An array of [Teams](/docs/reference/engine/classes/Team.md) in the game.

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

### Method: Teams:RebalanceTeams

**Signature:** `Teams:RebalanceTeams(): ()`

> **Deprecated:** This function has been deprecated and no longer functions correctly. It should not be used. Developers should instead implement their own team sorting systems.

Evens the number of people on each team. This function does not work
correctly and should not be used.

*Security: None · Thread Safety: Unsafe · Capabilities: Players*

**Returns:** `()`

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