---
name: "Experiments"
last_updated: 2026-10-30T19:56:08Z
type: feature
api_base_url: "https://apis.roblox.com"
endpoints: 11
auth: [api-key, oauth2, cookie]
description: "Manage and analyze experiments for your experiences programmatically"
---

# Experiments

Manage and analyze experiments for your experiences programmatically. See the [Experiments guide](https://create.roblox.com/docs/production/experiments) for setup and usage.

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

### GET `/creator-configs-public-api/v1/experimentation/universes/{universeId}/experiments` [EXPERIMENTAL]

Lists experiments for a universe.

Pagination is offset-based (`maxPageSize` + `skip`). The response carries the page slice plus the unpaginated total
matching the filters. Request includes optional pagination, search, and filters.

**Auth:** Cookie (`.ROBLOSECURITY`) or API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `universe:read`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer` | Yes |  |
| `maxPageSize` | query | `integer` | No |  |
| `skip` | query | `integer` | No |  |
| `searchKey` | query | `string` | No |  |
| `stateFilters` | query | `ExperimentState[]` | No |  |
| `sortOrder` | query | `any` | No | SORT_ORDER_ASCENDING  SORT_ORDER_DESCENDING |
| `sortKey` | query | `any` | No | LIST_EXPERIMENT_SORT_KEY_NAME  LIST_EXPERIMENT_SORT_KEY_LAST_MODIFIED_TIME  LIST_EXPERIMENT_SORT_KEY_START_TIME  LIST_EXPERIMENT_SORT_KEY_RELEVANCE |
| `productTypeFilter` | query | `any` | No | EXPERIMENT_PRODUCT_TYPE_IN_GAME_CONFIGS  EXPERIMENT_PRODUCT_TYPE_MATCHMAKING |

**Responses:**

- `200`: OK → `ListExperimentsResponse`
- `400`: Bad Request → `ActionResult`
- `401`: Unauthorized → `ActionResult`
- `404`: Not Found → `ActionResult`

**Response fields** (`ListExperimentsResponse`)

See [ListExperimentsResponse](#listexperimentsresponse) in Models.

**Response example:**
```json
{
  "experiments": [
    {
      "id": "...",
      "name": "...",
      "description": "...",
      "createdTime": "...",
      "lastUpdatedTime": "...",
      "startedTime": "..."
    }
  ],
  "total": 0
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Rate Limits:** perApiKeyOwner: 100/minute, perOauth2Authorization: 100/minute

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/creator-configs-public-api/v1/experimentation/universes/{UNIVERSEID}/experiments"
```

### POST `/creator-configs-public-api/v1/experimentation/universes/{universeId}/experiments` [EXPERIMENTAL]

Creates a new experiment for a universe.

Returns an ExperimentOperation describing the async create call.

**Auth:** Cookie (`.ROBLOSECURITY`) or API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `universe:write`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer` | Yes |  |

**Request Body:** `application/json-patch+json` — Type: `any`

**Responses:**

- `200`: OK → `CreateExperimentResponse`
- `400`: Bad Request → `ActionResult`
- `401`: Unauthorized → `ActionResult`
- `404`: Not Found → `ActionResult`

**Response fields** (`CreateExperimentResponse`)

See [CreateExperimentResponse](#createexperimentresponse) in Models.

**Response example:**
```json
{
  "operation": "..."
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Rate Limits:** perApiKeyOwner: 10/minute, perOauth2Authorization: 10/minute

**Example:**
```bash
curl -X POST -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/creator-configs-public-api/v1/experimentation/universes/{UNIVERSEID}/experiments" \
  -H "Content-Type: application/json" \
  -d '"..."'
```

### GET `/creator-configs-public-api/v1/experimentation/universes/{universeId}/experiments/{experimentId}` [EXPERIMENTAL]

Gets an experiment by ID.

Returns the `experiment`. Returns 404 if the experiment doesn't exist for the universe.

**Auth:** Cookie (`.ROBLOSECURITY`) or API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `universe:read`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer` | Yes |  |
| `experimentId` | path | `string` | Yes |  |

**Responses:**

- `200`: OK → `GetExperimentResponse`
- `400`: Bad Request → `ActionResult`
- `401`: Unauthorized → `ActionResult`
- `404`: Not Found → `ActionResult`

**Response fields** (`GetExperimentResponse`)

See [GetExperimentResponse](#getexperimentresponse) in Models.

**Response example:**
```json
{
  "experiment": "..."
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Rate Limits:** perApiKeyOwner: 100/minute, perOauth2Authorization: 100/minute

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/creator-configs-public-api/v1/experimentation/universes/{UNIVERSEID}/experiments/{EXPERIMENTID}"
```

### PATCH `/creator-configs-public-api/v1/experimentation/universes/{universeId}/experiments/{experimentId}` [EXPERIMENTAL]

Updates an existing experiment.

The payload is a full replacement of the mutable experiment fields. Returns an
ExperimentOperation describing the async update.

**Auth:** Cookie (`.ROBLOSECURITY`) or API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `universe:write`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer` | Yes |  |
| `experimentId` | path | `string` | Yes |  |

**Request Body:** `application/json-patch+json` — Type: `any`

**Responses:**

- `200`: OK → `UpdateExperimentResponse`
- `400`: Bad Request → `ActionResult`
- `401`: Unauthorized → `ActionResult`
- `404`: Not Found → `ActionResult`

**Response fields** (`UpdateExperimentResponse`)

See [UpdateExperimentResponse](#updateexperimentresponse) in Models.

**Response example:**
```json
{
  "operation": "..."
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Rate Limits:** perApiKeyOwner: 10/minute, perOauth2Authorization: 10/minute

**Example:**
```bash
curl -X PATCH -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/creator-configs-public-api/v1/experimentation/universes/{UNIVERSEID}/experiments/{EXPERIMENTID}" \
  -H "Content-Type: application/json" \
  -d '"..."'
```

### DELETE `/creator-configs-public-api/v1/experimentation/universes/{universeId}/experiments/{experimentId}` [EXPERIMENTAL]

Discards an experiment.

The experiment record is retained with state Deleted.

**Auth:** Cookie (`.ROBLOSECURITY`) or API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `universe:write`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer` | Yes |  |
| `experimentId` | path | `string` | Yes |  |

**Responses:**

- `200`: OK → `DiscardExperimentResponse`
- `400`: Bad Request → `ActionResult`
- `401`: Unauthorized → `ActionResult`
- `404`: Not Found → `ActionResult`

**Response fields** (`DiscardExperimentResponse`)

See [DiscardExperimentResponse](#discardexperimentresponse) in Models.

**Response example:**
```json
{
  "operation": "..."
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Rate Limits:** perApiKeyOwner: 10/minute, perOauth2Authorization: 10/minute

**Example:**
```bash
curl -X DELETE -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/creator-configs-public-api/v1/experimentation/universes/{UNIVERSEID}/experiments/{EXPERIMENTID}"
```

### GET `/creator-configs-public-api/v1/experimentation/universes/{universeId}/experiments/{experimentId}/stats` [EXPERIMENTAL]

Gets diagnostic stats for an experiment.

**Auth:** Cookie (`.ROBLOSECURITY`) or API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `universe:read`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer` | Yes |  |
| `experimentId` | path | `string` | Yes |  |

**Responses:**

- `200`: OK → `GetExperimentStatsResponse`
- `400`: Bad Request → `ActionResult`
- `401`: Unauthorized → `ActionResult`
- `404`: Not Found → `ActionResult`

**Response fields** (`GetExperimentStatsResponse`)

See [GetExperimentStatsResponse](#getexperimentstatsresponse) in Models.

**Response example:**
```json
{
  "operation": "..."
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Rate Limits:** perApiKeyOwner: 100/minute, perOauth2Authorization: 100/minute

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/creator-configs-public-api/v1/experimentation/universes/{UNIVERSEID}/experiments/{EXPERIMENTID}/stats"
```

### POST `/creator-configs-public-api/v1/experimentation/universes/{universeId}/experiments/{experimentId}:complete` [EXPERIMENTAL]

Completes an experiment by stopping it and rolling out the requested variant.

**Auth:** Cookie (`.ROBLOSECURITY`) or API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `universe:write`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer` | Yes |  |
| `experimentId` | path | `string` | Yes |  |

**Request Body:** `application/json-patch+json` — Type: `any`

**Responses:**

- `200`: OK → `CompleteExperimentResponse`
- `400`: Bad Request → `ActionResult`
- `401`: Unauthorized → `ActionResult`
- `404`: Not Found → `ActionResult`

**Response fields** (`CompleteExperimentResponse`)

See [CompleteExperimentResponse](#completeexperimentresponse) in Models.

**Response example:**
```json
{
  "operation": "..."
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Rate Limits:** perApiKeyOwner: 10/minute, perOauth2Authorization: 10/minute

**Example:**
```bash
curl -X POST -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/creator-configs-public-api/v1/experimentation/universes/{UNIVERSEID}/experiments/{EXPERIMENTID}:complete" \
  -H "Content-Type: application/json" \
  -d '"..."'
```

### POST `/creator-configs-public-api/v1/experimentation/universes/{universeId}/experiments/{experimentId}:schedule` [EXPERIMENTAL]

Schedules an experiment to start at a future UTC time.

Body must include `scheduledStartTime` as an ISO-8601 UTC timestamp.

**Auth:** Cookie (`.ROBLOSECURITY`) or API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `universe:write`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer` | Yes |  |
| `experimentId` | path | `string` | Yes |  |

**Request Body:** `application/json-patch+json` — Type: `any`

**Responses:**

- `200`: OK → `ScheduleExperimentResponse`
- `400`: Bad Request → `ActionResult`
- `401`: Unauthorized → `ActionResult`
- `404`: Not Found → `ActionResult`

**Response fields** (`ScheduleExperimentResponse`)

See [ScheduleExperimentResponse](#scheduleexperimentresponse) in Models.

**Response example:**
```json
{
  "operation": "..."
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Rate Limits:** perApiKeyOwner: 10/minute, perOauth2Authorization: 10/minute

**Example:**
```bash
curl -X POST -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/creator-configs-public-api/v1/experimentation/universes/{UNIVERSEID}/experiments/{EXPERIMENTID}:schedule" \
  -H "Content-Type: application/json" \
  -d '"..."'
```

### POST `/creator-configs-public-api/v1/experimentation/universes/{universeId}/experiments/{experimentId}:start` [EXPERIMENTAL]

Starts an experiment immediately.

For a future-dated start, use the sibling `:schedule` endpoint.

**Auth:** Cookie (`.ROBLOSECURITY`) or API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `universe:write`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer` | Yes |  |
| `experimentId` | path | `string` | Yes |  |

**Responses:**

- `200`: OK → `StartExperimentResponse`
- `400`: Bad Request → `ActionResult`
- `401`: Unauthorized → `ActionResult`
- `404`: Not Found → `ActionResult`

**Response fields** (`StartExperimentResponse`)

See [StartExperimentResponse](#startexperimentresponse) in Models.

**Response example:**
```json
{
  "operation": "..."
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Rate Limits:** perApiKeyOwner: 10/minute, perOauth2Authorization: 10/minute

**Example:**
```bash
curl -X POST -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/creator-configs-public-api/v1/experimentation/universes/{UNIVERSEID}/experiments/{EXPERIMENTID}:start"
```

### POST `/creator-configs-public-api/v1/experimentation/universes/{universeId}/experiments:calculateMde` [EXPERIMENTAL]

Calculates the Minimum Detectable Effect (MDE) for a prospective experiment.

Poll by clients until the operation is complete.

**Auth:** Cookie (`.ROBLOSECURITY`) or API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `universe:read`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer` | Yes |  |

**Request Body:** `application/json-patch+json` — Type: `any`

**Responses:**

- `200`: OK → `CalculateExperimentMdeResponse`
- `400`: Bad Request → `ActionResult`
- `401`: Unauthorized → `ActionResult`
- `404`: Not Found → `ActionResult`

**Response fields** (`CalculateExperimentMdeResponse`)

See [CalculateExperimentMdeResponse](#calculateexperimentmderesponse) in Models.

**Response example:**
```json
{
  "operation": "..."
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Rate Limits:** perApiKeyOwner: 10/minute, perOauth2Authorization: 10/minute

**Example:**
```bash
curl -X POST -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/creator-configs-public-api/v1/experimentation/universes/{UNIVERSEID}/experiments:calculateMde" \
  -H "Content-Type: application/json" \
  -d '"..."'
```

### GET `/creator-configs-public-api/v1/experimentation/universes/{universeId}/operations/{operationId}` [EXPERIMENTAL]

Gets the status of an experiment async operation.

Polled by clients between mutations (Create / Update / Start / Schedule /
Complete / Discard) to determine when the operation reaches `done = true`.

**Auth:** Cookie (`.ROBLOSECURITY`) or API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `universe:read`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer` | Yes |  |
| `operationId` | path | `string` | Yes |  |

**Responses:**

- `200`: OK → `GetExperimentOperationStatusResponse`
- `400`: Bad Request → `ActionResult`
- `401`: Unauthorized → `ActionResult`
- `404`: Not Found → `ActionResult`

**Response fields** (`GetExperimentOperationStatusResponse`)

See [GetExperimentOperationStatusResponse](#getexperimentoperationstatusresponse) in Models.

**Response example:**
```json
{
  "operation": "..."
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Rate Limits:** perApiKeyOwner: 100/minute, perOauth2Authorization: 100/minute

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/creator-configs-public-api/v1/experimentation/universes/{UNIVERSEID}/operations/{OPERATIONID}"
```

## Models

### ListExperimentsResponse

Response body for `GET /v1/experimentation/universes/{universeId}/experiments`.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `experiments` | `ExperimentSummary[]` | No | The page of experiments matching the query. |
| `total` | `integer` | No | Total number of experiments for the universe matching the filters             (independent of pagination). |

### CreateExperimentResponse

Response body for POST /v1/universes/{universeId}/experiment.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `operation` | `any` | No | Resulting async operation describing the create call. |

### GetExperimentResponse

Response body for GET /v1/universes/{universeId}/experiment/{experimentId}.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `experiment` | `any` | No | The requested experiment. |

### UpdateExperimentResponse

Response body for PATCH /v1/universes/{universeId}/experiment/{experimentId}.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `operation` | `any` | No | Resulting async operation describing the update call. |

### DiscardExperimentResponse

Response body for DELETE /v1/universes/{universeId}/experiment/{experimentId}.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `operation` | `any` | No | Resulting async operation describing the delete call. |

### GetExperimentStatsResponse

Response body for
`GET /v1/experimentation/universes/{universeId}/experiments/{experimentId}/stats`.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `operation` | `any` | No | The async operation containing the experiment stats. |

### CompleteExperimentResponse

Response body for
`POST /v1/experimentation/universes/{universeId}/experiments/{experimentId}:complete`.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `operation` | `any` | No | The async operation that completed the experiment. |

### ScheduleExperimentResponse

Response body for
`POST /v1/experimentation/universes/{universeId}/experiments/{experimentId}:schedule`.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `operation` | `any` | No | The async operation that scheduled the experiment. |

### StartExperimentResponse

Response body for
`POST /v1/experimentation/universes/{universeId}/experiments/{experimentId}:start`.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `operation` | `any` | No | The async operation that started the experiment. |

### CalculateExperimentMdeResponse

Response body for
`POST /v1/experimentation/universes/{universeId}/experiments:calculateMde`.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `operation` | `any` | No | The MDE async operation. |

### GetExperimentOperationStatusResponse

Response body for
`GET /v1/experimentation/universes/{universeId}/operations/{operationId}`.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `operation` | `any` | No | The current state of the async operation. |