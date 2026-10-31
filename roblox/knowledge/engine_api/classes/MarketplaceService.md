---
name: MarketplaceService
last_updated: 2026-10-30T19:55:52Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
tags:
  - NotCreatable
  - Service
summary: "The service responsible for in-experience transactions."
---

# Class: MarketplaceService

> The service responsible for in-experience transactions.

## Description

[MarketplaceService](/docs/reference/engine/classes/MarketplaceService.md) is responsible for in-experience transactions. The
most notable methods are
[PromptProductPurchase](/docs/reference/engine/classes/MarketplaceService.md) and
[PromptPurchase](/docs/reference/engine/classes/MarketplaceService.md), as well as the
callback [ProcessReceipt](/docs/reference/engine/classes/MarketplaceService.md) which must
be defined so that developer product transactions do not fail.
[BindReceiptHandler](/docs/reference/engine/classes/MarketplaceService.md) is a newer
alternative that processes developer product receipts (and Robux transfer
receipts) through one or more bound handlers instead of the single
`ProcessReceipt` callback.

[MarketplaceService](/docs/reference/engine/classes/MarketplaceService.md) also has methods that fetch information about
[developer products](/docs/en-us/production/monetization/developer-products.md)
([GetProductInfoAsync](/docs/reference/engine/classes/MarketplaceService.md) and
[GetDeveloperProductsAsync](/docs/reference/engine/classes/MarketplaceService.md)),
[passes](/docs/en-us/production/monetization/passes.md)
([UserOwnsGamePassAsync()](/docs/reference/engine/classes/MarketplaceService.md)),
and other assets
([PlayerOwnsAssetAsync](/docs/reference/engine/classes/MarketplaceService.md),
[PlayerOwnsBundleAsync](/docs/reference/engine/classes/MarketplaceService.md)).

Understanding [MarketplaceService](/docs/reference/engine/classes/MarketplaceService.md) is the first step towards learning to
[monetize](/docs/en-us/production/monetization.md) an experience on Roblox,
as well as learning to use [DataStoreService](/docs/reference/engine/classes/DataStoreService.md), which is responsible for
saving and loading all data related to purchases.

## Methods

### Method: MarketplaceService:BindReceiptHandler

**Signature:** `MarketplaceService:BindReceiptHandler(transactionType: ReceiptType, handler: Function, filter: Array?): RBXScriptConnection`

`BindReceiptHandler` registers a callback to process receipts of a
specific [ReceiptType](/docs/reference/engine/enums/ReceiptType.md). You can use it to handle developer product
receipts ([ReceiptType.DeveloperProduct](/docs/reference/engine/enums/ReceiptType.md)) and Robux transfer receipts
([ReceiptType.RobuxTransferSender](/docs/reference/engine/enums/ReceiptType.md) and
[ReceiptType.RobuxTransferReceiver](/docs/reference/engine/enums/ReceiptType.md)).

For [ReceiptType.DeveloperProduct](/docs/reference/engine/enums/ReceiptType.md), you can register handlers in two
ways:

- **Filtered** &mdash; Pass a `filter` array of developer product IDs so
  the handler only fires for receipts whose `ProductId` is in that array.
  Use this to route specific products to dedicated handlers.
- **Catch-all** &mdash; Omit `filter` so the handler fires for any
  developer product receipt not already claimed by a filtered handler.

For developer products, `BindReceiptHandler` is an alternative to the
legacy [ProcessReceipt](/docs/reference/engine/classes/MarketplaceService.md) callback.
A bound handler takes precedence; if no bound handler matches a developer
product receipt, it falls through to `ProcessReceipt`. This lets you adopt
`BindReceiptHandler` incrementally without removing an existing
`ProcessReceipt` callback.

The `handler` callback receives a receipt info dictionary and must return
an [ReceiptDecision](/docs/reference/engine/enums/ReceiptDecision.md) value:

- [ReceiptDecision.Processed](/docs/reference/engine/enums/ReceiptDecision.md) &mdash; Indicates the receipt was
  successfully processed and all benefits have been granted. The receipt
  is marked as complete.
- [ReceiptDecision.NotProcessedYet](/docs/reference/engine/enums/ReceiptDecision.md) &mdash; Indicates the receipt has
  not been processed yet. The receipt remains unresolved and will be
  delivered again on the next opportunity.

#### Receipt Info Dictionary

The receipt info dictionary passed to the `handler` contains the following
fields:

| Key | Type | Description |
| --- | --- | --- |
| `PurchaseId` | string | A unique identifier for this specific receipt. |
| `PlayerId` | number | The [Player.UserId](/docs/reference/engine/classes/Player.md) of the user associated with this receipt. |
| `PlaceIdWherePurchased` | number | The place ID where the transaction was initiated. |
| `ReceiptType` | [ReceiptType](/docs/reference/engine/enums/ReceiptType.md) | The type of this receipt. |
| `ProductId` | number | The developer product ID. Only present for [ReceiptType.DeveloperProduct](/docs/reference/engine/enums/ReceiptType.md) receipts. |
| `CurrencyType` | [CurrencyType](/docs/reference/engine/enums/CurrencyType.md) | The currency used for the purchase. Only present for [ReceiptType.DeveloperProduct](/docs/reference/engine/enums/ReceiptType.md) receipts. |
| `CurrencySpent` | number | The amount of Robux involved in the transaction. For [ReceiptType.DeveloperProduct](/docs/reference/engine/enums/ReceiptType.md) receipts, this is the product's price. For [ReceiptType.RobuxTransferSender](/docs/reference/engine/enums/ReceiptType.md) receipts, this is the amount sent. For [ReceiptType.RobuxTransferReceiver](/docs/reference/engine/enums/ReceiptType.md) receipts, this is the amount received. |
| `TransferRequestId` | string | The transfer request ID from [MarketplaceService:PromptRobuxTransferAsync()](/docs/reference/engine/classes/MarketplaceService.md). Only present for [ReceiptType.RobuxTransferSender](/docs/reference/engine/enums/ReceiptType.md) and [ReceiptType.RobuxTransferReceiver](/docs/reference/engine/enums/ReceiptType.md) receipts. |

#### Receipt Timing

For Robux transfer receipts, `handler` is invoked once the transfer
settles. A settled receipt is delivered to whichever server the user is
currently in (the user does not need to rejoin).

- [ReceiptType.RobuxTransferReceiver](/docs/reference/engine/enums/ReceiptType.md) &mdash; Delivered to the server
  the receiver is currently in once the transfer settles. If the receiver
  is offline at that time, delivery happens the next time they join a
  server.
- [ReceiptType.RobuxTransferSender](/docs/reference/engine/enums/ReceiptType.md) &mdash; Delivered immediately if
  the transfer settles synchronously. If the transfer is gated on receiver
  approval (for example, parental consent), delivery happens once the
  receiver accepts, to whichever server the sender is currently in or on
  their next join if they are offline.

For developer product receipts, `handler` is invoked when the purchase
completes while the buyer is on a server. If the handler returns
[ReceiptDecision.NotProcessedYet](/docs/reference/engine/enums/ReceiptDecision.md), or the buyer is not reachable, the
receipt remains unresolved and is redelivered on a later opportunity or
the next time the buyer joins a server.

The user must be on a server for `handler` to fire.

#### Errors

This method throws an error if:

- A handler is already registered for the same [ReceiptType](/docs/reference/engine/enums/ReceiptType.md) and
  product ID combination.
- A catch-all handler is already registered for the same
  [ReceiptType](/docs/reference/engine/enums/ReceiptType.md).

*Security: None · Thread Safety: Unsafe · Capabilities: Monetization*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `transactionType` | `ReceiptType` |  | The [ReceiptType](/docs/reference/engine/enums/ReceiptType.md) indicating which kind of receipt to handle. |
| `handler` | `Function` |  | A callback function that receives a receipt info dictionary and must return an [ReceiptDecision](/docs/reference/engine/enums/ReceiptDecision.md) value. |
| `filter` | `Array?` |  | An optional array of product IDs. When provided, the handler only fires for receipts matching those product IDs. Not supported for `RobuxTransferSender` or `RobuxTransferReceiver` receipt types. |

**Returns:** `RBXScriptConnection` — A [RBXScriptConnection](/docs/reference/engine/datatypes/RBXScriptConnection.md) that can be disconnected to
unregister the handler.

**MarketplaceService:BindReceiptHandler**

The following server-side [Script](/docs/reference/engine/classes/Script.md) example shows how to use
[MarketplaceService:BindReceiptHandler()](/docs/reference/engine/classes/MarketplaceService.md) to register handlers for Robux
transfer receipts. Both sender and receiver receipt types are handled to
acknowledge the transfer on each side.

```lua
-- NOTE: If your handler grants persistent benefits (currency, items), use
-- DataStoreService:UpdateAsync() on the TransferRequestId to prevent
-- double-granting when the same receipt is delivered to multiple servers.

local MarketplaceService = game:GetService("MarketplaceService")
local Players = game:GetService("Players")

-- Handle sender receipts (the player who sent Robux)
MarketplaceService:BindReceiptHandler(
	Enum.ReceiptType.RobuxTransferSender,
	function(receiptInfo)
		local player = Players:GetPlayerByUserId(receiptInfo.PlayerId)
		if not player then
			-- Player isn't on this server; defer so the receipt is
			-- redelivered to whichever server they're currently in
			return Enum.ReceiptDecision.NotProcessedYet
		end

		print(
			`{player.Name} sent {receiptInfo.CurrencySpent} Robux`
				.. ` (TransferRequestId: {receiptInfo.TransferRequestId})`
		)

		-- Grant any sender-side acknowledgement or update UI here

		return Enum.ReceiptDecision.Processed
	end
)

-- Handle receiver receipts (the player who received Robux)
MarketplaceService:BindReceiptHandler(
	Enum.ReceiptType.RobuxTransferReceiver,
	function(receiptInfo)
		local player = Players:GetPlayerByUserId(receiptInfo.PlayerId)
		if not player then
			return Enum.ReceiptDecision.NotProcessedYet
		end

		print(
			`{player.Name} received {receiptInfo.CurrencySpent} Robux`
				.. ` (TransferRequestId: {receiptInfo.TransferRequestId})`
		)

		-- Grant any receiver-side benefits or update UI here

		return Enum.ReceiptDecision.Processed
	end
)
```

**MarketplaceService:BindReceiptHandler**

The following server-side [Script](/docs/reference/engine/classes/Script.md) example shows how to use
[MarketplaceService:BindReceiptHandler()](/docs/reference/engine/classes/MarketplaceService.md) to process developer product
receipts. A filtered handler grants a single product, and the benefit is
granted idempotently with [GlobalDataStore:UpdateAsync()](/docs/reference/engine/classes/GlobalDataStore.md) keyed on the
receipt's `PurchaseId` so the same receipt is never granted twice.

```lua
local MarketplaceService = game:GetService("MarketplaceService")
local DataStoreService = game:GetService("DataStoreService")
local Players = game:GetService("Players")

-- Replace with the developer product ID that grants 100 coins
local COINS_PRODUCT_ID = 123456789
local COINS_PER_PURCHASE = 100

local purchaseHistoryStore = DataStoreService:GetDataStore("PurchaseHistory")

-- Passing a filter array binds this handler only to the listed product IDs.
-- Omit the filter to register a catch-all handler that fires for any
-- developer product receipt not claimed by a filtered handler.
MarketplaceService:BindReceiptHandler(
	Enum.ReceiptType.DeveloperProduct,
	function(receiptInfo)
		local player = Players:GetPlayerByUserId(receiptInfo.PlayerId)
		if not player then
			-- The buyer isn't on this server; defer so the receipt is
			-- redelivered later or the next time they join a server
			return Enum.ReceiptDecision.NotProcessedYet
		end

		-- Grant the product exactly once, even if the same receipt is
		-- delivered more than once, by keying on PurchaseId. The callback
		-- records true only when the benefit is durably granted, so
		-- UpdateAsync resolves to true precisely when this receipt is done.
		local success, granted = pcall(function()
			return purchaseHistoryStore:UpdateAsync(receiptInfo.PurchaseId, function(alreadyGranted)
				if alreadyGranted then
					-- A previous delivery already granted this purchase; don't
					-- grant it again, but keep the receipt resolved
					return true
				end

				local leaderstats = player:FindFirstChild("leaderstats")
				local coins = leaderstats and leaderstats:FindFirstChild("Coins")
				if not coins then
					-- The player's stats aren't ready yet. Return nil to cancel
					-- the write so nothing is recorded as granted and the
					-- receipt is redelivered later
					return nil
				end

				coins.Value += COINS_PER_PURCHASE
				return true
			end)
		end)

		if not success or granted ~= true then
			-- A data store error occurred or the benefit wasn't granted; leave
			-- the receipt unresolved so it is redelivered later
			return Enum.ReceiptDecision.NotProcessedYet
		end

		return Enum.ReceiptDecision.Processed
	end,
	{ COINS_PRODUCT_ID }
)
```

### Method: MarketplaceService:GetDeveloperProductsAsync

**Signature:** `MarketplaceService:GetDeveloperProductsAsync(): Instance`

Returns a [Pages](/docs/reference/engine/classes/Pages.md) object which contains information for all of the
current experience's
[developer products](/docs/en-us/production/monetization/developer-products.md).

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: AssetRead*

**Returns:** `Instance` — A [Pages](/docs/reference/engine/classes/Pages.md) object whose entries describe the current experience's
developer products.

**MarketplaceService:GetDeveloperProductsAsync**

The below example would print the name, price, ID, description and icon
AssetId for all of the developer products which belong to the current game.

```lua
local MarketplaceService = game:GetService("MarketplaceService")

local developerProducts = MarketplaceService:GetDeveloperProductsAsync():GetCurrentPage()

for _, developerProduct in pairs(developerProducts) do
	for field, value in pairs(developerProduct) do
		print(field .. ": " .. value)
	end
	print(" ")
end
```

### Method: MarketplaceService:GetProductInfoAsync

**Signature:** `MarketplaceService:GetProductInfoAsync(assetId: int64, infoType?: InfoType): Dictionary`

This method provides information about an asset,
[developer product](/docs/en-us/production/monetization/developer-products.md),
or [pass](/docs/en-us/production/monetization/passes.md) based on the asset
ID and the [InfoType](/docs/reference/engine/enums/InfoType.md). If an item with the given ID does not exist,
this method throws an error.

Information about the queried item is provided in a dictionary with the
following keys. Note that not all information is provided or necessarily
relevant for the kind of product you're querying.

| Key | Type | Description |
| --- | --- | --- |
| `Name` | string | The name shown on the asset's page. |
| `Description` | string | The description shown on the asset's page; can be `nil` if blank. |
| `PriceInRobux` | number | The cost of purchasing the asset using Robux. |
| `UserBasePriceInRobux` | number | The base price of the asset in Robux before any discounts are applied. |
| `PriceDiscountDetails` | Array | An ordered list of discounts representing the difference between `UserBasePriceInRobux` and `PriceInRobux`. Each entry contains the following keys: |
|  | `Type`: The type of discount. `"RobloxPlusSubscription"` indicates that the discount was applied due to the user’s Roblox Plus subscription. |
|  | `AmountInRobux`: number — The value of the discount in Robux. |
|  | `Percent`: number — The percentage of the discount. |
| `ProductId` | number | The product ID if [InfoType](/docs/reference/engine/enums/InfoType.md) is `Product`. |
| `ProductType` | string | A string describing what the product is. Not to be confused with [MarketplaceProductType](/docs/reference/engine/enums/MarketplaceProductType.md). |
| `Created` | string | Timestamp of when the asset was created, for example `2022-01-02T10:30:45Z`. Formatted using ISO 8601. |
| `Updated` | string | Timestamp of when the asset was last updated by its creator, for example `2022-02-12T11:22:15Z`. Formatted using ISO 8601. |
| `ContentRatingTypeId` | number | Indicates whether the item is marked as 13+ in catalog. |
| `MinimumMembershipLevel` | number | The minimum subscription level necessary to purchase the item. |
| `IsPublicDomain` | boolean | Describes whether the asset can be taken for free. |
| `TargetId` | number | The ID of the product or asset. |

#### Creator Information

| Key | Type | Description |
| --- | --- | --- |
| `Creator` | table | Dictionary table of information describing the creator of the asset, containing the following fields: |
|  | `CreatorType`: Either `User` or `Group`. |
|  | `CreatorTargetId`: The ID of the creator user or group. |
|  | `HasVerifiedBadge`: Boolean of whether the creator has a verified badge. |
|  | `Name`: The name/username of the creator. |
|  | `Id`: Use `CreatorTargetId` instead. |

#### Asset Information

| Key | Type | Description |
| --- | --- | --- |
| `AssetId` | number | The asset ID if [InfoType](/docs/reference/engine/enums/InfoType.md) is `Asset`. |
| `AssetTypeId` | number | The type of asset. See [AssetType](/docs/reference/engine/enums/AssetType.md) for the asset type ID numbers. |
| `IconImageAssetId` | number | The asset ID of the product's icon, or `0` if there isn't one. |
| `IsForSale` | boolean | Describes whether the asset is purchasable. |
| `IsLimited` | boolean | Describes whether the asset is a Roblox Limited that is no longer (if ever) sold. |
| `IsLimitedUnique` | boolean | Describes whether the asset is a unique Roblox Limited ("Limited U") item that only has a fixed number sold. |
| `IsNew` | boolean | Describes whether the asset is marked as "new" in the catalog. |
| `Remaining` | number | The remaining number of times a limited unique item may be sold. |
| `Sales` | number | The number of times the asset has been sold. |

#### Collectibles Information

| Key | Type | Description |
| --- | --- | --- |
| `CollectibleItemId` | string | The unique item ID of the collectible. |
| `CollectibleProductId` | string | The unique product ID of the collectible. |
| `CollectiblesItemDetails` | table | Dictionary table of information describing the collectible, containing the following fields: |
|  | `CollectibleLowestAvailableResaleItemInstanceId`: The unique item instance ID of the lowest available resale for the collectible. |
|  | `CollectibleLowestAvailableResaleProductId`: The unique product ID of the lowest available resale for the collectible. |
|  | `CollectibleLowestResalePrice`: The lowest resale price for the collectible in Robux. |
|  | `IsForSale`: Boolean of whether the collectible is available for sale (not resale). |
|  | `IsLimited`: Boolean of whether or not the collectible is limited. |
|  | `TotalQuantity`: The total quantity of the collectible available for purchase (not resale). |

#### Sale Location Settings

| Key | Type | Description |
| --- | --- | --- |
| `CanBeSoldInThisGame` | boolean | Describes whether the asset is purchasable in the current experience. |
| `SaleLocation` | table | Dictionary table of information describing where the item can be sold, containing the following fields: |
|  | `SaleLocationType`: The type of sale location setting. See [ProductLocationRestriction](/docs/reference/engine/enums/ProductLocationRestriction.md) for the sale location setting ID numbers. |
|  | `UniverseIds`: Array table of universes in which the item can be sold (not currently implemented). |

#### Timed Options

| Key | Type | Description |
| --- | --- | --- |
| `TimedOptions` | array | Optional. An array of available timed options with durations and prices. Only present for assets that support timed ownership. Do not hardcode duration values; always retrieve them from this API as they may change. Each entry contains: |
|  | `Duration`: number — The duration in seconds (e.g. 259200 for 3 days, 604800 for 7 days). |
|  | `Price`: number — The price in Robux for this duration. |

#### Batching behavior

This method is **Transparent Batching capable**. If you spawn multiple
calls concurrently using `task.spawn`, the engine automatically combines
them into fewer HTTP requests behind the scenes. This is faster and helps
you avoid rate limits. See
[Transparent Batching](/docs/en-us/scripting/transparent-batching.md) for
details and a code example.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: AssetRead*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `assetId` | `int64` |  | The asset ID of the specified product. |
| `infoType` | `InfoType` | `Asset` | An [InfoType](/docs/reference/engine/enums/InfoType.md) enum value specifying the type of information being retrieved. |

**Returns:** `Dictionary` — A dictionary containing information about the queried item, described
in the previous tables.

**Getting Product Info**

The below example will print the name and description of the asset with an ID
of 125378389. In this case it will print: _"Mr. Fancy Top Hat :: So fancy that
even his top hat's top hat has a top hat."_

```lua
local MarketplaceService = game:GetService("MarketplaceService")

local ASSET_ID = 125378389

local asset = MarketplaceService:GetProductInfoAsync(ASSET_ID)
print(asset.Name .. " :: " .. asset.Description)
```

**Displaying Price Discounts**

The example below will print discount information for a game pass.

```lua
local MarketplaceService = game:GetService("MarketplaceService")

local PASS_ID = 12345678
local textLabel = script.Parent

local DiscountTypeDisplay = {
	RobloxPlusSubscription = "Roblox Plus Discount",
}

local productInfo = MarketplaceService:GetProductInfoAsync(PASS_ID, Enum.InfoType.GamePass)
print(string.format("Original Price: %d", productInfo.UserBasePriceInRobux))

for _, discount in ipairs(productInfo.PriceDiscountDetails) do
	local displayName = DiscountTypeDisplay[discount.Type] or "Other Discount"
	print(string.format("%s (%d%%): -%d", displayName, discount.Percent, discount.AmountInRobux))
end

print(string.format("You Pay: %d", productInfo.PriceInRobux))
```

**Displaying Available Timed Options**

The example below retrieves timed options for an asset and prints the
available durations with their prices.

```lua
local MarketplaceService = game:GetService("MarketplaceService")
local info = MarketplaceService:GetProductInfoAsync(105589844216517, Enum.InfoType.Asset)

if info.TimedOptions then
	for _, option in info.TimedOptions do
		local days = option.Duration / 86400
		print(string.format("%d days - %d Robux", days, option.Price))
	end
end
```

**Parallel GetProductInfoAsync with Transparent Batching**

Shows how to fetch product info for multiple assets concurrently using
[task](/docs/reference/engine/globals/RobloxGlobals.md). When you call
[GetProductInfoAsync](/docs/reference/engine/classes/MarketplaceService.md) multiple
times at roughly the same time, the engine automatically batches them into
fewer HTTP requests behind the scenes.

```lua
local MarketplaceService = game:GetService("MarketplaceService")

local productIds = {123456, 987654, 555777}
local results = {}
local remaining = #productIds

local function fetch(productId)
	local success, info = pcall(function()
		return MarketplaceService:GetProductInfoAsync(productId, Enum.InfoType.Product)
	end)

	if success then
		results[productId] = info
	else
		warn("Failed to get info for product:", productId, info)
	end

	remaining -= 1
end

-- Spawning all calls concurrently lets the engine batch them into
-- fewer HTTP requests automatically.
for _, productId in productIds do
	task.spawn(fetch, productId)
end

-- Wait for all requests to complete.
while remaining > 0 do
	task.wait()
end

-- All results are now available.
for productId, info in results do
	print(info.Name, "-", info.PriceInRobux, "Robux")
end
```

### Method: MarketplaceService:GetRobloxSubscriptionDetailsAsync

**Signature:** `MarketplaceService:GetRobloxSubscriptionDetailsAsync(user: Player): Dictionary`

This method is a streamlined endpoint to check for a single, platform-wide
Roblox subscription product. By providing `StartTime` (conditionally) and
`IsOriginExperience` to reward long-term loyalists without compromising
user data across the platform.

The returned dictionary contains the following fields:

| Field | Type | Description |
| --- | --- | --- |
| `IsSubscribed` | bool | Returns true if the user has an active Roblox Subscription membership. |
| `IsOriginExperience` | bool | Returns true if the user originally subscribed to Roblox Subscription while inside the current Experience (Universe). |
| `StartTime` | DateTime? | A [DateTime](/docs/reference/engine/datatypes/DateTime.md) object representing the time when the user’s subscription period first began. Note: For privacy reasons, this field is only returned if `IsOriginExperience` is true. If the user subscribed in a different experience or on the web, this field will be nil. |

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Monetization*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `user` | `Player` |  | The user regarding whom to check the subscription status. |

**Returns:** `Dictionary` — A dictionary containing subscription details such as `IsSubscribed`,
`IsOriginExperience`, and optionally `StartTime`.

**Check Roblox Subscription Details**

Checks if a player has an active Roblox subscription and performs actions
based on loyalty and attribution.

```lua
local MarketplaceService = game:GetService("MarketplaceService")
local Players = game:GetService("Players")

Players.PlayerAdded:Connect(function(player)
    local success, details = pcall(function()
        return MarketplaceService:GetRobloxSubscriptionDetailsAsync(player)
    end)

    if success and details.IsSubscribed then
        -- 1. Check for Loyalty (e.g., Subscribed for > 60 days)
        local threeMonths = 60 * 24 * 60 * 60
        if details.StartTime and (os.time() - details.StartTime.UnixTimestamp) > threeMonths then
            print("Awarding the '3-Month Subscription Veteran' skin!")
        end

        -- 2. Check for Attribution
        if details.IsOriginExperience then
            print("Attribution confirmed: User subscribed via this experience.")
        else
            print("User subscribed elsewhere (Website or another Experience).")
        end
    end
end)
```

### Method: MarketplaceService:GetSubscriptionProductInfoAsync

**Signature:** `MarketplaceService:GetSubscriptionProductInfoAsync(subscriptionId: string): Dictionary`

Returns the product information of a subscription for the given
`subscriptionId`. Because it returns a localized price, you can only call
this method from a [Script](/docs/reference/engine/classes/Script.md) with [RunContext.Client](/docs/reference/engine/enums/RunContext.md).

| Key | Type | Description |
| --- | --- | --- |
| `Name` | string | The name of the subscription product. |
| `Description` | string | The description of the subscription product. |
| `IconImageAssetId` | number | The asset ID of the subscription product icon. |
| `SubscriptionPeriod` | [SubscriptionPeriod](/docs/reference/engine/enums/SubscriptionPeriod.md) | The duration of the subscription (for example, `Month`, `Year`, etc.). |
| `DisplayPrice` | string | Localized price with the appropriate currency symbol for display (for example, `$4.99`). For users in unsupported countries, `DisplayPrice` returns a string without specific price information. |
| `DisplaySubscriptionPeriod` | string | Localized subscription period text for display (for example, `/month`). Can be used together with `DisplayPrice`. |
| `SubscriptionProviderName` | string | Name of the subscription benefit provider (for example, the name of the associated experience). |
| `IsForSale` | boolean | True if the subscription product is available for sale. |
| `PriceTier` | number | A number that can be used to compare the price of different subscription products. This is not the actual price of the subscription (for example, 499). |
| `PriceInRobux` | number | The equivalent cost of the subscription in Robux. Returns 0 if the subscription product is not available to be purchased in Robux. |

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: AssetRead*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `subscriptionId` | `string` |  | The ID of the subscription to check. |

**Returns:** `Dictionary` — A dictionary containing the subscription product information described
in the following table.

### Method: MarketplaceService:GetUsersPriceLevelsAsync

**Signature:** `MarketplaceService:GetUsersPriceLevelsAsync(userIds: Array): List<PriceLevelInfo>`

Returns the regionalized price levels of users, representing the
recommended price for an item in each user's regional market. For example,
a price level of 100 means that the suggested price for that user (based
on their region and purchasing power) is 100 Robux.

See
[Protect your trades and gifts](/docs/en-us/production/monetization/regional-pricing.md#protect-your-trades-and-gifts)
for more information.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Monetization*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `userIds` | `Array` |  | An array of user IDs. |

**Returns:** `List<PriceLevelInfo>` — Returns an array of `PriceLevelInfo` objects with a dictionary where
the keys are user IDs (strings) and their values are the corresponding
price levels (integers between 1 and 1000).

**Get price levels for a list of users**

The following example uses GetUsersPriceLevelsAsync to map each price level to
a user ID and retrieve price levels for a list of users.

```lua
-- Get the MarketplaceService
local MarketplaceService = game:GetService("MarketplaceService")

-- Define a function to retrieve price levels for a list of users
local function getPriceLevels(userIds)
    local success, result = pcall(function()
        return MarketplaceService:GetUsersPriceLevelsAsync(userIds)
    end)

    if success then
        -- Map each PriceLevelInfo to a UserId -> PriceLevel lookup table
        local lookup = {}
        for _, info in ipairs(result) do
            lookup[info.UserId] = info.PriceLevel
        end 
        return lookup
    else
        warn("Error getting price levels:", result)
        return nil
    end
end

-- Example using placeholder IDs
local user1Id = 123456789
local user2Id = 987654321

-- Call the function and store the result
local priceLevels = getPriceLevels({user1Id, user2Id})
-- If successful, print each user's level
if priceLevels then
    print("Price level for User 1:", priceLevels[user1Id])
    print("Price level for User 2:", priceLevels[user2Id])
else
    print("Failed to retrieve price levels.")
end
```

### Method: MarketplaceService:GetUserSubscriptionDetailsAsync

**Signature:** `MarketplaceService:GetUserSubscriptionDetailsAsync(user: Player, subscriptionId: string): Dictionary`

Returns a dictionary table containing the details of the user's
subscription for the given `subscriptionId`. The table contains the
following keys:

| Key | Type | Description |
| --- | --- | --- |
| `SubscriptionState` | [SubscriptionState](/docs/reference/engine/enums/SubscriptionState.md) | Current state of this particular subscription. |
| `NextRenewTime` | [DateTime](/docs/reference/engine/datatypes/DateTime.md) | Renewal time for this current subscription. May be in the past if the subscription is in [SubscribedRenewalPaymentPending](/docs/reference/engine/enums/SubscriptionState.md) state. This field is will be `nil` if the subscription will not renew, is [Expired](/docs/reference/engine/enums/SubscriptionState.md), or the user never subscribed. |
| `ExpireTime` | [DateTime](/docs/reference/engine/datatypes/DateTime.md) | When this subscription expires. This field will be `nil` if the subscription is not cancelled or the user never subscribed. |
| `ExpirationDetails` | [table](/docs/reference/engine/globals/table.md) | Table containing the details of the subscription expiration. This field will be `nil` if the subscription is not in the [Expired](/docs/reference/engine/enums/SubscriptionState.md) state. If populated, the table contains a `ExpirationReason` key of type [SubscriptionExpirationReason](/docs/reference/engine/enums/SubscriptionExpirationReason.md) describing why the subscription is expired. |

Note that this method can only be called from a [Script](/docs/reference/engine/classes/Script.md) with
[RunContext](/docs/reference/engine/classes/BaseScript.md) of
[Server](/docs/reference/engine/enums/RunContext.md). If you only need to determine the
`IsSubscribed` status of a user, it's recommended to use
[GetUserSubscriptionStatusAsync](/docs/reference/engine/classes/MarketplaceService.md)
as it is faster and more efficient for that particular purpose.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Monetization*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `user` | `Player` |  | The [Player](/docs/reference/engine/classes/Player.md) object whose subscription details you want to check. |
| `subscriptionId` | `string` |  | The ID of the subscription to check. |

**Returns:** `Dictionary` — A dictionary containing the user's subscription details described in
the following table.

### Method: MarketplaceService:GetUserSubscriptionPaymentHistoryAsync

**Signature:** `MarketplaceService:GetUserSubscriptionPaymentHistoryAsync(user: Player, subscriptionId: string): Array`

Returns an [Array](/docs/reference/engine/globals/table.md) that contains up to one year of the
user's subscription payment history for the given `subscriptionId`, sorted
from the most recent status to the least recent. You can only call this
method from a [Script](/docs/reference/engine/classes/Script.md) with [RunContext.Server](/docs/reference/engine/enums/RunContext.md).

Each entry in the payment history [Array](/docs/reference/engine/globals/table.md) contains the
following keys:

| Key | Type | Description |
| --- | --- | --- |
| `CycleStartTime` | [DateTime](/docs/reference/engine/datatypes/DateTime.md) | [DateTime](/docs/reference/engine/datatypes/DateTime.md) at the start of this particular subscription period. |
| `CycleEndTime` | [DateTime](/docs/reference/engine/datatypes/DateTime.md) | [DateTime](/docs/reference/engine/datatypes/DateTime.md) at the end of this particular subscription period. |
| `PaymentStatus` | [SubscriptionPaymentStatus](/docs/reference/engine/enums/SubscriptionPaymentStatus.md) | [SubscriptionPaymentStatus.Paid](/docs/reference/engine/enums/SubscriptionPaymentStatus.md) if the user paid for this particular subscription period. [SubscriptionPaymentStatus.Refunded](/docs/reference/engine/enums/SubscriptionPaymentStatus.md) if the user refunded this particular subscription period. |

#### Payment History Length

Only creators affiliated with the subscription product can access up to
**one year** worth of the user's subscription payment history.
Non-associated creators can only get the user's **current** subscription
payment status or an empty [Array](/docs/reference/engine/globals/table.md) if the user has no active
subscription.

#### Grace Period

Subscription renewal payments can have some processing time. Payment
history doesn't return a table for this period. However, in order to
preserve a user's subscription experience during the processing period,
[GetUserSubscriptionStatusAsync](/docs/reference/engine/classes/MarketplaceService.md)
returns `IsSubscribed: true` for the given user. Don't grant durable items
or currency type subscription benefits to the user until after payment has
been confirmed for the current cycle.

For example, on August 31, 2023, User A's Subscription B is up for
renewal. On September 1, 2023, the payment has yet to be processed. If you
call
[GetUserSubscriptionPaymentHistoryAsync](/docs/reference/engine/classes/MarketplaceService.md)
on September 1, 2023 on User A for Subscription B, the first entry of the
return value is:

| Key | Value |
| --- | --- |
| `CycleStartTime` | ... |
| `CycleEndTime` | August 31, 2023 |
| `PaymentStatus` | [SubscriptionPaymentStatus.Paid](/docs/reference/engine/enums/SubscriptionPaymentStatus.md) |

Note that since the user is within the grace period, the cycle they have
yet to pay for (September 1, 2023) does not appear in the return value at
all. This field only populates after the payment has been received and
processed.

At the same time,
[GetUserSubscriptionStatusAsync](/docs/reference/engine/classes/MarketplaceService.md)
returns the following result until the renewal payment process fails or
the user cancels:

| Key | Return |
| --- | --- |
| `IsSubscribed` | True |
| `IsRenewing` | True |

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Monetization*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `user` | `Player` |  | The [Player](/docs/reference/engine/classes/Player.md) whose subscription payment history you want to retrieve. |
| `subscriptionId` | `string` |  | The ID of the subscription whose payment history you want to retrieve. |

**Returns:** `Array` — An array of payment-history entries, ordered from most recent to least
recent, as described in the following table.

**MarketplaceService:GetUserSubscriptionPaymentHistoryAsync**

This code sample demonstrates how to check the last 12 months of a user's
payment history for a given subscription ID. Rather than the raw values, it
prints formatted values for easier readability. Roblox Studio includes several
subscription IDs for testing purposes:

- `EXP-0` represents an active and renewing subscription.
- `EXP-1` represents a returning subscription.
- `EXP-2` represents a refunded subscription. Depending on your subscription
  benefits, refunds can require special handling, so testing for this case is
  particularly useful.
- `EXP-3` represents an active subscription that is pending successful payment
  for the current cycle. Continued failure to pay results in automatic
  cancellation of the subscription.

```lua
local MarketplaceService = game:GetService("MarketplaceService")
local Players = game:GetService("Players")

local SUBSCRIPTION_ID = "EXP-0"

local function checkSubscriptionHistory(player: Player)
	local subscriptionHistory = {}

	local success, err = pcall(function()
		subscriptionHistory = MarketplaceService:GetUserSubscriptionPaymentHistoryAsync(player, SUBSCRIPTION_ID)
	end)

	if not success then
		warn(`Error while checking subscription history: {err}`)
		return
	end

	if next(subscriptionHistory) then
		-- User has some subscription history within the past 12 months.
		-- Print the details of each payment entry from the subscription history.
		print(`Player {player.Name} has subscribed to {SUBSCRIPTION_ID} before:`)

		for entryNum, paymentEntry in subscriptionHistory do
			local paymentStatus = tostring(paymentEntry.PaymentStatus)
			local cycleStartTime = paymentEntry.CycleStartTime:FormatLocalTime("LLL", "en-us")
			local cycleEndTime = paymentEntry.CycleEndTime:FormatLocalTime("LLL", "en-us")
			print(`{entryNum}: {paymentStatus} ({cycleStartTime} - {cycleEndTime})`)
		end
	else
		print(`Player {player.Name} has never subscribed to {SUBSCRIPTION_ID} before.`)
	end
end

-- Call checkSubscriptionHistory for any players already in the game
for _, player in ipairs(Players:GetPlayers()) do
	checkSubscriptionHistory(player)
end

-- Call checkSubscriptionHistory for all future players
Players.PlayerAdded:Connect(checkSubscriptionHistory)
```

### Method: MarketplaceService:GetUserSubscriptionStatusAsync

**Signature:** `MarketplaceService:GetUserSubscriptionStatusAsync(user: Player, subscriptionId: string): Dictionary`

Returns a [table](/docs/reference/engine/globals/table.md) that contains the subscription status of the
user for the given `subscriptionId`. The table contains the following
keys:

| Key | Type | Description |
| --- | --- | --- |
| `IsSubscribed` | boolean | True if the user's subscription is active. |
| `IsRenewing` | boolean | True if the user is set to renew this subscription after the current subscription period ends. |

Note that `IsSubscribed` will be `true` only when a user has purchased the
subscription and the payment has been successfully processed. If the
payment for a user's initial subscription purchase is still processing or
has failed, `IsSubscribed` returns `false`. To understand when a user's
subscription status has changed, see the
[Players.UserSubscriptionStatusChanged](/docs/reference/engine/classes/Players.md) event.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Monetization*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `user` | `Player` |  | The [Player](/docs/reference/engine/classes/Player.md) object whose subscription status you want to check. |
| `subscriptionId` | `string` |  | The ID of the subscription to check for. |

**Returns:** `Dictionary` — A dictionary containing the user's subscription status described in
the following table.

**Check User Subscription Status**

This code sample demonstrates how to check the subscription status of a user
for a certain subscription. As a user enters the game, their account is
checked for the status of that subscription and a message is printed.

Notice how the call to GetUserSubscriptionStatusAsync is wrapped in `pcall` -
this prevents the code from throwing an error in case the user's subscription
status can't be checked for some reason. Should such an error occur, the
`success` variable would be false.

```lua
local MarketplaceService = game:GetService("MarketplaceService")
local Players = game:GetService("Players")

local subscriptionID = "EXP-00000"

local function checkSubStatus(player)
	local subStatus = {}
	local success, message = pcall(function()
		-- returns IsRenewing and IsSubscribed
		subStatus = MarketplaceService:GetUserSubscriptionStatusAsync(player, subscriptionID)
	end)

	if not success then
		warn("Error while checking if player has subscription: " .. tostring(message))
		return
	end

	if subStatus["IsSubscribed"] then
		print(player.Name .. " is subscribed with " .. subscriptionID)
		-- Give player permissions associated with the subscription
	end
end

Players.PlayerAdded:Connect(checkSubStatus)
```

### Method: MarketplaceService:OpenShop

**Signature:** `MarketplaceService:OpenShop(player: Player): ()`

Opens an [in-game Shop](/docs/en-us/production/monetization/shop.md) as an
overlay window for the given [Player](/docs/reference/engine/classes/Player.md). Shop displays a personalized
list of the experience's
[passes](/docs/en-us/production/monetization/passes.md) and
[developer products](/docs/en-us/production/monetization/developer-products.md)
ranked for the user.

A default Shop is generated automatically for every game and requires no
additional developer setup. You can customize which items appear in the
shop from Creator Hub.

This method can be called from either a server [Script](/docs/reference/engine/classes/Script.md) or a
[LocalScript](/docs/reference/engine/classes/LocalScript.md). When called from a [LocalScript](/docs/reference/engine/classes/LocalScript.md), `player` must
match the local player.

You can call this method in response to any user action, such as a button
click, the player reaching a specific location, or joining the experience.

*Security: None · Thread Safety: Unsafe · Capabilities: PromptExternalPurchase*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `player` | `Player` |  | The [Player](/docs/reference/engine/classes/Player.md) for whom to open the shop. If called from a [LocalScript](/docs/reference/engine/classes/LocalScript.md), this must be the local player. |

**Returns:** `()`

**Open In-Game Shop
description: This code sample demonstrates how to open the in-game shop
for the local player. The shop displays a personalized list of the game's
passes and developer products.**

```lua
local MarketplaceService = game:GetService("MarketplaceService")
local Players = game:GetService("Players")

local player = Players.LocalPlayer

MarketplaceService:OpenShop(player)
```

### Method: MarketplaceService:PlayerOwnsAssetAsync

**Signature:** `MarketplaceService:PlayerOwnsAssetAsync(player: Instance, assetId: int64): boolean`

Returns whether the inventory of a specific user contains an asset, based
on the asset ID. This method throws an error if the query fails, so you
should wrap calls to this method in `pcall()`.

- This method should **not** be used for
  [passes](/docs/en-us/production/monetization/passes.md) since they use a
  separate ID system. Legacy passes that still depend on an asset ID
  should use
  [UserOwnsGamePassAsync()](/docs/reference/engine/classes/MarketplaceService.md)
  instead of this method.
- This method cannot be used to check for
  [developer products](/docs/en-us/production/monetization/developer-products.md)
  since they can be purchased multiple times but not owned themselves.
  Instead, use a [data store](/docs/en-us/cloud-services/data-stores.md) to save
  when a user buys a developer product.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: AssetRead*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `player` | `Instance` |  | The [Player](/docs/reference/engine/classes/Player.md) whose inventory is tested for ownership of the given asset. |
| `assetId` | `int64` |  | The asset ID for which the given player's inventory is tested. |

**Returns:** `boolean` — Indicates whether the given player's inventory contains the given
asset.

**Check for Item Ownership**

This code sample demonstrates how to check if a player owns a certain item.
Here, we're checking for the item
[Midnight Shades](https://www.roblox.com/catalog/30331986/Midnight-Shades), a
hat that costs R$ 250. As a player enters the game, their account is checked
for the ownership of that item and a message is printed.

Notice how the call to PlayerOwnsAssetAsync is wrapped in `pcall` - this
prevents the code from throwing an error in case the player's inventory can't
be checked for some reason. Should such an error occur, the `success` variable
would be false.

```lua
local Players = game:GetService("Players")
local MarketplaceService = game:GetService("MarketplaceService")

-- The item we're checking for: https://www.roblox.com/catalog/30331986/Midnight-Shades
local ASSET_ID = 30331986
local ASSET_NAME = "Midnight Shades"

local function onPlayerAdded(player)
	local success, doesPlayerOwnAsset =
		pcall(MarketplaceService.PlayerOwnsAssetAsync, MarketplaceService, player, ASSET_ID)
	if not success then
		local errorMessage = doesPlayerOwnAsset
		warn(`Error checking if {player.Name} owns {ASSET_NAME}: {errorMessage}`)
		return
	end

	if doesPlayerOwnAsset then
		print(`{player.Name} owns {ASSET_NAME}`)
	else
		print(`{player.Name} doesn't own {ASSET_NAME}`)
	end
end

Players.PlayerAdded:Connect(onPlayerAdded)
```

**Expected output:** Player owns Midnight Shades

### Method: MarketplaceService:PlayerOwnsBundleAsync

**Signature:** `MarketplaceService:PlayerOwnsBundleAsync(player: Player, bundleId: int64): boolean`

Returns whether the inventory of a specific user contains a bundle, based
on the bundle ID. This method throws an error if the query fails, so you
should wrap calls to this method in `pcall()`.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: AssetRead*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `player` | `Player` |  | The [Player](/docs/reference/engine/classes/Player.md) whose inventory is tested for ownership of the given bundle. |
| `bundleId` | `int64` |  | The bundle ID for which the given player's inventory is tested. |

**Returns:** `boolean` — Indicates whether the given player's inventory contains the given
bundle.

**Check for Bundle Ownership**

This code sample demonstrates how to check if a player owns a certain bundle.
Here, we're checking for the bundle
[Junkbot](https://www.roblox.com/bundles/589/Junkbot). As a player enters the
game, their account is checked for the ownership of that item and a message is
printed.

Notice that a `pcall()` wraps the call to
`MarketplaceService:PlayerOwnsBundleAsync()` to prevent the code from throwing
an error in case the player's inventory can't be checked. If such an error
occurs, the `success` variable is false.

```lua
local Players = game:GetService("Players")
local MarketplaceService = game:GetService("MarketplaceService")

-- The bundle we're checking for: https://www.roblox.com/bundles/589/Junkbot
local BUNDLE_ID = 589
local BUNDLE_NAME = "Junkbot"

Players.PlayerAdded:Connect(function(player)
	local success, doesPlayerOwnBundle = pcall(function()
		return MarketplaceService:PlayerOwnsBundleAsync(player, BUNDLE_ID)
	end)

	if success == false then
		print("PlayerOwnsBundleAsync call failed: ", doesPlayerOwnBundle)
		return
	end

	if doesPlayerOwnBundle then
		print(player.Name .. " owns " .. BUNDLE_NAME)
	else
		print(player.Name .. " doesn't own " .. BUNDLE_NAME)
	end
end)
```

**Expected output:** Player owns Junkbot

### Method: MarketplaceService:PromptBulkPurchase

**Signature:** `MarketplaceService:PromptBulkPurchase(player: Player, lineItems: Array, options: Dictionary): ()`

Prompts a user to purchase multiple avatar items with the given `assetId`
or `bundleId`. Does not work with non-avatar items.

`PromptBulkPurchase` only allows prompting from server scripts.

For limited items, original copies are prompted until they run out,
regardless of the price. Once original copies are out, resale copies are
prompted.

A maximum of 20 items can be added to a single bulk purchase prompt.

#### PurchaseOptions

Each line item can optionally include a `PurchaseOptions` array to control
which purchase option appears in the prompt. If omitted, the user is
prompted for a permanent purchase only (default behavior).

`PurchaseOptions` currently supports only one entry. If more than one
option is provided, the API throws an error.

Each entry in `PurchaseOptions` contains:

| Key | Type | Description |
| --- | --- | --- |
| `Type` | Enum | [PurchaseOption.TimedOption](/docs/reference/engine/enums/PurchaseOption.md) for a timed option, or [PurchaseOption.Permanent](/docs/reference/engine/enums/PurchaseOption.md) for standard purchase. |
| `Value` | number | Required for `TimedOption`. The duration in seconds. |

**Do not hardcode duration values.** Available durations and prices are
determined by the backend and may change at any time. Always retrieve them
from one of the following APIs and pass the values through to
`PurchaseOptions`:

- [MarketplaceService:GetProductInfoAsync()](/docs/reference/engine/classes/MarketplaceService.md)
- [AvatarEditorService:GetItemDetailsAsync()](/docs/reference/engine/classes/AvatarEditorService.md)
- [AvatarEditorService:GetBatchItemDetailsAsync()](/docs/reference/engine/classes/AvatarEditorService.md)
- [AvatarEditorService:SearchCatalogAsync()](/docs/reference/engine/classes/AvatarEditorService.md)

*Security: None · Thread Safety: Unsafe · Capabilities: PromptExternalPurchase*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `player` | `Player` |  | The user to prompt to purchase items. |
| `lineItems` | `Array` |  | An array of avatar items to be included in the bulk purchase.  Each line item contains the following structure:  ```lua {   Type: MarketplaceProductType,   Id: string,   PurchaseOptions: { {Type: PurchaseOption, Value: number?} }? } ```  Each line item contains the following pairs:  - `Type`: The corresponding [MarketplaceProductType](/docs/reference/engine/enums/MarketplaceProductType.md) (Enum). - `Id`: The ID of the asset or bundle. - `PurchaseOptions`: Optional. An array containing a single purchase   option to display in the prompt. If omitted, the permanent purchase   is prompted. See the PurchaseOptions section below for details. |
| `options` | `Dictionary` |  | Not available at this time. |

**Returns:** `()`

**Prompt Bulk Purchase Client**

The following sample prompts players to buy "Beautiful Hair for Beautiful
People" and "Blue Collar Cat" when they join the experience.

Place this LocalScript somewhere on the client such as within Players ->
StarterPlayerScripts so that it will be able to fire a remote event signal
from a client to the server.

```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local promptBulkPurchaseEvent = ReplicatedStorage:WaitForChild("PromptBulkPurchaseEvent")

local part = Instance.new("Part")
part.Parent = workspace

local clickDetector = Instance.new("ClickDetector")
clickDetector.Parent = part

clickDetector.MouseClick:Connect(function()
	promptBulkPurchaseEvent:FireServer({
		{ Type = Enum.MarketplaceProductType.AvatarAsset, Id = "16630147" },
		{ Type = Enum.MarketplaceProductType.AvatarBundle, Id = "182" },
	})
end)
```

**Prompt Bulk Purchase Server**

The following code is listening for a [RemoteEvent.OnServerEvent](/docs/reference/engine/classes/RemoteEvent.md) to
fire to the Server from a Client. Place this script somewhere on the server
such as within `ServerStorage`.

```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")
local MarketplaceService = game:GetService("MarketplaceService")

local promptBulkPurchaseEvent = Instance.new("RemoteEvent")
promptBulkPurchaseEvent.Name = "PromptBulkPurchaseEvent"
promptBulkPurchaseEvent.Parent = ReplicatedStorage

--Listen for the RemoteEvent to fire from a Client and then trigger the bulk purchase prompt
promptBulkPurchaseEvent.OnServerEvent:Connect(function(player, items)
	MarketplaceService:PromptBulkPurchase(player, items, {})
end)
```

**Prompting Timed Option Purchase**

The example below retrieves available timed options, picks the shortest
duration, and prompts the player to purchase it.

```lua
local MarketplaceService = game:GetService("MarketplaceService")
local Players = game:GetService("Players")

local ASSET_ID = 105589844216517

Players.PlayerAdded:Connect(function(player)
	local info = MarketplaceService:GetProductInfoAsync(ASSET_ID, Enum.InfoType.Asset)

	if info.TimedOptions and #info.TimedOptions > 0 then
		-- Find the shortest duration option
		local shortest = info.TimedOptions[1]
		for _, option in info.TimedOptions do
			if option.Duration < shortest.Duration then
				shortest = option
			end
		end

		local items = {
			{
				Type = Enum.MarketplaceProductType.AvatarAsset,
				Id = tostring(ASSET_ID),
				PurchaseOptions = {
					{ Type = Enum.PurchaseOption.TimedOption, Value = shortest.Duration },
				},
			}
		}
		MarketplaceService:PromptBulkPurchase(player, items, {})
	end
end)
```

### Method: MarketplaceService:PromptBundlePurchase

**Signature:** `MarketplaceService:PromptBundlePurchase(player: Instance, bundleId: int64): ()`

Prompts a user to purchase a bundle with the given `bundleId`.

*Security: None · Thread Safety: Unsafe · Capabilities: PromptExternalPurchase*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `player` | `Instance` |  | The [Player](/docs/reference/engine/classes/Player.md) to prompt. |
| `bundleId` | `int64` |  | The ID of the bundle to purchase. |

**Returns:** `()`

### Method: MarketplaceService:PromptCancelSubscription

**Signature:** `MarketplaceService:PromptCancelSubscription(user: Player, subscriptionId: string): ()`

Prompts a user to cancel a subscription for the given `subscriptionId`.
Once the user successfully cancels the subscription, the
[Players.UserSubscriptionStatusChanged](/docs/reference/engine/classes/Players.md) event fires.

*Security: None · Thread Safety: Unsafe · Capabilities: PromptExternalPurchase*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `user` | `Player` |  | The [Player](/docs/reference/engine/classes/Player.md) to prompt. |
| `subscriptionId` | `string` |  | The ID of the subscription to cancel. |

**Returns:** `()`

### Method: MarketplaceService:PromptGamePassPurchase

**Signature:** `MarketplaceService:PromptGamePassPurchase(player: Instance, gamePassId: int64): ()`

Prompts a user to purchase a
[pass](/docs/en-us/production/monetization/passes.md) with the given
`gamePassId`.

You can only prompt purchases of passes that belong to the current game.
Purchases of passes from other games fail, even if you own both games.

In Studio, mocked purchases don't check that the pass belongs to the
current game, so prompting a pass purchase from another game might appear
to succeed. Before you publish, verify that the `gamePassId` belongs to
the current game.

*Security: None · Thread Safety: Unsafe · Capabilities: PromptExternalPurchase*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `player` | `Instance` |  | The [Player](/docs/reference/engine/classes/Player.md) to prompt. |
| `gamePassId` | `int64` |  | The pass ID to purchase. This is the `TargetId` returned by [GetProductInfo()](/docs/reference/engine/classes/MarketplaceService.md) when [InfoType](/docs/reference/engine/enums/InfoType.md) is `GamePass`. It is not the pass's asset ID and not its `ProductId`. |

**Returns:** `()`

### Method: MarketplaceService:PromptProductPurchase

**Signature:** `MarketplaceService:PromptProductPurchase(player: Instance, productId: int64, equipIfPurchased?: boolean, currencyType?: CurrencyType): ()`

Prompts a user to purchase a
[developer product](/docs/en-us/production/monetization/developer-products.md)
with the given `productId`.

You can only prompt purchases of developer products that belong to the
current game. Purchases of developer products from other games fail, even
if you own both games.

In Studio, mocked purchases don't check that the product belongs to the
current game, so prompting a product purchase from another game might
appear to succeed. Before you publish, verify that the `productId` belongs
to the current game.

*Security: None · Thread Safety: Unsafe · Capabilities: PromptExternalPurchase*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `player` | `Instance` |  | The [Player](/docs/reference/engine/classes/Player.md) to prompt. |
| `productId` | `int64` |  | The ID of the developer product to purchase. |
| `equipIfPurchased` | `boolean` | `true` | Ignored. |
| `currencyType` | `CurrencyType` | `Default` | Ignored. |

**Returns:** `()`

**MarketplaceService:PromptProductPurchase**

The following example illustrates how to prompt purchase of a
[developer product](/docs/en-us/production/monetization/developer-products.md) with the
[PromptProductPurchase()](/docs/reference/engine/classes/MarketplaceService.md)
method. Depending on the needs of your experience, you can call the
`promptPurchase()` function in situations such as when the player presses a
[button](/docs/en-us/ui/buttons.md) or when their character talks to a vendor
NPC.

```lua
local MarketplaceService = game:GetService("MarketplaceService")
local Players = game:GetService("Players")

local player = Players.LocalPlayer

local productId = 0000000 -- Change this to your developer product ID

-- Function to prompt purchase of the developer product
local function promptPurchase()
	MarketplaceService:PromptProductPurchase(player, productId)
end

promptPurchase()
```

### Method: MarketplaceService:PromptPurchase

**Signature:** `MarketplaceService:PromptPurchase(player: Instance, assetId: int64, equipIfPurchased?: boolean, currencyType?: CurrencyType): ()`

Prompts a user to purchase an item with the given `assetId`.

- This does not work for
  [USD Creator Store](/docs/en-us/production/creator-store.md) purchases.
- If the item has the
  [Sale Location](/docs/en-us/marketplace/publish-to-marketplace.md#sale-location)
  set as `Experience By Place ID (API Only)`, you must call
  [MarketplaceService:PromptPurchase](/docs/reference/engine/classes/MarketplaceService.md) from a server script.
- If prompting a purchase of a
  [limited](/docs/en-us/marketplace/marketplace-fees-and-commissions.md#limiteds)
  item:
  - (Recommended) Server requests prompt original copies until they run
    out, regardless of the price. Once original copies run out, resale
    copies are prompted.
  - Client requests prompt from the lowest resale price even if original
    copies are available.

*Security: None · Thread Safety: Unsafe · Capabilities: PromptExternalPurchase*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `player` | `Instance` |  | The [Player](/docs/reference/engine/classes/Player.md) to prompt. |
| `assetId` | `int64` |  | The ID of the asset to purchase. |
| `equipIfPurchased` | `boolean` | `true` | Ignored. |
| `currencyType` | `CurrencyType` | `Default` | Ignored. |

**Returns:** `()`

**LocalScript (Client)**

The below example would prompt all new players to buy Beautiful Hair for
Beautiful People when they click on a part.

Place this LocalScript somewhere on the Client such as within Players ->
StarterPlayerScripts so that it will be able to fire a
[RemoteEvent:FireServer()](/docs/reference/engine/classes/RemoteEvent.md) signal from a Client to the Server.

```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local promptPurchaseEvent = ReplicatedStorage:WaitForChild("PromptPurchaseEvent")

local part = Instance.new("Part")
part.Parent = workspace

local clickDetector = Instance.new("ClickDetector")
clickDetector.Parent = part

clickDetector.MouseClick:Connect(function()
	promptPurchaseEvent:FireServer(16630147)
end)
```

**Script (Server)**

Since the below code is listening for a [RemoteEvent.OnServerEvent](/docs/reference/engine/classes/RemoteEvent.md) to
fire to the Server from a Client. Place this script somewhere on the Server
such as within ServerStorage.

```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")
local MarketplaceService = game:GetService("MarketplaceService")

local promptPurchaseEvent = Instance.new("RemoteEvent")
promptPurchaseEvent.Name = "PromptPurchaseEvent"
promptPurchaseEvent.Parent = ReplicatedStorage

-- Listen for the RemoteEvent to fire from a Client and then trigger the purchase prompt
promptPurchaseEvent.OnServerEvent:Connect(function(player, id)
	MarketplaceService:PromptPurchase(player, id)
end)
```

### Method: MarketplaceService:PromptRobloxSubscriptionPurchase

**Signature:** `MarketplaceService:PromptRobloxSubscriptionPurchase(user: Player): ()`

Prompts a user to purchase a Roblox Plus subscription. When the user
successfully subscribes, any experience-defined rewards for the upsell are
granted automatically through the engine API.

#### See Also

- [MarketplaceService.PromptRobloxSubscriptionPurchaseFinished](/docs/reference/engine/classes/MarketplaceService.md)
  which fires when the Roblox Plus purchase UI closes.
- [Player.HasRobloxSubscription](/docs/reference/engine/classes/Player.md) which can be observed via
  [Instance:GetPropertyChangedSignal()](/docs/reference/engine/classes/Instance.md) to detect when a user's
  subscription status changes.

*Security: None · Thread Safety: Unsafe · Capabilities: PromptExternalPurchase*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `user` | `Player` |  | The [Player](/docs/reference/engine/classes/Player.md) to be prompted to purchase Roblox Plus. |

**Returns:** `()`

**Prompt Roblox Plus Subscription Purchase**

The following code prompts users to subscribe to Roblox Plus when their
character touches the part that the [Script](/docs/reference/engine/classes/Script.md) is attached to. Users who
already have an active subscription are immediately granted the reward and
teleported to an exclusive area.

```lua
local MarketplaceService = game:GetService("MarketplaceService")
local Players = game:GetService("Players")

local teleporter = script.Parent
local showModal = true

local EXCLUSIVE_AREA_POSITION = Vector3.new(1200, 200, 60)

-- Grant the reward and teleport the subscribing player to the exclusive area
local function grantRewardAndTeleport(player)
	player:RequestStreamAroundAsync(EXCLUSIVE_AREA_POSITION)

	local character = player.Character
	if character and character.Parent then
		local currentPivot = character:GetPivot()
		character:PivotTo(currentPivot * CFrame.new(EXCLUSIVE_AREA_POSITION))
	end
end

-- Detect character parts touching the teleporter
teleporter.Touched:Connect(function(otherPart)
	local player = Players:GetPlayerFromCharacter(otherPart.Parent)
	if not player then
		return
	end

	if not player:GetAttribute("CharacterPartsTouching") then
		player:SetAttribute("CharacterPartsTouching", 0)
	end
	player:SetAttribute("CharacterPartsTouching", player:GetAttribute("CharacterPartsTouching") + 1)

	if player.HasRobloxSubscription then
		-- Player already has Roblox Plus; grant reward immediately
		grantRewardAndTeleport(player)
	else
		-- Prompt Roblox Plus subscription, debounced to once every few seconds
		if not showModal then
			return
		end
		showModal = false
		task.delay(5, function()
			showModal = true
		end)
		MarketplaceService:PromptRobloxSubscriptionPurchase(player)
	end
end)

-- Detect character parts exiting the teleporter
teleporter.TouchEnded:Connect(function(otherPart)
	local player = Players:GetPlayerFromCharacter(otherPart.Parent)
	if player and player:GetAttribute("CharacterPartsTouching") then
		player:SetAttribute("CharacterPartsTouching", player:GetAttribute("CharacterPartsTouching") - 1)
	end
end)

-- Grant reward when the server confirms a subscription change
-- Connect HasRobloxSubscription change for each player
Players.PlayerAdded:Connect(function(player)
	player:GetPropertyChangedSignal("HasRobloxSubscription"):Connect(function()
		if player.HasRobloxSubscription
			and player:GetAttribute("CharacterPartsTouching")
			and player:GetAttribute("CharacterPartsTouching") > 0
		then
			grantRewardAndTeleport(player)
		end
	end)
end)
```

### Method: MarketplaceService:PromptRobuxTransferAsync

**Signature:** `MarketplaceService:PromptRobuxTransferAsync(sender: Player, receiverUserId: int64, amount: int64): string`

`PromptRobuxTransferAsync` initiates a Robux transfer from the `sender` to
the user specified by `receiverUserId`. This is a server-only method and
must be called from a [Script](/docs/reference/engine/classes/Script.md) with `RunContext` set to `Server`.

After a successful transfer, both the sender and receiver will have
receipts delivered to their respective
[BindReceiptHandler](/docs/reference/engine/classes/MarketplaceService.md)
callbacks:

- The sender's receipt has [ReceiptType.RobuxTransferSender](/docs/reference/engine/enums/ReceiptType.md).
- The receiver's receipt has [ReceiptType.RobuxTransferReceiver](/docs/reference/engine/enums/ReceiptType.md).

Both receipts include a `TransferRequestId` field matching the
`transferRequestId` returned by this method, which you can use for logging
or to correlate sender and receiver receipts.

#### Receipt Timing

Both receipts are delivered to whichever server the corresponding user is
currently in once the transfer settles (neither side needs to rejoin). If
a transfer is gated on receiver approval, for example parental consent for
the receiver's account, it does not settle until approval lands; receipts
are delivered after that point.

- **Receiver receipt** is delivered to the server the receiver is
  currently in once the transfer settles, or on their next session join if
  they are offline.
- **Sender receipt** is delivered immediately if the transfer settles
  synchronously. If approval is required, it is delivered to the server
  the sender is currently in once the receiver accepts, or on the sender's
  next session join if they are offline.

#### Errors

This method throws an error if:

- The `sender` is not a valid [Player](/docs/reference/engine/classes/Player.md) instance.
- `receiverUserId` is not a positive integer.
- `amount` is not a positive integer.
- The method is called from the client instead of the server.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: PromptExternalPurchase*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `sender` | `Player` |  | The [Player](/docs/reference/engine/classes/Player.md) initiating the transfer. Must be a valid player currently in the server. |
| `receiverUserId` | `int64` |  | The [UserId](/docs/reference/engine/classes/Player.md) of the user who will receive the Robux. |
| `amount` | `int64` |  | The amount of Robux to transfer. Must be a positive integer. |

**Returns:** `string` — A string `transferRequestId` that uniquely identifies this transfer
request. Use this ID to correlate with receipts delivered through
[BindReceiptHandler](/docs/reference/engine/classes/MarketplaceService.md).

**MarketplaceService:PromptRobuxTransferAsync**

The following server-side [Script](/docs/reference/engine/classes/Script.md) example shows how to use
[MarketplaceService:PromptRobuxTransferAsync()](/docs/reference/engine/classes/MarketplaceService.md) to initiate a Robux
transfer between two players. The method returns a `transferRequestId` that
uniquely identifies the transfer and can be used to correlate with receipts.

```lua
local MarketplaceService = game:GetService("MarketplaceService")
local Players = game:GetService("Players")

-- Example: transfer Robux when a player triggers a RemoteEvent
local transferEvent = game.ReplicatedStorage:WaitForChild("RequestTransfer")

transferEvent.OnServerEvent:Connect(function(sender, receiverUserId, amount)
	-- Validate inputs
	if not sender or not sender:IsA("Player") then
		return
	end

	if typeof(receiverUserId) ~= "number" or receiverUserId <= 0 then
		warn("Invalid receiverUserId")
		return
	end

	if typeof(amount) ~= "number" or amount <= 0 then
		warn("Invalid amount")
		return
	end

	local success, result = pcall(function()
		return MarketplaceService:PromptRobuxTransferAsync(sender, receiverUserId, amount)
	end)

	if success then
		print(`Transfer initiated with TransferRequestId: {result}`)
	else
		warn(`Transfer failed: {result}`)
	end
end)
```

### Method: MarketplaceService:PromptSubscriptionPurchase

**Signature:** `MarketplaceService:PromptSubscriptionPurchase(user: Player, subscriptionId: string): ()`

Prompts a user to purchase a subscription for the given `subscriptionId`.

*Security: None · Thread Safety: Unsafe · Capabilities: PromptExternalPurchase*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `user` | `Player` |  | The [Player](/docs/reference/engine/classes/Player.md) object to be prompted to subscribe. |
| `subscriptionId` | `string` |  | The ID of the subscription to subscribe to. |

**Returns:** `()`

### Method: MarketplaceService:RankProductsAsync

**Signature:** `MarketplaceService:RankProductsAsync(productIdentifiers: Array): List<RankedItem>`

Takes a list of product IDs and returns a personalized ordered list of
those products.

This API has a client-side throttling limit of 10 requests per minute. If
you exceed this limit, wait 60 seconds and make the request again.

*Yields · Security: None · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `productIdentifiers` | `Array` |  | An array of objects identifying the products you want to rank. This array can include up to 50 items.  Each `ProductIdentifier` has:  - [InfoType](/docs/reference/engine/enums/InfoType.md): Enum.InfoType   - Must be either [InfoType.GamePass](/docs/reference/engine/enums/InfoType.md) or     [InfoType.Product](/docs/reference/engine/enums/InfoType.md). - `Id`: number   - The ID of the game pass or developer product.  ```lua local ProductIdentifier = { 	InfoType = Enum.InfoType.GamePass, 	Id = 123456 } ``` |

**Returns:** `List<RankedItem>` — The array of ranked items in a personalized order for the current
user.

Each array has:

- `ProductIdentifier`: The corresponding ID from the input array.
- `ProductInfo`: The standard product info dictionary returned by
  [GetProductInfoAsync](/docs/reference/engine/classes/MarketplaceService.md).

**Get a list of ranked products based on the provided product IDs**

This sample takes a list of product IDs and returns a ranked list of those
products.

```lua
-- Get the MarketplaceService
  local MarketplaceService = game:GetService("MarketplaceService")

-- Create the array of products you want to rank
local productIdentifiers = {
    {InfoType = Enum.InfoType.GamePass, Id = 123},
    {InfoType = Enum.InfoType.Product, Id = 456},
    {InfoType = Enum.InfoType.Product, Id = 789}
}

-- Call in a protected call to handle errors gracefully
local success, rankedProducts = pcall(function()
    return MarketplaceService:RankProductsAsync(productIdentifiers)
end)

if not success then
    error("Failed to rank products")
end

-- Load the returned items into the store.
for i, rankedItem in ipairs(rankedProducts) do
    local productIdentifier = rankedItem.ProductIdentifier
    local productInfo = rankedItem.ProductInfo
    -- ...
    -- Logic to add products into store
end
```

### Method: MarketplaceService:RecommendTopProductsAsync

**Signature:** `MarketplaceService:RecommendTopProductsAsync(infoTypes: Array): List<RankedItem>`

Takes an array of [InfoType](/docs/reference/engine/enums/InfoType.md) and returns up to 50 items representing
the products a user is most likely to engage with and purchase. If no
recommendations can be determined, the method returns an empty list.

This API has a client-side throttling limit of 5 requests per minute. If
you exceed this limit, wait 60 seconds and make the request again.

*Yields · Security: None · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `infoTypes` | `Array` |  | An array of [InfoType](/docs/reference/engine/enums/InfoType.md) values specifying the types of product to retrieve recommendations for.  Supported `InfoTypes`: [InfoType.GamePass](/docs/reference/engine/enums/InfoType.md), [InfoType.Product](/docs/reference/engine/enums/InfoType.md).  ```lua local infoTypes = { 	Enum.InfoType.GamePass, 	Enum.InfoType.Product } ``` |

**Returns:** `List<RankedItem>` — A ranked list of up to 50 items the user is most likely to engage
with, based on the provided `InfoTypes`. If no recommendations can be
determined, the method returns an empty list.

**Get a ranked list of the top products for in your in-experience store**

This sample returns a ranked list of the top products for a user in your
in-experience store.

```lua
-- Get the MarketplaceService
local MarketplaceService = game:GetService("MarketplaceService")

-- Create an array of product types to include. In this case both game passes and developer products
local productTypes = {Enum.InfoType.GamePass, Enum.InfoType.Product}

-- Call in a protected call to handle errors gracefully
local success, topRankedItems = pcall(function()
    return MarketplaceService:RecommendTopProductsAsync(productTypes)
end)

if not success then
    error("Failed to rank products")
end

-- Load the returned items into the store. Make sure to filter out any ineligible items from topRankedItems such as developer products the user can no longer purchase
for i, rankedItem in ipairs(topRankedItems) do
    local productIdentifier = rankedItem.ProductIdentifier
    local productInfo = rankedItem.ProductInfo
    -- ...
    -- Logic to add products into store
end
```

### Method: MarketplaceService:UserOwnsGamePassAsync

**Signature:** `MarketplaceService:UserOwnsGamePassAsync(userId: User, gamePassId: int64): boolean`

Returns true if the user with the given [UserId](/docs/reference/engine/classes/Player.md) owns
the [pass](/docs/en-us/production/monetization/passes.md) with the given
`gamePassId` (not to be confused with an asset ID). You can use this
method on both the client and the server.

#### Caching Behavior

The results of this function are cached so that repeated calls are
returned faster. When the
[PromptGamePassPurchaseFinished](/docs/reference/engine/classes/MarketplaceService.md)
event fires, the cache gets updated to reflect the latest ownership state
of the associated game pass.

If the user purchases a game pass outside of the experience while
remaining in the same session, the cache is eventually updated, but this
process might take several minutes to propagate.

When a user first enters a server after purchasing a game pass, this
functions always returns true.

#### Batching behavior

This method is **Transparent Batching capable**. If you spawn multiple
calls concurrently using `task.spawn`, the engine automatically combines
them into fewer HTTP requests behind the scenes. This is faster and helps
you avoid rate limits. See
[Transparent Batching](/docs/en-us/scripting/transparent-batching.md) for
details.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: AssetRead*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `userId` | `User` |  | The [UserId](/docs/reference/engine/classes/Player.md) of the [Player](/docs/reference/engine/classes/Player.md) whose inventory you're checking. |
| `gamePassId` | `int64` |  | The pass ID you want to check for. Not to be confused with an asset ID. |

**Returns:** `boolean` — Whether the user owns the pass.

**Checking Multiple Game Passes with Transparent Batching**

Shows how to check ownership of multiple game passes concurrently using
[task](/docs/reference/engine/globals/RobloxGlobals.md). When you call
[UserOwnsGamePassAsync](/docs/reference/engine/classes/MarketplaceService.md)
multiple times at roughly the same time, the engine automatically batches them
into fewer HTTP requests behind the scenes.

```lua
local MarketplaceService = game:GetService("MarketplaceService")
local Players = game:GetService("Players")

local PASS_IDS = {1234567, 2345678, 3456789, 4567890}

local function checkPassesForPlayer(player: Player)
	local owned = {}
	local remaining = #PASS_IDS

	local function check(passId)
		local success, ownsPass = pcall(function()
			return MarketplaceService:UserOwnsGamePassAsync(player.UserId, passId)
		end)

		if success and ownsPass then
			table.insert(owned, passId)
		end

		remaining -= 1
	end

	-- Spawning all calls concurrently lets the engine batch them into
	-- fewer HTTP requests automatically.
	for _, passId in PASS_IDS do
		task.spawn(check, passId)
	end

	while remaining > 0 do
		task.wait()
	end

	return owned
end

Players.PlayerAdded:Connect(function(player)
	local ownedPasses = checkPassesForPlayer(player)
	print(player.Name, "owns", #ownedPasses, "passes")
end)
```

### Method: MarketplaceService:GetProductInfo

**Signature:** `MarketplaceService:GetProductInfo(assetId: int64, infoType?: InfoType): Dictionary`

> **Deprecated:** This method has been superseded by [GetProductInfoAsync()](/docs/reference/engine/classes/MarketplaceService.md).

Returns the product information of an asset using its asset ID.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: AssetRead*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `assetId` | `int64` |  | The asset ID of the specified product. |
| `infoType` | `InfoType` | `Asset` | An [InfoType](/docs/reference/engine/enums/InfoType.md) enum value specifying the type of information being retrieved. |

**Returns:** `Dictionary` — A dictionary containing information about the queried item, described
in the previous tables.

**Getting Product Info**

The below example will print the name and description of the asset with an ID
of 125378389. In this case it will print: _"Mr. Fancy Top Hat :: So fancy that
even his top hat's top hat has a top hat."_

```lua
local MarketplaceService = game:GetService("MarketplaceService")

local ASSET_ID = 125378389

local asset = MarketplaceService:GetProductInfoAsync(ASSET_ID)
print(asset.Name .. " :: " .. asset.Description)
```

### Method: MarketplaceService:PlayerOwnsAsset

**Signature:** `MarketplaceService:PlayerOwnsAsset(player: Instance, assetId: int64): boolean`

> **Deprecated:** This method has been superseded by [PlayerOwnsAssetAsync()](/docs/reference/engine/classes/MarketplaceService.md).

Returns whether the given user has the given asset.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: AssetRead*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `player` | `Instance` |  | The [Player](/docs/reference/engine/classes/Player.md) whose inventory is tested for ownership of the given asset. |
| `assetId` | `int64` |  | The asset ID for which the given player's inventory is tested. |

**Returns:** `boolean` — Indicates whether the given player's inventory contains the given
asset.

### Method: MarketplaceService:PlayerOwnsBundle

**Signature:** `MarketplaceService:PlayerOwnsBundle(player: Player, bundleId: int64): boolean`

> **Deprecated:** This method has been superseded by [PlayerOwnsBundleAsync()](/docs/reference/engine/classes/MarketplaceService.md).

Returns whether the given player owns the given bundle.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: AssetRead*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `player` | `Player` |  | The [Player](/docs/reference/engine/classes/Player.md) whose inventory is tested for ownership of the given bundle. |
| `bundleId` | `int64` |  | The bundle ID for which the given player's inventory is tested. |

**Returns:** `boolean` — Indicates whether the given player's inventory contains the given
bundle.

### Method: MarketplaceService:PromptPremiumPurchase

**Signature:** `MarketplaceService:PromptPremiumPurchase(player: Instance): ()`

> **Deprecated:** This method has been superseded by [PromptRobloxSubscriptionPurchase()](/docs/reference/engine/classes/MarketplaceService.md).

Prompts a user to purchase
[Roblox Premium](https://www.roblox.com/premium/membership). To learn more
about Premium and about incorporating Premium incentives into your
experience, see
[Engagement-based payouts](/docs/en-us/production/monetization/engagement-based-payouts.md).

#### See Also

- [MarketplaceService.PromptPremiumPurchaseFinished](/docs/reference/engine/classes/MarketplaceService.md) which fires
  when the Premium purchase UI closes.
- [Players.PlayerMembershipChanged](/docs/reference/engine/classes/Players.md) which fires when the server
  recognizes that a user's membership has changed.

*Security: None · Thread Safety: Unsafe · Capabilities: PromptExternalPurchase*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `player` | `Instance` |  | The user being prompted to purchase Premium. |

**Returns:** `()`

**Prompt Premium Purchase**

The following code prompts users to purchase Premium when their character
touches the part that its containing [Script](/docs/reference/engine/classes/Script.md) is attached to, such as a
teleporter that allows access to an exclusive area.

```lua
local MarketplaceService = game:GetService("MarketplaceService")
local Players = game:GetService("Players")

local teleporter = script.Parent
local showModal = true

local TELEPORT_POSITION = Vector3.new(1200, 200, 60)

-- Teleport character to exclusive area
local function teleportPlayer(player)
	-- Request streaming around target location
	player:RequestStreamAroundAsync(TELEPORT_POSITION)

	-- Teleport character
	local character = player.Character
	if character and character.Parent then
		local currentPivot = character:GetPivot()
		character:PivotTo(currentPivot * CFrame.new(TELEPORT_POSITION))
	end
end

-- Detect character parts touching teleporter
teleporter.Touched:Connect(function(otherPart)
	local player = Players:GetPlayerFromCharacter(otherPart.Parent)
	if not player then
		return
	end

	if not player:GetAttribute("CharacterPartsTouching") then
		player:SetAttribute("CharacterPartsTouching", 0)
	end
	player:SetAttribute("CharacterPartsTouching", player:GetAttribute("CharacterPartsTouching") + 1)

	if player.MembershipType == Enum.MembershipType.Premium then
		-- User has Premium; teleport character to exclusive area within experience
		teleportPlayer(player)
	else
		-- Show purchase modal, using debounce to show once every few seconds at most
		if not showModal then
			return
		end
		showModal = false
		task.delay(5, function()
			showModal = true
		end)
		MarketplaceService:PromptPremiumPurchase(player)
	end
end)

-- Detect character parts exiting teleporter
teleporter.TouchEnded:Connect(function(otherPart)
	local player = Players:GetPlayerFromCharacter(otherPart.Parent)
	if player and player:GetAttribute("CharacterPartsTouching") then
		player:SetAttribute("CharacterPartsTouching", player:GetAttribute("CharacterPartsTouching") - 1)
	end
end)

-- Handle membership changed event
Players.PlayerMembershipChanged:Connect(function(player)
	warn("User membership changed; new membership is " .. tostring(player.MembershipType))

	-- Teleport character if membership type is Premium and character is on teleporter
	if player.MembershipType == Enum.MembershipType.Premium and player:GetAttribute("CharacterPartsTouching") > 0 then
		teleportPlayer(player)
	end
end)
```

## Events

### Event: MarketplaceService.PromptBulkPurchaseFinished

**Signature:** `MarketplaceService.PromptBulkPurchaseFinished(player: Instance, status: MarketplaceBulkPurchasePromptStatus, results: Dictionary)`

This event fires when a purchase prompt for a bulk avatar items closes.
For example, when a user receives the purchase prompt and clicks
**Cancel**, or when they receive a success or error message and click
**OK**.

Note: This is not a trusted event from the client. To check if the user
owns the items purchased, use
[MarketplaceService.PlayerOwnsAssetAsync](/docs/reference/engine/classes/MarketplaceService.md) or
[MarketplaceService.PlayerOwnsBundleAsync](/docs/reference/engine/classes/MarketplaceService.md).

*Security: None · Capabilities: PromptExternalPurchase*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `player` | `Instance` | The [Player](/docs/reference/engine/classes/Player.md) who received the prompt. |
| `status` | `MarketplaceBulkPurchasePromptStatus` | The status of the bulk purchase. |
| `results` | `Dictionary` | The table type containing the line items and their status in the following format:  ```lua {   RobuxSpent: number   Items: {     {       type: MarketplaceProductType,       id: string,       status: MarketplaceItemPurchaseStatus     },     ...   } } ```  Each line item contains the following pairs:  - `type`: The corresponding [MarketplaceProductType](/docs/reference/engine/enums/MarketplaceProductType.md) (Enum). - `id`: The ID of the asset or bundle (string). - `status`: The [MarketplaceItemPurchaseStatus](/docs/reference/engine/enums/MarketplaceItemPurchaseStatus.md) of the purchase   (Enum) |

### Event: MarketplaceService.PromptBundlePurchaseFinished

**Signature:** `MarketplaceService.PromptBundlePurchaseFinished(player: Instance, bundleId: int64, wasPurchased: boolean)`

This event fires when a purchase prompt for a bundle closes. Use
[PlayerOwnsBundleAsync()](/docs/reference/engine/classes/MarketplaceService.md)
to verify ownership instead of trusting this client-originated event.

*Security: None · Capabilities: PromptExternalPurchase*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `player` | `Instance` | The [Player](/docs/reference/engine/classes/Player.md) who received the prompt. |
| `bundleId` | `int64` | The ID of the bundle shown in the prompt. |
| `wasPurchased` | `boolean` | Whether the bundle was purchased. |

### Event: MarketplaceService.PromptGamePassPurchaseFinished

**Signature:** `MarketplaceService.PromptGamePassPurchaseFinished(player: Instance, gamePassId: int64, wasPurchased: boolean)`

This event fires when a purchase prompt for a
[pass](/docs/en-us/production/monetization/passes.md) closes. For example,
when a user receives the purchase prompt and clicks **Cancel**, or when
they receive a success or error message and click **OK**.

#### See Also

- For repeatable **developer product** purchase prompts, use
  [PromptProductPurchaseFinished](/docs/reference/engine/classes/MarketplaceService.md).
- For **affiliate gear sales** or other assets, use
  [PromptPurchaseFinished](/docs/reference/engine/classes/MarketplaceService.md).
- For more information on saving and replicating user data like purchases
  and progress, see
  [Implementing player data and purchases](https://devforum.roblox.com/t/implementing-player-data-and-purchasing-systems/2839941).

*Security: None · Capabilities: PromptExternalPurchase*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `player` | `Instance` | The [Player](/docs/reference/engine/classes/Player.md) who received the prompt. |
| `gamePassId` | `int64` | The ID number of the pass shown in the prompt. Not to be confused with an asset ID. |
| `wasPurchased` | `boolean` | Indicates if the user pressed **OK** (true), **Cancel** (false) on the purchase prompt, or if the purchase prompt errored (false).  When `PromptGamePassPurchaseFinished` fires, it updates the cache used by [UserOwnsGamePassAsync()](/docs/reference/engine/classes/MarketplaceService.md) to reflect the current ownership state.  `PromptGamePassPurchaseFinished` should only be listened to in a server script. When used on the server, values such as `wasPurchased` reflect the final outcome of the purchase attempt. When used in a local script, these values should not be relied on for validation or game logic. |

**Handling Gamepass Purchase Finished**

```lua
local MarketplaceService = game:GetService("MarketplaceService")

local function gamepassPurchaseFinished(...)
	-- Print all the details of the prompt, for example:
	-- PromptGamePassPurchaseFinished PlayerName 123456 false
	print("PromptGamePassPurchaseFinished", ...)
end

MarketplaceService.PromptGamePassPurchaseFinished:Connect(gamepassPurchaseFinished)
```

### Event: MarketplaceService.PromptPremiumPurchaseFinished

**Signature:** `MarketplaceService.PromptPremiumPurchaseFinished()`

This event fires when a purchase prompt for
[Roblox Premium](https://www.roblox.com/premium/membership) closes. For
example, when a user receives the purchase prompt and clicks **Cancel**,
or when they receive a success or error message and click **OK**.

#### See Also

- [PromptPremiumPurchase](/docs/reference/engine/classes/MarketplaceService.md)
  to prompt a user to purchase Premium.
- [PlayerMembershipChanged](/docs/reference/engine/classes/Players.md), which
  fires when the server recognizes that a user's membership has changed.

*Security: None · Capabilities: PromptExternalPurchase*

### Event: MarketplaceService.PromptProductPurchaseFinished

**Signature:** `MarketplaceService.PromptProductPurchaseFinished(userId: int64, productId: int64, isPurchased: boolean)`

**IMPORTANT:** Do **not** use the `PromptProductPurchaseFinished` event to
process purchases; instead, use the
[ProcessReceipt](/docs/reference/engine/classes/MarketplaceService.md) callback. The
firing of `PromptProductPurchaseFinished` does **not** mean that a user
has successfully purchased an item.

This event fires when a purchase prompt for a
[developer product](/docs/en-us/production/monetization/developer-products.md)
closes. For example, when a user receives the purchase prompt and clicks
**Cancel**, or when they receive a success or error message and click
**OK**. The firing of this event does **not** mean that a user has
successfully purchased an item.

While you can use the `PromptProductPurchaseFinished` event to detect when
a user closes a purchase prompt, you should **not** use it to process
purchases because those purchases might still fail in the backend for
several reasons. For example, if a Roblox system is offline, or if the
product price has changed and the user now doesn't have enough Robux to
make the purchase. To process purchases, you must use
[ProcessReceipt](/docs/reference/engine/classes/MarketplaceService.md). Using
`ProcessReceipt` allows you to confirm that the purchase has succeeded
before you grant the user the item they have purchased.

The `PromptProductPurchaseFinished` event fires with a `Player.UserId`
instead of a reference to the `Player` object.

#### See Also

- [PromptGamePassPurchaseFinished](/docs/reference/engine/classes/MarketplaceService.md)
  to prompt a user to purchase a pass.
- [PromptPurchaseFinished](/docs/reference/engine/classes/MarketplaceService.md)
  to prompt a user to purchase affiliate gear or other assets.
- For more information on saving and replicating user data like purchases
  and progress, see
  [Implementing player data and purchases](https://devforum.roblox.com/t/implementing-player-data-and-purchasing-systems/2839941).

*Security: None · Capabilities: PromptExternalPurchase*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `userId` | `int64` | The [UserId](/docs/reference/engine/classes/Player.md) of the user who received the developer product prompt. |
| `productId` | `int64` | The ID number of the developer product shown in the prompt. Not to be confused with an asset ID. |
| `isPurchased` | `boolean` | Indicates if the user pressed **OK** (true), **Cancel** (false) on the purchase prompt, or if the purchase prompt errored (false).  Do not use this parameter to process developer product purchases. |

### Event: MarketplaceService.PromptPurchaseFinished

**Signature:** `MarketplaceService.PromptPurchaseFinished(player: Instance, assetId: int64, isPurchased: boolean)`

This event fires when a purchase prompt for an affiliate gear sale or
other asset closes. For example, when a user receives the purchase prompt
and clicks **Cancel**, or when they receive a success or error message and
click **OK**.

This event does not fire for
[developer product](/docs/en-us/production/monetization/developer-products.md)
or [pass](/docs/en-us/production/monetization/passes.md) prompts.

#### See Also

- [PromptGamePassPurchaseFinished](/docs/reference/engine/classes/MarketplaceService.md)
  to prompt a user to purchase a pass.
- [PromptProductPurchaseFinished](/docs/reference/engine/classes/MarketplaceService.md)
  to prompt a user to purchase a developer product.
- For more information on saving and replicating user data like purchases
  and progress, see
  [Implementing player data and purchases](https://devforum.roblox.com/t/implementing-player-data-and-purchasing-systems/2839941).

*Security: None · Capabilities: PromptExternalPurchase*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `player` | `Instance` | The [Player](/docs/reference/engine/classes/Player.md) who received the prompt. |
| `assetId` | `int64` | The asset ID of the item shown in the prompt. |
| `isPurchased` | `boolean` | Indicates if the user pressed **OK** (true), **Cancel** (false) on the purchase prompt, or if the purchase prompt errored (false).  This might not accurately reflect if the purchase itself has been successfully processed. |

**Handling PromptPurchaseFinished Event**

The below example would print 'Telamon bought an item with AssetID: 1111' to
the output, if they were to complete a transaction in (your) game with an item
that had an AssetID of 1111. Alternatively, it would print 'Telamon didn't buy
an item with AssetID: 1111' if the opposite was true.

```lua
local MarketplaceService = game:GetService("MarketplaceService")

local function onPromptPurchaseFinished(player, assetId, isPurchased)
	if isPurchased then
		print(player.Name, "bought an item with AssetID:", assetId)
	else
		print(player.Name, "didn't buy an item with AssetID:", assetId)
	end
end

MarketplaceService.PromptPurchaseFinished:Connect(onPromptPurchaseFinished)
```

### Event: MarketplaceService.PromptRobloxSubscriptionPurchaseFinished

**Signature:** `MarketplaceService.PromptRobloxSubscriptionPurchaseFinished(user: Player, didTryPurchasing: boolean)`

This event fires when a purchase prompt for Roblox Plus closes. For
example, when a user receives the purchase prompt and clicks **Cancel**,
or when they receive a success or error message and click **OK**.

Note that this event firing does **not** guarantee the subscription was
successfully processed. Listen to [Player.HasRobloxSubscription](/docs/reference/engine/classes/Player.md) via
[Instance:GetPropertyChangedSignal()](/docs/reference/engine/classes/Instance.md) on the server to confirm a
subscription change before granting rewards.

#### See Also

- [PromptRobloxSubscriptionPurchase](/docs/reference/engine/classes/MarketplaceService.md)
  to prompt a user to purchase Roblox Plus.
- [Player.HasRobloxSubscription](/docs/reference/engine/classes/Player.md), which can be observed via
  [Instance:GetPropertyChangedSignal()](/docs/reference/engine/classes/Instance.md) to detect when a user's
  subscription status changes.

*Security: None · Capabilities: PromptExternalPurchase*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `user` | `Player` | The [Player](/docs/reference/engine/classes/Player.md) who received the prompt. |
| `didTryPurchasing` | `boolean` | Whether the user attempted to purchase Roblox Plus. |

**Handle PromptRobloxSubscriptionPurchaseFinished Event**

The following code listens for the
[MarketplaceService.PromptRobloxSubscriptionPurchaseFinished](/docs/reference/engine/classes/MarketplaceService.md) event to
detect when a player closes the Roblox Plus purchase UI. This event does not
guarantee the subscription was successfully processed. To confirm a
subscription change before granting rewards, listen to
[Player.HasRobloxSubscription](/docs/reference/engine/classes/Player.md) via
[Instance:GetPropertyChangedSignal()](/docs/reference/engine/classes/Instance.md) on the server.

```lua
local MarketplaceService = game:GetService("MarketplaceService")

local function onPromptRobloxSubscriptionPurchaseFinished(player, didTryPurchasing)
	if didTryPurchasing then
		-- Player attempted to subscribe; wait for HasRobloxSubscription change to confirm
		print(player.Name, "attempted to subscribe to Roblox Plus")
	else
		print(player.Name, "closed the Roblox Plus subscription prompt without purchasing")
	end
end

MarketplaceService.PromptRobloxSubscriptionPurchaseFinished:Connect(onPromptRobloxSubscriptionPurchaseFinished)
```

### Event: MarketplaceService.PromptSubscriptionPurchaseFinished

**Signature:** `MarketplaceService.PromptSubscriptionPurchaseFinished(user: Player, subscriptionId: string, didTryPurchasing: boolean)`

This event fires when a purchase prompt for an affiliate gear sale or
other asset closes. For example, when a user receives the purchase prompt
and clicks **Cancel**, or when they receive a success or error message and
click **OK**.

#### See Also

- [PromptSubscriptionPurchase](/docs/reference/engine/classes/MarketplaceService.md)
  to prompt a user to purchase a subscription.
- [UserSubscriptionStatusChanged](/docs/reference/engine/classes/Players.md),
  which fires when the server recognizes that a user's membership has
  changed.

*Security: None · Capabilities: PromptExternalPurchase*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `user` | `Player` | The [Player](/docs/reference/engine/classes/Player.md) who received the prompt. |
| `subscriptionId` | `string` | The ID of the subscription with a status change. |
| `didTryPurchasing` | `boolean` | Whether the user attempted to purchase the subscription. |

## Callbacks

### Callback: MarketplaceService.ProcessReceipt

**Signature:** `MarketplaceService.ProcessReceipt(receiptInfo: Dictionary): ProductPurchaseDecision`

`ProcessReceipt` is a callback to process receipts from
[developer product purchases](/docs/en-us/production/monetization/developer-products.md).
You can sell developer products inside an experience using
`MarketplaceService` functions, or outside an experience on the Store tab
of your experience details page.

You should only set the `ProcessReceipt` callback one time in a single
server-side [Script](/docs/reference/engine/classes/Script.md). This callback must handle the receipts
for all developer products you have for sale.

**IMPORTANT:** It's **highly recommended** that you properly implement the
`ProcessReceipt` callback in order to sell your developer products. You
should use `ProcessReceipt` to grant users their purchased product over
any other granting method. If your `ProcessReceipt` implementation isn't
correct, you will **not** be able to grant users the products they have
purchased on the Store tab of your experience details page.

#### Guarantees

The `ProcessReceipt` callback is called for all unresolved developer
product purchases when:

- A user successfully completes the purchase of a developer product.
- A successful developer product purchase prompt appears to the user.
- A user joins the server.

A purchase is considered **successfully initiated** when:

- The purchase is processed on Roblox's backend.
- The funds are placed in escrow.

A purchase is considered **resolved** when:

- The `ProcessReceipt` callback returns a [ProductPurchaseDecision](/docs/reference/engine/enums/ProductPurchaseDecision.md)
  enum of [PurchaseGranted](/docs/reference/engine/enums/ProductPurchaseDecision.md).
- The purchase is successfully recorded on Roblox's backend.

#### Unresolved Developer Product Purchases

An **unresolved developer product purchase** takes place when a user's
purchase of a developer product has not yet been acknowledged by the
server through the `ProcessReceipt` function.

Unresolved developer product purchases are not removed or refunded after
the escrow period expires.

#### Retries and Timeouts

`ProcessReceipt` has no time-based retry mechanism. If a user makes a
purchase that returns a [ProductPurchaseDecision](/docs/reference/engine/enums/ProductPurchaseDecision.md) enum of
[NotProcessedYet](/docs/reference/engine/enums/ProductPurchaseDecision.md), the
`ProcessReceipt` callback is only called again on the same server if:

- The user successfully initiates another developer product purchase.
- The user re-joins any server under the same experience.

`ProcessReceipt` also has no timeout for yielded callbacks. A
`ProcessReceipt` callback can yield for as long as the server is running,
and the callback result is still accepted when the result returns.

#### Limitations

- If you don't implement a `ProcessReceipt` callback, your receipts will
  be auto-acknowledged. You can't get a receipt back after it has been
  acknowledged.
- When there are multiple purchases pending for a user, `ProcessReceipt`
  callbacks are called in a non-deterministic order.
- The user must be on the server for the `ProcessReceipt` callback to be
  invoked.
- The user does not have to be on the server for the result of the
  `ProcessReceipt` callback to be recorded on the backend.
- The `ProcessReceipt` callback for a specific purchase might run on two
  different servers at the same time if the user joins the second server
  before the callback returns on the first server.
- The `ProcessReceipt` callback might still fail to be recorded on the
  backend, even if it returns a [ProductPurchaseDecision](/docs/reference/engine/enums/ProductPurchaseDecision.md) enum of
  [PurchaseGranted](/docs/reference/engine/enums/ProductPurchaseDecision.md). When
  this happens, the purchase remains unresolved.

*Security: None · Thread Safety: Unsafe · Capabilities: Monetization*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `receiptInfo` | `Dictionary` |  | The `receiptInfo` table passed to this callback contains the following data:  - `PurchaseId` &mdash; A unique identifier for the specific purchase. - `PlayerId` &mdash; The user ID of the user who made the purchase. - `ProductId` &mdash; The ID of the purchased product. - `PlaceIdWherePurchased` &mdash; The place ID in which the purchase   was made. Depending on where the user is during gameplay, the   purchase place's ID can be the same as or different from the current   place's ID. - `CurrencySpent` &mdash; The amount of currency spent in the   transaction. - `CurrencyType` &mdash; The type of currency spent in the purchase;   always [CurrencyType.Robux](/docs/reference/engine/enums/CurrencyType.md). - `ProductPurchaseChannel` — How the user acquired the developer   product. One of [ProductPurchaseChannel](/docs/reference/engine/enums/ProductPurchaseChannel.md). |

**Returns:** `ProductPurchaseDecision` — An enum that represents how the developer product receipt was
processed.

- `PurchaseGranted`:
  - Indicates that the experience successfully granted the player the
    developer product.
  - Indicates to Roblox that the developer product sale was
    successful.
- `NotProcessedYet`:
  - Indicates that the experience failed to grant the player the
    developer product.

**ProcessReceipt Callback**

The following code sample:

- Sets up the `ProcessReceipt` callback function to handle the purchase of two
  developer products for an experience.
- Checks for and records purchases using a `GlobalDataStore` called
  `PurchaseHistory`.
- Properly returns
  [PurchaseGranted](/docs/reference/engine/enums/ProductPurchaseDecision.md) if the
  transaction completes successfully, or if the function detects that the
  purchase has already been granted using the `PurchaseHistory` data store.

After the receipt processing routine, it's possible that the purchase was
granted but **recording** it as granted failed due to a data store error. This
is one unavoidable scenario that leads to duplicate granting of the purchase,
because `processReceipt()` will be called for the purchase again. You can
mitigate this by keeping another in-memory record of purchases so that the
same server will not grant the same purchase twice, but you'll need a
[session locking](/docs/en-us/cloud-services/data-stores/player-data-purchasing.md)
implementation around your data store to avoid the potential of duplicate
grants across servers.

```lua
local MarketplaceService = game:GetService("MarketplaceService")
local DataStoreService = game:GetService("DataStoreService")
local Players = game:GetService("Players")

-- Data store setup for tracking purchases that were successfully processed
local purchaseHistoryStore = DataStoreService:GetDataStore("PurchaseHistory")

local productIdByName = {
	fullHeal = 123123,
	gold100 = 456456,
}

-- A dictionary to look up the handler function to grant a purchase corresponding to a product ID
-- These functions return true if the purchase was granted successfully
-- These functions must never yield since they're called later within an UpdateAsync() callback
local grantPurchaseHandlerByProductId = {
	[productIdByName.fullHeal] = function(_receipt, player)
		local character = player.Character
		local humanoid = character and character:FindFirstChild("Humanoid")

		-- Ensure the player has a humanoid to heal
		if not humanoid then
			return false
		end

		-- Heal the player to full Health
		humanoid.Health = humanoid.MaxHealth

		-- Indicate a successful grant
		return true
	end,

	[productIdByName.gold100] = function(_receipt, player)
		local leaderstats = player:FindFirstChild("leaderstats")
		local goldStat = leaderstats and leaderstats:FindFirstChild("Gold")

		if not goldStat then
			return false
		end

		-- Add 100 gold to the player's gold stat
		goldStat.Value += 100

		-- Indicate a successful grant
		return true
	end,
}

-- The core ProcessReceipt callback function
-- This implementation handles most failure scenarios but does not completely mitigate cross-server data failure scenarios
local function processReceipt(receiptInfo)
	local success, result = pcall(
		purchaseHistoryStore.UpdateAsync,
		purchaseHistoryStore,
		receiptInfo.PurchaseId,
		function(isPurchased)
			if isPurchased then
				-- This purchase was already recorded as granted, so it must have previously been handled
				-- Avoid calling the grant purchase handler here to prevent granting the purchase twice

				-- While the value in the data store is already true, true is returned again so that the pcall result variable is also true
				-- This will later be used to return PurchaseGranted from the receipt processor
				return true
			end

			local player = Players:GetPlayerByUserId(receiptInfo.PlayerId)
			if not player then
				-- Avoids granting the purchase if the player is not in the server
				-- When they rejoin, this receipt processor will be called again
				return nil
			end

			local grantPurchaseHandler = grantPurchaseHandlerByProductId[receiptInfo.ProductId]
			if not grantPurchaseHandler then
				-- If there's no handler defined for this product ID, the purchase cannot be processed
				-- This will never happen as long as a handler is set for every product ID sold in the experience
				warn(`No purchase handler defined for product ID '{receiptInfo.ProductId}'`)
				return nil
			end

			local handlerSucceeded, handlerResult = pcall(grantPurchaseHandler, receiptInfo, player)
			if not handlerSucceeded then
				local errorMessage = handlerResult
				warn(
					`Grant purchase handler errored while processing purchase from '{player.Name}' of product ID '{receiptInfo.ProductId}': {errorMessage}`
				)
				return nil
			end

			local didHandlerGrantPurchase = handlerResult == true
			if not didHandlerGrantPurchase then
				-- The handler did not grant the purchase, so record it as not granted
				return nil
			end

			-- The purchase is now granted to the player, so record it as granted
			-- This will later be used to return PurchaseGranted from the receipt processor
			return true
		end
	)

	if not success then
		local errorMessage = result
		warn(`Failed to process receipt due to data store error: {errorMessage}`)

		return Enum.ProductPurchaseDecision.NotProcessedYet
	end

	local didGrantPurchase = result == true
	return if didGrantPurchase
		then Enum.ProductPurchaseDecision.PurchaseGranted
		else Enum.ProductPurchaseDecision.NotProcessedYet
end

-- Set the callback; this can only be done once by one script on the server
MarketplaceService.ProcessReceipt = processReceipt
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