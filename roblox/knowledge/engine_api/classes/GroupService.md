---
name: GroupService
last_updated: 2026-10-30T19:55:52Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
tags:
  - NotCreatable
  - Service
  - NotReplicated
summary: "GroupService is a service that allows developers to fetch information about a Roblox group from within a game."
---

# Class: GroupService

> GroupService is a service that allows developers to fetch information about a
> Roblox group from within a game.

## Description

`GroupService` is a service that allows developers to fetch information about
a Roblox group from within a game.

Basic information on the group, including its name, description, owner, roles
and emblem can be fetched using [GroupService:GetGroupInfoAsync()](/docs/reference/engine/classes/GroupService.md).
Lists of a group's allies and enemies can be fetched using
[GroupService:GetAlliesAsync()](/docs/reference/engine/classes/GroupService.md) and
[GroupService:GetEnemiesAsync()](/docs/reference/engine/classes/GroupService.md).

`GroupService` can also be used to fetch a list of groups a player is a member
of, using [GroupService:GetGroupsAsync()](/docs/reference/engine/classes/GroupService.md). If you wish to verify if a
player is in a group, use the [Player:IsInGroupAsync()](/docs/reference/engine/classes/Player.md) method rather
than [GroupService:GetGroupsAsync()](/docs/reference/engine/classes/GroupService.md).

The service has a number of useful applications, such as detecting if a player
is an ally or enemy upon joining the game, or prompting a player to join a
group using the [GroupService:PromptJoinAsync()](/docs/reference/engine/classes/GroupService.md) method.

## Code Samples

**Group Ally/Enemy Checker**

This code sample demonstrates how `GroupService` and
[Player:IsInGroupAsync()](/docs/reference/engine/classes/Player.md) can be used to determine whether a player is a
member of a group, or any of its allies or enemies.

Note as [GroupService:GetAlliesAsync()](/docs/reference/engine/classes/GroupService.md) and
[GroupService:GetEnemiesAsync()](/docs/reference/engine/classes/GroupService.md) use `StandardPages` objects a utility
function is used to convert them to allies.

```lua
local GroupService = game:GetService("GroupService")
local Players = game:GetService("Players")

-- Define group ID here
local GROUP_ID = 271454

-- Utility function for dealing with pages
local function pagesToArray(pages)
	local array = {}
	while true do
		for _, v in ipairs(pages:GetCurrentPage()) do
			table.insert(array, v)
		end
		if pages.IsFinished then
			break
		end
		pages:AdvanceToNextPageAsync()
	end
	return array
end

-- Get lists of allies and enemies
local alliesPages = GroupService:GetAlliesAsync(GROUP_ID)
local enemiesPages = GroupService:GetEnemiesAsync(GROUP_ID)

-- Convert to array
local allies = pagesToArray(alliesPages)
local enemies = pagesToArray(enemiesPages)

local function playerAdded(player)
	-- Check to see if the player is in the group
	if player:IsInGroupAsync(GROUP_ID) then
		print(player.Name .. " is a member!")
	else
		local isAlly, isEnemy = false, false

		-- Check to see if the player is in any ally groups
		for _, groupInfo in ipairs(allies) do
			local groupId = groupInfo.Id
			if player:IsInGroupAsync(groupId) then
				isAlly = true
				break
			end
		end

		-- Check to see if the player is in any enemy groups
		for _, groupInfo in ipairs(enemies) do
			local groupId = groupInfo.Id
			if player:IsInGroupAsync(groupId) then
				isEnemy = true
				break
			end
		end

		if isAlly and not isEnemy then
			print(player.Name .. " is an ally!")
		elseif isEnemy and not isAlly then
			print(player.Name .. " is an enemy!")
		elseif isEnemy and isAlly then
			print(player.Name .. " is both an ally and an enemy!")
		else
			print(player.Name .. " is neither an ally or an enemy!")
		end
	end
end

-- Listen for new players being added
Players.PlayerAdded:Connect(playerAdded)

-- Handle players already in game
for _, player in ipairs(Players:GetPlayers()) do
	playerAdded(player)
end
```

## Methods

### Method: GroupService:GetAlliesAsync

**Signature:** `GroupService:GetAlliesAsync(groupId: int64): StandardPages`

Returns a [StandardPages](/docs/reference/engine/classes/StandardPages.md) object including information on all of the
specified group's allies.

This pages does not include a list of group IDs but instead a list of
group information tables, mirroring the format of those returned by
[GroupService:GetGroupInfoAsync()](/docs/reference/engine/classes/GroupService.md). See below for the structure of
these tables.

```lua
group = {
    Name = "Knights of the Seventh Sanctum",
    Id = 377251,
    Owner = {
        Name = "Vilicus",
        Id = 23415609
    },
    EmblemUrl = "http://www.roblox.com/asset/?id=60428602",
    Description = "We fight alongside the balance to make sure no one becomes too powerful",
    Roles = {
        [1] = {
            Name = "Apprentice",
            Rank = 1
        },
        [2] = {
            Name = "Warrior",
            Rank = 2
        },
        [3] = {
            Name = "Earth Walker",
            Rank = 255
        }
    }
}
```

Note, as this function returns a [StandardPages](/docs/reference/engine/classes/StandardPages.md) object rather than
an array, developers may wish to convert it to an array for ease of use
(see examples).

This function has a number of useful applications, including detecting if
a player is a member of an allied group.

For enemies, use [GroupService:GetEnemiesAsync()](/docs/reference/engine/classes/GroupService.md).

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Groups*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `groupId` | `int64` |  | The group's ID. |

**Returns:** `StandardPages` — A [StandardPages](/docs/reference/engine/classes/StandardPages.md) object containing group information tables for
each of the specified group's allies.

**GroupService:GetAlliesAsync**

```lua
local Players = game:GetService("Players")
local GroupService = game:GetService("GroupService")

local GROUP_ID = 57

-- creates a table of all of the allies of a given group
local allies = {}

local pages = GroupService:GetAlliesAsync(GROUP_ID)

while true do
	for _, group in pairs(pages:GetCurrentPage()) do
		table.insert(allies, group)
	end
	if pages.IsFinished then
		break
	end
	pages:AdvanceToNextPageAsync()
end

function onPlayerAdded(player)
	for _, group in pairs(allies) do
		if player:IsInGroupAsync(group.Id) then
			print("Player is an ally!")
			break
		end
	end
end

Players.PlayerAdded:Connect(onPlayerAdded)
-- handle players who joined while the allies list was still loading
for _, player in pairs(Players:GetPlayers()) do
	onPlayerAdded(player)
end
```

**Group Ally/Enemy Checker**

This code sample demonstrates how `GroupService` and
[Player:IsInGroupAsync()](/docs/reference/engine/classes/Player.md) can be used to determine whether a player is a
member of a group, or any of its allies or enemies.

Note as [GroupService:GetAlliesAsync()](/docs/reference/engine/classes/GroupService.md) and
[GroupService:GetEnemiesAsync()](/docs/reference/engine/classes/GroupService.md) use `StandardPages` objects a utility
function is used to convert them to allies.

```lua
local GroupService = game:GetService("GroupService")
local Players = game:GetService("Players")

-- Define group ID here
local GROUP_ID = 271454

-- Utility function for dealing with pages
local function pagesToArray(pages)
	local array = {}
	while true do
		for _, v in ipairs(pages:GetCurrentPage()) do
			table.insert(array, v)
		end
		if pages.IsFinished then
			break
		end
		pages:AdvanceToNextPageAsync()
	end
	return array
end

-- Get lists of allies and enemies
local alliesPages = GroupService:GetAlliesAsync(GROUP_ID)
local enemiesPages = GroupService:GetEnemiesAsync(GROUP_ID)

-- Convert to array
local allies = pagesToArray(alliesPages)
local enemies = pagesToArray(enemiesPages)

local function playerAdded(player)
	-- Check to see if the player is in the group
	if player:IsInGroupAsync(GROUP_ID) then
		print(player.Name .. " is a member!")
	else
		local isAlly, isEnemy = false, false

		-- Check to see if the player is in any ally groups
		for _, groupInfo in ipairs(allies) do
			local groupId = groupInfo.Id
			if player:IsInGroupAsync(groupId) then
				isAlly = true
				break
			end
		end

		-- Check to see if the player is in any enemy groups
		for _, groupInfo in ipairs(enemies) do
			local groupId = groupInfo.Id
			if player:IsInGroupAsync(groupId) then
				isEnemy = true
				break
			end
		end

		if isAlly and not isEnemy then
			print(player.Name .. " is an ally!")
		elseif isEnemy and not isAlly then
			print(player.Name .. " is an enemy!")
		elseif isEnemy and isAlly then
			print(player.Name .. " is both an ally and an enemy!")
		else
			print(player.Name .. " is neither an ally or an enemy!")
		end
	end
end

-- Listen for new players being added
Players.PlayerAdded:Connect(playerAdded)

-- Handle players already in game
for _, player in ipairs(Players:GetPlayers()) do
	playerAdded(player)
end
```

### Method: GroupService:GetEnemiesAsync

**Signature:** `GroupService:GetEnemiesAsync(groupId: int64): StandardPages`

Returns a [StandardPages](/docs/reference/engine/classes/StandardPages.md) object including information on all of the
specified group's enemies.

This pages does not include a list of group IDs but instead a list of
group information tables, mirroring the format of those returned by
[GroupService:GetGroupInfoAsync()](/docs/reference/engine/classes/GroupService.md). See below for the structure of
these tables.

```lua
group = {
    Name = "Knights of the Seventh Sanctum",
    Id = 377251,
    Owner = {
        Name = "Vilicus",
        Id = 23415609
    },
    EmblemUrl = "http://www.roblox.com/asset/?id=60428602",
    Description = "We fight alongside the balance to make sure no one becomes too powerful",
    Roles = {
        [1] = {
            Name = "Apprentice",
            Rank = 1
        },
        [2] = {
            Name = "Warrior",
            Rank = 2
        },
        [3] = {
            Name = "Earth Walker",
            Rank = 255
        }
    }
}
```

Note, as this function returns a [StandardPages](/docs/reference/engine/classes/StandardPages.md) object rather than
an array, developers may wish to convert it to an array for ease of use
(see examples).

This function has a number of useful applications, including detecting if
a player is a member of an enemy group.

For allies, use [GroupService:GetAlliesAsync()](/docs/reference/engine/classes/GroupService.md).

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Groups*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `groupId` | `int64` |  | The group's ID. |

**Returns:** `StandardPages` — A [StandardPages](/docs/reference/engine/classes/StandardPages.md) object containing group information tables for
each of the specified group's enemies.

**GroupService:GetEnemiesAsync**

```lua
local Players = game:GetService("Players")
local GroupService = game:GetService("GroupService")

local GROUP_ID = 57

-- creates a list of all of the enemies of a given group
local enemies = {}

local pages = GroupService:GetEnemiesAsync(GROUP_ID)

while true do
	for _, group in pairs(pages:GetCurrentPage()) do
		table.insert(enemies, group)
	end
	if pages.IsFinished then
		break
	end
	pages:AdvanceToNextPageAsync()
end

function onPlayerAdded(player)
	for _, enemyGroup in pairs(enemies) do
		if player:IsInGroupAsync(enemyGroup.Id) then
			print("Player is an enemy!")
			break
		end
	end
end

Players.PlayerAdded:Connect(onPlayerAdded)
-- handle players who joined while the enemies list was still loading
for _, player in pairs(Players:GetPlayers()) do
	onPlayerAdded(player)
end
```

**Group Ally/Enemy Checker**

This code sample demonstrates how `GroupService` and
[Player:IsInGroupAsync()](/docs/reference/engine/classes/Player.md) can be used to determine whether a player is a
member of a group, or any of its allies or enemies.

Note as [GroupService:GetAlliesAsync()](/docs/reference/engine/classes/GroupService.md) and
[GroupService:GetEnemiesAsync()](/docs/reference/engine/classes/GroupService.md) use `StandardPages` objects a utility
function is used to convert them to allies.

```lua
local GroupService = game:GetService("GroupService")
local Players = game:GetService("Players")

-- Define group ID here
local GROUP_ID = 271454

-- Utility function for dealing with pages
local function pagesToArray(pages)
	local array = {}
	while true do
		for _, v in ipairs(pages:GetCurrentPage()) do
			table.insert(array, v)
		end
		if pages.IsFinished then
			break
		end
		pages:AdvanceToNextPageAsync()
	end
	return array
end

-- Get lists of allies and enemies
local alliesPages = GroupService:GetAlliesAsync(GROUP_ID)
local enemiesPages = GroupService:GetEnemiesAsync(GROUP_ID)

-- Convert to array
local allies = pagesToArray(alliesPages)
local enemies = pagesToArray(enemiesPages)

local function playerAdded(player)
	-- Check to see if the player is in the group
	if player:IsInGroupAsync(GROUP_ID) then
		print(player.Name .. " is a member!")
	else
		local isAlly, isEnemy = false, false

		-- Check to see if the player is in any ally groups
		for _, groupInfo in ipairs(allies) do
			local groupId = groupInfo.Id
			if player:IsInGroupAsync(groupId) then
				isAlly = true
				break
			end
		end

		-- Check to see if the player is in any enemy groups
		for _, groupInfo in ipairs(enemies) do
			local groupId = groupInfo.Id
			if player:IsInGroupAsync(groupId) then
				isEnemy = true
				break
			end
		end

		if isAlly and not isEnemy then
			print(player.Name .. " is an ally!")
		elseif isEnemy and not isAlly then
			print(player.Name .. " is an enemy!")
		elseif isEnemy and isAlly then
			print(player.Name .. " is both an ally and an enemy!")
		else
			print(player.Name .. " is neither an ally or an enemy!")
		end
	end
end

-- Listen for new players being added
Players.PlayerAdded:Connect(playerAdded)

-- Handle players already in game
for _, player in ipairs(Players:GetPlayers()) do
	playerAdded(player)
end
```

### Method: GroupService:GetGroupInfoAsync

**Signature:** `GroupService:GetGroupInfoAsync(groupId: int64): Variant`

Returns a table containing information about the given group.

The table returned is the same format as that returned in
[GroupService:GetAlliesAsync()](/docs/reference/engine/classes/GroupService.md) and
[GroupService:GetEnemiesAsync()](/docs/reference/engine/classes/GroupService.md). This format can be seen below.

```lua
group = {
    Name = "Knights of the Seventh Sanctum",
    Id = 377251,
    Owner = {
        Name = "Vilicus",
        Id = 23415609
    },
    EmblemUrl = "http://www.roblox.com/asset/?id=60428602",
    Description = "We fight alongside the balance to make sure no one becomes too powerful",
    Roles = {
        [1] = {
            Name = "Apprentice",
            Rank = 1
        },
        [2] = {
            Name = "Warrior",
            Rank = 2
        },
        [3] = {
            Name = "Earth Walker",
            Rank = 255
        }
    }
}
```

Note, if a group has no owner the Owner field will be set to `nil`.

This function has a number of useful applications, including loading the
latest description and logo of a group for display in a group base.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Groups*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `groupId` | `int64` |  | The group ID of the group. |

**Returns:** `Variant` — A dictionary of information about the group.

**GroupService:GetGroupInfoAsync**

```lua
local GroupService = game:GetService("GroupService")

local GROUP_ID = 377251

local group = GroupService:GetGroupInfoAsync(GROUP_ID)

print(group.Name .. " has the following roles:")
for _, role in ipairs(group.Roles) do
	print("Rank " .. role.Rank .. ": " .. role.Name)
end
```

**Load Group Emblem**

The code in this sample spawns a `Part` in the Workspace that includes a
texture of the given group's emblem.

```lua
local GroupService = game:GetService("GroupService")

local function getEmblemAsync(groupId)
	local groupInfo = GroupService:GetGroupInfoAsync(groupId)
	return groupInfo.EmblemUrl
end

local part = Instance.new("Part")
part.Anchored = true
part.CanCollide = false
part.Size = Vector3.new(5, 5, 1)
part.Position = Vector3.new(0, 5, 0)

local decal = Instance.new("Decal")
decal.Parent = part
part.Parent = workspace

decal.ColorMapContent = Content.fromUri(getEmblemAsync(377251))
```

### Method: GroupService:GetGroupsAsync

**Signature:** `GroupService:GetGroupsAsync(userId: User): Array`

This function returns a list of tables containing information on all of
the groups a given [Player](/docs/reference/engine/classes/Player.md) is a member of.

The list returned will include an entry for every group the player is a
member of. These entries are tables with the following fields.

| Name | Description |
| --- | --- |
| **Name** | The group's name |
| **Id** | The group ID |
| **EmblemUrl** | An asset url linking to the group's thumbnail (for example: http://www.roblox.com/asset/?id=276165514) |
| **EmblemId** | The assetId of the emblem, the same which is used in the EmblemUrl |
| **Rank** _(deprecated)_ | The rankId the player has. Deprecated: players may now hold more than one role in a group. Use [GroupService:GetRolesInGroupAsync()](/docs/reference/engine/classes/GroupService.md) instead. |
| **Role** _(deprecated)_ | The name of the player's group rank. Deprecated: players may now hold more than one role in a group. Use [GroupService:GetRolesInGroupAsync()](/docs/reference/engine/classes/GroupService.md) instead. |
| **IsPrimary** | A boolean indicating if this is the player's primary group |
| **IsInClan** _(deprecated)_ | Always `false`. Deprecated: the Clans feature has been sunset. |

Note unlike [GroupService:GetAlliesAsync()](/docs/reference/engine/classes/GroupService.md) and
[GroupService:GetEnemiesAsync()](/docs/reference/engine/classes/GroupService.md), GetGroupsAsync returns a table
rather than a [StandardPages](/docs/reference/engine/classes/StandardPages.md) object.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Groups*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `userId` | `User` |  | The [Player.UserId](/docs/reference/engine/classes/Player.md) of the user. |

**Returns:** `Array` — An array of dictionaries containing information on the group's the
[Player](/docs/reference/engine/classes/Player.md) is a member of.

**Getting the Groups that a User is A Member Of**

This code sample will print information on all of the groups a player is a
member of when they join the game, using
[GroupService:GetGroupsAsync()](/docs/reference/engine/classes/GroupService.md).

```lua
local GroupService = game:GetService("GroupService")
local Players = game:GetService("Players")

local function playerAdded(player)
	-- load a list of info on all groups the player is a member of
	local groups = GroupService:GetGroupsAsync(player.UserId)

	for _, groupInfo in pairs(groups) do
		for key, value in pairs(groupInfo) do
			print(key .. ": " .. tostring(value))
		end

		print("--")
	end
end

Players.PlayerAdded:Connect(playerAdded)

-- go through existing players
for _, player in pairs(Players:GetPlayers()) do
	playerAdded(player)
end
```

### Method: GroupService:GetRolesInGroupAsync

**Signature:** `GroupService:GetRolesInGroupAsync(userId: User, groupId: int64): Variant`

Returns a table describing all roles the specified user holds in the
specified group. In a multi-role world, a user may belong to more than one
role simultaneously.

The returned table has the following structure:

| Key      | Type    | Description                                                       |
| -------- | ------- | ----------------------------------------------------------------- |
| IsMember | boolean | `true` if the user is a member of the group                       |
| Roles    | array   | Array of role tables (empty if not a member or no non-base roles) |

Each entry in the `Roles` array has the following structure:

| Key  | Type    | Description              |
| ---- | ------- | ------------------------ |
| Id   | integer | Unique role ID           |
| Name | string  | Display name of the role |
| Rank | integer | Rank value (0–255)       |

The `Roles` array is ordered from the highest role to the lowest role.
Only public roles are included. A role's `Rank` value is retained for
backwards compatibility, but does not determine its position in the role
hierarchy. Use the stable `Id` to identify a role.

This method supersedes [Player:GetRankInGroupAsync()](/docs/reference/engine/classes/Player.md) and
[Player:GetRoleInGroupAsync()](/docs/reference/engine/classes/Player.md), which return only the member's
highest public role.

This call may not yield the most up-to-date information. Results are
cached per user and group, so multiple calls with the same `userId` and
`groupId` may yield the same result until the cache expires. The caching
behavior is on a per-peer basis: a server does not share the same cache as
a client.

When a player joins a group in-experience due to a call to
[GroupService:PromptJoinAsync()](/docs/reference/engine/classes/GroupService.md), any cached result for that player
and group will be cleared on the client where the prompt was shown.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Groups*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `userId` | `User` |  | The user's ID. |
| `groupId` | `int64` |  | The group's ID. |

**Returns:** `Variant` — A table with two fields: `IsMember` (boolean) and `Roles` (array of
public role tables). Each role table contains `Id` (integer), `Name`
(string), and `Rank` (integer). The array is ordered from highest to
lowest role.

**Get Roles In Group Async**

Demonstrates [GroupService:GetRolesInGroupAsync()](/docs/reference/engine/classes/GroupService.md).

```lua
local GroupService = game:GetService("GroupService")
local Players = game:GetService("Players")

local GROUP_ID = 377251
local localPlayer = Players.LocalPlayer

local result = GroupService:GetRolesInGroupAsync(localPlayer.UserId, GROUP_ID)
if result.IsMember then
    print("User is a member with", #result.Roles, "role(s)")
    for _, role in ipairs(result.Roles) do
        print(role.Name, "rank", role.Rank)
    end
else
    print("User is not a member")
end
```

### Method: GroupService:PromptJoinAsync

**Signature:** `GroupService:PromptJoinAsync(groupId: int64): GroupMembershipStatus`

`PromptJoinAsync()` displays a prompt to the local player through which
they may join the specified Roblox group. The group must exist and the
player must meet the eligibility criteria to join. If the player is
ineligible, this method will return [GroupMembershipStatus.None](/docs/reference/engine/enums/GroupMembershipStatus.md).

Note that you can use [Player:IsInGroupAsync()](/docs/reference/engine/classes/Player.md) to check the
player's current membership status before calling this method.

If the player successfully joins, any cached results from
[GroupService:GetRolesInGroupAsync()](/docs/reference/engine/classes/GroupService.md),
[Player:GetRankInGroupAsync()](/docs/reference/engine/classes/Player.md), and
[Player:GetRoleInGroupAsync()](/docs/reference/engine/classes/Player.md) for that player and group will be
cleared on the client where the prompt was shown.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Groups*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `groupId` | `int64` |  | ID of the group to prompt the player to join. This must be a valid group ID. |

**Returns:** `GroupMembershipStatus` — [GroupMembershipStatus](/docs/reference/engine/enums/GroupMembershipStatus.md) indicating the player's group membership
status after the prompt is closed. If the player closes the prompt
without joining, this will return [GroupMembershipStatus.None](/docs/reference/engine/enums/GroupMembershipStatus.md) or
their previous status if they were already a member.

**Prompting a player to join a group**

This code sample demonstrates how to prompt a player to join a group, using
[GroupService:PromptJoinAsync()](/docs/reference/engine/classes/GroupService.md).

```lua
local GroupService = game:GetService("GroupService")

local GROUP_ID = 377251

-- This should be done in a script running on the client
local success, result = pcall(function()
    return GroupService:PromptJoinAsync(GROUP_ID)
end)

if success then
    if result == Enum.GroupMembershipStatus.Joined then
        print("Player joined the group!")
    elseif result == Enum.GroupMembershipStatus.JoinRequestPending then
        print("Player has an outstanding join request")
    elseif result == Enum.GroupMembershipStatus.AlreadyMember then
        print("Already a member")
    else
        print("Did not join or not eligible")
    end
else
    warn("Prompt failed:", result)
end
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