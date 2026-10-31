---
name: "Games Api v2"
last_updated: 2026-10-30T19:56:08Z
type: legacy
api_base_url: "https://games.roblox.com"
versions: [v2, v1]
endpoints: 12
auth: [cookie]
---

# Games Api v2

> **Warning:** Legacy APIs with cookie authentication can incorporate breaking changes without notice. We don't recommend them for production applications.

**Base URL:** `https://games.roblox.com`
**Versions:** v2, v1

## V2

### GET `/v2/games/{universeId}/media`

Get the game media data

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer (int64)` | Yes | The id of the universe we get media data from. |
| `fetchAllExperienceRelatedMedia` | query | `boolean` | No | to tell if the API query is to fetch all related media for this experience |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.Web.Responses.Games.GameMediaItemResponseV2]`
- `400`: 3: The universe's root place is invalid.
- `404`: 2: The requested universe does not exist.

**Response fields** (`Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.Web.Responses.Games.GameMediaItemResponseV2]`)

See [Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.Web.Responses.Games.GameMediaItemResponseV2]](#roblox-web-webapi-models-apiarrayresponse-roblox-web-responses-games-gamemediaitemresponsev2-) in Models.

**Response example:**
```json
{
  "data": [
    {
      "assetTypeId": "...",
      "assetType": "...",
      "imageId": "...",
      "videoHash": "...",
      "videoTitle": "...",
      "approved": "..."
    }
  ]
}
```

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://games.roblox.com/v2/games/{UNIVERSEID}/media"
```

### GET `/v2/users/{userId}/favorite/games`

Gets users favorite games.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer (int64)` | Yes | The user Id. |
| `accessFilter` | query | `integer (int32)` | No | Filtering option via access level. Valid values: `1`, `2`, `4` |
| `limit` | query | `integer (int32)` | No | The number of results per request. Valid values: `10`, `25`, `50`, `100` |
| `cursor` | query | `string` | No | The paging cursor for the previous or next page. |
| `sortOrder` | query | `string` | No | The order the results are sorted in. Valid values: `Asc`, `Desc` |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiPageResponse[Roblox.Web.Responses.Games.GameFavoriteResponseModel]`

**Response fields** (`Roblox.Web.WebAPI.Models.ApiPageResponse[Roblox.Web.Responses.Games.GameFavoriteResponseModel]`)

See [Roblox.Web.WebAPI.Models.ApiPageResponse[Roblox.Web.Responses.Games.GameFavoriteResponseModel]](#roblox-web-webapi-models-apipageresponse-roblox-web-responses-games-gamefavoriteresponsemodel-) in Models.

**Response example:**
```json
{
  "previousPageCursor": "string",
  "nextPageCursor": "string",
  "data": [
    {
      "price": "...",
      "contentMetadata": "...",
      "id": "...",
      "name": "...",
      "description": "...",
      "creator": "..."
    }
  ]
}
```

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://games.roblox.com/v2/users/{USERID}/favorite/games"
```

### GET `/v2/users/{userId}/games`

Gets games created by the specified user.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer (int64)` | Yes | The user Id. |
| `accessFilter` | query | `integer (int32)` | No | Filtering option via access level. Valid values: `1`, `2`, `4` |
| `limit` | query | `integer (int32)` | No | The number of results per request. Valid values: `10`, `25`, `50` |
| `cursor` | query | `string` | No | The paging cursor for the previous or next page. |
| `sortOrder` | query | `string` | No | The order the results are sorted in. Valid values: `Asc`, `Desc` |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiPageResponse[Roblox.Web.Responses.Games.GameResponseV2]`

**Response fields** (`Roblox.Web.WebAPI.Models.ApiPageResponse[Roblox.Web.Responses.Games.GameResponseV2]`)

See [Roblox.Web.WebAPI.Models.ApiPageResponse[Roblox.Web.Responses.Games.GameResponseV2]](#roblox-web-webapi-models-apipageresponse-roblox-web-responses-games-gameresponsev2-) in Models.

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
      "creator": "...",
      "rootPlace": "...",
      "created": "..."
    }
  ]
}
```

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://games.roblox.com/v2/users/{USERID}/games"
```

## Models

### Roblox.Games.Api.Models.Response.GameContentMetadataResponseModel

Response model for game-level content metadata.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `badgePosition` | `string` | No |  |
| `badgeAnalyticsId` | `string` | No |  |
| `badgeType` | `string` | No |  |
| `badgeIcon` | `string` | No |  |
| `badgeComponentType` | `string` | No |  |

### Roblox.Web.Responses.Games.GameFavoriteResponseModel

Response model representing a user's favorited game.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `price` | `integer` | No | The game paid access price in robux. Given that there is no actual owner for this product surface, we will keep existing behavior where we display offsale for games priced in fiat currency. |
| `contentMetadata` | `Roblox.Games.Api.Models.Response.GameContentMetadataResponseModel` | No |  |
| `id` | `integer` | No | The game (universe) Id. |
| `name` | `string` | No | The game name. |
| `description` | `string` | No | The game description. |
| `creator` | `Roblox.Web.Responses.RelatedEntityTypeResponse[Roblox.Platform.Core.CreatorType]` | No |  |
| `rootPlace` | `Roblox.Web.Responses.RelatedEntityTypeResponse[Roblox.Platform.Assets.AssetType]` | No |  |
| `created` | `string` | No | When the game was created. |
| `updated` | `string` | No | When the game was last updated. |
| `placeVisits` | `integer` | No | The number of place visits for this game. |

### Roblox.Web.Responses.Games.GameMediaItemResponseV2

Response model for getting the game media item

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `assetTypeId` | `integer` | No | The media item type id |
| `assetType` | `string` | No | The media item type, Image or YouTubeVideo |
| `imageId` | `integer` | No | The media item image id |
| `videoHash` | `string` | No | The media item video hash |
| `videoTitle` | `string` | No | The video title for video items. |
| `approved` | `boolean` | No | The media item is approved or not |
| `altText` | `string` | No | The media item alt text |
| `videoId` | `string` | No | The video asset ID |

### Roblox.Web.Responses.Games.GameResponseV2

A response model representing a game.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | `integer` | No | The game (universe) Id. |
| `name` | `string` | No | The game name. |
| `description` | `string` | No | The game description. |
| `creator` | `Roblox.Web.Responses.RelatedEntityTypeResponse[Roblox.Platform.Core.CreatorType]` | No |  |
| `rootPlace` | `Roblox.Web.Responses.RelatedEntityTypeResponse[Roblox.Platform.Assets.AssetType]` | No |  |
| `created` | `string` | No | When the game was created. |
| `updated` | `string` | No | When the game was last updated. |
| `placeVisits` | `integer` | No | The number of place visits for this game. |

### Roblox.Web.Responses.RelatedEntityTypeResponse[Roblox.Platform.Assets.AssetType]

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | `integer` | No |  |
| `type` | `integer enum (87 values)` | No | ['Image' = 1, 'TShirt' = 2, 'Audio' = 3, 'Mesh' = 4, 'Lua' = 5, 'HTML' = 6, 'Text' = 7, 'Hat' = 8, 'Place' = 9, 'Model' = 10, 'Shirt' = 11, 'Pants' = 12, 'Decal' = 13, 'Avatar' = 16, 'Head' = 17, 'Face' = 18, 'Gear' = 19, 'Badge' = 21, 'GroupEmblem' = 22, 'Animation' = 24, 'Arms' = 25, 'Legs' = 26, 'Torso' = 27, 'RightArm' = 28, 'LeftArm' = 29, 'LeftLeg' = 30, 'RightLeg' = 31, 'Package' = 32, 'YouTubeVideo' = 33, 'GamePass' = 34, 'App' = 35, 'Code' = 37, 'Plugin' = 38, 'SolidModel' = 39, 'MeshPart' = 40, 'HairAccessory' = 41, 'FaceAccessory' = 42, 'NeckAccessory' = 43, 'ShoulderAccessory' = 44, 'FrontAccessory' = 45, 'BackAccessory' = 46, 'WaistAccessory' = 47, 'ClimbAnimation' = 48, 'DeathAnimation' = 49, 'FallAnimation' = 50, 'IdleAnimation' = 51, 'JumpAnimation' = 52, 'RunAnimation' = 53, 'SwimAnimation' = 54, 'WalkAnimation' = 55, 'PoseAnimation' = 56, 'LocalizationTableManifest' = 59, 'LocalizationTableTranslation' = 60, 'EmoteAnimation' = 61, 'Video' = 62, 'TexturePack' = 63, 'TShirtAccessory' = 64, 'ShirtAccessory' = 65, 'PantsAccessory' = 66, 'JacketAccessory' = 67, 'SweaterAccessory' = 68, 'ShortsAccessory' = 69, 'LeftShoeAccessory' = 70, 'RightShoeAccessory' = 71, 'DressSkirtAccessory' = 72, 'FontFamily' = 73, 'FontFace' = 74, 'MeshHiddenSurfaceRemoval' = 75, 'EyebrowAccessory' = 76, 'EyelashAccessory' = 77, 'MoodAnimation' = 78, 'DynamicHead' = 79, 'CodeSnippet' = 80, 'AdsVideo' = 81, 'OtaUpdate' = 82, 'Screenshot' = 83, 'RuntimePropertySet' = 84, 'StorePreviewVideo' = 85, 'GamePreviewVideo' = 86, 'CreatorExperienceConfig' = 87, 'FaceMakeup' = 88, 'LipMakeup' = 89, 'EyeMakeup' = 90, 'VoxelFragment' = 91, 'AvatarBackground' = 92, 'TextDocument' = 93, 'Post' = 94] Values: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 16, 17, 18, 19, 21, 22, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94 |
| `name` | `string` | No |  |

### Roblox.Web.Responses.RelatedEntityTypeResponse[Roblox.Platform.Core.CreatorType]

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | `integer` | No |  |
| `type` | `0 \| 1` | No | ['User' = 0, 'Group' = 1] |
| `name` | `string` | No |  |

### Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.Web.Responses.Games.GameMediaItemResponseV2]

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | `Roblox.Web.Responses.Games.GameMediaItemResponseV2[]` | No |  |

### Roblox.Web.WebAPI.Models.ApiPageResponse[Roblox.Web.Responses.Games.GameFavoriteResponseModel]

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `previousPageCursor` | `string` | No |  |
| `nextPageCursor` | `string` | No |  |
| `data` | `Roblox.Web.Responses.Games.GameFavoriteResponseModel[]` | No |  |

### Roblox.Web.WebAPI.Models.ApiPageResponse[Roblox.Web.Responses.Games.GameResponseV2]

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `previousPageCursor` | `string` | No |  |
| `nextPageCursor` | `string` | No |  |
| `data` | `Roblox.Web.Responses.Games.GameResponseV2[]` | No |  |

## V1

### GET `/v1/games`

Gets a list of games' detail

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeIds` | query | `array` | Yes | A list of universe Ids. Cannot exceed a maximum of 50 IDs. |
| `fields` | query | `string` | No | Optional comma-separated list of field names to include in the response. When omitted, all fields are returned. |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.Games.Api.Models.Response.GameDetailResponse]`
- `400`: 8: The universe IDs specified are invalid. 9: Too many universe IDs were requested.
- `429`: 4: Too many requests have been made.

**Response fields** (`Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.Games.Api.Models.Response.GameDetailResponse]`)

See [Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.Games.Api.Models.Response.GameDetailResponse]](#roblox-web-webapi-models-apiarrayresponse-roblox-games-api-models-response-gamedetailresponse-) in Models.

**Response example:**
```json
{
  "data": [
    {
      "id": "...",
      "rootPlaceId": "...",
      "name": "...",
      "description": "...",
      "sourceName": "...",
      "sourceDescription": "..."
    }
  ]
}
```

**Error handling:** `429`: Retry with exponential backoff (start at 1s). 

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://games.roblox.com/v1/games?universeIds={VALUE}"
```

### GET `/v1/games/{universeId}/favorites`

Returns if a game was marked as favorite for the authenticated user

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer (int64)` | Yes | The Id of the universe. |

**Responses:**

- `200`: OK → `Roblox.Games.Api.Models.Response.GameFavoriteResponse`
- `400`: 3: The universe's root place is invalid.
- `401`: 0: Authorization has been denied for this request.
- `404`: 2: The requested universe does not exist.

**Response fields** (`Roblox.Games.Api.Models.Response.GameFavoriteResponse`)

See [Roblox.Games.Api.Models.Response.GameFavoriteResponse](#roblox-games-api-models-response-gamefavoriteresponse) in Models.

**Response example:**
```json
{
  "isFavorited": false
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://games.roblox.com/v1/games/{UNIVERSEID}/favorites"
```

### POST `/v1/games/{universeId}/favorites`

Favors (or unfavors) a game for the authenticated user

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer (int64)` | Yes | The Id of the universe. |

**Request Body:** `application/json` — Type: `Roblox.Games.Api.Models.Request.GameFavoritesRequest`

See [Roblox.Games.Api.Models.Request.GameFavoritesRequest](#roblox-games-api-models-request-gamefavoritesrequest) in Models.

**Request example:**
```json
{
  "isFavorited": false
}
```

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: 3: The universe's root place is invalid.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 11: You are not authorized to perform this action.
- `404`: 2: The requested universe does not exist.
- `429`: 4: Too many requests have been made.

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `429`: Retry with exponential backoff (start at 1s). `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://games.roblox.com/v1/games/{UNIVERSEID}/favorites" \
  -H "Content-Type: application/json" \
  -d '{
  "isFavorited": false
}'
```

### GET `/v1/games/{universeId}/favorites/count`

Get the favorites count of a specific game.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer (int64)` | Yes | The Id of the universe. |

**Responses:**

- `200`: OK → `Roblox.Games.Api.Models.Response.GameFavoritesCountResponse`
- `400`: 3: The universe's root place is invalid.
- `404`: 2: The requested universe does not exist.

**Response fields** (`Roblox.Games.Api.Models.Response.GameFavoritesCountResponse`)

See [Roblox.Games.Api.Models.Response.GameFavoritesCountResponse](#roblox-games-api-models-response-gamefavoritescountresponse) in Models.

**Response example:**
```json
{
  "favoritesCount": 0
}
```

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://games.roblox.com/v1/games/{UNIVERSEID}/favorites/count"
```

### GET `/v1/games/{universeId}/media` *(deprecated)*

Get the game media data

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer (int64)` | Yes | The id of the universe we get media data from. |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.Games.Api.Models.Response.GameMediaItem]`
- `400`: 3: The universe's root place is invalid.
- `404`: 2: The requested universe does not exist.

**Response fields** (`Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.Games.Api.Models.Response.GameMediaItem]`)

See [Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.Games.Api.Models.Response.GameMediaItem]](#roblox-web-webapi-models-apiarrayresponse-roblox-games-api-models-response-gamemediaitem-) in Models.

**Response example:**
```json
{
  "data": [
    {
      "id": "...",
      "assetTypeId": "...",
      "assetType": "...",
      "imageId": "...",
      "videoHash": "...",
      "videoTitle": "..."
    }
  ]
}
```

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://games.roblox.com/v1/games/{UNIVERSEID}/media"
```

### GET `/v1/games/games-product-info`

Gets a list of games' product info, used to purchase a game

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeIds` | query | `array` | Yes | A list of universe Ids. Cannot exceed a maximum of 100 IDs. |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.Games.Api.Models.Response.GameProductResponse]`
- `400`: 8: The universe IDs specified are invalid. 9: Too many universe IDs were requested.

**Response fields** (`Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.Games.Api.Models.Response.GameProductResponse]`)

See [Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.Games.Api.Models.Response.GameProductResponse]](#roblox-web-webapi-models-apiarrayresponse-roblox-games-api-models-response-gameproductresponse-) in Models.

**Response example:**
```json
{
  "data": [
    {
      "universeId": "...",
      "isForSale": "...",
      "productId": "...",
      "price": "...",
      "sellerId": "...",
      "fiatPurchaseData": "..."
    }
  ]
}
```

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://games.roblox.com/v1/games/games-product-info?universeIds={VALUE}"
```

### GET `/v1/games/multiget-place-details`

Get place details

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `placeIds` | query | `array` | Yes | List of placeId to uniquely Identify a place |

**Responses:**

- `200`: OK → `Roblox.Games.Api.Models.Response.PlaceDetails[]`
- `401`: 0: Authorization has been denied for this request.

**Response fields** (`Roblox.Games.Api.Models.Response.PlaceDetails[]`)

See [Roblox.Games.Api.Models.Response.PlaceDetails](#roblox-games-api-models-response-placedetails) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://games.roblox.com/v1/games/multiget-place-details?placeIds={VALUE}"
```

### GET `/v1/games/multiget-playability-status`

Gets a list of universe playability statuses for the authenticated user

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeIds` | query | `array` | Yes | A list of universe Ids. Cannot exceed a maximum of 50 IDs. |

**Responses:**

- `200`: OK → `Roblox.Games.Api.Models.Response.PlayabilityStatusResponse[]`
- `400`: 8: The universe IDs specified are invalid. 9: Too many universe IDs were requested.
- `429`: 4: Too many requests have been made.

**Response fields** (`Roblox.Games.Api.Models.Response.PlayabilityStatusResponse[]`)

See [Roblox.Games.Api.Models.Response.PlayabilityStatusResponse](#roblox-games-api-models-response-playabilitystatusresponse) in Models.

**Error handling:** `429`: Retry with exponential backoff (start at 1s). 

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://games.roblox.com/v1/games/multiget-playability-status?universeIds={VALUE}"
```

### GET `/v1/games/recommendations/game/{universeId}`

Get games recommendations based on a given universe

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer (int64)` | Yes | The universe to base recommendations on |
| `PaginationKey` | query | `string` | Yes | The key of a page, which includes the start row index and all other necessary information to query the data. This parameter is usually not needed for the first page. |
| `MaxRows` | query | `integer (int32)` | Yes | The requested number of rows. |
| `IsTruncatedResultsEnabled` | query | `boolean` | Yes | Truncated Results |

**Responses:**

- `200`: OK → `Roblox.Games.Api.Models.Response.GameRecommendationsResponse`
- `400`: 1: The pagination key is invalid.
- `404`: 2: The requested universe does not exist.

**Response fields** (`Roblox.Games.Api.Models.Response.GameRecommendationsResponse`)

See [Roblox.Games.Api.Models.Response.GameRecommendationsResponse](#roblox-games-api-models-response-gamerecommendationsresponse) in Models.

**Response example:**
```json
{
  "games": [
    {
      "creatorId": "...",
      "creatorName": "...",
      "creatorType": "...",
      "creatorHasVerifiedBadge": "...",
      "totalUpVotes": "...",
      "totalDownVotes": "..."
    }
  ],
  "nextPaginationKey": "string"
}
```

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://games.roblox.com/v1/games/recommendations/game/{UNIVERSEID}?PaginationKey={VALUE}&MaxRows={VALUE}&IsTruncatedResultsEnabled={VALUE}"
```

## Models

### Roblox.Games.Api.Models.Request.GameFavoritesRequest

Game favorite request model.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `isFavorited` | `boolean` | No | true for favor the game, false for unfavor the game. |

### Roblox.Games.Api.Models.Response.GameContentMetadataResponseModel

Response model for game-level content metadata.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `badgePosition` | `string` | No |  |
| `badgeAnalyticsId` | `string` | No |  |
| `badgeType` | `string` | No |  |
| `badgeIcon` | `string` | No |  |
| `badgeComponentType` | `string` | No |  |

### Roblox.Games.Api.Models.Response.GameCreator

Response model for getting the game creator

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | `integer` | No | The game creator id |
| `name` | `string` | No | The game creator name |
| `type` | `string` | No | The game creator type |
| `isRNVAccount` | `boolean` | No | The game creator account is Luobu Real Name Verified |
| `hasVerifiedBadge` | `boolean` | No | Builder verified badge status. |

### Roblox.Games.Api.Models.Response.GameDetailResponse

Response model for getting the game detail

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | `integer` | No | The game universe id |
| `rootPlaceId` | `integer` | No | The game root place id |
| `name` | `string` | No | The game name |
| `description` | `string` | No | The game description |
| `sourceName` | `string` | No | The game name in the source language, if different from the returned name. |
| `sourceDescription` | `string` | No | The game description in the source language, if different from the returned description. |
| `creator` | `Roblox.Games.Api.Models.Response.GameCreator` | No |  |
| `price` | `integer` | No | The game paid access price |
| `allowedGearGenres` | `string[]` | No | The game allowed gear genres |
| `allowedGearCategories` | `string[]` | No | The game allowed gear categoris |
| `isGenreEnforced` | `boolean` | No | The game must specify a genre |
| `copyingAllowed` | `boolean` | No | The game allows place to be copied |
| `playing` | `integer` | No | Current player count of the game |
| `visits` | `integer` | No | The total visits to the game |
| `maxPlayers` | `integer` | No | The game max players |
| `created` | `string` | No | The game created time |
| `updated` | `string` | No | The game updated time |
| `studioAccessToApisAllowed` | `boolean` | No | The setting of IsStudioAccessToApisAllowed of the universe |
| `createVipServersAllowed` | `boolean` | No | Gets or sets the flag to indicate whether the create vip servers button should be allowed in game details page |
| `universeAvatarType` | `1 \| 2 \| 3` | No | Avatar type. Possible values are MorphToR6, MorphToR15, and PlayerChoice |
| `genre` | `string` | No | The game genre display name |
| `genre_l1` | `string` | No | The game genre from experience-genres-service |
| `genre_l2` | `string` | No | The game subgenre from experience-genres-service |
| `untranslated_genre_l1` | `string` | No | The game genre from experience-genres-service untranslated |
| `isAllGenre` | `boolean` | No | Is this game all genre. |
| `isFavoritedByUser` | `boolean` | No | Is this game favorited by user. |
| `favoritedCount` | `integer` | No | Game number of favorites. |
| `licenseDescription` | `string` | No |  |
| `refundLink` | `string` | No |  |
| `localizedFiatPrice` | `string` | No |  |
| `refundPolicy` | `Roblox.Games.Api.Models.Response.RefundPolicy` | No |  |
| `canonicalUrlPath` | `string` | No | Canonical URL path for the game page, e.g. /games/{placeId}/{canonical-slug}. It must be the same as the canonical URL (rel-canonical meta tag) on the game's EDP. |
| `isContentRestricted` | `boolean` | No | Indicates whether this experience is content-restricted and has had its details wiped. When true, the content fields (name, description, creator, etc.) contain placeholder or empty values rather than the real data. Consumers should branch on this flag instead of inferring restriction from placeholder text. |
| `creationSource` | `string` | No | How the experience was created, as reported by hydration (e.g. "build"). Omitted when hydration does not return a value. |

### Roblox.Games.Api.Models.Response.GameFavoriteResponse

Game favorite response model.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `isFavorited` | `boolean` | No | Is it a favorite game. |

### Roblox.Games.Api.Models.Response.GameFavoritesCountResponse

Response model for favorited game count.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `favoritesCount` | `integer` | No | Favorites count. |

### Roblox.Games.Api.Models.Response.GameMediaItem

Response model for getting the game media item

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | `integer` | No | The media item id. |
| `assetTypeId` | `integer` | No | The media item type id |
| `assetType` | `string` | No | The media item type, Image or YouTubeVideo |
| `imageId` | `integer` | No | The media item image id |
| `videoHash` | `string` | No | The media item video hash |
| `videoTitle` | `string` | No | The video title for video items. |
| `approved` | `boolean` | No | The media item is approved or not |
| `altText` | `string` | No | The media item's alt text |

### Roblox.Games.Api.Models.Response.GameProductResponse

Response model for getting the game product information

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `universeId` | `integer` | No | The game universe id |
| `isForSale` | `boolean` | No | The game purchasability |
| `productId` | `integer` | No | The game product id |
| `price` | `integer` | No | The game price |
| `sellerId` | `integer` | No | The game seller id User ID for users, Agent ID for groups |
| `fiatPurchaseData` | `Roblox.Games.Api.Models.Response.PurchaseData` | No |  |

### Roblox.Games.Api.Models.Response.GameRecommendationsResponse

Game recommendations response model.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `games` | `Roblox.Games.Api.Models.Response.GameResponseModel[]` | No | The recommended games. |
| `nextPaginationKey` | `string` | No | The pagination key for next page query. It will be null if there is no more data. |

### Roblox.Games.Api.Models.Response.GameResponseModel

Response model for games.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `creatorId` | `integer` | No | Creator Id |
| `creatorName` | `string` | No | Creator name |
| `creatorType` | `string` | No | Creator type |
| `creatorHasVerifiedBadge` | `boolean` | No | Creator verified badge status |
| `totalUpVotes` | `integer` | No | Total up votes |
| `totalDownVotes` | `integer` | No | Total down votes |
| `universeId` | `integer` | No | Universe id |
| `name` | `string` | No | Game name |
| `placeId` | `integer` | No | Place Id |
| `playerCount` | `integer` | No | Player count |
| `imageToken` | `string` | No | Place image token |
| `isSponsored` | `boolean` | No | Is sponsored |
| `nativeAdData` | `string` | No | Native ad data |
| `isShowSponsoredLabel` | `boolean` | No | Show the sponsored label |
| `price` | `integer` | No | The game paid access price |
| `analyticsIdentifier` | `string` | No | Provide all necessary information which helps analytics for improvement, for example, the algorithm, dataset version, position, etc.. |
| `gameDescription` | `string` | No | Provide all necessary information which helps analytics for improvement, for example, the algorithm, dataset version, position, etc.. |
| `genre` | `string` | No | The game genre display name |
| `minimumAge` | `integer` | No | Age Recommendation minimum age. |
| `ageRecommendationDisplayName` | `string` | No | Age Recommendation display name. |
| `contentMetadata` | `Roblox.Games.Api.Models.Response.GameContentMetadataResponseModel` | No |  |
| `canonicalUrlPath` | `string` | No | Canonical URL path for the game page, e.g. /games/{placeId}/{canonical-slug}. It must be the same as the canonical URL (rel-canonical meta tag) on the game's EDP. |

### Roblox.Games.Api.Models.Response.PlaceDetails

Response model for a place.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `placeId` | `integer` | No | Place Id |
| `name` | `string` | No | Place name |
| `description` | `string` | No | Place description |
| `sourceName` | `string` | No | Place name in source language |
| `sourceDescription` | `string` | No | Place description in source language |
| `url` | `string` | No | Url |
| `builder` | `string` | No | Creator name |
| `builderId` | `integer` | No | Creator Id |
| `hasVerifiedBadge` | `boolean` | No | Builder verified badge status. |
| `isPlayable` | `boolean` | No | Is playable |
| `reasonProhibited` | `string` | No | Reason prohibited |
| `universeId` | `integer` | No | Universe id |
| `universeRootPlaceId` | `integer` | No | UniverseRootPlaceId |
| `price` | `integer` | No | Price |
| `imageToken` | `string` | No | Place image token |
| `fiatPurchaseData` | `Roblox.Games.Api.Models.Response.PurchaseData` | No |  |

### Roblox.Games.Api.Models.Response.PlayabilityStatusResponse

Response model for getting a universe's playability status for a user

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `playabilityStatus` | `integer enum (34 values)` | No | The actual playability status of the universe including the reason if unplayable ['UnplayableOtherReason' = 0, 'Playable' = 1, 'GuestProhibited' = 2, 'GameUnapproved' = 3, 'IncorrectConfiguration' = 4, 'UniverseRootPlaceIsPrivate' = 5, 'InsufficientPermissionFriendsOnly' = 6, 'InsufficientPermissionGroupOnly' = 7, 'DeviceRestricted' = 8, 'UnderReview' = 9, 'PurchaseRequired' = 10, 'AccountRestricted' = 11, 'TemporarilyUnavailable' = 12, 'PlaceHasNoPublishedVersion' = 13, 'ComplianceBlocked' = 14, 'ContextualPlayabilityRegionalAvailability' = 15, 'ContextualPlayabilityRegionalCompliance' = 16, 'ContextualPlayabilityAgeRecommendationParentalControls' = 17, 'ContextualPlayabilityExperienceBlockedParentalControls' = 18, 'ContextualPlayabilityAgeGated' = 19, 'ContextualPlayabilityUnverifiedSeventeenPlusUser' = 20, 'FiatPurchaseRequired' = 21, 'FiatPurchaseDeviceRestricted' = 22, 'ContextualPlayabilityUnrated' = 23, 'ContextualPlayabilityAgeGatedByDescriptor' = 24, 'ContextualPlayabilityGeneral' = 25, 'ContextualPlayabilityAgeCheckRequired' = 26, 'ContextualPlayabilityRequireParentApproval' = 27, 'ContextualPlayabilityCoreGated' = 28, 'ContextualPlayabilityTrustedFriendRequired' = 29, 'PlusSubscriptionRequired' = 30, 'ContextualPlayabilityPlaytestDisabled' = 31, 'InsufficientPermissionEditorsOnly' = 32, 'InsufficientPermissionPlayTestersOnly' = 33] Values: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33 |
| `isPlayable` | `boolean` | No | Whether or not the universe is playable for the user |
| `universeId` | `integer` | No | The universeId of the requested universe to help with batching requests |
| `unplayableDisplayText` | `string` | No | Localized display text explaining why unplayable |
| `playableUxTreatment` | `Roblox.Games.Api.Models.Response.PlayableUxTreatment` | No |  |
| `upsellUxTreatment` | `Roblox.Games.Api.Models.Response.UpsellUxTreatment` | No |  |
| `demoModeAvailable` | `boolean` | No | Whether the game supports demo play for users who have not purchased it. Only set when PlayabilityStatus is PurchaseRequired or FiatPurchaseRequired. |
| `privatePlaytestInfo` | `Roblox.Games.Api.Models.Response.PrivatePlaytestInfoResponse` | No |  |

### Roblox.Games.Api.Models.Response.PlayableUxTreatment

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `treatment` | `string` | No |  |
| `data` | `Roblox.Games.Api.Models.Response.PlayableUxTreatmentData` | No |  |

### Roblox.Games.Api.Models.Response.PlayableUxTreatmentData

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `titleText` | `string` | No |  |
| `bodyText` | `string` | No |  |
| `primaryActionText` | `string` | No |  |
| `secondaryActionText` | `string` | No |  |

### Roblox.Games.Api.Models.Response.PrivatePlaytestInfoResponse

Private playtest eligibility for the authenticated user.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `isPlayable` | `boolean` | No | Whether the user is eligible to play as a private playtester. |
| `playabilityStatus` | `integer enum (34 values)` | No | The private playtest eligibility status. ['UnplayableOtherReason' = 0, 'Playable' = 1, 'GuestProhibited' = 2, 'GameUnapproved' = 3, 'IncorrectConfiguration' = 4, 'UniverseRootPlaceIsPrivate' = 5, 'InsufficientPermissionFriendsOnly' = 6, 'InsufficientPermissionGroupOnly' = 7, 'DeviceRestricted' = 8, 'UnderReview' = 9, 'PurchaseRequired' = 10, 'AccountRestricted' = 11, 'TemporarilyUnavailable' = 12, 'PlaceHasNoPublishedVersion' = 13, 'ComplianceBlocked' = 14, 'ContextualPlayabilityRegionalAvailability' = 15, 'ContextualPlayabilityRegionalCompliance' = 16, 'ContextualPlayabilityAgeRecommendationParentalControls' = 17, 'ContextualPlayabilityExperienceBlockedParentalControls' = 18, 'ContextualPlayabilityAgeGated' = 19, 'ContextualPlayabilityUnverifiedSeventeenPlusUser' = 20, 'FiatPurchaseRequired' = 21, 'FiatPurchaseDeviceRestricted' = 22, 'ContextualPlayabilityUnrated' = 23, 'ContextualPlayabilityAgeGatedByDescriptor' = 24, 'ContextualPlayabilityGeneral' = 25, 'ContextualPlayabilityAgeCheckRequired' = 26, 'ContextualPlayabilityRequireParentApproval' = 27, 'ContextualPlayabilityCoreGated' = 28, 'ContextualPlayabilityTrustedFriendRequired' = 29, 'PlusSubscriptionRequired' = 30, 'ContextualPlayabilityPlaytestDisabled' = 31, 'InsufficientPermissionEditorsOnly' = 32, 'InsufficientPermissionPlayTestersOnly' = 33] Values: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33 |

### Roblox.Games.Api.Models.Response.PurchaseData

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `localizedFiatPrice` | `string` | No | Fiat purchase price in a localized string for display on client. |
| `basePriceId` | `string` | No | ID of base price, needed by clients to prepare purchase url. |

### Roblox.Games.Api.Models.Response.RefundPolicy

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `policyText` | `string` | No | The display text with a placeholder for clients to inject a link, such as:   "Learn more about policy xyz {linkStart}Learn More{linkEnd}" |
| `learnMoreBaseUrl` | `string` | No | The base URL that the client should redirect to. |
| `locale` | `string` | No | The Roblox selected language locale that the user has presently selected. |
| `articleId` | `string` | No | Zendesk (or similar forum provider) article ID for the client to build a redirect URL. |

### Roblox.Games.Api.Models.Response.UpsellUxTreatment

Upsell UX treatment metadata appended to a playability response.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `treatment` | `string` | No | Identifier of the client component to render. |
| `data` | `Roblox.Games.Api.Models.Response.UpsellUxTreatmentData` | No |  |

### Roblox.Games.Api.Models.Response.UpsellUxTreatmentData

Localized strings for an Roblox.Games.Api.Models.Response.UpsellUxTreatment.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `bodyText` | `string` | No | Localized body text for the upsell. |

### Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.Games.Api.Models.Response.GameDetailResponse]

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | `Roblox.Games.Api.Models.Response.GameDetailResponse[]` | No |  |

### Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.Games.Api.Models.Response.GameMediaItem]

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | `Roblox.Games.Api.Models.Response.GameMediaItem[]` | No |  |

### Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.Games.Api.Models.Response.GameProductResponse]

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | `Roblox.Games.Api.Models.Response.GameProductResponse[]` | No |  |