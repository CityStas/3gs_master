---
name: "Trades"
last_updated: 2026-10-30T19:56:08Z
type: feature
api_base_url: "https://apis.roblox.com"
endpoints: 16
auth: [api-key, oauth2, cookie]
description: "Manage item trades between users on the Roblox platform"
---

# Trades

Manage item trades between users on the Roblox platform. [Check trade eligibility](#trades_get_v2_users__userId__can_trade_with) between users, [retrieve trade details](#trades_get_v2_trades__tradeId_), and [list trades by status](#trades_get_v1_trades__tradeStatusType_) (pending, completed, declined, expired).

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

### POST `/v1/trades/expire-outdated`

Deprecated. TradeSession are automatically set to expire while the inbound/outbound trades are fetched.
Expires Outdated Inbound Trades for User

**Server:** `https://trades.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

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
  "https://trades.roblox.com/v1/trades/expire-outdated"
```

### GET `/v1/trades/metadata` [EXPERIMENTAL]

Gets metadata about the trade system.

**Server:** `https://trades.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

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
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://trades.roblox.com/v1/trades/metadata"
```

### POST `/v1/trades/send`

Sends a trade.

**Server:** `https://trades.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

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
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://trades.roblox.com/v1/trades/send" \
  -H "Content-Type: application/json" \
  -d '{"key": "value"}'
```

### GET `/v1/trades/{tradeId}` [EXPERIMENTAL]

Gets detailed information about a trade.

**Server:** `https://trades.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `tradeId` | path | `integer` | Yes | The trade id. |

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
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://trades.roblox.com/v1/trades/{TRADEID}"
```

### POST `/v1/trades/{tradeId}/accept`

Accepts a trade.

**Server:** `https://trades.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `tradeId` | path | `integer` | Yes | The trade id. |

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
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://trades.roblox.com/v1/trades/{TRADEID}/accept"
```

### POST `/v1/trades/{tradeId}/counter`

Counters a trade.

**Server:** `https://trades.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `tradeId` | path | `integer` | Yes | The trade id. |

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
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://trades.roblox.com/v1/trades/{TRADEID}/counter" \
  -H "Content-Type: application/json" \
  -d '{"key": "value"}'
```

### POST `/v1/trades/{tradeId}/decline` [EXPERIMENTAL]

Declines a trade.

**Server:** `https://trades.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `tradeId` | path | `integer` | Yes | The trade id. |

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
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://trades.roblox.com/v1/trades/{TRADEID}/decline"
```

### GET `/v1/trades/{tradeStatusType}` [EXPERIMENTAL]

Fetches a list of the authenticated user's trades.

**Server:** `https://trades.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `tradeStatusType` | path | `1 \| 2 \| 3 \| 4` | Yes | The trade status type. Valid values: `1`, `2`, `3`, `4` |
| `limit` | query | `10 \| 25 \| 50 \| 100` | No | The number of results per request. Valid values: `10`, `25`, `50`, `100` |
| `cursor` | query | `string` | No | The paging cursor for the previous or next page. |
| `sortOrder` | query | `Asc \| Desc` | No | Sorted by trade creation date Valid values: `Asc`, `Desc` |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.Trades.Api.TradeResponse_`
- `400`: 1: Invalid trade status type.
- `401`: 0: Authorization has been denied for this request.

**Response fields** (`Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.Trades.Api.TradeResponse_`)

See [Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.Trades.Api.TradeResponse_](#roblox-web-webapi-models-apipageresponse-roblox-trades-api-traderesponse-) in Models.

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
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://trades.roblox.com/v1/trades/{TRADESTATUSTYPE}"
```

### GET `/v1/trades/{tradeStatusType}/count` [EXPERIMENTAL]

Gets the total number of pending trades for the authenticated user.
Inbound is the only accepted tradeStatusType.

**Server:** `https://trades.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `tradeStatusType` | path | `1 \| 2 \| 3 \| 4` | Yes | The trade status type to fetch a total count for. Valid values: `1`, `2`, `3`, `4` |

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
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://trades.roblox.com/v1/trades/{TRADESTATUSTYPE}/count"
```

### GET `/v1/users/{userId}/can-trade-with` [EXPERIMENTAL]

Returns whether you can trade with another user.

**Server:** `https://trades.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer` | Yes | The other user's id. |

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
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://trades.roblox.com/v1/users/{USERID}/can-trade-with"
```

### POST `/v2/trades/send`

Sends a new trade.

**Server:** `https://trades.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

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
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://trades.roblox.com/v2/trades/send" \
  -H "Content-Type: application/json" \
  -d '{"key": "value"}'
```

### GET `/v2/trades/{tradeId}` [EXPERIMENTAL]

Gets the details of a trade.

**Server:** `https://trades.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `tradeId` | path | `integer` | Yes | The id of the trade. |

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
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://trades.roblox.com/v2/trades/{TRADEID}"
```

### POST `/v2/trades/{tradeId}/counter`

Counters an existing trade.

**Server:** `https://trades.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `tradeId` | path | `integer` | Yes |  |

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
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://trades.roblox.com/v2/trades/{TRADEID}/counter" \
  -H "Content-Type: application/json" \
  -d '{"key": "value"}'
```

### GET `/v2/users/me/can-trade` [EXPERIMENTAL]

Checks if the calling user can trade with others.

**Server:** `https://trades.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

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
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://trades.roblox.com/v2/users/me/can-trade"
```

### GET `/v2/users/{userId}/can-trade-with` [EXPERIMENTAL]

Checks if the user can trade with a specific user.

**Server:** `https://trades.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer` | Yes |  |

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
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://trades.roblox.com/v2/users/{USERID}/can-trade-with"
```

### GET `/v2/users/{userId}/tradableItems` [EXPERIMENTAL]

Gets tradable items for a user.

**Server:** `https://trades.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer` | Yes | The id of the user. |
| `search` | query | `string` | No | Optional search query to filter items by. |
| `itemTargetTypes` | query | `string enum (18 values)[]` | No | Optional list of item target types to filter by. |
| `sortBy` | query | `Unknown \| CreationTime \| AcquisitionTime` | No | The key to sort tradable items by. Valid values: `Unknown`, `CreationTime`, `AcquisitionTime` |
| `sortOrder` | query | `0 \| 1 \| 2` | No | The sort order for the tradable items. Valid values: `0`, `1`, `2` |
| `limit` | query | `integer` | No | The maximum number of items to return. |
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
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://trades.roblox.com/v2/users/{USERID}/tradableItems"
```

## Models

### Roblox.Trades.Api.TradeMetadata

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `maxItemsPerSide` | `integer` | No |  |
| `minValueRatio` | `number` | No |  |
| `tradeSystemMaxRobuxPercent` | `number` | No |  |
| `tradeSystemRobuxFee` | `number` | No |  |

### Roblox.Trades.Api.NewTradeResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | `integer` | No | The trade id. |

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

### Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.Trades.Api.TradeResponse_

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `previousPageCursor` | `string` | No |  |
| `nextPageCursor` | `string` | No |  |
| `data` | `Roblox.Trades.Api.TradeResponse[]` | No |  |

### Roblox.Trades.Api.TradeCountResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `count` | `integer` | No |  |

### Roblox.Trades.Api.CanTradeResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `canTrade` | `boolean` | No | Returns true if you can trade with the given user. |
| `status` | `integer enum (9 values)` | No | If you can't trade with a user, status explains why you can't trade with them. ['Unknown' = 0, 'CanTrade' = 1, 'CannotTradeWithSelf' = 2, 'SenderCannotTrade' = 3, 'ReceiverCannotTrade' = 4, 'SenderPrivacyTooStrict' = 5, 'UsersCannotTrade' = 6, 'TradeAccepterNeedsFriction' = 7, 'SenderAgeCheckRequired' = 8] Values: 0, 1, 2, 3, 4, 5, 6, 7, 8 |

### Roblox.Trades.Api.Models.V2.NewTradeResponse

Represents a newly created trade.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `tradeId` | `integer` | No | The ID of the trade. |

### Roblox.Trades.Api.Models.V2.TradeDetailsResponse

The response for the TradeDetailsV2 endpoint.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `tradeId` | `integer` | No | The ID of the trade. |
| `status` | `string enum (11 values)` | No | The status of the trade. ['Unknown' = 1, 'Open' = 2, 'Pending' = 3, 'Completed' = 4, 'Expired' = 5, 'Declined' = 6, 'RejectedDueToError' = 7, 'Countered' = 8, 'Processing' = 9, 'InterventionRequired' = 10, 'TwoStepVerificationRequired' = 11] Values: Unknown, Open, Pending, Completed, Expired, Declined, RejectedDueToError, Countered, Processing, InterventionRequired, TwoStepVerificationRequired |
| `participantAOffer` | `Roblox.Trades.Api.Models.V2.TradeOffer` | No |  |
| `participantBOffer` | `Roblox.Trades.Api.Models.V2.TradeOffer` | No |  |

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

### Roblox.Trades.Api.Models.V2.GetUserTradableItemsResponse

The response for the GetUserTradableItems endpoint.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `userId` | `integer` | No | The ID of the user. |
| `items` | `Roblox.Trades.Api.Models.V2.TradableItem[]` | No | The items that the user can trade. |
| `nextPageCursor` | `string` | No | The cursor for the next page of items. |