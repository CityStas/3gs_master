---
name: "Private servers"
last_updated: 2026-10-30T19:56:08Z
type: feature
api_base_url: "https://apis.roblox.com"
endpoints: 9
auth: [api-key, oauth2, cookie]
description: "Create and manage private servers for your experiences, including server creation, access control, and subscription management"
---

# Private servers

Create and manage private servers for your experiences, including server creation, access control, and subscription management.

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

### POST `/v1/games/vip-servers/{universeId}`

**Server:** `https://games.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer` | Yes |  |

**Request Body:** `application/json` — Type: `any`

**Responses:**

- `200`: OK → `PrivateServersApi.GameServerResponse`

**Response fields** (`PrivateServersApi.GameServerResponse`)

See [PrivateServersApi.GameServerResponse](#privateserversapi-gameserverresponse) in Models.

**Response example:**
```json
{
  "id": "string",
  "maxPlayers": 0,
  "playing": 0,
  "playerTokens": [
    "string"
  ],
  "players": [
    {
      "id": "...",
      "name": "...",
      "displayName": "...",
      "playerToken": "..."
    }
  ],
  "fps": 0
}
```

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://games.roblox.com/v1/games/vip-servers/{UNIVERSEID}" \
  -H "Content-Type: application/json" \
  -d '"..."'
```

### GET `/v1/games/{placeId}/private-servers` [EXPERIMENTAL]

**Server:** `https://games.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `placeId` | path | `integer` | Yes |  |
| `exclusiveStartKeyCursor` | query | `any` | No |  |
| `excludeFriendServers` | query | `boolean` | No |  |

**Responses:**

- `200`: OK → `GetPrivateServerListResponse`

**Response fields** (`GetPrivateServerListResponse`)

See [GetPrivateServerListResponse](#getprivateserverlistresponse) in Models.

**Response example:**
```json
{
  "data": [
    {
      "id": "...",
      "maxPlayers": "...",
      "playing": "...",
      "playerTokens": "...",
      "players": "...",
      "fps": "..."
    }
  ],
  "previousPageCursor": "string",
  "nextPageCursor": "string",
  "gameJoinRestricted": false
}
```

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://games.roblox.com/v1/games/{PLACEID}/private-servers"
```

### GET `/v1/private-servers/enabled-in-universe/{universeId}`

**Server:** `https://games.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer` | Yes |  |

**Responses:**

- `200`: OK → `PrivateServersEnabledInUniverseResponse`

**Response fields** (`PrivateServersEnabledInUniverseResponse`)

See [PrivateServersEnabledInUniverseResponse](#privateserversenabledinuniverseresponse) in Models.

**Response example:**
```json
{
  "privateServersEnabled": false
}
```

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://games.roblox.com/v1/private-servers/enabled-in-universe/{UNIVERSEID}"
```

### GET `/v1/private-servers/my-private-servers`

**Server:** `https://games.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `privateServersTab` | query | `any` | No |  |
| `itemsPerPage` | query | `integer` | No |  |
| `cursor` | query | `string` | No |  |

**Responses:**

- `200`: OK → `MyPrivateServersResponse`

**Response fields** (`MyPrivateServersResponse`)

See [MyPrivateServersResponse](#myprivateserversresponse) in Models.

**Response example:**
```json
{
  "nextPageCursor": "string",
  "previousPageCursor": "string",
  "data": [
    {
      "active": "...",
      "universeId": "...",
      "placeId": "...",
      "name": "...",
      "ownerId": "...",
      "ownerName": "..."
    }
  ]
}
```

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://games.roblox.com/v1/private-servers/my-private-servers"
```

### GET `/v1/universes/{universeId}/configuration/vip-servers` [EXPERIMENTAL]

Get settings for an owned universe's VIP servers.

**Server:** `https://develop.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer` | Yes | The universe Id. |

**Responses:**

- `200`: OK → `Roblox.Api.Develop.Models.PrivateServerDetailsResponse`
- `400`: 1: The universe does not exist.
- `401`: 0: Authorization has been denied for this request.
- `403`: 2: You are not authorized to configure this universe.

**Response fields** (`Roblox.Api.Develop.Models.PrivateServerDetailsResponse`)

See [Roblox.Api.Develop.Models.PrivateServerDetailsResponse](#roblox-api-develop-models-privateserverdetailsresponse) in Models.

**Response example:**
```json
{
  "isEnabled": false,
  "price": 0,
  "activeServersCount": 0,
  "activeSubscriptionsCount": 0
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://develop.roblox.com/v1/universes/{UNIVERSEID}/configuration/vip-servers"
```

### GET `/v1/vip-server/can-invite/{userId}`

**Server:** `https://games.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer` | Yes |  |

**Responses:**

- `200`: OK → `CanInviteUserResponse`

**Response fields** (`CanInviteUserResponse`)

See [CanInviteUserResponse](#caninviteuserresponse) in Models.

**Response example:**
```json
{
  "canInvite": false,
  "doesOwnerPrivacyRestrictJoins": false,
  "inviteResponseType": "..."
}
```

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://games.roblox.com/v1/vip-server/can-invite/{USERID}"
```

### GET `/v1/vip-servers/my-private-servers`

**Server:** `https://games.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `privateServersTab` | query | `any` | No |  |
| `itemsPerPage` | query | `integer` | No |  |
| `cursor` | query | `string` | No |  |

**Responses:**

- `200`: OK → `MyPrivateServersResponse`

**Response fields** (`MyPrivateServersResponse`)

See [MyPrivateServersResponse](#myprivateserversresponse) in Models.

**Response example:**
```json
{
  "nextPageCursor": "string",
  "previousPageCursor": "string",
  "data": [
    {
      "active": "...",
      "universeId": "...",
      "placeId": "...",
      "name": "...",
      "ownerId": "...",
      "ownerName": "..."
    }
  ]
}
```

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://games.roblox.com/v1/vip-servers/my-private-servers"
```

### PATCH `/v1/vip-servers/{id}`

**Server:** `https://games.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `id` | path | `integer` | Yes |  |

**Request Body:** `application/json` — Type: `any`

**Responses:**

- `200`: OK → `PrivateServerResponse`

**Response fields** (`PrivateServerResponse`)

See [PrivateServerResponse](#privateserverresponse) in Models.

**Response example:**
```json
{
  "id": 0,
  "name": "string",
  "game": "...",
  "joinCode": "string",
  "active": false,
  "subscription": "..."
}
```

**Example:**
```bash
curl -X PATCH -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://games.roblox.com/v1/vip-servers/{ID}" \
  -H "Content-Type: application/json" \
  -d '"..."'
```

### PATCH `/v1/vip-servers/{id}/subscription`

**Server:** `https://games.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `id` | path | `integer` | Yes |  |

**Request Body:** `application/json` — Type: `any`

**Responses:**

- `200`: OK → `PrivateServerSubscriptionResponse`

**Response fields** (`PrivateServerSubscriptionResponse`)

See [PrivateServerSubscriptionResponse](#privateserversubscriptionresponse) in Models.

**Response example:**
```json
{
  "active": false,
  "expired": false,
  "expirationDate": "2024-01-01T00:00:00Z",
  "price": 0,
  "canRenew": false,
  "hasInsufficientFunds": false
}
```

**Example:**
```bash
curl -X PATCH -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://games.roblox.com/v1/vip-servers/{ID}/subscription" \
  -H "Content-Type: application/json" \
  -d '"..."'
```

## Models

### PrivateServersApi.GameServerResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | `string` | No |  |
| `maxPlayers` | `integer` | No |  |
| `playing` | `integer` | No |  |
| `playerTokens` | `string[]` | No |  |
| `players` | `PrivateServerPlayerResponse[]` | No |  |
| `fps` | `number` | No |  |
| `ping` | `integer` | No |  |
| `name` | `string` | No |  |
| `vipServerId` | `integer` | No |  |
| `accessCode` | `string` | No |  |
| `owner` | `any` | No |  |

### GetPrivateServerListResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | `PrivateServersApi.GameServerResponse[]` | No |  |
| `previousPageCursor` | `string` | No |  |
| `nextPageCursor` | `string` | No |  |
| `gameJoinRestricted` | `boolean` | No |  |

### PrivateServersEnabledInUniverseResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `privateServersEnabled` | `boolean` | No |  |

### MyPrivateServersResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `nextPageCursor` | `string` | No |  |
| `previousPageCursor` | `string` | No |  |
| `data` | `MyPrivateServersData[]` | No |  |

### Roblox.Api.Develop.Models.PrivateServerDetailsResponse

Model for private server details responses from the UniverseSettings controller.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `isEnabled` | `boolean` | No | Whether or not VIP servers are enabled on this universe. |
| `price` | `integer` | No | The price of the VIP server. |
| `activeServersCount` | `integer` | No | The number of active VIP servers for this universe. A negative value indicates at least this many exist (i.e. -100 means 100+ active private servers). |
| `activeSubscriptionsCount` | `integer` | No | The number of active VIP server subscriptions. A negative value indicates at least this many exist (i.e. -100 means 100+ active subscriptions). |

### CanInviteUserResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `canInvite` | `boolean` | No |  |
| `doesOwnerPrivacyRestrictJoins` | `boolean` | No |  |
| `inviteResponseType` | `any` | No |  |

### PrivateServerResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | `integer` | No |  |
| `name` | `string` | No |  |
| `game` | `any` | No |  |
| `joinCode` | `string` | No |  |
| `active` | `boolean` | No |  |
| `subscription` | `any` | No |  |
| `permissions` | `any` | No |  |
| `link` | `string` | No |  |

### PrivateServerSubscriptionResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `active` | `boolean` | No |  |
| `expired` | `boolean` | No |  |
| `expirationDate` | `string` | No |  |
| `price` | `integer` | No |  |
| `canRenew` | `boolean` | No |  |
| `hasInsufficientFunds` | `boolean` | No |  |
| `hasRecurringProfile` | `boolean` | No |  |
| `hasPriceChanged` | `boolean` | No |  |
| `purchaseScheduleId` | `integer` | No |  |
| `totalDiscountAmountInRobux` | `integer` | No |  |
| `metadata` | `any` | No |  |