---
name: "Avatars"
last_updated: 2026-10-30T19:56:08Z
type: feature
api_base_url: "https://apis.roblox.com"
endpoints: 36
auth: [api-key, oauth2, cookie]
description: "Customize user avatars and manage outfits programmatically, including [retrieving a user's avatar configuration](#avatar_get_v4_avatar_users__userId_), body colors, scales, [thumbnail generation](#Cloud_GenerateUserThumbnail), and [thumbnail generation operation retrieval](#Cloud_GetUserThumbnailGenerationOperation)"
---

# Avatars

Customize user avatars and manage outfits programmatically, including [retrieving a user's avatar configuration](#avatar_get_v4_avatar_users__userId_), body colors, scales, [thumbnail generation](#Cloud_GenerateUserThumbnail), and [thumbnail generation operation retrieval](#Cloud_GetUserThumbnailGenerationOperation).

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

### GET `/cloud/v2/users/{user_id}/operations/{operation_id}` [STABLE]

Get User Thumbnail Generation Operation

Gets the status and result of a
[Generate User Thumbnail](https://create.roblox.com/docs/cloud/reference/features/users#Cloud_GenerateUserThumbnail)
long-running operation.
            
Call this with the operation `path` returned by Generate User Thumbnail,
polling until `done` is `true`. Once complete, the operation contains
either `response` or `error`:
            
- If `response` is set, `response.imageUri` contains the generated
  thumbnail URL.
- If `error` is set, the thumbnail couldn't be generated and `response` is
  not set. `error.code` and `error.message` describe the reason.
            
Always check for `error` before reading `response.imageUri`.

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `user_id` | path | `string` | Yes | The user ID. |
| `operation_id` | path | `string` | Yes | The operation ID returned by Generate User Thumbnail. |

**Responses:**

- `200`: OK → `OpenCloudUsers.Operation`

**Response fields** (`OpenCloudUsers.Operation`)

See [OpenCloudUsers.Operation](#opencloudusers-operation) in Models.

**Response example:**
```json
{
  "path": "string",
  "metadata": "...",
  "done": false,
  "error": "...",
  "response": "..."
}
```

**Rate Limits:** perApiKeyOwner: 1000/minute, perOauth2Authorization: 10/minute

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/cloud/v2/users/{USER_ID}/operations/{OPERATION_ID}"
```

### GET `/cloud/v2/users/{user_id}:generateThumbnail` [STABLE]

Generate User Thumbnail

Generates and returns the URL for the user's avatar thumbnail.
            
This is a long-running operation: the response is an `Operation` object.
Poll the operation using its returned `path` until `done` is `true`. A
completed operation contains either `response` or `error`:
            
- If `response` is set, `response.imageUri` contains the thumbnail URL.
- If `error` is set, the thumbnail couldn't be generated and `response` is
  not set. `error.code` and `error.message` describe the reason.
            
Always check for `error` before reading `response.imageUri`. See
[Get User Thumbnail Generation Operation](https://create.roblox.com/docs/cloud/reference/features/users#Cloud_GetUserThumbnailGenerationOperation).

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `user_id` | path | `string` | Yes | The user ID. |
| `size` | query | `integer` | No | Size of the generated thumbnail. The generated thumbnail will have `size * size` dimension.              Currently supported values: 48, 50, 60, 75, 100, 110, 150, 180, 352, 420, 720 Default is 420. |
| `format` | query | `FORMAT_UNSPECIFIED \| PNG \| JPEG` | No | Specify the format of the generated thumbnail. Default is `PNG`.              Possible values:                \| Value \| Description \|   \| --- \| --- \|   \| FORMAT_UNSPECIFIED \| Default UserThumbnail Format -- set to png \|   \| PNG \| Generate thumbnail in `.png` format \|   \| JPEG \| Generate thumbnail in `.jpg` format \| Valid values: `FORMAT_UNSPECIFIED`, `PNG`, `JPEG` |
| `shape` | query | `SHAPE_UNSPECIFIED \| ROUND \| SQUARE` | No | Specify the shape of the thumbnail. Default is `ROUND` (circular).              Possible values:                \| Value \| Description \|   \| --- \| --- \|   \| SHAPE_UNSPECIFIED \| Default UserThumbnail Shape -- set to round \|   \| ROUND \| Generate thumbnail as a circle. \|   \| SQUARE \| Generate thumbnail as a rectangle. \| Valid values: `SHAPE_UNSPECIFIED`, `ROUND`, `SQUARE` |

**Responses:**

- `200`: OK → `OpenCloudUsers.Operation`

**Response fields** (`OpenCloudUsers.Operation`)

See [OpenCloudUsers.Operation](#opencloudusers-operation) in Models.

**Response example:**
```json
{
  "path": "string",
  "metadata": "...",
  "done": false,
  "error": "...",
  "response": "..."
}
```

**Rate Limits:** perApiKeyOwner: 1000/minute, perOauth2Authorization: 10/minute

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/cloud/v2/users/{USER_ID}:generateThumbnail"
```

### GET `/v1/avatar` *(deprecated)*

Returns details about the authenticated user's avatar.

Please use GET v4/avatar

**Server:** `https://avatar.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `Roblox-Place-Id` | header | `integer` | No |  |

**Responses:**

- `200`: OK → `Roblox.Api.Avatar.Models.AvatarModelV2`
- `401`: 0: Authorization has been denied for this request.

**Response fields** (`Roblox.Api.Avatar.Models.AvatarModelV2`)

See [Roblox.Api.Avatar.Models.AvatarModelV2](#roblox-api-avatar-models-avatarmodelv2) in Models.

**Response example:**
```json
{
  "scales": {
    "height": 0,
    "width": 0,
    "head": 0,
    "depth": 0,
    "proportion": 0,
    "bodyType": 0
  },
  "playerAvatarType": 1,
  "bodyColors": {
    "headColorId": 0,
    "torsoColorId": 0,
    "rightArmColorId": 0,
    "leftArmColorId": 0,
    "rightLegColorId": 0,
    "leftLegColorId": 0
  },
  "assets": [
    {
      "id": "...",
      "name": "...",
      "assetType": "...",
      "currentVersionId": "...",
      "meta": "...",
      "availabilityStatus": "..."
    }
  ],
  "defaultShirtApplied": false,
  "defaultPantsApplied": false
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://avatar.roblox.com/v1/avatar"
```

### GET `/v1/avatar-rules`

Returns the business rules related to avatars.

BodyColorsPalette is a list of valid brickColors you can choose for your avatar.
WearableAssetTypes contains a list of asset types with names, ids, and the maximum number that you can wear at a time.
Does not include packages because they cannot be worn on your avatar directly.
PlayerAvatarTypes are the types of avatars you can choose between.

**Server:** `https://avatar.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `Roblox-Place-Id` | header | `integer` | No |  |

**Responses:**

- `200`: OK → `Roblox.Api.Avatar.Models.AvatarRulesModel`

**Response fields** (`Roblox.Api.Avatar.Models.AvatarRulesModel`)

See [Roblox.Api.Avatar.Models.AvatarRulesModel](#roblox-api-avatar-models-avatarrulesmodel) in Models.

**Response example:**
```json
{
  "playerAvatarTypes": [
    1
  ],
  "scales": "...",
  "wearableAssetTypes": [
    {
      "maxNumber": "...",
      "id": "...",
      "name": "..."
    }
  ],
  "accessoryRefinementTypes": [
    0
  ],
  "accessoryRefinementLowerBounds": "...",
  "accessoryRefinementUpperBounds": "..."
}
```

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://avatar.roblox.com/v1/avatar-rules"
```

### GET `/v1/avatar/metadata`

Returns metadata used by the avatar page of the website.

**Server:** `https://avatar.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Responses:**

- `200`: OK → `Roblox.Api.Avatar.Models.AvatarMetadataModel`

**Response fields** (`Roblox.Api.Avatar.Models.AvatarMetadataModel`)

See [Roblox.Api.Avatar.Models.AvatarMetadataModel](#roblox-api-avatar-models-avatarmetadatamodel) in Models.

**Response example:**
```json
{
  "enableDefaultClothingMessage": false,
  "isAvatarScaleEmbeddedInTab": false,
  "isBodyTypeScaleOutOfTab": false,
  "scaleHeightIncrement": 0,
  "scaleWidthIncrement": 0,
  "scaleHeadIncrement": 0
}
```

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://avatar.roblox.com/v1/avatar/metadata"
```

### POST `/v1/avatar/redraw-thumbnail`

Requests the authenticated user's thumbnail be redrawn.

**Server:** `https://avatar.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `Roblox-Place-Id` | header | `integer` | No |  |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed
- `429`: 1: Redrawing your avatar thumbnail is floodchecked at this time. 1: Redrawing your avatar thumbnail is floodchecked at this time

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `429`: Retry with exponential backoff (start at 1s). `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://avatar.roblox.com/v1/avatar/redraw-thumbnail"
```

### POST `/v1/avatar/set-body-colors` *(deprecated)*

Sets the authenticated user's body colors.

Please use PATCH v4/avatar

**Server:** `https://avatar.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `Roblox-Place-Id` | header | `integer` | No |  |

**Request Body:** `application/json` — Type: `Roblox.Api.Avatar.Models.BodyColorsModel`

See [Roblox.Api.Avatar.Models.BodyColorsModel](#roblox-api-avatar-models-bodycolorsmodel) in Models.

**Request example:**
```json
{
  "headColorId": 0,
  "torsoColorId": 0,
  "rightArmColorId": 0,
  "leftArmColorId": 0,
  "rightLegColorId": 0,
  "leftLegColorId": 0
}
```

**Responses:**

- `200`: OK → `Roblox.Api.Avatar.Models.AvatarApiSuccessResponse`
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed

**Response fields** (`Roblox.Api.Avatar.Models.AvatarApiSuccessResponse`)

See [Roblox.Api.Avatar.Models.AvatarApiSuccessResponse](#roblox-api-avatar-models-avatarapisuccessresponse) in Models.

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
  "https://avatar.roblox.com/v1/avatar/set-body-colors" \
  -H "Content-Type: application/json" \
  -d '{
  "headColorId": 0,
  "torsoColorId": 0,
  "rightArmColorId": 0,
  "leftArmColorId": 0,
  "rightLegColorId": 0,
  "leftLegColorId": 0
}'
```

### POST `/v1/avatar/set-player-avatar-type` *(deprecated)*

Sets the authenticated user's player avatar type (e.g. R6 or R15).

This is the avatar type chosen on the Avatar page. Some games can override this and force your character to be R6 or R15.

Please use PATCH v4/avatar

**Server:** `https://avatar.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `Roblox-Place-Id` | header | `integer` | No |  |

**Request Body:** `application/json` — Type: `Roblox.Api.Avatar.Models.PlayerAvatarTypeModel`

See [Roblox.Api.Avatar.Models.PlayerAvatarTypeModel](#roblox-api-avatar-models-playeravatartypemodel) in Models.

**Request example:**
```json
{
  "playerAvatarType": 1
}
```

**Responses:**

- `200`: OK → `Roblox.Api.Avatar.Models.AvatarApiSuccessResponse`
- `400`: 1: Invalid playerAvatarType. Valid values are:
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 2: You are not allowed to change player avatar type.

**Response fields** (`Roblox.Api.Avatar.Models.AvatarApiSuccessResponse`)

See [Roblox.Api.Avatar.Models.AvatarApiSuccessResponse](#roblox-api-avatar-models-avatarapisuccessresponse) in Models.

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
  "https://avatar.roblox.com/v1/avatar/set-player-avatar-type" \
  -H "Content-Type: application/json" \
  -d '{
  "playerAvatarType": 1
}'
```

### POST `/v1/avatar/set-scales` *(deprecated)*

Sets the authenticated user's scales.

Please use PATCH v4/avatar

**Server:** `https://avatar.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `Roblox-Place-Id` | header | `integer` | No |  |

**Request Body:** `application/json` — Type: `Roblox.Web.Responses.Avatar.ScaleModel`

See [Roblox.Web.Responses.Avatar.ScaleModel](#roblox-web-responses-avatar-scalemodel) in Models.

**Request example:**
```json
{
  "height": 0,
  "width": 0,
  "head": 0,
  "depth": 0,
  "proportion": 0,
  "bodyType": 0
}
```

**Responses:**

- `200`: OK → `Roblox.Api.Avatar.Models.AvatarApiSuccessResponse`
- `400`: 1: Please pass in the scales JSON
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 3: The user does not have permissions to change scales.

**Response fields** (`Roblox.Api.Avatar.Models.AvatarApiSuccessResponse`)

See [Roblox.Api.Avatar.Models.AvatarApiSuccessResponse](#roblox-api-avatar-models-avatarapisuccessresponse) in Models.

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
  "https://avatar.roblox.com/v1/avatar/set-scales" \
  -H "Content-Type: application/json" \
  -d '{
  "height": 0,
  "width": 0,
  "head": 0,
  "depth": 0,
  "proportion": 0,
  "bodyType": 0
}'
```

### GET `/v1/bundles/thumbnails` [STABLE]

Get bundle thumbnails for the given CSV of bundle ids

**Server:** `https://thumbnails.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `bundleIds` | query | `integer[]` | Yes | CSV for the bundle ids to get bundle thumbnails |
| `size` | query | `150x150 \| 420x420` | No | The thumbnail size, formatted widthxheight Valid values: `150x150`, `420x420` |
| `format` | query | `Png \| Webp` | No | The thumbnail format Valid values: `Png`, `Webp` |
| `isCircular` | query | `true \| false` | No | The circle thumbnail output parameter, true or false Valid values: `true`, `false` |

**Responses:**

- `200`: OK
- `400`: 1: There are too many requested Ids. 2: The requested image format is invalid. Please see documentation for valid thumbnail format parameter name and values. 3: The requested size is invalid. Please see documentation for valid thumbnail size parameter name and format. 4: The requested Ids are invalid, of an invalid type or missing. 10: Circular thumbnail requests are not allowed

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://thumbnails.roblox.com/v1/bundles/thumbnails?bundleIds={VALUE}"
```

### GET `/v1/game-start-info`

The server will call this on game server start to request general information about the universe
This is version 1.1, which returns an entry from the UniverseAvatarType enum.
During mixed mode this may return unreliable results.

**Server:** `https://avatar.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | query | `integer` | Yes |  |
| `Roblox-Place-Id` | header | `integer` | No |  |

**Responses:**

- `200`: OK → `Roblox.Api.Avatar.Models.GameStartInfoResponse`

**Response fields** (`Roblox.Api.Avatar.Models.GameStartInfoResponse`)

See [Roblox.Api.Avatar.Models.GameStartInfoResponse](#roblox-api-avatar-models-gamestartinforesponse) in Models.

**Response example:**
```json
{
  "gameAvatarType": "string",
  "allowCustomAnimations": "string",
  "universeAvatarCollisionType": "string",
  "universeAvatarBodyType": "string",
  "jointPositioningType": "string",
  "message": "string"
}
```

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://avatar.roblox.com/v1/game-start-info?universeId={VALUE}"
```

### POST `/v1/outfits/{userOutfitId}/delete`

Deletes the outfit.

You are only allowed to delete outfits you created.

**Server:** `https://avatar.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userOutfitId` | path | `integer` | Yes | The user outfit id. |
| `Roblox-Place-Id` | header | `integer` | No |  |

**Responses:**

- `200`: OK → `Roblox.Api.Avatar.Models.AvatarApiSuccessResponse`
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 2: You don't have permission to delete this outfit.
- `404`: 1: The specified userOutfitId is invalid!
- `500`: 3: An error occurred while deleting the outfit.

**Response fields** (`Roblox.Api.Avatar.Models.AvatarApiSuccessResponse`)

See [Roblox.Api.Avatar.Models.AvatarApiSuccessResponse](#roblox-api-avatar-models-avatarapisuccessresponse) in Models.

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
  "https://avatar.roblox.com/v1/outfits/{USEROUTFITID}/delete"
```

### GET `/v1/outfits/{userOutfitId}/details` *(deprecated)*

Gets details about the contents of an outfit.

Please use GET v4/outfits/{outfitId}/details

**Server:** `https://avatar.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userOutfitId` | path | `integer` | Yes | The user outfit id. |
| `Roblox-Place-Id` | header | `integer` | No |  |

**Responses:**

- `200`: OK → `Roblox.Api.Avatar.Models.OutfitDetailsModel`
- `400`: 2: The outfit for the specified userOutfit is invalid.
- `403`: 3: The requester does not have access to the details for the given user outfit.
- `404`: 1: The specified userOutfitId is invalid.

**Response fields** (`Roblox.Api.Avatar.Models.OutfitDetailsModel`)

See [Roblox.Api.Avatar.Models.OutfitDetailsModel](#roblox-api-avatar-models-outfitdetailsmodel) in Models.

**Response example:**
```json
{
  "id": 0,
  "universeId": 0,
  "name": "string",
  "assets": [
    {
      "id": "...",
      "name": "...",
      "assetType": "...",
      "currentVersionId": "...",
      "meta": "...",
      "availabilityStatus": "..."
    }
  ],
  "bodyColors": {
    "headColorId": 0,
    "torsoColorId": 0,
    "rightArmColorId": 0,
    "leftArmColorId": 0,
    "rightLegColorId": 0,
    "leftLegColorId": 0
  },
  "scale": {
    "height": 0,
    "width": 0,
    "head": 0,
    "depth": 0,
    "proportion": 0,
    "bodyType": 0
  }
}
```

**Error handling:** `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://avatar.roblox.com/v1/outfits/{USEROUTFITID}/details"
```

### GET `/v1/users/avatar` [STABLE]

Get Avatar Full body shots for the given CSV of userIds

**Server:** `https://thumbnails.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userIds` | query | `integer[]` | Yes | CSV for the userIds to get avatar full body shots |
| `includeBackground` | query | `boolean` | No | Whether to include a background in the thumbnail (defaults to false) |
| `size` | query | `string enum (14 values)` | No | The thumbnail size, formatted widthxheight Valid values: `30x30`, `48x48`, `60x60`, `75x75`, `100x100`, `110x110`, `140x140`, `150x150`, `150x200`, `180x180`, `250x250`, `352x352`, `420x420`, `720x720` |
| `format` | query | `Png \| Jpeg \| Webp` | No | The thumbnail format Valid values: `Png`, `Jpeg`, `Webp` |
| `isCircular` | query | `true \| false` | No | The circle thumbnail output parameter, true or false Valid values: `true`, `false` |

**Responses:**

- `200`: OK
- `400`: 1: There are too many requested Ids. 2: The requested image format is invalid. Please see documentation for valid thumbnail format parameter name and values. 3: The requested size is invalid. Please see documentation for valid thumbnail size parameter name and format. 4: The requested Ids are invalid, of an invalid type or missing. 10: Circular thumbnail requests are not allowed

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://thumbnails.roblox.com/v1/users/avatar?userIds={VALUE}"
```

### GET `/v1/users/avatar-3d` [BETA]

Get Avatar 3d object for a user

**Server:** `https://thumbnails.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`) or API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `thumbnail:read`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | query | `integer` | Yes | user Id for avatar |

**Responses:**

- `200`: OK
- `400`: 4: The requested Ids are invalid, of an invalid type or missing.

**Rate Limits:** perApiKeyOwner: 500/minute, perOauth2Authorization: 500/minute

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://thumbnails.roblox.com/v1/users/avatar-3d?userId={VALUE}"
```

### GET `/v1/users/avatar-bust` [STABLE]

Get Avatar Busts for the given CSV of userIds

**Server:** `https://thumbnails.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userIds` | query | `integer[]` | Yes | CSV for the userIds to get avatar headshots |
| `includeBackground` | query | `boolean` | No | Whether to include a background in the thumbnail (defaults to false) |
| `size` | query | `string enum (9 values)` | No | The thumbnail size, formatted widthxheight Valid values: `48x48`, `50x50`, `60x60`, `75x75`, `100x100`, `150x150`, `180x180`, `352x352`, `420x420` |
| `format` | query | `Png \| Webp` | No | The thumbnail format Valid values: `Png`, `Webp` |
| `isCircular` | query | `true \| false` | No | The circle thumbnail output parameter, true or false Valid values: `true`, `false` |

**Responses:**

- `200`: OK
- `400`: 1: There are too many requested Ids. 2: The requested image format is invalid. Please see documentation for valid thumbnail format parameter name and values. 3: The requested size is invalid. Please see documentation for valid thumbnail size parameter name and format. 4: The requested Ids are invalid, of an invalid type or missing. 10: Circular thumbnail requests are not allowed

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://thumbnails.roblox.com/v1/users/avatar-bust?userIds={VALUE}"
```

### GET `/v1/users/avatar-headshot` [STABLE]

Get Avatar Headshots for the given CSV of userIds

**Server:** `https://thumbnails.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userIds` | query | `integer[]` | Yes | CSV for the userIds to get avatar headshots |
| `includeBackground` | query | `boolean` | No | Whether to include a background in the thumbnail (defaults to false) |
| `includeProfileFrame` | query | `boolean` | No | Whether to composite the user's equipped profile frame into the thumbnail (defaults to false) |
| `size` | query | `string enum (11 values)` | No | The thumbnail size, formatted widthxheight Valid values: `48x48`, `50x50`, `60x60`, `75x75`, `100x100`, `110x110`, `150x150`, `180x180`, `352x352`, `420x420`, `720x720` |
| `format` | query | `Png \| Jpeg \| Webp` | No | The thumbnail format Valid values: `Png`, `Jpeg`, `Webp` |
| `isCircular` | query | `true \| false` | No | The circle thumbnail output parameter, true or false Valid values: `true`, `false` |

**Responses:**

- `200`: OK
- `400`: 1: There are too many requested Ids. 2: The requested image format is invalid. Please see documentation for valid thumbnail format parameter name and values. 3: The requested size is invalid. Please see documentation for valid thumbnail size parameter name and format. 4: The requested Ids are invalid, of an invalid type or missing. 10: Circular thumbnail requests are not allowed

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://thumbnails.roblox.com/v1/users/avatar-headshot?userIds={VALUE}"
```

### GET `/v1/users/{userId}/avatar` *(deprecated)*

Returns details about a specified user's avatar.

Includes assets, bodycolors, and playerAvatarType.

Please use GET v4/avatar/users/{userId}

**Server:** `https://avatar.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer` | Yes |  |
| `Roblox-Place-Id` | header | `integer` | No |  |

**Responses:**

- `200`: OK → `Roblox.Api.Avatar.Models.AvatarModelV2`
- `400`: 1: The specified user does not exist. 2: An account for the given userId does not exist!

**Response fields** (`Roblox.Api.Avatar.Models.AvatarModelV2`)

See [Roblox.Api.Avatar.Models.AvatarModelV2](#roblox-api-avatar-models-avatarmodelv2) in Models.

**Response example:**
```json
{
  "scales": {
    "height": 0,
    "width": 0,
    "head": 0,
    "depth": 0,
    "proportion": 0,
    "bodyType": 0
  },
  "playerAvatarType": 1,
  "bodyColors": {
    "headColorId": 0,
    "torsoColorId": 0,
    "rightArmColorId": 0,
    "leftArmColorId": 0,
    "rightLegColorId": 0,
    "leftLegColorId": 0
  },
  "assets": [
    {
      "id": "...",
      "name": "...",
      "assetType": "...",
      "currentVersionId": "...",
      "meta": "...",
      "availabilityStatus": "..."
    }
  ],
  "defaultShirtApplied": false,
  "defaultPantsApplied": false
}
```

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://avatar.roblox.com/v1/users/{USERID}/avatar"
```

### GET `/v1/users/{userId}/outfits` *(deprecated)*

Deprecated, user v2.
Gets a list of outfits for the specified user.

Please use GET v2/avatar/users/{userId}/outfits

**Server:** `https://avatar.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer` | Yes | The user id. |
| `outfitType` | query | `string` | No | The outfit type being searched for, null will return all outfitTypes. |
| `page` | query | `integer` | No | The page number of the current page of requests, default is 1. |
| `itemsPerPage` | query | `integer` | No | The max number of outfits that can be returned. |
| `isEditable` | query | `boolean` | No | Whether the outfits are editable. A null value will lead to no filtering. |
| `Roblox-Place-Id` | header | `integer` | No | The placeId of the caller, not required to be passed in. |

**Responses:**

- `200`: OK → `Roblox.Api.Avatar.Models.AvatarFilteredPageResponse_Roblox.Api.Avatar.Models.OutfitModel_`
- `400`: 1: The specified user does not exist. 2: An account for the given userId does not exist!

**Response fields** (`Roblox.Api.Avatar.Models.AvatarFilteredPageResponse_Roblox.Api.Avatar.Models.OutfitModel_`)

See [Roblox.Api.Avatar.Models.AvatarFilteredPageResponse_Roblox.Api.Avatar.Models.OutfitModel_](#roblox-api-avatar-models-avatarfilteredpageresponse-roblox-api-avatar-models-outfitmodel-) in Models.

**Response example:**
```json
{
  "filteredCount": 0,
  "data": [
    {
      "id": "...",
      "name": "...",
      "isEditable": "...",
      "outfitType": "..."
    }
  ],
  "total": 0
}
```

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://avatar.roblox.com/v1/users/{USERID}/outfits"
```

### PATCH `/v2/avatar` *(deprecated)*

Sets the avatar to the incoming avatar using field masks.

Only allows items that you own, are not expired, and are wearable asset types.
Any assets being worn before this method is called are automatically removed.

Please use PATCH v4/avatar

**Server:** `https://avatar.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `Roblox-Place-Id` | header | `integer` | No |  |

**Request Body:** `application/json` — Type: `Roblox.Api.Avatar.Models.UpdateAvatarRequestModel`

See [Roblox.Api.Avatar.Models.UpdateAvatarRequestModel](#roblox-api-avatar-models-updateavatarrequestmodel) in Models.

**Request example:**
```json
{
  "updateMask": [
    0
  ],
  "data": {
    "scales": {
      "height": "...",
      "width": "...",
      "head": "...",
      "depth": "...",
      "proportion": "...",
      "bodyType": "..."
    },
    "playerAvatarType": 1,
    "bodyColors": {
      "headColor3": "...",
      "torsoColor3": "...",
      "rightArmColor3": "...",
      "leftArmColor3": "...",
      "rightLegColor3": "...",
      "leftLegColor3": "..."
    },
    "assets": [
      "..."
    ]
  }
}
```

**Responses:**

- `200`: OK → `Roblox.Api.Avatar.Models.UpdateAvatarResponseModel`
- `400`: 3: Invalid assetId 5: Meta does not apply to specified asset type 7: Required meta is not provided for the specific asset type
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed
- `500`: 2: Failed to wear asset.

**Response fields** (`Roblox.Api.Avatar.Models.UpdateAvatarResponseModel`)

See [Roblox.Api.Avatar.Models.UpdateAvatarResponseModel](#roblox-api-avatar-models-updateavatarresponsemodel) in Models.

**Response example:**
```json
{
  "invalidAssets": [
    {
      "id": "...",
      "name": "...",
      "assetType": "...",
      "currentVersionId": "...",
      "meta": "...",
      "availabilityStatus": "..."
    }
  ],
  "success": false
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X PATCH -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://avatar.roblox.com/v2/avatar" \
  -H "Content-Type: application/json" \
  -d '{"updateMask":[0],"data":{"scales":{"height":"...","width":"...","head":"...","depth":"...","proportion":"...","bodyType":"..."},"playerAvatarType":1,"bodyColors":{"headColor3":"...","torsoColor3":"...","rightArmColor3":"...","leftArmColor3":"...","rightLegColor3":"...","leftLegColor3":"..."},"assets":["..."]}}'
```

### GET `/v2/avatar/avatar` *(deprecated)*

Returns details about the authenticated user's avatar.

Please use GET v4/avatar

**Server:** `https://avatar.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `Roblox-Place-Id` | header | `integer` | No |  |
| `checkAssetAvailability` | query | `boolean` | No | Whether to return assets with availability status. |

**Responses:**

- `200`: OK → `Roblox.Api.Avatar.Models.AvatarModelV3`
- `401`: 0: Authorization has been denied for this request.

**Response fields** (`Roblox.Api.Avatar.Models.AvatarModelV3`)

See [Roblox.Api.Avatar.Models.AvatarModelV3](#roblox-api-avatar-models-avatarmodelv3) in Models.

**Response example:**
```json
{
  "scales": {
    "height": 0,
    "width": 0,
    "head": 0,
    "depth": 0,
    "proportion": 0,
    "bodyType": 0
  },
  "playerAvatarType": 1,
  "bodyColor3s": {
    "headColor3": "string",
    "torsoColor3": "string",
    "rightArmColor3": "string",
    "leftArmColor3": "string",
    "rightLegColor3": "string",
    "leftLegColor3": "string"
  },
  "assets": [
    {
      "id": "...",
      "name": "...",
      "assetType": "...",
      "currentVersionId": "...",
      "meta": "...",
      "availabilityStatus": "..."
    }
  ],
  "defaultShirtApplied": false,
  "defaultPantsApplied": false
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://avatar.roblox.com/v2/avatar/avatar"
```

### POST `/v2/avatar/set-body-colors` *(deprecated)*

Sets the authenticated user's body colors.

Please use PATCH v4/avatar

**Server:** `https://avatar.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `Roblox-Place-Id` | header | `integer` | No |  |

**Request Body:** `application/json` — Type: `Roblox.Platform.Avatar.BodyColorsModelV2`

See [Roblox.Platform.Avatar.BodyColorsModelV2](#roblox-platform-avatar-bodycolorsmodelv2) in Models.

**Request example:**
```json
{
  "headColor3": "string",
  "torsoColor3": "string",
  "rightArmColor3": "string",
  "leftArmColor3": "string",
  "rightLegColor3": "string",
  "leftLegColor3": "string"
}
```

**Responses:**

- `200`: OK → `Roblox.Api.Avatar.Models.AvatarApiSuccessResponse`
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed

**Response fields** (`Roblox.Api.Avatar.Models.AvatarApiSuccessResponse`)

See [Roblox.Api.Avatar.Models.AvatarApiSuccessResponse](#roblox-api-avatar-models-avatarapisuccessresponse) in Models.

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
  "https://avatar.roblox.com/v2/avatar/set-body-colors" \
  -H "Content-Type: application/json" \
  -d '{
  "headColor3": "string",
  "torsoColor3": "string",
  "rightArmColor3": "string",
  "leftArmColor3": "string",
  "rightLegColor3": "string",
  "leftLegColor3": "string"
}'
```

### POST `/v2/avatar/set-wearing-assets` *(deprecated)*

Sets the avatar's current assets to the list.

Only allows items that you own, are not expired, and are wearable asset types.
Any assets being worn before this method is called are automatically removed.

Please use PATCH v4/avatar

**Server:** `https://avatar.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `Roblox-Place-Id` | header | `integer` | No |  |

**Request Body:** `application/json` — Type: `Roblox.Api.Avatar.Models.WearRequestModel`

See [Roblox.Api.Avatar.Models.WearRequestModel](#roblox-api-avatar-models-wearrequestmodel) in Models.

**Request example:**
```json
{
  "assets": [
    {
      "id": "...",
      "meta": "..."
    }
  ]
}
```

**Responses:**

- `200`: OK → `Roblox.Api.Avatar.Models.WearResponseModel`
- `400`: 3: Invalid assetId 5: Meta does not apply to specified asset type 7: Required meta is not provided for the specific asset type
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed
- `500`: 2: Failed to wear asset.

**Response fields** (`Roblox.Api.Avatar.Models.WearResponseModel`)

See [Roblox.Api.Avatar.Models.WearResponseModel](#roblox-api-avatar-models-wearresponsemodel) in Models.

**Response example:**
```json
{
  "invalidAssets": [
    {
      "id": "...",
      "name": "...",
      "assetType": "...",
      "currentVersionId": "...",
      "meta": "...",
      "availabilityStatus": "..."
    }
  ],
  "invalidAssetIds": [
    0
  ],
  "success": false
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://avatar.roblox.com/v2/avatar/set-wearing-assets" \
  -H "Content-Type: application/json" \
  -d '{
  "assets": [
    {
      "id": "...",
      "meta": "..."
    }
  ]
}'
```

### GET `/v2/avatar/users/{userId}/avatar` *(deprecated)*

Returns details about a specified user's avatar.

Includes assets, bodycolors, and playerAvatarType.

Please use GET v4/avatar/users/{userId}

**Server:** `https://avatar.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer` | Yes |  |
| `Roblox-Place-Id` | header | `integer` | No |  |
| `checkAssetAvailability` | query | `boolean` | No | Whether to return assets with availability status. |

**Responses:**

- `200`: OK → `Roblox.Api.Avatar.Models.AvatarModelV3`
- `400`: 1: The specified user does not exist. 2: An account for the given userId does not exist!

**Response fields** (`Roblox.Api.Avatar.Models.AvatarModelV3`)

See [Roblox.Api.Avatar.Models.AvatarModelV3](#roblox-api-avatar-models-avatarmodelv3) in Models.

**Response example:**
```json
{
  "scales": {
    "height": 0,
    "width": 0,
    "head": 0,
    "depth": 0,
    "proportion": 0,
    "bodyType": 0
  },
  "playerAvatarType": 1,
  "bodyColor3s": {
    "headColor3": "string",
    "torsoColor3": "string",
    "rightArmColor3": "string",
    "leftArmColor3": "string",
    "rightLegColor3": "string",
    "leftLegColor3": "string"
  },
  "assets": [
    {
      "id": "...",
      "name": "...",
      "assetType": "...",
      "currentVersionId": "...",
      "meta": "...",
      "availabilityStatus": "..."
    }
  ],
  "defaultShirtApplied": false,
  "defaultPantsApplied": false
}
```

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://avatar.roblox.com/v2/avatar/users/{USERID}/avatar"
```

### GET `/v2/avatar/users/{userId}/outfits`

Gets a list of outfits for the specified user.

**Server:** `https://avatar.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer` | Yes | The user id. |
| `paginationToken` | query | `string` | No | The token received from the response to get the next page. For the first request, this value should be empty. Note : If no value is sent the 1st page will be returned. |
| `outfitType` | query | `string` | No | The outfit type being searched for, null will return all outfitTypes. |
| `page` | query | `integer` | No | The page number of the current page of requests, default is 1. |
| `itemsPerPage` | query | `integer` | No | The max number of outfits that can be returned. |
| `isEditable` | query | `boolean` | No | Whether the outfits are editable. A null value will lead to no filtering. |
| `Roblox-Place-Id` | header | `integer` | No | The placeId of the caller, not required to be passed in. |

**Responses:**

- `200`: OK → `Roblox.Api.Avatar.Models.AvatarPageResponse_Roblox.Api.Avatar.Models.OutfitModel_`
- `400`: 1: The specified user does not exist. 2: An account for the given userId does not exist!

**Response fields** (`Roblox.Api.Avatar.Models.AvatarPageResponse_Roblox.Api.Avatar.Models.OutfitModel_`)

See [Roblox.Api.Avatar.Models.AvatarPageResponse_Roblox.Api.Avatar.Models.OutfitModel_](#roblox-api-avatar-models-avatarpageresponse-roblox-api-avatar-models-outfitmodel-) in Models.

**Response example:**
```json
{
  "data": [
    {
      "id": "...",
      "name": "...",
      "isEditable": "...",
      "outfitType": "..."
    }
  ],
  "paginationToken": "string"
}
```

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://avatar.roblox.com/v2/avatar/users/{USERID}/outfits"
```

### POST `/v2/outfits/create` *(deprecated)*

Creates a new outfit.

Fails if any of the assetIds are not owned by the user, or not wearable types.
The name property of the request is optional as one will be auto-generated when the request has a null name.

Please use POST v4/outfits/create

**Server:** `https://avatar.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `Roblox-Place-Id` | header | `integer` | No |  |

**Request Body:** `application/json` — Type: `Roblox.Api.Avatar.Models.OutfitUpdateModelV2`

See [Roblox.Api.Avatar.Models.OutfitUpdateModelV2](#roblox-api-avatar-models-outfitupdatemodelv2) in Models.

**Request example:**
```json
{
  "name": "string",
  "bodyColors": {
    "headColorId": 0,
    "torsoColorId": 0,
    "rightArmColorId": 0,
    "leftArmColorId": 0,
    "rightLegColorId": 0,
    "leftLegColorId": 0
  },
  "assets": [
    {
      "id": "...",
      "meta": "..."
    }
  ],
  "scale": {
    "height": 0,
    "width": 0,
    "head": 0,
    "depth": 0,
    "proportion": 0,
    "bodyType": 0
  },
  "playerAvatarType": "string",
  "outfitType": 0
}
```

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: 3: Body colors must be valid BrickColor IDs 4: Invalid outfit name 5: Asset is not wearable by you and was not added to the outfit 7: Invalid Player Avatar Type. Valid types are R6 and R15 8: Invalid assetIds 9: Meta does not apply to specified asset type 10: Required meta is not provided for the specific asset type 12: Outfit type invalid or not permitted 13: Invalid Scale
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 1: You already have the maximum number of outfits
- `500`: 6: An error occurred while creating the outfit

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://avatar.roblox.com/v2/outfits/create" \
  -H "Content-Type: application/json" \
  -d '{"name":"string","bodyColors":{"headColorId":0,"torsoColorId":0,"rightArmColorId":0,"leftArmColorId":0,"rightLegColorId":0,"leftLegColorId":0},"assets":[{"id":"...","meta":"..."}],"scale":{"height":0,"width":0,"head":0,"depth":0,"proportion":0,"bodyType":0},"playerAvatarType":"string","outfitType":0}'
```

### PATCH `/v2/outfits/{userOutfitId}` *(deprecated)*

Updates the contents of an outfit.

Fails if the user does not own any of the assetIds or if they are not wearable asset types.
Accepts partial updates.

Please use PATCH v4/outfits/{outfitId}

**Server:** `https://avatar.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userOutfitId` | path | `integer` | Yes | The user outfit id. |
| `Roblox-Place-Id` | header | `integer` | No |  |

**Request Body:** `application/json` — Type: `Roblox.Api.Avatar.Models.OutfitUpdateModelV2`

See [Roblox.Api.Avatar.Models.OutfitUpdateModelV2](#roblox-api-avatar-models-outfitupdatemodelv2) in Models.

**Request example:**
```json
{
  "name": "string",
  "bodyColors": {
    "headColorId": 0,
    "torsoColorId": 0,
    "rightArmColorId": 0,
    "leftArmColorId": 0,
    "rightLegColorId": 0,
    "leftLegColorId": 0
  },
  "assets": [
    {
      "id": "...",
      "meta": "..."
    }
  ],
  "scale": {
    "height": 0,
    "width": 0,
    "head": 0,
    "depth": 0,
    "proportion": 0,
    "bodyType": 0
  },
  "playerAvatarType": "string",
  "outfitType": 0
}
```

**Responses:**

- `200`: OK → `Roblox.Api.Avatar.Models.OutfitModel`
- `400`: 3: Body colors must be valid BrickColor IDs 4: Invalid outfit name 5: Asset is not wearable by you 8: Invalid Player Avatar Type. Valid types are R6 and R15 11: Meta does not apply to specified asset type 12: Meta is required for this specific asset type 13: Invalid Outfit Type 14: Invalid scale
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 2: You don't have permission to update this outfit.
- `404`: 1: The specified userOutfit does not exist!
- `500`: 6: An error occurred while trying to update the outfit

**Response fields** (`Roblox.Api.Avatar.Models.OutfitModel`)

See [Roblox.Api.Avatar.Models.OutfitModel](#roblox-api-avatar-models-outfitmodel) in Models.

**Response example:**
```json
{
  "id": 0,
  "name": "string",
  "isEditable": false,
  "outfitType": "string"
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X PATCH -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://avatar.roblox.com/v2/outfits/{USEROUTFITID}" \
  -H "Content-Type: application/json" \
  -d '{"name":"string","bodyColors":{"headColorId":0,"torsoColorId":0,"rightArmColorId":0,"leftArmColorId":0,"rightLegColorId":0,"leftLegColorId":0},"assets":[{"id":"...","meta":"..."}],"scale":{"height":0,"width":0,"head":0,"depth":0,"proportion":0,"bodyType":0},"playerAvatarType":"string","outfitType":0}'
```

### POST `/v3/outfits/create` *(deprecated)*

Creates a new outfit.

Fails if any of the assetIds are not owned by the user, or not wearable types.
The name property of the request is optional as one will be auto-generated when the request has a null name.

Please use POST v4/outfits/create

**Server:** `https://avatar.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `Roblox-Place-Id` | header | `integer` | No |  |

**Request Body:** `application/json` — Type: `Roblox.Api.Avatar.Models.OutfitUpdateModelV3`

See [Roblox.Api.Avatar.Models.OutfitUpdateModelV3](#roblox-api-avatar-models-outfitupdatemodelv3) in Models.

**Request example:**
```json
{
  "name": "string",
  "bodyColor3s": {
    "headColor3": "string",
    "torsoColor3": "string",
    "rightArmColor3": "string",
    "leftArmColor3": "string",
    "rightLegColor3": "string",
    "leftLegColor3": "string"
  },
  "assets": [
    {
      "id": "...",
      "meta": "..."
    }
  ],
  "scale": {
    "height": 0,
    "width": 0,
    "head": 0,
    "depth": 0,
    "proportion": 0,
    "bodyType": 0
  },
  "playerAvatarType": "string",
  "outfitType": 0
}
```

**Responses:**

- `200`: OK → `Roblox.Api.Avatar.Models.OutfitModel`
- `400`: 3: Body colors must be valid BrickColor IDs 4: Invalid outfit name 5: Asset is not wearable by you and was not added to the outfit 7: Invalid Player Avatar Type. Valid types are R6 and R15 8: Invalid assetIds 9: Meta does not apply to specified asset type 10: Required meta is not provided for the specific asset type 12: Outfit type invalid or not permitted 13: Invalid Scale
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 1: You already have the maximum number of outfits
- `500`: 6: An error occurred while creating the outfit

**Response fields** (`Roblox.Api.Avatar.Models.OutfitModel`)

See [Roblox.Api.Avatar.Models.OutfitModel](#roblox-api-avatar-models-outfitmodel) in Models.

**Response example:**
```json
{
  "id": 0,
  "name": "string",
  "isEditable": false,
  "outfitType": "string"
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://avatar.roblox.com/v3/outfits/create" \
  -H "Content-Type: application/json" \
  -d '{"name":"string","bodyColor3s":{"headColor3":"string","torsoColor3":"string","rightArmColor3":"string","leftArmColor3":"string","rightLegColor3":"string","leftLegColor3":"string"},"assets":[{"id":"...","meta":"..."}],"scale":{"height":0,"width":0,"head":0,"depth":0,"proportion":0,"bodyType":0},"playerAvatarType":"string","outfitType":0}'
```

### PATCH `/v3/outfits/{userOutfitId}` *(deprecated)*

Updates the contents of an outfit.

Fails if the user does not own any of the assetIds or if they are not wearable asset types.
Accepts partial updates.

Please use PATCH v4/outfits/{outfitId}

**Server:** `https://avatar.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userOutfitId` | path | `integer` | Yes | The user outfit id. |
| `Roblox-Place-Id` | header | `integer` | No |  |

**Request Body:** `application/json` — Type: `Roblox.Api.Avatar.Models.OutfitUpdateModelV3`

See [Roblox.Api.Avatar.Models.OutfitUpdateModelV3](#roblox-api-avatar-models-outfitupdatemodelv3) in Models.

**Request example:**
```json
{
  "name": "string",
  "bodyColor3s": {
    "headColor3": "string",
    "torsoColor3": "string",
    "rightArmColor3": "string",
    "leftArmColor3": "string",
    "rightLegColor3": "string",
    "leftLegColor3": "string"
  },
  "assets": [
    {
      "id": "...",
      "meta": "..."
    }
  ],
  "scale": {
    "height": 0,
    "width": 0,
    "head": 0,
    "depth": 0,
    "proportion": 0,
    "bodyType": 0
  },
  "playerAvatarType": "string",
  "outfitType": 0
}
```

**Responses:**

- `200`: OK → `Roblox.Api.Avatar.Models.OutfitModel`
- `400`: 3: Body colors must be valid BrickColor IDs 4: Invalid outfit name 5: Asset is not wearable by you 8: Invalid Player Avatar Type. Valid types are R6 and R15 11: Meta does not apply to specified asset type 12: Meta is required for this specific asset type 13: Invalid Outfit Type 14: Invalid scale
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 2: You don't have permission to update this outfit.
- `404`: 1: The specified userOutfit does not exist!
- `500`: 6: An error occurred while trying to update the outfit

**Response fields** (`Roblox.Api.Avatar.Models.OutfitModel`)

See [Roblox.Api.Avatar.Models.OutfitModel](#roblox-api-avatar-models-outfitmodel) in Models.

**Response example:**
```json
{
  "id": 0,
  "name": "string",
  "isEditable": false,
  "outfitType": "string"
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X PATCH -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://avatar.roblox.com/v3/outfits/{USEROUTFITID}" \
  -H "Content-Type: application/json" \
  -d '{"name":"string","bodyColor3s":{"headColor3":"string","torsoColor3":"string","rightArmColor3":"string","leftArmColor3":"string","rightLegColor3":"string","leftLegColor3":"string"},"assets":[{"id":"...","meta":"..."}],"scale":{"height":0,"width":0,"head":0,"depth":0,"proportion":0,"bodyType":0},"playerAvatarType":"string","outfitType":0}'
```

### GET `/v3/outfits/{userOutfitId}/details` *(deprecated)*

Gets details about the contents of an outfit.

Please use GET v4/outfits/{outfitId}/details

**Server:** `https://avatar.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userOutfitId` | path | `integer` | Yes | The user outfit id. |
| `Roblox-Place-Id` | header | `integer` | No |  |
| `checkAssetAvailability` | query | `boolean` | No | Whether to return assets with availability status. |

**Responses:**

- `200`: OK → `Roblox.Api.Avatar.Models.OutfitDetailsModelV2`
- `400`: 2: The outfit for the specified userOutfit is invalid.
- `403`: 3: The requester does not have access to the details for the given user outfit.
- `404`: 1: The specified userOutfitId is invalid.

**Response fields** (`Roblox.Api.Avatar.Models.OutfitDetailsModelV2`)

See [Roblox.Api.Avatar.Models.OutfitDetailsModelV2](#roblox-api-avatar-models-outfitdetailsmodelv2) in Models.

**Response example:**
```json
{
  "id": 0,
  "name": "string",
  "assets": [
    {
      "id": "...",
      "name": "...",
      "assetType": "...",
      "currentVersionId": "...",
      "meta": "...",
      "availabilityStatus": "..."
    }
  ],
  "bodyColor3s": {
    "headColor3": "string",
    "torsoColor3": "string",
    "rightArmColor3": "string",
    "leftArmColor3": "string",
    "rightLegColor3": "string",
    "leftLegColor3": "string"
  },
  "scale": {
    "height": 0,
    "width": 0,
    "head": 0,
    "depth": 0,
    "proportion": 0,
    "bodyType": 0
  },
  "playerAvatarType": "string"
}
```

**Error handling:** `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://avatar.roblox.com/v3/outfits/{USEROUTFITID}/details"
```

### GET `/v4/avatar`

Gets the currently wearing avatar definition for the authenticated user.

Returns an Roblox.Api.Avatar.Models.V4.AvatarDefinition containing an Roblox.Api.Avatar.Models.V4.AvatarModelV4 and Roblox.Api.Avatar.Models.V4.AvatarConfigurations.

**Server:** `https://avatar.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `selectionTypes` | query | `integer enum (7 values)[]` | Yes | Selection types for the avatar data to return. |
| `Roblox-Place-Id` | header | `integer` | No |  |

**Responses:**

- `200`: OK → `Roblox.Api.Avatar.Models.V4.AvatarDefinition`
- `401`: 0: Authorization has been denied for this request.

**Response fields** (`Roblox.Api.Avatar.Models.V4.AvatarDefinition`)

See [Roblox.Api.Avatar.Models.V4.AvatarDefinition](#roblox-api-avatar-models-v4-avatardefinition) in Models.

**Response example:**
```json
{
  "avatarModel": {
    "scales": {
      "height": "...",
      "width": "...",
      "head": "...",
      "depth": "...",
      "proportion": "...",
      "bodyType": "..."
    },
    "playerAvatarType": 1,
    "bodyColors": {
      "headColor": "...",
      "torsoColor": "...",
      "rightArmColor": "...",
      "leftArmColor": "...",
      "rightLegColor": "...",
      "leftLegColor": "..."
    },
    "assets": [
      "..."
    ]
  },
  "avatarConfigurations": {
    "emotes": [
      "..."
    ],
    "background": {
      "backgroundAsset": "..."
    },
    "thumbnailCustomizations": [
      "..."
    ],
    "profileFrame": {
      "frameAsset": "..."
    }
  }
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://avatar.roblox.com/v4/avatar?selectionTypes={VALUE}"
```

### PATCH `/v4/avatar`

Sets the avatar to the incoming avatar using field masks.

Only allows items that you own, are not expired, and are wearable asset types.
Any assets being worn before this method is called are automatically removed.

**Server:** `https://avatar.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `Roblox-Place-Id` | header | `integer` | No |  |

**Request Body:** `application/json` — Type: `Roblox.Api.Avatar.Models.V4.Request.UpdateAvatarDefinitionRequestV4`

See [Roblox.Api.Avatar.Models.V4.Request.UpdateAvatarDefinitionRequestV4](#roblox-api-avatar-models-v4-request-updateavatardefinitionrequestv4) in Models.

**Request example:**
```json
{
  "updateTypes": [
    0
  ],
  "avatarDefinition": {
    "updateAvatarModel": {
      "scales": "...",
      "playerAvatarType": "...",
      "bodyColors": "...",
      "assets": "..."
    },
    "updateAvatarConfig": {
      "emoteRequestModels": "...",
      "thumbnailCustomizationModels": "...",
      "backgroundRequestModel": "...",
      "profileFrameRequestModel": "..."
    }
  }
}
```

**Responses:**

- `200`: OK → `Roblox.Api.Avatar.Models.V4.Response.UpdateAvatarDefinitionResponseV4`
- `400`: 3: Invalid assetId 5: Meta does not apply to specified asset type 7: Required meta is not provided for the specific asset type
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed
- `500`: 2: Failed to wear asset.

**Response fields** (`Roblox.Api.Avatar.Models.V4.Response.UpdateAvatarDefinitionResponseV4`)

See [Roblox.Api.Avatar.Models.V4.Response.UpdateAvatarDefinitionResponseV4](#roblox-api-avatar-models-v4-response-updateavatardefinitionresponsev4) in Models.

**Response example:**
```json
{
  "success": false,
  "invalidAssets": [
    {
      "id": "...",
      "name": "...",
      "assetType": "...",
      "currentVersionId": "...",
      "meta": "...",
      "availabilityStatus": "..."
    }
  ],
  "validation": {
    "invalidAssets": [
      "..."
    ],
    "invalidBackground": [
      "..."
    ],
    "invalidProfileFrame": [
      "..."
    ],
    "invalidEmotes": [
      "..."
    ],
    "invalidThumbnailCustomizations": [
      "..."
    ]
  }
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X PATCH -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://avatar.roblox.com/v4/avatar" \
  -H "Content-Type: application/json" \
  -d '{"updateTypes":[0],"avatarDefinition":{"updateAvatarModel":{"scales":"...","playerAvatarType":"...","bodyColors":"...","assets":"..."},"updateAvatarConfig":{"emoteRequestModels":"...","thumbnailCustomizationModels":"...","backgroundRequestModel":"...","profileFrameRequestModel":"..."}}}'
```

### GET `/v4/avatar/users/{userId}`

Gets the currently wearing avatar definition for the specified user.

Returns an Roblox.Api.Avatar.Models.V4.AvatarDefinition containing an Roblox.Api.Avatar.Models.V4.AvatarModelV4 and Roblox.Api.Avatar.Models.V4.AvatarConfigurations.
Behavior is aligned with the V2 `GET v2/avatar/users/{userId}/avatar` endpoint.

**Server:** `https://avatar.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer` | Yes | The target user id. |
| `selectionTypes` | query | `integer enum (7 values)[]` | Yes | Selection types for the avatar data to return. |
| `Roblox-Place-Id` | header | `integer` | No |  |

**Responses:**

- `200`: OK → `Roblox.Api.Avatar.Models.V4.AvatarDefinition`
- `400`: 1: The specified user does not exist. 2: An account for the given userId does not exist!

**Response fields** (`Roblox.Api.Avatar.Models.V4.AvatarDefinition`)

See [Roblox.Api.Avatar.Models.V4.AvatarDefinition](#roblox-api-avatar-models-v4-avatardefinition) in Models.

**Response example:**
```json
{
  "avatarModel": {
    "scales": {
      "height": "...",
      "width": "...",
      "head": "...",
      "depth": "...",
      "proportion": "...",
      "bodyType": "..."
    },
    "playerAvatarType": 1,
    "bodyColors": {
      "headColor": "...",
      "torsoColor": "...",
      "rightArmColor": "...",
      "leftArmColor": "...",
      "rightLegColor": "...",
      "leftLegColor": "..."
    },
    "assets": [
      "..."
    ]
  },
  "avatarConfigurations": {
    "emotes": [
      "..."
    ],
    "background": {
      "backgroundAsset": "..."
    },
    "thumbnailCustomizations": [
      "..."
    ],
    "profileFrame": {
      "frameAsset": "..."
    }
  }
}
```

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://avatar.roblox.com/v4/avatar/users/{USERID}?selectionTypes={VALUE}"
```

### POST `/v4/outfits/create`

Creates a new outfit.

Fails if any of the assetIds are not owned by the user, or not wearable types.
The name property of the request is optional as one will be auto-generated when the request has a null name.

**Server:** `https://avatar.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `Roblox-Place-Id` | header | `integer` | No |  |

**Request Body:** `application/json` — Type: `Roblox.Api.Avatar.Models.V4.Request.CreateOutfitDefinitionRequestV4`

See [Roblox.Api.Avatar.Models.V4.Request.CreateOutfitDefinitionRequestV4](#roblox-api-avatar-models-v4-request-createoutfitdefinitionrequestv4) in Models.

**Request example:**
```json
{
  "outfitDefinition": {
    "updateOutfitModel": {
      "name": "...",
      "bodyColors": "...",
      "assets": "...",
      "scale": "...",
      "playerAvatarType": "...",
      "outfitType": "..."
    },
    "updateOutfitConfig": {
      "backgroundRequestModel": "..."
    }
  }
}
```

**Responses:**

- `200`: OK → `Roblox.Api.Avatar.Models.V4.Response.CreateOutfitDefinitionResponseV4`
- `400`: 3: Body colors must be valid BrickColor IDs 4: Invalid outfit name 5: Asset is not wearable by you and was not added to the outfit 7: Invalid Player Avatar Type. Valid types are R6 and R15 8: Invalid assetIds 9: Meta does not apply to specified asset type 10: Required meta is not provided for the specific asset type 12: Outfit type invalid or not permitted 13: Invalid Scale
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 1: You already have the maximum number of outfits
- `500`: 6: An error occurred while creating the outfit

**Response fields** (`Roblox.Api.Avatar.Models.V4.Response.CreateOutfitDefinitionResponseV4`)

See [Roblox.Api.Avatar.Models.V4.Response.CreateOutfitDefinitionResponseV4](#roblox-api-avatar-models-v4-response-createoutfitdefinitionresponsev4) in Models.

**Response example:**
```json
{
  "success": false,
  "validation": {
    "unwornAssets": [
      "..."
    ],
    "invalidBackground": [
      "..."
    ]
  }
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://avatar.roblox.com/v4/outfits/create" \
  -H "Content-Type: application/json" \
  -d '{
  "outfitDefinition": {
    "updateOutfitModel": {
      "name": "...",
      "bodyColors": "...",
      "assets": "...",
      "scale": "...",
      "playerAvatarType": "...",
      "outfitType": "..."
    },
    "updateOutfitConfig": {
      "backgroundRequestModel": "..."
    }
  }
}'
```

### PATCH `/v4/outfits/{outfitId}`

Updates the contents of an outfit.

Fails if the user does not own any of the assetIds or if they are not wearable asset types.
Accepts partial updates via update types.

**Server:** `https://avatar.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `outfitId` | path | `string` | Yes | The user outfit id. |
| `Roblox-Place-Id` | header | `integer` | No |  |

**Request Body:** `application/json` — Type: `Roblox.Api.Avatar.Models.V4.Request.UpdateOutfitDefinitionRequestV4`

See [Roblox.Api.Avatar.Models.V4.Request.UpdateOutfitDefinitionRequestV4](#roblox-api-avatar-models-v4-request-updateoutfitdefinitionrequestv4) in Models.

**Request example:**
```json
{
  "updateTypes": [
    0
  ],
  "outfitDefinition": {
    "updateOutfitModel": {
      "name": "...",
      "bodyColors": "...",
      "assets": "...",
      "scale": "...",
      "playerAvatarType": "...",
      "outfitType": "..."
    },
    "updateOutfitConfig": {
      "backgroundRequestModel": "..."
    }
  }
}
```

**Responses:**

- `200`: OK → `Roblox.Api.Avatar.Models.V4.Response.UpdateOutfitDefinitionResponseV4`
- `400`: 3: Body colors must be valid BrickColor IDs 4: Invalid outfit name 5: Asset is not wearable by you 8: Invalid Player Avatar Type. Valid types are R6 and R15 11: Meta does not apply to specified asset type 12: Meta is required for this specific asset type 13: Invalid Outfit Type 14: Invalid scale
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 2: You don't have permission to update this outfit.
- `404`: 1: The specified userOutfit does not exist!
- `500`: 6: An error occurred while trying to update the outfit

**Response fields** (`Roblox.Api.Avatar.Models.V4.Response.UpdateOutfitDefinitionResponseV4`)

See [Roblox.Api.Avatar.Models.V4.Response.UpdateOutfitDefinitionResponseV4](#roblox-api-avatar-models-v4-response-updateoutfitdefinitionresponsev4) in Models.

**Response example:**
```json
{
  "success": false,
  "validation": {
    "unwornAssets": [
      "..."
    ],
    "invalidBackground": [
      "..."
    ]
  }
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X PATCH -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://avatar.roblox.com/v4/outfits/{OUTFITID}" \
  -H "Content-Type: application/json" \
  -d '{"updateTypes":[0],"outfitDefinition":{"updateOutfitModel":{"name":"...","bodyColors":"...","assets":"...","scale":"...","playerAvatarType":"...","outfitType":"..."},"updateOutfitConfig":{"backgroundRequestModel":"..."}}}'
```

### GET `/v4/outfits/{outfitId}/details`

Gets the definition for an outfit.

Returns an Roblox.Api.Avatar.Models.V4.OutfitDefinition containing an Roblox.Api.Avatar.Models.V4.OutfitModelV4 and background Roblox.Api.Avatar.Models.V4.OutfitConfigurations.
Behavior is aligned with the V1/V3 `GET v{1|3}/outfits/{userOutfitId}/details` endpoints (authentication optional).

**Server:** `https://avatar.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `outfitId` | path | `string` | Yes | The outfit id. |
| `selectionTypes` | query | `0 \| 1[]` | No | Selection types for the outfit data to return. |
| `checkAssetAvailability` | query | `boolean` | No | Whether to return assets with availability status. |
| `Roblox-Place-Id` | header | `integer` | No |  |

**Responses:**

- `200`: OK → `Roblox.Api.Avatar.Models.V4.OutfitDefinition`
- `400`: 2: The outfit for the specified userOutfit is invalid.
- `403`: 3: The requester does not have access to the details for the given user outfit.
- `404`: 1: The specified userOutfitId is invalid.

**Response fields** (`Roblox.Api.Avatar.Models.V4.OutfitDefinition`)

See [Roblox.Api.Avatar.Models.V4.OutfitDefinition](#roblox-api-avatar-models-v4-outfitdefinition) in Models.

**Response example:**
```json
{
  "moderationStatus": "string",
  "bundleId": 0,
  "outfitModel": {
    "universeId": 0,
    "inventoryType": "string",
    "id": "string",
    "name": "string",
    "isEditable": false,
    "outfitType": 0
  },
  "outfitConfigurations": {
    "background": {
      "backgroundAsset": "..."
    }
  }
}
```

**Error handling:** `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://avatar.roblox.com/v4/outfits/{OUTFITID}/details"
```

## Models

### OpenCloudUsers.Operation

This resource represents a long-running operation that is the result of a
network API call.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `path` | `string` | No | The server-assigned path, which is only unique within the same service that originally returns it. If you use the default HTTP mapping, the `path` should be a resource path ending with `operations/{unique_id}`. |
| `metadata` | `any` | No | Service-specific metadata associated with the operation.  It typically contains progress information and common metadata such as create time. Some services might not provide such metadata.  Any method that returns a long-running operation should document the metadata type, if any. |
| `done` | `boolean` | No | If the value is `false`, it means the operation is still in progress. If `true`, the operation is completed, and either `error` or `response` is available. |
| `error` | `any` | No | The error result of the operation in case of failure or cancellation. |
| `response` | `any` | No | The normal response of the operation in case of success.  If the original method returns no data on success, such as `Delete`, the response is `google.protobuf.Empty`.  If the original method is standard `Get`/`Create`/`Update`, the response should be the resource.  For other methods, the response should have the type `XxxResponse`, where `Xxx` is the original method name.  For example, if the original method name is `TakeSnapshot()`, the inferred response type is `TakeSnapshotResponse`. |

### Roblox.Api.Avatar.Models.AvatarModelV2

A model containing details about an avatar

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `scales` | `Roblox.Web.Responses.Avatar.ScaleModel` | No |  |
| `playerAvatarType` | `1 \| 3` | No | The avatar type |
| `bodyColors` | `Roblox.Api.Avatar.Models.BodyColorsModel` | No |  |
| `assets` | `Roblox.Api.Avatar.Models.AssetModelV2[]` | No | The assets worn on the character |
| `defaultShirtApplied` | `boolean` | No | Whether default clothing has been applied to this avatar. |
| `defaultPantsApplied` | `boolean` | No | Whether default clothing has been applied to this avatar. |
| `emotes` | `Roblox.Api.Avatar.Models.EmoteResponseModel[]` | No | The emotes on the character |

### Roblox.Api.Avatar.Models.AvatarRulesModel

A model containing details about avatar-related business rules

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `playerAvatarTypes` | `1 \| 3[]` | No | The avatar type |
| `scales` | `object` | No | The scales |
| `wearableAssetTypes` | `Roblox.Api.Avatar.Models.AssetTypeRulesModel[]` | No | The assets worn on the character |
| `accessoryRefinementTypes` | `integer[]` | No | The list of asset type ids for Accessory Refinement. |
| `accessoryRefinementLowerBounds` | `object` | No | The lower bounds for accessory refinement settings. |
| `accessoryRefinementUpperBounds` | `object` | No | The lower bounds for accessory refinement settings. |
| `bodyColorsPalette` | `Roblox.Api.Avatar.Models.BodyColorModel[]` | No | The full set of usable body colors |
| `basicBodyColorsPalette` | `Roblox.Api.Avatar.Models.BodyColorModel[]` | No | The basic set of body colors |
| `minimumDeltaEBodyColorDifference` | `number` | No | The minimum Delta-E difference in body colors for default clothing not to be applied |
| `proportionsAndBodyTypeEnabledForUser` | `boolean` | No | Whether proportion and bodyType scales are allowed to be set by the authenticated user |
| `defaultClothingAssetLists` | `Roblox.Api.Avatar.Models.DefaultClothingAssets` | No |  |
| `bundlesEnabledForUser` | `boolean` | No | Whether or not bundles are enabled for the specific user |
| `emotesEnabledForUser` | `boolean` | No | Whether or not emotes are enabled |

### Roblox.Api.Avatar.Models.AvatarMetadataModel

A model containing website metadata for avatars

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `enableDefaultClothingMessage` | `boolean` | No | Whether or not to show the Default Clothing message |
| `isAvatarScaleEmbeddedInTab` | `boolean` | No | Whether or not the Scales is embedded in the tab |
| `isBodyTypeScaleOutOfTab` | `boolean` | No | Whether or not the Boby Type scale is embedded in the tab |
| `scaleHeightIncrement` | `number` | No | How much the height scaler should increment by |
| `scaleWidthIncrement` | `number` | No | How much the width scaler should increment by |
| `scaleHeadIncrement` | `number` | No | How much the head scaler should increment by |
| `scaleProportionIncrement` | `number` | No | How much the proportion scaler should increment by |
| `scaleBodyTypeIncrement` | `number` | No | How much the body type scaler should increment by |
| `supportProportionAndBodyType` | `boolean` | No | Whether or not to support proportion and body type |
| `showDefaultClothingMessageOnPageLoad` | `boolean` | No | Whether or not to show the default clothing message when the page loads |
| `areThreeDeeThumbsEnabled` | `boolean` | No | Whether or not 3D thumbnails are shown |
| `isAvatarWearingApiCallsLockingOnFrontendEnabled` | `boolean` | No | Does the frontend lock avatar editor input until the wearing call returns |
| `isOutfitHandlingOnFrontendEnabled` | `boolean` | No | Does the frontend lock avatar editor input until the wearing call returns |
| `isJustinUiChangesEnabled` | `boolean` | No | Determines whether a bunch of UI improvements are released |
| `isCategoryReorgEnabled` | `boolean` | No | Determines whether Category Reorg is released |
| `LCEnabledInEditorAndCatalog` | `boolean` | No | Flag for both web UI and App, name is fixed due to sharing, do not change |
| `isLCCompletelyEnabled` | `boolean` | No | Useful for the time between enabling Jackets for most users and all LC types for everyone, meanwhile Soothsayers need all types at all times |

### Roblox.Api.Avatar.Models.BodyColorsModel

A model container BrickColor ids for each body part.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `headColorId` | `integer` | No | The BrickColor id for head color |
| `torsoColorId` | `integer` | No | The BrickColor id for torso color |
| `rightArmColorId` | `integer` | No | The BrickColor id for right arm color |
| `leftArmColorId` | `integer` | No | The BrickColor id for left arm color |
| `rightLegColorId` | `integer` | No | The BrickColor id for right leg color |
| `leftLegColorId` | `integer` | No | The BrickColor id for left leg color |

### Roblox.Api.Avatar.Models.AvatarApiSuccessResponse

Success response class

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | `boolean` | No | Gets or sets a value indicating whether the request was a success. |

### Roblox.Api.Avatar.Models.PlayerAvatarTypeModel

A model that contains a playerAvatarType

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `playerAvatarType` | `1 \| 3` | No | The playerAvatarType |

### Roblox.Web.Responses.Avatar.ScaleModel

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `height` | `number` | No |  |
| `width` | `number` | No |  |
| `head` | `number` | No |  |
| `depth` | `number` | No |  |
| `proportion` | `number` | No |  |
| `bodyType` | `number` | No |  |

### Roblox.Api.Avatar.Models.GameStartInfoResponse

The game start info

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `gameAvatarType` | `string` | No | Avatar Type |
| `allowCustomAnimations` | `string` | No | Custom animation enabled |
| `universeAvatarCollisionType` | `string` | No | collision type for the univers |
| `universeAvatarBodyType` | `string` | No | Body type for the univers |
| `jointPositioningType` | `string` | No | Joing positioning type |
| `message` | `string` | No | Mesasge |
| `universeAvatarMinScales` | `Roblox.Web.Responses.Avatar.ScaleModel` | No |  |
| `universeAvatarMaxScales` | `Roblox.Web.Responses.Avatar.ScaleModel` | No |  |
| `universeAvatarAssetOverrides` | `Roblox.Api.Avatar.Models.UniverseAvatarAssetOverrideResponseModel[]` | No | asset overrides for the univers |
| `moderationStatus` | `string` | No | Moderation status |

### Roblox.Api.Avatar.Models.OutfitDetailsModel

A model containing details about a user outfit

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | `integer` | No | The id |
| `universeId` | `integer` | No | The universe id of the outfit, null when outfit is not created in-experience |
| `name` | `string` | No | The name |
| `assets` | `Roblox.Api.Avatar.Models.AssetModelV2[]` | No | A list of assetIds |
| `bodyColors` | `Roblox.Api.Avatar.Models.BodyColorsModel` | No |  |
| `scale` | `Roblox.Web.Responses.Avatar.ScaleModel` | No |  |
| `playerAvatarType` | `string` | No | The player avatar type - this can be R6 or R15. |
| `outfitType` | `string` | No | The outfit type of the outfit |
| `isEditable` | `boolean` | No | Whether the outfit can be edited by the user |
| `moderationStatus` | `string` | No | The moderation status of the outfit, not applicable when outfit is created outside experience |

### Roblox.Api.Avatar.Models.AvatarFilteredPageResponse_Roblox.Api.Avatar.Models.OutfitModel_

Filtered page response

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `filteredCount` | `integer` | No | Number of !:TPagedObject filtered. |
| `data` | `Roblox.Api.Avatar.Models.OutfitModel[]` | No |  |
| `total` | `integer` | No |  |

### Roblox.Api.Avatar.Models.UpdateAvatarRequestModel

A model containing details about an avatar update request.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `updateMask` | `integer enum (9 values)[]` | No | Update mask specifying which avatar fields to update (can include multiple). Acceptable values: - UpdateAvatarType: updates avatar.type (R6/R15) - UpdateScales: updates avatar.scale - UpdateBodyColors: updates avatar.body_color_set - UpdateAssets: updates avatar.avatar_assets |
| `data` | `Roblox.Api.Avatar.Models.UpdateAvatarDataModel` | No |  |

### Roblox.Api.Avatar.Models.UpdateAvatarResponseModel

A model for update avatar responses.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `invalidAssets` | `Roblox.Api.Avatar.Models.AssetModelV2[]` | No | The assets that could not be worn Unlike invalidAssetIds, only contains assets that are wearable types. |
| `success` | `boolean` | No | Whether or not all the outfit contents were successfully worn. |

### Roblox.Api.Avatar.Models.AvatarModelV3

A model containing details about an avatar

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `scales` | `Roblox.Web.Responses.Avatar.ScaleModel` | No |  |
| `playerAvatarType` | `1 \| 3` | No | The avatar type |
| `bodyColor3s` | `Roblox.Api.Avatar.Models.BodyColors3Model` | No |  |
| `assets` | `Roblox.Api.Avatar.Models.AssetModelV2[]` | No | The assets worn on the character |
| `defaultShirtApplied` | `boolean` | No | Whether default clothing has been applied to this avatar. |
| `defaultPantsApplied` | `boolean` | No | Whether default clothing has been applied to this avatar. |
| `emotes` | `Roblox.Api.Avatar.Models.EmoteResponseModel[]` | No | The emotes on the character |

### Roblox.Platform.Avatar.BodyColorsModelV2

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `headColor3` | `string` | No |  |
| `torsoColor3` | `string` | No |  |
| `rightArmColor3` | `string` | No |  |
| `leftArmColor3` | `string` | No |  |
| `rightLegColor3` | `string` | No |  |
| `leftLegColor3` | `string` | No |  |

### Roblox.Api.Avatar.Models.WearRequestModel

A model that contains a list of AssetWear models

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `assets` | `Roblox.Api.Avatar.Models.AssetWearModel[]` | No | The asset ids |

### Roblox.Api.Avatar.Models.WearResponseModel

A model for wear outfit responses

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `invalidAssets` | `Roblox.Api.Avatar.Models.AssetModelV2[]` | No | The assets that could not be worn Unlike invalidAssetIds, only contains assets that are wearable types |
| `invalidAssetIds` | `integer[]` | No | The asset ids that could not be worn |
| `success` | `boolean` | No | Whether or not all the outfit contents were successfully worn |

### Roblox.Api.Avatar.Models.AvatarPageResponse_Roblox.Api.Avatar.Models.OutfitModel_

Avatar page response.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | `Roblox.Api.Avatar.Models.OutfitModel[]` | No | The data |
| `paginationToken` | `string` | No | A non empty string indicates that there is more data available than this response contains. An empty string indicates the last page. |

### Roblox.Api.Avatar.Models.OutfitUpdateModelV2

A model containing details needed to update or create an outfit

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | `string` | No | The outfit name |
| `bodyColors` | `Roblox.Api.Avatar.Models.BodyColorsModel` | No |  |
| `assets` | `Roblox.Api.Avatar.Models.AssetWearModel[]` | No | Array of assets |
| `scale` | `Roblox.Web.Responses.Avatar.ScaleModel` | No |  |
| `playerAvatarType` | `string` | No | The avatar scale |
| `outfitType` | `integer enum (6 values)` | No | The type of outfit Values: 0, 1, 2, 4, 5, 6 |

### Roblox.Api.Avatar.Models.OutfitModel

A slim model for user outfits.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | `integer` | No | The id. |
| `name` | `string` | No | The name. |
| `isEditable` | `boolean` | No | Whether the outfit can be modified by the user. |
| `outfitType` | `string` | No | The type of the Outfit. |

### Roblox.Api.Avatar.Models.OutfitUpdateModelV3

A model containing details needed to update or create an outfit.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | `string` | No | The outfit name. |
| `bodyColor3s` | `Roblox.Api.Avatar.Models.BodyColors3Model` | No |  |
| `assets` | `Roblox.Api.Avatar.Models.AssetWearModel[]` | No | Array of assets. |
| `scale` | `Roblox.Web.Responses.Avatar.ScaleModel` | No |  |
| `playerAvatarType` | `string` | No | The avatar scale. |
| `outfitType` | `integer enum (6 values)` | No | The type of outfit. Values: 0, 1, 2, 4, 5, 6 |

### Roblox.Api.Avatar.Models.OutfitDetailsModelV2

A model containing details about a user outfit

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | `integer` | No | The id |
| `name` | `string` | No | The name |
| `assets` | `Roblox.Api.Avatar.Models.AssetModelV2[]` | No | A list of assetIds |
| `bodyColor3s` | `Roblox.Api.Avatar.Models.BodyColors3Model` | No |  |
| `scale` | `Roblox.Web.Responses.Avatar.ScaleModel` | No |  |
| `playerAvatarType` | `string` | No | The player avatar type - this can be R6 or R15. |
| `outfitType` | `string` | No | The outfit type of the outfit |
| `isEditable` | `boolean` | No | Whether the outfit can be edited by the user |
| `universeId` | `integer` | No | The universe id of the outfit, null when outfit is not created in-experience |
| `moderationStatus` | `string` | No | The moderation status of the outfit, not applicable when outfit is created outside experience |
| `bundleId` | `integer` | No | The bundle ID, currently only returned for in-experience created outfits. |
| `inventoryType` | `string` | No | The inventory type of the outfit. |

### Roblox.Api.Avatar.Models.V4.AvatarDefinition

Details about an avatar.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `avatarModel` | `Roblox.Api.Avatar.Models.V4.AvatarModelV4` | No |  |
| `avatarConfigurations` | `Roblox.Api.Avatar.Models.V4.AvatarConfigurations` | No |  |

### Roblox.Api.Avatar.Models.V4.Request.UpdateAvatarDefinitionRequestV4

Request model for updating an avatar definition (V4).

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `updateTypes` | `integer enum (9 values)[]` | No | The list of data needed to be updated. |
| `avatarDefinition` | `Roblox.Api.Avatar.Models.V4.UpdateAvatarDefinition` | No |  |

### Roblox.Api.Avatar.Models.V4.Response.UpdateAvatarDefinitionResponseV4

Response model for update avatar (V4).

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | `boolean` | No | Whether all requested changes were successfully applied. |
| `invalidAssets` | `Roblox.Api.Avatar.Models.AssetModelV2[]` | No | Temporary top-level mirror of Roblox.Api.Avatar.Models.V4.Response.AvatarValidationResultV4.InvalidAssets to unblock clients that still read `invalidAssets` at the response root during backgrounds rollout. Prefer Roblox.Api.Avatar.Models.V4.Response.UpdateAvatarDefinitionResponseV4.Validation.Roblox.Api.Avatar.Models.V4.Response.AvatarValidationResultV4.InvalidAssets. Will be reverted once the engine fix is fully deployed. |
| `validation` | `Roblox.Api.Avatar.Models.V4.Response.AvatarValidationResultV4` | No |  |

### Roblox.Api.Avatar.Models.V4.Request.CreateOutfitDefinitionRequestV4

Request model for creating an outfit (V4).

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `outfitDefinition` | `Roblox.Api.Avatar.Models.V4.UpdateOutfitDefinition` | No |  |

### Roblox.Api.Avatar.Models.V4.Response.CreateOutfitDefinitionResponseV4

Response model for create outfit (V4).

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | `boolean` | No | Whether all requested changes were successfully applied. |
| `validation` | `Roblox.Api.Avatar.Models.V4.Response.OutfitValidationResultV4` | No |  |

### Roblox.Api.Avatar.Models.V4.Request.UpdateOutfitDefinitionRequestV4

Request model for updating an outfit (V4).

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `updateTypes` | `integer enum (7 values)[]` | No | The list of data needed to be updated. |
| `outfitDefinition` | `Roblox.Api.Avatar.Models.V4.UpdateOutfitDefinition` | No |  |

### Roblox.Api.Avatar.Models.V4.Response.UpdateOutfitDefinitionResponseV4

Response model for update outfit (V4).

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | `boolean` | No | Whether all requested changes were successfully applied. |
| `validation` | `Roblox.Api.Avatar.Models.V4.Response.OutfitValidationResultV4` | No |  |

### Roblox.Api.Avatar.Models.V4.OutfitDefinition

Details about an outfit.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `moderationStatus` | `string` | No | The moderation status of the outfit, not applicable when outfit is created outside experience |
| `bundleId` | `integer` | No | The bundle ID, currently only returned for in-experience created outfits. |
| `outfitModel` | `Roblox.Api.Avatar.Models.V4.OutfitModelV4` | No |  |
| `outfitConfigurations` | `Roblox.Api.Avatar.Models.V4.OutfitConfigurations` | No |  |