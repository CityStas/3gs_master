---
name: "Followings Api v2"
last_updated: 2026-10-30T19:56:08Z
type: legacy
api_base_url: "https://followings.roblox.com"
versions: [v2, v1]
endpoints: 5
auth: [cookie]
---

# Followings Api v2

> **Warning:** Legacy APIs with cookie authentication can incorporate breaking changes without notice. We don't recommend them for production applications.

**Base URL:** `https://followings.roblox.com`
**Versions:** v2, v1

## V2

### GET `/v2/users/{userId}/universes`

Gets all universes followed by a user.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer (int64)` | Yes | The user ID. |

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
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://followings.roblox.com/v2/users/{USERID}/universes"
```

## Models

### Roblox.Followings.Api.Models.FollowsByTypeResponse

Data model containing collection of all followed sources of a specific type.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `followerType` | `0 \| 1` | No | Type of the follower entity. |
| `followerId` | `integer` | No | ID of the follower entity. |
| `sourceType` | `0 \| 1` | No | Type of the source entity. |
| `followedSources` | `object` | No | Followed sources: map of (source ID => follow date) |

## V1

### GET `/v1/users/{userId}/universes`

Gets all the followings between a user with userId and universes

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer (int64)` | Yes |  |

**Responses:**

- `200`: A list of user to game followings. → `Roblox.Followings.Api.Models.UserFollowingUniverseResponse[]`
- `401`: 0: Authorization has been denied for this request.
- `403`: User is not authorized for this action.

**Response fields** (`Roblox.Followings.Api.Models.UserFollowingUniverseResponse[]`)

See [Roblox.Followings.Api.Models.UserFollowingUniverseResponse](#roblox-followings-api-models-userfollowinguniverseresponse) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://followings.roblox.com/v1/users/{USERID}/universes"
```

### GET `/v1/users/{userId}/universes/{universeId}/status`

Gets the status of a following relationship between a user and a universe.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer (int64)` | Yes |  |
| `universeId` | path | `integer (int64)` | Yes |  |

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
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://followings.roblox.com/v1/users/{USERID}/universes/{UNIVERSEID}/status"
```

### POST `/v1/users/{userId}/universes/{universeId}`

Creates the following between a user with userId and universe with universeId

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer (int64)` | Yes |  |
| `universeId` | path | `integer (int64)` | Yes |  |

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
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://followings.roblox.com/v1/users/{USERID}/universes/{UNIVERSEID}"
```

### DELETE `/v1/users/{userId}/universes/{universeId}`

Deletes the following between a user with userId and universe with universeId

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer (int64)` | Yes |  |
| `universeId` | path | `integer (int64)` | Yes |  |

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
curl -X DELETE -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://followings.roblox.com/v1/users/{USERID}/universes/{UNIVERSEID}"
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