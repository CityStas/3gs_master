---
name: "ItemConfiguration Api v1"
last_updated: 2026-10-30T19:56:08Z
type: legacy
api_base_url: "https://itemconfiguration.roblox.com"
versions: [v1]
endpoints: 6
auth: [cookie]
---

# ItemConfiguration Api v1

> **Warning:** Legacy APIs with cookie authentication can incorporate breaking changes without notice. We don't recommend them for production applications.

**Base URL:** `https://itemconfiguration.roblox.com`
**Versions:** v1

## Endpoints

### GET `/v1/creations/get-assets`

Gets the user created asset information filtered by the given asset type.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `assetType` | query | `string` | Yes |  |
| `isArchived` | query | `boolean` | No |  |
| `groupId` | query | `integer (int64)` | No |  |
| `limit` | query | `integer (int32)` | No | The number of results per request. Valid values: `10`, `25`, `50`, `100` |
| `cursor` | query | `string` | No | The paging cursor for the previous or next page. |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiPageResponse[Roblox.ItemConfiguration.Api.AssetCreationsResponse]`
- `400`: 5: Invalid assetType 10: Invalid Asset Category
- `401`: 0: Authorization has been denied for this request.
- `403`: 7: User does not have necessary permissions for group 8: Asset type does not have necessary permissions for group
- `429`: 9: Flood Limit Exceeded
- `503`: 6: Service Unavailable

**Response fields** (`Roblox.Web.WebAPI.Models.ApiPageResponse[Roblox.ItemConfiguration.Api.AssetCreationsResponse]`)

See [Roblox.Web.WebAPI.Models.ApiPageResponse[Roblox.ItemConfiguration.Api.AssetCreationsResponse]](#roblox-web-webapi-models-apipageresponse-roblox-itemconfiguration-api-assetcreationsresponse-) in Models.

**Response example:**
```json
{
  "previousPageCursor": "string",
  "nextPageCursor": "string",
  "data": [
    {
      "assetId": "...",
      "name": "..."
    }
  ]
}
```

**Error handling:** `429`: Retry with exponential backoff (start at 1s). `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://itemconfiguration.roblox.com/v1/creations/get-assets?assetType={VALUE}"
```

### GET `/v1/preferences/publishing`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | query | `integer (int64)` | No |  |

**Responses:**

- `200`: OK → `Roblox.ItemConfiguration.Api.Models.Response.PublishingPreferences.PublishingPreferencesResponse`
- `401`: 0: Authorization has been denied for this request.

**Response fields** (`Roblox.ItemConfiguration.Api.Models.Response.PublishingPreferences.PublishingPreferencesResponse`)

See [Roblox.ItemConfiguration.Api.Models.Response.PublishingPreferences.PublishingPreferencesResponse](#roblox-itemconfiguration-api-models-response-publishingpreferences-publishingpreferencesresponse) in Models.

**Response example:**
```json
{
  "id": "string",
  "creatorUserId": 0,
  "creatorGroupId": 0,
  "publishingType": 0,
  "saleLocationType": 0,
  "places": [
    0
  ]
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://itemconfiguration.roblox.com/v1/preferences/publishing"
```

### POST `/v1/preferences/publishing`

**Request Body:** `application/json` — Type: `Roblox.ItemConfiguration.Api.Models.Request.PublishingPreferences.CreatePublishingPreferencesRequest`

See [Roblox.ItemConfiguration.Api.Models.Request.PublishingPreferences.CreatePublishingPreferencesRequest](#roblox-itemconfiguration-api-models-request-publishingpreferences-createpublishingpreferencesrequest) in Models.

**Request example:**
```json
{
  "creatorUserId": 0,
  "creatorGroupId": 0,
  "publishingType": 0,
  "saleLocationType": 0,
  "places": [
    0
  ],
  "priceInRobux": 0
}
```

**Responses:**

- `200`: OK → `Roblox.ItemConfiguration.Api.Models.Response.PublishingPreferences.PublishingPreferencesResponse`
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed

**Response fields** (`Roblox.ItemConfiguration.Api.Models.Response.PublishingPreferences.PublishingPreferencesResponse`)

See [Roblox.ItemConfiguration.Api.Models.Response.PublishingPreferences.PublishingPreferencesResponse](#roblox-itemconfiguration-api-models-response-publishingpreferences-publishingpreferencesresponse) in Models.

**Response example:**
```json
{
  "id": "string",
  "creatorUserId": 0,
  "creatorGroupId": 0,
  "publishingType": 0,
  "saleLocationType": 0,
  "places": [
    0
  ]
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://itemconfiguration.roblox.com/v1/preferences/publishing" \
  -H "Content-Type: application/json" \
  -d '{
  "creatorUserId": 0,
  "creatorGroupId": 0,
  "publishingType": 0,
  "saleLocationType": 0,
  "places": [
    0
  ],
  "priceInRobux": 0
}'
```

### PATCH `/v1/preferences/publishing`

**Request Body:** `application/json` — Type: `Roblox.ItemConfiguration.Api.Models.Request.PublishingPreferences.UpdatePublishingPreferencesRequest`

See [Roblox.ItemConfiguration.Api.Models.Request.PublishingPreferences.UpdatePublishingPreferencesRequest](#roblox-itemconfiguration-api-models-request-publishingpreferences-updatepublishingpreferencesrequest) in Models.

**Request example:**
```json
{
  "creatorUserId": 0,
  "creatorGroupId": 0,
  "publishingType": 0,
  "saleLocationType": 0,
  "places": [
    0
  ],
  "priceInRobux": 0
}
```

**Responses:**

- `200`: OK → `Roblox.ItemConfiguration.Api.Models.Response.PublishingPreferences.PublishingPreferencesResponse`
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed

**Response fields** (`Roblox.ItemConfiguration.Api.Models.Response.PublishingPreferences.PublishingPreferencesResponse`)

See [Roblox.ItemConfiguration.Api.Models.Response.PublishingPreferences.PublishingPreferencesResponse](#roblox-itemconfiguration-api-models-response-publishingpreferences-publishingpreferencesresponse) in Models.

**Response example:**
```json
{
  "id": "string",
  "creatorUserId": 0,
  "creatorGroupId": 0,
  "publishingType": 0,
  "saleLocationType": 0,
  "places": [
    0
  ]
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X PATCH -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://itemconfiguration.roblox.com/v1/preferences/publishing" \
  -H "Content-Type: application/json" \
  -d '{
  "creatorUserId": 0,
  "creatorGroupId": 0,
  "publishingType": 0,
  "saleLocationType": 0,
  "places": [
    0
  ],
  "priceInRobux": 0
}'
```

### DELETE `/v1/preferences/publishing`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | query | `integer (int64)` | No |  |

**Responses:**

- `200`: OK
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X DELETE -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://itemconfiguration.roblox.com/v1/preferences/publishing"
```

### POST `/v1/creations/get-asset-details`

Gets the asset status and other configuration details for the given assetIds list.

**Request Body:** `application/json` — Type: `Roblox.ItemConfiguration.Api.AssetCreationsDetailsRequest`

See [Roblox.ItemConfiguration.Api.AssetCreationsDetailsRequest](#roblox-itemconfiguration-api-assetcreationsdetailsrequest) in Models.

**Request example:**
```json
{
  "AssetIds": [
    0
  ]
}
```

**Responses:**

- `200`: OK → `Roblox.ItemConfiguration.Api.AssetCreationsDetailsResponse[]`
- `400`: 1: Missing AssetIds parameters 2: Invalid asset Ids
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed
- `414`: 3: Too many asset Ids
- `429`: 9: Flood Limit Exceeded
- `503`: 6: Service Unavailable

**Response fields** (`Roblox.ItemConfiguration.Api.AssetCreationsDetailsResponse[]`)

See [Roblox.ItemConfiguration.Api.AssetCreationsDetailsResponse](#roblox-itemconfiguration-api-assetcreationsdetailsresponse) in Models.

**Error handling:** `429`: Retry with exponential backoff (start at 1s). `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://itemconfiguration.roblox.com/v1/creations/get-asset-details" \
  -H "Content-Type: application/json" \
  -d '{
  "AssetIds": [
    0
  ]
}'
```

## Models

### Roblox.ItemConfiguration.Api.AssetCreationsDetailsRequest

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `AssetIds` | `integer[]` | No |  |

### Roblox.ItemConfiguration.Api.AssetCreationsDetailsResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `assetId` | `integer` | No | The asset Id. |
| `name` | `string` | No | The asset name. |
| `status` | `string enum (8 values)` | No | The asset status. ['Unknown' = 0, 'ReviewPending' = 1, 'Moderated' = 2, 'ReviewApproved' = 3, 'OnSale' = 4, 'OffSale' = 5, 'DelayedRelease' = 6, 'Free' = 7] Values: Unknown, ReviewPending, Moderated, ReviewApproved, OnSale, OffSale, DelayedRelease, Free |
| `description` | `string` | No | The asset description. |
| `creatorType` | `Unknown \| User \| Group` | No | The creator type. ['Unknown' = 0, 'User' = 1, 'Group' = 2] |
| `creatorTargetId` | `integer` | No | The creator target Id. |
| `isArchived` | `boolean` | No | Is the asset archived. |
| `assetType` | `string` | No | Type of the asset. |
| `created` | `string` | No | Date asset was created. |
| `updated` | `string` | No | Date asset was created. |

### Roblox.ItemConfiguration.Api.AssetCreationsResponse

Asset Status response model.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `assetId` | `integer` | No | The asset Id. |
| `name` | `string` | No | The asset name. |

### Roblox.ItemConfiguration.Api.Models.Request.PublishingPreferences.CreatePublishingPreferencesRequest

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `creatorUserId` | `integer` | No |  |
| `creatorGroupId` | `integer` | No |  |
| `publishingType` | `0 \| 1 \| 2` | No | Publishing type for the collectible. Currently can be either Limited or NonLimited. ['Invalid' = 0, 'Limited' = 1, 'NonLimited' = 2] |
| `saleLocationType` | `0 \| 1 \| 2 \| 3 \| 4` | No | Represents possible SaleLocation types of the Collectibles System. ['SALE_LOCATION_TYPE_INVALID' = 0, 'SALE_LOCATION_TYPE_SHOP_AND_ALL_EXPERIENCES' = 1, 'SALE_LOCATION_EXPERIENCES_AND_DEV_API_ONLY' = 2, 'SALE_LOCATION_TYPE_SHOP_ONLY' = 3, 'SALE_LOCATION_TYPE_SHOP_AND_EXPERIENCES_BY_ID' = 4] |
| `places` | `integer[]` | No |  |
| `priceInRobux` | `integer` | No |  |
| `priceOffset` | `integer` | No |  |
| `isFree` | `boolean` | No |  |
| `enableRegionalPricing` | `boolean` | No |  |
| `isRentalOptIn` | `boolean` | No |  |
| `autoPublishEnabled` | `boolean` | No |  |

### Roblox.ItemConfiguration.Api.Models.Request.PublishingPreferences.UpdatePublishingPreferencesRequest

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `creatorUserId` | `integer` | No |  |
| `creatorGroupId` | `integer` | No |  |
| `publishingType` | `0 \| 1 \| 2` | No |  |
| `saleLocationType` | `0 \| 1 \| 2 \| 3 \| 4` | No |  |
| `places` | `integer[]` | No |  |
| `priceInRobux` | `integer` | No |  |
| `priceOffset` | `integer` | No |  |
| `isFree` | `boolean` | No |  |
| `enableRegionalPricing` | `boolean` | No |  |
| `isRentalOptIn` | `boolean` | No |  |
| `autoPublishEnabled` | `boolean` | No |  |

### Roblox.ItemConfiguration.Api.Models.Response.PublishingPreferences.PublishingPreferencesResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | `string` | No |  |
| `creatorUserId` | `integer` | No |  |
| `creatorGroupId` | `integer` | No |  |
| `publishingType` | `0 \| 1 \| 2` | No | Publishing type for the collectible. Currently can be either Limited or NonLimited. ['Invalid' = 0, 'Limited' = 1, 'NonLimited' = 2] |
| `saleLocationType` | `0 \| 1 \| 2 \| 3 \| 4` | No | Represents possible SaleLocation types of the Collectibles System. ['SALE_LOCATION_TYPE_INVALID' = 0, 'SALE_LOCATION_TYPE_SHOP_AND_ALL_EXPERIENCES' = 1, 'SALE_LOCATION_EXPERIENCES_AND_DEV_API_ONLY' = 2, 'SALE_LOCATION_TYPE_SHOP_ONLY' = 3, 'SALE_LOCATION_TYPE_SHOP_AND_EXPERIENCES_BY_ID' = 4] |
| `places` | `integer[]` | No |  |
| `priceInRobux` | `integer` | No |  |
| `priceOffset` | `integer` | No |  |
| `isFree` | `boolean` | No |  |
| `enableRegionalPricing` | `boolean` | No |  |
| `isRentalOptIn` | `boolean` | No |  |
| `autoPublishEnabled` | `boolean` | No |  |
| `created` | `string` | No |  |
| `updated` | `string` | No |  |

### Roblox.Web.WebAPI.Models.ApiPageResponse[Roblox.ItemConfiguration.Api.AssetCreationsResponse]

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `previousPageCursor` | `string` | No |  |
| `nextPageCursor` | `string` | No |  |
| `data` | `Roblox.ItemConfiguration.Api.AssetCreationsResponse[]` | No |  |