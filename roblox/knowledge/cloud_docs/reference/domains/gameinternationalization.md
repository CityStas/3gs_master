---
name: "GameInternationalization Api v2"
last_updated: 2026-10-30T19:56:08Z
type: legacy
api_base_url: "https://gameinternationalization.roblox.com"
versions: [v2, v1]
endpoints: 66
auth: [cookie]
---

# GameInternationalization Api v2

> **Warning:** Legacy APIs with cookie authentication can incorporate breaking changes without notice. We don't recommend them for production applications.

**Base URL:** `https://gameinternationalization.roblox.com`
**Versions:** v2, v1

## V2

### GET `/v2/supported-languages/games/{gameId}`

Get the supported languages for a game.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gameId` | path | `integer (int64)` | Yes | The id of the game. |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.GameInternationalization.Api.LanguageWithLocales]`
- `400`: 14: Invalid game id
- `503`: 17: Feature is disabled

**Response fields** (`Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.GameInternationalization.Api.LanguageWithLocales]`)

See [Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.GameInternationalization.Api.LanguageWithLocales]](#roblox-web-webapi-models-apiarrayresponse-roblox-gameinternationalization-api-languagewithlocales-) in Models.

**Response example:**
```json
{
  "data": [
    {
      "languageFamily": "...",
      "childLocales": "..."
    }
  ]
}
```

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://gameinternationalization.roblox.com/v2/supported-languages/games/{GAMEID}"
```

## Models

### Roblox.GameInternationalization.Api.Language

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | `string` | No |  |
| `nativeName` | `string` | No |  |
| `languageCode` | `string` | No |  |

### Roblox.GameInternationalization.Api.LanguageWithLocales

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `languageFamily` | `Roblox.GameInternationalization.Api.Language` | No |  |
| `childLocales` | `Roblox.Localization.Client.SupportedLocale[]` | No |  |

### Roblox.Localization.Client.LanguageFamily

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | `integer` | No |  |
| `name` | `string` | No |  |
| `nativeName` | `string` | No |  |
| `languageCode` | `string` | No |  |
| `isRightToLeft` | `boolean` | No |  |

### Roblox.Localization.Client.SupportedLocale

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | `integer` | No |  |
| `locale` | `string enum (51 values)` | No |  Values: en_us, es_es, fr_fr, id_id, it_it, ja_jp, ko_kr, ru_ru, th_th, tr_tr, vi_vn, pt_br, de_de, zh_cn, zh_tw, bg_bg, bn_bd, cs_cz, da_dk, el_gr, et_ee, fi_fi, hi_in, hr_hr, hu_hu, ka_ge, kk_kz, km_kh, lt_lt, lv_lv, ms_my, my_mm, nb_no, nl_nl, fil_ph, pl_pl, ro_ro, uk_ua, si_lk, sk_sk, sl_sl, sq_al, bs_ba, sr_rs, sv_se, zh_cjv, ar_001, en_gb, pt_pt, es_mx, fr_ca |
| `localeCode` | `string` | No |  |
| `name` | `string` | No |  |
| `nativeName` | `string` | No |  |
| `language` | `Roblox.Localization.Client.LanguageFamily` | No |  |

### Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.GameInternationalization.Api.LanguageWithLocales]

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | `Roblox.GameInternationalization.Api.LanguageWithLocales[]` | No |  |

## V1

### GET `/v1/autolocalization/metadata` *(deprecated)*

Metadata for AutoLocalization Configuration

**Responses:**

- `200`: OK → `Roblox.GameInternationalization.Api.AutoLocalizationMetadataResponse`
- `401`: 0: Authorization has been denied for this request.

**Response fields** (`Roblox.GameInternationalization.Api.AutoLocalizationMetadataResponse`)

See [Roblox.GameInternationalization.Api.AutoLocalizationMetadataResponse](#roblox-gameinternationalization-api-autolocalizationmetadataresponse) in Models.

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
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://gameinternationalization.roblox.com/v1/autolocalization/metadata"
```

### GET `/v1/automatic-translation/games/{gameId}/feature-status`

Checks if automatic translation can be enabled for a game.
The user must still have proper permissions for the game to get this info.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gameId` | path | `integer (int64)` | Yes | The game id. |

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
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://gameinternationalization.roblox.com/v1/automatic-translation/games/{GAMEID}/feature-status"
```

### GET `/v1/automatic-translation/games/{gameId}/quota`

Returns the automatic translation quota info for a game.
The user must still have proper permissions for the game to get this info.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gameId` | path | `integer (int64)` | Yes | The game id. |

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
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://gameinternationalization.roblox.com/v1/automatic-translation/games/{GAMEID}/quota"
```

### GET `/v1/automatic-translation/languages/{languageCode}/target-languages`

Checks if the requested target languages are allowed for automatic translation based on the source language.
If there are no requested target languages, then all allowed target languages for the source language will be returned.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `languageCode` | path | `string` | Yes | The source language. |
| `targetLanguages` | query | `array` | No | Optional target languages. If not passed in, all allowed target languages for the source language will be returned. |
| `gameId` | query | `integer (int64)` | No | Optional gameId. If not passed in, we'll return the default list of languages allowed. |

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

### GET `/v1/badges/{badgeId}/icons`

Get all icons for a badge

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `badgeId` | path | `integer (int64)` | Yes | The id of the badge |
| `width` | query | `integer (int32)` | No | The width of the icon to request |
| `height` | query | `integer (int32)` | No | The height of the icon to request |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.GameInternationalization.Api.GetBadgeIconResponse]`
- `400`: 52: Image dimensions are invalid 62: Invalid game badge id
- `401`: 0: Authorization has been denied for this request.
- `500`: 0: An unknown error occurred.
- `503`: 17: Feature is disabled

**Response fields** (`Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.GameInternationalization.Api.GetBadgeIconResponse]`)

See [Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.GameInternationalization.Api.GetBadgeIconResponse]](#roblox-web-webapi-models-apiarrayresponse-roblox-gameinternationalization-api-getbadgeiconresponse-) in Models.

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
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://gameinternationalization.roblox.com/v1/badges/{BADGEID}/icons"
```

### GET `/v1/badges/{badgeId}/name-description`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `badgeId` | path | `integer (int64)` | Yes |  |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.GameInternationalization.Api.NameDescription]`
- `400`: 62: Invalid game badge id
- `401`: 0: Authorization has been denied for this request.
- `503`: 17: Feature is disabled

**Response fields** (`Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.GameInternationalization.Api.NameDescription]`)

See [Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.GameInternationalization.Api.NameDescription]](#roblox-web-webapi-models-apiarrayresponse-roblox-gameinternationalization-api-namedescription-) in Models.

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
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://gameinternationalization.roblox.com/v1/badges/{BADGEID}/name-description"
```

### GET `/v1/developer-products/{developerProductId}/icons`

Get all icons for a developer product

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `developerProductId` | path | `integer (int64)` | Yes | The id of the developer product |
| `width` | query | `integer (int32)` | No | The width of the icon to request |
| `height` | query | `integer (int32)` | No | The height of the icon to request |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.GameInternationalization.Api.GetDeveloperProductIconResponse]`
- `400`: 52: Image dimensions are invalid 70: Invalid developer product id
- `401`: 0: Authorization has been denied for this request.
- `500`: 0: An unknown error occurred.
- `503`: 17: Feature is disabled

**Response fields** (`Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.GameInternationalization.Api.GetDeveloperProductIconResponse]`)

See [Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.GameInternationalization.Api.GetDeveloperProductIconResponse]](#roblox-web-webapi-models-apiarrayresponse-roblox-gameinternationalization-api-getdeveloperproducticonresponse-) in Models.

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
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://gameinternationalization.roblox.com/v1/developer-products/{DEVELOPERPRODUCTID}/icons"
```

### GET `/v1/developer-products/{developerProductId}/name-description`

Get all names and descriptions of a developer product

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `developerProductId` | path | `integer (int64)` | Yes | The developer product Id |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.GameInternationalization.Api.NameDescription]`
- `400`: 70: Invalid developer product id
- `401`: 0: Authorization has been denied for this request.
- `503`: 17: Feature is disabled

**Response fields** (`Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.GameInternationalization.Api.NameDescription]`)

See [Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.GameInternationalization.Api.NameDescription]](#roblox-web-webapi-models-apiarrayresponse-roblox-gameinternationalization-api-namedescription-) in Models.

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
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://gameinternationalization.roblox.com/v1/developer-products/{DEVELOPERPRODUCTID}/name-description"
```

### GET `/v1/game-icon/games/{gameId}`

Get all icons for a game

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gameId` | path | `integer (int64)` | Yes | The id of the game |
| `width` | query | `integer (int32)` | No | The width of the icon to request |
| `height` | query | `integer (int32)` | No | The height of the icon to request |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.GameInternationalization.Api.GetGameIconResponse]`
- `400`: 14: Invalid game id 52: Image dimensions are invalid
- `500`: 0: An unknown error occurred.
- `503`: 17: Feature is disabled

**Response fields** (`Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.GameInternationalization.Api.GetGameIconResponse]`)

See [Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.GameInternationalization.Api.GetGameIconResponse]](#roblox-web-webapi-models-apiarrayresponse-roblox-gameinternationalization-api-getgameiconresponse-) in Models.

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
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://gameinternationalization.roblox.com/v1/game-icon/games/{GAMEID}"
```

### GET `/v1/game-localization-status/{gameId}/translation-counts`

Gets the language translation counts for all languages of a game

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gameId` | path | `integer (int64)` | Yes | GameID of the game to get translation counts for |

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
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://gameinternationalization.roblox.com/v1/game-localization-status/{GAMEID}/translation-counts"
```

### GET `/v1/game-localization-status/translation-counts-for-language-or-locale`

Gets the language translation counts for the specified table.
The languages to retrieve must be provided.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gameIds` | query | `array` | Yes | List of game ids to retrieve translation counts for. |
| `languageOrLocaleCode` | query | `string` | Yes | The code for the language or locale. |
| `languageOrLocaleType` | query | `string` | Yes | Indicates whether the languageOrLocaleCode represents a language or locale. Valid values: `Language`, `Locale` |

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
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://gameinternationalization.roblox.com/v1/game-localization-status/translation-counts-for-language-or-locale?gameIds={VALUE}&languageOrLocaleCode={VALUE}&languageOrLocaleType={VALUE}"
```

### GET `/v1/game-passes/{gamePassId}/icons`

Get all icons for a game pass

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gamePassId` | path | `integer (int64)` | Yes | The game pass id |
| `width` | query | `integer (int32)` | No | The width of the icon to request |
| `height` | query | `integer (int32)` | No | The height of the icon to request |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.GameInternationalization.Api.GetGamePassIconResponse]`
- `400`: 52: Image dimensions are invalid 61: Invalid game pass id
- `401`: 0: Authorization has been denied for this request.
- `500`: 0: An unknown error occurred.
- `503`: 17: Feature is disabled

**Response fields** (`Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.GameInternationalization.Api.GetGamePassIconResponse]`)

See [Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.GameInternationalization.Api.GetGamePassIconResponse]](#roblox-web-webapi-models-apiarrayresponse-roblox-gameinternationalization-api-getgamepassiconresponse-) in Models.

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
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://gameinternationalization.roblox.com/v1/game-passes/{GAMEPASSID}/icons"
```

### GET `/v1/game-passes/{gamePassId}/name-description`

Get all names and descriptions of a game pass

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gamePassId` | path | `integer (int64)` | Yes | The game pass Id |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.GameInternationalization.Api.NameDescription]`
- `400`: 61: Invalid game pass id
- `401`: 0: Authorization has been denied for this request.
- `503`: 17: Feature is disabled

**Response fields** (`Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.GameInternationalization.Api.NameDescription]`)

See [Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.GameInternationalization.Api.NameDescription]](#roblox-web-webapi-models-apiarrayresponse-roblox-gameinternationalization-api-namedescription-) in Models.

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
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://gameinternationalization.roblox.com/v1/game-passes/{GAMEPASSID}/name-description"
```

### GET `/v1/game-thumbnails/games/{gameId}/images`

Get the localized image ids in all languages for a game.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gameId` | path | `integer (int64)` | Yes | The game identifier. |
| `width` | query | `integer (int32)` | No | The width. |
| `height` | query | `integer (int32)` | No | The height. |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.GameInternationalization.Api.GetGameThumbnailsResponse]`
- `400`: 14: Invalid game id 52: Image dimensions are invalid
- `500`: 0: An unknown error occurred.
- `503`: 17: Feature is disabled

**Response fields** (`Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.GameInternationalization.Api.GetGameThumbnailsResponse]`)

See [Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.GameInternationalization.Api.GetGameThumbnailsResponse]](#roblox-web-webapi-models-apiarrayresponse-roblox-gameinternationalization-api-getgamethumbnailsresponse-) in Models.

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

### GET `/v1/name-description/games/{gameId}`

Gets a game's name and description in all supported languages

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gameId` | path | `integer (int64)` | Yes | The id of the game |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.GameInternationalization.Api.NameDescription]`
- `400`: 14: Invalid game id
- `503`: 17: Feature is disabled

**Response fields** (`Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.GameInternationalization.Api.NameDescription]`)

See [Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.GameInternationalization.Api.NameDescription]](#roblox-web-webapi-models-apiarrayresponse-roblox-gameinternationalization-api-namedescription-) in Models.

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

### PATCH `/v1/name-description/games/{gameId}`

Updates a game's name and/or description in multiple languages.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gameId` | path | `integer (int64)` | Yes | The id of the game. |

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
curl -X PATCH -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
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

### GET `/v1/name-description/metadata`

Rollout settings for name/description migration to new page

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
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://gameinternationalization.roblox.com/v1/name-description/metadata"
```

### GET `/v1/source-language/games/{gameId}`

Gets the source language of a game

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gameId` | path | `integer (int64)` | Yes |  |

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

### PATCH `/v1/source-language/games/{gameId}`

Sets the source language of a game

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gameId` | path | `integer (int64)` | Yes |  |
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
curl -X PATCH -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://gameinternationalization.roblox.com/v1/source-language/games/{GAMEID}?languageCode={VALUE}"
```

### GET `/v1/source-language/games/{gameId}/language-with-locales`

Gets the source language of a game

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gameId` | path | `integer (int64)` | Yes |  |

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

### GET `/v1/supported-languages/games/{gameId}`

Get the supported languages for a game.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gameId` | path | `integer (int64)` | Yes | The id of the game. |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.GameInternationalization.Api.LanguageOrLocale]`
- `400`: 14: Invalid game id
- `503`: 17: Feature is disabled

**Response fields** (`Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.GameInternationalization.Api.LanguageOrLocale]`)

See [Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.GameInternationalization.Api.LanguageOrLocale]](#roblox-web-webapi-models-apiarrayresponse-roblox-gameinternationalization-api-languageorlocale-) in Models.

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
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://gameinternationalization.roblox.com/v1/supported-languages/games/{GAMEID}"
```

### PATCH `/v1/supported-languages/games/{gameId}`

Add or remove supported languages for a game.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gameId` | path | `integer (int64)` | Yes | The id of the game. |

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
curl -X PATCH -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
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

### GET `/v1/supported-languages/games/{gameId}/automatic-translation-status`

Get the automatic translation status of supported languages for a game.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gameId` | path | `integer (int64)` | Yes | The id of the game. |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.GameInternationalization.Api.LanguageOrLocaleSettings]`
- `400`: 14: Invalid game id
- `401`: 0: Authorization has been denied for this request.
- `403`: 18: You do not have permission to manage this game
- `503`: 17: Feature is disabled

**Response fields** (`Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.GameInternationalization.Api.LanguageOrLocaleSettings]`)

See [Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.GameInternationalization.Api.LanguageOrLocaleSettings]](#roblox-web-webapi-models-apiarrayresponse-roblox-gameinternationalization-api-languageorlocalesettings-) in Models.

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
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://gameinternationalization.roblox.com/v1/supported-languages/games/{GAMEID}/automatic-translation-status"
```

### GET `/v1/supported-languages/games/{gameId}/in-experience-language-selection`

Get the user's in-experience language selector languages for a game.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gameId` | path | `integer (int64)` | Yes | The id of the game. |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.GameInternationalization.Api.LanguageOrLocale]`
- `400`: 14: Invalid game id
- `503`: 17: Feature is disabled

**Response fields** (`Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.GameInternationalization.Api.LanguageOrLocale]`)

See [Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.GameInternationalization.Api.LanguageOrLocale]](#roblox-web-webapi-models-apiarrayresponse-roblox-gameinternationalization-api-languageorlocale-) in Models.

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
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://gameinternationalization.roblox.com/v1/supported-languages/games/{GAMEID}/in-experience-language-selection"
```

### GET `/v1/supported-languages/games/{gameId}/universe-display-info-automatic-translation-settings`

Get UniverseDisplayInfo automatic translation settings.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gameId` | path | `integer (int64)` | Yes | The game id. |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.GameInternationalization.Api.UniverseDisplayInfoAutomaticTranslationSettings]`
- `400`: 14: Invalid game id
- `401`: 0: Authorization has been denied for this request.
- `403`: 18: You do not have permission to manage this game
- `500`: 0: An unknown error occurred. 22: Invalid language code 83: Failed to get UniverseDisplayInformation content instance auto translation settings 84: Count of language code is larger than max batch get size

**Response fields** (`Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.GameInternationalization.Api.UniverseDisplayInfoAutomaticTranslationSettings]`)

See [Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.GameInternationalization.Api.UniverseDisplayInfoAutomaticTranslationSettings]](#roblox-web-webapi-models-apiarrayresponse-roblox-gameinternationalization-api-universedisplayinfoautomatictranslationsettings-) in Models.

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
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://gameinternationalization.roblox.com/v1/supported-languages/games/{GAMEID}/universe-display-info-automatic-translation-settings"
```

### GET `/v1/supported-languages/metadata`

Rollout settings for supported languages of a game

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
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://gameinternationalization.roblox.com/v1/supported-languages/metadata"
```

### GET `/v1/translation-analytics/games/{gameId}/download-translation-analytics-report`

Download translation analytics report after the report is ready

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gameId` | path | `integer (int64)` | Yes | The game's id |
| `startDateTime` | query | `string (date-time)` | Yes | The inclusive start dateTime of report in UTC |
| `endDateTime` | query | `string (date-time)` | Yes | The exclusive end dateTime of report in UTC |
| `reportType` | query | `string` | Yes | The report type Valid values: `GameTranslationStatus`, `GameTranslationStatusForTranslator`, `GameTranslationStatusForTranslatorGroup`, `Test` |
| `reportSubjectTargetId` | query | `integer (int64)` | Yes | The translator group id |

**Responses:**

- `200`: OK → `object`
- `400`: 14: Invalid game id 56: You need to provide a valid translator group id to get report. 58: Start datetime or end datetime is invlaid. 59: Report type is invalid
- `401`: 0: Authorization has been denied for this request.
- `403`: 57: You do not have permission to request translation analytics report.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://gameinternationalization.roblox.com/v1/translation-analytics/games/{GAMEID}/download-translation-analytics-report?startDateTime={VALUE}&endDateTime={VALUE}&reportType={VALUE}&reportSubjectTargetId={VALUE}"
```

### GET `/v1/translation-analytics/metadata`

Get metadata related to UI and rollout settings

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
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://gameinternationalization.roblox.com/v1/translation-analytics/metadata"
```

### GET `/v1/ui-configurations`

Get ui configurations for frontend to use.

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
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://gameinternationalization.roblox.com/v1/ui-configurations"
```

### GET `/v1/user-localization-settings/player-choice/{universeId}`

Get user player choice settings for universe.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer (int64)` | Yes | The universe's ID. |

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
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://gameinternationalization.roblox.com/v1/user-localization-settings/player-choice/{UNIVERSEID}"
```

### GET `/v1/user-localization-settings/universe/{universeId}`

Get user localization settings for universe.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer (int64)` | Yes | The universe's ID. |

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
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://gameinternationalization.roblox.com/v1/user-localization-settings/universe/{UNIVERSEID}"
```

### POST `/v1/user-localization-settings/universe/{universeId}`

Set user localization settings for universe.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer (int64)` | Yes | The universe's ID. |

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
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
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

### POST `/v1/autolocalization/games/{gameId}/autolocalizationtable` *(deprecated)*

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gameId` | path | `integer (int64)` | Yes |  |

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
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://gameinternationalization.roblox.com/v1/autolocalization/games/{GAMEID}/autolocalizationtable"
```

### PATCH `/v1/autolocalization/games/{gameId}/autolocalizationtable` *(deprecated)*

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gameId` | path | `integer (int64)` | Yes |  |

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
curl -X PATCH -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://gameinternationalization.roblox.com/v1/autolocalization/games/{GAMEID}/autolocalizationtable" \
  -H "Content-Type: application/json" \
  -d '{
  "tableId": "string"
}'
```

### POST `/v1/badges/{badgeId}/icons/language-codes/{languageCode}`

Update a badge's icon

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `badgeId` | path | `integer (int64)` | Yes | The id of the badge |
| `languageCode` | path | `string` | Yes | The language code of this icon to update |
| `Files` | formData | `file` | No |  |

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
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://gameinternationalization.roblox.com/v1/badges/{BADGEID}/icons/language-codes/{LANGUAGECODE}"
```

### DELETE `/v1/badges/{badgeId}/icons/language-codes/{languageCode}`

Delete a localized icon from a badge

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `badgeId` | path | `integer (int64)` | Yes | The id of the badge |
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
curl -X DELETE -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://gameinternationalization.roblox.com/v1/badges/{BADGEID}/icons/language-codes/{LANGUAGECODE}"
```

### POST `/v1/developer-products/{developerProductId}/icons/language-codes/{languageCode}`

Update a developer product's icon

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `developerProductId` | path | `integer (int64)` | Yes | The id of the developer product |
| `languageCode` | path | `string` | Yes | The language code of this icon to update |
| `Files` | formData | `file` | No |  |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: 22: Invalid language code 26: You can't update translations for source language 45: File uploaded does not match known image format 46: File not present in request 53: Language is not supported for the game. 70: Invalid developer product id
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
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://gameinternationalization.roblox.com/v1/developer-products/{DEVELOPERPRODUCTID}/icons/language-codes/{LANGUAGECODE}"
```

### DELETE `/v1/developer-products/{developerProductId}/icons/language-codes/{languageCode}`

Delete a localized icon from a developer product

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `developerProductId` | path | `integer (int64)` | Yes | The id of the developer product |
| `languageCode` | path | `string` | Yes | The language code of the localized icon to delete |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: 22: Invalid language code 23: You can't delete translations for source language 53: Language is not supported for the game. 70: Invalid developer product id
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 18: You do not have permission to manage this game
- `500`: 0: An unknown error occurred.
- `503`: 17: Feature is disabled

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X DELETE -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://gameinternationalization.roblox.com/v1/developer-products/{DEVELOPERPRODUCTID}/icons/language-codes/{LANGUAGECODE}"
```

### POST `/v1/game-icon/games/{gameId}/language-codes/{languageCode}`

Update a game's icon

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gameId` | path | `integer (int64)` | Yes | The id of the game |
| `languageCode` | path | `string` | Yes | The language code of this icon to update |
| `Files` | formData | `file` | No |  |

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
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://gameinternationalization.roblox.com/v1/game-icon/games/{GAMEID}/language-codes/{LANGUAGECODE}"
```

### DELETE `/v1/game-icon/games/{gameId}/language-codes/{languageCode}`

Delete a localized icon from a game

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gameId` | path | `integer (int64)` | Yes | The id of the game |
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
curl -X DELETE -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://gameinternationalization.roblox.com/v1/game-icon/games/{GAMEID}/language-codes/{LANGUAGECODE}"
```

### POST `/v1/game-passes/{gamePassId}/icons/language-codes/{languageCode}`

Update a game pass's icon

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gamePassId` | path | `integer (int64)` | Yes | The game pass id |
| `languageCode` | path | `string` | Yes | The language code of this icon to update |
| `Files` | formData | `file` | No |  |

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
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://gameinternationalization.roblox.com/v1/game-passes/{GAMEPASSID}/icons/language-codes/{LANGUAGECODE}"
```

### DELETE `/v1/game-passes/{gamePassId}/icons/language-codes/{languageCode}`

Delete a localized icon from a game pass

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gamePassId` | path | `integer (int64)` | Yes | The game pass id |
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
curl -X DELETE -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://gameinternationalization.roblox.com/v1/game-passes/{GAMEPASSID}/icons/language-codes/{LANGUAGECODE}"
```

### POST `/v1/game-thumbnails/games/{gameId}/language-codes/{languageCode}/alt-text`

Updates the game thumbnail alt text.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gameId` | path | `integer (int64)` | Yes | The game identifier. |
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
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://gameinternationalization.roblox.com/v1/game-thumbnails/games/{GAMEID}/language-codes/{LANGUAGECODE}/alt-text" \
  -H "Content-Type: application/json" \
  -d '{
  "thumbnailId": 0,
  "altText": "string"
}'
```

### POST `/v1/game-thumbnails/games/{gameId}/language-codes/{languageCode}/image`

Uploads the game thumbnail.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gameId` | path | `integer (int64)` | Yes | The game identifier. |
| `languageCode` | path | `string` | Yes | The language code. |
| `Files` | formData | `file` | No |  |

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
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://gameinternationalization.roblox.com/v1/game-thumbnails/games/{GAMEID}/language-codes/{LANGUAGECODE}/image"
```

### POST `/v1/game-thumbnails/games/{gameId}/language-codes/{languageCode}/images/order`

Orders the specified image Ids for the game thumbnails.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gameId` | path | `integer (int64)` | Yes | The game identifier. |
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
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://gameinternationalization.roblox.com/v1/game-thumbnails/games/{GAMEID}/language-codes/{LANGUAGECODE}/images/order" \
  -H "Content-Type: application/json" \
  -d '{
  "mediaAssetIds": [
    0
  ]
}'
```

### POST `/v1/name-description/games/translation-history`

Gets the history for name or description in a provided language.

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
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
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

### POST `/v1/translation-analytics/games/{gameId}/request-translation-analytics-report`

Request translation analytics report to be generated

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gameId` | path | `integer (int64)` | Yes | The game's id |

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
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://gameinternationalization.roblox.com/v1/translation-analytics/games/{GAMEID}/request-translation-analytics-report" \
  -H "Content-Type: application/json" \
  -d '{
  "startDateTime": "2024-01-01T00:00:00Z",
  "endDateTime": "2024-01-01T00:00:00Z",
  "reportType": "GameTranslationStatus",
  "reportSubjectTargetId": 0
}'
```

### PATCH `/v1/autolocalization/games/{gameId}/settings` *(deprecated)*

Sets a game's auto-localization related settings

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gameId` | path | `integer (int64)` | Yes | The id of the game. |

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
curl -X PATCH -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://gameinternationalization.roblox.com/v1/autolocalization/games/{GAMEID}/settings" \
  -H "Content-Type: application/json" \
  -d '{
  "isAutolocalizationEnabled": false,
  "shouldUseLocalizationTable": false
}'
```

### PATCH `/v1/badges/{badgeId}/description/language-codes/{languageCode}`

Update localized description of a badge

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `badgeId` | path | `integer (int64)` | Yes | The badge id |
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
curl -X PATCH -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://gameinternationalization.roblox.com/v1/badges/{BADGEID}/description/language-codes/{LANGUAGECODE}" \
  -H "Content-Type: application/json" \
  -d '{
  "description": "string"
}'
```

### PATCH `/v1/badges/{badgeId}/name-description/language-codes/{languageCode}`

Update localized name and description of a badge

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `badgeId` | path | `integer (int64)` | Yes | The badge id |
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
curl -X PATCH -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://gameinternationalization.roblox.com/v1/badges/{BADGEID}/name-description/language-codes/{LANGUAGECODE}" \
  -H "Content-Type: application/json" \
  -d '{
  "name": "string",
  "description": "string"
}'
```

### DELETE `/v1/badges/{badgeId}/name-description/language-codes/{languageCode}`

Delete localized name and description of a badge

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `badgeId` | path | `integer (int64)` | Yes | The badge id |
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
curl -X DELETE -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://gameinternationalization.roblox.com/v1/badges/{BADGEID}/name-description/language-codes/{LANGUAGECODE}"
```

### PATCH `/v1/badges/{badgeId}/name/language-codes/{languageCode}`

Update localized name of a badge

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `badgeId` | path | `integer (int64)` | Yes | The badge id |
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
curl -X PATCH -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://gameinternationalization.roblox.com/v1/badges/{BADGEID}/name/language-codes/{LANGUAGECODE}" \
  -H "Content-Type: application/json" \
  -d '{
  "name": "string"
}'
```

### PATCH `/v1/developer-products/{developerProductId}/description/language-codes/{languageCode}`

Update localized description of a developer product

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `developerProductId` | path | `integer (int64)` | Yes | The developer product id |
| `languageCode` | path | `string` | Yes | The language code of the description to update |

**Request Body:** `application/json` — Type: `Roblox.GameInternationalization.Api.UpdateDeveloperProductDescriptionRequest`

See [Roblox.GameInternationalization.Api.UpdateDeveloperProductDescriptionRequest](#roblox-gameinternationalization-api-updatedeveloperproductdescriptionrequest) in Models.

**Request example:**
```json
{
  "description": "string"
}
```

**Responses:**

- `200`: OK → `Roblox.GameInternationalization.Api.UpdateDeveloperProductDescriptionResponse`
- `400`: 13: Request body can't be null 19: New name is null or whitespaces or new name/description is too long 20: New name or description is moderated 22: Invalid language code 26: You can't update translations for source language 53: Language is not supported for the game. 70: Invalid developer product id
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 18: You do not have permission to manage this game
- `500`: 0: An unknown error occurred.
- `503`: 17: Feature is disabled

**Response fields** (`Roblox.GameInternationalization.Api.UpdateDeveloperProductDescriptionResponse`)

See [Roblox.GameInternationalization.Api.UpdateDeveloperProductDescriptionResponse](#roblox-gameinternationalization-api-updatedeveloperproductdescriptionresponse) in Models.

**Response example:**
```json
{
  "description": "string"
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X PATCH -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://gameinternationalization.roblox.com/v1/developer-products/{DEVELOPERPRODUCTID}/description/language-codes/{LANGUAGECODE}" \
  -H "Content-Type: application/json" \
  -d '{
  "description": "string"
}'
```

### PATCH `/v1/developer-products/{developerProductId}/name-description/language-codes/{languageCode}`

Update localized name and description of a developer product

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `developerProductId` | path | `integer (int64)` | Yes | The developer product id |
| `languageCode` | path | `string` | Yes | The language code of the name and description to Update |

**Request Body:** `application/json` — Type: `Roblox.GameInternationalization.Api.UpdateDeveloperProductNameDescriptionRequest`

See [Roblox.GameInternationalization.Api.UpdateDeveloperProductNameDescriptionRequest](#roblox-gameinternationalization-api-updatedeveloperproductnamedescriptionrequest) in Models.

**Request example:**
```json
{
  "name": "string",
  "description": "string"
}
```

**Responses:**

- `200`: OK → `Roblox.GameInternationalization.Api.UpdateDeveloperProductNameDescriptionResponse`
- `400`: 13: Request body can't be null 19: New name is null or whitespaces or new name/description is too long 20: New name or description is moderated 22: Invalid language code 26: You can't update translations for source language 53: Language is not supported for the game. 70: Invalid developer product id
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 18: You do not have permission to manage this game
- `500`: 0: An unknown error occurred.
- `503`: 17: Feature is disabled

**Response fields** (`Roblox.GameInternationalization.Api.UpdateDeveloperProductNameDescriptionResponse`)

See [Roblox.GameInternationalization.Api.UpdateDeveloperProductNameDescriptionResponse](#roblox-gameinternationalization-api-updatedeveloperproductnamedescriptionresponse) in Models.

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
curl -X PATCH -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://gameinternationalization.roblox.com/v1/developer-products/{DEVELOPERPRODUCTID}/name-description/language-codes/{LANGUAGECODE}" \
  -H "Content-Type: application/json" \
  -d '{
  "name": "string",
  "description": "string"
}'
```

### DELETE `/v1/developer-products/{developerProductId}/name-description/language-codes/{languageCode}`

Delete localized name and description of a developer product

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `developerProductId` | path | `integer (int64)` | Yes | The developer product id |
| `languageCode` | path | `string` | Yes | The language code of the name and description to delete |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: 22: Invalid language code 23: You can't delete translations for source language 53: Language is not supported for the game. 70: Invalid developer product id
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 18: You do not have permission to manage this game
- `500`: 0: An unknown error occurred.
- `503`: 17: Feature is disabled

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X DELETE -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://gameinternationalization.roblox.com/v1/developer-products/{DEVELOPERPRODUCTID}/name-description/language-codes/{LANGUAGECODE}"
```

### PATCH `/v1/developer-products/{developerProductId}/name/language-codes/{languageCode}`

Update localized name of a developer product

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `developerProductId` | path | `integer (int64)` | Yes | The developer product id |
| `languageCode` | path | `string` | Yes | The language code of the name to update |

**Request Body:** `application/json` — Type: `Roblox.GameInternationalization.Api.UpdateDeveloperProductNameRequest`

See [Roblox.GameInternationalization.Api.UpdateDeveloperProductNameRequest](#roblox-gameinternationalization-api-updatedeveloperproductnamerequest) in Models.

**Request example:**
```json
{
  "name": "string"
}
```

**Responses:**

- `200`: OK → `Roblox.GameInternationalization.Api.UpdateDeveloperProductNameResponse`
- `400`: 13: Request body can't be null 19: New name is null or whitespaces or new name/description is too long 20: New name or description is moderated 22: Invalid language code 26: You can't update translations for source language 53: Language is not supported for the game. 70: Invalid developer product id
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 18: You do not have permission to manage this game
- `500`: 0: An unknown error occurred.
- `503`: 17: Feature is disabled

**Response fields** (`Roblox.GameInternationalization.Api.UpdateDeveloperProductNameResponse`)

See [Roblox.GameInternationalization.Api.UpdateDeveloperProductNameResponse](#roblox-gameinternationalization-api-updatedeveloperproductnameresponse) in Models.

**Response example:**
```json
{
  "name": "string"
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X PATCH -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://gameinternationalization.roblox.com/v1/developer-products/{DEVELOPERPRODUCTID}/name/language-codes/{LANGUAGECODE}" \
  -H "Content-Type: application/json" \
  -d '{
  "name": "string"
}'
```

### PATCH `/v1/game-passes/{gamePassId}/description/language-codes/{languageCode}`

Update localized description of a game pass

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gamePassId` | path | `integer (int64)` | Yes | The game pass id |
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
curl -X PATCH -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://gameinternationalization.roblox.com/v1/game-passes/{GAMEPASSID}/description/language-codes/{LANGUAGECODE}" \
  -H "Content-Type: application/json" \
  -d '{
  "description": "string"
}'
```

### PATCH `/v1/game-passes/{gamePassId}/name-description/language-codes/{languageCode}`

Update localized name and description of a game pass

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gamePassId` | path | `integer (int64)` | Yes | The game pass id |
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
curl -X PATCH -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://gameinternationalization.roblox.com/v1/game-passes/{GAMEPASSID}/name-description/language-codes/{LANGUAGECODE}" \
  -H "Content-Type: application/json" \
  -d '{
  "name": "string",
  "description": "string"
}'
```

### DELETE `/v1/game-passes/{gamePassId}/name-description/language-codes/{languageCode}`

Delete localized name and description of a game pass

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gamePassId` | path | `integer (int64)` | Yes | The game pass id |
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
curl -X DELETE -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://gameinternationalization.roblox.com/v1/game-passes/{GAMEPASSID}/name-description/language-codes/{LANGUAGECODE}"
```

### PATCH `/v1/game-passes/{gamePassId}/name/language-codes/{languageCode}`

Update localized name of a game pass

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gamePassId` | path | `integer (int64)` | Yes | The game pass id |
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
curl -X PATCH -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://gameinternationalization.roblox.com/v1/game-passes/{GAMEPASSID}/name/language-codes/{LANGUAGECODE}" \
  -H "Content-Type: application/json" \
  -d '{
  "name": "string"
}'
```

### PATCH `/v1/localizationtable/gametables/{gameId}`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gameId` | path | `integer (int64)` | Yes |  |

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
curl -X PATCH -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
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

### PATCH `/v1/supported-languages/games/{gameId}/languages/{languageCode}/automatic-translation-status`

Enable or disable automatic translation for a game and language.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gameId` | path | `integer (int64)` | Yes | The id of the game. |
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
curl -X PATCH -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://gameinternationalization.roblox.com/v1/supported-languages/games/{GAMEID}/languages/{LANGUAGECODE}/automatic-translation-status" \
  -H "Content-Type: application/json" \
  -d 'false'
```

### PATCH `/v1/supported-languages/games/{gameId}/languages/{languageCode}/image-translation-status`

Enable or disable image translation for a game and language.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gameId` | path | `integer (int64)` | Yes | The id of the game. |
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
curl -X PATCH -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://gameinternationalization.roblox.com/v1/supported-languages/games/{GAMEID}/languages/{LANGUAGECODE}/image-translation-status" \
  -H "Content-Type: application/json" \
  -d 'false'
```

### PATCH `/v1/supported-languages/games/{gameId}/languages/{languageCode}/universe-display-info-automatic-translation-settings`

Update the switch which controls if the UniverseDisplayInformation should be automatically translated.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gameId` | path | `integer (int64)` | Yes | The game id. |
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
curl -X PATCH -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://gameinternationalization.roblox.com/v1/supported-languages/games/{GAMEID}/languages/{LANGUAGECODE}/universe-display-info-automatic-translation-settings" \
  -H "Content-Type: application/json" \
  -d 'false'
```

### DELETE `/v1/game-thumbnails/games/{gameId}/language-codes/{languageCode}/images/{imageId}`

Deletes the game thumbnail.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gameId` | path | `integer (int64)` | Yes | The game identifier. |
| `languageCode` | path | `string` | Yes | The language code. |
| `imageId` | path | `integer (int64)` | Yes | The image identifier. |

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
curl -X DELETE -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://gameinternationalization.roblox.com/v1/game-thumbnails/games/{GAMEID}/language-codes/{LANGUAGECODE}/images/{IMAGEID}"
```

## Models

### Roblox.GameInternationalization.Api.AssociateLocalizationTablesToGameRequest

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `tables` | `Roblox.GameInternationalization.Api.LocalizationTableGameAssociation[]` | No |  |

### Roblox.GameInternationalization.Api.AssociateLocalizationTablesToGameResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | `boolean` | No |  |

### Roblox.GameInternationalization.Api.AutoLocalizationMetadataResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `isReactVersionEnabledForAutoLocalizationSettings` | `boolean` | No | Is React Implementation of AutoLocalization Settings Enabled |
| `isTabbedUIEnabledForConfigureLocalizationPage` | `boolean` | No | Is Tabbed UI Enabled for Configure Localization Page |
| `isAutomaticTranslationToggleUIEnabled` | `boolean` | No | Is Toggle UI Enabled for Automatic Translations |
| `isAutomaticTranslationQuotaUIEnabled` | `boolean` | No | Is Quota UI Enabled for Automatic Translations |

### Roblox.GameInternationalization.Api.AutomaticTranslationStatusTargetLanguage

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `languageCode` | `string` | No | The language code. |
| `isAutomaticTranslationAllowed` | `boolean` | No | Indicates whether or not automatic translation is allowed for the target language. |

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

### Roblox.GameInternationalization.Api.FailedNameDescription

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `languageCode` | `string` | No |  |
| `errorCode` | `integer` | No |  |

### Roblox.GameInternationalization.Api.GameAutolocalizationInformationResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `isAutolocalizationEnabled` | `boolean` | No |  |
| `shouldUseLocalizationTable` | `boolean` | No |  |
| `shouldUseImageLocalizationTable` | `boolean` | No |  |
| `isAutoLocalizationForImageEnabled` | `boolean` | No |  |
| `autoLocalizationTableId` | `string` | No |  |
| `assetId` | `integer` | No |  |

### Roblox.GameInternationalization.Api.GetAllowedAutomaticTranslationStatusForLanguagesResponse

A response model for getting the automatic translation allowed status of target languages.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `sourceLanguage` | `string` | No | The source language. |
| `targetLanguages` | `Roblox.GameInternationalization.Api.AutomaticTranslationStatusTargetLanguage[]` | No | The target languages with the automatic translation allowed status. The status basically says if automatic translation can be enabled for the source and target. |

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

### Roblox.GameInternationalization.Api.GetBadgeIconResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `imageId` | `string` | No |  |
| `imageUrl` | `string` | No |  |
| `state` | `Approved \| PendingReview \| UnAvailable \| Rejected \| Error` | No | Enum for image status. |
| `languageCode` | `string` | No |  |

### Roblox.GameInternationalization.Api.GetDeveloperProductIconResponse

A response model for getting developer product icon

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `imageId` | `string` | No |  |
| `imageUrl` | `string` | No |  |
| `state` | `Approved \| PendingReview \| UnAvailable \| Rejected \| Error` | No | Enum for image status. |
| `languageCode` | `string` | No |  |

### Roblox.GameInternationalization.Api.GetGameIconResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `imageId` | `string` | No |  |
| `imageUrl` | `string` | No |  |
| `state` | `Approved \| PendingReview \| UnAvailable \| Rejected \| Error` | No | Enum for image status. |
| `languageCode` | `string` | No |  |

### Roblox.GameInternationalization.Api.GetGamePassIconResponse

A response model for getting game pass icon

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `imageId` | `string` | No |  |
| `imageUrl` | `string` | No |  |
| `state` | `Approved \| PendingReview \| UnAvailable \| Rejected \| Error` | No | Enum for image status. |
| `languageCode` | `string` | No |  |

### Roblox.GameInternationalization.Api.GetGameThumbnailsResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `languageCode` | `string` | No |  |
| `mediaAssets` | `Roblox.GameInternationalization.Api.MediaAssetResponse[]` | No |  |

### Roblox.GameInternationalization.Api.GetNameDescriptionHistoryResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `history` | `Roblox.GameInternationalization.Api.TranslationHistory[]` | No |  |
| `lastEvaluatedId` | `string` | No |  |

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

### Roblox.GameInternationalization.Api.GetTranslationCountsForGameResponse

A response model that contains game info for getting a translation count.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `gameId` | `integer` | No | The game id. |
| `languagesOrLocales` | `Roblox.GameInternationalization.Api.TranslationCountLanguageOrLocaleResponse[]` | No | The list of languages/locales of the game. |

### Roblox.GameInternationalization.Api.GetTranslationCountsForLanguageOrLocaleResponse

A response model for getting translation counts for a language or locale.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `languageOrLocaleCode` | `string` | No | The code of the language or locale. |
| `languageOrLocaleType` | `Language \| Locale` | No | An indicator that says whether the passed in language/locale code represents a language or locale. |
| `games` | `Roblox.GameInternationalization.Api.TranslationCountGameInfoResponse[]` | No | Info for the requested games, including their translation counts for the specified language or locale. |

### Roblox.GameInternationalization.Api.GetUiConfigurationsResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `isGameProductsEnabled` | `boolean` | No | Game products translation management page is enabled or not. |
| `isBadgeIconEnabled` | `boolean` | No | Badge Icon translation management is enabled or not. |
| `isGamePassEnabled` | `boolean` | No | Game pass translation management is enabled or not. |
| `isDeveloperProductEnabled` | `boolean` | No | Developer product translation management is enabled or not. |

### Roblox.GameInternationalization.Api.Language

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | `string` | No |  |
| `nativeName` | `string` | No |  |
| `languageCode` | `string` | No |  |

### Roblox.GameInternationalization.Api.LanguageOrLocale

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | `string` | No |  |
| `languageCodeType` | `Language \| Locale` | No | An enum to distinguish between locale codes and language codes. |
| `languageCode` | `string` | No |  |

### Roblox.GameInternationalization.Api.LanguageOrLocaleSettings

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `languageCodeType` | `Language \| Locale` | No | The language code type. |
| `languageCode` | `string` | No | The language code. |
| `isAutomaticTranslationEnabled` | `boolean` | No | Indicates whether or not automatic translation is currently enabled for the game and language. |
| `isImageTranslationEnabled` | `boolean` | No | Indicates whether image translation is currently enabled for the game and language. |

### Roblox.GameInternationalization.Api.LocalizationTableGameAssociation

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | `string` | No |  |
| `dissociate` | `boolean` | No |  |

### Roblox.GameInternationalization.Api.MediaAssetResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `mediaAssetId` | `string` | No |  |
| `mediaAssetAltText` | `string` | No |  |
| `state` | `Approved \| PendingReview \| UnAvailable \| Rejected \| Error` | No | Enum for image status. |
| `mediaAssetUrl` | `string` | No |  |

### Roblox.GameInternationalization.Api.Models.Request.SetUserLocalizationSettingsRequest

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `settingValue` | `Roblox.GameLocalization.Client.UserUniverseLocalizationSettingValue` | No |  |

### Roblox.GameInternationalization.Api.Models.Response.GameNameDescriptionMetadataResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `isNameDescriptionMigrationEnabled` | `boolean` | No |  |

### Roblox.GameInternationalization.Api.Models.Response.GetPlayerChoiceUniverseSettingsResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `IsPlayerChoiceEnabled` | `boolean` | No | Checks whether player choice warning should be displayed to users. |

### Roblox.GameInternationalization.Api.Models.Response.GetUserLocalizationSettingsForUniverseResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `userUniverseLocalizationSettingValue` | `Roblox.GameLocalization.Client.UserUniverseLocalizationSettingValue` | No |  |

### Roblox.GameInternationalization.Api.Models.Response.UploadImageForGameThumbnailResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `mediaAssetId` | `string` | No |  |

### Roblox.GameInternationalization.Api.MonthlyQuotaModel

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `previousRefreshDate` | `string` | No |  |
| `nextRefreshDate` | `string` | No |  |
| `remaining` | `integer` | No |  |
| `capacity` | `integer` | No |  |

### Roblox.GameInternationalization.Api.NameDescription

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | `string` | No |  |
| `description` | `string` | No |  |
| `updateType` | `Invalid \| Name \| Description` | No |  |
| `languageCode` | `string` | No |  |

### Roblox.GameInternationalization.Api.PatchLanguage

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `languageCodeType` | `Language \| Locale` | No | The language code type. |
| `languageCode` | `string` | No | The language code for the language to edit. |
| `delete` | `boolean` | No | An optional field used to indicate whether a language should be deleted from this game's list of supported languages. |

### Roblox.GameInternationalization.Api.QuotaModel

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `remaining` | `integer` | No |  |
| `capacity` | `integer` | No |  |

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

### Roblox.GameInternationalization.Api.SetAutolocalizationSettingsForGameRequest

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `isAutolocalizationEnabled` | `boolean` | No |  |
| `shouldUseLocalizationTable` | `boolean` | No |  |

### Roblox.GameInternationalization.Api.SetAutolocalizationTableForGameRequest

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `tableId` | `string` | No |  |

### Roblox.GameInternationalization.Api.SortImageIdsRequest

A request model for sorting of image Ids for game thumbnails

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `mediaAssetIds` | `integer[]` | No | List of thumbnail ids in desired order. |

### Roblox.GameInternationalization.Api.SourceLanguageWithLocales

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `languageFamily` | `Roblox.GameInternationalization.Api.Language` | No |  |
| `defaultLocale` | `Roblox.Localization.Client.SupportedLocale` | No |  |
| `childLocales` | `Roblox.Localization.Client.SupportedLocale[]` | No |  |

### Roblox.GameInternationalization.Api.SupportedLanguagesMetadataResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `isFeatureEnabled` | `boolean` | No |  |
| `areAllLanguagesEnabled` | `boolean` | No |  |
| `minimumUniverseIdForFeature` | `integer` | No |  |
| `isHumanTranslationProgressUIEnabled` | `boolean` | No | Is translation progress for human translations enabled on UI |
| `isAutomaticTranslationProgressUIEnabled` | `boolean` | No | Is translation progress for automatic translations enabled on UI |
| `isSupportedLanguagesChildLocalesUIEnabled` | `boolean` | No | Is Language Locales UI Enabled for Supported Languages |

### Roblox.GameInternationalization.Api.TranslationAnalyticsMetadataResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `isFeatureEnabledOnUI` | `boolean` | No | Is Translation Analytics feature enabled on UI |
| `reportRequestPollingIntervalSeconds` | `integer` | No | Number of seconds to poll the server for report availability |
| `minimumDateTimeForAnalyticsReport` | `string` | No | Date-Time since the Analytics Reports can be downloaded |

### Roblox.GameInternationalization.Api.TranslationCount

A model that contains the count value of a translation count and relevant metadata.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `count` | `integer` | No |  |
| `translationStatus` | `Approved` | No | The enum representing a translation status. |
| `translatorType` | `Automation \| User` | No | Gets or sets the type of the translator associated with the count, or `null` if the count is not associated with a specific type of translator. |

### Roblox.GameInternationalization.Api.TranslationCountCategoryInfoResponse

A response model that contains category info for getting a translation count.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `category` | `InGameContent` | No | The category of the translation counts. |
| `translationCounts` | `Roblox.GameInternationalization.Api.TranslationCount[]` | No | The translation counts. |
| `totalTranslatableItemCount` | `integer` | No | The total number of translatable items. The translation count percentage can be calculated by doing translationCounts / totalTranslatableItemCount. |

### Roblox.GameInternationalization.Api.TranslationCountGameInfoResponse

A response model that contains game info for getting a translation count.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `gameId` | `integer` | No | The game id. |
| `status` | `string enum (7 values)` | No | The status of the response for the requested game. Values: LanguageOrLocaleSupportedForGame, LanguageOrLocaleNotSupportedForGame, LanguageOrLocaleIsSource, InsufficientPermission, GameDoesNotExist, GameDoesNotHaveTable, UnknownError |
| `categories` | `Roblox.GameInternationalization.Api.TranslationCountCategoryInfoResponse[]` | No | Categories of translation counts. |

### Roblox.GameInternationalization.Api.TranslationCountLanguageOrLocaleResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `status` | `Success \| LanguageOrLocaleNotSupportedForGame` | No | The status of the response for the requested game. |
| `categories` | `Roblox.GameInternationalization.Api.TranslationCountCategoryInfoResponse[]` | No | Categories of translation counts. |
| `name` | `string` | No |  |
| `languageCodeType` | `Language \| Locale` | No | An enum to distinguish between locale codes and language codes. |
| `languageCode` | `string` | No |  |

### Roblox.GameInternationalization.Api.TranslationHistory

A model containing a translation, translator, and translation time.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `translationText` | `string` | No | The translation provided by the translator. |
| `translator` | `Roblox.GameInternationalization.Api.Translator` | No |  |
| `created` | `string` | No | The time the translation was provided. |

### Roblox.GameInternationalization.Api.Translator

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | `integer` | No |  |
| `agentType` | `User \| Automation` | No | ['User' = 0, 'Automation' = 1] |

### Roblox.GameInternationalization.Api.UniverseDisplayInfoAutomaticTranslationSettings

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `languageCode` | `string` | No | The language code. |
| `isUniverseDisplayInfoAutomaticTranslationEnabled` | `boolean` | No | Indicates whether or not automatic translation is currently enabled for Game and Place Information for a game and language. |

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

### Roblox.GameInternationalization.Api.UpdateDeveloperProductDescriptionRequest

A request model for updating developer product description

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `description` | `string` | No | Developer product description |

### Roblox.GameInternationalization.Api.UpdateDeveloperProductDescriptionResponse

A response model for updating developer product description

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `description` | `string` | No | Developer product description saved |

### Roblox.GameInternationalization.Api.UpdateDeveloperProductNameDescriptionRequest

A request model for updating developer product name and description

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | `string` | No | Developer product name |
| `description` | `string` | No | Developer product description |

### Roblox.GameInternationalization.Api.UpdateDeveloperProductNameDescriptionResponse

A response model for updating developer product name and description

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | `string` | No | Developer product name saved |
| `description` | `string` | No | Developer product description saved |

### Roblox.GameInternationalization.Api.UpdateDeveloperProductNameRequest

A request model for updating developer product name

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | `string` | No | Developer product name |

### Roblox.GameInternationalization.Api.UpdateDeveloperProductNameResponse

A response model for updating developer product name

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | `string` | No | Developer product name saved |

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

### Roblox.GameInternationalization.Api.UpdateNameDescriptionsRequest

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | `Roblox.GameInternationalization.Api.NameDescription[]` | No |  |

### Roblox.GameInternationalization.Api.UpdateNameDescriptionsResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `successOperations` | `Roblox.GameInternationalization.Api.NameDescription[]` | No |  |
| `failedOperations` | `Roblox.GameInternationalization.Api.FailedNameDescription[]` | No |  |

### Roblox.GameInternationalization.Api.UpdateThumbnailAltTextRequest

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `thumbnailId` | `integer` | No |  |
| `altText` | `string` | No |  |

### Roblox.GameInternationalization.Api.UpdateUniverseDisplayInfoAutomaticTranslationSettingsResponse

A response model for getting the automatic translation allowed status for game information.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `gameId` | `integer` | No | The game id. |
| `languageCode` | `string` | No | The language code. |
| `isUniverseDisplayInfoAutomaticTranslationEnabled` | `boolean` | No | Indicates universeDisplayInformation automatic translation is enabled. |

### Roblox.GameLocalization.Client.UserUniverseLocalizationSettingValue

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `settingType` | `LanguageFamily \| SupportedLocale \| SourceOrTranslation` | No | ['LanguageFamily' = 0, 'SupportedLocale' = 1, 'SourceOrTranslation' = 2] |
| `settingTargetId` | `integer` | No |  |
| `settingTargetCode` | `string` | No |  |

### Roblox.Localization.Client.LanguageFamily

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | `integer` | No |  |
| `name` | `string` | No |  |
| `nativeName` | `string` | No |  |
| `languageCode` | `string` | No |  |
| `isRightToLeft` | `boolean` | No |  |

### Roblox.Localization.Client.SupportedLocale

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | `integer` | No |  |
| `locale` | `string enum (51 values)` | No |  Values: en_us, es_es, fr_fr, id_id, it_it, ja_jp, ko_kr, ru_ru, th_th, tr_tr, vi_vn, pt_br, de_de, zh_cn, zh_tw, bg_bg, bn_bd, cs_cz, da_dk, el_gr, et_ee, fi_fi, hi_in, hr_hr, hu_hu, ka_ge, kk_kz, km_kh, lt_lt, lv_lv, ms_my, my_mm, nb_no, nl_nl, fil_ph, pl_pl, ro_ro, uk_ua, si_lk, sk_sk, sl_sl, sq_al, bs_ba, sr_rs, sv_se, zh_cjv, ar_001, en_gb, pt_pt, es_mx, fr_ca |
| `localeCode` | `string` | No |  |
| `name` | `string` | No |  |
| `nativeName` | `string` | No |  |
| `language` | `Roblox.Localization.Client.LanguageFamily` | No |  |

### Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.GameInternationalization.Api.GetBadgeIconResponse]

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | `Roblox.GameInternationalization.Api.GetBadgeIconResponse[]` | No |  |

### Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.GameInternationalization.Api.GetDeveloperProductIconResponse]

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | `Roblox.GameInternationalization.Api.GetDeveloperProductIconResponse[]` | No |  |

### Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.GameInternationalization.Api.GetGameIconResponse]

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | `Roblox.GameInternationalization.Api.GetGameIconResponse[]` | No |  |

### Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.GameInternationalization.Api.GetGamePassIconResponse]

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | `Roblox.GameInternationalization.Api.GetGamePassIconResponse[]` | No |  |

### Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.GameInternationalization.Api.GetGameThumbnailsResponse]

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | `Roblox.GameInternationalization.Api.GetGameThumbnailsResponse[]` | No |  |

### Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.GameInternationalization.Api.LanguageOrLocaleSettings]

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | `Roblox.GameInternationalization.Api.LanguageOrLocaleSettings[]` | No |  |

### Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.GameInternationalization.Api.LanguageOrLocale]

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | `Roblox.GameInternationalization.Api.LanguageOrLocale[]` | No |  |

### Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.GameInternationalization.Api.NameDescription]

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | `Roblox.GameInternationalization.Api.NameDescription[]` | No |  |

### Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.GameInternationalization.Api.UniverseDisplayInfoAutomaticTranslationSettings]

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | `Roblox.GameInternationalization.Api.UniverseDisplayInfoAutomaticTranslationSettings[]` | No |  |