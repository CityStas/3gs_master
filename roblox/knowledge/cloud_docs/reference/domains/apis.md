---
name: "Open Cloud v1 REST APIs"
last_updated: 2026-10-30T19:56:08Z
type: v1
api_base_url: "https://apis.roblox.com"
services: 11
auth: [api-key, oauth2]
description: "Original Open Cloud REST APIs — prefer v2 feature APIs for new code"
---

# Open Cloud v1 REST APIs

These are the original Open Cloud REST APIs. For newer functionality, see the Open Cloud v2 feature-based APIs.

**Base URL:** `https://apis.roblox.com`

## Roblox.AssetPermissionsApi (1.0)

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
- `400`: Bad Request → `ErrorResponse`
- `403`: Forbidden → `ErrorResponse`
- `500`: Internal Server Error → `ErrorResponse`

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

## Models

### AssetGrantRequest

Asset grant requests with additional options to grant to dependencies.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `assetId` | `integer` | No | The asset ID to grant permission to. |
| `grantToDependencies` | `boolean` | No | Whether to extend the permission grant to dependencies of the asset. This will be done asynchronously after the main grant. |
| `parentVersionNumber` | `integer` | No | The version number of 'assetId' to use for determining asset dependencies. |

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

### Error

The error object for results.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `code` | `ErrorCode` | No |  |
| `message` | `string` | No | The human readable error message. |

### ErrorResponse

The error object for responses.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `error` | `Error` | No |  |

### GrantPermissionError

Single error for BatchGrantPermissionsResponse.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `assetId` | `integer` | No | Failed asset ID. |
| `code` | `ErrorCode` | No |  |

## Assets API (0.0.1)

You can send and receive the following request and response payloads to create assets on Roblox. For information on the usage of the API, see the [usage guide](/cloud/guides/usage-assets.md).

### POST `/v1/assets` [BETA]

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

- `200`: Returns the Operation ID for checking the creation status. → `Operation`
- `400`: Invalid argument. Failed to parse the request or the file. → `Status`
- `401`: The API key is not valid for this operation / You don't have the authorization.
- `500`: Server internal error / Unknown error.

**Response fields** (`Operation`)

See [Operation](#operation) in Models.

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

**Example:**
```bash
curl -X POST -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/v1/assets" \
  -F "request={"assetType":"string","assetId":0,"creationContext":{"assetPrivacy":"default","creator":{"userId":"...","groupId":"..."},"expectedPrice":0},"description":"string","displayName":"string","path":"string"};type=application/json" \
  -F "fileContent=@file.bin;type=application/octet-stream"
```

### GET `/v1/assets/{assetId}` [BETA]

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

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/v1/assets/{ASSETID}"
```

### PATCH `/v1/assets/{assetId}` [BETA]

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

- `200`: Returns the Operation ID for checking the update status / Returns the updated metadata fields. → `Operation`
- `400`: Invalid argument. Failed to parse the request or the file. → `Status`
- `401`: The API key is not valid for this operation / You don't have the authorization.
- `500`: Server internal error / Unknown error.

**Response fields** (`Operation`)

See [Operation](#operation) in Models.

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

**Example:**
```bash
curl -X PATCH -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/v1/assets/{ASSETID}" \
  -F "request={"assetType":"string","assetId":0,"creationContext":{"assetPrivacy":"default","creator":{"userId":"...","groupId":"..."},"expectedPrice":0},"description":"string","displayName":"string","path":"string"};type=application/json" \
  -F "fileContent=@file.bin;type=application/octet-stream"
```

### POST `/v1/assets/{assetId}:archive` [BETA]

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

**Example:**
```bash
curl -X POST -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/v1/assets/{ASSETID}:archive"
```

### POST `/v1/assets/{assetId}:restore` [BETA]

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

**Example:**
```bash
curl -X POST -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/v1/assets/{ASSETID}:restore"
```

### GET `/v1/assets/{assetId}/versions/{versionNumber}` [BETA]

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

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/v1/assets/{ASSETID}/versions/{VERSIONNUMBER}"
```

### GET `/v1/assets/{assetId}/versions` [BETA]

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

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/v1/assets/{ASSETID}/versions"
```

### POST `/v1/assets/{assetId}/versions:rollback` [BETA]

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

**Example:**
```bash
curl -X POST -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/v1/assets/{ASSETID}/versions:rollback" \
  -F "assetVersion=string"
```

### GET `/v1/operations/{operationId}` [BETA]

Get the result of an asset creation or update.

Get the result of an asset creation or update using the returned Operation ID. Requires **Read** for the API key permission and **asset:read** for OAuth 2.0 apps.

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `asset:read`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `operationId` | path | `string` | Yes | The unique identifier of the operation. |

**Responses:**

- `200`: Operation result retrieved successfully. → `Operation`
- `400`: Invalid argument. Failed to parse the request or the file. → `Status`
- `401`: The API key is not valid for this operation / You don't have the authorization.
- `500`: Server internal error / Unknown error.

**Response fields** (`Operation`)

See [Operation](#operation) in Models.

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

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/v1/operations/{OPERATIONID}"
```

## Models

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

### AssetVersion

An asset version.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `creationContext` | `CreationContext` | No |  |
| `path` | `string` | No | The returned resource path of the asset version. Format: `assets/{assetId}/versions/{version}`. Example: `assets/2205400862/versions/1`. |
| `moderationResult` | `ModerationResult` | No |  |
| `published` | `boolean` | No | Only applies to place asset types. Indicates if the place has been published or not. |

### CreationContext

The context of creation that is not part of the asset content, such as metadata and creator information. Required for [Create Asset](#POST-v1-assets).

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `assetPrivacy` | `AssetPrivacy` | No | Desired privacy setting for the asset on creation. Only applies to asset types that support privacy override. |
| `creator` | `Creator` | No |  |
| `expectedPrice` | `integer` | No | Expected asset upload fee in Robux. When the actual price is more than expected, the operation fails with a 400 error. |

### Creator

Represents a creator.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `userId` | `integer` | No | The User ID the creator. Required if the asset is individual-user-owned. |
| `groupId` | `integer` | No | The Group ID. Required if the asset is group-owned. |

### ModerationResult

The moderation result of the asset. 

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `moderationState` | `string` | No | The moderation state of the asset. Can be `Reviewing`, `Rejected`, or `Approved`. |

### Operation

This resource represents a long-running operation that is the result of a network API call.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `path` | `string` | No | The server-assigned resource path. The default format is `operations/{operation_id}`. |
| `done` | `boolean` | No | If `false`, the operation is still in progress. If `true`, the operation is completed. |
| `error` | `Status` | No |  |
| `response` | `Asset` | No |  |

### Preview

An asset preview.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `asset` | `string` | No | The preview asset path. |
| `altText` | `string` | No | Alt text for the preview asset. |

### SocialLink

A social media link for the asset. Maximum of three per asset. Object name can be any of: <ul><li>`facebookSocialLink`</li><li>`twitterSocialLink`</li><li>`youtubeSocialLink`</li><li>`twitchSocialLink`</li><li>`discordSocialLink`</li><li>`githubSocialLink`</li><li>`robloxSocialLink`</li><li>`guildedSocialLink`</li><li>`devForumSocialLink`</li></ul>For syntax, see the sample request under [Update Asset](#PATCH-v1-assets-_assetId_).

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `title` | `string` | No | An optional title for the social media link. Not used on the Creator Hub. |
| `uri` | `string` | No | The URI for the social media link. Must match the expected format for the type of link. For example, the title for a `twitchSocialLink` object must be of the format `https://twitch.tv/your-channel`. |

### Status

The logical error model explaining the error status.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `code` | `integer` | No | The HTTP status code. |
| `message` | `string` | No | The error message. |

## Ordered data stores (beta) (0.0.1)

This page includes reference documentation for working with the Open Cloud v1 API for ordered data stores. For information on using the v2 API, see the [usage guide](/cloud/guides/data-stores/index.md).

### GET `/v1/universes/{universeId}/orderedDataStores/{orderedDataStore}/scopes/{scope}/entries` [BETA]

Returns a list of entries from an ordered data store.

**Auth:** API Key (`x-api-key` header)

**Scopes:** `universe.ordered-data-store.scope.entry:read`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `string` | Yes | The identifier of the experience with ordered data stores that you want to access. You can find your experience's universe ID on Creator Hub. |
| `orderedDataStore` | path | `string` | Yes | The name of the target ordered data store. |
| `scope` | path | `string` | Yes | The name of the data store scope. See [Scopes](/cloud/guides/data-stores/request-handling.md#scopes). |
| `max_page_size` | query | `integer` | No | The maximum number of entries to return. The service may return fewer than this value. The default value is `10`. The maximum value is `100`, and any input above 100 is coerced to `100`. |
| `page_token` | query | `string` | No | A page token received from a previous `List` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `List` must match the call providing the page token. |
| `order_by` | query | `string` | No | The enumeration direction. The order by default is ascending. Input a `desc` suffix for descending. |
| `filter` | query | `string` | No | The range of qualifying values of entries to return. See [Filters](/cloud/guides/data-stores/request-handling.md#filters). |

**Responses:**

- `200`: OK → `ListEntriesResponse`
- `400`: Bad Request: invalid orderedDataStore, scope or entry name or encoding.
- `403`: Forbidden: studio access to APIs is not allowed, incorrect API key or scope.
- `429`: Too Many Requests.

**Response fields** (`ListEntriesResponse`)

See [ListEntriesResponse](#listentriesresponse) in Models.

**Response example:**
```json
{
  "entries": [
    {
      "path": "...",
      "id": "...",
      "value": "..."
    }
  ],
  "nextPageToken": "string"
}
```

**Error handling:** `429`: Retry with exponential backoff (start at 1s). `403`: Verify your API key has the required scopes listed above. 

**Rate Limit Note:** See [Throttling](/cloud/guides/data-stores/throttling.md).

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/v1/universes/{UNIVERSEID}/orderedDataStores/{ORDEREDDATASTORE}/scopes/{SCOPE}/entries"
```

### POST `/v1/universes/{universeId}/orderedDataStores/{orderedDataStore}/scopes/{scope}/entries` [BETA]

Creates a new entry with the content value provided.

**Auth:** API Key (`x-api-key` header)

**Scopes:** `universe.ordered-data-store.scope.entry:write`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `string` | Yes | The identifier of the experience with ordered data stores that you want to access. You can find your experience's universe ID on Creator Hub. |
| `orderedDataStore` | path | `string` | Yes | The name of the ordered data store. |
| `scope` | path | `string` | Yes | The name of the data store scope. See [Scopes](/cloud/guides/data-stores/request-handling.md#scopes). |
| `id` | query | `string` | Yes | The name of the entry. |

**Request Body:** `application/json` — Type: `CreateEntryRequest`

See [CreateEntryRequest](#createentryrequest) in Models.

**Request example:**
```json
{
  "value": 0
}
```

**Responses:**

- `200`: OK → `Entry`
- `400`: Bad Request: invalid orderedDataStore, scope or entry name or encoding.
- `403`: Forbidden: studio access to APIs is not allowed, incorrect API key or scope.
- `404`: Not found.
- `429`: Too Many Requests.

**Response fields** (`Entry`)

See [Entry](#entry) in Models.

**Response example:**
```json
{
  "path": "string",
  "id": "string",
  "value": 0
}
```

**Error handling:** `429`: Retry with exponential backoff (start at 1s). `403`: Verify your API key has the required scopes listed above. 

**Rate Limit Note:** See [Throttling](/cloud/guides/data-stores/throttling.md).

**Example:**
```bash
curl -X POST -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/v1/universes/{UNIVERSEID}/orderedDataStores/{ORDEREDDATASTORE}/scopes/{SCOPE}/entries?id={VALUE}" \
  -H "Content-Type: application/json" \
  -d '{
  "value": 0
}'
```

### GET `/v1/universes/{universeId}/orderedDataStores/{orderedDataStore}/scopes/{scope}/entries/{entry}` [BETA]

Gets and returns the specified entry.

**Auth:** API Key (`x-api-key` header)

**Scopes:** `universe.ordered-data-store.scope.entry:read`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `string` | Yes | The identifier of the experience with ordered data stores that you want to access. You can find your experience's universe ID on Creator Hub. |
| `orderedDataStore` | path | `string` | Yes | The name of the ordered data store. |
| `scope` | path | `string` | Yes | The name of the data store scope. See [Scopes](/cloud/guides/data-stores/request-handling.md#scopes). |
| `entry` | path | `string` | Yes | The entry ID. |

**Responses:**

- `200`: OK → `Entry`
- `400`: Bad Request: invalid orderedDataStore, scope or entry name or encoding.
- `403`: Forbidden: studio access to APIs is not allowed, incorrect API key or scope.
- `404`: Not found.
- `429`: Too Many Requests.

**Response fields** (`Entry`)

See [Entry](#entry) in Models.

**Response example:**
```json
{
  "path": "string",
  "id": "string",
  "value": 0
}
```

**Error handling:** `429`: Retry with exponential backoff (start at 1s). `403`: Verify your API key has the required scopes listed above. 

**Rate Limit Note:** See [Throttling](/cloud/guides/data-stores/throttling.md).

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/v1/universes/{UNIVERSEID}/orderedDataStores/{ORDEREDDATASTORE}/scopes/{SCOPE}/entries/{ENTRY}"
```

### PATCH `/v1/universes/{universeId}/orderedDataStores/{orderedDataStore}/scopes/{scope}/entries/{entry}` [BETA]

Updates an entry value and returns the updated entry.

**Auth:** API Key (`x-api-key` header)

**Scopes:** `universe.ordered-data-store.scope.entry:write`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `string` | Yes | The identifier of the experience with ordered data stores that you want to access. You can find your experience's universe ID on Creator Hub. |
| `orderedDataStore` | path | `string` | Yes | The name of the ordered data store. |
| `scope` | path | `string` | Yes | The name of the data store scope. See [Scopes](/cloud/guides/data-stores/request-handling.md#scopes). |
| `entry` | path | `string` | Yes | The entry ID. |
| `allow_missing` | query | `boolean` | No | The flag to allow the creation of an entry if the entry doesn't exist. See [Allow missing flags](/cloud/guides/data-stores/request-handling.md.md#allow-missing-flags). |

**Request Body:** `application/json` — Type: `UpdateEntryRequest`

See [UpdateEntryRequest](#updateentryrequest) in Models.

**Request example:**
```json
{
  "value": 0
}
```

**Responses:**

- `200`: OK → `Entry`
- `400`: Bad Request: invalid orderedDataStore, scope or entry name or encoding.
- `403`: Forbidden: studio access to APIs is not allowed, incorrect API key or scope.
- `404`: Not found.
- `409`: Aborted.
- `429`: Too Many Requests.

**Response fields** (`Entry`)

See [Entry](#entry) in Models.

**Response example:**
```json
{
  "path": "string",
  "id": "string",
  "value": 0
}
```

**Error handling:** `429`: Retry with exponential backoff (start at 1s). `403`: Verify your API key has the required scopes listed above. 

**Rate Limit Note:** See [Throttling](/cloud/guides/data-stores/throttling.md).

**Example:**
```bash
curl -X PATCH -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/v1/universes/{UNIVERSEID}/orderedDataStores/{ORDEREDDATASTORE}/scopes/{SCOPE}/entries/{ENTRY}" \
  -H "Content-Type: application/json" \
  -d '{
  "value": 0
}'
```

### DELETE `/v1/universes/{universeId}/orderedDataStores/{orderedDataStore}/scopes/{scope}/entries/{entry}` [BETA]

Deletes the specified entry. Unlike standard data stores, which mark entries for deletion, ordered data store entries are deleted immediately.

**Auth:** API Key (`x-api-key` header)

**Scopes:** `universe.ordered-data-store.scope.entry:write`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `string` | Yes | The identifier of the experience with ordered data stores that you want to access. You can find your experience's universe ID on Creator Hub. |
| `orderedDataStore` | path | `string` | Yes | The name of the ordered data store. |
| `scope` | path | `string` | Yes | The name of the data store scope. See [Scopes](/cloud/guides/data-stores/request-handling.md#scopes). |
| `entry` | path | `string` | Yes | The entry ID. |

**Responses:**

- `200`: Success: the entry was successfully deleted or didn't exist.
- `400`: Bad Request: invalid orderedDataStore, scope or entry name or encoding.
- `403`: Forbidden: Studio access to APIs is not allowed, incorrect API key or scope.
- `404`: Not found.
- `429`: Too Many Requests.

**Error handling:** `429`: Retry with exponential backoff (start at 1s). `403`: Verify your API key has the required scopes listed above. 

**Rate Limit Note:** See [Throttling](/cloud/guides/data-stores/throttling.md).

**Example:**
```bash
curl -X DELETE -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/v1/universes/{UNIVERSEID}/orderedDataStores/{ORDEREDDATASTORE}/scopes/{SCOPE}/entries/{ENTRY}"
```

### POST `/v1/universes/{universeId}/orderedDataStores/{orderedDataStore}/scopes/{scope}/entries/{entry}:increment` [BETA]

Increments the value of the key by the provided amount and returns the updated entry.

Known issue: Entry values can increment past the valid range and this may persist in the backend. Returned values will clamp to the valid range.

**Auth:** API Key (`x-api-key` header)

**Scopes:** `universe.ordered-data-store.scope.entry:write`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `string` | Yes | The identifier of the experience with ordered data stores that you want to access. You can find your experience's universe ID on Creator Hub. |
| `orderedDataStore` | path | `string` | Yes | The name of the ordered data store. |
| `scope` | path | `string` | Yes | The name of the data store scope. See [Scopes](/cloud/guides/data-stores/request-handling.md#scopes). |
| `entry` | path | `string` | Yes | The entry ID. |

**Request Body:** `application/json` — Type: `IncrementEntryRequest`

See [IncrementEntryRequest](#incremententryrequest) in Models.

**Request example:**
```json
{
  "amount": 0
}
```

**Responses:**

- `200`: OK → `Entry`
- `400`: Bad Request: invalid orderedDataStore, scope or entry name or encoding.
- `403`: Forbidden: studio access to APIs is not allowed, incorrect API key or scope.
- `404`: Not found.
- `429`: Too Many Requests.

**Response fields** (`Entry`)

See [Entry](#entry) in Models.

**Response example:**
```json
{
  "path": "string",
  "id": "string",
  "value": 0
}
```

**Error handling:** `429`: Retry with exponential backoff (start at 1s). `403`: Verify your API key has the required scopes listed above. 

**Rate Limit Note:** See [Throttling](/cloud/guides/data-stores/throttling.md).

**Example:**
```bash
curl -X POST -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/v1/universes/{UNIVERSEID}/orderedDataStores/{ORDEREDDATASTORE}/scopes/{SCOPE}/entries/{ENTRY}:increment" \
  -H "Content-Type: application/json" \
  -d '{
  "amount": 0
}'
```

## Models

### Entry

Represents an entry.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `path` | `string` | No | The resource path of the request. |
| `id` | `string` | No | The name of the entry |
| `value` | `integer` | No | The value of the entry. |

### IncrementEntryRequest

Increments entry value.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `amount` | `integer` | Yes | The amount to increment by the entry value. If the input value exceeds the maximum value supported by int64, which is 9,223,372,036,854,775,807, the request fails with a 400 Bad Request error. |

### UpdateEntryRequest

Updates the entry provided with a new value.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `value` | `integer` | Yes | The value to update the entry. If the input value exceeds the maximum value supported by int64, which is 9,223,372,036,854,775,807, the request fails with a 400 Bad Request error. |

### CreateEntryRequest

Creates a new entry with the value provided.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `value` | `integer` | Yes | The value to set the new entry. If the input value exceeds the maximum value supported by int64, which is 9,223,372,036,854,775,807, the request fails with a 400 Bad Request error. |

### ListEntriesResponse

A list of Entries in the parent collection.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `entries` | `Entry[]` | No | The Entries from the specified Scope. |
| `nextPageToken` | `string` | No | A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages. |

## Standard data stores (v1)

This page includes reference documentation for working with the Open Cloud v1 API for standard data stores. For information on using the v2 API, see the [usage guide](/cloud/guides/data-stores/index.md).

### GET `/v1/universes/{universeId}/standard-datastores` [BETA]

List data stores in an experience

Returns a list of an experience's data stores.

**Auth:** API Key (`x-api-key` header)

**Scopes:** `universe-datastores.control:list`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer` | Yes | The identifier of the experience with data stores that you want to access. You can find your experience's universe ID on Creator Hub. |
| `cursor` | query | `string` | No | Provide to request the next set of data. |
| `limit` | query | `integer` | No | The maximum number of items to return. Each call only reads one partition, so it can return fewer than the given value when running out of objectives on one partition. |
| `prefix` | query | `string` | No | Provide to return only data stores with this prefix. |

**Responses:**

- `200`:  → `object`

**Response fields** (`object`)

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | `DataStore[]` | No | An array of data stores in the target experience. |
| `nextPageCursor` | `string` | No | Indicates that there is more data available in the requested result set. |

**Response example:**
```json
{
  "data": [
    {
      "name": "...",
      "createdTime": "..."
    }
  ],
  "nextPageCursor": "string"
}
```

**Rate Limit Note:** See [Throttling](/cloud/guides/data-stores/throttling.md).

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/v1/universes/{UNIVERSEID}/standard-datastores"
```

### GET `/v1/universes/{universeId}/standard-datastores/datastore/entries` [BETA]

List entries

Returns a list of entry keys within a data store.

 Entries marked deleted with a tombstone version are still included in the response if they have yet to be permanently deleted.

**Auth:** API Key (`x-api-key` header)

**Scopes:** `universe-datastores.objects:list`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer` | Yes | The identifier of the experience with data stores that you want to access. You can find your experience's universe ID on Creator Hub. |
| `datastoreName` | query | `string` | No | The name of the data store. |
| `scope` | query | `string` | No | The value is `global` by default. See [Scopes](/cloud-services/data-stores/index.md#scopes). |
| `allScopes` | query | `boolean` | No | Set to true to return keys from all scopes. |
| `prefix` | query | `string` | No | Provide to return only keys with this prefix. |
| `cursor` | query | `string` | No | Provide to request the next set of data. |
| `limit` | query | `integer` | No | The maximum number of items to return. Each call only reads one partition, so it can return fewer than the given value when running out of objectives on one partition. |

**Responses:**

- `200`:  → `object`

**Response fields** (`object`)

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `keys` | `string[]` | No | An array of entry keys within the target data store. |
| `nextPageCursor` | `string` | No | Indicates that there is more data available in the requested result set. |

**Response example:**
```json
{
  "keys": [
    "string"
  ],
  "nextPageCursor": "string"
}
```

**Rate Limit Note:** See [Throttling](/cloud/guides/data-stores/throttling.md).

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/v1/universes/{UNIVERSEID}/standard-datastores/datastore/entries"
```

### GET `/v1/universes/{universeId}/standard-datastores/datastore/entries/entry` [BETA]

Get entry.

Returns the value and metadata associated with an entry.

Entries marked deleted with a tombstone version will return 404 Not Found.

Metadata can be found in the response headers like the following:
```text
content-md5: zuYxEhwuySMv0i8CitXImw==
roblox-entry-version: 08D9E6A3F2188CFF.0000000001.08D9E6A3F2188CFF.01
roblox-entry-created-time: 2022-02-02T23:30:06.5388799+00:00
roblox-entry-version-created-time: 2022-02-02T23:30:06.5388799+00:00
roblox-entry-attributes: { "myAttribute": "myValue" }
roblox-entry-userids: [1, 2, 3]
```

| Header | Description |
|---|---| 
| `content-md5` | The base64-encoded MD5 checksum of the content. See [Content-MD5](/cloud/guides/data-stores/request-handling.md#content-md5). |
| `roblox-entry-version` | The version of the returned entry. |
| `roblox-entry-created-time` | The time at which the entry was created. |
| `roblox-entry-version-created-time` | The time at which this particular version was created. |
| `roblox-entry-attributes` | Attributes tagged with the entry. Serialized JSON map object. |
| `roblox-entry-userids` | Comma-separated list of Roblox user IDs tagged with the entry. |

**Auth:** API Key (`x-api-key` header)

**Scopes:** `universe-datastores.objects:read`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer` | Yes | The identifier of the experience with data stores that you want to access. You can find your experience's universe ID on Creator Hub. |
| `datastoreName` | query | `string` | No | The name of the data store. |
| `entryKey` | query | `string` | No | The key identifying the entry. |
| `scope` | query | `string` | No | The value is `global` by default. See [Scopes](/cloud-services/data-stores/index.md#scopes). |

**Responses:**

- `200`: Successfully retrieved the entry. → `object`
- `204`: The key is marked as deleted.

**Rate Limit Note:** See [Throttling](/cloud/guides/data-stores/throttling.md).

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/v1/universes/{UNIVERSEID}/standard-datastores/datastore/entries/entry"
```

### POST `/v1/universes/{universeId}/standard-datastores/datastore/entries/entry` [BETA]

Set entry.

Sets the value, metadata and user IDs associated with an entry.

**Auth:** API Key (`x-api-key` header)

**Scopes:** `universe-datastores.objects:update`, `universe-datastores.objects:create`, `universe-datastores.control:create`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer` | Yes | The identifier of the experience with data stores that you want to access. You can find your experience's universe ID on Creator Hub. |
| `datastoreName` | query | `string` | No | The name of the data store. |
| `entryKey` | query | `string` | No | The key identifying the entry. |
| `matchVersion` | query | `string` | No | Provide to update only if the current version matches this. |
| `exclusiveCreate` | query | `boolean` | No | Create the entry only if it does not exist. |
| `scope` | query | `string` | No | The value is `global` by default. See [Scopes](/cloud-services/data-stores/index.md#scopes). |
| `roblox-entry-attributes` | header | `string` | No | Attributes to be associated with new version of the entry. Serialized by JSON map objects. If not provided, existing attributes are cleared. |
| `roblox-entry-userids` | header | `string` | No | Comma-separated list of Roblox user IDs tagged with the entry. If not provided, existing user IDs are cleared. |
| `content-md5` | header | `string` | No | The base64-encoded MD5 checksum of the content. See [Content-MD5](/cloud/guides/data-stores/request-handling.md#content-md5). |

**Request Body:** `application/json` — Type: `string`

**Responses:**

- `200`:  → `EntryVersion`

**Response fields** (`EntryVersion`)

See [EntryVersion](#entryversion) in Models.

**Response example:**
```json
{
  "version": "string",
  "deleted": false,
  "contentLength": 0,
  "createdTime": "2024-01-01T00:00:00Z",
  "objectCreatedTime": "2024-01-01T00:00:00Z"
}
```

**Rate Limit Note:** See [Throttling](/cloud/guides/data-stores/throttling.md).

**Example:**
```bash
curl -X POST -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/v1/universes/{UNIVERSEID}/standard-datastores/datastore/entries/entry" \
  -H "Content-Type: application/json" \
  -d '"string"'
```

### DELETE `/v1/universes/{universeId}/standard-datastores/datastore/entries/entry` [BETA]

Delete entry.

Marks the entry as deleted by creating a tombstone version. Entries are deleted permanently after 30 days.

**Auth:** API Key (`x-api-key` header)

**Scopes:** `universe-datastores.objects:delete`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer` | Yes | The identifier of the experience with data stores that you want to access. You can find your experience's universe ID on Creator Hub. |
| `datastoreName` | query | `string` | No | The name of the data store. |
| `entryKey` | query | `string` | No | The key identifying the entry. |
| `scope` | query | `string` | No | The value is `global` by default. See [Scopes](/cloud-services/data-stores/index.md#scopes). |

**Responses:**

- `204`: The entry is deleted.

**Rate Limit Note:** See [Throttling](/cloud/guides/data-stores/throttling.md).

**Example:**
```bash
curl -X DELETE -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/v1/universes/{UNIVERSEID}/standard-datastores/datastore/entries/entry"
```

### POST `/v1/universes/{universeId}/standard-datastores/datastore/entries/entry/increment` [BETA]

Increment entry

Increments the value for an entry by a given amount, or create a new entry with that amount. Returns the entry and metadata.

Metadata can be found in the response headers like the following:
```text
content-md5: zuYxEhwuySMv0i8CitXImw==
roblox-entry-version: 08D9E6A3F2188CFF.0000000001.08D9E6A3F2188CFF.01
roblox-entry-created-time: 2022-02-02T23:30:06.5388799+00:00
roblox-entry-version-created-time: 2022-02-02T23:30:06.5388799+00:00
roblox-entry-attributes: { "myAttribute": "myValue" }
roblox-entry-userids: [1, 2, 3]
```

| Header | Description |
|---|---| 
| `content-md5` | The base64-encoded MD5 checksum of the content. See [Content-MD5](/cloud/guides/data-stores/request-handling.md#content-md5). |
| `roblox-entry-version` | The version of the returned entry. |
| `roblox-entry-created-time` | The time at which the entry was created. |
| `roblox-entry-version-created-time` | The time at which this particular version was created. |
| `roblox-entry-attributes` | Attributes tagged with the entry. Serialized JSON map object. |
| `roblox-entry-userids` | Comma-separated list of Roblox user IDs tagged with the entry. |

**Auth:** API Key (`x-api-key` header)

**Scopes:** `universe-datastores.objects:update`, `universe-datastores.objects:create`, `universe-datastores.control:create`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer` | Yes | The identifier of the experience with data stores that you want to access. You can find your experience's universe ID on Creator Hub. |
| `datastoreName` | query | `string` | No | The name of the data store. |
| `entryKey` | query | `string` | No | The key identifying the entry. |
| `incrementBy` | query | `integer` | No | The amount by which the entry should be incremented, or the starting value if it doesn't exist. |
| `scope` | query | `string` | No | The value is `global` by default. See [Scopes](/cloud-services/data-stores/index.md#scopes). |
| `roblox-entry-attributes` | header | `string` | No | Attributes to be associated with new version of the entry. Serialized by JSON map objects. If not provided, existing attributes are cleared. |
| `roblox-entry-userids` | header | `string` | No | A comma-separated list of Roblox user IDs that the entry is tagged with. If not provided, existing user IDs are cleared. |

**Responses:**

- `200`: Returns the latest version of the entry after it has been incremented. → `object`
- `204`: The key is marked as deleted.

**Rate Limit Note:** See [Throttling](/cloud/guides/data-stores/throttling.md).

**Example:**
```bash
curl -X POST -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/v1/universes/{UNIVERSEID}/standard-datastores/datastore/entries/entry/increment"
```

### GET `/v1/universes/{universeId}/standard-datastores/datastore/entries/entry/versions/version` [BETA]

Get entry version.

Returns the value and metadata of a specific version of an entry.

Metadata can be found in the response headers like the following:
```text
content-md5: zuYxEhwuySMv0i8CitXImw==
roblox-entry-version: 08D9E6A3F2188CFF.0000000001.08D9E6A3F2188CFF.01
roblox-entry-created-time: 2022-02-02T23:30:06.5388799+00:00
roblox-entry-version-created-time: 2022-02-02T23:30:06.5388799+00:00
roblox-entry-attributes: { "myAttribute": "myValue" }
roblox-entry-userids: [1, 2, 3]
```

| Header | Description |
|---|---| 
| `content-md5` | The base64-encoded MD5 checksum of the content. See [Content-MD5](/cloud/guides/data-stores/request-handling.md#content-md5). |
| `roblox-entry-version` | The version of the returned entry. |
| `roblox-entry-created-time` | The time at which the entry was created. |
| `roblox-entry-version-created-time` | The time at which this particular version was created. |
| `roblox-entry-attributes` | Attributes tagged with the entry. Serialized JSON map object. |
| `roblox-entry-userids` | Comma-separated list of Roblox user IDs tagged with the entry. |

**Auth:** API Key (`x-api-key` header)

**Scopes:** `universe-datastores.versions:read`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer` | Yes | The identifier of the experience with data stores that you want to access. You can find your experience's universe ID on Creator Hub. |
| `datastoreName` | query | `string` | No | The name of the data store. |
| `entryKey` | query | `string` | No | The key identifying the entry. |
| `versionId` | query | `string` | No | The version to inspect. |
| `scope` | query | `string` | No | The value is `global` by default. See [Scopes](/cloud-services/data-stores/index.md#scopes). |

**Responses:**

- `200`: Successfully retrieved the entry. → `object`

**Rate Limit Note:** See [Throttling](/cloud/guides/data-stores/throttling.md).

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/v1/universes/{UNIVERSEID}/standard-datastores/datastore/entries/entry/versions/version"
```

### GET `/v1/universes/{universeId}/standard-datastores/datastore/entries/entry/versions` [BETA]

List entry versions

Returns a list of versions for an entry.

**Auth:** API Key (`x-api-key` header)

**Scopes:** `universe-datastores.versions:list`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer` | Yes | The identifier of the experience with data stores that you want to access. You can find your experience's universe ID on Creator Hub. |
| `datastoreName` | query | `string` | No | The name of the data store. |
| `entryKey` | query | `string` | No | The key identifying the entry. |
| `scope` | query | `string` | No | The value is `global` by default. See [Scopes](/cloud-services/data-stores/index.md#scopes). |
| `cursor` | query | `string` | No | Provide to request the next set of data. |
| `startTime` | query | `string` | No | Provide to not include versions earlier than this timestamp. |
| `endTime` | query | `string` | No | Provide to not include versions later than this timestamp. |
| `sortOrder` | query | `string` | No | Either `Ascending` (earlier versions first) or `Descending` (later versions first). |
| `limit` | query | `integer` | No | The maximum number of items to return. Each call only reads one partition, so it can return fewer than the given value when running out of objectives on one partition. |

**Responses:**

- `200`:  → `EntryVersion`
- `400`: Invalid request / Invalid file content.
- `403`: Publish not allowed on place.
- `404`: The experience or data store was not found.
- `429`: Too Many Requests.

**Response fields** (`EntryVersion`)

See [EntryVersion](#entryversion) in Models.

**Response example:**
```json
{
  "version": "string",
  "deleted": false,
  "contentLength": 0,
  "createdTime": "2024-01-01T00:00:00Z",
  "objectCreatedTime": "2024-01-01T00:00:00Z"
}
```

**Error handling:** `429`: Retry with exponential backoff (start at 1s). `403`: Verify your API key has the required scopes listed above. 

**Rate Limit Note:** See [Throttling](/cloud/guides/data-stores/throttling.md).

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/v1/universes/{UNIVERSEID}/standard-datastores/datastore/entries/entry/versions"
```

## Models

### DataStore

The data store object with its name and created time.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | `string` | No | The name of your data store. |
| `createdTime` | `string` | No | The timestamp of when the data store was created in the ISO time format. |

### EntryVersion

The entry version object returned by the `List Entry Versions` method.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `version` | `string` | No | The version name of the qualifying entry. |
| `deleted` | `boolean` | No | Indicates whether the entry has been deleted. |
| `contentLength` | `number` | No | The length of the content. |
| `createdTime` | `string` | No | The timestamp of when the version was created in the ISO time format. |
| `objectCreatedTime` | `string` | No | The timestamp of when the data store was created in the ISO time format. |

## developer-products-api (v1)

### POST `/developer-products/v2/universes/{universeId}/developer-products` [BETA]

Create developer product

Creates a new developer product with the provided configuration details.

**Auth:** Cookie (`.ROBLOSECURITY`) or API Key (`x-api-key` header)

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

**Rate Limits:** perApiKeyOwner: 3/second

**Example:**
```bash
curl -X POST -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/developer-products/v2/universes/{UNIVERSEID}/developer-products" \
  -F "name=string" \
  -F "description=string" \
  -F "isForSale=false" \
  -F "price=0" \
  -F "imageFile=@file.bin;type=application/octet-stream" \
  -F "isRegionalPricingEnabled=false"
```

### PATCH `/developer-products/v2/universes/{universeId}/developer-products/{productId}` [BETA]

Update developer product

Updates a developer product with the provided configuration details. 
Note that only fields provided in the request will be updated.

**Auth:** Cookie (`.ROBLOSECURITY`) or API Key (`x-api-key` header)

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

**Rate Limits:** perApiKeyOwner: 3/second

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
  -F "storePageEnabled=false"
```

### GET `/developer-products/v2/universes/{universeId}/developer-products/{productId}/creator` [BETA]

Get developer product with configuration details

**Auth:** Cookie (`.ROBLOSECURITY`) or API Key (`x-api-key` header)

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

**Rate Limits:** perApiKeyOwner: 10/second

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/developer-products/v2/universes/{UNIVERSEID}/developer-products/{PRODUCTID}/creator"
```

### GET `/developer-products/v2/universes/{universeId}/developer-products/creator` [BETA]

List developer products by universe with configuration details

**Auth:** Cookie (`.ROBLOSECURITY`) or API Key (`x-api-key` header)

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

**Rate Limits:** perApiKeyOwner: 10/second

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/developer-products/v2/universes/{UNIVERSEID}/developer-products/creator"
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
| `storePageEnabled` | `boolean` | Yes | Whether the developer product is currently available for purchase on the external store page. |
| `priceInformation` | `any` | Yes | The pricing configuration associated with the product. |
| `isImmutable` | `boolean` | Yes | Whether the developer product cannot be modified, such as when created as a commerce product. |
| `createdTimestamp` | `string` | Yes | The timestamp when the developer product was created. |
| `updatedTimestamp` | `string` | Yes | The timestamp when the developer product was last updated. |

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

### PriceInformationStruct

The pricing configuration information.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `defaultPriceInRobux` | `integer` | Yes | The configured default price in Robux. |
| `enabledFeatures` | `PricingFeature[]` | Yes | The enabled pricing features for the developer product. |

## game-passes-http-service (v1)

### POST `/game-passes/v1/universes/{universeId}/game-passes` [BETA]

Create game pass

Creates a new game pass with the provided configuration details.

**Auth:** Cookie (`.ROBLOSECURITY`) or API Key (`x-api-key` header)

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
- `400`: Bad Request → `ErrorResponse`
- `401`: Unauthorized → `ErrorResponse`
- `403`: Forbidden → `ErrorResponse`
- `404`: Not Found → `ErrorResponse`

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

**Rate Limits:** perApiKeyOwner: 5/second

**Example:**
```bash
curl -X POST -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/game-passes/v1/universes/{UNIVERSEID}/game-passes" \
  -F "name=string" \
  -F "description=string" \
  -F "imageFile=@file.bin;type=application/octet-stream" \
  -F "isForSale=false" \
  -F "price=0" \
  -F "isRegionalPricingEnabled=false"
```

### PATCH `/game-passes/v1/universes/{universeId}/game-passes/{gamePassId}` [BETA]

Update game pass

Updates a game pass with the provided configuration details.
Note that only fields provided in the request will be updated.

**Auth:** Cookie (`.ROBLOSECURITY`) or API Key (`x-api-key` header)

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
| `file` | `string` | No | The thumbnail image file to be uploaded. |
| `isForSale` | `boolean` | No | Whether the game pass should be on sale. |
| `price` | `integer` | No | The default price of the game pass. |
| `isRegionalPricingEnabled` | `boolean` | No | Whether regional pricing should be enabled for the game pass. |

**Request example:**
```json
{
  "name": "string",
  "description": "string",
  "file": "string",
  "isForSale": false,
  "price": 0,
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

**Rate Limits:** perApiKeyOwner: 5/second

**Example:**
```bash
curl -X PATCH -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/game-passes/v1/universes/{UNIVERSEID}/game-passes/{GAMEPASSID}" \
  -F "name=string" \
  -F "description=string" \
  -F "file=@file.bin;type=application/octet-stream" \
  -F "isForSale=false" \
  -F "price=0" \
  -F "isRegionalPricingEnabled=false"
```

### GET `/game-passes/v1/universes/{universeId}/game-passes/{gamePassId}/creator` [BETA]

Get game pass with configuration details

**Auth:** Cookie (`.ROBLOSECURITY`) or API Key (`x-api-key` header)

**Scopes:** `game-pass:read`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer` | Yes | The universe ID. |
| `gamePassId` | path | `integer` | Yes | The game pass ID. |

**Responses:**

- `200`: Success → `GamePassConfigV2`
- `401`: Unauthorized → `ErrorResponse`
- `403`: Forbidden → `ErrorResponse`
- `404`: Not Found → `ErrorResponse`

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

**Rate Limits:** perApiKeyOwner: 10/second

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/game-passes/v1/universes/{UNIVERSEID}/game-passes/{GAMEPASSID}/creator"
```

### GET `/game-passes/v1/universes/{universeId}/game-passes/creator` [BETA]

List game passes by universe with configuration details

**Auth:** Cookie (`.ROBLOSECURITY`) or API Key (`x-api-key` header)

**Scopes:** `game-pass:read`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer` | Yes | The universe ID. |
| `pageSize` | query | `integer` | No | The number of results to return. Defaults to 50 if not provided. |
| `pageToken` | query | `string` | No | The cursor token for pagination. |

**Responses:**

- `200`: Success → `ListGamePassConfigsByUniverseResponse`
- `400`: Bad Request → `ErrorResponse`
- `401`: Unauthorized → `ErrorResponse`
- `403`: Forbidden → `ErrorResponse`
- `404`: Not Found → `ErrorResponse`

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

**Rate Limits:** perApiKeyOwner: 10/second

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/game-passes/v1/universes/{UNIVERSEID}/game-passes/creator"
```

## Models

### ErrorResponse

This is the base class for all custom Exceptions that are thrown in this API.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `errorCode` | `any` | No | The ErrorCode for the exception. |
| `errorMessage` | `string` | No | The human readable error message. |
| `field` | `string` | No | The relevant field that caused the error. |
| `hint` | `string` | No | A hint as to what caused the error, if applicable. |

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

### ListGamePassConfigsByUniverseResponse

Response for listing game pass configuration details by universe

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `gamePasses` | `GamePassConfigV2[]` | Yes | The list of game passes with their corresponding configuration details. |
| `nextPageToken` | `string` | Yes | The next page token. |

### PriceInformationStruct

The pricing configuration information.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `defaultPriceInRobux` | `integer` | Yes | The configured default price in Robux. |
| `enabledFeatures` | `PricingFeature[]` | Yes | The enabled pricing features for the game pass. |

## Messaging Service (v1)

This page contains reference documentation for the Open Cloud v1 Messaging Service API, which can broadcast messages across all servers in your experience.

The v2 API has its own version of the [Publish Message](/cloud/reference/Universe#Cloud_PublishUniverseMessage) method. For information on using the v2 method, see the [Messaging usage guide](/cloud/guides/usage-messaging.md).

### POST `/v1/universes/{universeId}/topics/{topic}` [BETA]

Publish a cross-server message to a universe

Publish a message to a pre-defined topic of an experience, with the size of the message up to 1,024 characters (1 KB). Requires the **Publish** permission for API keys and the **universe-messaging-service:publish** scope for OAuth 2.0 apps. See [Cross-server messaging](/cloud-services/cross-server-messaging.md#subscribe-users-to-receive-messages) for defining and subscribing users to a topic.

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `universe-messaging-service:publish`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer` | Yes | The identifier of the experience in which you want to send your messages to. You can [copy your experience's Universe ID](/cloud/guides/usage-messaging.md#publishing-messages-to-live-servers) on **Creator Dashboard**. |
| `topic` | path | `string` | Yes | The topic that you want to publish your message to, with up to 80 characters. |

**Request Body:** `application/json-patch+json` — Type: `PublishRequest`

See [PublishRequest](#publishrequest) in Models.

**Request example:**
```json
{
  "message": "string"
}
```

**Responses:**

- `200`: Returns an empty response body.
- `400`: Invalid request.
- `401`: The API key is not valid for this operation / You don't have the authorization.
- `403`: Publishing is not allowed on this experience.
- `500`: Server internal error / Unknown error.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/v1/universes/{UNIVERSEID}/topics/{TOPIC}" \
  -H "Content-Type: application/json" \
  -d '{
  "message": "string"
}'
```

## Models

### PublishRequest

The request body object with the message string that you want to publish to the live server.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `message` | `string` | No | The message content that you want to publish to the live server. |

## OpenEvalApi (1.0)

### POST `/open-eval-api/v1/eval` [BETA]

Performs the evaluation of the Lua script.

**Auth:** Cookie (`.ROBLOSECURITY`) or API Key (`x-api-key` header)

**Scopes:** `studio-evaluations:create`

**Request Body:** `application/json-patch+json` — Type: `EvalRequest`

See [EvalRequest](#evalrequest) in Models.

**Request example:**
```json
{
  "name": "string",
  "description": "string",
  "use_reference_mode": false,
  "input_script": "string",
  "custom_llm_info": {
    "name": "string",
    "model_version": "string",
    "url": "string",
    "api_key": "string"
  }
}
```

**Responses:**

- `200`: OK → `EvalResponse`

**Response fields** (`EvalResponse`)

See [EvalResponse](#evalresponse) in Models.

**Response example:**
```json
{
  "job_id": "string",
  "status_code": 0,
  "error": "string"
}
```

**Rate Limits:** perApiKeyOwner: 100/day

**Example:**
```bash
curl -X POST -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/open-eval-api/v1/eval" \
  -H "Content-Type: application/json" \
  -d '{
  "name": "string",
  "description": "string",
  "use_reference_mode": false,
  "input_script": "string",
  "custom_llm_info": {
    "name": "string",
    "model_version": "string",
    "url": "string",
    "api_key": "string"
  }
}'
```

### GET `/open-eval-api/v1/eval-records/{jobId}` [BETA]

Gets the evaluation record by job ID.

**Auth:** Cookie (`.ROBLOSECURITY`) or API Key (`x-api-key` header)

**Scopes:** `studio-evaluations:create`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `jobId` | path | `string` | Yes | The job ID of the evaluation record. |

**Responses:**

- `200`: OK → `EvalRecord`

**Response fields** (`EvalRecord`)

See [EvalRecord](#evalrecord) in Models.

**Response example:**
```json
{
  "id": 0,
  "name": "string",
  "user": {
    "id": "string"
  },
  "useReferenceMode": "string",
  "description": "string",
  "jobId": "string"
}
```

**Rate Limits:** perApiKeyOwner: 60/minute

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/open-eval-api/v1/eval-records/{JOBID}"
```

## Models

### CustomLlmInfo

Contains information to override the default LLM endpoint and credentials.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | `string` | Yes | The name of the custom LLM provider (claude, gemini, openai). |
| `model_version` | `string` | No | The specific model version to use (e.g., "gemini-2.5-pro-preview-03-25"). If not provided, falls back to the provider name. |
| `url` | `string` | Yes | The custom LLM endpoint URL. |
| `api_key` | `string` | No | The API key to access the custom LLM. |

### EvalJsonRecord

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `passes` | `integer` | No |  |
| `fails` | `integer` | No |  |
| `checks` | `integer` | No |  |
| `warning` | `string` | No |  |
| `error` | `string` | No |  |
| `interruptions` | `InterruptionRecord[]` | No |  |

### EvalRecord

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | `integer` | No |  |
| `name` | `string` | Yes |  |
| `user` | `User` | No |  |
| `useReferenceMode` | `string` | No |  |
| `description` | `string` | No |  |
| `jobId` | `string` | Yes |  |
| `inputScript` | `string` | Yes |  |
| `jobStatus` | `string` | No |  |
| `results` | `EvalResultRecord[]` | No |  |
| `fullLogs` | `string` | No |  |
| `evalSucceeded` | `string` | No |  |
| `createUtc` | `string` | No |  |

### EvalRequest

The request model for the evaluation.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | `string` | Yes |  |
| `description` | `string` | No |  |
| `use_reference_mode` | `boolean` | No |  |
| `input_script` | `string` | Yes |  |
| `custom_llm_info` | `CustomLlmInfo` | No |  |

### EvalResponse

The response model for the evaluation.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `job_id` | `string` | No |  |
| `status_code` | `integer` | No | Gets or sets the status code of the response. |
| `error` | `string` | No | Gets or sets the error message associated with the response. |

### EvalResultRecord

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `mode` | `string` | No |  |
| `result` | `EvalJsonRecord` | No |  |

### InterruptionRecord

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `check` | `integer` | No |  |
| `type` | `string` | No |  |

### User

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | `string` | No |  |

## SecretsStoreService (1.0)

### GET `/cloud/v2/universes/{universeId}/secrets` [BETA]

List Secrets

Lists all secrets defined for a universe.
Secret content is not returned for security reasons - only metadata such as ID, domain, creation and update timestamps are included.

Only the owner of the universe can list secrets. For group-owned universes, only the group owner or authorized
members can list secrets.

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `universe.secret:read`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer` | Yes | The universe ID |
| `limit` | query | `integer` | No | Number of secrets to return per page (1-500, default 10) |
| `cursor` | query | `string` | No | Pagination cursor from previous response |

**Responses:**

- `200`: OK → `SecretPaginatedList`
- `400`: Bad Request → `ProblemDetails`
- `403`: Forbidden → `ProblemDetails`

**Response fields** (`SecretPaginatedList`)

See [SecretPaginatedList](#secretpaginatedlist) in Models.

**Response example:**
```json
{
  "secrets": [
    {
      "id": "...",
      "secret": "...",
      "key_id": "...",
      "domain": "...",
      "create_time": "...",
      "update_time": "..."
    }
  ],
  "nextPageCursor": "string",
  "previousPageCursor": "string"
}
```

**Error handling:** `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 120/minute, perOauth2Authorization: 120/minute

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/cloud/v2/universes/{UNIVERSEID}/secrets"
```

### POST `/cloud/v2/universes/{universeId}/secrets` [BETA]

Create Secret

Creates a new secret. A maximum of 500 secrets per universe is allowed.
            
Only the owner of the universe can create secrets. For group-owned universes, only the group owner or authorized
members can create secrets.
            
To encrypt the secret:
1. Get the public key using the Get Public Key endpoint
2. Encrypt your secret using LibSodium sealed box
3. Base64 encode the encrypted content

Include the key_id from the public key response in the request.

For an example, see the [Secrets store guide](https://create.roblox.com/docs/cloud/guides/secrets-store).

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `universe.secret:write`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer` | Yes | The universe ID |

**Request Body:** `application/json` — Type: `Secret`

See [Secret](#secret) in Models.

**Request example:**
```json
{
  "id": "string",
  "secret": "string",
  "key_id": "string",
  "domain": "string",
  "create_time": "string",
  "update_time": "string"
}
```

**Responses:**

- `201`: Created → `Secret`
- `400`: Bad Request → `ProblemDetails`
- `403`: Forbidden → `ProblemDetails`
- `409`: Conflict → `ProblemDetails`

**Response fields** (`Secret`)

See [Secret](#secret) in Models.

**Response example:**
```json
{
  "id": "string",
  "secret": "string",
  "key_id": "string",
  "domain": "string",
  "create_time": "string",
  "update_time": "string"
}
```

**Error handling:** `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 120/minute, perOauth2Authorization: 120/minute

**Example:**
```bash
curl -X POST -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/cloud/v2/universes/{UNIVERSEID}/secrets" \
  -H "Content-Type: application/json" \
  -d '{
  "id": "string",
  "secret": "string",
  "key_id": "string",
  "domain": "string",
  "create_time": "string",
  "update_time": "string"
}'
```

### PATCH `/cloud/v2/universes/{universeId}/secrets/{secretId}` [BETA]

Update Secret

Updates an existing secret.

Only the owner of the universe can update secrets. For group-owned universes, only the group owner or authorized
members can update secrets.

Only the secret content, key_id, and domain can be updated - the secret ID cannot be changed.

To encrypt the updated secret:
1. Get the current public key using the GetPublicKey endpoint
2. Encrypt your new secret content using LibSodium sealed box
3. Base64 encode the encrypted content

Include the key_id from the public key response in the request.

For an example, see the [Secrets store guide](https://create.roblox.com/docs/cloud/guides/secrets-store).

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `universe.secret:write`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer` | Yes | The universe ID |
| `secretId` | path | `string` | Yes | The ID of the secret to update |

**Request Body:** `application/json` — Type: `Secret`

See [Secret](#secret) in Models.

**Request example:**
```json
{
  "id": "string",
  "secret": "string",
  "key_id": "string",
  "domain": "string",
  "create_time": "string",
  "update_time": "string"
}
```

**Responses:**

- `200`: OK → `Secret`
- `400`: Bad Request → `ProblemDetails`
- `403`: Forbidden → `ProblemDetails`
- `404`: Not Found → `ProblemDetails`

**Response fields** (`Secret`)

See [Secret](#secret) in Models.

**Response example:**
```json
{
  "id": "string",
  "secret": "string",
  "key_id": "string",
  "domain": "string",
  "create_time": "string",
  "update_time": "string"
}
```

**Error handling:** `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 120/minute, perOauth2Authorization: 120/minute

**Example:**
```bash
curl -X PATCH -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/cloud/v2/universes/{UNIVERSEID}/secrets/{SECRETID}" \
  -H "Content-Type: application/json" \
  -d '{
  "id": "string",
  "secret": "string",
  "key_id": "string",
  "domain": "string",
  "create_time": "string",
  "update_time": "string"
}'
```

### DELETE `/cloud/v2/universes/{universeId}/secrets/{secretId}` [BETA]

Delete Secret

Permanently deletes a secret from a universe.

Only the owner of the universe can delete secrets. For group-owned universes, only the group owner or authorized
members can delete secrets.

This operation is irreversible. Make sure you no longer need the secret before deleting it.

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `universe.secret:write`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer` | Yes | The universe ID |
| `secretId` | path | `string` | Yes | The ID of the secret to delete |

**Responses:**

- `200`: OK
- `400`: Bad Request → `ProblemDetails`
- `403`: Forbidden → `ProblemDetails`
- `404`: Not Found → `ProblemDetails`

**Error handling:** `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 120/minute, perOauth2Authorization: 120/minute

**Example:**
```bash
curl -X DELETE -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/cloud/v2/universes/{UNIVERSEID}/secrets/{SECRETID}"
```

### GET `/cloud/v2/universes/{universeId}/secrets/public-key` [BETA]

Get Public Key

Retrieves the public key for a universe. You need this key to encrypt secret content 
before sending it to Roblox.

Only the owner of the universe can retrieve the public key. For group-owned universes, only the group owner or
authorized members can retrieve the public key.

The secret id field is static and always returns "public-key".

The returned public key in the secret field is universe-specific and derived from a master key using the universe ID.
Use this key with LibSodium sealed box encryption to encrypt your secret content before 
creating or updating secrets.

Include the key_id from the public key response in the request to create or update a secret.

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `universe.secret:read`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer` | Yes | The universe ID |

**Responses:**

- `200`: OK → `Secret`
- `400`: Bad Request → `ProblemDetails`
- `403`: Forbidden → `ProblemDetails`

**Response fields** (`Secret`)

See [Secret](#secret) in Models.

**Response example:**
```json
{
  "id": "string",
  "secret": "string",
  "key_id": "string",
  "domain": "string",
  "create_time": "string",
  "update_time": "string"
}
```

**Error handling:** `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 120/minute, perOauth2Authorization: 120/minute

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/cloud/v2/universes/{UNIVERSEID}/secrets/public-key"
```

## Models

### ProblemDetails

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `type` | `string` | No |  |
| `title` | `string` | No |  |
| `status` | `string` | No |  |
| `detail` | `string` | No |  |
| `instance` | `string` | No |  |

### Secret

Universe-specific secret, identified by `id`, and belonging to a specific `environment`.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | `string` | No | The user-specified secret name. Examples: "aws", "gcp", "discord".  Static when getting the public key for a universe.  Must be alphanumeric or underscore, 1-64 characters, not starting with a number. |
| `secret` | `string` | No | The binary secret content. Examples: API key content (text), private keys.  When created, the secret must be encrypted using LibSodium sealed box and encoded in base64 with the universe's public key.  Contains the public key when getting the public key for a universe. |
| `key_id` | `string` | No | Encryption key identifier. Identifies the key that was used to encrypt the secret content. |
| `domain` | `string` | No | The domain wildcard that restricts the purpose of the key.   You can restrict the URLs callable via HttpService to a specific domain, e.g. "api.example.com" or "*.myservice.org".  An empty or null domain means that the secret is a private key and cannot be transformed with addPrefix/addSuffix or sent as a header or URL.  In order to make the secret accessible for all domains, use "*" |
| `create_time` | `string` | No | Date and time when the secret was originally created. |
| `update_time` | `string` | No | Date and time when the secret was last updated |

### SecretPaginatedList

Wrapper for the paginated collection output.
Complies with the REST conventions, containing
next/previous page, and a data field containing the actual list.
            
Needed only to simplify JSON serialization, and can technically
be AutoMapper-ed from the EaaS or any other data provider.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `secrets` | `Secret[]` | No | Gets the actual list of items to return |
| `nextPageCursor` | `string` | No | Gets the cursor where the pagination stopped after fetching `data`. `null` if there is no more data available. |
| `previousPageCursor` | `string` | No | Gets the cursor pointing at the previous page. `null` when it's the first page. |

## Toolbox.Service (1.0)

### GET `/toolbox-service/v2/assets:search` [BETA]

Search Creator Store Assets

Search Creator Store for assets.

**Auth:** Cookie (`.ROBLOSECURITY`) or API Key (`x-api-key` header)

**Scopes:** `creator-store-product:read`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `searchCategoryType` | query | `any` | Yes | The asset type to search within. |
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
| `includeTopCharts` | query | `boolean` | No |  |
| `audioTypes` | query | `SearchAudioTypeModel[]` | No | When searching for audio, the type of the audio assets. |
| `includedInstanceTypes` | query | `ModelInstanceType[]` | No | When searching for models, this filters that the following [Instance](https://create.roblox.com/docs/reference/engine/classes/Instance) types are included in the model. |
| `includeOnlyVerifiedCreators` | query | `boolean` | No | Whether the results should only include assets created by verified creators. |
| `minPriceCents` | query | `integer` | No | The minimum price of the asset in cents. If included, must be greater than or equal to 0. |
| `maxPriceCents` | query | `integer` | No | The maximum price of the asset in cents. If included, must be greater than or equal to 0. |
| `facets` | query | `string[]` | No | Additional keywords to query by. |
| `categoryPath` | query | `string` | No |  |
| `searchView` | query | `any` | No | Indicates which fields will be populated in the response. |
| `musicChartType` | query | `any` | No | Indicates which music charts to filter from. |

**Responses:**

- `200`: Success → `SearchCreatorStoreAssetsResponse`
- `400`: Bad Request → `any`
- `429`: Too Many Requests → `any`
- `500`: Server Error

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
  "filteredKeyword": "string"
}
```

**Error handling:** `429`: Retry with exponential backoff (start at 1s). 

**Rate Limits:** perApiKeyOwner: 1000/minute

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/toolbox-service/v2/assets:search?searchCategoryType={VALUE}"
```

### GET `/toolbox-service/v2/assets/{id}` [BETA]

Get Creator Store Asset Details

Get details for a single Creator Store asset.

**Auth:** Cookie (`.ROBLOSECURITY`) or API Key (`x-api-key` header)

**Scopes:** `creator-store-product:read`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `id` | path | `integer` | Yes | The asset ID to retrieve details for. |

**Responses:**

- `200`: Success → `CreatorStoreAsset`
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

**Rate Limits:** perApiKeyOwner: 1000/minute

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/toolbox-service/v2/assets/{ID}"
```

## Place publishing (v1)

You can send and receive the following request and response payloads to publish and update your places on Roblox. For information on the usage of the API, see the [usage guide](/cloud/guides/usage-place-publishing.md).

### POST `/v1/{universeId}/places/{placeId}/versions` [BETA]

Publish a new place or update an existing place with a new version. Provide a RBXL or RBXLX file in the data-binary.

**Auth:** API Key (`x-api-key` header)

**Scopes:** `universe-places:write`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer` | Yes | The identifier of the experience in which you want to publish your place to. You can [copy your experience's Universe ID](/cloud/guides/usage-place-publishing.md#publishing-a-place) on **Creator Dashboard**. |
| `placeId` | path | `integer` | Yes | The identifier of your place. See [Publishing places with API keys](/cloud/guides/usage-place-publishing.md) on obtaining a Place ID. |
| `versionType` | query | `string` | No | Can only be either:  - `Saved`: the place file should be saved, but not published.   - `Published`: the place file should be saved and published. |

**Responses:**

- `200`: Returns the published place's version number. → `string`
- `400`: Invalid request / Invalid file content.
- `401`: API key not valid for operation, user does not have authorization.
- `403`: Publish not allowed on place.
- `404`: Place or universe does not exist.
- `409`: Place not part of the universe.
- `500`: Server internal error / Unknown error.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/v1/{UNIVERSEID}/places/{PLACEID}/versions"
```