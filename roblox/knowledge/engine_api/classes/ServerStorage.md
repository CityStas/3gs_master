---
name: ServerStorage
last_updated: 2026-10-30T19:55:53Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
tags:
  - NotCreatable
  - Service
  - NotReplicated
summary: "A container whose contents are only accessible on the server. Objects descending from ServerStorage will not replicate to the client and will not be accessible from LocalScripts."
---

# Class: ServerStorage

> A container whose contents are only accessible on the server. Objects
> descending from ServerStorage will not replicate to the client and will not be
> accessible from [LocalScripts](/docs/reference/engine/classes/LocalScript.md).

## Description

A container whose contents are only accessible on the server. Objects
descending from ServerStorage will not replicate to the client and will not be
accessible from [LocalScripts](/docs/reference/engine/classes/LocalScript.md).

As ServerStorage is a service it can only be accessed using the
[DataModel.GetService](/docs/reference/engine/classes/DataModel.md) method.

By storing large objects such as maps in ServerStorage until they are needed,
network traffic will not be used up transmitting these objects to the client
when they join the game.

[Scripts](/docs/reference/engine/classes/Script.md) will not run when they are parented to ServerStorage,
although [ModuleScripts](/docs/reference/engine/classes/ModuleScript.md) contained within can be accessed
and ran. It is recommended developers use [ServerScriptService](/docs/reference/engine/classes/ServerScriptService.md) to hold
[Scripts](/docs/reference/engine/classes/Script.md) they wish the server to execute.

Note that as the contents of ServerStorage can only be accessed by the server,
its contents will need to be parented elsewhere (such as [Workspace](/docs/reference/engine/classes/Workspace.md))
before clients can access them. Developers who require a container that is
accessible by both the server and client are advised to use
[ReplicatedStorage](/docs/reference/engine/classes/ReplicatedStorage.md) instead.

## Code Samples

**ServerStorage Map Rotation**

This is a very simple example of how a multiple map system can be made using
ServerStorage.

It creates three dummy models (to take the place of maps), that are parented
to ServerStorage. Then, it will load a random map (different to the previous
map) and wait a specified duration on a loop.

Developers wishing to integrate something similar into their games should
consider measures to ensure players respawn correctly, or go to a lobby during
intermission periods.

```lua
local ServerStorage = game:GetService("ServerStorage")

local ROUND_TIME = 5

local map1 = Instance.new("Model")
map1.Name = "Map1"
map1.Parent = ServerStorage

local map2 = Instance.new("Model")
map2.Name = "Map2"
map2.Parent = ServerStorage

local map3 = Instance.new("Model")
map3.Name = "Map3"
map3.Parent = ServerStorage

local maps = { map1, map2, map3 }
local RNG = Random.new()
local currentMap = nil
local lastPick = nil

while true do
	print("New map!")

	-- remove current map
	if currentMap then
		currentMap:Destroy()
	end

	-- pick a map
	local randomPick = nil
	if #maps > 1 then
		repeat
			randomPick = RNG:NextInteger(1, #maps)
		until randomPick ~= lastPick
		lastPick = randomPick
	end

	-- fetch new map
	local map = maps[randomPick]
	currentMap = map:Clone()
	currentMap.Parent = workspace

	task.wait(ROUND_TIME)
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