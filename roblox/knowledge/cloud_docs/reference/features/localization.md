---
name: "Localization"
last_updated: 2026-10-30T19:56:08Z
type: feature
api_base_url: "https://apis.roblox.com"
endpoints: 96
auth: [api-key, oauth2, cookie]
description: "Extend [built-in Roblox localization features](production/localization) with automation"
---

# Localization

Extend [built-in Roblox localization features](production/localization) with automation.

Common use cases include:

- Content translation: Update localized names and descriptions for [badges](#patch_legacy_game_internationalization_v1_badges__badgeId__description_language_codes__languageCode_), [game passes](#patch_legacy_game_internationalization_v1_game_passes__gamePassId__description_language_codes__languageCode_), and [developer products](#patch_legacy_game_internationalization_v1_developer_products__developerProductId__description_language_codes__languageCode_)
- Localization tables: [Manage localization table entries](#patch_legacy_localization_tables_v1_localization_table_tables__tableId_) and [retrieve localized asset entries](#localizationtables_get_v1_localization_table_tables__tableId__asset_entries) for in-game text
- Automatic translation: [Configure automatic translation settings](#patch_legacy_localization_tables_v1_autolocalization_games__gameId__settings) for supported languages

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

### GET `/legacy-game-internationalization/v1/game-icon/games/{gameId}` [EXPERIMENTAL]

Get all icons for a game

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `legacy-universe:manage`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gameId` | path | `integer` | Yes | The id of the game |
| `width` | query | `integer` | No | The width of the icon to request |
| `height` | query | `integer` | No | The height of the icon to request |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.GameInternationalization.Api.GetGameIconResponse_`
- `400`: 14: Invalid game id 52: Image dimensions are invalid
- `500`: 0: An unknown error occurred.
- `503`: 17: Feature is disabled

**Response fields** (`Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.GameInternationalization.Api.GetGameIconResponse_`)

See [Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.GameInternationalization.Api.GetGameIconResponse_](#roblox-web-webapi-models-apiarrayresponse-roblox-gameinternationalization-api-getgameiconresponse-) in Models.

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

**Rate Limits:** perApiKeyOwner: 100/minute, perOauth2Authorization: 100/minute

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/legacy-game-internationalization/v1/game-icon/games/{GAMEID}"
```

### POST `/legacy-game-internationalization/v1/game-icon/games/{gameId}/language-codes/{languageCode}` [EXPERIMENTAL]

Update a game's icon

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `legacy-universe:manage`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gameId` | path | `integer` | Yes | The id of the game |
| `languageCode` | path | `string` | Yes | The language code of this icon to update |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: 14: Invalid game id 22: Invalid language code 26: You can't update translations for source language 45: File uploaded does not match known image format 46: File not present in request 53: Language is not supported for the game.
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
  "https://apis.roblox.com/legacy-game-internationalization/v1/game-icon/games/{GAMEID}/language-codes/{LANGUAGECODE}" \
  -H "Content-Type: application/json" \
  -d '{"key": "value"}'
```

### DELETE `/legacy-game-internationalization/v1/game-icon/games/{gameId}/language-codes/{languageCode}` [EXPERIMENTAL]

Delete a localized icon from a game

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `legacy-universe:manage`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gameId` | path | `integer` | Yes | The id of the game |
| `languageCode` | path | `string` | Yes | The language code of the localized icon to delete |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: 14: Invalid game id 22: Invalid language code 23: You can't delete translations for source language 53: Language is not supported for the game.
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
  "https://apis.roblox.com/legacy-game-internationalization/v1/game-icon/games/{GAMEID}/language-codes/{LANGUAGECODE}"
```

### POST `/legacy-game-internationalization/v1/game-thumbnails/games/{gameId}/language-codes/{languageCode}/alt-text` [EXPERIMENTAL]

Updates the game thumbnail alt text.

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `legacy-universe:manage`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gameId` | path | `integer` | Yes | The game identifier. |
| `languageCode` | path | `string` | Yes | The language code. |

**Request Body:** `application/json` — Type: `Roblox.GameInternationalization.Api.UpdateThumbnailAltTextRequest`

See [Roblox.GameInternationalization.Api.UpdateThumbnailAltTextRequest](#roblox-gameinternationalization-api-updatethumbnailalttextrequest) in Models.

**Request example:**
```json
{
  "thumbnailId": 0,
  "altText": "string"
}
```

**Responses:**

- `200`: OK → `string`
- `400`: 14: Invalid game id 19: New name is null or whitespaces or new name/description is too long 20: New name or description is moderated 22: Invalid language code 26: You can't update translations for source language 45: File uploaded does not match known image format 53: Language is not supported for the game.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 18: You do not have permission to manage this game
- `429`: 24: Too many attempts.Please try again later.
- `500`: 0: An unknown error occurred. 88: Failed to filter text
- `503`: 17: Feature is disabled

**Error handling:** `429`: Retry with exponential backoff (start at 1s). `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 100/minute, perOauth2Authorization: 100/minute

**Example:**
```bash
curl -X POST -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/legacy-game-internationalization/v1/game-thumbnails/games/{GAMEID}/language-codes/{LANGUAGECODE}/alt-text" \
  -H "Content-Type: application/json" \
  -d '{
  "thumbnailId": 0,
  "altText": "string"
}'
```

### POST `/legacy-game-internationalization/v1/game-thumbnails/games/{gameId}/language-codes/{languageCode}/image` [EXPERIMENTAL]

Uploads the game thumbnail.

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `legacy-universe:manage`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gameId` | path | `integer` | Yes | The game identifier. |
| `languageCode` | path | `string` | Yes | The language code. |

**Responses:**

- `200`: OK → `Roblox.GameInternationalization.Api.Models.Response.UploadImageForGameThumbnailResponse`
- `400`: 14: Invalid game id 22: Invalid language code 26: You can't update translations for source language 53: Language is not supported for the game.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 18: You do not have permission to manage this game
- `429`: 24: Too many attempts.Please try again later.
- `500`: 0: An unknown error occurred.
- `503`: 17: Feature is disabled

**Response fields** (`Roblox.GameInternationalization.Api.Models.Response.UploadImageForGameThumbnailResponse`)

See [Roblox.GameInternationalization.Api.Models.Response.UploadImageForGameThumbnailResponse](#roblox-gameinternationalization-api-models-response-uploadimageforgamethumbnailresponse) in Models.

**Response example:**
```json
{
  "mediaAssetId": "string"
}
```

**Error handling:** `429`: Retry with exponential backoff (start at 1s). `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 100/minute, perOauth2Authorization: 100/minute

**Example:**
```bash
curl -X POST -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/legacy-game-internationalization/v1/game-thumbnails/games/{GAMEID}/language-codes/{LANGUAGECODE}/image" \
  -H "Content-Type: application/json" \
  -d '{"key": "value"}'
```

### POST `/legacy-game-internationalization/v1/game-thumbnails/games/{gameId}/language-codes/{languageCode}/images/order` [EXPERIMENTAL]

Orders the specified image Ids for the game thumbnails.

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `legacy-universe:manage`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gameId` | path | `integer` | Yes | The game identifier. |
| `languageCode` | path | `string` | Yes | The language code. |

**Request Body:** `application/json` — Type: `Roblox.GameInternationalization.Api.SortImageIdsRequest`

See [Roblox.GameInternationalization.Api.SortImageIdsRequest](#roblox-gameinternationalization-api-sortimageidsrequest) in Models.

**Request example:**
```json
{
  "mediaAssetIds": [
    0
  ]
}
```

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: 14: Invalid game id 22: Invalid language code 26: You can't update translations for source language 53: Language is not supported for the game.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 18: You do not have permission to manage this game
- `503`: 17: Feature is disabled

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 100/minute, perOauth2Authorization: 100/minute

**Example:**
```bash
curl -X POST -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/legacy-game-internationalization/v1/game-thumbnails/games/{GAMEID}/language-codes/{LANGUAGECODE}/images/order" \
  -H "Content-Type: application/json" \
  -d '{
  "mediaAssetIds": [
    0
  ]
}'
```

### DELETE `/legacy-game-internationalization/v1/game-thumbnails/games/{gameId}/language-codes/{languageCode}/images/{imageId}` [EXPERIMENTAL]

Deletes the game thumbnail.

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `legacy-universe:manage`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gameId` | path | `integer` | Yes | The game identifier. |
| `languageCode` | path | `string` | Yes | The language code. |
| `imageId` | path | `integer` | Yes | The image identifier. |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: 14: Invalid game id 22: Invalid language code 23: You can't delete translations for source language 53: Language is not supported for the game.
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
  "https://apis.roblox.com/legacy-game-internationalization/v1/game-thumbnails/games/{GAMEID}/language-codes/{LANGUAGECODE}/images/{IMAGEID}"
```

### POST `/legacy-game-internationalization/v1/name-description/games/translation-history` [EXPERIMENTAL]

Gets the history for name or description in a provided language.

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `legacy-universe:manage`

**Request Body:** `application/json` — Type: `Roblox.GameInternationalization.Api.GetNameDescriptionHistoryV2Request`

See [Roblox.GameInternationalization.Api.GetNameDescriptionHistoryV2Request](#roblox-gameinternationalization-api-getnamedescriptionhistoryv2request) in Models.

**Request example:**
```json
{
  "contentId": 0,
  "contentType": "UniverseDisplayNames",
  "languageCode": "string",
  "cursor": "string",
  "count": 0,
  "sortOrder": "Asc"
}
```

**Responses:**

- `200`: OK → `Roblox.GameInternationalization.Api.GetNameDescriptionHistoryResponse`
- `400`: 13: Request body can't be null 14: Invalid game id 18: You do not have permission to manage this game 22: Invalid language code 39: Count should be at least 1 and less than 50. 53: Language is not supported for the game. 54: No history available for source data 55: Invalid exclusive start Id
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed
- `500`: 0: An unknown error occurred.
- `503`: 17: Feature is disabled

**Response fields** (`Roblox.GameInternationalization.Api.GetNameDescriptionHistoryResponse`)

See [Roblox.GameInternationalization.Api.GetNameDescriptionHistoryResponse](#roblox-gameinternationalization-api-getnamedescriptionhistoryresponse) in Models.

**Response example:**
```json
{
  "history": [
    {
      "translationText": "...",
      "translator": "...",
      "created": "..."
    }
  ],
  "lastEvaluatedId": "string"
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 100/minute, perOauth2Authorization: 100/minute

**Example:**
```bash
curl -X POST -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/legacy-game-internationalization/v1/name-description/games/translation-history" \
  -H "Content-Type: application/json" \
  -d '{
  "contentId": 0,
  "contentType": "UniverseDisplayNames",
  "languageCode": "string",
  "cursor": "string",
  "count": 0,
  "sortOrder": "Asc"
}'
```

### PATCH `/legacy-game-internationalization/v1/name-description/games/{gameId}` [EXPERIMENTAL]

Updates a game's name and/or description in multiple languages.

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `legacy-universe:manage`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gameId` | path | `integer` | Yes | The id of the game. |

**Request Body:** `application/json` — Type: `Roblox.GameInternationalization.Api.UpdateNameDescriptionsRequest`

See [Roblox.GameInternationalization.Api.UpdateNameDescriptionsRequest](#roblox-gameinternationalization-api-updatenamedescriptionsrequest) in Models.

**Request example:**
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

**Responses:**

- `200`: OK → `Roblox.GameInternationalization.Api.UpdateNameDescriptionsResponse`
- `400`: 14: Invalid game id 19: New name is null or whitespaces or new name/description is too long 20: New name or description is moderated 22: Invalid language code 23: You can't delete translations for source language 26: You can't update translations for source language 53: Language is not supported for the game.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 18: You do not have permission to manage this game
- `503`: 17: Feature is disabled

**Response fields** (`Roblox.GameInternationalization.Api.UpdateNameDescriptionsResponse`)

See [Roblox.GameInternationalization.Api.UpdateNameDescriptionsResponse](#roblox-gameinternationalization-api-updatenamedescriptionsresponse) in Models.

**Response example:**
```json
{
  "successOperations": [
    {
      "name": "...",
      "description": "...",
      "updateType": "...",
      "languageCode": "..."
    }
  ],
  "failedOperations": [
    {
      "languageCode": "...",
      "errorCode": "..."
    }
  ]
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 100/minute, perOauth2Authorization: 100/minute

**Example:**
```bash
curl -X PATCH -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/legacy-game-internationalization/v1/name-description/games/{GAMEID}" \
  -H "Content-Type: application/json" \
  -d '{
  "data": [
    {
      "name": "...",
      "description": "...",
      "updateType": "...",
      "languageCode": "..."
    }
  ]
}'
```

### PATCH `/legacy-game-internationalization/v1/source-language/games/{gameId}` [EXPERIMENTAL]

Sets the source language of a game

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `legacy-universe:manage`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gameId` | path | `integer` | Yes |  |
| `languageCode` | query | `string` | Yes |  |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: 14: Invalid game id 22: Invalid language code
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 18: You do not have permission to manage this game
- `500`: 85: Failed to disable automatic translation status for languages
- `503`: 17: Feature is disabled

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 100/minute, perOauth2Authorization: 100/minute

**Example:**
```bash
curl -X PATCH -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/legacy-game-internationalization/v1/source-language/games/{GAMEID}?languageCode={VALUE}"
```

### PATCH `/legacy-game-internationalization/v1/supported-languages/games/{gameId}` [EXPERIMENTAL]

Add or remove supported languages for a game.

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `legacy-universe:manage`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gameId` | path | `integer` | Yes | The id of the game. |

**Request Body:** `application/json` — Type: `Roblox.GameInternationalization.Api.PatchLanguage[]`

See [Roblox.GameInternationalization.Api.PatchLanguage](#roblox-gameinternationalization-api-patchlanguage) in Models.

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: 14: Invalid game id 22: Invalid language code 49: Duplicate language codes are not allowed.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 18: You do not have permission to manage this game
- `503`: 17: Feature is disabled

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 100/minute, perOauth2Authorization: 100/minute

**Example:**
```bash
curl -X PATCH -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/legacy-game-internationalization/v1/supported-languages/games/{GAMEID}" \
  -H "Content-Type: application/json" \
  -d '[
  {
    "languageCodeType": "Language",
    "languageCode": "string",
    "delete": false
  }
]'
```

### GET `/legacy-game-internationalization/v1/supported-languages/games/{gameId}/automatic-translation-status` [EXPERIMENTAL]

Get the automatic translation status of supported languages for a game.

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `legacy-universe:manage`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gameId` | path | `integer` | Yes | The id of the game. |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.GameInternationalization.Api.LanguageOrLocaleSettings_`
- `400`: 14: Invalid game id
- `401`: 0: Authorization has been denied for this request.
- `403`: 18: You do not have permission to manage this game
- `503`: 17: Feature is disabled

**Response fields** (`Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.GameInternationalization.Api.LanguageOrLocaleSettings_`)

See [Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.GameInternationalization.Api.LanguageOrLocaleSettings_](#roblox-web-webapi-models-apiarrayresponse-roblox-gameinternationalization-api-languageorlocalesettings-) in Models.

**Response example:**
```json
{
  "data": [
    {
      "languageCodeType": "...",
      "languageCode": "...",
      "isAutomaticTranslationEnabled": "...",
      "isImageTranslationEnabled": "..."
    }
  ]
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 100/minute, perOauth2Authorization: 100/minute

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/legacy-game-internationalization/v1/supported-languages/games/{GAMEID}/automatic-translation-status"
```

### PATCH `/legacy-game-internationalization/v1/supported-languages/games/{gameId}/languages/{languageCode}/automatic-translation-status` [EXPERIMENTAL]

Enable or disable automatic translation for a game and language.

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `legacy-universe:manage`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gameId` | path | `integer` | Yes | The id of the game. |
| `languageCode` | path | `string` | Yes | The language to enable or disable for automatic translation. |

**Request Body:** `application/json` — Type: `boolean`

**Responses:**

- `200`: OK → `Roblox.GameInternationalization.Api.EditAutomaticTranslationStatusForGameAndLanguageResponse`
- `400`: 14: Invalid game id 22: Invalid language code 53: Language is not supported for the game. 72: Automatic translation cannot be enabled for game. 75: Automatic translation cannot be enabled for language.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 18: You do not have permission to manage this game
- `503`: 17: Feature is disabled

**Response fields** (`Roblox.GameInternationalization.Api.EditAutomaticTranslationStatusForGameAndLanguageResponse`)

See [Roblox.GameInternationalization.Api.EditAutomaticTranslationStatusForGameAndLanguageResponse](#roblox-gameinternationalization-api-editautomatictranslationstatusforgameandlanguageresponse) in Models.

**Response example:**
```json
{
  "gameId": 0,
  "languageCode": "string",
  "isAutomaticTranslationEnabled": false
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 100/minute, perOauth2Authorization: 100/minute

**Example:**
```bash
curl -X PATCH -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/legacy-game-internationalization/v1/supported-languages/games/{GAMEID}/languages/{LANGUAGECODE}/automatic-translation-status" \
  -H "Content-Type: application/json" \
  -d 'false'
```

### PATCH `/legacy-game-internationalization/v1/supported-languages/games/{gameId}/languages/{languageCode}/image-translation-status` [EXPERIMENTAL]

Enable or disable image translation for a game and language.

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `legacy-universe:manage`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gameId` | path | `integer` | Yes | The id of the game. |
| `languageCode` | path | `string` | Yes | The language to enable or disable for image translation. |

**Request Body:** `application/json` — Type: `boolean`

**Responses:**

- `200`: OK → `Roblox.GameInternationalization.Api.EditImageTranslationStatusForGameAndLanguageResponse`
- `400`: 14: Invalid game id 22: Invalid language code 53: Language is not supported for the game. 93: Image translation cannot be enabled for language.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 18: You do not have permission to manage this game
- `503`: 17: Feature is disabled

**Response fields** (`Roblox.GameInternationalization.Api.EditImageTranslationStatusForGameAndLanguageResponse`)

See [Roblox.GameInternationalization.Api.EditImageTranslationStatusForGameAndLanguageResponse](#roblox-gameinternationalization-api-editimagetranslationstatusforgameandlanguageresponse) in Models.

**Response example:**
```json
{
  "gameId": 0,
  "languageCode": "string",
  "isImageTranslationEnabled": false
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 100/minute, perOauth2Authorization: 100/minute

**Example:**
```bash
curl -X PATCH -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/legacy-game-internationalization/v1/supported-languages/games/{GAMEID}/languages/{LANGUAGECODE}/image-translation-status" \
  -H "Content-Type: application/json" \
  -d 'false'
```

### PATCH `/legacy-game-internationalization/v1/supported-languages/games/{gameId}/languages/{languageCode}/universe-display-info-automatic-translation-settings` [EXPERIMENTAL]

Update the switch which controls if the UniverseDisplayInformation should be automatically translated.

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `legacy-universe:manage`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gameId` | path | `integer` | Yes | The game id. |
| `languageCode` | path | `string` | Yes | The language code. |

**Request Body:** `application/json` — Type: `boolean`

**Responses:**

- `200`: OK → `Roblox.GameInternationalization.Api.UpdateUniverseDisplayInfoAutomaticTranslationSettingsResponse`
- `400`: 14: Invalid game id 72: Automatic translation cannot be enabled for game.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 18: You do not have permission to manage this game
- `500`: 77: Content localization set settings return error code invalid 79: Invalid content instance settings 80: Invalid quota settings 81: Invalid change agent 82: Failed to update UniverseDisplayInformation content instance auto translation settings

**Response fields** (`Roblox.GameInternationalization.Api.UpdateUniverseDisplayInfoAutomaticTranslationSettingsResponse`)

See [Roblox.GameInternationalization.Api.UpdateUniverseDisplayInfoAutomaticTranslationSettingsResponse](#roblox-gameinternationalization-api-updateuniversedisplayinfoautomatictranslationsettingsresponse) in Models.

**Response example:**
```json
{
  "gameId": 0,
  "languageCode": "string",
  "isUniverseDisplayInfoAutomaticTranslationEnabled": false
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 100/minute, perOauth2Authorization: 100/minute

**Example:**
```bash
curl -X PATCH -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/legacy-game-internationalization/v1/supported-languages/games/{GAMEID}/languages/{LANGUAGECODE}/universe-display-info-automatic-translation-settings" \
  -H "Content-Type: application/json" \
  -d 'false'
```

### GET `/legacy-game-internationalization/v1/supported-languages/games/{gameId}/universe-display-info-automatic-translation-settings` [EXPERIMENTAL]

Get UniverseDisplayInfo automatic translation settings.

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `legacy-universe:manage`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gameId` | path | `integer` | Yes | The game id. |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.GameInternationalization.Api.UniverseDisplayInfoAutomaticTranslationSettings_`
- `400`: 14: Invalid game id
- `401`: 0: Authorization has been denied for this request.
- `403`: 18: You do not have permission to manage this game
- `500`: 0: An unknown error occurred. 22: Invalid language code 83: Failed to get UniverseDisplayInformation content instance auto translation settings 84: Count of language code is larger than max batch get size

**Response fields** (`Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.GameInternationalization.Api.UniverseDisplayInfoAutomaticTranslationSettings_`)

See [Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.GameInternationalization.Api.UniverseDisplayInfoAutomaticTranslationSettings_](#roblox-web-webapi-models-apiarrayresponse-roblox-gameinternationalization-api-universedisplayinfoautomatictranslationsettings-) in Models.

**Response example:**
```json
{
  "data": [
    {
      "languageCode": "...",
      "isUniverseDisplayInfoAutomaticTranslationEnabled": "..."
    }
  ]
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 100/minute, perOauth2Authorization: 100/minute

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/legacy-game-internationalization/v1/supported-languages/games/{GAMEID}/universe-display-info-automatic-translation-settings"
```

### POST `/legacy-localization-tables/v1/autolocalization/games/{gameId}/autolocalizationtable` [EXPERIMENTAL]

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `legacy-universe:manage`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gameId` | path | `integer` | Yes |  |

**Responses:**

- `200`: OK → `Roblox.LocalizationTables.Api.GameAutolocalizationInformationResponse`
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed

**Response fields** (`Roblox.LocalizationTables.Api.GameAutolocalizationInformationResponse`)

See [Roblox.LocalizationTables.Api.GameAutolocalizationInformationResponse](#roblox-localizationtables-api-gameautolocalizationinformationresponse) in Models.

**Response example:**
```json
{
  "isAutolocalizationEnabled": false,
  "isAutomaticEntriesSettingEnabled": false,
  "isAutomaticEntriesDeletionEnabled": false,
  "shouldUseLocalizationTable": false,
  "autoLocalizationTableId": "string",
  "sourceLanguage": "string"
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 100/minute, perOauth2Authorization: 100/minute

**Example:**
```bash
curl -X POST -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/legacy-localization-tables/v1/autolocalization/games/{GAMEID}/autolocalizationtable"
```

### PATCH `/legacy-localization-tables/v1/autolocalization/games/{gameId}/settings` [EXPERIMENTAL]

Sets a game's auto-localization related settings

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `legacy-universe:manage`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gameId` | path | `integer` | Yes | The id of the game. |

**Request Body:** `application/json` — Type: `Roblox.LocalizationTables.Api.SetAutolocalizationSettingsForGameRequest`

See [Roblox.LocalizationTables.Api.SetAutolocalizationSettingsForGameRequest](#roblox-localizationtables-api-setautolocalizationsettingsforgamerequest) in Models.

**Request example:**
```json
{
  "isAutolocalizationEnabled": false,
  "isAutomaticEntriesSettingEnabled": false,
  "isAutomaticEntriesDeletionsEnabled": false,
  "shouldUseLocalizationTable": false,
  "shouldUseImageLocalizationTable": false,
  "isAutoLocalizationForImageEnabled": false
}
```

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: 14: Invalid game id 61: IsAutomaticEntriesSettingEnabled can only be enabled if IsAutolocalizationEnabled is also enabled.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 18: You do not have permission to manage this game
- `503`: 17: Feature is disabled

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 100/minute, perOauth2Authorization: 100/minute

**Example:**
```bash
curl -X PATCH -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/legacy-localization-tables/v1/autolocalization/games/{GAMEID}/settings" \
  -H "Content-Type: application/json" \
  -d '{
  "isAutolocalizationEnabled": false,
  "isAutomaticEntriesSettingEnabled": false,
  "isAutomaticEntriesDeletionsEnabled": false,
  "shouldUseLocalizationTable": false,
  "shouldUseImageLocalizationTable": false,
  "isAutoLocalizationForImageEnabled": false
}'
```

### GET `/legacy-localization-tables/v1/autolocalization/metadata` [EXPERIMENTAL]

Metadata for AutoLocalization Configuration

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `legacy-universe:manage`

**Responses:**

- `200`: OK → `Roblox.LocalizationTables.Api.AutoLocalizationMetadataResponse`
- `401`: 0: Authorization has been denied for this request.

**Response fields** (`Roblox.LocalizationTables.Api.AutoLocalizationMetadataResponse`)

See [Roblox.LocalizationTables.Api.AutoLocalizationMetadataResponse](#roblox-localizationtables-api-autolocalizationmetadataresponse) in Models.

**Response example:**
```json
{
  "isReactVersionEnabledForAutoLocalizationSettings": false,
  "isTabbedUIEnabledForConfigureLocalizationPage": false,
  "isAutomaticTranslationToggleUIEnabled": false,
  "isAutomaticTranslationQuotaUIEnabled": false
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Rate Limits:** perApiKeyOwner: 100/minute, perOauth2Authorization: 100/minute

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/legacy-localization-tables/v1/autolocalization/metadata"
```

### GET `/legacy-localization-tables/v1/localization-table/limits` [EXPERIMENTAL]

Get limits for translation table entries operations

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `legacy-universe:manage`

**Responses:**

- `200`: OK → `Roblox.LocalizationTables.Api.GetLimitsResponse`
- `401`: 0: Authorization has been denied for this request.

**Response fields** (`Roblox.LocalizationTables.Api.GetLimitsResponse`)

See [Roblox.LocalizationTables.Api.GetLimitsResponse](#roblox-localizationtables-api-getlimitsresponse) in Models.

**Response example:**
```json
{
  "entryOperationLimits": {
    "maxContextLength": 0,
    "maxKeyLength": 0,
    "maxSourceLength": 0,
    "maxExampleLength": 0,
    "maxGameLocationPathLength": 0
  },
  "tableOperationLimits": {
    "maxEntriesPerUpdate": 0
  }
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Rate Limits:** perApiKeyOwner: 100/minute, perOauth2Authorization: 100/minute

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/legacy-localization-tables/v1/localization-table/limits"
```

### GET `/legacy-localization-tables/v1/localization-table/tables/{tableId}` [EXPERIMENTAL]

Get table information by the id of the table.

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `legacy-universe:manage`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `tableId` | path | `string` | Yes |  |

**Responses:**

- `200`: OK → `Roblox.LocalizationTables.Api.GetTableResponse`
- `400`: 3: Invalid table id.
- `401`: 0: Authorization has been denied for this request.
- `403`: 2: You do not have permission to get this table.

**Response fields** (`Roblox.LocalizationTables.Api.GetTableResponse`)

See [Roblox.LocalizationTables.Api.GetTableResponse](#roblox-localizationtables-api-gettableresponse) in Models.

**Response example:**
```json
{
  "id": "string",
  "name": "string",
  "ownerType": "User",
  "ownerId": 0,
  "assetId": 0
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 100/minute, perOauth2Authorization: 100/minute

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/legacy-localization-tables/v1/localization-table/tables/{TABLEID}"
```

### PATCH `/legacy-localization-tables/v1/localization-table/tables/{tableId}` [EXPERIMENTAL]

Updates the tables contents based on what is provided.

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `legacy-universe:manage`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `tableId` | path | `string` | Yes | The table guid for the table to update. |
| `gameId` | query | `integer` | No | The game id. |

**Request Body:** `application/json` — Type: `Roblox.LocalizationTables.Api.UpdateTableContentsRequest`

See [Roblox.LocalizationTables.Api.UpdateTableContentsRequest](#roblox-localizationtables-api-updatetablecontentsrequest) in Models.

**Request example:**
```json
{
  "name": "string",
  "entries": [
    {
      "identifier": "...",
      "metadata": "...",
      "translations": "...",
      "delete": "..."
    }
  ]
}
```

**Responses:**

- `200`: OK → `Roblox.LocalizationTables.Api.UpdateTableContentsResponse`
- `400`: 3: Invalid table id. 4: Table does not exist. 10: Maximum entries exceeded. Please keep the number of entries per request below the maximum. 13: Request body can't be null 14: Invalid game id
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 6: You do not have permission to create this table.
- `503`: 17: Feature is disabled

**Response fields** (`Roblox.LocalizationTables.Api.UpdateTableContentsResponse`)

See [Roblox.LocalizationTables.Api.UpdateTableContentsResponse](#roblox-localizationtables-api-updatetablecontentsresponse) in Models.

**Response example:**
```json
{
  "failedEntriesAndTranslations": [
    {
      "error": "...",
      "identifier": "...",
      "metadata": "...",
      "translations": "...",
      "createdTime": "..."
    }
  ],
  "modifiedEntriesAndTranslations": [
    {
      "identifier": "...",
      "translations": "..."
    }
  ]
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 100/minute, perOauth2Authorization: 100/minute

**Example:**
```bash
curl -X PATCH -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/legacy-localization-tables/v1/localization-table/tables/{TABLEID}" \
  -H "Content-Type: application/json" \
  -d '{
  "name": "string",
  "entries": [
    {
      "identifier": "...",
      "metadata": "...",
      "translations": "...",
      "delete": "..."
    }
  ]
}'
```

### GET `/legacy-localization-tables/v1/localization-table/tables/{tableId}/entries` [EXPERIMENTAL]

Gets a batch of entries for a table.

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `legacy-universe:manage`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `tableId` | path | `string` | Yes |  |
| `cursor` | query | `string` | No | If null, there are no more entries in the table and you've reached the last page. |
| `gameId` | query | `integer` | No |  |
| `entryFormat` | query | `Invalid \| Legacy \| Icu` | No | Valid values: `Invalid`, `Legacy`, `Icu` |

**Responses:**

- `200`: OK → `Roblox.LocalizationTables.Api.GetTableEntriesPagedResponse`
- `400`: 3: Invalid table id. 14: Invalid game id
- `401`: 0: Authorization has been denied for this request.
- `403`: 2: You do not have permission to get this table.

**Response fields** (`Roblox.LocalizationTables.Api.GetTableEntriesPagedResponse`)

See [Roblox.LocalizationTables.Api.GetTableEntriesPagedResponse](#roblox-localizationtables-api-gettableentriespagedresponse) in Models.

**Response example:**
```json
{
  "previousPageCursor": "string",
  "nextPageCursor": "string",
  "data": [
    {
      "identifier": "...",
      "metadata": "...",
      "translations": "...",
      "createdTime": "..."
    }
  ]
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 100/minute, perOauth2Authorization: 100/minute

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/legacy-localization-tables/v1/localization-table/tables/{TABLEID}/entries"
```

### POST `/legacy-localization-tables/v1/localization-table/tables/{tableId}/entries/translation-history` [EXPERIMENTAL]

Gets the translation history for each entry passed in.

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `legacy-universe:manage`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `tableId` | path | `string` | Yes | The entries' tableId. |
| `gameId` | query | `integer` | No | The game id. |

**Request Body:** `application/json` — Type: `Roblox.LocalizationTables.Api.GetTableEntriesTranslationHistoryRequest`

See [Roblox.LocalizationTables.Api.GetTableEntriesTranslationHistoryRequest](#roblox-localizationtables-api-gettableentriestranslationhistoryrequest) in Models.

**Request example:**
```json
{
  "locale": "string",
  "entries": [
    {
      "cursor": "...",
      "identifier": "...",
      "count": "...",
      "sortOrder": "..."
    }
  ],
  "sourceType": "Invalid"
}
```

**Responses:**

- `200`: OK → `Roblox.LocalizationTables.Api.GetTableEntriesTranslationHistoryResponse`
- `400`: 3: Invalid table id. 13: Request body can't be null 14: Invalid game id 16: Entries can't be null or empty 35: The entries provided are invalid 37: Invalid locale code. 38: Invalid entry identifier. 39: Count should be at least 1. 45: Invalid exclusive start id.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 2: You do not have permission to get this table.
- `429`: 24: Too many attempts.Please try again later.
- `503`: 17: Feature is disabled

**Response fields** (`Roblox.LocalizationTables.Api.GetTableEntriesTranslationHistoryResponse`)

See [Roblox.LocalizationTables.Api.GetTableEntriesTranslationHistoryResponse](#roblox-localizationtables-api-gettableentriestranslationhistoryresponse) in Models.

**Response example:**
```json
{
  "tableId": "string",
  "locale": "string",
  "entries": [
    {
      "identifier": "...",
      "history": "...",
      "nextCursor": "..."
    }
  ],
  "failedEntries": [
    {
      "identifier": "...",
      "count": "...",
      "error": "..."
    }
  ]
}
```

**Error handling:** `429`: Retry with exponential backoff (start at 1s). `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 100/minute, perOauth2Authorization: 100/minute

**Example:**
```bash
curl -X POST -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/legacy-localization-tables/v1/localization-table/tables/{TABLEID}/entries/translation-history" \
  -H "Content-Type: application/json" \
  -d '{
  "locale": "string",
  "entries": [
    {
      "cursor": "...",
      "identifier": "...",
      "count": "...",
      "sortOrder": "..."
    }
  ],
  "sourceType": "Invalid"
}'
```

### GET `/legacy-localization-tables/v1/localization-table/tables/{tableId}/entry-count` [EXPERIMENTAL]

Gets the number of entries in the specified table

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `legacy-universe:manage`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `tableId` | path | `string` | Yes | The table id |
| `gameId` | query | `integer` | No | The game id |
| `entryFormat` | query | `Invalid \| Legacy \| Icu` | No | Valid values: `Invalid`, `Legacy`, `Icu` |

**Responses:**

- `200`: OK → `Roblox.LocalizationTables.Api.GetTableEntryCountResponse`
- `400`: 3: Invalid table id. 14: Invalid game id
- `401`: 0: Authorization has been denied for this request.
- `403`: 2: You do not have permission to get this table.

**Response fields** (`Roblox.LocalizationTables.Api.GetTableEntryCountResponse`)

See [Roblox.LocalizationTables.Api.GetTableEntryCountResponse](#roblox-localizationtables-api-gettableentrycountresponse) in Models.

**Response example:**
```json
{
  "id": "string",
  "entryCount": 0
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 100/minute, perOauth2Authorization: 100/minute

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/legacy-localization-tables/v1/localization-table/tables/{TABLEID}/entry-count"
```

### POST `/v1/auto-localization-table/games/{gameId}/assets-generation-request` [EXPERIMENTAL]

Generates localization asset of a game.

**Server:** `https://localizationtables.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gameId` | path | `integer` | Yes | The game id. |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: 3: Invalid table id. 14: Invalid game id 29: You do not have permission to generate asset for this table. 32: LocalizationTable is not available for the game. 34: Actor provided is invalid
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed
- `429`: 24: Too many attempts.Please try again later.

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `429`: Retry with exponential backoff (start at 1s). `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://localizationtables.roblox.com/v1/auto-localization-table/games/{GAMEID}/assets-generation-request"
```

### POST `/v1/auto-localization-table/games/{gameId}/auto-scrape-cleanup-request` [EXPERIMENTAL]

Enqueues an event to flush the auto scraped entries which doesn't have translations.

**Server:** `https://localizationtables.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gameId` | path | `integer` | Yes | The id of the game. |

**Request Body:** `application/json` — Type: `Roblox.LocalizationTables.Api.RaiseEventForAutoScrapedEntriesCleanupRequest`

See [Roblox.LocalizationTables.Api.RaiseEventForAutoScrapedEntriesCleanupRequest](#roblox-localizationtables-api-raiseeventforautoscrapedentriescleanuprequest) in Models.

**Request example:**
```json
{
  "maxAgeForFlush": "string"
}
```

**Responses:**

- `200`: OK → `object`
- `400`: 14: Invalid game id 31: You do not have permission to flush auto scraped entries asset for this game. 32: LocalizationTable is not available for the game. 34: Actor provided is invalid
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed
- `429`: 33: Too many attempts to flush the game.Please try again later.

**Error handling:** `429`: Retry with exponential backoff (start at 1s). `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://localizationtables.roblox.com/v1/auto-localization-table/games/{GAMEID}/auto-scrape-cleanup-request" \
  -H "Content-Type: application/json" \
  -d '{
  "maxAgeForFlush": "string"
}'
```

### PATCH `/v1/auto-localization-table/games/{gameId}/ingestion`

Ingests entries for auto localization. Needs to be an authorized user.

**Server:** `https://localizationtables.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gameId` | path | `integer` | Yes | The game id. |

**Responses:**

- `200`: OK → `object`
- `400`: 10: Maximum entries exceeded. Please keep the number of entries per request below the maximum. 13: Request body can't be null 16: Entries can't be null or empty 34: Actor provided is invalid
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed
- `503`: 17: Feature is disabled

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X PATCH -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://localizationtables.roblox.com/v1/auto-localization-table/games/{GAMEID}/ingestion" \
  -H "Content-Type: application/json" \
  -d '{"key": "value"}'
```

### POST `/v1/autolocalization/games/{gameId}/autolocalizationtable` *(deprecated)*

Use the Autolocalization controller in LocalizationTables API

**Server:** `https://gameinternationalization.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gameId` | path | `integer` | Yes |  |

**Responses:**

- `200`: OK → `Roblox.GameInternationalization.Api.GameAutolocalizationInformationResponse`
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed

**Response fields** (`Roblox.GameInternationalization.Api.GameAutolocalizationInformationResponse`)

See [Roblox.GameInternationalization.Api.GameAutolocalizationInformationResponse](#roblox-gameinternationalization-api-gameautolocalizationinformationresponse) in Models.

**Response example:**
```json
{
  "isAutolocalizationEnabled": false,
  "shouldUseLocalizationTable": false,
  "shouldUseImageLocalizationTable": false,
  "isAutoLocalizationForImageEnabled": false,
  "autoLocalizationTableId": "string",
  "assetId": 0
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://gameinternationalization.roblox.com/v1/autolocalization/games/{GAMEID}/autolocalizationtable"
```

### PATCH `/v1/autolocalization/games/{gameId}/autolocalizationtable` *(deprecated)*

Use the Autolocalization controller in LocalizationTables API

**Server:** `https://gameinternationalization.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gameId` | path | `integer` | Yes |  |

**Request Body:** `application/json` — Type: `Roblox.GameInternationalization.Api.SetAutolocalizationTableForGameRequest`

See [Roblox.GameInternationalization.Api.SetAutolocalizationTableForGameRequest](#roblox-gameinternationalization-api-setautolocalizationtableforgamerequest) in Models.

**Request example:**
```json
{
  "tableId": "string"
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
curl -X PATCH -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://gameinternationalization.roblox.com/v1/autolocalization/games/{GAMEID}/autolocalizationtable" \
  -H "Content-Type: application/json" \
  -d '{
  "tableId": "string"
}'
```

### POST `/v1/autolocalization/games/{gameId}/autolocalizationtable#localizationtables.roblox.com` [EXPERIMENTAL]

**Server:** `https://localizationtables.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gameId` | path | `integer` | Yes |  |

**Responses:**

- `200`: OK → `Roblox.LocalizationTables.Api.GameAutolocalizationInformationResponse`
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed

**Response fields** (`Roblox.LocalizationTables.Api.GameAutolocalizationInformationResponse`)

See [Roblox.LocalizationTables.Api.GameAutolocalizationInformationResponse](#roblox-localizationtables-api-gameautolocalizationinformationresponse) in Models.

**Response example:**
```json
{
  "isAutolocalizationEnabled": false,
  "isAutomaticEntriesSettingEnabled": false,
  "isAutomaticEntriesDeletionEnabled": false,
  "shouldUseLocalizationTable": false,
  "autoLocalizationTableId": "string",
  "sourceLanguage": "string"
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://localizationtables.roblox.com/v1/autolocalization/games/{GAMEID}/autolocalizationtable#localizationtables.roblox.com"
```

### PATCH `/v1/autolocalization/games/{gameId}/autolocalizationtable#localizationtables.roblox.com` [EXPERIMENTAL]

**Server:** `https://localizationtables.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gameId` | path | `integer` | Yes |  |

**Request Body:** `application/json` — Type: `Roblox.LocalizationTables.Api.SetAutolocalizationTableForGameRequest`

See [Roblox.LocalizationTables.Api.SetAutolocalizationTableForGameRequest](#roblox-localizationtables-api-setautolocalizationtableforgamerequest) in Models.

**Request example:**
```json
{
  "tableId": "string"
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
curl -X PATCH -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://localizationtables.roblox.com/v1/autolocalization/games/{GAMEID}/autolocalizationtable#localizationtables.roblox.com" \
  -H "Content-Type: application/json" \
  -d '{
  "tableId": "string"
}'
```

### PATCH `/v1/autolocalization/games/{gameId}/settings` *(deprecated)*

Sets a game's auto-localization related settings

Use the Autolocalization controller in LocalizationTables API

**Server:** `https://gameinternationalization.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gameId` | path | `integer` | Yes | The id of the game. |

**Request Body:** `application/json` — Type: `Roblox.GameInternationalization.Api.SetAutolocalizationSettingsForGameRequest`

See [Roblox.GameInternationalization.Api.SetAutolocalizationSettingsForGameRequest](#roblox-gameinternationalization-api-setautolocalizationsettingsforgamerequest) in Models.

**Request example:**
```json
{
  "isAutolocalizationEnabled": false,
  "shouldUseLocalizationTable": false
}
```

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: 14: Invalid game id
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 18: You do not have permission to manage this game
- `503`: 17: Feature is disabled

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X PATCH -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://gameinternationalization.roblox.com/v1/autolocalization/games/{GAMEID}/settings" \
  -H "Content-Type: application/json" \
  -d '{
  "isAutolocalizationEnabled": false,
  "shouldUseLocalizationTable": false
}'
```

### PATCH `/v1/autolocalization/games/{gameId}/settings#localizationtables.roblox.com` [EXPERIMENTAL]

Sets a game's auto-localization related settings

**Server:** `https://localizationtables.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gameId` | path | `integer` | Yes | The id of the game. |

**Request Body:** `application/json` — Type: `Roblox.LocalizationTables.Api.SetAutolocalizationSettingsForGameRequest`

See [Roblox.LocalizationTables.Api.SetAutolocalizationSettingsForGameRequest](#roblox-localizationtables-api-setautolocalizationsettingsforgamerequest) in Models.

**Request example:**
```json
{
  "isAutolocalizationEnabled": false,
  "isAutomaticEntriesSettingEnabled": false,
  "isAutomaticEntriesDeletionsEnabled": false,
  "shouldUseLocalizationTable": false,
  "shouldUseImageLocalizationTable": false,
  "isAutoLocalizationForImageEnabled": false
}
```

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: 14: Invalid game id 61: IsAutomaticEntriesSettingEnabled can only be enabled if IsAutolocalizationEnabled is also enabled.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 18: You do not have permission to manage this game
- `503`: 17: Feature is disabled

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X PATCH -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://localizationtables.roblox.com/v1/autolocalization/games/{GAMEID}/settings#localizationtables.roblox.com" \
  -H "Content-Type: application/json" \
  -d '{
  "isAutolocalizationEnabled": false,
  "isAutomaticEntriesSettingEnabled": false,
  "isAutomaticEntriesDeletionsEnabled": false,
  "shouldUseLocalizationTable": false,
  "shouldUseImageLocalizationTable": false,
  "isAutoLocalizationForImageEnabled": false
}'
```

### GET `/v1/autolocalization/metadata#localizationtables.roblox.com` [EXPERIMENTAL]

Metadata for AutoLocalization Configuration

**Server:** `https://localizationtables.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Responses:**

- `200`: OK → `Roblox.LocalizationTables.Api.AutoLocalizationMetadataResponse`
- `401`: 0: Authorization has been denied for this request.

**Response fields** (`Roblox.LocalizationTables.Api.AutoLocalizationMetadataResponse`)

See [Roblox.LocalizationTables.Api.AutoLocalizationMetadataResponse](#roblox-localizationtables-api-autolocalizationmetadataresponse) in Models.

**Response example:**
```json
{
  "isReactVersionEnabledForAutoLocalizationSettings": false,
  "isTabbedUIEnabledForConfigureLocalizationPage": false,
  "isAutomaticTranslationToggleUIEnabled": false,
  "isAutomaticTranslationQuotaUIEnabled": false
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://localizationtables.roblox.com/v1/autolocalization/metadata#localizationtables.roblox.com"
```

### GET `/v1/automatic-translation/games/{gameId}/feature-status` [EXPERIMENTAL]

Checks if automatic translation can be enabled for a game.
The user must still have proper permissions for the game to get this info.

**Server:** `https://gameinternationalization.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gameId` | path | `integer` | Yes | The game id. |

**Responses:**

- `200`: OK → `Roblox.GameInternationalization.Api.GetAutomaticTranslationFeatureStatusForGameResponse`
- `401`: 0: Authorization has been denied for this request.
- `403`: 18: You do not have permission to manage this game
- `503`: 17: Feature is disabled

**Response fields** (`Roblox.GameInternationalization.Api.GetAutomaticTranslationFeatureStatusForGameResponse`)

See [Roblox.GameInternationalization.Api.GetAutomaticTranslationFeatureStatusForGameResponse](#roblox-gameinternationalization-api-getautomatictranslationfeaturestatusforgameresponse) in Models.

**Response example:**
```json
{
  "gameId": 0,
  "isAutomaticTranslationAllowed": false,
  "isAutomaticTranslationSwitchesUIEnabled": false
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://gameinternationalization.roblox.com/v1/automatic-translation/games/{GAMEID}/feature-status"
```

### GET `/v1/automatic-translation/games/{gameId}/quota` [EXPERIMENTAL]

Returns the automatic translation quota info for a game.
The user must still have proper permissions for the game to get this info.

**Server:** `https://gameinternationalization.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gameId` | path | `integer` | Yes | The game id. |

**Responses:**

- `200`: OK → `Roblox.GameInternationalization.Api.GetAutomaticTranslationQuotaForGameResponse`
- `400`: 14: Invalid game id
- `401`: 0: Authorization has been denied for this request.
- `403`: 18: You do not have permission to manage this game
- `503`: 17: Feature is disabled

**Response fields** (`Roblox.GameInternationalization.Api.GetAutomaticTranslationQuotaForGameResponse`)

See [Roblox.GameInternationalization.Api.GetAutomaticTranslationQuotaForGameResponse](#roblox-gameinternationalization-api-getautomatictranslationquotaforgameresponse) in Models.

**Response example:**
```json
{
  "monthlyQuota": {
    "previousRefreshDate": "2024-01-01T00:00:00Z",
    "nextRefreshDate": "2024-01-01T00:00:00Z",
    "remaining": 0,
    "capacity": 0
  },
  "bankQuota": {
    "remaining": 0,
    "capacity": 0
  }
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://gameinternationalization.roblox.com/v1/automatic-translation/games/{GAMEID}/quota"
```

### GET `/v1/automatic-translation/languages/{languageCode}/target-languages` [EXPERIMENTAL]

Checks if the requested target languages are allowed for automatic translation based on the source language.
If there are no requested target languages, then all allowed target languages for the source language will be returned.

**Server:** `https://gameinternationalization.roblox.com`

**Auth:** 

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `languageCode` | path | `string` | Yes | The source language. |
| `targetLanguages` | query | `string[]` | No | Optional target languages. If not passed in, all allowed target languages for the source language will be returned. |
| `gameId` | query | `integer` | No | Optional gameId. If not passed in, we'll return the default list of languages allowed. |

**Responses:**

- `200`: OK → `Roblox.GameInternationalization.Api.GetAllowedAutomaticTranslationStatusForLanguagesResponse`
- `400`: 73: Maximum languages exceeded. Please keep the number of languages per request below the maximum. 74: A target language cannot be null or whitespace.
- `503`: 17: Feature is disabled

**Response fields** (`Roblox.GameInternationalization.Api.GetAllowedAutomaticTranslationStatusForLanguagesResponse`)

See [Roblox.GameInternationalization.Api.GetAllowedAutomaticTranslationStatusForLanguagesResponse](#roblox-gameinternationalization-api-getallowedautomatictranslationstatusforlanguagesresponse) in Models.

**Response example:**
```json
{
  "sourceLanguage": "string",
  "targetLanguages": [
    {
      "languageCode": "...",
      "isAutomaticTranslationAllowed": "..."
    }
  ]
}
```

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://gameinternationalization.roblox.com/v1/automatic-translation/languages/{LANGUAGECODE}/target-languages"
```

### GET `/v1/country-regions`

Get list of country regions sorted by localized name

**Server:** `https://locale.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `locale` | query | `string` | No |  |

**Responses:**

- `200`: OK → `Roblox.Locale.Api.CountryRegionListResponse`
- `400`: 2: Invalid supported locale code.
- `403`: 7: Feature is disabled

**Response fields** (`Roblox.Locale.Api.CountryRegionListResponse`)

See [Roblox.Locale.Api.CountryRegionListResponse](#roblox-locale-api-countryregionlistresponse) in Models.

**Response example:**
```json
{
  "countryRegionList": [
    {
      "code": "...",
      "name": "...",
      "displayName": "..."
    }
  ]
}
```

**Error handling:** `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://locale.roblox.com/v1/country-regions"
```

### GET `/v1/game-icon/games/{gameId}` [EXPERIMENTAL]

Get all icons for a game

**Server:** `https://gameinternationalization.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gameId` | path | `integer` | Yes | The id of the game |
| `width` | query | `integer` | No | The width of the icon to request |
| `height` | query | `integer` | No | The height of the icon to request |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.GameInternationalization.Api.GetGameIconResponse_`
- `400`: 14: Invalid game id 52: Image dimensions are invalid
- `500`: 0: An unknown error occurred.
- `503`: 17: Feature is disabled

**Response fields** (`Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.GameInternationalization.Api.GetGameIconResponse_`)

See [Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.GameInternationalization.Api.GetGameIconResponse_](#roblox-web-webapi-models-apiarrayresponse-roblox-gameinternationalization-api-getgameiconresponse-) in Models.

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

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://gameinternationalization.roblox.com/v1/game-icon/games/{GAMEID}"
```

### POST `/v1/game-icon/games/{gameId}/language-codes/{languageCode}` [EXPERIMENTAL]

Update a game's icon

**Server:** `https://gameinternationalization.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gameId` | path | `integer` | Yes | The id of the game |
| `languageCode` | path | `string` | Yes | The language code of this icon to update |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: 14: Invalid game id 22: Invalid language code 26: You can't update translations for source language 45: File uploaded does not match known image format 46: File not present in request 53: Language is not supported for the game.
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
  "https://gameinternationalization.roblox.com/v1/game-icon/games/{GAMEID}/language-codes/{LANGUAGECODE}" \
  -H "Content-Type: application/json" \
  -d '{"key": "value"}'
```

### DELETE `/v1/game-icon/games/{gameId}/language-codes/{languageCode}` [EXPERIMENTAL]

Delete a localized icon from a game

**Server:** `https://gameinternationalization.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gameId` | path | `integer` | Yes | The id of the game |
| `languageCode` | path | `string` | Yes | The language code of the localized icon to delete |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: 14: Invalid game id 22: Invalid language code 23: You can't delete translations for source language 53: Language is not supported for the game.
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
  "https://gameinternationalization.roblox.com/v1/game-icon/games/{GAMEID}/language-codes/{LANGUAGECODE}"
```

### PATCH `/v1/game-localization-roles/games/{gameId}`

Assigns or revokes a role

**Server:** `https://translationroles.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gameId` | path | `integer` | Yes | The id of the game |

**Request Body:** `application/json` — Type: `Roblox.TranslationRoles.Api.UpdateRoleRequest`

See [Roblox.TranslationRoles.Api.UpdateRoleRequest](#roblox-translationroles-api-updaterolerequest) in Models.

**Request example:**
```json
{
  "assigneeId": 0,
  "assigneeType": "user",
  "role": "translator",
  "revoke": false
}
```

**Responses:**

- `200`: OK → `TranslationRolesApi.Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: 3: Invalid game id 4: Invalid assignee id 6: Request body can't be null 7: The role you are assigning has reached max limit
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 1: You must be authorized to use this endpoint
- `429`: 5: Too many attempts. Please try again later.
- `503`: 2: Feature is disabled

**Response fields** (`TranslationRolesApi.Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [TranslationRolesApi.Roblox.Web.WebAPI.ApiEmptyResponseModel](#translationrolesapi-roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `429`: Retry with exponential backoff (start at 1s). `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X PATCH -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://translationroles.roblox.com/v1/game-localization-roles/games/{GAMEID}" \
  -H "Content-Type: application/json" \
  -d '{
  "assigneeId": 0,
  "assigneeType": "user",
  "role": "translator",
  "revoke": false
}'
```

### GET `/v1/game-localization-roles/games/{gameId}/current-user/roles`

Retrieves the list of roles granted to current logged-in user

**Server:** `https://translationroles.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gameId` | path | `integer` | Yes | The id of the game |

**Responses:**

- `200`: OK → `TranslationRolesApi.Roblox.Web.WebAPI.Models.ApiArrayResponse_System.String_`
- `400`: 3: Invalid game id
- `401`: 0: Authorization has been denied for this request.
- `503`: 2: Feature is disabled

**Response fields** (`TranslationRolesApi.Roblox.Web.WebAPI.Models.ApiArrayResponse_System.String_`)

See [TranslationRolesApi.Roblox.Web.WebAPI.Models.ApiArrayResponse_System.String_](#translationrolesapi-roblox-web-webapi-models-apiarrayresponse-system-string-) in Models.

**Response example:**
```json
{
  "data": [
    "string"
  ]
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://translationroles.roblox.com/v1/game-localization-roles/games/{GAMEID}/current-user/roles"
```

### GET `/v1/game-localization-roles/games/{gameId}/roles/{role}/assignees`

Gets list of users assigned a specific role in a game.

**Server:** `https://translationroles.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gameId` | path | `integer` | Yes | The id of the game |
| `role` | path | `translator` | Yes | The Roblox.GameLocalization.Client.GameLocalizationRoles.GameLocalizationRoleType Valid values: `translator` |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.TranslationRoles.Api.Assignee_`
- `400`: 3: Invalid game id
- `401`: 0: Authorization has been denied for this request.
- `403`: 1: You must be authorized to use this endpoint
- `503`: 2: Feature is disabled

**Response fields** (`Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.TranslationRoles.Api.Assignee_`)

See [Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.TranslationRoles.Api.Assignee_](#roblox-web-webapi-models-apiarrayresponse-roblox-translationroles-api-assignee-) in Models.

**Response example:**
```json
{
  "data": [
    {
      "id": "...",
      "name": "...",
      "type": "..."
    }
  ]
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://translationroles.roblox.com/v1/game-localization-roles/games/{GAMEID}/roles/{ROLE}/assignees"
```

### GET `/v1/game-localization-roles/roles/{role}/current-user`

Gets the list of games and associated role assignment info for the requested user and role.

**Server:** `https://translationroles.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `role` | path | `translator` | Yes | The Roblox.GameLocalization.Client.GameLocalizationRoles.GameLocalizationRoleType Valid values: `translator` |
| `exclusiveStartKey` | query | `string` | No | Part of pagination. Last primary key of returned items in previous operation. |
| `pageSize` | query | `integer` | No | Part of pagination. Maximum number of items that might be returned in the page. |
| `groupId` | query | `integer` | No | Optional seleted groupId of resources requested for the user and role. |

**Responses:**

- `200`: OK → `Roblox.TranslationRoles.Api.GetGameLocalizationRoleAssignmentsForUserResponse`
- `400`: 10: Invalid page size 11: Maximum page size exceeded 12: Invalid exclusive start key
- `401`: 0: Authorization has been denied for this request.
- `500`: 0: An unknown error occurred
- `503`: 2: Feature is disabled

**Response fields** (`Roblox.TranslationRoles.Api.GetGameLocalizationRoleAssignmentsForUserResponse`)

See [Roblox.TranslationRoles.Api.GetGameLocalizationRoleAssignmentsForUserResponse](#roblox-translationroles-api-getgamelocalizationroleassignmentsforuserresponse) in Models.

**Response example:**
```json
{
  "games": [
    {
      "gameId": "...",
      "assignee": "..."
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
  "https://translationroles.roblox.com/v1/game-localization-roles/roles/{ROLE}/current-user"
```

### GET `/v1/game-localization-status/translation-counts-for-language-or-locale` [EXPERIMENTAL]

Gets the language translation counts for the specified table.
The languages to retrieve must be provided.

**Server:** `https://gameinternationalization.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gameIds` | query | `integer[]` | Yes | List of game ids to retrieve translation counts for. |
| `languageOrLocaleCode` | query | `string` | Yes | The code for the language or locale. |
| `languageOrLocaleType` | query | `Language \| Locale` | Yes | Indicates whether the languageOrLocaleCode represents a language or locale. Valid values: `Language`, `Locale` |

**Responses:**

- `200`: OK → `Roblox.GameInternationalization.Api.GetTranslationCountsForLanguageOrLocaleResponse`
- `400`: 66: Games can't be null or empty 67: Maximum games exceeded. Please keep the number of games per request below the maximum. 68: LanguageOrLocaleCode is null or whitespace
- `401`: 0: Authorization has been denied for this request.

**Response fields** (`Roblox.GameInternationalization.Api.GetTranslationCountsForLanguageOrLocaleResponse`)

See [Roblox.GameInternationalization.Api.GetTranslationCountsForLanguageOrLocaleResponse](#roblox-gameinternationalization-api-gettranslationcountsforlanguageorlocaleresponse) in Models.

**Response example:**
```json
{
  "languageOrLocaleCode": "string",
  "languageOrLocaleType": "Language",
  "games": [
    {
      "gameId": "...",
      "status": "...",
      "categories": "..."
    }
  ]
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://gameinternationalization.roblox.com/v1/game-localization-status/translation-counts-for-language-or-locale?gameIds={VALUE}&languageOrLocaleCode={VALUE}&languageOrLocaleType={VALUE}"
```

### GET `/v1/game-localization-status/{gameId}/translation-counts` [EXPERIMENTAL]

Gets the language translation counts for all languages of a game

**Server:** `https://gameinternationalization.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gameId` | path | `integer` | Yes | GameID of the game to get translation counts for |

**Responses:**

- `200`: OK → `Roblox.GameInternationalization.Api.GetTranslationCountsForGameResponse`
- `400`: 4: Table does not exist. 14: Invalid game id
- `401`: 0: Authorization has been denied for this request.
- `500`: 0: An unknown error occurred.

**Response fields** (`Roblox.GameInternationalization.Api.GetTranslationCountsForGameResponse`)

See [Roblox.GameInternationalization.Api.GetTranslationCountsForGameResponse](#roblox-gameinternationalization-api-gettranslationcountsforgameresponse) in Models.

**Response example:**
```json
{
  "gameId": 0,
  "languagesOrLocales": [
    {
      "status": "...",
      "categories": "...",
      "name": "...",
      "languageCodeType": "...",
      "languageCode": "..."
    }
  ]
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://gameinternationalization.roblox.com/v1/game-localization-status/{GAMEID}/translation-counts"
```

### GET `/v1/game-thumbnails/games/{gameId}/images` [EXPERIMENTAL]

Get the localized image ids in all languages for a game.

**Server:** `https://gameinternationalization.roblox.com`

**Auth:** 

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gameId` | path | `integer` | Yes | The game identifier. |
| `width` | query | `integer` | No | The width. |
| `height` | query | `integer` | No | The height. |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.GameInternationalization.Api.GetGameThumbnailsResponse_`
- `400`: 14: Invalid game id 52: Image dimensions are invalid
- `500`: 0: An unknown error occurred.
- `503`: 17: Feature is disabled

**Response fields** (`Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.GameInternationalization.Api.GetGameThumbnailsResponse_`)

See [Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.GameInternationalization.Api.GetGameThumbnailsResponse_](#roblox-web-webapi-models-apiarrayresponse-roblox-gameinternationalization-api-getgamethumbnailsresponse-) in Models.

**Response example:**
```json
{
  "data": [
    {
      "languageCode": "...",
      "mediaAssets": "..."
    }
  ]
}
```

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://gameinternationalization.roblox.com/v1/game-thumbnails/games/{GAMEID}/images"
```

### POST `/v1/game-thumbnails/games/{gameId}/language-codes/{languageCode}/alt-text` [EXPERIMENTAL]

Updates the game thumbnail alt text.

**Server:** `https://gameinternationalization.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gameId` | path | `integer` | Yes | The game identifier. |
| `languageCode` | path | `string` | Yes | The language code. |

**Request Body:** `application/json` — Type: `Roblox.GameInternationalization.Api.UpdateThumbnailAltTextRequest`

See [Roblox.GameInternationalization.Api.UpdateThumbnailAltTextRequest](#roblox-gameinternationalization-api-updatethumbnailalttextrequest) in Models.

**Request example:**
```json
{
  "thumbnailId": 0,
  "altText": "string"
}
```

**Responses:**

- `200`: OK → `string`
- `400`: 14: Invalid game id 19: New name is null or whitespaces or new name/description is too long 20: New name or description is moderated 22: Invalid language code 26: You can't update translations for source language 45: File uploaded does not match known image format 53: Language is not supported for the game.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 18: You do not have permission to manage this game
- `429`: 24: Too many attempts.Please try again later.
- `500`: 0: An unknown error occurred. 88: Failed to filter text
- `503`: 17: Feature is disabled

**Error handling:** `429`: Retry with exponential backoff (start at 1s). `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://gameinternationalization.roblox.com/v1/game-thumbnails/games/{GAMEID}/language-codes/{LANGUAGECODE}/alt-text" \
  -H "Content-Type: application/json" \
  -d '{
  "thumbnailId": 0,
  "altText": "string"
}'
```

### POST `/v1/game-thumbnails/games/{gameId}/language-codes/{languageCode}/image` [EXPERIMENTAL]

Uploads the game thumbnail.

**Server:** `https://gameinternationalization.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gameId` | path | `integer` | Yes | The game identifier. |
| `languageCode` | path | `string` | Yes | The language code. |

**Responses:**

- `200`: OK → `Roblox.GameInternationalization.Api.Models.Response.UploadImageForGameThumbnailResponse`
- `400`: 14: Invalid game id 22: Invalid language code 26: You can't update translations for source language 53: Language is not supported for the game.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 18: You do not have permission to manage this game
- `429`: 24: Too many attempts.Please try again later.
- `500`: 0: An unknown error occurred.
- `503`: 17: Feature is disabled

**Response fields** (`Roblox.GameInternationalization.Api.Models.Response.UploadImageForGameThumbnailResponse`)

See [Roblox.GameInternationalization.Api.Models.Response.UploadImageForGameThumbnailResponse](#roblox-gameinternationalization-api-models-response-uploadimageforgamethumbnailresponse) in Models.

**Response example:**
```json
{
  "mediaAssetId": "string"
}
```

**Error handling:** `429`: Retry with exponential backoff (start at 1s). `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://gameinternationalization.roblox.com/v1/game-thumbnails/games/{GAMEID}/language-codes/{LANGUAGECODE}/image" \
  -H "Content-Type: application/json" \
  -d '{"key": "value"}'
```

### POST `/v1/game-thumbnails/games/{gameId}/language-codes/{languageCode}/images/order` [EXPERIMENTAL]

Orders the specified image Ids for the game thumbnails.

**Server:** `https://gameinternationalization.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gameId` | path | `integer` | Yes | The game identifier. |
| `languageCode` | path | `string` | Yes | The language code. |

**Request Body:** `application/json` — Type: `Roblox.GameInternationalization.Api.SortImageIdsRequest`

See [Roblox.GameInternationalization.Api.SortImageIdsRequest](#roblox-gameinternationalization-api-sortimageidsrequest) in Models.

**Request example:**
```json
{
  "mediaAssetIds": [
    0
  ]
}
```

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: 14: Invalid game id 22: Invalid language code 26: You can't update translations for source language 53: Language is not supported for the game.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 18: You do not have permission to manage this game
- `503`: 17: Feature is disabled

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://gameinternationalization.roblox.com/v1/game-thumbnails/games/{GAMEID}/language-codes/{LANGUAGECODE}/images/order" \
  -H "Content-Type: application/json" \
  -d '{
  "mediaAssetIds": [
    0
  ]
}'
```

### DELETE `/v1/game-thumbnails/games/{gameId}/language-codes/{languageCode}/images/{imageId}` [EXPERIMENTAL]

Deletes the game thumbnail.

**Server:** `https://gameinternationalization.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gameId` | path | `integer` | Yes | The game identifier. |
| `languageCode` | path | `string` | Yes | The language code. |
| `imageId` | path | `integer` | Yes | The image identifier. |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: 14: Invalid game id 22: Invalid language code 23: You can't delete translations for source language 53: Language is not supported for the game.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 18: You do not have permission to manage this game
- `503`: 17: Feature is disabled

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X DELETE -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://gameinternationalization.roblox.com/v1/game-thumbnails/games/{GAMEID}/language-codes/{LANGUAGECODE}/images/{IMAGEID}"
```

### GET `/v1/locales`

Get list of Supported locales with user locus information.

**Server:** `https://locale.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `displayValueLocale` | query | `string` | No |  |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.Locale.Api.SupportedLocaleLocus_`
- `403`: Feature is turned off temporary
- `500`: Internal server error

**Response fields** (`Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.Locale.Api.SupportedLocaleLocus_`)

See [Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.Locale.Api.SupportedLocaleLocus_](#roblox-web-webapi-models-apiarrayresponse-roblox-locale-api-supportedlocalelocus-) in Models.

**Response example:**
```json
{
  "data": [
    {
      "locale": "...",
      "isEnabledForFullExperience": "...",
      "isEnabledForSignupAndLogin": "...",
      "isEnabledForInGameUgc": "..."
    }
  ]
}
```

**Error handling:** `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://locale.roblox.com/v1/locales"
```

### POST `/v1/locales/set-show-roblox-translations`

Sets whether translations suggested by Roblox will be shown to the user.

**Server:** `https://locale.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Request Body:** `application/json` — Type: `Roblox.Locale.Api.SetShowRobloxTranslationsRequest`

See [Roblox.Locale.Api.SetShowRobloxTranslationsRequest](#roblox-locale-api-setshowrobloxtranslationsrequest) in Models.

**Request example:**
```json
{
  "showRobloxTranslations": false
}
```

**Responses:**

- `200`: OK → `Roblox.Locale.Api.SuccessResponse`
- `400`: Bad Request
- `401`: Unauthorized 0: Authorization has been denied for this request.
- `403`: Feature is turned off temporary 0: Token Validation Failed
- `500`: Internal server error

**Response fields** (`Roblox.Locale.Api.SuccessResponse`)

See [Roblox.Locale.Api.SuccessResponse](#roblox-locale-api-successresponse) in Models.

**Response example:**
```json
{
  "success": false
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://locale.roblox.com/v1/locales/set-show-roblox-translations" \
  -H "Content-Type: application/json" \
  -d '{
  "showRobloxTranslations": false
}'
```

### POST `/v1/locales/set-user-supported-locale`

Sets user's supported locale.
Null supported locale will clear out user's supported locale (set users' supported locale to null)

**Server:** `https://locale.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Request Body:** `application/json` — Type: `Roblox.Locale.Api.SetSupportedLocaleForUserRequest`

See [Roblox.Locale.Api.SetSupportedLocaleForUserRequest](#roblox-locale-api-setsupportedlocaleforuserrequest) in Models.

**Request example:**
```json
{
  "supportedLocaleCode": "string"
}
```

**Responses:**

- `200`: OK → `Roblox.Locale.Api.SuccessResponse`
- `400`: Bad Request
- `401`: Unauthorized 0: Authorization has been denied for this request.
- `403`: Feature is turned off temporary 0: Token Validation Failed
- `500`: Internal server error

**Response fields** (`Roblox.Locale.Api.SuccessResponse`)

See [Roblox.Locale.Api.SuccessResponse](#roblox-locale-api-successresponse) in Models.

**Response example:**
```json
{
  "success": false
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://locale.roblox.com/v1/locales/set-user-supported-locale" \
  -H "Content-Type: application/json" \
  -d '{
  "supportedLocaleCode": "string"
}'
```

### GET `/v1/locales/supported-locales`

Get list of supported locales sorted by the Native Name property.

**Server:** `https://locale.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Responses:**

- `200`: OK → `Roblox.Locale.Api.SupportedLocalesResponse`
- `403`: Feature is turned off temporary
- `500`: Internal server error

**Response fields** (`Roblox.Locale.Api.SupportedLocalesResponse`)

See [Roblox.Locale.Api.SupportedLocalesResponse](#roblox-locale-api-supportedlocalesresponse) in Models.

**Response example:**
```json
{
  "supportedLocales": [
    {
      "id": "...",
      "locale": "...",
      "name": "...",
      "nativeName": "...",
      "language": "..."
    }
  ]
}
```

**Error handling:** `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://locale.roblox.com/v1/locales/supported-locales"
```

### GET `/v1/locales/supported-locales-for-creators`

**Server:** `https://locale.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `displayValueLocale` | query | `string` | No |  |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.Locale.Api.SupportedLocaleLocus_`

**Response fields** (`Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.Locale.Api.SupportedLocaleLocus_`)

See [Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.Locale.Api.SupportedLocaleLocus_](#roblox-web-webapi-models-apiarrayresponse-roblox-locale-api-supportedlocalelocus-) in Models.

**Response example:**
```json
{
  "data": [
    {
      "locale": "...",
      "isEnabledForFullExperience": "...",
      "isEnabledForSignupAndLogin": "...",
      "isEnabledForInGameUgc": "..."
    }
  ]
}
```

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://locale.roblox.com/v1/locales/supported-locales-for-creators"
```

### GET `/v1/locales/supported-locales-for-feature`

Get list of Supported locales for a specific feature.

**Server:** `https://locale.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `featureName` | query | `string` | Yes |  |

**Responses:**

- `200`: OK → `Roblox.Locale.Api.SupportedLocalesResponse`
- `500`: Internal server error

**Response fields** (`Roblox.Locale.Api.SupportedLocalesResponse`)

See [Roblox.Locale.Api.SupportedLocalesResponse](#roblox-locale-api-supportedlocalesresponse) in Models.

**Response example:**
```json
{
  "supportedLocales": [
    {
      "id": "...",
      "locale": "...",
      "name": "...",
      "nativeName": "...",
      "language": "..."
    }
  ]
}
```

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://locale.roblox.com/v1/locales/supported-locales-for-feature?featureName={VALUE}"
```

### GET `/v1/locales/user-locale`

Gets user locale. If user is absent returns, locale from http request object.

**Server:** `https://locale.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Responses:**

- `200`: OK → `Roblox.Locale.Api.UserLocaleResponse`
- `500`: Internal server error

**Response fields** (`Roblox.Locale.Api.UserLocaleResponse`)

See [Roblox.Locale.Api.UserLocaleResponse](#roblox-locale-api-userlocaleresponse) in Models.

**Response example:**
```json
{
  "supportedLocale": {
    "id": 0,
    "locale": "string",
    "name": "string",
    "nativeName": "string",
    "language": {
      "id": "...",
      "name": "...",
      "nativeName": "...",
      "languageCode": "...",
      "isRightToLeft": "..."
    }
  },
  "nativeLanguage": {
    "id": 0,
    "name": "string",
    "nativeName": "string",
    "languageCode": "string",
    "isRightToLeft": false
  }
}
```

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://locale.roblox.com/v1/locales/user-locale"
```

### GET `/v1/locales/user-localization-locus-supported-locales`

Gets each of a user's localization locus supported locales. A localization locus supported locale is a page (or group of pages) that
have been defined by the International team which need independent locale support.
If the user is null we will attempt to return the locales appropriate for the user's device language.

**Server:** `https://locale.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Responses:**

- `200`: OK → `Roblox.Locale.Api.UserLocalizationLocusLocalesResponse`
- `500`: Internal server error

**Response fields** (`Roblox.Locale.Api.UserLocalizationLocusLocalesResponse`)

See [Roblox.Locale.Api.UserLocalizationLocusLocalesResponse](#roblox-locale-api-userlocalizationlocuslocalesresponse) in Models.

**Response example:**
```json
{
  "signupAndLogin": {
    "id": 0,
    "locale": "string",
    "name": "string",
    "nativeName": "string",
    "language": {
      "id": "...",
      "name": "...",
      "nativeName": "...",
      "languageCode": "...",
      "isRightToLeft": "..."
    }
  },
  "generalExperience": {
    "id": 0,
    "locale": "string",
    "name": "string",
    "nativeName": "string",
    "language": {
      "id": "...",
      "name": "...",
      "nativeName": "...",
      "languageCode": "...",
      "isRightToLeft": "..."
    }
  },
  "ugc": {
    "id": 0,
    "locale": "string",
    "name": "string",
    "nativeName": "string",
    "language": {
      "id": "...",
      "name": "...",
      "nativeName": "...",
      "languageCode": "...",
      "isRightToLeft": "..."
    }
  },
  "showRobloxTranslations": false
}
```

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://locale.roblox.com/v1/locales/user-localization-locus-supported-locales"
```

### GET `/v1/localization-table/limits` [EXPERIMENTAL]

Get limits for translation table entries operations

**Server:** `https://localizationtables.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Responses:**

- `200`: OK → `Roblox.LocalizationTables.Api.GetLimitsResponse`
- `401`: 0: Authorization has been denied for this request.

**Response fields** (`Roblox.LocalizationTables.Api.GetLimitsResponse`)

See [Roblox.LocalizationTables.Api.GetLimitsResponse](#roblox-localizationtables-api-getlimitsresponse) in Models.

**Response example:**
```json
{
  "entryOperationLimits": {
    "maxContextLength": 0,
    "maxKeyLength": 0,
    "maxSourceLength": 0,
    "maxExampleLength": 0,
    "maxGameLocationPathLength": 0
  },
  "tableOperationLimits": {
    "maxEntriesPerUpdate": 0
  }
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://localizationtables.roblox.com/v1/localization-table/limits"
```

### GET `/v1/localization-table/metadata` [EXPERIMENTAL]

Get metadata for localization UI

**Server:** `https://localizationtables.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Responses:**

- `200`: OK → `Roblox.LocalizationTables.Api.LocalizationTablesMetadataResponse`

**Response fields** (`Roblox.LocalizationTables.Api.LocalizationTablesMetadataResponse`)

See [Roblox.LocalizationTables.Api.LocalizationTablesMetadataResponse](#roblox-localizationtables-api-localizationtablesmetadataresponse) in Models.

**Response example:**
```json
{
  "isBulkUploadFeatureEnabled": false,
  "isCsvDownloadEnabled": false,
  "isAccessToTranslationMetaDataEnabled": false,
  "isTranslationManagementRedirectionEnabled": false,
  "isUntranslatedFilterEnabled": false,
  "isAutomaticTranslationFilterEnabled": false
}
```

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://localizationtables.roblox.com/v1/localization-table/metadata"
```

### POST `/v1/localization-table/tables` [EXPERIMENTAL]

Creates a Localization Table with the given data.
Note that this endpoint simply creates a table and does not associate it with any universe, so if intending to use this to create tables usable in experience more setup will be needed to grant those experiences access.

**Server:** `https://localizationtables.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Request Body:** `application/json` — Type: `Roblox.LocalizationTables.Api.CreateTableRequest`

See [Roblox.LocalizationTables.Api.CreateTableRequest](#roblox-localizationtables-api-createtablerequest) in Models.

**Request example:**
```json
{
  "name": "string",
  "ownerType": "User",
  "ownerId": 0
}
```

**Responses:**

- `200`: OK → `Roblox.LocalizationTables.Api.CreateTableResponse`
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 2: You do not have permission to get this table.

**Response fields** (`Roblox.LocalizationTables.Api.CreateTableResponse`)

See [Roblox.LocalizationTables.Api.CreateTableResponse](#roblox-localizationtables-api-createtableresponse) in Models.

**Response example:**
```json
{
  "id": "string",
  "assetId": 0
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://localizationtables.roblox.com/v1/localization-table/tables" \
  -H "Content-Type: application/json" \
  -d '{
  "name": "string",
  "ownerType": "User",
  "ownerId": 0
}'
```

### GET `/v1/localization-table/tables/{tableId}` [EXPERIMENTAL]

Get table information by the id of the table.

**Server:** `https://localizationtables.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `tableId` | path | `string` | Yes |  |

**Responses:**

- `200`: OK → `Roblox.LocalizationTables.Api.GetTableResponse`
- `400`: 3: Invalid table id.
- `401`: 0: Authorization has been denied for this request.
- `403`: 2: You do not have permission to get this table.

**Response fields** (`Roblox.LocalizationTables.Api.GetTableResponse`)

See [Roblox.LocalizationTables.Api.GetTableResponse](#roblox-localizationtables-api-gettableresponse) in Models.

**Response example:**
```json
{
  "id": "string",
  "name": "string",
  "ownerType": "User",
  "ownerId": 0,
  "assetId": 0
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://localizationtables.roblox.com/v1/localization-table/tables/{TABLEID}"
```

### PATCH `/v1/localization-table/tables/{tableId}` [EXPERIMENTAL]

Updates the tables contents based on what is provided.

**Server:** `https://localizationtables.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `tableId` | path | `string` | Yes | The table guid for the table to update. |
| `gameId` | query | `integer` | No | The game id. |

**Request Body:** `application/json` — Type: `Roblox.LocalizationTables.Api.UpdateTableContentsRequest`

See [Roblox.LocalizationTables.Api.UpdateTableContentsRequest](#roblox-localizationtables-api-updatetablecontentsrequest) in Models.

**Request example:**
```json
{
  "name": "string",
  "entries": [
    {
      "identifier": "...",
      "metadata": "...",
      "translations": "...",
      "delete": "..."
    }
  ]
}
```

**Responses:**

- `200`: OK → `Roblox.LocalizationTables.Api.UpdateTableContentsResponse`
- `400`: 3: Invalid table id. 4: Table does not exist. 10: Maximum entries exceeded. Please keep the number of entries per request below the maximum. 13: Request body can't be null 14: Invalid game id
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 6: You do not have permission to create this table.
- `503`: 17: Feature is disabled

**Response fields** (`Roblox.LocalizationTables.Api.UpdateTableContentsResponse`)

See [Roblox.LocalizationTables.Api.UpdateTableContentsResponse](#roblox-localizationtables-api-updatetablecontentsresponse) in Models.

**Response example:**
```json
{
  "failedEntriesAndTranslations": [
    {
      "error": "...",
      "identifier": "...",
      "metadata": "...",
      "translations": "...",
      "createdTime": "..."
    }
  ],
  "modifiedEntriesAndTranslations": [
    {
      "identifier": "...",
      "translations": "..."
    }
  ]
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X PATCH -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://localizationtables.roblox.com/v1/localization-table/tables/{TABLEID}" \
  -H "Content-Type: application/json" \
  -d '{
  "name": "string",
  "entries": [
    {
      "identifier": "...",
      "metadata": "...",
      "translations": "...",
      "delete": "..."
    }
  ]
}'
```

### GET `/v1/localization-table/tables/{tableId}/asset-entries` [EXPERIMENTAL]

Gets a page of asset (image) entries for the specified table, along with the table's
per-locale asset translations.

**Server:** `https://localizationtables.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `tableId` | path | `string` | Yes | The table id. |
| `cursor` | query | `string` | No | The source asset id to start after. If null, starts from the first page. A null cursor in the response means there are no more entries. |
| `gameId` | query | `integer` | No | The universe id that owns the table. |

**Responses:**

- `200`: OK → `Roblox.LocalizationTables.Api.GetTableAssetEntriesPagedResponse`
- `400`: 3: Invalid table id. 14: Invalid game id 25: Invalid cursor
- `401`: 0: Authorization has been denied for this request.
- `403`: 2: You do not have permission to get this table.

**Response fields** (`Roblox.LocalizationTables.Api.GetTableAssetEntriesPagedResponse`)

See [Roblox.LocalizationTables.Api.GetTableAssetEntriesPagedResponse](#roblox-localizationtables-api-gettableassetentriespagedresponse) in Models.

**Response example:**
```json
{
  "previousPageCursor": "string",
  "nextPageCursor": "string",
  "data": [
    {
      "sourceAssetId": "...",
      "assetType": "...",
      "assetClass": "...",
      "assetProp": "...",
      "translations": "...",
      "creator": "..."
    }
  ]
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://localizationtables.roblox.com/v1/localization-table/tables/{TABLEID}/asset-entries"
```

### GET `/v1/localization-table/tables/{tableId}/entries` [EXPERIMENTAL]

Gets a batch of entries for a table.

**Server:** `https://localizationtables.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `tableId` | path | `string` | Yes |  |
| `cursor` | query | `string` | No | If null, there are no more entries in the table and you've reached the last page. |
| `gameId` | query | `integer` | No |  |
| `entryFormat` | query | `Invalid \| Legacy \| Icu` | No | Valid values: `Invalid`, `Legacy`, `Icu` |

**Responses:**

- `200`: OK → `Roblox.LocalizationTables.Api.GetTableEntriesPagedResponse`
- `400`: 3: Invalid table id. 14: Invalid game id
- `401`: 0: Authorization has been denied for this request.
- `403`: 2: You do not have permission to get this table.

**Response fields** (`Roblox.LocalizationTables.Api.GetTableEntriesPagedResponse`)

See [Roblox.LocalizationTables.Api.GetTableEntriesPagedResponse](#roblox-localizationtables-api-gettableentriespagedresponse) in Models.

**Response example:**
```json
{
  "previousPageCursor": "string",
  "nextPageCursor": "string",
  "data": [
    {
      "identifier": "...",
      "metadata": "...",
      "translations": "...",
      "createdTime": "..."
    }
  ]
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://localizationtables.roblox.com/v1/localization-table/tables/{TABLEID}/entries"
```

### POST `/v1/localization-table/tables/{tableId}/entries/translation-feedback` [EXPERIMENTAL]

Gets the translation feedback for each entry passed in.

**Server:** `https://localizationtables.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `tableId` | path | `string` | Yes | The entries' tableId. |
| `gameId` | query | `integer` | No | The game id. |

**Request Body:** `application/json` — Type: `Roblox.LocalizationTables.Api.GetTableEntriesTranslationFeedbackRequest`

See [Roblox.LocalizationTables.Api.GetTableEntriesTranslationFeedbackRequest](#roblox-localizationtables-api-gettableentriestranslationfeedbackrequest) in Models.

**Request example:**
```json
{
  "sourceLocale": "string",
  "entries": [
    {
      "translation": "...",
      "key": "...",
      "context": "...",
      "source": "...",
      "entryFormat": "..."
    }
  ]
}
```

**Responses:**

- `200`: OK → `Roblox.LocalizationTables.Api.GetTableEntriesTranslationFeedbackResponse`
- `400`: 3: Invalid table id. 13: Request body can't be null 14: Invalid game id 16: Entries can't be null or empty 35: The entries provided are invalid 37: Invalid locale code. 38: Invalid entry identifier.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 2: You do not have permission to get this table.
- `429`: 24: Too many attempts.Please try again later.
- `503`: 17: Feature is disabled

**Response fields** (`Roblox.LocalizationTables.Api.GetTableEntriesTranslationFeedbackResponse`)

See [Roblox.LocalizationTables.Api.GetTableEntriesTranslationFeedbackResponse](#roblox-localizationtables-api-gettableentriestranslationfeedbackresponse) in Models.

**Response example:**
```json
{
  "tableId": "string",
  "entries": [
    {
      "identifier": "...",
      "feedbackCount": "...",
      "playerSuggestionText": "...",
      "reasons": "...",
      "robloxSuggestionText": "..."
    }
  ]
}
```

**Error handling:** `429`: Retry with exponential backoff (start at 1s). `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://localizationtables.roblox.com/v1/localization-table/tables/{TABLEID}/entries/translation-feedback" \
  -H "Content-Type: application/json" \
  -d '{
  "sourceLocale": "string",
  "entries": [
    {
      "translation": "...",
      "key": "...",
      "context": "...",
      "source": "...",
      "entryFormat": "..."
    }
  ]
}'
```

### POST `/v1/localization-table/tables/{tableId}/entries/translation-history` [EXPERIMENTAL]

Gets the translation history for each entry passed in.

**Server:** `https://localizationtables.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `tableId` | path | `string` | Yes | The entries' tableId. |
| `gameId` | query | `integer` | No | The game id. |

**Request Body:** `application/json` — Type: `Roblox.LocalizationTables.Api.GetTableEntriesTranslationHistoryRequest`

See [Roblox.LocalizationTables.Api.GetTableEntriesTranslationHistoryRequest](#roblox-localizationtables-api-gettableentriestranslationhistoryrequest) in Models.

**Request example:**
```json
{
  "locale": "string",
  "entries": [
    {
      "cursor": "...",
      "identifier": "...",
      "count": "...",
      "sortOrder": "..."
    }
  ],
  "sourceType": "Invalid"
}
```

**Responses:**

- `200`: OK → `Roblox.LocalizationTables.Api.GetTableEntriesTranslationHistoryResponse`
- `400`: 3: Invalid table id. 13: Request body can't be null 14: Invalid game id 16: Entries can't be null or empty 35: The entries provided are invalid 37: Invalid locale code. 38: Invalid entry identifier. 39: Count should be at least 1. 45: Invalid exclusive start id.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 2: You do not have permission to get this table.
- `429`: 24: Too many attempts.Please try again later.
- `503`: 17: Feature is disabled

**Response fields** (`Roblox.LocalizationTables.Api.GetTableEntriesTranslationHistoryResponse`)

See [Roblox.LocalizationTables.Api.GetTableEntriesTranslationHistoryResponse](#roblox-localizationtables-api-gettableentriestranslationhistoryresponse) in Models.

**Response example:**
```json
{
  "tableId": "string",
  "locale": "string",
  "entries": [
    {
      "identifier": "...",
      "history": "...",
      "nextCursor": "..."
    }
  ],
  "failedEntries": [
    {
      "identifier": "...",
      "count": "...",
      "error": "..."
    }
  ]
}
```

**Error handling:** `429`: Retry with exponential backoff (start at 1s). `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://localizationtables.roblox.com/v1/localization-table/tables/{TABLEID}/entries/translation-history" \
  -H "Content-Type: application/json" \
  -d '{
  "locale": "string",
  "entries": [
    {
      "cursor": "...",
      "identifier": "...",
      "count": "...",
      "sortOrder": "..."
    }
  ],
  "sourceType": "Invalid"
}'
```

### GET `/v1/localization-table/tables/{tableId}/entry-count` [EXPERIMENTAL]

Gets the number of entries in the specified table

**Server:** `https://localizationtables.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `tableId` | path | `string` | Yes | The table id |
| `gameId` | query | `integer` | No | The game id |
| `entryFormat` | query | `Invalid \| Legacy \| Icu` | No | Valid values: `Invalid`, `Legacy`, `Icu` |

**Responses:**

- `200`: OK → `Roblox.LocalizationTables.Api.GetTableEntryCountResponse`
- `400`: 3: Invalid table id. 14: Invalid game id
- `401`: 0: Authorization has been denied for this request.
- `403`: 2: You do not have permission to get this table.

**Response fields** (`Roblox.LocalizationTables.Api.GetTableEntryCountResponse`)

See [Roblox.LocalizationTables.Api.GetTableEntryCountResponse](#roblox-localizationtables-api-gettableentrycountresponse) in Models.

**Response example:**
```json
{
  "id": "string",
  "entryCount": 0
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://localizationtables.roblox.com/v1/localization-table/tables/{TABLEID}/entry-count"
```

### PATCH `/v1/localizationtable/gametables/{gameId}`

**Server:** `https://gameinternationalization.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gameId` | path | `integer` | Yes |  |

**Request Body:** `application/json` — Type: `Roblox.GameInternationalization.Api.AssociateLocalizationTablesToGameRequest`

See [Roblox.GameInternationalization.Api.AssociateLocalizationTablesToGameRequest](#roblox-gameinternationalization-api-associatelocalizationtablestogamerequest) in Models.

**Request example:**
```json
{
  "tables": [
    {
      "id": "...",
      "dissociate": "..."
    }
  ]
}
```

**Responses:**

- `200`: OK → `Roblox.GameInternationalization.Api.AssociateLocalizationTablesToGameResponse`
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed

**Response fields** (`Roblox.GameInternationalization.Api.AssociateLocalizationTablesToGameResponse`)

See [Roblox.GameInternationalization.Api.AssociateLocalizationTablesToGameResponse](#roblox-gameinternationalization-api-associatelocalizationtablestogameresponse) in Models.

**Response example:**
```json
{
  "success": false
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X PATCH -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://gameinternationalization.roblox.com/v1/localizationtable/gametables/{GAMEID}" \
  -H "Content-Type: application/json" \
  -d '{
  "tables": [
    {
      "id": "...",
      "dissociate": "..."
    }
  ]
}'
```

### POST `/v1/name-description/games/translation-history` [EXPERIMENTAL]

Gets the history for name or description in a provided language.

**Server:** `https://gameinternationalization.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Request Body:** `application/json` — Type: `Roblox.GameInternationalization.Api.GetNameDescriptionHistoryV2Request`

See [Roblox.GameInternationalization.Api.GetNameDescriptionHistoryV2Request](#roblox-gameinternationalization-api-getnamedescriptionhistoryv2request) in Models.

**Request example:**
```json
{
  "contentId": 0,
  "contentType": "UniverseDisplayNames",
  "languageCode": "string",
  "cursor": "string",
  "count": 0,
  "sortOrder": "Asc"
}
```

**Responses:**

- `200`: OK → `Roblox.GameInternationalization.Api.GetNameDescriptionHistoryResponse`
- `400`: 13: Request body can't be null 14: Invalid game id 18: You do not have permission to manage this game 22: Invalid language code 39: Count should be at least 1 and less than 50. 53: Language is not supported for the game. 54: No history available for source data 55: Invalid exclusive start Id
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed
- `500`: 0: An unknown error occurred.
- `503`: 17: Feature is disabled

**Response fields** (`Roblox.GameInternationalization.Api.GetNameDescriptionHistoryResponse`)

See [Roblox.GameInternationalization.Api.GetNameDescriptionHistoryResponse](#roblox-gameinternationalization-api-getnamedescriptionhistoryresponse) in Models.

**Response example:**
```json
{
  "history": [
    {
      "translationText": "...",
      "translator": "...",
      "created": "..."
    }
  ],
  "lastEvaluatedId": "string"
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://gameinternationalization.roblox.com/v1/name-description/games/translation-history" \
  -H "Content-Type: application/json" \
  -d '{
  "contentId": 0,
  "contentType": "UniverseDisplayNames",
  "languageCode": "string",
  "cursor": "string",
  "count": 0,
  "sortOrder": "Asc"
}'
```

### GET `/v1/name-description/games/{gameId}` [EXPERIMENTAL]

Gets a game's name and description in all supported languages

**Server:** `https://gameinternationalization.roblox.com`

**Auth:** 

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gameId` | path | `integer` | Yes | The id of the game |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.GameInternationalization.Api.NameDescription_`
- `400`: 14: Invalid game id
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

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://gameinternationalization.roblox.com/v1/name-description/games/{GAMEID}"
```

### PATCH `/v1/name-description/games/{gameId}` [EXPERIMENTAL]

Updates a game's name and/or description in multiple languages.

**Server:** `https://gameinternationalization.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gameId` | path | `integer` | Yes | The id of the game. |

**Request Body:** `application/json` — Type: `Roblox.GameInternationalization.Api.UpdateNameDescriptionsRequest`

See [Roblox.GameInternationalization.Api.UpdateNameDescriptionsRequest](#roblox-gameinternationalization-api-updatenamedescriptionsrequest) in Models.

**Request example:**
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

**Responses:**

- `200`: OK → `Roblox.GameInternationalization.Api.UpdateNameDescriptionsResponse`
- `400`: 14: Invalid game id 19: New name is null or whitespaces or new name/description is too long 20: New name or description is moderated 22: Invalid language code 23: You can't delete translations for source language 26: You can't update translations for source language 53: Language is not supported for the game.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 18: You do not have permission to manage this game
- `503`: 17: Feature is disabled

**Response fields** (`Roblox.GameInternationalization.Api.UpdateNameDescriptionsResponse`)

See [Roblox.GameInternationalization.Api.UpdateNameDescriptionsResponse](#roblox-gameinternationalization-api-updatenamedescriptionsresponse) in Models.

**Response example:**
```json
{
  "successOperations": [
    {
      "name": "...",
      "description": "...",
      "updateType": "...",
      "languageCode": "..."
    }
  ],
  "failedOperations": [
    {
      "languageCode": "...",
      "errorCode": "..."
    }
  ]
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X PATCH -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://gameinternationalization.roblox.com/v1/name-description/games/{GAMEID}" \
  -H "Content-Type: application/json" \
  -d '{
  "data": [
    {
      "name": "...",
      "description": "...",
      "updateType": "...",
      "languageCode": "..."
    }
  ]
}'
```

### GET `/v1/name-description/metadata` [EXPERIMENTAL]

Rollout settings for name/description migration to new page

**Server:** `https://gameinternationalization.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Responses:**

- `200`: OK → `Roblox.GameInternationalization.Api.Models.Response.GameNameDescriptionMetadataResponse`
- `401`: 0: Authorization has been denied for this request.

**Response fields** (`Roblox.GameInternationalization.Api.Models.Response.GameNameDescriptionMetadataResponse`)

See [Roblox.GameInternationalization.Api.Models.Response.GameNameDescriptionMetadataResponse](#roblox-gameinternationalization-api-models-response-gamenamedescriptionmetadataresponse) in Models.

**Response example:**
```json
{
  "isNameDescriptionMigrationEnabled": false
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://gameinternationalization.roblox.com/v1/name-description/metadata"
```

### GET `/v1/source-language/games/{gameId}` [EXPERIMENTAL]

Gets the source language of a game

**Server:** `https://gameinternationalization.roblox.com`

**Auth:** 

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gameId` | path | `integer` | Yes |  |

**Responses:**

- `200`: OK → `Roblox.GameInternationalization.Api.Language`
- `400`: 14: Invalid game id
- `503`: 17: Feature is disabled

**Response fields** (`Roblox.GameInternationalization.Api.Language`)

See [Roblox.GameInternationalization.Api.Language](#roblox-gameinternationalization-api-language) in Models.

**Response example:**
```json
{
  "name": "string",
  "nativeName": "string",
  "languageCode": "string"
}
```

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://gameinternationalization.roblox.com/v1/source-language/games/{GAMEID}"
```

### PATCH `/v1/source-language/games/{gameId}` [EXPERIMENTAL]

Sets the source language of a game

**Server:** `https://gameinternationalization.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gameId` | path | `integer` | Yes |  |
| `languageCode` | query | `string` | Yes |  |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: 14: Invalid game id 22: Invalid language code
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 18: You do not have permission to manage this game
- `500`: 85: Failed to disable automatic translation status for languages
- `503`: 17: Feature is disabled

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X PATCH -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://gameinternationalization.roblox.com/v1/source-language/games/{GAMEID}?languageCode={VALUE}"
```

### GET `/v1/source-language/games/{gameId}/language-with-locales` [EXPERIMENTAL]

Gets the source language of a game

**Server:** `https://gameinternationalization.roblox.com`

**Auth:** 

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gameId` | path | `integer` | Yes |  |

**Responses:**

- `200`: OK → `Roblox.GameInternationalization.Api.SourceLanguageWithLocales`
- `400`: 14: Invalid game id
- `503`: 17: Feature is disabled

**Response fields** (`Roblox.GameInternationalization.Api.SourceLanguageWithLocales`)

See [Roblox.GameInternationalization.Api.SourceLanguageWithLocales](#roblox-gameinternationalization-api-sourcelanguagewithlocales) in Models.

**Response example:**
```json
{
  "languageFamily": {
    "name": "string",
    "nativeName": "string",
    "languageCode": "string"
  },
  "defaultLocale": {
    "id": 0,
    "locale": "en_us",
    "localeCode": "string",
    "name": "string",
    "nativeName": "string",
    "language": {
      "id": "...",
      "name": "...",
      "nativeName": "...",
      "languageCode": "...",
      "isRightToLeft": "..."
    }
  },
  "childLocales": [
    {
      "id": "...",
      "locale": "...",
      "localeCode": "...",
      "name": "...",
      "nativeName": "...",
      "language": "..."
    }
  ]
}
```

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://gameinternationalization.roblox.com/v1/source-language/games/{GAMEID}/language-with-locales"
```

### GET `/v1/supported-languages/games/{gameId}` [EXPERIMENTAL]

Get the supported languages for a game.

**Server:** `https://gameinternationalization.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gameId` | path | `integer` | Yes | The id of the game. |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.GameInternationalization.Api.LanguageOrLocale_`
- `400`: 14: Invalid game id
- `503`: 17: Feature is disabled

**Response fields** (`Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.GameInternationalization.Api.LanguageOrLocale_`)

See [Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.GameInternationalization.Api.LanguageOrLocale_](#roblox-web-webapi-models-apiarrayresponse-roblox-gameinternationalization-api-languageorlocale-) in Models.

**Response example:**
```json
{
  "data": [
    {
      "name": "...",
      "languageCodeType": "...",
      "languageCode": "..."
    }
  ]
}
```

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://gameinternationalization.roblox.com/v1/supported-languages/games/{GAMEID}"
```

### PATCH `/v1/supported-languages/games/{gameId}` [EXPERIMENTAL]

Add or remove supported languages for a game.

**Server:** `https://gameinternationalization.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gameId` | path | `integer` | Yes | The id of the game. |

**Request Body:** `application/json` — Type: `Roblox.GameInternationalization.Api.PatchLanguage[]`

See [Roblox.GameInternationalization.Api.PatchLanguage](#roblox-gameinternationalization-api-patchlanguage) in Models.

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: 14: Invalid game id 22: Invalid language code 49: Duplicate language codes are not allowed.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 18: You do not have permission to manage this game
- `503`: 17: Feature is disabled

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X PATCH -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://gameinternationalization.roblox.com/v1/supported-languages/games/{GAMEID}" \
  -H "Content-Type: application/json" \
  -d '[
  {
    "languageCodeType": "Language",
    "languageCode": "string",
    "delete": false
  }
]'
```

### GET `/v1/supported-languages/games/{gameId}/automatic-translation-status` [EXPERIMENTAL]

Get the automatic translation status of supported languages for a game.

**Server:** `https://gameinternationalization.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gameId` | path | `integer` | Yes | The id of the game. |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.GameInternationalization.Api.LanguageOrLocaleSettings_`
- `400`: 14: Invalid game id
- `401`: 0: Authorization has been denied for this request.
- `403`: 18: You do not have permission to manage this game
- `503`: 17: Feature is disabled

**Response fields** (`Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.GameInternationalization.Api.LanguageOrLocaleSettings_`)

See [Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.GameInternationalization.Api.LanguageOrLocaleSettings_](#roblox-web-webapi-models-apiarrayresponse-roblox-gameinternationalization-api-languageorlocalesettings-) in Models.

**Response example:**
```json
{
  "data": [
    {
      "languageCodeType": "...",
      "languageCode": "...",
      "isAutomaticTranslationEnabled": "...",
      "isImageTranslationEnabled": "..."
    }
  ]
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://gameinternationalization.roblox.com/v1/supported-languages/games/{GAMEID}/automatic-translation-status"
```

### GET `/v1/supported-languages/games/{gameId}/in-experience-language-selection` [EXPERIMENTAL]

Get the user's in-experience language selector languages for a game.

**Server:** `https://gameinternationalization.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gameId` | path | `integer` | Yes | The id of the game. |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.GameInternationalization.Api.LanguageOrLocale_`
- `400`: 14: Invalid game id
- `503`: 17: Feature is disabled

**Response fields** (`Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.GameInternationalization.Api.LanguageOrLocale_`)

See [Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.GameInternationalization.Api.LanguageOrLocale_](#roblox-web-webapi-models-apiarrayresponse-roblox-gameinternationalization-api-languageorlocale-) in Models.

**Response example:**
```json
{
  "data": [
    {
      "name": "...",
      "languageCodeType": "...",
      "languageCode": "..."
    }
  ]
}
```

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://gameinternationalization.roblox.com/v1/supported-languages/games/{GAMEID}/in-experience-language-selection"
```

### PATCH `/v1/supported-languages/games/{gameId}/languages/{languageCode}/automatic-translation-status` [EXPERIMENTAL]

Enable or disable automatic translation for a game and language.

**Server:** `https://gameinternationalization.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gameId` | path | `integer` | Yes | The id of the game. |
| `languageCode` | path | `string` | Yes | The language to enable or disable for automatic translation. |

**Request Body:** `application/json` — Type: `boolean`

**Responses:**

- `200`: OK → `Roblox.GameInternationalization.Api.EditAutomaticTranslationStatusForGameAndLanguageResponse`
- `400`: 14: Invalid game id 22: Invalid language code 53: Language is not supported for the game. 72: Automatic translation cannot be enabled for game. 75: Automatic translation cannot be enabled for language.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 18: You do not have permission to manage this game
- `503`: 17: Feature is disabled

**Response fields** (`Roblox.GameInternationalization.Api.EditAutomaticTranslationStatusForGameAndLanguageResponse`)

See [Roblox.GameInternationalization.Api.EditAutomaticTranslationStatusForGameAndLanguageResponse](#roblox-gameinternationalization-api-editautomatictranslationstatusforgameandlanguageresponse) in Models.

**Response example:**
```json
{
  "gameId": 0,
  "languageCode": "string",
  "isAutomaticTranslationEnabled": false
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X PATCH -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://gameinternationalization.roblox.com/v1/supported-languages/games/{GAMEID}/languages/{LANGUAGECODE}/automatic-translation-status" \
  -H "Content-Type: application/json" \
  -d 'false'
```

### PATCH `/v1/supported-languages/games/{gameId}/languages/{languageCode}/image-translation-status` [EXPERIMENTAL]

Enable or disable image translation for a game and language.

**Server:** `https://gameinternationalization.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gameId` | path | `integer` | Yes | The id of the game. |
| `languageCode` | path | `string` | Yes | The language to enable or disable for image translation. |

**Request Body:** `application/json` — Type: `boolean`

**Responses:**

- `200`: OK → `Roblox.GameInternationalization.Api.EditImageTranslationStatusForGameAndLanguageResponse`
- `400`: 14: Invalid game id 22: Invalid language code 53: Language is not supported for the game. 93: Image translation cannot be enabled for language.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 18: You do not have permission to manage this game
- `503`: 17: Feature is disabled

**Response fields** (`Roblox.GameInternationalization.Api.EditImageTranslationStatusForGameAndLanguageResponse`)

See [Roblox.GameInternationalization.Api.EditImageTranslationStatusForGameAndLanguageResponse](#roblox-gameinternationalization-api-editimagetranslationstatusforgameandlanguageresponse) in Models.

**Response example:**
```json
{
  "gameId": 0,
  "languageCode": "string",
  "isImageTranslationEnabled": false
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X PATCH -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://gameinternationalization.roblox.com/v1/supported-languages/games/{GAMEID}/languages/{LANGUAGECODE}/image-translation-status" \
  -H "Content-Type: application/json" \
  -d 'false'
```

### PATCH `/v1/supported-languages/games/{gameId}/languages/{languageCode}/universe-display-info-automatic-translation-settings` [EXPERIMENTAL]

Update the switch which controls if the UniverseDisplayInformation should be automatically translated.

**Server:** `https://gameinternationalization.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gameId` | path | `integer` | Yes | The game id. |
| `languageCode` | path | `string` | Yes | The language code. |

**Request Body:** `application/json` — Type: `boolean`

**Responses:**

- `200`: OK → `Roblox.GameInternationalization.Api.UpdateUniverseDisplayInfoAutomaticTranslationSettingsResponse`
- `400`: 14: Invalid game id 72: Automatic translation cannot be enabled for game.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 18: You do not have permission to manage this game
- `500`: 77: Content localization set settings return error code invalid 79: Invalid content instance settings 80: Invalid quota settings 81: Invalid change agent 82: Failed to update UniverseDisplayInformation content instance auto translation settings

**Response fields** (`Roblox.GameInternationalization.Api.UpdateUniverseDisplayInfoAutomaticTranslationSettingsResponse`)

See [Roblox.GameInternationalization.Api.UpdateUniverseDisplayInfoAutomaticTranslationSettingsResponse](#roblox-gameinternationalization-api-updateuniversedisplayinfoautomatictranslationsettingsresponse) in Models.

**Response example:**
```json
{
  "gameId": 0,
  "languageCode": "string",
  "isUniverseDisplayInfoAutomaticTranslationEnabled": false
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X PATCH -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://gameinternationalization.roblox.com/v1/supported-languages/games/{GAMEID}/languages/{LANGUAGECODE}/universe-display-info-automatic-translation-settings" \
  -H "Content-Type: application/json" \
  -d 'false'
```

### GET `/v1/supported-languages/games/{gameId}/universe-display-info-automatic-translation-settings` [EXPERIMENTAL]

Get UniverseDisplayInfo automatic translation settings.

**Server:** `https://gameinternationalization.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gameId` | path | `integer` | Yes | The game id. |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.GameInternationalization.Api.UniverseDisplayInfoAutomaticTranslationSettings_`
- `400`: 14: Invalid game id
- `401`: 0: Authorization has been denied for this request.
- `403`: 18: You do not have permission to manage this game
- `500`: 0: An unknown error occurred. 22: Invalid language code 83: Failed to get UniverseDisplayInformation content instance auto translation settings 84: Count of language code is larger than max batch get size

**Response fields** (`Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.GameInternationalization.Api.UniverseDisplayInfoAutomaticTranslationSettings_`)

See [Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.GameInternationalization.Api.UniverseDisplayInfoAutomaticTranslationSettings_](#roblox-web-webapi-models-apiarrayresponse-roblox-gameinternationalization-api-universedisplayinfoautomatictranslationsettings-) in Models.

**Response example:**
```json
{
  "data": [
    {
      "languageCode": "...",
      "isUniverseDisplayInfoAutomaticTranslationEnabled": "..."
    }
  ]
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://gameinternationalization.roblox.com/v1/supported-languages/games/{GAMEID}/universe-display-info-automatic-translation-settings"
```

### GET `/v1/supported-languages/metadata` [EXPERIMENTAL]

Rollout settings for supported languages of a game

**Server:** `https://gameinternationalization.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Responses:**

- `200`: OK → `Roblox.GameInternationalization.Api.SupportedLanguagesMetadataResponse`
- `401`: 0: Authorization has been denied for this request.

**Response fields** (`Roblox.GameInternationalization.Api.SupportedLanguagesMetadataResponse`)

See [Roblox.GameInternationalization.Api.SupportedLanguagesMetadataResponse](#roblox-gameinternationalization-api-supportedlanguagesmetadataresponse) in Models.

**Response example:**
```json
{
  "isFeatureEnabled": false,
  "areAllLanguagesEnabled": false,
  "minimumUniverseIdForFeature": 0,
  "isHumanTranslationProgressUIEnabled": false,
  "isAutomaticTranslationProgressUIEnabled": false,
  "isSupportedLanguagesChildLocalesUIEnabled": false
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://gameinternationalization.roblox.com/v1/supported-languages/metadata"
```

### GET `/v1/translation-analytics/games/{gameId}/download-translation-analytics-report` [EXPERIMENTAL]

Download translation analytics report after the report is ready

**Server:** `https://gameinternationalization.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gameId` | path | `integer` | Yes | The game's id |
| `startDateTime` | query | `string` | Yes | The inclusive start dateTime of report in UTC |
| `endDateTime` | query | `string` | Yes | The exclusive end dateTime of report in UTC |
| `reportType` | query | `GameTranslationStatus \| GameTranslationStatusForTranslator \| GameTranslationStatusForTranslatorGroup \| Test` | Yes | The report type Valid values: `GameTranslationStatus`, `GameTranslationStatusForTranslator`, `GameTranslationStatusForTranslatorGroup`, `Test` |
| `reportSubjectTargetId` | query | `integer` | Yes | The translator group id |

**Responses:**

- `200`: OK → `object`
- `400`: 14: Invalid game id 56: You need to provide a valid translator group id to get report. 58: Start datetime or end datetime is invlaid. 59: Report type is invalid
- `401`: 0: Authorization has been denied for this request.
- `403`: 57: You do not have permission to request translation analytics report.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://gameinternationalization.roblox.com/v1/translation-analytics/games/{GAMEID}/download-translation-analytics-report?startDateTime={VALUE}&endDateTime={VALUE}&reportType={VALUE}&reportSubjectTargetId={VALUE}"
```

### POST `/v1/translation-analytics/games/{gameId}/request-translation-analytics-report` [EXPERIMENTAL]

Request translation analytics report to be generated

**Server:** `https://gameinternationalization.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gameId` | path | `integer` | Yes | The game's id |

**Request Body:** `application/json` — Type: `Roblox.GameInternationalization.Api.RequestTranslationAnalyticsReportRequest`

See [Roblox.GameInternationalization.Api.RequestTranslationAnalyticsReportRequest](#roblox-gameinternationalization-api-requesttranslationanalyticsreportrequest) in Models.

**Request example:**
```json
{
  "startDateTime": "2024-01-01T00:00:00Z",
  "endDateTime": "2024-01-01T00:00:00Z",
  "reportType": "GameTranslationStatus",
  "reportSubjectTargetId": 0
}
```

**Responses:**

- `200`: OK → `Roblox.GameInternationalization.Api.RequestTranslationAnalyticsReportResponse`
- `400`: 14: Invalid game id 56: You need to provide a valid translator group id to get report. 58: Start datetime or end datetime is invlaid. 59: Report type is invalid
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 57: You do not have permission to request translation analytics report.

**Response fields** (`Roblox.GameInternationalization.Api.RequestTranslationAnalyticsReportResponse`)

See [Roblox.GameInternationalization.Api.RequestTranslationAnalyticsReportResponse](#roblox-gameinternationalization-api-requesttranslationanalyticsreportresponse) in Models.

**Response example:**
```json
{
  "reportGenerationStatus": "inProgress"
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://gameinternationalization.roblox.com/v1/translation-analytics/games/{GAMEID}/request-translation-analytics-report" \
  -H "Content-Type: application/json" \
  -d '{
  "startDateTime": "2024-01-01T00:00:00Z",
  "endDateTime": "2024-01-01T00:00:00Z",
  "reportType": "GameTranslationStatus",
  "reportSubjectTargetId": 0
}'
```

### GET `/v1/translation-analytics/metadata` [EXPERIMENTAL]

Get metadata related to UI and rollout settings

**Server:** `https://gameinternationalization.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Responses:**

- `200`: OK → `Roblox.GameInternationalization.Api.TranslationAnalyticsMetadataResponse`
- `401`: 0: Authorization has been denied for this request.

**Response fields** (`Roblox.GameInternationalization.Api.TranslationAnalyticsMetadataResponse`)

See [Roblox.GameInternationalization.Api.TranslationAnalyticsMetadataResponse](#roblox-gameinternationalization-api-translationanalyticsmetadataresponse) in Models.

**Response example:**
```json
{
  "isFeatureEnabledOnUI": false,
  "reportRequestPollingIntervalSeconds": 0,
  "minimumDateTimeForAnalyticsReport": "2024-01-01T00:00:00Z"
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://gameinternationalization.roblox.com/v1/translation-analytics/metadata"
```

### GET `/v1/ui-configurations` [EXPERIMENTAL]

Get ui configurations for frontend to use.

**Server:** `https://gameinternationalization.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Responses:**

- `200`: OK → `Roblox.GameInternationalization.Api.GetUiConfigurationsResponse`
- `401`: 0: Authorization has been denied for this request.

**Response fields** (`Roblox.GameInternationalization.Api.GetUiConfigurationsResponse`)

See [Roblox.GameInternationalization.Api.GetUiConfigurationsResponse](#roblox-gameinternationalization-api-getuiconfigurationsresponse) in Models.

**Response example:**
```json
{
  "isGameProductsEnabled": false,
  "isBadgeIconEnabled": false,
  "isGamePassEnabled": false,
  "isDeveloperProductEnabled": false
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://gameinternationalization.roblox.com/v1/ui-configurations"
```

### GET `/v1/user-localization-settings/player-choice/{universeId}` [EXPERIMENTAL]

Get user player choice settings for universe.

**Server:** `https://gameinternationalization.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer` | Yes | The universe's ID. |

**Responses:**

- `200`: OK → `Roblox.GameInternationalization.Api.Models.Response.GetPlayerChoiceUniverseSettingsResponse`
- `400`: 14: Invalid game id
- `401`: 0: Authorization has been denied for this request.
- `500`: 0: An unknown error occurred.
- `503`: 17: Feature is disabled

**Response fields** (`Roblox.GameInternationalization.Api.Models.Response.GetPlayerChoiceUniverseSettingsResponse`)

See [Roblox.GameInternationalization.Api.Models.Response.GetPlayerChoiceUniverseSettingsResponse](#roblox-gameinternationalization-api-models-response-getplayerchoiceuniversesettingsresponse) in Models.

**Response example:**
```json
{
  "IsPlayerChoiceEnabled": false
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://gameinternationalization.roblox.com/v1/user-localization-settings/player-choice/{UNIVERSEID}"
```

### GET `/v1/user-localization-settings/universe/{universeId}` [EXPERIMENTAL]

Get user localization settings for universe.

**Server:** `https://gameinternationalization.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer` | Yes | The universe's ID. |

**Responses:**

- `200`: OK → `Roblox.GameInternationalization.Api.Models.Response.GetUserLocalizationSettingsForUniverseResponse`
- `400`: 14: Invalid game id 21: The language is not supported 22: Invalid language code
- `401`: 0: Authorization has been denied for this request.
- `503`: 17: Feature is disabled

**Response fields** (`Roblox.GameInternationalization.Api.Models.Response.GetUserLocalizationSettingsForUniverseResponse`)

See [Roblox.GameInternationalization.Api.Models.Response.GetUserLocalizationSettingsForUniverseResponse](#roblox-gameinternationalization-api-models-response-getuserlocalizationsettingsforuniverseresponse) in Models.

**Response example:**
```json
{
  "userUniverseLocalizationSettingValue": {
    "settingType": "LanguageFamily",
    "settingTargetId": 0,
    "settingTargetCode": "string"
  }
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://gameinternationalization.roblox.com/v1/user-localization-settings/universe/{UNIVERSEID}"
```

### POST `/v1/user-localization-settings/universe/{universeId}` [EXPERIMENTAL]

Set user localization settings for universe.

**Server:** `https://gameinternationalization.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer` | Yes | The universe's ID. |

**Request Body:** `application/json` — Type: `Roblox.GameInternationalization.Api.Models.Request.SetUserLocalizationSettingsRequest`

See [Roblox.GameInternationalization.Api.Models.Request.SetUserLocalizationSettingsRequest](#roblox-gameinternationalization-api-models-request-setuserlocalizationsettingsrequest) in Models.

**Request example:**
```json
{
  "settingValue": {
    "settingType": "LanguageFamily",
    "settingTargetId": 0,
    "settingTargetCode": "string"
  }
}
```

**Responses:**

- `200`: OK → `Roblox.GameInternationalization.Api.Models.Response.SetUserLocalizationSettingsResponse`
- `400`: 14: Invalid game id 22: Invalid language code
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed
- `503`: 17: Feature is disabled

**Response fields** (`Roblox.GameInternationalization.Api.Models.Response.SetUserLocalizationSettingsResponse`)

See [Roblox.GameInternationalization.Api.Models.Response.SetUserLocalizationSettingsResponse](#roblox-gameinternationalization-api-models-response-setuserlocalizationsettingsresponse) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://gameinternationalization.roblox.com/v1/user-localization-settings/universe/{UNIVERSEID}" \
  -H "Content-Type: application/json" \
  -d '{
  "settingValue": {
    "settingType": "LanguageFamily",
    "settingTargetId": 0,
    "settingTargetCode": "string"
  }
}'
```

### GET `/v1/user/currency`

Gets currency for the authenticated user.

Currency can only be retrieved for the authenticated user.

**Server:** `https://economy.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Responses:**

- `200`: OK → `Roblox.Web.Responses.Economy.CurrencyResponse`
- `401`: 0: Authorization has been denied for this request.
- `403`: 1: The user is invalid.

**Response fields** (`Roblox.Web.Responses.Economy.CurrencyResponse`)

See [Roblox.Web.Responses.Economy.CurrencyResponse](#roblox-web-responses-economy-currencyresponse) in Models.

**Response example:**
```json
{
  "robux": 0
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://economy.roblox.com/v1/user/currency"
```

## Models

### Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.GameInternationalization.Api.GetGameIconResponse_

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | `Roblox.GameInternationalization.Api.GetGameIconResponse[]` | No |  |

### Roblox.GameInternationalization.Api.UpdateThumbnailAltTextRequest

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `thumbnailId` | `integer` | No |  |
| `altText` | `string` | No |  |

### Roblox.GameInternationalization.Api.Models.Response.UploadImageForGameThumbnailResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `mediaAssetId` | `string` | No |  |

### Roblox.GameInternationalization.Api.SortImageIdsRequest

A request model for sorting of image Ids for game thumbnails

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `mediaAssetIds` | `integer[]` | No | List of thumbnail ids in desired order. |

### Roblox.GameInternationalization.Api.GetNameDescriptionHistoryV2Request

A model containing request for getting the translation history of
a content source type's name or description.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `contentId` | `integer` | No |  |
| `contentType` | `string enum (8 values)` | No | The enum representing the type of request while requesting name/description history Values: UniverseDisplayNames, UniverseDisplayDescriptions, BadgeDisplayName, BadgeDisplayDescription, DeveloperProductDisplayName, DeveloperProductDisplayDescription, GamePassDisplayName, GamePassDisplayDescription |
| `languageCode` | `string` | No |  |
| `cursor` | `string` | No |  |
| `count` | `integer` | No |  |
| `sortOrder` | `Asc \| Desc` | No | ['Asc' = 1, 'Desc' = 2] |

### Roblox.GameInternationalization.Api.GetNameDescriptionHistoryResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `history` | `Roblox.GameInternationalization.Api.TranslationHistory[]` | No |  |
| `lastEvaluatedId` | `string` | No |  |

### Roblox.GameInternationalization.Api.UpdateNameDescriptionsRequest

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | `Roblox.GameInternationalization.Api.NameDescription[]` | No |  |

### Roblox.GameInternationalization.Api.UpdateNameDescriptionsResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `successOperations` | `Roblox.GameInternationalization.Api.NameDescription[]` | No |  |
| `failedOperations` | `Roblox.GameInternationalization.Api.FailedNameDescription[]` | No |  |

### Roblox.GameInternationalization.Api.PatchLanguage

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `languageCodeType` | `Language \| Locale` | No | The language code type. |
| `languageCode` | `string` | No | The language code for the language to edit. |
| `delete` | `boolean` | No | An optional field used to indicate whether a language should be deleted from this game's list of supported languages. |

### Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.GameInternationalization.Api.LanguageOrLocaleSettings_

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | `Roblox.GameInternationalization.Api.LanguageOrLocaleSettings[]` | No |  |

### Roblox.GameInternationalization.Api.EditAutomaticTranslationStatusForGameAndLanguageResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `gameId` | `integer` | No | The game id. |
| `languageCode` | `string` | No | The language code. |
| `isAutomaticTranslationEnabled` | `boolean` | No | Indicates whether or not automatic translation is currently enabled for the game and language. |

### Roblox.GameInternationalization.Api.EditImageTranslationStatusForGameAndLanguageResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `gameId` | `integer` | No | The game id. |
| `languageCode` | `string` | No | The language code. |
| `isImageTranslationEnabled` | `boolean` | No | Indicates whether image translation is currently enabled for the game and language. |

### Roblox.GameInternationalization.Api.UpdateUniverseDisplayInfoAutomaticTranslationSettingsResponse

A response model for getting the automatic translation allowed status for game information.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `gameId` | `integer` | No | The game id. |
| `languageCode` | `string` | No | The language code. |
| `isUniverseDisplayInfoAutomaticTranslationEnabled` | `boolean` | No | Indicates universeDisplayInformation automatic translation is enabled. |

### Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.GameInternationalization.Api.UniverseDisplayInfoAutomaticTranslationSettings_

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | `Roblox.GameInternationalization.Api.UniverseDisplayInfoAutomaticTranslationSettings[]` | No |  |

### Roblox.LocalizationTables.Api.GameAutolocalizationInformationResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `isAutolocalizationEnabled` | `boolean` | No |  |
| `isAutomaticEntriesSettingEnabled` | `boolean` | No |  |
| `isAutomaticEntriesDeletionEnabled` | `boolean` | No |  |
| `shouldUseLocalizationTable` | `boolean` | No |  |
| `autoLocalizationTableId` | `string` | No |  |
| `sourceLanguage` | `string` | No |  |
| `assetId` | `integer` | No |  |
| `shouldUseImageLocalizationTable` | `boolean` | No |  |
| `isAutoLocalizationForImageEnabled` | `boolean` | No |  |

### Roblox.LocalizationTables.Api.SetAutolocalizationSettingsForGameRequest

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `isAutolocalizationEnabled` | `boolean` | No |  |
| `isAutomaticEntriesSettingEnabled` | `boolean` | No |  |
| `isAutomaticEntriesDeletionsEnabled` | `boolean` | No |  |
| `shouldUseLocalizationTable` | `boolean` | No |  |
| `shouldUseImageLocalizationTable` | `boolean` | No |  |
| `isAutoLocalizationForImageEnabled` | `boolean` | No |  |

### Roblox.LocalizationTables.Api.AutoLocalizationMetadataResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `isReactVersionEnabledForAutoLocalizationSettings` | `boolean` | No | Is React Implementation of AutoLocalization Settings Enabled |
| `isTabbedUIEnabledForConfigureLocalizationPage` | `boolean` | No | Is Tabbed UI Enabled for Configure Localization Page |
| `isAutomaticTranslationToggleUIEnabled` | `boolean` | No | Is Toggle UI Enabled for Automatic Translations |
| `isAutomaticTranslationQuotaUIEnabled` | `boolean` | No | Is Quota UI Enabled for Automatic Translations |

### Roblox.LocalizationTables.Api.GetLimitsResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `entryOperationLimits` | `Roblox.LocalizationTables.Api.EntryOperationLimits` | No |  |
| `tableOperationLimits` | `Roblox.LocalizationTables.Api.TableOperationLimits` | No |  |

### Roblox.LocalizationTables.Api.GetTableResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | `string` | No |  |
| `name` | `string` | No |  |
| `ownerType` | `User \| Group` | No | Enum for valid OwnerTypes. |
| `ownerId` | `integer` | No |  |
| `assetId` | `integer` | No |  |

### Roblox.LocalizationTables.Api.UpdateTableContentsRequest

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | `string` | No |  |
| `entries` | `Roblox.LocalizationTables.Api.PatchEntry[]` | No |  |

### Roblox.LocalizationTables.Api.UpdateTableContentsResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `failedEntriesAndTranslations` | `Roblox.LocalizationTables.Api.FailedEntry[]` | No |  |
| `modifiedEntriesAndTranslations` | `Roblox.LocalizationTables.Api.ModifiedEntry[]` | No |  |

### Roblox.LocalizationTables.Api.GetTableEntriesPagedResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `previousPageCursor` | `string` | No |  |
| `nextPageCursor` | `string` | No |  |
| `data` | `Roblox.LocalizationTables.Api.Entry[]` | No |  |

### Roblox.LocalizationTables.Api.GetTableEntriesTranslationHistoryRequest

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locale` | `string` | No |  |
| `entries` | `Roblox.LocalizationTables.Api.CursorEntryIdentifier[]` | No |  |
| `sourceType` | `Invalid \| Text \| AssetImage` | No |  |

### Roblox.LocalizationTables.Api.GetTableEntriesTranslationHistoryResponse

A response model for GetTableEntriesTranslationHistory.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `tableId` | `string` | No | The entries' tableId. |
| `locale` | `string` | No | The locale of the translations. |
| `entries` | `Roblox.LocalizationTables.Api.EntryTranslationHistoryPaged[]` | No | The entries with their identifier, translation history, and next cursor. |
| `failedEntries` | `Roblox.LocalizationTables.Api.FailedEntryTranslationHistoryPaged[]` | No | The failed entries. |

### Roblox.LocalizationTables.Api.GetTableEntryCountResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | `string` | No |  |
| `entryCount` | `integer` | No |  |

### Roblox.LocalizationTables.Api.RaiseEventForAutoScrapedEntriesCleanupRequest

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `maxAgeForFlush` | `string` | No | The time range to remove entries from. Following ISO 8601 Durations format |

### Roblox.GameInternationalization.Api.GameAutolocalizationInformationResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `isAutolocalizationEnabled` | `boolean` | No |  |
| `shouldUseLocalizationTable` | `boolean` | No |  |
| `shouldUseImageLocalizationTable` | `boolean` | No |  |
| `isAutoLocalizationForImageEnabled` | `boolean` | No |  |
| `autoLocalizationTableId` | `string` | No |  |
| `assetId` | `integer` | No |  |

### Roblox.GameInternationalization.Api.SetAutolocalizationTableForGameRequest

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `tableId` | `string` | No |  |

### Roblox.LocalizationTables.Api.SetAutolocalizationTableForGameRequest

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `tableId` | `string` | No |  |

### Roblox.GameInternationalization.Api.SetAutolocalizationSettingsForGameRequest

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `isAutolocalizationEnabled` | `boolean` | No |  |
| `shouldUseLocalizationTable` | `boolean` | No |  |

### Roblox.GameInternationalization.Api.GetAutomaticTranslationFeatureStatusForGameResponse

A response model for getting the automatic translation allowed status of a game.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `gameId` | `integer` | No | The game id. |
| `isAutomaticTranslationAllowed` | `boolean` | No | Indicates whether or not automatic translation is allowed for the game. |
| `isAutomaticTranslationSwitchesUIEnabled` | `boolean` | No | Indicates whether or not automatic translation switches are enabled for the game. |

### Roblox.GameInternationalization.Api.GetAutomaticTranslationQuotaForGameResponse

A response model for getting the automatic translation quota info of a game.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `monthlyQuota` | `Roblox.GameInternationalization.Api.MonthlyQuotaModel` | No |  |
| `bankQuota` | `Roblox.GameInternationalization.Api.QuotaModel` | No |  |

### Roblox.GameInternationalization.Api.GetAllowedAutomaticTranslationStatusForLanguagesResponse

A response model for getting the automatic translation allowed status of target languages.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `sourceLanguage` | `string` | No | The source language. |
| `targetLanguages` | `Roblox.GameInternationalization.Api.AutomaticTranslationStatusTargetLanguage[]` | No | The target languages with the automatic translation allowed status. The status basically says if automatic translation can be enabled for the source and target. |

### Roblox.Locale.Api.CountryRegionListResponse

Returns list of supported country/regions

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `countryRegionList` | `Roblox.Locale.Api.CountryRegion[]` | No | List of supported country/regions. Will be empty on error. |

### Roblox.TranslationRoles.Api.UpdateRoleRequest

The request body for update role endpoints

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `assigneeId` | `integer` | No | The id of the assignee |
| `assigneeType` | `user \| group \| groupRole` | No | The type of the assignee ['User' = 0, 'Group' = 1, 'GroupRole' = 2] |
| `role` | `translator` | No | The role to be assigned or revoked ['Translator' = 0] |
| `revoke` | `boolean` | No | To assign or to revoke |

### TranslationRolesApi.Roblox.Web.WebAPI.Models.ApiArrayResponse_System.String_

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | `string[]` | No |  |

### Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.TranslationRoles.Api.Assignee_

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | `Roblox.TranslationRoles.Api.Assignee[]` | No |  |

### Roblox.TranslationRoles.Api.GetGameLocalizationRoleAssignmentsForUserResponse

Response model containing a list of games and associated role assignment info for the requested user and role.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `games` | `Roblox.GameLocalization.Client.GameLocalizationRoles.GameLocalizationRoleAssignment[]` | No | List of games with associated role assignment info. |
| `previousPageCursor` | `string` | No | Cursor which can be used for navigating to previous page. |
| `nextPageCursor` | `string` | No | Cursor which can be used for navigating to next page. |

### Roblox.GameInternationalization.Api.GetTranslationCountsForLanguageOrLocaleResponse

A response model for getting translation counts for a language or locale.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `languageOrLocaleCode` | `string` | No | The code of the language or locale. |
| `languageOrLocaleType` | `Language \| Locale` | No | An indicator that says whether the passed in language/locale code represents a language or locale. |
| `games` | `Roblox.GameInternationalization.Api.TranslationCountGameInfoResponse[]` | No | Info for the requested games, including their translation counts for the specified language or locale. |

### Roblox.GameInternationalization.Api.GetTranslationCountsForGameResponse

A response model that contains game info for getting a translation count.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `gameId` | `integer` | No | The game id. |
| `languagesOrLocales` | `Roblox.GameInternationalization.Api.TranslationCountLanguageOrLocaleResponse[]` | No | The list of languages/locales of the game. |

### Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.GameInternationalization.Api.GetGameThumbnailsResponse_

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | `Roblox.GameInternationalization.Api.GetGameThumbnailsResponse[]` | No |  |

### Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.Locale.Api.SupportedLocaleLocus_

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | `Roblox.Locale.Api.SupportedLocaleLocus[]` | No |  |

### Roblox.Locale.Api.SetShowRobloxTranslationsRequest

Request entity to set the ShowRobloxTranslations field for an account

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `showRobloxTranslations` | `boolean` | No | Value to set the ShowRobloxTranslations field to |

### Roblox.Locale.Api.SuccessResponse

Tells the operation is successful or not

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | `boolean` | No | Returns true on success otherwise false |

### Roblox.Locale.Api.SetSupportedLocaleForUserRequest

Request entity to set Supported Locale for user

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `supportedLocaleCode` | `string` | No | SupportedLocale code |

### Roblox.Locale.Api.SupportedLocalesResponse

Returns list of supported locales

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `supportedLocales` | `Roblox.Locale.Api.SupportedLocale[]` | No | List of supported locales. Will be empty on error. |

### Roblox.Locale.Api.UserLocaleResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `supportedLocale` | `Roblox.Locale.Api.SupportedLocale` | No |  |
| `nativeLanguage` | `Roblox.Locale.Api.Language` | No |  |

### Roblox.Locale.Api.UserLocalizationLocusLocalesResponse

Returns available Roblox.Locale.Api.SupportedLocale models.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `signupAndLogin` | `Roblox.Locale.Api.SupportedLocale` | No |  |
| `generalExperience` | `Roblox.Locale.Api.SupportedLocale` | No |  |
| `ugc` | `Roblox.Locale.Api.SupportedLocale` | No |  |
| `showRobloxTranslations` | `boolean` | No | Whether Roblox-suggested translations should be shown to the user. |

### Roblox.LocalizationTables.Api.LocalizationTablesMetadataResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `isBulkUploadFeatureEnabled` | `boolean` | No | Is bulk upload feature enabled |
| `isCsvDownloadEnabled` | `boolean` | No | Is CSV download feature enabled |
| `isAccessToTranslationMetaDataEnabled` | `boolean` | No | Is access to translation metadata feature enabled |
| `isTranslationManagementRedirectionEnabled` | `boolean` | No | Is access to translation metadata feature enabled |
| `isUntranslatedFilterEnabled` | `boolean` | No | Is untranslated filter on UI is enabled |
| `isAutomaticTranslationFilterEnabled` | `boolean` | No | Is filter for automatic translations on UI is enabled |

### Roblox.LocalizationTables.Api.CreateTableRequest

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | `string` | No |  |
| `ownerType` | `User \| Group` | No |  |
| `ownerId` | `integer` | No |  |

### Roblox.LocalizationTables.Api.CreateTableResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | `string` | No |  |
| `assetId` | `integer` | No |  |

### Roblox.LocalizationTables.Api.GetTableAssetEntriesPagedResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `previousPageCursor` | `string` | No |  |
| `nextPageCursor` | `string` | No |  |
| `data` | `Roblox.LocalizationTables.Api.AssetEntry[]` | No |  |

### Roblox.LocalizationTables.Api.GetTableEntriesTranslationFeedbackRequest

A request model for GetTableEntriesTranslationFeedback.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `sourceLocale` | `string` | No | locale code of source language, we only accept language code at the moment. |
| `entries` | `Roblox.LocalizationTables.Api.EntryIdentifierWithTranslation[]` | No | entry identifier |

### Roblox.LocalizationTables.Api.GetTableEntriesTranslationFeedbackResponse

A response model for GetTableEntriesTranslationFeedback.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `tableId` | `string` | No | The entries' tableId. |
| `entries` | `Roblox.LocalizationTables.Api.EntryTranslationFeedback[]` | No | The entries with their identifier, translation feedback details. |

### Roblox.GameInternationalization.Api.AssociateLocalizationTablesToGameRequest

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `tables` | `Roblox.GameInternationalization.Api.LocalizationTableGameAssociation[]` | No |  |

### Roblox.GameInternationalization.Api.AssociateLocalizationTablesToGameResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | `boolean` | No |  |

### Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.GameInternationalization.Api.NameDescription_

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | `Roblox.GameInternationalization.Api.NameDescription[]` | No |  |

### Roblox.GameInternationalization.Api.Models.Response.GameNameDescriptionMetadataResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `isNameDescriptionMigrationEnabled` | `boolean` | No |  |

### Roblox.GameInternationalization.Api.Language

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | `string` | No |  |
| `nativeName` | `string` | No |  |
| `languageCode` | `string` | No |  |

### Roblox.GameInternationalization.Api.SourceLanguageWithLocales

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `languageFamily` | `Roblox.GameInternationalization.Api.Language` | No |  |
| `defaultLocale` | `Roblox.Localization.Client.SupportedLocale` | No |  |
| `childLocales` | `Roblox.Localization.Client.SupportedLocale[]` | No |  |

### Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.GameInternationalization.Api.LanguageOrLocale_

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | `Roblox.GameInternationalization.Api.LanguageOrLocale[]` | No |  |

### Roblox.GameInternationalization.Api.SupportedLanguagesMetadataResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `isFeatureEnabled` | `boolean` | No |  |
| `areAllLanguagesEnabled` | `boolean` | No |  |
| `minimumUniverseIdForFeature` | `integer` | No |  |
| `isHumanTranslationProgressUIEnabled` | `boolean` | No | Is translation progress for human translations enabled on UI |
| `isAutomaticTranslationProgressUIEnabled` | `boolean` | No | Is translation progress for automatic translations enabled on UI |
| `isSupportedLanguagesChildLocalesUIEnabled` | `boolean` | No | Is Language Locales UI Enabled for Supported Languages |

### Roblox.GameInternationalization.Api.RequestTranslationAnalyticsReportRequest

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `startDateTime` | `string` | No | The inclusive start dateTime of report in UTC |
| `endDateTime` | `string` | No | The exclusive end dateTime of report in UTC |
| `reportType` | `GameTranslationStatus \| GameTranslationStatusForTranslator \| GameTranslationStatusForTranslatorGroup \| Test` | No | The report type |
| `reportSubjectTargetId` | `integer` | No | The report subject target id |

### Roblox.GameInternationalization.Api.RequestTranslationAnalyticsReportResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `reportGenerationStatus` | `inProgress \| ready \| unavailable` | No | ['InProgress' = 0, 'Ready' = 1, 'Unavailable' = 2] |

### Roblox.GameInternationalization.Api.TranslationAnalyticsMetadataResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `isFeatureEnabledOnUI` | `boolean` | No | Is Translation Analytics feature enabled on UI |
| `reportRequestPollingIntervalSeconds` | `integer` | No | Number of seconds to poll the server for report availability |
| `minimumDateTimeForAnalyticsReport` | `string` | No | Date-Time since the Analytics Reports can be downloaded |

### Roblox.GameInternationalization.Api.GetUiConfigurationsResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `isGameProductsEnabled` | `boolean` | No | Game products translation management page is enabled or not. |
| `isBadgeIconEnabled` | `boolean` | No | Badge Icon translation management is enabled or not. |
| `isGamePassEnabled` | `boolean` | No | Game pass translation management is enabled or not. |
| `isDeveloperProductEnabled` | `boolean` | No | Developer product translation management is enabled or not. |

### Roblox.GameInternationalization.Api.Models.Response.GetPlayerChoiceUniverseSettingsResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `IsPlayerChoiceEnabled` | `boolean` | No | Checks whether player choice warning should be displayed to users. |

### Roblox.GameInternationalization.Api.Models.Response.GetUserLocalizationSettingsForUniverseResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `userUniverseLocalizationSettingValue` | `Roblox.GameLocalization.Client.UserUniverseLocalizationSettingValue` | No |  |

### Roblox.GameInternationalization.Api.Models.Request.SetUserLocalizationSettingsRequest

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `settingValue` | `Roblox.GameLocalization.Client.UserUniverseLocalizationSettingValue` | No |  |

### Roblox.Web.Responses.Economy.CurrencyResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `robux` | `integer` | No |  |