---
name: "Bans and blocks"
last_updated: 2026-10-30T19:56:08Z
type: feature
api_base_url: "https://apis.roblox.com"
endpoints: 15
auth: [api-key, oauth2, cookie]
description: "Manage user restrictions using the Ban API, which includes real-time alt account detection"
---

# Bans and blocks

Manage user restrictions using the Ban API, which includes real-time alt account detection. [Universe-level bans](#Cloud_UpdateUserRestriction__Using_Universes) affect all places, while [place-level bans](#Cloud_UpdateUserRestriction__Using_Universes_Places) allow granular control. Bans can also be managed via the Creator Hub dashboard.

Ban users with customizable duration and reasons, and [review moderation history](#Cloud_ListUserRestrictionLogs) for any banned users.

> **See also:** To user profiles and display names, see [user-profiles](/docs/cloud/reference/features/user-profiles.md).

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

### GET `/cloud/v2/universes/{universe_id}/places/{place_id}/user-restrictions` [BETA]

List User Restrictions

List user restrictions for users that have ever been banned in either a
universe or a specific place.

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `universe.user-restriction:read`, `universe.user-restriction:read`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universe_id` | path | `string` | Yes | The universe ID. |
| `place_id` | path | `string` | Yes | The place ID. |
| `maxPageSize` | query | `integer` | No | The maximum number of user restrictions to return. The service might return fewer than this value. If unspecified, at most 10 user restrictions are returned. The maximum value is 100 and higher values are set to 100. |
| `pageToken` | query | `string` | No | A page token, received from a previous call, to retrieve a subsequent page.  When paginating, all other parameters provided to the subsequent call must match the call that provided the page token. |

**Responses:**

- `200`: OK → `ListUserRestrictionsResponse`

**Response fields** (`ListUserRestrictionsResponse`)

See [ListUserRestrictionsResponse](#listuserrestrictionsresponse) in Models.

**Response example:**
```json
{
  "userRestrictions": [
    {
      "path": "...",
      "updateTime": "...",
      "user": "...",
      "gameJoinRestriction": "..."
    }
  ],
  "nextPageToken": "string"
}
```

**Rate Limits:** perApiKeyOwner: 150/second, perOauth2Authorization: 30/second
**Rate Limit Note:** User Restrictions are subject to the additional rate limits, applied per universe

* Get User Restriction: 50 req/s
* List User Restrictions: 50 req/s
* Update User Restrictions: 10 req/s
* List User Restriction Logs: 50 req/s

Additionally, we impose the following rate limit for the same user within a universe:

* Update User Restriction: 2 req/min

For example, Update User Restriction may not be called for user 123 more than twice every minute.

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/cloud/v2/universes/{UNIVERSE_ID}/places/{PLACE_ID}/user-restrictions"
```

### GET `/cloud/v2/universes/{universe_id}/places/{place_id}/user-restrictions/{user_restriction_id}` [BETA]

Get User Restriction

Get the user restriction.

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `universe.user-restriction:read`, `universe.user-restriction:read`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universe_id` | path | `string` | Yes | The universe ID. |
| `place_id` | path | `string` | Yes | The place ID. |
| `user_restriction_id` | path | `string` | Yes | The user-restriction ID. |

**Responses:**

- `200`: OK → `UserRestriction`

**Response fields** (`UserRestriction`)

See [UserRestriction](#userrestriction) in Models.

**Response example:**
```json
{
  "path": "string",
  "updateTime": "2024-01-01T00:00:00Z",
  "user": "string",
  "gameJoinRestriction": {
    "active": false,
    "startTime": "2024-01-01T00:00:00Z",
    "duration": "string",
    "privateReason": "string",
    "displayReason": "string",
    "excludeAltAccounts": false
  }
}
```

**Rate Limits:** perApiKeyOwner: 150/second, perOauth2Authorization: 30/second
**Rate Limit Note:** User Restrictions are subject to the additional rate limits, applied per universe

* Get User Restriction: 50 req/s
* List User Restrictions: 50 req/s
* Update User Restrictions: 10 req/s
* List User Restriction Logs: 50 req/s

Additionally, we impose the following rate limit for the same user within a universe:

* Update User Restriction: 2 req/min

For example, Update User Restriction may not be called for user 123 more than twice every minute.

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/cloud/v2/universes/{UNIVERSE_ID}/places/{PLACE_ID}/user-restrictions/{USER_RESTRICTION_ID}"
```

### PATCH `/cloud/v2/universes/{universe_id}/places/{place_id}/user-restrictions/{user_restriction_id}` [BETA]

Update User Restriction

Update the user restriction.

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `universe.user-restriction:write`, `universe.user-restriction:write`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universe_id` | path | `string` | Yes | The universe ID. |
| `place_id` | path | `string` | Yes | The place ID. |
| `user_restriction_id` | path | `string` | Yes | The user-restriction ID. |
| `updateMask` | query | `string` | No | The list of fields to update.  The `game_join_restriction` field must be updated atomically; field masks that index into `game_join_restriction` (such as `"game_join_restriction.active"`) are not supported. |
| `idempotencyKey.key` | query | `string` | No | The unique key to use for idempotency. |
| `idempotencyKey.firstSent` | query | `string` | No | The timestamp at which the first request was sent.  If this is further in the past than the lifetime of the idempotency key (which *may* exceed the annotated minimum lifetime), the server *must* return an error. |

**Request Body:** `application/json` — Type: `UserRestriction`

See [UserRestriction](#userrestriction) in Models.

**Request example:**
```json
{
  "path": "string",
  "updateTime": "2024-01-01T00:00:00Z",
  "user": "string",
  "gameJoinRestriction": {
    "active": false,
    "startTime": "2024-01-01T00:00:00Z",
    "duration": "string",
    "privateReason": "string",
    "displayReason": "string",
    "excludeAltAccounts": false
  }
}
```

**Responses:**

- `200`: OK → `UserRestriction`

**Response fields** (`UserRestriction`)

See [UserRestriction](#userrestriction) in Models.

**Response example:**
```json
{
  "path": "string",
  "updateTime": "2024-01-01T00:00:00Z",
  "user": "string",
  "gameJoinRestriction": {
    "active": false,
    "startTime": "2024-01-01T00:00:00Z",
    "duration": "string",
    "privateReason": "string",
    "displayReason": "string",
    "excludeAltAccounts": false
  }
}
```

**Rate Limits:** perApiKeyOwner: 150/second, perOauth2Authorization: 30/second
**Rate Limit Note:** User Restrictions are subject to the additional rate limits, applied per universe

* Get User Restriction: 50 req/s
* List User Restrictions: 50 req/s
* Update User Restrictions: 10 req/s
* List User Restriction Logs: 50 req/s

Additionally, we impose the following rate limit for the same user within a universe:

* Update User Restriction: 2 req/min

For example, Update User Restriction may not be called for user 123 more than twice every minute.

**Example:**
```bash
curl -X PATCH -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/cloud/v2/universes/{UNIVERSE_ID}/places/{PLACE_ID}/user-restrictions/{USER_RESTRICTION_ID}" \
  -H "Content-Type: application/json" \
  -d '{
  "path": "string",
  "updateTime": "2024-01-01T00:00:00Z",
  "user": "string",
  "gameJoinRestriction": {
    "active": false,
    "startTime": "2024-01-01T00:00:00Z",
    "duration": "string",
    "privateReason": "string",
    "displayReason": "string",
    "excludeAltAccounts": false
  }
}'
```

### GET `/cloud/v2/universes/{universe_id}/user-restrictions` [BETA]

List User Restrictions

List user restrictions for users that have ever been banned in either a
universe or a specific place.

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `universe.user-restriction:read`, `universe.user-restriction:read`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universe_id` | path | `string` | Yes | The universe ID. |
| `maxPageSize` | query | `integer` | No | The maximum number of user restrictions to return. The service might return fewer than this value. If unspecified, at most 10 user restrictions are returned. The maximum value is 100 and higher values are set to 100. |
| `pageToken` | query | `string` | No | A page token, received from a previous call, to retrieve a subsequent page.  When paginating, all other parameters provided to the subsequent call must match the call that provided the page token. |

**Responses:**

- `200`: OK → `ListUserRestrictionsResponse`

**Response fields** (`ListUserRestrictionsResponse`)

See [ListUserRestrictionsResponse](#listuserrestrictionsresponse) in Models.

**Response example:**
```json
{
  "userRestrictions": [
    {
      "path": "...",
      "updateTime": "...",
      "user": "...",
      "gameJoinRestriction": "..."
    }
  ],
  "nextPageToken": "string"
}
```

**Rate Limits:** perApiKeyOwner: 150/second, perOauth2Authorization: 30/second
**Rate Limit Note:** User Restrictions are subject to the additional rate limits, applied per universe

* Get User Restriction: 50 req/s
* List User Restrictions: 50 req/s
* Update User Restrictions: 10 req/s
* List User Restriction Logs: 50 req/s

Additionally, we impose the following rate limit for the same user within a universe:

* Update User Restriction: 2 req/min

For example, Update User Restriction may not be called for user 123 more than twice every minute.

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/cloud/v2/universes/{UNIVERSE_ID}/user-restrictions"
```

### GET `/cloud/v2/universes/{universe_id}/user-restrictions/{user_restriction_id}` [BETA]

Get User Restriction

Get the user restriction.

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `universe.user-restriction:read`, `universe.user-restriction:read`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universe_id` | path | `string` | Yes | The universe ID. |
| `user_restriction_id` | path | `string` | Yes | The user-restriction ID. |

**Responses:**

- `200`: OK → `UserRestriction`

**Response fields** (`UserRestriction`)

See [UserRestriction](#userrestriction) in Models.

**Response example:**
```json
{
  "path": "string",
  "updateTime": "2024-01-01T00:00:00Z",
  "user": "string",
  "gameJoinRestriction": {
    "active": false,
    "startTime": "2024-01-01T00:00:00Z",
    "duration": "string",
    "privateReason": "string",
    "displayReason": "string",
    "excludeAltAccounts": false
  }
}
```

**Rate Limits:** perApiKeyOwner: 150/second, perOauth2Authorization: 30/second
**Rate Limit Note:** User Restrictions are subject to the additional rate limits, applied per universe

* Get User Restriction: 50 req/s
* List User Restrictions: 50 req/s
* Update User Restrictions: 10 req/s
* List User Restriction Logs: 50 req/s

Additionally, we impose the following rate limit for the same user within a universe:

* Update User Restriction: 2 req/min

For example, Update User Restriction may not be called for user 123 more than twice every minute.

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/cloud/v2/universes/{UNIVERSE_ID}/user-restrictions/{USER_RESTRICTION_ID}"
```

### PATCH `/cloud/v2/universes/{universe_id}/user-restrictions/{user_restriction_id}` [BETA]

Update User Restriction

Update the user restriction.

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `universe.user-restriction:write`, `universe.user-restriction:write`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universe_id` | path | `string` | Yes | The universe ID. |
| `user_restriction_id` | path | `string` | Yes | The user-restriction ID. |
| `updateMask` | query | `string` | No | The list of fields to update.  The `game_join_restriction` field must be updated atomically; field masks that index into `game_join_restriction` (such as `"game_join_restriction.active"`) are not supported. |
| `idempotencyKey.key` | query | `string` | No | The unique key to use for idempotency. |
| `idempotencyKey.firstSent` | query | `string` | No | The timestamp at which the first request was sent.  If this is further in the past than the lifetime of the idempotency key (which *may* exceed the annotated minimum lifetime), the server *must* return an error. |

**Request Body:** `application/json` — Type: `UserRestriction`

See [UserRestriction](#userrestriction) in Models.

**Request example:**
```json
{
  "path": "string",
  "updateTime": "2024-01-01T00:00:00Z",
  "user": "string",
  "gameJoinRestriction": {
    "active": false,
    "startTime": "2024-01-01T00:00:00Z",
    "duration": "string",
    "privateReason": "string",
    "displayReason": "string",
    "excludeAltAccounts": false
  }
}
```

**Responses:**

- `200`: OK → `UserRestriction`

**Response fields** (`UserRestriction`)

See [UserRestriction](#userrestriction) in Models.

**Response example:**
```json
{
  "path": "string",
  "updateTime": "2024-01-01T00:00:00Z",
  "user": "string",
  "gameJoinRestriction": {
    "active": false,
    "startTime": "2024-01-01T00:00:00Z",
    "duration": "string",
    "privateReason": "string",
    "displayReason": "string",
    "excludeAltAccounts": false
  }
}
```

**Rate Limits:** perApiKeyOwner: 150/second, perOauth2Authorization: 30/second
**Rate Limit Note:** User Restrictions are subject to the additional rate limits, applied per universe

* Get User Restriction: 50 req/s
* List User Restrictions: 50 req/s
* Update User Restrictions: 10 req/s
* List User Restriction Logs: 50 req/s

Additionally, we impose the following rate limit for the same user within a universe:

* Update User Restriction: 2 req/min

For example, Update User Restriction may not be called for user 123 more than twice every minute.

**Example:**
```bash
curl -X PATCH -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/cloud/v2/universes/{UNIVERSE_ID}/user-restrictions/{USER_RESTRICTION_ID}" \
  -H "Content-Type: application/json" \
  -d '{
  "path": "string",
  "updateTime": "2024-01-01T00:00:00Z",
  "user": "string",
  "gameJoinRestriction": {
    "active": false,
    "startTime": "2024-01-01T00:00:00Z",
    "duration": "string",
    "privateReason": "string",
    "displayReason": "string",
    "excludeAltAccounts": false
  }
}'
```

### GET `/cloud/v2/universes/{universe_id}/user-restrictions:listLogs` [BETA]

List User Restriction Logs

List changes to UserRestriction resources within a given universe.
This includes both universe-level and place-level restrictions.

For universe-level restriction logs, the `place` field will be empty.

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `universe.user-restriction:read`, `universe.user-restriction:read`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universe_id` | path | `string` | Yes | The universe ID. |
| `maxPageSize` | query | `integer` | No | The maximum number of UserRestrictionLogs to return. The service may return fewer than this value. If unspecified, at most 10 UserRestrictionLogs are returned. The maximum value is 100 and higher values are set to 100. |
| `pageToken` | query | `string` | No | A page token, received from a previous call, to retrieve a subsequent page.  When paginating, all other parameters provided to the subsequent call must match the call that provided the page token. |
| `filter` | query | `string` | No | This field may be set to filter the logs returned.  The `filter` field supports a very small number of CEL:  * `user` * `place` * The `==` comparison operator is available. * The `&&` logical operator is also supported.  As an example, filtering for a user and a place takes the form `filter="user == 'users/123'" && "place == 'places/456'"` |

**Responses:**

- `200`: OK → `ListUserRestrictionLogsResponse`

**Response fields** (`ListUserRestrictionLogsResponse`)

See [ListUserRestrictionLogsResponse](#listuserrestrictionlogsresponse) in Models.

**Response example:**
```json
{
  "logs": [
    {
      "user": "...",
      "place": "...",
      "moderator": "...",
      "createTime": "...",
      "active": "...",
      "startTime": "..."
    }
  ],
  "nextPageToken": "string"
}
```

**Rate Limits:** perApiKeyOwner: 150/second, perOauth2Authorization: 30/second
**Rate Limit Note:** User Restrictions are subject to the additional rate limits, applied per universe

* Get User Restriction: 50 req/s
* List User Restrictions: 50 req/s
* Update User Restrictions: 10 req/s
* List User Restriction Logs: 50 req/s

Additionally, we impose the following rate limit for the same user within a universe:

* Update User Restriction: 2 req/min

For example, Update User Restriction may not be called for user 123 more than twice every minute.

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/cloud/v2/universes/{UNIVERSE_ID}/user-restrictions:listLogs"
```

### GET `/v1/groups/{groupId}/bans`

Gets the bans for the group

**Server:** `https://groups.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer` | Yes | The group Id. |
| `limit` | query | `10 \| 25 \| 50 \| 100` | No | The number of results per request. Valid values: `10`, `25`, `50`, `100` |
| `cursor` | query | `string` | No | The paging cursor for the previous or next page. |
| `sortOrder` | query | `Asc \| Desc` | No | The order the results are sorted in. Valid values: `Asc`, `Desc` |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.Groups.Api.GroupBanMemberResponse_`
- `401`: 0: Authorization has been denied for this request.
- `403`: 19: You have insufficient permissions for this request.
- `404`: 1: The group is invalid or does not exist.
- `405`: 18: The operation is temporarily unavailable. Please try again later.

**Response fields** (`Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.Groups.Api.GroupBanMemberResponse_`)

See [Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.Groups.Api.GroupBanMemberResponse_](#roblox-web-webapi-models-apipageresponse-roblox-groups-api-groupbanmemberresponse-) in Models.

**Response example:**
```json
{
  "previousPageCursor": "string",
  "nextPageCursor": "string",
  "data": [
    {
      "user": "...",
      "actingUser": "...",
      "created": "..."
    }
  ]
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/bans"
```

### GET `/v1/groups/{groupId}/bans/{userId}`

Fetch the group ban of a user from a group

**Server:** `https://groups.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer` | Yes | The group Id. |
| `userId` | path | `integer` | Yes | The user Id. |

**Responses:**

- `200`: OK → `Roblox.Groups.Api.GroupBanMemberResponse`
- `401`: 0: Authorization has been denied for this request.
- `403`: 19: You have insufficient permissions for this request.
- `404`: 1: The group is invalid or does not exist. 3: The user is invalid or does not exist.
- `405`: 18: The operation is temporarily unavailable. Please try again later.

**Response fields** (`Roblox.Groups.Api.GroupBanMemberResponse`)

See [Roblox.Groups.Api.GroupBanMemberResponse](#roblox-groups-api-groupbanmemberresponse) in Models.

**Response example:**
```json
{
  "user": {
    "buildersClubMembershipType": 0,
    "hasVerifiedBadge": false,
    "userId": 0,
    "username": "string",
    "displayName": "string"
  },
  "actingUser": {
    "user": {
      "buildersClubMembershipType": "...",
      "hasVerifiedBadge": "...",
      "userId": "...",
      "username": "...",
      "displayName": "..."
    },
    "role": {
      "id": "...",
      "name": "...",
      "description": "...",
      "rank": "...",
      "memberCount": "...",
      "isBase": "..."
    }
  },
  "created": "2024-01-01T00:00:00Z"
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/bans/{USERID}"
```

### POST `/v1/groups/{groupId}/bans/{userId}`

Bans a user from a group

**Server:** `https://groups.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer` | Yes | The group Id. |
| `userId` | path | `integer` | Yes | The Id of the user being banned. |

**Responses:**

- `200`: OK → `Roblox.Groups.Api.GroupBanMemberResponse`
- `400`: 28: The user is already banned from the group. 31: You cannot perform this action against the group owner.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 19: You have insufficient permissions for this request.
- `404`: 1: The group is invalid or does not exist. 3: The user is invalid or does not exist. 3: The user is invalid or does not exist. 15: User is not a member of the group.
- `405`: 18: The operation is temporarily unavailable. Please try again later.

**Response fields** (`Roblox.Groups.Api.GroupBanMemberResponse`)

See [Roblox.Groups.Api.GroupBanMemberResponse](#roblox-groups-api-groupbanmemberresponse) in Models.

**Response example:**
```json
{
  "user": {
    "buildersClubMembershipType": 0,
    "hasVerifiedBadge": false,
    "userId": 0,
    "username": "string",
    "displayName": "string"
  },
  "actingUser": {
    "user": {
      "buildersClubMembershipType": "...",
      "hasVerifiedBadge": "...",
      "userId": "...",
      "username": "...",
      "displayName": "..."
    },
    "role": {
      "id": "...",
      "name": "...",
      "description": "...",
      "rank": "...",
      "memberCount": "...",
      "isBase": "..."
    }
  },
  "created": "2024-01-01T00:00:00Z"
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/bans/{USERID}"
```

### DELETE `/v1/groups/{groupId}/bans/{userId}`

Unbans a user from a group

**Server:** `https://groups.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer` | Yes | The group Id. |
| `userId` | path | `integer` | Yes | The Id of the user being unbanned. |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: 29: The user is not banned from the group.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 19: You have insufficient permissions for this request.
- `404`: 1: The group is invalid or does not exist.
- `405`: 18: The operation is temporarily unavailable. Please try again later.

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X DELETE -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/bans/{USERID}"
```

### GET `/v1/groups/{groupId}/blocked-keywords`

Retrieves a paginated list of blocked keywords for a specific Group.

**Server:** `https://groups.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer` | Yes |  |
| `limit` | query | `10 \| 25 \| 50 \| 100` | No | The number of results per request. Valid values: `10`, `25`, `50`, `100` |
| `cursor` | query | `string` | No | The paging cursor for the previous or next page. |
| `sortOrder` | query | `Asc \| Desc` | No | The order the results are sorted in. Valid values: `Asc`, `Desc` |

**Responses:**

- `200`: OK → `Roblox.Groups.Api.BlockedKeywordPageResponse_Roblox.Groups.Client.BlockedKeywordModel_`
- `400`: 1: Group is invalid or does not exist. 6: Limit is invalid.
- `401`: 0: Authorization has been denied for this request.
- `403`: 9: User is invalid or does not exist. 10: Insufficient permissions to complete the request.
- `405`: 31: Service is currently unavailable.

**Response fields** (`Roblox.Groups.Api.BlockedKeywordPageResponse_Roblox.Groups.Client.BlockedKeywordModel_`)

See [Roblox.Groups.Api.BlockedKeywordPageResponse_Roblox.Groups.Client.BlockedKeywordModel_](#roblox-groups-api-blockedkeywordpageresponse-roblox-groups-client-blockedkeywordmodel-) in Models.

**Response example:**
```json
{
  "totalActiveKeywordsCount": 0,
  "previousPageCursor": "string",
  "nextPageCursor": "string",
  "data": [
    {
      "id": "...",
      "keyword": "...",
      "createdBy": "...",
      "isPrivate": "...",
      "createdAt": "...",
      "updatedAt": "..."
    }
  ]
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/blocked-keywords"
```

### POST `/v1/groups/{groupId}/blocked-keywords`

Adds new blocked keyword(s) to the specified Group.

**Server:** `https://groups.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer` | Yes |  |

**Request Body:** `application/json` — Type: `Roblox.Groups.Api.CreateBlockedKeywordsRequest`

See [Roblox.Groups.Api.CreateBlockedKeywordsRequest](#roblox-groups-api-createblockedkeywordsrequest) in Models.

**Request example:**
```json
{
  "keywords": "string",
  "isPrivate": false
}
```

**Responses:**

- `200`: OK → `Roblox.Groups.Client.CreateBlockedKeywordsResponse`
- `400`: 1: Group is invalid or does not exist. 2: One or more keywords are invalid. 4: Invalid request. 12: The provided content was moderated.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 8: Insufficient permissions to complete the request. 9: User is invalid or does not exist. 10: Insufficient permissions to complete the request.
- `405`: 31: Service is currently unavailable.
- `409`: 11: There was a conflict in your request.

**Response fields** (`Roblox.Groups.Client.CreateBlockedKeywordsResponse`)

See [Roblox.Groups.Client.CreateBlockedKeywordsResponse](#roblox-groups-client-createblockedkeywordsresponse) in Models.

**Response example:**
```json
{
  "createdKeywords": [
    {
      "id": "...",
      "keyword": "...",
      "createdBy": "...",
      "isPrivate": "...",
      "createdAt": "...",
      "updatedAt": "..."
    }
  ],
  "hadModeratedKeywords": false,
  "hadDuplicateKeywords": false
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/blocked-keywords" \
  -H "Content-Type: application/json" \
  -d '{
  "keywords": "string",
  "isPrivate": false
}'
```

### PATCH `/v1/groups/{groupId}/blocked-keywords/{keywordId}`

Updates an existing blocked keyword for the specified Group.

**Server:** `https://groups.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer` | Yes |  |
| `keywordId` | path | `string` | Yes |  |

**Request Body:** `application/json` — Type: `Roblox.Groups.Api.UpdateBlockedKeywordRequest`

See [Roblox.Groups.Api.UpdateBlockedKeywordRequest](#roblox-groups-api-updateblockedkeywordrequest) in Models.

**Request example:**
```json
{
  "keyword": "string",
  "isPrivate": false
}
```

**Responses:**

- `200`: OK → `Roblox.Groups.Client.BlockedKeywordModel`
- `400`: 1: Group is invalid or does not exist. 3: KeywordId is invalid. 4: Invalid request. 12: The provided content was moderated.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 8: Insufficient permissions to complete the request. 9: User is invalid or does not exist. 10: Insufficient permissions to complete the request.
- `404`: 7: Not found.
- `405`: 31: Service is currently unavailable.
- `409`: 11: There was a conflict in your request.

**Response fields** (`Roblox.Groups.Client.BlockedKeywordModel`)

See [Roblox.Groups.Client.BlockedKeywordModel](#roblox-groups-client-blockedkeywordmodel) in Models.

**Response example:**
```json
{
  "id": "string",
  "keyword": "string",
  "createdBy": 0,
  "isPrivate": false,
  "createdAt": "2024-01-01T00:00:00Z",
  "updatedAt": "2024-01-01T00:00:00Z"
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X PATCH -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/blocked-keywords/{KEYWORDID}" \
  -H "Content-Type: application/json" \
  -d '{
  "keyword": "string",
  "isPrivate": false
}'
```

### DELETE `/v1/groups/{groupId}/blocked-keywords/{keywordId}`

Deletes a specific blocked keyword from the specified Group.

**Server:** `https://groups.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer` | Yes |  |
| `keywordId` | path | `string` | Yes |  |

**Responses:**

- `200`: OK
- `400`: 1: Group is invalid or does not exist. 3: KeywordId is invalid. 4: Invalid request.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 9: User is invalid or does not exist. 10: Insufficient permissions to complete the request.
- `404`: 7: Not found.
- `405`: 31: Service is currently unavailable.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X DELETE -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://groups.roblox.com/v1/groups/{GROUPID}/blocked-keywords/{KEYWORDID}"
```

## Models

### ListUserRestrictionsResponse

A list of UserRestrictions in the parent collection.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `userRestrictions` | `UserRestriction[]` | No | The UserRestrictions from the specified Universe or Place. |
| `nextPageToken` | `string` | No | A token that you can send as a `pageToken` parameter to retrieve the next page. If this field is omitted, there are no subsequent pages. |

### UserRestriction

Represents a restriction on a user.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `path` | `string` | No | The resource path of the user restriction.  Formats: * `universes/{universe_id}/user-restrictions/{user_restriction_id}` * `universes/{universe_id}/places/{place_id}/user-restrictions/{user_restriction_id}` |
| `updateTime` | `string` | No | The timestamp when the user restriction was last updated. |
| `user` | `string` | No | The affected user. |
| `gameJoinRestriction` | `UserRestriction_GameJoinRestriction` | No | The user is banned from the parent universe or place. |

### ListUserRestrictionLogsResponse

Returns a list of change logs applied to UserRestriction resources.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `logs` | `UserRestrictionLog[]` | No | The UserRestrictionLogs from the specified Universe. |
| `nextPageToken` | `string` | No | A token that you can send as a `pageToken` parameter to retrieve the next page. If this field is omitted, there are no subsequent pages. |

### Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.Groups.Api.GroupBanMemberResponse_

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `previousPageCursor` | `string` | No |  |
| `nextPageCursor` | `string` | No |  |
| `data` | `Roblox.Groups.Api.GroupBanMemberResponse[]` | No |  |

### Roblox.Groups.Api.GroupBanMemberResponse

A ban member from group response

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `user` | `Roblox.Groups.Api.Models.Response.UserModel` | No |  |
| `actingUser` | `Roblox.Groups.Api.UserGroupRoleResponse` | No |  |
| `created` | `string` | No | The group ban's created time |

### Roblox.Groups.Api.BlockedKeywordPageResponse_Roblox.Groups.Client.BlockedKeywordModel_

ApiPageResponse for blocked keywords

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `totalActiveKeywordsCount` | `integer` | No | Total number of active keywords in the group |
| `previousPageCursor` | `string` | No |  |
| `nextPageCursor` | `string` | No |  |
| `data` | `Roblox.Groups.Client.BlockedKeywordModel[]` | No |  |

### Roblox.Groups.Api.CreateBlockedKeywordsRequest

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `keywords` | `string` | No |  |
| `isPrivate` | `boolean` | No |  |

### Roblox.Groups.Client.CreateBlockedKeywordsResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `createdKeywords` | `Roblox.Groups.Client.BlockedKeywordModel[]` | No |  |
| `hadModeratedKeywords` | `boolean` | No |  |
| `hadDuplicateKeywords` | `boolean` | No |  |

### Roblox.Groups.Api.UpdateBlockedKeywordRequest

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `keyword` | `string` | No |  |
| `isPrivate` | `boolean` | No |  |

### Roblox.Groups.Client.BlockedKeywordModel

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | `string` | No |  |
| `keyword` | `string` | No |  |
| `createdBy` | `integer` | No |  |
| `isPrivate` | `boolean` | No |  |
| `createdAt` | `string` | No |  |
| `updatedAt` | `string` | No |  |