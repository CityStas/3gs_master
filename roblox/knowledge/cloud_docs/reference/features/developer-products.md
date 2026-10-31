---
name: "Developer products"
last_updated: 2026-10-30T19:56:08Z
type: feature
api_base_url: "https://apis.roblox.com"
endpoints: 21
auth: [api-key, oauth2, cookie]
description: "Create and manage developer products for repeatable in-experience purchases like in-game currency, consumables, or temporary boosts"
---

# Developer products

Create and manage developer products for repeatable in-experience purchases like in-game currency, consumables, or temporary boosts. [Create](#DeveloperProducts_CreateDeveloperProductV2) and [update](#DeveloperProducts_UpdateDeveloperProductV2) products with custom icons and pricing, and [add localized names and descriptions](#patch_legacy_game_internationalization_v1_developer_products__developerProductId__description_language_codes__languageCode_) for different languages.

> **See also:** To game passes (permanent unlocks), see [game-passes](/docs/cloud/reference/features/game-passes.md).

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

### POST `/developer-products/v2/universes/{universeId}/developer-products` [BETA]

Create developer product

Creates a new developer product with the provided configuration details.

**Auth:** Cookie (`.ROBLOSECURITY`) or API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `developer-product:write`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer` | Yes | The universe ID. |

**Request Body:** `multipart/form-data` — Type: `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | `string` | Yes | The name of the developer product. |
| `description` | `string` | No | The description of the developer product. |
| `isForSale` | `boolean` | No | Whether the developer product should be on sale. |
| `price` | `integer` | No | The default price of the developer product. |
| `imageFile` | `string` | No | The thumbnail image file to be uploaded. |
| `isRegionalPricingEnabled` | `boolean` | No | Whether regional pricing should be enabled for the developer product. |
| `isManagedPricingEnabled` | `boolean` | No | Whether managed pricing should be enabled for the developer product. |

**Request example:**
```json
{
  "name": "string",
  "description": "string",
  "isForSale": false,
  "price": 0,
  "imageFile": "string",
  "isRegionalPricingEnabled": false
}
```

**Responses:**

- `200`: Success → `DeveloperProductConfigV2`
- `400`: Bad Request → `ErrorResponse`
- `401`: Unauthorized → `ErrorResponse`
- `403`: Forbidden → `ErrorResponse`
- `404`: Not Found → `ErrorResponse`

**Response fields** (`DeveloperProductConfigV2`)

See [DeveloperProductConfigV2](#developerproductconfigv2) in Models.

**Response example:**
```json
{
  "productId": 0,
  "name": "string",
  "description": "string",
  "iconImageAssetId": 0,
  "universeId": 0,
  "isForSale": false
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 3/second, perOauth2Authorization: 3/second

**Example:**
```bash
curl -X POST -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/developer-products/v2/universes/{UNIVERSEID}/developer-products" \
  -F "name=string" \
  -F "description=string" \
  -F "isForSale=false" \
  -F "price=0" \
  -F "imageFile=@file.bin;type=application/octet-stream" \
  -F "isRegionalPricingEnabled=false" \
  -F "isManagedPricingEnabled=false"
```

### GET `/developer-products/v2/universes/{universeId}/developer-products/creator` [BETA]

List developer products by universe with configuration details

**Auth:** Cookie (`.ROBLOSECURITY`) or API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `developer-product:read`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer` | Yes | The universe ID. |
| `pageSize` | query | `integer` | No | The number of results to return. Defaults to 50. |
| `pageToken` | query | `string` | No | The cursor token for pagination. |

**Responses:**

- `200`: Success → `ListDeveloperProductConfigsV2Response`
- `400`: Bad Request → `ErrorResponse`
- `401`: Unauthorized → `ErrorResponse`
- `403`: Forbidden → `ErrorResponse`
- `404`: Not Found → `ErrorResponse`

**Response fields** (`ListDeveloperProductConfigsV2Response`)

See [ListDeveloperProductConfigsV2Response](#listdeveloperproductconfigsv2response) in Models.

**Response example:**
```json
{
  "developerProducts": [
    {
      "productId": "...",
      "name": "...",
      "description": "...",
      "iconImageAssetId": "...",
      "universeId": "...",
      "isForSale": "..."
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
  "https://apis.roblox.com/developer-products/v2/universes/{UNIVERSEID}/developer-products/creator"
```

### PATCH `/developer-products/v2/universes/{universeId}/developer-products/{productId}` [BETA]

Update developer product

Updates a developer product with the provided configuration details. 
Note that only fields provided in the request will be updated.

**Auth:** Cookie (`.ROBLOSECURITY`) or API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `developer-product:write`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer` | Yes | The universe ID. |
| `productId` | path | `integer` | Yes | The product ID of the developer product. |

**Request Body:** `multipart/form-data` — Type: `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | `string` | No | The name of the developer product. |
| `description` | `string` | No | The description of the developer product. |
| `isForSale` | `boolean` | No | Whether the developer product should be on sale. |
| `price` | `integer` | No | The default price of the developer product. |
| `imageFile` | `string` | No | The thumbnail image file to be uploaded. |
| `isRegionalPricingEnabled` | `boolean` | No | Whether regional pricing should be enabled for the developer product. |
| `storePageEnabled` | `boolean` | No | Whether the developer product should be available for purchase on the external store page. |
| `isManagedPricingEnabled` | `boolean` | No | Whether managed pricing should be enabled for the developer product. |

**Request example:**
```json
{
  "name": "string",
  "description": "string",
  "isForSale": false,
  "price": 0,
  "imageFile": "string",
  "isRegionalPricingEnabled": false
}
```

**Responses:**

- `204`: No Content
- `400`: Bad Request → `ErrorResponse`
- `401`: Unauthorized → `ErrorResponse`
- `403`: Forbidden → `ErrorResponse`
- `404`: Not Found → `ErrorResponse`
- `409`: Conflict → `ErrorResponse`

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 3/second, perOauth2Authorization: 3/second

**Example:**
```bash
curl -X PATCH -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/developer-products/v2/universes/{UNIVERSEID}/developer-products/{PRODUCTID}" \
  -F "name=string" \
  -F "description=string" \
  -F "isForSale=false" \
  -F "price=0" \
  -F "imageFile=@file.bin;type=application/octet-stream" \
  -F "isRegionalPricingEnabled=false" \
  -F "storePageEnabled=false" \
  -F "isManagedPricingEnabled=false"
```

### GET `/developer-products/v2/universes/{universeId}/developer-products/{productId}/creator` [BETA]

Get developer product with configuration details

**Auth:** Cookie (`.ROBLOSECURITY`) or API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `developer-product:read`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer` | Yes | The universe ID. |
| `productId` | path | `integer` | Yes | The product ID of the developer product. |

**Responses:**

- `200`: Success → `DeveloperProductConfigV2`
- `401`: Unauthorized → `ErrorResponse`
- `403`: Forbidden → `ErrorResponse`
- `404`: Not Found → `ErrorResponse`

**Response fields** (`DeveloperProductConfigV2`)

See [DeveloperProductConfigV2](#developerproductconfigv2) in Models.

**Response example:**
```json
{
  "productId": 0,
  "name": "string",
  "description": "string",
  "iconImageAssetId": 0,
  "universeId": 0,
  "isForSale": false
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 10/second, perOauth2Authorization: 10/second

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/developer-products/v2/universes/{UNIVERSEID}/developer-products/{PRODUCTID}/creator"
```

### PATCH `/legacy-game-internationalization/v1/developer-products/{developerProductId}/description/language-codes/{languageCode}` [EXPERIMENTAL]

Update localized description of a developer product

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `legacy-developer-product:manage`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `developerProductId` | path | `integer` | Yes | The developer product id |
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

**Rate Limits:** perApiKeyOwner: 100/minute, perOauth2Authorization: 100/minute

**Example:**
```bash
curl -X PATCH -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/legacy-game-internationalization/v1/developer-products/{DEVELOPERPRODUCTID}/description/language-codes/{LANGUAGECODE}" \
  -H "Content-Type: application/json" \
  -d '{
  "description": "string"
}'
```

### GET `/legacy-game-internationalization/v1/developer-products/{developerProductId}/icons` [EXPERIMENTAL]

Get all icons for a developer product

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `legacy-developer-product:manage`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `developerProductId` | path | `integer` | Yes | The id of the developer product |
| `width` | query | `integer` | No | The width of the icon to request |
| `height` | query | `integer` | No | The height of the icon to request |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.GameInternationalization.Api.GetDeveloperProductIconResponse_`
- `400`: 52: Image dimensions are invalid 70: Invalid developer product id
- `401`: 0: Authorization has been denied for this request.
- `500`: 0: An unknown error occurred.
- `503`: 17: Feature is disabled

**Response fields** (`Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.GameInternationalization.Api.GetDeveloperProductIconResponse_`)

See [Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.GameInternationalization.Api.GetDeveloperProductIconResponse_](#roblox-web-webapi-models-apiarrayresponse-roblox-gameinternationalization-api-getdeveloperproducticonresponse-) in Models.

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
  "https://apis.roblox.com/legacy-game-internationalization/v1/developer-products/{DEVELOPERPRODUCTID}/icons"
```

### POST `/legacy-game-internationalization/v1/developer-products/{developerProductId}/icons/language-codes/{languageCode}` [EXPERIMENTAL]

Update a developer product's icon

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `legacy-developer-product:manage`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `developerProductId` | path | `integer` | Yes | The id of the developer product |
| `languageCode` | path | `string` | Yes | The language code of this icon to update |

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

**Rate Limits:** perApiKeyOwner: 100/minute, perOauth2Authorization: 100/minute

**Example:**
```bash
curl -X POST -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/legacy-game-internationalization/v1/developer-products/{DEVELOPERPRODUCTID}/icons/language-codes/{LANGUAGECODE}" \
  -H "Content-Type: application/json" \
  -d '{"key": "value"}'
```

### DELETE `/legacy-game-internationalization/v1/developer-products/{developerProductId}/icons/language-codes/{languageCode}` [EXPERIMENTAL]

Delete a localized icon from a developer product

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `legacy-developer-product:manage`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `developerProductId` | path | `integer` | Yes | The id of the developer product |
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

**Rate Limits:** perApiKeyOwner: 100/minute, perOauth2Authorization: 100/minute

**Example:**
```bash
curl -X DELETE -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/legacy-game-internationalization/v1/developer-products/{DEVELOPERPRODUCTID}/icons/language-codes/{LANGUAGECODE}"
```

### GET `/legacy-game-internationalization/v1/developer-products/{developerProductId}/name-description` [EXPERIMENTAL]

Get all names and descriptions of a developer product

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `legacy-developer-product:manage`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `developerProductId` | path | `integer` | Yes | The developer product Id |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.GameInternationalization.Api.NameDescription_`
- `400`: 70: Invalid developer product id
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
  "https://apis.roblox.com/legacy-game-internationalization/v1/developer-products/{DEVELOPERPRODUCTID}/name-description"
```

### PATCH `/legacy-game-internationalization/v1/developer-products/{developerProductId}/name-description/language-codes/{languageCode}` [EXPERIMENTAL]

Update localized name and description of a developer product

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `legacy-developer-product:manage`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `developerProductId` | path | `integer` | Yes | The developer product id |
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

**Rate Limits:** perApiKeyOwner: 100/minute, perOauth2Authorization: 100/minute

**Example:**
```bash
curl -X PATCH -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/legacy-game-internationalization/v1/developer-products/{DEVELOPERPRODUCTID}/name-description/language-codes/{LANGUAGECODE}" \
  -H "Content-Type: application/json" \
  -d '{
  "name": "string",
  "description": "string"
}'
```

### DELETE `/legacy-game-internationalization/v1/developer-products/{developerProductId}/name-description/language-codes/{languageCode}` [EXPERIMENTAL]

Delete localized name and description of a developer product

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `legacy-developer-product:manage`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `developerProductId` | path | `integer` | Yes | The developer product id |
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

**Rate Limits:** perApiKeyOwner: 100/minute, perOauth2Authorization: 100/minute

**Example:**
```bash
curl -X DELETE -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/legacy-game-internationalization/v1/developer-products/{DEVELOPERPRODUCTID}/name-description/language-codes/{LANGUAGECODE}"
```

### PATCH `/legacy-game-internationalization/v1/developer-products/{developerProductId}/name/language-codes/{languageCode}` [EXPERIMENTAL]

Update localized name of a developer product

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `legacy-developer-product:manage`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `developerProductId` | path | `integer` | Yes | The developer product id |
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

**Rate Limits:** perApiKeyOwner: 100/minute, perOauth2Authorization: 100/minute

**Example:**
```bash
curl -X PATCH -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/legacy-game-internationalization/v1/developer-products/{DEVELOPERPRODUCTID}/name/language-codes/{LANGUAGECODE}" \
  -H "Content-Type: application/json" \
  -d '{
  "name": "string"
}'
```

### GET `/v1/developer-products/icons` [STABLE]

Thumbnails developer product icons.

**Server:** `https://thumbnails.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `developerProductIds` | query | `integer[]` | Yes | The developer product ids. |
| `size` | query | `150x150 \| 420x420` | No | The thumbnail size, formatted widthxheight Valid values: `150x150`, `420x420` |
| `format` | query | `Png \| Webp` | No | The thumbnail format Valid values: `Png`, `Webp` |
| `isCircular` | query | `true \| false` | No | The circle thumbnail output parameter, true or false Valid values: `true`, `false` |

**Responses:**

- `200`: OK
- `400`: 1: There are too many requested Ids. 2: The requested image format is invalid. Please see documentation for valid thumbnail format parameter name and values. 3: The requested size is invalid. Please see documentation for valid thumbnail size parameter name and format. 4: The requested Ids are invalid, of an invalid type or missing. 10: Circular thumbnail requests are not allowed

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://thumbnails.roblox.com/v1/developer-products/icons?developerProductIds={VALUE}"
```

### PATCH `/v1/developer-products/{developerProductId}/description/language-codes/{languageCode}` [EXPERIMENTAL]

Update localized description of a developer product

**Server:** `https://gameinternationalization.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `developerProductId` | path | `integer` | Yes | The developer product id |
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
curl -X PATCH -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://gameinternationalization.roblox.com/v1/developer-products/{DEVELOPERPRODUCTID}/description/language-codes/{LANGUAGECODE}" \
  -H "Content-Type: application/json" \
  -d '{
  "description": "string"
}'
```

### GET `/v1/developer-products/{developerProductId}/icons` [EXPERIMENTAL]

Get all icons for a developer product

**Server:** `https://gameinternationalization.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `developerProductId` | path | `integer` | Yes | The id of the developer product |
| `width` | query | `integer` | No | The width of the icon to request |
| `height` | query | `integer` | No | The height of the icon to request |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.GameInternationalization.Api.GetDeveloperProductIconResponse_`
- `400`: 52: Image dimensions are invalid 70: Invalid developer product id
- `401`: 0: Authorization has been denied for this request.
- `500`: 0: An unknown error occurred.
- `503`: 17: Feature is disabled

**Response fields** (`Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.GameInternationalization.Api.GetDeveloperProductIconResponse_`)

See [Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.GameInternationalization.Api.GetDeveloperProductIconResponse_](#roblox-web-webapi-models-apiarrayresponse-roblox-gameinternationalization-api-getdeveloperproducticonresponse-) in Models.

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
  "https://gameinternationalization.roblox.com/v1/developer-products/{DEVELOPERPRODUCTID}/icons"
```

### POST `/v1/developer-products/{developerProductId}/icons/language-codes/{languageCode}` [EXPERIMENTAL]

Update a developer product's icon

**Server:** `https://gameinternationalization.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `developerProductId` | path | `integer` | Yes | The id of the developer product |
| `languageCode` | path | `string` | Yes | The language code of this icon to update |

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
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://gameinternationalization.roblox.com/v1/developer-products/{DEVELOPERPRODUCTID}/icons/language-codes/{LANGUAGECODE}" \
  -H "Content-Type: application/json" \
  -d '{"key": "value"}'
```

### DELETE `/v1/developer-products/{developerProductId}/icons/language-codes/{languageCode}` [EXPERIMENTAL]

Delete a localized icon from a developer product

**Server:** `https://gameinternationalization.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `developerProductId` | path | `integer` | Yes | The id of the developer product |
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
curl -X DELETE -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://gameinternationalization.roblox.com/v1/developer-products/{DEVELOPERPRODUCTID}/icons/language-codes/{LANGUAGECODE}"
```

### GET `/v1/developer-products/{developerProductId}/name-description` [EXPERIMENTAL]

Get all names and descriptions of a developer product

**Server:** `https://gameinternationalization.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `developerProductId` | path | `integer` | Yes | The developer product Id |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.GameInternationalization.Api.NameDescription_`
- `400`: 70: Invalid developer product id
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
  "https://gameinternationalization.roblox.com/v1/developer-products/{DEVELOPERPRODUCTID}/name-description"
```

### PATCH `/v1/developer-products/{developerProductId}/name-description/language-codes/{languageCode}` [EXPERIMENTAL]

Update localized name and description of a developer product

**Server:** `https://gameinternationalization.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `developerProductId` | path | `integer` | Yes | The developer product id |
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
curl -X PATCH -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://gameinternationalization.roblox.com/v1/developer-products/{DEVELOPERPRODUCTID}/name-description/language-codes/{LANGUAGECODE}" \
  -H "Content-Type: application/json" \
  -d '{
  "name": "string",
  "description": "string"
}'
```

### DELETE `/v1/developer-products/{developerProductId}/name-description/language-codes/{languageCode}` [EXPERIMENTAL]

Delete localized name and description of a developer product

**Server:** `https://gameinternationalization.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `developerProductId` | path | `integer` | Yes | The developer product id |
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
curl -X DELETE -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://gameinternationalization.roblox.com/v1/developer-products/{DEVELOPERPRODUCTID}/name-description/language-codes/{LANGUAGECODE}"
```

### PATCH `/v1/developer-products/{developerProductId}/name/language-codes/{languageCode}` [EXPERIMENTAL]

Update localized name of a developer product

**Server:** `https://gameinternationalization.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `developerProductId` | path | `integer` | Yes | The developer product id |
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
curl -X PATCH -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://gameinternationalization.roblox.com/v1/developer-products/{DEVELOPERPRODUCTID}/name/language-codes/{LANGUAGECODE}" \
  -H "Content-Type: application/json" \
  -d '{
  "name": "string"
}'
```

## Models

### DeveloperProductConfigV2

Creator-facing representation of a developer product configuration.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `productId` | `integer` | Yes | The product ID of the developer product. |
| `name` | `string` | Yes | The name of the developer product. |
| `description` | `string` | Yes | The description of the developer product. |
| `iconImageAssetId` | `integer` | Yes | The icon image (thumbnail) asset ID of the developer product. |
| `universeId` | `integer` | Yes | The universe ID that the developer product belongs to. |
| `isForSale` | `boolean` | Yes | Whether the developer product is currently on sale. |
| `storePageEnabled` | `boolean` | No | Whether the developer product is currently available for purchase on the external store page. |
| `priceInformation` | `any` | Yes | The pricing configuration associated with the product. |
| `isImmutable` | `boolean` | Yes | Whether the developer product cannot be modified, such as when created as a commerce product. |
| `createdTimestamp` | `string` | Yes | The timestamp when the developer product was created. |
| `updatedTimestamp` | `string` | Yes | The timestamp when the developer product was last updated. |
| `isManagedPricingEnabled` | `boolean` | Yes | Whether managed pricing is enabled for the developer product. |

### ErrorResponse

This is the base class for all custom Exceptions that are thrown in this API.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `errorCode` | `any` | No | The ErrorCode for the exception. |
| `errorMessage` | `string` | No | The human readable error message. |
| `field` | `string` | No | The relevant field that caused the error. |
| `hint` | `string` | No | A hint as to what caused the error, if applicable. |

### ListDeveloperProductConfigsV2Response

Response that contains the list of developer products with their corresponding configuration details and pagination information.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `developerProducts` | `DeveloperProductConfigV2[]` | Yes | The list of developer products with their corresponding configuration details. |
| `nextPageToken` | `string` | Yes | The next page token. |

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

### Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.GameInternationalization.Api.GetDeveloperProductIconResponse_

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | `Roblox.GameInternationalization.Api.GetDeveloperProductIconResponse[]` | No |  |

### Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.GameInternationalization.Api.NameDescription_

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | `Roblox.GameInternationalization.Api.NameDescription[]` | No |  |

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