---
name: GlobalDataStore
last_updated: 2026-10-30T19:55:52Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
tags:
  - NotCreatable
  - NotReplicated
summary: "An object that exposes methods to access a single data store."
---

# Class: GlobalDataStore

> An object that exposes methods to access a single data store.

## Description

A **GlobalDataStore** exposes functions for saving and loading data for the
[DataStoreService](/docs/reference/engine/classes/DataStoreService.md).

See [Data stores](/docs/en-us/cloud-services/data-stores.md) for an
in-depth guide on data structure, management, error handling, limits, and
more.

Ordered data stores do not support versioning and metadata, so
[DataStoreKeyInfo](/docs/reference/engine/classes/DataStoreKeyInfo.md) is always `nil` for keys in an
[OrderedDataStore](/docs/reference/engine/classes/OrderedDataStore.md). If you need versioning and metadata support, use a
[DataStore](/docs/reference/engine/classes/DataStore.md).

## Methods

### Method: GlobalDataStore:BatchGetAsync

**Signature:** `GlobalDataStore:BatchGetAsync(keys: Array, options?: Dictionary): Dictionary`

This function retrieves the values of multiple keys in a single request.

This method is currently only supported on [OrderedDataStore](/docs/reference/engine/classes/OrderedDataStore.md).
Calling it on a standard [GlobalDataStore](/docs/reference/engine/classes/GlobalDataStore.md) or [DataStore](/docs/reference/engine/classes/DataStore.md) will
throw an error.

Unlike [GlobalDataStore:GetAsync()](/docs/reference/engine/classes/GlobalDataStore.md), this method does not return
[DataStoreKeyInfo](/docs/reference/engine/classes/DataStoreKeyInfo.md) since ordered data stores do not support
versioning or metadata.

The returned dictionary maps each key to a table with a `value` field. For
example, if you request keys `{"coins", "gems"}`, the result might look
like:

```lua
{
    coins = { value = 100 },
    gems = { value = 50 }
}
```

Keys that do not exist in the data store or have empty values are omitted
from the result rather than returning nil values.

#### Limits

The `keys` array must contain at least one key and no more than the
server-configured maximum (default 100). Exceeding the limit will throw an
error. Each call counts against the ordered data store read budget based
on the number of keys requested.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: DataStore*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `keys` | `Array` |  | An array of key name strings to retrieve. The maximum number of keys per request is determined by a server-side limit (default 100). |
| `options` | `Dictionary` | `nil` | **(Optional)** Unused; has no effect. |

**Returns:** `Dictionary` — A dictionary mapping each requested key (string) to a table containing
a `value` field with the key's current value. Keys that don't exist or
have no value are omitted from the result.

**Batch retrieve player scores**

This code sample uses the GlobalDataStore:BatchGetAsync() method to retrieve
and print values for several players.

```lua
local DataStoreService = game:GetService("DataStoreService")
local playerScores = DataStoreService:GetOrderedDataStore("PlayerScores")
local keys = {"Player_123", "Player_456", "Player_789"}
local success, results = pcall(function()
	return playerScores:BatchGetAsync(keys)
end)
if success then
	for _, key in keys do
		local entry = results[key]
		if entry then
			print(key .. " : " .. tostring(entry.value))
		else
			print(key .. " has no saved entry")
		end
	end
end
```

### Method: GlobalDataStore:GetAsync

**Signature:** `GlobalDataStore:GetAsync(key: string, options?: DataStoreGetOptions): Tuple`

This function returns the latest value of the provided key and a
[DataStoreKeyInfo](/docs/reference/engine/classes/DataStoreKeyInfo.md) instance. If the key does not exist or if the
latest version has been marked as deleted, both return values will be
`nil`.

Keys are cached locally for 4 seconds after the first read. A
[GlobalDataStore:GetAsync()](/docs/reference/engine/classes/GlobalDataStore.md) call within these 4 seconds returns a
value from the cache. Modifications to the key by
[GlobalDataStore:SetAsync()](/docs/reference/engine/classes/GlobalDataStore.md) or
[GlobalDataStore:UpdateAsync()](/docs/reference/engine/classes/GlobalDataStore.md) apply to the cache immediately and
restart the 4 second timer.

To get a specific version, such as a version before the latest, use
[DataStore:GetVersionAsync()](/docs/reference/engine/classes/DataStore.md).

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: DataStore*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `key` | `string` |  | The key name for which the value is requested. If [DataStoreOptions.AllScopes](/docs/reference/engine/classes/DataStoreOptions.md) was set to true when accessing the data store through [DataStoreService:GetDataStore()](/docs/reference/engine/classes/DataStoreService.md), this key name must be prepended with the original scope as in "scope/key". |
| `options` | `DataStoreGetOptions` | `nil` | **(Optional)** A [DataStoreGetOptions](/docs/reference/engine/classes/DataStoreGetOptions.md) instance that controls aspects of the read, such as whether to bypass the locally cached value via its [DataStoreGetOptions.UseCache](/docs/reference/engine/classes/DataStoreGetOptions.md) property. |

**Returns:** `Tuple` — The value of the entry in the data store with the given key and a
[DataStoreKeyInfo](/docs/reference/engine/classes/DataStoreKeyInfo.md) instance that includes the version number,
date and time the version was created, and functions to retrieve
[UserIds](/docs/reference/engine/classes/Player.md) and metadata.

### Method: GlobalDataStore:IncrementAsync

**Signature:** `GlobalDataStore:IncrementAsync(key: string, delta?: int, userIds?: Array, options?: DataStoreIncrementOptions): Variant`

This function increments the value of a key by the provided amount (both
must be integers).

Values in [GlobalDataStores](/docs/reference/engine/classes/GlobalDataStore.md) are **versioned** as
outlined in
[versioning](/docs/en-us/cloud-services/data-stores/versioning-listing-and-caching.md#versioning).
[OrderedDataStores](/docs/reference/engine/classes/OrderedDataStore.md) do not support versioning, so
calling this method on an ordered data store key will overwrite the
current value with the incremented value and make previous versions
inaccessible.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: DataStore*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `key` | `string` |  | Key name for which the value should be updated. If [DataStoreOptions.AllScopes](/docs/reference/engine/classes/DataStoreOptions.md) was set to true when accessing the data store through [DataStoreService:GetDataStore()](/docs/reference/engine/classes/DataStoreService.md), this key name must be prepended with the original scope as in "scope/key". |
| `delta` | `int` | `1` | Amount to increment the current value by. |
| `userIds` | `Array` | `{}` | **(Optional)** A table of [UserIds](/docs/reference/engine/classes/Player.md) to associate with the key. |
| `options` | `DataStoreIncrementOptions` | `nil` | **(Optional)** [DataStoreIncrementOptions](/docs/reference/engine/classes/DataStoreIncrementOptions.md) instance that combines multiple additional parameters as custom metadata and allows for future extensibility. |

**Returns:** `Variant` — The updated value of the entry in the data store with the given key.

### Method: GlobalDataStore:RemoveAsync

**Signature:** `GlobalDataStore:RemoveAsync(key: string): Tuple`

This function marks the specified key as deleted by creating a new
"tombstone" version of the key. Prior to this, it returns the latest
version prior to the remove call.

After a key is removed via this function,
[GlobalDataStore:GetAsync()](/docs/reference/engine/classes/GlobalDataStore.md) calls for the key will return `nil`.
Older versions of the key remain accessible through
[DataStore:ListVersionsAsync()](/docs/reference/engine/classes/DataStore.md) and
[DataStore:GetVersionAsync()](/docs/reference/engine/classes/DataStore.md), assuming they have not expired.

[OrderedDataStore](/docs/reference/engine/classes/OrderedDataStore.md) does not support versioning, so calling
[RemoveAsync()](/docs/reference/engine/classes/GlobalDataStore.md) on an
[OrderedDataStore](/docs/reference/engine/classes/OrderedDataStore.md) key will permanently delete it.

Removed objects will be deleted permanently after 30 days.

If the previous values were already deleted via
[GlobalDataStore:RemoveAsync()](/docs/reference/engine/classes/GlobalDataStore.md) or
[DataStore:RemoveVersionAsync()](/docs/reference/engine/classes/DataStore.md), the function will return `nil`,
`nil` for value and [DataStoreKeyInfo](/docs/reference/engine/classes/DataStoreKeyInfo.md) respectively.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: DataStore*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `key` | `string` |  | Key name to be removed. If [DataStoreOptions.AllScopes](/docs/reference/engine/classes/DataStoreOptions.md) was set to true when accessing the data store through [DataStoreService:GetDataStore()](/docs/reference/engine/classes/DataStoreService.md), this key name must be prepended with the original scope as in "scope/key". |

**Returns:** `Tuple` — The value of the data store prior to deletion and a
[DataStoreKeyInfo](/docs/reference/engine/classes/DataStoreKeyInfo.md) instance that includes the version number,
date and time the version was created, and functions to retrieve
[UserIds](/docs/reference/engine/classes/Player.md) and metadata.

### Method: GlobalDataStore:SetAsync

**Signature:** `GlobalDataStore:SetAsync(key: string, value: Variant, userIds?: Array, options?: DataStoreSetOptions): Variant`

This function sets the latest value, [UserIds](/docs/reference/engine/classes/Player.md), and
metadata for the given key.

Values in [GlobalDataStores](/docs/reference/engine/classes/GlobalDataStore.md) are **versioned** as
outlined in
[versioning](/docs/en-us/cloud-services/data-stores/versioning-listing-and-caching.md#versioning).
[OrderedDataStores](/docs/reference/engine/classes/OrderedDataStore.md) do not support versioning, so
calling this method on an ordered data store key will overwrite the
current value and make previous versions inaccessible.

Metadata definitions must always be updated with a value, even if there
are no changes to the current value; otherwise the current value will be
lost.

Any string being stored in a data store must be valid
[UTF-8](/docs/reference/engine/globals/utf8.md). In UTF-8, values greater than 127 are used
exclusively for encoding multi-byte codepoints, so a single byte greater
than 127 will not be valid UTF-8 and the
[GlobalDataStore:SetAsync()](/docs/reference/engine/classes/GlobalDataStore.md) attempt will fail.

#### Set vs. Update

[GlobalDataStore:SetAsync()](/docs/reference/engine/classes/GlobalDataStore.md) is best for a quick update of a
specific key, and it only counts against the write limit. However, it may
cause data inconsistency if two servers attempt to set the same key at the
same time. [GlobalDataStore:UpdateAsync()](/docs/reference/engine/classes/GlobalDataStore.md) is safer for handling
multi-server attempts because it reads the current key value (from
whatever server last updated it) before making any changes. However, it's
somewhat slower because it reads before it writes, and it also counts
against both the read and write limit.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: DataStore*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `key` | `string` |  | Key name for which the value should be set. If [DataStoreOptions.AllScopes](/docs/reference/engine/classes/DataStoreOptions.md) was set to true when accessing the data store through [DataStoreService:GetDataStore()](/docs/reference/engine/classes/DataStoreService.md), this key name must be prepended with the original scope as in "scope/key". |
| `value` | `Variant` |  | The value that the data store key will be set to. |
| `userIds` | `Array` | `{}` | Table of [UserIds](/docs/reference/engine/classes/Player.md), highly recommended to assist with GDPR tracking/removal. |
| `options` | `DataStoreSetOptions` | `nil` | **(Optional)** [DataStoreSetOptions](/docs/reference/engine/classes/DataStoreSetOptions.md) instance that allows for metadata specification on the key. |

**Returns:** `Variant` — The version identifier of the newly created version. It can be used to
retrieve key info using
[GetVersionAsync()](/docs/reference/engine/classes/DataStore.md) or to remove it
using [RemoveVersionAsync()](/docs/reference/engine/classes/DataStore.md).

### Method: GlobalDataStore:UpdateAsync

**Signature:** `GlobalDataStore:UpdateAsync(key: string, transformFunction: Function): Tuple`

This function retrieves the value and metadata of a key from the data
store and updates it with a new value determined by the callback function
specified through the second parameter. If the callback returns `nil`, the
write operation is cancelled and the value remains unchanged.

Values in [GlobalDataStores](/docs/reference/engine/classes/GlobalDataStore.md) are **versioned** as
outlined in
[versioning](/docs/en-us/cloud-services/data-stores/versioning-listing-and-caching.md#versioning).
[OrderedDataStores](/docs/reference/engine/classes/OrderedDataStore.md) do not support versioning, so
calling this method on an ordered data store key will overwrite the
current value and make previous versions inaccessible.

In cases where another game server updated the key in the short timespan
between retrieving the key's current value and setting the key's value,
[GlobalDataStore:UpdateAsync()](/docs/reference/engine/classes/GlobalDataStore.md) will call the function again,
discarding the result of the previous call. The function will be called as
many times as needed until the data is saved **or** until the callback
function returns `nil`. This can be used to ensure that no data is
overwritten.

Any string being stored in a data store must be valid
[UTF-8](/docs/reference/engine/globals/utf8.md). In UTF-8, values greater than 127 are used
exclusively for encoding multi-byte codepoints, so a single byte greater
than 127 will not be valid UTF-8 and the
[GlobalDataStore:UpdateAsync()](/docs/reference/engine/classes/GlobalDataStore.md) attempt will fail.

#### Set vs. Update

[GlobalDataStore:SetAsync()](/docs/reference/engine/classes/GlobalDataStore.md) is best for a quick update of a
specific key, and it only counts against the write limit. However, it may
cause data inconsistency if two servers attempt to set the same key at the
same time. [GlobalDataStore:UpdateAsync()](/docs/reference/engine/classes/GlobalDataStore.md) is safer for handling
multi-server attempts because it reads the current key value (from
whatever server last updated it) before making any changes. However, it's
somewhat slower because it reads before it writes, and it also counts
against both the read and write limit.

#### Callback Function

The callback function accepts two arguments:

- Current value of the key prior to the update.
- [DataStoreKeyInfo](/docs/reference/engine/classes/DataStoreKeyInfo.md) instance that contains the latest version
  information (this argument can be ignored if metadata is not being
  used).

In turn, the callback function returns up to three values:

- The new value to set for the key.
- An array of [UserIds](/docs/reference/engine/classes/Player.md) to associate with the key.
  [DataStoreKeyInfo:GetUserIds()](/docs/reference/engine/classes/DataStoreKeyInfo.md) should be returned unless the
  existing IDs are being changed; otherwise all existing IDs will be
  cleared.
- A Luau table containing metadata to associate with the key.
  [DataStoreKeyInfo:GetMetadata()](/docs/reference/engine/classes/DataStoreKeyInfo.md) should be returned unless the
  existing metadata is being changed; otherwise all existing metadata will
  be cleared.

If the callback returns `nil` instead, the current server will stop
attempting to update the key.

The callback function cannot yield, so do **not** include calls like
[task.wait()](/docs/reference/engine/globals/task.md).

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: DataStore*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `key` | `string` |  | Key name for which the value should be updated. If [DataStoreOptions.AllScopes](/docs/reference/engine/classes/DataStoreOptions.md) was set to true when accessing the data store through [DataStoreService:GetDataStore()](/docs/reference/engine/classes/DataStoreService.md), this key name must be prepended with the original scope as in "scope/key". |
| `transformFunction` | `Function` |  | Transform function that takes the current value and [DataStoreKeyInfo](/docs/reference/engine/classes/DataStoreKeyInfo.md) as parameters and returns the new value along with optional [UserIds](/docs/reference/engine/classes/Player.md) and metadata. |

**Returns:** `Tuple` — The updated value of the entry in the data store with the given key
and a [DataStoreKeyInfo](/docs/reference/engine/classes/DataStoreKeyInfo.md) instance that includes the version
number, date and time the version was created, and functions to
retrieve [UserIds](/docs/reference/engine/classes/Player.md) and metadata.

### Method: GlobalDataStore:OnUpdate

**Signature:** `GlobalDataStore:OnUpdate(key: string, callback: Function): RBXScriptConnection`

> **Deprecated:** This function has been deprecated and should not be used in new work. You can use the [Cross Server Messaging Service](/docs/reference/engine/classes/MessagingService.md) to publish and subscribe to topics to receive near real-time updates, completely replacing the need for this function.

This function sets `callback` as the function to be run any time the value
associated with the `key` changes. Once every minute, OnUpdate polls for
changes by other servers. Changes made on the same server will run the
function immediately. In other words, functions like
[IncrementAsync()](/docs/reference/engine/classes/GlobalDataStore.md),
[SetAsync()](/docs/reference/engine/classes/GlobalDataStore.md), and
[UpdateAsync()](/docs/reference/engine/classes/GlobalDataStore.md) change the key's value
in the data store and will cause the function to run.

It's recommended that you **disconnect** the connection when the
subscription to the key is no longer needed.

*Security: None · Thread Safety: Unsafe · Capabilities: DataStore*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `key` | `string` |  | The key identifying the entry being retrieved from the data store. |
| `callback` | `Function` |  | The function to be executed any time the value associated with **key** is changed. |

**Returns:** `RBXScriptConnection` — The connection to the key being tracked for updates.

**Print Data Store Value on Update**

The sample creates an [GlobalDataStore:OnUpdate()](/docs/reference/engine/classes/GlobalDataStore.md) connection with the
key `myKey` and the `printOut()` function, then it sets the `myKey` store
to 11. Since the connection with `myKey` is open, `printOut()` executes and
prints the input (the updated value). Immediately after this occurs, the
script disconnects the connection.

```lua
local DataStoreService = game:GetService("DataStoreService")

local sampleDataStore = DataStoreService:GetDataStore("MyDataStore")

local connection

local function printOut(input)
	print(input)
	connection:Disconnect()
end

connection = sampleDataStore:OnUpdate("myKey", printOut)

local success, result = pcall(function()
	sampleDataStore:SetAsync("myKey", 11)
end)

if not success then
	warn(result)
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