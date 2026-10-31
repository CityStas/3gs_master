---
name: Pants
last_updated: 2026-10-30T19:55:52Z
inherits:
  - Clothing
  - CharacterAppearance
  - Instance
  - Object
type: class
memory_category: Instances
summary: "Displays a Pants texture from the Roblox website to display on a Humanoid rig."
---

# Class: Pants

> Displays a Pants texture from the Roblox website to display on a
> [Humanoid](/docs/reference/engine/classes/Humanoid.md) rig.

## Description

The `Pants` object displays a pants texture from Roblox on a [Humanoid](/docs/reference/engine/classes/Humanoid.md)
rig. Pants cover the torso and legs, and will be covered by a [Shirt](/docs/reference/engine/classes/Shirt.md) on
the torso. To be visible, a `Pants` must be a sibling of a [Humanoid](/docs/reference/engine/classes/Humanoid.md)
and have its [PantsTemplate](/docs/reference/engine/classes/Pants.md) property set to an
appropriate texture such as `rbxassetid://86896501`. The pants texture may be
colorized using the [Clothing.Color3](/docs/reference/engine/classes/Clothing.md) property.

Pants are automatically loaded on [Player](/docs/reference/engine/classes/Player.md) characters if their avatar is
wearing one.

## Code Samples

**Change Shirt / Pants**

This sample includes a simple function to change the texture of the `Shirt`
and `Pants` worn by a player's character. If shirt and pants don't exist then
they are created. Note, this should be run every time the character spawns. If
a developer is looking to permanently change a character's appearance to a
preset it is recommended they use [Player.CharacterAppearance](/docs/reference/engine/classes/Player.md).

```lua
local Players = game:GetService("Players")

local function replaceClothes(player)
	local character = player.Character
	if character then
		-- look for shirts / pants
		local shirt = character:FindFirstChildOfClass("Shirt")
		local pants = character:FindFirstChildOfClass("Pants")
		-- create shirts / pants if they don't exist
		if not shirt then
			shirt = Instance.new("Shirt")
			shirt.Parent = character
		end
		if not pants then
			pants = Instance.new("Pants")
			pants.Parent = character
		end
		-- reset shirt / pants content ids
		shirt.ShirtTemplate = "http://www.roblox.com/asset/?id=83326831"
		pants.PantsTemplate = "http://www.roblox.com/asset/?id=10045638"
	end
end

for _index, player in ipairs(Players:GetPlayers()) do
	replaceClothes(player)
end
```

## Properties

### Property: Pants.PantsTemplate

```json
{
  "type": "ContentId",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Appearance",
  "capabilities": [
    "AvatarAppearance"
  ]
}
```

The content ID link pointing to the pants template hosted on Roblox.

This content ID is different than the website URL of the pants. It can be
found by pasting the website URL of the pants into the **PantsTemplate**
property in Studio. Alternatively, [InsertService:LoadAsset()](/docs/reference/engine/classes/InsertService.md) can
be used to insert the pants into the workspace, for example:

```
local InsertService = game:GetService("InsertService")
local Workspace = game:GetService("Workspace")

local webURL = "https://www.roblox.com/catalog/1804739/Jeans"
local assetId = tonumber(string.match(webURL, "%d+") or 0)  -- Extract the number
local success, model = pcall(function()
	return InsertService:LoadAsset(assetId)
end)
if success then
	model.Parent = Workspace
end
```

For a [Shirt](/docs/reference/engine/classes/Shirt.md) object's template, see [Shirt.ShirtTemplate](/docs/reference/engine/classes/Shirt.md).

**Change Shirt / Pants**

This sample includes a simple function to change the texture of the `Shirt`
and `Pants` worn by a player's character. If shirt and pants don't exist then
they are created. Note, this should be run every time the character spawns. If
a developer is looking to permanently change a character's appearance to a
preset it is recommended they use [Player.CharacterAppearance](/docs/reference/engine/classes/Player.md).

```lua
local Players = game:GetService("Players")

local function replaceClothes(player)
	local character = player.Character
	if character then
		-- look for shirts / pants
		local shirt = character:FindFirstChildOfClass("Shirt")
		local pants = character:FindFirstChildOfClass("Pants")
		-- create shirts / pants if they don't exist
		if not shirt then
			shirt = Instance.new("Shirt")
			shirt.Parent = character
		end
		if not pants then
			pants = Instance.new("Pants")
			pants.Parent = character
		end
		-- reset shirt / pants content ids
		shirt.ShirtTemplate = "http://www.roblox.com/asset/?id=83326831"
		pants.PantsTemplate = "http://www.roblox.com/asset/?id=10045638"
	end
end

for _index, player in ipairs(Players:GetPlayers()) do
	replaceClothes(player)
end
```

### Property: Pants.PantsTemplateContent

```json
{
  "type": "Content",
  "access": "ReadWrite",
  "security": {
    "read": "None",
    "write": "None"
  },
  "serialization": {
    "can_load": true,
    "can_save": true
  },
  "thread_safety": "ReadSafe",
  "category": "Appearance",
  "capabilities": [
    "AvatarAppearance"
  ]
}
```

Specifies the pants texture using an
[asset URI](/docs/en-us/projects/assets.md#asset-uris). Although this
property uses Datatype.Content, it does not support [EditableImage](/docs/reference/engine/classes/EditableImage.md)
objects.

Setting either `PantsTemplateContent` or [Pants.PantsTemplate](/docs/reference/engine/classes/Pants.md)
updates the other; both reflect the same texture.

## Inherited Members

### From [Clothing](/docs/reference/engine/classes/Clothing.md)

- **Property `Color3`** (`Color3`): Determines the colorization to be applied to the Clothing texture.

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