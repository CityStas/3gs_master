---
name: OrderedDataStore
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
summary: "A GlobalDataStore that also allows for ordered data store entries."
---

# Class: OrderedDataStore

> A GlobalDataStore that also allows for ordered data store entries.

## Description

A **OrderedDataStore** is essentially a [GlobalDataStore](/docs/reference/engine/classes/GlobalDataStore.md) with the
exception that stored values must be **integers**. It exposes a method
[GetSortedAsync()](/docs/reference/engine/classes/OrderedDataStore.md) which allows
inspection of the entries in sorted order using a [DataStorePages](/docs/reference/engine/classes/DataStorePages.md)
object.

Ordered data stores do not support versioning and metadata, so
[DataStoreKeyInfo](/docs/reference/engine/classes/DataStoreKeyInfo.md) is always `nil` for keys in an
[OrderedDataStore](/docs/reference/engine/classes/OrderedDataStore.md). If you need versioning and metadata support, use a
[DataStore](/docs/reference/engine/classes/DataStore.md).

Ordered data stores do not support the optional `userIds` parameter for
[SetAsync()](/docs/reference/engine/classes/OrderedDataStore.md) or
[IncrementAsync()](/docs/reference/engine/classes/OrderedDataStore.md).

See [Data stores](/docs/en-us/cloud-services/data-stores.md) for an
overview on how to use ordered data stores.

## Code Samples

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

## Methods

### Method: OrderedDataStore:GetSortedAsync

**Signature:** `OrderedDataStore:GetSortedAsync(ascending: boolean, pagesize: int, minValue: Variant, maxValue: Variant): DataStorePages`

Returns a [DataStorePages](/docs/reference/engine/classes/DataStorePages.md) object. The sort order is determined by
**ascending**, the length of each page by **pageSize**, and
**minValue**/**maxValue** are optional parameters which filter the
results.

See
[Error codes and limits](/docs/en-us/cloud-services/data-stores/error-codes-and-limits.md)
for request limits and descriptions of the error codes.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: DataStore*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `ascending` | `boolean` |  | A boolean indicating whether the returned data pages are in ascending order. |
| `pagesize` | `int` |  | The length of each page. By default is 50. The max allowed value is 100. |
| `minValue` | `Variant` |  | Optional parameter. If set, data pages with a value less than **minValue** will be excluded. |
| `maxValue` | `Variant` |  | Optional parameter. If set, data pages with a value greater than **maxValue** will be excluded. |

**Returns:** `DataStorePages` — A sorted [DataStorePages](/docs/reference/engine/classes/DataStorePages.md) object based on the provided
arguments.

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