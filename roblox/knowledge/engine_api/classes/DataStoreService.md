---
name: DataStoreService
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
summary: "A game service that gives access to persistent data storage across places in a game."
---

# Class: DataStoreService

> A game service that gives access to persistent data storage across places in a
> game.

## Description

**DataStoreService** exposes methods for getting [GlobalDataStore](/docs/reference/engine/classes/GlobalDataStore.md) and
[OrderedDataStore](/docs/reference/engine/classes/OrderedDataStore.md) objects. Data stores can only be accessed by game
servers, so you can only use [DataStoreService](/docs/reference/engine/classes/DataStoreService.md) within a [Script](/docs/reference/engine/classes/Script.md)
or a [ModuleScript](/docs/reference/engine/classes/ModuleScript.md) that is used by a [Script](/docs/reference/engine/classes/Script.md).

See [Data stores](/docs/en-us/cloud-services/data-stores.md) for an
in-depth guide on data structure, management, error handling, limits, and
more.

## Code Samples

**DataStore Budget**

This code sample prints the request budget for all data store request types.

```lua
local DataStoreService = game:GetService("DataStoreService")

for _, enumItem in pairs(Enum.DataStoreRequestType:GetEnumItems()) do
	print(enumItem.Name, DataStoreService:GetRequestBudgetForRequestType(enumItem))
end
```

## Methods

### Method: DataStoreService:GetDataStore

**Signature:** `DataStoreService:GetDataStore(name: string, scope?: string, options?: Instance): DataStore`

This function creates a [DataStore](/docs/reference/engine/classes/DataStore.md) instance with the provided name
and scope. Subsequent calls to this method with the same name/scope will
return the same object.

Using the `scope` parameter will restrict operations to that scope by
automatically prepending the scope to keys in all operations done on the
data store. This function also accepts an optional
[DataStoreOptions](/docs/reference/engine/classes/DataStoreOptions.md) instance which includes options for enabling
[AllScopes](/docs/reference/engine/classes/DataStoreOptions.md). See
[Versioning, listing, and caching](/docs/en-us/cloud-services/data-stores/versioning-listing-and-caching.md#scopes)
for details on scope.

*Security: None · Thread Safety: Unsafe · Capabilities: DataStore*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `name` | `string` |  | Name of the data store. |
| `scope` | `string` | `global` | **(Optional)** A string specifying the scope. |
| `options` | `Instance` | `nil` | **(Optional)** A [DataStoreOptions](/docs/reference/engine/classes/DataStoreOptions.md) instance to enable experimental features and v2 API features. |

**Returns:** `DataStore` — A [DataStore](/docs/reference/engine/classes/DataStore.md) instance with provided name and optional scope.

### Method: DataStoreService:GetGlobalDataStore

**Signature:** `DataStoreService:GetGlobalDataStore(): DataStore`

This function returns the default [GlobalDataStore](/docs/reference/engine/classes/GlobalDataStore.md). If you want to
access a specific **named** data store instead, you should use the
[GetDataStore()](/docs/reference/engine/classes/DataStoreService.md) function.

Note that the [DataStore](/docs/reference/engine/classes/DataStore.md) returned by this function always uses the
scope `u`. See [Data stores](/docs/en-us/cloud-services/data-stores.md)
for details on scope.

*Security: None · Thread Safety: Unsafe · Capabilities: DataStore*

**Returns:** `DataStore` — The default [GlobalDataStore](/docs/reference/engine/classes/GlobalDataStore.md) instance.

**Get GlobalDataStore Instance**

The following example retrieves a default data store instance which behaves
like a regular [Instance](/docs/reference/engine/classes/Instance.md). Since a [GlobalDataStore](/docs/reference/engine/classes/GlobalDataStore.md) is an
[Instance](/docs/reference/engine/classes/Instance.md), functions such as [GlobalDataStore:GetChildren()](/docs/reference/engine/classes/GlobalDataStore.md) will
execute without error.

```lua
local DataStoreService = game:GetService("DataStoreService")

local GlobalDataStore = DataStoreService:GetGlobalDataStore()

print(GlobalDataStore.Name)
```

### Method: DataStoreService:GetOrderedDataStore

**Signature:** `DataStoreService:GetOrderedDataStore(name: string, scope?: string): OrderedDataStore`

This method returns an [OrderedDataStore](/docs/reference/engine/classes/OrderedDataStore.md), similar to the way
[GetDataStore()](/docs/reference/engine/classes/DataStoreService.md) does with
[GlobalDataStores](/docs/reference/engine/classes/GlobalDataStore.md). Subsequent calls to this method
with the same name/scope will return the same object.

*Security: None · Thread Safety: Unsafe · Capabilities: DataStore*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `name` | `string` |  | Name of the ordered data store. |
| `scope` | `string` | `global` | **(Optional)** A string specifying the scope. Default is "global". |

**Returns:** `OrderedDataStore` — An [OrderedDataStore](/docs/reference/engine/classes/OrderedDataStore.md) instance with the provided name and scope.

**OrderedDataStore Basics**

This code sample demonstrates usage of an `OrderedDataStore` and pages.

```lua
local DataStoreService = game:GetService("DataStoreService")
local pointsStore = DataStoreService:GetOrderedDataStore("Points")

local function printTopTenPlayers()
	local isAscending = false
	local pageSize = 10
	local pages = pointsStore:GetSortedAsync(isAscending, pageSize)
	local topTen = pages:GetCurrentPage()

	-- The data in 'topTen' is stored with the index being the index on the page
	-- For each item, 'data.key' is the key in the OrderedDataStore and 'data.value' is the value
	for rank, data in ipairs(topTen) do
		local name = data.key
		local points = data.value
		print(name .. " is ranked #" .. rank .. " with " .. points .. "points")
	end

	-- Potentially load the next page...
	--pages:AdvanceToNextPageAsync()
end

-- Create some data
pointsStore:SetAsync("Alex", 55)
pointsStore:SetAsync("Charley", 32)
pointsStore:SetAsync("Sydney", 68)

-- Display the top ten players
printTopTenPlayers()
```

### Method: DataStoreService:GetRequestBudgetForRequestType

**Signature:** `DataStoreService:GetRequestBudgetForRequestType(requestType: DataStoreRequestType): int`

This function returns the number of data store requests that the current
place can make based on the given [DataStoreRequestType](/docs/reference/engine/enums/DataStoreRequestType.md). Any
requests made that exceed this budget are subject to throttling.
Monitoring and adjusting the frequency of data store requests using this
function is recommended.

*Security: None · Thread Safety: Unsafe · Capabilities: DataStore*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `requestType` | `DataStoreRequestType` |  | The [DataStoreRequestType](/docs/reference/engine/enums/DataStoreRequestType.md) to check the budget for. |

**Returns:** `int` — The number of data store requests that can currently be made for the
specified request type.

**Print Request Budget**

```lua
local DataStoreService = game:GetService("DataStoreService")

local globalStore = DataStoreService:GetGlobalDataStore()

local function printBudget()
	local budget = DataStoreService:GetRequestBudgetForRequestType(Enum.DataStoreRequestType.SetIncrementAsync)
	print("Current set/increment budget:", budget)
end

for i = 1, 5 do
	local key = "key" .. i
	local success, err = pcall(function()
		globalStore:SetAsync(key, true)
	end)
	if success then
		printBudget()
	else
		print(err)
	end
end
```

### Method: DataStoreService:ListDataStoresAsync

**Signature:** `DataStoreService:ListDataStoresAsync(prefix: string, pageSize?: int, cursor: string): DataStoreListingPages`

Returns a [DataStoreListingPages](/docs/reference/engine/classes/DataStoreListingPages.md) object for enumerating through all
of the experience's data stores. It accepts an optional `prefix` parameter
to only locate data stores whose names start with the provided prefix.

Only data stores containing at least one object will be listed via this
function.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: DataStore*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `prefix` | `string` |  | **(Optional)** Prefix to enumerate data stores that start with the given prefix. |
| `pageSize` | `int` | `0` | **(Optional)** Number of items to be returned in each page. If no value is given, the engine sends a default value of 0 to the data store web service, which in turn defaults to 32 items per page. |
| `cursor` | `string` |  | **(Optional)** Cursor to continue iteration. |

**Returns:** `DataStoreListingPages` — [DataStoreListingPages](/docs/reference/engine/classes/DataStoreListingPages.md) instance containing
[DataStoreInfo](/docs/reference/engine/classes/DataStoreInfo.md) instances that provide details such as name,
creation time, and time last updated.

### Method: DataStoreService:SetRateLimitForRequestType

**Signature:** `DataStoreService:SetRateLimitForRequestType(requestType: DataStoreRequestType, baseLimit: int, perPlayerLimit: int): ()`

Sets the per-server rate limit (requests per minute) for a given Data
Store request type. The configured limit overrides the default rate limit
for that request type on the current server. The rate limit is calculated
as `rateLimit = baseLimit + (perPlayerLimit * numPlayers)`, where
`numPlayers` is the current number of active players on the server.
[DataStoreRequestType.OnUpdate](/docs/reference/engine/enums/DataStoreRequestType.md) and
[DataStoreRequestType.UpdateAsync](/docs/reference/engine/enums/DataStoreRequestType.md)
cannot be configured with this function. Calling this API with those
request types will result in an error.

You should call this API **once per request type during server
initialization**. We don't recommend calling this API during active
experience logic. If called multiple times, the new limit definitions will
immediately overwrite the previous ones.

The `baseLimit` and `perPlayerLimit` have different constraints depending
on the request type. See the table below for more information.

##### Constraints by Request Type

| Request Type            | baseLimit constraints | perPlayerLimit constraints |
| :---------------------- | :-------------------- | :------------------------- |
| GetAsync                | [0, 60]               | [0, 40]                    |
| SetIncrementAsync       | [0, 60]               | [0, 40]                    |
| UpdateAsync             | N/A                   | N/A                        |
| GetSortedAsync          | [0, 5]                | [0, 2]                     |
| SetIncrementSortedAsync | [0, 30]               | [0, 5]                     |
| OnUpdate                | N/A                   | N/A                        |
| ListAsync               | [0, 5]                | [0, 2]                     |
| GetVersionAsync         | [0, 5]                | [0, 2]                     |
| RemoveVersionAsync      | [0, 5]                | [0, 2]                     |
| StandardRead            | [0, 10000]            | [0, 200]                   |
| StandardWrite           | [0, 10000]            | [0, 200]                   |
| StandardList            | [0, 10000]            | [0, 200]                   |
| StandardRemove          | [0, 10000]            | [0, 200]                   |
| OrderedRead             | [0, 10000]            | [0, 200]                   |
| OrderedWrite            | [0, 10000]            | [0, 200]                   |
| OrderedList             | [0, 10000]            | [0, 200]                   |
| OrderedRemove           | [0, 10000]            | [0, 200]                   |

*Security: None · Thread Safety: Unsafe · Capabilities: DataStore*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `requestType` | `DataStoreRequestType` |  | The [DataStoreRequestType](/docs/reference/engine/enums/DataStoreRequestType.md) to configure the rate limit for. |
| `baseLimit` | `int` |  | The base number of requests allowed per minute regardless of player count. |
| `perPlayerLimit` | `int` |  | The additional number of requests per minute granted for each connected player. |

**Returns:** `()`

**Set Rate Limits**

The following example shows the initialization of a script that is used to
loop through and migrate all of the data from one standard data store to two
others, according to a hypothetical `MigrateScript` module script. It
ultimately deletes the data from the source data store.

```lua
local MigrateScript = require(script.Parent.MigrateScript)
local DataStoreService = game:GetService("DataStoreService")

DataStoreService:SetRateLimitForRequestType(Enum.DataStoreRequestType.StandardRead, 1000, 0)
DataStoreService:SetRateLimitForRequestType(Enum.DataStoreRequestType.StandardWrite, 2000, 0) -- two writes, so needs double the limit as get
DataStoreService:SetRateLimitForRequestType(Enum.DataStoreRequestType.StandardList, 100, 0)
DataStoreService:SetRateLimitForRequestType(Enum.DataStoreRequestType.StandardRemove, 1000, 0)

local sourceStore = DataStoreService:GetDataStore("ds_to_migrate")
local destinationStore1 = DataStoreService:GetDataStore("ds_destination_1")
local destinationStore2 = DataStoreService:GetDataStore("ds_destination_2")

-- Helper to wait for budget
local function waitForBudget(requestType)
	while (DataStoreService:GetRequestBudgetForRequestType(requestType) <= 0) do
		task.wait(1)
	end
end

waitForBudget(Enum.DataStoreRequestType.StandardList)

local success, pages = pcall(function()
	return sourceStore:ListKeysAsync()
end)

if success then
	while true do
		local items = pages:GetCurrentPage()

		for _, item in ipairs(items) do

			-- 1. Fetch data from Source
			waitForBudget(Enum.DataStoreRequestType.StandardRead)
			local getSuccess, value = pcall(function()
				return sourceStore:GetAsync(item.KeyName)
			end)

			if getSuccess and value ~= nil then
				-- 2. Migrate data to Destinations
				waitForBudget(Enum.DataStoreRequestType.StandardWrite)
				local setSuccess, err = pcall(function()
					destinationStore1:SetAsync(item.KeyName, MigrateScript.Migrate1(value))
				end)

				if setSuccess then
					print("Successfully migrated key to destination 1: " .. item.KeyName)
				else
					warn("Failed to migrate key to destination 1: " .. item.KeyName .. " - " .. tostring(err))
				end

waitForBudget(Enum.DataStoreRequestType.StandardWrite)
				local setSuccess, err = pcall(function()
					destinationStore2:SetAsync(item.KeyName, MigrateScript.Migrate2(value))
				end)

				if setSuccess then
					print("Successfully migrated key to destination 2: " .. item.KeyName)
				else
					warn("Failed to migrate key to destination 2: " .. item.KeyName .. " - " .. tostring(err))
				end

				-- 3. Delete data from source
				waitForBudget(Enum.DataStoreRequestType.StandardRemove)
				local deleteSuccess, err = pcall(function()
					sourceStore:RemoveAsync(item.KeyName)
				end)

				if deleteSuccess then
					print("Successfully deleted key from source: " .. item.KeyName)
				else
					warn("Failed to delete key from source: " .. item.KeyName .. " - " .. tostring(err))
				end
			else
				warn("Failed to fetch key from source: " .. item.KeyName)
			end
		end

		if pages.IsFinished then break end

		-- 3. Advance Page
		waitForBudget(Enum.DataStoreRequestType.StandardList)
		local nextSuccess = pcall(function()
			pages:AdvanceToNextPageAsync()
		end)

		if not nextSuccess then
			warn("Failed to advance to next page.")
			break
		end
	end
	print("Migration process complete.")
else
	warn("Failed to list keys.")
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