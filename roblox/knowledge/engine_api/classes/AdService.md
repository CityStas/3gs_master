---
name: AdService
last_updated: 2026-10-30T19:55:51Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
tags:
  - NotCreatable
  - Service
summary: "The service responsible for in-experience advertising."
---

# Class: AdService

> The service responsible for in-experience advertising.

## Description

[AdService](/docs/reference/engine/classes/AdService.md) is responsible for in-experience advertising. This includes
[rewarded video](/docs/en-us/production/promotion/rewarded-video-ads.md) and
[ad integrations](/docs/en-us/production/promotion/ad-integrations.md).

## Methods

### Method: AdService:CreateAdRewardFromDevProductId

**Signature:** `AdService:CreateAdRewardFromDevProductId(devProductId: int64): AdReward`

Constructs an [AdReward](/docs/reference/engine/datatypes/AdReward.md) that wraps the given developer product
so it can be passed to
[ShowRewardedVideoAdAsync](/docs/reference/engine/classes/AdService.md).
When the user watches the entire rewarded video ad, the developer product
identified by `devProductId` is granted through the
[ProcessReceipt](/docs/reference/engine/classes/MarketplaceService.md) callback with a
`ProductPurchaseChannel` of [ProductPurchaseChannel.AdReward](/docs/reference/engine/enums/ProductPurchaseChannel.md).

*Security: None · Thread Safety: Unsafe · Capabilities: Monetization*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `devProductId` | `int64` |  | The ID of the developer product you want to grant as a reward. |

**Returns:** `AdReward` — An [AdReward](/docs/reference/engine/datatypes/AdReward.md) configured as a developer product reward for
the specified product.

### Method: AdService:GetAdAvailabilityNowAsync

**Signature:** `AdService:GetAdAvailabilityNowAsync(adFormat: AdFormat): GetAdAvailabilityNowResult`

This method may only be called from a [Script](/docs/reference/engine/classes/Script.md) with
[RunContext.Client](/docs/reference/engine/enums/RunContext.md).

Note that you should call this method as close as possible to the moment
you plan to show the ad. For example, if you have a "Watch video ad to get
a reward" button in a shop menu, only call this method when the user opens
the shop menu. This approach improves performance by preventing ads from
unnecessarily being held in memory, and it benefits CPM (cost-per-thousand
impressions) and earnings by optimizing the ad fill rate.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Monetization*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `adFormat` | `AdFormat` |  | The format of the requested ad. For example, [AdFormat.RewardedVideo](/docs/reference/engine/enums/AdFormat.md). |

**Returns:** `GetAdAvailabilityNowResult` — A dictionary that looks like
`{ AdAvailabilityResult: Enum.AdAvailabilityResult }`.

### Method: AdService:GetCampaignEligibilityAsync

**Signature:** `AdService:GetCampaignEligibilityAsync(campaignId: string, player?: Player?): GetCampaignEligibilityResult`

[GetCampaignEligibilityAsync](/docs/reference/engine/classes/AdService.md)
checks whether a [Player](/docs/reference/engine/classes/Player.md) is eligible to be shown a specific
[ad integration](/docs/en-us/production/promotion/ad-integrations.md)
campaign, returning a dictionary that looks like
`{ IsEligible: boolean }`.

Call this method and confirm that `result.IsEligible` is `true` before you
display any of the campaign's ad integration assets or register their
disclosure buttons with
[RegisterDisclosureButton](/docs/reference/engine/classes/AdService.md). All
ad integration assets should remain hidden until the [Player](/docs/reference/engine/classes/Player.md) is
confirmed eligible.

When called from the client, the `player` argument defaults to the
[LocalPlayer](/docs/reference/engine/classes/Players.md). When called from the server,
`player` is required. The call raises an error if the supplied
`campaignId` exceeds the maximum allowed length.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Monetization*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `campaignId` | `string` |  | The ID of the campaign that you want to check a [Player](/docs/reference/engine/classes/Player.md)'s eligibility for. |
| `player` | `Player?` | `nil` | The [Player](/docs/reference/engine/classes/Player.md) you want to check eligibility for. If omitted, it will default to the [LocalPlayer](/docs/reference/engine/classes/Players.md). On the server, `player` argument is required. |

**Returns:** `GetCampaignEligibilityResult` — A dictionary that looks like `{ IsEligible: boolean }`.

**Example Ad Integration**

Verifies that the LocalPlayer is eligible to see the ad integration campaign,
then inserts it into the world and registers the ad disclosure. This code
sample is meant to run on the client.

```lua
local AdService = game:GetService("AdService")
local ReplicatedStorage = game:GetService("ReplicatedStorage")
local Players = game:GetService("Players")

local YOUR_CAMPAIGN_ID = "123" -- Enter your ad integration campaign ID from ads manager here.
local AD_INTEGRATION_IDS = {
	-- Enter your ad integration placement ID's for each asset you registered as part of your
	-- ad integration campaign.
	BrandedBuilding = "abc-123",
	BrandedScreenGui = "xyz-789",
}

-- Verify that the LocalPlayer is eligible to see your campaign
local success, result = pcall(function()
	return AdService:GetCampaignEligibilityAsync(YOUR_CAMPAIGN_ID)
end)

if success and result.IsEligible then
	-- All ad integration assets should be hidden by default. Once you know that the
	-- player is eligible, then it's safe to start showing the ad integration assets.
	local brandedBuildingModel = ReplicatedStorage.adIntegration.building
	local brandedBuildingModelDisclosureBillboardGui = brandedBuildingModel.disclosureBillboardGui

	-- Don't forget to register your ad disclosure buttons so players know who is paying for the ad!
	AdService:RegisterDisclosureButton(
		brandedBuildingModelDisclosureBillboardGui.adDisclosureButton,
		AD_INTEGRATION_IDS.BrandedBuilding
	)
	brandedBuildingModelDisclosureBillboardGui.Parent = Players.LocalPlayer.PlayerGui
	brandedBuildingModel.Parent = game.Workspace

	local brandedScreenGui = ReplicatedStorage.adIntegration.screenGui
	AdService:RegisterDisclosureButton(brandedScreenGui.adDisclosureButton, AD_INTEGRATION_IDS.BrandedScreenGui)
	brandedScreenGui.Parent = Players.LocalPlayer.PlayerGui
end
```

### Method: AdService:RegisterAdOpportunityAsync

**Signature:** `AdService:RegisterAdOpportunityAsync(instance: Instance, placementId: int64?): ()`

This method may only be called from a [Script](/docs/reference/engine/classes/Script.md) with
[RunContext.Client](/docs/reference/engine/enums/RunContext.md).

Registers a [GuiButton](/docs/reference/engine/classes/GuiButton.md) for ad opportunity tracking. Once
registered, the system periodically checks whether the button is visible
and unobstructed (the topmost input-sinking element at its center point).
These visibility transitions are reported as ad opportunity impressions
and used to measure the rate at which users are presented with, and choose
to watch, rewarded video ads.

The `instance` must be a [GuiButton](/docs/reference/engine/classes/GuiButton.md) that is a descendant of a
[ScreenGui](/docs/reference/engine/classes/ScreenGui.md) under [PlayerGui](/docs/reference/engine/classes/PlayerGui.md). If the instance is moved out of
a valid hierarchy at runtime, tracking pauses automatically and resumes
when it returns to a valid ancestor. Call
[UnregisterAdOpportunity](/docs/reference/engine/classes/AdService.md) to
stop tracking the instance.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Monetization*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `instance` | `Instance` |  | The [GuiButton](/docs/reference/engine/classes/GuiButton.md) to track as a rewarded video ad opportunity. Must be a descendant of a [ScreenGui](/docs/reference/engine/classes/ScreenGui.md). |
| `placementId` | `int64?` |  | The ID of the placement of the rewarded video ad inside the experience. Allows for reporting on the performance of individual ad placements. |

**Returns:** `()`

**Track ad opportunities**

Tracks ad opportunities for rewarded video ads.

```lua
local AdService = game:GetService("AdService")
local playerGui = game:GetService("Players").LocalPlayer:WaitForChild("PlayerGui")

-- Create the ScreenGui and the Button
local screenGui = Instance.new("ScreenGui", playerGui)
local adButton = Instance.new("TextButton", screenGui)

-- Register the button with AdService
local success, err = pcall(function()
	-- The second parameter is an optional Placement ID (Number) parameter generated in the Creator Hub.
	-- If you choose not to provide a Placement ID, the ad opportunity is tracked under the default placement.
	AdService:RegisterAdOpportunityAsync(adButton, 1234567891234567)
end)

if not success then
	warn("Failed to register ad opportunity:", err)
end
```

### Method: AdService:RegisterDisclosureButton

**Signature:** `AdService:RegisterDisclosureButton(disclosureButton: GuiButton, adIntegrationPlacementId: string): ()`

This method may only be called from a [Script](/docs/reference/engine/classes/Script.md) with
[RunContext.Client](/docs/reference/engine/enums/RunContext.md).

[RegisterDisclosureButton](/docs/reference/engine/classes/AdService.md)
marks a button in your experience as an ad disclosure for an ad
integration. When a user clicks it, they can see who is paying for the ad.
See
[ad integrations](/docs/en-us/production/promotion/ad-integrations.md#labeling-and-disclosure)
for guidance on what the disclosures should look like and when they should
be visible.

Note: you must verify that the [LocalPlayer](/docs/reference/engine/classes/Players.md) is
eligible to see the associated ad integration campaign by calling
[GetCampaignEligibilityAsync](/docs/reference/engine/classes/AdService.md)
and verifying that `result.IsEligible` is `true` before attempting to
register a disclosure button for it. If you do not wait, or the
[LocalPlayer](/docs/reference/engine/classes/Players.md) is not eligible to see the
associated campaign, then
[RegisterDisclosureButton](/docs/reference/engine/classes/AdService.md) will
raise an error.

*Security: None · Thread Safety: Unsafe · Capabilities: Monetization*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `disclosureButton` | `GuiButton` |  | The [GuiButton](/docs/reference/engine/classes/GuiButton.md) you want to mark as an ad integration disclosure. The [GuiButton](/docs/reference/engine/classes/GuiButton.md) must follow labeling guidelines outlined [here](/docs/en-us/production/promotion/ad-integrations.md#labeling-and-disclosure). |
| `adIntegrationPlacementId` | `string` |  | The ID of the placement that this disclosure is attached to. |

**Returns:** `()`

### Method: AdService:ShowRewardedVideoAdAsync

**Signature:** `AdService:ShowRewardedVideoAdAsync(player: Player, reward: AdReward, placementId: int64?): ShowAdResult`

**Warning**: Rewarded Video ads must be user opt-in and clearly disclosed.
For details, review our
[eligibility requirements](/docs/en-us/production/promotion/rewarded-video-ads.md#eligibility-requirements)
and
[advertising standards](https://en.help.roblox.com/hc/en-us/articles/13722260778260-Advertising-Standards).

This method may only be called from a [Script](/docs/reference/engine/classes/Script.md) with
[RunContext.Server](/docs/reference/engine/enums/RunContext.md).

Note: before calling this method, you must first verify that the specified
user has a rewarded video ad available to show by calling
[GetAdAvailabilityNowAsync](/docs/reference/engine/classes/AdService.md).
If the client does not have an available ad, then
[ShowRewardedVideoAdAsync](/docs/reference/engine/classes/AdService.md) will
return [ShowAdResult.AdNotReady](/docs/reference/engine/enums/ShowAdResult.md).

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: UI, Monetization*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `player` | `Player` |  | The [Player](/docs/reference/engine/classes/Player.md) to trigger a rewarded video ad play for. |
| `reward` | `AdReward` |  | The [AdReward](/docs/reference/engine/datatypes/AdReward.md) to grant the user after they view the ad. |
| `placementId` | `int64?` |  | The ID of the placement of the rewarded video ad inside the experience. Allows for reporting on the performance of individual ad placements. |

**Returns:** `ShowAdResult` — The [ShowAdResult](/docs/reference/engine/enums/ShowAdResult.md) of the client's ad presentation. You should
not use this result to grant the reward. Instead, you should grant the
reward from your
[ProcessReceipt](/docs/reference/engine/classes/MarketplaceService.md)
implementation. For
[developer products](/docs/en-us/production/monetization/developer-products.md)
earned through rewarded video ads, the
`receipt.ProductPurchaseChannel` will be
[ProductPurchaseChannel.AdReward](/docs/reference/engine/enums/ProductPurchaseChannel.md).

**Show Rewarded Video Ads**

An example of a rewarded video implementation.

```lua
-- In a script on the client:
local AdService = game:GetService("AdService")
local Players = game:GetService("Players")
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local rewardedVideoButton: GuiButton =
	Players.LocalPlayer.PlayerGui:WaitForChild("myAdGui"):WaitForChild("watchRewardedVideoButton")
local watchRewardedVideoAdRemoteEvent: RemoteEvent = ReplicatedStorage:WaitForChild("watchRewardedVideoAd")

-- The client doesn't have an ad ready yet; hide the button
rewardedVideoButton.Visible = false

local success, result = pcall(function()
	return AdService:GetAdAvailabilityNowAsync(Enum.AdFormat.RewardedVideo)
end)

if success and result.AdAvailabilityResult == Enum.AdAvailabilityResult.IsAvailable then
	-- Show the button if an ad is avilable
	rewardedVideoButton.Visible = true
end

rewardedVideoButton.Activated:Connect(function()
	watchRewardedVideoAdRemoteEvent:FireServer()
	-- The IsAvailable result is only good for a single ad play. To play another ad, you would have to call
	-- GetAdAvailabilityNowAsync and check availability again.
	rewardedVideoButton.Visible = false
end)

-- In a script on the server:
local AdService = game:GetService("AdService")
local MarketplaceService = game:GetService("MarketplaceService")
local Players = game:GetService("Players")
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local watchRewardedVideoAdRemoteEvent: RemoteEvent = ReplicatedStorage:WaitForChild("watchRewardedVideoAd")

local REWARDED_VIDEO_PRODUCT_ID = 123 -- Enter your dev product ID here

local function grantReward(player: Player)
	print(`giving a reward to {player.Name}!`)
end

MarketplaceService.ProcessReceipt = function(receiptInfo)
	local player = Players:GetPlayerByUserId(receiptInfo.PlayerId)
	if not player then
		return Enum.ProductPurchaseDecision.NotProcessedYet
	end

	if receiptInfo.ProductId == REWARDED_VIDEO_PRODUCT_ID then
		if receiptInfo.ProductPurchaseChannel == Enum.ProductPurchaseChannel.AdReward then
			print(`player {receiptInfo.PlayerId} earned my rewarded video reward by watching an ad`)
		else
			print(`player {receiptInfo.PlayerId} purchased my rewarded video product with Robux`)
		end

		-- Give the player their reward
		grantReward(player)
	else
		-- Handle other products
	end

	return Enum.ProductPurchaseDecision.PurchaseGranted
end

watchRewardedVideoAdRemoteEvent.OnServerEvent:Connect(function(player)
	local reward = AdService:CreateAdRewardFromDevProductId(REWARDED_VIDEO_PRODUCT_ID)
	AdService:ShowRewardedVideoAdAsync(player, reward)
end)
```

### Method: AdService:UnregisterAdOpportunity

**Signature:** `AdService:UnregisterAdOpportunity(instance: Instance): ()`

Removes `instance` from the ad opportunity tracker so that it no longer
counts toward the rewarded video ad opportunity reporting started by
[RegisterAdOpportunityAsync()](/docs/reference/engine/classes/AdService.md).
Call it once an instance should no longer be treated as an ad opportunity,
such as when its associated UI is closed or removed.

If the supplied `instance` is not currently being tracked, this method has
no effect.

*Security: None · Thread Safety: Unsafe · Capabilities: Monetization*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `instance` | `Instance` |  | The instance to stop tracking. This should be an instance that you previously passed to [RegisterAdOpportunityAsync()](/docs/reference/engine/classes/AdService.md). |

**Returns:** `()`

### Method: AdService:ShowVideoAd

**Signature:** `AdService:ShowVideoAd(): ()`

> **Deprecated:** [ShowVideoAd](/docs/reference/engine/classes/AdService.md) has been decommissioned and is no longer operational.

Show mobile video advertisements.

*Security: None · Thread Safety: Unsafe · Capabilities: Monetization*

**Returns:** `()`

## Events

### Event: AdService.VideoAdClosed

**Signature:** `AdService.VideoAdClosed(adShown: boolean)`

> **Deprecated:** [VideoAdClosed](/docs/reference/engine/classes/AdService.md) has been decommissioned and is no longer operational.

Fires when an [AdService](/docs/reference/engine/classes/AdService.md) video closes.

*Security: None · Capabilities: Monetization*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `adShown` | `boolean` |  |

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