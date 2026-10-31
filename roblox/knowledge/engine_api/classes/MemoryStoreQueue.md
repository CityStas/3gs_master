---
name: MemoryStoreQueue
last_updated: 2026-10-30T19:55:52Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
tags:
  - NotCreatable
  - NotReplicated
summary: "Provides access to a queue within MemoryStore."
---

# Class: MemoryStoreQueue

> Provides access to a queue within MemoryStore.

## Description

Provides access to a queue within MemoryStore. A queue is a data structure
that provides temporary storage for arbitrary items (up to the maximum item
size -- see
[MemoryStore Limits](/docs/en-us/cloud-services/memory-stores.md#limits-and-quotas)).
Each queue item has a numeric priority: MemoryStore retrieves items with
higher priority from the queue first, and it retrieves Items with the same
priority in order of addition.

Items in the queue can optionally be set to expire after a certain amount of
time. Expired items simply disappear from the queue as if they were never
added.

## Methods

### Method: MemoryStoreQueue:AddAsync

**Signature:** `MemoryStoreQueue:AddAsync(value: Variant, expiration: int64, priority?: double): ()`

Adds an item to the queue with the given priority and expiration. Items
with a higher `priority` are retrieved from the queue before items with a
lower priority, and items with the same priority are retrieved in the
order they were added; `priority` defaults to 0. The `expiration` value,
in seconds, sets how long the item remains in the queue before it is
automatically removed. This method yields until the item has been added.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: DataStore*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `value` | `Variant` |  | The value of the item to add to the queue. |
| `expiration` | `int64` |  | Item expiration time, in seconds, after which the item will be automatically removed from the queue. |
| `priority` | `double` | `0` | Item priority. Items with higher priority are retrieved from the queue before items with lower priority. |

**Returns:** `()`

### Method: MemoryStoreQueue:GetSizeAsync

**Signature:** `MemoryStoreQueue:GetSizeAsync(excludeInvisible?: boolean): int`

Returns the number of items currently in the queue. By default the
returned count includes invisible items -- items that have been read with
[MemoryStoreQueue:ReadAsync()](/docs/reference/engine/classes/MemoryStoreQueue.md) but not yet removed and whose
invisibility timeout has not expired. Set the `excludeInvisible` parameter
to `true` to omit these items from the count; it defaults to `false`. This
method yields until the size is retrieved.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: DataStore*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `excludeInvisible` | `boolean` | `false` | Determines whether to exclude invisible items from the size count. |

**Returns:** `int` — The number of items currently in the queue. Items that have been read
but not yet removed (invisible items) are included in the count unless
`excludeInvisible` is `true`.

### Method: MemoryStoreQueue:ReadAsync

**Signature:** `MemoryStoreQueue:ReadAsync(count: int, allOrNothing?: boolean, waitTimeout?: double): Tuple`

Reads one or more items from the queue as a single atomic operation.

This method does not automatically delete the returned items from the
queue but makes them invisible to other ReadAsync calls for the period of
the invisibility timeout. The items must be explicitly removed from the
queue with [MemoryStoreQueue:RemoveAsync()](/docs/reference/engine/classes/MemoryStoreQueue.md) before the invisibility
timeout expires. The invisibility timeout defaults to 30 seconds unless a
different value was provided in [MemoryStoreService:GetQueue()](/docs/reference/engine/classes/MemoryStoreService.md).

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: DataStore*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `count` | `int` |  | Number of items to read. The maximum allowed value of this parameter is 100. |
| `allOrNothing` | `boolean` | `false` | Controls the behavior of the method in the case the queue has fewer than `count` items: if set to false the method returns all available items; if set to true, it returns no items. The default value is false. |
| `waitTimeout` | `double` | `-1` | The duration, in seconds, for which the method will wait if the required number of items is not immediately available in the queue. Reads are attempted every two seconds during this period. This parameter can be set to zero to indicate no wait. If this parameter is not provided or set to -1, the method will wait indefinitely. |

**Returns:** `Tuple` — A tuple of two elements. The first element is an array of item values
read from the queue. The second element is a string identifier that
should be passed to [MemoryStoreQueue:RemoveAsync()](/docs/reference/engine/classes/MemoryStoreQueue.md) to
permanently remove these items from the queue.

**Using a MemoryStoreQueue**

The following code sample demonstrates using
[MemoryStoreQueue:ReadAsync()](/docs/reference/engine/classes/MemoryStoreQueue.md) and
[MemoryStoreQueue:RemoveAsync()](/docs/reference/engine/classes/MemoryStoreQueue.md) to reliably read, process, and remove
items from a queue. Though this process can be as complicated as necessary,
this example simply sets a flag in the corresponding data store item, which
guarantees that every item will eventually be processed even if some of the
calls encounter errors or the server crashes:

- If [MemoryStoreQueue:ReadAsync()](/docs/reference/engine/classes/MemoryStoreQueue.md) fails, no items are retrieved from
  the queue. An item will be picked up for processing during the next
  iteration of the loop.
- If [MemoryStoreQueue:ReadAsync()](/docs/reference/engine/classes/MemoryStoreQueue.md) succeeds but
  [DataStoreService:UpdateAsync()](/docs/reference/engine/classes/DataStoreService.md) fails, the item stays invisible until
  the queue's invisibility timeout expires, causing the item becoming visible
  again to be returned in a future loop iteration.
- Similarly, if [MemoryStoreQueue:RemoveAsync()](/docs/reference/engine/classes/MemoryStoreQueue.md) fails, the item will
  become visible again in the future and will be processed again.

Depending on where the failure happens, it's possible that an item will be
processed more than once. You should account for that like the following code
sample, in which the end result is the same even if
[DataStoreService:UpdateAsync()](/docs/reference/engine/classes/DataStoreService.md) is invoked multiple times.

```lua
local MemoryStoreService = game:GetService("MemoryStoreService")
local DataStoreService = game:GetService("DataStoreService")

local queue = MemoryStoreService:GetQueue("PlayerQueue")
local dataStore = DataStoreService:GetDataStore("PlayerStore")

while true do
	pcall(function()
		-- wait for an item to process
		local items, id = queue:ReadAsync(1, false, 30)

		-- check if an item was retrieved
		if #items > 0 then
			-- mark the item as processed
			dataStore:UpdateAsync(items[0], function(data)
				data = data or {}
				data.processed = 1
				return data
			end)

			-- remove the item from the queue
			queue:RemoveAsync(id)
		end
	end)
end
```

### Method: MemoryStoreQueue:RemoveAsync

**Signature:** `MemoryStoreQueue:RemoveAsync(id: string): ()`

Removes an item or items previously read from the queue. This method uses
the identifier returned by [MemoryStoreQueue:ReadAsync()](/docs/reference/engine/classes/MemoryStoreQueue.md) to
identify the items to remove. If called after the invisibility timeout has
expired, the call has no effect.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: DataStore*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `id` | `string` |  | Identifies the items to delete. Use the value returned by [MemoryStoreQueue:ReadAsync()](/docs/reference/engine/classes/MemoryStoreQueue.md). |

**Returns:** `()`

**Using a MemoryStoreQueue**

The following code sample demonstrates using
[MemoryStoreQueue:ReadAsync()](/docs/reference/engine/classes/MemoryStoreQueue.md) and
[MemoryStoreQueue:RemoveAsync()](/docs/reference/engine/classes/MemoryStoreQueue.md) to reliably read, process, and remove
items from a queue. Though this process can be as complicated as necessary,
this example simply sets a flag in the corresponding data store item, which
guarantees that every item will eventually be processed even if some of the
calls encounter errors or the server crashes:

- If [MemoryStoreQueue:ReadAsync()](/docs/reference/engine/classes/MemoryStoreQueue.md) fails, no items are retrieved from
  the queue. An item will be picked up for processing during the next
  iteration of the loop.
- If [MemoryStoreQueue:ReadAsync()](/docs/reference/engine/classes/MemoryStoreQueue.md) succeeds but
  [DataStoreService:UpdateAsync()](/docs/reference/engine/classes/DataStoreService.md) fails, the item stays invisible until
  the queue's invisibility timeout expires, causing the item becoming visible
  again to be returned in a future loop iteration.
- Similarly, if [MemoryStoreQueue:RemoveAsync()](/docs/reference/engine/classes/MemoryStoreQueue.md) fails, the item will
  become visible again in the future and will be processed again.

Depending on where the failure happens, it's possible that an item will be
processed more than once. You should account for that like the following code
sample, in which the end result is the same even if
[DataStoreService:UpdateAsync()](/docs/reference/engine/classes/DataStoreService.md) is invoked multiple times.

```lua
local MemoryStoreService = game:GetService("MemoryStoreService")
local DataStoreService = game:GetService("DataStoreService")

local queue = MemoryStoreService:GetQueue("PlayerQueue")
local dataStore = DataStoreService:GetDataStore("PlayerStore")

while true do
	pcall(function()
		-- wait for an item to process
		local items, id = queue:ReadAsync(1, false, 30)

		-- check if an item was retrieved
		if #items > 0 then
			-- mark the item as processed
			dataStore:UpdateAsync(items[0], function(data)
				data = data or {}
				data.processed = 1
				return data
			end)

			-- remove the item from the queue
			queue:RemoveAsync(id)
		end
	end)
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