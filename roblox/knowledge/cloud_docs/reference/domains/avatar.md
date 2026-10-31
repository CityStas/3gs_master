---
name: "Avatar Api v4"
last_updated: 2026-10-30T19:56:08Z
type: legacy
api_base_url: "https://avatar.roblox.com"
versions: [v4, v3, v2, v1]
endpoints: 30
auth: [cookie]
---

# Avatar Api v4

> **Warning:** Legacy APIs with cookie authentication can incorporate breaking changes without notice. We don't recommend them for production applications.

**Base URL:** `https://avatar.roblox.com`
**Versions:** v4, v3, v2, v1

## V4

### GET `/v4/avatar`

Gets the currently wearing avatar definition for the authenticated user.

Returns an Roblox.Api.Avatar.Models.V4.AvatarDefinition containing an Roblox.Api.Avatar.Models.V4.AvatarModelV4 and Roblox.Api.Avatar.Models.V4.AvatarConfigurations.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `selectionTypes` | query | `array` | Yes | Selection types for the avatar data to return. |
| `Roblox-Place-Id` | header | `integer (int64)` | No |  |

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
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://avatar.roblox.com/v4/avatar?selectionTypes={VALUE}"
```

### PATCH `/v4/avatar`

Sets the avatar to the incoming avatar using field masks.

Only allows items that you own, are not expired, and are wearable asset types.
Any assets being worn before this method is called are automatically removed.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `Roblox-Place-Id` | header | `integer (int64)` | No |  |

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
curl -X PATCH -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://avatar.roblox.com/v4/avatar" \
  -H "Content-Type: application/json" \
  -d '{"updateTypes":[0],"avatarDefinition":{"updateAvatarModel":{"scales":"...","playerAvatarType":"...","bodyColors":"...","assets":"..."},"updateAvatarConfig":{"emoteRequestModels":"...","thumbnailCustomizationModels":"...","backgroundRequestModel":"...","profileFrameRequestModel":"..."}}}'
```

### GET `/v4/avatar/users/{userId}`

Gets the currently wearing avatar definition for the specified user.

Returns an Roblox.Api.Avatar.Models.V4.AvatarDefinition containing an Roblox.Api.Avatar.Models.V4.AvatarModelV4 and Roblox.Api.Avatar.Models.V4.AvatarConfigurations.
Behavior is aligned with the V2 `GET v2/avatar/users/{userId}/avatar` endpoint.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer (int64)` | Yes | The target user id. |
| `selectionTypes` | query | `array` | Yes | Selection types for the avatar data to return. |
| `Roblox-Place-Id` | header | `integer (int64)` | No |  |

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
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://avatar.roblox.com/v4/avatar/users/{USERID}?selectionTypes={VALUE}"
```

### GET `/v4/outfits/{outfitId}/details`

Gets the definition for an outfit.

Returns an Roblox.Api.Avatar.Models.V4.OutfitDefinition containing an Roblox.Api.Avatar.Models.V4.OutfitModelV4 and background Roblox.Api.Avatar.Models.V4.OutfitConfigurations.
Behavior is aligned with the V1/V3 `GET v{1|3}/outfits/{userOutfitId}/details` endpoints (authentication optional).

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `outfitId` | path | `string` | Yes | The outfit id. |
| `selectionTypes` | query | `array` | No | Selection types for the outfit data to return. |
| `checkAssetAvailability` | query | `boolean` | No | Whether to return assets with availability status. |
| `Roblox-Place-Id` | header | `integer (int64)` | No |  |

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
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://avatar.roblox.com/v4/outfits/{OUTFITID}/details"
```

### POST `/v4/outfits/create`

Creates a new outfit.

Fails if any of the assetIds are not owned by the user, or not wearable types.
The name property of the request is optional as one will be auto-generated when the request has a null name.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `Roblox-Place-Id` | header | `integer (int64)` | No |  |

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
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
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

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `outfitId` | path | `string` | Yes | The user outfit id. |
| `Roblox-Place-Id` | header | `integer (int64)` | No |  |

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
curl -X PATCH -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://avatar.roblox.com/v4/outfits/{OUTFITID}" \
  -H "Content-Type: application/json" \
  -d '{"updateTypes":[0],"outfitDefinition":{"updateOutfitModel":{"name":"...","bodyColors":"...","assets":"...","scale":"...","playerAvatarType":"...","outfitType":"..."},"updateOutfitConfig":{"backgroundRequestModel":"..."}}}'
```

## Models

### Roblox.Api.Avatar.Models.AssetMetaModelV1

Exhaustive model denoting all possible metadata fields of an asset

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `order` | `integer` | No | Layered-clothing order |
| `puffiness` | `number` | No | Layered-clothing puffiness |
| `position` | `Roblox.Api.Avatar.Models.AssetPosition` | No |  |
| `rotation` | `Roblox.Api.Avatar.Models.AssetRotation` | No |  |
| `scale` | `Roblox.Api.Avatar.Models.AssetScale` | No |  |
| `headShape` | `integer enum (30 values)` | No | Head Shape selected for the asset id. Applicable for dynamic head assets. Values: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29 |
| `staticFacialAnimation` | `boolean` | No | Indicates user choice for facial animation. staticFacialAnimation=false, implies the toggle as on and face will animate. Applicable for dynamic head assets. |
| `version` | `integer` | No | Client-authoritative meta model format version - default is always 1 |

### Roblox.Api.Avatar.Models.AssetModelV2

A model containing details about an asset
- V2: adds CurrentVersionId, AssetMetaModel

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | `integer` | No | The id |
| `name` | `string` | No | The name |
| `assetType` | `Roblox.Api.Avatar.Models.AssetTypeModel` | No |  |
| `currentVersionId` | `integer` | No | Id of the current version of asset |
| `meta` | `Roblox.Api.Avatar.Models.AssetMetaModelV1` | No |  |
| `availabilityStatus` | `string` | No | Asset availability status. |
| `expirationTime` | `string` | No | For rental assets only. (Future) ownership expiration time of the asset. |
| `supportsHeadShapes` | `boolean` | No | If the "Id" is swappable, applicable for DH assets. |

### Roblox.Api.Avatar.Models.AssetPosition

A model which contains accessory position coordinates.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `X` | `number` | No | X coordinate of the position. |
| `Y` | `number` | No | y coordinate of the position. |
| `Z` | `number` | No | Z coordinate of the position. |

### Roblox.Api.Avatar.Models.AssetRotation

A model which contains accessory rotation coordinates.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `X` | `number` | No | X degrees of the rotation. |
| `Y` | `number` | No | Y degrees of the rotation. |
| `Z` | `number` | No | Z degrees of the rotation. |

### Roblox.Api.Avatar.Models.AssetScale

A model which contains accessory scale.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `X` | `number` | No | X scale multiplier of accessory. |
| `Y` | `number` | No | Y scale multiplier of accessory. |
| `Z` | `number` | No | Z scale multiplier of accessory. |

### Roblox.Api.Avatar.Models.AssetTypeModel

A model containing details about an asset type

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | `integer` | No | The id |
| `name` | `string` | No | The name |

### Roblox.Api.Avatar.Models.AssetWearModel

A model which contains
- an asset id
- AssetMetaModel

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | `integer` | No | An asset id |
| `meta` | `Roblox.Api.Avatar.Models.AssetMetaModelV1` | No |  |

### Roblox.Api.Avatar.Models.AvatarThumbnailCustomizationCameraModel

A model describing a the camera details for a single avatar thumbnail customization.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `fieldOfViewDeg` | `number` | No | Field of view for the camera, in degrees. |
| `yRotDeg` | `number` | No | Rotation around y axis, in degrees. |
| `distanceScale` | `number` | No | There's a natural camera distance we calculate based on avatar size. Apply this scale to that distance. |

### Roblox.Api.Avatar.Models.AvatarThumbnailCustomizationModel

A model describing a single avatar thumbnail customization.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `thumbnailType` | `0 \| 1 \| 2` | No | What type of 2D thumbnail are we customizing: \|Closeup, FullBody. |
| `emoteAssetId` | `integer` | No | What emote are we using to pose the avatar in the thumbnail. |
| `camera` | `Roblox.Api.Avatar.Models.AvatarThumbnailCustomizationCameraModel` | No |  |

### Roblox.Api.Avatar.Models.BodyColorsModelV4

A model containing RGB hex colors for each body part.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `headColor` | `string` | No | The RGB hex color for head color, e.g. #FFFFFF |
| `torsoColor` | `string` | No | The RGB hex color for torso color, e.g. #FFFFFF |
| `rightArmColor` | `string` | No | The RGB hex color for right arm color, e.g. #FFFFFF |
| `leftArmColor` | `string` | No | The RGB hex color for left arm color, e.g. #FFFFFF |
| `rightLegColor` | `string` | No | The RGB hex color for right leg color, e.g. #FFFFFF |
| `leftLegColor` | `string` | No | The RGB hex color for left leg color, e.g. #FFFFFF |

### Roblox.Api.Avatar.Models.EmoteRequestModel

Request model to equip a emote

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `assetId` | `integer` | No | The asset id of the emote |
| `position` | `integer` | No | The position to equip the emote to |

### Roblox.Api.Avatar.Models.EmoteResponseModel

Response object representing a user's emote

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `assetId` | `integer` | No | The asset id of the emote. |
| `assetName` | `string` | No | The name of the emote. |
| `position` | `integer` | No | The position the emote is equipped to. |

### Roblox.Api.Avatar.Models.InvalidBackgroundResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `BackgroundAssetId` | `integer` | No | The asset id of the emote |
| `Error` | `string` | No | The error associated with the background. |

### Roblox.Api.Avatar.Models.InvalidEmoteResponseModel

Response object representing an invalid emote

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `assetId` | `integer` | No | The asset id of the emote |
| `position` | `integer` | No | The position the emote is equipped to |
| `error` | `string` | No | The error occured while trying to equip this emote |

### Roblox.Api.Avatar.Models.InvalidProfileFrameResponse

Validation error for a profile frame that could not be applied.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `FrameAssetId` | `integer` | No | The asset id of the profile frame. |
| `Error` | `string` | No | The error associated with the profile frame. |

### Roblox.Api.Avatar.Models.V4.AvatarBackgroundModel

A model containing avatar background data.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `backgroundAsset` | `Roblox.Api.Avatar.Models.AssetModelV2` | No |  |

### Roblox.Api.Avatar.Models.V4.AvatarBackgroundRequestModel

A model which contains the asset id of the background. This can be
extended to have more attributes in the future.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | `integer` | No | An asset id. |

### Roblox.Api.Avatar.Models.V4.AvatarConfigurations

Avatar config details.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `emotes` | `Roblox.Api.Avatar.Models.EmoteResponseModel[]` | No | The emotes on the character. |
| `background` | `Roblox.Api.Avatar.Models.V4.AvatarBackgroundModel` | No |  |
| `thumbnailCustomizations` | `Roblox.Api.Avatar.Models.AvatarThumbnailCustomizationModel[]` | No | List of customizations set for this avatar. At most one per thumbnail type (Closeup, FullBody). |
| `profileFrame` | `Roblox.Api.Avatar.Models.V4.AvatarProfileFrameModel` | No |  |

### Roblox.Api.Avatar.Models.V4.AvatarDefinition

Details about an avatar.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `avatarModel` | `Roblox.Api.Avatar.Models.V4.AvatarModelV4` | No |  |
| `avatarConfigurations` | `Roblox.Api.Avatar.Models.V4.AvatarConfigurations` | No |  |

### Roblox.Api.Avatar.Models.V4.AvatarModelV4

A model containing details about an avatar.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `scales` | `Roblox.Web.Responses.Avatar.ScaleModel` | No |  |
| `playerAvatarType` | `1 \| 3` | No | The avatar type. |
| `bodyColors` | `Roblox.Api.Avatar.Models.BodyColorsModelV4` | No |  |
| `assets` | `Roblox.Api.Avatar.Models.AssetModelV2[]` | No | The assets worn on the character. |

### Roblox.Api.Avatar.Models.V4.AvatarProfileFrameModel

A model containing avatar profile frame data.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `frameAsset` | `Roblox.Api.Avatar.Models.AssetModelV2` | No |  |

### Roblox.Api.Avatar.Models.V4.AvatarProfileFrameRequestModel

A model which contains the asset id of the profile frame.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | `integer` | No | An asset id. Use 0 to clear the equipped frame. |

### Roblox.Api.Avatar.Models.V4.OutfitConfigurations

Background configuration for an outfit.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `background` | `Roblox.Api.Avatar.Models.V4.AvatarBackgroundModel` | No |  |

### Roblox.Api.Avatar.Models.V4.OutfitDefinition

Details about an outfit.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `moderationStatus` | `string` | No | The moderation status of the outfit, not applicable when outfit is created outside experience |
| `bundleId` | `integer` | No | The bundle ID, currently only returned for in-experience created outfits. |
| `outfitModel` | `Roblox.Api.Avatar.Models.V4.OutfitModelV4` | No |  |
| `outfitConfigurations` | `Roblox.Api.Avatar.Models.V4.OutfitConfigurations` | No |  |

### Roblox.Api.Avatar.Models.V4.OutfitModelV4

A model containing core outfit details.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `universeId` | `integer` | No | The universe id of the outfit, null when outfit is not created in-experience |
| `inventoryType` | `string` | No | The inventory type of the outfit. |
| `id` | `string` | No | The outfit id. |
| `name` | `string` | No | The outfit name. |
| `isEditable` | `boolean` | No | Whether the outfit can be modified by the user. |
| `outfitType` | `integer enum (6 values)` | No | The type of the outfit. Values: 0, 1, 2, 4, 5, 6 |
| `assets` | `Roblox.Api.Avatar.Models.AssetModelV2[]` | No | The assets on the outfit. |
| `bodyColors` | `Roblox.Api.Avatar.Models.BodyColorsModelV4` | No |  |
| `scale` | `Roblox.Web.Responses.Avatar.ScaleModel` | No |  |
| `playerAvatarType` | `1 \| 3` | No | The player avatar type. |

### Roblox.Api.Avatar.Models.V4.Request.CreateOutfitDefinitionRequestV4

Request model for creating an outfit (V4).

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `outfitDefinition` | `Roblox.Api.Avatar.Models.V4.UpdateOutfitDefinition` | No |  |

### Roblox.Api.Avatar.Models.V4.Request.UpdateAvatarDefinitionRequestV4

Request model for updating an avatar definition (V4).

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `updateTypes` | `integer enum (9 values)[]` | No | The list of data needed to be updated. |
| `avatarDefinition` | `Roblox.Api.Avatar.Models.V4.UpdateAvatarDefinition` | No |  |

### Roblox.Api.Avatar.Models.V4.Request.UpdateOutfitDefinitionRequestV4

Request model for updating an outfit (V4).

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `updateTypes` | `integer enum (7 values)[]` | No | The list of data needed to be updated. |
| `outfitDefinition` | `Roblox.Api.Avatar.Models.V4.UpdateOutfitDefinition` | No |  |

### Roblox.Api.Avatar.Models.V4.Response.AvatarValidationResultV4

Validation details for avatar mutation responses when one or more inputs could not be applied.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `invalidAssets` | `Roblox.Api.Avatar.Models.AssetModelV2[]` | No | Assets that could not be worn. |
| `invalidBackground` | `Roblox.Api.Avatar.Models.InvalidBackgroundResponse[]` | No | Background assets that could not be applied. |
| `invalidProfileFrame` | `Roblox.Api.Avatar.Models.InvalidProfileFrameResponse[]` | No | Profile frame assets that could not be applied. |
| `invalidEmotes` | `Roblox.Api.Avatar.Models.InvalidEmoteResponseModel[]` | No | Emotes that could not be equipped. |
| `invalidThumbnailCustomizations` | `Roblox.Api.Avatar.Models.V4.Response.InvalidThumbnailCustomizationResponse[]` | No | Thumbnail customizations that could not be applied. |

### Roblox.Api.Avatar.Models.V4.Response.CreateOutfitDefinitionResponseV4

Response model for create outfit (V4).

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | `boolean` | No | Whether all requested changes were successfully applied. |
| `validation` | `Roblox.Api.Avatar.Models.V4.Response.OutfitValidationResultV4` | No |  |

### Roblox.Api.Avatar.Models.V4.Response.InvalidThumbnailCustomizationResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `ThumbnailCustomizationModel` | `Roblox.Api.Avatar.Models.AvatarThumbnailCustomizationModel` | No |  |
| `Error` | `string` | No | The error associated with the thumbnail customization |

### Roblox.Api.Avatar.Models.V4.Response.OutfitValidationResultV4

Validation details for outfit mutation responses when one or more inputs could not be applied.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `unwornAssets` | `Roblox.Api.Avatar.Models.AssetModelV2[]` | No | Assets that could not be worn. |
| `invalidBackground` | `Roblox.Api.Avatar.Models.InvalidBackgroundResponse[]` | No | Background assets that could not be applied. |

### Roblox.Api.Avatar.Models.V4.Response.UpdateAvatarDefinitionResponseV4

Response model for update avatar (V4).

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | `boolean` | No | Whether all requested changes were successfully applied. |
| `invalidAssets` | `Roblox.Api.Avatar.Models.AssetModelV2[]` | No | Temporary top-level mirror of Roblox.Api.Avatar.Models.V4.Response.AvatarValidationResultV4.InvalidAssets to unblock clients that still read `invalidAssets` at the response root during backgrounds rollout. Prefer Roblox.Api.Avatar.Models.V4.Response.UpdateAvatarDefinitionResponseV4.Validation.Roblox.Api.Avatar.Models.V4.Response.AvatarValidationResultV4.InvalidAssets. Will be reverted once the engine fix is fully deployed. |
| `validation` | `Roblox.Api.Avatar.Models.V4.Response.AvatarValidationResultV4` | No |  |

### Roblox.Api.Avatar.Models.V4.Response.UpdateOutfitDefinitionResponseV4

Response model for update outfit (V4).

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | `boolean` | No | Whether all requested changes were successfully applied. |
| `validation` | `Roblox.Api.Avatar.Models.V4.Response.OutfitValidationResultV4` | No |  |

### Roblox.Api.Avatar.Models.V4.UpdateAvatarConfig

A model containing avatar config fields to update.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `emoteRequestModels` | `Roblox.Api.Avatar.Models.EmoteRequestModel[]` | No | The avatar's emotes. |
| `thumbnailCustomizationModels` | `Roblox.Api.Avatar.Models.AvatarThumbnailCustomizationModel[]` | No | The avatar's thumbnail customizations. |
| `backgroundRequestModel` | `Roblox.Api.Avatar.Models.V4.AvatarBackgroundRequestModel` | No |  |
| `profileFrameRequestModel` | `Roblox.Api.Avatar.Models.V4.AvatarProfileFrameRequestModel` | No |  |

### Roblox.Api.Avatar.Models.V4.UpdateAvatarDefinition

A model containing details about an avatar update.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `updateAvatarModel` | `Roblox.Api.Avatar.Models.V4.UpdateAvatarModelV4` | No |  |
| `updateAvatarConfig` | `Roblox.Api.Avatar.Models.V4.UpdateAvatarConfig` | No |  |

### Roblox.Api.Avatar.Models.V4.UpdateAvatarModelV4

A model containing avatar model fields to update.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `scales` | `Roblox.Web.Responses.Avatar.ScaleModel` | No |  |
| `playerAvatarType` | `1 \| 3` | No | The avatar type. |
| `bodyColors` | `Roblox.Api.Avatar.Models.BodyColorsModelV4` | No |  |
| `assets` | `Roblox.Api.Avatar.Models.AssetWearModel[]` | No | The assets worn on the character. |

### Roblox.Api.Avatar.Models.V4.UpdateOutfitConfig

A model containing outfit config fields to update.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `backgroundRequestModel` | `Roblox.Api.Avatar.Models.V4.AvatarBackgroundRequestModel` | No |  |

### Roblox.Api.Avatar.Models.V4.UpdateOutfitDefinition

A model containing outfit fields to create or update.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `updateOutfitModel` | `Roblox.Api.Avatar.Models.V4.UpdateOutfitModelV4` | No |  |
| `updateOutfitConfig` | `Roblox.Api.Avatar.Models.V4.UpdateOutfitConfig` | No |  |

### Roblox.Api.Avatar.Models.V4.UpdateOutfitModelV4

A model containing core outfit fields to update.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | `string` | No | The outfit name. |
| `bodyColors` | `Roblox.Api.Avatar.Models.BodyColorsModelV4` | No |  |
| `assets` | `Roblox.Api.Avatar.Models.AssetWearModel[]` | No | The assets on the outfit. |
| `scale` | `Roblox.Web.Responses.Avatar.ScaleModel` | No |  |
| `playerAvatarType` | `1 \| 3` | No | The player avatar type. |
| `outfitType` | `integer enum (6 values)` | No | The type of outfit (for example Avatar or Makeup). Defaults to Avatar when omitted. Values: 0, 1, 2, 4, 5, 6 |

### Roblox.Web.Responses.Avatar.ScaleModel

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `height` | `number` | No |  |
| `width` | `number` | No |  |
| `head` | `number` | No |  |
| `depth` | `number` | No |  |
| `proportion` | `number` | No |  |
| `bodyType` | `number` | No |  |

## V3

### GET `/v3/outfits/{userOutfitId}/details` *(deprecated)*

Gets details about the contents of an outfit.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userOutfitId` | path | `integer (int64)` | Yes | The user outfit id. |
| `Roblox-Place-Id` | header | `integer (int64)` | No |  |
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
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://avatar.roblox.com/v3/outfits/{USEROUTFITID}/details"
```

### POST `/v3/outfits/create` *(deprecated)*

Creates a new outfit.

Fails if any of the assetIds are not owned by the user, or not wearable types.
The name property of the request is optional as one will be auto-generated when the request has a null name.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `Roblox-Place-Id` | header | `integer (int64)` | No |  |

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
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://avatar.roblox.com/v3/outfits/create" \
  -H "Content-Type: application/json" \
  -d '{"name":"string","bodyColor3s":{"headColor3":"string","torsoColor3":"string","rightArmColor3":"string","leftArmColor3":"string","rightLegColor3":"string","leftLegColor3":"string"},"assets":[{"id":"...","meta":"..."}],"scale":{"height":0,"width":0,"head":0,"depth":0,"proportion":0,"bodyType":0},"playerAvatarType":"string","outfitType":0}'
```

### PATCH `/v3/outfits/{userOutfitId}` *(deprecated)*

Updates the contents of an outfit.

Fails if the user does not own any of the assetIds or if they are not wearable asset types.
Accepts partial updates.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userOutfitId` | path | `integer (int64)` | Yes | The user outfit id. |
| `Roblox-Place-Id` | header | `integer (int64)` | No |  |

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
curl -X PATCH -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://avatar.roblox.com/v3/outfits/{USEROUTFITID}" \
  -H "Content-Type: application/json" \
  -d '{"name":"string","bodyColor3s":{"headColor3":"string","torsoColor3":"string","rightArmColor3":"string","leftArmColor3":"string","rightLegColor3":"string","leftLegColor3":"string"},"assets":[{"id":"...","meta":"..."}],"scale":{"height":0,"width":0,"head":0,"depth":0,"proportion":0,"bodyType":0},"playerAvatarType":"string","outfitType":0}'
```

## Models

### Roblox.Api.Avatar.Models.AssetMetaModelV1

Exhaustive model denoting all possible metadata fields of an asset

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `order` | `integer` | No | Layered-clothing order |
| `puffiness` | `number` | No | Layered-clothing puffiness |
| `position` | `Roblox.Api.Avatar.Models.AssetPosition` | No |  |
| `rotation` | `Roblox.Api.Avatar.Models.AssetRotation` | No |  |
| `scale` | `Roblox.Api.Avatar.Models.AssetScale` | No |  |
| `headShape` | `integer enum (30 values)` | No | Head Shape selected for the asset id. Applicable for dynamic head assets. Values: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29 |
| `staticFacialAnimation` | `boolean` | No | Indicates user choice for facial animation. staticFacialAnimation=false, implies the toggle as on and face will animate. Applicable for dynamic head assets. |
| `version` | `integer` | No | Client-authoritative meta model format version - default is always 1 |

### Roblox.Api.Avatar.Models.AssetModelV2

A model containing details about an asset
- V2: adds CurrentVersionId, AssetMetaModel

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | `integer` | No | The id |
| `name` | `string` | No | The name |
| `assetType` | `Roblox.Api.Avatar.Models.AssetTypeModel` | No |  |
| `currentVersionId` | `integer` | No | Id of the current version of asset |
| `meta` | `Roblox.Api.Avatar.Models.AssetMetaModelV1` | No |  |
| `availabilityStatus` | `string` | No | Asset availability status. |
| `expirationTime` | `string` | No | For rental assets only. (Future) ownership expiration time of the asset. |
| `supportsHeadShapes` | `boolean` | No | If the "Id" is swappable, applicable for DH assets. |

### Roblox.Api.Avatar.Models.AssetPosition

A model which contains accessory position coordinates.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `X` | `number` | No | X coordinate of the position. |
| `Y` | `number` | No | y coordinate of the position. |
| `Z` | `number` | No | Z coordinate of the position. |

### Roblox.Api.Avatar.Models.AssetRotation

A model which contains accessory rotation coordinates.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `X` | `number` | No | X degrees of the rotation. |
| `Y` | `number` | No | Y degrees of the rotation. |
| `Z` | `number` | No | Z degrees of the rotation. |

### Roblox.Api.Avatar.Models.AssetScale

A model which contains accessory scale.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `X` | `number` | No | X scale multiplier of accessory. |
| `Y` | `number` | No | Y scale multiplier of accessory. |
| `Z` | `number` | No | Z scale multiplier of accessory. |

### Roblox.Api.Avatar.Models.AssetTypeModel

A model containing details about an asset type

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | `integer` | No | The id |
| `name` | `string` | No | The name |

### Roblox.Api.Avatar.Models.AssetWearModel

A model which contains
- an asset id
- AssetMetaModel

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | `integer` | No | An asset id |
| `meta` | `Roblox.Api.Avatar.Models.AssetMetaModelV1` | No |  |

### Roblox.Api.Avatar.Models.BodyColors3Model

A model containing RGB hex colors for each body part.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `headColor3` | `string` | No | The RGB hex color for head color, e.g. #FFFFFF |
| `torsoColor3` | `string` | No | The RGB hex color for torso color, e.g. #FFFFFF |
| `rightArmColor3` | `string` | No | The RGB hex color for right arm color, e.g. #FFFFFF |
| `leftArmColor3` | `string` | No | The RGB hex color for left arm color, e.g. #FFFFFF |
| `rightLegColor3` | `string` | No | The RGB hex color for right leg color, e.g. #FFFFFF |
| `leftLegColor3` | `string` | No | The RGB hex color for left leg color, e.g. #FFFFFF |

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

### Roblox.Web.Responses.Avatar.ScaleModel

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `height` | `number` | No |  |
| `width` | `number` | No |  |
| `head` | `number` | No |  |
| `depth` | `number` | No |  |
| `proportion` | `number` | No |  |
| `bodyType` | `number` | No |  |

## V2

### GET `/v2/avatar/avatar` *(deprecated)*

Returns details about the authenticated user's avatar.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `Roblox-Place-Id` | header | `integer (int64)` | No |  |
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
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://avatar.roblox.com/v2/avatar/avatar"
```

### GET `/v2/avatar/users/{userId}/avatar` *(deprecated)*

Returns details about a specified user's avatar.

Includes assets, bodycolors, and playerAvatarType.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer (int64)` | Yes |  |
| `Roblox-Place-Id` | header | `integer (int64)` | No |  |
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
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://avatar.roblox.com/v2/avatar/users/{USERID}/avatar"
```

### GET `/v2/avatar/users/{userId}/outfits`

Gets a list of outfits for the specified user.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer (int64)` | Yes | The user id. |
| `paginationToken` | query | `string` | No | The token received from the response to get the next page. For the first request, this value should be empty. Note : If no value is sent the 1st page will be returned. |
| `outfitType` | query | `string` | No | The outfit type being searched for, null will return all outfitTypes. |
| `page` | query | `integer (int32)` | No | The page number of the current page of requests, default is 1. |
| `itemsPerPage` | query | `integer (int32)` | No | The max number of outfits that can be returned. |
| `isEditable` | query | `boolean` | No | Whether the outfits are editable. A null value will lead to no filtering. |
| `Roblox-Place-Id` | header | `integer (int64)` | No | The placeId of the caller, not required to be passed in. |

**Responses:**

- `200`: OK → `Roblox.Api.Avatar.Models.AvatarPageResponse[Roblox.Api.Avatar.Models.OutfitModel]`
- `400`: 1: The specified user does not exist. 2: An account for the given userId does not exist!

**Response fields** (`Roblox.Api.Avatar.Models.AvatarPageResponse[Roblox.Api.Avatar.Models.OutfitModel]`)

See [Roblox.Api.Avatar.Models.AvatarPageResponse[Roblox.Api.Avatar.Models.OutfitModel]](#roblox-api-avatar-models-avatarpageresponse-roblox-api-avatar-models-outfitmodel-) in Models.

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
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://avatar.roblox.com/v2/avatar/users/{USERID}/outfits"
```

### POST `/v2/avatar/set-body-colors` *(deprecated)*

Sets the authenticated user's body colors.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `Roblox-Place-Id` | header | `integer (int64)` | No |  |

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
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
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

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `Roblox-Place-Id` | header | `integer (int64)` | No |  |

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
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
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

### POST `/v2/outfits/create` *(deprecated)*

Creates a new outfit.

Fails if any of the assetIds are not owned by the user, or not wearable types.
The name property of the request is optional as one will be auto-generated when the request has a null name.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `Roblox-Place-Id` | header | `integer (int64)` | No |  |

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
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://avatar.roblox.com/v2/outfits/create" \
  -H "Content-Type: application/json" \
  -d '{"name":"string","bodyColors":{"headColorId":0,"torsoColorId":0,"rightArmColorId":0,"leftArmColorId":0,"rightLegColorId":0,"leftLegColorId":0},"assets":[{"id":"...","meta":"..."}],"scale":{"height":0,"width":0,"head":0,"depth":0,"proportion":0,"bodyType":0},"playerAvatarType":"string","outfitType":0}'
```

### PATCH `/v2/avatar` *(deprecated)*

Sets the avatar to the incoming avatar using field masks.

Only allows items that you own, are not expired, and are wearable asset types.
Any assets being worn before this method is called are automatically removed.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `Roblox-Place-Id` | header | `integer (int64)` | No |  |

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
curl -X PATCH -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://avatar.roblox.com/v2/avatar" \
  -H "Content-Type: application/json" \
  -d '{"updateMask":[0],"data":{"scales":{"height":"...","width":"...","head":"...","depth":"...","proportion":"...","bodyType":"..."},"playerAvatarType":1,"bodyColors":{"headColor3":"...","torsoColor3":"...","rightArmColor3":"...","leftArmColor3":"...","rightLegColor3":"...","leftLegColor3":"..."},"assets":["..."]}}'
```

### PATCH `/v2/outfits/{userOutfitId}` *(deprecated)*

Updates the contents of an outfit.

Fails if the user does not own any of the assetIds or if they are not wearable asset types.
Accepts partial updates.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userOutfitId` | path | `integer (int64)` | Yes | The user outfit id. |
| `Roblox-Place-Id` | header | `integer (int64)` | No |  |

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
curl -X PATCH -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://avatar.roblox.com/v2/outfits/{USEROUTFITID}" \
  -H "Content-Type: application/json" \
  -d '{"name":"string","bodyColors":{"headColorId":0,"torsoColorId":0,"rightArmColorId":0,"leftArmColorId":0,"rightLegColorId":0,"leftLegColorId":0},"assets":[{"id":"...","meta":"..."}],"scale":{"height":0,"width":0,"head":0,"depth":0,"proportion":0,"bodyType":0},"playerAvatarType":"string","outfitType":0}'
```

## Models

### Roblox.Api.Avatar.Models.AssetMetaModelV1

Exhaustive model denoting all possible metadata fields of an asset

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `order` | `integer` | No | Layered-clothing order |
| `puffiness` | `number` | No | Layered-clothing puffiness |
| `position` | `Roblox.Api.Avatar.Models.AssetPosition` | No |  |
| `rotation` | `Roblox.Api.Avatar.Models.AssetRotation` | No |  |
| `scale` | `Roblox.Api.Avatar.Models.AssetScale` | No |  |
| `headShape` | `integer enum (30 values)` | No | Head Shape selected for the asset id. Applicable for dynamic head assets. Values: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29 |
| `staticFacialAnimation` | `boolean` | No | Indicates user choice for facial animation. staticFacialAnimation=false, implies the toggle as on and face will animate. Applicable for dynamic head assets. |
| `version` | `integer` | No | Client-authoritative meta model format version - default is always 1 |

### Roblox.Api.Avatar.Models.AssetModelV2

A model containing details about an asset
- V2: adds CurrentVersionId, AssetMetaModel

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | `integer` | No | The id |
| `name` | `string` | No | The name |
| `assetType` | `Roblox.Api.Avatar.Models.AssetTypeModel` | No |  |
| `currentVersionId` | `integer` | No | Id of the current version of asset |
| `meta` | `Roblox.Api.Avatar.Models.AssetMetaModelV1` | No |  |
| `availabilityStatus` | `string` | No | Asset availability status. |
| `expirationTime` | `string` | No | For rental assets only. (Future) ownership expiration time of the asset. |
| `supportsHeadShapes` | `boolean` | No | If the "Id" is swappable, applicable for DH assets. |

### Roblox.Api.Avatar.Models.AssetPosition

A model which contains accessory position coordinates.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `X` | `number` | No | X coordinate of the position. |
| `Y` | `number` | No | y coordinate of the position. |
| `Z` | `number` | No | Z coordinate of the position. |

### Roblox.Api.Avatar.Models.AssetRotation

A model which contains accessory rotation coordinates.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `X` | `number` | No | X degrees of the rotation. |
| `Y` | `number` | No | Y degrees of the rotation. |
| `Z` | `number` | No | Z degrees of the rotation. |

### Roblox.Api.Avatar.Models.AssetScale

A model which contains accessory scale.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `X` | `number` | No | X scale multiplier of accessory. |
| `Y` | `number` | No | Y scale multiplier of accessory. |
| `Z` | `number` | No | Z scale multiplier of accessory. |

### Roblox.Api.Avatar.Models.AssetTypeModel

A model containing details about an asset type

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | `integer` | No | The id |
| `name` | `string` | No | The name |

### Roblox.Api.Avatar.Models.AssetWearModel

A model which contains
- an asset id
- AssetMetaModel

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | `integer` | No | An asset id |
| `meta` | `Roblox.Api.Avatar.Models.AssetMetaModelV1` | No |  |

### Roblox.Api.Avatar.Models.AvatarApiSuccessResponse

Success response class

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | `boolean` | No | Gets or sets a value indicating whether the request was a success. |

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

### Roblox.Api.Avatar.Models.AvatarPageResponse[Roblox.Api.Avatar.Models.OutfitModel]

Avatar page response.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | `Roblox.Api.Avatar.Models.OutfitModel[]` | No | The data |
| `paginationToken` | `string` | No | A non empty string indicates that there is more data available than this response contains. An empty string indicates the last page. |

### Roblox.Api.Avatar.Models.BodyColors3Model

A model containing RGB hex colors for each body part.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `headColor3` | `string` | No | The RGB hex color for head color, e.g. #FFFFFF |
| `torsoColor3` | `string` | No | The RGB hex color for torso color, e.g. #FFFFFF |
| `rightArmColor3` | `string` | No | The RGB hex color for right arm color, e.g. #FFFFFF |
| `leftArmColor3` | `string` | No | The RGB hex color for left arm color, e.g. #FFFFFF |
| `rightLegColor3` | `string` | No | The RGB hex color for right leg color, e.g. #FFFFFF |
| `leftLegColor3` | `string` | No | The RGB hex color for left leg color, e.g. #FFFFFF |

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

### Roblox.Api.Avatar.Models.EmoteResponseModel

Response object representing a user's emote

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `assetId` | `integer` | No | The asset id of the emote. |
| `assetName` | `string` | No | The name of the emote. |
| `position` | `integer` | No | The position the emote is equipped to. |

### Roblox.Api.Avatar.Models.OutfitModel

A slim model for user outfits.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | `integer` | No | The id. |
| `name` | `string` | No | The name. |
| `isEditable` | `boolean` | No | Whether the outfit can be modified by the user. |
| `outfitType` | `string` | No | The type of the Outfit. |

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

### Roblox.Api.Avatar.Models.UpdateAvatarDataModel

A model containing details about an avatar.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `scales` | `Roblox.Web.Responses.Avatar.ScaleModel` | No |  |
| `playerAvatarType` | `1 \| 3` | No | The avatar type. |
| `bodyColors` | `Roblox.Api.Avatar.Models.BodyColors3Model` | No |  |
| `assets` | `Roblox.Api.Avatar.Models.AssetWearModel[]` | No | The assets worn on the character. |

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

### Roblox.Platform.Avatar.BodyColorsModelV2

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `headColor3` | `string` | No |  |
| `torsoColor3` | `string` | No |  |
| `rightArmColor3` | `string` | No |  |
| `leftArmColor3` | `string` | No |  |
| `rightLegColor3` | `string` | No |  |
| `leftLegColor3` | `string` | No |  |

### Roblox.Web.Responses.Avatar.ScaleModel

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `height` | `number` | No |  |
| `width` | `number` | No |  |
| `head` | `number` | No |  |
| `depth` | `number` | No |  |
| `proportion` | `number` | No |  |
| `bodyType` | `number` | No |  |

## V1

### GET `/v1/avatar` *(deprecated)*

Returns details about the authenticated user's avatar.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `Roblox-Place-Id` | header | `integer (int64)` | No |  |

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
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://avatar.roblox.com/v1/avatar"
```

### GET `/v1/avatar-rules`

Returns the business rules related to avatars.

BodyColorsPalette is a list of valid brickColors you can choose for your avatar.
WearableAssetTypes contains a list of asset types with names, ids, and the maximum number that you can wear at a time.
Does not include packages because they cannot be worn on your avatar directly.
PlayerAvatarTypes are the types of avatars you can choose between.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `Roblox-Place-Id` | header | `integer (int64)` | No |  |

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
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://avatar.roblox.com/v1/avatar-rules"
```

### GET `/v1/avatar/metadata`

Returns metadata used by the avatar page of the website.

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
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://avatar.roblox.com/v1/avatar/metadata"
```

### GET `/v1/game-start-info`

The server will call this on game server start to request general information about the universe
This is version 1.1, which returns an entry from the UniverseAvatarType enum.
During mixed mode this may return unreliable results.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | query | `integer (int64)` | Yes |  |
| `Roblox-Place-Id` | header | `integer (int64)` | No |  |

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
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://avatar.roblox.com/v1/game-start-info?universeId={VALUE}"
```

### GET `/v1/outfits/{userOutfitId}/details` *(deprecated)*

Gets details about the contents of an outfit.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userOutfitId` | path | `integer (int64)` | Yes | The user outfit id. |
| `Roblox-Place-Id` | header | `integer (int64)` | No |  |

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
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://avatar.roblox.com/v1/outfits/{USEROUTFITID}/details"
```

### GET `/v1/users/{userId}/avatar` *(deprecated)*

Returns details about a specified user's avatar.

Includes assets, bodycolors, and playerAvatarType.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer (int64)` | Yes |  |
| `Roblox-Place-Id` | header | `integer (int64)` | No |  |

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
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://avatar.roblox.com/v1/users/{USERID}/avatar"
```

### GET `/v1/users/{userId}/currently-wearing`

Gets a list of asset ids that the user is currently wearing.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer (int64)` | Yes | The user id. |
| `Roblox-Place-Id` | header | `integer (int64)` | No |  |

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
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://avatar.roblox.com/v1/users/{USERID}/currently-wearing"
```

### GET `/v1/users/{userId}/outfits` *(deprecated)*

Deprecated, user v2.
Gets a list of outfits for the specified user.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer (int64)` | Yes | The user id. |
| `outfitType` | query | `string` | No | The outfit type being searched for, null will return all outfitTypes. |
| `page` | query | `integer (int32)` | No | The page number of the current page of requests, default is 1. |
| `itemsPerPage` | query | `integer (int32)` | No | The max number of outfits that can be returned. |
| `isEditable` | query | `boolean` | No | Whether the outfits are editable. A null value will lead to no filtering. |
| `Roblox-Place-Id` | header | `integer (int64)` | No | The placeId of the caller, not required to be passed in. |

**Responses:**

- `200`: OK → `Roblox.Api.Avatar.Models.AvatarFilteredPageResponse[Roblox.Api.Avatar.Models.OutfitModel]`
- `400`: 1: The specified user does not exist. 2: An account for the given userId does not exist!

**Response fields** (`Roblox.Api.Avatar.Models.AvatarFilteredPageResponse[Roblox.Api.Avatar.Models.OutfitModel]`)

See [Roblox.Api.Avatar.Models.AvatarFilteredPageResponse[Roblox.Api.Avatar.Models.OutfitModel]](#roblox-api-avatar-models-avatarfilteredpageresponse-roblox-api-avatar-models-outfitmodel-) in Models.

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
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://avatar.roblox.com/v1/users/{USERID}/outfits"
```

### POST `/v1/avatar/redraw-thumbnail`

Requests the authenticated user's thumbnail be redrawn.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `Roblox-Place-Id` | header | `integer (int64)` | No |  |

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
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://avatar.roblox.com/v1/avatar/redraw-thumbnail"
```

### POST `/v1/avatar/set-body-colors` *(deprecated)*

Sets the authenticated user's body colors.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `Roblox-Place-Id` | header | `integer (int64)` | No |  |

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
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
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

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `Roblox-Place-Id` | header | `integer (int64)` | No |  |

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
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://avatar.roblox.com/v1/avatar/set-player-avatar-type" \
  -H "Content-Type: application/json" \
  -d '{
  "playerAvatarType": 1
}'
```

### POST `/v1/avatar/set-scales` *(deprecated)*

Sets the authenticated user's scales.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `Roblox-Place-Id` | header | `integer (int64)` | No |  |

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
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
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

### POST `/v1/outfits/{userOutfitId}/delete`

Deletes the outfit.

You are only allowed to delete outfits you created.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userOutfitId` | path | `integer (int64)` | Yes | The user outfit id. |
| `Roblox-Place-Id` | header | `integer (int64)` | No |  |

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
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://avatar.roblox.com/v1/outfits/{USEROUTFITID}/delete"
```

## Models

### Roblox.Api.Avatar.Models.AccessoryPositionModel

A model which contains accessory position coordinates

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `xPosition` | `number` | No | Float that determines the absolute position refinement in studs that this accessory is relocated in the x-direction |
| `yPosition` | `number` | No | Float that determines the absolute position refinement in studs that this accessory is relocated in the y-direction |
| `zPosition` | `number` | No | Float that determines the absolute position refinement in studs that this accessory is relocated in the z-direction |

### Roblox.Api.Avatar.Models.AccessoryRefinementModel

A model containing details about accessory refinement data

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `position` | `Roblox.Api.Avatar.Models.AccessoryPositionModel` | No |  |
| `rotation` | `Roblox.Api.Avatar.Models.AccessoryRotationModel` | No |  |
| `scale` | `Roblox.Api.Avatar.Models.AccessoryScaleModel` | No |  |

### Roblox.Api.Avatar.Models.AccessoryRotationModel

A model which contains accessory rotation coordinates

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `xRotation` | `number` | No | Float from -180 to 180 that determines the absolute rotation refinement that this accessory is rotated in the x-direction |
| `yRotation` | `number` | No | Float from -180 to 180 that determines the absolute rotation refinement that this accessory is rotated in the y-direction |
| `zRotation` | `number` | No | Float from -180 to 180 that determines the absolute rotation refinement that this accessory is rotated in the z-direction |

### Roblox.Api.Avatar.Models.AccessoryScaleModel

A model which contains accessory Scale, that is the multiplier
with respect to the default size. For example, scale = 2 means
twice the default size of an asset

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `xScale` | `number` | No | Float that determines the scale refinement that this accessory is resized in the x-direction Default size is 1 |
| `yScale` | `number` | No | Float that determines the scale refinement that this accessory is resized in the y-direction Default size is 1 |
| `zScale` | `number` | No | Float that determines the scale refinement that this accessory is resized in the z-direction Default size is 1 |

### Roblox.Api.Avatar.Models.AssetIdListModel

A model that contains a list of asset ids

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `assetIds` | `integer[]` | No | The asset ids |

### Roblox.Api.Avatar.Models.AssetMetaModelV1

Exhaustive model denoting all possible metadata fields of an asset

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `order` | `integer` | No | Layered-clothing order |
| `puffiness` | `number` | No | Layered-clothing puffiness |
| `position` | `Roblox.Api.Avatar.Models.AssetPosition` | No |  |
| `rotation` | `Roblox.Api.Avatar.Models.AssetRotation` | No |  |
| `scale` | `Roblox.Api.Avatar.Models.AssetScale` | No |  |
| `headShape` | `integer enum (30 values)` | No | Head Shape selected for the asset id. Applicable for dynamic head assets. Values: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29 |
| `staticFacialAnimation` | `boolean` | No | Indicates user choice for facial animation. staticFacialAnimation=false, implies the toggle as on and face will animate. Applicable for dynamic head assets. |
| `version` | `integer` | No | Client-authoritative meta model format version - default is always 1 |

### Roblox.Api.Avatar.Models.AssetModelV2

A model containing details about an asset
- V2: adds CurrentVersionId, AssetMetaModel

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | `integer` | No | The id |
| `name` | `string` | No | The name |
| `assetType` | `Roblox.Api.Avatar.Models.AssetTypeModel` | No |  |
| `currentVersionId` | `integer` | No | Id of the current version of asset |
| `meta` | `Roblox.Api.Avatar.Models.AssetMetaModelV1` | No |  |
| `availabilityStatus` | `string` | No | Asset availability status. |
| `expirationTime` | `string` | No | For rental assets only. (Future) ownership expiration time of the asset. |
| `supportsHeadShapes` | `boolean` | No | If the "Id" is swappable, applicable for DH assets. |

### Roblox.Api.Avatar.Models.AssetPosition

A model which contains accessory position coordinates.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `X` | `number` | No | X coordinate of the position. |
| `Y` | `number` | No | y coordinate of the position. |
| `Z` | `number` | No | Z coordinate of the position. |

### Roblox.Api.Avatar.Models.AssetRotation

A model which contains accessory rotation coordinates.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `X` | `number` | No | X degrees of the rotation. |
| `Y` | `number` | No | Y degrees of the rotation. |
| `Z` | `number` | No | Z degrees of the rotation. |

### Roblox.Api.Avatar.Models.AssetScale

A model which contains accessory scale.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `X` | `number` | No | X scale multiplier of accessory. |
| `Y` | `number` | No | Y scale multiplier of accessory. |
| `Z` | `number` | No | Z scale multiplier of accessory. |

### Roblox.Api.Avatar.Models.AssetTypeModel

A model containing details about an asset type

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | `integer` | No | The id |
| `name` | `string` | No | The name |

### Roblox.Api.Avatar.Models.AssetTypeRulesModel

A model containing details about an asset type and its business rules

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `maxNumber` | `integer` | No | The max number of this asset type that can be worn |
| `id` | `integer` | No | The id |
| `name` | `string` | No | The name |

### Roblox.Api.Avatar.Models.AvatarApiSuccessResponse

Success response class

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | `boolean` | No | Gets or sets a value indicating whether the request was a success. |

### Roblox.Api.Avatar.Models.AvatarFilteredPageResponse[Roblox.Api.Avatar.Models.OutfitModel]

Filtered page response

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `filteredCount` | `integer` | No | Number of !:TPagedObject filtered. |
| `data` | `Roblox.Api.Avatar.Models.OutfitModel[]` | No |  |
| `total` | `integer` | No |  |

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

### Roblox.Api.Avatar.Models.BodyColorModel

A model container BrickColor ids for each body part.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `brickColorId` | `integer` | No | The BrickColor id |
| `hexColor` | `string` | No | The hex color, e.g. #FFFFFF |
| `name` | `string` | No | The name of the BrickColor |

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

### Roblox.Api.Avatar.Models.DefaultClothingAssets

A model containing details about avatar-related business rules

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `defaultShirtAssetIds` | `integer[]` | No | List of asset Ids used to equip shirts for default clothing when the avatar appears nude. |
| `defaultPantAssetIds` | `integer[]` | No | List of asset Ids used to equip pants for default clothing when the avatar appears nude. |

### Roblox.Api.Avatar.Models.EmoteResponseModel

Response object representing a user's emote

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `assetId` | `integer` | No | The asset id of the emote. |
| `assetName` | `string` | No | The name of the emote. |
| `position` | `integer` | No | The position the emote is equipped to. |

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

### Roblox.Api.Avatar.Models.OutfitModel

A slim model for user outfits.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | `integer` | No | The id. |
| `name` | `string` | No | The name. |
| `isEditable` | `boolean` | No | Whether the outfit can be modified by the user. |
| `outfitType` | `string` | No | The type of the Outfit. |

### Roblox.Api.Avatar.Models.PlayerAvatarTypeModel

A model that contains a playerAvatarType

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `playerAvatarType` | `1 \| 3` | No | The playerAvatarType |

### Roblox.Api.Avatar.Models.ScaleRulesModel

A model that contains information about the max/mins for each scale

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `min` | `number` | No | The min scale |
| `max` | `number` | No | The max scale |
| `increment` | `number` | No | The increment of the scale |

### Roblox.Api.Avatar.Models.UniverseAvatarAssetOverrideResponseModel

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `assetID` | `integer` | No |  |
| `assetTypeID` | `integer` | No |  |
| `isPlayerChoice` | `boolean` | No |  |

### Roblox.Web.Responses.Avatar.ScaleModel

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `height` | `number` | No |  |
| `width` | `number` | No |  |
| `head` | `number` | No |  |
| `depth` | `number` | No |  |
| `proportion` | `number` | No |  |
| `bodyType` | `number` | No |  |