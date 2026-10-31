---
name: "Interactions"
last_updated: 2026-10-30T19:56:08Z
type: feature
api_base_url: "https://apis.roblox.com"
endpoints: 26
auth: [api-key, oauth2, cookie]
description: "Manage your favorites, experience notifications, and assets you voted on"
---

# Interactions

Manage your favorites, experience notifications, and assets you voted on. [List experiences opted-in for notifications for a user](#get_legacy_followings_v1_users__userId__universes), [manage favorites](#catalog_get_v1_favorites_users__userId__assets__assetId__favorite) for assets and bundles, and [track](#games_get_v1_games_votes) votes on experiences.

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

### GET `/legacy-followings/v1/users/{userId}/universes`

Gets all the followings between a user with userId and universes

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `legacy-universe.following:read`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer` | Yes |  |

**Responses:**

- `200`: A list of user to game followings. → `Roblox.Followings.Api.Models.UserFollowingUniverseResponse[]`
- `401`: 0: Authorization has been denied for this request.
- `403`: User is not authorized for this action.

**Response fields** (`Roblox.Followings.Api.Models.UserFollowingUniverseResponse[]`)

See [Roblox.Followings.Api.Models.UserFollowingUniverseResponse](#roblox-followings-api-models-userfollowinguniverseresponse) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 100/minute, perOauth2Authorization: 100/minute

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/legacy-followings/v1/users/{USERID}/universes"
```

### POST `/legacy-followings/v1/users/{userId}/universes/{universeId}`

Creates the following between a user with userId and universe with universeId

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `legacy-universe.following:write`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer` | Yes |  |
| `universeId` | path | `integer` | Yes |  |

**Responses:**

- `200`: The created following. → `Roblox.Followings.Api.Models.UserFollowingUniverseResponse`
- `400`: The user has reached the limit of number of followed universes.
- `401`: 0: Authorization has been denied for this request.
- `403`: User is not authorized for this action.

**Response fields** (`Roblox.Followings.Api.Models.UserFollowingUniverseResponse`)

See [Roblox.Followings.Api.Models.UserFollowingUniverseResponse](#roblox-followings-api-models-userfollowinguniverseresponse) in Models.

**Response example:**
```json
{
  "universeId": 0,
  "userId": 0
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 100/minute, perOauth2Authorization: 100/minute

**Example:**
```bash
curl -X POST -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/legacy-followings/v1/users/{USERID}/universes/{UNIVERSEID}"
```

### DELETE `/legacy-followings/v1/users/{userId}/universes/{universeId}`

Deletes the following between a user with userId and universe with universeId

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `legacy-universe.following:write`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer` | Yes |  |
| `universeId` | path | `integer` | Yes |  |

**Responses:**

- `200`: The deleted following. → `Roblox.Followings.Api.Models.UserFollowingUniverseResponse`
- `401`: 0: Authorization has been denied for this request.
- `403`: User is not authorized for this action.

**Response fields** (`Roblox.Followings.Api.Models.UserFollowingUniverseResponse`)

See [Roblox.Followings.Api.Models.UserFollowingUniverseResponse](#roblox-followings-api-models-userfollowinguniverseresponse) in Models.

**Response example:**
```json
{
  "universeId": 0,
  "userId": 0
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 100/minute, perOauth2Authorization: 100/minute

**Example:**
```bash
curl -X DELETE -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/legacy-followings/v1/users/{USERID}/universes/{UNIVERSEID}"
```

### GET `/legacy-followings/v1/users/{userId}/universes/{universeId}/status`

Gets the status of a following relationship between a user and a universe.

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `legacy-universe.following:read`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer` | Yes |  |
| `universeId` | path | `integer` | Yes |  |

**Responses:**

- `200`: The status of the following relationship. → `Roblox.Followings.Api.Models.UserFollowingUniverseStatusResponse`
- `401`: 0: Authorization has been denied for this request.
- `403`: User is not authorized for this action.

**Response fields** (`Roblox.Followings.Api.Models.UserFollowingUniverseStatusResponse`)

See [Roblox.Followings.Api.Models.UserFollowingUniverseStatusResponse](#roblox-followings-api-models-userfollowinguniversestatusresponse) in Models.

**Response example:**
```json
{
  "UniverseId": 0,
  "UserId": 0,
  "CanFollow": false,
  "IsFollowing": false,
  "FollowingCountByType": 0,
  "FollowingLimitByType": 0
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 100/minute, perOauth2Authorization: 100/minute

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/legacy-followings/v1/users/{USERID}/universes/{UNIVERSEID}/status"
```

### GET `/legacy-followings/v2/users/{userId}/universes`

Gets all universes followed by a user.

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `legacy-universe.following:read`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer` | Yes | The user ID. |

**Responses:**

- `200`: Data model containing map of (universe ID => follow date). → `Roblox.Followings.Api.Models.FollowsByTypeResponse`
- `401`: 0: Authorization has been denied for this request.
- `403`: User is not authorized for this action.

**Response fields** (`Roblox.Followings.Api.Models.FollowsByTypeResponse`)

See [Roblox.Followings.Api.Models.FollowsByTypeResponse](#roblox-followings-api-models-followsbytyperesponse) in Models.

**Response example:**
```json
{
  "followerType": 0,
  "followerId": 0,
  "sourceType": 0,
  "followedSources": "..."
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 100/minute, perOauth2Authorization: 100/minute

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/legacy-followings/v2/users/{USERID}/universes"
```

### GET `/v1/games/votes`

**Server:** `https://games.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeIds` | query | `integer[]` | No |  |

**Responses:**

- `200`: OK → `GameVoteResponseApiArrayResponse`

**Response fields** (`GameVoteResponseApiArrayResponse`)

See [GameVoteResponseApiArrayResponse](#gamevoteresponseapiarrayresponse) in Models.

**Response example:**
```json
{
  "data": [
    {
      "id": "...",
      "upVotes": "...",
      "downVotes": "..."
    }
  ]
}
```

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://games.roblox.com/v1/games/votes"
```

### GET `/v1/games/{universeId}/favorites` [EXPERIMENTAL]

Returns if a game was marked as favorite for the authenticated user

**Server:** `https://games.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer` | Yes | The Id of the universe. |

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
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://games.roblox.com/v1/games/{UNIVERSEID}/favorites"
```

### POST `/v1/games/{universeId}/favorites` [EXPERIMENTAL]

Favors (or unfavors) a game for the authenticated user

**Server:** `https://games.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer` | Yes | The Id of the universe. |

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
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://games.roblox.com/v1/games/{UNIVERSEID}/favorites" \
  -H "Content-Type: application/json" \
  -d '{
  "isFavorited": false
}'
```

### GET `/v1/games/{universeId}/favorites/count` [EXPERIMENTAL]

Get the favorites count of a specific game.

**Server:** `https://games.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer` | Yes | The Id of the universe. |

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
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://games.roblox.com/v1/games/{UNIVERSEID}/favorites/count"
```

### PATCH `/v1/games/{universeId}/user-votes` [EXPERIMENTAL]

**Server:** `https://games.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer` | Yes |  |

**Request Body:** `application/json-patch+json` — Type: `any`

**Responses:**

- `200`: OK → `ApiEmptyResponseModel`

**Response fields** (`ApiEmptyResponseModel`)

See [ApiEmptyResponseModel](#apiemptyresponsemodel) in Models.

**Example:**
```bash
curl -X PATCH -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://games.roblox.com/v1/games/{UNIVERSEID}/user-votes" \
  -H "Content-Type: application/json" \
  -d '"..."'
```

### GET `/v1/games/{universeId}/votes` [EXPERIMENTAL]

**Server:** `https://games.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer` | Yes |  |

**Responses:**

- `200`: OK → `GameVoteResponse`

**Response fields** (`GameVoteResponse`)

See [GameVoteResponse](#gamevoteresponse) in Models.

**Response example:**
```json
{
  "id": 0,
  "upVotes": 0,
  "downVotes": 0
}
```

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://games.roblox.com/v1/games/{UNIVERSEID}/votes"
```

### GET `/v1/games/{universeId}/votes/user`

**Server:** `https://games.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer` | Yes |  |

**Responses:**

- `200`: OK → `UserGameVoteResponse`

**Response fields** (`UserGameVoteResponse`)

See [UserGameVoteResponse](#usergamevoteresponse) in Models.

**Response example:**
```json
{
  "canVote": false,
  "userVote": false,
  "reasonForNotVoteable": "string"
}
```

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://games.roblox.com/v1/games/{UNIVERSEID}/votes/user"
```

### POST `/v1/user/following-exists`

Returns whether or not the current user is following each userId in a list of userIds

**Server:** `https://friends.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Request Body:** `application/json` — Type: `Roblox.Friends.Api.FollowingExistsRequestModel`

See [Roblox.Friends.Api.FollowingExistsRequestModel](#roblox-friends-api-followingexistsrequestmodel) in Models.

**Request example:**
```json
{
  "targetUserIds": [
    0
  ]
}
```

**Responses:**

- `200`: OK → `Roblox.Friends.Api.Models.Response.FollowingExistsResponseModel`
- `400`: 0: An invalid userId was passed in.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed
- `503`: 1: Followers are disabled at this time.

**Response fields** (`Roblox.Friends.Api.Models.Response.FollowingExistsResponseModel`)

See [Roblox.Friends.Api.Models.Response.FollowingExistsResponseModel](#roblox-friends-api-models-response-followingexistsresponsemodel) in Models.

**Response example:**
```json
{
  "followings": [
    {
      "isFollowing": "...",
      "isFollowed": "...",
      "userId": "..."
    }
  ]
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://friends.roblox.com/v1/user/following-exists" \
  -H "Content-Type: application/json" \
  -d '{
  "targetUserIds": [
    0
  ]
}'
```

### POST `/v1/users/{targetUserId}/follow`

Creates the following between a user and user with targetUserId

**Server:** `https://friends.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `targetUserId` | path | `integer` | Yes |  |

**Request Body:** `application/json` — Type: `Roblox.Web.Captcha.Models.Request.CaptchaTokenRequest`

See [Roblox.Web.Captcha.Models.Request.CaptchaTokenRequest](#roblox-web-captcha-models-request-captchatokenrequest) in Models.

**Request example:**
```json
{
  "captchaId": "string",
  "captchaToken": "string",
  "captchaProvider": "string",
  "challengeId": "string"
}
```

**Responses:**

- `200`: OK → `Roblox.Friends.Api.CaptchaStatusResponseModel`
- `400`: 1: The target user is invalid or does not exist. 6: Invalid parameters. 8: The user cannot follow itself.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 2: The user is banned from performing operation. 3: The user is blocked from performing this action. 14: The user has not passed the captcha.
- `429`: 9: The flood limit has been exceeded.

**Response fields** (`Roblox.Friends.Api.CaptchaStatusResponseModel`)

See [Roblox.Friends.Api.CaptchaStatusResponseModel](#roblox-friends-api-captchastatusresponsemodel) in Models.

**Response example:**
```json
{
  "success": false,
  "isCaptchaRequired": false,
  "notificationMuted": false
}
```

**Error handling:** `429`: Retry with exponential backoff (start at 1s). `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://friends.roblox.com/v1/users/{TARGETUSERID}/follow" \
  -H "Content-Type: application/json" \
  -d '{
  "captchaId": "string",
  "captchaToken": "string",
  "captchaProvider": "string",
  "challengeId": "string"
}'
```

### GET `/v1/users/{targetUserId}/followers`

Get all users that follow user with targetUserId in page response format

**Server:** `https://friends.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `targetUserId` | path | `integer` | Yes |  |
| `limit` | query | `10 \| 18 \| 25 \| 50 \| 100` | No | The number of results per request. Valid values: `10`, `18`, `25`, `50`, `100` |
| `cursor` | query | `string` | No | The paging cursor for the previous or next page. |
| `sortOrder` | query | `Asc \| Desc` | No | The order the results are sorted in. Valid values: `Asc`, `Desc` |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.Friends.Api.Models.Response.UserResponse_`
- `400`: 1: The target user is invalid or does not exist. 6: Invalid parameters.
- `403`: 2: The user is banned from performing operation. 3: The user is blocked from performing this action.
- `429`: 9: The flood limit has been exceeded.

**Response fields** (`Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.Friends.Api.Models.Response.UserResponse_`)

See [Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.Friends.Api.Models.Response.UserResponse_](#roblox-web-webapi-models-apipageresponse-roblox-friends-api-models-response-userresponse-) in Models.

**Response example:**
```json
{
  "previousPageCursor": "string",
  "nextPageCursor": "string",
  "data": [
    {
      "isOnline": "...",
      "presenceType": "...",
      "isDeleted": "...",
      "friendFrequentScore": "...",
      "friendFrequentRank": "...",
      "hasVerifiedBadge": "..."
    }
  ]
}
```

**Error handling:** `429`: Retry with exponential backoff (start at 1s). `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://friends.roblox.com/v1/users/{TARGETUSERID}/followers"
```

### GET `/v1/users/{targetUserId}/followers/count`

Get the number of following a user has

**Server:** `https://friends.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `targetUserId` | path | `integer` | Yes |  |

**Responses:**

- `200`: OK → `Roblox.Friends.Api.FollowCountResponse`
- `400`: 1: The target user is invalid or does not exist.

**Response fields** (`Roblox.Friends.Api.FollowCountResponse`)

See [Roblox.Friends.Api.FollowCountResponse](#roblox-friends-api-followcountresponse) in Models.

**Response example:**
```json
{
  "count": 0
}
```

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://friends.roblox.com/v1/users/{TARGETUSERID}/followers/count"
```

### GET `/v1/users/{targetUserId}/followings`

Get all users that user with targetUserId is following in page response format

**Server:** `https://friends.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `targetUserId` | path | `integer` | Yes |  |
| `limit` | query | `10 \| 18 \| 25 \| 50 \| 100` | No | The number of results per request. Valid values: `10`, `18`, `25`, `50`, `100` |
| `cursor` | query | `string` | No | The paging cursor for the previous or next page. |
| `sortOrder` | query | `Asc \| Desc` | No | The order the results are sorted in. Valid values: `Asc`, `Desc` |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.Friends.Api.Models.Response.UserResponse_`
- `400`: 1: The target user is invalid or does not exist. 6: Invalid parameters.
- `403`: 2: The user is banned from performing operation. 3: The user is blocked from performing this action.
- `429`: 9: The flood limit has been exceeded.

**Response fields** (`Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.Friends.Api.Models.Response.UserResponse_`)

See [Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.Friends.Api.Models.Response.UserResponse_](#roblox-web-webapi-models-apipageresponse-roblox-friends-api-models-response-userresponse-) in Models.

**Response example:**
```json
{
  "previousPageCursor": "string",
  "nextPageCursor": "string",
  "data": [
    {
      "isOnline": "...",
      "presenceType": "...",
      "isDeleted": "...",
      "friendFrequentScore": "...",
      "friendFrequentRank": "...",
      "hasVerifiedBadge": "..."
    }
  ]
}
```

**Error handling:** `429`: Retry with exponential backoff (start at 1s). `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://friends.roblox.com/v1/users/{TARGETUSERID}/followings"
```

### GET `/v1/users/{targetUserId}/followings/count`

Get the number of following a user has

**Server:** `https://friends.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `targetUserId` | path | `integer` | Yes |  |

**Responses:**

- `200`: OK → `Roblox.Friends.Api.FollowCountResponse`
- `400`: 1: The target user is invalid or does not exist.

**Response fields** (`Roblox.Friends.Api.FollowCountResponse`)

See [Roblox.Friends.Api.FollowCountResponse](#roblox-friends-api-followcountresponse) in Models.

**Response example:**
```json
{
  "count": 0
}
```

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://friends.roblox.com/v1/users/{TARGETUSERID}/followings/count"
```

### POST `/v1/users/{targetUserId}/unfollow`

Deletes the following between a user and user with targetUserId

**Server:** `https://friends.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `targetUserId` | path | `integer` | Yes |  |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: 1: The target user is invalid or does not exist. 6: Invalid parameters. 8: The user cannot follow itself.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 2: The user is banned from performing operation. 3: The user is blocked from performing this action. 14: The user has not passed the captcha.
- `429`: 9: The flood limit has been exceeded.

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `429`: Retry with exponential backoff (start at 1s). `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://friends.roblox.com/v1/users/{TARGETUSERID}/unfollow"
```

### GET `/v1/users/{userId}/categories/favorites`

Return favorites categories for a user

**Server:** `https://inventory.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer` | Yes |  |

**Responses:**

- `200`: OK → `Roblox.Inventory.Api.Models.CategoriesModel`

**Response fields** (`Roblox.Inventory.Api.Models.CategoriesModel`)

See [Roblox.Inventory.Api.Models.CategoriesModel](#roblox-inventory-api-models-categoriesmodel) in Models.

**Response example:**
```json
{
  "categories": [
    {
      "name": "...",
      "displayName": "...",
      "categoryType": "...",
      "items": "..."
    }
  ]
}
```

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://inventory.roblox.com/v1/users/{USERID}/categories/favorites"
```

### GET `/v1/users/{userId}/universes`

Gets all the followings between a user with userId and universes

**Server:** `https://followings.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer` | Yes |  |

**Responses:**

- `200`: A list of user to game followings. → `Roblox.Followings.Api.Models.UserFollowingUniverseResponse[]`
- `401`: 0: Authorization has been denied for this request.
- `403`: User is not authorized for this action.

**Response fields** (`Roblox.Followings.Api.Models.UserFollowingUniverseResponse[]`)

See [Roblox.Followings.Api.Models.UserFollowingUniverseResponse](#roblox-followings-api-models-userfollowinguniverseresponse) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://followings.roblox.com/v1/users/{USERID}/universes"
```

### POST `/v1/users/{userId}/universes/{universeId}`

Creates the following between a user with userId and universe with universeId

**Server:** `https://followings.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer` | Yes |  |
| `universeId` | path | `integer` | Yes |  |

**Responses:**

- `200`: The created following. → `Roblox.Followings.Api.Models.UserFollowingUniverseResponse`
- `400`: The user has reached the limit of number of followed universes.
- `401`: 0: Authorization has been denied for this request.
- `403`: User is not authorized for this action.

**Response fields** (`Roblox.Followings.Api.Models.UserFollowingUniverseResponse`)

See [Roblox.Followings.Api.Models.UserFollowingUniverseResponse](#roblox-followings-api-models-userfollowinguniverseresponse) in Models.

**Response example:**
```json
{
  "universeId": 0,
  "userId": 0
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://followings.roblox.com/v1/users/{USERID}/universes/{UNIVERSEID}"
```

### DELETE `/v1/users/{userId}/universes/{universeId}`

Deletes the following between a user with userId and universe with universeId

**Server:** `https://followings.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer` | Yes |  |
| `universeId` | path | `integer` | Yes |  |

**Responses:**

- `200`: The deleted following. → `Roblox.Followings.Api.Models.UserFollowingUniverseResponse`
- `401`: 0: Authorization has been denied for this request.
- `403`: User is not authorized for this action.

**Response fields** (`Roblox.Followings.Api.Models.UserFollowingUniverseResponse`)

See [Roblox.Followings.Api.Models.UserFollowingUniverseResponse](#roblox-followings-api-models-userfollowinguniverseresponse) in Models.

**Response example:**
```json
{
  "universeId": 0,
  "userId": 0
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X DELETE -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://followings.roblox.com/v1/users/{USERID}/universes/{UNIVERSEID}"
```

### GET `/v1/users/{userId}/universes/{universeId}/status`

Gets the status of a following relationship between a user and a universe.

**Server:** `https://followings.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer` | Yes |  |
| `universeId` | path | `integer` | Yes |  |

**Responses:**

- `200`: The status of the following relationship. → `Roblox.Followings.Api.Models.UserFollowingUniverseStatusResponse`
- `401`: 0: Authorization has been denied for this request.
- `403`: User is not authorized for this action.

**Response fields** (`Roblox.Followings.Api.Models.UserFollowingUniverseStatusResponse`)

See [Roblox.Followings.Api.Models.UserFollowingUniverseStatusResponse](#roblox-followings-api-models-userfollowinguniversestatusresponse) in Models.

**Response example:**
```json
{
  "UniverseId": 0,
  "UserId": 0,
  "CanFollow": false,
  "IsFollowing": false,
  "FollowingCountByType": 0,
  "FollowingLimitByType": 0
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://followings.roblox.com/v1/users/{USERID}/universes/{UNIVERSEID}/status"
```

### GET `/v2/users/{userId}/favorite/games` [EXPERIMENTAL]

Gets users favorite games.

**Server:** `https://games.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer` | Yes | The user Id. |
| `accessFilter` | query | `1 \| 2 \| 4` | No | Filtering option via access level. Valid values: `1`, `2`, `4` |
| `limit` | query | `10 \| 25 \| 50 \| 100` | No | The number of results per request. Valid values: `10`, `25`, `50`, `100` |
| `cursor` | query | `string` | No | The paging cursor for the previous or next page. |
| `sortOrder` | query | `Asc \| Desc` | No | The order the results are sorted in. Valid values: `Asc`, `Desc` |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.Web.Responses.Games.GameFavoriteResponseModel_`

**Response fields** (`Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.Web.Responses.Games.GameFavoriteResponseModel_`)

See [Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.Web.Responses.Games.GameFavoriteResponseModel_](#roblox-web-webapi-models-apipageresponse-roblox-web-responses-games-gamefavoriteresponsemodel-) in Models.

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
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://games.roblox.com/v2/users/{USERID}/favorite/games"
```

### GET `/v2/users/{userId}/universes`

Gets all universes followed by a user.

**Server:** `https://followings.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer` | Yes | The user ID. |

**Responses:**

- `200`: Data model containing map of (universe ID => follow date). → `Roblox.Followings.Api.Models.FollowsByTypeResponse`
- `401`: 0: Authorization has been denied for this request.
- `403`: User is not authorized for this action.

**Response fields** (`Roblox.Followings.Api.Models.FollowsByTypeResponse`)

See [Roblox.Followings.Api.Models.FollowsByTypeResponse](#roblox-followings-api-models-followsbytyperesponse) in Models.

**Response example:**
```json
{
  "followerType": 0,
  "followerId": 0,
  "sourceType": 0,
  "followedSources": "..."
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://followings.roblox.com/v2/users/{USERID}/universes"
```

## Models

### Roblox.Followings.Api.Models.UserFollowingUniverseResponse

Model for a user following a universe controller responses

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `universeId` | `integer` | No | The id of the universe being followed |
| `userId` | `integer` | No | The id of the user that is following |

### Roblox.Followings.Api.Models.UserFollowingUniverseStatusResponse

Model for a user following a universe  state controller responses

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `UniverseId` | `integer` | No | The id of the universe. |
| `UserId` | `integer` | No | The id of the user. |
| `CanFollow` | `boolean` | No | If the user can follow the universe. |
| `IsFollowing` | `boolean` | No | If the user is currently following the universe. |
| `FollowingCountByType` | `integer` | No | The number of followings between this user and a universe. |
| `FollowingLimitByType` | `integer` | No | The limit to the number of followings between a user and a universe for a specific user. |

### Roblox.Followings.Api.Models.FollowsByTypeResponse

Data model containing collection of all followed sources of a specific type.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `followerType` | `0 \| 1` | No | Type of the follower entity. |
| `followerId` | `integer` | No | ID of the follower entity. |
| `sourceType` | `0 \| 1` | No | Type of the source entity. |
| `followedSources` | `object` | No | Followed sources: map of (source ID => follow date) |

### GameVoteResponseApiArrayResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | `GameVoteResponse[]` | No |  |

### Roblox.Games.Api.Models.Response.GameFavoriteResponse

Game favorite response model.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `isFavorited` | `boolean` | No | Is it a favorite game. |

### Roblox.Games.Api.Models.Request.GameFavoritesRequest

Game favorite request model.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `isFavorited` | `boolean` | No | true for favor the game, false for unfavor the game. |

### Roblox.Games.Api.Models.Response.GameFavoritesCountResponse

Response model for favorited game count.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `favoritesCount` | `integer` | No | Favorites count. |

### GameVoteResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | `integer` | No |  |
| `upVotes` | `integer` | No |  |
| `downVotes` | `integer` | No |  |

### UserGameVoteResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `canVote` | `boolean` | No |  |
| `userVote` | `boolean` | No |  |
| `reasonForNotVoteable` | `string` | No |  |

### Roblox.Friends.Api.FollowingExistsRequestModel

Request model for FollowingExists endpoint

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `targetUserIds` | `integer[]` | No | The userIds which the user may or may not be following. |

### Roblox.Friends.Api.Models.Response.FollowingExistsResponseModel

Response model for FollowingExists endpoint.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `followings` | `Roblox.Friends.Api.Models.Response.FollowingExistsResponse[]` | No | A list of userIds and whether or not the given user is following them. |

### Roblox.Web.Captcha.Models.Request.CaptchaTokenRequest

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `captchaId` | `string` | No |  |
| `captchaToken` | `string` | No |  |
| `captchaProvider` | `string` | No |  |
| `challengeId` | `string` | No |  |

### Roblox.Friends.Api.CaptchaStatusResponseModel

This is response model to notify when action succeeded, failed, or captcha is required

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | `boolean` | No |  |
| `isCaptchaRequired` | `boolean` | No | Captcha is set to true if captcha is required from user to perform action |
| `notificationMuted` | `boolean` | No |  |

### Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.Friends.Api.Models.Response.UserResponse_

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `previousPageCursor` | `string` | No |  |
| `nextPageCursor` | `string` | No |  |
| `data` | `Roblox.Friends.Api.Models.Response.UserResponse[]` | No |  |

### Roblox.Friends.Api.FollowCountResponse

Response model for following or followers Count

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `count` | `integer` | No | Count of following or followers |

### Roblox.Inventory.Api.Models.CategoriesModel

Model class that contains the categories of the Inventory or Favorites page

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `categories` | `Roblox.Inventory.Api.Models.AssetsExplorerCategoryModel[]` | No | Categories to show up in Inventory or Favorites page |

### Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.Web.Responses.Games.GameFavoriteResponseModel_

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `previousPageCursor` | `string` | No |  |
| `nextPageCursor` | `string` | No |  |
| `data` | `Roblox.Web.Responses.Games.GameFavoriteResponseModel[]` | No |  |