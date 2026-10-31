---
name: MemoryStoreSortedMap
last_updated: 2026-10-30T19:55:52Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
tags:
  - NotCreatable
  - NotReplicated
summary: "Provides access to a sorted map within MemoryStoreService."
---

# Class: MemoryStoreSortedMap

> Provides access to a sorted map within [MemoryStoreService](/docs/reference/engine/classes/MemoryStoreService.md).

## Description

Provides access to a sorted map within [MemoryStoreService](/docs/reference/engine/classes/MemoryStoreService.md). A sorted
map is a collection of items where string keys are associated with arbitrary
values (up to the maximum allowed size -- see
[Memory Stores](/docs/en-us/cloud-services/memory-stores/sorted-map.md)). Each
item can also have an optional sort key, which can be a number or a string. In
the ordering of items, the sort key, if provided, takes precedence over the
key. Items with numeric sort keys are sorted before items with string sort
keys, which are sorted before items with no sort key. Items with the same sort
key and items with no sort key are arranged in alphabetical order by key.

## Methods

### Method: MemoryStoreSortedMap:GetAsync

**Signature:** `MemoryStoreSortedMap:GetAsync(key: string): Tuple`

Retrieves the value and sort key of a key in the sorted map.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: DataStore*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `key` | `string` |  | Key whose value and sort key to retrieve. |

**Returns:** `Tuple` — A tuple of two values:

- Key value, or `nil` if there's no item with the specified key.
- Sort key, or `nil` if there's no sort key associated with the
  specified key.

### Method: MemoryStoreSortedMap:GetRangeAsync

**Signature:** `MemoryStoreSortedMap:GetRangeAsync(direction: SortDirection, count: int, exclusiveLowerBound: Variant, exclusiveUpperBound: Variant): Array`

Gets items within a sorted range of keys and sort keys.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: DataStore*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `direction` | `SortDirection` |  | Sort direction, ascending or descending. |
| `count` | `int` |  | The number of items to retrieve; the maximum allowed value for this parameter is 200. |
| `exclusiveLowerBound` | `Variant` |  | **(Optional)** Lower bound, exclusive, for the returned keys. This is provided as a table where one or both of key and sort key can be specified: { key: string, sortKey: Variant } . |
| `exclusiveUpperBound` | `Variant` |  | **(Optional)** Upper bound, exclusive, for the returned keys. This is provided as a table where one or both of key and sort key can be specified: { key: string, sortKey: Variant } . |

**Returns:** `Array` — Item keys, values and sort keys in the requested range.

**Retrieving MemoryStore Keys**

The code below prints all keys in a sorted map in alphabetical order with the
help of the [MemoryStoreSortedMap:GetRangeAsync()](/docs/reference/engine/classes/MemoryStoreSortedMap.md) method.

```lua
local MemoryStoreService = game:GetService("MemoryStoreService")

local myMap = MemoryStoreService:GetSortedMap("MySortedMap")

function printAllKeys(map)
	-- the initial lower bound is nil which means to start from the very first item
	local exclusiveLowerBound = nil

	-- this loop continues until the end of the map is reached
	while true do
		-- get up to a hundred items starting from the current lower bound
		local items = map:GetRangeAsync(Enum.SortDirection.Ascending, 100, exclusiveLowerBound)

		for _, item in ipairs(items) do
			print(item.key)
			print(item.sortKey)
		end

		-- if the call returned less than a hundred items it means we've reached the end of the map
		if #items < 100 then
			break
		end

		-- the last retrieved key is the exclusive lower bound for the next iteration
		exclusiveLowerBound = {}
		exclusiveLowerBound["key"] = items[#items].key
		exclusiveLowerBound["sortKey"] = items[#items].sortKey
	end
end

printAllKeys(myMap)
```

### Method: MemoryStoreSortedMap:GetSizeAsync

**Signature:** `MemoryStoreSortedMap:GetSizeAsync(): int`

Gets the size of the sorted map.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: DataStore*

**Returns:** `int` — The number of items currently stored in the sorted map.

### Method: MemoryStoreSortedMap:RemoveAsync

**Signature:** `MemoryStoreSortedMap:RemoveAsync(key: string): ()`

Removes the provided key from the sorted map.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: DataStore*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `key` | `string` |  | Key to remove. |

**Returns:** `()`

### Method: MemoryStoreSortedMap:SetAsync

**Signature:** `MemoryStoreSortedMap:SetAsync(key: string, value: Variant, expiration: int64, sortKey: Variant): boolean`

Sets the value and sort key of the key overwriting any existing key value
and sort key.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: DataStore*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `key` | `string` |  | Key whose value to set. |
| `value` | `Variant` |  | Key value to set. |
| `expiration` | `int64` |  | Item expiration, in seconds. The item is automatically removed from the sorted map once the expiration duration is reached. The maximum expiration time is 45 days (3,888,000 seconds). |
| `sortKey` | `Variant` |  | **(Optional)** Sort key to set for this key. Accepted types are a number (integer or decimal) or a string. |

**Returns:** `boolean` — `true` if the value of an existing key was overwritten, or `false` if
a new key was added to the sorted map.

### Method: MemoryStoreSortedMap:UpdateAsync

**Signature:** `MemoryStoreSortedMap:UpdateAsync(key: string, transformFunction: Function, expiration: int64): Tuple`

Retrieves the value and sort key of a key from a sorted map and lets you
update it to a new value and sort key via a callback function.

This method accepts a callback function that transforms the old value and
old sort key into the updated value and updated sort key as required. The
method retrieves the existing key value and sort key and passes it to the
transform function which returns the new value and sort key for the item,
with these exceptions:

- If the key does not exist, the old value and old sort key passed to the
  function will be `nil`.
- If the function returns `nil`, the update is canceled.

The new value and new sort key is saved only if the key was not updated
(e.g. by a different game server) since the moment it was read. If the
value or sort key did change, the transform function is invoked again with
the most recent item value and sort key. This cycle repeats until the
value and sort key are saved successfully or the transform function
returns `nil` to abort the operation.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: DataStore*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `key` | `string` |  | Key whose value to update. |
| `transformFunction` | `Function` |  | A function which you need to provide. The function takes the key's old value and old sort key as input and returns the new value and new sort key. |
| `expiration` | `int64` |  | Item expiration time, in seconds, after which the item will be automatically removed from the sorted map. The maximum expiration time is 45 days (3,888,000 seconds). |

**Returns:** `Tuple` — The return value is a tuple of the last value and sort key returned by
the transform function.

**Updating a MemoryStore Sorted Map**

The code below updates the score in a leaderboard for a player in a game. The
score is calculated as kills / deaths. The use of
[MemoryStoreSortedMap:UpdateAsync()](/docs/reference/engine/classes/MemoryStoreSortedMap.md) ensures that the kills and deaths
are updated for the most recent values even if multiple game servers update
the same item simultaneously. A player's kills and deaths are monotonically
increasing values and can hence only increase in value in a session.

```lua
local MemoryStoreService = game:GetService("MemoryStoreService")
local map = MemoryStoreService:GetSortedMap("Leaderboard")
local Players = game:GetService("Players")

function updateLeaderboard(itemKey, killsToAdd, deathsToAdd)
	local success, newStats, newScore = pcall(function()
		return map:UpdateAsync(itemKey, function(playerStats, playerScore)
			playerStats = playerStats or { kills = 0, deaths = 0 }
			playerStats.kills += killsToAdd
			playerStats.deaths += deathsToAdd
			if playerStats then
				-- `playerScore` is the sortKey being used to sort items in the map
				playerScore = playerStats.kills / math.max(playerStats.deaths, 1)
				return playerStats, playerScore
			end
			return nil
		end, 30)
	end)
end

-- Add one kill to all players
for i, player in pairs(Players:GetPlayers()) do
	updateLeaderboard(player.UserId, 1, 0)
end
-- Add 5 kills and 1 death to player with userId 12345
updateLeaderboard(12345, 5, 1)
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