---
name: "Develop Api v2"
last_updated: 2026-10-30T19:56:08Z
type: legacy
api_base_url: "https://develop.roblox.com"
versions: [v2, v1]
endpoints: 36
auth: [cookie]
---

# Develop Api v2

> **Warning:** Legacy APIs with cookie authentication can incorporate breaking changes without notice. We don't recommend them for production applications.

**Base URL:** `https://develop.roblox.com`
**Versions:** v2, v1

## V2

### GET `/v2/assets/{id}/versions` *(deprecated)*

Retrieves asset information for the specified asset ID. The authenticated user must be able to manage the asset
or granted by package permission.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `id` | path | `integer (int64)` | Yes | The ID of the asset.Roblox.Platform.Assets.IAsset |
| `Roblox-Place-Id` | header | `integer (int64)` | Yes | The ID of the place.Roblox.Platform.Assets.IPlace |
| `limit` | query | `integer (int32)` | No | The number of results per request. Valid values: `10`, `25`, `50`, `100` |
| `cursor` | query | `string` | No | The paging cursor for the previous or next page. |
| `sortOrder` | query | `string` | No | Sort by version number, default is desc. Valid values: `Asc`, `Desc` |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiPageResponse[Roblox.Api.Develop.AssetVersion]`

**Response fields** (`Roblox.Web.WebAPI.Models.ApiPageResponse[Roblox.Api.Develop.AssetVersion]`)

See [Roblox.Web.WebAPI.Models.ApiPageResponse[Roblox.Api.Develop.AssetVersion]](#roblox-web-webapi-models-apipageresponse-roblox-api-develop-assetversion-) in Models.

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
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://develop.roblox.com/v2/assets/{ID}/versions"
```

### GET `/v2/places/{placeId}`

Gets the place configuration for the place with the id placeId

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `placeId` | path | `integer (int64)` | Yes | The place id for the place to be updated. |

**Responses:**

- `200`: OK → `Roblox.Api.Develop.Models.PlaceModelV2`
- `401`: 0: Authorization has been denied for this request.
- `403`: Authenticated user is not authorized to manage this place.
- `404`: placeId Place not found.

**Response fields** (`Roblox.Api.Develop.Models.PlaceModelV2`)

See [Roblox.Api.Develop.Models.PlaceModelV2](#roblox-api-develop-models-placemodelv2) in Models.

**Response example:**
```json
{
  "maxPlayerCount": 0,
  "socialSlotType": "string",
  "customSocialSlotsCount": 0,
  "allowCopying": false,
  "currentSavedVersion": 0,
  "isAllGenresAllowed": false
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://develop.roblox.com/v2/places/{PLACEID}"
```

### PATCH `/v2/places/{placeId}`

Updates the place configuration for the place with the id placeId

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `placeId` | path | `integer (int64)` | Yes | The place id for the place to be updated. |

**Request Body:** `application/json` — Type: `Roblox.Api.Develop.Models.PlaceConfigurationModelV2`

See [Roblox.Api.Develop.Models.PlaceConfigurationModelV2](#roblox-api-develop-models-placeconfigurationmodelv2) in Models.

**Request example:**
```json
{
  "name": "string",
  "description": "string",
  "maxPlayerCount": 0,
  "socialSlotType": "string",
  "customSocialSlotsCount": 0,
  "allowCopying": false
}
```

**Responses:**

- `200`: OK → `Roblox.Api.Develop.Models.PlaceModelV2`
- `401`: 0: Authorization has been denied for this request.
- `403`: Authenticated user is not authorized to manage this place. 0: Token Validation Failed
- `404`: placeId Place not found.

**Response fields** (`Roblox.Api.Develop.Models.PlaceModelV2`)

See [Roblox.Api.Develop.Models.PlaceModelV2](#roblox-api-develop-models-placemodelv2) in Models.

**Response example:**
```json
{
  "maxPlayerCount": 0,
  "socialSlotType": "string",
  "customSocialSlotsCount": 0,
  "allowCopying": false,
  "currentSavedVersion": 0,
  "isAllGenresAllowed": false
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X PATCH -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://develop.roblox.com/v2/places/{PLACEID}" \
  -H "Content-Type: application/json" \
  -d '{
  "name": "string",
  "description": "string",
  "maxPlayerCount": 0,
  "socialSlotType": "string",
  "customSocialSlotsCount": 0,
  "allowCopying": false
}'
```

### PATCH `/v2/universes/{universeId}/configuration`

Update universe settings for an owned universe.
V2 Contains data for avatar scale and asset override.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer (int64)` | Yes | The universeId. |

**Request Body:** `application/json` — Type: `Roblox.Api.Develop.Models.UniverseSettingsRequestV2`

See [Roblox.Api.Develop.Models.UniverseSettingsRequestV2](#roblox-api-develop-models-universesettingsrequestv2) in Models.

**Request example:**
```json
{
  "allowPrivateServers": false,
  "privateServerPrice": 0,
  "name": "string",
  "description": "string",
  "promotionalText": "string",
  "universeAvatarType": 1
}
```

**Responses:**

- `200`: OK → `Roblox.Api.Develop.Models.UniverseSettingsResponseV2`
- `400`: 1: The universe does not exist. 3: Invalid UniverseAvatarType. 4: Invalid UniverseScaleType. 5: Invalid UniverseAnimationType. 6: Invalid UniverseCollisionType. 7: New universe name or description has been rejected. 8: New universe name is too long. 10: Invalid UniverseBodyType. 11: Invalid UniverseJointPositioningType. 12: The universe has no root place. 15: Price is required when isForSale is true. 16: This game cannot be offered for sale because it is not public. 17: This game cannot be offered for sale because it has private servers enabled. 18: The game price is outside of the allowed range. 19: Invalid genre. 20: The request body is missing. 21: Invalid device type. 22: Invalid asset type. 23: Invalid value, the min must be less than or equal to the max 24: Invalid scale value 26: Invalid private server price 28: OptIn/Out Regions Not Supported. 41: You cannot change the private server price again so soon after the previous change. Please try again later. 44: The provided audience configuration is invalid. Ensure the audience list contains only supported audience values. 52: Promotional text has been rejected.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 2: You are not authorized to configure this universe. 14: You are not authorized to sell games. 25: Not authorized to update private server settings 29: Luobu app terms of service user agreement is missing. 30: Unknown error while updating Opt in out region. 45: The creator of this experience is not eligible to set this audience.
- `409`: 9: Failed to shutdown all intances of game after changing AvatarType. The change has been reverted.
- `500`: 27: Unknown error while updating private server settings 43: Failed to update the audience configuration. The change was not applied. Please try again.
- `503`: 53: Promotional text safety validation is temporarily unavailable.

**Response fields** (`Roblox.Api.Develop.Models.UniverseSettingsResponseV2`)

See [Roblox.Api.Develop.Models.UniverseSettingsResponseV2](#roblox-api-develop-models-universesettingsresponsev2) in Models.

**Response example:**
```json
{
  "allowPrivateServers": false,
  "privateServerPrice": 0,
  "optInRegions": [
    {
      "region": "...",
      "status": "..."
    }
  ],
  "isMeshTextureApiAccessAllowed": false,
  "isRewardedOnDemandAdsAllowed": false,
  "id": 0
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X PATCH -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://develop.roblox.com/v2/universes/{UNIVERSEID}/configuration" \
  -H "Content-Type: application/json" \
  -d '{
  "allowPrivateServers": false,
  "privateServerPrice": 0,
  "name": "string",
  "description": "string",
  "promotionalText": "string",
  "universeAvatarType": 1
}'
```

### DELETE `/v2/teamtest/{placeId}`

Close a game instance that is being used for team testing

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `placeId` | path | `integer (int64)` | Yes | The Id of the place we are setting the metadata for. |
| `gameId` | query | `string (uuid)` | Yes | the Guid of the game instance System.Guid |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X DELETE -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://develop.roblox.com/v2/teamtest/{PLACEID}?gameId={VALUE}"
```

## Models

### Roblox.Api.Develop.AssetVersion

Model of an asset version.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `Id` | `integer` | No | The VersionID of the asset version. |
| `assetId` | `integer` | No | The ID of the asset. |
| `assetVersionNumber` | `integer` | No | The version number. |
| `creatorType` | `string` | No | Type of the asset version creator. |
| `creatorTargetId` | `integer` | No | ID of the asset version creator. |
| `creatingUniverseId` | `integer` | No | ID of the universe this asset version was created in. |
| `created` | `string` | No | The created date of this asset version. |
| `isEqualToCurrentPublishedVersion` | `boolean` | No | Indicates if this version is same to current published version. This property is available on /v1/{assetId}/published-versions and /v1/{assetId}/version/{versionNumber}. |
| `isPublished` | `boolean` | No | Indicates if this version is / was published. This property is available on /v1/{assetId}/saved-versions. This should be true for all assets coming from GetAssetPublishedVersionsByAssetId |

### Roblox.Api.Develop.Models.PlaceConfigurationModelV2

A model containing information about a place to be configured

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | `string` | No | The name for the place. |
| `description` | `string` | No | The new description for the place. |
| `maxPlayerCount` | `integer` | No | The max number of players for the place. |
| `socialSlotType` | `string` | No | The social slot type for the place. Determines how users are placed into servers.  Examples:       Automatic,      Empty,      Custom |
| `customSocialSlotsCount` | `integer` | No | The number of social slots for the place when the slot type is custom. |
| `allowCopying` | `boolean` | No | Determines if copying of the place is allowed. |
| `allowedGearTypes` | `string[]` | No | List of allowed gear types |
| `isAllGenresAllowed` | `boolean` | No | If all genres are allowed, or only the experience type |

### Roblox.Api.Develop.Models.PlaceModelV2

A model containing information about a place

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `maxPlayerCount` | `integer` | No | The max number of players for the place. |
| `socialSlotType` | `string` | No | The social slot type for the place. Determines how users are placed into servers.  Examples:       Automatic,      Empty,      Custom |
| `customSocialSlotsCount` | `integer` | No | The number of social slots for the place when the slot type is custom. |
| `allowCopying` | `boolean` | No | Determines if copying of the place is allowed. |
| `currentSavedVersion` | `integer` | No | The current saved version number of the place. |
| `isAllGenresAllowed` | `boolean` | No | Whether all genres allowed in the place. |
| `allowedGearTypes` | `integer enum (10 values)[]` | No | Types of Roblox gear that are allowed to exist in the place. Valid values are from amp::AssetCategory |
| `maxPlayersAllowed` | `integer` | No | The maximum allowed number of players for the place that the user can set, based on user roleset. |
| `created` | `string` | No | The time place was created. |
| `updated` | `string` | No | The time place was updated. |
| `id` | `integer` | No | Returns the place id. |
| `universeId` | `integer` | No | Returns the id of the place's universe, or null - if the place is not part of a universe. |
| `name` | `string` | No | Returns the place name. |
| `description` | `string` | No | Returns the place description. |
| `isRootPlace` | `boolean` | No | Returns whether this place is the root place. |

### Roblox.Api.Develop.Models.UniverseModerationPolicyStatus

Represents a universe moderation policy status

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `region` | `0 \| 1` | No | The region policy label ['Unknown' = 0, 'China' = 1] |
| `status` | `string` | No | The status of the universe |

### Roblox.Api.Develop.Models.UniverseSettingsRequestV2

Model for UniverseSettings patch requests

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `allowPrivateServers` | `boolean` | No | If the universe allows the use of private servers. |
| `privateServerPrice` | `integer` | No | The price to purchase a private server in robux. |
| `name` | `string` | No | The name of the universe. |
| `description` | `string` | No | The description of the universe. |
| `promotionalText` | `string` | No | Promotional text for the universe. Empty stores an empty value. |
| `universeAvatarType` | `1 \| 2 \| 3` | No | Which avatar types are allowed in the universe. |
| `universeAnimationType` | `1 \| 2` | No | Whether custom animations are allowed in the universe. |
| `universeCollisionType` | `1 \| 2` | No | What type of collisions are used by the universe. |
| `universeJointPositioningType` | `1 \| 2` | No | What avatar joint positioning type is allowed by the universe. |
| `engineAvatarSettings` | `string` | No | Optional JSON string used to store avatar settings used by the game engine. Will not be updated if null or empty. To clear settings, set to empty JSON object "{}". Note: This is an experimental field which may be changed or removed in future. |
| `isArchived` | `boolean` | No | Archive status of the universe. |
| `isFriendsOnly` | `boolean` | No | Whether game access is limited to friends for user-owned games or group members for group-owned games. |
| `genre` | `integer enum (15 values)` | No | Game genre. Values: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 |
| `playableDevices` | `integer enum (6 values)[]` | No | List of device types this game can be played on. |
| `isForSale` | `boolean` | No | Whether the game is offered for sale. |
| `price` | `integer` | No | Price of the game, in Robux. |
| `universeAvatarAssetOverrides` | `Roblox.Platform.UniverseSettings.UniverseAvatarAssetOverrideResponseModel[]` | No | A list of avatar asset overrides. |
| `universeAvatarMinScales` | `Roblox.Web.Responses.Avatar.ScaleModel` | No |  |
| `universeAvatarMaxScales` | `Roblox.Web.Responses.Avatar.ScaleModel` | No |  |
| `studioAccessToApisAllowed` | `boolean` | No | Whether Studio can access data stores of this universe. |
| `permissions` | `Roblox.UniversePluginPermissionAuthority.Models.UniversePluginPermissions` | No |  |
| `optInRegions` | `0 \| 1[]` | No | A list of opt in region. |
| `optOutRegions` | `0 \| 1[]` | No | A list of opt out region. |
| `isMeshTextureApiAccessAllowed` | `boolean` | No | Sets whether access to APIs for mesh and texture is enabled for this universe. |
| `isRewardedOnDemandAdsAllowed` | `boolean` | No | Whether rewarded on-demand ads are allowed for this universe. |
| `fiatBasePriceId` | `string` | No | Sets the base price of the experience for Fiat purchases. |
| `fiatProductChangeType` | `0 \| 1 \| 2 \| 3` | No | Determines the change type of the Fiat Product Change request. Can either Activate, Update Base Price, or Deactivate. |
| `audiences` | `0 \| 1 \| 2 \| 3 \| 4[]` | No | The audiences this universe should be visible to (e.g. Editors, PlayTesters, Friends, Public). When provided, replaces the universe's existing audience set with the supplied values. |
| `demoModeEnabled` | `boolean` | No | Whether demo mode is enabled for this paid access game. |

### Roblox.Api.Develop.Models.UniverseSettingsResponseV2

Model for UniverseSettings controller responses

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `allowPrivateServers` | `boolean` | No | If the universe allows the use of private servers. |
| `privateServerPrice` | `integer` | No | The price to purchase a private server in robux. |
| `optInRegions` | `Roblox.Api.Develop.Models.UniverseModerationPolicyStatus[]` | No | The regions the universe has opted in for |
| `isMeshTextureApiAccessAllowed` | `boolean` | No | Whether access to APIs for mesh and texture is enabled for this universe. |
| `isRewardedOnDemandAdsAllowed` | `boolean` | No | Whether rewarded on-demand ads are allowed for this universe. |
| `id` | `integer` | No | The universe Id. |
| `name` | `string` | No | The universe name. |
| `description` | `string` | No | The universe description. |
| `promotionalText` | `string` | No | Promotional Text for the universe. |
| `universeAvatarType` | `1 \| 2 \| 3` | No | Which avatar types are allowed in the universe. ['MorphToR6' = 1, 'PlayerChoice' = 2, 'MorphToR15' = 3] |
| `universeAnimationType` | `1 \| 2` | No | Whether custom animations are allowed in the universe. ['Standard' = 1, 'PlayerChoice' = 2] |
| `universeCollisionType` | `1 \| 2` | No | What type of collisions are used by the universe. ['InnerBox' = 1, 'OuterBox' = 2] |
| `universeJointPositioningType` | `1 \| 2` | No | What avatar joint positioning is allowed by the universe. ['Standard' = 1, 'ArtistIntent' = 2] |
| `engineAvatarSettings` | `string` | No | Optional JSON string used to store avatar settings used by the game engine. Note: This is an experimental field which may be changed or removed in future. |
| `isArchived` | `boolean` | No | Archive status of the universe |
| `isFriendsOnly` | `boolean` | No | Whether game access is limited to friends for user-owned games or group members for group-owned games. |
| `genre` | `integer enum (15 values)` | No | Game genre. ['All' = 0, 'Tutorial' = 1, 'Scary' = 2, 'TownAndCity' = 3, 'War' = 4, 'Funny' = 5, 'Fantasy' = 6, 'Adventure' = 7, 'SciFi' = 8, 'Pirate' = 9, 'FPS' = 10, 'RPG' = 11, 'Sports' = 12, 'Ninja' = 13, 'WildWest' = 14] Values: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 |
| `playableDevices` | `integer enum (6 values)[]` | No | List of device types this game can be played on. |
| `isForSale` | `boolean` | No | Whether the game is offered for sale. |
| `price` | `integer` | No | Price of the game, in Robux. |
| `universeAvatarAssetOverrides` | `Roblox.Platform.UniverseSettings.UniverseAvatarAssetOverrideResponseModel[]` | No | A collection of avatar asset settings allowed by the universe. |
| `universeAvatarMinScales` | `Roblox.Web.Responses.Avatar.ScaleModel` | No |  |
| `universeAvatarMaxScales` | `Roblox.Web.Responses.Avatar.ScaleModel` | No |  |
| `studioAccessToApisAllowed` | `boolean` | No | Whether Studio can access data stores of this universe. |
| `permissions` | `Roblox.UniversePluginPermissionAuthority.Models.UniversePluginPermissions` | No |  |
| `isForSaleInFiat` | `boolean` | No | Whether the game is offered for sale in fiat. |
| `fiatBasePriceId` | `string` | No | The basePriceId for the Fiat product. |
| `fiatModerationStatus` | `0 \| 1 \| 2 \| 3 \| 4` | No | The current moderation status of the game if it is for sale in fiat. ['Invalid' = 0, 'NotModerated' = 1, 'Pending' = 2, 'Approved' = 3, 'Rejected' = 4] |
| `audiences` | `0 \| 1 \| 2 \| 3 \| 4[]` | No | The audiences this universe is visible to (e.g. Editors, PlayTesters, Friends, Public). Always non-null; may be empty when audience visibility has not been configured. |
| `demoModeEnabled` | `boolean` | No | Whether demo mode is enabled. |
| `demoModeChangeableAfter` | `string` | No | The earliest time at which demo mode can be toggled again (ISO 8601). Null when no cooldown is active (i.e. demo mode can be changed immediately). |

### Roblox.Platform.UniverseSettings.UniverseAvatarAssetOverrideResponseModel

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `assetID` | `integer` | No |  |
| `assetTypeID` | `integer` | No |  |
| `isPlayerChoice` | `boolean` | No |  |

### Roblox.UniversePluginPermissionAuthority.Models.UniversePluginPermissions

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `IsThirdPartyTeleportAllowed` | `boolean` | No |  |
| `IsThirdPartyAssetAllowed` | `boolean` | No |  |
| `IsThirdPartyPurchaseAllowed` | `boolean` | No |  |
| `IsClientTeleportAllowed` | `boolean` | No |  |

### Roblox.Web.Responses.Avatar.ScaleModel

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `height` | `number` | No |  |
| `width` | `number` | No |  |
| `head` | `number` | No |  |
| `depth` | `number` | No |  |
| `proportion` | `number` | No |  |
| `bodyType` | `number` | No |  |

### Roblox.Web.WebAPI.Models.ApiPageResponse[Roblox.Api.Develop.AssetVersion]

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `previousPageCursor` | `string` | No |  |
| `nextPageCursor` | `string` | No |  |
| `data` | `Roblox.Api.Develop.AssetVersion[]` | No |  |

## V1

### GET `/v1/assets/voting` *(deprecated)*

Gets the voting information of the given assets

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `assetIds` | query | `array` | Yes | The ids of the Roblox.Platform.Assets.IAsset. |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.Api.Develop.Models.Response.AssetVotingModel]`

**Response fields** (`Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.Api.Develop.Models.Response.AssetVotingModel]`)

See [Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.Api.Develop.Models.Response.AssetVotingModel]](#roblox-web-webapi-models-apiarrayresponse-roblox-api-develop-models-response-assetvotingmodel-) in Models.

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
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://develop.roblox.com/v1/assets/voting?assetIds={VALUE}"
```

### GET `/v1/gametemplates`

Gets a page of templates that can be used to start off making games.

Templates subject to change without notice.
Sort order of templates specified by Roblox.

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.Api.Develop.Models.GameTemplateModel]`

**Response fields** (`Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.Api.Develop.Models.GameTemplateModel]`)

See [Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.Api.Develop.Models.GameTemplateModel]](#roblox-web-webapi-models-apiarrayresponse-roblox-api-develop-models-gametemplatemodel-) in Models.

**Response example:**
```json
{
  "data": [
    {
      "gameTemplateType": "...",
      "hasTutorials": "...",
      "universe": "..."
    }
  ]
}
```

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://develop.roblox.com/v1/gametemplates"
```

### GET `/v1/groups/{groupId}/universes`

Gets a list of universes for the given group.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer (int64)` | Yes | The group id. |
| `isArchived` | query | `boolean` | No | Whether or not to return archived games. |
| `limit` | query | `integer (int32)` | No | The number of results per request. Valid values: `10`, `25`, `50`, `100` |
| `cursor` | query | `string` | No | The paging cursor for the previous or next page. |
| `sortOrder` | query | `string` | No | Sorted by universeId Valid values: `Asc`, `Desc` |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiPageResponse[Roblox.Api.Develop.Models.UniverseModel]`
- `400`: Invalid groupId.

**Response fields** (`Roblox.Web.WebAPI.Models.ApiPageResponse[Roblox.Api.Develop.Models.UniverseModel]`)

See [Roblox.Web.WebAPI.Models.ApiPageResponse[Roblox.Api.Develop.Models.UniverseModel]](#roblox-web-webapi-models-apipageresponse-roblox-api-develop-models-universemodel-) in Models.

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
      "isArchived": "...",
      "rootPlaceId": "...",
      "isActive": "..."
    }
  ]
}
```

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://develop.roblox.com/v1/groups/{GROUPID}/universes"
```

### GET `/v1/places/{placeId}/teamcreate/active_session/members`

List of users in the active Team Create session

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `placeId` | path | `integer (int64)` | Yes | The place Id. |
| `limit` | query | `integer (int32)` | No | The number of results per request. Valid values: `10`, `25`, `50`, `100` |
| `cursor` | query | `string` | No | The paging cursor for the previous or next page. |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.Web.Responses.Users.SkinnyUserResponse]`
- `400`: 1: The universe is invalid. 5: The place is invalid.
- `401`: 0: Authorization has been denied for this request.
- `403`: 2: Not authorized to perform this action. 4: TeamCreate on universe is disabled.
- `404`: 0: An unknown error occurred.
- `500`: 6: Multiple active sessions in a Team Create place.

**Response fields** (`Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.Web.Responses.Users.SkinnyUserResponse]`)

See [Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.Web.Responses.Users.SkinnyUserResponse]](#roblox-web-webapi-models-apiarrayresponse-roblox-web-responses-users-skinnyuserresponse-) in Models.

**Response example:**
```json
{
  "data": [
    {
      "id": "...",
      "name": "...",
      "displayName": "..."
    }
  ]
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://develop.roblox.com/v1/places/{PLACEID}/teamcreate/active_session/members"
```

### GET `/v1/plugins`

Gets plugin details by ids.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `pluginIds` | query | `array` | Yes | The plugin ids. |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.Web.Responses.Plugins.PluginResponse]`
- `400`: 1: Too many ids. 2: The format of the ids are invalid.

**Response fields** (`Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.Web.Responses.Plugins.PluginResponse]`)

See [Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.Web.Responses.Plugins.PluginResponse]](#roblox-web-webapi-models-apiarrayresponse-roblox-web-responses-plugins-pluginresponse-) in Models.

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

### GET `/v1/universes/{universeId}`

Gets a Roblox.Api.Develop.Models.UniverseModel.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer (int64)` | Yes | The Universe id. |

**Responses:**

- `200`: OK → `Roblox.Api.Develop.Models.UniverseModel`
- `400`: 1: The universe does not exist.

**Response fields** (`Roblox.Api.Develop.Models.UniverseModel`)

See [Roblox.Api.Develop.Models.UniverseModel](#roblox-api-develop-models-universemodel) in Models.

**Response example:**
```json
{
  "id": 0,
  "name": "string",
  "description": "string",
  "isArchived": false,
  "rootPlaceId": 0,
  "isActive": false
}
```

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://develop.roblox.com/v1/universes/{UNIVERSEID}"
```

### GET `/v1/universes/{universeId}/activation-eligibility`

Returns the result of various checks for a user's eligibility to activate a given universe from private to public universeId for authenticated user

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer (int64)` | Yes | The universe id. |

**Responses:**

- `200`: OK → `Roblox.Api.Develop.Models.ActivationEligibilityResponse`

**Response fields** (`Roblox.Api.Develop.Models.ActivationEligibilityResponse`)

See [Roblox.Api.Develop.Models.ActivationEligibilityResponse](#roblox-api-develop-models-activationeligibilityresponse) in Models.

**Response example:**
```json
{
  "isEligible": false,
  "maturityRated": false,
  "isUserEligibleForPublicPublish": false,
  "remainingPublicPublishCount": 0,
  "isPublicPublish": false,
  "isPublishToExistingUniverse": false
}
```

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://develop.roblox.com/v1/universes/{UNIVERSEID}/activation-eligibility"
```

### GET `/v1/universes/{universeId}/configuration`

Get settings for an owned universe.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer (int64)` | Yes | The universe Id. |

**Responses:**

- `200`: OK → `Roblox.Api.Develop.Models.UniverseSettingsResponse`
- `400`: 1: The universe does not exist.
- `401`: 0: Authorization has been denied for this request.
- `403`: 2: You are not authorized to configure this universe.

**Response fields** (`Roblox.Api.Develop.Models.UniverseSettingsResponse`)

See [Roblox.Api.Develop.Models.UniverseSettingsResponse](#roblox-api-develop-models-universesettingsresponse) in Models.

**Response example:**
```json
{
  "allowPrivateServers": false,
  "privateServerPrice": 0,
  "isMeshTextureApiAccessAllowed": false,
  "isRewardedOnDemandAdsAllowed": false,
  "id": 0,
  "name": "string"
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://develop.roblox.com/v1/universes/{UNIVERSEID}/configuration"
```

### PATCH `/v1/universes/{universeId}/configuration`

Update universe settings for an owned universe.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer (int64)` | Yes | The universeId. |

**Request Body:** `application/json` — Type: `Roblox.Api.Develop.Models.UniverseSettingsRequest`

See [Roblox.Api.Develop.Models.UniverseSettingsRequest](#roblox-api-develop-models-universesettingsrequest) in Models.

**Request example:**
```json
{
  "name": "string",
  "universeAvatarType": 1,
  "universeScaleType": 1,
  "universeAnimationType": 1,
  "universeCollisionType": 1,
  "universeBodyType": 1
}
```

**Responses:**

- `200`: OK → `Roblox.Api.Develop.Models.UniverseSettingsResponse`
- `400`: 1: The universe does not exist. 3: Invalid UniverseAvatarType. 4: Invalid UniverseScaleType. 5: Invalid UniverseAnimationType. 6: Invalid UniverseCollisionType. 7: New universe name or description has been rejected. 8: New universe name is too long. 10: Invalid UniverseBodyType. 11: Invalid UniverseJointPositioningType. 12: The universe has no root place. 15: Price is required when isForSale is true. 16: This game cannot be offered for sale because it is not public. 17: This game cannot be offered for sale because it has private servers enabled. 18: The game price is outside of the allowed range. 19: Invalid genre. 20: The request body is missing. 21: Invalid device type. 22: Invalid asset type. 23: Invalid value, the min must be less than or equal to the max 24: Invalid scale value 41: You cannot change the private server price again so soon after the previous change. Please try again later.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 2: You are not authorized to configure this universe. 14: You are not authorized to sell games.
- `409`: 9: Failed to shutdown all intances of game after changing AvatarType. The change has been reverted.

**Response fields** (`Roblox.Api.Develop.Models.UniverseSettingsResponse`)

See [Roblox.Api.Develop.Models.UniverseSettingsResponse](#roblox-api-develop-models-universesettingsresponse) in Models.

**Response example:**
```json
{
  "allowPrivateServers": false,
  "privateServerPrice": 0,
  "isMeshTextureApiAccessAllowed": false,
  "isRewardedOnDemandAdsAllowed": false,
  "id": 0,
  "name": "string"
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X PATCH -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://develop.roblox.com/v1/universes/{UNIVERSEID}/configuration" \
  -H "Content-Type: application/json" \
  -d '{
  "name": "string",
  "universeAvatarType": 1,
  "universeScaleType": 1,
  "universeAnimationType": 1,
  "universeCollisionType": 1,
  "universeBodyType": 1
}'
```

### GET `/v1/universes/{universeId}/configuration/playtesters`

Get the list of playtesters for an owned universe.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer (int64)` | Yes | The universe Id. |

**Responses:**

- `200`: OK → `Roblox.Api.Develop.Models.PlaytestersResponse`
- `400`: 1: The universe does not exist.
- `401`: 0: Authorization has been denied for this request.
- `403`: 2: You are not authorized to configure this universe.

**Response fields** (`Roblox.Api.Develop.Models.PlaytestersResponse`)

See [Roblox.Api.Develop.Models.PlaytestersResponse](#roblox-api-develop-models-playtestersresponse) in Models.

**Response example:**
```json
{
  "playtesters": [
    0
  ]
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://develop.roblox.com/v1/universes/{UNIVERSEID}/configuration/playtesters"
```

### POST `/v1/universes/{universeId}/configuration/playtesters`

Add playtesters to an owned universe. Existing ids are ignored (additive union).

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer (int64)` | Yes | The universe Id. |

**Request Body:** `application/json` — Type: `Roblox.Api.Develop.Models.PlaytestersRequest`

See [Roblox.Api.Develop.Models.PlaytestersRequest](#roblox-api-develop-models-playtestersrequest) in Models.

**Request example:**
```json
{
  "playtesters": [
    0
  ]
}
```

**Responses:**

- `200`: OK → `Roblox.Api.Develop.Models.PlaytestersResponse`
- `400`: 1: The universe does not exist. 48: The playtesters list is missing or empty. 49: Too many playtesters were specified in a single request. 51: One or more playtesters cannot be added due to safety restrictions.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 2: You are not authorized to configure this universe.

**Response fields** (`Roblox.Api.Develop.Models.PlaytestersResponse`)

See [Roblox.Api.Develop.Models.PlaytestersResponse](#roblox-api-develop-models-playtestersresponse) in Models.

**Response example:**
```json
{
  "playtesters": [
    0
  ]
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://develop.roblox.com/v1/universes/{UNIVERSEID}/configuration/playtesters" \
  -H "Content-Type: application/json" \
  -d '{
  "playtesters": [
    0
  ]
}'
```

### DELETE `/v1/universes/{universeId}/configuration/playtesters`

Remove playtesters from an owned universe.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer (int64)` | Yes | The universe Id. |

**Request Body:** `application/json` — Type: `Roblox.Api.Develop.Models.PlaytestersRequest`

See [Roblox.Api.Develop.Models.PlaytestersRequest](#roblox-api-develop-models-playtestersrequest) in Models.

**Request example:**
```json
{
  "playtesters": [
    0
  ]
}
```

**Responses:**

- `200`: OK → `Roblox.Api.Develop.Models.PlaytestersResponse`
- `400`: 1: The universe does not exist. 48: The playtesters list is missing or empty. 49: Too many playtesters were specified in a single request.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 2: You are not authorized to configure this universe.

**Response fields** (`Roblox.Api.Develop.Models.PlaytestersResponse`)

See [Roblox.Api.Develop.Models.PlaytestersResponse](#roblox-api-develop-models-playtestersresponse) in Models.

**Response example:**
```json
{
  "playtesters": [
    0
  ]
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X DELETE -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://develop.roblox.com/v1/universes/{UNIVERSEID}/configuration/playtesters" \
  -H "Content-Type: application/json" \
  -d '{
  "playtesters": [
    0
  ]
}'
```

### GET `/v1/universes/{universeId}/configuration/vip-servers`

Get settings for an owned universe's VIP servers.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer (int64)` | Yes | The universe Id. |

**Responses:**

- `200`: OK → `Roblox.Api.Develop.Models.PrivateServerDetailsResponse`
- `400`: 1: The universe does not exist.
- `401`: 0: Authorization has been denied for this request.
- `403`: 2: You are not authorized to configure this universe.

**Response fields** (`Roblox.Api.Develop.Models.PrivateServerDetailsResponse`)

See [Roblox.Api.Develop.Models.PrivateServerDetailsResponse](#roblox-api-develop-models-privateserverdetailsresponse) in Models.

**Response example:**
```json
{
  "isEnabled": false,
  "price": 0,
  "activeServersCount": 0,
  "activeSubscriptionsCount": 0
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://develop.roblox.com/v1/universes/{UNIVERSEID}/configuration/vip-servers"
```

### GET `/v1/universes/{universeId}/permissions`

Returns list of granted and declined permissions related to the universe with the id universeId for authenticated user

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer (int64)` | Yes | The universe id. |

**Responses:**

- `200`: OK → `Roblox.Api.Develop.Models.UniversePermissionsModel`
- `400`: 1: The universe does not exist.
- `401`: 0: Authorization has been denied for this request.

**Response fields** (`Roblox.Api.Develop.Models.UniversePermissionsModel`)

See [Roblox.Api.Develop.Models.UniversePermissionsModel](#roblox-api-develop-models-universepermissionsmodel) in Models.

**Response example:**
```json
{
  "canManage": false,
  "canCloudEdit": false
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://develop.roblox.com/v1/universes/{UNIVERSEID}/permissions"
```

### GET `/v1/universes/{universeId}/places`

Gets a list of places for a universe.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer (int64)` | Yes | The asset id. |
| `isUniverseCreation` | query | `boolean` | No |  |
| `limit` | query | `integer (int32)` | No | The number of results per request. Valid values: `10`, `25`, `50`, `100` |
| `cursor` | query | `string` | No | The paging cursor for the previous or next page. |
| `sortOrder` | query | `string` | No | Sorted by placeId Valid values: `Asc`, `Desc` |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiPageResponse[Roblox.Api.Develop.Models.IPlaceModel]`

**Response fields** (`Roblox.Web.WebAPI.Models.ApiPageResponse[Roblox.Api.Develop.Models.IPlaceModel]`)

See [Roblox.Web.WebAPI.Models.ApiPageResponse[Roblox.Api.Develop.Models.IPlaceModel]](#roblox-web-webapi-models-apipageresponse-roblox-api-develop-models-iplacemodel-) in Models.

**Response example:**
```json
{
  "previousPageCursor": "string",
  "nextPageCursor": "string",
  "data": [
    "..."
  ]
}
```

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://develop.roblox.com/v1/universes/{UNIVERSEID}/places"
```

### GET `/v1/universes/{universeId}/teamcreate`

Gets TeamCreate settings for an Roblox.Platform.Universes.IUniverse.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer (int64)` | Yes | The universe Id. |

**Responses:**

- `200`: OK → `Roblox.Api.Develop.Models.Response.TeamCreateSettingsResponse`
- `400`: Roblox.Api.Develop.ResponseEnums.TeamCreateErrors.InvalidUniverse
- `401`: 0: Authorization has been denied for this request.
- `403`: Roblox.Api.Develop.ResponseEnums.TeamCreateErrors.Unauthorized

**Response fields** (`Roblox.Api.Develop.Models.Response.TeamCreateSettingsResponse`)

See [Roblox.Api.Develop.Models.Response.TeamCreateSettingsResponse](#roblox-api-develop-models-response-teamcreatesettingsresponse) in Models.

**Response example:**
```json
{
  "isEnabled": false
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://develop.roblox.com/v1/universes/{UNIVERSEID}/teamcreate"
```

### PATCH `/v1/universes/{universeId}/teamcreate`

Edit team create settings for a universe.

Enables, or disables team create for a universe.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer (int64)` | Yes | The universe Id. |

**Request Body:** `application/json` — Type: `Roblox.Api.Develop.Models.UpdateTeamCreateSettingsRequest`

See [Roblox.Api.Develop.Models.UpdateTeamCreateSettingsRequest](#roblox-api-develop-models-updateteamcreatesettingsrequest) in Models.

**Request example:**
```json
{
  "isEnabled": false
}
```

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: Roblox.Api.Develop.ResponseEnums.TeamCreateErrors.InvalidUniverse
- `401`: 0: Authorization has been denied for this request.
- `403`: Roblox.Api.Develop.ResponseEnums.TeamCreateErrors.Unauthorized 0: Token Validation Failed

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X PATCH -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://develop.roblox.com/v1/universes/{UNIVERSEID}/teamcreate" \
  -H "Content-Type: application/json" \
  -d '{
  "isEnabled": false
}'
```

### GET `/v1/universes/multiget`

Gets a list of universes.

If a universe can not be found for a given ID (such as -1) it will be skipped.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `ids` | query | `array` | Yes | The universe IDs to get. Limit 100. |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.Api.Develop.Models.UniverseModel]`
- `400`: 8: No universe IDs sent to get. 9: Too many universe IDs sent to get, the limit is:

**Response fields** (`Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.Api.Develop.Models.UniverseModel]`)

See [Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.Api.Develop.Models.UniverseModel]](#roblox-web-webapi-models-apiarrayresponse-roblox-api-develop-models-universemodel-) in Models.

**Response example:**
```json
{
  "data": [
    {
      "id": "...",
      "name": "...",
      "description": "...",
      "isArchived": "...",
      "rootPlaceId": "...",
      "isActive": "..."
    }
  ]
}
```

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://develop.roblox.com/v1/universes/multiget?ids={VALUE}"
```

### GET `/v1/universes/multiget/permissions`

Returns an array of granted and declined permissions related to the universes with the ids in ids for the authenticated user.

If a universe can not be found for a given ID (such as -1) it will be skipped.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `ids` | query | `array` | Yes | The universe ids. |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.Api.Develop.Models.UniverseIdPermissionsModel]`
- `400`: 8: No universe IDs sent to get. 9: Too many universe IDs sent to get, the limit is:
- `401`: 0: Authorization has been denied for this request.

**Response fields** (`Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.Api.Develop.Models.UniverseIdPermissionsModel]`)

See [Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.Api.Develop.Models.UniverseIdPermissionsModel]](#roblox-web-webapi-models-apiarrayresponse-roblox-api-develop-models-universeidpermissionsmodel-) in Models.

**Response example:**
```json
{
  "data": [
    {
      "universeId": "...",
      "canManage": "...",
      "canCloudEdit": "..."
    }
  ]
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://develop.roblox.com/v1/universes/multiget/permissions?ids={VALUE}"
```

### GET `/v1/universes/multiget/teamcreate`

Gets TeamCreate settings for multiple universes specified by Ids

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `ids` | query | `array` | Yes | The universe Ids. |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.Api.Develop.Models.UniverseTeamCreateSettingsModel]`
- `400`: Roblox.Api.Develop.ResponseEnums.TeamCreateErrors.TooManyUniverseIdsSent
- `401`: 0: Authorization has been denied for this request.

**Response fields** (`Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.Api.Develop.Models.UniverseTeamCreateSettingsModel]`)

See [Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.Api.Develop.Models.UniverseTeamCreateSettingsModel]](#roblox-web-webapi-models-apiarrayresponse-roblox-api-develop-models-universeteamcreatesettingsmodel-) in Models.

**Response example:**
```json
{
  "data": [
    {
      "id": "...",
      "isEnabled": "..."
    }
  ]
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://develop.roblox.com/v1/universes/multiget/teamcreate?ids={VALUE}"
```

### GET `/v1/universes/user-public-publish-eligibility`

Returns the result of various checks for a user's eligibility to publish a public universe

**Responses:**

- `200`: OK → `Roblox.Api.Develop.Models.UserPublicPublishEligibilityResponse`

**Response fields** (`Roblox.Api.Develop.Models.UserPublicPublishEligibilityResponse`)

See [Roblox.Api.Develop.Models.UserPublicPublishEligibilityResponse](#roblox-api-develop-models-userpublicpublisheligibilityresponse) in Models.

**Response example:**
```json
{
  "isEligible": false,
  "hasTransactions": 0,
  "idVerified": 0,
  "hasDevex": 0
}
```

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://develop.roblox.com/v1/universes/user-public-publish-eligibility"
```

### GET `/v1/user/groups/canmanage`

Gets a list of Groups that a user can manage.

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.Api.Develop.Models.GroupModel]`
- `401`: 0: Authorization has been denied for this request.

**Response fields** (`Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.Api.Develop.Models.GroupModel]`)

See [Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.Api.Develop.Models.GroupModel]](#roblox-web-webapi-models-apiarrayresponse-roblox-api-develop-models-groupmodel-) in Models.

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
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://develop.roblox.com/v1/user/groups/canmanage"
```

### GET `/v1/user/groups/canmanagegamesoritems`

Gets a list of groups a user can manage games or items for.

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.Api.Develop.Models.GroupModel]`
- `401`: 0: Authorization has been denied for this request.

**Response fields** (`Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.Api.Develop.Models.GroupModel]`)

See [Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.Api.Develop.Models.GroupModel]](#roblox-web-webapi-models-apiarrayresponse-roblox-api-develop-models-groupmodel-) in Models.

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
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://develop.roblox.com/v1/user/groups/canmanagegamesoritems"
```

### GET `/v1/user/universes`

Gets a list of universes for the authenticated user.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `isArchived` | query | `boolean` | No | Whether or not to return archived games. |
| `limit` | query | `integer (int32)` | No | The number of results per request. Valid values: `10`, `25`, `50`, `100` |
| `cursor` | query | `string` | No | The paging cursor for the previous or next page. |
| `sortOrder` | query | `string` | No | Sorted by universeId Valid values: `Asc`, `Desc` |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiPageResponse[Roblox.Api.Develop.Models.UniverseModel]`
- `400`: cursor is not valid.
- `401`: 0: Authorization has been denied for this request.

**Response fields** (`Roblox.Web.WebAPI.Models.ApiPageResponse[Roblox.Api.Develop.Models.UniverseModel]`)

See [Roblox.Web.WebAPI.Models.ApiPageResponse[Roblox.Api.Develop.Models.UniverseModel]](#roblox-web-webapi-models-apipageresponse-roblox-api-develop-models-universemodel-) in Models.

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
      "isArchived": "...",
      "rootPlaceId": "...",
      "isActive": "..."
    }
  ]
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://develop.roblox.com/v1/user/universes"
```

### POST `/v1/places/{placeId}`

Updates the place configuration for the place with the id placeId

Currently the only supported functionality for updating the configuration is around Name, and Description.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `placeId` | path | `integer (int64)` | Yes | The place id for the place to be updated. |

**Request Body:** `application/json` — Type: `Roblox.Api.Develop.Models.PlaceConfigurationModel`

See [Roblox.Api.Develop.Models.PlaceConfigurationModel](#roblox-api-develop-models-placeconfigurationmodel) in Models.

**Request example:**
```json
{
  "name": "string",
  "description": "string"
}
```

**Responses:**

- `200`: OK → `Roblox.Api.Develop.Models.PlaceModel`
- `400`: placeId is invalid.
- `401`: 0: Authorization has been denied for this request.
- `403`: Authenticated user is not authorized to manage this place. 0: Token Validation Failed

**Response fields** (`Roblox.Api.Develop.Models.PlaceModel`)

See [Roblox.Api.Develop.Models.PlaceModel](#roblox-api-develop-models-placemodel) in Models.

**Response example:**
```json
{
  "id": 0,
  "universeId": 0,
  "name": "string",
  "description": "string"
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://develop.roblox.com/v1/places/{PLACEID}" \
  -H "Content-Type: application/json" \
  -d '{
  "name": "string",
  "description": "string"
}'
```

### PATCH `/v1/places/{placeId}`

Updates the place configuration for the place with the id placeId

Currently the only supported functionality for updating the configuration is around Name, and Description.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `placeId` | path | `integer (int64)` | Yes | The place id for the place to be updated. |

**Request Body:** `application/json` — Type: `Roblox.Api.Develop.Models.PlaceConfigurationModel`

See [Roblox.Api.Develop.Models.PlaceConfigurationModel](#roblox-api-develop-models-placeconfigurationmodel) in Models.

**Request example:**
```json
{
  "name": "string",
  "description": "string"
}
```

**Responses:**

- `200`: OK → `Roblox.Api.Develop.Models.PlaceModel`
- `400`: placeId is invalid.
- `401`: 0: Authorization has been denied for this request.
- `403`: Authenticated user is not authorized to manage this place. 0: Token Validation Failed

**Response fields** (`Roblox.Api.Develop.Models.PlaceModel`)

See [Roblox.Api.Develop.Models.PlaceModel](#roblox-api-develop-models-placemodel) in Models.

**Response example:**
```json
{
  "id": 0,
  "universeId": 0,
  "name": "string",
  "description": "string"
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X PATCH -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://develop.roblox.com/v1/places/{PLACEID}" \
  -H "Content-Type: application/json" \
  -d '{
  "name": "string",
  "description": "string"
}'
```

### POST `/v1/universes/{universeId}/activate`

Activates a universes.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer (int64)` | Yes | The universe id. |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: 1: The universe does not exist. 2: This universe does not have a root place.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 3: You are not authorized to configure this universe. 6: The root place for this universe is under review and can not be activated. 7: Creator already has the maximum number of places active.

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://develop.roblox.com/v1/universes/{UNIVERSEID}/activate"
```

### POST `/v1/universes/{universeId}/configuration/playtesters/eligibility`

Check whether each candidate user can currently be added as a private playtester.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer (int64)` | Yes | The universe Id. |

**Request Body:** `application/json` — Type: `Roblox.Api.Develop.Models.PlaytestersRequest`

See [Roblox.Api.Develop.Models.PlaytestersRequest](#roblox-api-develop-models-playtestersrequest) in Models.

**Request example:**
```json
{
  "playtesters": [
    0
  ]
}
```

**Responses:**

- `200`: OK → `Roblox.Api.Develop.Models.PlaytesterEligibilityResponse`
- `400`: 1: The universe does not exist. 48: The playtesters list is missing or empty. 49: Too many playtesters were specified in a single request.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 2: You are not authorized to configure this universe.

**Response fields** (`Roblox.Api.Develop.Models.PlaytesterEligibilityResponse`)

See [Roblox.Api.Develop.Models.PlaytesterEligibilityResponse](#roblox-api-develop-models-playtestereligibilityresponse) in Models.

**Response example:**
```json
{
  "playtesters": [
    {
      "userId": "...",
      "isEligible": "..."
    }
  ]
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://develop.roblox.com/v1/universes/{UNIVERSEID}/configuration/playtesters/eligibility" \
  -H "Content-Type: application/json" \
  -d '{
  "playtesters": [
    0
  ]
}'
```

### POST `/v1/universes/{universeId}/deactivate`

Deactivates a universe.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer (int64)` | Yes | The universe id. |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: 1: The universe does not exist. 2: This universe does not have a root place.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 3: You are not authorized to configure this universe.

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://develop.roblox.com/v1/universes/{UNIVERSEID}/deactivate"
```

### PATCH `/v1/plugins/{pluginId}`

Updates a plugin.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `pluginId` | path | `integer (int64)` | Yes | The id of the plugin. |

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
curl -X PATCH -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://develop.roblox.com/v1/plugins/{PLUGINID}" \
  -H "Content-Type: application/json" \
  -d '{
  "name": "string",
  "description": "string",
  "commentsEnabled": false
}'
```

### DELETE `/v1/universes/{universeId}/teamcreate/memberships`

Removes a user from a TeamCreate permissions list.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer (int64)` | Yes | The universe Id. |

**Request Body:** `application/json` — Type: `Roblox.Api.Develop.Models.TeamCreateMembershipRequest`

See [Roblox.Api.Develop.Models.TeamCreateMembershipRequest](#roblox-api-develop-models-teamcreatemembershiprequest) in Models.

**Request example:**
```json
{
  "userId": 0
}
```

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: Roblox.Api.Develop.ResponseEnums.TeamCreateErrors.InvalidUniverse OR Roblox.Api.Develop.ResponseEnums.TeamCreateErrors.InvalidUser
- `401`: 0: Authorization has been denied for this request.
- `403`: Roblox.Api.Develop.ResponseEnums.TeamCreateErrors.TeamCreateDisabled 0: Token Validation Failed

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X DELETE -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://develop.roblox.com/v1/universes/{UNIVERSEID}/teamcreate/memberships" \
  -H "Content-Type: application/json" \
  -d '{
  "userId": 0
}'
```

## Models

### Roblox.Api.Develop.Models.ActivationEligibilityResponse

The result of various checks for a user's eligibility to activate a given universe from private to public.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `isEligible` | `boolean` | No | The overall result of activation eligibility. This requires the user publish gate and either a maturity rating or an intact Build seal. |
| `maturityRated` | `boolean` | No | Whether the place has an active content maturity rating or not. |
| `isUserEligibleForPublicPublish` | `boolean` | No | isUserEligibleForPublicPublish |
| `remainingPublicPublishCount` | `integer` | No | How many public publishes are remaining for the given user / group. |
| `isPublicPublish` | `boolean` | No | Whether the universe is publicly published or not. |
| `isPublishToExistingUniverse` | `boolean` | No | Whether the universeId is within the tracked list of distinct allowed published universes. |
| `isUniverseSelect` | `boolean` | No | Whether the universe is in the "Select" program. |
| `creatorTier` | `0 \| 1 \| 2 \| 3 \| 4` | No | The creator tier of the universe owner. ['Invalid' = 0, 'Blocked' = 1, 'Private' = 2, 'Trusted' = 3, 'Everyone' = 4] |
| `allowedAudiences` | `0 \| 1 \| 2 \| 3 \| 4[]` | No | Audiences the universe is allowed to be published to. |
| `provisionalRatingAllowed` | `boolean` | No | Whether the universe has a provisional rating via a Build seal in Content Catalog. When true, the universe is eligible for activation even without a full maturity questionnaire. |
| `provisionalRating` | `Roblox.Api.Develop.Models.BuildGeneratedRatingPreviewResponse` | No |  |

### Roblox.Api.Develop.Models.BuildGeneratedRatingPreviewResponse

The complete build-generated rating preview returned by Experience Guidelines.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `ageRecommendationDetails` | `Roblox.Api.Develop.Models.BuildGeneratedRatingPreviewResponse.AgeRecommendationDetailsModel` | No |  |
| `restrictedCountries` | `Roblox.Api.Develop.Models.BuildGeneratedRatingPreviewResponse.RestrictedCountryModel[]` | No | Country-specific restrictions produced by the preview. |

### Roblox.Api.Develop.Models.BuildGeneratedRatingPreviewResponse.AgeRangeModel

Age range for a descriptor usage.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `minAgeInclusive` | `integer` | No | Inclusive minimum age. |
| `maxAgeInclusive` | `integer` | No | Inclusive maximum age. |

### Roblox.Api.Develop.Models.BuildGeneratedRatingPreviewResponse.AgeRecommendationDetailsModel

Age recommendation details.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `ageRecommendationSummary` | `Roblox.Api.Develop.Models.BuildGeneratedRatingPreviewResponse.AgeRecommendationSummaryModel` | No |  |
| `experienceDescriptorUsages` | `Roblox.Api.Develop.Models.BuildGeneratedRatingPreviewResponse.ExperienceDescriptorUsageModel[]` | No | Descriptor usages that contributed to the recommendation. |

### Roblox.Api.Develop.Models.BuildGeneratedRatingPreviewResponse.AgeRecommendationModel

Age recommendation.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `displayName` | `string` | No | Localized display name. |
| `minimumAge` | `integer` | No | Minimum recommended age. |
| `displayNameWithHeaderShort` | `string` | No | Localized short display name including the maturity header. |
| `minimumAgeDisplay` | `string` | No | Localized minimum-age display value. |
| `contentMaturity` | `string` | No | Explicit content maturity value. |
| `igrsRating` | `string` | No | IGRS rating enum name, when present. |
| `igrsRatingDisplayMessage` | `string` | No | Localized IGRS rating display message, when present. |

### Roblox.Api.Develop.Models.BuildGeneratedRatingPreviewResponse.AgeRecommendationSummaryModel

Age recommendation summary.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `ageRecommendation` | `Roblox.Api.Develop.Models.BuildGeneratedRatingPreviewResponse.AgeRecommendationModel` | No |  |

### Roblox.Api.Develop.Models.BuildGeneratedRatingPreviewResponse.ExperienceDescriptorDimensionUsageModel

Descriptor dimension usage.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `dimensionName` | `string` | No | Dimension name. |
| `dimensionValue` | `string` | No | Dimension value. |

### Roblox.Api.Develop.Models.BuildGeneratedRatingPreviewResponse.ExperienceDescriptorModel

Experience descriptor definition.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | `string` | No | Descriptor name. |
| `displayName` | `string` | No | Localized descriptor display name. |
| `complianceApiSupported` | `boolean` | No | Whether the descriptor is supported by the Compliance API. |
| `iconUrl` | `string` | No | Descriptor icon URL. |

### Roblox.Api.Develop.Models.BuildGeneratedRatingPreviewResponse.ExperienceDescriptorUsageModel

A descriptor usage that contributed to a recommendation.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | `string` | No | Descriptor usage name. |
| `followsComplianceApi` | `boolean` | No | Whether this usage follows the Compliance API, when specified. |
| `experienceDescriptor` | `Roblox.Api.Develop.Models.BuildGeneratedRatingPreviewResponse.ExperienceDescriptorModel` | No |  |
| `experienceDescriptorDimensionUsages` | `Roblox.Api.Develop.Models.BuildGeneratedRatingPreviewResponse.ExperienceDescriptorDimensionUsageModel[]` | No | Dimensions associated with this usage. |
| `contains` | `boolean` | No | Whether the experience contains this descriptor. |
| `ageRange` | `Roblox.Api.Develop.Models.BuildGeneratedRatingPreviewResponse.AgeRangeModel` | No |  |
| `descriptorDisplayName` | `string` | No | Localized descriptor display name. |
| `ageRangeDisplayName` | `string` | No | Localized age-range display name. |

### Roblox.Api.Develop.Models.BuildGeneratedRatingPreviewResponse.RestrictedCountryModel

Country-specific restrictions.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `countryCode` | `string` | No | ISO country code. |
| `experienceDescriptorUsages` | `Roblox.Api.Develop.Models.BuildGeneratedRatingPreviewResponse.ExperienceDescriptorUsageModel[]` | No | Descriptor usages responsible for the restriction. |
| `countryDisplayName` | `string` | No | Localized country display name. |

### Roblox.Api.Develop.Models.GameTemplateModel

Represents a game template in API endpoint responses.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `gameTemplateType` | `string` | No | The type of this game template. |
| `hasTutorials` | `boolean` | No | Whether this game template has tutorials. |
| `universe` | `Roblox.Api.Develop.Models.UniverseModel` | No |  |

### Roblox.Api.Develop.Models.GroupModel

A model containing information about a group

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | `integer` | No | The Roblox.Platform.Groups.IGroup's Id. |
| `name` | `string` | No | The Roblox.Platform.Groups.IGroup's name. |

### Roblox.Api.Develop.Models.PlaceConfigurationModel

A model containing information about a place to be configured

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | `string` | No | The name for the place. |
| `description` | `string` | No | The new description for the place. |

### Roblox.Api.Develop.Models.PlaceModel

A model containing information about a place

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | `integer` | No | Returns the place id. |
| `universeId` | `integer` | No | Returns the id of the place's universe, or null - if the place is not part of a universe. |
| `name` | `string` | No | Returns the place name. |
| `description` | `string` | No | Returns the place description. |

### Roblox.Api.Develop.Models.PlaytesterEligibility

Whether one candidate user can currently be added as a private playtester.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `userId` | `integer` | No | The candidate user id. |
| `isEligible` | `boolean` | No | Whether the candidate is eligible. |

### Roblox.Api.Develop.Models.PlaytesterEligibilityResponse

Per-user add eligibility for private playtester candidates.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `playtesters` | `Roblox.Api.Develop.Models.PlaytesterEligibility[]` | No | The per-user eligibility results. |

### Roblox.Api.Develop.Models.PlaytestersRequest

Request model for adding or removing playtesters.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `playtesters` | `integer[]` | No | The user ids to add or remove as playtesters for this universe. |

### Roblox.Api.Develop.Models.PlaytestersResponse

Response model for playtester list endpoints.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `playtesters` | `integer[]` | No | The user ids that are playtesters for this universe. |

### Roblox.Api.Develop.Models.PrivateServerDetailsResponse

Model for private server details responses from the UniverseSettings controller.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `isEnabled` | `boolean` | No | Whether or not VIP servers are enabled on this universe. |
| `price` | `integer` | No | The price of the VIP server. |
| `activeServersCount` | `integer` | No | The number of active VIP servers for this universe. A negative value indicates at least this many exist (i.e. -100 means 100+ active private servers). |
| `activeSubscriptionsCount` | `integer` | No | The number of active VIP server subscriptions. A negative value indicates at least this many exist (i.e. -100 means 100+ active subscriptions). |

### Roblox.Api.Develop.Models.Response.AssetVotingModel

Asset voting information

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `assetId` | `integer` | No | The !:IAsset's id. |
| `hasUserVoted` | `boolean` | No | Whether the user has voted on this !:IAsset. |
| `canUserVote` | `boolean` | No | Whether the user can vote on this !:IAsset. |
| `shouldShowVotes` | `boolean` | No | Whether votes should be shown. |
| `upVotes` | `integer` | No | The number of up votes. |
| `downVotes` | `integer` | No | The number of down votes. |
| `reasonForNotAbleToVote` | `string` | No | The reason this !:IAsset cannot be voted on. |

### Roblox.Api.Develop.Models.Response.TeamCreateSettingsResponse

Team create settings

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `isEnabled` | `boolean` | No | Whether or not the universe should be enabled for team create |

### Roblox.Api.Develop.Models.TeamCreateMembershipRequest

Request model for a TeamCreate membership

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `userId` | `integer` | No | The id of the user. |

### Roblox.Api.Develop.Models.UniverseIdPermissionsModel

A model containing information about a universe permissions

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `universeId` | `integer` | No | The universe Id these permissions reference |
| `canManage` | `boolean` | No | Determines whether or not consumer can manage the target universe |
| `canCloudEdit` | `boolean` | No | Determines whether or not consumer can cloud the target universe This is only nullable/optional in the context of https://develop.roblox.com/docs#!/Universes/get_v1_universes_universeId_context_permissions endpoint which is consumed only internally. It should be computed and set for all other usages. |

### Roblox.Api.Develop.Models.UniverseModel

Represents a universe in API endpoint results.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | `integer` | No | The universe Id. |
| `name` | `string` | No | The name of the universe |
| `description` | `string` | No | The description of the universe |
| `isArchived` | `boolean` | No | Is this universe archived |
| `rootPlaceId` | `integer` | No | The universe's root place id |
| `isActive` | `boolean` | No | Is this universe active |
| `privacyType` | `string` | No | The universe's privacy type. |
| `creatorType` | `string` | No | The creator type, either "User" or "Group" |
| `creatorTargetId` | `integer` | No | The id of the user or group that created this universe. |
| `creatorName` | `string` | No | The name of the creator of the universe. |
| `created` | `string` | No | The created System.DateTime |
| `updated` | `string` | No | The updated System.DateTime |
| `audiences` | `0 \| 1 \| 2 \| 3 \| 4[]` | No | The audiences this universe is visible to (e.g. Editors, PlayTesters, Friends, Public). Always non-null; may be empty when audience visibility has not been configured. |

### Roblox.Api.Develop.Models.UniversePermissionsModel

A model containing information about a universe permissions

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `canManage` | `boolean` | No | Determines whether or not consumer can manage the target universe |
| `canCloudEdit` | `boolean` | No | Determines whether or not consumer can cloud the target universe This is only nullable/optional in the context of https://develop.roblox.com/docs#!/Universes/get_v1_universes_universeId_context_permissions endpoint which is consumed only internally. It should be computed and set for all other usages. |

### Roblox.Api.Develop.Models.UniverseSettingsRequest

Model for UniverseSettings patch requests

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | `string` | No | The name of the universe. |
| `universeAvatarType` | `1 \| 2 \| 3` | No | Which avatar types are allowed in the universe. |
| `universeScaleType` | `1 \| 2` | No | Whether custom scales allowed in the universe. |
| `universeAnimationType` | `1 \| 2` | No | Whether custom animations are allowed in the universe. |
| `universeCollisionType` | `1 \| 2` | No | What type of collisions are used by the universe. |
| `universeBodyType` | `1 \| 2` | No | What avatar body types are allowed by the universe. |
| `universeJointPositioningType` | `1 \| 2` | No | What avatar joint positioning type is allowed by the universe. |
| `isArchived` | `boolean` | No | Archive status of the universe. |
| `isFriendsOnly` | `boolean` | No | Whether game access is limited to friends for user-owned games or group members for group-owned games. |
| `genre` | `integer enum (15 values)` | No | Game genre. Values: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 |
| `playableDevices` | `integer enum (6 values)[]` | No | List of device types this game can be played on. |
| `isForSale` | `boolean` | No | Whether the game is offered for sale. |
| `price` | `integer` | No | Price of the game, in Robux. |
| `isMeshTextureApiAccessAllowed` | `boolean` | No | Sets whether access to APIs for mesh and texture is enabled for this universe. |
| `isRewardedOnDemandAdsAllowed` | `boolean` | No | Set is rewarded on-demand ads are allowed for this universe. |
| `fiatBasePriceId` | `string` | No | Sets the base price of the experience for Fiat purchases. |
| `fiatProductChangeType` | `0 \| 1 \| 2 \| 3` | No | Determines the change type of the Fiat Product Change request. Can either Activate the product, Update the price, or Deactivate the product. |
| `demoModeEnabled` | `boolean` | No | Whether demo mode is enabled for this paid access game. |

### Roblox.Api.Develop.Models.UniverseSettingsResponse

Model for UniverseSettings controller responses

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `allowPrivateServers` | `boolean` | No | If the universe allows the use of private servers. |
| `privateServerPrice` | `integer` | No | The price to purchase a private server in robux. |
| `isMeshTextureApiAccessAllowed` | `boolean` | No | Whether access to APIs for mesh and texture is enabled for this universe. |
| `isRewardedOnDemandAdsAllowed` | `boolean` | No | Whether rewarded on-demand ads are allowed for this universe. |
| `id` | `integer` | No | The universe Id. |
| `name` | `string` | No | The universe name. |
| `promotionalText` | `string` | No | Promotional Text for the universe. |
| `universeAvatarType` | `1 \| 2 \| 3` | No | Which avatar types are allowed in the universe. ['MorphToR6' = 1, 'PlayerChoice' = 2, 'MorphToR15' = 3] |
| `universeScaleType` | `1 \| 2` | No | Whether custom scales allowed in the universe. ['NoScales' = 1, 'AllScales' = 2] |
| `universeAnimationType` | `1 \| 2` | No | Whether custom animations are allowed in the universe. ['Standard' = 1, 'PlayerChoice' = 2] |
| `universeCollisionType` | `1 \| 2` | No | What type of collisions are used by the universe. ['InnerBox' = 1, 'OuterBox' = 2] |
| `universeBodyType` | `1 \| 2` | No | What avatar body types are allowed by the universe. ['Standard' = 1, 'PlayerChoice' = 2] |
| `universeJointPositioningType` | `1 \| 2` | No | What avatar joint positioning is allowed by the universe. ['Standard' = 1, 'ArtistIntent' = 2] |
| `isArchived` | `boolean` | No | Archive status of the universe |
| `isFriendsOnly` | `boolean` | No | Whether game access is limited to friends for user-owned games or group members for group-owned games. |
| `genre` | `integer enum (15 values)` | No | Game genre. ['All' = 0, 'Tutorial' = 1, 'Scary' = 2, 'TownAndCity' = 3, 'War' = 4, 'Funny' = 5, 'Fantasy' = 6, 'Adventure' = 7, 'SciFi' = 8, 'Pirate' = 9, 'FPS' = 10, 'RPG' = 11, 'Sports' = 12, 'Ninja' = 13, 'WildWest' = 14] Values: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 |
| `playableDevices` | `integer enum (6 values)[]` | No | List of device types this game can be played on. |
| `isForSale` | `boolean` | No | Whether the game is offered for sale. |
| `price` | `integer` | No | Price of the game, in Robux. |
| `isStudioAccessToApisAllowed` | `boolean` | No | Whether studio access to APIs is allowed or not. |
| `privacyType` | `string` | No | Privacy type of the universe. |
| `isForSaleInFiat` | `boolean` | No | Whether the game is offered for sale in fiat. |
| `fiatBasePriceId` | `string` | No | The basePriceId for the Fiat product. |
| `fiatModerationStatus` | `0 \| 1 \| 2 \| 3 \| 4` | No | The current moderation status of the game if it is for sale in fiat. ['Invalid' = 0, 'NotModerated' = 1, 'Pending' = 2, 'Approved' = 3, 'Rejected' = 4] |
| `audiences` | `0 \| 1 \| 2 \| 3 \| 4[]` | No | The audiences this universe is visible to (e.g. Editors, PlayTesters, Friends, Public). Always non-null; may be empty when audience visibility has not been configured. |
| `demoModeEnabled` | `boolean` | No | Whether demo mode is enabled. |
| `demoModeChangeableAfter` | `string` | No | The earliest time at which demo mode can be toggled again (ISO 8601). Null when no cooldown is active (i.e. demo mode can be changed immediately). |

### Roblox.Api.Develop.Models.UniverseTeamCreateSettingsModel

Team create settings of a universe

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | `integer` | No | Id of the universe. |
| `isEnabled` | `boolean` | No | Whether or not the universe is enabled for team create |

### Roblox.Api.Develop.Models.UpdateTeamCreateSettingsRequest

Team create settings request

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `isEnabled` | `boolean` | No | Whether or not the universe should be enabled for team create |

### Roblox.Api.Develop.Models.UserPublicPublishEligibilityResponse

The result of various checks for a user's eligibility to publish a public universe.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `isEligible` | `boolean` | No | The overall result of eligibility. |
| `hasTransactions` | `0 \| 1 \| 2` | No | Whether user has spent any Robux since 1/1/25, including gift cards. ['Incomplete' = 0, 'NotRequired' = 1, 'Completed' = 2] |
| `idVerified` | `0 \| 1 \| 2` | No | Whether user has completed ID Verification or not. ['Incomplete' = 0, 'NotRequired' = 1, 'Completed' = 2] |
| `hasDevex` | `0 \| 1 \| 2` | No | Whether user is eligible for the developer exchange program. ['Incomplete' = 0, 'NotRequired' = 1, 'Completed' = 2] |

### Roblox.Develop.Api.UpdatePluginRequest

A request model for updating a plugin.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | `string` | No | The new plugin name. |
| `description` | `string` | No | The new plugin description. |
| `commentsEnabled` | `boolean` | No | Whether or not comments should be enabled. |

### Roblox.Web.Responses.Plugins.PluginResponse

Represents information about a plugin.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | `integer` | No | The plugin Id. |
| `name` | `string` | No | The plugin name. |
| `description` | `string` | No | The plugin description. |
| `commentsEnabled` | `boolean` | No | Whether or not the plugin allows comments to be posted. |
| `versionId` | `integer` | No | plugin version id |
| `created` | `string` | No | The time the plugin was created. |
| `updated` | `string` | No | The last time the plugin was updated. |

### Roblox.Web.Responses.Users.SkinnyUserResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | `integer` | No |  |
| `name` | `string` | No |  |
| `displayName` | `string` | No |  |

### Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.Api.Develop.Models.GameTemplateModel]

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | `Roblox.Api.Develop.Models.GameTemplateModel[]` | No |  |

### Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.Api.Develop.Models.GroupModel]

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | `Roblox.Api.Develop.Models.GroupModel[]` | No |  |

### Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.Api.Develop.Models.Response.AssetVotingModel]

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | `Roblox.Api.Develop.Models.Response.AssetVotingModel[]` | No |  |

### Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.Api.Develop.Models.UniverseIdPermissionsModel]

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | `Roblox.Api.Develop.Models.UniverseIdPermissionsModel[]` | No |  |

### Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.Api.Develop.Models.UniverseModel]

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | `Roblox.Api.Develop.Models.UniverseModel[]` | No |  |

### Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.Api.Develop.Models.UniverseTeamCreateSettingsModel]

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | `Roblox.Api.Develop.Models.UniverseTeamCreateSettingsModel[]` | No |  |

### Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.Web.Responses.Plugins.PluginResponse]

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | `Roblox.Web.Responses.Plugins.PluginResponse[]` | No |  |

### Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.Web.Responses.Users.SkinnyUserResponse]

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | `Roblox.Web.Responses.Users.SkinnyUserResponse[]` | No |  |

### Roblox.Web.WebAPI.Models.ApiPageResponse[Roblox.Api.Develop.Models.IPlaceModel]

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `previousPageCursor` | `string` | No |  |
| `nextPageCursor` | `string` | No |  |
| `data` | `Roblox.Api.Develop.Models.IPlaceModel[]` | No |  |

### Roblox.Web.WebAPI.Models.ApiPageResponse[Roblox.Api.Develop.Models.UniverseModel]

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `previousPageCursor` | `string` | No |  |
| `nextPageCursor` | `string` | No |  |
| `data` | `Roblox.Api.Develop.Models.UniverseModel[]` | No |  |