---
name: "Game passes"
last_updated: 2026-10-30T19:56:08Z
type: feature
api_base_url: "https://apis.roblox.com"
endpoints: 21
auth: [api-key, oauth2, cookie]
description: "Create and manage game passes to monetize your experiences"
---

# Game passes

Create and manage game passes to monetize your experiences. Game passes provide one-time purchases that grant permanent benefits to players. [Create](#GamePasses_CreateGamePass) and [update](#GamePasses_UpdateGamePass) game passes with custom icons and pricing, and [list all game passes](#GamePasses_ListGamePassConfigsByUniverse) for an experience.

> **See also:** To developer products (one-time consumables), see [developer-products](/docs/cloud/reference/features/developer-products.md).

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

### POST `/game-passes/v1/universes/{universeId}/game-passes` [BETA]

Create game pass

Creates a new game pass with the provided configuration details.

**Auth:** Cookie (`.ROBLOSECURITY`) or API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `game-pass:write`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer` | Yes | The universe ID. |

**Request Body:** `multipart/form-data` — Type: `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | `string` | Yes | The name of the game pass. |
| `description` | `string` | No | The description of the game pass. |
| `imageFile` | `string` | No | The thumbnail image file to be uploaded. |
| `isForSale` | `boolean` | No | Whether the game pass should be on sale. |
| `price` | `integer` | No | The default price of the game pass. |
| `isRegionalPricingEnabled` | `boolean` | No | Whether regional pricing should be enabled for the game pass. |
| `isManagedPricingEnabled` | `boolean` | No | Whether managed pricing should be enabled for the game pass. |

**Request example:**
```json
{
  "name": "string",
  "description": "string",
  "imageFile": "string",
  "isForSale": false,
  "price": 0,
  "isRegionalPricingEnabled": false
}
```

**Responses:**

- `200`: Success → `GamePassConfigV2`
- `400`: Bad Request → `GamePasses.ErrorResponse`
- `401`: Unauthorized → `GamePasses.ErrorResponse`
- `403`: Forbidden → `GamePasses.ErrorResponse`
- `404`: Not Found → `GamePasses.ErrorResponse`

**Response fields** (`GamePassConfigV2`)

See [GamePassConfigV2](#gamepassconfigv2) in Models.

**Response example:**
```json
{
  "gamePassId": 0,
  "name": "string",
  "description": "string",
  "isForSale": false,
  "iconAssetId": 0,
  "createdTimestamp": "2024-01-01T00:00:00Z"
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 5/second, perOauth2Authorization: 5/second

**Example:**
```bash
curl -X POST -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/game-passes/v1/universes/{UNIVERSEID}/game-passes" \
  -F "name=string" \
  -F "description=string" \
  -F "imageFile=@file.bin;type=application/octet-stream" \
  -F "isForSale=false" \
  -F "price=0" \
  -F "isRegionalPricingEnabled=false" \
  -F "isManagedPricingEnabled=false"
```

### GET `/game-passes/v1/universes/{universeId}/game-passes/creator` [BETA]

List game passes by universe with configuration details

**Auth:** Cookie (`.ROBLOSECURITY`) or API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `game-pass:read`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer` | Yes | The universe ID. |
| `pageSize` | query | `integer` | No | The number of results to return. Defaults to 50 if not provided. |
| `pageToken` | query | `string` | No | The cursor token for pagination. |

**Responses:**

- `200`: Success → `ListGamePassConfigsByUniverseResponse`
- `400`: Bad Request → `GamePasses.ErrorResponse`
- `401`: Unauthorized → `GamePasses.ErrorResponse`
- `403`: Forbidden → `GamePasses.ErrorResponse`
- `404`: Not Found → `GamePasses.ErrorResponse`

**Response fields** (`ListGamePassConfigsByUniverseResponse`)

See [ListGamePassConfigsByUniverseResponse](#listgamepassconfigsbyuniverseresponse) in Models.

**Response example:**
```json
{
  "gamePasses": [
    {
      "gamePassId": "...",
      "name": "...",
      "description": "...",
      "isForSale": "...",
      "iconAssetId": "...",
      "createdTimestamp": "..."
    }
  ],
  "nextPageToken": "string"
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 10/second, perOauth2Authorization: 10/second

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/game-passes/v1/universes/{UNIVERSEID}/game-passes/creator"
```

### PATCH `/game-passes/v1/universes/{universeId}/game-passes/{gamePassId}` [BETA]

Update game pass

Updates a game pass with the provided configuration details.
Note that only fields provided in the request will be updated.

**Auth:** Cookie (`.ROBLOSECURITY`) or API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `game-pass:write`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer` | Yes | The universe ID. |
| `gamePassId` | path | `integer` | Yes | The game pass ID. |

**Request Body:** `multipart/form-data` — Type: `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | `string` | No | The name of the game pass. |
| `description` | `string` | No | The description of the game pass. |
| `file` | `string` | No | The thumbnail image file to be uploaded. Alias for imageFile - if both are provided, imageFile will be used. |
| `imageFile` | `string` | No | The thumbnail image file to be uploaded. |
| `isForSale` | `boolean` | No | Whether the game pass should be on sale. |
| `price` | `integer` | No | The default price of the game pass. |
| `isRegionalPricingEnabled` | `boolean` | No | Whether regional pricing should be enabled for the game pass. |
| `isManagedPricingEnabled` | `boolean` | No | Whether managed pricing should be enabled for the game pass. |

**Request example:**
```json
{
  "name": "string",
  "description": "string",
  "file": "string",
  "imageFile": "string",
  "isForSale": false,
  "price": 0
}
```

**Responses:**

- `204`: No Content
- `400`: Bad Request → `GamePasses.ErrorResponse`
- `401`: Unauthorized → `GamePasses.ErrorResponse`
- `403`: Forbidden → `GamePasses.ErrorResponse`
- `404`: Not Found → `GamePasses.ErrorResponse`
- `409`: Conflict → `GamePasses.ErrorResponse`

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 5/second, perOauth2Authorization: 5/second

**Example:**
```bash
curl -X PATCH -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/game-passes/v1/universes/{UNIVERSEID}/game-passes/{GAMEPASSID}" \
  -F "name=string" \
  -F "description=string" \
  -F "file=@file.bin;type=application/octet-stream" \
  -F "imageFile=@file.bin;type=application/octet-stream" \
  -F "isForSale=false" \
  -F "price=0" \
  -F "isRegionalPricingEnabled=false" \
  -F "isManagedPricingEnabled=false"
```

### GET `/game-passes/v1/universes/{universeId}/game-passes/{gamePassId}/creator` [BETA]

Get game pass with configuration details

**Auth:** Cookie (`.ROBLOSECURITY`) or API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `game-pass:read`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer` | Yes | The universe ID. |
| `gamePassId` | path | `integer` | Yes | The game pass ID. |

**Responses:**

- `200`: Success → `GamePassConfigV2`
- `401`: Unauthorized → `GamePasses.ErrorResponse`
- `403`: Forbidden → `GamePasses.ErrorResponse`
- `404`: Not Found → `GamePasses.ErrorResponse`

**Response fields** (`GamePassConfigV2`)

See [GamePassConfigV2](#gamepassconfigv2) in Models.

**Response example:**
```json
{
  "gamePassId": 0,
  "name": "string",
  "description": "string",
  "isForSale": false,
  "iconAssetId": 0,
  "createdTimestamp": "2024-01-01T00:00:00Z"
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 10/second, perOauth2Authorization: 10/second

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/game-passes/v1/universes/{UNIVERSEID}/game-passes/{GAMEPASSID}/creator"
```

### PATCH `/legacy-game-internationalization/v1/game-passes/{gamePassId}/description/language-codes/{languageCode}` [EXPERIMENTAL]

Update localized description of a game pass

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `legacy-game-pass:manage`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gamePassId` | path | `integer` | Yes | The game pass id |
| `languageCode` | path | `string` | Yes | The language code of description to update |

**Request Body:** `application/json` — Type: `Roblox.GameInternationalization.Api.UpdateGamePassDescriptionRequest`

See [Roblox.GameInternationalization.Api.UpdateGamePassDescriptionRequest](#roblox-gameinternationalization-api-updategamepassdescriptionrequest) in Models.

**Request example:**
```json
{
  "description": "string"
}
```

**Responses:**

- `200`: OK → `Roblox.GameInternationalization.Api.UpdateGamePassDescriptionResponse`
- `400`: 13: Request body can't be null 19: New name is null or whitespaces or new name/description is too long 20: New name or description is moderated 22: Invalid language code 26: You can't update translations for source language 53: Language is not supported for the game. 61: Invalid game pass id
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 18: You do not have permission to manage this game
- `503`: 17: Feature is disabled

**Response fields** (`Roblox.GameInternationalization.Api.UpdateGamePassDescriptionResponse`)

See [Roblox.GameInternationalization.Api.UpdateGamePassDescriptionResponse](#roblox-gameinternationalization-api-updategamepassdescriptionresponse) in Models.

**Response example:**
```json
{
  "description": "string"
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 100/minute, perOauth2Authorization: 100/minute

**Example:**
```bash
curl -X PATCH -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/legacy-game-internationalization/v1/game-passes/{GAMEPASSID}/description/language-codes/{LANGUAGECODE}" \
  -H "Content-Type: application/json" \
  -d '{
  "description": "string"
}'
```

### GET `/legacy-game-internationalization/v1/game-passes/{gamePassId}/icons` [EXPERIMENTAL]

Get all icons for a game pass

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `legacy-game-pass:manage`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gamePassId` | path | `integer` | Yes | The game pass id |
| `width` | query | `integer` | No | The width of the icon to request |
| `height` | query | `integer` | No | The height of the icon to request |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.GameInternationalization.Api.GetGamePassIconResponse_`
- `400`: 52: Image dimensions are invalid 61: Invalid game pass id
- `401`: 0: Authorization has been denied for this request.
- `500`: 0: An unknown error occurred.
- `503`: 17: Feature is disabled

**Response fields** (`Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.GameInternationalization.Api.GetGamePassIconResponse_`)

See [Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.GameInternationalization.Api.GetGamePassIconResponse_](#roblox-web-webapi-models-apiarrayresponse-roblox-gameinternationalization-api-getgamepassiconresponse-) in Models.

**Response example:**
```json
{
  "data": [
    {
      "imageId": "...",
      "imageUrl": "...",
      "state": "...",
      "languageCode": "..."
    }
  ]
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Rate Limits:** perApiKeyOwner: 100/minute, perOauth2Authorization: 100/minute

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/legacy-game-internationalization/v1/game-passes/{GAMEPASSID}/icons"
```

### POST `/legacy-game-internationalization/v1/game-passes/{gamePassId}/icons/language-codes/{languageCode}` [EXPERIMENTAL]

Update a game pass's icon

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `legacy-game-pass:manage`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gamePassId` | path | `integer` | Yes | The game pass id |
| `languageCode` | path | `string` | Yes | The language code of this icon to update |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: 22: Invalid language code 26: You can't update translations for source language 45: File uploaded does not match known image format 46: File not present in request 53: Language is not supported for the game. 61: Invalid game pass id
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 18: You do not have permission to manage this game
- `429`: 24: Too many attempts.Please try again later.
- `500`: 0: An unknown error occurred.
- `503`: 17: Feature is disabled

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `429`: Retry with exponential backoff (start at 1s). `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 100/minute, perOauth2Authorization: 100/minute

**Example:**
```bash
curl -X POST -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/legacy-game-internationalization/v1/game-passes/{GAMEPASSID}/icons/language-codes/{LANGUAGECODE}" \
  -H "Content-Type: application/json" \
  -d '{"key": "value"}'
```

### DELETE `/legacy-game-internationalization/v1/game-passes/{gamePassId}/icons/language-codes/{languageCode}` [EXPERIMENTAL]

Delete a localized icon from a game pass

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `legacy-game-pass:manage`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gamePassId` | path | `integer` | Yes | The game pass id |
| `languageCode` | path | `string` | Yes | The language code of the localized icon to delete |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: 22: Invalid language code 23: You can't delete translations for source language 53: Language is not supported for the game. 61: Invalid game pass id
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 18: You do not have permission to manage this game
- `500`: 0: An unknown error occurred.
- `503`: 17: Feature is disabled

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 100/minute, perOauth2Authorization: 100/minute

**Example:**
```bash
curl -X DELETE -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/legacy-game-internationalization/v1/game-passes/{GAMEPASSID}/icons/language-codes/{LANGUAGECODE}"
```

### GET `/legacy-game-internationalization/v1/game-passes/{gamePassId}/name-description` [EXPERIMENTAL]

Get all names and descriptions of a game pass

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `legacy-game-pass:manage`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gamePassId` | path | `integer` | Yes | The game pass Id |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.GameInternationalization.Api.NameDescription_`
- `400`: 61: Invalid game pass id
- `401`: 0: Authorization has been denied for this request.
- `503`: 17: Feature is disabled

**Response fields** (`Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.GameInternationalization.Api.NameDescription_`)

See [Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.GameInternationalization.Api.NameDescription_](#roblox-web-webapi-models-apiarrayresponse-roblox-gameinternationalization-api-namedescription-) in Models.

**Response example:**
```json
{
  "data": [
    {
      "name": "...",
      "description": "...",
      "updateType": "...",
      "languageCode": "..."
    }
  ]
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Rate Limits:** perApiKeyOwner: 100/minute, perOauth2Authorization: 100/minute

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/legacy-game-internationalization/v1/game-passes/{GAMEPASSID}/name-description"
```

### PATCH `/legacy-game-internationalization/v1/game-passes/{gamePassId}/name-description/language-codes/{languageCode}` [EXPERIMENTAL]

Update localized name and description of a game pass

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `legacy-game-pass:manage`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gamePassId` | path | `integer` | Yes | The game pass id |
| `languageCode` | path | `string` | Yes | The language code of the name/description to update |

**Request Body:** `application/json` — Type: `Roblox.GameInternationalization.Api.UpdateGamePassNameDescriptionRequest`

See [Roblox.GameInternationalization.Api.UpdateGamePassNameDescriptionRequest](#roblox-gameinternationalization-api-updategamepassnamedescriptionrequest) in Models.

**Request example:**
```json
{
  "name": "string",
  "description": "string"
}
```

**Responses:**

- `200`: OK → `Roblox.GameInternationalization.Api.UpdateGamePassNameDescriptionResponse`
- `400`: 13: Request body can't be null 19: New name is null or whitespaces or new name/description is too long 20: New name or description is moderated 22: Invalid language code 26: You can't update translations for source language 53: Language is not supported for the game. 61: Invalid game pass id
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 18: You do not have permission to manage this game
- `503`: 17: Feature is disabled

**Response fields** (`Roblox.GameInternationalization.Api.UpdateGamePassNameDescriptionResponse`)

See [Roblox.GameInternationalization.Api.UpdateGamePassNameDescriptionResponse](#roblox-gameinternationalization-api-updategamepassnamedescriptionresponse) in Models.

**Response example:**
```json
{
  "name": "string",
  "description": "string"
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 100/minute, perOauth2Authorization: 100/minute

**Example:**
```bash
curl -X PATCH -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/legacy-game-internationalization/v1/game-passes/{GAMEPASSID}/name-description/language-codes/{LANGUAGECODE}" \
  -H "Content-Type: application/json" \
  -d '{
  "name": "string",
  "description": "string"
}'
```

### DELETE `/legacy-game-internationalization/v1/game-passes/{gamePassId}/name-description/language-codes/{languageCode}` [EXPERIMENTAL]

Delete localized name and description of a game pass

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `legacy-game-pass:manage`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gamePassId` | path | `integer` | Yes | The game pass id |
| `languageCode` | path | `string` | Yes | The language code of the name and description to delete |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: 22: Invalid language code 23: You can't delete translations for source language 53: Language is not supported for the game. 61: Invalid game pass id
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 18: You do not have permission to manage this game
- `503`: 17: Feature is disabled

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 100/minute, perOauth2Authorization: 100/minute

**Example:**
```bash
curl -X DELETE -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/legacy-game-internationalization/v1/game-passes/{GAMEPASSID}/name-description/language-codes/{LANGUAGECODE}"
```

### PATCH `/legacy-game-internationalization/v1/game-passes/{gamePassId}/name/language-codes/{languageCode}` [EXPERIMENTAL]

Update localized name of a game pass

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `legacy-game-pass:manage`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gamePassId` | path | `integer` | Yes | The game pass id |
| `languageCode` | path | `string` | Yes | The language code of the name to update |

**Request Body:** `application/json` — Type: `Roblox.GameInternationalization.Api.UpdateGamePassNameRequest`

See [Roblox.GameInternationalization.Api.UpdateGamePassNameRequest](#roblox-gameinternationalization-api-updategamepassnamerequest) in Models.

**Request example:**
```json
{
  "name": "string"
}
```

**Responses:**

- `200`: OK → `Roblox.GameInternationalization.Api.UpdateGamePassNameResponse`
- `400`: 13: Request body can't be null 19: New name is null or whitespaces or new name/description is too long 20: New name or description is moderated 22: Invalid language code 26: You can't update translations for source language 53: Language is not supported for the game. 61: Invalid game pass id
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 18: You do not have permission to manage this game
- `503`: 17: Feature is disabled

**Response fields** (`Roblox.GameInternationalization.Api.UpdateGamePassNameResponse`)

See [Roblox.GameInternationalization.Api.UpdateGamePassNameResponse](#roblox-gameinternationalization-api-updategamepassnameresponse) in Models.

**Response example:**
```json
{
  "name": "string"
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 100/minute, perOauth2Authorization: 100/minute

**Example:**
```bash
curl -X PATCH -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/legacy-game-internationalization/v1/game-passes/{GAMEPASSID}/name/language-codes/{LANGUAGECODE}" \
  -H "Content-Type: application/json" \
  -d '{
  "name": "string"
}'
```

### GET `/v1/game-passes` [STABLE]

Thumbnails game pass icons.

**Server:** `https://thumbnails.roblox.com`

**Auth:** 

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gamePassIds` | query | `integer[]` | Yes | The game pass ids. |
| `size` | query | `150x150` | No | The thumbnail size, formatted widthxheight Valid values: `150x150` |
| `format` | query | `Png \| Webp` | No | The thumbnail format Valid values: `Png`, `Webp` |
| `isCircular` | query | `true \| false` | No | The circle thumbnail output parameter, true or false Valid values: `true`, `false` |

**Responses:**

- `200`: OK
- `400`: 1: There are too many requested Ids. 2: The requested image format is invalid. Please see documentation for valid thumbnail format parameter name and values. 3: The requested size is invalid. Please see documentation for valid thumbnail size parameter name and format. 4: The requested Ids are invalid, of an invalid type or missing. 10: Circular thumbnail requests are not allowed

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://thumbnails.roblox.com/v1/game-passes?gamePassIds={VALUE}"
```

### PATCH `/v1/game-passes/{gamePassId}/description/language-codes/{languageCode}` [EXPERIMENTAL]

Update localized description of a game pass

**Server:** `https://gameinternationalization.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gamePassId` | path | `integer` | Yes | The game pass id |
| `languageCode` | path | `string` | Yes | The language code of description to update |

**Request Body:** `application/json` — Type: `Roblox.GameInternationalization.Api.UpdateGamePassDescriptionRequest`

See [Roblox.GameInternationalization.Api.UpdateGamePassDescriptionRequest](#roblox-gameinternationalization-api-updategamepassdescriptionrequest) in Models.

**Request example:**
```json
{
  "description": "string"
}
```

**Responses:**

- `200`: OK → `Roblox.GameInternationalization.Api.UpdateGamePassDescriptionResponse`
- `400`: 13: Request body can't be null 19: New name is null or whitespaces or new name/description is too long 20: New name or description is moderated 22: Invalid language code 26: You can't update translations for source language 53: Language is not supported for the game. 61: Invalid game pass id
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 18: You do not have permission to manage this game
- `503`: 17: Feature is disabled

**Response fields** (`Roblox.GameInternationalization.Api.UpdateGamePassDescriptionResponse`)

See [Roblox.GameInternationalization.Api.UpdateGamePassDescriptionResponse](#roblox-gameinternationalization-api-updategamepassdescriptionresponse) in Models.

**Response example:**
```json
{
  "description": "string"
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X PATCH -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://gameinternationalization.roblox.com/v1/game-passes/{GAMEPASSID}/description/language-codes/{LANGUAGECODE}" \
  -H "Content-Type: application/json" \
  -d '{
  "description": "string"
}'
```

### GET `/v1/game-passes/{gamePassId}/icons` [EXPERIMENTAL]

Get all icons for a game pass

**Server:** `https://gameinternationalization.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gamePassId` | path | `integer` | Yes | The game pass id |
| `width` | query | `integer` | No | The width of the icon to request |
| `height` | query | `integer` | No | The height of the icon to request |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.GameInternationalization.Api.GetGamePassIconResponse_`
- `400`: 52: Image dimensions are invalid 61: Invalid game pass id
- `401`: 0: Authorization has been denied for this request.
- `500`: 0: An unknown error occurred.
- `503`: 17: Feature is disabled

**Response fields** (`Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.GameInternationalization.Api.GetGamePassIconResponse_`)

See [Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.GameInternationalization.Api.GetGamePassIconResponse_](#roblox-web-webapi-models-apiarrayresponse-roblox-gameinternationalization-api-getgamepassiconresponse-) in Models.

**Response example:**
```json
{
  "data": [
    {
      "imageId": "...",
      "imageUrl": "...",
      "state": "...",
      "languageCode": "..."
    }
  ]
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://gameinternationalization.roblox.com/v1/game-passes/{GAMEPASSID}/icons"
```

### POST `/v1/game-passes/{gamePassId}/icons/language-codes/{languageCode}` [EXPERIMENTAL]

Update a game pass's icon

**Server:** `https://gameinternationalization.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gamePassId` | path | `integer` | Yes | The game pass id |
| `languageCode` | path | `string` | Yes | The language code of this icon to update |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: 22: Invalid language code 26: You can't update translations for source language 45: File uploaded does not match known image format 46: File not present in request 53: Language is not supported for the game. 61: Invalid game pass id
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 18: You do not have permission to manage this game
- `429`: 24: Too many attempts.Please try again later.
- `500`: 0: An unknown error occurred.
- `503`: 17: Feature is disabled

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `429`: Retry with exponential backoff (start at 1s). `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://gameinternationalization.roblox.com/v1/game-passes/{GAMEPASSID}/icons/language-codes/{LANGUAGECODE}" \
  -H "Content-Type: application/json" \
  -d '{"key": "value"}'
```

### DELETE `/v1/game-passes/{gamePassId}/icons/language-codes/{languageCode}` [EXPERIMENTAL]

Delete a localized icon from a game pass

**Server:** `https://gameinternationalization.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gamePassId` | path | `integer` | Yes | The game pass id |
| `languageCode` | path | `string` | Yes | The language code of the localized icon to delete |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: 22: Invalid language code 23: You can't delete translations for source language 53: Language is not supported for the game. 61: Invalid game pass id
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 18: You do not have permission to manage this game
- `500`: 0: An unknown error occurred.
- `503`: 17: Feature is disabled

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X DELETE -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://gameinternationalization.roblox.com/v1/game-passes/{GAMEPASSID}/icons/language-codes/{LANGUAGECODE}"
```

### GET `/v1/game-passes/{gamePassId}/name-description` [EXPERIMENTAL]

Get all names and descriptions of a game pass

**Server:** `https://gameinternationalization.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gamePassId` | path | `integer` | Yes | The game pass Id |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.GameInternationalization.Api.NameDescription_`
- `400`: 61: Invalid game pass id
- `401`: 0: Authorization has been denied for this request.
- `503`: 17: Feature is disabled

**Response fields** (`Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.GameInternationalization.Api.NameDescription_`)

See [Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.GameInternationalization.Api.NameDescription_](#roblox-web-webapi-models-apiarrayresponse-roblox-gameinternationalization-api-namedescription-) in Models.

**Response example:**
```json
{
  "data": [
    {
      "name": "...",
      "description": "...",
      "updateType": "...",
      "languageCode": "..."
    }
  ]
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://gameinternationalization.roblox.com/v1/game-passes/{GAMEPASSID}/name-description"
```

### PATCH `/v1/game-passes/{gamePassId}/name-description/language-codes/{languageCode}` [EXPERIMENTAL]

Update localized name and description of a game pass

**Server:** `https://gameinternationalization.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gamePassId` | path | `integer` | Yes | The game pass id |
| `languageCode` | path | `string` | Yes | The language code of the name/description to update |

**Request Body:** `application/json` — Type: `Roblox.GameInternationalization.Api.UpdateGamePassNameDescriptionRequest`

See [Roblox.GameInternationalization.Api.UpdateGamePassNameDescriptionRequest](#roblox-gameinternationalization-api-updategamepassnamedescriptionrequest) in Models.

**Request example:**
```json
{
  "name": "string",
  "description": "string"
}
```

**Responses:**

- `200`: OK → `Roblox.GameInternationalization.Api.UpdateGamePassNameDescriptionResponse`
- `400`: 13: Request body can't be null 19: New name is null or whitespaces or new name/description is too long 20: New name or description is moderated 22: Invalid language code 26: You can't update translations for source language 53: Language is not supported for the game. 61: Invalid game pass id
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 18: You do not have permission to manage this game
- `503`: 17: Feature is disabled

**Response fields** (`Roblox.GameInternationalization.Api.UpdateGamePassNameDescriptionResponse`)

See [Roblox.GameInternationalization.Api.UpdateGamePassNameDescriptionResponse](#roblox-gameinternationalization-api-updategamepassnamedescriptionresponse) in Models.

**Response example:**
```json
{
  "name": "string",
  "description": "string"
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X PATCH -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://gameinternationalization.roblox.com/v1/game-passes/{GAMEPASSID}/name-description/language-codes/{LANGUAGECODE}" \
  -H "Content-Type: application/json" \
  -d '{
  "name": "string",
  "description": "string"
}'
```

### DELETE `/v1/game-passes/{gamePassId}/name-description/language-codes/{languageCode}` [EXPERIMENTAL]

Delete localized name and description of a game pass

**Server:** `https://gameinternationalization.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gamePassId` | path | `integer` | Yes | The game pass id |
| `languageCode` | path | `string` | Yes | The language code of the name and description to delete |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: 22: Invalid language code 23: You can't delete translations for source language 53: Language is not supported for the game. 61: Invalid game pass id
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 18: You do not have permission to manage this game
- `503`: 17: Feature is disabled

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X DELETE -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://gameinternationalization.roblox.com/v1/game-passes/{GAMEPASSID}/name-description/language-codes/{LANGUAGECODE}"
```

### PATCH `/v1/game-passes/{gamePassId}/name/language-codes/{languageCode}` [EXPERIMENTAL]

Update localized name of a game pass

**Server:** `https://gameinternationalization.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gamePassId` | path | `integer` | Yes | The game pass id |
| `languageCode` | path | `string` | Yes | The language code of the name to update |

**Request Body:** `application/json` — Type: `Roblox.GameInternationalization.Api.UpdateGamePassNameRequest`

See [Roblox.GameInternationalization.Api.UpdateGamePassNameRequest](#roblox-gameinternationalization-api-updategamepassnamerequest) in Models.

**Request example:**
```json
{
  "name": "string"
}
```

**Responses:**

- `200`: OK → `Roblox.GameInternationalization.Api.UpdateGamePassNameResponse`
- `400`: 13: Request body can't be null 19: New name is null or whitespaces or new name/description is too long 20: New name or description is moderated 22: Invalid language code 26: You can't update translations for source language 53: Language is not supported for the game. 61: Invalid game pass id
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 18: You do not have permission to manage this game
- `503`: 17: Feature is disabled

**Response fields** (`Roblox.GameInternationalization.Api.UpdateGamePassNameResponse`)

See [Roblox.GameInternationalization.Api.UpdateGamePassNameResponse](#roblox-gameinternationalization-api-updategamepassnameresponse) in Models.

**Response example:**
```json
{
  "name": "string"
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X PATCH -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://gameinternationalization.roblox.com/v1/game-passes/{GAMEPASSID}/name/language-codes/{LANGUAGECODE}" \
  -H "Content-Type: application/json" \
  -d '{
  "name": "string"
}'
```

## Models

### GamePassConfigV2

Creator-facing representation of a game pass configuration.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `gamePassId` | `integer` | Yes | The game pass ID. |
| `name` | `string` | Yes | The name of the game pass. |
| `description` | `string` | Yes | The description of the game pass. |
| `isForSale` | `boolean` | Yes | Whether the game pass is currently on sale. |
| `iconAssetId` | `integer` | Yes | The icon image (thumbnail) asset ID of the game pass. |
| `createdTimestamp` | `string` | Yes | The timestamp when the game pass was created. |
| `updatedTimestamp` | `string` | Yes | The timestamp when the game pass was last updated. |
| `priceInformation` | `any` | Yes | The pricing configuration associated with the game pass. |
| `isManagedPricingEnabled` | `boolean` | Yes | Whether managed pricing is enabled for the game pass. |

### GamePasses.ErrorResponse

This is the base class for all custom Exceptions that are thrown in this API.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `errorCode` | `any` | No | The ErrorCode for the exception. |
| `errorMessage` | `string` | No | The human readable error message. |
| `field` | `string` | No | The relevant field that caused the error. |
| `hint` | `string` | No | A hint as to what caused the error, if applicable. |

### ListGamePassConfigsByUniverseResponse

Response for listing game pass configuration details by universe

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `gamePasses` | `GamePassConfigV2[]` | Yes | The list of game passes with their corresponding configuration details. |
| `nextPageToken` | `string` | Yes | The next page token. |

### Roblox.GameInternationalization.Api.UpdateGamePassDescriptionRequest

A request model for updating game pass description

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `description` | `string` | No | Game pass description |

### Roblox.GameInternationalization.Api.UpdateGamePassDescriptionResponse

A response model for updating game pass description

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `description` | `string` | No | Game pass description saved |

### Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.GameInternationalization.Api.GetGamePassIconResponse_

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | `Roblox.GameInternationalization.Api.GetGamePassIconResponse[]` | No |  |

### Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.GameInternationalization.Api.NameDescription_

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | `Roblox.GameInternationalization.Api.NameDescription[]` | No |  |

### Roblox.GameInternationalization.Api.UpdateGamePassNameDescriptionRequest

A request model for updating game pass name and description

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | `string` | No | Game pass name |
| `description` | `string` | No | Game pass description |

### Roblox.GameInternationalization.Api.UpdateGamePassNameDescriptionResponse

A response model for updating game pass name and description

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | `string` | No | Game pass name saved |
| `description` | `string` | No | Game pass description saved |

### Roblox.GameInternationalization.Api.UpdateGamePassNameRequest

A request model for updating game pass name

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | `string` | No | Game pass name |

### Roblox.GameInternationalization.Api.UpdateGamePassNameResponse

A response model for updating game pass name

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | `string` | No | Game pass name saved |