---
name: "Inventories"
last_updated: 2026-10-30T19:56:08Z
type: feature
api_base_url: "https://apis.roblox.com"
endpoints: 9
auth: [api-key, oauth2, cookie]
description: "Access user inventories to verify ownership and display player collections"
---

# Inventories

Access user inventories to verify ownership and display player collections. For detailed implementation details, see the [Inventory guide](/cloud/guides/inventory).

You can [retrieve and check](#Cloud_ListInventoryItems) if a user owns specific items, like limiteds, badges, passes, or private servers.

> **Getting started:** See [User inventories](/docs/en-us/cloud/guides/inventory.md) for a complete walkthrough with working examples.

**Base URL:** `https://apis.roblox.com`

    ## Authentication

    Each endpoint requires one of the following authentication methods:

    - **API Key**: Pass your key in the `x-api-key` HTTP header. Create keys at [Creator Dashboard](https://create.roblox.com/dashboard/credentials).
- **OAuth 2.0**: Use Bearer token in the `Authorization` header. Authorization URL: `https://apis.roblox.com/oauth/v1/authorize`, Token URL: `https://apis.roblox.com/oauth/v1/token`
- **Cookie** *(not recommended)*: `.ROBLOSECURITY` cookie. Do not use in production.

    ```
    # API Key example
    curl -H "x-api-key: YOUR_API_KEY" https://apis.roblox.com/...

    # OAuth 2.0 example
    curl -H "Authorization: Bearer YOUR_ACCESS_TOKEN" https://apis.roblox.com/...
    ```

## Endpoints

### GET `/cloud/v2/users/{user_id}/inventory-items` [BETA]

List Inventory Items

List the inventory items in a user's inventory.
            
The inventory items returned depend on the target user’s choice under
**Settings > Privacy > Who can see my inventory?**:
* If the user granted inventory visibility to "Everyone," then any API key
or OAuth2 token can be used to view the target’s inventory, no matter what
scopes it has or who created it.
* If the user has not granted inventory visibility to "Everyone":
  * Their inventory can still be viewed with an API key created by the
  target user with **Inventory: Read** permission.
  * Their inventory can still be viewed with an OAuth2 token if the target
  user authorizes an app requesting permissions for the
  `user.inventory-item:read` scope.

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `user.inventory-item:read`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `user_id` | path | `string` | Yes | The user ID. |
| `maxPageSize` | query | `integer` | No | The maximum number of inventory items to return. The service might return              fewer than this value. If unspecified, at most 10 inventory items are              returned. The maximum value is 100 and higher values are set to 100. |
| `pageToken` | query | `string` | No | A page token, received from a previous call, to retrieve a subsequent page.                           When paginating, all other parameters provided to the subsequent call must              match the call that provided the page token. |
| `filter` | query | `string` | No | This field may be set in order to filter the resources returned.                           See the              [filtering](/cloud/reference/patterns#list-inventory-items)              documentation for more information. |

**Responses:**

- `200`: OK → `ListInventoryItemsResponse`

**Response fields** (`ListInventoryItemsResponse`)

See [ListInventoryItemsResponse](#listinventoryitemsresponse) in Models.

**Response example:**
```json
{
  "inventoryItems": [
    {
      "path": "...",
      "assetDetails": "...",
      "badgeDetails": "...",
      "gamePassDetails": "...",
      "privateServerDetails": "...",
      "addTime": "..."
    }
  ],
  "nextPageToken": "string"
}
```

**Rate Limits:** perApiKeyOwner: 100/minute, perOauth2Authorization: 20/minute

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/cloud/v2/users/{USER_ID}/inventory-items"
```

### POST `/v1/collections/items/{itemType}/{itemTargetId}`

Adds an item to the appropriate collection

**Server:** `https://inventory.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `itemType` | path | `0 \| 1 \| 2 \| 3` | Yes | Type of the item (i.e. Asset, Bundle) Valid values: `0`, `1`, `2`, `3` |
| `itemTargetId` | path | `integer` | Yes | ID of the item |

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
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://inventory.roblox.com/v1/collections/items/{ITEMTYPE}/{ITEMTARGETID}"
```

### DELETE `/v1/collections/items/{itemType}/{itemTargetId}`

Removes an item to the appropriate collection

**Server:** `https://inventory.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `itemType` | path | `0 \| 1 \| 2 \| 3` | Yes | Type of the item (i.e. Asset, Bundle) Valid values: `0`, `1`, `2`, `3` |
| `itemTargetId` | path | `integer` | Yes | ID of the item |

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
curl -X DELETE -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://inventory.roblox.com/v1/collections/items/{ITEMTYPE}/{ITEMTARGETID}"
```

### GET `/v1/packages/{packageId}/assets` *(deprecated)*

Given a package ID, returns the list of asset IDs for that package

Packages have been migrated to bundles. Use catalog.roblox.com/v1/bundles/{bundleId}/details

**Server:** `https://inventory.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `packageID` | path | `integer` | Yes | The asset ID of the package |

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
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://inventory.roblox.com/v1/packages/{packageId}/assets"
```

### GET `/v1/users/{userId}/assets/collectibles`

Gets all collectible assets owned by the specified user.

**Server:** `https://inventory.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer` | Yes | The userid of the owner of the collectibles. |
| `assetType` | query | `integer enum (89 values)` | No | The asset type for the collectibles you're trying to get. Valid values: `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `13`, `16`, `17`, `18`, `19`, `21`, `22`, `24`, `25`, `26`, `27`, `28`, `29`, `30`, `31`, `32`, `33`, `34`, `35`, `37`, `38`, `39`, `40`, `41`, `42`, `43`, `44`, `45`, `46`, `47`, `48`, `49`, `50`, `51`, `52`, `53`, `54`, `55`, `56`, `59`, `60`, `61`, `62`, `63`, `64`, `65`, `66`, `67`, `68`, `69`, `70`, `71`, `72`, `73`, `74`, `75`, `76`, `77`, `78`, `79`, `80`, `81`, `82`, `83`, `84`, `85`, `86`, `87`, `88`, `89`, `90`, `91`, `92`, `93`, `94`, `95`, `96` |
| `limit` | query | `10 \| 25 \| 50 \| 100` | No | The number of results per request. Valid values: `10`, `25`, `50`, `100` |
| `cursor` | query | `string` | No | The paging cursor for the previous or next page. |
| `sortOrder` | query | `Asc \| Desc` | No | Sorted by userAssetId Valid values: `Asc`, `Desc` |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.Inventory.Api.Models.CollectibleUserAssetModel_`
- `400`: The specified asset type(s) are invalid.
- `403`: The specified user's inventory is hidden.

**Response fields** (`Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.Inventory.Api.Models.CollectibleUserAssetModel_`)

See [Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.Inventory.Api.Models.CollectibleUserAssetModel_](#roblox-web-webapi-models-apipageresponse-roblox-inventory-api-models-collectibleuserassetmodel-) in Models.

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
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://inventory.roblox.com/v1/users/{USERID}/assets/collectibles"
```

### GET `/v1/users/{userId}/categories`

Return inventory categories for a user

**Server:** `https://inventory.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer` | Yes |  |

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
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://inventory.roblox.com/v1/users/{USERID}/categories"
```

### GET `/v1/users/{userId}/items/{itemType}/{itemTargetId}/is-owned`

Gets whether a user owns an item of type itemType with id itemTargetId.

**Server:** `https://inventory.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer` | Yes | ID of the user in question |
| `itemType` | path | `0 \| 1 \| 2 \| 3 \| 4` | Yes | Type of the item in question (i.e. Asset, GamePass, Badge, Bundle) Valid values: `0`, `1`, `2`, `3`, `4` |
| `itemTargetId` | path | `integer` | Yes | ID of the item in question |

**Responses:**

- `200`: OK → `boolean`
- `400`: 1: The specified user does not exist! 5: The specified game pass does not exist! Are you using the new game pass ID? 6: The specified item type does not exist. 7: The specified Asset does not exist! 10: The specified asset is not a badge! 12: The specified bundle does not exist!

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://inventory.roblox.com/v1/users/{USERID}/items/{ITEMTYPE}/{ITEMTARGETID}/is-owned"
```

### GET `/v1/users/{userId}/places/inventory`

Gets Created, MyGames, or OtherGames places inventory for a user

**Server:** `https://inventory.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer` | Yes |  |
| `placesTab` | query | `integer enum (6 values)` | Yes | Valid values: `0`, `1`, `2`, `3`, `4`, `5` |
| `itemsPerPage` | query | `integer` | Yes |  |
| `cursor` | query | `integer` | Yes |  |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.Inventory.Api.Models.PlaceModel_`
- `400`: 6: Invalid request
- `403`: 3: Insufficient permission.

**Response fields** (`Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.Inventory.Api.Models.PlaceModel_`)

See [Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.Inventory.Api.Models.PlaceModel_](#roblox-web-webapi-models-apipageresponse-roblox-inventory-api-models-placemodel-) in Models.

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
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://inventory.roblox.com/v1/users/{USERID}/places/inventory?placesTab={VALUE}&itemsPerPage={VALUE}&cursor={VALUE}"
```

### GET `/v2/users/{userId}/inventory/{assetTypeId}`

Gets user's inventory based on specific asset type

**Server:** `https://inventory.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer` | Yes | The user Id of the inventory owner |
| `assetTypeId` | path | `integer` | Yes | The asset type Id of the items to get |
| `limit` | query | `10 \| 25 \| 50 \| 100` | No | The number of results per request. Valid values: `10`, `25`, `50`, `100` |
| `cursor` | query | `string` | No | The paging cursor for the previous or next page. |
| `sortOrder` | query | `Asc \| Desc` | No | The order the results are sorted in. Valid values: `Asc`, `Desc` |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.Inventory.Api.Models.InventoryItemModel_`
- `400`: 1: Invalid user Id. 2: Invalid asset type Id.
- `403`: 3: Insufficient permission. 4: You are not authorized to view this user's inventory.

**Response fields** (`Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.Inventory.Api.Models.InventoryItemModel_`)

See [Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.Inventory.Api.Models.InventoryItemModel_](#roblox-web-webapi-models-apipageresponse-roblox-inventory-api-models-inventoryitemmodel-) in Models.

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
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://inventory.roblox.com/v2/users/{USERID}/inventory/{ASSETTYPEID}"
```

## Models

### ListInventoryItemsResponse

A list of InventoryItems in the parent collection.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `inventoryItems` | `InventoryItem[]` | No | The InventoryItems from the specified User. |
| `nextPageToken` | `string` | No | A token that you can send as a `pageToken` parameter to retrieve the next page. If this field is omitted, there are no subsequent pages. |

### Roblox.Inventory.Api.Models.AssetIdListModel

A model that contains a list of asset ids

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `assetIds` | `integer[]` | No | The asset ids |

### Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.Inventory.Api.Models.CollectibleUserAssetModel_

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `previousPageCursor` | `string` | No |  |
| `nextPageCursor` | `string` | No |  |
| `data` | `Roblox.Inventory.Api.Models.CollectibleUserAssetModel[]` | No |  |

### Roblox.Inventory.Api.Models.CategoriesModel

Model class that contains the categories of the Inventory or Favorites page

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `categories` | `Roblox.Inventory.Api.Models.AssetsExplorerCategoryModel[]` | No | Categories to show up in Inventory or Favorites page |

### Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.Inventory.Api.Models.PlaceModel_

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `previousPageCursor` | `string` | No |  |
| `nextPageCursor` | `string` | No |  |
| `data` | `Roblox.Inventory.Api.Models.PlaceModel[]` | No |  |

### Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.Inventory.Api.Models.InventoryItemModel_

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `previousPageCursor` | `string` | No |  |
| `nextPageCursor` | `string` | No |  |
| `data` | `Roblox.Inventory.Api.Models.InventoryItemModel[]` | No |  |