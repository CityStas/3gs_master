---
name: "Analytics"
last_updated: 2026-10-30T19:56:08Z
type: feature
api_base_url: "https://apis.roblox.com"
endpoints: 17
auth: [api-key, oauth2, cookie]
description: "Query analytics data, compare your metrics against benchmarks, manage analytics alerts, and access error reports for your experiences programmatically"
---

# Analytics

Query analytics data, compare your metrics against benchmarks, manage analytics alerts, and access error reports for your experiences programmatically. See the [Analytics guide](https://create.roblox.com/docs/cloud/guides/analytics), [Alerts guide](https://create.roblox.com/docs/cloud/guides/alerts), or [Error Reporting guide](https://create.roblox.com/docs/cloud/guides/error-reporting) for Open Cloud setup and usage.

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

### GET `/analytics-alert-control-plane/v1/resource/{resourceType}/id/{resourceId}/alerts` [EXPERIMENTAL]

Returns the alert configurations for a resource. Optionally filter by alert IDs, firing
status, severity, or metric name.

**Auth:** Cookie (`.ROBLOSECURITY`) or API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `universe.analytics.alert:read`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `resourceType` | path | `AlertStorage.ResourceType` | Yes | The type of resource to query. Currently only `Universe` is supported.  Universe |
| `resourceId` | path | `string` | Yes | The numeric ID of the resource (e.g. the universe ID). |
| `ids` | query | `string[]` | No | Optional list of alert IDs to restrict results to. Repeat the parameter for multiple values: `?ids=1&ids=2`. IDs are string-encoded 64-bit integers. |
| `firingStatus` | query | `AlertStorage.FiringStatus` | No | Optional firing-status filter (`OK` or `Firing`).  OK  Firing |
| `severities` | query | `AlertStorage.Severity[]` | No | Optional list of severity levels to filter by. Repeat the parameter for multiple values: `?severities=SEV_0&severities=SEV_1`. |
| `metrics` | query | `string[]` | No | Optional list of metric names to filter by (exact match, case-sensitive). Repeat the parameter for multiple values: `?metrics=dau&metrics=mau`. |

**Responses:**

- `200`: OK → `AnalyticsAlertControlPlane.Models.AlertDetailResponse[]`
- `400`: Bad Request → `AnalyticsAlertControlPlane.Models.ErrorResponse`
- `401`: Unauthorized → `AnalyticsAlertControlPlane.Models.ErrorResponse`
- `403`: Forbidden → `AnalyticsAlertControlPlane.Models.ErrorResponse`
- `503`: Service Unavailable → `AnalyticsAlertControlPlane.Models.ErrorResponse`

**Response fields** (`AnalyticsAlertControlPlane.Models.AlertDetailResponse[]`)

See [AnalyticsAlertControlPlane.Models.AlertDetailResponse](#analyticsalertcontrolplane-models-alertdetailresponse) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 120/minute, perOauth2Authorization: 120/minute

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/analytics-alert-control-plane/v1/resource/{RESOURCETYPE}/id/{RESOURCEID}/alerts"
```

### POST `/analytics-alert-control-plane/v1/resource/{resourceType}/id/{resourceId}/alerts` [EXPERIMENTAL]

Creates a new alert configuration for a resource.

See the <a href="https://create.roblox.com/docs/cloud/guides/alerts/metrics">alerts guide</a> for supported metrics and dimensions.

**Auth:** Cookie (`.ROBLOSECURITY`) or API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `universe.analytics.alert:write`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `resourceType` | path | `AlertStorage.ResourceType` | Yes | The type of resource to create the alert on. Currently only `Universe` is supported.  Universe |
| `resourceId` | path | `string` | Yes | The numeric ID of the resource (e.g. the universe ID). |

**Request Body:** `application/json` — Type: `AnalyticsAlertControlPlane.Models.CreateAlertConfigRequest`

See [AnalyticsAlertControlPlane.Models.CreateAlertConfigRequest](#analyticsalertcontrolplane-models-createalertconfigrequest) in Models.

**Request example:**
```json
{
  "name": "string",
  "metric": "string",
  "description": "string",
  "severity": "SEV_0",
  "interval": "OneMinute",
  "consecutiveOccurrences": 0
}
```

**Responses:**

- `201`: Created → `AnalyticsAlertControlPlane.Models.AlertDetailResponse`
- `400`: Bad Request → `AnalyticsAlertControlPlane.Models.ErrorResponse`
- `401`: Unauthorized → `AnalyticsAlertControlPlane.Models.ErrorResponse`
- `403`: Forbidden → `AnalyticsAlertControlPlane.Models.ErrorResponse`
- `409`: Conflict. Possible error codes:              - `ALERT_NAME_EXISTED`: An alert with this name already exists for the resource.   Alert names must be unique per resource.              - `MAX_ALERT_REACHED`: The resource has reached the maximum number of allowed alerts. → `AnalyticsAlertControlPlane.Models.ErrorResponse`
- `503`: Service Unavailable → `AnalyticsAlertControlPlane.Models.ErrorResponse`

**Response fields** (`AnalyticsAlertControlPlane.Models.AlertDetailResponse`)

See [AnalyticsAlertControlPlane.Models.AlertDetailResponse](#analyticsalertcontrolplane-models-alertdetailresponse) in Models.

**Response example:**
```json
{
  "alertId": "string",
  "resourceType": "Universe",
  "resourceId": "string",
  "name": "string",
  "metric": "string",
  "description": "string"
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 30/minute, perOauth2Authorization: 30/minute

**Example:**
```bash
curl -X POST -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/analytics-alert-control-plane/v1/resource/{RESOURCETYPE}/id/{RESOURCEID}/alerts" \
  -H "Content-Type: application/json" \
  -d '{
  "name": "string",
  "metric": "string",
  "description": "string",
  "severity": "SEV_0",
  "interval": "OneMinute",
  "consecutiveOccurrences": 0
}'
```

### GET `/analytics-alert-control-plane/v1/resource/{resourceType}/id/{resourceId}/alerts/incidents` [EXPERIMENTAL]

Returns alert incidents for a resource whose active window overlaps the specified time
range. An incident is included if it was open at any point between `startTime` and
`endTime`.

**Auth:** Cookie (`.ROBLOSECURITY`) or API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `universe.analytics.alert:read`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `resourceType` | path | `AlertStorage.ResourceType` | Yes | The type of resource to query. Currently only `Universe` is supported.  Universe |
| `resourceId` | path | `string` | Yes | The numeric ID of the resource (e.g. the universe ID). |
| `startTime` | query | `string` | Yes | Start of the time range to query (ISO 8601, UTC). Must be within the last 30 days (see AnalyticsAlertControlPlane.Operations.GetAlertIncidentsOperation.MaxQueryDays). |
| `endTime` | query | `string` | Yes | End of the time range to query (ISO 8601, UTC). Must be greater than or equal to `startTime`. |
| `metric` | query | `string` | No | Optional metric name to restrict results to incidents from alerts on that metric (exact match, case-sensitive). |
| `alertIds` | query | `string[]` | No | Optional list of alert IDs to restrict results to. Repeat the parameter for multiple values: `?alertIds=1&alertIds=2`. IDs are string-encoded 64-bit integers. |
| `severities` | query | `AlertStorage.Severity[]` | No | Optional list of severity levels to restrict results to. Repeat the parameter for multiple values: `?severities=SEV_0&severities=SEV_1`. |

**Responses:**

- `200`: OK → `AnalyticsAlertControlPlane.Models.IncidentDetailResponse[]`
- `400`: Bad Request → `AnalyticsAlertControlPlane.Models.ErrorResponse`
- `401`: Unauthorized → `AnalyticsAlertControlPlane.Models.ErrorResponse`
- `403`: Forbidden → `AnalyticsAlertControlPlane.Models.ErrorResponse`
- `503`: Service Unavailable → `AnalyticsAlertControlPlane.Models.ErrorResponse`

**Response fields** (`AnalyticsAlertControlPlane.Models.IncidentDetailResponse[]`)

See [AnalyticsAlertControlPlane.Models.IncidentDetailResponse](#analyticsalertcontrolplane-models-incidentdetailresponse) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 120/minute, perOauth2Authorization: 120/minute

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/analytics-alert-control-plane/v1/resource/{RESOURCETYPE}/id/{RESOURCEID}/alerts/incidents?startTime={VALUE}&endTime={VALUE}"
```

### PATCH `/analytics-alert-control-plane/v1/resource/{resourceType}/id/{resourceId}/alerts/{alertId}` [EXPERIMENTAL]

Updates an existing alert configuration. Only the fields included in the request body are
changed; omitted fields retain their current values.

See the <a href="https://create.roblox.com/docs/cloud/guides/alerts/metrics">alerts guide</a> for supported metrics and dimensions.

**Auth:** Cookie (`.ROBLOSECURITY`) or API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `universe.analytics.alert:write`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `resourceType` | path | `AlertStorage.ResourceType` | Yes | The type of resource the alert belongs to. Currently only `Universe` is supported.  Universe |
| `resourceId` | path | `string` | Yes | The numeric ID of the resource (e.g. the universe ID). |
| `alertId` | path | `string` | Yes | The ID of the alert to update. |

**Request Body:** `application/json` — Type: `AnalyticsAlertControlPlane.Models.UpdateAlertConfigRequest`

See [AnalyticsAlertControlPlane.Models.UpdateAlertConfigRequest](#analyticsalertcontrolplane-models-updatealertconfigrequest) in Models.

**Request example:**
```json
{
  "name": "string",
  "metric": "string",
  "description": "string",
  "severity": "SEV_0",
  "interval": "OneMinute",
  "consecutiveOccurrences": 0
}
```

**Responses:**

- `200`: OK → `AnalyticsAlertControlPlane.Models.AlertDetailResponse`
- `400`: Bad Request → `AnalyticsAlertControlPlane.Models.ErrorResponse`
- `401`: Unauthorized → `AnalyticsAlertControlPlane.Models.ErrorResponse`
- `403`: Forbidden → `AnalyticsAlertControlPlane.Models.ErrorResponse`
- `404`: Not Found → `AnalyticsAlertControlPlane.Models.ErrorResponse`
- `409`: Conflict (`ALERT_NAME_EXISTED`): the new name collides with an existing alert on the same resource. Alert names must be unique per resource. → `AnalyticsAlertControlPlane.Models.ErrorResponse`
- `503`: Service Unavailable → `AnalyticsAlertControlPlane.Models.ErrorResponse`

**Response fields** (`AnalyticsAlertControlPlane.Models.AlertDetailResponse`)

See [AnalyticsAlertControlPlane.Models.AlertDetailResponse](#analyticsalertcontrolplane-models-alertdetailresponse) in Models.

**Response example:**
```json
{
  "alertId": "string",
  "resourceType": "Universe",
  "resourceId": "string",
  "name": "string",
  "metric": "string",
  "description": "string"
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 30/minute, perOauth2Authorization: 30/minute

**Example:**
```bash
curl -X PATCH -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/analytics-alert-control-plane/v1/resource/{RESOURCETYPE}/id/{RESOURCEID}/alerts/{ALERTID}" \
  -H "Content-Type: application/json" \
  -d '{
  "name": "string",
  "metric": "string",
  "description": "string",
  "severity": "SEV_0",
  "interval": "OneMinute",
  "consecutiveOccurrences": 0
}'
```

### DELETE `/analytics-alert-control-plane/v1/resource/{resourceType}/id/{resourceId}/alerts/{alertId}` [EXPERIMENTAL]

Deletes an alert configuration. This action is irreversible.

**Auth:** Cookie (`.ROBLOSECURITY`) or API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `universe.analytics.alert:write`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `resourceType` | path | `AlertStorage.ResourceType` | Yes | The type of resource the alert belongs to. Currently only `Universe` is supported.  Universe |
| `resourceId` | path | `string` | Yes | The numeric ID of the resource (e.g. the universe ID). |
| `alertId` | path | `string` | Yes | The ID of the alert to delete. |

**Responses:**

- `204`: No Content
- `400`: Bad Request → `AnalyticsAlertControlPlane.Models.ErrorResponse`
- `401`: Unauthorized → `AnalyticsAlertControlPlane.Models.ErrorResponse`
- `403`: Forbidden → `AnalyticsAlertControlPlane.Models.ErrorResponse`
- `404`: Not Found → `AnalyticsAlertControlPlane.Models.ErrorResponse`
- `503`: Service Unavailable → `AnalyticsAlertControlPlane.Models.ErrorResponse`

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 30/minute, perOauth2Authorization: 30/minute

**Example:**
```bash
curl -X DELETE -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/analytics-alert-control-plane/v1/resource/{RESOURCETYPE}/id/{RESOURCEID}/alerts/{ALERTID}"
```

### POST `/analytics-benchmark/v1/universes/{universeId}/benchmarks` [EXPERIMENTAL]

Returns daily benchmark percentiles for a metric, comparing a universe against other experiences on Roblox.

See [Analytics Guide](https://create.roblox.com/docs/cloud/guides/analytics) for more information.

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `universe.analytics:read`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer` | Yes | The ID of the universe to compare against benchmarks. |

**Request Body:** `application/json` — Type: `any`

**Responses:**

- `200`: OK → `QueryUniverseBenchmarkResponse`
- `default`: Error → `AnalyticsBenchmarkApi.Status`

**Response fields** (`QueryUniverseBenchmarkResponse`)

See [QueryUniverseBenchmarkResponse](#queryuniversebenchmarkresponse) in Models.

**Response example:**
```json
{
  "result": "...",
  "availableTypes": [
    "BENCHMARK_TYPE_INVALID"
  ],
  "objective": "BENCHMARK_OBJECTIVE_INVALID"
}
```

**Rate Limits:** perApiKeyOwner: 300/minute, perOauth2Authorization: 300/minute

**Example:**
```bash
curl -X POST -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/analytics-benchmark/v1/universes/{UNIVERSEID}/benchmarks" \
  -H "Content-Type: application/json" \
  -d '"..."'
```

### POST `/analytics-query-api/v1/universes/{universeId}/dimension-values` [BETA]

Queries dimension values for a universe.

See the <a href="https://create.roblox.com/docs/cloud/guides/analytics">Analytics guide</a> for more information.

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `universe.analytics:read`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer` | Yes | The universe ID to query dimension values for. |

**Request Body:** `application/json` — Type: `AnalyticsQueryPublicApi.DimensionValuesRequest`

See [AnalyticsQueryPublicApi.DimensionValuesRequest](#analyticsquerypublicapi-dimensionvaluesrequest) in Models.

**Request example:**
```json
{
  "metric": "string",
  "dimensions": [
    "string"
  ],
  "startTime": "2024-01-01T00:00:00Z",
  "endTime": "2024-01-01T00:00:00Z",
  "filter": [
    {
      "dimension": "...",
      "values": "...",
      "operation": "..."
    }
  ],
  "granularity": "OneMinute"
}
```

**Responses:**

- `200`: OK → `DimensionValuesOperationResult`
- `202`: Accepted → `OperationPending`
- `400`: Bad Request → `AnalyticsQueryPublicApi.OperationError`
- `403`: Forbidden → `AnalyticsQueryPublicApi.OperationError`
- `429`: Too Many Requests → `AnalyticsQueryPublicApi.OperationError`
- `500`: Internal Server Error → `AnalyticsQueryPublicApi.OperationError`
- `503`: Service Unavailable → `AnalyticsQueryPublicApi.OperationError`
- `504`: Gateway Timeout → `AnalyticsQueryPublicApi.OperationError`

**Response fields** (`DimensionValuesOperationResult`)

See [DimensionValuesOperationResult](#dimensionvaluesoperationresult) in Models.

**Response example:**
```json
{
  "path": "string",
  "done": false,
  "response": {
    "values": [
      "..."
    ]
  },
  "metadata": {
    "createdTime": "2024-01-01T00:00:00Z"
  }
}
```

**Error handling:** `429`: Retry with exponential backoff (start at 1s). `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 30/minute, perOauth2Authorization: 30/minute

**Example:**
```bash
curl -X POST -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/analytics-query-api/v1/universes/{UNIVERSEID}/dimension-values" \
  -H "Content-Type: application/json" \
  -d '{
  "metric": "string",
  "dimensions": [
    "string"
  ],
  "startTime": "2024-01-01T00:00:00Z",
  "endTime": "2024-01-01T00:00:00Z",
  "filter": [
    {
      "dimension": "...",
      "values": "...",
      "operation": "..."
    }
  ],
  "granularity": "OneMinute"
}'
```

### POST `/analytics-query-api/v1/universes/{universeId}/metrics` [BETA]

Queries time series metric data for a universe.

See the <a href="https://create.roblox.com/docs/cloud/guides/analytics">Analytics guide</a> for more information.

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `universe.analytics:read`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer` | Yes | The universe ID to query metrics for. |

**Request Body:** `application/json` — Type: `AnalyticsQueryPublicApi.QueryRequest`

See [AnalyticsQueryPublicApi.QueryRequest](#analyticsquerypublicapi-queryrequest) in Models.

**Request example:**
```json
{
  "metric": "string",
  "granularity": "OneMinute",
  "startTime": "2024-01-01T00:00:00Z",
  "endTime": "2024-01-01T00:00:00Z",
  "breakdown": [
    "string"
  ],
  "filter": [
    {
      "dimension": "...",
      "values": "...",
      "operation": "..."
    }
  ]
}
```

**Responses:**

- `200`: OK → `QueryOperationResult`
- `202`: Accepted → `OperationPending`
- `400`: Bad Request → `AnalyticsQueryPublicApi.OperationError`
- `403`: Forbidden → `AnalyticsQueryPublicApi.OperationError`
- `429`: Too Many Requests → `AnalyticsQueryPublicApi.OperationError`
- `500`: Internal Server Error → `AnalyticsQueryPublicApi.OperationError`
- `503`: Service Unavailable → `AnalyticsQueryPublicApi.OperationError`
- `504`: Gateway Timeout → `AnalyticsQueryPublicApi.OperationError`

**Response fields** (`QueryOperationResult`)

See [QueryOperationResult](#queryoperationresult) in Models.

**Response example:**
```json
{
  "path": "string",
  "done": false,
  "response": {
    "values": [
      "..."
    ]
  },
  "metadata": {
    "createdTime": "2024-01-01T00:00:00Z"
  }
}
```

**Error handling:** `429`: Retry with exponential backoff (start at 1s). `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 30/minute, perOauth2Authorization: 30/minute

**Example:**
```bash
curl -X POST -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/analytics-query-api/v1/universes/{UNIVERSEID}/metrics" \
  -H "Content-Type: application/json" \
  -d '{
  "metric": "string",
  "granularity": "OneMinute",
  "startTime": "2024-01-01T00:00:00Z",
  "endTime": "2024-01-01T00:00:00Z",
  "breakdown": [
    "string"
  ],
  "filter": [
    {
      "dimension": "...",
      "values": "...",
      "operation": "..."
    }
  ]
}'
```

### GET `/analytics-query-api/v1/universes/{universeId}/operations/dimension-values/{operationId}` [BETA]

Retrieves the result of a long-running dimension values operation.

See the <a href="https://create.roblox.com/docs/cloud/guides/analytics">Analytics guide</a> for more information.

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `universe.analytics:read`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer` | Yes | The universe ID the operation belongs to. |
| `operationId` | path | `string` | Yes | The operation id returned from a prior dimension values request. |

**Responses:**

- `200`: OK → `DimensionValuesOperationResult`
- `202`: Accepted → `OperationPending`
- `400`: Bad Request → `AnalyticsQueryPublicApi.OperationError`
- `404`: Not Found → `AnalyticsQueryPublicApi.OperationError`
- `429`: Too Many Requests → `AnalyticsQueryPublicApi.OperationError`
- `500`: Internal Server Error → `AnalyticsQueryPublicApi.OperationError`
- `503`: Service Unavailable → `AnalyticsQueryPublicApi.OperationError`
- `504`: Gateway Timeout → `AnalyticsQueryPublicApi.OperationError`

**Response fields** (`DimensionValuesOperationResult`)

See [DimensionValuesOperationResult](#dimensionvaluesoperationresult) in Models.

**Response example:**
```json
{
  "path": "string",
  "done": false,
  "response": {
    "values": [
      "..."
    ]
  },
  "metadata": {
    "createdTime": "2024-01-01T00:00:00Z"
  }
}
```

**Error handling:** `429`: Retry with exponential backoff (start at 1s). 

**Rate Limits:** perApiKeyOwner: 3000/minute, perOauth2Authorization: 3000/minute

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/analytics-query-api/v1/universes/{UNIVERSEID}/operations/dimension-values/{OPERATIONID}"
```

### GET `/analytics-query-api/v1/universes/{universeId}/operations/metrics/{operationId}` [BETA]

Retrieves the result of a long-running metrics query operation.

See the <a href="https://create.roblox.com/docs/cloud/guides/analytics">Analytics guide</a> for more information.

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `universe.analytics:read`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer` | Yes | The universe ID the operation belongs to. |
| `operationId` | path | `string` | Yes | The operation id returned from a prior query request. |

**Responses:**

- `200`: OK → `QueryOperationResult`
- `202`: Accepted → `OperationPending`
- `400`: Bad Request → `AnalyticsQueryPublicApi.OperationError`
- `404`: Not Found → `AnalyticsQueryPublicApi.OperationError`
- `429`: Too Many Requests → `AnalyticsQueryPublicApi.OperationError`
- `500`: Internal Server Error → `AnalyticsQueryPublicApi.OperationError`
- `503`: Service Unavailable → `AnalyticsQueryPublicApi.OperationError`
- `504`: Gateway Timeout → `AnalyticsQueryPublicApi.OperationError`

**Response fields** (`QueryOperationResult`)

See [QueryOperationResult](#queryoperationresult) in Models.

**Response example:**
```json
{
  "path": "string",
  "done": false,
  "response": {
    "values": [
      "..."
    ]
  },
  "metadata": {
    "createdTime": "2024-01-01T00:00:00Z"
  }
}
```

**Error handling:** `429`: Retry with exponential backoff (start at 1s). 

**Rate Limits:** perApiKeyOwner: 3000/minute, perOauth2Authorization: 3000/minute

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/analytics-query-api/v1/universes/{UNIVERSEID}/operations/metrics/{OPERATIONID}"
```

### GET `/log-attribute-http-service/v1/universe-regexes` [EXPERIMENTAL]

**Auth:** Cookie (`.ROBLOSECURITY`) or API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `universe.analytics:read`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | query | `integer` | No |  |
| `status` | query | `any` | No |  |

**Responses:**

- `200`: OK → `FindUniverseRegexesHttpResponse`

**Response fields** (`FindUniverseRegexesHttpResponse`)

See [FindUniverseRegexesHttpResponse](#finduniverseregexeshttpresponse) in Models.

**Response example:**
```json
{
  "universeRegexes": [
    {
      "id": "...",
      "universeId": "...",
      "regexStatus": "...",
      "pattern": "...",
      "output": "...",
      "order": "..."
    }
  ]
}
```

**Rate Limits:** perApiKeyOwner: 60/minute, perOauth2Authorization: 60/minute

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/log-attribute-http-service/v1/universe-regexes"
```

### POST `/log-attribute-http-service/v1/universe-regexes` [EXPERIMENTAL]

**Auth:** Cookie (`.ROBLOSECURITY`) or API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `universe.analytics:write`

**Request Body:** `application/json` — Type: `any`

**Responses:**

- `200`: OK → `UniverseRegexMutationHttpResponse`

**Response fields** (`UniverseRegexMutationHttpResponse`)

See [UniverseRegexMutationHttpResponse](#universeregexmutationhttpresponse) in Models.

**Response example:**
```json
{
  "order": 0
}
```

**Rate Limits:** perApiKeyOwner: 60/minute, perOauth2Authorization: 60/minute

**Example:**
```bash
curl -X POST -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/log-attribute-http-service/v1/universe-regexes" \
  -H "Content-Type: application/json" \
  -d '"..."'
```

### PUT `/log-attribute-http-service/v1/universe-regexes/{id}` [EXPERIMENTAL]

**Auth:** Cookie (`.ROBLOSECURITY`) or API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `universe.analytics:write`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `id` | path | `integer` | Yes |  |

**Request Body:** `application/json` — Type: `any`

**Responses:**

- `200`: OK → `UniverseRegexMutationHttpResponse`

**Response fields** (`UniverseRegexMutationHttpResponse`)

See [UniverseRegexMutationHttpResponse](#universeregexmutationhttpresponse) in Models.

**Response example:**
```json
{
  "order": 0
}
```

**Rate Limits:** perApiKeyOwner: 60/minute, perOauth2Authorization: 60/minute

**Example:**
```bash
curl -X PUT -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/log-attribute-http-service/v1/universe-regexes/{ID}" \
  -H "Content-Type: application/json" \
  -d '"..."'
```

### DELETE `/log-attribute-http-service/v1/universe-regexes/{id}` [EXPERIMENTAL]

**Auth:** Cookie (`.ROBLOSECURITY`) or API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `universe.analytics:write`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `id` | path | `integer` | Yes |  |

**Responses:**

- `200`: OK

**Rate Limits:** perApiKeyOwner: 60/minute, perOauth2Authorization: 60/minute

**Example:**
```bash
curl -X DELETE -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/log-attribute-http-service/v1/universe-regexes/{ID}"
```

### PUT `/log-attribute-http-service/v1/universe-regexes/{id}/ignore` [EXPERIMENTAL]

**Auth:** Cookie (`.ROBLOSECURITY`) or API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `universe.analytics:write`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `id` | path | `integer` | Yes |  |

**Responses:**

- `200`: OK

**Rate Limits:** perApiKeyOwner: 60/minute, perOauth2Authorization: 60/minute

**Example:**
```bash
curl -X PUT -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/log-attribute-http-service/v1/universe-regexes/{ID}/ignore"
```

### PUT `/log-attribute-http-service/v1/universe-regexes/{id}/reorder` [EXPERIMENTAL]

**Auth:** Cookie (`.ROBLOSECURITY`) or API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `universe.analytics:write`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `id` | path | `integer` | Yes |  |

**Request Body:** `application/json` — Type: `any`

**Responses:**

- `200`: OK → `UniverseRegexMutationHttpResponse`

**Response fields** (`UniverseRegexMutationHttpResponse`)

See [UniverseRegexMutationHttpResponse](#universeregexmutationhttpresponse) in Models.

**Response example:**
```json
{
  "order": 0
}
```

**Rate Limits:** perApiKeyOwner: 60/minute, perOauth2Authorization: 60/minute

**Example:**
```bash
curl -X PUT -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/log-attribute-http-service/v1/universe-regexes/{ID}/reorder" \
  -H "Content-Type: application/json" \
  -d '"..."'
```

### GET `/universe-performance-raqi/v1/events/logging/universe/{universeId}/log-details` [EXPERIMENTAL]

Get logs based on message hash ids, keywords, placeVersions, start/end time.

**Auth:** Cookie (`.ROBLOSECURITY`) or API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `universe.analytics:read`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer` | Yes |  |
| `messageHashIds` | query | `string[]` | No |  |
| `keyword` | query | `string` | No | Optional keyword to help highlight matching keyword in the error message |
| `startTime` | query | `string` | No | Optional query window start; omitted values are defaulted server-side. |
| `endTime` | query | `string` | No | Optional query window end; omitted values are defaulted server-side. |
| `placeId` | query | `integer` | No | Optional place id filter. |
| `placeVersions` | query | `integer[]` | No | Optional place version filters. |
| `firstSeenPlaceVersion` | query | `integer` | No | Optional minimum first seen place version filter (inclusive). |

**Responses:**

- `200`: Success → `ErrorLogDetailResponse`
- `400`: Bad Request → `ActionResult`
- `401`: Unauthorized → `ActionResult`
- `403`: Forbidden → `ActionResult`
- `500`: Server Error → `ActionResult`

**Response fields** (`ErrorLogDetailResponse`)

See [ErrorLogDetailResponse](#errorlogdetailresponse) in Models.

**Response example:**
```json
{
  "values": [
    {
      "id": "...",
      "logSeverity": "...",
      "logSource": "...",
      "os": "...",
      "platform": "...",
      "message": "..."
    }
  ]
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 60/minute, perOauth2Authorization: 60/minute

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/universe-performance-raqi/v1/events/logging/universe/{UNIVERSEID}/log-details"
```

## Models

### AnalyticsAlertControlPlane.Models.AlertDetailResponse

Full details of a saved alert configuration.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `alertId` | `string` | Yes | Unique identifier of the alert configuration (string-encoded 64-bit integer). |
| `resourceType` | `AlertStorage.ResourceType` | Yes |  |
| `resourceId` | `string` | Yes | Numeric ID of the resource this alert monitors (e.g. the universe ID). |
| `name` | `string` | Yes | Display name of the alert. Must be unique within the resource. |
| `metric` | `string` | Yes | Name of the metric this alert evaluates. |
| `description` | `string` | No | Optional free-text description of the alert's purpose. |
| `severity` | `AlertStorage.Severity` | Yes |  |
| `interval` | `AlertStorage.AlertInterval` | Yes |  |
| `consecutiveOccurrences` | `integer` | Yes | Number of consecutive evaluation periods the condition must be met before the alert fires. Must be at least 1. For example, a value of 3 with a 1-minute interval means the condition must hold for 3 consecutive minutes before an incident is opened. |
| `filter` | `AnalyticsAlertControlPlane.Models.AlertQueryFilter[]` | No | Optional dimension filters applied to the metric query. Each entry restricts the metric to rows where the specified dimension matches one of the given values. |
| `breakdown` | `AnalyticsAlertControlPlane.Models.AlertQueryBreakdown[]` | No | Optional grouping dimensions for the metric query. When set, the alert evaluates the metric independently for each combination of dimension values and fires if any group breaches the condition. |
| `condition` | `AlertStorage.AlertCondition` | Yes |  |
| `configState` | `AlertStorage.AlertConfigState` | Yes |  |
| `webhookReceiverConfig` | `AlertStorage.WebhookReceiverConfig` | No |  |
| `firingStatus` | `AlertStorage.FiringStatus` | Yes |  |
| `lastFiredAt` | `string` | No | Timestamp of the most recent firing event. `null` if the alert has never fired. |
| `createdAt` | `string` | Yes | Timestamp when this alert configuration was created (UTC). |
| `lastModifiedAt` | `string` | Yes | Timestamp of the most recent modification to this alert configuration (UTC). |
| `lastModifiedBy` | `string` | No | ID of the user who last modified this alert configuration. `null` if the last modification was made by the system. |

### AnalyticsAlertControlPlane.Models.ErrorResponse

Standard error response body for the Alerts API.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `errorCode` | `string` | No | Machine-readable error code (e.g. PERMISSION_DENIED). |
| `message` | `string` | No | Human-readable error description. |

### AnalyticsAlertControlPlane.Models.CreateAlertConfigRequest

Request body for creating a new alert configuration.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | `string` | Yes | Display name of the alert. Must be unique within the resource. Maximum length is 128 characters and the value is subject to Roblox text-moderation policies. |
| `metric` | `string` | Yes | Name of the metric this alert should evaluate. |
| `description` | `string` | No | Optional free-text description of the alert's purpose. |
| `severity` | `AlertStorage.Severity` | Yes |  |
| `interval` | `AlertStorage.AlertInterval` | Yes |  |
| `consecutiveOccurrences` | `integer` | Yes | Number of consecutive evaluation periods the condition must be met before the alert fires. Must be at least 1. For example, a value of 3 with a 1-minute interval means the condition must hold for 3 consecutive minutes before an incident is opened. |
| `breakdown` | `AnalyticsAlertControlPlane.Models.AlertQueryBreakdown[]` | No | Optional grouping dimensions for the metric query. When set, the alert evaluates the metric independently for each combination of dimension values and fires if any group breaches the condition. |
| `filter` | `AnalyticsAlertControlPlane.Models.AlertQueryFilter[]` | No | Optional dimension filters applied to the metric query. Each entry restricts the metric to rows where the specified dimension matches one of the given values. |
| `condition` | `AnalyticsAlertControlPlane.Models.AlertConditionInput` | Yes |  |
| `webhookReceiverConfig` | `AlertStorage.WebhookReceiverConfig` | No |  |

### AnalyticsAlertControlPlane.Models.IncidentDetailResponse

Details of a single alert incident.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | `string` | Yes | Unique identifier of this incident. |
| `resourceType` | `AlertStorage.ResourceType` | Yes |  |
| `resourceId` | `string` | Yes | Numeric ID of the resource this incident belongs to (e.g. the universe ID). |
| `status` | `AlertStorage.FiringStatus` | Yes |  |
| `openedAt` | `string` | Yes | Timestamp when this incident was first opened (UTC). |
| `openedWindowStartAt` | `string` | Yes | Start of the evaluation window that first satisfied the alert condition and opened this incident (UTC). |
| `resolvedAt` | `string` | No | Timestamp when this incident was resolved (UTC). `null` if the incident is still active. |
| `resolvedWindowStartAt` | `string` | No | Start of the evaluation window in which the alert condition was no longer satisfied, causing the incident to be resolved (UTC). `null` if the incident is still active. |
| `firstFiringMetadata` | `AnalyticsAlertControlPlane.Models.FiringMetadataResponse` | Yes |  |
| `latestFiringMetadata` | `AnalyticsAlertControlPlane.Models.FiringMetadataResponse` | Yes |  |
| `alertConfig` | `AnalyticsAlertControlPlane.Models.AlertConfigSummary` | Yes |  |

### AnalyticsAlertControlPlane.Models.UpdateAlertConfigRequest

Request body for partially updating an alert configuration (PATCH semantics). All fields
are optional; only the fields present in the request body are updated.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | `string` | No | New display name for the alert. Must be unique within the resource. Subject to Roblox text-moderation policies. |
| `metric` | `string` | No | New metric name this alert should evaluate. |
| `description` | `string` | No | New free-text description of the alert's purpose. |
| `severity` | `AlertStorage.Severity` | No |  |
| `interval` | `AlertStorage.AlertInterval` | No |  |
| `consecutiveOccurrences` | `integer` | No | New consecutive-occurrences count. When set, the alert will require the condition to hold for this many consecutive evaluation periods before firing. Must be at least 1. |
| `breakdown` | `AnalyticsAlertControlPlane.Models.AlertQueryBreakdown[]` | No | New grouping dimensions for the metric query. Replaces the existing breakdown entirely when provided. |
| `filter` | `AnalyticsAlertControlPlane.Models.AlertQueryFilter[]` | No | New dimension filters for the metric query. Replaces the existing filter list entirely when provided. |
| `condition` | `AnalyticsAlertControlPlane.Models.AlertConditionInput` | No |  |
| `webhookReceiverConfig` | `AlertStorage.WebhookReceiverConfig` | No |  |
| `configState` | `AlertStorage.AlertConfigState` | No |  |

### QueryUniverseBenchmarkResponse

QueryUniverseBenchmarkResponse is the response message for QueryUniverseBenchmark.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `result` | `any` | No | The benchmark series, one per percentile. |
| `availableTypes` | `BenchmarkType[]` | No | The benchmark types available for this universe and metric. Request one with `benchmark_type`. |
| `objective` | `BENCHMARK_OBJECTIVE_INVALID \| BENCHMARK_OBJECTIVE_MAXIMIZE \| BENCHMARK_OBJECTIVE_MINIMIZE` | No | Whether higher (`BENCHMARK_OBJECTIVE_MAXIMIZE`) or lower (`BENCHMARK_OBJECTIVE_MINIMIZE`) values of the metric are favorable. |

### AnalyticsBenchmarkApi.Status

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `code` | `integer` | No |  |
| `message` | `string` | No |  |
| `details` | `AnalyticsBenchmarkApi.Any[]` | No |  |

### AnalyticsQueryPublicApi.DimensionValuesRequest

A request to query dimension values.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `metric` | `string` | Yes | The metric that provides context for resolving dimension namespaces. |
| `dimensions` | `string[]` | No | The dimensions to retrieve values for. Each entry is a single dimension name. |
| `startTime` | `string` | Yes | The inclusive start of the query time range. Any UTC offset is accepted; results are always bucketed in UTC. |
| `endTime` | `string` | Yes | The exclusive end of the query time range. Any UTC offset is accepted; results are always bucketed in UTC. |
| `filter` | `AnalyticsQueryPublicApi.QueryFilter[]` | No | Filters to apply to the query. |
| `granularity` | `AnalyticsQueryPublicApi.MetricGranularity` | No |  |
| `limit` | `integer` | No | The maximum number of values to return per dimension. |

### DimensionValuesOperationResult

A completed long-running dimension values operation with results.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `path` | `string` | No | The server-assigned resource path. |
| `done` | `boolean` | No | If false, the operation is still in progress. If true, the operation is completed. |
| `response` | `AnalyticsQueryPublicApi.DimensionValuesResponse` | No |  |
| `metadata` | `AnalyticsQueryPublicApi.OperationMetadata` | No |  |

### OperationPending

A long-running operation that is still in progress.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `path` | `string` | No | The server-assigned resource path. |
| `done` | `boolean` | No | If false, the operation is still in progress. If true, the operation is completed. |
| `metadata` | `AnalyticsQueryPublicApi.OperationMetadata` | No |  |

### AnalyticsQueryPublicApi.OperationError

A completed long-running operation that failed with an error.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `path` | `string` | No | The server-assigned resource path. |
| `done` | `boolean` | No | If false, the operation is still in progress. If true, the operation is completed. |
| `error` | `AnalyticsQueryPublicApi.QueryError` | No |  |
| `metadata` | `AnalyticsQueryPublicApi.OperationMetadata` | No |  |

### AnalyticsQueryPublicApi.QueryRequest

A request to query time series metric data.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `metric` | `string` | Yes | The metric to query. |
| `granularity` | `AnalyticsQueryPublicApi.MetricGranularity` | Yes |  |
| `startTime` | `string` | Yes | The inclusive start of the query time range. Any UTC offset is accepted; results are always bucketed in UTC. |
| `endTime` | `string` | Yes | The exclusive end of the query time range. Any UTC offset is accepted; results are always bucketed in UTC. |
| `breakdown` | `string[]` | No | The dimensions to group results by. Each entry is a single dimension name. |
| `filter` | `AnalyticsQueryPublicApi.QueryFilter[]` | No | Filters to apply to the query. |
| `limit` | `integer` | No | The maximum number of breakdown series to return. |

### QueryOperationResult

A completed long-running query operation with results.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `path` | `string` | No | The server-assigned resource path. |
| `done` | `boolean` | No | If false, the operation is still in progress. If true, the operation is completed. |
| `response` | `AnalyticsQueryPublicApi.QueryResponse` | No |  |
| `metadata` | `AnalyticsQueryPublicApi.OperationMetadata` | No |  |

### FindUniverseRegexesHttpResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `universeRegexes` | `UniverseRegexHttpResponse[]` | No |  |

### UniverseRegexMutationHttpResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `order` | `integer` | No |  |

### ErrorLogDetailResponse

Response for top error logs

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `values` | `ErrorLogDetail[]` | No | The analytics data for display. |