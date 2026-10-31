---
name: "Team Create"
last_updated: 2026-10-30T19:56:08Z
type: feature
api_base_url: "https://apis.roblox.com"
endpoints: 8
auth: [api-key, oauth2, cookie]
description: "Manage Team Create collaborative sessions for your experiences, including session monitoring, membership management, and collaboration settings"
---

# Team Create

Manage Team Create collaborative sessions for your experiences, including session monitoring, membership management, and collaboration settings.

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

### GET `/legacy-develop/v1/universes/multiget/teamcreate` [EXPERIMENTAL]

Gets TeamCreate settings for multiple universes specified by Ids

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `legacy-team-collaboration:manage`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `ids` | query | `integer[]` | Yes | The universe Ids. |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.Api.Develop.Models.UniverseTeamCreateSettingsModel_`
- `400`: Roblox.Api.Develop.ResponseEnums.TeamCreateErrors.TooManyUniverseIdsSent
- `401`: 0: Authorization has been denied for this request.

**Response fields** (`Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.Api.Develop.Models.UniverseTeamCreateSettingsModel_`)

See [Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.Api.Develop.Models.UniverseTeamCreateSettingsModel_](#roblox-web-webapi-models-apiarrayresponse-roblox-api-develop-models-universeteamcreatesettingsmodel-) in Models.

**Response example:**
```json
{
  "data": [
    {
      "id": "...",
      "isEnabled": "..."
    }
  ]
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Rate Limits:** perApiKeyOwner: 100/minute, perOauth2Authorization: 100/minute

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/legacy-develop/v1/universes/multiget/teamcreate?ids={VALUE}"
```

### GET `/legacy-develop/v1/universes/{universeId}/teamcreate` [EXPERIMENTAL]

Gets TeamCreate settings for an Roblox.Platform.Universes.IUniverse.

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `legacy-team-collaboration:manage`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer` | Yes | The universe Id. |

**Responses:**

- `200`: OK → `Roblox.Api.Develop.Models.Response.TeamCreateSettingsResponse`
- `400`: Roblox.Api.Develop.ResponseEnums.TeamCreateErrors.InvalidUniverse
- `401`: 0: Authorization has been denied for this request.
- `403`: Roblox.Api.Develop.ResponseEnums.TeamCreateErrors.Unauthorized

**Response fields** (`Roblox.Api.Develop.Models.Response.TeamCreateSettingsResponse`)

See [Roblox.Api.Develop.Models.Response.TeamCreateSettingsResponse](#roblox-api-develop-models-response-teamcreatesettingsresponse) in Models.

**Response example:**
```json
{
  "isEnabled": false
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 100/minute, perOauth2Authorization: 100/minute

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/legacy-develop/v1/universes/{UNIVERSEID}/teamcreate"
```

### PATCH `/legacy-develop/v1/universes/{universeId}/teamcreate` [EXPERIMENTAL]

Edit team create settings for a universe.

Enables, or disables team create for a universe.

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `legacy-team-collaboration:manage`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer` | Yes | The universe Id. |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: Roblox.Api.Develop.ResponseEnums.TeamCreateErrors.InvalidUniverse
- `401`: 0: Authorization has been denied for this request.
- `403`: Roblox.Api.Develop.ResponseEnums.TeamCreateErrors.Unauthorized 0: Token Validation Failed

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 100/minute, perOauth2Authorization: 100/minute

**Example:**
```bash
curl -X PATCH -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/legacy-develop/v1/universes/{UNIVERSEID}/teamcreate" \
  -H "Content-Type: application/json" \
  -d '{"key": "value"}'
```

### DELETE `/legacy-develop/v1/universes/{universeId}/teamcreate/memberships` [EXPERIMENTAL]

Removes a user from a TeamCreate permissions list.

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `legacy-team-collaboration:manage`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer` | Yes | The universe Id. |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: Roblox.Api.Develop.ResponseEnums.TeamCreateErrors.InvalidUniverse OR Roblox.Api.Develop.ResponseEnums.TeamCreateErrors.InvalidUser
- `401`: 0: Authorization has been denied for this request.
- `403`: Roblox.Api.Develop.ResponseEnums.TeamCreateErrors.TeamCreateDisabled 0: Token Validation Failed

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 100/minute, perOauth2Authorization: 100/minute

**Example:**
```bash
curl -X DELETE -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/legacy-develop/v1/universes/{UNIVERSEID}/teamcreate/memberships" \
  -H "Content-Type: application/json" \
  -d '{"key": "value"}'
```

### GET `/v1/universes/multiget/teamcreate` [EXPERIMENTAL]

Gets TeamCreate settings for multiple universes specified by Ids

**Server:** `https://develop.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `ids` | query | `integer[]` | Yes | The universe Ids. |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.Api.Develop.Models.UniverseTeamCreateSettingsModel_`
- `400`: Roblox.Api.Develop.ResponseEnums.TeamCreateErrors.TooManyUniverseIdsSent
- `401`: 0: Authorization has been denied for this request.

**Response fields** (`Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.Api.Develop.Models.UniverseTeamCreateSettingsModel_`)

See [Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.Api.Develop.Models.UniverseTeamCreateSettingsModel_](#roblox-web-webapi-models-apiarrayresponse-roblox-api-develop-models-universeteamcreatesettingsmodel-) in Models.

**Response example:**
```json
{
  "data": [
    {
      "id": "...",
      "isEnabled": "..."
    }
  ]
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://develop.roblox.com/v1/universes/multiget/teamcreate?ids={VALUE}"
```

### GET `/v1/universes/{universeId}/teamcreate` [EXPERIMENTAL]

Gets TeamCreate settings for an Roblox.Platform.Universes.IUniverse.

**Server:** `https://develop.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer` | Yes | The universe Id. |

**Responses:**

- `200`: OK → `Roblox.Api.Develop.Models.Response.TeamCreateSettingsResponse`
- `400`: Roblox.Api.Develop.ResponseEnums.TeamCreateErrors.InvalidUniverse
- `401`: 0: Authorization has been denied for this request.
- `403`: Roblox.Api.Develop.ResponseEnums.TeamCreateErrors.Unauthorized

**Response fields** (`Roblox.Api.Develop.Models.Response.TeamCreateSettingsResponse`)

See [Roblox.Api.Develop.Models.Response.TeamCreateSettingsResponse](#roblox-api-develop-models-response-teamcreatesettingsresponse) in Models.

**Response example:**
```json
{
  "isEnabled": false
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://develop.roblox.com/v1/universes/{UNIVERSEID}/teamcreate"
```

### PATCH `/v1/universes/{universeId}/teamcreate` [EXPERIMENTAL]

Edit team create settings for a universe.

Enables, or disables team create for a universe.

**Server:** `https://develop.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer` | Yes | The universe Id. |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: Roblox.Api.Develop.ResponseEnums.TeamCreateErrors.InvalidUniverse
- `401`: 0: Authorization has been denied for this request.
- `403`: Roblox.Api.Develop.ResponseEnums.TeamCreateErrors.Unauthorized 0: Token Validation Failed

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X PATCH -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://develop.roblox.com/v1/universes/{UNIVERSEID}/teamcreate" \
  -H "Content-Type: application/json" \
  -d '{"key": "value"}'
```

### DELETE `/v1/universes/{universeId}/teamcreate/memberships` [EXPERIMENTAL]

Removes a user from a TeamCreate permissions list.

**Server:** `https://develop.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer` | Yes | The universe Id. |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: Roblox.Api.Develop.ResponseEnums.TeamCreateErrors.InvalidUniverse OR Roblox.Api.Develop.ResponseEnums.TeamCreateErrors.InvalidUser
- `401`: 0: Authorization has been denied for this request.
- `403`: Roblox.Api.Develop.ResponseEnums.TeamCreateErrors.TeamCreateDisabled 0: Token Validation Failed

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X DELETE -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://develop.roblox.com/v1/universes/{UNIVERSEID}/teamcreate/memberships" \
  -H "Content-Type: application/json" \
  -d '{"key": "value"}'
```

## Models

### Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.Api.Develop.Models.UniverseTeamCreateSettingsModel_

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | `Roblox.Api.Develop.Models.UniverseTeamCreateSettingsModel[]` | No |  |

### Roblox.Api.Develop.Models.Response.TeamCreateSettingsResponse

Team create settings

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `isEnabled` | `boolean` | No | Whether or not the universe should be enabled for team create |