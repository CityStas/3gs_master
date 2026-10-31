---
name: "TranslationRoles Api v1"
last_updated: 2026-10-30T19:56:08Z
type: legacy
api_base_url: "https://translationroles.roblox.com"
versions: [v1]
endpoints: 4
auth: [cookie]
---

# TranslationRoles Api v1

> **Warning:** Legacy APIs with cookie authentication can incorporate breaking changes without notice. We don't recommend them for production applications.

**Base URL:** `https://translationroles.roblox.com`
**Versions:** v1

## Endpoints

### GET `/v1/game-localization-roles/games/{gameId}/current-user/roles`

Retrieves the list of roles granted to current logged-in user

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gameId` | path | `integer (int64)` | Yes | The id of the game |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiArrayResponse[System.String]`
- `400`: 3: Invalid game id
- `401`: 0: Authorization has been denied for this request.
- `503`: 2: Feature is disabled

**Response fields** (`Roblox.Web.WebAPI.Models.ApiArrayResponse[System.String]`)

See [Roblox.Web.WebAPI.Models.ApiArrayResponse[System.String]](#roblox-web-webapi-models-apiarrayresponse-system-string-) in Models.

**Response example:**
```json
{
  "data": [
    "string"
  ]
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://translationroles.roblox.com/v1/game-localization-roles/games/{GAMEID}/current-user/roles"
```

### GET `/v1/game-localization-roles/games/{gameId}/roles/{role}/assignees`

Gets list of users assigned a specific role in a game.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gameId` | path | `integer (int64)` | Yes | The id of the game |
| `role` | path | `string` | Yes | The Roblox.GameLocalization.Client.GameLocalizationRoles.GameLocalizationRoleType Valid values: `translator` |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.TranslationRoles.Api.Assignee]`
- `400`: 3: Invalid game id
- `401`: 0: Authorization has been denied for this request.
- `403`: 1: You must be authorized to use this endpoint
- `503`: 2: Feature is disabled

**Response fields** (`Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.TranslationRoles.Api.Assignee]`)

See [Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.TranslationRoles.Api.Assignee]](#roblox-web-webapi-models-apiarrayresponse-roblox-translationroles-api-assignee-) in Models.

**Response example:**
```json
{
  "data": [
    {
      "id": "...",
      "name": "...",
      "type": "..."
    }
  ]
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://translationroles.roblox.com/v1/game-localization-roles/games/{GAMEID}/roles/{ROLE}/assignees"
```

### GET `/v1/game-localization-roles/roles/{role}/current-user`

Gets the list of games and associated role assignment info for the requested user and role.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `role` | path | `string` | Yes | The Roblox.GameLocalization.Client.GameLocalizationRoles.GameLocalizationRoleType Valid values: `translator` |
| `exclusiveStartKey` | query | `string` | No | Part of pagination. Last primary key of returned items in previous operation. |
| `pageSize` | query | `integer (int32)` | No | Part of pagination. Maximum number of items that might be returned in the page. |
| `groupId` | query | `integer (int64)` | No | Optional seleted groupId of resources requested for the user and role. |

**Responses:**

- `200`: OK → `Roblox.TranslationRoles.Api.GetGameLocalizationRoleAssignmentsForUserResponse`
- `400`: 10: Invalid page size 11: Maximum page size exceeded 12: Invalid exclusive start key
- `401`: 0: Authorization has been denied for this request.
- `500`: 0: An unknown error occurred
- `503`: 2: Feature is disabled

**Response fields** (`Roblox.TranslationRoles.Api.GetGameLocalizationRoleAssignmentsForUserResponse`)

See [Roblox.TranslationRoles.Api.GetGameLocalizationRoleAssignmentsForUserResponse](#roblox-translationroles-api-getgamelocalizationroleassignmentsforuserresponse) in Models.

**Response example:**
```json
{
  "games": [
    {
      "gameId": "...",
      "assignee": "..."
    }
  ],
  "previousPageCursor": "string",
  "nextPageCursor": "string"
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://translationroles.roblox.com/v1/game-localization-roles/roles/{ROLE}/current-user"
```

### PATCH `/v1/game-localization-roles/games/{gameId}`

Assigns or revokes a role

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gameId` | path | `integer (int64)` | Yes | The id of the game |

**Request Body:** `application/json` — Type: `Roblox.TranslationRoles.Api.UpdateRoleRequest`

See [Roblox.TranslationRoles.Api.UpdateRoleRequest](#roblox-translationroles-api-updaterolerequest) in Models.

**Request example:**
```json
{
  "assigneeId": 0,
  "assigneeType": "user",
  "role": "translator",
  "revoke": false
}
```

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: 3: Invalid game id 4: Invalid assignee id 6: Request body can't be null 7: The role you are assigning has reached max limit
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 1: You must be authorized to use this endpoint
- `429`: 5: Too many attempts. Please try again later.
- `503`: 2: Feature is disabled

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `429`: Retry with exponential backoff (start at 1s). `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X PATCH -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://translationroles.roblox.com/v1/game-localization-roles/games/{GAMEID}" \
  -H "Content-Type: application/json" \
  -d '{
  "assigneeId": 0,
  "assigneeType": "user",
  "role": "translator",
  "revoke": false
}'
```

## Models

### Roblox.GameLocalization.Client.GameLocalizationRoles.Assignee

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `assigneeType` | `user \| group \| groupRole` | No | ['User' = 0, 'Group' = 1, 'GroupRole' = 2] |
| `id` | `integer` | No |  |

### Roblox.GameLocalization.Client.GameLocalizationRoles.GameLocalizationRoleAssignment

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `gameId` | `integer` | No |  |
| `assignee` | `Roblox.GameLocalization.Client.GameLocalizationRoles.Assignee` | No |  |

### Roblox.TranslationRoles.Api.Assignee

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | `integer` | No |  |
| `name` | `string` | No |  |
| `type` | `user \| group \| groupRole` | No | ['User' = 0, 'Group' = 1, 'GroupRole' = 2] |

### Roblox.TranslationRoles.Api.GetGameLocalizationRoleAssignmentsForUserResponse

Response model containing a list of games and associated role assignment info for the requested user and role.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `games` | `Roblox.GameLocalization.Client.GameLocalizationRoles.GameLocalizationRoleAssignment[]` | No | List of games with associated role assignment info. |
| `previousPageCursor` | `string` | No | Cursor which can be used for navigating to previous page. |
| `nextPageCursor` | `string` | No | Cursor which can be used for navigating to next page. |

### Roblox.TranslationRoles.Api.UpdateRoleRequest

The request body for update role endpoints

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `assigneeId` | `integer` | No | The id of the assignee |
| `assigneeType` | `user \| group \| groupRole` | No | The type of the assignee ['User' = 0, 'Group' = 1, 'GroupRole' = 2] |
| `role` | `translator` | No | The role to be assigned or revoked ['Translator' = 0] |
| `revoke` | `boolean` | No | To assign or to revoke |

### Roblox.Web.WebAPI.Models.ApiArrayResponse[Roblox.TranslationRoles.Api.Assignee]

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | `Roblox.TranslationRoles.Api.Assignee[]` | No |  |

### Roblox.Web.WebAPI.Models.ApiArrayResponse[System.String]

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | `string[]` | No |  |