---
name: BadgeService
last_updated: 2026-10-30T19:55:52Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
tags:
  - NotCreatable
  - Service
summary: "Provides information on badges and awards them."
---

# Class: BadgeService

> Provides information on badges and awards them.

## Description

`BadgeService` provides information and functionality related to
[badges](/docs/en-us/production/publishing/badges.md). Badges are used across the
platform to recognize a player's achievements and activity. Upon awarding a
badge to a player, it is added to their inventory and displayed on their
profile page.

## Methods

### Method: BadgeService:AwardBadgeAsync

**Signature:** `BadgeService:AwardBadgeAsync(userId: User, badgeId: int64): boolean`

Grants a [Player](/docs/reference/engine/classes/Player.md) a badge with the [UserId](/docs/reference/engine/classes/Player.md) and
the badge ID.

In order to successfully award a badge:

- The player must be presently connected to the experience.
- The player must not already have the badge (note that a player may
  delete an awarded badge from their profile and be awarded the badge
  again).
- The badge must be awarded from a server script (a [Script](/docs/reference/engine/classes/Script.md) with
  [RunContext](/docs/reference/engine/classes/BaseScript.md) of [RunContext.Server](/docs/reference/engine/enums/RunContext.md) or
  [RunContext.Legacy](/docs/reference/engine/enums/RunContext.md)) or a [ModuleScript](/docs/reference/engine/classes/ModuleScript.md) eventually required
  by one, not from a client script.
- The badge must be awarded in a place that is part of the experience
  associated with the badge.
- The badge must be enabled; check this using the `IsEnabled` property of
  the badge fetched through [BadgeService:GetBadgeInfoAsync()](/docs/reference/engine/classes/BadgeService.md).

Rate limit is `50 + 35 * [number of users]` per minute.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: AssetManagement*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `userId` | `User` |  | The [Player.UserId](/docs/reference/engine/classes/Player.md) of the user the badge is to be awarded to. |
| `badgeId` | `int64` |  | The ID of the badge to be awarded. |

**Returns:** `boolean` — Boolean of `true` if the badge was awarded successfully.

**Awarding a Badge**

The following example creates an `awardBadge()` function that handles
potential errors that may occur when awarding a badge.

```lua
local BadgeService = game:GetService("BadgeService")
local Players = game:GetService("Players")

local BADGE_ID = 0

local function awardBadge(player, badgeId)
	-- Fetch badge information
	local success, badgeInfo = pcall(function()
		return BadgeService:GetBadgeInfoAsync(badgeId)
	end)

	if success then
		-- Confirm that badge can be awarded
		if badgeInfo.IsEnabled then
			-- Award badge
			local awarded, errorMessage = pcall(BadgeService.AwardBadgeAsync, BadgeService, player.UserId, badgeId)
			if not awarded then
				warn("Error while awarding badge:", errorMessage)
			end
		end
	else
		warn("Error while fetching badge info: " .. badgeInfo)
	end
end

local function onPlayerAdded(player)
	awardBadge(player, BADGE_ID)
end

Players.PlayerAdded:Connect(onPlayerAdded)
```

### Method: BadgeService:CheckUserBadgesAsync

**Signature:** `BadgeService:CheckUserBadgesAsync(userId: User, badgeIds: Array): Array`

Checks a list of badge IDs against a [UserId](/docs/reference/engine/classes/Player.md) and
returns a list of badge IDs that the player owns. This method supports
batches of up to 10 badges; use [BadgeService:UserHasBadgeAsync()](/docs/reference/engine/classes/BadgeService.md)
for single badge lookups.

When called from a server script, any [UserId](/docs/reference/engine/classes/Player.md) can be
used. If the user with the target user ID has not recently been in the
server, only badge IDs that are associated with the requesting experience
will be checked, and any badge IDs that are not associated with the
requesting experience will not be included in the response (as if they
were not owned).

For users that have recently been in the server, any badges for any
experiences can be queried, no matter who created the badge or which
experience it is used for.

In a client script (a [LocalScript](/docs/reference/engine/classes/LocalScript.md) or a [Script](/docs/reference/engine/classes/Script.md) with
[RunContext](/docs/reference/engine/classes/BaseScript.md) of [RunContext.Client](/docs/reference/engine/enums/RunContext.md)),
only the [UserId](/docs/reference/engine/classes/Player.md) of the local user whose client is
running the script can be used.

Rate limit is `10 + 5 * [number of players]` per minute in each server.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: AssetManagement*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `userId` | `User` |  | The [UserId](/docs/reference/engine/classes/Player.md) of the player to check for ownership of the specified badges. |
| `badgeIds` | `Array` |  | The list of IDs of the badges to check ownership of. Maximum length of 10. |

**Returns:** `Array` — The list of badge IDs the given user owns out of the provided badge
IDs. Empty if none of the provided badges are owned by the given user.
Not guaranteed to be in the same order as the input list. Some badge
IDs may be omitted if the user with the target `userId` has not
recently been in the server and the badge IDs are not associated with
the requesting experience.

**Checking Earned Badges in Batches**

This script checks which badges a user owns when they join the experience.

```lua
local BadgeService = game:GetService("BadgeService")
local Players = game:GetService("Players")

local badgeIds = { 0000000000, 1111111111, 2222222222 } -- Change this to a list of your badge IDs

local function onPlayerAdded(player)
	-- Check if the player has any of the badges
	local success, result = pcall(function()
		return BadgeService:CheckUserBadgesAsync(player.UserId, badgeIds)
	end)
	-- If there's an error, issue a warning and exit the function
	if not success then
		warn("Error while checking if player", player.Name, "has badges:", result)
		return
	end

	local ownedBadgeIds = result

	if #ownedBadgeIds == 0 then
		print(player.Name, "does not have any of the badges")
	else
		print(player.Name, "has the following badges:", table.concat(ownedBadgeIds, ", "))
	end
end

Players.PlayerAdded:Connect(onPlayerAdded)
```

### Method: BadgeService:GetBadgeInfoAsync

**Signature:** `BadgeService:GetBadgeInfoAsync(badgeId: int64): Dictionary`

This method fetches information about a badge given its ID and returns a
dictionary with the following fields:

| Key | Type | Description |
| --- | --- | --- |
| `Name` | string | The name of the badge. |
| `Description` | string | The description of the badge. |
| `IconImageId` | int64 | The asset ID of the image for the badge. |
| `IsEnabled` | boolean | Indicates whether the badge is available to be awarded. |
| `AwardCount` | int64 | The total number of times the badge has been awarded. |
| `PastDayAwardCount` | int64 | The number of times the badge was awarded in the past day. |
| `Rarity` | number | The rarity of the badge as a value from 0.0 (0%) to 1.0 (100%), representing the percentage of players who earned the badge in the past day. |

This method takes a brief moment to load the information from Roblox;
repeated calls will cache for a short duration.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: AssetManagement*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `badgeId` | `int64` |  | The badge ID of the badge whose information should be fetched. |

**Returns:** `Dictionary` — A dictionary of information about the specified badge.

**Getting Badge Info**

This sample prints badge information fetched via
[BadgeService:GetBadgeInfoAsync()](/docs/reference/engine/classes/BadgeService.md).

```lua
local BadgeService = game:GetService("BadgeService")

-- Fetch badge information
local success, result = pcall(function()
	return BadgeService:GetBadgeInfoAsync(00000000) -- Change this to desired badge ID
end)

-- Output the information
if success then
	print("Badge:", result.Name)
	print("Enabled:", result.IsEnabled)
	print("Description:", result.Description)
	print("Icon:", "rbxassetid://" .. result.IconImageId)
else
	warn("Error while fetching badge info:", result)
end
```

### Method: BadgeService:GetUserBadgesAsync

**Signature:** `BadgeService:GetUserBadgesAsync(userId: User, badgeIds: Array): Array`

Checks a list of badge IDs against a [User](/docs/reference/engine/datatypes/User.md) and returns, for each
badge the player owns, a dictionary containing the badge's ID and the date
it was awarded. This method supports batches of up to 100 badges; use
[BadgeService:UserHasBadgeAsync()](/docs/reference/engine/classes/BadgeService.md) for single badge lookups.

Each entry in the returned list is a dictionary with the following fields:

| Key | Type | Description |
| --- | --- | --- |
| `BadgeId` | int64 | The ID of the owned badge. |
| `AwardedDate` | DateTime | The date and time the badge was awarded to the user. |

When called from a server script, any [User](/docs/reference/engine/datatypes/User.md) can be used. If the
user with the target [User](/docs/reference/engine/datatypes/User.md) has not recently been in the server,
only badge IDs that are associated with the requesting experience will be
checked, and any badge IDs that are not associated with the requesting
experience will not be included in the response (as if they were not
owned).

For users that have recently been in the server, any badges for any
experiences can be queried, no matter who created the badge or which
experience it is used for.

In a client script (a [LocalScript](/docs/reference/engine/classes/LocalScript.md) or a [Script](/docs/reference/engine/classes/Script.md) with
[RunContext](/docs/reference/engine/classes/BaseScript.md) of [RunContext.Client](/docs/reference/engine/enums/RunContext.md)),
only the [User](/docs/reference/engine/datatypes/User.md) of the local user whose client is running the
script can be used.

Rate limit is `10 + 5 * [number of players]` per minute in each server.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: AssetManagement*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `userId` | `User` |  | The [User](/docs/reference/engine/datatypes/User.md) of the player to check for ownership of the specified badges. |
| `badgeIds` | `Array` |  | The list of IDs of the badges to check ownership of. Maximum length of 100. |

**Returns:** `Array` — A list of dictionaries, one for each badge the given user owns out of
the provided badge IDs. Each dictionary contains a `BadgeId` and an
`AwardedDate`. Empty if none of the provided badges are owned by the
given user. Not guaranteed to be in the same order as the input list.
Some badge IDs may be omitted if the user with the target
[User](/docs/reference/engine/datatypes/User.md) has not recently been in the server and the badge IDs
are not associated with the requesting experience.

**Getting Earned Badges and Award Dates**

This script checks which badges a user owns and when they were awarded when
they join the experience.

```lua
local BadgeService = game:GetService("BadgeService")
local Players = game:GetService("Players")

local badgeIds = { 0000000000, 1111111111, 2222222222 } -- Change this to a list of your badge IDs

local function onPlayerAdded(player)
	-- Get which of the badges the player owns, along with when each was awarded
	local success, result = pcall(function()
		return BadgeService:GetUserBadgesAsync(player.UserId, badgeIds)
	end)
	-- If there's an error, issue a warning and exit the function
	if not success then
		warn("Error while getting badges for player", player.Name, ":", result)
		return
	end

	local ownedBadges = result

	if #ownedBadges == 0 then
		print(player.Name, "does not have any of the badges")
	else
		for _, badge in ownedBadges do
			print(player.Name, "was awarded badge", badge.BadgeId, "on", badge.AwardedDate:ToIsoDate())
		end
	end
end

Players.PlayerAdded:Connect(onPlayerAdded)
```

### Method: BadgeService:UserHasBadgeAsync

**Signature:** `BadgeService:UserHasBadgeAsync(userId: User, badgeId: int64): boolean`

Checks and returns whether a [Player](/docs/reference/engine/classes/Player.md) owns a badge given their
[UserId](/docs/reference/engine/classes/Player.md) and the badge ID. You can call this method
from a server script or a [ModuleScript](/docs/reference/engine/classes/ModuleScript.md) eventually required by one.
When calling this method from a client script (a [LocalScript](/docs/reference/engine/classes/LocalScript.md) or a
[Script](/docs/reference/engine/classes/Script.md) with [RunContext](/docs/reference/engine/classes/BaseScript.md) of
[RunContext.Client](/docs/reference/engine/enums/RunContext.md)), it only works for the local user whose client
is running the script.

When called from a server script, any [UserId](/docs/reference/engine/classes/Player.md) can be
used. If the user with the target user ID has not recently been in the
server, only badge IDs that are associated with the requesting experience
will be checked. If the requested badge ID is not associated with the
requesting experience and the target user has not recently been in the
server, the method behaves as if the badge is not owned.

For users that have recently been in the server, any badge for any
experience can be queried, no matter who created the badge or which
experience it is used for.

Rate limit is `50 + 35 * [number of players]` per minute.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: AssetManagement*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `userId` | `User` |  | The [Player.UserId](/docs/reference/engine/classes/Player.md) of the player to check for ownership of the specified badge. |
| `badgeId` | `int64` |  | The badge ID of the badge whose ownership will be checked. |

**Returns:** `boolean` — Indicates if the specified user has the specified badge.

**Checking Earned Badges**

The following script waits for any player to enter the game and checks if they
own a specific badge. This is useful for creating a restricted area with
[collision filtering](/docs/en-us/workspace/collisions.md#collision-filtering) or
[teleportation](/docs/en-us/projects/teleporting.md) that only works if a player
owns a special badge.

```lua
local BadgeService = game:GetService("BadgeService")
local Players = game:GetService("Players")

local badgeId = 00000000 -- Change this to your badge ID

local function onPlayerAdded(player)
	-- Check if the player has the badge
	local success, hasBadge = pcall(function()
		return BadgeService:UserHasBadgeAsync(player.UserId, badgeId)
	end)

	-- If there's an error, issue a warning and exit the function
	if not success then
		warn("Error while checking if player has badge!")
		return
	end

	if hasBadge then
		-- Handle player's badge ownership as needed
		print(player.Name, "has badge", badgeId)
	end
end

-- Connect "PlayerAdded" events to the "onPlayerAdded()" function
Players.PlayerAdded:Connect(onPlayerAdded)
```

### Method: BadgeService:AwardBadge

**Signature:** `BadgeService:AwardBadge(userId: User, badgeId: int64): boolean`

> **Deprecated:** Use [AwardBadgeAsync()](/docs/reference/engine/classes/BadgeService.md) instead.

Award a badge to a player given the ID of each.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: AssetManagement*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `userId` | `User` |  | The [Player.UserId](/docs/reference/engine/classes/Player.md) of the user the badge is to be awarded to. |
| `badgeId` | `int64` |  | The ID of the badge to be awarded. |

**Returns:** `boolean` — Boolean of `true` if the badge was awarded successfully.

### Method: BadgeService:IsDisabled

**Signature:** `BadgeService:IsDisabled(badgeId: int64): boolean`

> **Deprecated:** This function is deprecated. Do not use it for new work. Instead, it can be checked by calling BadgeService:GetBadgeInfoAsync() and checking the IsEnabled field.

This function returns whether the badge with the given ID is marked
**disabled** on the Roblox website. A badge can be disabled by its owner
on its page on the Roblox website, in the settings sub-menu. When a badge
is disabled, this function returns true and the badge can no longer be
awarded. A badge may be quickly re-enabled through the same menu.

In Studio, a badge can only be tested if it is **disabled**. Calling this
function with an enabled badge in Studio will return **true** and produce
a warning "Sorry, badges can only be tested if they are disabled on Roblox
game servers".

Note that even if a badge is enabled it may not necessarily be awardable
(for example if it isn't associated with the current game).

Badges that are associated with special events are a common reason for a
badge to be disabled. Often, it is easier to simply disable a badge
instead of hard-coding a time check for when some event ends.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: AssetManagement*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `badgeId` | `int64` |  | The ID of the badge. |

**Returns:** `boolean` — True if the specified badge is not available to be awarded.

### Method: BadgeService:IsLegal

**Signature:** `BadgeService:IsLegal(badgeId: int64): boolean`

> **Deprecated:** This function is deprecated and will always return true. Do not use it for new work.

This function determines if a given badge is associated with the current
game. It returns true if the badge is associated with the current game.

Badges can only be awarded from a place that is part of the game
associated with the badge. This means, for example, a developer cannot
award a badge associated with another developer's game.

Even if this returns true, a badge may still not be award-able. For
example, it may be disabled.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: AssetManagement*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `badgeId` | `int64` |  | The badge ID of the badge. |

**Returns:** `boolean` — True if the badge is associated with the current game.

### Method: BadgeService:UserHasBadge

**Signature:** `BadgeService:UserHasBadge(userId: User, badgeId: int64): boolean`

> **Deprecated:** This method has been superseded by [BadgeService:UserHasBadgeAsync()](/docs/reference/engine/classes/BadgeService.md) which should be used for new work instead.

Checks and returns whether a [Player](/docs/reference/engine/classes/Player.md) owns a badge given their
[UserId](/docs/reference/engine/classes/Player.md) and the badge ID. You can call the function
from a server script or a [ModuleScript](/docs/reference/engine/classes/ModuleScript.md) eventually required by one.
When calling the method from a client script (a [LocalScript](/docs/reference/engine/classes/LocalScript.md) or a
[Script](/docs/reference/engine/classes/Script.md) with [RunContext](/docs/reference/engine/classes/BaseScript.md) of
[RunContext.Client](/docs/reference/engine/enums/RunContext.md)), it only works for the local user whose client
is running the script.

When called from a server script, any [UserId](/docs/reference/engine/classes/Player.md) can be
used. If the user with the target user ID has not recently been in the
server, only badge IDs that are associated with the requesting experience
will be checked. If the requested badge ID is not associated with the
requesting experience and the target user has not recently been in the
server, the method behaves as if the badge is not owned.

For users that have recently been in the server, any badge for any
experience can be queried, no matter who created the badge or which
experience it is used for.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: AssetManagement*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `userId` | `User` |  | The user ID of the user. |
| `badgeId` | `int64` |  | The badge ID of the badge. |

**Returns:** `boolean` — True if the user has the badge.

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