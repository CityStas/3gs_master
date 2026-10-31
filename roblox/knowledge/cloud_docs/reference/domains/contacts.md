---
name: "Contacts Api v1"
last_updated: 2026-10-30T19:56:08Z
type: legacy
api_base_url: "https://contacts.roblox.com"
versions: [v1]
endpoints: 3
auth: [cookie]
---

# Contacts Api v1

> **Warning:** Legacy APIs with cookie authentication can incorporate breaking changes without notice. We don't recommend them for production applications.

**Base URL:** `https://contacts.roblox.com`
**Versions:** v1

## Endpoints

### GET `/v1/user/tag/validate`

Validates the tag for a user

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `alias` | query | `string` | No | The tag to validate |

**Responses:**

- `200`: OK → `Roblox.Contacts.Api.Response.ValidateUserTagResponseModel`
- `400`: 4: Invalid parameters.
- `401`: 0: Authorization has been denied for this request.
- `429`: 10: The flood limit has been exceeded.

**Response fields** (`Roblox.Contacts.Api.Response.ValidateUserTagResponseModel`)

See [Roblox.Contacts.Api.Response.ValidateUserTagResponseModel](#roblox-contacts-api-response-validateusertagresponsemodel) in Models.

**Response example:**
```json
{
  "status": "Success"
}
```

**Error handling:** `429`: Retry with exponential backoff (start at 1s). `401`: Check that your API key/token is valid and not expired. 

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://contacts.roblox.com/v1/user/tag/validate"
```

### POST `/v1/user/get-tags`

Gets the tags for multiple users

**Request Body:** `application/json` — Type: `Roblox.Contacts.Api.Request.GetUserTagsRequestModel`

See [Roblox.Contacts.Api.Request.GetUserTagsRequestModel](#roblox-contacts-api-request-getusertagsrequestmodel) in Models.

**Request example:**
```json
{
  "targetUserIds": [
    0
  ]
}
```

**Responses:**

- `200`: OK → `Roblox.Contacts.Api.Response.GetUserTagsResponseModel[]`
- `400`: 4: Invalid parameters. 8: Too many user Tags are requested.
- `401`: 0: Authorization has been denied for this request.
- `429`: 10: The flood limit has been exceeded.

**Response fields** (`Roblox.Contacts.Api.Response.GetUserTagsResponseModel[]`)

See [Roblox.Contacts.Api.Response.GetUserTagsResponseModel](#roblox-contacts-api-response-getusertagsresponsemodel) in Models.

**Error handling:** `429`: Retry with exponential backoff (start at 1s). `401`: Check that your API key/token is valid and not expired. 

**Example:**
```bash
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://contacts.roblox.com/v1/user/get-tags" \
  -H "Content-Type: application/json" \
  -d '{
  "targetUserIds": [
    0
  ]
}'
```

### POST `/v1/user/tag`

Sets the tag for a user

**Request Body:** `application/json` — Type: `Roblox.Contacts.Api.Request.SetUserTagRequestModel`

See [Roblox.Contacts.Api.Request.SetUserTagRequestModel](#roblox-contacts-api-request-setusertagrequestmodel) in Models.

**Request example:**
```json
{
  "targetUserId": 0,
  "userTag": "string"
}
```

**Responses:**

- `200`: OK → `Roblox.Contacts.Api.Response.SetUserTagResponseModel`
- `400`: 2: The target user is invalid or does not exist. 4: Invalid parameters. 6: The userTag is too long.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 5: The user cannot tag themselves.
- `429`: 10: The flood limit has been exceeded.

**Response fields** (`Roblox.Contacts.Api.Response.SetUserTagResponseModel`)

See [Roblox.Contacts.Api.Response.SetUserTagResponseModel](#roblox-contacts-api-response-setusertagresponsemodel) in Models.

**Response example:**
```json
{
  "status": "Success"
}
```

**Error handling:** `429`: Retry with exponential backoff (start at 1s). `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://contacts.roblox.com/v1/user/tag" \
  -H "Content-Type: application/json" \
  -d '{
  "targetUserId": 0,
  "userTag": "string"
}'
```

## Models

### Roblox.Contacts.Api.Request.GetUserTagsRequestModel

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `targetUserIds` | `integer[]` | No |  |

### Roblox.Contacts.Api.Request.SetUserTagRequestModel

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `targetUserId` | `integer` | No | The userId of the target of the userTag. |
| `userTag` | `string` | No | The userTag to be set |

### Roblox.Contacts.Api.Response.GetUserTagsResponseModel

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `targetUserId` | `integer` | No |  |
| `targetUserTag` | `string` | No |  |

### Roblox.Contacts.Api.Response.SetUserTagResponseModel

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `status` | `Success \| Moderated` | No | Status message to be sent to the setter of the userTag ['Success' = 0, 'Moderated' = 1] |

### Roblox.Contacts.Api.Response.ValidateUserTagResponseModel

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `status` | `Success \| Moderated \| TooLong` | No | Status message to be sent to the requester of the userTag validation ['Success' = 0, 'Moderated' = 1, 'TooLong' = 2] |