---
name: "Advertising"
last_updated: 2026-10-30T19:56:08Z
type: feature
api_base_url: "https://apis.roblox.com"
endpoints: 24
auth: [api-key, oauth2, cookie]
description: "Create and manage advertising on Roblox"
---

# Advertising

Create and manage advertising on Roblox. Experience advertising drives engagement to your experiences through the Ads API, and item advertising promotes Marketplace items through sponsored campaigns. See the [Advertising guide](https://create.roblox.com/docs/cloud/guides/advertising) for Open Cloud setup and usage.

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

### GET `/ads-management/v1/advertisable-universes` [BETA]

List advertisable universes

Returns the universe IDs of every experience the billing account is eligible to advertise. The complete list is returned in a single response; this endpoint is not paginated. Use these IDs to set targetUniverseId when creating a campaign, and resolve experience names with the Open Cloud Universe API.

**Auth:** Cookie (`.ROBLOSECURITY`) or API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `ad.campaign:read`

**Responses:**

- `200`: OK → `internal_public_v1.ListAdvertisableUniversesResponse`
- `403`: Permission denied → `internal_public_v1.ErrorEnvelope`
- `429`: Rate limit exceeded → `internal_public_v1.ErrorEnvelope`
- `500`: Internal server error → `internal_public_v1.ErrorEnvelope`

**Response fields** (`internal_public_v1.ListAdvertisableUniversesResponse`)

See [internal_public_v1.ListAdvertisableUniversesResponse](#internal-public-v1-listadvertisableuniversesresponse) in Models.

**Response example:**
```json
{
  "advertisableUniverses": [
    {
      "universeId": "..."
    }
  ]
}
```

**Error handling:** `429`: Retry with exponential backoff (start at 1s). `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 600/minute, perOauth2Authorization: 600/minute

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/ads-management/v1/advertisable-universes"
```

### GET `/ads-management/v1/billing-accounts` [BETA]

List billing accounts

Lists the billing accounts owned by the authenticated user. Each account includes its type, status, time zone, and create/update timestamps. Results are paginated with a cursor (pageToken).

**Auth:** Cookie (`.ROBLOSECURITY`) or API Key (`x-api-key` header)

**Scopes:** `ad.billing:read`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `maxPageSize` | query | `integer` | No | Maximum results per page (1-100, default 50) |
| `pageToken` | query | `string` | No | Opaque cursor from a prior nextPageToken |

**Responses:**

- `200`: OK → `internal_public_v1.ListBillingAccountsResponse`
- `400`: Invalid maxPageSize or pageToken → `internal_public_v1.ErrorEnvelope`
- `403`: Permission denied → `internal_public_v1.ErrorEnvelope`
- `429`: Rate limit exceeded → `internal_public_v1.ErrorEnvelope`
- `500`: Internal server error → `internal_public_v1.ErrorEnvelope`

**Response fields** (`internal_public_v1.ListBillingAccountsResponse`)

See [internal_public_v1.ListBillingAccountsResponse](#internal-public-v1-listbillingaccountsresponse) in Models.

**Response example:**
```json
{
  "billingAccounts": [
    {
      "createTime": "...",
      "displayName": "...",
      "id": "...",
      "organizationId": "...",
      "status": "...",
      "timeZone": "..."
    }
  ],
  "nextPageToken": "string"
}
```

**Error handling:** `429`: Retry with exponential backoff (start at 1s). `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 600/minute

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/ads-management/v1/billing-accounts"
```

### GET `/ads-management/v1/billing-accounts/{id}` [BETA]

Get a billing account

Returns a single billing account owned by the authenticated user. Returns 404 if the account does not exist or is not owned by the caller.

**Auth:** Cookie (`.ROBLOSECURITY`) or API Key (`x-api-key` header)

**Scopes:** `ad.billing:read`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `id` | path | `string` | Yes | Billing account ID |

**Responses:**

- `200`: OK → `internal_public_v1.BillingAccount`
- `403`: Permission denied → `internal_public_v1.ErrorEnvelope`
- `404`: Billing account not found → `internal_public_v1.ErrorEnvelope`
- `429`: Rate limit exceeded → `internal_public_v1.ErrorEnvelope`
- `500`: Internal server error → `internal_public_v1.ErrorEnvelope`

**Response fields** (`internal_public_v1.BillingAccount`)

See [internal_public_v1.BillingAccount](#internal-public-v1-billingaccount) in Models.

**Response example:**
```json
{
  "createTime": "string",
  "displayName": "string",
  "id": "string",
  "organizationId": "string",
  "status": "ACTIVE",
  "timeZone": "string"
}
```

**Error handling:** `429`: Retry with exponential backoff (start at 1s). `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 600/minute

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/ads-management/v1/billing-accounts/{ID}"
```

### GET `/ads-management/v1/campaign-options` [BETA]

Get campaign options

Returns the values accepted when creating a campaign: supported objectives, payment types, ad formats, and targeting dimensions. When universeId is supplied, the response also includes an eligibility block indicating whether that experience can currently be advertised, along with the reasons when it cannot.

**Auth:** Cookie (`.ROBLOSECURITY`) or API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `ad.campaign:read`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | query | `string` | No | Universe ID to check eligibility for |
| `objective` | query | `PLAYS \| ENGAGEMENT` | No | Objective filter (PLAYS or ENGAGEMENT) Valid values: `PLAYS`, `ENGAGEMENT` |

**Responses:**

- `200`: OK → `internal_public_v1.CampaignOptionsResponse`
- `400`: Invalid objective or universeId → `internal_public_v1.ErrorEnvelope`
- `403`: Permission denied → `internal_public_v1.ErrorEnvelope`
- `429`: Rate limit exceeded → `internal_public_v1.ErrorEnvelope`
- `500`: Internal server error → `internal_public_v1.ErrorEnvelope`

**Response fields** (`internal_public_v1.CampaignOptionsResponse`)

See [internal_public_v1.CampaignOptionsResponse](#internal-public-v1-campaignoptionsresponse) in Models.

**Response example:**
```json
{
  "adFormats": [
    {
      "format": "...",
      "height": "...",
      "width": "..."
    }
  ],
  "eligibility": "...",
  "objectives": [
    "PLAYS"
  ],
  "paymentTypes": [
    "CREDIT_CARD"
  ],
  "targetingDimensions": {
    "ageGroups": [
      "..."
    ],
    "countries": [
      "..."
    ],
    "devices": [
      "..."
    ]
  }
}
```

**Error handling:** `429`: Retry with exponential backoff (start at 1s). `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 600/minute, perOauth2Authorization: 600/minute

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/ads-management/v1/campaign-options"
```

### GET `/ads-management/v1/campaigns` [BETA]

List campaigns

Lists the campaigns in the caller's billing account. Campaigns are grouped by status (ACTIVE first, then PAUSED, then CANCELLED) and returned newest first within each group. Results are paginated with a cursor (pageToken); each page returns up to maxPageSize campaigns (default 50, max 100).

**Auth:** Cookie (`.ROBLOSECURITY`) or API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `ad.campaign:read`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `maxPageSize` | query | `integer` | No | Maximum results per page (1-100, default 50) |
| `pageToken` | query | `string` | No | Opaque cursor from a prior nextPageToken |

**Responses:**

- `200`: OK → `internal_public_v1.ListCampaignsResponse`
- `400`: Invalid maxPageSize or pageToken → `internal_public_v1.ErrorEnvelope`
- `403`: Permission denied → `internal_public_v1.ErrorEnvelope`
- `429`: Rate limit exceeded → `internal_public_v1.ErrorEnvelope`
- `500`: Internal server error → `internal_public_v1.ErrorEnvelope`

**Response fields** (`internal_public_v1.ListCampaignsResponse`)

See [internal_public_v1.ListCampaignsResponse](#internal-public-v1-listcampaignsresponse) in Models.

**Response example:**
```json
{
  "campaigns": [
    {
      "bid": "...",
      "billingAccountId": "...",
      "budget": "...",
      "createTime": "...",
      "creativeAssetIds": "...",
      "deliveryStatus": "..."
    }
  ],
  "nextPageToken": "string"
}
```

**Error handling:** `429`: Retry with exponential backoff (start at 1s). `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 600/minute, perOauth2Authorization: 600/minute

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/ads-management/v1/campaigns"
```

### POST `/ads-management/v1/campaigns` [BETA]

Create a campaign

Creates an ad campaign in the billing account. The creatives you reference must already exist as Open Cloud image assets that you have permission to use; they are validated and saved to your account's reusable creatives when the campaign is created. On success the campaign is returned with deliveryStatus IN_REVIEW, meaning it is queued for ad-policy review and not yet serving — poll the campaign (or campaigns:batchGetStatus) until this changes. budget.amountMicros is the budget in micro-USD as a decimal string (e.g. "5000000" = $5.00). It must be at least the minimum campaign budget; an amount below the minimum returns 400 with the required minimum stated in the error message. schedule.durationInDays must not exceed 3650 (~10 years). The x-idempotency-key header is required and must be a UUID: retrying the same key with an identical body within 24 hours returns the original campaign (200), while reusing a key with a different body returns 409.

**Auth:** Cookie (`.ROBLOSECURITY`) or API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `ad.campaign:write`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `x-idempotency-key` | header | `string` | Yes | Idempotency key (UUID); 24h dedupe window. Identical replay returns the original campaign (200); mismatched replay may conflict (409). |

**Request Body:** `application/json` — Type: `internal_public_v1.CreateCampaignRequest`

See [internal_public_v1.CreateCampaignRequest](#internal-public-v1-createcampaignrequest) in Models.

**Request example:**
```json
{
  "bid": "...",
  "budget": {
    "amountMicros": "string",
    "scheduledAmountMicros": "string",
    "scheduledEffectiveTime": "string",
    "type": "DAILY"
  },
  "creativeAssetIds": [
    "string"
  ],
  "name": "string",
  "objective": "PLAYS",
  "paymentType": "CREDIT_CARD"
}
```

**Responses:**

- `200`: Campaign created, or idempotent replay of a prior create with the same key and body → `internal_public_v1.Campaign`
- `400`: Validation error, invalid asset, or endTime sent → `internal_public_v1.ErrorEnvelope`
- `403`: Cannot manage account, universe not advertisable, or USE-permission denied → `internal_public_v1.ErrorEnvelope`
- `409`: Idempotency key reused with a different request body, or concurrent write conflict → `internal_public_v1.ErrorEnvelope`
- `429`: Rate limit exceeded → `internal_public_v1.ErrorEnvelope`
- `500`: Internal server error → `internal_public_v1.ErrorEnvelope`

**Response fields** (`internal_public_v1.Campaign`)

See [internal_public_v1.Campaign](#internal-public-v1-campaign) in Models.

**Response example:**
```json
{
  "bid": {
    "strategy": "AUTOMATED"
  },
  "billingAccountId": "string",
  "budget": {
    "amountMicros": "string",
    "scheduledAmountMicros": "string",
    "scheduledEffectiveTime": "string",
    "type": "DAILY"
  },
  "createTime": "string",
  "creativeAssetIds": [
    "string"
  ],
  "deliveryStatus": "SERVING"
}
```

**Error handling:** `429`: Retry with exponential backoff (start at 1s). `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 60/minute, perOauth2Authorization: 60/minute

**Example:**
```bash
curl -X POST -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/ads-management/v1/campaigns" \
  -H "Content-Type: application/json" \
  -d '{
  "bid": "...",
  "budget": {
    "amountMicros": "string",
    "scheduledAmountMicros": "string",
    "scheduledEffectiveTime": "string",
    "type": "DAILY"
  },
  "creativeAssetIds": [
    "string"
  ],
  "name": "string",
  "objective": "PLAYS",
  "paymentType": "CREDIT_CARD"
}'
```

### GET `/ads-management/v1/campaigns/{id}` [BETA]

Get a campaign

Returns a single campaign, including its status (the lifecycle state you control: ACTIVE, PAUSED, or CANCELLED) and its deliveryStatus (whether it is currently serving: SERVING, IN_REVIEW, NOT_SERVING, or REJECTED). deliveryStatusReasons lists any reasons that affect delivery — for example why a campaign is not serving or was rejected, or that a serving campaign is still in its initial learning period. Returns 404 if the campaign does not exist or is not owned by the caller.

**Auth:** Cookie (`.ROBLOSECURITY`) or API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `ad.campaign:read`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `id` | path | `string` | Yes | Campaign ID |

**Responses:**

- `200`: OK → `internal_public_v1.Campaign`
- `400`: Invalid campaign ID → `internal_public_v1.ErrorEnvelope`
- `403`: Permission denied → `internal_public_v1.ErrorEnvelope`
- `404`: Campaign not found → `internal_public_v1.ErrorEnvelope`
- `429`: Rate limit exceeded → `internal_public_v1.ErrorEnvelope`
- `500`: Internal server error → `internal_public_v1.ErrorEnvelope`

**Response fields** (`internal_public_v1.Campaign`)

See [internal_public_v1.Campaign](#internal-public-v1-campaign) in Models.

**Response example:**
```json
{
  "bid": {
    "strategy": "AUTOMATED"
  },
  "billingAccountId": "string",
  "budget": {
    "amountMicros": "string",
    "scheduledAmountMicros": "string",
    "scheduledEffectiveTime": "string",
    "type": "DAILY"
  },
  "createTime": "string",
  "creativeAssetIds": [
    "string"
  ],
  "deliveryStatus": "SERVING"
}
```

**Error handling:** `429`: Retry with exponential backoff (start at 1s). `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 600/minute, perOauth2Authorization: 600/minute

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/ads-management/v1/campaigns/{ID}"
```

### PATCH `/ads-management/v1/campaigns/{id}` [BETA]

Update a campaign

Updates the mutable fields of a campaign. You can change: name, budget.amountMicros, schedule.startTime and schedule.durationInDays (schedule changes are only allowed before the campaign starts), and status. Set status to ACTIVE to run or resume the campaign, PAUSED to pause it, or CANCELLED to cancel it permanently. budget.type cannot be changed — only the amount. A budget increase takes effect immediately, but a budget decrease on a running campaign is scheduled for the next midnight in the account's time zone; while a decrease is pending, the response reports it in budget.scheduledAmountMicros and budget.scheduledEffectiveTime. The fields objective, paymentType, targeting, creativeAssetIds, and bid are fixed after creation and return 400 if included. The updated campaign is returned with its recomputed deliveryStatus.

**Auth:** Cookie (`.ROBLOSECURITY`) or API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `ad.campaign:write`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `id` | path | `string` | Yes | Campaign ID |

**Request Body:** `application/json` — Type: `internal_public_v1.UpdateCampaignRequest`

See [internal_public_v1.UpdateCampaignRequest](#internal-public-v1-updatecampaignrequest) in Models.

**Request example:**
```json
{
  "bid": "...",
  "budget": "...",
  "creativeAssetIds": [
    "string"
  ],
  "name": "string",
  "schedule": "...",
  "status": "ACTIVE"
}
```

**Responses:**

- `200`: OK → `internal_public_v1.Campaign`
- `400`: Validation error or immutable field supplied → `internal_public_v1.ErrorEnvelope`
- `403`: Permission denied → `internal_public_v1.ErrorEnvelope`
- `404`: Campaign not found → `internal_public_v1.ErrorEnvelope`
- `429`: Rate limit exceeded → `internal_public_v1.ErrorEnvelope`
- `500`: Internal server error → `internal_public_v1.ErrorEnvelope`

**Response fields** (`internal_public_v1.Campaign`)

See [internal_public_v1.Campaign](#internal-public-v1-campaign) in Models.

**Response example:**
```json
{
  "bid": {
    "strategy": "AUTOMATED"
  },
  "billingAccountId": "string",
  "budget": {
    "amountMicros": "string",
    "scheduledAmountMicros": "string",
    "scheduledEffectiveTime": "string",
    "type": "DAILY"
  },
  "createTime": "string",
  "creativeAssetIds": [
    "string"
  ],
  "deliveryStatus": "SERVING"
}
```

**Error handling:** `429`: Retry with exponential backoff (start at 1s). `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 60/minute, perOauth2Authorization: 60/minute

**Example:**
```bash
curl -X PATCH -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/ads-management/v1/campaigns/{ID}" \
  -H "Content-Type: application/json" \
  -d '{
  "bid": "...",
  "budget": "...",
  "creativeAssetIds": [
    "string"
  ],
  "name": "string",
  "schedule": "...",
  "status": "ACTIVE"
}'
```

### POST `/ads-management/v1/campaigns:batchGetStatus` [BETA]

Batch get campaign status

Returns the status (lifecycle state) and deliveryStatus (whether the campaign is currently serving), along with deliveryStatusReasons, for up to 100 campaigns in a single call. This is the recommended way to poll the review and serving state of many campaigns at once. Provide the campaign IDs in campaignIds; any ID that is not found or is not owned by the caller is returned in the failures array with reason NOT_FOUND.

**Auth:** Cookie (`.ROBLOSECURITY`) or API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `ad.campaign:read`

**Request Body:** `application/json` — Type: `internal_public_v1.BatchGetStatusRequest`

See [internal_public_v1.BatchGetStatusRequest](#internal-public-v1-batchgetstatusrequest) in Models.

**Request example:**
```json
{
  "campaignIds": [
    "string"
  ]
}
```

**Responses:**

- `200`: OK → `internal_public_v1.BatchGetStatusResponse`
- `400`: Invalid request or exceeds 100 IDs → `internal_public_v1.ErrorEnvelope`
- `403`: Permission denied → `internal_public_v1.ErrorEnvelope`
- `429`: Rate limit exceeded → `internal_public_v1.ErrorEnvelope`
- `500`: Internal server error → `internal_public_v1.ErrorEnvelope`

**Response fields** (`internal_public_v1.BatchGetStatusResponse`)

See [internal_public_v1.BatchGetStatusResponse](#internal-public-v1-batchgetstatusresponse) in Models.

**Response example:**
```json
{
  "failures": [
    {
      "id": "...",
      "reason": "..."
    }
  ],
  "statuses": [
    {
      "deliveryStatus": "...",
      "deliveryStatusReasons": "...",
      "id": "...",
      "status": "..."
    }
  ]
}
```

**Error handling:** `429`: Retry with exponential backoff (start at 1s). `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 1000/minute, perOauth2Authorization: 1000/minute

**Example:**
```bash
curl -X POST -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/ads-management/v1/campaigns:batchGetStatus" \
  -H "Content-Type: application/json" \
  -d '{
  "campaignIds": [
    "string"
  ]
}'
```

### GET `/ads-management/v1/creatives` [BETA]

List creatives

Lists the reusable creatives saved to the caller's billing account. Each creative includes its assetId, name, moderation status, dimensions, and source. Use isArchived to filter by archive state. Results are paginated with a cursor (pageToken).

**Auth:** Cookie (`.ROBLOSECURITY`) or API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `ad.campaign:read`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `isArchived` | query | `boolean` | No | Filter by archived status |
| `maxPageSize` | query | `integer` | No | Maximum results per page (1-100, default 50) |
| `pageToken` | query | `string` | No | Opaque cursor from a prior nextPageToken |

**Responses:**

- `200`: OK → `internal_public_v1.ListCreativesResponse`
- `400`: Invalid maxPageSize or pageToken → `internal_public_v1.ErrorEnvelope`
- `403`: Permission denied → `internal_public_v1.ErrorEnvelope`
- `429`: Rate limit exceeded → `internal_public_v1.ErrorEnvelope`
- `500`: Internal server error → `internal_public_v1.ErrorEnvelope`

**Response fields** (`internal_public_v1.ListCreativesResponse`)

See [internal_public_v1.ListCreativesResponse](#internal-public-v1-listcreativesresponse) in Models.

**Response example:**
```json
{
  "creatives": [
    {
      "assetId": "...",
      "assetName": "...",
      "assetType": "...",
      "createTime": "...",
      "height": "...",
      "id": "..."
    }
  ],
  "nextPageToken": "string"
}
```

**Error handling:** `429`: Retry with exponential backoff (start at 1s). `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 600/minute, perOauth2Authorization: 600/minute

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/ads-management/v1/creatives"
```

### POST `/v1/ads-tracking/click`

Records an ad click.

**Server:** `https://ads.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Request Body:** `application/json` — Type: `Roblox.Ads.Api.RecordClickRequest`

See [Roblox.Ads.Api.RecordClickRequest](#roblox-ads-api-recordclickrequest) in Models.

**Request example:**
```json
{
  "encryptedAdTrackingData": "string",
  "campaignTargetType": 0,
  "placementLocation": 1
}
```

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://ads.roblox.com/v1/ads-tracking/click" \
  -H "Content-Type: application/json" \
  -d '{
  "encryptedAdTrackingData": "string",
  "campaignTargetType": 0,
  "placementLocation": 1
}'
```

### POST `/v1/sponsored-games/click`

Records clicks for sponsored games.

**Server:** `https://ads.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Request Body:** `application/json` — Type: `string`

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://ads.roblox.com/v1/sponsored-games/click" \
  -H "Content-Type: application/json" \
  -d '"string"'
```

### GET `/v1/sponsored-pages`

Retrieves sponsored pages to serve to a user on a specific device type in a specific country.

**Server:** `https://ads.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.Ads.Api.Models.Response.SponsoredPageResponse_`
- `401`: 0: Authorization has been denied for this request.

**Response fields** (`Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.Ads.Api.Models.Response.SponsoredPageResponse_`)

See [Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.Ads.Api.Models.Response.SponsoredPageResponse_](#roblox-web-webapi-models-apiarrayresponse-roblox-ads-api-models-response-sponsoredpageresponse-) in Models.

**Response example:**
```json
{
  "data": [
    {
      "name": "...",
      "title": "...",
      "logoImageUrl": "...",
      "pageType": "...",
      "pagePath": "..."
    }
  ]
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://ads.roblox.com/v1/sponsored-pages"
```

### GET `/v1/sponsored/catalog-assets/{targetId}/create`

Returns the asset information for creating a new sponsored campaign.

**Server:** `https://ads.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `targetId` | path | `integer` | Yes | The target of the campaign |

**Responses:**

- `200`: OK → `Roblox.Ads.Api.Models.Response.CreateSponsoredItemCampaignResponse`
- `401`: 0: Authorization has been denied for this request.

**Response fields** (`Roblox.Ads.Api.Models.Response.CreateSponsoredItemCampaignResponse`)

See [Roblox.Ads.Api.Models.Response.CreateSponsoredItemCampaignResponse](#roblox-ads-api-models-response-createsponsoreditemcampaignresponse) in Models.

**Response example:**
```json
{
  "creatorTargetId": 0,
  "creatorType": "string",
  "creatorName": "string"
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://ads.roblox.com/v1/sponsored/catalog-assets/{TARGETID}/create"
```

### GET `/v2/sponsored-campaigns`

Gets a page of Roblox.AdConfiguration.Api.SponsoredCampaignModel with specified input parameters.

**Server:** `https://adconfiguration.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `campaignTargetType` | query | `0 \| 1 \| 2 \| 3` | Yes | The campaign target type enum value Valid values: `0`, `1`, `2`, `3` |
| `campaignTargetId` | query | `integer` | Yes | The id of the campaign target |
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
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://adconfiguration.roblox.com/v2/sponsored-campaigns?campaignTargetType={VALUE}&campaignTargetId={VALUE}"
```

### POST `/v2/sponsored-campaigns/create`

Creates a complete ad. Including ad campaign, ad set, escrow, and the ad.
Currently intended for creation of sponsorships only.

**Server:** `https://adconfiguration.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

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
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
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

### GET `/v2/sponsored-campaigns/eligible-asset-type-ids`

Get all asset type IDs that are eligible to be sponsored.

**Server:** `https://adconfiguration.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Responses:**

- `200`: OK → `integer[]`
- `401`: 0: Authorization has been denied for this request.
- `403`: 10: Insufficient permissions.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://adconfiguration.roblox.com/v2/sponsored-campaigns/eligible-asset-type-ids"
```

### POST `/v2/sponsored-campaigns/eligible-campaign-targets`

Returns a collection of Roblox.AdConfiguration.Api.Models.CampaignTargetModel that the user is authorized to sponsor, ordered by most recently advertised

**Server:** `https://adconfiguration.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

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
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://adconfiguration.roblox.com/v2/sponsored-campaigns/eligible-campaign-targets" \
  -H "Content-Type: application/json" \
  -d '{
  "campaignTargetTypes": [
    0
  ],
  "groupId": 0
}'
```

### GET `/v2/sponsored-campaigns/multi-get-can-user-sponsor`

Checks whether the targets are eligible for sponsorship, and
if the user is authorized to sponsor the targets.

**Server:** `https://adconfiguration.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `campaignTargetType` | query | `0 \| 1 \| 2 \| 3` | Yes | Ads.Management.Service.CampaignTargetType. Valid values: `0`, `1`, `2`, `3` |
| `campaignTargetIds` | query | `integer[]` | Yes | The IDs of the campaign targets. |

**Responses:**

- `200`: OK → `object`
- `400`: Bad Request
- `401`: 0: Authorization has been denied for this request.
- `403`: Forbidden
- `500`: Server Error

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://adconfiguration.roblox.com/v2/sponsored-campaigns/multi-get-can-user-sponsor?campaignTargetType={VALUE}&campaignTargetIds={VALUE}"
```

### POST `/v2/sponsored-campaigns/stop`

Stops a sponsored campaign / ad (ad set) from running. Initiated by a user.

**Server:** `https://adconfiguration.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

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
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://adconfiguration.roblox.com/v2/sponsored-campaigns/stop" \
  -H "Content-Type: application/json" \
  -d '{
  "adSetId": 0
}'
```

### GET `/v2/sponsored-games`

Gets a page of Roblox.AdConfiguration.Api.SponsoredGameV2Model with specified input parameters.

**Server:** `https://adconfiguration.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | query | `integer` | Yes | The universe id of the ad campaign. |
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
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://adconfiguration.roblox.com/v2/sponsored-games?universeId={VALUE}"
```

### POST `/v2/sponsored-games/create`

Creates a new sponsored game ad with specified input parameters.

**Server:** `https://adconfiguration.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

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
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
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

**Server:** `https://adconfiguration.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

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
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://adconfiguration.roblox.com/v2/sponsored-games/stop" \
  -H "Content-Type: application/json" \
  -d '{
  "adSetId": 0
}'
```

### GET `/v2/sponsored-games/universes`

Gets a list of universes for the authenticated user, or the given group, ordered by most recently created sponsored game ads.

**Server:** `https://adconfiguration.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | query | `integer` | No | The group id, if applicable. |

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
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://adconfiguration.roblox.com/v2/sponsored-games/universes"
```

## Models

### internal_public_v1.ListAdvertisableUniversesResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `advertisableUniverses` | `internal_public_v1.AdvertisableUniverse[]` | No | The complete set of experiences the caller can advertise. This endpoint is not paginated; the full list is returned in one response. |

### internal_public_v1.ErrorEnvelope

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `detail` | `string` | No | A human-readable explanation of this specific failure. |
| `errors` | `internal_public_v1.PublicError[]` | No | The individual errors. There is at least one entry; each has a code and message. |
| `status` | `integer` | No | The HTTP status code, repeated here for convenience. |
| `title` | `string` | No | A short summary of the error class. |

### internal_public_v1.ListBillingAccountsResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `billingAccounts` | `internal_public_v1.BillingAccount[]` | No | The page of billing accounts. |
| `nextPageToken` | `string` | No | The cursor for the next page. Pass it as pageToken to fetch the next page. Absent on the last page. |

### internal_public_v1.BillingAccount

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `createTime` | `string` | No | The time the account was created, as an RFC 3339 UTC timestamp. |
| `displayName` | `string` | No | The human-readable name of the account. |
| `id` | `string` | No | The unique identifier of the billing account. Use it as the {id} path parameter. |
| `organizationId` | `string` | No | The identifier of the organization that owns the account. |
| `status` | `ACTIVE \| DISABLED \| ARCHIVED` | No | The current state of the account. Can be `ACTIVE`, `DISABLED`, or `ARCHIVED`. |
| `timeZone` | `string` | No | The IANA time zone the account's reporting dates and budget schedules are interpreted in. Example: `America/Los_Angeles`. |
| `type` | `SELF_SERVICE \| MANAGED \| INTERNAL` | No | The account category. External advertisers are always SELF_SERVICE; MANAGED and INTERNAL are Roblox-operated accounts. Can be `SELF_SERVICE`, `MANAGED`, or `INTERNAL`. |
| `updateTime` | `string` | No | The time the account was last updated, as an RFC 3339 UTC timestamp. |

### internal_public_v1.CampaignOptionsResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `adFormats` | `internal_public_v1.AdFormat[]` | No | The supported creative formats and their pixel dimensions. |
| `eligibility` | `any` | No | The eligibility result for the requested experience. Present only when universeId was supplied in the request. |
| `objectives` | `PLAYS \| ENGAGEMENT[]` | No | The campaign objectives you can create. Values can be `PLAYS` or `ENGAGEMENT`. |
| `paymentTypes` | `CREDIT_CARD \| ADS_CREDIT \| INVOICE[]` | No | The payment types available for the caller's account. Values can be `CREDIT_CARD`, `ADS_CREDIT`, or `INVOICE`. |
| `targetingDimensions` | `internal_public_v1.TargetingDimensions` | No |  |

### internal_public_v1.ListCampaignsResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `campaigns` | `internal_public_v1.Campaign[]` | No | The page of campaigns. |
| `nextPageToken` | `string` | No | The cursor for the next page. Pass it as pageToken to fetch the next page. Absent on the last page. |

### internal_public_v1.CreateCampaignRequest

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `bid` | `any` | No | Optional bidding strategy. Only `AUTOMATED` is accepted in v1; may be omitted. |
| `budget` | `internal_public_v1.Budget` | Yes |  |
| `creativeAssetIds` | `string[]` | Yes | The Open Cloud image asset IDs to advertise, as decimal strings. Required. The assets must already exist and be usable by the caller. |
| `name` | `string` | Yes | The display name of the campaign. Required. |
| `objective` | `PLAYS \| ENGAGEMENT` | Yes | The advertising goal. Required. Can be `PLAYS` or `ENGAGEMENT`. `ENGAGEMENT` does not support targeting and is not available for every experience. |
| `paymentType` | `CREDIT_CARD \| ADS_CREDIT \| INVOICE` | Yes | How the campaign is paid for. Required. Can be `CREDIT_CARD`, `ADS_CREDIT`, or `INVOICE`, subject to what the billing account supports. |
| `schedule` | `internal_public_v1.Schedule` | Yes |  |
| `targetUniverseId` | `string` | Yes | The identifier of the experience to advertise. Required. |
| `targeting` | `any` | No | Optional audience targeting. Omit it, or send an empty object, to reach all audiences. |

### internal_public_v1.Campaign

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `bid` | `internal_public_v1.Bid` | No |  |
| `billingAccountId` | `string` | No | The billing account that owns and funds the campaign. |
| `budget` | `internal_public_v1.Budget` | No |  |
| `createTime` | `string` | No | The time the campaign was created, as an RFC 3339 UTC timestamp. |
| `creativeAssetIds` | `string[]` | No | The Open Cloud image asset IDs the campaign advertises, as decimal strings. |
| `deliveryStatus` | `SERVING \| IN_REVIEW \| NOT_SERVING \| REJECTED` | No | The current serving state, derived by the system (read-only). Can be `SERVING`, `IN_REVIEW`, `NOT_SERVING`, or `REJECTED`. |
| `deliveryStatusReasons` | `string enum (13 values)[]` | No | The reasons behind the current deliveryStatus, such as why a campaign is not serving or was rejected, or `LEARNING` while a serving campaign ramps up. Omitted when there are none. |
| `id` | `string` | No | The server-assigned unique identifier of the campaign. |
| `name` | `string` | No | The display name of the campaign. |
| `objective` | `string enum (6 values)` | No | The advertising goal of the campaign. `PLAYS` or `ENGAGEMENT` for campaigns created via this API; campaigns from other surfaces may report `AWARENESS`, `REACH`, `VIDEO_VIEWS`, or `ROBUX_SPEND`. Values: PLAYS, ENGAGEMENT, AWARENESS, REACH, VIDEO_VIEWS, ROBUX_SPEND |
| `paymentType` | `CREDIT_CARD \| ADS_CREDIT \| INVOICE` | No | How the campaign is paid for. Fixed when the campaign is created. Can be `CREDIT_CARD`, `ADS_CREDIT`, or `INVOICE`. |
| `schedule` | `internal_public_v1.Schedule` | No |  |
| `status` | `ACTIVE \| PAUSED \| CANCELLED` | No | The lifecycle state you control through update requests. Can be `ACTIVE`, `PAUSED`, or `CANCELLED`. `CANCELLED` is permanent. |
| `targetUniverseId` | `string` | No | The identifier of the experience the campaign advertises. |
| `targeting` | `internal_public_v1.Targeting` | No |  |
| `updateTime` | `string` | No | The time the campaign was last updated, as an RFC 3339 UTC timestamp. |

### internal_public_v1.UpdateCampaignRequest

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `bid` | `any` | No | Immutable in v1; including it returns 400. |
| `budget` | `any` | No | A budget change. Only the amount is mutable; the budget type is fixed at creation, so it is not part of this object. Sending `type` returns 400. |
| `creativeAssetIds` | `string[]` | No | Immutable in v1; including it returns 400. |
| `name` | `string` | No | A new display name for the campaign. |
| `schedule` | `any` | No | A schedule change. Allowed only before the campaign starts. |
| `status` | `ACTIVE \| PAUSED \| CANCELLED` | No | A lifecycle transition: `ACTIVE` to run or resume, `PAUSED` to pause, or `CANCELLED` to cancel permanently. |
| `targeting` | `any` | No | Immutable in v1; including it returns 400. |

### internal_public_v1.BatchGetStatusRequest

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `campaignIds` | `string[]` | Yes | The campaign IDs to look up. Required. At most 100 per request. |

### internal_public_v1.BatchGetStatusResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `failures` | `internal_public_v1.CampaignIDFailure[]` | No | The IDs that could not be resolved. Omitted when every ID resolved. |
| `statuses` | `internal_public_v1.CampaignStatus[]` | No | One entry per successfully resolved campaign. |

### internal_public_v1.ListCreativesResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `creatives` | `internal_public_v1.Creative[]` | No | The page of creatives. |
| `nextPageToken` | `string` | No | The cursor for the next page. Pass it as pageToken to fetch the next page. Absent on the last page. |

### Roblox.Ads.Api.RecordClickRequest

A request model for an ad click.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `encryptedAdTrackingData` | `string` | No | The encrypted tracking data |
| `campaignTargetType` | `0 \| 1 \| 2 \| 3` | No | The campaign target type ['Undefined' = 0, 'Universe' = 1, 'Asset' = 2, 'ImmersiveAd' = 3] |
| `placementLocation` | `integer enum (8 values)` | No | The placement location ['Undefined' = 1, 'GameSort' = 2, 'AvatarShop' = 4, 'ItemDetails' = 8, 'HomePage' = 16, 'Billboard300x250' = 32, 'Billboard600x300' = 64, 'Billboard300x600' = 128] Values: 1, 2, 4, 8, 16, 32, 64, 128 |

### Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.Ads.Api.Models.Response.SponsoredPageResponse_

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | `Roblox.Ads.Api.Models.Response.SponsoredPageResponse[]` | No |  |

### Roblox.Ads.Api.Models.Response.CreateSponsoredItemCampaignResponse

The response model for serving a sponsored game.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `creatorTargetId` | `integer` | No | Id of the universe that is being sponsored. |
| `creatorType` | `string` | No | Type of the creator. |
| `creatorName` | `string` | No | Name of the creator. |

### Roblox.AdConfiguration.Api.GetSponsoredCampaignsResponse

A response model for retrieving a page of Roblox.AdConfiguration.Api.SponsoredCampaignModel.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `sponsoredCampaigns` | `Roblox.AdConfiguration.Api.SponsoredCampaignModel[]` | No | A collection of Roblox.AdConfiguration.Api.SponsoredCampaignModel. |
| `previousPageCursor` | `string` | No | The cursor for retrieving the previous page, if present. |
| `nextPageCursor` | `string` | No | The cursor for retrieving the next page, if present. |

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

### Roblox.AdConfiguration.Api.Models.GetEligibleCampaignTargetsRequest

A model represents a request to stop a sponsored campaign / ad.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `campaignTargetTypes` | `0 \| 1 \| 2 \| 3[]` | No | The list of campaign types we want to include in the results |
| `groupId` | `integer` | No | The group id, if applicable. |

### Roblox.AdConfiguration.Api.Models.GetCampaignTargetsResponse

The response model which returns a collection of Roblox.AdConfiguration.Api.Models.CampaignTargetModel

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `campaignTargetModels` | `Roblox.AdConfiguration.Api.Models.CampaignTargetModel[]` | No | Gets or sets a collection of Roblox.AdConfiguration.Api.Models.CampaignTargetModel |

### Roblox.AdConfiguration.Api.Models.StopSponsoredCampaignRequest

A model represents a request to stop a sponsored campaign / ad.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `adSetId` | `integer` | No | The ID of the ad set to stop. |

### Roblox.AdConfiguration.Api.GetSponsoredGamesResponse

A response model for retrieving a page of Roblox.AdConfiguration.Api.SponsoredGameV2Model.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `sponsoredGames` | `Roblox.AdConfiguration.Api.SponsoredGameV2Model[]` | No | A collection of Roblox.AdConfiguration.Api.SponsoredGameV2Model. |
| `previousPageCursor` | `string` | No | The cursor for retrieving the previous page, if present. |
| `nextPageCursor` | `string` | No | The cursor for retrieving the next page, if present. |

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

### Roblox.AdConfiguration.Api.Models.StopSponsoredGameV2Request

A model represents a request to stop a sponsored game ad.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `adSetId` | `integer` | No | Gets the ID of the ad set to stop. |

### Roblox.AdConfiguration.Api.Models.GetRecentAdsRankedUniversesResponse

The response model for getting a list of recent-ads-ranked universes.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `universes` | `Roblox.AdConfiguration.Api.Models.UniverseModel[]` | No | Gets or sets a list of Roblox.AdConfiguration.Api.Models.UniverseModel. |