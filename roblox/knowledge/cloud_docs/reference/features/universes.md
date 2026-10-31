---
name: "Universes"
last_updated: 2026-10-30T19:56:08Z
type: feature
api_base_url: "https://apis.roblox.com"
endpoints: 38
auth: [api-key, oauth2, cookie]
description: "Manage experiences (universes), publish updates, and communicate with live servers"
---

# Universes

Manage experiences (universes), publish updates, and communicate with live servers. See the [Messaging Usage Guide](/cloud/guides/usage-messaging) and [Place Publishing Guide](/cloud/guides/usage-place-publishing).

Common use cases include:

- **Cross-Server Messaging**: [Send announcements](#Cloud_PublishUniverseMessage), trigger events, or update all players across servers using the Messaging Service
- User restrictions: [Ban or restrict users](#Cloud_UpdateUserRestriction__Using_Universes) from your experience at the universe or place level
- Playtester access: [List](#develop_get_v1_universes__universeId__configuration_playtesters), [add](#develop_post_v1_universes__universeId__configuration_playtesters), or [remove](#develop_delete_v1_universes__universeId__configuration_playtesters) playtesters for a universe
- Service configuration: [Retrieve](#ServiceEfficiencyApi_GetConsumerConfigurationsByUniverse) or [update](#ServiceEfficiencyApi_UpdateConsumerConfigurationsByUniverse) consumer configuration for a universe

> **See also:** To list all your experiences, see [develop](/docs/cloud/reference/features/develop.md).

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

### GET `/cloud/v2/universes/{universeId}/secrets` [BETA]

List Secrets

Lists all secrets defined for a universe.
Secret content is not returned for security reasons - only metadata such as ID, domain, creation and update timestamps are included.

Only the owner of the universe can list secrets. For group-owned universes, only the group owner or authorized
members can list secrets.

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `universe.secret:read`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer` | Yes | The universe ID |
| `limit` | query | `integer` | No | Number of secrets to return per page (1-500, default 10) |
| `cursor` | query | `string` | No | Pagination cursor from previous response |

**Responses:**

- `200`: OK → `SecretPaginatedList`
- `400`: Bad Request → `SecretsStoreService.ProblemDetails`
- `403`: Forbidden → `SecretsStoreService.ProblemDetails`

**Response fields** (`SecretPaginatedList`)

See [SecretPaginatedList](#secretpaginatedlist) in Models.

**Response example:**
```json
{
  "secrets": [
    {
      "id": "...",
      "secret": "...",
      "key_id": "...",
      "domain": "...",
      "create_time": "...",
      "update_time": "..."
    }
  ],
  "nextPageCursor": "string",
  "previousPageCursor": "string"
}
```

**Error handling:** `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 120/minute, perOauth2Authorization: 120/minute

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/cloud/v2/universes/{UNIVERSEID}/secrets"
```

### POST `/cloud/v2/universes/{universeId}/secrets` [BETA]

Create Secret

Creates a new secret. A maximum of 500 secrets per universe is allowed.
            
Only the owner of the universe can create secrets. For group-owned universes, only the group owner or authorized
members can create secrets.
            
To encrypt the secret:
1. Get the public key using the Get Public Key endpoint
2. Encrypt your secret using LibSodium sealed box
3. Base64 encode the encrypted content

Include the key_id from the public key response in the request.

For an example, see the [Secrets store guide](https://create.roblox.com/docs/cloud/guides/secrets-store).

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `universe.secret:write`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer` | Yes | The universe ID |

**Request Body:** `application/json` — Type: `Secret`

See [Secret](#secret) in Models.

**Request example:**
```json
{
  "id": "string",
  "secret": "string",
  "key_id": "string",
  "domain": "string",
  "create_time": "2024-01-01T00:00:00Z",
  "update_time": "2024-01-01T00:00:00Z"
}
```

**Responses:**

- `201`: Created → `Secret`
- `400`: Bad Request → `SecretsStoreService.ProblemDetails`
- `403`: Forbidden → `SecretsStoreService.ProblemDetails`
- `409`: Conflict → `SecretsStoreService.ProblemDetails`

**Response fields** (`Secret`)

See [Secret](#secret) in Models.

**Response example:**
```json
{
  "id": "string",
  "secret": "string",
  "key_id": "string",
  "domain": "string",
  "create_time": "2024-01-01T00:00:00Z",
  "update_time": "2024-01-01T00:00:00Z"
}
```

**Error handling:** `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 120/minute, perOauth2Authorization: 120/minute

**Example:**
```bash
curl -X POST -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/cloud/v2/universes/{UNIVERSEID}/secrets" \
  -H "Content-Type: application/json" \
  -d '{
  "id": "string",
  "secret": "string",
  "key_id": "string",
  "domain": "string",
  "create_time": "2024-01-01T00:00:00Z",
  "update_time": "2024-01-01T00:00:00Z"
}'
```

### GET `/cloud/v2/universes/{universeId}/secrets/public-key` [BETA]

Get Public Key

Retrieves the public key for a universe. You need this key to encrypt secret content 
before sending it to Roblox.

Only the owner of the universe can retrieve the public key. For group-owned universes, only the group owner or
authorized members can retrieve the public key.

The secret id field is static and always returns "public-key".

The returned public key in the secret field is universe-specific and derived from a master key using the universe ID.
Use this key with LibSodium sealed box encryption to encrypt your secret content before 
creating or updating secrets.

Include the key_id from the public key response in the request to create or update a secret.

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `universe.secret:read`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer` | Yes | The universe ID |

**Responses:**

- `200`: OK → `Secret`
- `400`: Bad Request → `SecretsStoreService.ProblemDetails`
- `403`: Forbidden → `SecretsStoreService.ProblemDetails`

**Response fields** (`Secret`)

See [Secret](#secret) in Models.

**Response example:**
```json
{
  "id": "string",
  "secret": "string",
  "key_id": "string",
  "domain": "string",
  "create_time": "2024-01-01T00:00:00Z",
  "update_time": "2024-01-01T00:00:00Z"
}
```

**Error handling:** `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 120/minute, perOauth2Authorization: 120/minute

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/cloud/v2/universes/{UNIVERSEID}/secrets/public-key"
```

### PATCH `/cloud/v2/universes/{universeId}/secrets/{secretId}` [BETA]

Update Secret

Updates an existing secret.

Only the owner of the universe can update secrets. For group-owned universes, only the group owner or authorized
members can update secrets.

Only the secret content, key_id, and domain can be updated - the secret ID cannot be changed.

To encrypt the updated secret:
1. Get the current public key using the GetPublicKey endpoint
2. Encrypt your new secret content using LibSodium sealed box
3. Base64 encode the encrypted content

Include the key_id from the public key response in the request.

For an example, see the [Secrets store guide](https://create.roblox.com/docs/cloud/guides/secrets-store).

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `universe.secret:write`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer` | Yes | The universe ID |
| `secretId` | path | `string` | Yes | The ID of the secret to update |

**Request Body:** `application/json` — Type: `Secret`

See [Secret](#secret) in Models.

**Request example:**
```json
{
  "id": "string",
  "secret": "string",
  "key_id": "string",
  "domain": "string",
  "create_time": "2024-01-01T00:00:00Z",
  "update_time": "2024-01-01T00:00:00Z"
}
```

**Responses:**

- `200`: OK → `Secret`
- `400`: Bad Request → `SecretsStoreService.ProblemDetails`
- `403`: Forbidden → `SecretsStoreService.ProblemDetails`
- `404`: Not Found → `SecretsStoreService.ProblemDetails`

**Response fields** (`Secret`)

See [Secret](#secret) in Models.

**Response example:**
```json
{
  "id": "string",
  "secret": "string",
  "key_id": "string",
  "domain": "string",
  "create_time": "2024-01-01T00:00:00Z",
  "update_time": "2024-01-01T00:00:00Z"
}
```

**Error handling:** `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 120/minute, perOauth2Authorization: 120/minute

**Example:**
```bash
curl -X PATCH -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/cloud/v2/universes/{UNIVERSEID}/secrets/{SECRETID}" \
  -H "Content-Type: application/json" \
  -d '{
  "id": "string",
  "secret": "string",
  "key_id": "string",
  "domain": "string",
  "create_time": "2024-01-01T00:00:00Z",
  "update_time": "2024-01-01T00:00:00Z"
}'
```

### DELETE `/cloud/v2/universes/{universeId}/secrets/{secretId}` [BETA]

Delete Secret

Permanently deletes a secret from a universe.

Only the owner of the universe can delete secrets. For group-owned universes, only the group owner or authorized
members can delete secrets.

This operation is irreversible. Make sure you no longer need the secret before deleting it.

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `universe.secret:write`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer` | Yes | The universe ID |
| `secretId` | path | `string` | Yes | The ID of the secret to delete |

**Responses:**

- `200`: OK
- `400`: Bad Request → `SecretsStoreService.ProblemDetails`
- `403`: Forbidden → `SecretsStoreService.ProblemDetails`
- `404`: Not Found → `SecretsStoreService.ProblemDetails`

**Error handling:** `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 120/minute, perOauth2Authorization: 120/minute

**Example:**
```bash
curl -X DELETE -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/cloud/v2/universes/{UNIVERSEID}/secrets/{SECRETID}"
```

### GET `/cloud/v2/universes/{universe_id}` [STABLE]

Get Universe

Gets the specified universe.

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universe_id` | path | `string` | Yes | The universe ID. |

**Responses:**

- `200`: OK → `Universe`

**Response fields** (`Universe`)

See [Universe](#universe) in Models.

**Response example:**
```json
{
  "path": "string",
  "createTime": "2024-01-01T00:00:00Z",
  "updateTime": "2024-01-01T00:00:00Z",
  "displayName": "string",
  "description": "string",
  "user": "string"
}
```

**Rate Limits:** perApiKeyOwner: 100/minute, perOauth2Authorization: 100/minute

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/cloud/v2/universes/{UNIVERSE_ID}"
```

### PATCH `/cloud/v2/universes/{universe_id}` [STABLE]

Update Universe

Updates the specified universe.

This method is guaranteed to return all updated fields.
This method may additionally return the full resource.

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `universe:write`, `universe:write`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universe_id` | path | `string` | Yes | The universe ID. |
| `updateMask` | query | `string` | No | The list of fields to update. |

**Request Body:** `application/json` — Type: `Universe`

See [Universe](#universe) in Models.

**Request example:**
```json
{
  "path": "string",
  "createTime": "2024-01-01T00:00:00Z",
  "updateTime": "2024-01-01T00:00:00Z",
  "displayName": "string",
  "description": "string",
  "user": "string"
}
```

**Responses:**

- `200`: OK → `Universe`

**Response fields** (`Universe`)

See [Universe](#universe) in Models.

**Response example:**
```json
{
  "path": "string",
  "createTime": "2024-01-01T00:00:00Z",
  "updateTime": "2024-01-01T00:00:00Z",
  "displayName": "string",
  "description": "string",
  "user": "string"
}
```

**Rate Limits:** perApiKeyOwner: 100/minute, perOauth2Authorization: 100/minute

**Example:**
```bash
curl -X PATCH -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/cloud/v2/universes/{UNIVERSE_ID}" \
  -H "Content-Type: application/json" \
  -d '{
  "path": "string",
  "createTime": "2024-01-01T00:00:00Z",
  "updateTime": "2024-01-01T00:00:00Z",
  "displayName": "string",
  "description": "string",
  "user": "string"
}'
```

### POST `/cloud/v2/universes/{universe_id}:publishMessage` [STABLE]

Publish Universe Message

Publishes a message to the universe's live servers.

Servers can consume messages via
[MessagingService](https://create.roblox.com/docs/reference/engine/classes/MessagingService).

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `universe-messaging-service:publish`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universe_id` | path | `string` | Yes | The universe ID. |

**Request Body:** `application/json` — Type: `PublishUniverseMessageRequest`

See [PublishUniverseMessageRequest](#publishuniversemessagerequest) in Models.

**Request example:**
```json
{
  "topic": "string",
  "message": "string"
}
```

**Responses:**

- `200`: OK

**Rate Limits:** perApiKeyOwner: 5000/minute, perOauth2Authorization: 5000/minute
**Rate Limit Note:** Messaging Service requests are subject to additional throttling limits described in the [Open Cloud guide for Messaging Service](https://create.roblox.com/docs/cloud/guides/usage-messaging#limits).

**Example:**
```bash
curl -X POST -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/cloud/v2/universes/{UNIVERSE_ID}:publishMessage" \
  -H "Content-Type: application/json" \
  -d '{
  "topic": "string",
  "message": "string"
}'
```

### POST `/cloud/v2/universes/{universe_id}:restartServers` [STABLE]

Restart Universe Servers

Restarts active servers for a specific universe. Defaults to only
restarting servers running older versions, but can be configured to restart
all servers regardless of version. Used for releasing experience updates.

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `universe:write`, `universe:write`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universe_id` | path | `string` | Yes | The universe ID. |

**Request Body:** `application/json` — Type: `RestartUniverseServersRequest`

See [RestartUniverseServersRequest](#restartuniverseserversrequest) in Models.

**Request example:**
```json
{
  "placeIds": [
    0
  ],
  "closeAllVersions": false,
  "bleedOffServers": false,
  "bleedOffDurationMinutes": 0
}
```

**Responses:**

- `200`: OK → `RestartUniverseServersResponse`

**Response fields** (`RestartUniverseServersResponse`)

See [RestartUniverseServersResponse](#restartuniverseserversresponse) in Models.

**Response example:**
```json
{}
```

**Rate Limits:** perApiKeyOwner: 30/minute, perOauth2Authorization: 30/minute

**Example:**
```bash
curl -X POST -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/cloud/v2/universes/{UNIVERSE_ID}:restartServers" \
  -H "Content-Type: application/json" \
  -d '{
  "placeIds": [
    0
  ],
  "closeAllVersions": false,
  "bleedOffServers": false,
  "bleedOffDurationMinutes": 0
}'
```

### GET `/legacy-develop/v1/universes/multiget/permissions` [EXPERIMENTAL]

Returns an array of granted and declined permissions related to the universes with the ids in ids for the authenticated user.

If a universe can not be found for a given ID (such as -1) it will be skipped.

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `legacy-universe:manage`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `ids` | query | `integer[]` | Yes | The universe ids. |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.Api.Develop.Models.UniverseIdPermissionsModel_`
- `400`: 8: No universe IDs sent to get. 9: Too many universe IDs sent to get, the limit is:
- `401`: 0: Authorization has been denied for this request.

**Response fields** (`Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.Api.Develop.Models.UniverseIdPermissionsModel_`)

See [Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.Api.Develop.Models.UniverseIdPermissionsModel_](#roblox-web-webapi-models-apiarrayresponse-roblox-api-develop-models-universeidpermissionsmodel-) in Models.

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

**Rate Limits:** perApiKeyOwner: 100/minute, perOauth2Authorization: 100/minute

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/legacy-develop/v1/universes/multiget/permissions?ids={VALUE}"
```

### POST `/legacy-develop/v1/universes/{universeId}/activate` [EXPERIMENTAL]

Activates a universes.

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `legacy-universe:manage`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer` | Yes | The universe id. |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: 1: The universe does not exist. 2: This universe does not have a root place.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 3: You are not authorized to configure this universe. 6: The root place for this universe is under review and can not be activated. 7: Creator already has the maximum number of places active.

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 100/minute, perOauth2Authorization: 100/minute

**Example:**
```bash
curl -X POST -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/legacy-develop/v1/universes/{UNIVERSEID}/activate"
```

### POST `/legacy-develop/v1/universes/{universeId}/deactivate` [EXPERIMENTAL]

Deactivates a universe.

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `legacy-universe:manage`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer` | Yes | The universe id. |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: 1: The universe does not exist. 2: This universe does not have a root place.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 3: You are not authorized to configure this universe.

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 100/minute, perOauth2Authorization: 100/minute

**Example:**
```bash
curl -X POST -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/legacy-develop/v1/universes/{UNIVERSEID}/deactivate"
```

### GET `/legacy-develop/v1/universes/{universeId}/permissions` [EXPERIMENTAL]

Returns list of granted and declined permissions related to the universe with the id universeId for authenticated user

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `legacy-universe:manage`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer` | Yes | The universe id. |

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

**Rate Limits:** perApiKeyOwner: 100/minute, perOauth2Authorization: 100/minute

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/legacy-develop/v1/universes/{UNIVERSEID}/permissions"
```

### POST `/messaging-service/v1/universes/{universeId}/topics/{topic}` [BETA]

Publish a cross-server message to a universe

Publish a message to a pre-defined topic of an experience, with the size of the message up to 1,024 characters (1 KB). Requires the **Publish** permission for API keys and the **universe-messaging-service:publish** scope for OAuth 2.0 apps. See [Cross-server messaging](/cloud-services/cross-server-messaging.md#subscribe-users-to-receive-messages) for defining and subscribing users to a topic.

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `universe-messaging-service:publish`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer` | Yes | The identifier of the experience in which you want to send your messages to. You can [copy your experience's Universe ID](/cloud/guides/usage-messaging.md#publishing-messages-to-live-servers) on **Creator Dashboard**. |
| `topic` | path | `string` | Yes | The topic that you want to publish your message to, with up to 80 characters. |

**Request Body:** `application/json-patch+json` — Type: `PublishRequest`

See [PublishRequest](#publishrequest) in Models.

**Request example:**
```json
{
  "message": "string"
}
```

**Responses:**

- `200`: Returns an empty response body.
- `400`: Invalid request.
- `401`: The API key is not valid for this operation / You don't have the authorization.
- `403`: Publishing is not allowed on this experience.
- `500`: Server internal error / Unknown error.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 5000/minute, perOauth2Authorization: 5000/minute

**Example:**
```bash
curl -X POST -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/messaging-service/v1/universes/{UNIVERSEID}/topics/{TOPIC}" \
  -H "Content-Type: application/json" \
  -d '{
  "message": "string"
}'
```

### GET `/v1/games` [EXPERIMENTAL]

Gets a list of games' detail

**Server:** `https://games.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeIds` | query | `integer[]` | Yes | A list of universe Ids. Cannot exceed a maximum of 50 IDs. |
| `fields` | query | `string` | No | Optional comma-separated list of field names to include in the response. When omitted, all fields are returned. |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.Games.Api.Models.Response.GameDetailResponse_`
- `400`: 8: The universe IDs specified are invalid. 9: Too many universe IDs were requested.
- `429`: 4: Too many requests have been made.

**Response fields** (`Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.Games.Api.Models.Response.GameDetailResponse_`)

See [Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.Games.Api.Models.Response.GameDetailResponse_](#roblox-web-webapi-models-apiarrayresponse-roblox-games-api-models-response-gamedetailresponse-) in Models.

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
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://games.roblox.com/v1/games?universeIds={VALUE}"
```

### GET `/v1/games/games-product-info` [EXPERIMENTAL]

Gets a list of games' product info, used to purchase a game

**Server:** `https://games.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeIds` | query | `integer[]` | Yes | A list of universe Ids. Cannot exceed a maximum of 100 IDs. |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.Games.Api.Models.Response.GameProductResponse_`
- `400`: 8: The universe IDs specified are invalid. 9: Too many universe IDs were requested.

**Response fields** (`Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.Games.Api.Models.Response.GameProductResponse_`)

See [Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.Games.Api.Models.Response.GameProductResponse_](#roblox-web-webapi-models-apiarrayresponse-roblox-games-api-models-response-gameproductresponse-) in Models.

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
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://games.roblox.com/v1/games/games-product-info?universeIds={VALUE}"
```

### GET `/v1/games/recommendations/game/{universeId}` [EXPERIMENTAL]

Get games recommendations based on a given universe

**Server:** `https://games.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer` | Yes | The universe to base recommendations on |
| `PaginationKey` | query | `string` | Yes | The key of a page, which includes the start row index and all other necessary information to query the data. This parameter is usually not needed for the first page. |
| `MaxRows` | query | `integer` | Yes | The requested number of rows. |
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
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://games.roblox.com/v1/games/recommendations/game/{UNIVERSEID}?PaginationKey={VALUE}&MaxRows={VALUE}&IsTruncatedResultsEnabled={VALUE}"
```

### GET `/v1/gametemplates` [EXPERIMENTAL]

Gets a page of templates that can be used to start off making games.

Templates subject to change without notice.
Sort order of templates specified by Roblox.

**Server:** `https://develop.roblox.com`

**Auth:** 

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.Api.Develop.Models.GameTemplateModel_`

**Response fields** (`Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.Api.Develop.Models.GameTemplateModel_`)

See [Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.Api.Develop.Models.GameTemplateModel_](#roblox-web-webapi-models-apiarrayresponse-roblox-api-develop-models-gametemplatemodel-) in Models.

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

### GET `/v1/universes/multiget` [EXPERIMENTAL]

Gets a list of universes.

If a universe can not be found for a given ID (such as -1) it will be skipped.

**Server:** `https://develop.roblox.com`

**Auth:** 

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `ids` | query | `integer[]` | Yes | The universe IDs to get. Limit 100. |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.Api.Develop.Models.UniverseModel_`
- `400`: 8: No universe IDs sent to get. 9: Too many universe IDs sent to get, the limit is:

**Response fields** (`Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.Api.Develop.Models.UniverseModel_`)

See [Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.Api.Develop.Models.UniverseModel_](#roblox-web-webapi-models-apiarrayresponse-roblox-api-develop-models-universemodel-) in Models.

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

### GET `/v1/universes/multiget/permissions` [EXPERIMENTAL]

Returns an array of granted and declined permissions related to the universes with the ids in ids for the authenticated user.

If a universe can not be found for a given ID (such as -1) it will be skipped.

**Server:** `https://develop.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `ids` | query | `integer[]` | Yes | The universe ids. |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.Api.Develop.Models.UniverseIdPermissionsModel_`
- `400`: 8: No universe IDs sent to get. 9: Too many universe IDs sent to get, the limit is:
- `401`: 0: Authorization has been denied for this request.

**Response fields** (`Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.Api.Develop.Models.UniverseIdPermissionsModel_`)

See [Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.Api.Develop.Models.UniverseIdPermissionsModel_](#roblox-web-webapi-models-apiarrayresponse-roblox-api-develop-models-universeidpermissionsmodel-) in Models.

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
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://develop.roblox.com/v1/universes/multiget/permissions?ids={VALUE}"
```

### GET `/v1/universes/user-public-publish-eligibility` [EXPERIMENTAL]

Returns the result of various checks for a user's eligibility to publish a public universe

**Server:** `https://develop.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

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
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://develop.roblox.com/v1/universes/user-public-publish-eligibility"
```

### GET `/v1/universes/{universeId}` [EXPERIMENTAL]

Gets a Roblox.Api.Develop.Models.UniverseModel.

**Server:** `https://develop.roblox.com`

**Auth:** 

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer` | Yes | The Universe id. |

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

### POST `/v1/universes/{universeId}/activate` [EXPERIMENTAL]

Activates a universes.

**Server:** `https://develop.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer` | Yes | The universe id. |

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
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://develop.roblox.com/v1/universes/{UNIVERSEID}/activate"
```

### GET `/v1/universes/{universeId}/activation-eligibility` [EXPERIMENTAL]

Returns the result of various checks for a user's eligibility to activate a given universe from private to public universeId for authenticated user

**Server:** `https://develop.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer` | Yes | The universe id. |

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
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://develop.roblox.com/v1/universes/{UNIVERSEID}/activation-eligibility"
```

### GET `/v1/universes/{universeId}/configuration` [EXPERIMENTAL]

Get settings for an owned universe.

**Server:** `https://develop.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer` | Yes | The universe Id. |

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
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://develop.roblox.com/v1/universes/{UNIVERSEID}/configuration"
```

### PATCH `/v1/universes/{universeId}/configuration` [EXPERIMENTAL]

Update universe settings for an owned universe.

**Server:** `https://develop.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer` | Yes | The universeId. |

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
curl -X PATCH -b ".ROBLOSECURITY=$ROBLOSECURITY" \
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

**Server:** `https://develop.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer` | Yes | The universe Id. |

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
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://develop.roblox.com/v1/universes/{UNIVERSEID}/configuration/playtesters"
```

### POST `/v1/universes/{universeId}/configuration/playtesters`

Add playtesters to an owned universe. Existing ids are ignored (additive union).

**Server:** `https://develop.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer` | Yes | The universe Id. |

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
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
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

**Server:** `https://develop.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer` | Yes | The universe Id. |

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
curl -X DELETE -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://develop.roblox.com/v1/universes/{UNIVERSEID}/configuration/playtesters" \
  -H "Content-Type: application/json" \
  -d '{
  "playtesters": [
    0
  ]
}'
```

### POST `/v1/universes/{universeId}/configuration/playtesters/eligibility`

Check whether each candidate user can currently be added as a private playtester.

**Server:** `https://develop.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer` | Yes | The universe Id. |

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
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://develop.roblox.com/v1/universes/{UNIVERSEID}/configuration/playtesters/eligibility" \
  -H "Content-Type: application/json" \
  -d '{
  "playtesters": [
    0
  ]
}'
```

### POST `/v1/universes/{universeId}/deactivate` [EXPERIMENTAL]

Deactivates a universe.

**Server:** `https://develop.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer` | Yes | The universe id. |

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
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://develop.roblox.com/v1/universes/{UNIVERSEID}/deactivate"
```

### GET `/v1/universes/{universeId}/permissions` [EXPERIMENTAL]

Returns list of granted and declined permissions related to the universe with the id universeId for authenticated user

**Server:** `https://develop.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer` | Yes | The universe id. |

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
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://develop.roblox.com/v1/universes/{UNIVERSEID}/permissions"
```

### GET `/v1/universes/{universeId}/stats`

Get statistics data for a universe.

**Server:** `https://economycreatorstats.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer` | Yes | The universe id. |
| `Type` | query | `PremiumUpsells \| PremiumVisits` | Yes | The type of a statistics dataset. ['PremiumUpsells' = 0, 'PremiumVisits' = 1] Valid values: `PremiumUpsells`, `PremiumVisits` |
| `StartTime` | query | `string` | Yes |  |
| `EndTime` | query | `string` | Yes |  |

**Responses:**

- `200`: OK → `Roblox.EconomyCreatorStats.Api.Models.StatisticsResponse`
- `400`: 1: The Universe is invalid. 3: Too many data points requested. 4: The requested data type is not known.
- `401`: 0: Authorization has been denied for this request. 2: Not authorized to perform this action.

**Response fields** (`Roblox.EconomyCreatorStats.Api.Models.StatisticsResponse`)

See [Roblox.EconomyCreatorStats.Api.Models.StatisticsResponse](#roblox-economycreatorstats-api-models-statisticsresponse) in Models.

**Response example:**
```json
{
  "dataGranularity": 0,
  "data": "..."
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://economycreatorstats.roblox.com/v1/universes/{UNIVERSEID}/stats?Type={VALUE}&StartTime={VALUE}&EndTime={VALUE}"
```

### GET `/v1/user/universes` [EXPERIMENTAL]

Gets a list of universes for the authenticated user.

**Server:** `https://develop.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `isArchived` | query | `boolean` | No | Whether or not to return archived games. |
| `limit` | query | `10 \| 25 \| 50 \| 100` | No | The number of results per request. Valid values: `10`, `25`, `50`, `100` |
| `cursor` | query | `string` | No | The paging cursor for the previous or next page. |
| `sortOrder` | query | `Asc \| Desc` | No | Sorted by universeId Valid values: `Asc`, `Desc` |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.Api.Develop.Models.UniverseModel_`
- `400`: cursor is not valid.
- `401`: 0: Authorization has been denied for this request.

**Response fields** (`Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.Api.Develop.Models.UniverseModel_`)

See [Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.Api.Develop.Models.UniverseModel_](#roblox-web-webapi-models-apipageresponse-roblox-api-develop-models-universemodel-) in Models.

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
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://develop.roblox.com/v1/user/universes"
```

### POST `/v2/sales/sales-report-download`

**Server:** `https://economy.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Request Body:** `application/json-patch+json` — Type: `any`

**Responses:**

- `200`: OK → `HttpResponseMessage`

**Response fields** (`HttpResponseMessage`)

See [HttpResponseMessage](#httpresponsemessage) in Models.

**Response example:**
```json
{
  "version": "string",
  "content": "...",
  "statusCode": "...",
  "reasonPhrase": "string",
  "headers": [
    {
      "key": "...",
      "value": "..."
    }
  ],
  "trailingHeaders": [
    {
      "key": "...",
      "value": "..."
    }
  ]
}
```

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://economy.roblox.com/v2/sales/sales-report-download" \
  -H "Content-Type: application/json" \
  -d '"..."'
```

### GET `/v2/supported-languages/games/{gameId}` [EXPERIMENTAL]

Get the supported languages for a game.

**Server:** `https://gameinternationalization.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gameId` | path | `integer` | Yes | The id of the game. |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.GameInternationalization.Api.LanguageWithLocales_`
- `400`: 14: Invalid game id
- `503`: 17: Feature is disabled

**Response fields** (`Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.GameInternationalization.Api.LanguageWithLocales_`)

See [Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.GameInternationalization.Api.LanguageWithLocales_](#roblox-web-webapi-models-apiarrayresponse-roblox-gameinternationalization-api-languagewithlocales-) in Models.

**Response example:**
```json
{
  "data": [
    {
      "languageFamily": "...",
      "childLocales": "..."
    }
  ]
}
```

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://gameinternationalization.roblox.com/v2/supported-languages/games/{GAMEID}"
```

### PATCH `/v2/universes/{universeId}/configuration` [EXPERIMENTAL]

Update universe settings for an owned universe.
V2 Contains data for avatar scale and asset override.

**Server:** `https://develop.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer` | Yes | The universeId. |

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
- `400`: 1: The universe does not exist. 3: Invalid UniverseAvatarType. 4: Invalid UniverseScaleType. 5: Invalid UniverseAnimationType. 6: Invalid UniverseCollisionType. 7: New universe name or description has been rejected. 8: New universe name is too long. 10: Invalid UniverseBodyType. 11: Invalid UniverseJointPositioningType. 12: The universe has no root place. 15: Price is required when isForSale is true. 16: This game cannot be offered for sale because it is not public. 17: This game cannot be offered for sale because it has private servers enabled. 18: The game price is outside of the allowed range. 19: Invalid genre. 20: The request body is missing. 21: Invalid device type. 22: Invalid asset type. 23: Invalid value, the min must be less than or equal to the max 24: Invalid scale value 26: Invalid private server price 28: OptIn/Out Regions Not Supported. 41: You cannot change the private server price again so soon after the previous change. Please try again later. 44: The provided audience configuration is invalid. Ensure the audience list contains only supported audience values. 52: Promotional text has been rejected. 54: An archived experience can't have a Friends or Public audience.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 2: You are not authorized to configure this universe. 14: You are not authorized to sell games. 25: Not authorized to update private server settings 29: Luobu app terms of service user agreement is missing. 30: Unknown error while updating Opt in out region. 45: The creator of this experience is not eligible to set this audience. 55: Creator already has the maximum number of places active. 56: The root place for this universe is under review and can not be activated.
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
curl -X PATCH -b ".ROBLOSECURITY=$ROBLOSECURITY" \
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

### GET `/v2/users/{userId}/games` [EXPERIMENTAL]

Gets games created by the specified user.

**Server:** `https://games.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer` | Yes | The user Id. |
| `accessFilter` | query | `1 \| 2 \| 4` | No | Filtering option via access level. Valid values: `1`, `2`, `4` |
| `limit` | query | `10 \| 25 \| 50` | No | The number of results per request. Valid values: `10`, `25`, `50` |
| `cursor` | query | `string` | No | The paging cursor for the previous or next page. |
| `sortOrder` | query | `Asc \| Desc` | No | The order the results are sorted in. Valid values: `Asc`, `Desc` |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.Web.Responses.Games.GameResponseV2_`

**Response fields** (`Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.Web.Responses.Games.GameResponseV2_`)

See [Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.Web.Responses.Games.GameResponseV2_](#roblox-web-webapi-models-apipageresponse-roblox-web-responses-games-gameresponsev2-) in Models.

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
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://games.roblox.com/v2/users/{USERID}/games"
```

## Models

### SecretPaginatedList

Wrapper for the paginated collection output.
Complies with the REST conventions, containing
next/previous page, and a data field containing the actual list.
            
Needed only to simplify JSON serialization, and can technically
be AutoMapper-ed from the EaaS or any other data provider.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `secrets` | `Secret[]` | No | Gets the actual list of items to return |
| `nextPageCursor` | `string` | No | Gets the cursor where the pagination stopped after fetching `data`. `null` if there is no more data available. |
| `previousPageCursor` | `string` | No | Gets the cursor pointing at the previous page. `null` when it's the first page. |

### SecretsStoreService.ProblemDetails

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `type` | `string` | No |  |
| `title` | `string` | No |  |
| `status` | `integer` | No |  |
| `detail` | `string` | No |  |
| `instance` | `string` | No |  |

### Secret

Universe-specific secret, identified by `id`, and belonging to a specific `environment`.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | `string` | No | The user-specified secret name. Examples: "aws", "gcp", "discord".  Static when getting the public key for a universe.  Must be alphanumeric or underscore, 1-64 characters, not starting with a number. |
| `secret` | `string` | No | The binary secret content. Examples: API key content (text), private keys.  When created, the secret must be encrypted using LibSodium sealed box and encoded in base64 with the universe's public key.  Contains the public key when getting the public key for a universe. |
| `key_id` | `string` | No | Encryption key identifier. Identifies the key that was used to encrypt the secret content. |
| `domain` | `string` | No | The domain wildcard that restricts the purpose of the key.   You can restrict the URLs callable via HttpService to a specific domain, e.g. "api.example.com" or "*.myservice.org".  An empty or null domain means that the secret is a private key and cannot be transformed with addPrefix/addSuffix or sent as a header or URL.  In order to make the secret accessible for all domains, use "*" |
| `create_time` | `string` | No | Date and time when the secret was originally created. |
| `update_time` | `string` | No | Date and time when the secret was last updated |

### Universe

Represents a Roblox experience.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `path` | `string` | No | The resource path of the universe.  Format: `universes/{universe_id}` |
| `createTime` | `string` | No | The timestamp when the universe was created. |
| `updateTime` | `string` | No | The timestamp when the universe was last updated. |
| `displayName` | `string` | No | The name of the universe.  This field can be updated by updating the root place's name. |
| `description` | `string` | No | The description of the universe.  This field can be updated by updating the root place's description. |
| `user` | `string` | No | The universe is user-owned. |
| `group` | `string` | No |  *(immutable)* The universe is group-owned. |
| `visibility` | `VISIBILITY_UNSPECIFIED \| PUBLIC \| PRIVATE` | No | Whether or not the universe is publicly accessible.  Possible values:    \| Value \| Description \|   \| --- \| --- \|   \| VISIBILITY_UNSPECIFIED \| Updates using this value will throw an error on the backend. \|   \| PUBLIC \| The universe is public. \|   \| PRIVATE \| The universe is private.  If a universe's visibility is set to PRIVATE, all active players will immediately be removed from all running servers. \| |
| `facebookSocialLink` | `Universe_SocialLink` | No | The Facebook social link. |
| `twitterSocialLink` | `Universe_SocialLink` | No | The Twitter social link. |
| `youtubeSocialLink` | `Universe_SocialLink` | No | The Youtube social link. |
| `twitchSocialLink` | `Universe_SocialLink` | No | The Twitch social link. |
| `discordSocialLink` | `Universe_SocialLink` | No | The Discord social link. |
| `robloxGroupSocialLink` | `Universe_SocialLink` | No | The Roblox group social link. |
| `guildedSocialLink` | `Universe_SocialLink` | No | The Guilded social link. |
| `voiceChatEnabled` | `boolean` | No | Whether or not voice chat is enabled for users in the Experience.  Updating this value will not affect active servers. |
| `ageRating` | `AGE_RATING_UNSPECIFIED \| AGE_RATING_ALL \| AGE_RATING_9_PLUS \| AGE_RATING_13_PLUS \| AGE_RATING_17_PLUS` | No | The age rating of this universe.  Possible values:    \| Value \| Description \|   \| --- \| --- \|   \| AGE_RATING_UNSPECIFIED \| The age rating is not set. \|   \| AGE_RATING_ALL \| Supported for all users. \|   \| AGE_RATING_9_PLUS \| Supported for users aged 9 and up. \|   \| AGE_RATING_13_PLUS \| Supported for users aged 13 and up. \|   \| AGE_RATING_17_PLUS \| Supported for users aged 17 and up. \| |
| `privateServerPriceRobux` | `integer` | No | Represents the price in Robux of private servers.  If unset, private servers are not supported for this universe.  Can only be disabled when using a field mask.  Setting to null will disable all active private servers.  Changing the price will cancel all private server subscriptions. |
| `desktopEnabled` | `boolean` | No | Whether or not players can join the Experience via Desktop. |
| `mobileEnabled` | `boolean` | No | Whether or not players can join the Experience via Mobile. |
| `tabletEnabled` | `boolean` | No | Whether or not players can join the Experience via Tablet. |
| `consoleEnabled` | `boolean` | No | Whether or not players can join the Experience via Console. |
| `vrEnabled` | `boolean` | No | Whether or not players can join the Experience via VR. |
| `rootPlace` | `string` | No | The resource path of the root place of this universe Format: universes/{universe_id}/places/{place_id} |
| `templateRootPlace` | `string` | Yes |  *(immutable)* The resource path of the template place, used for CreateUniverse. The root place of the newly-created universe will be a clone of this template. A list of the valid template places can be obtained from ListTemplatePlaces. Format: universes/{universe_id}/places/{place_id} |

### PublishUniverseMessageRequest

Publish a message on the specified topic.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `topic` | `string` | Yes | The topic on which to publish the message. |
| `message` | `string` | Yes | The message to publish. |

### RestartUniverseServersRequest

Restarts all of the universe's servers.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `placeIds` | `integer[]` | No | The place IDs to update. If none are specified, all active places in the universe will be updated. |
| `closeAllVersions` | `boolean` | No | If true, players from servers running both old and new place versions will be restarted. If false, restarts all active servers for a specific universe if and only if a new version of the experience has been published. |
| `bleedOffServers` | `boolean` | No | If true, matchmaking to servers will stop, but servers will stay up for bleed_off_duration_minutes before shutting down. This setting gives players time to naturally migrate to the newer version. If false, servers will immediately start shutting down. |
| `bleedOffDurationMinutes` | `integer` | No | If bleed_off_servers is true, how long (in minutes) old servers are allowed to stay up before shutting them down. Valid values: 1-60 minutes. |

### RestartUniverseServersResponse

Empty response. May later contain a status.

| Property | Type | Required | Description |
|----------|------|----------|-------------|

### Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.Api.Develop.Models.UniverseIdPermissionsModel_

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | `Roblox.Api.Develop.Models.UniverseIdPermissionsModel[]` | No |  |

### Roblox.Api.Develop.Models.UniversePermissionsModel

A model containing information about a universe permissions

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `canManage` | `boolean` | No | Determines whether or not consumer can manage the target universe |
| `canCloudEdit` | `boolean` | No | Determines whether or not consumer can cloud the target universe This is only nullable/optional in the context of https://develop.roblox.com/docs#!/Universes/get_v1_universes_universeId_context_permissions endpoint which is consumed only internally. It should be computed and set for all other usages. |

### PublishRequest

The request body object with the message string that you want to publish to the live server.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `message` | `string` | No | The message content that you want to publish to the live server. |

### Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.Games.Api.Models.Response.GameDetailResponse_

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | `Roblox.Games.Api.Models.Response.GameDetailResponse[]` | No |  |

### Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.Games.Api.Models.Response.GameProductResponse_

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | `Roblox.Games.Api.Models.Response.GameProductResponse[]` | No |  |

### Roblox.Games.Api.Models.Response.GameRecommendationsResponse

Game recommendations response model.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `games` | `Roblox.Games.Api.Models.Response.GameResponseModel[]` | No | The recommended games. |
| `nextPaginationKey` | `string` | No | The pagination key for next page query. It will be null if there is no more data. |

### Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.Api.Develop.Models.GameTemplateModel_

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | `Roblox.Api.Develop.Models.GameTemplateModel[]` | No |  |

### Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.Api.Develop.Models.UniverseModel_

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | `Roblox.Api.Develop.Models.UniverseModel[]` | No |  |

### Roblox.Api.Develop.Models.UserPublicPublishEligibilityResponse

The result of various checks for a user's eligibility to publish a public universe.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `isEligible` | `boolean` | No | The overall result of eligibility. |
| `hasTransactions` | `0 \| 1 \| 2` | No | Whether user has spent any Robux since 1/1/25, including gift cards. ['Incomplete' = 0, 'NotRequired' = 1, 'Completed' = 2] |
| `idVerified` | `0 \| 1 \| 2` | No | Whether user has completed ID Verification or not. ['Incomplete' = 0, 'NotRequired' = 1, 'Completed' = 2] |
| `hasDevex` | `0 \| 1 \| 2` | No | Whether user is eligible for the developer exchange program. ['Incomplete' = 0, 'NotRequired' = 1, 'Completed' = 2] |

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

### Roblox.Api.Develop.Models.PlaytestersResponse

Response model for playtester list endpoints.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `playtesters` | `integer[]` | No | The user ids that are playtesters for this universe. |

### Roblox.Api.Develop.Models.PlaytestersRequest

Request model for adding or removing playtesters.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `playtesters` | `integer[]` | No | The user ids to add or remove as playtesters for this universe. |

### Roblox.Api.Develop.Models.PlaytesterEligibilityResponse

Per-user add eligibility for private playtester candidates.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `playtesters` | `Roblox.Api.Develop.Models.PlaytesterEligibility[]` | No | The per-user eligibility results. |

### Roblox.EconomyCreatorStats.Api.Models.StatisticsResponse

The response model

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `dataGranularity` | `0 \| 1 \| 2` | No | The Roblox.EconomyCreatorStats.Api.StatisticsDataGranularity. ['Hourly' = 0, 'Daily' = 1, 'Monthly' = 2] |
| `data` | `object` | No | The actual data. |

### Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.Api.Develop.Models.UniverseModel_

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `previousPageCursor` | `string` | No |  |
| `nextPageCursor` | `string` | No |  |
| `data` | `Roblox.Api.Develop.Models.UniverseModel[]` | No |  |

### HttpResponseMessage

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `version` | `string` | No |  |
| `content` | `any` | No |  |
| `statusCode` | `any` | No |  |
| `reasonPhrase` | `string` | No |  |
| `headers` | `StringStringIEnumerableKeyValuePair[]` | No |  |
| `trailingHeaders` | `StringStringIEnumerableKeyValuePair[]` | No |  |
| `requestMessage` | `any` | No |  |
| `isSuccessStatusCode` | `boolean` | No |  |

### Roblox.Web.WebAPI.Models.ApiArrayResponse_Roblox.GameInternationalization.Api.LanguageWithLocales_

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | `Roblox.GameInternationalization.Api.LanguageWithLocales[]` | No |  |

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

### Roblox.Web.WebAPI.Models.ApiPageResponse_Roblox.Web.Responses.Games.GameResponseV2_

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `previousPageCursor` | `string` | No |  |
| `nextPageCursor` | `string` | No |  |
| `data` | `Roblox.Web.Responses.Games.GameResponseV2[]` | No |  |