---
name: "Friends Api v1"
last_updated: 2026-10-30T19:56:08Z
type: legacy
api_base_url: "https://friends.roblox.com"
versions: [v1]
endpoints: 26
auth: [cookie]
---

# Friends Api v1

> **Warning:** Legacy APIs with cookie authentication can incorporate breaking changes without notice. We don't recommend them for production applications.

**Base URL:** `https://friends.roblox.com`
**Versions:** v1

## Endpoints

### GET `/v1/metadata`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `targetUserId` | query | `integer (int64)` | No |  |

**Responses:**

- `200`: OK → `Roblox.Friends.Api.Models.Response.FriendsPageMetadataResponse`

**Response fields** (`Roblox.Friends.Api.Models.Response.FriendsPageMetadataResponse`)

See [Roblox.Friends.Api.Models.Response.FriendsPageMetadataResponse](#roblox-friends-api-models-response-friendspagemetadataresponse) in Models.

**Response example:**
```json
{
  "isFriendsFilterBarEnabled": false,
  "isFriendsPageSortExperimentEnabled": false,
  "isFriendsUserDataStoreCacheEnabled": false,
  "frequentFriendSortRollout": 0,
  "userName": "string",
  "displayName": "string"
}
```

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://friends.roblox.com/v1/metadata"
```

### GET `/v1/my/friends/{userId}/check-qr-session`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer (int64)` | Yes | user Id that shows the qr code |

**Responses:**

- `200`: OK → `boolean`
- `401`: 0: Authorization has been denied for this request.

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://friends.roblox.com/v1/my/friends/{USERID}/check-qr-session"
```

### GET `/v1/my/friends/count`

Get the number of friends a user has

**Responses:**

- `200`: OK → `Roblox.Friends.Api.FriendsCountResponse`
- `401`: 0: Authorization has been denied for this request.

**Response fields** (`Roblox.Friends.Api.FriendsCountResponse`)

See [Roblox.Friends.Api.FriendsCountResponse](#roblox-friends-api-friendscountresponse) in Models.

**Response example:**
```json
{
  "count": 0
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://friends.roblox.com/v1/my/friends/count"
```

### GET `/v1/my/friends/requests`

Get all users that friend requests with targetUserId using exclusive start paging

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `limit` | query | `integer (int32)` | No | The number of results per request. |
| `cursor` | query | `string` | No | The paging cursor for the previous or next page. |
| `sessionId` | query | `string` | No | Optional session identifier. |
| `friendRequestSort` | query | `integer (int32)` | No | Valid values: `0`, `1`, `2` |
| `uprankUnseen` | query | `boolean` | No | Whether to uprank unseen friend requests and return isUnseen per friend request. |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiPageResponse[Roblox.Friends.Api.FriendRequestResponse]`
- `400`: 1: The target user is invalid or does not exist. 6: Invalid parameters. 34: Invalid pagination cursor.
- `401`: 0: Authorization has been denied for this request.
- `403`: 2: The user is banned from performing operation. 3: The user is blocked from performing this action.
- `429`: 9: The flood limit has been exceeded.

**Response fields** (`Roblox.Web.WebAPI.Models.ApiPageResponse[Roblox.Friends.Api.FriendRequestResponse]`)

See [Roblox.Web.WebAPI.Models.ApiPageResponse[Roblox.Friends.Api.FriendRequestResponse]](#roblox-web-webapi-models-apipageresponse-roblox-friends-api-friendrequestresponse-) in Models.

**Response example:**
```json
{
  "previousPageCursor": "string",
  "nextPageCursor": "string",
  "data": [
    {
      "friendRequest": "...",
      "mutualFriendsList": "...",
      "hasVerifiedBadge": "...",
      "isUnseen": "...",
      "description": "...",
      "created": "..."
    }
  ]
}
```

**Error handling:** `429`: Retry with exponential backoff (start at 1s). `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://friends.roblox.com/v1/my/friends/requests"
```

### GET `/v1/my/new-friend-requests/count`

**Responses:**

- `200`: OK → `Roblox.Friends.Api.Models.Response.NewFriendRequestsCountResponse`
- `401`: 0: Authorization has been denied for this request.

**Response fields** (`Roblox.Friends.Api.Models.Response.NewFriendRequestsCountResponse`)

See [Roblox.Friends.Api.Models.Response.NewFriendRequestsCountResponse](#roblox-friends-api-models-response-newfriendrequestscountresponse) in Models.

**Response example:**
```json
{
  "count": 0
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://friends.roblox.com/v1/my/new-friend-requests/count"
```

### GET `/v1/my/trusted-friends/count`

Get the number of trusted friends a user has

**Responses:**

- `200`: OK → `Roblox.Friends.Api.FriendsCountResponse`
- `401`: 0: Authorization has been denied for this request.

**Response fields** (`Roblox.Friends.Api.FriendsCountResponse`)

See [Roblox.Friends.Api.FriendsCountResponse](#roblox-friends-api-friendscountresponse) in Models.

**Response example:**
```json
{
  "count": 0
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://friends.roblox.com/v1/my/trusted-friends/count"
```

### GET `/v1/my/trusted-friends/requests`

Get all incoming trusted friend requests using exclusive start paging.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `limit` | query | `integer (int32)` | No | The number of results per request. |
| `cursor` | query | `string` | No | The paging cursor for the previous or next page. |
| `sortOrder` | query | `integer (int32)` | No | Specifies how to sort the returned trusted friend requests. Valid values: `0`, `1` |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiPageResponse[Roblox.Friends.Api.Models.Response.TrustedFriendRequestResponse]`
- `400`: 1: The target user is invalid or does not exist. 6: Invalid parameters.
- `401`: 0: Authorization has been denied for this request.
- `403`: 2: The user is banned from performing operation. 3: The user is blocked from performing this action.
- `429`: 9: The flood limit has been exceeded.

**Response fields** (`Roblox.Web.WebAPI.Models.ApiPageResponse[Roblox.Friends.Api.Models.Response.TrustedFriendRequestResponse]`)

See [Roblox.Web.WebAPI.Models.ApiPageResponse[Roblox.Friends.Api.Models.Response.TrustedFriendRequestResponse]](#roblox-web-webapi-models-apipageresponse-roblox-friends-api-models-response-trustedfriendrequestresponse-) in Models.

**Response example:**
```json
{
  "previousPageCursor": "string",
  "nextPageCursor": "string",
  "data": [
    {
      "sentAt": "...",
      "senderId": "..."
    }
  ]
}
```

**Error handling:** `429`: Retry with exponential backoff (start at 1s). `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://friends.roblox.com/v1/my/trusted-friends/requests"
```

### GET `/v1/user/friend-requests/count`

Return the number of pending friend requests.

**Responses:**

- `200`: OK → `Roblox.Friends.Api.PendingFriendRequestCountModel`
- `401`: 0: Authorization has been denied for this request.

**Response fields** (`Roblox.Friends.Api.PendingFriendRequestCountModel`)

See [Roblox.Friends.Api.PendingFriendRequestCountModel](#roblox-friends-api-pendingfriendrequestcountmodel) in Models.

**Response example:**
```json
{
  "count": 0
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://friends.roblox.com/v1/user/friend-requests/count"
```

### GET `/v1/user/trusted-friend-requests/count`

Return the number of pending trusted friend requests.

**Responses:**

- `200`: OK → `Roblox.Friends.Api.PendingFriendRequestCountModel`
- `401`: 0: Authorization has been denied for this request.

**Response fields** (`Roblox.Friends.Api.PendingFriendRequestCountModel`)

See [Roblox.Friends.Api.PendingFriendRequestCountModel](#roblox-friends-api-pendingfriendrequestcountmodel) in Models.

**Response example:**
```json
{
  "count": 0
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://friends.roblox.com/v1/user/trusted-friend-requests/count"
```

### GET `/v1/users/{targetUserId}/followers`

Get all users that follow user with targetUserId in page response format

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `targetUserId` | path | `integer (int64)` | Yes |  |
| `limit` | query | `integer (int32)` | No | The number of results per request. Valid values: `10`, `18`, `25`, `50`, `100` |
| `cursor` | query | `string` | No | The paging cursor for the previous or next page. |
| `sortOrder` | query | `string` | No | The order the results are sorted in. Valid values: `Asc`, `Desc` |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiPageResponse[Roblox.Friends.Api.Models.Response.UserResponse]`
- `400`: 1: The target user is invalid or does not exist. 6: Invalid parameters.
- `403`: 2: The user is banned from performing operation. 3: The user is blocked from performing this action.
- `429`: 9: The flood limit has been exceeded.

**Response fields** (`Roblox.Web.WebAPI.Models.ApiPageResponse[Roblox.Friends.Api.Models.Response.UserResponse]`)

See [Roblox.Web.WebAPI.Models.ApiPageResponse[Roblox.Friends.Api.Models.Response.UserResponse]](#roblox-web-webapi-models-apipageresponse-roblox-friends-api-models-response-userresponse-) in Models.

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
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://friends.roblox.com/v1/users/{TARGETUSERID}/followers"
```

### GET `/v1/users/{targetUserId}/followers/count`

Get the number of following a user has

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `targetUserId` | path | `integer (int64)` | Yes |  |

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
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://friends.roblox.com/v1/users/{TARGETUSERID}/followers/count"
```

### GET `/v1/users/{targetUserId}/followings`

Get all users that user with targetUserId is following in page response format

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `targetUserId` | path | `integer (int64)` | Yes |  |
| `limit` | query | `integer (int32)` | No | The number of results per request. Valid values: `10`, `18`, `25`, `50`, `100` |
| `cursor` | query | `string` | No | The paging cursor for the previous or next page. |
| `sortOrder` | query | `string` | No | The order the results are sorted in. Valid values: `Asc`, `Desc` |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiPageResponse[Roblox.Friends.Api.Models.Response.UserResponse]`
- `400`: 1: The target user is invalid or does not exist. 6: Invalid parameters.
- `403`: 2: The user is banned from performing operation. 3: The user is blocked from performing this action.
- `429`: 9: The flood limit has been exceeded.

**Response fields** (`Roblox.Web.WebAPI.Models.ApiPageResponse[Roblox.Friends.Api.Models.Response.UserResponse]`)

See [Roblox.Web.WebAPI.Models.ApiPageResponse[Roblox.Friends.Api.Models.Response.UserResponse]](#roblox-web-webapi-models-apipageresponse-roblox-friends-api-models-response-userresponse-) in Models.

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
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://friends.roblox.com/v1/users/{TARGETUSERID}/followings"
```

### GET `/v1/users/{targetUserId}/followings/count`

Get the number of following a user has

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `targetUserId` | path | `integer (int64)` | Yes |  |

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
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://friends.roblox.com/v1/users/{TARGETUSERID}/followings/count"
```

### GET `/v1/users/{userId}/friends`

Get list of all friends for the specified user.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer (int64)` | Yes | The user Id to get the friends for. |
| `userSort` | query | `integer (int32)` | No | Specifies how to sort the returned friends. Valid values: `0`, `1`, `2` |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.Friends.Api.Models.Response.UserResponse]`
- `400`: 1: The target user is invalid or does not exist.

**Response fields** (`Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.Friends.Api.Models.Response.UserResponse]`)

See [Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.Friends.Api.Models.Response.UserResponse]](#roblox-web-webapi-models-apiarrayresponse-roblox-friends-api-models-response-userresponse-) in Models.

**Response example:**
```json
{
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

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://friends.roblox.com/v1/users/{USERID}/friends"
```

### GET `/v1/users/{userId}/friends/count`

Get the number of friends a user has

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer (int64)` | Yes |  |

**Responses:**

- `200`: OK → `Roblox.Friends.Api.FriendsCountResponse`
- `400`: 1: The target user is invalid or does not exist.

**Response fields** (`Roblox.Friends.Api.FriendsCountResponse`)

See [Roblox.Friends.Api.FriendsCountResponse](#roblox-friends-api-friendscountresponse) in Models.

**Response example:**
```json
{
  "count": 0
}
```

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://friends.roblox.com/v1/users/{USERID}/friends/count"
```

### GET `/v1/users/{userId}/friends/find`

Get a paginated list of all friends for the specified user.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer (int64)` | Yes | The user Id to get the friends for. |
| `userSort` | query | `integer (int32)` | No | Specifies how to sort the returned friends. Valid values: `0`, `1`, `2` |
| `cursor` | query | `string` | No | The paging cursor for the previous or next page. |
| `limit` | query | `integer (int32)` | No | The number of results per request. |
| `findFriendsType` | query | `integer (int32)` | No | ['FindFriends' = 0, 'FindTrustedFriends' = 1] Valid values: `0`, `1` |

**Responses:**

- `200`: OK → `Roblox.Paging.CursoredPagedResult[Roblox.Friends.Api.Models.Response.FriendResponse]`
- `400`: 1: The target user is invalid or does not exist. 6: Invalid parameters.

**Response fields** (`Roblox.Paging.CursoredPagedResult[Roblox.Friends.Api.Models.Response.FriendResponse]`)

See [Roblox.Paging.CursoredPagedResult[Roblox.Friends.Api.Models.Response.FriendResponse]](#roblox-paging-cursoredpagedresult-roblox-friends-api-models-response-friendresponse-) in Models.

**Response example:**
```json
{
  "PreviousCursor": "string",
  "PageItems": [
    {
      "id": "...",
      "hasVerifiedBadge": "..."
    }
  ],
  "NextCursor": "string",
  "HasMore": false
}
```

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://friends.roblox.com/v1/users/{USERID}/friends/find"
```

### GET `/v1/users/{userId}/friends/inactive`

Get list of inactive friends for the specified user.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer (int64)` | Yes | The user Id to get the friends for. |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.Friends.Api.Models.Response.UserResponse]`
- `400`: 1: The target user is invalid or does not exist. 6: Invalid parameters.
- `401`: 0: Authorization has been denied for this request.

**Response fields** (`Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.Friends.Api.Models.Response.UserResponse]`)

See [Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.Friends.Api.Models.Response.UserResponse]](#roblox-web-webapi-models-apiarrayresponse-roblox-friends-api-models-response-userresponse-) in Models.

**Response example:**
```json
{
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

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://friends.roblox.com/v1/users/{USERID}/friends/inactive"
```

### GET `/v1/users/{userId}/friends/online`

Get list of all online friends for the specified user.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer (int64)` | Yes | The user Id to get the friends for. |
| `userSort` | query | `integer (int32)` | No | The sort order to return the friends. Valid values: `0`, `1`, `2` |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.Friends.Api.Models.Response.UserPresenceResponse]`
- `400`: 1: The target user is invalid or does not exist. 6: Invalid parameters.
- `401`: 0: Authorization has been denied for this request.

**Response fields** (`Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.Friends.Api.Models.Response.UserPresenceResponse]`)

See [Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.Friends.Api.Models.Response.UserPresenceResponse]](#roblox-web-webapi-models-apiarrayresponse-roblox-friends-api-models-response-userpresenceresponse-) in Models.

**Response example:**
```json
{
  "data": [
    {
      "userPresence": "...",
      "sortScore": "...",
      "id": "...",
      "name": "...",
      "displayName": "..."
    }
  ]
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://friends.roblox.com/v1/users/{USERID}/friends/online"
```

### GET `/v1/users/{userId}/friends/search`

Search for friends by name using a text query.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer (int64)` | Yes | The user Id to get the friends for. |
| `query` | query | `string` | No | The string to search names of friends for. |
| `cursor` | query | `string` | No | The paging cursor for the previous or next page. |
| `limit` | query | `integer (int32)` | No | The number of results per request. |

**Responses:**

- `200`: OK → `Roblox.Paging.CursoredPagedResult[Roblox.Friends.Api.Models.Response.FriendResponse]`
- `400`: 1: The target user is invalid or does not exist. 6: Invalid parameters.
- `401`: 0: Authorization has been denied for this request.

**Response fields** (`Roblox.Paging.CursoredPagedResult[Roblox.Friends.Api.Models.Response.FriendResponse]`)

See [Roblox.Paging.CursoredPagedResult[Roblox.Friends.Api.Models.Response.FriendResponse]](#roblox-paging-cursoredpagedresult-roblox-friends-api-models-response-friendresponse-) in Models.

**Response example:**
```json
{
  "PreviousCursor": "string",
  "PageItems": [
    {
      "id": "...",
      "hasVerifiedBadge": "..."
    }
  ],
  "NextCursor": "string",
  "HasMore": false
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://friends.roblox.com/v1/users/{USERID}/friends/search"
```

### GET `/v1/users/{userId}/friends/statuses`

Gets a list of friend statuses of specified users against the specified user.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer (int64)` | Yes | The user to check the friend statuses against. |
| `userIds` | query | `array` | Yes |  |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.Friends.Api.FriendStatusResponse]`
- `400`: 1: The target user is invalid or does not exist. 15: Too many ids. 16: Invalid ids.

**Response fields** (`Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.Friends.Api.FriendStatusResponse]`)

See [Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.Friends.Api.FriendStatusResponse]](#roblox-web-webapi-models-apiarrayresponse-roblox-friends-api-friendstatusresponse-) in Models.

**Response example:**
```json
{
  "data": [
    {
      "id": "...",
      "status": "..."
    }
  ]
}
```

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://friends.roblox.com/v1/users/{USERID}/friends/statuses?userIds={VALUE}"
```

### GET `/v1/users/{userId}/trusted-friends/count`

Get the number of trusted friends a user has

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer (int64)` | Yes |  |

**Responses:**

- `200`: OK → `Roblox.Friends.Api.FriendsCountResponse`
- `401`: 0: Authorization has been denied for this request.

**Response fields** (`Roblox.Friends.Api.FriendsCountResponse`)

See [Roblox.Friends.Api.FriendsCountResponse](#roblox-friends-api-friendscountresponse) in Models.

**Response example:**
```json
{
  "count": 0
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://friends.roblox.com/v1/users/{USERID}/trusted-friends/count"
```

### POST `/v1/my/friends/refresh-qr-session`

**Responses:**

- `200`: OK → `Roblox.Friends.Api.Models.Response.RefreshQrSessionResponse`
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed

**Response fields** (`Roblox.Friends.Api.Models.Response.RefreshQrSessionResponse`)

See [Roblox.Friends.Api.Models.Response.RefreshQrSessionResponse](#roblox-friends-api-models-response-refreshqrsessionresponse) in Models.

**Response example:**
```json
{
  "Success": false
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://friends.roblox.com/v1/my/friends/refresh-qr-session"
```

### POST `/v1/user/{userId}/multiget-are-friends`

Check if the requesting user is friends with the specified users.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer (int64)` | Yes | The requesting userId. |

**Request Body:** `application/json` — Type: `Roblox.Friends.Api.MultigetAreFriendsRequestModel`

See [Roblox.Friends.Api.MultigetAreFriendsRequestModel](#roblox-friends-api-multigetarefriendsrequestmodel) in Models.

**Request example:**
```json
{
  "targetUserIds": [
    0
  ]
}
```

**Responses:**

- `200`: OK → `Roblox.Friends.Api.MultigetAreFriendsResponse`
- `400`: 1: The target user is invalid or does not exist.
- `403`: 0: Token Validation Failed

**Response fields** (`Roblox.Friends.Api.MultigetAreFriendsResponse`)

See [Roblox.Friends.Api.MultigetAreFriendsResponse](#roblox-friends-api-multigetarefriendsresponse) in Models.

**Response example:**
```json
{
  "friendsId": [
    0
  ]
}
```

**Error handling:** `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://friends.roblox.com/v1/user/{USERID}/multiget-are-friends" \
  -H "Content-Type: application/json" \
  -d '{
  "targetUserIds": [
    0
  ]
}'
```

### POST `/v1/user/following-exists`

Returns whether or not the current user is following each userId in a list of userIds

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
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
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

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `targetUserId` | path | `integer (int64)` | Yes |  |

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
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://friends.roblox.com/v1/users/{TARGETUSERID}/follow" \
  -H "Content-Type: application/json" \
  -d '{
  "captchaId": "string",
  "captchaToken": "string",
  "captchaProvider": "string",
  "challengeId": "string"
}'
```

### POST `/v1/users/{targetUserId}/unfollow`

Deletes the following between a user and user with targetUserId

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `targetUserId` | path | `integer (int64)` | Yes |  |

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
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://friends.roblox.com/v1/users/{TARGETUSERID}/unfollow"
```

## Models

### Roblox.Friends.Api.CaptchaStatusResponseModel

This is response model to notify when action succeeded, failed, or captcha is required

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | `boolean` | No |  |
| `isCaptchaRequired` | `boolean` | No | Captcha is set to true if captcha is required from user to perform action |
| `notificationMuted` | `boolean` | No |  |

### Roblox.Friends.Api.FollowCountResponse

Response model for following or followers Count

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `count` | `integer` | No | Count of following or followers |

### Roblox.Friends.Api.FollowingExistsRequestModel

Request model for FollowingExists endpoint

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `targetUserIds` | `integer[]` | No | The userIds which the user may or may not be following. |

### Roblox.Friends.Api.FriendRequest

A response model representing a friend request.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `sentAt` | `string` | No | When the friend request was sent. |
| `senderId` | `integer` | No | The sender user Id. |
| `sourceUniverseId` | `integer` | No | The source universe Id which the request was sent in. |
| `originSourceType` | `integer enum (14 values)` | No | The origin source type associated with the friend request. ['Unknown' = 0, 'PlayerSearch' = 1, 'QrCode' = 2, 'InGame' = 3, 'UserProfile' = 4, 'QqContactImporter' = 5, 'WeChatContactImporter' = 6, 'ProfileShare' = 7, 'PhoneContactImporter' = 8, 'FriendRecommendations' = 9, 'UserCommunities' = 10, 'TrustedFriend' = 11, 'SchoolMemberList' = 12, 'SocialTabsPage' = 13] Values: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 |
| `contactName` | `string` | No | The contact name associated with the friend request. |
| `senderNickname` | `string` | No | The nickname associated with the friend request. |

### Roblox.Friends.Api.FriendRequestResponse

A response model representing a friend request.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `friendRequest` | `Roblox.Friends.Api.FriendRequest` | No |  |
| `mutualFriendsList` | `string[]` | No | mutualFriendsList |
| `hasVerifiedBadge` | `boolean` | No | The user's verified badge status. |
| `isUnseen` | `boolean` | No | The user's verified badge status. |
| `description` | `string` | No | The user description. |
| `created` | `string` | No | When the user signed up. |
| `isBanned` | `boolean` | No | Whether or not the user is banned |
| `externalAppDisplayName` | `string` | No | Used when user is logged in from third party app (e.g. QQ) ExternalAppDisplayName is the name used in that app (e.g. QQ nickname) |
| `id` | `integer` | No | The user Id. |
| `name` | `string` | No | The user name. |
| `displayName` | `string` | No | The user DisplayName. |

### Roblox.Friends.Api.FriendStatusResponse

The friendship status response model.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | `integer` | No | The user Id of the friend. |
| `status` | `0 \| 1 \| 2 \| 3` | No | The friendship status. ['NotFriends' = 0, 'Friends' = 1, 'RequestSent' = 2, 'RequestReceived' = 3] |

### Roblox.Friends.Api.FriendsCountResponse

Response model for Friends Count

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `count` | `integer` | No | Count of friends |

### Roblox.Friends.Api.Models.Response.FollowingExistsResponse

Response contained in list for FollowingExists endpoint. Corresponds to a single userId.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `isFollowing` | `boolean` | No | Whether or not a user is following userId in FriendsController.FollowingExists |
| `isFollowed` | `boolean` | No | Whether or not a user is followed by userId in FriendsController.FollowingExists |
| `userId` | `integer` | No | The userId being potentially followed |

### Roblox.Friends.Api.Models.Response.FollowingExistsResponseModel

Response model for FollowingExists endpoint.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `followings` | `Roblox.Friends.Api.Models.Response.FollowingExistsResponse[]` | No | A list of userIds and whether or not the given user is following them. |

### Roblox.Friends.Api.Models.Response.FriendResponse

A response model representing friend information

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | `integer` | No | The friend's userId |
| `hasVerifiedBadge` | `boolean` | No | The friend's verified badge status. |

### Roblox.Friends.Api.Models.Response.FriendsPageMetadataResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `isFriendsFilterBarEnabled` | `boolean` | No |  |
| `isFriendsPageSortExperimentEnabled` | `boolean` | No |  |
| `isFriendsUserDataStoreCacheEnabled` | `boolean` | No |  |
| `frequentFriendSortRollout` | `integer` | No |  |
| `userName` | `string` | No |  |
| `displayName` | `string` | No |  |

### Roblox.Friends.Api.Models.Response.NewFriendRequestsCountResponse

The friendship status response model.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `count` | `integer` | No | Count of new friend requests. |

### Roblox.Friends.Api.Models.Response.RefreshQrSessionResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `Success` | `boolean` | No |  |

### Roblox.Friends.Api.Models.Response.TrustedFriendRequestResponse

A response model representing a friend request.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `sentAt` | `string` | No | When the TF request was sent. |
| `senderId` | `integer` | No | The sender user Id. |

### Roblox.Friends.Api.Models.Response.UserPresenceResponse

A response model representing user presence information.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `userPresence` | `Roblox.Friends.Api.Models.Response.UserPresenceResponseModel` | No |  |
| `sortScore` | `number` | No | Carousel sort score |
| `id` | `integer` | No | The user Id. |
| `name` | `string` | No | The user name. |
| `displayName` | `string` | No | The user DisplayName. |

### Roblox.Friends.Api.Models.Response.UserPresenceResponseModel

Response model for !:IUserPresence objects

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `UserPresenceType` | `string` | No | User Presence Type |
| `UserLocationType` | `string` | No | Location Type |
| `lastLocation` | `string` | No | Last Location |
| `placeId` | `integer` | No | Place Id |
| `rootPlaceId` | `integer` | No | Root Place Id |
| `gameInstanceId` | `string` | No | Game Instance Id |
| `universeId` | `integer` | No | Universe Id |
| `lastOnline` | `string` | No | Most recent time online |

### Roblox.Friends.Api.Models.Response.UserResponse

A response model representing user information that also contains select presence information

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `isOnline` | `boolean` | No | Whether the user is online. |
| `presenceType` | `0 \| 1 \| 2 \| 3 \| 4` | No | Where the user is online. |
| `isDeleted` | `boolean` | No | Whether the user is deleted. |
| `friendFrequentScore` | `integer` | No | Frequents value for the user. |
| `friendFrequentRank` | `integer` | No | Frequents rank for the user. |
| `hasVerifiedBadge` | `boolean` | No | The user's verified badge status. |
| `description` | `string` | No | The user description. |
| `created` | `string` | No | When the user signed up. |
| `isBanned` | `boolean` | No | Whether or not the user is banned |
| `externalAppDisplayName` | `string` | No | Used when user is logged in from third party app (e.g. QQ) ExternalAppDisplayName is the name used in that app (e.g. QQ nickname) |
| `id` | `integer` | No | The user Id. |
| `name` | `string` | No | The user name. |
| `displayName` | `string` | No | The user DisplayName. |

### Roblox.Friends.Api.MultigetAreFriendsRequestModel

Request model for MultigetAreFriends endpoint

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `targetUserIds` | `integer[]` | No | The target userIds to check against with the requesting user regarding friendship. |

### Roblox.Friends.Api.MultigetAreFriendsResponse

Response model for MultigetAreFriendsResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `friendsId` | `integer[]` | No | friends id list |

### Roblox.Friends.Api.PendingFriendRequestCountModel

Response model for Pending Friend Request Count

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `count` | `integer` | No | Count of pending friend requests |

### Roblox.Paging.CursoredPagedResult[Roblox.Friends.Api.Models.Response.FriendResponse]

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `PreviousCursor` | `string` | No |  |
| `PageItems` | `Roblox.Friends.Api.Models.Response.FriendResponse[]` | No |  |
| `NextCursor` | `string` | No |  |
| `HasMore` | `boolean` | No |  |

### Roblox.Web.Captcha.Models.Request.CaptchaTokenRequest

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `captchaId` | `string` | No |  |
| `captchaToken` | `string` | No |  |
| `captchaProvider` | `string` | No |  |
| `challengeId` | `string` | No |  |

### Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.Friends.Api.FriendStatusResponse]

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | `Roblox.Friends.Api.FriendStatusResponse[]` | No |  |

### Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.Friends.Api.Models.Response.UserPresenceResponse]

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | `Roblox.Friends.Api.Models.Response.UserPresenceResponse[]` | No |  |

### Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.Friends.Api.Models.Response.UserResponse]

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | `Roblox.Friends.Api.Models.Response.UserResponse[]` | No |  |

### Roblox.Web.WebAPI.Models.ApiPageResponse[Roblox.Friends.Api.FriendRequestResponse]

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `previousPageCursor` | `string` | No |  |
| `nextPageCursor` | `string` | No |  |
| `data` | `Roblox.Friends.Api.FriendRequestResponse[]` | No |  |

### Roblox.Web.WebAPI.Models.ApiPageResponse[Roblox.Friends.Api.Models.Response.TrustedFriendRequestResponse]

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `previousPageCursor` | `string` | No |  |
| `nextPageCursor` | `string` | No |  |
| `data` | `Roblox.Friends.Api.Models.Response.TrustedFriendRequestResponse[]` | No |  |

### Roblox.Web.WebAPI.Models.ApiPageResponse[Roblox.Friends.Api.Models.Response.UserResponse]

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `previousPageCursor` | `string` | No |  |
| `nextPageCursor` | `string` | No |  |
| `data` | `Roblox.Friends.Api.Models.Response.UserResponse[]` | No |  |