---
name: "User profiles"
last_updated: 2026-10-30T19:56:08Z
type: feature
api_base_url: "https://apis.roblox.com"
endpoints: 5
auth: [api-key, oauth2, cookie]
description: "Access user profile pages"
---

# User profiles

Access user profile pages. [Retrieve user descriptions](#users_get_v1_description), [badges](#accountinformation_get_v1_users__userId__roblox_badges), [avatar configuration](#avatar_get_v1_users__userId__avatar), and [wearing items](#avatar_get_v1_users__userId__currently_wearing).

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

### GET `/v1/users/{userId}`

Gets detailed user information by id.

**Server:** `https://users.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer` | Yes | The user id. |

**Responses:**

- `200`: OK → `Roblox.Users.Api.GetUserResponse`
- `404`: 3: The user id is invalid.

**Response fields** (`Roblox.Users.Api.GetUserResponse`)

See [Roblox.Users.Api.GetUserResponse](#roblox-users-api-getuserresponse) in Models.

**Response example:**
```json
{
  "description": "string",
  "created": "2024-01-01T00:00:00Z",
  "isBanned": false,
  "externalAppDisplayName": "string",
  "hasVerifiedBadge": false,
  "id": 0
}
```

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://users.roblox.com/v1/users/{USERID}"
```

### PATCH `/v1/users/{userId}/display-names`

Set the display name for the authorized user.

**Server:** `https://users.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer` | Yes | the user id |

**Request Body:** `application/json` — Type: `Roblox.Users.Api.SetDisplayNameRequest`

See [Roblox.Users.Api.SetDisplayNameRequest](#roblox-users-api-setdisplaynamerequest) in Models.

**Request example:**
```json
{
  "newDisplayName": "string"
}
```

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: 1: Display name is too short 2: Display name is too long 3: Display name contains invalid characters 4: Display name has been moderated 8: Display name has too many combinations of character sets
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 7: The user id is invalid.
- `429`: 5: Display name updates for this user have been throttled

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `429`: Retry with exponential backoff (start at 1s). `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X PATCH -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://users.roblox.com/v1/users/{USERID}/display-names" \
  -H "Content-Type: application/json" \
  -d '{
  "newDisplayName": "string"
}'
```

### GET `/v1/users/{userId}/premium-upsell-precheck`

Premium upsell precheck

**Server:** `https://premiumfeatures.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer` | Yes | User ID |
| `universeId` | query | `integer` | Yes |  |
| `placeId` | query | `integer` | Yes |  |

**Responses:**

- `200`: OK
- `401`: 0: Authorization has been denied for this request.

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://premiumfeatures.roblox.com/v1/users/{USERID}/premium-upsell-precheck?universeId={VALUE}&placeId={VALUE}"
```

### GET `/v1/users/{userId}/username-history`

Retrieves the username history for a particular user.

**Server:** `https://users.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer` | Yes |  |
| `limit` | query | `10 \| 25 \| 50 \| 100` | No | The number of results per request. Valid values: `10`, `25`, `50`, `100` |
| `cursor` | query | `string` | No | The paging cursor for the previous or next page. |
| `sortOrder` | query | `Asc \| Desc` | No | The order the results are sorted in. Valid values: `Asc`, `Desc` |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.Users.Api.UsernameHistoryResponse_`
- `400`: 3: The user id is invalid.

**Response fields** (`Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.Users.Api.UsernameHistoryResponse_`)

See [Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.Users.Api.UsernameHistoryResponse_](#roblox-web-webapi-models-apipageresponse-roblox-users-api-usernamehistoryresponse-) in Models.

**Response example:**
```json
{
  "previousPageCursor": "string",
  "nextPageCursor": "string",
  "data": [
    {
      "name": "..."
    }
  ]
}
```

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://users.roblox.com/v1/users/{USERID}/username-history"
```

### GET `/v1/users/{userId}/validate-membership`

Get if a user has a Premium membership

**Server:** `https://premiumfeatures.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer` | Yes | User ID |

**Responses:**

- `200`: OK
- `401`: 0: Authorization has been denied for this request.

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://premiumfeatures.roblox.com/v1/users/{USERID}/validate-membership"
```

## Models

### Roblox.Users.Api.GetUserResponse

A response model representing user information.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `description` | `string` | No | The user description. |
| `created` | `string` | No | When the user signed up. |
| `isBanned` | `boolean` | No | Whether the user is banned |
| `externalAppDisplayName` | `string` | No | Unused, legacy attribute. For now always null to not disturb existing client code that might rely on its existence. |
| `hasVerifiedBadge` | `boolean` | No | The user's verified badge status. |
| `id` | `integer` | No | The user Id. |
| `name` | `string` | No | The user name. |
| `displayName` | `string` | No | The user DisplayName. |

### Roblox.Users.Api.SetDisplayNameRequest

Request model for changing a display name.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `newDisplayName` | `string` | No | The users new display name. |

### Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.Users.Api.UsernameHistoryResponse_

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `previousPageCursor` | `string` | No |  |
| `nextPageCursor` | `string` | No |  |
| `data` | `Roblox.Users.Api.UsernameHistoryResponse[]` | No |  |