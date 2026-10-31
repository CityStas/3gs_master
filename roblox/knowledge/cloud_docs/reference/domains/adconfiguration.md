---
name: "AdConfiguration Api v2"
last_updated: 2026-10-30T19:56:08Z
type: legacy
api_base_url: "https://adconfiguration.roblox.com"
versions: [v2]
endpoints: 10
auth: [cookie]
---

# AdConfiguration Api v2

> **Warning:** Legacy APIs with cookie authentication can incorporate breaking changes without notice. We don't recommend them for production applications.

**Base URL:** `https://adconfiguration.roblox.com`
**Versions:** v2

## Endpoints

### GET `/v2/sponsored-campaigns`

Gets a page of Roblox.AdConfiguration.Api.SponsoredCampaignModel with specified input parameters.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `campaignTargetType` | query | `integer (int32)` | Yes | The campaign target type enum value Valid values: `0`, `1`, `2`, `3` |
| `campaignTargetId` | query | `integer (int64)` | Yes | The id of the campaign target |
| `includeReportingStats` | query | `boolean` | No | Indicates whether to include reporting stats in the response |
| `isArchived` | query | `boolean` | No | Indicates whether to retrieve archived ads |
| `pageCursor` | query | `string` | No | The cursor of the page to retrieve. If empty, fetches the first page |

**Responses:**

- `200`: OK → `Roblox.AdConfiguration.Api.GetSponsoredCampaignsResponse`
- `400`: 22: Invalid campaign target ID. 23: Invalid campaign target type.
- `401`: 0: Authorization has been denied for this request.
- `503`: 1: This feature is disabled.

**Response fields** (`Roblox.AdConfiguration.Api.GetSponsoredCampaignsResponse`)

See [Roblox.AdConfiguration.Api.GetSponsoredCampaignsResponse](#roblox-adconfiguration-api-getsponsoredcampaignsresponse) in Models.

**Response example:**
```json
{
  "sponsoredCampaigns": [
    {
      "adId": "...",
      "adSetId": "...",
      "adName": "...",
      "adStatus": "...",
      "creativeType": "...",
      "creativeTargetId": "..."
    }
  ],
  "previousPageCursor": "string",
  "nextPageCursor": "string"
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://adconfiguration.roblox.com/v2/sponsored-campaigns?campaignTargetType={VALUE}&campaignTargetId={VALUE}"
```

### GET `/v2/sponsored-campaigns/eligible-asset-type-ids`

Get all asset type IDs that are eligible to be sponsored.

**Responses:**

- `200`: OK → `integer[]`
- `401`: 0: Authorization has been denied for this request.
- `403`: 10: Insufficient permissions.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://adconfiguration.roblox.com/v2/sponsored-campaigns/eligible-asset-type-ids"
```

### GET `/v2/sponsored-campaigns/multi-get-can-user-sponsor`

Checks whether the targets are eligible for sponsorship, and
if the user is authorized to sponsor the targets.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `campaignTargetType` | query | `integer (int32)` | Yes | Ads.Management.Service.CampaignTargetType. Valid values: `0`, `1`, `2`, `3` |
| `campaignTargetIds` | query | `array` | Yes | The IDs of the campaign targets. |

**Responses:**

- `200`: OK → `object`
- `400`: Bad Request
- `401`: 0: Authorization has been denied for this request.
- `403`: Forbidden
- `500`: Server Error

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://adconfiguration.roblox.com/v2/sponsored-campaigns/multi-get-can-user-sponsor?campaignTargetType={VALUE}&campaignTargetIds={VALUE}"
```

### GET `/v2/sponsored-games`

Gets a page of Roblox.AdConfiguration.Api.SponsoredGameV2Model with specified input parameters.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | query | `integer (int64)` | Yes | The universe id of the ad campaign. |
| `includeReportingStats` | query | `boolean` | No | Indicates whether to include reporting stats in the response. |
| `isArchived` | query | `boolean` | No | Indicates whether to retrieve archived ads. |
| `pageCursor` | query | `string` | No | The cursor of the page to retrieve. |

**Responses:**

- `200`: OK → `Roblox.AdConfiguration.Api.GetSponsoredGamesResponse`
- `400`: 9: Cannot load the universe for the specified universe id. 9: Cannot load the universe for the specified universe id.
- `401`: 0: Authorization has been denied for this request.
- `503`: 1: This feature is disabled.

**Response fields** (`Roblox.AdConfiguration.Api.GetSponsoredGamesResponse`)

See [Roblox.AdConfiguration.Api.GetSponsoredGamesResponse](#roblox-adconfiguration-api-getsponsoredgamesresponse) in Models.

**Response example:**
```json
{
  "sponsoredGames": [
    {
      "adId": "...",
      "adSetId": "...",
      "adName": "...",
      "adStatus": "...",
      "creativeType": "...",
      "creativeTargetId": "..."
    }
  ],
  "previousPageCursor": "string",
  "nextPageCursor": "string"
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://adconfiguration.roblox.com/v2/sponsored-games?universeId={VALUE}"
```

### GET `/v2/sponsored-games/universes`

Gets a list of universes for the authenticated user, or the given group, ordered by most recently created sponsored game ads.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | query | `integer (int64)` | No | The group id, if applicable. |

**Responses:**

- `200`: OK → `Roblox.AdConfiguration.Api.Models.GetRecentAdsRankedUniversesResponse`
- `400`: 19: Invalid group id.
- `401`: 0: Authorization has been denied for this request.
- `403`: 10: Insufficient permissions.

**Response fields** (`Roblox.AdConfiguration.Api.Models.GetRecentAdsRankedUniversesResponse`)

See [Roblox.AdConfiguration.Api.Models.GetRecentAdsRankedUniversesResponse](#roblox-adconfiguration-api-models-getrecentadsrankeduniversesresponse) in Models.

**Response example:**
```json
{
  "universes": [
    {
      "id": "...",
      "name": "..."
    }
  ]
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://adconfiguration.roblox.com/v2/sponsored-games/universes"
```

### POST `/v2/sponsored-campaigns/create`

Creates a complete ad. Including ad campaign, ad set, escrow, and the ad.
Currently intended for creation of sponsorships only.

**Request Body:** `application/json` — Type: `Roblox.AdConfiguration.Api.Models.CreateSponsoredCampaignRequest`

See [Roblox.AdConfiguration.Api.Models.CreateSponsoredCampaignRequest](#roblox-adconfiguration-api-models-createsponsoredcampaignrequest) in Models.

**Request example:**
```json
{
  "campaignTargetId": 0,
  "campaignTargetType": 0,
  "targetGender": 1,
  "targetAgeBracket": 1,
  "startDate": "2024-01-01T00:00:00Z",
  "endDate": "2024-01-01T00:00:00Z"
}
```

**Responses:**

- `200`: OK → `integer`
- `400`: 2: Daily budget is lower than minimum allowed. 3: Total budget must be greater than 0. 4: Ad name cannot be empty. 5: Start date must not be a future date. 6: End date must be a future date. 7: Start date must be earlier than end date. 8: Total budget does not match daily spend and number of days being scheduled 9: Cannot load the universe for the specified universe id. 11: Invalid target age bracket. 12: Invalid target gender. 13: Invalid target device type. 14: Invalid ad set id. 15: Ad name cannot exceed 255 characters. 16: Insufficient Robux balance. 17: Name has already been taken. 18: Daily budget is higher than maximum allowed. 19: Invalid group id. 20: Number of days scheduled exceeded maximum days allowed. 21: Your experience is currently not eligible for advertising. 22: Invalid campaign target ID. 23: Invalid campaign target type. 24: Invalid creative ID. 25: Invalid creative type. 28: Total budget must be campaign duration * daily bid 29: The target is not eligible for new campaigns 30: Invalid user ID
- `401`: 0: Authorization has been denied for this request. 10: Insufficient permissions.
- `403`: 0: Token Validation Failed
- `500`: 0: An unknown error occurred. 31: Internal server error
- `503`: 1: This feature is disabled.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://adconfiguration.roblox.com/v2/sponsored-campaigns/create" \
  -H "Content-Type: application/json" \
  -d '{
  "campaignTargetId": 0,
  "campaignTargetType": 0,
  "targetGender": 1,
  "targetAgeBracket": 1,
  "startDate": "2024-01-01T00:00:00Z",
  "endDate": "2024-01-01T00:00:00Z"
}'
```

### POST `/v2/sponsored-campaigns/eligible-campaign-targets`

Returns a collection of Roblox.AdConfiguration.Api.Models.CampaignTargetModel that the user is authorized to sponsor, ordered by most recently advertised

**Request Body:** `application/json` — Type: `Roblox.AdConfiguration.Api.Models.GetEligibleCampaignTargetsRequest`

See [Roblox.AdConfiguration.Api.Models.GetEligibleCampaignTargetsRequest](#roblox-adconfiguration-api-models-geteligiblecampaigntargetsrequest) in Models.

**Request example:**
```json
{
  "campaignTargetTypes": [
    0
  ],
  "groupId": 0
}
```

**Responses:**

- `200`: OK → `Roblox.AdConfiguration.Api.Models.GetCampaignTargetsResponse`
- `400`: 19: Invalid group id.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 10: Insufficient permissions.

**Response fields** (`Roblox.AdConfiguration.Api.Models.GetCampaignTargetsResponse`)

See [Roblox.AdConfiguration.Api.Models.GetCampaignTargetsResponse](#roblox-adconfiguration-api-models-getcampaigntargetsresponse) in Models.

**Response example:**
```json
{
  "campaignTargetModels": [
    {
      "campaignTargetType": "...",
      "campaignTargetId": "...",
      "name": "..."
    }
  ]
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://adconfiguration.roblox.com/v2/sponsored-campaigns/eligible-campaign-targets" \
  -H "Content-Type: application/json" \
  -d '{
  "campaignTargetTypes": [
    0
  ],
  "groupId": 0
}'
```

### POST `/v2/sponsored-campaigns/stop`

Stops a sponsored campaign / ad (ad set) from running. Initiated by a user.

**Request Body:** `application/json` — Type: `Roblox.AdConfiguration.Api.Models.StopSponsoredCampaignRequest`

See [Roblox.AdConfiguration.Api.Models.StopSponsoredCampaignRequest](#roblox-adconfiguration-api-models-stopsponsoredcampaignrequest) in Models.

**Request example:**
```json
{
  "adSetId": 0
}
```

**Responses:**

- `200`: OK → `integer`
- `400`: 10: Insufficient permissions. 14: Invalid ad set id. 31: Internal server error
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed
- `503`: 1: This feature is disabled.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://adconfiguration.roblox.com/v2/sponsored-campaigns/stop" \
  -H "Content-Type: application/json" \
  -d '{
  "adSetId": 0
}'
```

### POST `/v2/sponsored-games/create`

Creates a new sponsored game ad with specified input parameters.

**Request Body:** `application/json` — Type: `Roblox.AdConfiguration.Api.CreateSponsoredGameV2Request`

See [Roblox.AdConfiguration.Api.CreateSponsoredGameV2Request](#roblox-adconfiguration-api-createsponsoredgamev2request) in Models.

**Request example:**
```json
{
  "universeId": 0,
  "targetGender": 1,
  "targetAgeBracket": 1,
  "budgetInRobux": 0,
  "startDate": "2024-01-01T00:00:00Z",
  "endDate": "2024-01-01T00:00:00Z"
}
```

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: 2: Daily budget is lower than minimum allowed. 3: Total budget must be greater than 0. 4: Ad name cannot be empty. 5: Start date must not be a future date. 6: End date must be a future date. 7: Start date must be earlier than end date. 8: Total budget does not match daily spend and number of days being scheduled 9: Cannot load the universe for the specified universe id. 11: Invalid target age bracket. 12: Invalid target gender. 13: Invalid target device type. 14: Invalid ad set id. 15: Ad name cannot exceed 255 characters. 16: Insufficient Robux balance. 17: Name has already been taken. 18: Daily budget is higher than maximum allowed. 19: Invalid group id. 20: Number of days scheduled exceeded maximum days allowed. 21: Your experience is currently not eligible for advertising. 22: Invalid campaign target ID. 23: Invalid campaign target type. 24: Invalid creative ID. 25: Invalid creative type. 28: Total budget must be campaign duration * daily bid 29: The target is not eligible for new campaigns 30: Invalid user ID
- `401`: 0: Authorization has been denied for this request. 10: Insufficient permissions.
- `403`: 0: Token Validation Failed
- `500`: 0: An unknown error occurred. 31: Internal server error
- `503`: 1: This feature is disabled.

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://adconfiguration.roblox.com/v2/sponsored-games/create" \
  -H "Content-Type: application/json" \
  -d '{
  "universeId": 0,
  "targetGender": 1,
  "targetAgeBracket": 1,
  "budgetInRobux": 0,
  "startDate": "2024-01-01T00:00:00Z",
  "endDate": "2024-01-01T00:00:00Z"
}'
```

### POST `/v2/sponsored-games/stop`

To stop a sponsored-game ad (ad set) from running, initiated by a user.

**Request Body:** `application/json` — Type: `Roblox.AdConfiguration.Api.Models.StopSponsoredGameV2Request`

See [Roblox.AdConfiguration.Api.Models.StopSponsoredGameV2Request](#roblox-adconfiguration-api-models-stopsponsoredgamev2request) in Models.

**Request example:**
```json
{
  "adSetId": 0
}
```

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: 14: Invalid ad set id.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 10: Insufficient permissions.
- `503`: 1: This feature is disabled.

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://adconfiguration.roblox.com/v2/sponsored-games/stop" \
  -H "Content-Type: application/json" \
  -d '{
  "adSetId": 0
}'
```

## Models

### Roblox.AdConfiguration.Api.CreateSponsoredGameV2Request

A request model for creating a sponsored game

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `universeId` | `integer` | No | The target universe id |
| `targetGender` | `1 \| 2 \| 4` | No | Targeting gender(s) of the ad set ['Undefined' = 1, 'Male' = 2, 'Female' = 4] |
| `targetAgeBracket` | `1 \| 2 \| 4 \| 8 \| 16` | No | Targeting age bracket(s) of the ad set ['Undefined' = 1, 'AgeUnder13' = 2, 'Age13OrOver' = 4, 'Age13To16' = 8, 'Age17OrOver' = 16] |
| `budgetInRobux` | `integer` | No | The budget in Robux |
| `startDate` | `string` | No | The start date of the ad set |
| `endDate` | `string` | No | The end date of the ad set |
| `targetDeviceType` | `integer enum (6 values)` | No | Targeting device type(s) of the ad set ['Undefined' = 1, 'Computer' = 2, 'Phone' = 4, 'Tablet' = 8, 'Console' = 16, 'VR' = 32] Values: 1, 2, 4, 8, 16, 32 |
| `adName` | `string` | No | The name of the Ad |
| `bidAmountInRobux` | `integer` | No | The bid amount of the Ad in Robux |

### Roblox.AdConfiguration.Api.CreativeModel

A model representing an Ad Creative (for example, an ad thumbnail).

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `creativeId` | `integer` | No | The ID of the creative. Typically, a thumbnail's imageId. |
| `creativeType` | `0 \| 1 \| 2` | No | The type of the ad creative. Typically, CreativeType.Image. ['Undefined' = 0, 'Image' = 1, 'Video' = 2] |

### Roblox.AdConfiguration.Api.GetSponsoredCampaignsResponse

A response model for retrieving a page of Roblox.AdConfiguration.Api.SponsoredCampaignModel.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `sponsoredCampaigns` | `Roblox.AdConfiguration.Api.SponsoredCampaignModel[]` | No | A collection of Roblox.AdConfiguration.Api.SponsoredCampaignModel. |
| `previousPageCursor` | `string` | No | The cursor for retrieving the previous page, if present. |
| `nextPageCursor` | `string` | No | The cursor for retrieving the next page, if present. |

### Roblox.AdConfiguration.Api.GetSponsoredGamesResponse

A response model for retrieving a page of Roblox.AdConfiguration.Api.SponsoredGameV2Model.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `sponsoredGames` | `Roblox.AdConfiguration.Api.SponsoredGameV2Model[]` | No | A collection of Roblox.AdConfiguration.Api.SponsoredGameV2Model. |
| `previousPageCursor` | `string` | No | The cursor for retrieving the previous page, if present. |
| `nextPageCursor` | `string` | No | The cursor for retrieving the next page, if present. |

### Roblox.AdConfiguration.Api.Models.CampaignTargetModel

Represents a sponsored ad campaign target

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `campaignTargetType` | `0 \| 1 \| 2 \| 3` | No | The campaign target type ['Undefined' = 0, 'Universe' = 1, 'Asset' = 2, 'ImmersiveAd' = 3] |
| `campaignTargetId` | `integer` | No | The ID of the campaign target |
| `name` | `string` | No | The name of the campaign target (i.e. the asset name, universe name, group name, etc.) |

### Roblox.AdConfiguration.Api.Models.CreateSponsoredCampaignRequest

A request model for creating a sponsored game

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `campaignTargetId` | `integer` | No | The ID of the campaign target |
| `campaignTargetType` | `0 \| 1 \| 2 \| 3` | No | The type of the campaign target ['Undefined' = 0, 'Universe' = 1, 'Asset' = 2, 'ImmersiveAd' = 3] |
| `targetGender` | `1 \| 2 \| 4` | No | Targeting gender(s) of the ad set ['Undefined' = 1, 'Male' = 2, 'Female' = 4] |
| `targetAgeBracket` | `1 \| 2 \| 4 \| 8 \| 16` | No | Targeting age bracket(s) of the ad set ['Undefined' = 1, 'AgeUnder13' = 2, 'Age13OrOver' = 4, 'Age13To16' = 8, 'Age17OrOver' = 16] |
| `startDate` | `string` | No | The start date of the ad set |
| `endDate` | `string` | No | The end date of the ad set |
| `targetDeviceType` | `integer enum (6 values)` | No | Targeting device type(s) of the ad set ['Undefined' = 1, 'Computer' = 2, 'Phone' = 4, 'Tablet' = 8, 'Console' = 16, 'VR' = 32] Values: 1, 2, 4, 8, 16, 32 |
| `campaignName` | `string` | No | The name of the Campaign / Ad |
| `dailyBidAmountInRobux` | `integer` | No | The daily bid amount for the campaign / ad, in Robux |
| `placementLocation` | `integer enum (8 values)` | No | The location to place the campaign ['Undefined' = 1, 'GameSort' = 2, 'AvatarShop' = 4, 'ItemDetails' = 8, 'HomePage' = 16, 'Billboard300x250' = 32, 'Billboard600x300' = 64, 'Billboard300x600' = 128] Values: 1, 2, 4, 8, 16, 32, 64, 128 |
| `creativeModel` | `Roblox.AdConfiguration.Api.CreativeModel` | No |  |

### Roblox.AdConfiguration.Api.Models.GetCampaignTargetsResponse

The response model which returns a collection of Roblox.AdConfiguration.Api.Models.CampaignTargetModel

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `campaignTargetModels` | `Roblox.AdConfiguration.Api.Models.CampaignTargetModel[]` | No | Gets or sets a collection of Roblox.AdConfiguration.Api.Models.CampaignTargetModel |

### Roblox.AdConfiguration.Api.Models.GetEligibleCampaignTargetsRequest

A model represents a request to stop a sponsored campaign / ad.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `campaignTargetTypes` | `0 \| 1 \| 2 \| 3[]` | No | The list of campaign types we want to include in the results |
| `groupId` | `integer` | No | The group id, if applicable. |

### Roblox.AdConfiguration.Api.Models.GetRecentAdsRankedUniversesResponse

The response model for getting a list of recent-ads-ranked universes.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `universes` | `Roblox.AdConfiguration.Api.Models.UniverseModel[]` | No | Gets or sets a list of Roblox.AdConfiguration.Api.Models.UniverseModel. |

### Roblox.AdConfiguration.Api.Models.StopSponsoredCampaignRequest

A model represents a request to stop a sponsored campaign / ad.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `adSetId` | `integer` | No | The ID of the ad set to stop. |

### Roblox.AdConfiguration.Api.Models.StopSponsoredGameV2Request

A model represents a request to stop a sponsored game ad.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `adSetId` | `integer` | No | Gets the ID of the ad set to stop. |

### Roblox.AdConfiguration.Api.Models.UniverseModel

Represents a universe in API endpoint results.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | `integer` | No | The universe Id. |
| `name` | `string` | No | The name of the universe |

### Roblox.AdConfiguration.Api.SponsoredCampaignModel

A response model represents an Ad with complete information, including infos from its associated campaign and ad set

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `adId` | `integer` | No | The id of the ad |
| `adSetId` | `integer` | No | The id of the ad set |
| `adName` | `string` | No | The name of the Ad |
| `adStatus` | `0 \| 1 \| 2 \| 3 \| 4` | No | The status of the ad ['Undefined' = 0, 'Draft' = 1, 'PendingApproval' = 2, 'Approved' = 3, 'Moderated' = 4] |
| `creativeType` | `0 \| 1 \| 2` | No | The type of the creative associated with the Ad ['Undefined' = 0, 'Image' = 1, 'Video' = 2] |
| `creativeTargetId` | `integer` | No | The target id of the creative associated with the Ad |
| `bidAmountInRobux` | `integer` | No | The bid amount of the Ad in Robux |
| `budgetInRobux` | `integer` | No | The budget of the ad set in Robux |
| `adSetStatus` | `integer enum (7 values)` | No | The status of the ad set ['Undefined' = 0, 'Draft' = 1, 'Scheduled' = 2, 'Running' = 3, 'Paused' = 4, 'Stopped' = 5, 'Completed' = 6] Values: 0, 1, 2, 3, 4, 5, 6 |
| `startDate` | `string` | No | The start date of the ad set |
| `endDate` | `string` | No | The end date of the ad set |
| `targetGender` | `1 \| 2 \| 4` | No | The target gender of the ad set ['Undefined' = 1, 'Male' = 2, 'Female' = 4] |
| `targetAgeBracket` | `1 \| 2 \| 4 \| 8 \| 16` | No | The target age bracket of the ad set ['Undefined' = 1, 'AgeUnder13' = 2, 'Age13OrOver' = 4, 'Age13To16' = 8, 'Age17OrOver' = 16] |
| `targetDeviceType` | `integer enum (6 values)` | No | The target device type of the ad set ['Undefined' = 1, 'Computer' = 2, 'Phone' = 4, 'Tablet' = 8, 'Console' = 16, 'VR' = 32] Values: 1, 2, 4, 8, 16, 32 |
| `campaignTargetType` | `0 \| 1 \| 2 \| 3` | No | The target type of the campaign ['Undefined' = 0, 'Universe' = 1, 'Asset' = 2, 'ImmersiveAd' = 3] |
| `campaignTargetId` | `integer` | No | The target id of the campaign |
| `totalSpendInRobux` | `integer` | No | The total spend of the ad set in Robux |
| `totalImpressions` | `integer` | No | The total number of impressions generated by the ad |
| `totalClicks` | `integer` | No | The total number of clicks generated by the ad |
| `totalConversions` | `integer` | No | The total number of conversions generated by the ad |
| `impressionConversions` | `integer` | No | The number of conversions by ad impression generated by the ad |
| `clickConversions` | `integer` | No | The number of conversions by ad click generated by the ad |

### Roblox.AdConfiguration.Api.SponsoredGameV2Model

A response model represents an Ad with complete information, including infos from its associated campaign and ad set

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `adId` | `integer` | No | The id of the ad |
| `adSetId` | `integer` | No | The id of the ad set |
| `adName` | `string` | No | The name of the Ad |
| `adStatus` | `0 \| 1 \| 2 \| 3 \| 4` | No | The status of the ad ['Undefined' = 0, 'Draft' = 1, 'PendingApproval' = 2, 'Approved' = 3, 'Moderated' = 4] |
| `creativeType` | `0 \| 1 \| 2` | No | The type of the creative associated with the Ad ['Undefined' = 0, 'Image' = 1, 'Video' = 2] |
| `creativeTargetId` | `integer` | No | The target id of the creative associated with the Ad |
| `creativeUrl` | `string` | No | The Url of the creative |
| `bidAmountInRobux` | `integer` | No | The bid amount of the Ad in Robux |
| `budgetInRobux` | `integer` | No | The budget of the ad set in Robux |
| `adSetStatus` | `integer enum (7 values)` | No | The status of the ad set ['Undefined' = 0, 'Draft' = 1, 'Scheduled' = 2, 'Running' = 3, 'Paused' = 4, 'Stopped' = 5, 'Completed' = 6] Values: 0, 1, 2, 3, 4, 5, 6 |
| `startDate` | `string` | No | The start date of the ad set |
| `endDate` | `string` | No | The end date of the ad set |
| `targetGender` | `1 \| 2 \| 4` | No | The target gender of the ad set ['Undefined' = 1, 'Male' = 2, 'Female' = 4] |
| `targetAgeBracket` | `1 \| 2 \| 4 \| 8 \| 16` | No | The target age bracket of the ad set ['Undefined' = 1, 'AgeUnder13' = 2, 'Age13OrOver' = 4, 'Age13To16' = 8, 'Age17OrOver' = 16] |
| `targetDeviceType` | `integer enum (6 values)` | No | The target device type of the ad set ['Undefined' = 1, 'Computer' = 2, 'Phone' = 4, 'Tablet' = 8, 'Console' = 16, 'VR' = 32] Values: 1, 2, 4, 8, 16, 32 |
| `campaignTargetType` | `0 \| 1 \| 2 \| 3` | No | The target type of the campaign ['Undefined' = 0, 'Universe' = 1, 'Asset' = 2, 'ImmersiveAd' = 3] |
| `campaignTargetId` | `integer` | No | The target id of the campaign |
| `totalSpendInRobux` | `integer` | No | The total spend of the ad set in Robux |
| `totalImpressions` | `integer` | No | The total number of impressions generated by the ad |
| `totalClicks` | `integer` | No | The total number of clicks generated by the ad |
| `totalConversions` | `integer` | No | The total number of conversions generated by the ad |
| `impressionConversions` | `integer` | No | The number of conversions by ad impression generated by the ad |
| `clickConversions` | `integer` | No | The number of conversions by ad click generated by the ad |