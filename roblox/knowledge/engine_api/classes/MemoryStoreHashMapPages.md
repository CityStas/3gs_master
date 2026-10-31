---
name: MemoryStoreHashMapPages
last_updated: 2026-10-30T19:55:52Z
inherits:
  - Pages
  - Instance
  - Object
type: class
memory_category: Instances
tags:
  - NotCreatable
  - NotReplicated
summary: "A special type of Pages object whose pages contain key-value pairs from a MemoryStoreHashMap."
---

# Class: MemoryStoreHashMapPages

> A special type of [Pages](/docs/reference/engine/classes/Pages.md) object whose pages contain key-value pairs
> from a [MemoryStoreHashMap](/docs/reference/engine/classes/MemoryStoreHashMap.md).

## Description

A special type of [Pages](/docs/reference/engine/classes/Pages.md) object whose pages contain key-value pairs
from a [MemoryStoreHashMap](/docs/reference/engine/classes/MemoryStoreHashMap.md). [Pages:GetCurrentPage()](/docs/reference/engine/classes/Pages.md) can be used
to retrieve an array of tables, each containing a key and value; these reflect
the key-value pair data.

## Code Samples

**Listing items in a MemoryStore Hash Map**

The code below lists all the items in a Memory Store Hash Map.

```lua
local MemoryStoreService = game:GetService("MemoryStoreService")

local testHashMap = MemoryStoreService:GetHashMap("HashMap1")

local EXPIRATION = 600
local NUM_TEST_ITEMS = 32

local function populateHashMap(hashMap: MemoryStoreHashMap, numItems: number): { [string]: any }
	print("Setting HashMap data...")
	local createdItems = {}

	for index = 1, numItems do
		local key = tostring(index) -- HashMap keys must be strings
		local value = `{key}_test_value`
		local success, result = pcall(hashMap.SetAsync, hashMap, key, value, EXPIRATION)

		if success then
			createdItems[key] = value
		else
			warn(`Error setting key {key}: {result}`)
		end
	end

	print("Done setting HashMap data.")
	return createdItems
end

local function getItemsFromAllPages(pages: MemoryStoreHashMapPages): { [string]: any }
	-- Purely for logging purposes, we track what page number we're on
	local currentPageNumber = 1
	local retrievedItems = {}

	while not pages.IsFinished do
		print(`Getting items on page {currentPageNumber}...`)
		local items = pages:GetCurrentPage()

		for _, entry in pairs(items) do
			print(`	{entry.key}: {entry.value}`)
			retrievedItems[entry.key] = entry.value
		end

		-- Advance pages if there are more pages to read
		if not pages.IsFinished then
			pages:AdvanceToNextPageAsync()
			currentPageNumber += 1
		end
	end

	print("Finished reading all pages")
	return retrievedItems
end

local function compareAllItems(retrievedItems: { [string]: any }, expectedItems: { [string]: any }): number
	print("Comparing retrieved items to expected items...")
	local numMatchingItems = 0

	for key, expectedValue in pairs(expectedItems) do
		if retrievedItems[key] == expectedValue then
			numMatchingItems += 1
		else
			warn(`Mismatched retrieved value for key {key}: expected {expectedValue}, retrieved {retrievedItems[key]}`)
		end
	end

	print("Comparison complete!")
	return numMatchingItems
end

-- Keys added to the hashmap are also added to this expectedItems table.
-- Later, the retrieved hashmap items will be compared against this table of expected items.
local expectedItems = populateHashMap(testHashMap, NUM_TEST_ITEMS)

-- Getting pages can error. In this case, we will let it error and stop program execution,
-- but you may want to pcall it and handle it differently.
print(`Getting HashMap pages with ListItemsAsync...`)
local pages = testHashMap:ListItemsAsync(NUM_TEST_ITEMS)

local retrievedItems = getItemsFromAllPages(pages)
local numMatchingItems = compareAllItems(retrievedItems, expectedItems)

-- If there were no errors setting or getting items, all items should match.
print(`Program complete. {numMatchingItems}/{NUM_TEST_ITEMS} retrieved items matched the expected values.`)
```

## Inherited Members

### From [Pages](/docs/reference/engine/classes/Pages.md)

- **Property `IsFinished`** (`boolean`): Whether or not the current page is the last page available.
- **Method `AdvanceToNextPageAsync(): ()`**: Iterates to the next page in the pages object, if possible.
- **Method `GetCurrentPage(): Array`**: Returns the items on the current page. The keys in the item are determined

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