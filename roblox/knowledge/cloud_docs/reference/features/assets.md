---
name: "Assets"
last_updated: 2026-10-30T19:56:08Z
type: feature
api_base_url: "https://apis.roblox.com"
endpoints: 81
auth: [api-key, oauth2, cookie]
description: "Upload, update, and manage assets programmatically"
---

# Assets

Upload, update, and manage assets programmatically. Supported asset types include Audio, Decals, Images, Models, Meshes, and Videos. For detailed implementation, see the [Assets Usage Guide](/cloud/guides/usage-assets).

Common use cases include:

- Asset creation: [Create an asset](#Assets_CreateAsset), then [poll the operation endpoint](#Assets_GetOperation) for completion
- Asset retrieval: [Retrieve asset content](#get_asset_delivery_api_v1_assetId__assetId_) or [a specific version of it](#get_asset_delivery_api_v1_assetId__assetId__version__versionNumber_) for external tools
- Versioning: [Manage asset versions](#listAssetVersions) with [rollback](#Assets_RollbackAssetVersion) support

> **Getting started:** See [Usage guide for assets](/docs/en-us/cloud/guides/usage-assets.md) for a complete walkthrough with working examples.

> **See also:** To thumbnails for assets, see [thumbnails](/docs/cloud/reference/features/thumbnails.md).

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

### GET `/asset-delivery-api/v1/assetId/{assetId}`

Retrieves an asset by its ID with OpenCloud auth.

Returns an object containing a `location` property which is a temporary CDN URL for the asset content. All asset types are supported.
You should request that URL with the `Accept-Encoding: gzip` header and decompress the result if the response is gzipped. If you are using cURL, the `--compressed` flag will automate these steps for you.
This endpoint is expected to be called with API key authentication through `apis.roblox.com/asset-delivery-api/v1/assetId/{assetId}`.
While you are able to make requests to this endpoint with Cookie authentication via `assetdelivery.roblox.com/v1/openCloud/assetId/{assetId}`, we highly discourage use this way.
Expect unannounced removal of this second route in the future.

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `legacy-asset:manage`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `assetId` | path | `integer` | Yes | The ID of the asset to retrieve. |
| `Accept-Encoding` | header | `string` | No | The Accept-Encoding header value specifying compression formats (e.g., "gzip, deflate"). Defaults to "gzip, deflate" if not provided. |
| `Roblox-Place-Id` | header | `integer` | No | The Roblox-Place-Id header value identifying the place making the request. |
| `AssetType` | header | `string` | No | The AssetType header value specifying the expected asset type. |
| `AssetFormat` | header | `string` | No | The AssetFormat header value specifying the desired asset format. Overridden by robloxAssetFormat if both are provided. |
| `Roblox-AssetFormat` | header | `string` | No | The Roblox-AssetFormat header value specifying the preferred Roblox-specific asset format. Takes precedence over assetFormat. |
| `Roblox-Usage-Context` | header | `string` | No |  |
| `skipSigningScripts` | query | `boolean` | No | Whether to skip script signing for the returned asset. Used for script assets that don't require signing. |
| `clientInsert` | query | `integer` | No | Set to 1 to indicate this is a client insert request. |
| `scriptinsert` | query | `integer` | No | Set to 1 to indicate this is a script insert request. |
| `modulePlaceId` | query | `integer` | No | The place ID of the module making the request. |
| `serverplaceid` | query | `integer` | No | The server place ID making the request. |
| `expectedAssetType` | query | `string` | No | The expected asset type as a fallback when assetType header is not provided. |
| `doNotFallbackToBaselineRepresentation` | query | `boolean` | No | Whether to prevent fallback to baseline representation when specific content representations are not available. |
| `contentRepresentationPriorityList` | query | `string` | No | Base64URL-encoded JSON string specifying the priority list of desired content representations (format, version, fidelity). |
| `accessContext` | query | `string` | No |  |

**Responses:**

- `200`: OK
- `401`: 0: Authorization has been denied for this request.

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Rate Limits:** perApiKeyOwner: 1000/minute, perOauth2Authorization: 1000/minute

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/asset-delivery-api/v1/assetId/{ASSETID}"
```

### GET `/asset-delivery-api/v1/assetId/{assetId}/version/{versionNumber}`

Retrieves an asset by its ID and version number with OpenCloud auth.

Refer to the assetId endpoint for details on usage.
This endpoint is expected to be called with API key authentication through `apis.roblox.com/asset-delivery-api/v1/assetId/{assetId}/version/{versionNumber}`.
While you are able to make requests to this endpoint with Cookie authentication via `assetdelivery.roblox.com/v1/openCloud/assetId/{assetId}/version/{versionNumber}`, we highly discourage use this way.
Expect unannounced removal of this second route in the future.

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `legacy-asset:manage`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `assetId` | path | `integer` | Yes | The ID of the asset to retrieve. |
| `versionNumber` | path | `integer` | Yes | The version number of the asset to retrieve. |
| `Accept-Encoding` | header | `string` | No |  |
| `Roblox-Place-Id` | header | `integer` | No |  |
| `AssetType` | header | `string` | No |  |
| `AssetFormat` | header | `string` | No |  |
| `Roblox-AssetFormat` | header | `string` | No |  |
| `Roblox-Usage-Context` | header | `string` | No |  |
| `skipSigningScripts` | query | `boolean` | No |  |
| `clientInsert` | query | `integer` | No |  |
| `scriptinsert` | query | `integer` | No |  |
| `modulePlaceId` | query | `integer` | No |  |
| `serverplaceid` | query | `integer` | No |  |
| `expectedAssetType` | query | `string` | No |  |
| `doNotFallbackToBaselineRepresentation` | query | `boolean` | No |  |
| `contentRepresentationPriorityList` | query | `string` | No |  |
| `accessContext` | query | `string` | No |  |

**Responses:**

- `200`: OK
- `401`: 0: Authorization has been denied for this request.

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Rate Limits:** perApiKeyOwner: 1000/minute, perOauth2Authorization: 1000/minute

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/asset-delivery-api/v1/assetId/{ASSETID}/version/{VERSIONNUMBER}"
```

### PATCH `/asset-permissions-api/v1/assets/permissions` [BETA]

Grant a subject permission to multiple assets.
            
Authorization is required to grant permissions to the subject and asset IDs in the request.

**Auth:** Cookie (`.ROBLOSECURITY`) or API Key (`x-api-key` header)

**Scopes:** `asset-permissions:write`

**Request Body:** `application/json-patch+json` — Type: `BatchGrantPermissionsRequest`

See [BatchGrantPermissionsRequest](#batchgrantpermissionsrequest) in Models.

**Request example:**
```json
{
  "subjectType": "Invalid",
  "subjectId": "string",
  "action": "Invalid",
  "requests": [
    {
      "assetId": "...",
      "grantToDependencies": "...",
      "parentVersionNumber": "..."
    }
  ],
  "assetIds": [
    0
  ],
  "enableDeepAccessCheck": false
}
```

**Responses:**

- `200`: OK → `BatchGrantPermissionsResponse`
- `400`: Bad Request → `AssetPermissions.ErrorResponse`
- `403`: Forbidden → `AssetPermissions.ErrorResponse`
- `500`: Internal Server Error → `AssetPermissions.ErrorResponse`

**Response fields** (`BatchGrantPermissionsResponse`)

See [BatchGrantPermissionsResponse](#batchgrantpermissionsresponse) in Models.

**Response example:**
```json
{
  "successAssetIds": [
    0
  ],
  "errors": [
    {
      "assetId": "...",
      "code": "..."
    }
  ]
}
```

**Error handling:** `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 100/minute

**Example:**
```bash
curl -X PATCH -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/asset-permissions-api/v1/assets/permissions" \
  -H "Content-Type: application/json" \
  -d '{
  "subjectType": "Invalid",
  "subjectId": "string",
  "action": "Invalid",
  "requests": [
    {
      "assetId": "...",
      "grantToDependencies": "...",
      "parentVersionNumber": "..."
    }
  ],
  "assetIds": [
    0
  ],
  "enableDeepAccessCheck": false
}'
```

### POST `/assets/v1/assets` [BETA]

Creates an asset with provided content and metadata.

Creates an asset with provided content and metadata.

You can't add [SocialLink](#SocialLink) objects when you create an asset. Instead, use [Update Asset](#PATCH-v1-assets-_assetId_).

Provide the [Asset](#Asset), binary asset file path, and [content type](/cloud/guides/usage-assets.md#supported-asset-types-and-limits) in the form data.

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `asset:read`, `asset:write`

**Request Body:** `multipart/form-data` — Type: `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `request` | [Asset](#asset) | Yes | Asset attributes to create. |
| `request.assetType` | `string` | No | The asset type. Required for [Create Asset](#POST-v1-assets). |
| `request.assetId` | `integer` | No | The unique identifier of the asset. Required for [Update Asset](#PATCH-v1-assets-_asset_). |
| `request.creationContext` | [CreationContext](#creationcontext) | No |  |
| `request.description` | `string` | No | The description of the asset. Limit to 1000 characters. Required for [Create Asset](#POST-v1-assets) |
| `request.displayName` | `string` | No | Display name of the asset. Required for [Create Asset](#POST-v1-assets). |
| `request.path` | `string` | No | The returned resource path of the asset. Format: `assets/{assetId}`. Example: `assets/2205400862`. |
| `fileContent` | `string` | Yes | The binary asset file path and the content type. See [Asset types and limits](/cloud/guides/usage-assets.md#supported-as |

**Request example:**
```json
{
  "request": {
    "assetType": "string",
    "assetId": 0,
    "creationContext": {
      "assetPrivacy": "...",
      "creator": "...",
      "expectedPrice": "..."
    },
    "description": "string",
    "displayName": "string",
    "path": "string"
  },
  "fileContent": "string"
}
```

**Responses:**

- `200`: Returns the Operation ID for checking the creation status. → `OCV1.Assets.Operation`
- `400`: Invalid argument. Failed to parse the request or the file. → `OCV1.Assets.Status`
- `401`: The API key is not valid for this operation / You don't have the authorization.
- `500`: Server internal error / Unknown error.

**Response fields** (`OCV1.Assets.Operation`)

See [OCV1.Assets.Operation](#ocv1-assets-operation) in Models.

**Response example:**
```json
{
  "path": "string",
  "done": false,
  "error": {
    "code": 0,
    "message": "string"
  },
  "response": {
    "assetType": "string",
    "assetId": 0,
    "creationContext": {
      "assetPrivacy": "...",
      "creator": "...",
      "expectedPrice": "..."
    },
    "description": "string",
    "displayName": "string",
    "path": "string"
  }
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Rate Limits:** perApiKeyOwner: 120/minute, perOauth2Authorization: 120/minute

**Example:**
```bash
curl -X POST -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/assets/v1/assets" \
  -F "request={"assetType":"string","assetId":0,"creationContext":{"assetPrivacy":"default","creator":{"userId":"...","groupId":"..."},"expectedPrice":0},"description":"string","displayName":"string","path":"string"};type=application/json" \
  -F "fileContent=@file.bin;type=application/octet-stream"
```

### GET `/assets/v1/assets/{assetId}` [BETA]

Retrieve specific asset metadata. Include the `readMask` parameter for additional asset metadata.

Retrieve specific asset metadata.

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `asset:read`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `assetId` | path | `string` | Yes | The unique identifier of the asset. |
| `readMask` | query | `string` | No | Asset metadata fields to retrieve, including the description, display name, icon, social links, and previews. Examples: `description%2CdisplayName`, `previews%2CtwitchSocialLink`. |

**Responses:**

- `200`: Asset resource retrieved successfully. → `Asset`
- `400`: Malformed request, likely due to an invalid read mask.
- `401`: The API key is not valid for this operation / You don't have the authorization.
- `403`: Doesn't have the required permission.
- `404`: Asset doesn't exist.
- `500`: Server internal error / Unknown error.

**Response fields** (`Asset`)

See [Asset](#asset) in Models.

**Response example:**
```json
{
  "assetType": "string",
  "assetId": 0,
  "creationContext": {
    "assetPrivacy": "default",
    "creator": {
      "userId": "...",
      "groupId": "..."
    },
    "expectedPrice": 0
  },
  "description": "string",
  "displayName": "string",
  "path": "string"
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 120/minute, perOauth2Authorization: 120/minute

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/assets/v1/assets/{ASSETID}"
```

### PATCH `/assets/v1/assets/{assetId}` [BETA]

Updates an asset with provided content and metadata.

Updates an asset with provided content and metadata, including the description, display name, icon, social links, and previews. Currently can only update the content body for **Models**. Icons and Previews must be **Image** assets. Icons must have square dimensions.

Provide the [Asset](#Asset), binary asset file path, and [content type](/cloud/guides/usage-assets.md#supported-asset-types-and-limits) in the form data.

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `asset:read`, `asset:write`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `assetId` | path | `string` | Yes | The unique identifier of the asset. |
| `updateMask` | query | `string` | No | Asset metadata fields to update, including the description, display name, icon, and previews. Examples: `description%2CdisplayName`, `previews%2CtwitchSocialLink`. |

**Request Body:** `multipart/form-data` — Type: `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `request` | [Asset](#asset) | Yes | Asset attributes to update. |
| `request.assetType` | `string` | No | The asset type. Required for [Create Asset](#POST-v1-assets). |
| `request.assetId` | `integer` | No | The unique identifier of the asset. Required for [Update Asset](#PATCH-v1-assets-_asset_). |
| `request.creationContext` | [CreationContext](#creationcontext) | No |  |
| `request.description` | `string` | No | The description of the asset. Limit to 1000 characters. Required for [Create Asset](#POST-v1-assets) |
| `request.displayName` | `string` | No | Display name of the asset. Required for [Create Asset](#POST-v1-assets). |
| `request.path` | `string` | No | The returned resource path of the asset. Format: `assets/{assetId}`. Example: `assets/2205400862`. |
| `fileContent` | `string` | Yes | The binary asset file path and the content type. See [Asset types and limits](/cloud/guides/usage-assets.md#supported-as |

**Request example:**
```json
{
  "request": {
    "assetType": "string",
    "assetId": 0,
    "creationContext": {
      "assetPrivacy": "...",
      "creator": "...",
      "expectedPrice": "..."
    },
    "description": "string",
    "displayName": "string",
    "path": "string"
  },
  "fileContent": "string"
}
```

**Responses:**

- `200`: Returns the Operation ID for checking the update status / Returns the updated metadata fields. → `OCV1.Assets.Operation`
- `400`: Invalid argument. Failed to parse the request or the file. → `OCV1.Assets.Status`
- `401`: The API key is not valid for this operation / You don't have the authorization.
- `500`: Server internal error / Unknown error.

**Response fields** (`OCV1.Assets.Operation`)

See [OCV1.Assets.Operation](#ocv1-assets-operation) in Models.

**Response example:**
```json
{
  "path": "string",
  "done": false,
  "error": {
    "code": 0,
    "message": "string"
  },
  "response": {
    "assetType": "string",
    "assetId": 0,
    "creationContext": {
      "assetPrivacy": "...",
      "creator": "...",
      "expectedPrice": "..."
    },
    "description": "string",
    "displayName": "string",
    "path": "string"
  }
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Rate Limits:** perApiKeyOwner: 120/minute, perOauth2Authorization: 120/minute

**Example:**
```bash
curl -X PATCH -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/assets/v1/assets/{ASSETID}" \
  -F "request={"assetType":"string","assetId":0,"creationContext":{"assetPrivacy":"default","creator":{"userId":"...","groupId":"..."},"expectedPrice":0},"description":"string","displayName":"string","path":"string"};type=application/json" \
  -F "fileContent=@file.bin;type=application/octet-stream"
```

### GET `/assets/v1/assets/{assetId}/versions` [BETA]

List Asset Versions of an Asset

List all versions of a specific asset, with optional pagination.

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `asset:read`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `assetId` | path | `string` | Yes | The unique identifier of the asset. |
| `maxPageSize` | query | `integer` | No | Specifies the number of asset versions to include in the response. Valid values range from 1 to 50 (inclusive). Defaults to 8 when not provided. |
| `pageToken` | query | `string` | No | A token for pagination. The value is obtained from a previous request and allows for retrieving the next page of asset versions. |

**Responses:**

- `200`: Asset versions listed successfully. → `AssetVersion[]`
- `400`: Bad request - invalid parameters.
- `403`: Forbidden - API key without Read scope or user doesn't have access.
- `404`: Asset not found.

**Response fields** (`AssetVersion[]`)

See [AssetVersion](#assetversion) in Models.

**Error handling:** `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 100/minute, perOauth2Authorization: 100/minute

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/assets/v1/assets/{ASSETID}/versions"
```

### GET `/assets/v1/assets/{assetId}/versions/{versionNumber}` [BETA]

Get Asset Version

Retrieve a specific asset version by the asset ID and the version number.

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `asset:read`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `assetId` | path | `string` | Yes | The unique identifier of the asset. |
| `versionNumber` | path | `string` | Yes | The version number. |

**Responses:**

- `200`: Asset version retrieved successfully. → `AssetVersion`
- `403`: Forbidden - API key without Read scope or user doesn't have access.
- `404`: Asset or Asset Version not found.

**Response fields** (`AssetVersion`)

See [AssetVersion](#assetversion) in Models.

**Response example:**
```json
{
  "creationContext": {
    "assetPrivacy": "default",
    "creator": {
      "userId": "...",
      "groupId": "..."
    },
    "expectedPrice": 0
  },
  "path": "string",
  "moderationResult": {
    "moderationState": "string"
  },
  "published": false
}
```

**Error handling:** `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 100/minute, perOauth2Authorization: 100/minute

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/assets/v1/assets/{ASSETID}/versions/{VERSIONNUMBER}"
```

### POST `/assets/v1/assets/{assetId}/versions:rollback` [BETA]

Rollback an asset to a previous version.

Rollback an asset to a specific previous version.

 Provide the asset version path in the form data.

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `asset:read`, `asset:write`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `assetId` | path | `string` | Yes | The unique identifier of the asset. |

**Request Body:** `multipart/form-data` — Type: `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `assetVersion` | `string` | Yes | The asset version path in the format of `assets/{assetId}/versions/{versionNumber}`. |

**Request example:**
```json
{
  "assetVersion": "string"
}
```

**Responses:**

- `200`: Asset rolled back successfully. → `AssetVersion`
- `400`: Bad request - invalid request body.
- `403`: Forbidden - API key without Write scope or user doesn't have access.
- `404`: Asset or Asset Version not found.

**Response fields** (`AssetVersion`)

See [AssetVersion](#assetversion) in Models.

**Response example:**
```json
{
  "creationContext": {
    "assetPrivacy": "default",
    "creator": {
      "userId": "...",
      "groupId": "..."
    },
    "expectedPrice": 0
  },
  "path": "string",
  "moderationResult": {
    "moderationState": "string"
  },
  "published": false
}
```

**Error handling:** `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 100/minute, perOauth2Authorization: 100/minute

**Example:**
```bash
curl -X POST -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/assets/v1/assets/{ASSETID}/versions:rollback" \
  -F "assetVersion=string"
```

### POST `/assets/v1/assets/{assetId}:archive` [BETA]

Archives the asset.

Archives the asset. Archived assets disappear from the website and are no longer usable or visible in Roblox experiences, but you can [restore](#POST-v1-assets-{assetId}:restore) them.

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `asset:read`, `asset:write`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `assetId` | path | `string` | Yes | The unique identifier of the asset. |

**Responses:**

- `200`: Asset archived succesfully successfully. → `Asset`
- `400`: Bad request - invalid request.
- `403`: Forbidden - API key without Write scope or user doesn't have access.
- `404`: Asset not found.

**Response fields** (`Asset`)

See [Asset](#asset) in Models.

**Response example:**
```json
{
  "assetType": "string",
  "assetId": 0,
  "creationContext": {
    "assetPrivacy": "default",
    "creator": {
      "userId": "...",
      "groupId": "..."
    },
    "expectedPrice": 0
  },
  "description": "string",
  "displayName": "string",
  "path": "string"
}
```

**Error handling:** `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 100/minute, perOauth2Authorization: 100/minute

**Example:**
```bash
curl -X POST -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/assets/v1/assets/{ASSETID}:archive"
```

### POST `/assets/v1/assets/{assetId}:restore` [BETA]

Restores an archived asset.

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `asset:read`, `asset:write`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `assetId` | path | `string` | Yes | The unique identifier of the asset. |

**Responses:**

- `200`: Asset restored successfully. → `Asset`
- `400`: Bad request - invalid request.
- `403`: Forbidden - API key without Write scope or user doesn't have access.
- `404`: Asset not found.

**Response fields** (`Asset`)

See [Asset](#asset) in Models.

**Response example:**
```json
{
  "assetType": "string",
  "assetId": 0,
  "creationContext": {
    "assetPrivacy": "default",
    "creator": {
      "userId": "...",
      "groupId": "..."
    },
    "expectedPrice": 0
  },
  "description": "string",
  "displayName": "string",
  "path": "string"
}
```

**Error handling:** `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 100/minute, perOauth2Authorization: 100/minute

**Example:**
```bash
curl -X POST -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/assets/v1/assets/{ASSETID}:restore"
```

### GET `/assets/v1/operations/{operationId}` [BETA]

Get the result of an asset creation or update.

Get the result of an asset creation or update using the returned Operation ID. Requires **Read** for the API key permission and **asset:read** for OAuth 2.0 apps.

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `asset:read`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `operationId` | path | `string` | Yes | The unique identifier of the operation. |

**Responses:**

- `200`: Operation result retrieved successfully. → `OCV1.Assets.Operation`
- `400`: Invalid argument. Failed to parse the request or the file. → `OCV1.Assets.Status`
- `401`: The API key is not valid for this operation / You don't have the authorization.
- `500`: Server internal error / Unknown error.

**Response fields** (`OCV1.Assets.Operation`)

See [OCV1.Assets.Operation](#ocv1-assets-operation) in Models.

**Response example:**
```json
{
  "path": "string",
  "done": false,
  "error": {
    "code": 0,
    "message": "string"
  },
  "response": {
    "assetType": "string",
    "assetId": 0,
    "creationContext": {
      "assetPrivacy": "...",
      "creator": "...",
      "expectedPrice": "..."
    },
    "description": "string",
    "displayName": "string",
    "path": "string"
  }
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Rate Limits:** perApiKeyOwner: 300/minute, perOauth2Authorization: 300/minute

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/assets/v1/operations/{OPERATIONID}"
```

### POST `/cloud/v2/universes/{universe_id}:generateSpeechAsset` [BETA]

Generate Speech Asset

Generates an English speech audio asset from the specified text.

This endpoint requires the `asset:read` and `asset:write` scopes in
addition to the `universe:write` scope.

The response returns an `Operation` object that must be prefixed with
`/assets/v1`. For example, the URL to discover the result of the operation
could be
`https://apis.roblox.com/assets/v1/operations/8b42ef30-9c17-4526-b8cf-2ff0136ca94d`.

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `universe:write`, `asset:read`, `asset:write`, `universe:write`, `asset:read`, `asset:write`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universe_id` | path | `string` | Yes | The universe ID. |

**Request Body:** `application/json` — Type: `GenerateSpeechAssetRequest`

See [GenerateSpeechAssetRequest](#generatespeechassetrequest) in Models.

**Request example:**
```json
{
  "text": "string",
  "speechStyle": {
    "voiceId": "string",
    "pitch": 0,
    "speed": 0
  }
}
```

**Responses:**

- `200`: OK → `Operation`

**Response fields** (`Operation`)

See [Operation](#operation) in Models.

**Response example:**
```json
{
  "path": "string",
  "metadata": {
    "@type": "string"
  },
  "done": false,
  "error": {
    "code": 0,
    "message": "string",
    "details": [
      "..."
    ]
  },
  "response": {
    "@type": "string"
  }
}
```

**Rate Limits:** perApiKeyOwner: 4/second, perOauth2Authorization: 4/second

**Example:**
```bash
curl -X POST -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/cloud/v2/universes/{UNIVERSE_ID}:generateSpeechAsset" \
  -H "Content-Type: application/json" \
  -d '{
  "text": "string",
  "speechStyle": {
    "voiceId": "string",
    "pitch": 0,
    "speed": 0
  }
}'
```

### GET `/cloud/v2/users/{user_id}/asset-quotas` [BETA]

List Asset Quotas

Returns a list of asset quotas.

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `asset:read`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `user_id` | path | `string` | Yes | The user ID. |
| `maxPageSize` | query | `integer` | No | The maximum number of asset quotas to return. The service might return fewer than this value. If unspecified, at most 10 asset quotas are returned. The maximum value is 100 and higher values are set to 100. |
| `pageToken` | query | `string` | No | A page token, received from a previous call, to retrieve a subsequent page.  When paginating, all other parameters provided to the subsequent call must match the call that provided the page token. |
| `filter` | query | `string` | No | This field may be set in order to filter the resources returned.  Supports the following subset of CEL: * Only the `quotaType` and `assetType` fields are supported. * Only the `==` and `&&` operator are supported.  For example:   `quotaType == RateLimitUpload && assetType == Audio` |

**Responses:**

- `200`: OK → `ListAssetQuotasResponse`

**Response fields** (`ListAssetQuotasResponse`)

See [ListAssetQuotasResponse](#listassetquotasresponse) in Models.

**Response example:**
```json
{
  "assetQuotas": [
    {
      "path": "...",
      "quotaType": "...",
      "assetType": "...",
      "usage": "...",
      "capacity": "...",
      "period": "..."
    }
  ],
  "nextPageToken": "string"
}
```

**Rate Limits:** perApiKeyOwner: 60/minute, perOauth2Authorization: 60/minute

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/cloud/v2/users/{USER_ID}/asset-quotas"
```

### GET `/legacy-localization-tables/v1/localization-table/tables/{assetId}` [EXPERIMENTAL]

Get table information by the assetId of the table.

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `legacy-universe:manage`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `assetId` | path | `integer` | Yes | The asset id associated with the table. |

**Responses:**

- `200`: OK → `Roblox.LocalizationTables.Api.GetTableResponse`
- `400`: 12: Invalid asset id.
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
  "https://apis.roblox.com/legacy-localization-tables/v1/localization-table/tables/{ASSETID}"
```

### POST `/legacy-publish/v1/badges/{badgeId}/icon` [EXPERIMENTAL]

Overwrites a badge icon with a new one.

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `legacy-badge:manage`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `badgeId` | path | `integer` | Yes | The badge Id. |

**Responses:**

- `200`: OK → `Roblox.Publish.Api.UploadResponse`
- `400`: 2: File not present in request. 12: Name or description is moderated.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 5: You do not have permission to manage this item.
- `404`: 4: Target item is invalid or does not exist.
- `429`: 3: You're uploading too much, please wait and try again later.

**Response fields** (`Roblox.Publish.Api.UploadResponse`)

See [Roblox.Publish.Api.UploadResponse](#roblox-publish-api-uploadresponse) in Models.

**Response example:**
```json
{
  "targetId": 0
}
```

**Error handling:** `429`: Retry with exponential backoff (start at 1s). `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 100/minute, perOauth2Authorization: 100/minute

**Example:**
```bash
curl -X POST -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/legacy-publish/v1/badges/{BADGEID}/icon" \
  -H "Content-Type: application/json" \
  -d '{"key": "value"}'
```

### GET `/toolbox-service/v2/assets/{id}` [BETA]

Get Creator Store Asset Details

Get details for a single Creator Store asset.

**Auth:** Cookie (`.ROBLOSECURITY`) or API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `creator-store-product:read`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `id` | path | `integer` | Yes | The asset ID to retrieve details for. |

**Responses:**

- `200`: OK → `CreatorStoreAsset`
- `403`: Forbidden → `any`
- `404`: Not Found → `any`
- `429`: Too Many Requests → `any`

**Response fields** (`CreatorStoreAsset`)

See [CreatorStoreAsset](#creatorstoreasset) in Models.

**Response example:**
```json
{
  "voting": "...",
  "creator": "...",
  "creatorStoreProduct": "...",
  "asset": "..."
}
```

**Error handling:** `429`: Retry with exponential backoff (start at 1s). `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 1000/minute, perOauth2Authorization: 1000/minute

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/toolbox-service/v2/assets/{ID}"
```

### GET `/toolbox-service/v2/assets:search` [BETA]

Search Creator Store Assets

Search Creator Store for assets.

**Auth:** Cookie (`.ROBLOSECURITY`) or API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `creator-store-product:read`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `searchCategoryType` | query | `any` | No | The asset type to search within. Optional when categoryPath is present in the request; otherwise required. |
| `query` | query | `string` | No | The search terms used to filter the results. |
| `modelSubTypes` | query | `ModelSubType[]` | No | When searching for models, the subtypes associated with the search results. |
| `excludedModelSubTypes` | query | `ModelSubType[]` | No | When searching for models, the subtypes not associated with the search results. |
| `creator` | query | `string` | No | Deprecated: Please refer to the 'userId' and 'groupId' properties instead. The creator type and ID. E.g. "user/123" or "group/456" |
| `userId` | query | `integer` | No | The User ID of the creator. Only one of 'userId' and 'groupId' can be present in a query. |
| `groupId` | query | `integer` | No | The Group ID of the creator. Only one of 'userId' and 'groupId' can be present in a query. |
| `pageToken` | query | `string` | No | The identifier for the desired search results page. Only one of 'pageNumber' and 'pageToken' can be present in a query. |
| `pageNumber` | query | `integer` | No | The page number to retrieve, starting from 0. Only one of 'pageNumber' and 'pageToken' can be present in a query. |
| `maxPageSize` | query | `integer` | No | The number of assets to be returned. Cannot be larger than 100. |
| `sortDirection` | query | `any` | No | The sort direction of the search results. |
| `sortCategory` | query | `any` | No | The category to sort the search results by. |
| `audioMinDurationSeconds` | query | `integer` | No | When searching for audio, the minimum duration of the audio assets. If included, must be greater than or equal to 0. |
| `audioMaxDurationSeconds` | query | `integer` | No | When searching for audio, the maximum duration of the audio assets. If included, must be greater than or equal to 0. |
| `audioArtist` | query | `string` | No | When searching for audio, the artist name of the audio assets. |
| `audioAlbum` | query | `string` | No | When searching for audio, the album name of the audio assets. |
| `audioTypes` | query | `SearchAudioTypeModel[]` | No | When searching for audio, the type of the audio assets. |
| `includedInstanceTypes` | query | `ModelInstanceType[]` | No | When searching for models, this filters that the following [Instance](https://create.roblox.com/docs/reference/engine/classes/Instance) types are included in the model. |
| `includeOnlyVerifiedCreators` | query | `boolean` | No | Whether the results should only include assets created by verified creators. |
| `minPriceCents` | query | `integer` | No | The minimum price of the asset in cents. If included, must be greater than or equal to 0. |
| `maxPriceCents` | query | `integer` | No | The maximum price of the asset in cents. If included, must be greater than or equal to 0. |
| `facets` | query | `string[]` | No | Additional keywords to query by. |
| `tags` | query | `string[]` | No | The tags used to filter the results. |
| `categoryPath` | query | `string` | No |  |
| `searchView` | query | `any` | No | Indicates which fields will be populated in the response. |
| `musicChartType` | query | `any` | No | Indicates which music charts to filter from. |
| `swimlane` | query | `string` | No | Indicates which swimlane to filter from. |

**Responses:**

- `200`: OK → `SearchCreatorStoreAssetsResponse`
- `400`: Bad Request → `any`
- `429`: Too Many Requests → `any`
- `500`: Internal Server Error

**Response fields** (`SearchCreatorStoreAssetsResponse`)

See [SearchCreatorStoreAssetsResponse](#searchcreatorstoreassetsresponse) in Models.

**Response example:**
```json
{
  "nextPageToken": "string",
  "queryFacets": "...",
  "creatorStoreAssets": [
    {
      "voting": "...",
      "creator": "...",
      "creatorStoreProduct": "...",
      "asset": "..."
    }
  ],
  "totalResults": 0,
  "queryCorrection": "...",
  "filteredKeyword": "string"
}
```

**Error handling:** `429`: Retry with exponential backoff (start at 1s). 

**Rate Limits:** perApiKeyOwner: 1000/minute, perOauth2Authorization: 1000/minute

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/toolbox-service/v2/assets:search"
```

### GET `/v1/asset`

**Server:** `https://assetdelivery.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `Accept-Encoding` | header | `string` | Yes |  |
| `Roblox-Place-Id` | header | `integer` | Yes |  |
| `AssetType` | header | `string` | Yes |  |
| `AssetFormat` | header | `string` | Yes |  |
| `Roblox-AssetFormat` | header | `string` | Yes |  |
| `Roblox-Usage-Context` | header | `string` | No |  |
| `id` | query | `integer` | No |  |
| `userAssetId` | query | `integer` | No |  |
| `assetVersionId` | query | `integer` | No |  |
| `version` | query | `integer` | No |  |
| `universeId` | query | `integer` | No |  |
| `clientInsert` | query | `integer` | No |  |
| `scriptinsert` | query | `integer` | No |  |
| `modulePlaceId` | query | `integer` | No |  |
| `serverplaceid` | query | `string` | No |  |
| `assetName` | query | `string` | No |  |
| `hash` | query | `string` | No |  |
| `marAssetHash` | query | `string` | No |  |
| `marCheckSum` | query | `string` | No |  |
| `expectedAssetType` | query | `string` | No |  |
| `skipSigningScripts` | query | `boolean` | No |  |
| `permissionContext` | query | `string` | No |  |
| `doNotFallbackToBaselineRepresentation` | query | `boolean` | No |  |
| `contentRepresentationPriorityList` | query | `string` | No |  |
| `assetResolutionMode` | query | `string` | No |  |
| `accessContext` | query | `string` | No |  |

**Responses:**

- `200`: OK

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://assetdelivery.roblox.com/v1/asset"
```

### GET `/v1/asset-quotas`

List asset quotas of the given resource type and asset type.

**Server:** `https://publish.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `resourceType` | query | `string` | Yes | Resource type of the asset quota |
| `assetType` | query | `string` | Yes | Asset type of the asset quota |
| `useDummyData` | query | `boolean` | No | Use dummy data for testing. This is for internal use only |

**Responses:**

- `200`: OK → `Roblox.Publish.Api.AssetQuotasResponse`
- `400`: 7: The asset type is not appropriate for this request. 8: The resource type is not appropriate for this request.
- `401`: 0: Authorization has been denied for this request.
- `500`: 0: Reserved for base level errors. Do not use in your endpoint directly, do not document.

**Response fields** (`Roblox.Publish.Api.AssetQuotasResponse`)

See [Roblox.Publish.Api.AssetQuotasResponse](#roblox-publish-api-assetquotasresponse) in Models.

**Response example:**
```json
{
  "quotas": [
    {
      "duration": "...",
      "usage": "...",
      "capacity": "...",
      "expirationTime": "..."
    }
  ]
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://publish.roblox.com/v1/asset-quotas?resourceType={VALUE}&assetType={VALUE}"
```

### GET `/v1/asset-thumbnail-animated` [STABLE]

Thumbnails asset animated.

**Server:** `https://thumbnails.roblox.com`

**Auth:** 

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `assetId` | query | `integer` | Yes | The asset id. |
| `Roblox-Place-Id` | header | `integer` | No | (optional) placeid |

**Responses:**

- `200`: OK
- `400`: 4: The requested Ids are invalid, of an invalid type or missing.

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://thumbnails.roblox.com/v1/asset-thumbnail-animated?assetId={VALUE}"
```

### GET `/v1/asset-to-category`

Lists a mapping for assets to category IDs to convert from inventory ID to catalog ID. Creates a mapping to link 'Get More' button in inventory page to the relevant catalog page.

**Server:** `https://catalog.roblox.com`

**Auth:** 

**Responses:**

- `200`: OK → `object`

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://catalog.roblox.com/v1/asset-to-category"
```

### GET `/v1/asset-to-subcategory`

Lists a mapping for assets to subcategory IDs to convert from inventory ID to catalog ID. Creates a mapping to link 'Get More' button in inventory page to the relevant catalog page.

**Server:** `https://catalog.roblox.com`

**Auth:** 

**Responses:**

- `200`: OK → `object`

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://catalog.roblox.com/v1/asset-to-subcategory"
```

### GET `/v1/assetId/{assetId}`

Retrieves an asset by its ID

**Server:** `https://assetdelivery.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `assetId` | path | `integer` | Yes | The ID of the asset to retrieve. |
| `Accept-Encoding` | header | `string` | Yes |  |
| `Roblox-Place-Id` | header | `integer` | Yes |  |
| `AssetType` | header | `string` | Yes |  |
| `AssetFormat` | header | `string` | Yes |  |
| `Roblox-AssetFormat` | header | `string` | Yes |  |
| `Roblox-Usage-Context` | header | `string` | No |  |
| `skipSigningScripts` | query | `boolean` | No |  |
| `clientInsert` | query | `integer` | No |  |
| `scriptinsert` | query | `integer` | No |  |
| `modulePlaceId` | query | `integer` | No |  |
| `serverplaceid` | query | `integer` | No |  |
| `expectedAssetType` | query | `string` | No |  |
| `doNotFallbackToBaselineRepresentation` | query | `boolean` | No |  |
| `contentRepresentationPriorityList` | query | `string` | No |  |
| `accessContext` | query | `string` | No |  |

**Responses:**

- `200`: OK

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://assetdelivery.roblox.com/v1/assetId/{ASSETID}"
```

### GET `/v1/assetId/{assetId}/version/{versionNumber}`

Retrieves an asset by its ID and version number.

**Server:** `https://assetdelivery.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `assetId` | path | `integer` | Yes | The ID of the asset to retrieve. |
| `versionNumber` | path | `integer` | Yes | The version of the asset to retrieve. |
| `Accept-Encoding` | header | `string` | Yes |  |
| `Roblox-Place-Id` | header | `integer` | Yes |  |
| `AssetType` | header | `string` | Yes |  |
| `AssetFormat` | header | `string` | Yes |  |
| `Roblox-AssetFormat` | header | `string` | Yes |  |
| `Roblox-Usage-Context` | header | `string` | No |  |
| `skipSigningScripts` | query | `boolean` | No |  |
| `clientInsert` | query | `integer` | No |  |
| `scriptinsert` | query | `integer` | No |  |
| `modulePlaceId` | query | `integer` | No |  |
| `serverplaceid` | query | `integer` | No |  |
| `expectedAssetType` | query | `string` | No |  |
| `doNotFallbackToBaselineRepresentation` | query | `boolean` | No |  |
| `contentRepresentationPriorityList` | query | `string` | No |  |
| `accessContext` | query | `string` | No |  |

**Responses:**

- `200`: OK

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://assetdelivery.roblox.com/v1/assetId/{ASSETID}/version/{VERSIONNUMBER}"
```

### GET `/v1/assets#thumbnails.roblox.com` [STABLE]

Thumbnails assets.

**Server:** `https://thumbnails.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `assetIds` | query | `integer[]` | Yes | The asset ids. |
| `Roblox-Place-Id` | header | `integer` | No | (optional) placeid |
| `returnPolicy` | query | `PlaceHolder \| ForcePlaceHolder \| AutoGenerated \| ForceAutoGenerated` | No | Optional policy to use in selecting thumbnail to return (default = PlaceHolder). Valid values: `PlaceHolder`, `ForcePlaceHolder`, `AutoGenerated`, `ForceAutoGenerated` |
| `size` | query | `string enum (30 values)` | No | The thumbnail size, formatted widthxheight Valid values: `30x30`, `42x42`, `50x50`, `60x62`, `75x75`, `110x110`, `140x140`, `150x150`, `160x100`, `160x600`, `250x250`, `256x144`, `300x250`, `304x166`, `384x216`, `396x216`, `420x420`, `480x270`, `512x512`, `576x324`, `700x700`, `728x90`, `768x432`, `1200x80`, `330x110`, `660x220`, `1320x440`, `720x228`, `1440x456`, `930x480` |
| `format` | query | `Png \| Jpeg \| Webp` | No | The thumbnail format Valid values: `Png`, `Jpeg`, `Webp` |
| `isCircular` | query | `true \| false` | No | The circle thumbnail output parameter, true or false Valid values: `true`, `false` |

**Responses:**

- `200`: OK
- `400`: 1: There are too many requested Ids. 2: The requested image format is invalid. Please see documentation for valid thumbnail format parameter name and values. 3: The requested size is invalid. Please see documentation for valid thumbnail size parameter name and format. 4: The requested Ids are invalid, of an invalid type or missing. 8: The requested return policy is invalid (must be PlaceHolder, AutoGenerated or ForceAutoGenerated). 10: Circular thumbnail requests are not allowed
- `403`: 9: User not authorized to use AutoGenerated or ForceAutoGenerated return policies.

**Error handling:** `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://thumbnails.roblox.com/v1/assets#thumbnails.roblox.com?assetIds={VALUE}"
```

### GET `/v1/assets-thumbnail-3d` [BETA]

Thumbnails assets.

**Server:** `https://thumbnails.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`) or API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `thumbnail:read`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `assetId` | query | `integer` | Yes | The asset id. |
| `useGltf` | query | `boolean` | No | (optional) formatType |
| `Roblox-Place-Id` | header | `integer` | No | (optional) placeid |

**Responses:**

- `200`: OK
- `400`: 4: The requested Ids are invalid, of an invalid type or missing.

**Rate Limits:** perApiKeyOwner: 100/minute, perOauth2Authorization: 100/minute

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://thumbnails.roblox.com/v1/assets-thumbnail-3d?assetId={VALUE}"
```

### POST `/v1/assets/batch`

**Server:** `https://assetdelivery.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `Roblox-Place-Id` | header | `integer` | Yes |  |
| `Roblox-Browser-Asset-Request` | header | `string` | Yes |  |

**Request Body:** `application/json` — Type: `Roblox.Web.Assets.BatchAssetRequestItem[]`

See [Roblox.Web.Assets.BatchAssetRequestItem](#roblox-web-assets-batchassetrequestitem) in Models.

**Responses:**

- `200`: OK

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://assetdelivery.roblox.com/v1/assets/batch" \
  -H "Content-Type: application/json" \
  -d '[
  {
    "assetName": "string",
    "assetType": "string",
    "clientInsert": false,
    "placeId": 0,
    "requestId": "string",
    "scriptInsert": false
  }
]'
```

### GET `/v1/assets/voting` *(deprecated)*

Gets the voting information of the given assets

Please use toolbox service to get asset voting information.

**Server:** `https://develop.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `assetIds` | query | `integer[]` | Yes | The ids of the Roblox.Platform.Assets.IAsset. |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.Api.Develop.Models.Response.AssetVotingModel_`

**Response fields** (`Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.Api.Develop.Models.Response.AssetVotingModel_`)

See [Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.Api.Develop.Models.Response.AssetVotingModel_](#roblox-web-webapi-models-apiarrayresponse-roblox-api-develop-models-response-assetvotingmodel-) in Models.

**Response example:**
```json
{
  "data": [
    {
      "assetId": "...",
      "hasUserVoted": "...",
      "canUserVote": "...",
      "shouldShowVotes": "...",
      "upVotes": "...",
      "downVotes": "..."
    }
  ]
}
```

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://develop.roblox.com/v1/assets/voting?assetIds={VALUE}"
```

### GET `/v1/assets/{assetId}/bundles` [EXPERIMENTAL]

Lists the bundles a particular asset belongs to. Use the Id of the last bundle in the response to get the next page.

**Server:** `https://catalog.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `assetId` | path | `integer` | Yes |  |
| `limit` | query | `10 \| 25 \| 50 \| 100` | No | The number of results per request. Valid values: `10`, `25`, `50`, `100` |
| `cursor` | query | `string` | No | The paging cursor for the previous or next page. |
| `sortOrder` | query | `Asc \| Desc` | No | The order the results are sorted in. Valid values: `Asc`, `Desc` |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.Catalog.Api.BundleDetailsModel_`
- `400`: 1: Invalid assetId 4: Invalid Cursor.

**Response fields** (`Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.Catalog.Api.BundleDetailsModel_`)

See [Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.Catalog.Api.BundleDetailsModel_](#roblox-web-webapi-models-apipageresponse-roblox-catalog-api-bundledetailsmodel-) in Models.

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
      "bundleType": "...",
      "isRecolorable": "...",
      "items": "..."
    }
  ]
}
```

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://catalog.roblox.com/v1/assets/{ASSETID}/bundles"
```

### POST `/v1/audio`

Published an audio file and returns the new asset info.

**Server:** `https://publish.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Request Body:** `application/json` — Type: `Roblox.Publish.Api.UploadAudioRequest`

See [Roblox.Publish.Api.UploadAudioRequest](#roblox-publish-api-uploadaudiorequest) in Models.

**Request example:**
```json
{
  "name": "string",
  "file": "string",
  "groupId": 0,
  "paymentSource": "string",
  "estimatedFileSize": 0,
  "estimatedDuration": 0
}
```

**Responses:**

- `200`: OK → `Roblox.Publish.Api.PublishAudioResponse`
- `400`: 3: The request did not contain a file to be uploaded. 4: The file in the request is too large. 5: The duration of the audio file is too long. 7: Failed to parse the file. 8: The file type is not supported. 9: The file is corrupted 11: Missing permissions to spend group funds. 14: The user/group does not have suffiecient funds to publish. 14: The user/group does not have suffiecient funds to publish. 15: The audio file has already been reviewed and rejected. 18: Too many requests. Try again later. 20: Error while trying to purchase the product. 22: The file size estimation error was greater than the acceptable margin of error. 23: The duration estimation error was greater than the acceptable margin of error. 24: Asset privacy is invalid. 29: Invalid argument in the request.
- `401`: 0: Authorization has been denied for this request. 1: The request did not include an authorization.
- `403`: 0: Token Validation Failed
- `500`: 19: Asset creation was unavailable. Please try again.

**Response fields** (`Roblox.Publish.Api.PublishAudioResponse`)

See [Roblox.Publish.Api.PublishAudioResponse](#roblox-publish-api-publishaudioresponse) in Models.

**Response example:**
```json
{
  "Id": 0,
  "Name": "string"
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://publish.roblox.com/v1/audio" \
  -H "Content-Type: application/json" \
  -d '{
  "name": "string",
  "file": "string",
  "groupId": 0,
  "paymentSource": "string",
  "estimatedFileSize": 0,
  "estimatedDuration": 0
}'
```

### POST `/v1/audio/verify`

Verifies an audio file and returns a product that you can purchase to publish the audio file.

**Server:** `https://publish.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Request Body:** `application/json` — Type: `Roblox.Publish.Api.VerifyAudioRequest`

See [Roblox.Publish.Api.VerifyAudioRequest](#roblox-publish-api-verifyaudiorequest) in Models.

**Request example:**
```json
{
  "name": "string",
  "file": "string",
  "groupId": 0,
  "paymentSource": "string",
  "fileSize": 0,
  "duration": 0
}
```

**Responses:**

- `200`: OK → `Roblox.Publish.Api.VerifyAudioResponse`
- `400`: 3: The request did not contain a file to be uploaded. 4: The file in the request is too large. 5: The duration of the audio file is too long. 7: Failed to parse the file. 8: The file type is not supported. 9: The file is corrupted 18: Too many requests. Try again later.
- `401`: 0: Authorization has been denied for this request. 1: The request did not include an authorization.
- `403`: 0: Token Validation Failed

**Response fields** (`Roblox.Publish.Api.VerifyAudioResponse`)

See [Roblox.Publish.Api.VerifyAudioResponse](#roblox-publish-api-verifyaudioresponse) in Models.

**Response example:**
```json
{
  "name": "string",
  "price": 0,
  "balance": 0,
  "canAfford": false
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://publish.roblox.com/v1/audio/verify" \
  -H "Content-Type: application/json" \
  -d '{
  "name": "string",
  "file": "string",
  "groupId": 0,
  "paymentSource": "string",
  "fileSize": 0,
  "duration": 0
}'
```

### POST `/v1/badges/{badgeId}/icon`

Overwrites a badge icon with a new one.

Accepts a moderated image upload and updates the badge's icon asset.

**Server:** `https://badges.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `badgeId` | path | `integer` | Yes | The badge Id. |

**Request Body:** `multipart/form-data` — Type: `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `Files` | `string` | No |  |

**Request example:**
```json
{
  "Files": "string"
}
```

**Responses:**

- `200`: OK → `Roblox.Badges.Api.IconUploadResponse`
- `400`: 6: Text moderated. 22: Icon file is not present in the request.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 2: You do not have permission to manage this badge.
- `404`: 1: Badge is invalid or does not exist.
- `429`: 13: Too many requests, try again later.

**Response fields** (`Roblox.Badges.Api.IconUploadResponse`)

See [Roblox.Badges.Api.IconUploadResponse](#roblox-badges-api-iconuploadresponse) in Models.

**Response example:**
```json
{
  "targetId": 0
}
```

**Error handling:** `429`: Retry with exponential backoff (start at 1s). `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://badges.roblox.com/v1/badges/{BADGEID}/icon" \
  -F "Files=@file.bin;type=application/octet-stream"
```

### POST `/v1/badges/{badgeId}/icon#publish.roblox.com` [EXPERIMENTAL]

Overwrites a badge icon with a new one.

**Server:** `https://publish.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `badgeId` | path | `integer` | Yes | The badge Id. |

**Responses:**

- `200`: OK → `Roblox.Publish.Api.UploadResponse`
- `400`: 2: File not present in request. 12: Name or description is moderated.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 5: You do not have permission to manage this item.
- `404`: 4: Target item is invalid or does not exist.
- `429`: 3: You're uploading too much, please wait and try again later.

**Response fields** (`Roblox.Publish.Api.UploadResponse`)

See [Roblox.Publish.Api.UploadResponse](#roblox-publish-api-uploadresponse) in Models.

**Response example:**
```json
{
  "targetId": 0
}
```

**Error handling:** `429`: Retry with exponential backoff (start at 1s). `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://publish.roblox.com/v1/badges/{BADGEID}/icon#publish.roblox.com" \
  -H "Content-Type: application/json" \
  -d '{"key": "value"}'
```

### GET `/v1/bundles/details` [EXPERIMENTAL]

Returns details about the given bundleIds.

**Server:** `https://catalog.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `bundleIds` | query | `integer[]` | Yes |  |

**Responses:**

- `200`: OK → `Roblox.Catalog.Api.BundleDetailsModel[]`
- `400`: 3: Cannot request so many bundles at once.

**Response fields** (`Roblox.Catalog.Api.BundleDetailsModel[]`)

See [Roblox.Catalog.Api.BundleDetailsModel](#roblox-catalog-api-bundledetailsmodel) in Models.

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://catalog.roblox.com/v1/bundles/details?bundleIds={VALUE}"
```

### GET `/v1/bundles/{bundleId}/details` [EXPERIMENTAL]

Returns details about the given bundleId.

**Server:** `https://catalog.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `bundleId` | path | `integer` | Yes |  |

**Responses:**

- `200`: OK → `Roblox.Catalog.Api.BundleDetailsModel`
- `400`: 1: Invalid bundle

**Response fields** (`Roblox.Catalog.Api.BundleDetailsModel`)

See [Roblox.Catalog.Api.BundleDetailsModel](#roblox-catalog-api-bundledetailsmodel) in Models.

**Response example:**
```json
{
  "id": 0,
  "name": "string",
  "description": "string",
  "bundleType": "string",
  "isRecolorable": false,
  "items": [
    {
      "owned": "...",
      "id": "...",
      "name": "...",
      "type": "...",
      "supportsHeadShapes": "...",
      "assetType": "..."
    }
  ]
}
```

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://catalog.roblox.com/v1/bundles/{BUNDLEID}/details"
```

### GET `/v1/bundles/{bundleId}/recommendations`

Gets recommendations for a given bundle, bundleId of 0 returns randomized bundles
- Accepts both public and authenticated users.

**Server:** `https://catalog.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `bundleId` | path | `integer` | Yes |  |
| `numItems` | query | `integer` | No | The number of recommended items to return. |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.Catalog.Api.BundleDetailsModel_`
- `400`: 1: Invalid bundle 2: Error retrieving bundles 3: Error getting bundle recommendations 4: NumItems exceed maximum

**Response fields** (`Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.Catalog.Api.BundleDetailsModel_`)

See [Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.Catalog.Api.BundleDetailsModel_](#roblox-web-webapi-models-apiarrayresponse-roblox-catalog-api-bundledetailsmodel-) in Models.

**Response example:**
```json
{
  "data": [
    {
      "id": "...",
      "name": "...",
      "description": "...",
      "bundleType": "...",
      "isRecolorable": "...",
      "items": "..."
    }
  ]
}
```

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://catalog.roblox.com/v1/bundles/{BUNDLEID}/recommendations"
```

### POST `/v1/catalog/items/details` [EXPERIMENTAL]

Returns details for one or more catalog items.

There is an item count limit per request. Exceeding this returns 400 Bad Request.

**Server:** `https://catalog.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.Catalog.Api.CatalogSearchDetailedResponseItemV2_`
- `400`: 2: Invalid count
- `403`: 0: Token Validation Failed 7: User is unauthorized.
- `429`: 8: The flood limit has been exceeded.

**Response fields** (`Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.Catalog.Api.CatalogSearchDetailedResponseItemV2_`)

See [Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.Catalog.Api.CatalogSearchDetailedResponseItemV2_](#roblox-web-webapi-models-apiarrayresponse-roblox-catalog-api-catalogsearchdetailedresponseitemv2-) in Models.

**Response example:**
```json
{
  "data": [
    {
      "bundledItems": "...",
      "taxonomy": "...",
      "itemCreatedUtc": "...",
      "discountInformation": "...",
      "license": "...",
      "id": "..."
    }
  ]
}
```

**Error handling:** `429`: Retry with exponential backoff (start at 1s). `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://catalog.roblox.com/v1/catalog/items/details" \
  -H "Content-Type: application/json" \
  -d '{"key": "value"}'
```

### POST `/v1/catalog/items/details/complete`

Returns list of item details complete with user ownership and economy information.
Batch version of GetItemDetailsComplete. Items with critical errors are returned in ItemErrors
with their corresponding HTTP status code (404 for not-found, 500 for other errors).

**Server:** `https://catalog.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `Roblox-Place-Id` | header | `integer` | Yes |  |
| `Roblox-Game-Id` | header | `string` | Yes |  |

**Responses:**

- `200`: OK → `Roblox.Catalog.Api.BatchItemDetailsCompleteResponse`
- `400`: 2: Invalid count
- `403`: 0: Token Validation Failed 7: User is unauthorized.
- `429`: 8: The flood limit has been exceeded.

**Response fields** (`Roblox.Catalog.Api.BatchItemDetailsCompleteResponse`)

See [Roblox.Catalog.Api.BatchItemDetailsCompleteResponse](#roblox-catalog-api-batchitemdetailscompleteresponse) in Models.

**Response example:**
```json
{
  "data": [
    {
      "id": "...",
      "itemType": "...",
      "item": "...",
      "httpStatusCode": "..."
    }
  ]
}
```

**Error handling:** `429`: Retry with exponential backoff (start at 1s). `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://catalog.roblox.com/v1/catalog/items/details/complete" \
  -H "Content-Type: application/json" \
  -d '{"key": "value"}'
```

### GET `/v1/categories`

Lists Category Names and their Ids.

**Server:** `https://catalog.roblox.com`

**Auth:** 

**Responses:**

- `200`: OK → `Roblox.Catalog.Api.CategoryModel[]`

**Response fields** (`Roblox.Catalog.Api.CategoryModel[]`)

See [Roblox.Catalog.Api.CategoryModel](#roblox-catalog-api-categorymodel) in Models.

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://catalog.roblox.com/v1/categories"
```

### POST `/v1/creations/get-asset-details` [EXPERIMENTAL]

Gets the asset status and other configuration details for the given assetIds list.

**Server:** `https://itemconfiguration.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Request Body:** `application/json` — Type: `Roblox.ItemConfiguration.Api.AssetCreationsDetailsRequest`

See [Roblox.ItemConfiguration.Api.AssetCreationsDetailsRequest](#roblox-itemconfiguration-api-assetcreationsdetailsrequest) in Models.

**Request example:**
```json
{
  "AssetIds": [
    0
  ]
}
```

**Responses:**

- `200`: OK → `Roblox.ItemConfiguration.Api.AssetCreationsDetailsResponse[]`
- `400`: 1: Missing AssetIds parameters 2: Invalid asset Ids
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed
- `414`: 3: Too many asset Ids
- `429`: 9: Flood Limit Exceeded
- `503`: 6: Service Unavailable

**Response fields** (`Roblox.ItemConfiguration.Api.AssetCreationsDetailsResponse[]`)

See [Roblox.ItemConfiguration.Api.AssetCreationsDetailsResponse](#roblox-itemconfiguration-api-assetcreationsdetailsresponse) in Models.

**Error handling:** `429`: Retry with exponential backoff (start at 1s). `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://itemconfiguration.roblox.com/v1/creations/get-asset-details" \
  -H "Content-Type: application/json" \
  -d '{
  "AssetIds": [
    0
  ]
}'
```

### GET `/v1/creations/get-assets` [EXPERIMENTAL]

Gets the user created asset information filtered by the given asset type.

**Server:** `https://itemconfiguration.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `assetType` | query | `string` | Yes |  |
| `isArchived` | query | `boolean` | No |  |
| `groupId` | query | `integer` | No |  |
| `limit` | query | `10 \| 25 \| 50 \| 100` | No | The number of results per request. Valid values: `10`, `25`, `50`, `100` |
| `cursor` | query | `string` | No | The paging cursor for the previous or next page. |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.ItemConfiguration.Api.AssetCreationsResponse_`
- `400`: 5: Invalid assetType 10: Invalid Asset Category
- `401`: 0: Authorization has been denied for this request.
- `403`: 7: User does not have necessary permissions for group 8: Asset type does not have necessary permissions for group
- `429`: 9: Flood Limit Exceeded
- `503`: 6: Service Unavailable

**Response fields** (`Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.ItemConfiguration.Api.AssetCreationsResponse_`)

See [Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.ItemConfiguration.Api.AssetCreationsResponse_](#roblox-web-webapi-models-apipageresponse-roblox-itemconfiguration-api-assetcreationsresponse-) in Models.

**Response example:**
```json
{
  "previousPageCursor": "string",
  "nextPageCursor": "string",
  "data": [
    {
      "assetId": "...",
      "name": "..."
    }
  ]
}
```

**Error handling:** `429`: Retry with exponential backoff (start at 1s). `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://itemconfiguration.roblox.com/v1/creations/get-assets?assetType={VALUE}"
```

### GET `/v1/favorites/assets/{assetId}/count` [EXPERIMENTAL]

Gets the favorite count for the given asset Id.

**Server:** `https://catalog.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `assetId` | path | `integer` | Yes |  |

**Responses:**

- `200`: OK → `integer`
- `400`: 2: Invalid asset Id.

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://catalog.roblox.com/v1/favorites/assets/{ASSETID}/count"
```

### GET `/v1/favorites/bundles/{bundleId}/count` [EXPERIMENTAL]

Gets the favorite count for the given bundle Id.

**Server:** `https://catalog.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `bundleId` | path | `integer` | Yes |  |

**Responses:**

- `200`: OK → `integer`
- `400`: 2: Invalid bundle Id.

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://catalog.roblox.com/v1/favorites/bundles/{BUNDLEID}/count"
```

### GET `/v1/favorites/users/{userId}/assets/{assetId}/favorite`

Gets the favorite model for the asset and user.

**Server:** `https://catalog.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer` | Yes |  |
| `assetId` | path | `integer` | Yes |  |

**Responses:**

- `200`: OK → `Roblox.Catalog.Api.AssetFavoriteModel`
- `400`: 1: Invalid user Id. 2: Invalid asset Id.
- `401`: 0: Authorization has been denied for this request.

**Response fields** (`Roblox.Catalog.Api.AssetFavoriteModel`)

See [Roblox.Catalog.Api.AssetFavoriteModel](#roblox-catalog-api-assetfavoritemodel) in Models.

**Response example:**
```json
{
  "assetId": 0,
  "userId": 0,
  "created": "2024-01-01T00:00:00Z"
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://catalog.roblox.com/v1/favorites/users/{USERID}/assets/{ASSETID}/favorite"
```

### POST `/v1/favorites/users/{userId}/assets/{assetId}/favorite`

Create a favorite for an asset by the authenticated user.

**Server:** `https://catalog.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer` | Yes |  |
| `assetId` | path | `integer` | Yes |  |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: 1: Invalid user Id. 2: Invalid asset Id.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 6: You are not authorized to perform this action.
- `409`: 3: Asset is already favorited.
- `429`: 5: This action was floodchecked. Please try again later.

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `429`: Retry with exponential backoff (start at 1s). `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://catalog.roblox.com/v1/favorites/users/{USERID}/assets/{ASSETID}/favorite"
```

### DELETE `/v1/favorites/users/{userId}/assets/{assetId}/favorite`

Delete a favorite for an asset by the authenticated user.

**Server:** `https://catalog.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer` | Yes |  |
| `assetId` | path | `integer` | Yes |  |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: 1: Invalid user Id. 2: Invalid asset Id.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 6: You are not authorized to perform this action.
- `409`: 4: Asset is already not favorited.
- `429`: 5: This action was floodchecked. Please try again later.

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `429`: Retry with exponential backoff (start at 1s). `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X DELETE -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://catalog.roblox.com/v1/favorites/users/{USERID}/assets/{ASSETID}/favorite"
```

### GET `/v1/favorites/users/{userId}/bundles/{bundleId}/favorite`

Gets the favorite model for the bundle and user.

**Server:** `https://catalog.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer` | Yes |  |
| `bundleId` | path | `integer` | Yes |  |

**Responses:**

- `200`: OK → `Roblox.Catalog.Api.BundleFavoriteModel`
- `400`: 1: Invalid user Id. 2: Invalid bundle Id.
- `401`: 0: Authorization has been denied for this request.

**Response fields** (`Roblox.Catalog.Api.BundleFavoriteModel`)

See [Roblox.Catalog.Api.BundleFavoriteModel](#roblox-catalog-api-bundlefavoritemodel) in Models.

**Response example:**
```json
{
  "bundleId": 0,
  "userId": 0,
  "created": "2024-01-01T00:00:00Z"
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://catalog.roblox.com/v1/favorites/users/{USERID}/bundles/{BUNDLEID}/favorite"
```

### POST `/v1/favorites/users/{userId}/bundles/{bundleId}/favorite`

Create a favorite for the bundle by the authenticated user.

**Server:** `https://catalog.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer` | Yes |  |
| `bundleId` | path | `integer` | Yes |  |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: 1: Invalid user Id. 2: Invalid bundle Id.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 6: You are not authorized to perform this action.
- `409`: 3: Bundle is already favorited.
- `429`: 5: This action was floodchecked. Please try again later.

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `429`: Retry with exponential backoff (start at 1s). `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://catalog.roblox.com/v1/favorites/users/{USERID}/bundles/{BUNDLEID}/favorite"
```

### DELETE `/v1/favorites/users/{userId}/bundles/{bundleId}/favorite`

Delete favorite for the bundle by the authenticated user.

**Server:** `https://catalog.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer` | Yes |  |
| `bundleId` | path | `integer` | Yes |  |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: 1: Invalid user Id. 2: Invalid bundle Id.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 6: You are not authorized to perform this action.
- `409`: 4: Bundle is already not favorited.
- `429`: 5: This action was floodchecked. Please try again later.

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `429`: Retry with exponential backoff (start at 1s). `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X DELETE -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://catalog.roblox.com/v1/favorites/users/{USERID}/bundles/{BUNDLEID}/favorite"
```

### GET `/v1/favorites/users/{userId}/favorites/{assetTypeId}/assets` [EXPERIMENTAL]

Lists the marketplace assets favorited by a given user with the given assetTypeId.

**Server:** `https://catalog.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer` | Yes |  |
| `assetTypeId` | path | `integer` | Yes |  |
| `limit` | query | `integer enum (6 values)` | No | The number of results per request. Valid values: `10`, `18`, `24`, `25`, `50`, `100` |
| `cursor` | query | `string` | No | The paging cursor for the previous or next page. |
| `sortOrder` | query | `Asc \| Desc` | No | The order the results are sorted in. Valid values: `Asc`, `Desc` |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.Catalog.Api.CatalogSearchDetailedResponseItem_`
- `400`: 1: Invalid user Id. 8: Ascending order is not allowed. 11: Invalid asset type id.
- `500`: 99: Internal server error.

**Response fields** (`Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.Catalog.Api.CatalogSearchDetailedResponseItem_`)

See [Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.Catalog.Api.CatalogSearchDetailedResponseItem_](#roblox-web-webapi-models-apipageresponse-roblox-catalog-api-catalogsearchdetailedresponseitem-) in Models.

**Response example:**
```json
{
  "previousPageCursor": "string",
  "nextPageCursor": "string",
  "data": [
    {
      "id": "...",
      "itemType": "...",
      "assetType": "...",
      "bundleType": "...",
      "isRecolorable": "...",
      "name": "..."
    }
  ]
}
```

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://catalog.roblox.com/v1/favorites/users/{USERID}/favorites/{ASSETTYPEID}/assets"
```

### GET `/v1/favorites/users/{userId}/favorites/{subtypeId}/bundles`

Lists the bundles favorited by a given user with the given bundle subtypeId.Switched to EAAS style pagination cursors since July 2024.

**Server:** `https://catalog.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer` | Yes |  |
| `subtypeId` | path | `integer` | Yes |  |
| `itemsPerPage` | query | `integer` | No |  |
| `cursor` | query | `string` | No |  |
| `isPrevious` | query | `boolean` | No |  |

**Responses:**

- `200`: OK → `Roblox.Catalog.Api.FavoriteBundlesResponse`
- `400`: 1: Invalid user Id. 3: Cannot request so many bundles at once. 10: Invalid previous pagination request. Please provide a cursor when isPrevious is true
- `401`: 0: Authorization has been denied for this request.
- `403`: 6: You are not authorized to perform this action.
- `500`: 11: Internal server error. Please check if you have provided correct pagination cursor

**Response fields** (`Roblox.Catalog.Api.FavoriteBundlesResponse`)

See [Roblox.Catalog.Api.FavoriteBundlesResponse](#roblox-catalog-api-favoritebundlesresponse) in Models.

**Response example:**
```json
{
  "favorites": [
    {
      "id": "...",
      "name": "...",
      "description": "...",
      "bundleType": "...",
      "isRecolorable": "...",
      "items": "..."
    }
  ],
  "moreFavorites": false,
  "nextCursor": "string",
  "previousCursor": "string"
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://catalog.roblox.com/v1/favorites/users/{USERID}/favorites/{SUBTYPEID}/bundles"
```

### POST `/v1/games/{gameId}/thumbnail/image`

Uploads a game thumbnail.

**Server:** `https://publish.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gameId` | path | `integer` | Yes | The universe Id. |

**Responses:**

- `200`: OK → `Roblox.Publish.Api.UploadResponse`
- `400`: 1: File uploaded does not match known image format. Try converting to png. 2: File not present in request.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 5: You do not have permission to manage this item.
- `404`: 4: Target item is invalid or does not exist.
- `429`: 3: You're uploading too much, please wait and try again later.

**Response fields** (`Roblox.Publish.Api.UploadResponse`)

See [Roblox.Publish.Api.UploadResponse](#roblox-publish-api-uploadresponse) in Models.

**Response example:**
```json
{
  "targetId": 0
}
```

**Error handling:** `429`: Retry with exponential backoff (start at 1s). `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://publish.roblox.com/v1/games/{GAMEID}/thumbnail/image" \
  -H "Content-Type: application/json" \
  -d '{"key": "value"}'
```

### GET `/v1/localization-table/tables/{assetId}` [EXPERIMENTAL]

Get table information by the assetId of the table.

**Server:** `https://localizationtables.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `assetId` | path | `integer` | Yes | The asset id associated with the table. |

**Responses:**

- `200`: OK → `Roblox.LocalizationTables.Api.GetTableResponse`
- `400`: 12: Invalid asset id.
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
  "https://localizationtables.roblox.com/v1/localization-table/tables/{ASSETID}"
```

### GET `/v1/marAssetHash/{marAssetHash}/marCheckSum/{marCheckSum}`

Retrieves an asset by its mar (moderation agnostic) hash and mar (moderation agnostic) checksum.

**Server:** `https://assetdelivery.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `marAssetHash` | path | `string` | Yes | The mar (moderation agnostic) hash of the asset to retrieve. |
| `marCheckSum` | path | `string` | Yes | The mar (moderation agnostic) checksum of the asset to retrieve. |
| `Accept-Encoding` | header | `string` | Yes |  |
| `Roblox-Place-Id` | header | `integer` | Yes |  |
| `AssetType` | header | `string` | Yes |  |
| `AssetFormat` | header | `string` | Yes |  |
| `Roblox-AssetFormat` | header | `string` | Yes |  |
| `skipSigningScripts` | query | `boolean` | No |  |
| `clientInsert` | query | `integer` | No |  |
| `scriptinsert` | query | `integer` | No |  |
| `modulePlaceId` | query | `integer` | No |  |
| `serverplaceid` | query | `integer` | No |  |
| `expectedAssetType` | query | `string` | No |  |

**Responses:**

- `200`: OK
- `400`: 2: invalid server request 3: Encoding cannot be empty
- `404`: 5: Asset hash cannot be empty

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://assetdelivery.roblox.com/v1/marAssetHash/{MARASSETHASH}/marCheckSum/{MARCHECKSUM}"
```

### GET `/v1/plugins` [EXPERIMENTAL]

Gets plugin details by ids.

**Server:** `https://develop.roblox.com`

**Auth:** 

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `pluginIds` | query | `integer[]` | Yes | The plugin ids. |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.Web.Responses.Plugins.PluginResponse_`
- `400`: 1: Too many ids. 2: The format of the ids are invalid.

**Response fields** (`Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.Web.Responses.Plugins.PluginResponse_`)

See [Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.Web.Responses.Plugins.PluginResponse_](#roblox-web-webapi-models-apiarrayresponse-roblox-web-responses-plugins-pluginresponse-) in Models.

**Response example:**
```json
{
  "data": [
    {
      "id": "...",
      "name": "...",
      "description": "...",
      "commentsEnabled": "...",
      "versionId": "...",
      "created": "..."
    }
  ]
}
```

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://develop.roblox.com/v1/plugins?pluginIds={VALUE}"
```

### PATCH `/v1/plugins/{pluginId}` [EXPERIMENTAL]

Updates a plugin.

**Server:** `https://develop.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `pluginId` | path | `integer` | Yes | The id of the plugin. |

**Request Body:** `application/json` — Type: `Roblox.Develop.Api.UpdatePluginRequest`

See [Roblox.Develop.Api.UpdatePluginRequest](#roblox-develop-api-updatepluginrequest) in Models.

**Request example:**
```json
{
  "name": "string",
  "description": "string",
  "commentsEnabled": false
}
```

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: 5: Description too long. 6: Text moderated. 7: Invalid name. 8: The request body is missing.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 4: Insufficient permissions.
- `404`: 3: The id is invalid.

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X PATCH -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://develop.roblox.com/v1/plugins/{PLUGINID}" \
  -H "Content-Type: application/json" \
  -d '{
  "name": "string",
  "description": "string",
  "commentsEnabled": false
}'
```

### POST `/v1/plugins/{pluginId}/icon`

Overwrites a plugin icon with a new one.

**Server:** `https://publish.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `pluginId` | path | `integer` | Yes | The plugin Id. |

**Responses:**

- `200`: OK → `Roblox.Publish.Api.UploadResponse`
- `400`: 2: File not present in request.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 5: You do not have permission to manage this item.
- `404`: 4: Target item is invalid or does not exist.
- `429`: 3: You're uploading too much, please wait and try again later.

**Response fields** (`Roblox.Publish.Api.UploadResponse`)

See [Roblox.Publish.Api.UploadResponse](#roblox-publish-api-uploadresponse) in Models.

**Response example:**
```json
{
  "targetId": 0
}
```

**Error handling:** `429`: Retry with exponential backoff (start at 1s). `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://publish.roblox.com/v1/plugins/{PLUGINID}/icon" \
  -H "Content-Type: application/json" \
  -d '{"key": "value"}'
```

### GET `/v1/preferences/publishing` [EXPERIMENTAL]

**Server:** `https://itemconfiguration.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | query | `integer` | No |  |

**Responses:**

- `200`: OK → `Roblox.ItemConfiguration.Api.Models.Response.PublishingPreferences.PublishingPreferencesResponse`
- `401`: 0: Authorization has been denied for this request.

**Response fields** (`Roblox.ItemConfiguration.Api.Models.Response.PublishingPreferences.PublishingPreferencesResponse`)

See [Roblox.ItemConfiguration.Api.Models.Response.PublishingPreferences.PublishingPreferencesResponse](#roblox-itemconfiguration-api-models-response-publishingpreferences-publishingpreferencesresponse) in Models.

**Response example:**
```json
{
  "id": "string",
  "creatorUserId": 0,
  "creatorGroupId": 0,
  "publishingType": 0,
  "saleLocationType": 0,
  "places": [
    0
  ]
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://itemconfiguration.roblox.com/v1/preferences/publishing"
```

### POST `/v1/preferences/publishing` [EXPERIMENTAL]

**Server:** `https://itemconfiguration.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Request Body:** `application/json` — Type: `Roblox.ItemConfiguration.Api.Models.Request.PublishingPreferences.CreatePublishingPreferencesRequest`

See [Roblox.ItemConfiguration.Api.Models.Request.PublishingPreferences.CreatePublishingPreferencesRequest](#roblox-itemconfiguration-api-models-request-publishingpreferences-createpublishingpreferencesrequest) in Models.

**Request example:**
```json
{
  "creatorUserId": 0,
  "creatorGroupId": 0,
  "publishingType": 0,
  "saleLocationType": 0,
  "places": [
    0
  ],
  "priceInRobux": 0
}
```

**Responses:**

- `200`: OK → `Roblox.ItemConfiguration.Api.Models.Response.PublishingPreferences.PublishingPreferencesResponse`
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed

**Response fields** (`Roblox.ItemConfiguration.Api.Models.Response.PublishingPreferences.PublishingPreferencesResponse`)

See [Roblox.ItemConfiguration.Api.Models.Response.PublishingPreferences.PublishingPreferencesResponse](#roblox-itemconfiguration-api-models-response-publishingpreferences-publishingpreferencesresponse) in Models.

**Response example:**
```json
{
  "id": "string",
  "creatorUserId": 0,
  "creatorGroupId": 0,
  "publishingType": 0,
  "saleLocationType": 0,
  "places": [
    0
  ]
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://itemconfiguration.roblox.com/v1/preferences/publishing" \
  -H "Content-Type: application/json" \
  -d '{
  "creatorUserId": 0,
  "creatorGroupId": 0,
  "publishingType": 0,
  "saleLocationType": 0,
  "places": [
    0
  ],
  "priceInRobux": 0
}'
```

### PATCH `/v1/preferences/publishing` [EXPERIMENTAL]

**Server:** `https://itemconfiguration.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Request Body:** `application/json` — Type: `Roblox.ItemConfiguration.Api.Models.Request.PublishingPreferences.UpdatePublishingPreferencesRequest`

See [Roblox.ItemConfiguration.Api.Models.Request.PublishingPreferences.UpdatePublishingPreferencesRequest](#roblox-itemconfiguration-api-models-request-publishingpreferences-updatepublishingpreferencesrequest) in Models.

**Request example:**
```json
{
  "creatorUserId": 0,
  "creatorGroupId": 0,
  "publishingType": 0,
  "saleLocationType": 0,
  "places": [
    0
  ],
  "priceInRobux": 0
}
```

**Responses:**

- `200`: OK → `Roblox.ItemConfiguration.Api.Models.Response.PublishingPreferences.PublishingPreferencesResponse`
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed

**Response fields** (`Roblox.ItemConfiguration.Api.Models.Response.PublishingPreferences.PublishingPreferencesResponse`)

See [Roblox.ItemConfiguration.Api.Models.Response.PublishingPreferences.PublishingPreferencesResponse](#roblox-itemconfiguration-api-models-response-publishingpreferences-publishingpreferencesresponse) in Models.

**Response example:**
```json
{
  "id": "string",
  "creatorUserId": 0,
  "creatorGroupId": 0,
  "publishingType": 0,
  "saleLocationType": 0,
  "places": [
    0
  ]
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X PATCH -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://itemconfiguration.roblox.com/v1/preferences/publishing" \
  -H "Content-Type: application/json" \
  -d '{
  "creatorUserId": 0,
  "creatorGroupId": 0,
  "publishingType": 0,
  "saleLocationType": 0,
  "places": [
    0
  ],
  "priceInRobux": 0
}'
```

### DELETE `/v1/preferences/publishing` [EXPERIMENTAL]

**Server:** `https://itemconfiguration.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | query | `integer` | No |  |

**Responses:**

- `200`: OK
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X DELETE -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://itemconfiguration.roblox.com/v1/preferences/publishing"
```

### GET `/v1/subcategories`

Lists Subcategory Names and their Ids.

**Server:** `https://catalog.roblox.com`

**Auth:** 

**Responses:**

- `200`: OK → `object`

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://catalog.roblox.com/v1/subcategories"
```

### POST `/v1/topic/get-topics`

Gets topics for a populated request, or trending queries when the request has no topic inputs.
Topics and queries are mutually exclusive in the response.

**Server:** `https://catalog.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Request Body:** `application/json` — Type: `Roblox.Catalog.Api.TopicRequestModel`

See [Roblox.Catalog.Api.TopicRequestModel](#roblox-catalog-api-topicrequestmodel) in Models.

**Request example:**
```json
{
  "items": [
    {
      "TargetId": "...",
      "ItemType": "..."
    }
  ],
  "selectTopics": [
    "string"
  ],
  "inputQuery": "string",
  "maxResult": 0,
  "genderType": 1
}
```

**Responses:**

- `200`: OK → `Roblox.Catalog.Api.TopicResponse`
- `403`: 0: Token Validation Failed

**Response fields** (`Roblox.Catalog.Api.TopicResponse`)

See [Roblox.Catalog.Api.TopicResponse](#roblox-catalog-api-topicresponse) in Models.

**Response example:**
```json
{
  "topics": [
    {
      "displayName": "...",
      "originalTopicName": "..."
    }
  ],
  "queries": [
    "string"
  ],
  "error": {
    "Message": "string",
    "Code": 0
  }
}
```

**Error handling:** `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://catalog.roblox.com/v1/topic/get-topics" \
  -H "Content-Type: application/json" \
  -d '{
  "items": [
    {
      "TargetId": "...",
      "ItemType": "..."
    }
  ],
  "selectTopics": [
    "string"
  ],
  "inputQuery": "string",
  "maxResult": 0,
  "genderType": 1
}'
```

### GET `/v1/user/groups/canmanagegamesoritems` [EXPERIMENTAL]

Gets a list of groups a user can manage games or items for.

**Server:** `https://develop.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.Api.Develop.Models.GroupModel_`
- `401`: 0: Authorization has been denied for this request.

**Response fields** (`Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.Api.Develop.Models.GroupModel_`)

See [Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.Api.Develop.Models.GroupModel_](#roblox-web-webapi-models-apiarrayresponse-roblox-api-develop-models-groupmodel-) in Models.

**Response example:**
```json
{
  "data": [
    {
      "id": "...",
      "name": "..."
    }
  ]
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://develop.roblox.com/v1/user/groups/canmanagegamesoritems"
```

### GET `/v1/users/{userId}/bundles`

Lists the bundles owned by a given user.

**Server:** `https://catalog.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer` | Yes |  |
| `cursor` | query | `string` | No |  |
| `limit` | query | `integer` | No |  |
| `sortOrder` | query | `1 \| 2` | No | Valid values: `1`, `2` |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.Catalog.Api.OwnedBundleModel_`
- `400`: 1: Invalid bundle

**Response fields** (`Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.Catalog.Api.OwnedBundleModel_`)

See [Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.Catalog.Api.OwnedBundleModel_](#roblox-web-webapi-models-apipageresponse-roblox-catalog-api-ownedbundlemodel-) in Models.

**Response example:**
```json
{
  "previousPageCursor": "string",
  "nextPageCursor": "string",
  "data": [
    {
      "id": "...",
      "name": "...",
      "bundleType": "...",
      "creator": "..."
    }
  ]
}
```

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://catalog.roblox.com/v1/users/{USERID}/bundles"
```

### GET `/v1/users/{userId}/bundles/{bundleType}` [EXPERIMENTAL]

**Server:** `https://catalog.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer` | Yes |  |
| `bundleType` | path | `1 \| 2 \| 3 \| 4` | Yes | ['BodyParts' = 1, 'AvatarAnimations' = 2, 'Shoes' = 3, 'DynamicHead' = 4] Valid values: `1`, `2`, `3`, `4` |
| `cursor` | query | `string` | Yes |  |
| `limit` | query | `integer` | No |  |
| `sortOrder` | query | `1 \| 2` | No | ['Asc' = 1, 'Desc' = 2] Valid values: `1`, `2` |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.Catalog.Api.OwnedBundleModel_`

**Response fields** (`Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.Catalog.Api.OwnedBundleModel_`)

See [Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.Catalog.Api.OwnedBundleModel_](#roblox-web-webapi-models-apipageresponse-roblox-catalog-api-ownedbundlemodel-) in Models.

**Response example:**
```json
{
  "previousPageCursor": "string",
  "nextPageCursor": "string",
  "data": [
    {
      "id": "...",
      "name": "...",
      "bundleType": "...",
      "creator": "..."
    }
  ]
}
```

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://catalog.roblox.com/v1/users/{USERID}/bundles/{BUNDLETYPE}?cursor={VALUE}"
```

### GET `/v1/users/{userId}/currently-wearing`

Gets a list of asset ids that the user is currently wearing.

**Server:** `https://avatar.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer` | Yes | The user id. |
| `Roblox-Place-Id` | header | `integer` | No |  |

**Responses:**

- `200`: OK → `Roblox.Api.Avatar.Models.AssetIdListModel`
- `400`: 1: The specified user does not exist. 2: An account for the given userId does not exist!

**Response fields** (`Roblox.Api.Avatar.Models.AssetIdListModel`)

See [Roblox.Api.Avatar.Models.AssetIdListModel](#roblox-api-avatar-models-assetidlistmodel) in Models.

**Response example:**
```json
{
  "assetIds": [
    0
  ]
}
```

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://avatar.roblox.com/v1/users/{USERID}/currently-wearing"
```

### GET `/v1/users/{userId}/items/{itemType}/{itemTargetId}`

Gets owned items of the specified item type. Game Servers can make requests for any user, but can only make requests for game passes that belong to the place sending the request.
Place creators can make requests as if they were the Game Server.

**Server:** `https://inventory.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer` | Yes | ID of the user in question |
| `itemType` | path | `0 \| 1 \| 2 \| 3 \| 4` | Yes | Type of the item in question (i.e. Asset, GamePass, Badge, Bundle) Valid values: `0`, `1`, `2`, `3`, `4` |
| `itemTargetId` | path | `integer` | Yes | ID of the item in question |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.Inventory.Api.Models.IItemModel_`
- `400`: 1: The specified user does not exist! 5: The specified game pass does not exist! Are you using the new game pass ID? 6: The specified item type does not exist. 7: The specified Asset does not exist! 10: The specified asset is not a badge! 12: The specified bundle does not exist!

**Response fields** (`Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.Inventory.Api.Models.IItemModel_`)

See [Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.Inventory.Api.Models.IItemModel_](#roblox-web-webapi-models-apipageresponse-roblox-inventory-api-models-iitemmodel-) in Models.

**Response example:**
```json
{
  "previousPageCursor": "string",
  "nextPageCursor": "string",
  "data": [
    {
      "id": "...",
      "name": "...",
      "type": "...",
      "instanceId": "..."
    }
  ]
}
```

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://inventory.roblox.com/v1/users/{USERID}/items/{ITEMTYPE}/{ITEMTARGETID}"
```

### GET `/v2/asset`

**Server:** `https://assetdelivery.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `Accept-Encoding` | header | `string` | Yes |  |
| `Roblox-Place-Id` | header | `integer` | Yes |  |
| `AssetType` | header | `string` | Yes |  |
| `AssetFormat` | header | `string` | Yes |  |
| `Roblox-AssetFormat` | header | `string` | Yes |  |
| `Roblox-Usage-Context` | header | `string` | No |  |
| `id` | query | `integer` | No |  |
| `userAssetId` | query | `integer` | No |  |
| `assetVersionId` | query | `integer` | No |  |
| `version` | query | `integer` | No |  |
| `universeId` | query | `integer` | No |  |
| `clientInsert` | query | `integer` | No |  |
| `scriptinsert` | query | `integer` | No |  |
| `modulePlaceId` | query | `integer` | No |  |
| `serverplaceid` | query | `string` | No |  |
| `assetName` | query | `string` | No |  |
| `hash` | query | `string` | No |  |
| `marAssetHash` | query | `string` | No |  |
| `marCheckSum` | query | `string` | No |  |
| `expectedAssetType` | query | `string` | No |  |
| `skipSigningScripts` | query | `boolean` | No |  |
| `permissionContext` | query | `string` | No |  |
| `doNotFallbackToBaselineRepresentation` | query | `boolean` | No |  |
| `contentRepresentationPriorityList` | query | `string` | No |  |
| `accessContext` | query | `string` | No |  |

**Responses:**

- `200`: OK

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://assetdelivery.roblox.com/v2/asset"
```

### GET `/v2/assetId/{assetId}`

**Server:** `https://assetdelivery.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `assetId` | path | `integer` | Yes |  |
| `Accept-Encoding` | header | `string` | Yes |  |
| `Roblox-Place-Id` | header | `integer` | Yes |  |
| `AssetType` | header | `string` | Yes |  |
| `AssetFormat` | header | `string` | Yes |  |
| `Roblox-AssetFormat` | header | `string` | Yes |  |
| `Roblox-Usage-Context` | header | `string` | No |  |
| `skipSigningScripts` | query | `boolean` | No |  |
| `clientInsert` | query | `integer` | No |  |
| `scriptinsert` | query | `integer` | No |  |
| `modulePlaceId` | query | `integer` | No |  |
| `serverplaceid` | query | `integer` | No |  |
| `expectedAssetType` | query | `string` | No |  |
| `doNotFallbackToBaselineRepresentation` | query | `boolean` | No |  |
| `contentRepresentationPriorityList` | query | `string` | No |  |
| `accessContext` | query | `string` | No |  |

**Responses:**

- `200`: OK

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://assetdelivery.roblox.com/v2/assetId/{ASSETID}"
```

### GET `/v2/assetId/{assetId}/version/{versionNumber}`

**Server:** `https://assetdelivery.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `assetId` | path | `integer` | Yes |  |
| `versionNumber` | path | `integer` | Yes |  |
| `Accept-Encoding` | header | `string` | Yes |  |
| `Roblox-Place-Id` | header | `integer` | Yes |  |
| `AssetType` | header | `string` | Yes |  |
| `AssetFormat` | header | `string` | Yes |  |
| `Roblox-AssetFormat` | header | `string` | Yes |  |
| `Roblox-Usage-Context` | header | `string` | No |  |
| `skipSigningScripts` | query | `boolean` | No |  |
| `clientInsert` | query | `integer` | No |  |
| `scriptinsert` | query | `integer` | No |  |
| `modulePlaceId` | query | `integer` | No |  |
| `serverplaceid` | query | `integer` | No |  |
| `expectedAssetType` | query | `string` | No |  |
| `doNotFallbackToBaselineRepresentation` | query | `boolean` | No |  |
| `contentRepresentationPriorityList` | query | `string` | No |  |
| `accessContext` | query | `string` | No |  |

**Responses:**

- `200`: OK

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://assetdelivery.roblox.com/v2/assetId/{ASSETID}/version/{VERSIONNUMBER}"
```

### POST `/v2/assets/batch`

**Server:** `https://assetdelivery.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `Roblox-Place-Id` | header | `integer` | Yes |  |
| `Roblox-Browser-Asset-Request` | header | `string` | Yes |  |

**Request Body:** `application/json` — Type: `Roblox.Web.Assets.BatchAssetRequestItem[]`

See [Roblox.Web.Assets.BatchAssetRequestItem](#roblox-web-assets-batchassetrequestitem) in Models.

**Responses:**

- `200`: OK

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://assetdelivery.roblox.com/v2/assets/batch" \
  -H "Content-Type: application/json" \
  -d '[
  {
    "assetName": "string",
    "assetType": "string",
    "clientInsert": false,
    "placeId": 0,
    "requestId": "string",
    "scriptInsert": false
  }
]'
```

### GET `/v2/assets/{assetId}/bundles`

Lists bundles that contain the given asset (hydrated search-detail shape for marketplace).

**Server:** `https://catalog.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `assetId` | path | `integer` | Yes | Asset id. |
| `Roblox-Place-Id` | header | `integer` | Yes | Roblox-Place-Id header. |
| `Roblox-Game-Id` | header | `string` | Yes | Roblox-Game-Id header. |
| `limit` | query | `10 \| 25 \| 50 \| 100` | No | The number of results per request. Valid values: `10`, `25`, `50`, `100` |
| `cursor` | query | `string` | No | The paging cursor for the previous or next page. |
| `sortOrder` | query | `Asc \| Desc` | No | The order the results are sorted in. Valid values: `Asc`, `Desc` |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.Catalog.Api.CatalogSearchDetailedResponseItem_`
- `400`: 1: Invalid assetId 4: Invalid Cursor.
- `403`: 7: User is unauthorized.

**Response fields** (`Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.Catalog.Api.CatalogSearchDetailedResponseItem_`)

See [Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.Catalog.Api.CatalogSearchDetailedResponseItem_](#roblox-web-webapi-models-apipageresponse-roblox-catalog-api-catalogsearchdetailedresponseitem-) in Models.

**Response example:**
```json
{
  "previousPageCursor": "string",
  "nextPageCursor": "string",
  "data": [
    {
      "id": "...",
      "itemType": "...",
      "assetType": "...",
      "bundleType": "...",
      "isRecolorable": "...",
      "name": "..."
    }
  ]
}
```

**Error handling:** `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://catalog.roblox.com/v2/assets/{ASSETID}/bundles"
```

### GET `/v2/assets/{assetId}/owners`

Gets a list of owners of an asset.

**Server:** `https://inventory.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `assetId` | path | `integer` | Yes | The asset id. |
| `limit` | query | `10 \| 25 \| 50 \| 100` | No | The number of results per request. Valid values: `10`, `25`, `50`, `100` |
| `cursor` | query | `string` | No | The paging cursor for the previous or next page. |
| `sortOrder` | query | `Asc \| Desc` | No | Sorted by userAssetId Valid values: `Asc`, `Desc` |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.Inventory.Api.V2.AssetOwnerResponse_`
- `400`: 1: The asset id is invalid.
- `403`: 2: You do not have permission to view the owners of this asset.

**Response fields** (`Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.Inventory.Api.V2.AssetOwnerResponse_`)

See [Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.Inventory.Api.V2.AssetOwnerResponse_](#roblox-web-webapi-models-apipageresponse-roblox-inventory-api-v2-assetownerresponse-) in Models.

**Response example:**
```json
{
  "previousPageCursor": "string",
  "nextPageCursor": "string",
  "data": [
    {
      "id": "...",
      "collectibleItemInstanceId": "...",
      "serialNumber": "...",
      "owner": "...",
      "created": "...",
      "updated": "..."
    }
  ]
}
```

**Error handling:** `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://inventory.roblox.com/v2/assets/{ASSETID}/owners"
```

### GET `/v2/assets/{id}/versions` *(deprecated)*

Retrieves asset information for the specified asset ID. The authenticated user must be able to manage the asset
or granted by package permission.

Use OpenCloud Assets API instead.

**Server:** `https://develop.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `id` | path | `integer` | Yes | The ID of the asset.Roblox.Platform.Assets.IAsset |
| `Roblox-Place-Id` | header | `integer` | Yes | The ID of the place.Roblox.Platform.Assets.IPlace |
| `limit` | query | `10 \| 25 \| 50 \| 100` | No | The number of results per request. Valid values: `10`, `25`, `50`, `100` |
| `cursor` | query | `string` | No | The paging cursor for the previous or next page. |
| `sortOrder` | query | `Asc \| Desc` | No | Sort by version number, default is desc. Valid values: `Asc`, `Desc` |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.Api.Develop.AssetVersion_`

**Response fields** (`Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.Api.Develop.AssetVersion_`)

See [Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.Api.Develop.AssetVersion_](#roblox-web-webapi-models-apipageresponse-roblox-api-develop-assetversion-) in Models.

**Response example:**
```json
{
  "previousPageCursor": "string",
  "nextPageCursor": "string",
  "data": [
    {
      "Id": "...",
      "assetId": "...",
      "assetVersionNumber": "...",
      "creatorType": "...",
      "creatorTargetId": "...",
      "creatingUniverseId": "..."
    }
  ]
}
```

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://develop.roblox.com/v2/assets/{ID}/versions"
```

### GET `/v2/collectible-items/{collectibleItemId}/owners`

Gets a list of owners of a collectible item.

**Server:** `https://inventory.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `collectibleItemId` | path | `string` | Yes | The collectible item ID. |
| `limit` | query | `integer` | No | The number of results per request. |
| `cursor` | query | `string` | No | The paging cursor for the previous or next page. |
| `sortOrder` | query | `1 \| 2` | No | The order the results are sorted in. Valid values: `1`, `2` |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.Inventory.Api.V2.CollectibleItemOwnerResponse_`
- `400`: 1: The collectible item id is invalid.
- `401`: 0: Authorization has been denied for this request.
- `403`: 2: You do not have permission to view the owners of this item.

**Response fields** (`Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.Inventory.Api.V2.CollectibleItemOwnerResponse_`)

See [Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.Inventory.Api.V2.CollectibleItemOwnerResponse_](#roblox-web-webapi-models-apipageresponse-roblox-inventory-api-v2-collectibleitemownerresponse-) in Models.

**Response example:**
```json
{
  "previousPageCursor": "string",
  "nextPageCursor": "string",
  "data": [
    {
      "collectibleItemInstanceId": "...",
      "serialNumber": "...",
      "owner": "..."
    }
  ]
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://inventory.roblox.com/v2/collectible-items/{COLLECTIBLEITEMID}/owners"
```

### DELETE `/v2/inventory/asset/{assetId}`

Give up an asset owned by the authenticated user.
Assets that are created by Roblox user or are limited edition are not eligible for deletion
and will return NotEligibleForDelete.

**Server:** `https://inventory.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `assetId` | path | `integer` | Yes | ID of the asset to delete. |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `401`: 0: Authorization has been denied for this request. 4: You are not authorized.
- `403`: 0: Token Validation Failed 2: You don't own the specified item. 3: The item is not allowed to be deleted.
- `404`: 1: The item does not exist.
- `500`: 0: An unknown error occured.

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X DELETE -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://inventory.roblox.com/v2/inventory/asset/{ASSETID}"
```

### GET `/v2/marAssetHash/{marAssetHash}/marCheckSum/{marCheckSum}`

**Server:** `https://assetdelivery.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `marAssetHash` | path | `string` | Yes |  |
| `marCheckSum` | path | `string` | Yes |  |
| `Accept-Encoding` | header | `string` | Yes |  |
| `Roblox-Place-Id` | header | `integer` | Yes |  |
| `AssetType` | header | `string` | Yes |  |
| `AssetFormat` | header | `string` | Yes |  |
| `Roblox-AssetFormat` | header | `string` | Yes |  |
| `skipSigningScripts` | query | `boolean` | No |  |
| `clientInsert` | query | `integer` | No |  |
| `scriptinsert` | query | `integer` | No |  |
| `modulePlaceId` | query | `integer` | No |  |
| `serverplaceid` | query | `integer` | No |  |
| `expectedAssetType` | query | `string` | No |  |

**Responses:**

- `200`: OK

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://assetdelivery.roblox.com/v2/marAssetHash/{MARASSETHASH}/marCheckSum/{MARCHECKSUM}"
```

### GET `/v2/search/items/details` [EXPERIMENTAL]

Search for catalog items.

This endpoint is for search by item type ids.

**Server:** `https://catalog.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `Taxonomy` | query | `string` | No |  |
| `AssetTypeIds` | query | `integer[]` | No |  |
| `BundleTypeIds` | query | `integer[]` | No |  |
| `CategoryFilter` | query | `integer enum (8 values)` | No | The category filter types, representing generic collections of catalog items requested by client. ['None' = 0, 'Featured' = 1, 'Collectibles' = 2, 'CommunityCreations' = 3, 'Landing' = 4, 'Premium' = 5, 'Recommended' = 6, 'HighDefinition' = 7] Valid values: `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7` |
| `SortAggregation` | query | `integer enum (6 values)` | No | ['Past12Hours' = 0, 'PastDay' = 1, 'Past3Days' = 2, 'PastWeek' = 3, 'PastMonth' = 4, 'AllTime' = 5] Valid values: `0`, `1`, `2`, `3`, `4`, `5` |
| `SortType` | query | `integer enum (6 values)` | No | Price values to be consolidated after roll out to api site. ['Relevance' = 0, 'Favorited' = 1, 'Sales' = 2, 'Created' = 3, 'Updated' = 3, 'PriceAsc' = 4, 'PriceDesc' = 5] Valid values: `0`, `1`, `2`, `3`, `4`, `5` |
| `CreatorType` | query | `0 \| 1 \| 2` | No | ['All' = 0, 'User' = 1, 'Group' = 2] Valid values: `0`, `1`, `2` |
| `CreatorTargetId` | query | `integer` | No |  |
| `CreatorName` | query | `string` | No |  |
| `MaxPrice` | query | `integer` | No |  |
| `MinPrice` | query | `integer` | No |  |
| `Keyword` | query | `string` | No |  |
| `IncludeNotForSale` | query | `boolean` | No |  |
| `TriggeredByTopicDiscovery` | query | `boolean` | No |  |
| `SalesTypeFilter` | query | `0 \| 1 \| 2 \| 3 \| 4` | No | The Sales Type filter options for search. ['Unknown' = 0, 'All' = 1, 'Collectibles' = 2, 'Premium' = 3, 'TimedOptions' = 4] Valid values: `0`, `1`, `2`, `3`, `4` |
| `Topics` | query | `string` | No | The input topics format is split by ",". E.g "topics=cat,hat,red". |
| `limit` | query | `10 \| 28 \| 30 \| 60 \| 120` | No | The number of results per request. Valid values: `10`, `28`, `30`, `60`, `120` |
| `cursor` | query | `string` | No | The paging cursor for the previous or next page. |
| `sortOrder` | query | `Desc` | No | The order the results are sorted in. Valid values: `Desc` |

**Responses:**

- `200`: OK → `Roblox.Catalog.Api.CatalogSearchPageResponse_Roblox.Catalog.Api.CatalogSearchDetailedResponseItemV2_`
- `400`: 1: Category subcategory selection not supported. 2: Creator id not found. 3: Creator type not found or cannot search by CreatorTargetId with CreatorType.All 4: Genre not found. 5: Sort combination not supported. 6: Invalid price range. 10: StartRequest is invalid.
- `403`: 7: User is unauthorized. 22: In-experience search is denied for this place or universe.
- `429`: 8: The flood limit has been exceeded. 8: The flood limit has been exceeded.
- `503`: 18: Search request timed out

**Response fields** (`Roblox.Catalog.Api.CatalogSearchPageResponse_Roblox.Catalog.Api.CatalogSearchDetailedResponseItemV2_`)

See [Roblox.Catalog.Api.CatalogSearchPageResponse_Roblox.Catalog.Api.CatalogSearchDetailedResponseItemV2_](#roblox-catalog-api-catalogsearchpageresponse-roblox-catalog-api-catalogsearchdetailedresponseitemv2-) in Models.

**Response example:**
```json
{
  "keyword": "string",
  "elasticsearchDebugInfo": {
    "elasticsearchQuery": "string",
    "isFromCache": false,
    "indexName": "string",
    "isTerminatedEarly": false,
    "isForceTerminationEnabledByRequest": false,
    "searchResultDataSource": "string"
  },
  "previousPageCursor": "string",
  "nextPageCursor": "string",
  "data": [
    {
      "bundledItems": "...",
      "taxonomy": "...",
      "itemCreatedUtc": "...",
      "discountInformation": "...",
      "license": "...",
      "id": "..."
    }
  ]
}
```

**Error handling:** `429`: Retry with exponential backoff (start at 1s). `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://catalog.roblox.com/v2/search/items/details"
```

### GET `/v2/users/{userId}/inventory`

Get user's inventory by multiple Roblox.Platform.Assets.AssetType.

GamePass and Badges not allowed.

**Server:** `https://inventory.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer` | Yes | The inventory owner's userId. |
| `assetTypes` | query | `string enum (89 values)[]` | Yes | The asset types to query. |
| `filterDisapprovedAssets` | query | `boolean` | No | Filters moderated assets when enabled. |
| `showApprovedOnly` | query | `boolean` | No | Filters moderated assets and assets pending review when enabled. |
| `limit` | query | `10 \| 25 \| 50 \| 100` | No | The number of results per request. Valid values: `10`, `25`, `50`, `100` |
| `cursor` | query | `string` | No | The paging cursor for the previous or next page. |
| `sortOrder` | query | `Asc \| Desc` | No | The order the results are sorted in. Valid values: `Asc`, `Desc` |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.Inventory.Api.V2.UserAssetItemModelV2_`
- `400`: 1: Invalid user Id. 2: Invalid asset type Id.
- `403`: 3: Insufficient permission. 4: You are not authorized to view this user's inventory.

**Response fields** (`Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.Inventory.Api.V2.UserAssetItemModelV2_`)

See [Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.Inventory.Api.V2.UserAssetItemModelV2_](#roblox-web-webapi-models-apipageresponse-roblox-inventory-api-v2-userassetitemmodelv2-) in Models.

**Response example:**
```json
{
  "previousPageCursor": "string",
  "nextPageCursor": "string",
  "data": [
    {
      "assetId": "...",
      "name": "...",
      "assetType": "...",
      "created": "..."
    }
  ]
}
```

**Error handling:** `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://inventory.roblox.com/v2/users/{USERID}/inventory?assetTypes={VALUE}"
```

## Models

### BatchGrantPermissionsRequest

Request object to grant one permission to multiple assets.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `subjectType` | `SubjectType` | No |  |
| `subjectId` | `string` | No | The subject ID to grant to. Must be empty for SubjectType 'All'. |
| `action` | `AssetAction` | No |  |
| `requests` | `AssetGrantRequest[]` | No | Array of asset grant requests. If populated, 'requests' will override 'assetIds'. |
| `assetIds` | `integer[]` | No | [Deprecated] The list of asset IDs to grant this permission to. 'requests' will be prioritized over this list. |
| `enableDeepAccessCheck` | `boolean` | No | [Do not use] An optional boolean to indicate if a deep access check should be done. This is not intended for public use. |

### BatchGrantPermissionsResponse

Response object to grant one permission to multiple assets.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `successAssetIds` | `integer[]` | No | The list of asset IDs that granted successfully. |
| `errors` | `GrantPermissionError[]` | No | The list of grants that had errors. |

### AssetPermissions.ErrorResponse

The error object for responses.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `error` | `AssetPermissions.Error` | No |  |

### Asset

Represents an asset.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `assetType` | `string` | No | The asset type. Required for [Create Asset](#POST-v1-assets). |
| `assetId` | `integer` | No | The unique identifier of the asset. Required for [Update Asset](#PATCH-v1-assets-_asset_). |
| `creationContext` | `CreationContext` | No |  |
| `description` | `string` | No | The description of the asset. Limit to 1000 characters. Required for [Create Asset](#POST-v1-assets). |
| `displayName` | `string` | No | Display name of the asset. Required for [Create Asset](#POST-v1-assets). |
| `path` | `string` | No | The returned resource path of the asset. Format: `assets/{assetId}`. Example: `assets/2205400862`. |
| `revisionId` | `string` | No | Revision ID of the asset. Equivalent to `versionNumber`. Every change of the asset automatically commits a new version. The format is an integer string. Example: `1`. |
| `revisionCreateTime` | `string` | No | The creation timestamp of the current revision. |
| `moderationResult` | `ModerationResult` | No |  |
| `icon` | `string` | No | The resource path for the icon. |
| `previews` | `Preview[]` | No | A list of previews, each with an asset path and alt text. Previews must be **Image** assets. |
| `state` | `State` | No |  |
| `socialLink` | `SocialLink` | No |  |

### OCV1.Assets.Operation

This resource represents a long-running operation that is the result of a network API call.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `path` | `string` | No | The server-assigned resource path. The default format is `operations/{operation_id}`. |
| `done` | `boolean` | No | If `false`, the operation is still in progress. If `true`, the operation is completed. |
| `error` | `OCV1.Assets.Status` | No |  |
| `response` | `Asset` | No |  |

### OCV1.Assets.Status

The logical error model explaining the error status.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `code` | `integer` | No | The HTTP status code. |
| `message` | `string` | No | The error message. |

### AssetVersion

An asset version.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `creationContext` | `CreationContext` | No |  |
| `path` | `string` | No | The returned resource path of the asset version. Format: `assets/{assetId}/versions/{version}`. Example: `assets/2205400862/versions/1`. |
| `moderationResult` | `ModerationResult` | No |  |
| `published` | `boolean` | No | Only applies to place asset types. Indicates if the place has been published or not. |

### GenerateSpeechAssetRequest

Specifies the text from which to generate speech and the voice style.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `text` | `string` | Yes | The text to be translated. |
| `speechStyle` | `GenerateSpeechAssetRequest_GeneratedSpeechStyle` | No | The style of the generated speech. |

### Operation

This resource represents a long-running operation that is the result of a
network API call.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `path` | `string` | No | The server-assigned path, which is only unique within the same service that originally returns it. If you use the default HTTP mapping, the `path` should be a resource path ending with `operations/{unique_id}`. |
| `metadata` | `GoogleProtobufAny` | No | Service-specific metadata associated with the operation.  It typically contains progress information and common metadata such as create time. Some services might not provide such metadata.  Any method that returns a long-running operation should document the metadata type, if any. |
| `done` | `boolean` | No | If the value is `false`, it means the operation is still in progress. If `true`, the operation is completed, and either `error` or `response` is available. |
| `error` | `Status` | No | The error result of the operation in case of failure or cancellation. |
| `response` | `GoogleProtobufAny` | No | The normal response of the operation in case of success.  If the original method returns no data on success, such as `Delete`, the response is `google.protobuf.Empty`.  If the original method is standard `Get`/`Create`/`Update`, the response should be the resource.  For other methods, the response should have the type `XxxResponse`, where `Xxx` is the original method name.  For example, if the original method name is `TakeSnapshot()`, the inferred response type is `TakeSnapshotResponse`. |

### ListAssetQuotasResponse

A list of AssetQuotas in the parent collection.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `assetQuotas` | `AssetQuota[]` | No | The AssetQuotas from the specified User. |
| `nextPageToken` | `string` | No | A token that you can send as a `pageToken` parameter to retrieve the next page. If this field is omitted, there are no subsequent pages. |

### Roblox.LocalizationTables.Api.GetTableResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | `string` | No |  |
| `name` | `string` | No |  |
| `ownerType` | `User \| Group` | No | Enum for valid OwnerTypes. |
| `ownerId` | `integer` | No |  |
| `assetId` | `integer` | No |  |

### Roblox.Publish.Api.UploadResponse

A response used when an upload has completed.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `targetId` | `integer` | No | The target Id of the uploaded item. |

### CreatorStoreAsset

Representation of a creator store asset.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `voting` | `any` | No | The asset's voting details. |
| `creator` | `any` | No | The asset creator's details. |
| `creatorStoreProduct` | `any` | No | The asset's product details. |
| `asset` | `any` | Yes | The asset information. |

### SearchCreatorStoreAssetsResponse

The response for the SearchCreatorStoreAssets endpoint.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `nextPageToken` | `string` | No | The page token to view the next page of results. |
| `queryFacets` | `any` | No | The applied and available facets of a query. |
| `creatorStoreAssets` | `CreatorStoreAsset[]` | Yes | The list of creator store assets returned by the search query. |
| `totalResults` | `integer` | Yes | The total number of results for the given search query. |
| `queryCorrection` | `any` | No | Query correction information, if a correction was available for the search query. |
| `filteredKeyword` | `string` | No | The filtered keyword that was used to search for assets, if applicable. |

### Roblox.Publish.Api.AssetQuotasResponse

Response model for asset quotas.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `quotas` | `Roblox.Publish.Api.AssetQuota[]` | No | A list of quotas. |

### Roblox.Web.Assets.BatchAssetRequestItem

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `assetName` | `string` | No |  |
| `assetType` | `string` | No |  |
| `clientInsert` | `boolean` | No |  |
| `placeId` | `integer` | No |  |
| `requestId` | `string` | No |  |
| `scriptInsert` | `boolean` | No |  |
| `serverPlaceId` | `integer` | No |  |
| `universeId` | `integer` | No |  |
| `accept` | `string` | No |  |
| `encoding` | `string` | No |  |
| `hash` | `string` | No |  |
| `userAssetId` | `integer` | No |  |
| `assetId` | `integer` | No |  |
| `version` | `integer` | No |  |
| `assetVersionId` | `integer` | No |  |
| `modulePlaceId` | `integer` | No |  |
| `assetFormat` | `string` | No |  |
| `roblox-assetFormat` | `string` | No |  |
| `assetResolutionMode` | `string` | No |  |
| `accessContext` | `string` | No |  |
| `usageContext` | `string` | No |  |
| `contentRepresentationPriorityList` | `string` | No |  |
| `doNotFallbackToBaselineRepresentation` | `boolean` | No |  |
| `xcachesplit` | `integer` | No |  |

### Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.Api.Develop.Models.Response.AssetVotingModel_

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | `Roblox.Api.Develop.Models.Response.AssetVotingModel[]` | No |  |

### Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.Catalog.Api.BundleDetailsModel_

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `previousPageCursor` | `string` | No |  |
| `nextPageCursor` | `string` | No |  |
| `data` | `Roblox.Catalog.Api.BundleDetailsModel[]` | No |  |

### Roblox.Publish.Api.UploadAudioRequest

A request model for uploading an audio file.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | `string` | No | Name for the audio file. |
| `file` | `string` | No | File to be uploaded. Formatted as a base64 string. |
| `groupId` | `integer` | No | Id of the group you are publishing the audio asset for. Null if not publishing under a group. |
| `paymentSource` | `string` | No | The source of funds for payment.   User: Use personal funds of authenticated user.   Group: Use group funds from Roblox.Publish.Api.UploadAudioRequest.GroupId.   Null/Empty: Will default to authenticated user funds. |
| `estimatedFileSize` | `integer` | No | Estimated file size of the audio file in bytes. |
| `estimatedDuration` | `number` | No | Estimated duration of the audio file in seconds. |
| `assetPrivacy` | `1 \| 2` | No | The asset privacy of the audio asset. |

### Roblox.Publish.Api.PublishAudioResponse

Response model for publish audio.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `Id` | `integer` | No | Id of the published asset. |
| `Name` | `string` | No | Name of the published asset. |

### Roblox.Publish.Api.VerifyAudioRequest

Request model to publish an audio asset.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | `string` | No | Gets or sets the name of the audio asset. |
| `file` | `string` | No | File to be uploaded. Formatted as a base64 string. |
| `groupId` | `integer` | No | Gets or sets the ID of the group if applicable. Optional. |
| `paymentSource` | `string` | No | Gets or sets the payment source. 'User' or 'Group'. Required if Group ID is set. |
| `fileSize` | `integer` | No | Gets or sets the size of the audio file in bytes. |
| `duration` | `number` | No | Gets or sets the duration of the audio in seconds. |

### Roblox.Publish.Api.VerifyAudioResponse

Response model for verify audio endpoint.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | `string` | No | Name of the audio file. |
| `price` | `integer` | No | Price in robux to publish the audio file. |
| `balance` | `integer` | No | User's current Robux balance. |
| `canAfford` | `boolean` | No | Boolean, true if the user can afford to purchase the publishing of the audio file. |

### Roblox.Badges.Api.IconUploadResponse

Badge icon upload response.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `targetId` | `integer` | No | The asset id of the uploaded icon. |

### Roblox.Catalog.Api.BundleDetailsModel

The hydration model representing a bundle on marketplace. Returned in all bundles controller endpoints.
Bound in the game-engine MarketplaceService.GetProductInfo method.
https://create.roblox.com/docs/reference/engine/classes/MarketplaceService#GetProductInfo.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | `integer` | No |  |
| `name` | `string` | No |  |
| `description` | `string` | No |  |
| `bundleType` | `string` | No |  |
| `isRecolorable` | `boolean` | No |  |
| `items` | `Roblox.Catalog.Api.BundleItemDetailModel[]` | No |  |
| `creator` | `Roblox.Catalog.Api.BundleCreatorModel` | No |  |
| `product` | `Roblox.Catalog.Api.BundleProductModel` | No |  |
| `itemRestrictions` | `integer enum (9 values)[]` | No |  |
| `collectibleItemDetail` | `Roblox.Catalog.Api.CollectibleItemDetail` | No |  |
| `discountInformation` | `Roblox.Catalog.Api.DiscountInformation` | No |  |

### Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.Catalog.Api.BundleDetailsModel_

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | `Roblox.Catalog.Api.BundleDetailsModel[]` | No |  |

### Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.Catalog.Api.CatalogSearchDetailedResponseItemV2_

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | `Roblox.Catalog.Api.CatalogSearchDetailedResponseItemV2[]` | No |  |

### Roblox.Catalog.Api.BatchItemDetailsCompleteResponse

Response for the batch GetItemDetailsComplete endpoint.
Each entry in Roblox.Catalog.Api.BatchItemDetailsCompleteResponse.Data is either a successfully hydrated item or a critical error.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | `Roblox.Catalog.Api.CatalogItemOrError[]` | No |  |

### Roblox.Catalog.Api.CategoryModel

Response model for category.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `category` | `integer enum (14 values)` | No | Category type. Values: 0, 1, 2, 3, 4, 5, 11, 12, 13, 14, 15, 16, 17, 18 |
| `taxonomy` | `string` | No | The associated public facing web_stable_id corresponding to internal taxonomy uuid for this category. |
| `assetTypeIds` | `integer[]` | No | List of AssetTypeIds corresponding to AssetType enum that this category returns. |
| `bundleTypeIds` | `integer[]` | No | List of bundleTypeIds corresponding to BundleType enum that this category returns. |
| `categoryId` | `integer` | No | Category id. |
| `name` | `string` | No | Category name. |
| `orderIndex` | `integer` | No | Category order index. |
| `subcategories` | `Roblox.Catalog.Api.SubcategoryModel[]` | No | Subcategories under this category. |
| `isSearchable` | `boolean` | No | Gets or sets whether the category is searchable in search bar. |

### Roblox.ItemConfiguration.Api.AssetCreationsDetailsRequest

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `AssetIds` | `integer[]` | No |  |

### Roblox.ItemConfiguration.Api.AssetCreationsDetailsResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `assetId` | `integer` | No | The asset Id. |
| `name` | `string` | No | The asset name. |
| `status` | `string enum (8 values)` | No | The asset status. ['Unknown' = 0, 'ReviewPending' = 1, 'Moderated' = 2, 'ReviewApproved' = 3, 'OnSale' = 4, 'OffSale' = 5, 'DelayedRelease' = 6, 'Free' = 7] Values: Unknown, ReviewPending, Moderated, ReviewApproved, OnSale, OffSale, DelayedRelease, Free |
| `description` | `string` | No | The asset description. |
| `creatorType` | `Unknown \| User \| Group` | No | The creator type. ['Unknown' = 0, 'User' = 1, 'Group' = 2] |
| `creatorTargetId` | `integer` | No | The creator target Id. |
| `isArchived` | `boolean` | No | Is the asset archived. |
| `assetType` | `string` | No | Type of the asset. |
| `created` | `string` | No | Date asset was created. |
| `updated` | `string` | No | Date asset was created. |

### Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.ItemConfiguration.Api.AssetCreationsResponse_

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `previousPageCursor` | `string` | No |  |
| `nextPageCursor` | `string` | No |  |
| `data` | `Roblox.ItemConfiguration.Api.AssetCreationsResponse[]` | No |  |

### Roblox.Catalog.Api.AssetFavoriteModel

A model to represent asset favorites.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `assetId` | `integer` | No | The Id of the asset being favorited. |
| `userId` | `integer` | No | The Id of the user favoriting the asset. |
| `created` | `string` | No | The time at which the user favorited the asset. |

### Roblox.Catalog.Api.BundleFavoriteModel

A model to represent bundle favorites.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `bundleId` | `integer` | No | The Id of the bundle being favorited. |
| `userId` | `integer` | No | The Id of the user favoriting the bundle. |
| `created` | `string` | No | The time at which the user favorited the bundle. |

### Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.Catalog.Api.CatalogSearchDetailedResponseItem_

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `previousPageCursor` | `string` | No |  |
| `nextPageCursor` | `string` | No |  |
| `data` | `Roblox.Catalog.Api.CatalogSearchDetailedResponseItem[]` | No |  |

### Roblox.Catalog.Api.FavoriteBundlesResponse

A response containing favorited bundles and whether there are more.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `favorites` | `Roblox.Catalog.Api.BundleDetailsModel[]` | No | Collection of favorited bundles and associated details. |
| `moreFavorites` | `boolean` | No | True if there exists a next page of favorited bundles. |
| `nextCursor` | `string` | No | Pagination cursor for the next page. |
| `previousCursor` | `string` | No | Pagination cursor for the previous page. |

### Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.Web.Responses.Plugins.PluginResponse_

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | `Roblox.Web.Responses.Plugins.PluginResponse[]` | No |  |

### Roblox.Develop.Api.UpdatePluginRequest

A request model for updating a plugin.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | `string` | No | The new plugin name. |
| `description` | `string` | No | The new plugin description. |
| `commentsEnabled` | `boolean` | No | Whether or not comments should be enabled. |

### Roblox.ItemConfiguration.Api.Models.Response.PublishingPreferences.PublishingPreferencesResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | `string` | No |  |
| `creatorUserId` | `integer` | No |  |
| `creatorGroupId` | `integer` | No |  |
| `publishingType` | `0 \| 1 \| 2` | No | Publishing type for the collectible. Currently can be either Limited or NonLimited. ['Invalid' = 0, 'Limited' = 1, 'NonLimited' = 2] |
| `saleLocationType` | `0 \| 1 \| 2 \| 3 \| 4` | No | Represents possible SaleLocation types of the Collectibles System. ['SALE_LOCATION_TYPE_INVALID' = 0, 'SALE_LOCATION_TYPE_SHOP_AND_ALL_EXPERIENCES' = 1, 'SALE_LOCATION_EXPERIENCES_AND_DEV_API_ONLY' = 2, 'SALE_LOCATION_TYPE_SHOP_ONLY' = 3, 'SALE_LOCATION_TYPE_SHOP_AND_EXPERIENCES_BY_ID' = 4] |
| `places` | `integer[]` | No |  |
| `priceInRobux` | `integer` | No |  |
| `priceOffset` | `integer` | No |  |
| `isFree` | `boolean` | No |  |
| `enableRegionalPricing` | `boolean` | No |  |
| `isRentalOptIn` | `boolean` | No |  |
| `autoPublishEnabled` | `boolean` | No |  |
| `created` | `string` | No |  |
| `updated` | `string` | No |  |

### Roblox.ItemConfiguration.Api.Models.Request.PublishingPreferences.CreatePublishingPreferencesRequest

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `creatorUserId` | `integer` | No |  |
| `creatorGroupId` | `integer` | No |  |
| `publishingType` | `0 \| 1 \| 2` | No | Publishing type for the collectible. Currently can be either Limited or NonLimited. ['Invalid' = 0, 'Limited' = 1, 'NonLimited' = 2] |
| `saleLocationType` | `0 \| 1 \| 2 \| 3 \| 4` | No | Represents possible SaleLocation types of the Collectibles System. ['SALE_LOCATION_TYPE_INVALID' = 0, 'SALE_LOCATION_TYPE_SHOP_AND_ALL_EXPERIENCES' = 1, 'SALE_LOCATION_EXPERIENCES_AND_DEV_API_ONLY' = 2, 'SALE_LOCATION_TYPE_SHOP_ONLY' = 3, 'SALE_LOCATION_TYPE_SHOP_AND_EXPERIENCES_BY_ID' = 4] |
| `places` | `integer[]` | No |  |
| `priceInRobux` | `integer` | No |  |
| `priceOffset` | `integer` | No |  |
| `isFree` | `boolean` | No |  |
| `enableRegionalPricing` | `boolean` | No |  |
| `isRentalOptIn` | `boolean` | No |  |
| `autoPublishEnabled` | `boolean` | No |  |

### Roblox.ItemConfiguration.Api.Models.Request.PublishingPreferences.UpdatePublishingPreferencesRequest

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `creatorUserId` | `integer` | No |  |
| `creatorGroupId` | `integer` | No |  |
| `publishingType` | `0 \| 1 \| 2` | No |  |
| `saleLocationType` | `0 \| 1 \| 2 \| 3 \| 4` | No |  |
| `places` | `integer[]` | No |  |
| `priceInRobux` | `integer` | No |  |
| `priceOffset` | `integer` | No |  |
| `isFree` | `boolean` | No |  |
| `enableRegionalPricing` | `boolean` | No |  |
| `isRentalOptIn` | `boolean` | No |  |
| `autoPublishEnabled` | `boolean` | No |  |

### Roblox.Catalog.Api.TopicRequestModel

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `items` | `Roblox.MarketplaceTopicDiscovery.TopicDiscoveryService.V1Beta1.AvatarItem[]` | No |  |
| `selectTopics` | `string[]` | No |  |
| `inputQuery` | `string` | No |  |
| `maxResult` | `integer` | No | Maximum number of topic results returned from the server. |
| `genderType` | `1 \| 2 \| 3` | No | ['Unknown' = 1, 'Male' = 2, 'Female' = 3] |

### Roblox.Catalog.Api.TopicResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `topics` | `Roblox.Catalog.Api.TopicModel[]` | No |  |
| `queries` | `string[]` | No |  |
| `error` | `Roblox.MarketplaceTopicDiscovery.TopicDiscoveryService.V1Beta1.Error` | No |  |

### Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.Api.Develop.Models.GroupModel_

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | `Roblox.Api.Develop.Models.GroupModel[]` | No |  |

### Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.Catalog.Api.OwnedBundleModel_

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `previousPageCursor` | `string` | No |  |
| `nextPageCursor` | `string` | No |  |
| `data` | `Roblox.Catalog.Api.OwnedBundleModel[]` | No |  |

### Roblox.Api.Avatar.Models.AssetIdListModel

A model that contains a list of asset ids

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `assetIds` | `integer[]` | No | The asset ids |

### Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.Inventory.Api.Models.IItemModel_

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `previousPageCursor` | `string` | No |  |
| `nextPageCursor` | `string` | No |  |
| `data` | `Roblox.Inventory.Api.Models.IItemModel[]` | No |  |

### Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.Inventory.Api.V2.AssetOwnerResponse_

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `previousPageCursor` | `string` | No |  |
| `nextPageCursor` | `string` | No |  |
| `data` | `Roblox.Inventory.Api.V2.AssetOwnerResponse[]` | No |  |

### Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.Api.Develop.AssetVersion_

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `previousPageCursor` | `string` | No |  |
| `nextPageCursor` | `string` | No |  |
| `data` | `Roblox.Api.Develop.AssetVersion[]` | No |  |

### Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.Inventory.Api.V2.CollectibleItemOwnerResponse_

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `previousPageCursor` | `string` | No |  |
| `nextPageCursor` | `string` | No |  |
| `data` | `Roblox.Inventory.Api.V2.CollectibleItemOwnerResponse[]` | No |  |

### Roblox.Catalog.Api.CatalogSearchPageResponse_Roblox.Catalog.Api.CatalogSearchDetailedResponseItemV2_

ApiPageResponse for catalog search.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `keyword` | `string` | No | Keyword used for search query. |
| `elasticsearchDebugInfo` | `Roblox.Catalog.Api.ElasticsearchDebugInfo` | No |  |
| `previousPageCursor` | `string` | No |  |
| `nextPageCursor` | `string` | No |  |
| `data` | `Roblox.Catalog.Api.CatalogSearchDetailedResponseItemV2[]` | No |  |

### Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.Inventory.Api.V2.UserAssetItemModelV2_

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `previousPageCursor` | `string` | No |  |
| `nextPageCursor` | `string` | No |  |
| `data` | `Roblox.Inventory.Api.V2.UserAssetItemModelV2[]` | No |  |