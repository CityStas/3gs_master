---
name: "Observability"
last_updated: 2026-10-30T19:56:08Z
type: feature
api_base_url: "https://apis.roblox.com"
endpoints: 6
auth: [api-key, oauth2, cookie]
description: "Monitor and manage game servers for an experience"
---

# Observability

Monitor and manage game servers for an experience.

Common use cases include:

- Server discovery: [List active game servers](#GameServers_ListGameServers) for a specific place version and [retrieve available filter options](#GameServers_GetFilterOptions)
- Log retrieval: [Inspect logs](#GameServers_ListGameServerLogs) for a specific game server
- Server restarts: [Forecast the impact](#Restarts_ForecastRestart) of a restart, [launch it](#Restarts_LaunchRestart), and [monitor its status](#Restarts_ListRestartStatuses)

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

### GET `/server-management/v1/universes/{universeId}/places/{placeId}/game-servers:filter-options` [BETA]

Gets available filter options for game servers.

**Auth:** Cookie (`.ROBLOSECURITY`) or API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `universe:read`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer` | Yes | The universe ID |
| `placeId` | path | `integer` | Yes | The place ID |
| `Filter` | query | `any` | No | The specific filter to query. If null or empty, the endpoint returns all available filters. |

**Responses:**

- `200`: Success → `FilterOptionsResponse`
- `400`: Bad Request → `ServerManagementService.ProblemDetails`
- `401`: Unauthorized → `ServerManagementService.ProblemDetails`
- `403`: Forbidden → `ServerManagementService.ProblemDetails`

**Response fields** (`FilterOptionsResponse`)

See [FilterOptionsResponse](#filteroptionsresponse) in Models.

**Response example:**
```json
{
  "filters": "..."
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 100/minute, perOauth2Authorization: 100/minute

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/server-management/v1/universes/{UNIVERSEID}/places/{PLACEID}/game-servers:filter-options"
```

### GET `/server-management/v1/universes/{universeId}/places/{placeId}/versions/{versionNumber}/game-servers` [BETA]

Lists game servers for a specific place version.

**Auth:** Cookie (`.ROBLOSECURITY`) or API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `universe:read`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer` | Yes | The universe ID |
| `placeId` | path | `integer` | Yes | The place ID |
| `versionNumber` | path | `string` | Yes | The version number |
| `MaxPageSize` | query | `integer` | No | The maximum number of game servers to return. The service might return fewer than this value. If unspecified, at most 25 game servers are returned. The maximum value is 100 and higher values are set to 100. Zero returns no game servers and only the total count, for callers that need the count without paging through rows. |
| `PageToken` | query | `string` | No | A page token, received from a previous call, to retrieve a subsequent page. When paginating, all other parameters provided to the subsequent call must match the call that provided the page token. |
| `OrderBy` | query | `string` | No | Sorting is supported only for a single field at a time. Example: "orderBy": "uptime" Defaults to ascending, but descending ordering is also supported by including the " desc" suffix. For example: "orderBy": "uptime desc". |
| `Filter` | query | `string` | No | This field may be set in order to filter the resources returned. - CEL filtering is supported on all fields. - Supported operators &&, <, <=, >, >=, ==, and `in` |

**Responses:**

- `200`: Success → `ServerManagementService.ListGameServersResponse`
- `400`: Bad Request → `ServerManagementService.ProblemDetails`
- `401`: Unauthorized → `ServerManagementService.ProblemDetails`
- `403`: Forbidden → `ServerManagementService.ProblemDetails`

**Response fields** (`ServerManagementService.ListGameServersResponse`)

See [ServerManagementService.ListGameServersResponse](#servermanagementservice-listgameserversresponse) in Models.

**Response example:**
```json
{
  "gameServers": [
    {
      "placeId": "...",
      "placeVersion": "...",
      "jobId": "...",
      "engineVersion": "...",
      "createTime": "...",
      "uptime": "..."
    }
  ],
  "nextPageToken": "string",
  "previousPageToken": "string",
  "totalCount": 0,
  "shutdownServersFetchError": false,
  "activeServersFetchError": false
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 100/minute, perOauth2Authorization: 100/minute

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/server-management/v1/universes/{UNIVERSEID}/places/{PLACEID}/versions/{VERSIONNUMBER}/game-servers"
```

### GET `/server-management/v1/universes/{universeId}/places/{placeId}/versions/{versionNumber}/game-servers/{jobId}/logs` [BETA]

Lists game server logs for a specific server job id

**Auth:** Cookie (`.ROBLOSECURITY`) or API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `universe:read`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer` | Yes | The universe id |
| `placeId` | path | `integer` | Yes | The place id |
| `versionNumber` | path | `string` | Yes | The version number |
| `jobId` | path | `string` | Yes | The server job id |
| `MaxPageSize` | query | `integer` | No | The maximum number of log entries to return. Defaults to 25 and values above 100 are capped at 100. |
| `PageToken` | query | `string` | No | An opaque token from a previous response. Preserve the other query parameters when requesting the next page. |
| `OrderBy` | query | `string` | No | Sorts by `message_timestamp` or `log_severity`. Append ` desc` for descending order. Each endpoint defines its own default when this value is omitted. |
| `Filter` | query | `string` | No | Filters log entries with CEL. Use `severity` with equality or `in`, `message_timestamp` with comparisons, or `search` with equality or inequality for case-insensitive full-text matching. |

**Responses:**

- `200`: Success → `ListGameServerLogsResponse`
- `400`: Bad Request → `ServerManagementService.ProblemDetails`
- `401`: Unauthorized → `ServerManagementService.ProblemDetails`
- `403`: Forbidden → `ServerManagementService.ProblemDetails`

**Response fields** (`ListGameServerLogsResponse`)

See [ListGameServerLogsResponse](#listgameserverlogsresponse) in Models.

**Response example:**
```json
{
  "gameServerLogs": [
    {
      "messageTimestampMs": "...",
      "universeId": "...",
      "placeId": "...",
      "placeVersion": "...",
      "jobId": "...",
      "severity": "..."
    }
  ],
  "nextPageToken": "string"
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 100/minute, perOauth2Authorization: 100/minute

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/server-management/v1/universes/{UNIVERSEID}/places/{PLACEID}/versions/{VERSIONNUMBER}/game-servers/{JOBID}/logs"
```

### GET `/server-management/v1/universes/{universeId}/restarts` [BETA]

List restart statuses for a universe.

**Auth:** Cookie (`.ROBLOSECURITY`) or API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `universe:read`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer` | Yes | The universe ID |

**Responses:**

- `200`: Success → `ListRestartStatusesResponse`
- `400`: Bad Request → `ServerManagementService.ProblemDetails`
- `401`: Unauthorized → `ServerManagementService.ProblemDetails`
- `403`: Forbidden → `ServerManagementService.ProblemDetails`

**Response fields** (`ListRestartStatusesResponse`)

See [ListRestartStatusesResponse](#listrestartstatusesresponse) in Models.

**Response example:**
```json
{
  "restartStatuses": "..."
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 100/minute, perOauth2Authorization: 100/minute

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/server-management/v1/universes/{UNIVERSEID}/restarts"
```

### POST `/server-management/v1/universes/{universeId}/restarts` [BETA]

Launch a game server restart for a universe.

**Auth:** Cookie (`.ROBLOSECURITY`) or API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `universe:write`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer` | Yes | The universe ID |

**Request Body:** `application/json` — Type: `any`

**Responses:**

- `200`: Success → `LaunchRestartResponse`
- `400`: Bad Request → `ServerManagementService.ProblemDetails`
- `401`: Unauthorized → `ServerManagementService.ProblemDetails`
- `403`: Forbidden → `ServerManagementService.ProblemDetails`

**Response fields** (`LaunchRestartResponse`)

See [LaunchRestartResponse](#launchrestartresponse) in Models.

**Response example:**
```json
{
  "id": "string",
  "playersImpacted": 0,
  "instancesImpacted": 0
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 100/minute, perOauth2Authorization: 100/minute

**Example:**
```bash
curl -X POST -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/server-management/v1/universes/{UNIVERSEID}/restarts" \
  -H "Content-Type: application/json" \
  -d '"..."'
```

### GET `/server-management/v1/universes/{universeId}/restarts:forecast` [BETA]

Forecast the impact of restarting game servers for a universe.

**Auth:** Cookie (`.ROBLOSECURITY`) or API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `universe:read`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer` | Yes | The universe ID |

**Responses:**

- `200`: Success → `ForecastRestartResponse`
- `400`: Bad Request → `ServerManagementService.ProblemDetails`
- `401`: Unauthorized → `ServerManagementService.ProblemDetails`
- `403`: Forbidden → `ServerManagementService.ProblemDetails`

**Response fields** (`ForecastRestartResponse`)

See [ForecastRestartResponse](#forecastrestartresponse) in Models.

**Response example:**
```json
{
  "placeForecasts": "..."
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 100/minute, perOauth2Authorization: 100/minute

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/server-management/v1/universes/{UNIVERSEID}/restarts:forecast"
```

## Models

### FilterOptionsResponse

Response model for filter options endpoint.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `filters` | `object` | No | A dictionary of filter field names to their metadata and available values. |

### ServerManagementService.ProblemDetails

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `type` | `string` | No |  |
| `title` | `string` | No |  |
| `status` | `integer` | No |  |
| `detail` | `string` | No |  |
| `instance` | `string` | No |  |

### ServerManagementService.ListGameServersResponse

Response model for listing game servers.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `gameServers` | `ServerManagementService.GameServer[]` | No | The GameServers from the specified PlaceVersion. |
| `nextPageToken` | `string` | No | A token that you can send as a `pageToken` parameter to retrieve the next page. If this field is omitted, there are no subsequent pages. |
| `previousPageToken` | `string` | No | A token that you can send as a `pageToken` parameter to retrieve the previous page (reverse cursor). If this field is omitted, there are no prior pages. |
| `totalCount` | `integer` | No | Total matching rows across all pages. Combined active+shutdown queries return the sum of each source total when both are known; omitted when a source failed or omitted its total. |
| `shutdownServersFetchError` | `boolean` | No | True when this page includes active rows but shutdown rows could not be fetched. Results may be a partial slice of the globally ordered combined stream. |
| `activeServersFetchError` | `boolean` | No | True when this page includes shutdown rows but active rows could not be fetched. Results may be a partial slice of the globally ordered combined stream. |

### ListGameServerLogsResponse

Response model for listing game servers.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `gameServerLogs` | `GameServerLog[]` | No | The GameServers from the specified PlaceVersion. |
| `nextPageToken` | `string` | No | A token that you can send as a `pageToken` parameter to retrieve the next page. If this field is omitted, there are no subsequent pages. |

### ListRestartStatusesResponse

Response model for listing restart statuses.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `restartStatuses` | `object` | No | Restart statuses keyed by restart ID. |

### LaunchRestartResponse

Response model for launching a game restart.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | `string` | No | ID of the restart. |
| `playersImpacted` | `integer` | No | Number of players in instances that will be shut down. |
| `instancesImpacted` | `integer` | No | Number of game instances that will be closed. |

### ForecastRestartResponse

Response model for the forecast restart endpoint.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `placeForecasts` | `object` | No | Per-place forecast data keyed by place ID. Empty if no active places. |