---
name: "Trades Api v2"
last_updated: 2026-10-30T19:56:08Z
type: legacy
api_base_url: "https://trades.roblox.com"
versions: [v2, v1]
endpoints: 16
auth: [cookie]
---

# Trades Api v2

> **Warning:** Legacy APIs with cookie authentication can incorporate breaking changes without notice. We don't recommend them for production applications.

**Base URL:** `https://trades.roblox.com`
**Versions:** v2, v1

## V2

### GET `/v2/trades/{tradeId}`

Gets the details of a trade.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `tradeId` | path | `integer (int64)` | Yes | The id of the trade. |

**Responses:**

- `200`: OK → `Roblox.Trades.Api.Models.V2.TradeDetailsResponse`
- `400`: 0: An unknown error occured.
- `401`: 0: Authorization has been denied for this request. 4: You are not authorized to modify this trade.
- `403`: 4: You are not authorized to modify this trade.
- `404`: 0: An unknown error occured.

**Response fields** (`Roblox.Trades.Api.Models.V2.TradeDetailsResponse`)

See [Roblox.Trades.Api.Models.V2.TradeDetailsResponse](#roblox-trades-api-models-v2-tradedetailsresponse) in Models.

**Response example:**
```json
{
  "tradeId": 0,
  "status": "Unknown",
  "participantAOffer": {
    "user": {
      "id": "...",
      "name": "...",
      "displayName": "..."
    },
    "robux": 0,
    "items": [
      "..."
    ]
  },
  "participantBOffer": {
    "user": {
      "id": "...",
      "name": "...",
      "displayName": "..."
    },
    "robux": 0,
    "items": [
      "..."
    ]
  }
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://trades.roblox.com/v2/trades/{TRADEID}"
```

### GET `/v2/users/{userId}/can-trade-with`

Checks if the user can trade with a specific user.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer (int64)` | Yes |  |

**Responses:**

- `200`: OK → `Roblox.Trades.Api.Models.V2.CanTradeWithResponse`
- `401`: 0: Authorization has been denied for this request. 4: You are not authorized to modify this trade.

**Response fields** (`Roblox.Trades.Api.Models.V2.CanTradeWithResponse`)

See [Roblox.Trades.Api.Models.V2.CanTradeWithResponse](#roblox-trades-api-models-v2-cantradewithresponse) in Models.

**Response example:**
```json
{
  "userId": 0,
  "targetUserId": 0,
  "canTrade": false,
  "mutualTradeEligibility": "Unknown",
  "currencyTransferEligibility": {
    "canSend": false,
    "canRequest": false
  }
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://trades.roblox.com/v2/users/{USERID}/can-trade-with"
```

### GET `/v2/users/{userId}/tradableItems`

Gets tradable items for a user.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer (int64)` | Yes | The id of the user. |
| `search` | query | `string` | No | Optional search query to filter items by. |
| `itemTargetTypes` | query | `array` | No | Optional list of item target types to filter by. |
| `sortBy` | query | `string` | No | The key to sort tradable items by. Valid values: `Unknown`, `CreationTime`, `AcquisitionTime` |
| `sortOrder` | query | `integer (int32)` | No | The sort order for the tradable items. Valid values: `0`, `1`, `2` |
| `limit` | query | `integer (int32)` | No | The maximum number of items to return. |
| `cursor` | query | `string` | No | The pagination cursor. |

**Responses:**

- `200`: OK → `Roblox.Trades.Api.Models.V2.GetUserTradableItemsResponse`
- `400`: 25: The cursor provided is invalid.
- `401`: 0: Authorization has been denied for this request. 4: You are not authorized to modify this trade.
- `403`: 4: You are not authorized to modify this trade.
- `404`: 0: An unknown error occured.

**Response fields** (`Roblox.Trades.Api.Models.V2.GetUserTradableItemsResponse`)

See [Roblox.Trades.Api.Models.V2.GetUserTradableItemsResponse](#roblox-trades-api-models-v2-getusertradableitemsresponse) in Models.

**Response example:**
```json
{
  "userId": 0,
  "items": [
    {
      "collectibleItemId": "...",
      "itemTarget": "...",
      "itemName": "...",
      "originalPrice": "...",
      "recentAveragePrice": "...",
      "assetStock": "..."
    }
  ],
  "nextPageCursor": "string"
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://trades.roblox.com/v2/users/{USERID}/tradableItems"
```

### GET `/v2/users/me/can-trade`

Checks if the calling user can trade with others.

**Responses:**

- `200`: OK → `Roblox.Trades.Api.Models.V2.CanTradeResponse`
- `401`: 0: Authorization has been denied for this request. 4: You are not authorized to modify this trade.

**Response fields** (`Roblox.Trades.Api.Models.V2.CanTradeResponse`)

See [Roblox.Trades.Api.Models.V2.CanTradeResponse](#roblox-trades-api-models-v2-cantraderesponse) in Models.

**Response example:**
```json
{
  "userId": 0,
  "canTrade": false,
  "tradeEligibility": "Unknown",
  "freeTradesAllowance": {
    "limit": 0,
    "remaining": 0,
    "window": "day"
  },
  "currencyTransferEligibility": {
    "canSend": false,
    "canRequest": false
  }
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://trades.roblox.com/v2/users/me/can-trade"
```

### POST `/v2/trades/{tradeId}/counter`

Counters an existing trade.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `tradeId` | path | `integer (int64)` | Yes |  |

**Request Body:** `application/json` — Type: `Roblox.Trades.Api.Models.V2.TradeRequest`

See [Roblox.Trades.Api.Models.V2.TradeRequest](#roblox-trades-api-models-v2-traderequest) in Models.

**Request example:**
```json
{
  "senderOffer": {
    "userId": 0,
    "robux": 0,
    "collectibleItemInstanceIds": [
      "..."
    ]
  },
  "recipientOffer": {
    "userId": 0,
    "robux": 0,
    "collectibleItemInstanceIds": [
      "..."
    ]
  }
}
```

**Responses:**

- `200`: OK → `Roblox.Trades.Api.Models.V2.NewTradeResponse`
- `401`: 0: Authorization has been denied for this request. 4: You are not authorized to modify this trade.
- `403`: 0: Token Validation Failed
- `404`: 0: An unknown error occured.

**Response fields** (`Roblox.Trades.Api.Models.V2.NewTradeResponse`)

See [Roblox.Trades.Api.Models.V2.NewTradeResponse](#roblox-trades-api-models-v2-newtraderesponse) in Models.

**Response example:**
```json
{
  "tradeId": 0
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://trades.roblox.com/v2/trades/{TRADEID}/counter" \
  -H "Content-Type: application/json" \
  -d '{
  "senderOffer": {
    "userId": 0,
    "robux": 0,
    "collectibleItemInstanceIds": [
      "..."
    ]
  },
  "recipientOffer": {
    "userId": 0,
    "robux": 0,
    "collectibleItemInstanceIds": [
      "..."
    ]
  }
}'
```

### POST `/v2/trades/send`

Sends a new trade.

**Request Body:** `application/json` — Type: `Roblox.Trades.Api.Models.V2.TradeRequest`

See [Roblox.Trades.Api.Models.V2.TradeRequest](#roblox-trades-api-models-v2-traderequest) in Models.

**Request example:**
```json
{
  "senderOffer": {
    "userId": 0,
    "robux": 0,
    "collectibleItemInstanceIds": [
      "..."
    ]
  },
  "recipientOffer": {
    "userId": 0,
    "robux": 0,
    "collectibleItemInstanceIds": [
      "..."
    ]
  }
}
```

**Responses:**

- `200`: OK → `Roblox.Trades.Api.Models.V2.NewTradeResponse`
- `401`: 0: Authorization has been denied for this request. 4: You are not authorized to modify this trade.
- `403`: 0: Token Validation Failed
- `404`: 0: An unknown error occured.

**Response fields** (`Roblox.Trades.Api.Models.V2.NewTradeResponse`)

See [Roblox.Trades.Api.Models.V2.NewTradeResponse](#roblox-trades-api-models-v2-newtraderesponse) in Models.

**Response example:**
```json
{
  "tradeId": 0
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://trades.roblox.com/v2/trades/send" \
  -H "Content-Type: application/json" \
  -d '{
  "senderOffer": {
    "userId": 0,
    "robux": 0,
    "collectibleItemInstanceIds": [
      "..."
    ]
  },
  "recipientOffer": {
    "userId": 0,
    "robux": 0,
    "collectibleItemInstanceIds": [
      "..."
    ]
  }
}'
```

## Models

### Roblox.Trades.Api.Models.V2.CanTradeResponse

The response for the CanTrade endpoint.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `userId` | `integer` | No | The ID of the user. |
| `canTrade` | `boolean` | No | Whether the user can trade or not. |
| `tradeEligibility` | `string enum (9 values)` | No | The trade eligibility status of the user. ['Unknown' = 0, 'Eligible' = 1, 'IneligibleTradeSystemDisabled' = 2, 'IneligibleCannotTradeWithRoblox' = 3, 'IneligibleUserNotFound' = 4, 'IneligibleMissingPremiumMembership' = 5, 'IneligibleLegalOrRegulatoryRestrictions' = 6, 'IneligibleFreeTradesLimitReached' = 7, 'IneligibleAgeCheckRequired' = 8] Values: Unknown, Eligible, IneligibleTradeSystemDisabled, IneligibleCannotTradeWithRoblox, IneligibleUserNotFound, IneligibleMissingPremiumMembership, IneligibleLegalOrRegulatoryRestrictions, IneligibleFreeTradesLimitReached, IneligibleAgeCheckRequired |
| `freeTradesAllowance` | `Roblox.Trades.Api.Models.V2.FreeTradesAllowanceResponse` | No |  |
| `currencyTransferEligibility` | `Roblox.Trades.Api.Models.V2.CurrencyTransferEligibilityResponse` | No |  |

### Roblox.Trades.Api.Models.V2.CanTradeWithResponse

The response for the CanTradeWith endpoint.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `userId` | `integer` | No | The ID of the user. |
| `targetUserId` | `integer` | No | The ID of the target user. |
| `canTrade` | `boolean` | No | Whether the user can trade with the target user or not. |
| `mutualTradeEligibility` | `string enum (7 values)` | No | The mutual trade eligibility status between the two users. ['Unknown' = 0, 'Eligible' = 1, 'CallingUserIneligible' = 2, 'TargetUserIneligible' = 3, 'CannotTradeWithSelf' = 4, 'CallingUserPrivacySettingsRestricted' = 5, 'CallingUserAgeCheckRequired' = 6] Values: Unknown, Eligible, CallingUserIneligible, TargetUserIneligible, CannotTradeWithSelf, CallingUserPrivacySettingsRestricted, CallingUserAgeCheckRequired |
| `currencyTransferEligibility` | `Roblox.Trades.Api.Models.V2.CurrencyTransferEligibilityResponse` | No |  |

### Roblox.Trades.Api.Models.V2.CurrencyTransferEligibilityResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `canSend` | `boolean` | No |  |
| `canRequest` | `boolean` | No |  |

### Roblox.Trades.Api.Models.V2.FreeTradesAllowanceResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `limit` | `integer` | No |  |
| `remaining` | `integer` | No |  |
| `window` | `day \| week \| month \| year \| lifetime` | No | ['Day' = 1, 'Week' = 2, 'Month' = 3, 'Year' = 4, 'Lifetime' = 5] |

### Roblox.Trades.Api.Models.V2.GetUserTradableItemsResponse

The response for the GetUserTradableItems endpoint.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `userId` | `integer` | No | The ID of the user. |
| `items` | `Roblox.Trades.Api.Models.V2.TradableItem[]` | No | The items that the user can trade. |
| `nextPageCursor` | `string` | No | The cursor for the next page of items. |

### Roblox.Trades.Api.Models.V2.ItemTarget

The underlying of a tradable item.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `itemType` | `Unknown \| Asset \| Bundle` | No | The type of the underlying. ['Unknown' = 0, 'Asset' = 1, 'Bundle' = 2] |
| `targetId` | `string` | No | The id of the underlying. |

### Roblox.Trades.Api.Models.V2.NewTradeResponse

Represents a newly created trade.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `tradeId` | `integer` | No | The ID of the trade. |

### Roblox.Trades.Api.Models.V2.TradableItem

A tradable item.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `collectibleItemId` | `string` | No | The collectible item id. |
| `itemTarget` | `Roblox.Trades.Api.Models.V2.ItemTarget` | No |  |
| `itemName` | `string` | No | The name of the item. |
| `originalPrice` | `integer` | No | The original price of the item. |
| `recentAveragePrice` | `integer` | No | The recent average price of the item. |
| `assetStock` | `integer` | No | Total quantity of the item. |
| `instances` | `Roblox.Trades.Api.Models.V2.TradableItemInstance[]` | No |  |

### Roblox.Trades.Api.Models.V2.TradableItemInstance

A tradable item instance.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `collectibleItemInstanceId` | `string` | No | The collectible item instance id. |
| `itemTarget` | `Roblox.Trades.Api.Models.V2.ItemTarget` | No |  |
| `itemName` | `string` | No | The name of the item. |
| `serialNumber` | `integer` | No | The serial number of the item if it is LimitedUnique. |
| `originalPrice` | `integer` | No | The original price of the item. |
| `recentAveragePrice` | `integer` | No | The recent average price of the item. |
| `assetStock` | `integer` | No | Total quantity of the item. |
| `isOnHold` | `boolean` | No | Whether the item is on hold. |

### Roblox.Trades.Api.Models.V2.TradeDetailsResponse

The response for the TradeDetailsV2 endpoint.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `tradeId` | `integer` | No | The ID of the trade. |
| `status` | `string enum (11 values)` | No | The status of the trade. ['Unknown' = 1, 'Open' = 2, 'Pending' = 3, 'Completed' = 4, 'Expired' = 5, 'Declined' = 6, 'RejectedDueToError' = 7, 'Countered' = 8, 'Processing' = 9, 'InterventionRequired' = 10, 'TwoStepVerificationRequired' = 11] Values: Unknown, Open, Pending, Completed, Expired, Declined, RejectedDueToError, Countered, Processing, InterventionRequired, TwoStepVerificationRequired |
| `participantAOffer` | `Roblox.Trades.Api.Models.V2.TradeOffer` | No |  |
| `participantBOffer` | `Roblox.Trades.Api.Models.V2.TradeOffer` | No |  |

### Roblox.Trades.Api.Models.V2.TradeOffer

Represents a trade offer.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `user` | `Roblox.Web.Responses.Users.SkinnyUserResponse` | No |  |
| `robux` | `integer` | No | The amount of Robux in the trade offer. |
| `items` | `Roblox.Trades.Api.Models.V2.TradableItemInstance[]` | No | The items in the trade offer. |

### Roblox.Trades.Api.Models.V2.TradeOfferRequest

Represents a trade offer.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `userId` | `integer` | No | The user ID of the offer. |
| `robux` | `integer` | No | The amount of Robux in the trade offer. |
| `collectibleItemInstanceIds` | `string[]` | No | List of items in the trade offer. |

### Roblox.Trades.Api.Models.V2.TradeRequest

Represents a trade request. The calling user must be either participant A or B in the trade.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `senderOffer` | `Roblox.Trades.Api.Models.V2.TradeOfferRequest` | No |  |
| `recipientOffer` | `Roblox.Trades.Api.Models.V2.TradeOfferRequest` | No |  |

### Roblox.Web.Responses.Users.SkinnyUserResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | `integer` | No |  |
| `name` | `string` | No |  |
| `displayName` | `string` | No |  |

## V1

### GET `/v1/trades/{tradeId}`

Gets detailed information about a trade.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `tradeId` | path | `integer (int64)` | Yes | The trade id. |

**Responses:**

- `200`: OK → `Roblox.Trades.Api.TradeDetailResponse`
- `400`: 2: The trade cannot be found or you are not authorized to view it.
- `401`: 0: Authorization has been denied for this request. 4: You are not authorized to modify this trade.
- `404`: 2: The trade cannot be found or you are not authorized to view it.
- `500`: 0: An unknown error occured.

**Response fields** (`Roblox.Trades.Api.TradeDetailResponse`)

See [Roblox.Trades.Api.TradeDetailResponse](#roblox-trades-api-tradedetailresponse) in Models.

**Response example:**
```json
{
  "offers": [
    {
      "user": "...",
      "userAssets": "...",
      "robux": "..."
    }
  ],
  "id": 0,
  "user": {
    "id": 0,
    "name": "string",
    "displayName": "string"
  },
  "created": "2024-01-01T00:00:00Z",
  "expiration": "2024-01-01T00:00:00Z",
  "isActive": false
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://trades.roblox.com/v1/trades/{TRADEID}"
```

### GET `/v1/trades/{tradeStatusType}`

Fetches a list of the authenticated user's trades.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `tradeStatusType` | path | `integer (int32)` | Yes | The trade status type. Valid values: `1`, `2`, `3`, `4` |
| `limit` | query | `integer (int32)` | No | The number of results per request. Valid values: `10`, `25`, `50`, `100` |
| `cursor` | query | `string` | No | The paging cursor for the previous or next page. |
| `sortOrder` | query | `string` | No | Sorted by trade creation date Valid values: `Asc`, `Desc` |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiPageResponse[Roblox.Trades.Api.TradeResponse]`
- `400`: 1: Invalid trade status type.
- `401`: 0: Authorization has been denied for this request.

**Response fields** (`Roblox.Web.WebAPI.Models.ApiPageResponse[Roblox.Trades.Api.TradeResponse]`)

See [Roblox.Web.WebAPI.Models.ApiPageResponse[Roblox.Trades.Api.TradeResponse]](#roblox-web-webapi-models-apipageresponse-roblox-trades-api-traderesponse-) in Models.

**Response example:**
```json
{
  "previousPageCursor": "string",
  "nextPageCursor": "string",
  "data": [
    {
      "id": "...",
      "user": "...",
      "created": "...",
      "expiration": "...",
      "isActive": "...",
      "status": "..."
    }
  ]
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://trades.roblox.com/v1/trades/{TRADESTATUSTYPE}"
```

### GET `/v1/trades/{tradeStatusType}/count`

Gets the total number of pending trades for the authenticated user.
Inbound is the only accepted tradeStatusType.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `tradeStatusType` | path | `integer (int32)` | Yes | The trade status type to fetch a total count for. Valid values: `1`, `2`, `3`, `4` |

**Responses:**

- `200`: OK → `Roblox.Trades.Api.TradeCountResponse`
- `400`: 1: Invalid trade status type.
- `401`: 0: Authorization has been denied for this request.

**Response fields** (`Roblox.Trades.Api.TradeCountResponse`)

See [Roblox.Trades.Api.TradeCountResponse](#roblox-trades-api-tradecountresponse) in Models.

**Response example:**
```json
{
  "count": 0
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://trades.roblox.com/v1/trades/{TRADESTATUSTYPE}/count"
```

### GET `/v1/trades/metadata`

Gets metadata about the trade system.

**Responses:**

- `200`: OK → `Roblox.Trades.Api.TradeMetadata`
- `401`: 0: Authorization has been denied for this request.

**Response fields** (`Roblox.Trades.Api.TradeMetadata`)

See [Roblox.Trades.Api.TradeMetadata](#roblox-trades-api-trademetadata) in Models.

**Response example:**
```json
{
  "maxItemsPerSide": 0,
  "minValueRatio": 0,
  "tradeSystemMaxRobuxPercent": 0,
  "tradeSystemRobuxFee": 0
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://trades.roblox.com/v1/trades/metadata"
```

### GET `/v1/users/{userId}/can-trade-with`

Returns whether you can trade with another user.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer (int64)` | Yes | The other user's id. |

**Responses:**

- `200`: OK → `Roblox.Trades.Api.CanTradeResponse`
- `400`: 10: Invalid trade partner. See field for whether the invalid partner is the sender or receiver.
- `401`: 0: Authorization has been denied for this request.

**Response fields** (`Roblox.Trades.Api.CanTradeResponse`)

See [Roblox.Trades.Api.CanTradeResponse](#roblox-trades-api-cantraderesponse) in Models.

**Response example:**
```json
{
  "canTrade": false,
  "status": 0
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://trades.roblox.com/v1/users/{USERID}/can-trade-with"
```

### POST `/v1/trades/{tradeId}/accept`

Accepts a trade.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `tradeId` | path | `integer (int64)` | Yes | The trade id. |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: 2: The trade cannot be found or you are not authorized to view it. 3: The trade is inactive. 4: You are not authorized to modify this trade. 6: Trade needs to be confirmed by the other party. 6: Trade needs to be confirmed by the other party. 7: The user cannot trade. See field for whether the user who cannot trade is the sender or receiver. 23: The trade reaches Two Step Verification thresholds and the user has not verified in the past time threshold.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed
- `503`: 5: Trading system is unavailable

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://trades.roblox.com/v1/trades/{TRADEID}/accept"
```

### POST `/v1/trades/{tradeId}/counter`

Counters a trade.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `tradeId` | path | `integer (int64)` | Yes | The trade id. |

**Request Body:** `application/json` — Type: `Roblox.Trades.Api.TradeRequest`

See [Roblox.Trades.Api.TradeRequest](#roblox-trades-api-traderequest) in Models.

**Request example:**
```json
{
  "offers": [
    {
      "userId": "...",
      "userAssetIds": "...",
      "robux": "..."
    }
  ]
}
```

**Responses:**

- `200`: OK → `Roblox.Trades.Api.NewTradeResponse`
- `400`: 2: The trade cannot be found or you are not authorized to view it. 4: You are not authorized to modify this trade. 7: The user cannot trade. See field for whether the user who cannot trade is the sender or receiver. 8: The trade request should include offers. 9: Invalid number of trade offers. 10: Invalid trade partner. See field for whether the invalid partner is the sender or receiver. 11: Cannot add negative Robux amounts to a trade. 12: One or more userAssets are invalid. See fieldData for details. 13: Invalid number of userAssets in one side of the trade. 15: The trade is unbalanced. 16: Trade value ratio is not sufficient. 17: You have insufficient Robux to make this offer. 18: Too many Robux in one side of the offer. See field for whether the side is the sender or receiver. 19: Unknown error while processing the trade. 21: Cannot trade with yourself. 22: User's privacy settings are too strict to allow trading. See field for whether the user is the sender or receiver.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed
- `429`: 14: You are sending too many trade requests. Please slow down and try again later.
- `502`: 0: An unknown error occured.
- `503`: 5: Trading system is unavailable

**Response fields** (`Roblox.Trades.Api.NewTradeResponse`)

See [Roblox.Trades.Api.NewTradeResponse](#roblox-trades-api-newtraderesponse) in Models.

**Response example:**
```json
{
  "id": 0
}
```

**Error handling:** `429`: Retry with exponential backoff (start at 1s). `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://trades.roblox.com/v1/trades/{TRADEID}/counter" \
  -H "Content-Type: application/json" \
  -d '{
  "offers": [
    {
      "userId": "...",
      "userAssetIds": "...",
      "robux": "..."
    }
  ]
}'
```

### POST `/v1/trades/{tradeId}/decline`

Declines a trade.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `tradeId` | path | `integer (int64)` | Yes | The trade id. |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: 2: The trade cannot be found or you are not authorized to view it. 3: The trade is inactive. 4: You are not authorized to modify this trade. 7: The user cannot trade. See field for whether the user who cannot trade is the sender or receiver.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed
- `503`: 5: Trading system is unavailable

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://trades.roblox.com/v1/trades/{TRADEID}/decline"
```

### POST `/v1/trades/expire-outdated`

Deprecated. TradeSession are automatically set to expire while the inbound/outbound trades are fetched.
Expires Outdated Inbound Trades for User

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://trades.roblox.com/v1/trades/expire-outdated"
```

### POST `/v1/trades/send`

Sends a trade.

**Request Body:** `application/json` — Type: `Roblox.Trades.Api.TradeRequest`

See [Roblox.Trades.Api.TradeRequest](#roblox-trades-api-traderequest) in Models.

**Request example:**
```json
{
  "offers": [
    {
      "userId": "...",
      "userAssetIds": "...",
      "robux": "..."
    }
  ]
}
```

**Responses:**

- `200`: OK → `Roblox.Trades.Api.NewTradeResponse`
- `400`: 7: The user cannot trade. See field for whether the user who cannot trade is the sender or receiver. 8: The trade request should include offers. 9: Invalid number of trade offers. 10: Invalid trade partner. See field for whether the invalid partner is the sender or receiver. 11: Cannot add negative Robux amounts to a trade. 12: One or more userAssets are invalid. See fieldData for details. 13: Invalid number of userAssets in one side of the trade. 15: The trade is unbalanced. 16: Trade value ratio is not sufficient. 17: You have insufficient Robux to make this offer. 18: Too many Robux in one side of the offer. See field for whether the side is the sender or receiver. 19: Unknown error while processing the trade. 21: Cannot trade with yourself. 22: User's privacy settings are too strict to allow trading. See field for whether the user is the sender or receiver. 23: The trade reaches Two Step Verification thresholds and the user has not verified in the past time threshold.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed
- `429`: 14: You are sending too many trade requests. Please slow down and try again later.
- `502`: 0: An unknown error occured.
- `503`: 5: Trading system is unavailable

**Response fields** (`Roblox.Trades.Api.NewTradeResponse`)

See [Roblox.Trades.Api.NewTradeResponse](#roblox-trades-api-newtraderesponse) in Models.

**Response example:**
```json
{
  "id": 0
}
```

**Error handling:** `429`: Retry with exponential backoff (start at 1s). `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://trades.roblox.com/v1/trades/send" \
  -H "Content-Type: application/json" \
  -d '{
  "offers": [
    {
      "userId": "...",
      "userAssetIds": "...",
      "robux": "..."
    }
  ]
}'
```

## Models

### Roblox.Trades.Api.CanTradeResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `canTrade` | `boolean` | No | Returns true if you can trade with the given user. |
| `status` | `integer enum (9 values)` | No | If you can't trade with a user, status explains why you can't trade with them. ['Unknown' = 0, 'CanTrade' = 1, 'CannotTradeWithSelf' = 2, 'SenderCannotTrade' = 3, 'ReceiverCannotTrade' = 4, 'SenderPrivacyTooStrict' = 5, 'UsersCannotTrade' = 6, 'TradeAccepterNeedsFriction' = 7, 'SenderAgeCheckRequired' = 8] Values: 0, 1, 2, 3, 4, 5, 6, 7, 8 |

### Roblox.Trades.Api.NewTradeResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | `integer` | No | The trade id. |

### Roblox.Trades.Api.TradeCountResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `count` | `integer` | No |  |

### Roblox.Trades.Api.TradeDetailResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `offers` | `Roblox.Trades.Api.TradeOfferResponse[]` | No |  |
| `id` | `integer` | No |  |
| `user` | `Roblox.Web.Responses.Users.SkinnyUserResponse` | No |  |
| `created` | `string` | No |  |
| `expiration` | `string` | No |  |
| `isActive` | `boolean` | No |  |
| `status` | `string enum (11 values)` | No | ['Unknown' = 1, 'Open' = 2, 'Pending' = 3, 'Completed' = 4, 'Expired' = 5, 'Declined' = 6, 'RejectedDueToError' = 7, 'Countered' = 8, 'Processing' = 9, 'InterventionRequired' = 10, 'TwoStepVerificationRequired' = 11] Values: Unknown, Open, Pending, Completed, Expired, Declined, RejectedDueToError, Countered, Processing, InterventionRequired, TwoStepVerificationRequired |

### Roblox.Trades.Api.TradeMetadata

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `maxItemsPerSide` | `integer` | No |  |
| `minValueRatio` | `number` | No |  |
| `tradeSystemMaxRobuxPercent` | `number` | No |  |
| `tradeSystemRobuxFee` | `number` | No |  |

### Roblox.Trades.Api.TradeOfferRequest

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `userId` | `integer` | No |  |
| `userAssetIds` | `integer[]` | No |  |
| `robux` | `integer` | No |  |

### Roblox.Trades.Api.TradeOfferResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `user` | `Roblox.Web.Responses.Users.SkinnyUserResponse` | No |  |
| `userAssets` | `Roblox.Trades.Api.UserAssetResponse[]` | No |  |
| `robux` | `integer` | No |  |

### Roblox.Trades.Api.TradeRequest

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `offers` | `Roblox.Trades.Api.TradeOfferRequest[]` | No |  |

### Roblox.Trades.Api.TradeResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | `integer` | No |  |
| `user` | `Roblox.Web.Responses.Users.SkinnyUserResponse` | No |  |
| `created` | `string` | No |  |
| `expiration` | `string` | No |  |
| `isActive` | `boolean` | No |  |
| `status` | `string enum (11 values)` | No | ['Unknown' = 1, 'Open' = 2, 'Pending' = 3, 'Completed' = 4, 'Expired' = 5, 'Declined' = 6, 'RejectedDueToError' = 7, 'Countered' = 8, 'Processing' = 9, 'InterventionRequired' = 10, 'TwoStepVerificationRequired' = 11] Values: Unknown, Open, Pending, Completed, Expired, Declined, RejectedDueToError, Countered, Processing, InterventionRequired, TwoStepVerificationRequired |

### Roblox.Trades.Api.UserAssetResponse

A model containing information about a UserAsset.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | `integer` | No | The user asset id |
| `serialNumber` | `integer` | No | The serial number of the user asset |
| `assetId` | `integer` | No | The asset id of the user asset |
| `name` | `string` | No | The asset name of the asset |
| `recentAveragePrice` | `integer` | No | The recent average price of the asset |
| `originalPrice` | `integer` | No | The original price of the asset |
| `assetStock` | `integer` | No | The asset stock. |
| `membershipType` | `0 \| 1 \| 2 \| 3 \| 4` | No | The minimum MembershipType required to own the userAsset. ['None' = 0, 'BC' = 1, 'TBC' = 2, 'OBC' = 3, 'RobloxPremium' = 4] |

### Roblox.Web.Responses.Users.SkinnyUserResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | `integer` | No |  |
| `name` | `string` | No |  |
| `displayName` | `string` | No |  |

### Roblox.Web.WebAPI.Models.ApiPageResponse[Roblox.Trades.Api.TradeResponse]

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `previousPageCursor` | `string` | No |  |
| `nextPageCursor` | `string` | No |  |
| `data` | `Roblox.Trades.Api.TradeResponse[]` | No |  |