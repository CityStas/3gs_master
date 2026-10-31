---
name: "Badges"
last_updated: 2026-10-30T19:56:08Z
type: feature
api_base_url: "https://apis.roblox.com"
endpoints: 29
auth: [api-key, oauth2, cookie]
description: "Create and manage experience badges to recognize player achievements"
---

# Badges

Create and manage experience badges to recognize player achievements. [Create](#post_legacy_badges_v1_universes__universeId__badges) and [update](#patch_legacy_badges_v1_badges__badgeId_) badges with custom icons, and [track which badges users have earned](#badges_get_v1_users__userId__badges_awarded_dates) and when they were awarded.

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

### PATCH `/legacy-badges/v1/badges/{badgeId}` [EXPERIMENTAL]

Updates badge configuration.

Managers may change enabled state, name, and description when authorized for the badge.

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `legacy-universe.badge:write`, `legacy-universe.badge:manage-and-spend-robux`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `badgeId` | path | `integer` | Yes | The badge Id. |

**Request Body:** `application/json` — Type: `Roblox.Badges.Api.UpdateBadgeRequest`

See [Roblox.Badges.Api.UpdateBadgeRequest](#roblox-badges-api-updatebadgerequest) in Models.

**Request example:**
```json
{
  "name": "string",
  "description": "string",
  "enabled": false
}
```

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: 6: Text moderated. 14: Invalid badge name. 15: Invalid badge description.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 2: You do not have permission to manage this badge.
- `404`: 1: Badge is invalid or does not exist. 3: The game is invalid or does not exist.

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 100/minute, perOauth2Authorization: 100/minute

**Example:**
```bash
curl -X PATCH -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/legacy-badges/v1/badges/{BADGEID}" \
  -H "Content-Type: application/json" \
  -d '{
  "name": "string",
  "description": "string",
  "enabled": false
}'
```

### POST `/legacy-badges/v1/universes/{universeId}/badges` [EXPERIMENTAL]

Creates a new badge.

Charges the selected payment source and creates the badge under the universe's root place.

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `legacy-universe.badge:manage-and-spend-robux`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer` | Yes | The ID of the universe to create the badge for. |

**Request Body:** `multipart/form-data` — Type: `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | `string` | No | The badge name. |
| `description` | `string` | No | The badge description. |
| `paymentSourceType` | `1 \| 2` | No | Whether or not to pay for the badge with user funds, or group funds. |
| `files` | `string` | No | The badge icon. Optional: when omitted and a curated default badge icon is configured on |
| `expectedCost` | `integer` | No | User expected cost of a badge. |
| `isActive` | `boolean` | No | Whether or not the badge should be created in the active state. |

**Request example:**
```json
{
  "name": "string",
  "description": "string",
  "paymentSourceType": 1,
  "files": "string",
  "expectedCost": 0,
  "isActive": false
}
```

**Responses:**

- `200`: OK → `Roblox.Web.Responses.Badges.BadgeResponseV2`
- `400`: 11: The badge icon is invalid. 14: Invalid badge name. 15: Invalid badge description. 16: Payment source is invalid. 18: Expected badge cost is different from the actual badge cost.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 6: Text moderated. 12: You do not have permission to manage this game's badges. 17: Insufficient funds.
- `404`: 3: The game is invalid or does not exist.
- `429`: 13: Too many requests, try again later.

**Response fields** (`Roblox.Web.Responses.Badges.BadgeResponseV2`)

See [Roblox.Web.Responses.Badges.BadgeResponseV2](#roblox-web-responses-badges-badgeresponsev2) in Models.

**Response example:**
```json
{
  "id": 0,
  "name": "string",
  "description": "string",
  "displayName": "string",
  "displayDescription": "string",
  "enabled": false
}
```

**Error handling:** `429`: Retry with exponential backoff (start at 1s). `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 100/minute, perOauth2Authorization: 100/minute

**Example:**
```bash
curl -X POST -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/legacy-badges/v1/universes/{UNIVERSEID}/badges" \
  -F "name=string" \
  -F "description=string" \
  -F "paymentSourceType=1" \
  -F "files=@file.bin;type=application/octet-stream" \
  -F "expectedCost=0" \
  -F "isActive=false"
```

### PATCH `/legacy-game-internationalization/v1/badges/{badgeId}/description/language-codes/{languageCode}` [EXPERIMENTAL]

Update localized description of a badge

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `legacy-badge:manage`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `badgeId` | path | `integer` | Yes | The badge id |
| `languageCode` | path | `string` | Yes | The language code of the description to update |

**Request Body:** `application/json` — Type: `Roblox.GameInternationalization.Api.UpdateBadgeDescriptionRequest`

See [Roblox.GameInternationalization.Api.UpdateBadgeDescriptionRequest](#roblox-gameinternationalization-api-updatebadgedescriptionrequest) in Models.

**Request example:**
```json
{
  "description": "string"
}
```

**Responses:**

- `200`: OK → `Roblox.GameInternationalization.Api.UpdateBadgeDescriptionResponse`
- `400`: 13: Request body can't be null 19: New name is null or whitespaces or new name/description is too long 20: New name or description is moderated 22: Invalid language code 26: You can't update translations for source language 53: Language is not supported for the game. 62: Invalid game badge id
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 18: You do not have permission to manage this game
- `500`: 0: An unknown error occurred.
- `503`: 17: Feature is disabled

**Response fields** (`Roblox.GameInternationalization.Api.UpdateBadgeDescriptionResponse`)

See [Roblox.GameInternationalization.Api.UpdateBadgeDescriptionResponse](#roblox-gameinternationalization-api-updatebadgedescriptionresponse) in Models.

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
  "https://apis.roblox.com/legacy-game-internationalization/v1/badges/{BADGEID}/description/language-codes/{LANGUAGECODE}" \
  -H "Content-Type: application/json" \
  -d '{
  "description": "string"
}'
```

### GET `/legacy-game-internationalization/v1/badges/{badgeId}/icons` [EXPERIMENTAL]

Get all icons for a badge

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `legacy-badge:manage`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `badgeId` | path | `integer` | Yes | The id of the badge |
| `width` | query | `integer` | No | The width of the icon to request |
| `height` | query | `integer` | No | The height of the icon to request |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.GameInternationalization.Api.GetBadgeIconResponse_`
- `400`: 52: Image dimensions are invalid 62: Invalid game badge id
- `401`: 0: Authorization has been denied for this request.
- `500`: 0: An unknown error occurred.
- `503`: 17: Feature is disabled

**Response fields** (`Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.GameInternationalization.Api.GetBadgeIconResponse_`)

See [Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.GameInternationalization.Api.GetBadgeIconResponse_](#roblox-web-webapi-models-apiarrayresponse-roblox-gameinternationalization-api-getbadgeiconresponse-) in Models.

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
  "https://apis.roblox.com/legacy-game-internationalization/v1/badges/{BADGEID}/icons"
```

### POST `/legacy-game-internationalization/v1/badges/{badgeId}/icons/language-codes/{languageCode}` [EXPERIMENTAL]

Update a badge's icon

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `legacy-badge:manage`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `badgeId` | path | `integer` | Yes | The id of the badge |
| `languageCode` | path | `string` | Yes | The language code of this icon to update |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: 22: Invalid language code 26: You can't update translations for source language 45: File uploaded does not match known image format 46: File not present in request 53: Language is not supported for the game. 62: Invalid game badge id
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
  "https://apis.roblox.com/legacy-game-internationalization/v1/badges/{BADGEID}/icons/language-codes/{LANGUAGECODE}" \
  -H "Content-Type: application/json" \
  -d '{"key": "value"}'
```

### DELETE `/legacy-game-internationalization/v1/badges/{badgeId}/icons/language-codes/{languageCode}` [EXPERIMENTAL]

Delete a localized icon from a badge

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `legacy-badge:manage`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `badgeId` | path | `integer` | Yes | The id of the badge |
| `languageCode` | path | `string` | Yes | The language code of the localized icon to delete |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: 22: Invalid language code 23: You can't delete translations for source language 53: Language is not supported for the game. 62: Invalid game badge id
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
  "https://apis.roblox.com/legacy-game-internationalization/v1/badges/{BADGEID}/icons/language-codes/{LANGUAGECODE}"
```

### GET `/legacy-game-internationalization/v1/badges/{badgeId}/name-description` [EXPERIMENTAL]

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `legacy-badge:manage`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `badgeId` | path | `integer` | Yes |  |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.GameInternationalization.Api.NameDescription_`
- `400`: 62: Invalid game badge id
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
  "https://apis.roblox.com/legacy-game-internationalization/v1/badges/{BADGEID}/name-description"
```

### PATCH `/legacy-game-internationalization/v1/badges/{badgeId}/name-description/language-codes/{languageCode}` [EXPERIMENTAL]

Update localized name and description of a badge

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `legacy-badge:manage`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `badgeId` | path | `integer` | Yes | The badge id |
| `languageCode` | path | `string` | Yes | The language code of the name and description to Update |

**Request Body:** `application/json` — Type: `Roblox.GameInternationalization.Api.UpdateBadgeNameDescriptionRequest`

See [Roblox.GameInternationalization.Api.UpdateBadgeNameDescriptionRequest](#roblox-gameinternationalization-api-updatebadgenamedescriptionrequest) in Models.

**Request example:**
```json
{
  "name": "string",
  "description": "string"
}
```

**Responses:**

- `200`: OK → `Roblox.GameInternationalization.Api.UpdateBadgeNameDescriptionResponse`
- `400`: 13: Request body can't be null 19: New name is null or whitespaces or new name/description is too long 20: New name or description is moderated 22: Invalid language code 26: You can't update translations for source language 53: Language is not supported for the game. 62: Invalid game badge id
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 18: You do not have permission to manage this game
- `500`: 0: An unknown error occurred.
- `503`: 17: Feature is disabled

**Response fields** (`Roblox.GameInternationalization.Api.UpdateBadgeNameDescriptionResponse`)

See [Roblox.GameInternationalization.Api.UpdateBadgeNameDescriptionResponse](#roblox-gameinternationalization-api-updatebadgenamedescriptionresponse) in Models.

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
  "https://apis.roblox.com/legacy-game-internationalization/v1/badges/{BADGEID}/name-description/language-codes/{LANGUAGECODE}" \
  -H "Content-Type: application/json" \
  -d '{
  "name": "string",
  "description": "string"
}'
```

### DELETE `/legacy-game-internationalization/v1/badges/{badgeId}/name-description/language-codes/{languageCode}` [EXPERIMENTAL]

Delete localized name and description of a badge

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `legacy-badge:manage`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `badgeId` | path | `integer` | Yes | The badge id |
| `languageCode` | path | `string` | Yes | The language code of the name and description to delete |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: 22: Invalid language code 23: You can't delete translations for source language 53: Language is not supported for the game. 62: Invalid game badge id
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
  "https://apis.roblox.com/legacy-game-internationalization/v1/badges/{BADGEID}/name-description/language-codes/{LANGUAGECODE}"
```

### PATCH `/legacy-game-internationalization/v1/badges/{badgeId}/name/language-codes/{languageCode}` [EXPERIMENTAL]

Update localized name of a badge

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `legacy-badge:manage`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `badgeId` | path | `integer` | Yes | The badge id |
| `languageCode` | path | `string` | Yes | The language code of the name to update |

**Request Body:** `application/json` — Type: `Roblox.GameInternationalization.Api.UpdateBadgeNameRequest`

See [Roblox.GameInternationalization.Api.UpdateBadgeNameRequest](#roblox-gameinternationalization-api-updatebadgenamerequest) in Models.

**Request example:**
```json
{
  "name": "string"
}
```

**Responses:**

- `200`: OK → `Roblox.GameInternationalization.Api.UpdateBadgeNameResponse`
- `400`: 13: Request body can't be null 19: New name is null or whitespaces or new name/description is too long 20: New name or description is moderated 22: Invalid language code 26: You can't update translations for source language 53: Language is not supported for the game. 62: Invalid game badge id
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 18: You do not have permission to manage this game
- `500`: 0: An unknown error occurred.
- `503`: 17: Feature is disabled

**Response fields** (`Roblox.GameInternationalization.Api.UpdateBadgeNameResponse`)

See [Roblox.GameInternationalization.Api.UpdateBadgeNameResponse](#roblox-gameinternationalization-api-updatebadgenameresponse) in Models.

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
  "https://apis.roblox.com/legacy-game-internationalization/v1/badges/{BADGEID}/name/language-codes/{LANGUAGECODE}" \
  -H "Content-Type: application/json" \
  -d '{
  "name": "string"
}'
```

### GET `/v1/badges/icons` [STABLE]

Thumbnails badge icons.

**Server:** `https://thumbnails.roblox.com`

**Auth:** 

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `badgeIds` | query | `integer[]` | Yes | The badge ids. |
| `size` | query | `150x150` | No | The thumbnail size, formatted widthxheight Valid values: `150x150` |
| `format` | query | `Png \| Webp` | No | The thumbnail format Valid values: `Png`, `Webp` |
| `isCircular` | query | `true \| false` | No | The circle thumbnail output parameter, true or false Valid values: `true`, `false` |

**Responses:**

- `200`: OK
- `400`: 1: There are too many requested Ids. 2: The requested image format is invalid. Please see documentation for valid thumbnail format parameter name and values. 3: The requested size is invalid. Please see documentation for valid thumbnail size parameter name and format. 4: The requested Ids are invalid, of an invalid type or missing. 10: Circular thumbnail requests are not allowed

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://thumbnails.roblox.com/v1/badges/icons?badgeIds={VALUE}"
```

### GET `/v1/badges/metadata` [EXPERIMENTAL]

Gets metadata about the badges system.

Returns creation price and field length limits. Callers use this before creating or editing badges.

**Server:** `https://badges.roblox.com`

**Auth:** 

**Responses:**

- `200`: OK → `Roblox.Badges.Api.BadgeMetadataResponse`

**Response fields** (`Roblox.Badges.Api.BadgeMetadataResponse`)

See [Roblox.Badges.Api.BadgeMetadataResponse](#roblox-badges-api-badgemetadataresponse) in Models.

**Response example:**
```json
{
  "badgeCreationPrice": 0,
  "maxBadgeNameLength": 0,
  "maxBadgeDescriptionLength": 0,
  "defaultBadgeIconImageId": 0
}
```

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://badges.roblox.com/v1/badges/metadata"
```

### GET `/v1/badges/{badgeId}` [EXPERIMENTAL]

Gets badge information by the badge Id.

Returns display fields, award statistics, and owning universe for a single badge.

**Server:** `https://badges.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `badgeId` | path | `integer` | Yes | The badge Id. |

**Responses:**

- `200`: OK → `Roblox.Badges.Api.BadgeResponse`
- `404`: 1: Badge is invalid or does not exist. 3: The game is invalid or does not exist.

**Response fields** (`Roblox.Badges.Api.BadgeResponse`)

See [Roblox.Badges.Api.BadgeResponse](#roblox-badges-api-badgeresponse) in Models.

**Response example:**
```json
{
  "id": 0,
  "name": "string",
  "description": "string",
  "displayName": "string",
  "displayDescription": "string",
  "enabled": false
}
```

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://badges.roblox.com/v1/badges/{BADGEID}"
```

### PATCH `/v1/badges/{badgeId}` [EXPERIMENTAL]

Updates badge configuration.

Managers may change enabled state, name, and description when authorized for the badge.

**Server:** `https://badges.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `badgeId` | path | `integer` | Yes | The badge Id. |

**Request Body:** `application/json` — Type: `Roblox.Badges.Api.UpdateBadgeRequest`

See [Roblox.Badges.Api.UpdateBadgeRequest](#roblox-badges-api-updatebadgerequest) in Models.

**Request example:**
```json
{
  "name": "string",
  "description": "string",
  "enabled": false
}
```

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: 6: Text moderated. 14: Invalid badge name. 15: Invalid badge description.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 2: You do not have permission to manage this badge.
- `404`: 1: Badge is invalid or does not exist. 3: The game is invalid or does not exist.

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X PATCH -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://badges.roblox.com/v1/badges/{BADGEID}" \
  -H "Content-Type: application/json" \
  -d '{
  "name": "string",
  "description": "string",
  "enabled": false
}'
```

### PATCH `/v1/badges/{badgeId}/description/language-codes/{languageCode}` [EXPERIMENTAL]

Update localized description of a badge

**Server:** `https://gameinternationalization.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `badgeId` | path | `integer` | Yes | The badge id |
| `languageCode` | path | `string` | Yes | The language code of the description to update |

**Request Body:** `application/json` — Type: `Roblox.GameInternationalization.Api.UpdateBadgeDescriptionRequest`

See [Roblox.GameInternationalization.Api.UpdateBadgeDescriptionRequest](#roblox-gameinternationalization-api-updatebadgedescriptionrequest) in Models.

**Request example:**
```json
{
  "description": "string"
}
```

**Responses:**

- `200`: OK → `Roblox.GameInternationalization.Api.UpdateBadgeDescriptionResponse`
- `400`: 13: Request body can't be null 19: New name is null or whitespaces or new name/description is too long 20: New name or description is moderated 22: Invalid language code 26: You can't update translations for source language 53: Language is not supported for the game. 62: Invalid game badge id
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 18: You do not have permission to manage this game
- `500`: 0: An unknown error occurred.
- `503`: 17: Feature is disabled

**Response fields** (`Roblox.GameInternationalization.Api.UpdateBadgeDescriptionResponse`)

See [Roblox.GameInternationalization.Api.UpdateBadgeDescriptionResponse](#roblox-gameinternationalization-api-updatebadgedescriptionresponse) in Models.

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
  "https://gameinternationalization.roblox.com/v1/badges/{BADGEID}/description/language-codes/{LANGUAGECODE}" \
  -H "Content-Type: application/json" \
  -d '{
  "description": "string"
}'
```

### GET `/v1/badges/{badgeId}/icons` [EXPERIMENTAL]

Get all icons for a badge

**Server:** `https://gameinternationalization.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `badgeId` | path | `integer` | Yes | The id of the badge |
| `width` | query | `integer` | No | The width of the icon to request |
| `height` | query | `integer` | No | The height of the icon to request |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.GameInternationalization.Api.GetBadgeIconResponse_`
- `400`: 52: Image dimensions are invalid 62: Invalid game badge id
- `401`: 0: Authorization has been denied for this request.
- `500`: 0: An unknown error occurred.
- `503`: 17: Feature is disabled

**Response fields** (`Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.GameInternationalization.Api.GetBadgeIconResponse_`)

See [Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.GameInternationalization.Api.GetBadgeIconResponse_](#roblox-web-webapi-models-apiarrayresponse-roblox-gameinternationalization-api-getbadgeiconresponse-) in Models.

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
  "https://gameinternationalization.roblox.com/v1/badges/{BADGEID}/icons"
```

### POST `/v1/badges/{badgeId}/icons/language-codes/{languageCode}` [EXPERIMENTAL]

Update a badge's icon

**Server:** `https://gameinternationalization.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `badgeId` | path | `integer` | Yes | The id of the badge |
| `languageCode` | path | `string` | Yes | The language code of this icon to update |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: 22: Invalid language code 26: You can't update translations for source language 45: File uploaded does not match known image format 46: File not present in request 53: Language is not supported for the game. 62: Invalid game badge id
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
  "https://gameinternationalization.roblox.com/v1/badges/{BADGEID}/icons/language-codes/{LANGUAGECODE}" \
  -H "Content-Type: application/json" \
  -d '{"key": "value"}'
```

### DELETE `/v1/badges/{badgeId}/icons/language-codes/{languageCode}` [EXPERIMENTAL]

Delete a localized icon from a badge

**Server:** `https://gameinternationalization.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `badgeId` | path | `integer` | Yes | The id of the badge |
| `languageCode` | path | `string` | Yes | The language code of the localized icon to delete |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: 22: Invalid language code 23: You can't delete translations for source language 53: Language is not supported for the game. 62: Invalid game badge id
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
  "https://gameinternationalization.roblox.com/v1/badges/{BADGEID}/icons/language-codes/{LANGUAGECODE}"
```

### GET `/v1/badges/{badgeId}/name-description` [EXPERIMENTAL]

**Server:** `https://gameinternationalization.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `badgeId` | path | `integer` | Yes |  |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.GameInternationalization.Api.NameDescription_`
- `400`: 62: Invalid game badge id
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
  "https://gameinternationalization.roblox.com/v1/badges/{BADGEID}/name-description"
```

### PATCH `/v1/badges/{badgeId}/name-description/language-codes/{languageCode}` [EXPERIMENTAL]

Update localized name and description of a badge

**Server:** `https://gameinternationalization.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `badgeId` | path | `integer` | Yes | The badge id |
| `languageCode` | path | `string` | Yes | The language code of the name and description to Update |

**Request Body:** `application/json` — Type: `Roblox.GameInternationalization.Api.UpdateBadgeNameDescriptionRequest`

See [Roblox.GameInternationalization.Api.UpdateBadgeNameDescriptionRequest](#roblox-gameinternationalization-api-updatebadgenamedescriptionrequest) in Models.

**Request example:**
```json
{
  "name": "string",
  "description": "string"
}
```

**Responses:**

- `200`: OK → `Roblox.GameInternationalization.Api.UpdateBadgeNameDescriptionResponse`
- `400`: 13: Request body can't be null 19: New name is null or whitespaces or new name/description is too long 20: New name or description is moderated 22: Invalid language code 26: You can't update translations for source language 53: Language is not supported for the game. 62: Invalid game badge id
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 18: You do not have permission to manage this game
- `500`: 0: An unknown error occurred.
- `503`: 17: Feature is disabled

**Response fields** (`Roblox.GameInternationalization.Api.UpdateBadgeNameDescriptionResponse`)

See [Roblox.GameInternationalization.Api.UpdateBadgeNameDescriptionResponse](#roblox-gameinternationalization-api-updatebadgenamedescriptionresponse) in Models.

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
  "https://gameinternationalization.roblox.com/v1/badges/{BADGEID}/name-description/language-codes/{LANGUAGECODE}" \
  -H "Content-Type: application/json" \
  -d '{
  "name": "string",
  "description": "string"
}'
```

### DELETE `/v1/badges/{badgeId}/name-description/language-codes/{languageCode}` [EXPERIMENTAL]

Delete localized name and description of a badge

**Server:** `https://gameinternationalization.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `badgeId` | path | `integer` | Yes | The badge id |
| `languageCode` | path | `string` | Yes | The language code of the name and description to delete |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: 22: Invalid language code 23: You can't delete translations for source language 53: Language is not supported for the game. 62: Invalid game badge id
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
  "https://gameinternationalization.roblox.com/v1/badges/{BADGEID}/name-description/language-codes/{LANGUAGECODE}"
```

### PATCH `/v1/badges/{badgeId}/name/language-codes/{languageCode}` [EXPERIMENTAL]

Update localized name of a badge

**Server:** `https://gameinternationalization.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `badgeId` | path | `integer` | Yes | The badge id |
| `languageCode` | path | `string` | Yes | The language code of the name to update |

**Request Body:** `application/json` — Type: `Roblox.GameInternationalization.Api.UpdateBadgeNameRequest`

See [Roblox.GameInternationalization.Api.UpdateBadgeNameRequest](#roblox-gameinternationalization-api-updatebadgenamerequest) in Models.

**Request example:**
```json
{
  "name": "string"
}
```

**Responses:**

- `200`: OK → `Roblox.GameInternationalization.Api.UpdateBadgeNameResponse`
- `400`: 13: Request body can't be null 19: New name is null or whitespaces or new name/description is too long 20: New name or description is moderated 22: Invalid language code 26: You can't update translations for source language 53: Language is not supported for the game. 62: Invalid game badge id
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 18: You do not have permission to manage this game
- `500`: 0: An unknown error occurred.
- `503`: 17: Feature is disabled

**Response fields** (`Roblox.GameInternationalization.Api.UpdateBadgeNameResponse`)

See [Roblox.GameInternationalization.Api.UpdateBadgeNameResponse](#roblox-gameinternationalization-api-updatebadgenameresponse) in Models.

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
  "https://gameinternationalization.roblox.com/v1/badges/{BADGEID}/name/language-codes/{LANGUAGECODE}" \
  -H "Content-Type: application/json" \
  -d '{
  "name": "string"
}'
```

### GET `/v1/universes/{universeId}/badges` [EXPERIMENTAL]

Gets badges by their awarding game.

Lists badges created under the universe's root place, with paging and optional sort.

**Server:** `https://badges.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer` | Yes | The universe Id. |
| `sortBy` | query | `Rank \| DateCreated` | No | The key to sort badges by. Valid values: `Rank`, `DateCreated` |
| `limit` | query | `10 \| 25 \| 50 \| 100` | No | The number of results per request. Valid values: `10`, `25`, `50`, `100` |
| `cursor` | query | `string` | No | The paging cursor for the previous or next page. |
| `sortOrder` | query | `Asc \| Desc` | No | The order the results are sorted in. Valid values: `Asc`, `Desc` |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.Badges.Api.BadgeResponse_`
- `400`: 26: The pagination cursor is invalid or incompatible with the current request.
- `404`: 3: The game is invalid or does not exist.

**Response fields** (`Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.Badges.Api.BadgeResponse_`)

See [Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.Badges.Api.BadgeResponse_](#roblox-web-webapi-models-apipageresponse-roblox-badges-api-badgeresponse-) in Models.

**Response example:**
```json
{
  "previousPageCursor": "string",
  "nextPageCursor": "string",
  "data": [
    {
      "id": "...",
      "name": "...",
      "description": "...",
      "displayName": "...",
      "displayDescription": "...",
      "enabled": "..."
    }
  ]
}
```

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://badges.roblox.com/v1/universes/{UNIVERSEID}/badges"
```

### POST `/v1/universes/{universeId}/badges` [EXPERIMENTAL]

Creates a new badge.

Charges the selected payment source and creates the badge under the universe's root place.

**Server:** `https://badges.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer` | Yes | The ID of the universe to create the badge for. |

**Request Body:** `multipart/form-data` — Type: `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | `string` | No | The badge name. |
| `description` | `string` | No | The badge description. |
| `paymentSourceType` | `1 \| 2` | No | Whether or not to pay for the badge with user funds, or group funds. |
| `files` | `string` | No | The badge icon. Optional: when omitted and a curated default badge icon is configured on |
| `expectedCost` | `integer` | No | User expected cost of a badge. |
| `isActive` | `boolean` | No | Whether or not the badge should be created in the active state. |

**Request example:**
```json
{
  "name": "string",
  "description": "string",
  "paymentSourceType": 1,
  "files": "string",
  "expectedCost": 0,
  "isActive": false
}
```

**Responses:**

- `200`: OK → `Roblox.Web.Responses.Badges.BadgeResponseV2`
- `400`: 11: The badge icon is invalid. 14: Invalid badge name. 15: Invalid badge description. 16: Payment source is invalid. 18: Expected badge cost is different from the actual badge cost.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 6: Text moderated. 12: You do not have permission to manage this game's badges. 17: Insufficient funds.
- `404`: 3: The game is invalid or does not exist.
- `429`: 13: Too many requests, try again later.

**Response fields** (`Roblox.Web.Responses.Badges.BadgeResponseV2`)

See [Roblox.Web.Responses.Badges.BadgeResponseV2](#roblox-web-responses-badges-badgeresponsev2) in Models.

**Response example:**
```json
{
  "id": 0,
  "name": "string",
  "description": "string",
  "displayName": "string",
  "displayDescription": "string",
  "enabled": false
}
```

**Error handling:** `429`: Retry with exponential backoff (start at 1s). `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://badges.roblox.com/v1/universes/{UNIVERSEID}/badges" \
  -F "name=string" \
  -F "description=string" \
  -F "paymentSourceType=1" \
  -F "files=@file.bin;type=application/octet-stream" \
  -F "expectedCost=0" \
  -F "isActive=false"
```

### GET `/v1/universes/{universeId}/free-badges-quota` [EXPERIMENTAL]

Gets the number of free badges left for the current UTC day by their awarding game.

Reflects daily free-creation allowance for the universe when the feature is enabled.

**Server:** `https://badges.roblox.com`

**Auth:** 

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer` | Yes | The universe Id. |

**Responses:**

- `200`: OK → `integer`
- `404`: 3: The game is invalid or does not exist.

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://badges.roblox.com/v1/universes/{UNIVERSEID}/free-badges-quota"
```

### DELETE `/v1/user/badges/{badgeId}` [EXPERIMENTAL]

Removes a badge from the authenticated user.

Revokes the caller's own awarded badge instance when the badge exists on their account.

**Server:** `https://badges.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `badgeId` | path | `integer` | Yes | The badge Id. |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed
- `404`: 1: Badge is invalid or does not exist.

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X DELETE -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://badges.roblox.com/v1/user/badges/{BADGEID}"
```

### GET `/v1/users/{userId}/badges`

Gets a list of badges a user has been awarded.

Respects inventory privacy settings when evaluating which awarded badges are visible.

**Server:** `https://badges.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer` | Yes | The user Id. |
| `limit` | query | `10 \| 25 \| 50 \| 100` | No | The number of results per request. Valid values: `10`, `25`, `50`, `100` |
| `cursor` | query | `string` | No | The paging cursor for the previous or next page. |
| `sortOrder` | query | `Asc \| Desc` | No | The order the results are sorted in. Valid values: `Asc`, `Desc` |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.Badges.Api.GetBadgesByUserResponse_`
- `404`: 4: User is invalid or does not exist.

**Response fields** (`Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.Badges.Api.GetBadgesByUserResponse_`)

See [Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.Badges.Api.GetBadgesByUserResponse_](#roblox-web-webapi-models-apipageresponse-roblox-badges-api-getbadgesbyuserresponse-) in Models.

**Response example:**
```json
{
  "previousPageCursor": "string",
  "nextPageCursor": "string",
  "data": [
    {
      "creator": "...",
      "id": "...",
      "name": "...",
      "description": "...",
      "displayName": "...",
      "displayDescription": "..."
    }
  ]
}
```

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://badges.roblox.com/v1/users/{USERID}/badges"
```

### GET `/v1/users/{userId}/badges/awarded-dates`

Gets timestamps for when badges were awarded to a user.

Batch form of awarded-date lookup with a maximum number of badge ids per request.

**Server:** `https://badges.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer` | Yes | The user Id. |
| `badgeIds` | query | `integer[]` | Yes | The CSV of badge Ids. |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.Badges.Api.BadgeAwardResponse_`
- `400`: 5: Too many badge Ids.
- `404`: 4: User is invalid or does not exist.

**Response fields** (`Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.Badges.Api.BadgeAwardResponse_`)

See [Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.Badges.Api.BadgeAwardResponse_](#roblox-web-webapi-models-apiarrayresponse-roblox-badges-api-badgeawardresponse-) in Models.

**Response example:**
```json
{
  "data": [
    {
      "badgeId": "...",
      "awardedDate": "..."
    }
  ]
}
```

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://badges.roblox.com/v1/users/{USERID}/badges/awarded-dates?badgeIds={VALUE}"
```

### GET `/v1/users/{userId}/badges/{badgeId}/awarded-date`

Gets timestamp for when a single badge was awarded to a user.

Returns 204 when the user has not been awarded the badge or the badge is filtered from view.

**Server:** `https://badges.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer` | Yes | User id. |
| `badgeId` | path | `integer` | Yes | Badge id. |

**Responses:**

- `200`: OK
- `404`: 4: User is invalid or does not exist.

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://badges.roblox.com/v1/users/{USERID}/badges/{BADGEID}/awarded-date"
```

## Models

### Roblox.Badges.Api.UpdateBadgeRequest

A request model used for updating badge information.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | `string` | No | The new badge name. |
| `description` | `string` | No | The new badge description. |
| `enabled` | `boolean` | No | The new enabled state of the badge. |

### Roblox.Web.Responses.Badges.BadgeResponseV2

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | `integer` | No |  |
| `name` | `string` | No |  |
| `description` | `string` | No |  |
| `displayName` | `string` | No |  |
| `displayDescription` | `string` | No |  |
| `enabled` | `boolean` | No |  |
| `iconImageId` | `integer` | No |  |
| `displayIconImageId` | `integer` | No |  |
| `awarder` | `Roblox.Web.Responses.RelatedEntityTypeResponse_Roblox.Platform.Badges.BadgeAwarderType_` | No |  |
| `statistics` | `Roblox.Web.Responses.Badges.BadgeAwardStatisticsResponse` | No |  |
| `created` | `string` | No |  |
| `updated` | `string` | No |  |

### Roblox.GameInternationalization.Api.UpdateBadgeDescriptionRequest

A request model for updating badge description

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `description` | `string` | No | Badge description |

### Roblox.GameInternationalization.Api.UpdateBadgeDescriptionResponse

A response model for updating badge description

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `description` | `string` | No | Badge description saved |

### Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.GameInternationalization.Api.GetBadgeIconResponse_

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | `Roblox.GameInternationalization.Api.GetBadgeIconResponse[]` | No |  |

### Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.GameInternationalization.Api.NameDescription_

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | `Roblox.GameInternationalization.Api.NameDescription[]` | No |  |

### Roblox.GameInternationalization.Api.UpdateBadgeNameDescriptionRequest

A request model for updating badge name and description

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | `string` | No | Badge name |
| `description` | `string` | No | Badge description |

### Roblox.GameInternationalization.Api.UpdateBadgeNameDescriptionResponse

A response model for updating badge name and description

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | `string` | No | Badge name saved |
| `description` | `string` | No | Badge description saved |

### Roblox.GameInternationalization.Api.UpdateBadgeNameRequest

A request model for updating badge name

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | `string` | No | Badge name |

### Roblox.GameInternationalization.Api.UpdateBadgeNameResponse

A response model for updating badge name

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | `string` | No | Badge name saved |

### Roblox.Badges.Api.BadgeMetadataResponse

Metadata about badges.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `badgeCreationPrice` | `integer` | No | The cost in Robux for creating a new badge. |
| `maxBadgeNameLength` | `integer` | No | The max length for a badge name. |
| `maxBadgeDescriptionLength` | `integer` | No | The max length for a badge description. |
| `defaultBadgeIconImageId` | `integer` | No | The asset ID of the curated default badge icon used when a badge is created without an uploaded icon file, or `0` when the default badge icon feature is disabled. |

### Roblox.Badges.Api.BadgeResponse

A response containing badge information.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | `integer` | No | The badge Id. |
| `name` | `string` | No | The name of the badge. |
| `description` | `string` | No | The badge description. |
| `displayName` | `string` | No | The localized name of the badge. |
| `displayDescription` | `string` | No | The localized badge description. |
| `enabled` | `boolean` | No | Whether or not the badge is enabled. |
| `iconImageId` | `integer` | No | The badge icon asset Id. |
| `displayIconImageId` | `integer` | No | The localized badge icon asset Id. |
| `created` | `string` | No | When the badge was created. |
| `updated` | `string` | No | When the badge was updated. |
| `statistics` | `Roblox.Web.Responses.Badges.BadgeAwardStatisticsResponse` | No |  |
| `awardingUniverse` | `Roblox.Badges.Api.UniverseResponse` | No |  |

### Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.Badges.Api.BadgeResponse_

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `previousPageCursor` | `string` | No |  |
| `nextPageCursor` | `string` | No |  |
| `data` | `Roblox.Badges.Api.BadgeResponse[]` | No |  |

### Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.Badges.Api.GetBadgesByUserResponse_

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `previousPageCursor` | `string` | No |  |
| `nextPageCursor` | `string` | No |  |
| `data` | `Roblox.Badges.Api.GetBadgesByUserResponse[]` | No |  |

### Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.Badges.Api.BadgeAwardResponse_

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | `Roblox.Badges.Api.BadgeAwardResponse[]` | No |  |