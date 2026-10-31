---
name: KeyframeSequenceProvider
last_updated: 2026-10-30T19:55:52Z
inherits:
  - Instance
  - Object
type: class
memory_category: Animation
tags:
  - NotCreatable
  - Service
  - NotReplicated
summary: "Provides functions to load and preview KeyframeSequence."
---

# Class: KeyframeSequenceProvider

> Provides functions to load and preview [KeyframeSequence](/docs/reference/engine/classes/KeyframeSequence.md).

## Description

The **KeyframeSequenceProvider** service provides functions to load and
preview [KeyframeSequences](/docs/reference/engine/classes/KeyframeSequence.md). It includes a number of
functions that are useful when working with [Animations](/docs/reference/engine/classes/Animation.md).

A [KeyframeSequence](/docs/reference/engine/classes/KeyframeSequence.md) stores a series of [Poses](/docs/reference/engine/classes/Pose.md) that encode
the hierarchy and motion of an animation. The animation data Roblox uses in
the playback of an animation, referenced by the [Animation.AnimationId](/docs/reference/engine/classes/Animation.md)
property, can be constructed from a [KeyframeSequence](/docs/reference/engine/classes/KeyframeSequence.md).
[KeyframeSequences](/docs/reference/engine/classes/KeyframeSequence.md) are usually created by the Roblox
[Animation Editor](/docs/en-us/animation/editor.md) but can be created through
other plugins or even manually.

## Code Samples

**Create temporary animation**

This code sample contains a simple function to generate an [Animation](/docs/reference/engine/classes/Animation.md)
with a generated hash ID to preview a [KeyframeSequence](/docs/reference/engine/classes/KeyframeSequence.md) locally.

```lua
local KeyframeSequenceProvider = game:GetService("KeyframeSequenceProvider")

local function createPreviewAnimation(keyframeSequence)
	local hashId = KeyframeSequenceProvider:RegisterKeyframeSequence(keyframeSequence)
	local Animation = Instance.new("Animation")
	Animation.AnimationId = hashId
	return Animation
end

local keyframeSequence = Instance.new("KeyframeSequence")

local animation = createPreviewAnimation(keyframeSequence)

print(animation)
```

## Methods

### Method: KeyframeSequenceProvider:GetAnimationsAsync

**Signature:** `KeyframeSequenceProvider:GetAnimationsAsync(userId: User): Instance`

This function returns an [InventoryPages](/docs/reference/engine/classes/InventoryPages.md) object which can be used
to iterate over animations owned by a specific user.

This function has a number of potential uses, such as allowing users to
browse and import animations into a custom animation plugin.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Animation*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `userId` | `User` |  | The user ID of the user. |

**Returns:** `Instance` — An [InventoryPages](/docs/reference/engine/classes/InventoryPages.md) of animations.

**KeyframeSequenceProvider GetAnimationsAsync**

This code sample includes a demonstration of how the content IDs of animations
belonging to a player can be downloaded using
[KeyframeSequenceProvider:GetAnimationsAsync()](/docs/reference/engine/classes/KeyframeSequenceProvider.md). To run this code be
sure to change the _USER_ID_ variable to the ID of the user whose animations
you want to download.

```lua
local KeyframeSequenceProvider = game:GetService("KeyframeSequenceProvider")

local USER_ID = 0 -- Insert your UserId here

local function extractPages(pagesObject)
	local array = {}
	while true do
		local thisPage = pagesObject:GetCurrentPage()
		for _, v in pairs(thisPage) do
			table.insert(array, v)
		end
		if pagesObject.IsFinished then
			break
		end
		pagesObject:AdvanceToNextPageAsync()
	end
	return array
end

local inventoryPages = KeyframeSequenceProvider:GetAnimationsAsync(USER_ID)

local animationIds = extractPages(inventoryPages)

for _, id in pairs(animationIds) do
	print(id)
end
print("total: ", #animationIds)
```

### Method: KeyframeSequenceProvider:GetKeyframeSequenceAsync

**Signature:** `KeyframeSequenceProvider:GetKeyframeSequenceAsync(assetId: ContentId): Instance`

GetKeyframeSequenceAsync returns a [KeyframeSequence](/docs/reference/engine/classes/KeyframeSequence.md) based on the
specified assetId. The assetId must correspond to an animation. The
function will yield until the [KeyframeSequence](/docs/reference/engine/classes/KeyframeSequence.md) is loaded from the
website. Because this is a webcall it should wrapped in a pcall.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Animation*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `assetId` | `ContentId` |  | The content ID of the animation. |

**Returns:** `Instance` — The [KeyframeSequence](/docs/reference/engine/classes/KeyframeSequence.md) found.

**Getting an animation's KeyframeSequence**

Demonstrates getting an animation's KeyframeSequence using
[KeyframeSequenceProvider:GetKeyframeSequenceAsync()](/docs/reference/engine/classes/KeyframeSequenceProvider.md) and printing the
time of each keyframe.

```lua
local KeyframeSequenceProvider = game:GetService("KeyframeSequenceProvider")

local ANIMATION_ID = "rbxassetid://507771019"

-- Get the keyframe sequence for the asset
local keyframeSequence
local success, err = pcall(function()
	keyframeSequence = KeyframeSequenceProvider:GetKeyframeSequenceAsync(ANIMATION_ID)
end)

if success then
	-- Iterate over each keyframe and print its time value
	local keyframeTable = keyframeSequence:GetKeyframes()
	for key, value in keyframeTable do
		print(`The time of keyframe number {key} is: {value.Time}`)
	end
else
	print(`Error getting KeyframeSequence: {err}`)
end
```

### Method: KeyframeSequenceProvider:RegisterActiveKeyframeSequence

**Signature:** `KeyframeSequenceProvider:RegisterActiveKeyframeSequence(keyframeSequence: Instance): ContentId`

Generates a temporary asset ID from a [KeyframeSequence](/docs/reference/engine/classes/KeyframeSequence.md) that can be
used for localized testing of an animation.

This function performs the same function to
[KeyframeSequenceProvider:RegisterKeyframeSequence()](/docs/reference/engine/classes/KeyframeSequenceProvider.md) however this
function generates an _active://_ URL instead of a hash.

The ID generated can be used in an [Animation.AnimationId](/docs/reference/engine/classes/Animation.md) property
for testing.

The asset ID generated by this function is temporary and cannot be used
outside of Studio. Developers wishing to generate an asset ID that can be
used online should upload the [KeyframeSequence](/docs/reference/engine/classes/KeyframeSequence.md) to Roblox.

*Security: None · Thread Safety: Unsafe · Capabilities: Animation*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `keyframeSequence` | `Instance` |  | The [KeyframeSequence](/docs/reference/engine/classes/KeyframeSequence.md) to be used. |

**Returns:** `ContentId` — A temporary asset ID generated for localized animation playback.

**Create temporary animation**

This code sample contains a simple function to generate an [Animation](/docs/reference/engine/classes/Animation.md)
with a generated hash ID to preview a [KeyframeSequence](/docs/reference/engine/classes/KeyframeSequence.md) locally.

```lua
local KeyframeSequenceProvider = game:GetService("KeyframeSequenceProvider")

local function createPreviewAnimation(keyframeSequence)
	local hashId = KeyframeSequenceProvider:RegisterKeyframeSequence(keyframeSequence)
	local Animation = Instance.new("Animation")
	Animation.AnimationId = hashId
	return Animation
end

local keyframeSequence = Instance.new("KeyframeSequence")

local animation = createPreviewAnimation(keyframeSequence)

print(animation)
```

### Method: KeyframeSequenceProvider:RegisterKeyframeSequence

**Signature:** `KeyframeSequenceProvider:RegisterKeyframeSequence(keyframeSequence: Instance): ContentId`

Generates a temporary asset ID from a [KeyframeSequence](/docs/reference/engine/classes/KeyframeSequence.md) that can be
used for localized testing of an animation.

This function performs the same function to
[KeyframeSequenceProvider:RegisterActiveKeyframeSequence()](/docs/reference/engine/classes/KeyframeSequenceProvider.md) however
this function generates a hash instead of an _active://_ URL.

The ID generated can be used for the [Animation.AnimationId](/docs/reference/engine/classes/Animation.md)
property to test animations.

The asset ID generated by this function is temporary and cannot be used
outside of Studio. Developers wishing to generate an asset ID that can be
used online should upload the [KeyframeSequence](/docs/reference/engine/classes/KeyframeSequence.md) to Roblox.

*Security: None · Thread Safety: Unsafe · Capabilities: Animation*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `keyframeSequence` | `Instance` |  | The [KeyframeSequence](/docs/reference/engine/classes/KeyframeSequence.md) to be used. |

**Returns:** `ContentId` — A temporary asset ID generated for localized animation playback.

**KeyframeSequenceProvider:RegisterKeyframeSequence**

```lua
local KeyframeSequenceProvider = game:GetService("KeyframeSequenceProvider")

local asset = KeyframeSequenceProvider:RegisterKeyframeSequence(workspace.KeyframeSequence)

local animation = Instance.new("Animation")
animation.Name = "TestAnimation"
animation.AnimationId = asset
animation.Parent = workspace
```

### Method: KeyframeSequenceProvider:GetAnimations

**Signature:** `KeyframeSequenceProvider:GetAnimations(userId: User): Instance`

This function returns an [InventoryPages](/docs/reference/engine/classes/InventoryPages.md) object which can be used
to iterate over animations owned by a specific user.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Animation*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `userId` | `User` |  | The user ID of the user. |

**Returns:** `Instance` — An [InventoryPages](/docs/reference/engine/classes/InventoryPages.md) of animations.

**KeyframeSequenceProvider GetAnimationsAsync**

This code sample includes a demonstration of how the content IDs of animations
belonging to a player can be downloaded using
[KeyframeSequenceProvider:GetAnimationsAsync()](/docs/reference/engine/classes/KeyframeSequenceProvider.md). To run this code be
sure to change the _USER_ID_ variable to the ID of the user whose animations
you want to download.

```lua
local KeyframeSequenceProvider = game:GetService("KeyframeSequenceProvider")

local USER_ID = 0 -- Insert your UserId here

local function extractPages(pagesObject)
	local array = {}
	while true do
		local thisPage = pagesObject:GetCurrentPage()
		for _, v in pairs(thisPage) do
			table.insert(array, v)
		end
		if pagesObject.IsFinished then
			break
		end
		pagesObject:AdvanceToNextPageAsync()
	end
	return array
end

local inventoryPages = KeyframeSequenceProvider:GetAnimationsAsync(USER_ID)

local animationIds = extractPages(inventoryPages)

for _, id in pairs(animationIds) do
	print(id)
end
print("total: ", #animationIds)
```

### Method: KeyframeSequenceProvider:GetKeyframeSequence

**Signature:** `KeyframeSequenceProvider:GetKeyframeSequence(assetId: ContentId): Instance`

> **Deprecated:** This function is deprecated and can lead to the game freezing until the animation is loaded. Developers are recommended to use [KeyframeSequenceProvider:GetKeyframeSequenceAsync()](/docs/reference/engine/classes/KeyframeSequenceProvider.md) instead.

Returns a [KeyframeSequence](/docs/reference/engine/classes/KeyframeSequence.md) from a given asset URL.

*Security: PluginSecurity · Thread Safety: Unsafe · Capabilities: Animation*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `assetId` | `ContentId` |  | The content ID of the animation. |

**Returns:** `Instance` — The [KeyframeSequence](/docs/reference/engine/classes/KeyframeSequence.md) found.

### Method: KeyframeSequenceProvider:GetKeyframeSequenceById

**Signature:** `KeyframeSequenceProvider:GetKeyframeSequenceById(assetId: int64, useCache: boolean): Instance`

> **Deprecated:** This function is deprecated and can lead to the game freezing until the animation is loaded. Developers are recommended to use [KeyframeSequenceProvider:GetKeyframeSequenceAsync()](/docs/reference/engine/classes/KeyframeSequenceProvider.md) instead.

Returns a [KeyframeSequence](/docs/reference/engine/classes/KeyframeSequence.md) from the supplied assetId. Can
optionally cache to reduce unnecessary loading freezes.

*Security: PluginSecurity · Thread Safety: Unsafe · Capabilities: Animation*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `assetId` | `int64` |  | The content ID of the animation. |
| `useCache` | `boolean` |  | True if a cached version can be returned. |

**Returns:** `Instance` — The [KeyframeSequence](/docs/reference/engine/classes/KeyframeSequence.md) found.

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