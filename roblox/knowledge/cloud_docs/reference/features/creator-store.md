---
name: "Creator Store"
last_updated: 2026-10-30T19:56:08Z
type: feature
api_base_url: "https://apis.roblox.com"
endpoints: 8
auth: [api-key, oauth2, cookie]
description: "Manage your presence on the [Creator Store](/production/creator-store)"
---

# Creator Store

Manage your presence on the [Creator Store](/production/creator-store). [Create](#Cloud_CreateCreatorStoreProduct) and [update](#Cloud_UpdateCreatorStoreProduct) product listings for your assets, and [search the toolbox](#Toolbox_SearchCreatorStoreAssets) for assets using various filters.

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

### POST `/cloud/v2/creator-store-products` [BETA]

Create Creator Store Product

Add a Creator Store product. Only use this method if your product has never
been distributed on the Creator Store; otherwise, use the `PATCH` method to
update the product.

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `creator-store-product:write`, `creator-store-product:write`

**Request Body:** `application/json` — Type: `CreatorStoreProduct`

See [CreatorStoreProduct](#creatorstoreproduct) in Models.

**Request example:**
```json
{
  "path": "string",
  "basePrice": {
    "currencyCode": "string",
    "quantity": {
      "significand": "...",
      "exponent": "..."
    }
  },
  "purchasePrice": {
    "currencyCode": "string",
    "quantity": {
      "significand": "...",
      "exponent": "..."
    }
  },
  "published": false,
  "restrictions": [
    "RESTRICTION_UNSPECIFIED"
  ],
  "purchasable": false
}
```

**Responses:**

- `200`: OK → `CreatorStoreProduct`

**Response fields** (`CreatorStoreProduct`)

See [CreatorStoreProduct](#creatorstoreproduct) in Models.

**Response example:**
```json
{
  "path": "string",
  "basePrice": {
    "currencyCode": "string",
    "quantity": {
      "significand": "...",
      "exponent": "..."
    }
  },
  "purchasePrice": {
    "currencyCode": "string",
    "quantity": {
      "significand": "...",
      "exponent": "..."
    }
  },
  "published": false,
  "restrictions": [
    "RESTRICTION_UNSPECIFIED"
  ],
  "purchasable": false
}
```

**Rate Limits:** perApiKeyOwner: 30/minute, perOauth2Authorization: 30/minute

**Example:**
```bash
curl -X POST -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/cloud/v2/creator-store-products" \
  -H "Content-Type: application/json" \
  -d '{"path":"string","basePrice":{"currencyCode":"string","quantity":{"significand":"...","exponent":"..."}},"purchasePrice":{"currencyCode":"string","quantity":{"significand":"...","exponent":"..."}},"published":false,"restrictions":["RESTRICTION_UNSPECIFIED"],"purchasable":false}'
```

### GET `/cloud/v2/creator-store-products/{creator_store_product_id}` [BETA]

Get Creator Store Product

Get a Creator Store product.

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `creator-store-product:read`, `creator-store-product:read`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `creator_store_product_id` | path | `string` | Yes | The creator-store-product ID. |

**Responses:**

- `200`: OK → `CreatorStoreProduct`

**Response fields** (`CreatorStoreProduct`)

See [CreatorStoreProduct](#creatorstoreproduct) in Models.

**Response example:**
```json
{
  "path": "string",
  "basePrice": {
    "currencyCode": "string",
    "quantity": {
      "significand": "...",
      "exponent": "..."
    }
  },
  "purchasePrice": {
    "currencyCode": "string",
    "quantity": {
      "significand": "...",
      "exponent": "..."
    }
  },
  "published": false,
  "restrictions": [
    "RESTRICTION_UNSPECIFIED"
  ],
  "purchasable": false
}
```

**Rate Limits:** perApiKeyOwner: 30/minute, perOauth2Authorization: 30/minute

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/cloud/v2/creator-store-products/{CREATOR_STORE_PRODUCT_ID}"
```

### PATCH `/cloud/v2/creator-store-products/{creator_store_product_id}` [BETA]

Update Creator Store Product

Update a Creator Store product.

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `creator-store-product:write`, `creator-store-product:write`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `creator_store_product_id` | path | `string` | Yes | The creator-store-product ID. |
| `updateMask` | query | `string` | No | The list of fields to update. |
| `allowMissing` | query | `boolean` | No | If set to true, and the creator store product is not found, a creator store product is created. In this situation, `update_mask` is ignored. |

**Request Body:** `application/json` — Type: `CreatorStoreProduct`

See [CreatorStoreProduct](#creatorstoreproduct) in Models.

**Request example:**
```json
{
  "path": "string",
  "basePrice": {
    "currencyCode": "string",
    "quantity": {
      "significand": "...",
      "exponent": "..."
    }
  },
  "purchasePrice": {
    "currencyCode": "string",
    "quantity": {
      "significand": "...",
      "exponent": "..."
    }
  },
  "published": false,
  "restrictions": [
    "RESTRICTION_UNSPECIFIED"
  ],
  "purchasable": false
}
```

**Responses:**

- `200`: OK → `CreatorStoreProduct`

**Response fields** (`CreatorStoreProduct`)

See [CreatorStoreProduct](#creatorstoreproduct) in Models.

**Response example:**
```json
{
  "path": "string",
  "basePrice": {
    "currencyCode": "string",
    "quantity": {
      "significand": "...",
      "exponent": "..."
    }
  },
  "purchasePrice": {
    "currencyCode": "string",
    "quantity": {
      "significand": "...",
      "exponent": "..."
    }
  },
  "published": false,
  "restrictions": [
    "RESTRICTION_UNSPECIFIED"
  ],
  "purchasable": false
}
```

**Rate Limits:** perApiKeyOwner: 30/minute, perOauth2Authorization: 30/minute

**Example:**
```bash
curl -X PATCH -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/cloud/v2/creator-store-products/{CREATOR_STORE_PRODUCT_ID}" \
  -H "Content-Type: application/json" \
  -d '{"path":"string","basePrice":{"currencyCode":"string","quantity":{"significand":"...","exponent":"..."}},"purchasePrice":{"currencyCode":"string","quantity":{"significand":"...","exponent":"..."}},"published":false,"restrictions":["RESTRICTION_UNSPECIFIED"],"purchasable":false}'
```

### GET `/toolbox-service/v1/saves` [BETA]

Gets saves from a collection.

**Auth:** Cookie (`.ROBLOSECURITY`) or API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `creator-store-save:read`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `targetType` | query | `any` | No | The asset type to filter by |
| `targetId` | query | `integer` | No | The ID of the asset to filter by. If provided, targetType must also be provided. |
| `collectionName` | query | `string` | No | Custom collections are not currently supported. This field should be omitted. |
| `sortBy` | query | `any` | No | The field to sort by |
| `sortDirection` | query | `any` | No | The direction to sort by |
| `limit` | query | `integer` | No | The maximum number of saves to return |
| `page` | query | `integer` | No | The page number to return, starting from 1 |
| `keyword` | query | `string` | No | The keyword to filter by |
| `hideOwnedAssets` | query | `boolean` | No | Whether to hide owned assets |

**Responses:**

- `200`: OK → `GetSavesResponse`
- `400`: Bad Request → `any`

**Response fields** (`GetSavesResponse`)

See [GetSavesResponse](#getsavesresponse) in Models.

**Response example:**
```json
{
  "totalCount": 0,
  "saves": [
    {
      "owned": "...",
      "dateSaved": "...",
      "creatorStoreAsset": "..."
    }
  ]
}
```

**Rate Limits:** perApiKeyOwner: 200/minute, perOauth2Authorization: 200/minute

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/toolbox-service/v1/saves"
```

### POST `/toolbox-service/v1/saves` [BETA]

Creates a save.

**Auth:** Cookie (`.ROBLOSECURITY`) or API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `creator-store-save:write`

**Request Body:** `application/json-patch+json` — Type: `CreateSaveRequest`

See [CreateSaveRequest](#createsaverequest) in Models.

**Request example:**
```json
{
  "targetType": "...",
  "targetId": 0,
  "collectionName": "string"
}
```

**Responses:**

- `201`: Created
- `400`: Bad Request → `any`
- `404`: Not Found → `any`
- `409`: Conflict → `any`

**Rate Limits:** perApiKeyOwner: 200/minute, perOauth2Authorization: 200/minute

**Example:**
```bash
curl -X POST -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/toolbox-service/v1/saves" \
  -H "Content-Type: application/json" \
  -d '{
  "targetType": "...",
  "targetId": 0,
  "collectionName": "string"
}'
```

### DELETE `/toolbox-service/v1/saves` [BETA]

Deletes a save.

**Auth:** Cookie (`.ROBLOSECURITY`) or API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `creator-store-save:write`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `targetType` | query | `any` | No | The type of asset being deleted |
| `targetId` | query | `integer` | No | The ID of the asset being deleted |
| `collectionName` | query | `string` | No | Custom collections are not currently supported. This field should be omitted. |

**Responses:**

- `204`: No Content
- `400`: Bad Request → `any`
- `404`: Not Found → `any`

**Rate Limits:** perApiKeyOwner: 200/minute, perOauth2Authorization: 200/minute

**Example:**
```bash
curl -X DELETE -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/toolbox-service/v1/saves"
```

### POST `/toolbox-service/v1/saves:bulkDelete` [BETA]

Bulk deletes saves.
Max of 5000 saves per request.

**Auth:** Cookie (`.ROBLOSECURITY`) or API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `creator-store-save:write`

**Request Body:** `application/json-patch+json` — Type: `BulkDeleteSavesRequest`

See [BulkDeleteSavesRequest](#bulkdeletesavesrequest) in Models.

**Request example:**
```json
{
  "targets": [
    {
      "targetType": "...",
      "targetId": "...",
      "collectionName": "..."
    }
  ]
}
```

**Responses:**

- `200`: OK → `BulkDeleteSavesResponse`
- `400`: Bad Request → `any`
- `404`: Not Found → `any`

**Response fields** (`BulkDeleteSavesResponse`)

See [BulkDeleteSavesResponse](#bulkdeletesavesresponse) in Models.

**Response example:**
```json
{
  "deletedCount": 0
}
```

**Rate Limits:** perApiKeyOwner: 200/minute, perOauth2Authorization: 200/minute

**Example:**
```bash
curl -X POST -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/toolbox-service/v1/saves:bulkDelete" \
  -H "Content-Type: application/json" \
  -d '{
  "targets": [
    {
      "targetType": "...",
      "targetId": "...",
      "collectionName": "..."
    }
  ]
}'
```

### POST `/toolbox-service/v2/assets:search` [BETA]

Search Creator Store Assets

Search Creator Store for assets.

**Auth:** Cookie (`.ROBLOSECURITY`) or API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `creator-store-product:read`

**Request Body:** `application/json-patch+json` — Type: `SearchCreatorStoreAssetsRequest`

See [SearchCreatorStoreAssetsRequest](#searchcreatorstoreassetsrequest) in Models.

**Request example:**
```json
{
  "searchCategoryType": "...",
  "query": "string",
  "image": "string",
  "userId": 0,
  "groupId": 0,
  "pageToken": "string"
}
```

**Responses:**

- `200`: OK → `SearchCreatorStoreAssetsResponse`
- `400`: Bad Request → `any`
- `429`: Too Many Requests → `any`
- `500`: Internal Server Error

**Response fields** (`SearchCreatorStoreAssetsResponse`)

See [SearchCreatorStoreAssetsResponse](#searchcreatorstoreassetsresponse) in Models.

**Response example:**
```json
{
  "nextPageToken": "string",
  "queryFacets": "...",
  "creatorStoreAssets": [
    {
      "voting": "...",
      "creator": "...",
      "creatorStoreProduct": "...",
      "asset": "..."
    }
  ],
  "totalResults": 0,
  "queryCorrection": "...",
  "filteredKeyword": "string"
}
```

**Error handling:** `429`: Retry with exponential backoff (start at 1s). 

**Rate Limits:** perApiKeyOwner: 1000/minute, perOauth2Authorization: 1000/minute

**Example:**
```bash
curl -X POST -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/toolbox-service/v2/assets:search" \
  -H "Content-Type: application/json" \
  -d '{
  "searchCategoryType": "...",
  "query": "string",
  "image": "string",
  "userId": 0,
  "groupId": 0,
  "pageToken": "string"
}'
```

## Models

### CreatorStoreProduct

Represents a product in the Creator Store. This resource is used to manage
distribution and pricing of assets on the Creator Store.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `path` | `string` | No | The resource path of the creator store product.  Format: `creator-store-products/{creator_store_product_id}` |
| `basePrice` | `Money` | No | The base price of the product. For more information, see [Money](/cloud/reference/types.md#money). Each product type (such as `pluginAssetId`) supports a set of specific prices. Currently, only setting a base price in USD is supported.  Depending on type, each Creator Store product has a fixed set of supported prices; see the `productType` attribute for the full list. For example, to set the price of a plugin to $4.99, use the following base price: ``` "basePrice": {   "currencyCode": "USD",   "quantity": {     "significand": 4990000000,     "exponent": -9   } } ```  Note: The exponent **must** be -9, and the significand must be in this format. The corresponding [Decimal](/cloud/reference/types.md#decimal) format is `significand * 10^exponent`.  If you want to set the price of a plugin to $0 (i.e. free), use the following `base_price`  ``` "basePrice": {   "currencyCode": "USD",   "quantity": {     "significand": 0,     "exponent": 0   } } ```  Note: You must still set the `currencyCode` to USD, even for free products.  The actual purchase price is based on this base price, but often differs slightly due to locale-specific considerations.  Set this to zero to make the product free. |
| `purchasePrice` | `Money` | No | The effective purchase price for the user, after factoring in locale-specific considerations. |
| `published` | `boolean` | No | Whether the seller intends to distribute the Creator Store product on the Creator Store. A seller might intend to distribute a product, but due to some restrictions on the seller or underlying Creator Store product, the product may not be available for purchase. See `restrictions` and `purchasable` for more details. |
| `restrictions` | `RESTRICTION_UNSPECIFIED \| SOLD_ITEM_RESTRICTED \| SELLER_TEMPORARILY_RESTRICTED \| SELLER_PERMANENTLY_RESTRICTED \| SELLER_NO_LONGER_ACTIVE[]` | No | Restrictions applied to the product. A product can have multiple restrictions active at one time.  Possible values:    \| Value \| Description \|   \| --- \| --- \|   \| RESTRICTION_UNSPECIFIED \| Unspecified restriction. \|   \| SOLD_ITEM_RESTRICTED \| The item being sold has been restricted by Roblox  Details may be available by looking up that item directly. \|   \| SELLER_TEMPORARILY_RESTRICTED \| The product is restricted because the seller's account is temporarily restricted by Roblox. \|   \| SELLER_PERMANENTLY_RESTRICTED \| The product is restricted because the seller's account is permanently restricted by Roblox. \|   \| SELLER_NO_LONGER_ACTIVE \| The product is restricted because the seller's account was deleted or is otherwise no longer active. \| |
| `purchasable` | `boolean` | No | Whether the product is purchasable.  For this value to be true, `published` must be true and `restrictions` must be empty. If this value is false, the product may not be acquired by any user. |
| `userSeller` | `string` | No | The Roblox user selling the product. |
| `groupSeller` | `string` | No | The Roblox group selling the product. |
| `modelAssetId` | `string` | No |  *(immutable)* The Creator Store product is a model with this asset ID. |
| `pluginAssetId` | `string` | No |  *(immutable)* The Creator Store product is a plugin with this asset ID.  Supported base prices in USD: $0, $4.99, $5.99, $6.99, $7.99, $8.99, $9.99, $10.99, $11.99, $12.99, $13.99, $14.99, $15.99, $16.99, $17.99, $18.99, $19.99, $24.99, $29.99, $34.99, $39.99, $44.99, $49.99, $59.99, $69.99, $79.99, $89.99, $99.99, $149.99, $199.99, $249.99 |
| `audioAssetId` | `string` | No |  *(immutable)* The Creator Store product is an audio file with this asset ID. |
| `decalAssetId` | `string` | No |  *(immutable)* The Creator Store product is a decal with this asset ID. |
| `meshPartAssetId` | `string` | No |  *(immutable)* The Creator Store product is a mesh part with this asset ID. |
| `videoAssetId` | `string` | No |  *(immutable)* The Creator Store product is a video with this asset ID. |
| `fontFamilyAssetId` | `string` | No |  *(immutable)* The Creator Store product is a font family with this asset ID. |

### GetSavesResponse

Response model for getting saves

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `totalCount` | `integer` | Yes | The total number of saves that match the query. |
| `saves` | `HydratedSave[]` | Yes | Gets or sets the saves. |

### CreateSaveRequest

Request model for creating a save

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `targetType` | `any` | Yes | The type of asset being saved |
| `targetId` | `integer` | Yes | The ID of the asset being saved |
| `collectionName` | `string` | No | Custom collections are not currently supported. This field should be omitted. |

### BulkDeleteSavesRequest

Request model for bulk deleting saves

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `targets` | `DeleteSaveRequest[]` | Yes | A list of saves being deleted |

### BulkDeleteSavesResponse

Response model for bulk delete saves operation

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `deletedCount` | `integer` | No | Number of saves that were successfully deleted |

### SearchCreatorStoreAssetsRequest

Request model for searching Creator Store assets.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `searchCategoryType` | `any` | No | The asset type to search within. Optional when Toolbox.Service.SearchCreatorStoreAssetsRequest.CategoryPath resolves to an asset type; otherwise required. |
| `query` | `string` | No | The search terms used to filter the results. Only one of 'query' and 'image' can be present in a query. |
| `image` | `string` | No | The image file to search by. The image must be base64 encoded to be used in the search. Only one of 'query' and 'image' can be present in a query. |
| `userId` | `integer` | No | The User ID of the creator. Only one of 'userId' and 'groupId' can be present in a query. |
| `groupId` | `integer` | No | The Group ID of the creator. Only one of 'userId' and 'groupId' can be present in a query. |
| `pageToken` | `string` | No | The identifier for the desired search results page. Only one of 'pageNumber' and 'pageToken' can be present in a query. |
| `pageNumber` | `integer` | No | The page number to retrieve, starting from 0. Only one of 'pageNumber' and 'pageToken' can be present in a query. |
| `maxPageSize` | `integer` | No | The number of assets to be returned. Cannot be larger than 100. |
| `sortDirection` | `any` | No | The sort direction of the search results. |
| `sortCategory` | `any` | No | The category to sort the search results by. |
| `includeOnlyVerifiedCreators` | `boolean` | No | Whether the results should only include assets created by verified creators. |
| `minPriceCents` | `integer` | No | The minimum price of the asset in cents. If included, must be greater than or equal to 0. |
| `maxPriceCents` | `integer` | No | The maximum price of the asset in cents. If included, must be greater than or equal to 0. |
| `facets` | `string[]` | No | Additional keywords to query by. |
| `tags` | `string[]` | No | The tags to filter by. |
| `categoryPath` | `string` | No | The category path to filter by. |
| `swimlane` | `string` | No | Optional swimlane identifier (e.g. "trending", "essential", "priced"). |
| `searchView` | `any` | No | Indicates which fields will be populated in the response. |
| `audioSearchFilters` | `any` | No | Audio-specific search filters. |
| `modelSearchFilters` | `any` | No | Model-specific search filters. |

### SearchCreatorStoreAssetsResponse

The response for the SearchCreatorStoreAssets endpoint.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `nextPageToken` | `string` | No | The page token to view the next page of results. |
| `queryFacets` | `any` | No | The applied and available facets of a query. |
| `creatorStoreAssets` | `CreatorStoreAsset[]` | Yes | The list of creator store assets returned by the search query. |
| `totalResults` | `integer` | Yes | The total number of results for the given search query. |
| `queryCorrection` | `any` | No | Query correction information, if a correction was available for the search query. |
| `filteredKeyword` | `string` | No | The filtered keyword that was used to search for assets, if applicable. |