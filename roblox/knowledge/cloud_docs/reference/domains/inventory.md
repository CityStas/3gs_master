---
name: "Inventory Api v2"
last_updated: 2026-10-30T19:56:08Z
type: legacy
api_base_url: "https://inventory.roblox.com"
versions: [v2, v1]
endpoints: 15
auth: [cookie]
---

# Inventory Api v2

> **Warning:** Legacy APIs with cookie authentication can incorporate breaking changes without notice. We don't recommend them for production applications.

**Base URL:** `https://inventory.roblox.com`
**Versions:** v2, v1

## V2

### GET `/v2/assets/{assetId}/owners`

Gets a list of owners of an asset.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `assetId` | path | `integer (int64)` | Yes | The asset id. |
| `limit` | query | `integer (int32)` | No | The number of results per request. Valid values: `10`, `25`, `50`, `100` |
| `cursor` | query | `string` | No | The paging cursor for the previous or next page. |
| `sortOrder` | query | `string` | No | Sorted by userAssetId Valid values: `Asc`, `Desc` |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiPageResponse[Roblox.Inventory.Api.V2.AssetOwnerResponse]`
- `400`: 1: The asset id is invalid.
- `403`: 2: You do not have permission to view the owners of this asset.

**Response fields** (`Roblox.Web.WebAPI.Models.ApiPageResponse[Roblox.Inventory.Api.V2.AssetOwnerResponse]`)

See [Roblox.Web.WebAPI.Models.ApiPageResponse[Roblox.Inventory.Api.V2.AssetOwnerResponse]](#roblox-web-webapi-models-apipageresponse-roblox-inventory-api-v2-assetownerresponse-) in Models.

**Response example:**
```json
{
  "previousPageCursor": "string",
  "nextPageCursor": "string",
  "data": [
    {
      "id": "...",
      "collectibleItemInstanceId": "...",
      "serialNumber": "...",
      "owner": "...",
      "created": "...",
      "updated": "..."
    }
  ]
}
```

**Error handling:** `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://inventory.roblox.com/v2/assets/{ASSETID}/owners"
```

### GET `/v2/collectible-items/{collectibleItemId}/owners`

Gets a list of owners of a collectible item.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `collectibleItemId` | path | `string` | Yes | The collectible item ID. |
| `limit` | query | `integer (int32)` | No | The number of results per request. |
| `cursor` | query | `string` | No | The paging cursor for the previous or next page. |
| `sortOrder` | query | `integer (int32)` | No | The order the results are sorted in. Valid values: `1`, `2` |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiPageResponse[Roblox.Inventory.Api.V2.CollectibleItemOwnerResponse]`
- `400`: 1: The collectible item id is invalid.
- `401`: 0: Authorization has been denied for this request.
- `403`: 2: You do not have permission to view the owners of this item.

**Response fields** (`Roblox.Web.WebAPI.Models.ApiPageResponse[Roblox.Inventory.Api.V2.CollectibleItemOwnerResponse]`)

See [Roblox.Web.WebAPI.Models.ApiPageResponse[Roblox.Inventory.Api.V2.CollectibleItemOwnerResponse]](#roblox-web-webapi-models-apipageresponse-roblox-inventory-api-v2-collectibleitemownerresponse-) in Models.

**Response example:**
```json
{
  "previousPageCursor": "string",
  "nextPageCursor": "string",
  "data": [
    {
      "collectibleItemInstanceId": "...",
      "serialNumber": "...",
      "owner": "..."
    }
  ]
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://inventory.roblox.com/v2/collectible-items/{COLLECTIBLEITEMID}/owners"
```

### GET `/v2/users/{userId}/inventory`

Get user's inventory by multiple Roblox.Platform.Assets.AssetType.

GamePass and Badges not allowed.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer (int64)` | Yes | The inventory owner's userId. |
| `assetTypes` | query | `array` | Yes | The asset types to query. |
| `filterDisapprovedAssets` | query | `boolean` | No | Filters moderated assets when enabled. |
| `showApprovedOnly` | query | `boolean` | No | Filters moderated assets and assets pending review when enabled. |
| `limit` | query | `integer (int32)` | No | The number of results per request. Valid values: `10`, `25`, `50`, `100` |
| `cursor` | query | `string` | No | The paging cursor for the previous or next page. |
| `sortOrder` | query | `string` | No | The order the results are sorted in. Valid values: `Asc`, `Desc` |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiPageResponse[Roblox.Inventory.Api.V2.UserAssetItemModelV2]`
- `400`: 1: Invalid user Id. 2: Invalid asset type Id.
- `403`: 3: Insufficient permission. 4: You are not authorized to view this user's inventory.

**Response fields** (`Roblox.Web.WebAPI.Models.ApiPageResponse[Roblox.Inventory.Api.V2.UserAssetItemModelV2]`)

See [Roblox.Web.WebAPI.Models.ApiPageResponse[Roblox.Inventory.Api.V2.UserAssetItemModelV2]](#roblox-web-webapi-models-apipageresponse-roblox-inventory-api-v2-userassetitemmodelv2-) in Models.

**Response example:**
```json
{
  "previousPageCursor": "string",
  "nextPageCursor": "string",
  "data": [
    {
      "assetId": "...",
      "name": "...",
      "assetType": "...",
      "created": "..."
    }
  ]
}
```

**Error handling:** `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://inventory.roblox.com/v2/users/{USERID}/inventory?assetTypes={VALUE}"
```

### GET `/v2/users/{userId}/inventory/{assetTypeId}`

Gets user's inventory based on specific asset type

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer (int64)` | Yes | The user Id of the inventory owner |
| `assetTypeId` | path | `integer (int32)` | Yes | The asset type Id of the items to get |
| `limit` | query | `integer (int32)` | No | The number of results per request. Valid values: `10`, `25`, `50`, `100` |
| `cursor` | query | `string` | No | The paging cursor for the previous or next page. |
| `sortOrder` | query | `string` | No | The order the results are sorted in. Valid values: `Asc`, `Desc` |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiPageResponse[Roblox.Inventory.Api.Models.InventoryItemModel]`
- `400`: 1: Invalid user Id. 2: Invalid asset type Id.
- `403`: 3: Insufficient permission. 4: You are not authorized to view this user's inventory.

**Response fields** (`Roblox.Web.WebAPI.Models.ApiPageResponse[Roblox.Inventory.Api.Models.InventoryItemModel]`)

See [Roblox.Web.WebAPI.Models.ApiPageResponse[Roblox.Inventory.Api.Models.InventoryItemModel]](#roblox-web-webapi-models-apipageresponse-roblox-inventory-api-models-inventoryitemmodel-) in Models.

**Response example:**
```json
{
  "previousPageCursor": "string",
  "nextPageCursor": "string",
  "data": [
    {
      "expireAt": "...",
      "userAssetId": "...",
      "assetId": "...",
      "assetName": "...",
      "collectibleItemId": "...",
      "collectibleItemInstanceId": "..."
    }
  ]
}
```

**Error handling:** `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://inventory.roblox.com/v2/users/{USERID}/inventory/{ASSETTYPEID}"
```

### DELETE `/v2/inventory/asset/{assetId}`

Give up an asset owned by the authenticated user.
Assets that are created by Roblox user or are limited edition are not eligible for deletion
and will return NotEligibleForDelete.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `assetId` | path | `integer (int64)` | Yes | ID of the asset to delete. |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `401`: 0: Authorization has been denied for this request. 4: You are not authorized.
- `403`: 0: Token Validation Failed 2: You don't own the specified item. 3: The item is not allowed to be deleted.
- `404`: 1: The item does not exist.
- `500`: 0: An unknown error occured.

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X DELETE -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://inventory.roblox.com/v2/inventory/asset/{ASSETID}"
```

## Models

### Roblox.Inventory.Api.Models.InventoryItemModel

A model containing information about an inventory item.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `expireAt` | `string` | No | Expiration timestamp for transient items |
| `userAssetId` | `integer` | No | The user asset id |
| `assetId` | `integer` | No | The asset id of the user asset |
| `assetName` | `string` | No | The asset name of the user asset |
| `collectibleItemId` | `string` | No | The id of the corresponding collectible item |
| `collectibleItemInstanceId` | `string` | No | The id of the corresponding collectible item instance |
| `serialNumber` | `integer` | No | The serial number of the user asset |
| `owner` | `Roblox.Inventory.Api.Models.UserModel` | No |  |
| `created` | `string` | No | The creation date of the user asset |
| `updated` | `string` | No | The updated date of the user asset |

### Roblox.Inventory.Api.Models.UserModel

A model representing data about an Roblox.Platform.Membership.IUser

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `userId` | `integer` | No | The user id |
| `username` | `string` | No | The username |
| `buildersClubMembershipType` | `0 \| 1 \| 2 \| 3 \| 4` | No | The user's builders club membership type ['None' = 0, 'BC' = 1, 'TBC' = 2, 'OBC' = 3, 'RobloxPremium' = 4] |

### Roblox.Inventory.Api.V2.AssetOwnerResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | `integer` | No |  |
| `collectibleItemInstanceId` | `string` | No |  |
| `serialNumber` | `integer` | No |  |
| `owner` | `Roblox.Web.Responses.RelatedEntityTypeResponse[Roblox.Users.Client.AssociatedEntityType]` | No |  |
| `created` | `string` | No |  |
| `updated` | `string` | No |  |

### Roblox.Inventory.Api.V2.CollectibleItemOwnerResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `collectibleItemInstanceId` | `string` | No |  |
| `serialNumber` | `integer` | No |  |
| `owner` | `Roblox.Web.Responses.RelatedEntityTypeResponse[Roblox.Users.Client.AssociatedEntityType]` | No |  |

### Roblox.Inventory.Api.V2.UserAssetItemModelV2

The user asset item model for V2 controllers.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `assetId` | `integer` | No | The asset id of the user asset. |
| `name` | `string` | No | The name of asset with id Roblox.Inventory.Api.V2.UserAssetItemModelV2.AssetId. |
| `assetType` | `integer enum (89 values)` | No | The asset type id of asset with id Roblox.Inventory.Api.V2.UserAssetItemModelV2.AssetId. ['Image' = 1, 'TShirt' = 2, 'Audio' = 3, 'Mesh' = 4, 'Lua' = 5, 'HTML' = 6, 'Text' = 7, 'Hat' = 8, 'Place' = 9, 'Model' = 10, 'Shirt' = 11, 'Pants' = 12, 'Decal' = 13, 'Avatar' = 16, 'Head' = 17, 'Face' = 18, 'Gear' = 19, 'Badge' = 21, 'GroupEmblem' = 22, 'Animation' = 24, 'Arms' = 25, 'Legs' = 26, 'Torso' = 27, 'RightArm' = 28, 'LeftArm' = 29, 'LeftLeg' = 30, 'RightLeg' = 31, 'Package' = 32, 'YouTubeVideo' = 33, 'GamePass' = 34, 'App' = 35, 'Code' = 37, 'Plugin' = 38, 'SolidModel' = 39, 'MeshPart' = 40, 'HairAccessory' = 41, 'FaceAccessory' = 42, 'NeckAccessory' = 43, 'ShoulderAccessory' = 44, 'FrontAccessory' = 45, 'BackAccessory' = 46, 'WaistAccessory' = 47, 'ClimbAnimation' = 48, 'DeathAnimation' = 49, 'FallAnimation' = 50, 'IdleAnimation' = 51, 'JumpAnimation' = 52, 'RunAnimation' = 53, 'SwimAnimation' = 54, 'WalkAnimation' = 55, 'PoseAnimation' = 56, 'LocalizationTableManifest' = 59, 'LocalizationTableTranslation' = 60, 'EmoteAnimation' = 61, 'Video' = 62, 'TexturePack' = 63, 'TShirtAccessory' = 64, 'ShirtAccessory' = 65, 'PantsAccessory' = 66, 'JacketAccessory' = 67, 'SweaterAccessory' = 68, 'ShortsAccessory' = 69, 'LeftShoeAccessory' = 70, 'RightShoeAccessory' = 71, 'DressSkirtAccessory' = 72, 'FontFamily' = 73, 'FontFace' = 74, 'MeshHiddenSurfaceRemoval' = 75, 'EyebrowAccessory' = 76, 'EyelashAccessory' = 77, 'MoodAnimation' = 78, 'DynamicHead' = 79, 'CodeSnippet' = 80, 'AdsVideo' = 81, 'OtaUpdate' = 82, 'Screenshot' = 83, 'RuntimePropertySet' = 84, 'StorePreviewVideo' = 85, 'GamePreviewVideo' = 86, 'CreatorExperienceConfig' = 87, 'FaceMakeup' = 88, 'LipMakeup' = 89, 'EyeMakeup' = 90, 'VoxelFragment' = 91, 'AvatarBackground' = 92, 'TextDocument' = 93, 'Post' = 94, 'AnimatedImage' = 95, 'ComputeFunction' = 96] Values: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 16, 17, 18, 19, 21, 22, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96 |
| `created` | `string` | No | The created date time of the user asset. |

### Roblox.Web.Responses.RelatedEntityTypeResponse[Roblox.Users.Client.AssociatedEntityType]

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | `integer` | No |  |
| `type` | `1 \| 2` | No | ['User' = 1, 'Group' = 2] |
| `name` | `string` | No |  |

### Roblox.Web.WebAPI.Models.ApiPageResponse[Roblox.Inventory.Api.Models.InventoryItemModel]

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `previousPageCursor` | `string` | No |  |
| `nextPageCursor` | `string` | No |  |
| `data` | `Roblox.Inventory.Api.Models.InventoryItemModel[]` | No |  |

### Roblox.Web.WebAPI.Models.ApiPageResponse[Roblox.Inventory.Api.V2.AssetOwnerResponse]

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `previousPageCursor` | `string` | No |  |
| `nextPageCursor` | `string` | No |  |
| `data` | `Roblox.Inventory.Api.V2.AssetOwnerResponse[]` | No |  |

### Roblox.Web.WebAPI.Models.ApiPageResponse[Roblox.Inventory.Api.V2.CollectibleItemOwnerResponse]

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `previousPageCursor` | `string` | No |  |
| `nextPageCursor` | `string` | No |  |
| `data` | `Roblox.Inventory.Api.V2.CollectibleItemOwnerResponse[]` | No |  |

### Roblox.Web.WebAPI.Models.ApiPageResponse[Roblox.Inventory.Api.V2.UserAssetItemModelV2]

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `previousPageCursor` | `string` | No |  |
| `nextPageCursor` | `string` | No |  |
| `data` | `Roblox.Inventory.Api.V2.UserAssetItemModelV2[]` | No |  |

## V1

### GET `/v1/packages/{packageId}/assets` *(deprecated)*

Given a package ID, returns the list of asset IDs for that package

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `packageID` | path | `integer (int64)` | Yes | The asset ID of the package |

**Responses:**

- `200`: OK → `Roblox.Inventory.Api.Models.AssetIdListModel`

**Response fields** (`Roblox.Inventory.Api.Models.AssetIdListModel`)

See [Roblox.Inventory.Api.Models.AssetIdListModel](#roblox-inventory-api-models-assetidlistmodel) in Models.

**Response example:**
```json
{
  "assetIds": [
    0
  ]
}
```

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://inventory.roblox.com/v1/packages/{packageId}/assets"
```

### GET `/v1/users/{userId}/assets/collectibles`

Gets all collectible assets owned by the specified user.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer (int64)` | Yes | The userid of the owner of the collectibles. |
| `assetType` | query | `integer (int32)` | No | The asset type for the collectibles you're trying to get. Valid values: `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `13`, `16`, `17`, `18`, `19`, `21`, `22`, `24`, `25`, `26`, `27`, `28`, `29`, `30`, `31`, `32`, `33`, `34`, `35`, `37`, `38`, `39`, `40`, `41`, `42`, `43`, `44`, `45`, `46`, `47`, `48`, `49`, `50`, `51`, `52`, `53`, `54`, `55`, `56`, `59`, `60`, `61`, `62`, `63`, `64`, `65`, `66`, `67`, `68`, `69`, `70`, `71`, `72`, `73`, `74`, `75`, `76`, `77`, `78`, `79`, `80`, `81`, `82`, `83`, `84`, `85`, `86`, `87`, `88`, `89`, `90`, `91`, `92`, `93`, `94`, `95`, `96` |
| `limit` | query | `integer (int32)` | No | The number of results per request. Valid values: `10`, `25`, `50`, `100` |
| `cursor` | query | `string` | No | The paging cursor for the previous or next page. |
| `sortOrder` | query | `string` | No | Sorted by userAssetId Valid values: `Asc`, `Desc` |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiPageResponse[Roblox.Inventory.Api.Models.CollectibleUserAssetModel]`
- `400`: The specified asset type(s) are invalid.
- `403`: The specified user's inventory is hidden.

**Response fields** (`Roblox.Web.WebAPI.Models.ApiPageResponse[Roblox.Inventory.Api.Models.CollectibleUserAssetModel]`)

See [Roblox.Web.WebAPI.Models.ApiPageResponse[Roblox.Inventory.Api.Models.CollectibleUserAssetModel]](#roblox-web-webapi-models-apipageresponse-roblox-inventory-api-models-collectibleuserassetmodel-) in Models.

**Response example:**
```json
{
  "previousPageCursor": "string",
  "nextPageCursor": "string",
  "data": [
    {
      "userAssetId": "...",
      "serialNumber": "...",
      "assetId": "...",
      "name": "...",
      "recentAveragePrice": "...",
      "originalPrice": "..."
    }
  ]
}
```

**Error handling:** `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://inventory.roblox.com/v1/users/{USERID}/assets/collectibles"
```

### GET `/v1/users/{userId}/can-view-inventory`

Gets whether the specified user's inventory can be viewed.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer (int64)` | Yes | The user identifier. |

**Responses:**

- `200`: OK → `Roblox.Inventory.Api.Models.CanViewInventoryResponse`
- `400`: 1: The specified user does not exist!

**Response fields** (`Roblox.Inventory.Api.Models.CanViewInventoryResponse`)

See [Roblox.Inventory.Api.Models.CanViewInventoryResponse](#roblox-inventory-api-models-canviewinventoryresponse) in Models.

**Response example:**
```json
{
  "canView": false
}
```

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://inventory.roblox.com/v1/users/{USERID}/can-view-inventory"
```

### GET `/v1/users/{userId}/categories`

Return inventory categories for a user

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer (int64)` | Yes |  |

**Responses:**

- `200`: OK → `Roblox.Inventory.Api.Models.CategoriesModel`

**Response fields** (`Roblox.Inventory.Api.Models.CategoriesModel`)

See [Roblox.Inventory.Api.Models.CategoriesModel](#roblox-inventory-api-models-categoriesmodel) in Models.

**Response example:**
```json
{
  "categories": [
    {
      "name": "...",
      "displayName": "...",
      "categoryType": "...",
      "items": "..."
    }
  ]
}
```

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://inventory.roblox.com/v1/users/{USERID}/categories"
```

### GET `/v1/users/{userId}/categories/favorites`

Return favorites categories for a user

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer (int64)` | Yes |  |

**Responses:**

- `200`: OK → `Roblox.Inventory.Api.Models.CategoriesModel`

**Response fields** (`Roblox.Inventory.Api.Models.CategoriesModel`)

See [Roblox.Inventory.Api.Models.CategoriesModel](#roblox-inventory-api-models-categoriesmodel) in Models.

**Response example:**
```json
{
  "categories": [
    {
      "name": "...",
      "displayName": "...",
      "categoryType": "...",
      "items": "..."
    }
  ]
}
```

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://inventory.roblox.com/v1/users/{USERID}/categories/favorites"
```

### GET `/v1/users/{userId}/items/{itemType}/{itemTargetId}`

Gets owned items of the specified item type. Game Servers can make requests for any user, but can only make requests for game passes that belong to the place sending the request.
Place creators can make requests as if they were the Game Server.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer (int64)` | Yes | ID of the user in question |
| `itemType` | path | `integer (int32)` | Yes | Type of the item in question (i.e. Asset, GamePass, Badge, Bundle) Valid values: `0`, `1`, `2`, `3`, `4` |
| `itemTargetId` | path | `integer (int64)` | Yes | ID of the item in question |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiPageResponse[Roblox.Inventory.Api.Models.IItemModel]`
- `400`: 1: The specified user does not exist! 5: The specified game pass does not exist! Are you using the new game pass ID? 6: The specified item type does not exist. 7: The specified Asset does not exist! 10: The specified asset is not a badge! 12: The specified bundle does not exist!

**Response fields** (`Roblox.Web.WebAPI.Models.ApiPageResponse[Roblox.Inventory.Api.Models.IItemModel]`)

See [Roblox.Web.WebAPI.Models.ApiPageResponse[Roblox.Inventory.Api.Models.IItemModel]](#roblox-web-webapi-models-apipageresponse-roblox-inventory-api-models-iitemmodel-) in Models.

**Response example:**
```json
{
  "previousPageCursor": "string",
  "nextPageCursor": "string",
  "data": [
    {
      "id": "...",
      "name": "...",
      "type": "...",
      "instanceId": "..."
    }
  ]
}
```

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://inventory.roblox.com/v1/users/{USERID}/items/{ITEMTYPE}/{ITEMTARGETID}"
```

### GET `/v1/users/{userId}/items/{itemType}/{itemTargetId}/is-owned`

Gets whether a user owns an item of type itemType with id itemTargetId.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer (int64)` | Yes | ID of the user in question |
| `itemType` | path | `integer (int32)` | Yes | Type of the item in question (i.e. Asset, GamePass, Badge, Bundle) Valid values: `0`, `1`, `2`, `3`, `4` |
| `itemTargetId` | path | `integer (int64)` | Yes | ID of the item in question |

**Responses:**

- `200`: OK → `boolean`
- `400`: 1: The specified user does not exist! 5: The specified game pass does not exist! Are you using the new game pass ID? 6: The specified item type does not exist. 7: The specified Asset does not exist! 10: The specified asset is not a badge! 12: The specified bundle does not exist!

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://inventory.roblox.com/v1/users/{USERID}/items/{ITEMTYPE}/{ITEMTARGETID}/is-owned"
```

### GET `/v1/users/{userId}/places/inventory`

Gets Created, MyGames, or OtherGames places inventory for a user

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer (int64)` | Yes |  |
| `placesTab` | query | `integer (int32)` | Yes | Valid values: `0`, `1`, `2`, `3`, `4`, `5` |
| `itemsPerPage` | query | `integer (int32)` | Yes |  |
| `cursor` | query | `integer (int32)` | Yes |  |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiPageResponse[Roblox.Inventory.Api.Models.PlaceModel]`
- `400`: 6: Invalid request
- `403`: 3: Insufficient permission.

**Response fields** (`Roblox.Web.WebAPI.Models.ApiPageResponse[Roblox.Inventory.Api.Models.PlaceModel]`)

See [Roblox.Web.WebAPI.Models.ApiPageResponse[Roblox.Inventory.Api.Models.PlaceModel]](#roblox-web-webapi-models-apipageresponse-roblox-inventory-api-models-placemodel-) in Models.

**Response example:**
```json
{
  "previousPageCursor": "string",
  "nextPageCursor": "string",
  "data": [
    {
      "universeId": "...",
      "placeId": "...",
      "name": "...",
      "creator": "...",
      "priceInRobux": "..."
    }
  ]
}
```

**Error handling:** `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://inventory.roblox.com/v1/users/{USERID}/places/inventory?placesTab={VALUE}&itemsPerPage={VALUE}&cursor={VALUE}"
```

### POST `/v1/collections/items/{itemType}/{itemTargetId}`

Adds an item to the appropriate collection

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `itemType` | path | `integer (int32)` | Yes | Type of the item (i.e. Asset, Bundle) Valid values: `0`, `1`, `2`, `3` |
| `itemTargetId` | path | `integer (int64)` | Yes | ID of the item |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: 1: The item type does not exist. 2: The asset does not exist. 3: The bundle does not exist.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 4: You don't own the specified item. 5: Assets of this type are not allowed in collections. 6: Items of this type are not allowed in collections. 7: The item is already in the collection. 9: The collection is full.

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://inventory.roblox.com/v1/collections/items/{ITEMTYPE}/{ITEMTARGETID}"
```

### DELETE `/v1/collections/items/{itemType}/{itemTargetId}`

Removes an item to the appropriate collection

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `itemType` | path | `integer (int32)` | Yes | Type of the item (i.e. Asset, Bundle) Valid values: `0`, `1`, `2`, `3` |
| `itemTargetId` | path | `integer (int64)` | Yes | ID of the item |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: 1: The item type does not exist. 2: The asset does not exist. 3: The bundle does not exist.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 8: The item is not in the collection.

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X DELETE -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://inventory.roblox.com/v1/collections/items/{ITEMTYPE}/{ITEMTARGETID}"
```

## Models

### Roblox.Inventory.Api.Models.AssetIdListModel

A model that contains a list of asset ids

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `assetIds` | `integer[]` | No | The asset ids |

### Roblox.Inventory.Api.Models.AssetsExplorerCategoryItemModel

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | `string` | No |  |
| `displayName` | `string` | No |  |
| `filter` | `string` | No |  |
| `id` | `integer` | No |  |
| `type` | `0 \| 1 \| 2 \| 3 \| 4` | No | Describes what type an AssetsExplorerCategoryItemModel contains ['AssetType' = 0, 'Bundle' = 1, 'Outfit' = 2, 'Set' = 3, 'Avatar' = 4] |
| `categoryType` | `string` | No |  |

### Roblox.Inventory.Api.Models.AssetsExplorerCategoryModel

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | `string` | No |  |
| `displayName` | `string` | No |  |
| `categoryType` | `string` | No |  |
| `items` | `Roblox.Inventory.Api.Models.AssetsExplorerCategoryItemModel[]` | No |  |

### Roblox.Inventory.Api.Models.CanViewInventoryResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `canView` | `boolean` | No | Boolean describing if the user's inventory can be viewed |

### Roblox.Inventory.Api.Models.CategoriesModel

Model class that contains the categories of the Inventory or Favorites page

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `categories` | `Roblox.Inventory.Api.Models.AssetsExplorerCategoryModel[]` | No | Categories to show up in Inventory or Favorites page |

### Roblox.Inventory.Api.Models.CollectibleUserAssetModel

A model containing information about a Roblox.Platform.AssetOwnership.UserAsset

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `userAssetId` | `integer` | No | The user asset id |
| `serialNumber` | `integer` | No | The serial number of the user asset |
| `assetId` | `integer` | No | The asset id of the user asset |
| `name` | `string` | No | The asset name of the asset |
| `recentAveragePrice` | `integer` | No | The recent average price of the asset |
| `originalPrice` | `integer` | No | The original price of the asset |
| `assetStock` | `integer` | No | The recent average price of the user asset |
| `buildersClubMembershipType` | `0 \| 1 \| 2 \| 3 \| 4` | No | The recent average price of the user asset ['None' = 0, 'BC' = 1, 'TBC' = 2, 'OBC' = 3, 'RobloxPremium' = 4] |
| `isOnHold` | `boolean` | No | Whether the user asset has an active hold. |

### Roblox.Inventory.Api.Models.CreatorModel

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | `integer` | No |  |
| `name` | `string` | No |  |
| `type` | `1 \| 2 \| 3` | No | ['User' = 1, 'Group' = 2, 'Experience' = 3] |

### Roblox.Inventory.Api.Models.IItemModel

Model representing an inventory item

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | `integer` | No | The ID of the item |
| `name` | `string` | No | The name of the item |
| `type` | `0 \| 1 \| 2 \| 3 \| 4` | No | The type of the item ['Asset' = 0, 'GamePass' = 1, 'Badge' = 2, 'Bundle' = 3, 'Avatar' = 4] |
| `instanceId` | `integer` | No | The instance id of the item if applicable |

### Roblox.Inventory.Api.Models.PlaceModel

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `universeId` | `integer` | No |  |
| `placeId` | `integer` | No |  |
| `name` | `string` | No |  |
| `creator` | `Roblox.Inventory.Api.Models.CreatorModel` | No |  |
| `priceInRobux` | `integer` | No |  |

### Roblox.Web.WebAPI.Models.ApiPageResponse[Roblox.Inventory.Api.Models.CollectibleUserAssetModel]

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `previousPageCursor` | `string` | No |  |
| `nextPageCursor` | `string` | No |  |
| `data` | `Roblox.Inventory.Api.Models.CollectibleUserAssetModel[]` | No |  |

### Roblox.Web.WebAPI.Models.ApiPageResponse[Roblox.Inventory.Api.Models.IItemModel]

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `previousPageCursor` | `string` | No |  |
| `nextPageCursor` | `string` | No |  |
| `data` | `Roblox.Inventory.Api.Models.IItemModel[]` | No |  |

### Roblox.Web.WebAPI.Models.ApiPageResponse[Roblox.Inventory.Api.Models.PlaceModel]

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `previousPageCursor` | `string` | No |  |
| `nextPageCursor` | `string` | No |  |
| `data` | `Roblox.Inventory.Api.Models.PlaceModel[]` | No |  |