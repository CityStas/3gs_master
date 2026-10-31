---
name: "Asset Delivery Api v2"
last_updated: 2026-10-30T19:56:08Z
type: legacy
api_base_url: "https://assetdelivery.roblox.com"
versions: [v2, v1]
endpoints: 14
auth: [cookie]
---

# Asset Delivery Api v2

> **Warning:** Legacy APIs with cookie authentication can incorporate breaking changes without notice. We don't recommend them for production applications.

**Base URL:** `https://assetdelivery.roblox.com`
**Versions:** v2, v1

## V2

### GET `/v2/alias/{alias}`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `alias` | path | `string` | Yes |  |
| `Accept-Encoding` | header | `string` | Yes |  |
| `Roblox-Place-Id` | header | `integer (int64)` | Yes |  |
| `AssetType` | header | `string` | Yes |  |
| `AssetFormat` | header | `string` | Yes |  |
| `Roblox-AssetFormat` | header | `string` | Yes |  |
| `Roblox-Usage-Context` | header | `string` | No |  |
| `skipSigningScripts` | query | `boolean` | No |  |
| `clientInsert` | query | `integer (int32)` | No |  |
| `scriptinsert` | query | `integer (int32)` | No |  |
| `modulePlaceId` | query | `integer (int64)` | No |  |
| `serverplaceid` | query | `integer (int64)` | No |  |
| `expectedAssetType` | query | `string` | No |  |
| `accessContext` | query | `string` | No |  |

**Responses:**

- `200`: OK

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://assetdelivery.roblox.com/v2/alias/{ALIAS}"
```

### GET `/v2/asset`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `Accept-Encoding` | header | `string` | Yes |  |
| `Roblox-Place-Id` | header | `integer (int64)` | Yes |  |
| `AssetType` | header | `string` | Yes |  |
| `AssetFormat` | header | `string` | Yes |  |
| `Roblox-AssetFormat` | header | `string` | Yes |  |
| `Roblox-Usage-Context` | header | `string` | No |  |
| `id` | query | `integer (int64)` | No |  |
| `userAssetId` | query | `integer (int64)` | No |  |
| `assetVersionId` | query | `integer (int64)` | No |  |
| `version` | query | `integer (int32)` | No |  |
| `universeId` | query | `integer (int64)` | No |  |
| `clientInsert` | query | `integer (int32)` | No |  |
| `scriptinsert` | query | `integer (int32)` | No |  |
| `modulePlaceId` | query | `integer (int64)` | No |  |
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
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://assetdelivery.roblox.com/v2/asset"
```

### GET `/v2/assetId/{assetId}`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `assetId` | path | `integer (int64)` | Yes |  |
| `Accept-Encoding` | header | `string` | Yes |  |
| `Roblox-Place-Id` | header | `integer (int64)` | Yes |  |
| `AssetType` | header | `string` | Yes |  |
| `AssetFormat` | header | `string` | Yes |  |
| `Roblox-AssetFormat` | header | `string` | Yes |  |
| `Roblox-Usage-Context` | header | `string` | No |  |
| `skipSigningScripts` | query | `boolean` | No |  |
| `clientInsert` | query | `integer (int32)` | No |  |
| `scriptinsert` | query | `integer (int32)` | No |  |
| `modulePlaceId` | query | `integer (int64)` | No |  |
| `serverplaceid` | query | `integer (int64)` | No |  |
| `expectedAssetType` | query | `string` | No |  |
| `doNotFallbackToBaselineRepresentation` | query | `boolean` | No |  |
| `contentRepresentationPriorityList` | query | `string` | No |  |
| `accessContext` | query | `string` | No |  |

**Responses:**

- `200`: OK

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://assetdelivery.roblox.com/v2/assetId/{ASSETID}"
```

### GET `/v2/assetId/{assetId}/version/{versionNumber}`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `assetId` | path | `integer (int64)` | Yes |  |
| `versionNumber` | path | `integer (int32)` | Yes |  |
| `Accept-Encoding` | header | `string` | Yes |  |
| `Roblox-Place-Id` | header | `integer (int64)` | Yes |  |
| `AssetType` | header | `string` | Yes |  |
| `AssetFormat` | header | `string` | Yes |  |
| `Roblox-AssetFormat` | header | `string` | Yes |  |
| `Roblox-Usage-Context` | header | `string` | No |  |
| `skipSigningScripts` | query | `boolean` | No |  |
| `clientInsert` | query | `integer (int32)` | No |  |
| `scriptinsert` | query | `integer (int32)` | No |  |
| `modulePlaceId` | query | `integer (int64)` | No |  |
| `serverplaceid` | query | `integer (int64)` | No |  |
| `expectedAssetType` | query | `string` | No |  |
| `doNotFallbackToBaselineRepresentation` | query | `boolean` | No |  |
| `contentRepresentationPriorityList` | query | `string` | No |  |
| `accessContext` | query | `string` | No |  |

**Responses:**

- `200`: OK

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://assetdelivery.roblox.com/v2/assetId/{ASSETID}/version/{VERSIONNUMBER}"
```

### GET `/v2/marAssetHash/{marAssetHash}/marCheckSum/{marCheckSum}`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `marAssetHash` | path | `string` | Yes |  |
| `marCheckSum` | path | `string` | Yes |  |
| `Accept-Encoding` | header | `string` | Yes |  |
| `Roblox-Place-Id` | header | `integer (int64)` | Yes |  |
| `AssetType` | header | `string` | Yes |  |
| `AssetFormat` | header | `string` | Yes |  |
| `Roblox-AssetFormat` | header | `string` | Yes |  |
| `skipSigningScripts` | query | `boolean` | No |  |
| `clientInsert` | query | `integer (int32)` | No |  |
| `scriptinsert` | query | `integer (int32)` | No |  |
| `modulePlaceId` | query | `integer (int64)` | No |  |
| `serverplaceid` | query | `integer (int64)` | No |  |
| `expectedAssetType` | query | `string` | No |  |

**Responses:**

- `200`: OK

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://assetdelivery.roblox.com/v2/marAssetHash/{MARASSETHASH}/marCheckSum/{MARCHECKSUM}"
```

### POST `/v2/assets/batch`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `Roblox-Place-Id` | header | `integer (int64)` | Yes |  |
| `Roblox-Browser-Asset-Request` | header | `string` | Yes |  |

**Request Body:** `application/json` — Type: `Roblox.Web.Assets.BatchAssetRequestItem[]`

See [Roblox.Web.Assets.BatchAssetRequestItem](#roblox-web-assets-batchassetrequestitem) in Models.

**Responses:**

- `200`: OK

**Example:**
```bash
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
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

## Models

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

## V1

### GET `/v1/alias/{alias}`

Retrieves an asset by its alias (universeID/name)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `alias` | path | `string` | Yes | The alias of the asset to retrieve. |
| `Accept-Encoding` | header | `string` | Yes |  |
| `Roblox-Place-Id` | header | `integer (int64)` | Yes |  |
| `AssetType` | header | `string` | Yes |  |
| `AssetFormat` | header | `string` | Yes |  |
| `Roblox-AssetFormat` | header | `string` | Yes |  |
| `Roblox-Usage-Context` | header | `string` | No |  |
| `skipSigningScripts` | query | `boolean` | No |  |
| `clientInsert` | query | `integer (int32)` | No |  |
| `scriptinsert` | query | `integer (int32)` | No |  |
| `modulePlaceId` | query | `integer (int64)` | No |  |
| `serverplaceid` | query | `integer (int64)` | No |  |
| `expectedAssetType` | query | `string` | No |  |
| `accessContext` | query | `string` | No |  |

**Responses:**

- `200`: OK

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://assetdelivery.roblox.com/v1/alias/{ALIAS}"
```

### GET `/v1/asset`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `Accept-Encoding` | header | `string` | Yes |  |
| `Roblox-Place-Id` | header | `integer (int64)` | Yes |  |
| `AssetType` | header | `string` | Yes |  |
| `AssetFormat` | header | `string` | Yes |  |
| `Roblox-AssetFormat` | header | `string` | Yes |  |
| `Roblox-Usage-Context` | header | `string` | No |  |
| `id` | query | `integer (int64)` | No |  |
| `userAssetId` | query | `integer (int64)` | No |  |
| `assetVersionId` | query | `integer (int64)` | No |  |
| `version` | query | `integer (int32)` | No |  |
| `universeId` | query | `integer (int64)` | No |  |
| `clientInsert` | query | `integer (int32)` | No |  |
| `scriptinsert` | query | `integer (int32)` | No |  |
| `modulePlaceId` | query | `integer (int64)` | No |  |
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
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://assetdelivery.roblox.com/v1/asset"
```

### GET `/v1/assetId/{assetId}`

Retrieves an asset by its ID

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `assetId` | path | `integer (int64)` | Yes | The ID of the asset to retrieve. |
| `Accept-Encoding` | header | `string` | Yes |  |
| `Roblox-Place-Id` | header | `integer (int64)` | Yes |  |
| `AssetType` | header | `string` | Yes |  |
| `AssetFormat` | header | `string` | Yes |  |
| `Roblox-AssetFormat` | header | `string` | Yes |  |
| `Roblox-Usage-Context` | header | `string` | No |  |
| `skipSigningScripts` | query | `boolean` | No |  |
| `clientInsert` | query | `integer (int32)` | No |  |
| `scriptinsert` | query | `integer (int32)` | No |  |
| `modulePlaceId` | query | `integer (int64)` | No |  |
| `serverplaceid` | query | `integer (int64)` | No |  |
| `expectedAssetType` | query | `string` | No |  |
| `doNotFallbackToBaselineRepresentation` | query | `boolean` | No |  |
| `contentRepresentationPriorityList` | query | `string` | No |  |
| `accessContext` | query | `string` | No |  |

**Responses:**

- `200`: OK

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://assetdelivery.roblox.com/v1/assetId/{ASSETID}"
```

### GET `/v1/assetId/{assetId}/version/{versionNumber}`

Retrieves an asset by its ID and version number.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `assetId` | path | `integer (int64)` | Yes | The ID of the asset to retrieve. |
| `versionNumber` | path | `integer (int32)` | Yes | The version of the asset to retrieve. |
| `Accept-Encoding` | header | `string` | Yes |  |
| `Roblox-Place-Id` | header | `integer (int64)` | Yes |  |
| `AssetType` | header | `string` | Yes |  |
| `AssetFormat` | header | `string` | Yes |  |
| `Roblox-AssetFormat` | header | `string` | Yes |  |
| `Roblox-Usage-Context` | header | `string` | No |  |
| `skipSigningScripts` | query | `boolean` | No |  |
| `clientInsert` | query | `integer (int32)` | No |  |
| `scriptinsert` | query | `integer (int32)` | No |  |
| `modulePlaceId` | query | `integer (int64)` | No |  |
| `serverplaceid` | query | `integer (int64)` | No |  |
| `expectedAssetType` | query | `string` | No |  |
| `doNotFallbackToBaselineRepresentation` | query | `boolean` | No |  |
| `contentRepresentationPriorityList` | query | `string` | No |  |
| `accessContext` | query | `string` | No |  |

**Responses:**

- `200`: OK

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://assetdelivery.roblox.com/v1/assetId/{ASSETID}/version/{VERSIONNUMBER}"
```

### GET `/v1/marAssetHash/{marAssetHash}/marCheckSum/{marCheckSum}`

Retrieves an asset by its mar (moderation agnostic) hash and mar (moderation agnostic) checksum.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `marAssetHash` | path | `string` | Yes | The mar (moderation agnostic) hash of the asset to retrieve. |
| `marCheckSum` | path | `string` | Yes | The mar (moderation agnostic) checksum of the asset to retrieve. |
| `Accept-Encoding` | header | `string` | Yes |  |
| `Roblox-Place-Id` | header | `integer (int64)` | Yes |  |
| `AssetType` | header | `string` | Yes |  |
| `AssetFormat` | header | `string` | Yes |  |
| `Roblox-AssetFormat` | header | `string` | Yes |  |
| `skipSigningScripts` | query | `boolean` | No |  |
| `clientInsert` | query | `integer (int32)` | No |  |
| `scriptinsert` | query | `integer (int32)` | No |  |
| `modulePlaceId` | query | `integer (int64)` | No |  |
| `serverplaceid` | query | `integer (int64)` | No |  |
| `expectedAssetType` | query | `string` | No |  |

**Responses:**

- `200`: OK
- `400`: 2: invalid server request 3: Encoding cannot be empty
- `404`: 5: Asset hash cannot be empty

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://assetdelivery.roblox.com/v1/marAssetHash/{MARASSETHASH}/marCheckSum/{MARCHECKSUM}"
```

### GET `/v1/openCloud/assetId/{assetId}`

Retrieves an asset by its ID with OpenCloud auth.

Returns an object containing a `location` property which is a temporary CDN URL for the asset content. All asset types are supported.
You should request that URL with the `Accept-Encoding: gzip` header and decompress the result if the response is gzipped. If you are using cURL, the `--compressed` flag will automate these steps for you.
This endpoint is expected to be called with API key authentication through `apis.roblox.com/asset-delivery-api/v1/assetId/{assetId}`.
While you are able to make requests to this endpoint with Cookie authentication via `assetdelivery.roblox.com/v1/openCloud/assetId/{assetId}`, we highly discourage use this way.
Expect unannounced removal of this second route in the future.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `assetId` | path | `integer (int64)` | Yes | The ID of the asset to retrieve. |
| `Accept-Encoding` | header | `string` | No | The Accept-Encoding header value specifying compression formats (e.g., "gzip, deflate"). Defaults to "gzip, deflate" if not provided. |
| `Roblox-Place-Id` | header | `integer (int64)` | No | The Roblox-Place-Id header value identifying the place making the request. |
| `AssetType` | header | `string` | No | The AssetType header value specifying the expected asset type. |
| `AssetFormat` | header | `string` | No | The AssetFormat header value specifying the desired asset format. Overridden by robloxAssetFormat if both are provided. |
| `Roblox-AssetFormat` | header | `string` | No | The Roblox-AssetFormat header value specifying the preferred Roblox-specific asset format. Takes precedence over assetFormat. |
| `Roblox-Usage-Context` | header | `string` | No |  |
| `skipSigningScripts` | query | `boolean` | No | Whether to skip script signing for the returned asset. Used for script assets that don't require signing. |
| `clientInsert` | query | `integer (int32)` | No | Set to 1 to indicate this is a client insert request. |
| `scriptinsert` | query | `integer (int32)` | No | Set to 1 to indicate this is a script insert request. |
| `modulePlaceId` | query | `integer (int64)` | No | The place ID of the module making the request. |
| `serverplaceid` | query | `integer (int64)` | No | The server place ID making the request. |
| `expectedAssetType` | query | `string` | No | The expected asset type as a fallback when assetType header is not provided. |
| `doNotFallbackToBaselineRepresentation` | query | `boolean` | No | Whether to prevent fallback to baseline representation when specific content representations are not available. |
| `contentRepresentationPriorityList` | query | `string` | No | Base64URL-encoded JSON string specifying the priority list of desired content representations (format, version, fidelity). |
| `accessContext` | query | `string` | No |  |

**Responses:**

- `200`: OK
- `401`: 0: Authorization has been denied for this request.

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://assetdelivery.roblox.com/v1/openCloud/assetId/{ASSETID}"
```

### GET `/v1/openCloud/assetId/{assetId}/version/{versionNumber}`

Retrieves an asset by its ID and version number with OpenCloud auth.

Refer to the assetId endpoint for details on usage.
This endpoint is expected to be called with API key authentication through `apis.roblox.com/asset-delivery-api/v1/assetId/{assetId}/version/{versionNumber}`.
While you are able to make requests to this endpoint with Cookie authentication via `assetdelivery.roblox.com/v1/openCloud/assetId/{assetId}/version/{versionNumber}`, we highly discourage use this way.
Expect unannounced removal of this second route in the future.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `assetId` | path | `integer (int64)` | Yes | The ID of the asset to retrieve. |
| `versionNumber` | path | `integer (int32)` | Yes | The version number of the asset to retrieve. |
| `Accept-Encoding` | header | `string` | No |  |
| `Roblox-Place-Id` | header | `integer (int64)` | No |  |
| `AssetType` | header | `string` | No |  |
| `AssetFormat` | header | `string` | No |  |
| `Roblox-AssetFormat` | header | `string` | No |  |
| `Roblox-Usage-Context` | header | `string` | No |  |
| `skipSigningScripts` | query | `boolean` | No |  |
| `clientInsert` | query | `integer (int32)` | No |  |
| `scriptinsert` | query | `integer (int32)` | No |  |
| `modulePlaceId` | query | `integer (int64)` | No |  |
| `serverplaceid` | query | `integer (int64)` | No |  |
| `expectedAssetType` | query | `string` | No |  |
| `doNotFallbackToBaselineRepresentation` | query | `boolean` | No |  |
| `contentRepresentationPriorityList` | query | `string` | No |  |
| `accessContext` | query | `string` | No |  |

**Responses:**

- `200`: OK
- `401`: 0: Authorization has been denied for this request.

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://assetdelivery.roblox.com/v1/openCloud/assetId/{ASSETID}/version/{VERSIONNUMBER}"
```

### POST `/v1/assets/batch`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `Roblox-Place-Id` | header | `integer (int64)` | Yes |  |
| `Roblox-Browser-Asset-Request` | header | `string` | Yes |  |

**Request Body:** `application/json` — Type: `Roblox.Web.Assets.BatchAssetRequestItem[]`

See [Roblox.Web.Assets.BatchAssetRequestItem](#roblox-web-assets-batchassetrequestitem) in Models.

**Responses:**

- `200`: OK

**Example:**
```bash
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
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

## Models

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