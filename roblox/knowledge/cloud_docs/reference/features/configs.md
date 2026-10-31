---
name: "Configs"
last_updated: 2026-10-30T19:56:08Z
type: feature
api_base_url: "https://apis.roblox.com"
endpoints: 9
auth: [api-key, oauth2, cookie]
description: "Manage your in-experience config values in real time without restarting servers"
---

# Configs

Manage your in-experience config values in real time without restarting servers. See the [Configs guide](https://create.roblox.com/docs/cloud/guides/configs) for Open Cloud setup and usage.

> **Getting started:** See [Experience configs](/docs/en-us/cloud/guides/configs.md) for a complete walkthrough with working examples.

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

### GET `/creator-configs-public-api/v1/configs/universes/{universeId}/repositories/{repository}` [BETA]

Gets published config values without metadata.

Returns the latest published config values without metadata and decorators.
This response can be used as a direct copy-and-paste to the draft update endpoints.

**Auth:** Cookie (`.ROBLOSECURITY`) or API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `universe:read`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `string` | Yes |  |
| `repository` | path | `any` | Yes | InExperienceConfig  RecommendationServicesConfig  DataStoresConfig  ExtendedServicesConfig  LeaderboardsConfig  ExperienceUserConfig  JourneysConfig  AntiCheatConfig |

**Responses:**

- `200`: OK → `ConfigRepositoryValues`
- `400`: Bad Request → `ActionResult`
- `401`: Unauthorized → `ActionResult`
- `404`: Not Found → `ActionResult`

**Response fields** (`ConfigRepositoryValues`)

See [ConfigRepositoryValues](#configrepositoryvalues) in Models.

**Response example:**
```json
{
  "metadata": "...",
  "entries": "...",
  "conditionalRules": "..."
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Rate Limits:** perApiKeyOwner: 100/minute, perOauth2Authorization: 100/minute

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/creator-configs-public-api/v1/configs/universes/{UNIVERSEID}/repositories/{REPOSITORY}"
```

### GET `/creator-configs-public-api/v1/configs/universes/{universeId}/repositories/{repository}/draft` [BETA]

Gets the current draft.

Returns the current draft changes for the configuration repository.

**Auth:** Cookie (`.ROBLOSECURITY`) or API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `universe:read`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `string` | Yes |  |
| `repository` | path | `any` | Yes | InExperienceConfig  RecommendationServicesConfig  DataStoresConfig  ExtendedServicesConfig  LeaderboardsConfig  ExperienceUserConfig  JourneysConfig  AntiCheatConfig |

**Responses:**

- `200`: OK → `ConfigRepositoryDraft`
- `400`: Bad Request → `ActionResult`
- `401`: Unauthorized → `ActionResult`
- `404`: Not Found → `ActionResult`

**Response fields** (`ConfigRepositoryDraft`)

See [ConfigRepositoryDraft](#configrepositorydraft) in Models.

**Response example:**
```json
{
  "draftHash": "string",
  "entries": "...",
  "conditionalRules": "..."
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Rate Limits:** perApiKeyOwner: 100/minute, perOauth2Authorization: 100/minute

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/creator-configs-public-api/v1/configs/universes/{UNIVERSEID}/repositories/{REPOSITORY}/draft"
```

### PATCH `/creator-configs-public-api/v1/configs/universes/{universeId}/repositories/{repository}/draft` [BETA]

Partially updates the draft.

Updates the draft treating the payload as a partial changeset.
If draftHash is provided, this call will fail if the hash doesn't match.
A key not included will not be changed. To indicate deletion, set key to null.
To discard a change, set key to its currently published value.
When `conditionalRules` is omitted or empty (`{}`), the CMS update omits the conditional-rules field so existing published rules remain at publish time;
send a non-empty `conditionalRules` object to merge rule changes.
Entry count and per-value size limits are enforced here via CreatorConfigsPublicApi.Utils.DraftValidationHelper; further schema validation is performed by Config Management.

**Auth:** Cookie (`.ROBLOSECURITY`) or API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `universe:write`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `string` | Yes |  |
| `repository` | path | `any` | Yes | InExperienceConfig  RecommendationServicesConfig  DataStoresConfig  ExtendedServicesConfig  LeaderboardsConfig  ExperienceUserConfig  JourneysConfig  AntiCheatConfig |

**Request Body:** `application/json-patch+json` — Type: `any`

**Responses:**

- `200`: OK → `DraftHashResponse`
- `400`: Bad Request → `ActionResult`
- `401`: Unauthorized → `ActionResult`
- `404`: Not Found → `ActionResult`

**Response fields** (`DraftHashResponse`)

See [DraftHashResponse](#drafthashresponse) in Models.

**Response example:**
```json
{
  "draftHash": "string"
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Rate Limits:** perApiKeyOwner: 50/minute, perOauth2Authorization: 50/minute

**Example:**
```bash
curl -X PATCH -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/creator-configs-public-api/v1/configs/universes/{UNIVERSEID}/repositories/{REPOSITORY}/draft" \
  -H "Content-Type: application/json" \
  -d '"..."'
```

### DELETE `/creator-configs-public-api/v1/configs/universes/{universeId}/repositories/{repository}/draft` [BETA]

Resets (deletes) the current draft.

Resets the current draft area. If draftHash is provided, this call will fail if the hash doesn't match.

**Auth:** Cookie (`.ROBLOSECURITY`) or API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `universe:write`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `string` | Yes |  |
| `repository` | path | `any` | Yes | InExperienceConfig  RecommendationServicesConfig  DataStoresConfig  ExtendedServicesConfig  LeaderboardsConfig  ExperienceUserConfig  JourneysConfig  AntiCheatConfig |

**Request Body:** `application/json-patch+json` — Type: `any`

**Responses:**

- `200`: OK → `DraftHashResponse`
- `400`: Bad Request → `ActionResult`
- `401`: Unauthorized → `ActionResult`
- `404`: Not Found → `ActionResult`

**Response fields** (`DraftHashResponse`)

See [DraftHashResponse](#drafthashresponse) in Models.

**Response example:**
```json
{
  "draftHash": "string"
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Rate Limits:** perApiKeyOwner: 50/minute, perOauth2Authorization: 50/minute

**Example:**
```bash
curl -X DELETE -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/creator-configs-public-api/v1/configs/universes/{UNIVERSEID}/repositories/{REPOSITORY}/draft" \
  -H "Content-Type: application/json" \
  -d '"..."'
```

### PUT `/creator-configs-public-api/v1/configs/universes/{universeId}/repositories/{repository}/draft:overwrite` [BETA]

Overwrites the entire draft with the request payload.

Full overwrite of current draft. The payload is the expected final state after publish (not a merge with the draft or published config from the client’s perspective).
The service aligns that intent with CMS validation by emitting explicit deletions for published keys and conditional branches omitted from the body.
If a key is not included, it is interpreted as removed.
When `conditionalRules` is included, `conditionalRules.rules` is authoritative for rule definitions:
any conditional rule that exists on the latest published configuration but is omitted from `rules` is removed (same as sending an empty RPN rule).
When `conditionalRules` is omitted, all published conditional rules are removed; entries must not use conditional branches or `.RBX.conditional.*` keys unless you send `conditionalRules`.
If draftHash is provided, this call will fail if the hash doesn't match.
Entry count and per-value size limits are enforced here via CreatorConfigsPublicApi.Utils.DraftValidationHelper; further schema validation is performed by Config Management.

**Auth:** Cookie (`.ROBLOSECURITY`) or API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `universe:write`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `string` | Yes |  |
| `repository` | path | `any` | Yes | InExperienceConfig  RecommendationServicesConfig  DataStoresConfig  ExtendedServicesConfig  LeaderboardsConfig  ExperienceUserConfig  JourneysConfig  AntiCheatConfig |

**Request Body:** `application/json-patch+json` — Type: `any`

**Responses:**

- `200`: OK → `DraftHashResponse`
- `400`: Bad Request → `ActionResult`
- `401`: Unauthorized → `ActionResult`
- `404`: Not Found → `ActionResult`

**Response fields** (`DraftHashResponse`)

See [DraftHashResponse](#drafthashresponse) in Models.

**Response example:**
```json
{
  "draftHash": "string"
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Rate Limits:** perApiKeyOwner: 50/minute, perOauth2Authorization: 50/minute

**Example:**
```bash
curl -X PUT -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/creator-configs-public-api/v1/configs/universes/{UNIVERSEID}/repositories/{REPOSITORY}/draft:overwrite" \
  -H "Content-Type: application/json" \
  -d '"..."'
```

### GET `/creator-configs-public-api/v1/configs/universes/{universeId}/repositories/{repository}/full` [BETA]

Gets full config with metadata.

Returns the full config including metadata (version, descriptions, last modified/accessed times).

**Auth:** Cookie (`.ROBLOSECURITY`) or API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `universe:read`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `string` | Yes |  |
| `repository` | path | `any` | Yes | InExperienceConfig  RecommendationServicesConfig  DataStoresConfig  ExtendedServicesConfig  LeaderboardsConfig  ExperienceUserConfig  JourneysConfig  AntiCheatConfig |

**Responses:**

- `200`: OK → `ConfigRepositoryFull`
- `400`: Bad Request → `ActionResult`
- `401`: Unauthorized → `ActionResult`
- `404`: Not Found → `ActionResult`

**Response fields** (`ConfigRepositoryFull`)

See [ConfigRepositoryFull](#configrepositoryfull) in Models.

**Response example:**
```json
{
  "entries": "...",
  "metadata": "...",
  "conditionalRules": "..."
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Rate Limits:** perApiKeyOwner: 100/minute, perOauth2Authorization: 100/minute

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/creator-configs-public-api/v1/configs/universes/{UNIVERSEID}/repositories/{REPOSITORY}/full"
```

### POST `/creator-configs-public-api/v1/configs/universes/{universeId}/repositories/{repository}/publish` [BETA]

Publishes draft changes.

Applies the current draft to the published config. Requires a draft hash and optional message and deployment strategy.

**Auth:** Cookie (`.ROBLOSECURITY`) or API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `universe:write`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `string` | Yes |  |
| `repository` | path | `any` | Yes | InExperienceConfig  RecommendationServicesConfig  DataStoresConfig  ExtendedServicesConfig  LeaderboardsConfig  ExperienceUserConfig  JourneysConfig  AntiCheatConfig |

**Request Body:** `application/json-patch+json` — Type: `any`

**Responses:**

- `200`: OK → `PublishDraftResponse`
- `400`: Bad Request → `ActionResult`
- `401`: Unauthorized → `ActionResult`
- `404`: Not Found → `ActionResult`

**Response fields** (`PublishDraftResponse`)

See [PublishDraftResponse](#publishdraftresponse) in Models.

**Response example:**
```json
{
  "configVersion": 0
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Rate Limits:** perApiKeyOwner: 10/minute, perOauth2Authorization: 10/minute

**Example:**
```bash
curl -X POST -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/creator-configs-public-api/v1/configs/universes/{UNIVERSEID}/repositories/{REPOSITORY}/publish" \
  -H "Content-Type: application/json" \
  -d '"..."'
```

### GET `/creator-configs-public-api/v1/configs/universes/{universeId}/repositories/{repository}/revisions` [BETA]

Lists revision history.

Returns the list of previous revisions to the repository. Supports optional start/end time and pagination.

**Auth:** Cookie (`.ROBLOSECURITY`) or API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `universe:read`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `string` | Yes |  |
| `repository` | path | `any` | Yes | InExperienceConfig  RecommendationServicesConfig  DataStoresConfig  ExtendedServicesConfig  LeaderboardsConfig  ExperienceUserConfig  JourneysConfig  AntiCheatConfig |
| `startTime` | query | `string` | No | Optional start time for filtering revisions. |
| `endTime` | query | `string` | No | Optional end time for filtering revisions. |
| `MaxPageSize` | query | `integer` | No | Maximum page size. |
| `Skip` | query | `integer` | No | Number of items to skip. |
| `SearchKey` | query | `string` | No | Search key to filter by. |
| `SortOrder` | query | `string` | No | Sort order (e.g., "SORT_ORDER_DESCENDING", "SORT_ORDER_ASCENDING"). |
| `SortKey` | query | `string` | No | Sort key (e.g., "SORT_KEY_LAST_MODIFIED_TIME"). |

**Responses:**

- `200`: OK → `ListRevisionsResponse`
- `400`: Bad Request → `ActionResult`
- `401`: Unauthorized → `ActionResult`
- `404`: Not Found → `ActionResult`

**Response fields** (`ListRevisionsResponse`)

See [ListRevisionsResponse](#listrevisionsresponse) in Models.

**Response example:**
```json
{
  "revisions": [
    {
      "revisionId": "...",
      "version": "...",
      "time": "...",
      "publishedBy": "...",
      "message": "...",
      "deploymentResult": "..."
    }
  ]
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Rate Limits:** perApiKeyOwner: 100/minute, perOauth2Authorization: 100/minute

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/creator-configs-public-api/v1/configs/universes/{UNIVERSEID}/repositories/{REPOSITORY}/revisions"
```

### POST `/creator-configs-public-api/v1/configs/universes/{universeId}/repositories/{repository}/revisions/{revisionId}/restore` [BETA]

Stages a revert to a previous revision.

Attempts to restore configs to the provided revision. This will clear the staging and stage a revert commit.
You must call publish for the revert to take effect.

**Auth:** Cookie (`.ROBLOSECURITY`) or API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `universe:write`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `string` | Yes |  |
| `repository` | path | `any` | Yes | InExperienceConfig  RecommendationServicesConfig  DataStoresConfig  ExtendedServicesConfig  LeaderboardsConfig  ExperienceUserConfig  JourneysConfig  AntiCheatConfig |
| `revisionId` | path | `string` | Yes |  |

**Responses:**

- `200`: OK → `DraftHashResponse`
- `400`: Bad Request → `ActionResult`
- `401`: Unauthorized → `ActionResult`
- `404`: Not Found → `ActionResult`

**Response fields** (`DraftHashResponse`)

See [DraftHashResponse](#drafthashresponse) in Models.

**Response example:**
```json
{
  "draftHash": "string"
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Rate Limits:** perApiKeyOwner: 10/minute, perOauth2Authorization: 10/minute

**Example:**
```bash
curl -X POST -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/creator-configs-public-api/v1/configs/universes/{UNIVERSEID}/repositories/{REPOSITORY}/revisions/{REVISIONID}/restore"
```

## Models

### ConfigRepositoryValues

A representation of a configuration repository with just the values (no metadata or decorators).
This response can be used as a direct copy-and-paste to the draft update endpoints.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `metadata` | `any` | No | Metadata about the configuration repository. |
| `entries` | `object` | No | The configuration entries (key-value pairs) in the repository. |
| `conditionalRules` | `any` | No | Conditional RPN rules and evaluation order, when any exist. |

### ConfigRepositoryDraft

A representation of the current draft changes for a configuration repository.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `draftHash` | `string` | No | The hash of the draft for concurrency control. |
| `entries` | `object` | No | The configuration entries in the draft (key to value and optional description). |
| `conditionalRules` | `any` | No | Conditional rules staged on the draft, when any exist. |

### DraftHashResponse

Response model containing the draft hash.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `draftHash` | `string` | No | The hash of the draft for concurrency control. |

### ConfigRepositoryFull

A full representation of a configuration repository, including all entries and their metadata.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `entries` | `object` | No | The configuration entries (key-value with metadata such as description, last modified/accessed times). |
| `metadata` | `any` | No | Metadata about the configuration repository. |
| `conditionalRules` | `any` | No | Conditional RPN rules and evaluation order, when any exist. |

### PublishDraftResponse

Response model for publishing a draft.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `configVersion` | `integer` | No | The configuration version after publishing. |

### ListRevisionsResponse

Response model for listing revisions.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `revisions` | `RevisionResponse[]` | No | The list of revisions. |