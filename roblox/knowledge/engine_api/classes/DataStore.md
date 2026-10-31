---
name: DataStore
last_updated: 2026-10-30T19:55:52Z
inherits:
  - GlobalDataStore
  - Instance
  - Object
type: class
memory_category: Instances
tags:
  - NotCreatable
  - NotReplicated
summary: "A GlobalDataStore that also supports versioning, key metadata, and enumerating keys."
---

# Class: DataStore

> A [GlobalDataStore](/docs/reference/engine/classes/GlobalDataStore.md) that also supports versioning, key metadata, and
> enumerating keys.

## Description

See [Data stores](/docs/en-us/cloud-services/data-stores.md) for an
in-depth guide on data structure, management, error handling, limits, and
more.

## Methods

### Method: DataStore:GetVersionAsync

**Signature:** `DataStore:GetVersionAsync(key: string, version: string): Tuple`

This function retrieves the specified key version as well as a
[DataStoreKeyInfo](/docs/reference/engine/classes/DataStoreKeyInfo.md) instance. A version identifier can be found
through [DataStore:ListVersionsAsync()](/docs/reference/engine/classes/DataStore.md) or alternatively be the
identifier returned by [GlobalDataStore:SetAsync()](/docs/reference/engine/classes/GlobalDataStore.md).

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: DataStore*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `key` | `string` |  | Key name for which the version info is requested. If [DataStoreOptions.AllScopes](/docs/reference/engine/classes/DataStoreOptions.md) was set to true when accessing the data store through [DataStoreService:GetDataStore()](/docs/reference/engine/classes/DataStoreService.md), this key name must be prepended with the original scope as in "scope/key". |
| `version` | `string` |  | Version number of the key for which the version info is requested. |

**Returns:** `Tuple` — The value of the key at the specified version and a
[DataStoreKeyInfo](/docs/reference/engine/classes/DataStoreKeyInfo.md) instance that includes the version number,
date and time the version was created, and functions to retrieve
[UserIds](/docs/reference/engine/classes/Player.md) and metadata.

### Method: DataStore:GetVersionAtTimeAsync

**Signature:** `DataStore:GetVersionAtTimeAsync(key: string, timestamp: int64): Tuple`

This function retrieves the key version that was current at a given time
as well as a [DataStoreKeyInfo](/docs/reference/engine/classes/DataStoreKeyInfo.md) instance.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: DataStore*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `key` | `string` |  | Key name for which the version info is requested. If [DataStoreOptions.AllScopes](/docs/reference/engine/classes/DataStoreOptions.md) was set to true when accessing the data store through [DataStoreService:GetDataStore()](/docs/reference/engine/classes/DataStoreService.md), this key name must be prepended with the original scope as in "scope/key". |
| `timestamp` | `int64` |  | Unix timestamp in milliseconds for which the requested version was current. Must be greater than zero. Must not be more than ten minutes in the future. |

**Returns:** `Tuple` — The value of the key that was current at the specified time and a
[DataStoreKeyInfo](/docs/reference/engine/classes/DataStoreKeyInfo.md) instance that includes the version number,
date and time the version was created, and functions to retrieve
[UserIds](/docs/reference/engine/classes/Player.md) and metadata. `nil` if no available
version was current at the requested time.

**Retrieving DataStore Versions by Time**

The following code sample retrieves data store key versions using timestamps.

```lua
local DataStoreService = game:GetService("DataStoreService")
local dataStore = DataStoreService:GetDataStore("DataStore")
local key = "key-123"

function setData(data)
	local success, result = pcall(function()
		dataStore:SetAsync(key, data)
	end)
	if not success then
		warn(result)
	end
end

function getVersionAtTime(timestamp)
	local success, result, keyInfo = pcall(function()
		return dataStore:GetVersionAtTimeAsync(key, timestamp.UnixTimestampMillis)
	end)
	if success then
		if result == nil then
			print("No version found at time")
		else
			print(result, keyInfo.Version)
		end
	else
		warn(result)
	end
end

-- Previously ran at 2024/12/02 6:00 UTC
setData("version 1")

-- Previously ran at 2024/12/02 9:00 UTC
setData("version 2")

-- Prints "No version found at time"
local time1 = DateTime.fromUniversalTime(2024, 12, 02, 05, 00)
getVersionAtTime(time1)

-- Prints "version 1 <version>"
local time2 = DateTime.fromUniversalTime(2024, 12, 02, 07, 00)
getVersionAtTime(time2)

-- Prints "version 2 <version>"
local time3 = DateTime.fromUniversalTime(2024, 12, 02, 10, 00)
getVersionAtTime(time3)
```

### Method: DataStore:ListKeysAsync

**Signature:** `DataStore:ListKeysAsync(prefix: string, pageSize?: int, cursor: string, excludeDeleted?: boolean): DataStoreKeyPages`

This function returns a [DataStoreKeyPages](/docs/reference/engine/classes/DataStoreKeyPages.md) object for enumerating
through keys of a data store. It accepts an optional `prefix` parameter to
only locate keys whose names start with the provided prefix.

If [DataStoreOptions.AllScopes](/docs/reference/engine/classes/DataStoreOptions.md) was set to true when accessing the
data store through [DataStoreService:GetDataStore()](/docs/reference/engine/classes/DataStoreService.md), keys will be
returned with all scopes as prefixes.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: DataStore*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `prefix` | `string` |  | **(Optional)** Prefix to use for locating keys. |
| `pageSize` | `int` | `0` | **(Optional)** Number of items to be returned in each page. If no value is given, the engine sends a default value of 0 to the data store web service, which in turn defaults to 50 items per page. |
| `cursor` | `string` |  | **(Optional)** Cursor to continue iteration. |
| `excludeDeleted` | `boolean` | `false` | **(Optional)** Exclude deleted keys from being returned.  When enabled ListKeys will check up to 512 keys. If all checked keys are deleted then it will return an empty list with a cursor to continue iteration. |

**Returns:** `DataStoreKeyPages` — A [DataStoreKeyPages](/docs/reference/engine/classes/DataStoreKeyPages.md) instance that enumerates the keys as
[DataStoreKey](/docs/reference/engine/classes/DataStoreKey.md) instances.

### Method: DataStore:ListVersionsAsync

**Signature:** `DataStore:ListVersionsAsync(key: string, sortDirection?: SortDirection, minDate?: int64, maxDate?: int64, pageSize?: int): DataStoreVersionPages`

This function enumerates versions of the specified key in either ascending
or descending order specified by a [SortDirection](/docs/reference/engine/enums/SortDirection.md) parameter. It can
optionally filter the returned versions by minimum and maximum timestamp.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: DataStore*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `key` | `string` |  | Key name for the versions to list. If [DataStoreOptions.AllScopes](/docs/reference/engine/classes/DataStoreOptions.md) was set to true when accessing the data store through [DataStoreService:GetDataStore()](/docs/reference/engine/classes/DataStoreService.md), this key name must be prepended with the original scope as in "scope/key". |
| `sortDirection` | `SortDirection` | `Ascending` | **(Optional)** Enum specifying ascending or descending sort order. |
| `minDate` | `int64` | `0` | **(Optional)** Unix timestamp in milliseconds after which the versions should be listed. |
| `maxDate` | `int64` | `0` | **(Optional)** Unix timestamp in milliseconds up to which the versions should be listed. |
| `pageSize` | `int` | `0` | **(Optional)** Number of items to be returned in each page. If no value is given, the engine sends a default value of 0 to the data store web service, which in turn defaults to 1024 items per page. |

**Returns:** `DataStoreVersionPages` — A [DataStoreVersionPages](/docs/reference/engine/classes/DataStoreVersionPages.md) instance that enumerates all the
versions of the key as [DataStoreObjectVersionInfo](/docs/reference/engine/classes/DataStoreObjectVersionInfo.md) instances.

**Retrieving DataStore Versions With A Date Filter**

The following code sample retrieves all versions after a specified starting
time, sorted in ascending order.

```lua
local DataStoreService = game:GetService("DataStoreService")

local experienceStore = DataStoreService:GetDataStore("PlayerExperience")

local time = DateTime.fromUniversalTime(2020, 10, 09, 01, 42)

local listSuccess, pages = pcall(function()
	return experienceStore:ListVersionsAsync("User_1234", nil, time.UnixTimestampMillis)
end)

if listSuccess then
	local items = pages:GetCurrentPage()

	for key, info in pairs(items) do
		print("Key:", key, "; Version:", info.Version, "; Created:", info.CreatedTime, "; Deleted:", info.IsDeleted)
	end
end
```

### Method: DataStore:RemoveVersionAsync

**Signature:** `DataStore:RemoveVersionAsync(key: string, version: string): ()`

> **Deprecated:** This method is deprecated. Do not use it for new work.

This function permanently deletes the specified version of a key. Version
identifiers can be found through [DataStore:ListVersionsAsync()](/docs/reference/engine/classes/DataStore.md).

Unlike [GlobalDataStore:RemoveAsync()](/docs/reference/engine/classes/GlobalDataStore.md), this function does not
create a new "tombstone" version and the removed value cannot be retrieved
later.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: DataStore*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `key` | `string` |  | Key name for which a version is to be removed. If [DataStoreOptions.AllScopes](/docs/reference/engine/classes/DataStoreOptions.md) was set to true when accessing the data store through [DataStoreService:GetDataStore()](/docs/reference/engine/classes/DataStoreService.md), this key name must be prepended with the original scope as in "scope/key". |
| `version` | `string` |  | Version number of the key to remove. |

**Returns:** `()`

## Inherited Members

### From [GlobalDataStore](/docs/reference/engine/classes/GlobalDataStore.md)

- **Method `BatchGetAsync(keys: Array, options?: Dictionary): Dictionary`**: Returns the values of multiple keys from the data store in a single
- **Method `GetAsync(key: string, options?: DataStoreGetOptions): Tuple`**: Returns the value of a key in a specified data store and a
- **Method `IncrementAsync(key: string, delta?: int, userIds?: Array, options?: DataStoreIncrementOptions): Variant`**: Increments the value of a key by the provided amount (both must be
- **Method `OnUpdate(key: string, callback: Function): RBXScriptConnection`**: Sets a callback function to be executed any time the value associated with *(deprecated)*
- **Method `RemoveAsync(key: string): Tuple`**: Removes the specified key while also retaining an accessible version.
- **Method `SetAsync(key: string, value: Variant, userIds?: Array, options?: DataStoreSetOptions): Variant`**: Sets the value of the data store for the given key.
- **Method `UpdateAsync(key: string, transformFunction: Function): Tuple`**: Updates a key's value with a new value from the specified callback

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