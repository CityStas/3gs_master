---
name: AvatarEditorService
last_updated: 2026-10-30T19:55:52Z
inherits:
  - Instance
  - Object
type: class
memory_category: Instances
tags:
  - NotCreatable
  - Service
summary: "A service to support developer Avatar Editors."
---

# Class: AvatarEditorService

> A service to support developer Avatar Editors.

## Description

AvatarEditorService is a service to support developer Avatar Editors. It
provides methods to modify the player's platform avatar, request information
about a user's inventory, and request information about the catalog.

For more information regarding the Avatar Editor, see
[Avatar Editor Service](/docs/en-us/players/avatar-editor.md).

#### Throttling

The following endpoints on `AvatarEditorService` have experience-level
throttling:

- [AvatarEditorService.GetItemDetailsAsync](/docs/reference/engine/classes/AvatarEditorService.md)
- [AvatarEditorService.GetBatchItemDetailsAsync](/docs/reference/engine/classes/AvatarEditorService.md)
- [AvatarEditorService.GetRecommendedAssetsAsync](/docs/reference/engine/classes/AvatarEditorService.md)
- [AvatarEditorService.GetRecommendedBundlesAsync](/docs/reference/engine/classes/AvatarEditorService.md)
- [AvatarEditorService.SearchCatalogAsync](/docs/reference/engine/classes/AvatarEditorService.md)
- [AvatarEditorService.PromptSetFavorite](/docs/reference/engine/classes/AvatarEditorService.md)
- [AvatarEditorService.GetFavoriteAsync](/docs/reference/engine/classes/AvatarEditorService.md)

For each experience, this throttling allows you to send up to 100 requests per
second to these `AvatarEditorService` endpoints, regardless of the number of
servers or user count. Exceeding these limits returns a
`429 Too Many Requests` error.

#### Item Details Response

The following methods return item data in a shared response format:

- [AvatarEditorService:GetItemDetailsAsync()](/docs/reference/engine/classes/AvatarEditorService.md)
- [AvatarEditorService:GetBatchItemDetailsAsync()](/docs/reference/engine/classes/AvatarEditorService.md)
- [AvatarEditorService:GetBundlesByAssetIdAsync()](/docs/reference/engine/classes/AvatarEditorService.md)
- [AvatarEditorService:SearchCatalogAsync()](/docs/reference/engine/classes/AvatarEditorService.md)

```lua
{
  "Id": 0,
  "ItemType": "Asset",
  "AssetType": "Image",
  "BundleType": "BodyParts",
  "Name": "string",
  "Description": "string",
  "ProductId": 0,
  "ItemStatus": ["New"],
  "ItemRestrictions": ["Collectible"],

  "BundledItems": [
    {
      "Id": 0,
      "Name": "string",
      "Type": "Asset",
      "AssetType": "string",
      "SupportsHeadShapes": false,
      "Owned": false
    }
  ],
  "IsRecolorable": false,

  "CollectibleItemId": "string",
  "TotalQuantity": 0,
  "UnitsAvailableForConsumption": 0,
  "QuantityLimitPerUser": 0,
  "HasResellers": false,
  "OffSaleDeadline": null,

  "Price": 0,
  "PremiumPricing": {
    "PremiumDiscountPercentage": 0,
    "PremiumPriceInRobux": 0
  },
  "LowestPrice": 0,
  "LowestResalePrice": 0,
  "PriceStatus": "string",
  "SaleLocationType": "ShopAndAllExperiences",
  "PurchaseCount": 0,
  "FavoriteCount": 0,

  "CreatorType": "User",
  "CreatorTargetId": 0,
  "CreatorName": "string",
  "CreatorHasVerifiedBadge": false,

  "SupportsHeadShapes": false,

  "TimedOptions": [
    { "Duration": 259200, "Price": 30 },
    { "Duration": 604800, "Price": 40 },
    { "Duration": 1209600, "Price": 50 }
  ]
}
```

##### Basic Information

| Field | Type | Description |
| --- | --- | --- |
| `Id` | number | The unique identifier of the item. |
| `ItemType` | string | The type of item: `"Asset"` or `"Bundle"`. Corresponds to [AvatarItemType](/docs/reference/engine/enums/AvatarItemType.md). |
| `AssetType` | string | The asset type. Corresponds to [AvatarAssetType](/docs/reference/engine/enums/AvatarAssetType.md) values (e.g., `"Hat"`, `"Shirt"`). Only present if `ItemType` is `"Asset"`. |
| `SupportsHeadShapes` | boolean | Whether the asset supports head shape swapping. Only present if `AssetType` is `"DynamicHead"`. |
| `BundleType` | string | The bundle type. Corresponds to [BundleType](/docs/reference/engine/enums/BundleType.md) values (e.g., `"BodyParts"`, `"Animations"`). Only present if `ItemType` is `"Bundle"`. |
| `Name` | string | The display name of the item. |
| `Description` | string | The item's description text. |
| `ProductId` | number | The product ID associated with this item. |
| `ItemStatus` | array | An array of status strings (e.g., `"New"`, `"Sale"`, `"XboxExclusive"`, `"AmazonExclusive"`). |
| `ItemRestrictions` | array | An array of restriction strings. See the `itemRestrictions` table below. |

##### Bundle Information

| Field | Type | Description |
| --- | --- | --- |
| `BundledItems` | array | An array of items contained in the bundle. Only present if `ItemType` is `"Bundle"`. Each entry contains: |
|  | `Id`: The unique identifier of the bundled item. |
|  | `Name`: The display name of the bundled item. |
|  | `Type`: The type of the bundled item (e.g., `"Asset"`). |
|  | `AssetType`: The asset type as a string. Corresponds to [AvatarAssetType](/docs/reference/engine/enums/AvatarAssetType.md) values (e.g., `"Hat"`, `"DynamicHead"`). |
|  | `SupportsHeadShapes`: Whether the asset supports head shape swapping. Only present if `AssetType` is `"DynamicHead"`. |
|  | `Owned`: Whether the bundled item is owned by the current user. |
| `IsRecolorable` | boolean | Whether the bundle supports skin tone matching. Only applies to BodyParts and DynamicHead bundles. |

##### Collectible Information

| Field | Type | Description |
| --- | --- | --- |
| `CollectibleItemId` | string | The unique item ID of the collectible. |
| `TotalQuantity` | number | The total quantity of the collectible available for purchase (not resale). |
| `UnitsAvailableForConsumption` | number | The number of units available for purchase. Only applies to Limited items with remaining stock. |
| `QuantityLimitPerUser` | number | Maximum number of the same collectible item a user can own. |
| `HasResellers` | boolean | `true` when item is a Limited collectible and there are copies available for resale. |
| `OffSaleDeadline` | string | The date/time when the item goes off sale. |

##### Pricing and Sale Information

| Field | Type | Description |
| --- | --- | --- |
| `Price` | number | The price in Robux. `0` if free or not for sale. |
| `PremiumPricing` | table | Premium pricing information. Contains the following fields: |
|  | `PremiumDiscountPercentage`: The discount percentage for Premium members. |
|  | `PremiumPriceInRobux`: The discounted price in Robux for Premium members. |
| `LowestPrice` | number | The lowest resale price for Limited items. |
| `LowestResalePrice` | number | The lowest resale price for the collectible in Robux. |
| `PriceStatus` | string | The price status (e.g., `"Free"`, `"Off Sale"`, `"No Resellers"`). |
| `SaleLocationType` | string | The type of sale location setting. See `SaleLocationType` values below. |
| `PurchaseCount` | number | The total number of times this item has been purchased. |
| `FavoriteCount` | number | The total number of users who have favorited this item. |

##### Creator Information

| Field | Type | Description |
| --- | --- | --- |
| `CreatorType` | string | Either `User` or `Group`. See [CreatorType](/docs/reference/engine/enums/CreatorType.md). |
| `CreatorTargetId` | number | The ID of the creator user or group. |
| `CreatorName` | string | The display name of the creator. |
| `CreatorHasVerifiedBadge` | boolean | Boolean of whether the creator has a verified badge. |

##### Timed Options Information

| Field | Type | Description |
| --- | --- | --- |
| `TimedOptions` | array | Optional. An array of available timed options with durations and prices. Only present for assets that support timed ownership. Do not hardcode duration values; always retrieve them from the API as available options may change. Each entry contains: |
|  | `Duration`: The duration in seconds (e.g. 259200 for 3 days, 604800 for 7 days). |
|  | `Price`: The price in Robux for this duration. |

##### SaleLocationType Values

| Value                    | Description                                                                            |
| :----------------------- | :------------------------------------------------------------------------------------- |
| `NotApplicable`          | Default value, should not occur in practice.                                           |
| `ShopOnly`               | Item can only be purchased in the Roblox catalog shop.                                 |
| `MyExperiencesOnly`      | Item can only be purchased in the creator's experiences.                               |
| `ShopAndMyExperiences`   | Item can be purchased in the Roblox catalog shop or the creator's experiences.         |
| `ExperiencesById`        | Item can only be purchased in a specific list of experiences.                          |
| `ShopAndAllExperiences`  | Item can be purchased in the Roblox catalog shop and all experiences.                  |
| `ExperiencesDevApiOnly`  | Item can only be purchased in experiences via developer APIs.                          |
| `ShopAndExperiencesById` | Item can be purchased in the Roblox catalog shop or a whitelisted list of experiences. |

##### itemRestrictions Values

| itemRestrictions | Limited or Unlimited  |
| :--------------: | :-------------------: |
|     `empty`      |       Unlimited       |
|  `Collectible`   |      UGC Limited      |
|    `Limited`     |    Roblox Limited     |
| `LimitedUnique`  | Roblox Limited Unique |

## Methods

### Method: AvatarEditorService:CheckApplyDefaultClothingAsync

**Signature:** `AvatarEditorService:CheckApplyDefaultClothingAsync(humanoidDescription: HumanoidDescription): HumanoidDescription`

Returns a new [HumanoidDescription](/docs/reference/engine/classes/HumanoidDescription.md) with the Shirt and Pants
properties updated if necessary. Returns `nil` if default clothing was not
needed.

Default clothing is necessary if the HumanoidDescription does not
currently have Shirt and Pants equipped and the body colors are too
similar.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: AvatarAppearance*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `humanoidDescription` | `HumanoidDescription` |  | The HumanoidDescription to check if default clothing is required. |

**Returns:** `HumanoidDescription` — Returns a HumanoidDescription if default clothing was necessary.
Otherwise returns `nil`.

### Method: AvatarEditorService:ConformToAvatarRulesAsync

**Signature:** `AvatarEditorService:ConformToAvatarRulesAsync(humanoidDescription: HumanoidDescription): HumanoidDescription`

This method also remaps classic face and classic head assets to their
corresponding Dynamic Head asset IDs, with the appropriate
[HeadShape](/docs/reference/engine/classes/BodyPartDescription.md) pre-applied. This
remapping happens automatically and requires no code changes.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: AvatarAppearance*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `humanoidDescription` | `HumanoidDescription` |  | The [HumanoidDescription](/docs/reference/engine/classes/HumanoidDescription.md) to conform. |

**Returns:** `HumanoidDescription` — A new [HumanoidDescription](/docs/reference/engine/classes/HumanoidDescription.md) that conforms to the platform Avatar
rules.

### Method: AvatarEditorService:GetAccessoryType

**Signature:** `AvatarEditorService:GetAccessoryType(avatarAssetType: AvatarAssetType): AccessoryType`

Returns the [AccessoryType](/docs/reference/engine/enums/AccessoryType.md) that corresponds to the given
[AvatarAssetType](/docs/reference/engine/enums/AvatarAssetType.md), which is useful for grouping avatar assets by the
accessory slot they occupy.

The mapping covers accessory asset types — for example,
[AvatarAssetType.HairAccessory](/docs/reference/engine/enums/AvatarAssetType.md) maps to [AccessoryType.Hair](/docs/reference/engine/enums/AccessoryType.md),
and layered-clothing types such as [AvatarAssetType.ShirtAccessory](/docs/reference/engine/enums/AvatarAssetType.md)
map to [AccessoryType.Shirt](/docs/reference/engine/enums/AccessoryType.md). An [AvatarAssetType](/docs/reference/engine/enums/AvatarAssetType.md) that does not
correspond to an accessory (for example, an animation or a body part)
returns [AccessoryType.Unknown](/docs/reference/engine/enums/AccessoryType.md).

This method returns immediately; it does not yield or perform a web
request.

*Security: None · Thread Safety: Unsafe*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `avatarAssetType` | `AvatarAssetType` |  | The [AvatarAssetType](/docs/reference/engine/enums/AvatarAssetType.md) to convert to its corresponding [AccessoryType](/docs/reference/engine/enums/AccessoryType.md). |

**Returns:** `AccessoryType` — The [AccessoryType](/docs/reference/engine/enums/AccessoryType.md) corresponding to the given
[AvatarAssetType](/docs/reference/engine/enums/AvatarAssetType.md), or [AccessoryType.Unknown](/docs/reference/engine/enums/AccessoryType.md) if the asset
type has no matching accessory type.

### Method: AvatarEditorService:GetAvatarRulesAsync

**Signature:** `AvatarEditorService:GetAvatarRulesAsync(): Dictionary`

This function returns the platform Avatar rules for things like scaling,
default shirts and pants, number of wearable assets, ect.

The returned table includes the following fields:

```lua
{
  "PlayerAvatarTypes": [
    "R6"
  ],
  "Scales": {},
  "WearableAssetTypes": [
    {
      "MaxNumber": 0,
      "Id": 0,
      "Name": "string"
    }
  ],
  "BodyColorsPalette": [
    {
      "BrickColorId": 0,
      "NexColor": "string",
      "Name": "string"
    }
  ],
  "BasicBodyColorsPalette": [
    {
      "BrickColorId": 0,
      "HexColor": "string",
      "Name": "string"
    }
  ],
  "MinimumDeltaEBodyColorDifference": 0,
  "ProportionsAndBodyTypeEnabledForUser": true,
  "DefaultClothingAssetLists": {
    "DefaultShirtAssetIds": [
      0
    ],
    "DefaultPantAssetIds": [
      0
    ]
  },
  "BundlesEnabledForUser": true,
  "EmotesEnabledForUser": true
}
```

*Yields · Security: None · Thread Safety: Unsafe*

**Returns:** `Dictionary` — A dictionary containing the platform Avatar rules for things like
scaling, default shirts and pants, number of wearable assets, ect. See
the example return in the main description above.

### Method: AvatarEditorService:GetBatchItemDetailsAsync

**Signature:** `AvatarEditorService:GetBatchItemDetailsAsync(itemIds: Array, itemType: AvatarItemType): Array`

Gets the item details for a list of items at once. More efficient than
[AvatarEditorService:GetItemDetailsAsync()](/docs/reference/engine/classes/AvatarEditorService.md) if you need to get the
item details for multiple items.

Returns an array of items (see Item Details Response above in summary).
Each item includes the `TimedOptions` field when the asset supports timed
ownership.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: AssetRead*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `itemIds` | `Array` |  | The list of item ids to get details of. |
| `itemType` | `AvatarItemType` |  | The type of the item ids provided. |

**Returns:** `Array` — Returns an array of item details.

### Method: AvatarEditorService:GetBundlesByAssetIdAsync

**Signature:** `AvatarEditorService:GetBundlesByAssetIdAsync(assetId: int64, limit?: int64): CatalogPages`

Returns a paginated list of bundles that contain the specified asset.
Results are returned in ascending order by date created. Each page entry
uses the **Item Details Response** format (see service description above).

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: AssetRead*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `assetId` | `int64` |  | The ID of the asset to find bundles for. |
| `limit` | `int64` | `10` | The number of results per page. Accepts `10`, `25`, `50`, and `100`. |

**Returns:** `CatalogPages` — A [CatalogPages](/docs/reference/engine/classes/CatalogPages.md) object containing bundles that include the
given asset.

### Method: AvatarEditorService:GetFavoriteAsync

**Signature:** `AvatarEditorService:GetFavoriteAsync(itemId: int64, itemType: AvatarItemType): boolean`

This function returns if the [Players.LocalPlayer](/docs/reference/engine/classes/Players.md) has favorited the
given bundle or asset.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Players, AssetRead*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `itemId` | `int64` |  | The ID of the specified asset or bundle. |
| `itemType` | `AvatarItemType` |  | The [AvatarItemType](/docs/reference/engine/enums/AvatarItemType.md) of the specified asset or bundle. |

**Returns:** `boolean` — Whether the `LocalPlayer` has favorited the given bundle or asset.

### Method: AvatarEditorService:GetHeadShapesAsync

**Signature:** `AvatarEditorService:GetHeadShapesAsync(): Array`

Each head shape corresponds to a classic head owned by the user and can be
applied to any Dynamic Head that supports shape swapping (see
[BodyPartDescription.HeadShape](/docs/reference/engine/classes/BodyPartDescription.md)).

This method requires the user to have accepted the
[AvatarEditorService:PromptAllowInventoryReadAccess()](/docs/reference/engine/classes/AvatarEditorService.md) prompt.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Players, AssetRead*

**Returns:** `Array` — An array of strings, each identifying a head shape owned by
[Players.LocalPlayer](/docs/reference/engine/classes/Players.md). Possible values include: `"Blockhead"`,
`"Cheeks"`, `"Chiseled"`, `"ClassicFemaleV2"`, `"ClassicMaleV2"`,
`"CoolThing"`, `"Default"`, `"EraserHead"`, `"FatHead"`, `"FlatTop"`,
`"GoldenKorbloxGeneral"`, `"GoldenMrRobot"`, `"KnightOfChivalry"`,
`"KnightOfCourage"`, `"ManHead"`, `"MercilessNinja"`, `"MrToilet"`,
`"Narrow"`, `"NeoClassicFemaleV2"`, `"NeoClassicMaleV2"`, `"Paragon"`,
`"Peabrain"`, `"Perfection"`, `"RobloxClassic"`, `"Roll"`, `"Roundy"`,
`"RoxBox"`, `"StrongJaw"`, `"TheEngineer"`, `"Trim"`, `"WomanHead"`.

**Getting owned head shapes**

This returns a list of head shapes. Each head shape corresponds to a classic
head owned by the user and can be applied to any Dynamic Head that supports
shape swapping.

```lua
local AvatarEditorService = game:GetService("AvatarEditorService")

AvatarEditorService:PromptAllowInventoryReadAccess()

local result = AvatarEditorService.PromptAllowInventoryReadAccessCompleted:Wait()

if result == Enum.AvatarPromptResult.Success then
	local shapes = AvatarEditorService:GetHeadShapesAsync()
	for i, shape in ipairs(shapes) do
		print(i, shape)
	end
end
```

### Method: AvatarEditorService:GetInventoryAsync

**Signature:** `AvatarEditorService:GetInventoryAsync(assetTypes: Array): InventoryPages`

Returns an [InventoryPages](/docs/reference/engine/classes/InventoryPages.md) object with information about owned
items in the users inventory with the given
[AvatarAssetTypes](/docs/reference/engine/enums/AvatarAssetType.md).

The returned table includes the following fields:

```lua
[
    {
      "AssetId": 0,
      "AssetType": "string",
      "Created": "string",
      "Name": "string",
      "CreatedTime": DateTime,
      "ExpirationTime": DateTime,
    }
]
```

| Field | Type | Description |
| --- | --- | --- |
| `AssetId` | number | The asset ID. |
| `AssetType` | string | The asset type as a string. |
| `Created` | string | ISO 8601 timestamp of when the item was acquired. |
| `Name` | string | The display name of the item. |
| `CreatedTime` | DateTime | When the item was acquired, as a [DateTime](/docs/reference/engine/datatypes/DateTime.md) value. |
| `ExpirationTime` | DateTime | Optional. The absolute time when the item's timed ownership expires. Only present for items acquired via a timed option. Absent for permanently owned items. |

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Players, AssetRead*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `assetTypes` | `Array` |  | The [AvatarAssetType](/docs/reference/engine/enums/AvatarAssetType.md) that can will be checked for in the player's inventory. |

**Returns:** `InventoryPages` — An [InventoryPages](/docs/reference/engine/classes/InventoryPages.md) object containing information about owned
items matching the given asset types.

**Finding Expiring Items**

The example below retrieves the player's inventory and warns about items
expiring within 24 hours.

```lua
local AvatarEditorService = game:GetService("AvatarEditorService")
local pages = AvatarEditorService:GetInventoryAsync({ Enum.AvatarAssetType.Hat })

local currentPage = pages:GetCurrentPage()
for _, item in currentPage do
	if item.ExpirationTime then
		local secondsLeft = item.ExpirationTime.UnixTimestamp - DateTime.now().UnixTimestamp
		local hoursLeft = math.floor(secondsLeft / 3600)
		if hoursLeft < 24 then
			warn(string.format("%s expires in %d hours", item.Name, hoursLeft))
		end
	end
end
```

### Method: AvatarEditorService:GetItemDetailsAsync

**Signature:** `AvatarEditorService:GetItemDetailsAsync(itemId: int64, itemType: AvatarItemType): Dictionary`

This function returns the item details for the given item. It accepts two
parameters - the first indicating the ID of the item being retrieved and
the second indicating its [AvatarItemType](/docs/reference/engine/enums/AvatarItemType.md).

The response includes all fields from Item Details Response (see above in
summary), plus the following additional fields specific to single-item
queries:

| Field | Type | Description |
| --- | --- | --- |
| `Owned` | boolean | Whether the item is owned by the current user. |
| `IsPurchasable` | boolean | Whether the item can be purchased by the current user. |
| `ExpectedSellerId` | number | The user ID of the lowest private seller if resellable, or the creator's target ID otherwise. Used when calling purchase APIs. |
| `CreatingUniverseId` | number | If this asset was created in an experience via the In-Experience Creation (IEC) pipeline, this is the universe ID of the creating experience. `nil` for standard catalog items. Use this to display attribution (e.g., "Created in [experience]") in your avatar editor UI. |
| `ExpirationTime` | DateTime | Optional. The absolute time when the item's timed ownership expires. Only present when the item is owned by the current user via a timed option. Absent for permanently owned items. |

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: AssetRead*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `itemId` | `int64` |  | The ID of the item whose details are being retrieved. |
| `itemType` | `AvatarItemType` |  | An enum value indicating the type of item whose details are being retrieved. |

**Returns:** `Dictionary` — A table containing the item info for the retrieved item.

**Checking Item Expiration**

The example below checks if an item owned via timed option is expiring soon.

```lua
local AvatarEditorService = game:GetService("AvatarEditorService")
local details = AvatarEditorService:GetItemDetailsAsync(105589844216517, Enum.AvatarItemType.Asset)

if details.ExpirationTime then
	local secondsLeft = details.ExpirationTime.UnixTimestamp - DateTime.now().UnixTimestamp
	local hoursLeft = math.floor(secondsLeft / 3600)
	if hoursLeft < 24 then
		warn(details.Name .. " expires in less than 24 hours!")
	end
end
```

### Method: AvatarEditorService:GetOutfitDetailsAsync

**Signature:** `AvatarEditorService:GetOutfitDetailsAsync(outfitId: int64): Dictionary`

This function returns the outfit details for the given outfit. It accepts
one parameter: the ID of the outfit.

Data returns in the following format:

```lua
{
  "Assets": [
    {
      "AssetType": {
        "Id": 31,
        "Name": "RightLeg"
      },
      "CurrentVersionId": 16447385805,
      "Id": 11584239464,
      "Name": "Anime Female - Right Leg",
      "SupportsHeadShapes": false
    }
  ],
  "BodyColors": {
    "HeadColor": Color3(204, 142, 105),
    "LeftArmColor": Color3(204, 142, 105),
    "LeftLegColor": Color3(204, 142, 105),
    "RightArmColor": Color3(204, 142, 105),
    "RightLegColor": Color3(204, 142, 105),
    "TorsoColor": Color3(204, 142, 105)
  },
  "Id": 14703770624,
  "IsEditable": true,
  "Name": "Your Costume",
  "OutfitType": "Avatar",
  "PlayerAvatarType": "R15",
  "Scale": {
    "BodyType": 0,
    "Depth": 1,
    "Head": 1,
    "Height": 1,
    "Proportion": 0,
    "Width": 1
  },
}
```

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: AssetRead*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `outfitId` | `int64` |  | The ID of the outfit whose details are being retrieved. |

**Returns:** `Dictionary` — A table containing the outfit info for the retrieved outfit. See above
for a sample table.

### Method: AvatarEditorService:GetOutfitsAsync

**Signature:** `AvatarEditorService:GetOutfitsAsync(outfitSource?: OutfitSource, outfitType?: OutfitType): OutfitPages`

This function returns outfit data for the [Players.LocalPlayer](/docs/reference/engine/classes/Players.md).
This would be used with
[Players:GetHumanoidDescriptionFromOutfitIdAsync()](/docs/reference/engine/classes/Players.md) to update the
players character to the outfit. Access to this would also depend on
[AvatarEditorService:PromptAllowInventoryReadAccess()](/docs/reference/engine/classes/AvatarEditorService.md) being
accepted by the user.

The returned table includes the following fields:

```lua
[
    {
      "Id": 0,
      "Name": "string",
      "IsEditable": true
    }
]
```

| Name | type | Description |
| --- | --- | --- |
| id | int | |
| name | string | |
| isEditable | boolean | |

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Players, AssetRead*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `outfitSource` | `OutfitSource` | `All` | An [OutfitSource](/docs/reference/engine/enums/OutfitSource.md) filter specifying which outfits to include. Defaults to [OutfitSource.All](/docs/reference/engine/enums/OutfitSource.md). |
| `outfitType` | `OutfitType` | `All` | An [OutfitType](/docs/reference/engine/enums/OutfitType.md) filter specifying the type of outfits to return. Defaults to [OutfitType.All](/docs/reference/engine/enums/OutfitType.md). |

**Returns:** `OutfitPages` — An [OutfitPages](/docs/reference/engine/classes/OutfitPages.md) object containing the outfit data for the local
player.

### Method: AvatarEditorService:GetRecommendedAssetsAsync

**Signature:** `AvatarEditorService:GetRecommendedAssetsAsync(assetType: AvatarAssetType, contextAssetId?: int64): Array`

Returns a list of recommended assets based on a given [AssetType](/docs/reference/engine/enums/AssetType.md) and
asset ID. Use this to gather a list of similar assets to the asset
provided. Take a look at the code sample below for more information on
possible usages for this function.

Data is in the format:

```lua
[
    {
      "Item": {
        "AssetId": 0,
        "Name": "string",
        "Price": 0,
        "PremiumPrice": 0
      },
      "Creator": {
        "CreatorId": 0,
        "CreatorType": "string",
        "Name": "string"
      },
      "Product": {
        "Id": 0,
        "PriceInRobux": 0,
        "IsForSale": true,
        "IsResellable": true,
        "IsLimited": true,
        "IsLimitedUnique": true,
        "TotalPrivateSales": 0,
        "OffsaleDeadline": "string",
        "IsFree": true
      }
    }
]
```

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: AssetRead*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `assetType` | `AvatarAssetType` |  | The type of asset recommendations to retrieve recommendations for. Only affects the response when item based recommendations don't exist for the given `contextAssetId`. |
| `contextAssetId` | `int64` | `0` | The ID of an asset with a type matching the provided assetType used for context when retrieving recommendations. |

**Returns:** `Array` — A list of recommendations based on the given [AssetType](/docs/reference/engine/enums/AssetType.md).

**Getting a Hat Recommendation**

This will return a list of similar hats much like how similar assets are
displayed when viewing the catalog page on the website. The contextAssetId is
optional and if not provided it will return some popular items from that
category.

```lua
local AvatarEditorService = game:GetService("AvatarEditorService")

local assets = AvatarEditorService:GetRecommendedAssetsAsync(Enum.AvatarAssetType.Hat, 9255093)

for _, asset in ipairs(assets) do
	print(asset.Item.Name)
end
```

### Method: AvatarEditorService:GetRecommendedBundlesAsync

**Signature:** `AvatarEditorService:GetRecommendedBundlesAsync(bundleId: int64): Array`

This function returns a list of recommended bundles for a given bundle id.

Data is in the format:

```lua
[
    {
      "Id": 0,
      "Name": "string",
      "Description": "string",
      "BundleType": "string",
      "Items": [
        {
          "Owned": true,
          "Id": 0,
          "Name": "string",
          "Type": "string",
          "AssetType": "string",
          "SupportsHeadShapes": false
        }
      ],
      "Creator": {
        "Id": 0,
        "Name": "string",
        "Type": "string"
      },
      "Product": {
        "Id": 0,
        "Type": "string",
        "IsPublicDomain": true,
        "IsForSale": true,
        "PriceInRobux": 0,
        "PremiumPricing": {
          "PremiumDiscountPercentage": 0,
          "PremiumPriceInRobux": 0
        }
      }
    }
]
```

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: AssetRead*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `bundleId` | `int64` |  | A list of recommended bundles. |

**Returns:** `Array` — The bundle ID that the recommended bundles will be returned for.

### Method: AvatarEditorService:PromptAllowInventoryReadAccess

**Signature:** `AvatarEditorService:PromptAllowInventoryReadAccess(): ()`

Prompts the [Players.LocalPlayer](/docs/reference/engine/classes/Players.md) to allow the developer to read
what items the user has in their inventory and other avatar editor related
information. The prompt needs to be confirmed by the user for the
developer to use [AvatarEditorService:GetInventoryAsync()](/docs/reference/engine/classes/AvatarEditorService.md),
[AvatarEditorService:GetOutfitsAsync()](/docs/reference/engine/classes/AvatarEditorService.md) and
[AvatarEditorService:GetFavoriteAsync()](/docs/reference/engine/classes/AvatarEditorService.md). Permission does not
persist between sessions.

*Security: None · Thread Safety: Unsafe · Capabilities: Players, AssetRead*

**Returns:** `()`

### Method: AvatarEditorService:PromptCreateOutfit

**Signature:** `AvatarEditorService:PromptCreateOutfit(outfit: HumanoidDescription, rigType: HumanoidRigType, outfitOptions?: Dictionary, outfitType: Variant): ()`

Prompts the [Players.LocalPlayer](/docs/reference/engine/classes/Players.md) to save the given
[HumanoidDescription](/docs/reference/engine/classes/HumanoidDescription.md) as an outfit. Does not yield. The result can
be retrieved by listening to the
[AvatarEditorService.PromptCreateOutfitCompleted](/docs/reference/engine/classes/AvatarEditorService.md) event.

*Security: None · Thread Safety: Unsafe · Capabilities: Players, PlatformAvatarEditing*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `outfit` | `HumanoidDescription` |  | The `Outfit` that the player will be prompted to created. |
| `rigType` | `HumanoidRigType` |  | The [HumanoidRigType](/docs/reference/engine/enums/HumanoidRigType.md) that the outfit will be created for if the player confirms the prompt. |
| `outfitOptions` | `Dictionary` | `nil` | Reserved for future options. Must be empty or omitted. |
| `outfitType` | `Variant` |  | Optional [OutfitType](/docs/reference/engine/enums/OutfitType.md). Only `Avatar` and `Makeup` values are accepted. When omitted, the type is inferred from the description. |

**Returns:** `()`

### Method: AvatarEditorService:PromptDeleteOutfit

**Signature:** `AvatarEditorService:PromptDeleteOutfit(outfitId: int64): ()`

Prompts the [Players.LocalPlayer](/docs/reference/engine/classes/Players.md) to delete the given outfit. Does
not yield. The result can be retrieved by listening to the
[AvatarEditorService.PromptDeleteOutfitCompleted](/docs/reference/engine/classes/AvatarEditorService.md) event.

*Security: None · Thread Safety: Unsafe · Capabilities: Players, PlatformAvatarEditing*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `outfitId` | `int64` |  | The outfitId of the outfit to delete. |

**Returns:** `()`

### Method: AvatarEditorService:PromptRenameOutfit

**Signature:** `AvatarEditorService:PromptRenameOutfit(outfitId: int64): ()`

Prompts the [Players.LocalPlayer](/docs/reference/engine/classes/Players.md) to rename the given outfit. Does
not yield. The result can be retrieved by listening to the
[AvatarEditorService.PromptRenameOutfitCompleted](/docs/reference/engine/classes/AvatarEditorService.md) event.

*Security: None · Thread Safety: Unsafe · Capabilities: Players, PlatformAvatarEditing*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `outfitId` | `int64` |  | The outfitId of the outfit to rename. |

**Returns:** `()`

### Method: AvatarEditorService:PromptSaveAvatar

**Signature:** `AvatarEditorService:PromptSaveAvatar(humanoidDescription: HumanoidDescription, rigType: HumanoidRigType): ()`

This function prompts the [Players.LocalPlayer](/docs/reference/engine/classes/Players.md) to update their
avatar based on the given [HumanoidDescription](/docs/reference/engine/classes/HumanoidDescription.md) and
[HumanoidRigType](/docs/reference/engine/enums/HumanoidRigType.md) (R6 or R15). Does not yield and can get the result
by listening to the PromptSaveAvatarCompleted event. This is similar to
how other prompts such as PromptPurchase work.

*Security: None · Thread Safety: Unsafe · Capabilities: Players, PlatformAvatarEditing*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `humanoidDescription` | `HumanoidDescription` |  | The given [HumanoidDescription](/docs/reference/engine/classes/HumanoidDescription.md) being prompted to save. |
| `rigType` | `HumanoidRigType` |  | The [HumanoidRigType](/docs/reference/engine/enums/HumanoidRigType.md) that the avatar will be saved for if the player confirms the prompt. |

**Returns:** `()`

### Method: AvatarEditorService:PromptSetFavorite

**Signature:** `AvatarEditorService:PromptSetFavorite(itemId: int64, itemType: AvatarItemType, shouldFavorite: boolean): ()`

This function prompts the [Players.LocalPlayer](/docs/reference/engine/classes/Players.md) to favorite or
unfavorite the given asset or bundle.

*Security: None · Thread Safety: Unsafe · Capabilities: Players, PlatformAvatarEditing*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `itemId` | `int64` |  | The ItemId of the item being prompted to favorite. |
| `itemType` | `AvatarItemType` |  | The type of item being prompted to favorite. |
| `shouldFavorite` | `boolean` |  | Whether to favorite (`true`) or unfavorite (`false`) the item. |

**Returns:** `()`

### Method: AvatarEditorService:PromptUpdateOutfit

**Signature:** `AvatarEditorService:PromptUpdateOutfit(outfitId: int64, updatedOutfit: HumanoidDescription, rigType: HumanoidRigType): ()`

Prompts the [Players.LocalPlayer](/docs/reference/engine/classes/Players.md) to update the given outfit with
the given HumanoidDescription.

*Security: None · Thread Safety: Unsafe · Capabilities: Players, PlatformAvatarEditing*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `outfitId` | `int64` |  | The outfitId of the outfit to update. |
| `updatedOutfit` | `HumanoidDescription` |  | A [HumanoidDescription](/docs/reference/engine/classes/HumanoidDescription.md) that represents the new outfit data. |
| `rigType` | `HumanoidRigType` |  | The [HumanoidRigType](/docs/reference/engine/enums/HumanoidRigType.md) to update the outfit to. |

**Returns:** `()`

### Method: AvatarEditorService:SearchCatalogAsync

**Signature:** `AvatarEditorService:SearchCatalogAsync(searchParameters: CatalogSearchParams): CatalogPages`

This function returns a [CatalogPages](/docs/reference/engine/classes/CatalogPages.md) object containing the result
of the given search.

Each item in the returned pages uses the Item Details Response format (see
above in summary), including the `TimedOptions` field for assets that
support timed ownership.

Use [SalesTypeFilter.TimedOptions](/docs/reference/engine/enums/SalesTypeFilter.md) in [CatalogSearchParams](/docs/reference/engine/datatypes/CatalogSearchParams.md)
to filter results to only items with timed options available.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: AssetRead*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `searchParameters` | `CatalogSearchParams` |  | An object containing the parameters used for the search. |

**Returns:** `CatalogPages` — A [CatalogPages](/docs/reference/engine/classes/CatalogPages.md) object containing the search results.

**Searching for Items with Timed Options**

The example below searches the catalog for items that have timed options
available and prints their durations.

```lua
local AvatarEditorService = game:GetService("AvatarEditorService")

local params = CatalogSearchParams.new()
params.SalesTypeFilter = Enum.SalesTypeFilter.TimedOptions
params.Limit = 10

local pages = AvatarEditorService:SearchCatalogAsync(params)
local results = pages:GetCurrentPage()

for _, item in results do
	if item.TimedOptions then
		for _, option in item.TimedOptions do
			local days = option.Duration / 86400
			print(string.format("%s: %d days for %d R$", item.Name, days, option.Price))
		end
	end
end
```

### Method: AvatarEditorService:CheckApplyDefaultClothing

**Signature:** `AvatarEditorService:CheckApplyDefaultClothing(humanoidDescription: HumanoidDescription): HumanoidDescription`

Deprecated in favor of
[AvatarEditorService:CheckApplyDefaultClothingAsync()](/docs/reference/engine/classes/AvatarEditorService.md). This method
has the same behavior: it returns a new [HumanoidDescription](/docs/reference/engine/classes/HumanoidDescription.md) with
the Shirt and Pants properties updated if necessary, or `nil` if default
clothing was not needed.

Default clothing is necessary if the HumanoidDescription does not
currently have Shirt and Pants equipped and the body colors are too
similar.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: AvatarAppearance*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `humanoidDescription` | `HumanoidDescription` |  | The HumanoidDescription to check if default clothing is required. |

**Returns:** `HumanoidDescription` — Returns a HumanoidDescription if default clothing was necessary.
Otherwise returns `nil`.

### Method: AvatarEditorService:ConformToAvatarRules

**Signature:** `AvatarEditorService:ConformToAvatarRules(humanoidDescription: HumanoidDescription): HumanoidDescription`

Deprecated in favor of
[AvatarEditorService:ConformToAvatarRulesAsync()](/docs/reference/engine/classes/AvatarEditorService.md). Clones the given
description and adjusts scale values, accessory counts, accessory
adjustments, default clothing, and layered-clothing limits to comply with
the platform Avatar rules. It also remaps classic face and classic head
assets to their corresponding Dynamic Head asset IDs.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: AvatarAppearance*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `humanoidDescription` | `HumanoidDescription` |  | The [HumanoidDescription](/docs/reference/engine/classes/HumanoidDescription.md) to conform to the platform Avatar rules. |

**Returns:** `HumanoidDescription` — A new [HumanoidDescription](/docs/reference/engine/classes/HumanoidDescription.md) that conforms to the platform Avatar
rules.

### Method: AvatarEditorService:GetAvatarRules

**Signature:** `AvatarEditorService:GetAvatarRules(): Dictionary`

Deprecated in favor of [AvatarEditorService:GetAvatarRulesAsync()](/docs/reference/engine/classes/AvatarEditorService.md).
This method has the same behavior: it returns a dictionary containing the
platform Avatar rules. See
[AvatarEditorService:GetAvatarRulesAsync()](/docs/reference/engine/classes/AvatarEditorService.md) for the response format.

*Yields · Security: None · Thread Safety: Unsafe*

**Returns:** `Dictionary` — A dictionary containing the platform Avatar rules for things like
scaling, default shirts and pants, number of wearable assets, ect. See
the example return in the main description above.

### Method: AvatarEditorService:GetBatchItemDetails

**Signature:** `AvatarEditorService:GetBatchItemDetails(itemIds: Array, itemType: AvatarItemType): Array`

Deprecated in favor of
[AvatarEditorService:GetBatchItemDetailsAsync()](/docs/reference/engine/classes/AvatarEditorService.md). This method has
the same behavior: it gets the item details for a list of items at once
and returns an array of item details in the Item Details Response format.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: AssetRead*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `itemIds` | `Array` |  | The list of item ids to get details of. |
| `itemType` | `AvatarItemType` |  | The type of the item ids provided. |

**Returns:** `Array` — Returns an array of item details. See
[AvatarEditorService:GetBatchItemDetailsAsync()](/docs/reference/engine/classes/AvatarEditorService.md) for the
response format.

### Method: AvatarEditorService:GetFavorite

**Signature:** `AvatarEditorService:GetFavorite(itemId: int64, itemType: AvatarItemType): boolean`

Deprecated in favor of [AvatarEditorService:GetFavoriteAsync()](/docs/reference/engine/classes/AvatarEditorService.md).
This method has the same behavior: it returns whether the
[Players.LocalPlayer](/docs/reference/engine/classes/Players.md) has favorited the given bundle or asset.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Players, AssetRead*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `itemId` | `int64` |  | The ID of the specified asset or bundle. |
| `itemType` | `AvatarItemType` |  | The [AvatarItemType](/docs/reference/engine/enums/AvatarItemType.md) of the specified asset or bundle. |

**Returns:** `boolean` — Whether the `LocalPlayer` has favorited the given bundle or asset.

### Method: AvatarEditorService:GetInventory

**Signature:** `AvatarEditorService:GetInventory(assetTypes: Array): InventoryPages`

Deprecated in favor of [AvatarEditorService:GetInventoryAsync()](/docs/reference/engine/classes/AvatarEditorService.md).
This method has the same behavior: it returns an [InventoryPages](/docs/reference/engine/classes/InventoryPages.md)
object with information about items owned by the
[Players.LocalPlayer](/docs/reference/engine/classes/Players.md) that match the given
[AvatarAssetTypes](/docs/reference/engine/enums/AvatarAssetType.md). See
[AvatarEditorService:GetInventoryAsync()](/docs/reference/engine/classes/AvatarEditorService.md) for the response format.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Players, AssetRead*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `assetTypes` | `Array` |  | The [AvatarAssetType](/docs/reference/engine/enums/AvatarAssetType.md) that can will be checked for in the player's inventory. |

**Returns:** `InventoryPages` — An [InventoryPages](/docs/reference/engine/classes/InventoryPages.md) object containing information about owned
items matching the given asset types.

### Method: AvatarEditorService:GetItemDetails

**Signature:** `AvatarEditorService:GetItemDetails(itemId: int64, itemType: AvatarItemType): Dictionary`

Deprecated in favor of [AvatarEditorService:GetItemDetailsAsync()](/docs/reference/engine/classes/AvatarEditorService.md).
This method has the same behavior: it returns a table containing the item
details for the given item. See
[AvatarEditorService:GetItemDetailsAsync()](/docs/reference/engine/classes/AvatarEditorService.md) for the response format.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: AssetRead*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `itemId` | `int64` |  | The ID of the item whose details are being retrieved. |
| `itemType` | `AvatarItemType` |  | An enum value indicating the type of item whose details are being retrieved. |

**Returns:** `Dictionary` — A table containing the item info for the retrieved item. See above for
a sample table.

### Method: AvatarEditorService:GetOutfitDetails

**Signature:** `AvatarEditorService:GetOutfitDetails(outfitId: int64): Dictionary`

Deprecated in favor of
[AvatarEditorService:GetOutfitDetailsAsync()](/docs/reference/engine/classes/AvatarEditorService.md). This method has the
same behavior: it returns a table containing the outfit details for the
given outfit. See [AvatarEditorService:GetOutfitDetailsAsync()](/docs/reference/engine/classes/AvatarEditorService.md) for
the response format.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: AssetRead*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `outfitId` | `int64` |  | The ID of the outfit whose details are being retrieved. |

**Returns:** `Dictionary` — A table containing the outfit info for the retrieved outfit. See above
for a sample table.

### Method: AvatarEditorService:GetOutfits

**Signature:** `AvatarEditorService:GetOutfits(outfitSource?: OutfitSource, outfitType?: OutfitType): OutfitPages`

Deprecated in favor of [AvatarEditorService:GetOutfitsAsync()](/docs/reference/engine/classes/AvatarEditorService.md). This
method has the same behavior: it returns outfit data for the
[Players.LocalPlayer](/docs/reference/engine/classes/Players.md). See
[AvatarEditorService:GetOutfitsAsync()](/docs/reference/engine/classes/AvatarEditorService.md) for the response format.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: Players, AssetRead*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `outfitSource` | `OutfitSource` | `All` | An [OutfitSource](/docs/reference/engine/enums/OutfitSource.md) filter specifying which outfits to include. Defaults to [OutfitSource.All](/docs/reference/engine/enums/OutfitSource.md). |
| `outfitType` | `OutfitType` | `All` | An [OutfitType](/docs/reference/engine/enums/OutfitType.md) filter specifying the type of outfits to return. Defaults to [OutfitType.All](/docs/reference/engine/enums/OutfitType.md). |

**Returns:** `OutfitPages` — An [OutfitPages](/docs/reference/engine/classes/OutfitPages.md) object containing the outfit data for the local
player.

### Method: AvatarEditorService:GetRecommendedAssets

**Signature:** `AvatarEditorService:GetRecommendedAssets(assetType: AvatarAssetType, contextAssetId?: int64): Array`

Deprecated in favor of
[AvatarEditorService:GetRecommendedAssetsAsync()](/docs/reference/engine/classes/AvatarEditorService.md). This method has
the same behavior: it returns a list of recommended assets based on the
given [AvatarAssetType](/docs/reference/engine/enums/AvatarAssetType.md) and context asset ID. See
[AvatarEditorService:GetRecommendedAssetsAsync()](/docs/reference/engine/classes/AvatarEditorService.md) for the response
format.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: AssetRead*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `assetType` | `AvatarAssetType` |  | The type of asset recommendations to retrieve recommendations for. Only affects the response when item based recommendations don't exist for the given `contextAssetId`. |
| `contextAssetId` | `int64` | `0` | The ID of an asset with a type matching the provided assetType used for context when retrieving recommendations. |

**Returns:** `Array` — A list of recommendations based on the given [AssetType](/docs/reference/engine/enums/AssetType.md).

**Getting a Hat Recommendation**

This will return a list of similar hats much like how similar assets are
displayed when viewing the catalog page on the website. The contextAssetId is
optional and if not provided it will return some popular items from that
category.

```lua
local AvatarEditorService = game:GetService("AvatarEditorService")

local assets = AvatarEditorService:GetRecommendedAssetsAsync(Enum.AvatarAssetType.Hat, 9255093)

for _, asset in ipairs(assets) do
	print(asset.Item.Name)
end
```

### Method: AvatarEditorService:GetRecommendedBundles

**Signature:** `AvatarEditorService:GetRecommendedBundles(bundleId: int64): Array`

Deprecated in favor of
[AvatarEditorService:GetRecommendedBundlesAsync()](/docs/reference/engine/classes/AvatarEditorService.md). This method has
the same behavior: it returns a list of recommended bundles for a given
bundle ID. See [AvatarEditorService:GetRecommendedBundlesAsync()](/docs/reference/engine/classes/AvatarEditorService.md)
for the response format.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: AssetRead*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `bundleId` | `int64` |  | A list of recommended bundles. |

**Returns:** `Array` — The bundle ID that the recommended bundles will be returned for.

### Method: AvatarEditorService:SearchCatalog

**Signature:** `AvatarEditorService:SearchCatalog(searchParameters: CatalogSearchParams): CatalogPages`

Deprecated in favor of [AvatarEditorService:SearchCatalogAsync()](/docs/reference/engine/classes/AvatarEditorService.md).
This method has the same behavior: it returns a [CatalogPages](/docs/reference/engine/classes/CatalogPages.md)
object containing the result of the given search. See
[AvatarEditorService:SearchCatalogAsync()](/docs/reference/engine/classes/AvatarEditorService.md) for details on the
response format.

*Yields · Security: None · Thread Safety: Unsafe · Capabilities: AssetRead*

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `searchParameters` | `CatalogSearchParams` |  | An object containing the parameters used for the search. |

**Returns:** `CatalogPages` — A [CatalogPages](/docs/reference/engine/classes/CatalogPages.md) object containing the search results.

## Events

### Event: AvatarEditorService.PromptAllowInventoryReadAccessCompleted

**Signature:** `AvatarEditorService.PromptAllowInventoryReadAccessCompleted(result: AvatarPromptResult)`

This event fires when the
[AvatarEditorService:PromptAllowInventoryReadAccess()](/docs/reference/engine/classes/AvatarEditorService.md) prompt is
responded to by the user. It can only return the Success or
PermissionDenied [enum](/docs/reference/engine/enums/AvatarPromptResult.md) statuses as it does not
perform any web requests which could fail.

*Security: None · Capabilities: Players, AssetRead*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `result` | `AvatarPromptResult` | The result of the prompt. |

### Event: AvatarEditorService.PromptCreateOutfitCompleted

**Signature:** `AvatarEditorService.PromptCreateOutfitCompleted(result: AvatarPromptResult, failureType: Variant)`

This event fires when the PromptSaveOutfit operation is completed. It
gives a status [enum](/docs/reference/engine/enums/AvatarPromptResult.md) indicating whether the
prompt succeeded, failed or permission was not granted by the user.

*Security: None · Capabilities: Players, PlatformAvatarEditing*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `result` | `AvatarPromptResult` | The result of the prompt. |
| `failureType` | `Variant` | An [CreateOutfitFailure](/docs/reference/engine/enums/CreateOutfitFailure.md) value indicating the reason the outfit creation failed, or `nil` on success. |

**Handling Outfit Creation Results**

The example below listens for the result of a PromptCreateOutfit call and
branches on the outcome, using the Enum.CreateOutfitFailure value to explain
why creation failed.

```lua
local AvatarEditorService = game:GetService("AvatarEditorService")

AvatarEditorService.PromptCreateOutfitCompleted:Connect(function(result, failureType)
	if result == Enum.AvatarPromptResult.Success then
		-- Outfit was created
	elseif result == Enum.AvatarPromptResult.PermissionDenied then
		-- User declined the prompt; ignore failureType
	else -- Enum.AvatarPromptResult.Failed
		if failureType == Enum.CreateOutfitFailure.OutfitLimitReached then
			-- Tell the user they hit the outfit cap
		elseif failureType == Enum.CreateOutfitFailure.InvalidName then
			-- Tell the user to pick a different name
		else -- Enum.CreateOutfitFailure.Other
			-- Generic failure; retry or show a generic error
		end
	end
end)
```

### Event: AvatarEditorService.PromptDeleteOutfitCompleted

**Signature:** `AvatarEditorService.PromptDeleteOutfitCompleted(result: AvatarPromptResult)`

Fires when the PromptDeleteOutfit operation is completed. It gives a
status [enum](/docs/reference/engine/enums/AvatarPromptResult.md) indicating whether the prompt
succeeded, failed or permission was not granted by the user.

*Security: None · Capabilities: Players, PlatformAvatarEditing*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `result` | `AvatarPromptResult` | The result of the prompt. |

### Event: AvatarEditorService.PromptRenameOutfitCompleted

**Signature:** `AvatarEditorService.PromptRenameOutfitCompleted(result: AvatarPromptResult)`

Fires when the PromptRenameOutfit operation is completed. It gives a
status [enum](/docs/reference/engine/enums/AvatarPromptResult.md) indicating whether the prompt
succeeded, failed or permission was not granted by the user.

*Security: None · Capabilities: Players, PlatformAvatarEditing*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `result` | `AvatarPromptResult` | The result of the prompt. |

### Event: AvatarEditorService.PromptSaveAvatarCompleted

**Signature:** `AvatarEditorService.PromptSaveAvatarCompleted(result: AvatarPromptResult, humanoidDescription: HumanoidDescription)`

This event fires when the [AvatarEditorService:PromptSaveAvatar()](/docs/reference/engine/classes/AvatarEditorService.md)
operation is completed. It gives a status [enum](/docs/reference/engine/enums/AvatarPromptResult.md)
indicating whether the prompt succeeded, failed or permission was not
granted by the user.

*Security: None · Capabilities: Players, PlatformAvatarEditing*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `result` | `AvatarPromptResult` | The result of the prompt. |
| `humanoidDescription` | `HumanoidDescription` | The [HumanoidDescription](/docs/reference/engine/classes/HumanoidDescription.md) that was saved (or attempted to be saved) to the platform avatar. |

### Event: AvatarEditorService.PromptSetFavoriteCompleted

**Signature:** `AvatarEditorService.PromptSetFavoriteCompleted(result: AvatarPromptResult)`

Fires when the [AvatarEditorService:PromptSetFavorite()](/docs/reference/engine/classes/AvatarEditorService.md) operation
is completed. It gives a status [enum](/docs/reference/engine/enums/AvatarPromptResult.md) indicating
whether the prompt succeeded, failed or permission was not granted by the
user.

*Security: None · Capabilities: Players, PlatformAvatarEditing*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `result` | `AvatarPromptResult` | The result of the prompt. |

### Event: AvatarEditorService.PromptUpdateOutfitCompleted

**Signature:** `AvatarEditorService.PromptUpdateOutfitCompleted(result: AvatarPromptResult)`

Fires when the [AvatarEditorService:PromptUpdateOutfit()](/docs/reference/engine/classes/AvatarEditorService.md) operation
is completed. It gives a status [enum](/docs/reference/engine/enums/AvatarPromptResult.md) indicating
whether the prompt succeeded, failed or permission was not granted by the
user.

*Security: None · Capabilities: Players, PlatformAvatarEditing*

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `result` | `AvatarPromptResult` | The result of the prompt. |

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