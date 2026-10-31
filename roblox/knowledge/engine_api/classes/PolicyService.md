---
name: PolicyService
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
summary: "Helps you query information regarding policy compliance for players around the world based on age range, location, and platform type."
---

# Class: PolicyService

> Helps you query information regarding policy compliance for players around the
> world based on age range, location, and platform type.

## Description

`PolicyService` helps you query information regarding policy compliance for
players around the world based on age range, location, and platform type.

## Methods

### Method: PolicyService:CanViewBrandProjectAsync

**Signature:** `PolicyService:CanViewBrandProjectAsync(player: Player, brandProjectId: string): boolean`

Determines if a user can see brand project assets inside your experience.
This method lets you work with brands to only show commercial assets to
brand-compliant audiences.

To use `CanViewBrandProjectAsync`, you must use a brand project ID
provided by Roblox. To request a brand project ID,
<a href="https://docs.google.com/forms/d/e/1FAIpQLSfGTRQwATB2wUg0P4HUSTtyXrhptFahJifo1ew84SyqtfSBfg/viewform">contact
us</a>.

You must call this method on a server-side Script and wrap it in a
[LuaGlobals.pcall()](/docs/reference/engine/globals/LuaGlobals.md).

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Basic*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `player` | `Player` |  | The `Player` object you're trying to show the brand project to. |
| `brandProjectId` | `string` |  | The brand project ID provided by Roblox. Represents all assets associated with a brand project. |

**Returns:** `boolean` — Whether or not the brand project can be shown to the specific user.

**Server-side code sample**

You must call `CanViewBrandProjectAsync` from the server-side and then fire an
event on the client. Calling this method from the client-side returns an
error.

```lua
-- In ServerScriptService
local Players = game:GetService("Players")
local ReplicatedStorage = game:GetService("ReplicatedStorage")
local PolicyService = game:GetService("PolicyService")

-- Pre-created RemoteEvent in ReplicatedStorage
local RemoteEvent = ReplicatedStorage:WaitForChild("RemoteEvent")

local brandedAsset = ReplicatedStorage:WaitForChild("BrandedAsset")
local defaultAsset = Instance.new("Part")

Players.PlayerAdded:Connect(function(player)
	-- PolicyService:CanViewBrandProjectAsync can only be called from the Server
	local success, canView = pcall(function()
		return PolicyService:CanViewBrandProjectAsync(player, "BRP-0123456789")
	end)

	if success and canView then
		RemoteEvent:FireClient(player, brandedAsset)
	else
		RemoteEvent:FireClient(player, defaultAsset)
	end
end)
```

**Client-side code sample**

```lua
-- In StarterPlayerScripts
local Players = game:GetService("Players")
local ReplicatedStorage = game:GetService("ReplicatedStorage")

-- Pre-created RemoteEvent in ReplicatedStorage
local RemoteEvent = ReplicatedStorage:WaitForChild("RemoteEvent")

RemoteEvent.OnClientEvent:Connect(function(partToLoad)
	local clonedPart = partToLoad:Clone()
	clonedPart.Parent = workspace
end)
```

### Method: PolicyService:GetPolicyInfoForPlayerAsync

**Signature:** `PolicyService:GetPolicyInfoForPlayerAsync(player: Instance): Dictionary`

Returns policy information about a player based on geolocation, age group,
and platform. The structure of the returned dictionary is as follows:

| Name | Type | Required for | Description |
| --- | --- | --- | --- |
| `AreAdsAllowed` | Boolean | Any experience that includes [immersive ads](/docs/en-us/production/monetization/immersive-ads.md). | When `true`, the player might see immersive ads within an experience. |
| `ArePaidRandomItemsRestricted` | Boolean | Any experience that has paid random items. | When `true`, the player can **not** interact with paid random item generators, either via in‑experience currency bought with Robux or Robux directly. |
| `IsContentSharingAllowed` | Boolean | Any feature in the experience that enables users to create content (e.g. text, images, video, audio) that other users can see in the experience or allows user to share content within experiences. | When `true`, the player can use features related to sharing UGC within an experience, such as uploading a screen capture, sharing a video, or posting an image to a content feed that other users can see. |
| `IsEligibleToPurchaseCommerceProduct` | Boolean | Any experience that wants to sell [commerce products](/docs/en-us/production/monetization/commerce-products.md). | When `true`, the player is eligible to purchase commerce products within an experience. |
| `IsEligibleToPurchaseSubscription` | Boolean | Any experience that wants to sell subscriptions. | When `true`, the player is eligible to purchase subscriptions within an experience. |
| `IsPaidItemTradingAllowed` | Boolean | Any experience that allows users to purchase virtual items that they can trade with other players. | When `true`, the player can trade virtual items that they purchased with in-experience currency or Robux. |
| `IsPhotoToAvatarAllowed` | Boolean | Any experience that uses the Photo-to-Avatar APIs. | When `true`, the player is permitted by policy to use the Photo-to-Avatar API [AvatarCreationService:PromptSelectAvatarGenerationImageAsync()](/docs/reference/engine/classes/AvatarCreationService.md). This flag reflects age (for example, users under 13) and regional restrictions, which are evaluated server-side. Check it before calling Photo-to-Avatar APIs to avoid policy-related errors. Note that a `true` value does not by itself guarantee the prompt will succeed: camera and photo-library availability is checked separately on the player's device, so calls can still fail on platforms where camera access is unavailable. |
| `IsSubjectToChinaPolicies` | Boolean | Any experience that is available in China. | When `true`, an experience should enforce compliance changes. See [this forum post](https://devforum.roblox.com/t/new-programs-available-roblox-china-licensed-to-operate/1023361) for more information. |
| `AllowedExternalLinkReferences` | Array | Not required. | This is a legacy field. It always returns an empty array. |
| `IsEndlessContentLoadAllowed` | Boolean | Any experience that includes a feature where content loads automatically and endlessly as the user scrolls, such as a feed, providing an endless flow of media content without requiring the user to engage in any specific interaction such as manual "load more" actions or separate pagination. | When `true`, the player can use features with endless content loading within an experience. |
| `IsEndlessContentAutoplayAllowed` | Boolean | Any experience that contains media content (video or audio) that automatically and endlessly plays without requiring user interaction or initiation, for example clicking a play button. | When `true`, the player can use features within an experience that automatically and endlessly play media content. |

##### Exceptions

Like any async call, this method needs to be wrapped in
[LuaGlobals.pcall()](/docs/reference/engine/globals/LuaGlobals.md) and error-handled properly. A full list of
possible error messages and their reasons is:

| Message | Reason |
| --- | --- |
| Instance was not a player | The `player` parameter is not a [Player](/docs/reference/engine/classes/Player.md) instance. |
| Players not found | Internal error that the [Players](/docs/reference/engine/classes/Players.md) object is missing. |
| This method cannot be called on the client for a non-local player | This method cannot be called on the client for a non-local [Player](/docs/reference/engine/classes/Player.md). |
| GetPolicyInfoForPlayerAsync is called too many times | Internal error that `GetPolicyInfoForPlayerAsync()` is called more than 100 (current setting) times before an HTTP response comes back. |

See also [LocalizationService:GetCountryRegionForPlayerAsync()](/docs/reference/engine/classes/LocalizationService.md)
which returns a country/region code string according to the player's
client IP geolocation.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Basic*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `player` | `Instance` |  | The [Player](/docs/reference/engine/classes/Player.md) to get policy information for. |

**Returns:** `Dictionary` — A dictionary containing information about the policy information of
the requested player; see above for the dictionary structure.

**Getting Policy Information for a Player**

This code sample gets policy information for the local player and warns if
they cannot interact with paid random item generators.

```lua
local PolicyService = game:GetService("PolicyService")
local Players = game:GetService("Players")

local player = Players.LocalPlayer

local success, result = pcall(function()
	return PolicyService:GetPolicyInfoForPlayerAsync(player)
end)

if not success then
	warn("PolicyService error: " .. result)
elseif result.ArePaidRandomItemsRestricted then
	warn("Player cannot interact with paid random item generators")
end
```

**Getting Policy Information for a Player**

This code sample gets policy information for the local player and warns if
they cannot purchase a real-world commerce product.

```lua
local PolicyService = game:GetService("PolicyService")
local Players = game:GetService("Players")

local player = Players.LocalPlayer

local success, result = pcall(function()
	return PolicyService:GetPolicyInfoForPlayerAsync(player)
end)

if not success then
	warn("PolicyService error: " .. result)
elseif not result.IsEligibleToPurchaseCommerceProduct then
	warn("Player is not eligible to purchase commerce products")
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