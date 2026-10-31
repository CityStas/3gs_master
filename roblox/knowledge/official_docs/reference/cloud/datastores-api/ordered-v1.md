---
name: "Ordered data stores (beta)"
last_updated: 2026-10-30T19:55:51Z
type: opencloud
api_base_url: "https://apis.roblox.com/ordered-data-stores"
version: "0.0.1"
endpoints: 6
auth: [api-key]
description: "This page includes reference documentation for working with the Open Cloud v1 API for ordered data stores"
---

# Ordered data stores (beta)

This page includes reference documentation for working with the Open Cloud v1 API for ordered data stores. For information on using the v2 API, see the [usage guide](/docs/en-us/cloud/guides/data-stores.md).

**API Version:** 0.0.1

**Base URL(s):**
- `https://apis.roblox.com/ordered-data-stores`

## Authentication

Each endpoint requires one of the following authentication methods:

- **API Key**: Pass your key in the `x-api-key` HTTP header. Create keys at [Creator Dashboard](https://create.roblox.com/dashboard/credentials).

```
# API Key example
curl -H "x-api-key: YOUR_API_KEY" https://apis.roblox.com/...

# OAuth 2.0 example
curl -H "Authorization: Bearer YOUR_ACCESS_TOKEN" https://apis.roblox.com/...
```

## Endpoints

### GET `/v1/universes/{universeId}/orderedDataStores/{orderedDataStore}/scopes/{scope}/entries` [BETA]

Returns a list of entries from an ordered data store.

**Auth:** API Key (`x-api-key` header)

**Scopes:** `universe.ordered-data-store.scope.entry:read`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `string` | Yes | The identifier of the experience with ordered data stores that you want to access. You can find your experience's universe ID on Creator Hub. |
| `orderedDataStore` | path | `string` | Yes | The name of the target ordered data store. |
| `scope` | path | `string` | Yes | The name of the data store scope. See [Scopes](/docs/en-us/cloud/guides/data-stores/request-handling.md#scopes). |
| `max_page_size` | query | `integer` | No | The maximum number of entries to return. The service may return fewer than this value. The default value is `10`. The maximum value is `100`, and any input above 100 is coerced to `100`. |
| `page_token` | query | `string` | No | A page token received from a previous `List` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `List` must match the call providing the page token. |
| `order_by` | query | `string` | No | The enumeration direction. The order by default is ascending. Input a `desc` suffix for descending. |
| `filter` | query | `string` | No | The range of qualifying values of entries to return. See [Filters](/docs/en-us/cloud/guides/data-stores/request-handling.md#filters). |

**Responses:**

- `200`: OK → `ListEntriesResponse`
- `400`: Bad Request: invalid orderedDataStore, scope or entry name or encoding.
- `403`: Forbidden: studio access to APIs is not allowed, incorrect API key or scope.
- `429`: Too Many Requests.

**Response fields** (`ListEntriesResponse`)

See [ListEntriesResponse](#listentriesresponse) in Models.

**Response example:**
```json
{
  "entries": [
    {
      "path": "...",
      "id": "...",
      "value": "..."
    }
  ],
  "nextPageToken": "string"
}
```

**Error handling:** `429`: Retry with exponential backoff (start at 1s). `403`: Verify your API key has the required scopes listed above. 

**Rate Limit Note:** See [Throttling](/docs/en-us/cloud/guides/data-stores/throttling.md).

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/ordered-data-stores/v1/universes/{UNIVERSEID}/orderedDataStores/{ORDEREDDATASTORE}/scopes/{SCOPE}/entries"
```

### POST `/v1/universes/{universeId}/orderedDataStores/{orderedDataStore}/scopes/{scope}/entries` [BETA]

Creates a new entry with the content value provided.

**Auth:** API Key (`x-api-key` header)

**Scopes:** `universe.ordered-data-store.scope.entry:write`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `string` | Yes | The identifier of the experience with ordered data stores that you want to access. You can find your experience's universe ID on Creator Hub. |
| `orderedDataStore` | path | `string` | Yes | The name of the ordered data store. |
| `scope` | path | `string` | Yes | The name of the data store scope. See [Scopes](/docs/en-us/cloud/guides/data-stores/request-handling.md#scopes). |
| `id` | query | `string` | Yes | The name of the entry. |

**Request Body:** `application/json` — Type: `CreateEntryRequest`

See [CreateEntryRequest](#createentryrequest) in Models.

**Request example:**
```json
{
  "value": 0
}
```

**Responses:**

- `200`: OK → `Entry`
- `400`: Bad Request: invalid orderedDataStore, scope or entry name or encoding.
- `403`: Forbidden: studio access to APIs is not allowed, incorrect API key or scope.
- `404`: Not found.
- `429`: Too Many Requests.

**Response fields** (`Entry`)

See [Entry](#entry) in Models.

**Response example:**
```json
{
  "path": "string",
  "id": "string",
  "value": 0
}
```

**Error handling:** `429`: Retry with exponential backoff (start at 1s). `403`: Verify your API key has the required scopes listed above. 

**Rate Limit Note:** See [Throttling](/docs/en-us/cloud/guides/data-stores/throttling.md).

**Example:**
```bash
curl -X POST -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/ordered-data-stores/v1/universes/{UNIVERSEID}/orderedDataStores/{ORDEREDDATASTORE}/scopes/{SCOPE}/entries?id={VALUE}" \
  -H "Content-Type: application/json" \
  -d '{
  "value": 0
}'
```

### GET `/v1/universes/{universeId}/orderedDataStores/{orderedDataStore}/scopes/{scope}/entries/{entry}` [BETA]

Gets and returns the specified entry.

**Auth:** API Key (`x-api-key` header)

**Scopes:** `universe.ordered-data-store.scope.entry:read`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `string` | Yes | The identifier of the experience with ordered data stores that you want to access. You can find your experience's universe ID on Creator Hub. |
| `orderedDataStore` | path | `string` | Yes | The name of the ordered data store. |
| `scope` | path | `string` | Yes | The name of the data store scope. See [Scopes](/docs/en-us/cloud/guides/data-stores/request-handling.md#scopes). |
| `entry` | path | `string` | Yes | The entry ID. |

**Responses:**

- `200`: OK → `Entry`
- `400`: Bad Request: invalid orderedDataStore, scope or entry name or encoding.
- `403`: Forbidden: studio access to APIs is not allowed, incorrect API key or scope.
- `404`: Not found.
- `429`: Too Many Requests.

**Response fields** (`Entry`)

See [Entry](#entry) in Models.

**Response example:**
```json
{
  "path": "string",
  "id": "string",
  "value": 0
}
```

**Error handling:** `429`: Retry with exponential backoff (start at 1s). `403`: Verify your API key has the required scopes listed above. 

**Rate Limit Note:** See [Throttling](/docs/en-us/cloud/guides/data-stores/throttling.md).

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/ordered-data-stores/v1/universes/{UNIVERSEID}/orderedDataStores/{ORDEREDDATASTORE}/scopes/{SCOPE}/entries/{ENTRY}"
```

### PATCH `/v1/universes/{universeId}/orderedDataStores/{orderedDataStore}/scopes/{scope}/entries/{entry}` [BETA]

Updates an entry value and returns the updated entry.

**Auth:** API Key (`x-api-key` header)

**Scopes:** `universe.ordered-data-store.scope.entry:write`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `string` | Yes | The identifier of the experience with ordered data stores that you want to access. You can find your experience's universe ID on Creator Hub. |
| `orderedDataStore` | path | `string` | Yes | The name of the ordered data store. |
| `scope` | path | `string` | Yes | The name of the data store scope. See [Scopes](/docs/en-us/cloud/guides/data-stores/request-handling.md#scopes). |
| `entry` | path | `string` | Yes | The entry ID. |
| `allow_missing` | query | `boolean` | No | The flag to allow the creation of an entry if the entry doesn't exist. See [Allow missing flags](/docs/en-us/cloud/guides/data-stores/request-handling.md.md#allow-missing-flags). |

**Request Body:** `application/json` — Type: `UpdateEntryRequest`

See [UpdateEntryRequest](#updateentryrequest) in Models.

**Request example:**
```json
{
  "value": 0
}
```

**Responses:**

- `200`: OK → `Entry`
- `400`: Bad Request: invalid orderedDataStore, scope or entry name or encoding.
- `403`: Forbidden: studio access to APIs is not allowed, incorrect API key or scope.
- `404`: Not found.
- `409`: Aborted.
- `429`: Too Many Requests.

**Response fields** (`Entry`)

See [Entry](#entry) in Models.

**Response example:**
```json
{
  "path": "string",
  "id": "string",
  "value": 0
}
```

**Error handling:** `429`: Retry with exponential backoff (start at 1s). `403`: Verify your API key has the required scopes listed above. 

**Rate Limit Note:** See [Throttling](/docs/en-us/cloud/guides/data-stores/throttling.md).

**Example:**
```bash
curl -X PATCH -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/ordered-data-stores/v1/universes/{UNIVERSEID}/orderedDataStores/{ORDEREDDATASTORE}/scopes/{SCOPE}/entries/{ENTRY}" \
  -H "Content-Type: application/json" \
  -d '{
  "value": 0
}'
```

### DELETE `/v1/universes/{universeId}/orderedDataStores/{orderedDataStore}/scopes/{scope}/entries/{entry}` [BETA]

Deletes the specified entry. Unlike standard data stores, which mark entries for deletion, ordered data store entries are deleted immediately.

**Auth:** API Key (`x-api-key` header)

**Scopes:** `universe.ordered-data-store.scope.entry:write`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `string` | Yes | The identifier of the experience with ordered data stores that you want to access. You can find your experience's universe ID on Creator Hub. |
| `orderedDataStore` | path | `string` | Yes | The name of the ordered data store. |
| `scope` | path | `string` | Yes | The name of the data store scope. See [Scopes](/docs/en-us/cloud/guides/data-stores/request-handling.md#scopes). |
| `entry` | path | `string` | Yes | The entry ID. |

**Responses:**

- `200`: Success: the entry was successfully deleted or didn't exist.
- `400`: Bad Request: invalid orderedDataStore, scope or entry name or encoding.
- `403`: Forbidden: Studio access to APIs is not allowed, incorrect API key or scope.
- `404`: Not found.
- `429`: Too Many Requests.

**Error handling:** `429`: Retry with exponential backoff (start at 1s). `403`: Verify your API key has the required scopes listed above. 

**Rate Limit Note:** See [Throttling](/docs/en-us/cloud/guides/data-stores/throttling.md).

**Example:**
```bash
curl -X DELETE -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/ordered-data-stores/v1/universes/{UNIVERSEID}/orderedDataStores/{ORDEREDDATASTORE}/scopes/{SCOPE}/entries/{ENTRY}"
```

### POST `/v1/universes/{universeId}/orderedDataStores/{orderedDataStore}/scopes/{scope}/entries/{entry}:increment` [BETA]

Increments the value of the key by the provided amount and returns the updated entry.

Known issue: Entry values can increment past the valid range and this may persist in the backend. Returned values will clamp to the valid range.

**Auth:** API Key (`x-api-key` header)

**Scopes:** `universe.ordered-data-store.scope.entry:write`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `string` | Yes | The identifier of the experience with ordered data stores that you want to access. You can find your experience's universe ID on Creator Hub. |
| `orderedDataStore` | path | `string` | Yes | The name of the ordered data store. |
| `scope` | path | `string` | Yes | The name of the data store scope. See [Scopes](/docs/en-us/cloud/guides/data-stores/request-handling.md#scopes). |
| `entry` | path | `string` | Yes | The entry ID. |

**Request Body:** `application/json` — Type: `IncrementEntryRequest`

See [IncrementEntryRequest](#incremententryrequest) in Models.

**Request example:**
```json
{
  "amount": 0
}
```

**Responses:**

- `200`: OK → `Entry`
- `400`: Bad Request: invalid orderedDataStore, scope or entry name or encoding.
- `403`: Forbidden: studio access to APIs is not allowed, incorrect API key or scope.
- `404`: Not found.
- `429`: Too Many Requests.

**Response fields** (`Entry`)

See [Entry](#entry) in Models.

**Response example:**
```json
{
  "path": "string",
  "id": "string",
  "value": 0
}
```

**Error handling:** `429`: Retry with exponential backoff (start at 1s). `403`: Verify your API key has the required scopes listed above. 

**Rate Limit Note:** See [Throttling](/docs/en-us/cloud/guides/data-stores/throttling.md).

**Example:**
```bash
curl -X POST -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/ordered-data-stores/v1/universes/{UNIVERSEID}/orderedDataStores/{ORDEREDDATASTORE}/scopes/{SCOPE}/entries/{ENTRY}:increment" \
  -H "Content-Type: application/json" \
  -d '{
  "amount": 0
}'
```

## Models

### Entry

Represents an entry.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `path` | `string` | No | The resource path of the request. |
| `id` | `string` | No | The name of the entry |
| `value` | `integer` | No | The value of the entry. |

### IncrementEntryRequest

Increments entry value.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `amount` | `integer` | Yes | The amount to increment by the entry value. If the input value exceeds the maximum value supported by int64, which is 9,223,372,036,854,775,807, the request fails with a 400 Bad Request error. |

### UpdateEntryRequest

Updates the entry provided with a new value.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `value` | `integer` | Yes | The value to update the entry. If the input value exceeds the maximum value supported by int64, which is 9,223,372,036,854,775,807, the request fails with a 400 Bad Request error. |

### CreateEntryRequest

Creates a new entry with the value provided.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `value` | `integer` | Yes | The value to set the new entry. If the input value exceeds the maximum value supported by int64, which is 9,223,372,036,854,775,807, the request fails with a 400 Bad Request error. |

### ListEntriesResponse

A list of Entries in the parent collection.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `entries` | `Entry[]` | No | The Entries from the specified Scope. |
| `nextPageToken` | `string` | No | A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages. |
