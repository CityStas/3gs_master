---
name: "Data and memory stores"
last_updated: 2026-10-30T19:56:08Z
type: feature
api_base_url: "https://apis.roblox.com"
endpoints: 48
auth: [api-key, oauth2, cookie]
description: "Manage persistent player data using standard data stores, ordered data stores, and memory stores"
---

# Data and memory stores

Manage persistent player data using standard data stores, ordered data stores, and memory stores. See the [Data Stores Guide](/cloud/guides/data-stores) for implementation examples.

Common use cases include:

- **Player Data Management**: [Store](#Cloud_CreateDataStoreEntry__Using_Universes) and [retrieve](#Cloud_GetDataStoreEntry__Using_Universes_DataStores) player profiles, inventories, and progress
- **Leaderboards**: Use [ordered data stores](#Cloud_ListOrderedDataStoreEntries) to create global or per-experience leaderboards sorted by score
- **Customer Support Tools**: Build external portals to [view](#Cloud_GetDataStoreEntry__Using_Universes_DataStores) and [modify](#Cloud_UpdateDataStoreEntry__Using_Universes_DataStores) player data

> **Getting started:** See [Open Cloud data stores](/docs/en-us/cloud/guides/data-stores.md), [Handle Open Cloud data store requests](/docs/en-us/cloud/guides/data-stores/request-handling.md), [Rate limits and throttling](/docs/en-us/cloud/guides/data-stores/throttling.md) for a complete walkthrough with working examples.

> **See also:** To secrets store for API keys and tokens, see [secrets-store](/docs/cloud/reference/features/secrets-store.md).

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

### GET `/cloud/v2/universes/{universe_id}/data-stores` [STABLE]

List Data Stores

Returns a list of data stores.

Data stores scheduled for permanent deletion are omitted from the results
by default (or when `showDeleted` is set to `false`). When this is the
case, the operation will check up to 512 data stores. If all checked data
stores are deleted, it will return an empty list with a page token to
continue iteration.

**Auth:** API Key (`x-api-key` header)

**Scopes:** `universe-datastores.control:list`, `universe-datastores.control:list`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universe_id` | path | `string` | Yes | The universe ID. |
| `maxPageSize` | query | `integer` | No | The maximum number of data stores to return. The service might return fewer than this value. If unspecified, at most 10 data stores are returned. The maximum value is 100 and higher values are set to 100. |
| `pageToken` | query | `string` | No | A page token, received from a previous call, to retrieve a subsequent page.  When paginating, all other parameters provided to the subsequent call must match the call that provided the page token. |
| `filter` | query | `string` | No | This field may be set in order to filter the resources returned.  The `filter` field supports a very small subset of CEL:  * Only the `id` field is supported. * Only the `startsWith` function is available; no other operators nor   built-ins are supported.  Example filter: `id.startsWith("foo")` |
| `showDeleted` | query | `boolean` | No | If true, resources marked for pending deletion will be included in the results. |

**Responses:**

- `200`: OK → `ListDataStoresResponse`

**Response fields** (`ListDataStoresResponse`)

See [ListDataStoresResponse](#listdatastoresresponse) in Models.

**Response example:**
```json
{
  "dataStores": [
    {
      "path": "...",
      "createTime": "...",
      "expireTime": "...",
      "state": "...",
      "id": "..."
    }
  ],
  "nextPageToken": "string"
}
```

**Rate Limits:** perApiKeyOwner: 1000000/minute
**Rate Limit Note:** Data stores requests are subject to additional throttling limits described in the [Open Cloud guide for data stores](https://create.roblox.com/docs/cloud/guides/data-stores/throttling).

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/cloud/v2/universes/{UNIVERSE_ID}/data-stores"
```

### DELETE `/cloud/v2/universes/{universe_id}/data-stores/{data_store_id}` [BETA]

Delete Data Store

Schedules the specified data store for permanent deletion.

This operation assigns the data store an expiry time 30 days in the future,
at which point permanent deletion begins. To cancel, use the
`UndeleteDataStore` operation before the data store's expiry time.

Permanent deletion consists of deleting all of the entries in the data
store and then the data store resource itself. The data store is no longer
returned by the `ListDataStores` Open Cloud endpoint or
`ListDataStoresAsync` Luau API, and you can reuse the data store's name.

The duration of the permanent deletion process depends on the number of
entries in the data store. However, you can expect a data store with 1
million or fewer entries to be permanently deleted within 3 days.

Data stores scheduled for permanent deletion are returned by the
`ListDataStores` Open Cloud endpoint when the query parameter `showDeleted`
is set to `true`. In the return value, each data store will have a
`DELETED` state and an `expireTime` field.

Data stores scheduled for permanent deletion are immediately made
inaccessible, meaning attempts to read or write to their entries will fail.

Note: Due to caching in the backend service, attempts to read from or write
to entries in these data stores can continue to succeed for a limited time
after the deletion:
* `GetDataStoreEntry`: can succeed for up to 24 hours.
* All other endpoints: can succeed for several minutes.

If the data store is already in a `DELETED` state, this operation is a
no-op, and the data store is returned as-is.

**Auth:** API Key (`x-api-key` header)

**Scopes:** `universe-datastores.control:delete`, `universe-datastores.control:delete`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universe_id` | path | `string` | Yes | The universe ID. |
| `data_store_id` | path | `string` | Yes | The data-store ID. |

**Responses:**

- `200`: OK → `DataStore`

**Response fields** (`DataStore`)

See [DataStore](#datastore) in Models.

**Response example:**
```json
{
  "path": "string",
  "createTime": "2024-01-01T00:00:00Z",
  "expireTime": "2024-01-01T00:00:00Z",
  "state": "STATE_UNSPECIFIED",
  "id": "string"
}
```

**Rate Limits:** perApiKeyOwner: 1000000/minute
**Rate Limit Note:** Data stores requests are subject to additional throttling limits described in the [Open Cloud guide for data stores](https://create.roblox.com/docs/cloud/guides/data-stores/throttling).

**Example:**
```bash
curl -X DELETE -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/cloud/v2/universes/{UNIVERSE_ID}/data-stores/{DATA_STORE_ID}"
```

### GET `/cloud/v2/universes/{universe_id}/data-stores/{data_store_id}/entries` [STABLE]

List Data Store Entries

Returns a list of entries from a data store.

Only the `path` and `id` fields are populated; use `GetDataStoreEntry`
to retrieve other fields.

Specify the wildcard scope (`-`) to list entries from all scopes.

**Auth:** API Key (`x-api-key` header)

**Scopes:** `universe-datastores.objects:list`, `universe-datastores.objects:list`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universe_id` | path | `string` | Yes | The universe ID. |
| `data_store_id` | path | `string` | Yes | The data-store ID. |
| `maxPageSize` | query | `integer` | No | The maximum number of data store entries to return. The service might return fewer than this value. If unspecified, at most 10 data store entries are returned. The maximum value is 256 and higher values are set to 256. |
| `pageToken` | query | `string` | No | A page token, received from a previous call, to retrieve a subsequent page.  When paginating, all other parameters provided to the subsequent call must match the call that provided the page token. |
| `filter` | query | `string` | No | This field may be set in order to filter the resources returned.  The `filter` field supports a very small subset of CEL:  * Only the `id` field is supported. * Only the `startsWith` function is available; no other operators nor   built-ins are supported.  Example filter: `id.startsWith("foo")` |
| `showDeleted` | query | `boolean` | No | If true, resources marked for pending deletion will be included in the results. |

**Responses:**

- `200`: OK → `ListDataStoreEntriesResponse`

**Response fields** (`ListDataStoreEntriesResponse`)

See [ListDataStoreEntriesResponse](#listdatastoreentriesresponse) in Models.

**Response example:**
```json
{
  "dataStoreEntries": [
    {
      "path": "...",
      "createTime": "...",
      "revisionId": "...",
      "revisionCreateTime": "...",
      "state": "...",
      "etag": "..."
    }
  ],
  "nextPageToken": "string"
}
```

**Rate Limits:** perApiKeyOwner: 1000000/minute
**Rate Limit Note:** Data stores requests are subject to additional throttling limits described in the [Open Cloud guide for data stores](https://create.roblox.com/docs/cloud/guides/data-stores/throttling).

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/cloud/v2/universes/{UNIVERSE_ID}/data-stores/{DATA_STORE_ID}/entries"
```

### POST `/cloud/v2/universes/{universe_id}/data-stores/{data_store_id}/entries` [STABLE]

Create Data Store Entry

Creates an entry with the provided ID and value.

Returns a 400 Bad Request if the entry exists.

**Auth:** API Key (`x-api-key` header)

**Scopes:** `universe-datastores.objects:create`, `universe-datastores.objects:create`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universe_id` | path | `string` | Yes | The universe ID. |
| `data_store_id` | path | `string` | Yes | The data-store ID. |
| `id` | query | `string` | No | The ID to use for the data store entry, which will become the final component of the data store entry's resource path.  This value should be a 1-50 character string. We strongly recommend using only lowercase letters, numeric digits, and hyphens. |

**Request Body:** `application/json` — Type: `DataStoreEntry`

See [DataStoreEntry](#datastoreentry) in Models.

**Request example:**
```json
{
  "path": "string",
  "createTime": "2024-01-01T00:00:00Z",
  "revisionId": "string",
  "revisionCreateTime": "2024-01-01T00:00:00Z",
  "state": "STATE_UNSPECIFIED",
  "etag": "string"
}
```

**Responses:**

- `200`: OK → `DataStoreEntry`

**Response fields** (`DataStoreEntry`)

See [DataStoreEntry](#datastoreentry) in Models.

**Response example:**
```json
{
  "path": "string",
  "createTime": "2024-01-01T00:00:00Z",
  "revisionId": "string",
  "revisionCreateTime": "2024-01-01T00:00:00Z",
  "state": "STATE_UNSPECIFIED",
  "etag": "string"
}
```

**Rate Limits:** perApiKeyOwner: 1000000/minute
**Rate Limit Note:** Data stores requests are subject to additional throttling limits described in the [Open Cloud guide for data stores](https://create.roblox.com/docs/cloud/guides/data-stores/throttling).

**Example:**
```bash
curl -X POST -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/cloud/v2/universes/{UNIVERSE_ID}/data-stores/{DATA_STORE_ID}/entries" \
  -H "Content-Type: application/json" \
  -d '{
  "path": "string",
  "createTime": "2024-01-01T00:00:00Z",
  "revisionId": "string",
  "revisionCreateTime": "2024-01-01T00:00:00Z",
  "state": "STATE_UNSPECIFIED",
  "etag": "string"
}'
```

### GET `/cloud/v2/universes/{universe_id}/data-stores/{data_store_id}/entries/{entry_id}` [STABLE]

Get Data Store Entry

Gets the specified entry.

To get the entry at a specific revision, add `@<revisionId>` to the end of
the path.

For example, to get `my-entry` at the revision ID
`08DC3D3F43F9FCC1.0000000001.08DC3D3F43F9FCC1.01`, use the path
`/cloud/v2/universes/1234/data-stores/5678/entries/my-entry@08DC3D3F43F9FCC1.0000000001.08DC3D3F43F9FCC1.01`.

If your entry ID contains one or more `@` characters, and you want to get
the latest version rather than at any specific revision, append the special
revision ID `@latest` to the end of the path. Otherwise, the segment of the
entry ID after the last `@` will be interpreted as a revision ID.

For example, to get the latest revision of `my-entry`, use the path
`/cloud/v2/universes/1234/data-stores/5678/entries/my@entry@latest`.

To get the entry that was current at a specific time, add
`@latest:<timestamp>` to the end of the path, where `<timestamp>` is
RFC-3339 formatted. The given timestamp must be after
the Unix epoch (1/1/1970) and not more than ten minutes in the future.

For example, to get the revision of `my-entry` that was current on
12/2/2024 at 06:00 UTC, use the path
`/cloud/v2/universes/1234/data-stores/5678/entries/my-entry@latest:2024-12-02T06:00:00Z`.

**Auth:** API Key (`x-api-key` header)

**Scopes:** `universe-datastores.objects:read`, `universe-datastores.objects:read`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universe_id` | path | `string` | Yes | The universe ID. |
| `data_store_id` | path | `string` | Yes | The data-store ID. |
| `entry_id` | path | `string` | Yes | The entry ID. |

**Responses:**

- `200`: OK → `DataStoreEntry`

**Response fields** (`DataStoreEntry`)

See [DataStoreEntry](#datastoreentry) in Models.

**Response example:**
```json
{
  "path": "string",
  "createTime": "2024-01-01T00:00:00Z",
  "revisionId": "string",
  "revisionCreateTime": "2024-01-01T00:00:00Z",
  "state": "STATE_UNSPECIFIED",
  "etag": "string"
}
```

**Rate Limits:** perApiKeyOwner: 1000000/minute
**Rate Limit Note:** Data stores requests are subject to additional throttling limits described in the [Open Cloud guide for data stores](https://create.roblox.com/docs/cloud/guides/data-stores/throttling).

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/cloud/v2/universes/{UNIVERSE_ID}/data-stores/{DATA_STORE_ID}/entries/{ENTRY_ID}"
```

### PATCH `/cloud/v2/universes/{universe_id}/data-stores/{data_store_id}/entries/{entry_id}` [STABLE]

Update Data Store Entry

Updates the value, attributes, and users of an entry.

Updating specific revisions of the entry is **unsupported**. If you specify
a revision ID in the path and `allow_missing` is `true`, the update request
will instead create a new entry with the `@<revisionId>` suffix as part of
the key.

Partial update is **unsupported**. If attributes or users are not
provided when updating the value, they will be cleared. Value must always
be provided when updating an entry.

**Auth:** API Key (`x-api-key` header)

**Scopes:** `universe-datastores.objects:update`, `universe-datastores.objects:update`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universe_id` | path | `string` | Yes | The universe ID. |
| `data_store_id` | path | `string` | Yes | The data-store ID. |
| `entry_id` | path | `string` | Yes | The entry ID. |
| `allowMissing` | query | `boolean` | No | If set to true, and the data store entry is not found, a data store entry is created. |

**Request Body:** `application/json` — Type: `DataStoreEntry`

See [DataStoreEntry](#datastoreentry) in Models.

**Request example:**
```json
{
  "path": "string",
  "createTime": "2024-01-01T00:00:00Z",
  "revisionId": "string",
  "revisionCreateTime": "2024-01-01T00:00:00Z",
  "state": "STATE_UNSPECIFIED",
  "etag": "string"
}
```

**Responses:**

- `200`: OK → `DataStoreEntry`

**Response fields** (`DataStoreEntry`)

See [DataStoreEntry](#datastoreentry) in Models.

**Response example:**
```json
{
  "path": "string",
  "createTime": "2024-01-01T00:00:00Z",
  "revisionId": "string",
  "revisionCreateTime": "2024-01-01T00:00:00Z",
  "state": "STATE_UNSPECIFIED",
  "etag": "string"
}
```

**Rate Limits:** perApiKeyOwner: 1000000/minute
**Rate Limit Note:** Data stores requests are subject to additional throttling limits described in the [Open Cloud guide for data stores](https://create.roblox.com/docs/cloud/guides/data-stores/throttling).

**Example:**
```bash
curl -X PATCH -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/cloud/v2/universes/{UNIVERSE_ID}/data-stores/{DATA_STORE_ID}/entries/{ENTRY_ID}" \
  -H "Content-Type: application/json" \
  -d '{
  "path": "string",
  "createTime": "2024-01-01T00:00:00Z",
  "revisionId": "string",
  "revisionCreateTime": "2024-01-01T00:00:00Z",
  "state": "STATE_UNSPECIFIED",
  "etag": "string"
}'
```

### DELETE `/cloud/v2/universes/{universe_id}/data-stores/{data_store_id}/entries/{entry_id}` [STABLE]

Delete Data Store Entry

Marks the specified entry for deletion.

Entries are not be deleted immediately; instead, the `state` field will
be set to `DELETED`. Permanent deletion occurs after 30 days.

On success, returns 200 OK. If the entry doesn't exist, returns
404 Not Found.

**Auth:** API Key (`x-api-key` header)

**Scopes:** `universe-datastores.objects:delete`, `universe-datastores.objects:delete`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universe_id` | path | `string` | Yes | The universe ID. |
| `data_store_id` | path | `string` | Yes | The data-store ID. |
| `entry_id` | path | `string` | Yes | The entry ID. |

**Responses:**

- `200`: OK

**Rate Limits:** perApiKeyOwner: 1000000/minute
**Rate Limit Note:** Data stores requests are subject to additional throttling limits described in the [Open Cloud guide for data stores](https://create.roblox.com/docs/cloud/guides/data-stores/throttling).

**Example:**
```bash
curl -X DELETE -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/cloud/v2/universes/{UNIVERSE_ID}/data-stores/{DATA_STORE_ID}/entries/{ENTRY_ID}"
```

### POST `/cloud/v2/universes/{universe_id}/data-stores/{data_store_id}/entries/{entry_id}:increment` [STABLE]

Increment Data Store Entry

Increments the value of the specified entry. Both the existing value and
the increment amount must be integers.

If the entry doesn't exist, creates an entry with the specified value.

Incrementing specific revisions of the entry is **unsupported**. If you
specify a revision ID in the path, the increment request will create a new
entry with the `@<revisionId>` suffix as part of the key.

Known issue: the value may be incremented past the valid range of  values.
When this happens, the returned value will be clamped to the valid range,
but the backend may persist the original value. This behavior is maintained
for backwards compatibility reasons, but may change in a future version of
this API.

**Auth:** API Key (`x-api-key` header)

**Scopes:** `universe-datastores.objects:create`, `universe-datastores.objects:update`, `universe-datastores.objects:create`, `universe-datastores.objects:update`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universe_id` | path | `string` | Yes | The universe ID. |
| `data_store_id` | path | `string` | Yes | The data-store ID. |
| `entry_id` | path | `string` | Yes | The entry ID. |

**Request Body:** `application/json` — Type: `IncrementDataStoreEntryRequest`

See [IncrementDataStoreEntryRequest](#incrementdatastoreentryrequest) in Models.

**Request example:**
```json
{
  "amount": 0,
  "users": [
    "string"
  ],
  "attributes": "..."
}
```

**Responses:**

- `200`: OK → `DataStoreEntry`

**Response fields** (`DataStoreEntry`)

See [DataStoreEntry](#datastoreentry) in Models.

**Response example:**
```json
{
  "path": "string",
  "createTime": "2024-01-01T00:00:00Z",
  "revisionId": "string",
  "revisionCreateTime": "2024-01-01T00:00:00Z",
  "state": "STATE_UNSPECIFIED",
  "etag": "string"
}
```

**Rate Limits:** perApiKeyOwner: 1000000/minute
**Rate Limit Note:** Data stores requests are subject to additional throttling limits described in the [Open Cloud guide for data stores](https://create.roblox.com/docs/cloud/guides/data-stores/throttling).

**Example:**
```bash
curl -X POST -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/cloud/v2/universes/{UNIVERSE_ID}/data-stores/{DATA_STORE_ID}/entries/{ENTRY_ID}:increment" \
  -H "Content-Type: application/json" \
  -d '{
  "amount": 0,
  "users": [
    "string"
  ],
  "attributes": "..."
}'
```

### GET `/cloud/v2/universes/{universe_id}/data-stores/{data_store_id}/entries/{entry_id}:listRevisions` [STABLE]

List Data Store Entry Revisions

List revisions of the data store entry.

This method returns partial data store entries.

In particular, only the `path`, `id`, `createTime`, `revisionCreateTime`,
`revisionId`, `etag`, and `state` fields are populated. Both the `path` and
`id` fields will have an `@<version>` suffix.

In order to get the full entry at a revision, you can use the provided
`path` field with the `GetDataStoreEntry` method, i.e. `GET
/cloud/v2/universes/1234/data-stores/5678/entries/my-entry@<version>`.

**Auth:** API Key (`x-api-key` header)

**Scopes:** `universe-datastores.versions:list`, `universe-datastores.versions:list`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universe_id` | path | `string` | Yes | The universe ID. |
| `data_store_id` | path | `string` | Yes | The data-store ID. |
| `entry_id` | path | `string` | Yes | The entry ID. |
| `maxPageSize` | query | `integer` | No | The maximum number of revisions to return per page.  The service might return fewer than the maximum number of revisions. If unspecified, at most 10 revisions are returned. The maximum value is 100 values and higher values are set to 100. |
| `pageToken` | query | `string` | No | A page token, received from a previous call, to retrieve a subsequent page.  When paginating, all other parameters provided to the subsequent call must match the call that provided the page token. |
| `filter` | query | `string` | No | Supports the following subset of CEL:  * Only the `&&`, `<=`, and `>=` operators are supported. * Only the `revision_create_time` field is supported.  For example:    `"revision_create_time >= 2000-01-01T00:00:00Z && revision_create_time <=   2001-01-01T00:00:00Z"` |

**Responses:**

- `200`: OK → `ListDataStoreEntryRevisionsResponse`

**Response fields** (`ListDataStoreEntryRevisionsResponse`)

See [ListDataStoreEntryRevisionsResponse](#listdatastoreentryrevisionsresponse) in Models.

**Response example:**
```json
{
  "dataStoreEntries": [
    {
      "path": "...",
      "createTime": "...",
      "revisionId": "...",
      "revisionCreateTime": "...",
      "state": "...",
      "etag": "..."
    }
  ],
  "nextPageToken": "string"
}
```

**Rate Limits:** perApiKeyOwner: 1000000/minute
**Rate Limit Note:** Data stores requests are subject to additional throttling limits described in the [Open Cloud guide for data stores](https://create.roblox.com/docs/cloud/guides/data-stores/throttling).

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/cloud/v2/universes/{UNIVERSE_ID}/data-stores/{DATA_STORE_ID}/entries/{ENTRY_ID}:listRevisions"
```

### GET `/cloud/v2/universes/{universe_id}/data-stores/{data_store_id}/scopes/{scope_id}/entries` [STABLE]

List Data Store Entries

Returns a list of entries from a data store.

Only the `path` and `id` fields are populated; use `GetDataStoreEntry`
to retrieve other fields.

Specify the wildcard scope (`-`) to list entries from all scopes.

**Auth:** API Key (`x-api-key` header)

**Scopes:** `universe-datastores.objects:list`, `universe-datastores.objects:list`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universe_id` | path | `string` | Yes | The universe ID. |
| `data_store_id` | path | `string` | Yes | The data-store ID. |
| `scope_id` | path | `string` | Yes | The scope ID. |
| `maxPageSize` | query | `integer` | No | The maximum number of data store entries to return. The service might return fewer than this value. If unspecified, at most 10 data store entries are returned. The maximum value is 256 and higher values are set to 256. |
| `pageToken` | query | `string` | No | A page token, received from a previous call, to retrieve a subsequent page.  When paginating, all other parameters provided to the subsequent call must match the call that provided the page token. |
| `filter` | query | `string` | No | This field may be set in order to filter the resources returned.  The `filter` field supports a very small subset of CEL:  * Only the `id` field is supported. * Only the `startsWith` function is available; no other operators nor   built-ins are supported.  Example filter: `id.startsWith("foo")` |
| `showDeleted` | query | `boolean` | No | If true, resources marked for pending deletion will be included in the results. |

**Responses:**

- `200`: OK → `ListDataStoreEntriesResponse`

**Response fields** (`ListDataStoreEntriesResponse`)

See [ListDataStoreEntriesResponse](#listdatastoreentriesresponse) in Models.

**Response example:**
```json
{
  "dataStoreEntries": [
    {
      "path": "...",
      "createTime": "...",
      "revisionId": "...",
      "revisionCreateTime": "...",
      "state": "...",
      "etag": "..."
    }
  ],
  "nextPageToken": "string"
}
```

**Rate Limits:** perApiKeyOwner: 1000000/minute
**Rate Limit Note:** Data stores requests are subject to additional throttling limits described in the [Open Cloud guide for data stores](https://create.roblox.com/docs/cloud/guides/data-stores/throttling).

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/cloud/v2/universes/{UNIVERSE_ID}/data-stores/{DATA_STORE_ID}/scopes/{SCOPE_ID}/entries"
```

### POST `/cloud/v2/universes/{universe_id}/data-stores/{data_store_id}/scopes/{scope_id}/entries` [STABLE]

Create Data Store Entry

Creates an entry with the provided ID and value.

Returns a 400 Bad Request if the entry exists.

**Auth:** API Key (`x-api-key` header)

**Scopes:** `universe-datastores.objects:create`, `universe-datastores.objects:create`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universe_id` | path | `string` | Yes | The universe ID. |
| `data_store_id` | path | `string` | Yes | The data-store ID. |
| `scope_id` | path | `string` | Yes | The scope ID. |
| `id` | query | `string` | No | The ID to use for the data store entry, which will become the final component of the data store entry's resource path.  This value should be a 1-50 character string. We strongly recommend using only lowercase letters, numeric digits, and hyphens. |

**Request Body:** `application/json` — Type: `DataStoreEntry`

See [DataStoreEntry](#datastoreentry) in Models.

**Request example:**
```json
{
  "path": "string",
  "createTime": "2024-01-01T00:00:00Z",
  "revisionId": "string",
  "revisionCreateTime": "2024-01-01T00:00:00Z",
  "state": "STATE_UNSPECIFIED",
  "etag": "string"
}
```

**Responses:**

- `200`: OK → `DataStoreEntry`

**Response fields** (`DataStoreEntry`)

See [DataStoreEntry](#datastoreentry) in Models.

**Response example:**
```json
{
  "path": "string",
  "createTime": "2024-01-01T00:00:00Z",
  "revisionId": "string",
  "revisionCreateTime": "2024-01-01T00:00:00Z",
  "state": "STATE_UNSPECIFIED",
  "etag": "string"
}
```

**Rate Limits:** perApiKeyOwner: 1000000/minute
**Rate Limit Note:** Data stores requests are subject to additional throttling limits described in the [Open Cloud guide for data stores](https://create.roblox.com/docs/cloud/guides/data-stores/throttling).

**Example:**
```bash
curl -X POST -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/cloud/v2/universes/{UNIVERSE_ID}/data-stores/{DATA_STORE_ID}/scopes/{SCOPE_ID}/entries" \
  -H "Content-Type: application/json" \
  -d '{
  "path": "string",
  "createTime": "2024-01-01T00:00:00Z",
  "revisionId": "string",
  "revisionCreateTime": "2024-01-01T00:00:00Z",
  "state": "STATE_UNSPECIFIED",
  "etag": "string"
}'
```

### GET `/cloud/v2/universes/{universe_id}/data-stores/{data_store_id}/scopes/{scope_id}/entries/{entry_id}` [STABLE]

Get Data Store Entry

Gets the specified entry.

To get the entry at a specific revision, add `@<revisionId>` to the end of
the path.

For example, to get `my-entry` at the revision ID
`08DC3D3F43F9FCC1.0000000001.08DC3D3F43F9FCC1.01`, use the path
`/cloud/v2/universes/1234/data-stores/5678/entries/my-entry@08DC3D3F43F9FCC1.0000000001.08DC3D3F43F9FCC1.01`.

If your entry ID contains one or more `@` characters, and you want to get
the latest version rather than at any specific revision, append the special
revision ID `@latest` to the end of the path. Otherwise, the segment of the
entry ID after the last `@` will be interpreted as a revision ID.

For example, to get the latest revision of `my-entry`, use the path
`/cloud/v2/universes/1234/data-stores/5678/entries/my@entry@latest`.

To get the entry that was current at a specific time, add
`@latest:<timestamp>` to the end of the path, where `<timestamp>` is
RFC-3339 formatted. The given timestamp must be after
the Unix epoch (1/1/1970) and not more than ten minutes in the future.

For example, to get the revision of `my-entry` that was current on
12/2/2024 at 06:00 UTC, use the path
`/cloud/v2/universes/1234/data-stores/5678/entries/my-entry@latest:2024-12-02T06:00:00Z`.

**Auth:** API Key (`x-api-key` header)

**Scopes:** `universe-datastores.objects:read`, `universe-datastores.objects:read`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universe_id` | path | `string` | Yes | The universe ID. |
| `data_store_id` | path | `string` | Yes | The data-store ID. |
| `scope_id` | path | `string` | Yes | The scope ID. |
| `entry_id` | path | `string` | Yes | The entry ID. |

**Responses:**

- `200`: OK → `DataStoreEntry`

**Response fields** (`DataStoreEntry`)

See [DataStoreEntry](#datastoreentry) in Models.

**Response example:**
```json
{
  "path": "string",
  "createTime": "2024-01-01T00:00:00Z",
  "revisionId": "string",
  "revisionCreateTime": "2024-01-01T00:00:00Z",
  "state": "STATE_UNSPECIFIED",
  "etag": "string"
}
```

**Rate Limits:** perApiKeyOwner: 1000000/minute
**Rate Limit Note:** Data stores requests are subject to additional throttling limits described in the [Open Cloud guide for data stores](https://create.roblox.com/docs/cloud/guides/data-stores/throttling).

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/cloud/v2/universes/{UNIVERSE_ID}/data-stores/{DATA_STORE_ID}/scopes/{SCOPE_ID}/entries/{ENTRY_ID}"
```

### PATCH `/cloud/v2/universes/{universe_id}/data-stores/{data_store_id}/scopes/{scope_id}/entries/{entry_id}` [STABLE]

Update Data Store Entry

Updates the value, attributes, and users of an entry.

Updating specific revisions of the entry is **unsupported**. If you specify
a revision ID in the path and `allow_missing` is `true`, the update request
will instead create a new entry with the `@<revisionId>` suffix as part of
the key.

Partial update is **unsupported**. If attributes or users are not
provided when updating the value, they will be cleared. Value must always
be provided when updating an entry.

**Auth:** API Key (`x-api-key` header)

**Scopes:** `universe-datastores.objects:update`, `universe-datastores.objects:update`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universe_id` | path | `string` | Yes | The universe ID. |
| `data_store_id` | path | `string` | Yes | The data-store ID. |
| `scope_id` | path | `string` | Yes | The scope ID. |
| `entry_id` | path | `string` | Yes | The entry ID. |
| `allowMissing` | query | `boolean` | No | If set to true, and the data store entry is not found, a data store entry is created. |

**Request Body:** `application/json` — Type: `DataStoreEntry`

See [DataStoreEntry](#datastoreentry) in Models.

**Request example:**
```json
{
  "path": "string",
  "createTime": "2024-01-01T00:00:00Z",
  "revisionId": "string",
  "revisionCreateTime": "2024-01-01T00:00:00Z",
  "state": "STATE_UNSPECIFIED",
  "etag": "string"
}
```

**Responses:**

- `200`: OK → `DataStoreEntry`

**Response fields** (`DataStoreEntry`)

See [DataStoreEntry](#datastoreentry) in Models.

**Response example:**
```json
{
  "path": "string",
  "createTime": "2024-01-01T00:00:00Z",
  "revisionId": "string",
  "revisionCreateTime": "2024-01-01T00:00:00Z",
  "state": "STATE_UNSPECIFIED",
  "etag": "string"
}
```

**Rate Limits:** perApiKeyOwner: 1000000/minute
**Rate Limit Note:** Data stores requests are subject to additional throttling limits described in the [Open Cloud guide for data stores](https://create.roblox.com/docs/cloud/guides/data-stores/throttling).

**Example:**
```bash
curl -X PATCH -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/cloud/v2/universes/{UNIVERSE_ID}/data-stores/{DATA_STORE_ID}/scopes/{SCOPE_ID}/entries/{ENTRY_ID}" \
  -H "Content-Type: application/json" \
  -d '{
  "path": "string",
  "createTime": "2024-01-01T00:00:00Z",
  "revisionId": "string",
  "revisionCreateTime": "2024-01-01T00:00:00Z",
  "state": "STATE_UNSPECIFIED",
  "etag": "string"
}'
```

### DELETE `/cloud/v2/universes/{universe_id}/data-stores/{data_store_id}/scopes/{scope_id}/entries/{entry_id}` [STABLE]

Delete Data Store Entry

Marks the specified entry for deletion.

Entries are not be deleted immediately; instead, the `state` field will
be set to `DELETED`. Permanent deletion occurs after 30 days.

On success, returns 200 OK. If the entry doesn't exist, returns
404 Not Found.

**Auth:** API Key (`x-api-key` header)

**Scopes:** `universe-datastores.objects:delete`, `universe-datastores.objects:delete`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universe_id` | path | `string` | Yes | The universe ID. |
| `data_store_id` | path | `string` | Yes | The data-store ID. |
| `scope_id` | path | `string` | Yes | The scope ID. |
| `entry_id` | path | `string` | Yes | The entry ID. |

**Responses:**

- `200`: OK

**Rate Limits:** perApiKeyOwner: 1000000/minute
**Rate Limit Note:** Data stores requests are subject to additional throttling limits described in the [Open Cloud guide for data stores](https://create.roblox.com/docs/cloud/guides/data-stores/throttling).

**Example:**
```bash
curl -X DELETE -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/cloud/v2/universes/{UNIVERSE_ID}/data-stores/{DATA_STORE_ID}/scopes/{SCOPE_ID}/entries/{ENTRY_ID}"
```

### POST `/cloud/v2/universes/{universe_id}/data-stores/{data_store_id}/scopes/{scope_id}/entries/{entry_id}:increment` [STABLE]

Increment Data Store Entry

Increments the value of the specified entry. Both the existing value and
the increment amount must be integers.

If the entry doesn't exist, creates an entry with the specified value.

Incrementing specific revisions of the entry is **unsupported**. If you
specify a revision ID in the path, the increment request will create a new
entry with the `@<revisionId>` suffix as part of the key.

Known issue: the value may be incremented past the valid range of  values.
When this happens, the returned value will be clamped to the valid range,
but the backend may persist the original value. This behavior is maintained
for backwards compatibility reasons, but may change in a future version of
this API.

**Auth:** API Key (`x-api-key` header)

**Scopes:** `universe-datastores.objects:create`, `universe-datastores.objects:update`, `universe-datastores.objects:create`, `universe-datastores.objects:update`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universe_id` | path | `string` | Yes | The universe ID. |
| `data_store_id` | path | `string` | Yes | The data-store ID. |
| `scope_id` | path | `string` | Yes | The scope ID. |
| `entry_id` | path | `string` | Yes | The entry ID. |

**Request Body:** `application/json` — Type: `IncrementDataStoreEntryRequest`

See [IncrementDataStoreEntryRequest](#incrementdatastoreentryrequest) in Models.

**Request example:**
```json
{
  "amount": 0,
  "users": [
    "string"
  ],
  "attributes": "..."
}
```

**Responses:**

- `200`: OK → `DataStoreEntry`

**Response fields** (`DataStoreEntry`)

See [DataStoreEntry](#datastoreentry) in Models.

**Response example:**
```json
{
  "path": "string",
  "createTime": "2024-01-01T00:00:00Z",
  "revisionId": "string",
  "revisionCreateTime": "2024-01-01T00:00:00Z",
  "state": "STATE_UNSPECIFIED",
  "etag": "string"
}
```

**Rate Limits:** perApiKeyOwner: 1000000/minute
**Rate Limit Note:** Data stores requests are subject to additional throttling limits described in the [Open Cloud guide for data stores](https://create.roblox.com/docs/cloud/guides/data-stores/throttling).

**Example:**
```bash
curl -X POST -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/cloud/v2/universes/{UNIVERSE_ID}/data-stores/{DATA_STORE_ID}/scopes/{SCOPE_ID}/entries/{ENTRY_ID}:increment" \
  -H "Content-Type: application/json" \
  -d '{
  "amount": 0,
  "users": [
    "string"
  ],
  "attributes": "..."
}'
```

### GET `/cloud/v2/universes/{universe_id}/data-stores/{data_store_id}/scopes/{scope_id}/entries/{entry_id}:listRevisions` [STABLE]

List Data Store Entry Revisions

List revisions of the data store entry.

This method returns partial data store entries.

In particular, only the `path`, `id`, `createTime`, `revisionCreateTime`,
`revisionId`, `etag`, and `state` fields are populated. Both the `path` and
`id` fields will have an `@<version>` suffix.

In order to get the full entry at a revision, you can use the provided
`path` field with the `GetDataStoreEntry` method, i.e. `GET
/cloud/v2/universes/1234/data-stores/5678/entries/my-entry@<version>`.

**Auth:** API Key (`x-api-key` header)

**Scopes:** `universe-datastores.versions:list`, `universe-datastores.versions:list`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universe_id` | path | `string` | Yes | The universe ID. |
| `data_store_id` | path | `string` | Yes | The data-store ID. |
| `scope_id` | path | `string` | Yes | The scope ID. |
| `entry_id` | path | `string` | Yes | The entry ID. |
| `maxPageSize` | query | `integer` | No | The maximum number of revisions to return per page.  The service might return fewer than the maximum number of revisions. If unspecified, at most 10 revisions are returned. The maximum value is 100 values and higher values are set to 100. |
| `pageToken` | query | `string` | No | A page token, received from a previous call, to retrieve a subsequent page.  When paginating, all other parameters provided to the subsequent call must match the call that provided the page token. |
| `filter` | query | `string` | No | Supports the following subset of CEL:  * Only the `&&`, `<=`, and `>=` operators are supported. * Only the `revision_create_time` field is supported.  For example:    `"revision_create_time >= 2000-01-01T00:00:00Z && revision_create_time <=   2001-01-01T00:00:00Z"` |

**Responses:**

- `200`: OK → `ListDataStoreEntryRevisionsResponse`

**Response fields** (`ListDataStoreEntryRevisionsResponse`)

See [ListDataStoreEntryRevisionsResponse](#listdatastoreentryrevisionsresponse) in Models.

**Response example:**
```json
{
  "dataStoreEntries": [
    {
      "path": "...",
      "createTime": "...",
      "revisionId": "...",
      "revisionCreateTime": "...",
      "state": "...",
      "etag": "..."
    }
  ],
  "nextPageToken": "string"
}
```

**Rate Limits:** perApiKeyOwner: 1000000/minute
**Rate Limit Note:** Data stores requests are subject to additional throttling limits described in the [Open Cloud guide for data stores](https://create.roblox.com/docs/cloud/guides/data-stores/throttling).

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/cloud/v2/universes/{UNIVERSE_ID}/data-stores/{DATA_STORE_ID}/scopes/{SCOPE_ID}/entries/{ENTRY_ID}:listRevisions"
```

### POST `/cloud/v2/universes/{universe_id}/data-stores/{data_store_id}:undelete` [BETA]

Undelete Data Store

Restore the data store

**Auth:** API Key (`x-api-key` header)

**Scopes:** `universe-datastores.control:delete`, `universe-datastores.control:delete`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universe_id` | path | `string` | Yes | The universe ID. |
| `data_store_id` | path | `string` | Yes | The data-store ID. |

**Request Body:** `application/json` — Type: `UndeleteDataStoreRequest`

See [UndeleteDataStoreRequest](#undeletedatastorerequest) in Models.

**Request example:**
```json
{}
```

**Responses:**

- `200`: OK → `DataStore`

**Response fields** (`DataStore`)

See [DataStore](#datastore) in Models.

**Response example:**
```json
{
  "path": "string",
  "createTime": "2024-01-01T00:00:00Z",
  "expireTime": "2024-01-01T00:00:00Z",
  "state": "STATE_UNSPECIFIED",
  "id": "string"
}
```

**Rate Limits:** perApiKeyOwner: 1000000/minute
**Rate Limit Note:** Data stores requests are subject to additional throttling limits described in the [Open Cloud guide for data stores](https://create.roblox.com/docs/cloud/guides/data-stores/throttling).

**Example:**
```bash
curl -X POST -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/cloud/v2/universes/{UNIVERSE_ID}/data-stores/{DATA_STORE_ID}:undelete" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### POST `/cloud/v2/universes/{universe_id}/data-stores:snapshot` [STABLE]

Snapshot Data Stores

Takes a new snapshot of the data stores in an experience.

After a snapshot, the next write to every key in the experience will
create a versioned backup of the previous data, regardless of the time of
the last write.

In effect, all data current at the time of the snapshot is guaranteed to be
available as a versioned backup for at least 30 days.

Snapshots can be taken once per UTC day, per experience. If the latest
snapshot was taken within the same UTC day, this operation is a no-op and
the time of the latest snapshot will be returned.

For more information on using snapshots, see the [Data
stores](https://create.roblox.com/docs/cloud-services/data-stores#snapshots)
Engine guide.

**Auth:** API Key (`x-api-key` header)

**Scopes:** `universe-datastores.control:snapshot`, `universe-datastores.control:snapshot`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universe_id` | path | `string` | Yes | The universe ID. |

**Request Body:** `application/json` — Type: `SnapshotDataStoresRequest`

See [SnapshotDataStoresRequest](#snapshotdatastoresrequest) in Models.

**Request example:**
```json
{}
```

**Responses:**

- `200`: OK → `SnapshotDataStoresResponse`

**Response fields** (`SnapshotDataStoresResponse`)

See [SnapshotDataStoresResponse](#snapshotdatastoresresponse) in Models.

**Response example:**
```json
{
  "newSnapshotTaken": false,
  "latestSnapshotTime": "2024-01-01T00:00:00Z"
}
```

**Rate Limits:** perApiKeyOwner: 60/minute
**Rate Limit Note:** Data stores requests are subject to additional throttling limits described in the [Open Cloud guide for data stores](https://create.roblox.com/docs/cloud/guides/data-stores/throttling).

**Example:**
```bash
curl -X POST -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/cloud/v2/universes/{UNIVERSE_ID}/data-stores:snapshot" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### GET `/cloud/v2/universes/{universe_id}/memory-store/operations/{operation_id}` [BETA]

Get Memory Store Flush Operation

Retrieves the status of the operation to [flush the memory stores of a universe](https://create.roblox.com/docs/cloud/reference/features/storage#Cloud_FlushMemoryStore).

**Auth:** API Key (`x-api-key` header)

**Scopes:** `memory-store:get`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universe_id` | path | `string` | Yes | The universe ID. |
| `operation_id` | path | `string` | Yes | The operation ID. |
| `scope` | query | `LIVE \| TEST` | No | The scope of the memory store flush operation.  Possible values:    \| Value \| Description \|   \| --- \| --- \|   \| LIVE \|  Flush the live memory store scope. This is the default. \|   \| TEST \| Flush the test memory store scope. \| Valid values: `LIVE`, `TEST` |

**Responses:**

- `200`: OK → `OCV2.Operations.Operation`

**Response fields** (`OCV2.Operations.Operation`)

See [OCV2.Operations.Operation](#ocv2-operations-operation) in Models.

**Response example:**
```json
{
  "path": "string",
  "metadata": {
    "@type": "string"
  },
  "done": false,
  "error": {
    "code": 0,
    "message": "string",
    "details": [
      "..."
    ]
  },
  "response": {
    "@type": "string"
  }
}
```

**Rate Limits:** perApiKeyOwner: 1000000/minute

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/cloud/v2/universes/{UNIVERSE_ID}/memory-store/operations/{OPERATION_ID}"
```

### POST `/cloud/v2/universes/{universe_id}/memory-store/queues/{queue_id}/items` [STABLE]

Create Memory Store Queue Item

Creates a new queue item.

If `ttl` is set, the item will automatically be removed from the queue
after the time interval specified.

If a numerical `priority` is set, the item will be inserted into the queue
based on the priority value. The higher the value, the closer to the front
of the queue the item will be. If priority values are the same then the
item will be inserted after existing values with the same priority.

**Auth:** API Key (`x-api-key` header)

**Scopes:** `memory-store.queue:add`, `memory-store.queue:add`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universe_id` | path | `string` | Yes | The universe ID. |
| `queue_id` | path | `string` | Yes | The queue ID. |

**Request Body:** `application/json` — Type: `MemoryStoreQueueItem`

See [MemoryStoreQueueItem](#memorystorequeueitem) in Models.

**Request example:**
```json
{
  "path": "string",
  "data": "...",
  "priority": 0,
  "ttl": "string",
  "expireTime": "2024-01-01T00:00:00Z",
  "id": "string"
}
```

**Responses:**

- `200`: OK → `MemoryStoreQueueItem`

**Response fields** (`MemoryStoreQueueItem`)

See [MemoryStoreQueueItem](#memorystorequeueitem) in Models.

**Response example:**
```json
{
  "path": "string",
  "data": "...",
  "priority": 0,
  "ttl": "string",
  "expireTime": "2024-01-01T00:00:00Z",
  "id": "string"
}
```

**Rate Limits:** perApiKeyOwner: 1000000/minute

**Example:**
```bash
curl -X POST -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/cloud/v2/universes/{UNIVERSE_ID}/memory-store/queues/{QUEUE_ID}/items" \
  -H "Content-Type: application/json" \
  -d '{
  "path": "string",
  "data": "...",
  "priority": 0,
  "ttl": "string",
  "expireTime": "2024-01-01T00:00:00Z",
  "id": "string"
}'
```

### POST `/cloud/v2/universes/{universe_id}/memory-store/queues/{queue_id}/items:discard` [STABLE]

Discard Memory Store Queue Items

Discards read items from the front of the queue.

Takes a `readId` from a previous `Read` operation.

**Auth:** API Key (`x-api-key` header)

**Scopes:** `memory-store.queue:discard`, `memory-store.queue:discard`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universe_id` | path | `string` | Yes | The universe ID. |
| `queue_id` | path | `string` | Yes | The queue ID. |

**Request Body:** `application/json` — Type: `DiscardMemoryStoreQueueItemsRequest`

See [DiscardMemoryStoreQueueItemsRequest](#discardmemorystorequeueitemsrequest) in Models.

**Request example:**
```json
{
  "readId": "string"
}
```

**Responses:**

- `200`: OK

**Rate Limits:** perApiKeyOwner: 1000000/minute

**Example:**
```bash
curl -X POST -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/cloud/v2/universes/{UNIVERSE_ID}/memory-store/queues/{QUEUE_ID}/items:discard" \
  -H "Content-Type: application/json" \
  -d '{
  "readId": "string"
}'
```

### GET `/cloud/v2/universes/{universe_id}/memory-store/queues/{queue_id}/items:read` [STABLE]

Read Memory Store Queue Items

Returns the specified number of items at the front of the queue.

**Auth:** API Key (`x-api-key` header)

**Scopes:** `memory-store.queue:dequeue`, `memory-store.queue:dequeue`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universe_id` | path | `string` | Yes | The universe ID. |
| `queue_id` | path | `string` | Yes | The queue ID. |
| `count` | query | `integer` | No | The number of items to read from the queue If unspecified, 1 item will be returned. The maximum value is 200; values above 200 will be coerced to 200. |
| `allOrNothing` | query | `boolean` | No | If `all_or_nothing` is true and the requested number of objects is not available, will return a 404 Error.  Otherwise, will return the path and read_id of the read operation and a list of the MemoryStoreQueue items. |
| `invisibilityWindow` | query | `string` | No | Invisibility window for items read, in seconds.  Items read are invisible in subsequent reads during the invisibility window duration.  It must be written in seconds greater than 0 and end with `s`.  Defaults to `30s`. |

**Responses:**

- `200`: OK → `ReadMemoryStoreQueueItemsResponse`

**Response fields** (`ReadMemoryStoreQueueItemsResponse`)

See [ReadMemoryStoreQueueItemsResponse](#readmemorystorequeueitemsresponse) in Models.

**Response example:**
```json
{
  "readId": "string",
  "items": [
    {
      "path": "...",
      "data": "...",
      "priority": "...",
      "ttl": "...",
      "expireTime": "...",
      "id": "..."
    }
  ]
}
```

**Rate Limits:** perApiKeyOwner: 1000000/minute

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/cloud/v2/universes/{UNIVERSE_ID}/memory-store/queues/{QUEUE_ID}/items:read"
```

### GET `/cloud/v2/universes/{universe_id}/memory-store/sorted-maps/{sorted_map_id}/items` [STABLE]

List Memory Store Sorted Map Items

Gets and returns items in the map with a given order and filter.

**Auth:** API Key (`x-api-key` header)

**Scopes:** `memory-store.sorted-map:read`, `memory-store.sorted-map:read`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universe_id` | path | `string` | Yes | The universe ID. |
| `sorted_map_id` | path | `string` | Yes | The sorted-map ID. |
| `maxPageSize` | query | `integer` | No | The maximum number of memory store sorted map items to return. The service might return fewer than this value. If unspecified, at most 1 memory store sorted map items are returned. The maximum value is 100 and higher values are set to 100. |
| `pageToken` | query | `string` | No | A page token, received from a previous call, to retrieve a subsequent page.  When paginating, all other parameters provided to the subsequent call must match the call that provided the page token. |
| `orderBy` | query | `string` | No | If specified, results are ordered according to the specified fields.  Values must be a comma-separated list of fields, with an optional, per-field " desc" suffix to sort by descending rather than ascending values. You can access subfields with a `.` operator.  Results may be ordered by the following fields: id.  Example: "id desc" |
| `filter` | query | `string` | No | This field may be set in order to filter the resources returned.  Filtering conforms to Common Expression Language (CEL). Only the `id` and `sortKey` fields are supported. In terms of operators, only `<`, `>` and `&&` are allowed'  Example: `id > "key-001" && id < "key-100"` |

**Responses:**

- `200`: OK → `ListMemoryStoreSortedMapItemsResponse`

**Response fields** (`ListMemoryStoreSortedMapItemsResponse`)

See [ListMemoryStoreSortedMapItemsResponse](#listmemorystoresortedmapitemsresponse) in Models.

**Response example:**
```json
{
  "items": [
    {
      "path": "...",
      "value": "...",
      "etag": "...",
      "ttl": "...",
      "expireTime": "...",
      "id": "..."
    }
  ],
  "nextPageToken": "string"
}
```

**Rate Limits:** perApiKeyOwner: 1000000/minute

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/cloud/v2/universes/{UNIVERSE_ID}/memory-store/sorted-maps/{SORTED_MAP_ID}/items"
```

### POST `/cloud/v2/universes/{universe_id}/memory-store/sorted-maps/{sorted_map_id}/items` [STABLE]

Create Memory Store Sorted Map Item

Creates the specified map item if it doesn't exist.

**Auth:** API Key (`x-api-key` header)

**Scopes:** `memory-store.sorted-map:write`, `memory-store.sorted-map:write`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universe_id` | path | `string` | Yes | The universe ID. |
| `sorted_map_id` | path | `string` | Yes | The sorted-map ID. |
| `id` | query | `string` | No | The ID to use for the memory store sorted map item, which will become the final component of the memory store sorted map item's resource path.  This value should be a 1-127 character string that supports alphanumeric and special characters. This id is case sensitive. The id must be url encoded if it contains any url breaking special characters. |

**Request Body:** `application/json` — Type: `MemoryStoreSortedMapItem`

See [MemoryStoreSortedMapItem](#memorystoresortedmapitem) in Models.

**Request example:**
```json
{
  "path": "string",
  "value": "...",
  "etag": "string",
  "ttl": "string",
  "expireTime": "2024-01-01T00:00:00Z",
  "id": "string"
}
```

**Responses:**

- `200`: OK → `MemoryStoreSortedMapItem`

**Response fields** (`MemoryStoreSortedMapItem`)

See [MemoryStoreSortedMapItem](#memorystoresortedmapitem) in Models.

**Response example:**
```json
{
  "path": "string",
  "value": "...",
  "etag": "string",
  "ttl": "string",
  "expireTime": "2024-01-01T00:00:00Z",
  "id": "string"
}
```

**Rate Limits:** perApiKeyOwner: 1000000/minute

**Example:**
```bash
curl -X POST -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/cloud/v2/universes/{UNIVERSE_ID}/memory-store/sorted-maps/{SORTED_MAP_ID}/items" \
  -H "Content-Type: application/json" \
  -d '{
  "path": "string",
  "value": "...",
  "etag": "string",
  "ttl": "string",
  "expireTime": "2024-01-01T00:00:00Z",
  "id": "string"
}'
```

### GET `/cloud/v2/universes/{universe_id}/memory-store/sorted-maps/{sorted_map_id}/items/{item_id}` [STABLE]

Get Memory Store Sorted Map Item

Gets and returns the value of the given key in the map.

**Auth:** API Key (`x-api-key` header)

**Scopes:** `memory-store.sorted-map:read`, `memory-store.sorted-map:read`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universe_id` | path | `string` | Yes | The universe ID. |
| `sorted_map_id` | path | `string` | Yes | The sorted-map ID. |
| `item_id` | path | `string` | Yes | The item ID. |

**Responses:**

- `200`: OK → `MemoryStoreSortedMapItem`

**Response fields** (`MemoryStoreSortedMapItem`)

See [MemoryStoreSortedMapItem](#memorystoresortedmapitem) in Models.

**Response example:**
```json
{
  "path": "string",
  "value": "...",
  "etag": "string",
  "ttl": "string",
  "expireTime": "2024-01-01T00:00:00Z",
  "id": "string"
}
```

**Rate Limits:** perApiKeyOwner: 1000000/minute

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/cloud/v2/universes/{UNIVERSE_ID}/memory-store/sorted-maps/{SORTED_MAP_ID}/items/{ITEM_ID}"
```

### PATCH `/cloud/v2/universes/{universe_id}/memory-store/sorted-maps/{sorted_map_id}/items/{item_id}` [STABLE]

Update Memory Store Sorted Map Item

Updates the specified map item.

**Auth:** API Key (`x-api-key` header)

**Scopes:** `memory-store.sorted-map:write`, `memory-store.sorted-map:write`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universe_id` | path | `string` | Yes | The universe ID. |
| `sorted_map_id` | path | `string` | Yes | The sorted-map ID. |
| `item_id` | path | `string` | Yes | The item ID. |
| `allowMissing` | query | `boolean` | No | If set to true, and the memory store sorted map item is not found, a memory store sorted map item is created. |

**Request Body:** `application/json` — Type: `MemoryStoreSortedMapItem`

See [MemoryStoreSortedMapItem](#memorystoresortedmapitem) in Models.

**Request example:**
```json
{
  "path": "string",
  "value": "...",
  "etag": "string",
  "ttl": "string",
  "expireTime": "2024-01-01T00:00:00Z",
  "id": "string"
}
```

**Responses:**

- `200`: OK → `MemoryStoreSortedMapItem`

**Response fields** (`MemoryStoreSortedMapItem`)

See [MemoryStoreSortedMapItem](#memorystoresortedmapitem) in Models.

**Response example:**
```json
{
  "path": "string",
  "value": "...",
  "etag": "string",
  "ttl": "string",
  "expireTime": "2024-01-01T00:00:00Z",
  "id": "string"
}
```

**Rate Limits:** perApiKeyOwner: 1000000/minute

**Example:**
```bash
curl -X PATCH -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/cloud/v2/universes/{UNIVERSE_ID}/memory-store/sorted-maps/{SORTED_MAP_ID}/items/{ITEM_ID}" \
  -H "Content-Type: application/json" \
  -d '{
  "path": "string",
  "value": "...",
  "etag": "string",
  "ttl": "string",
  "expireTime": "2024-01-01T00:00:00Z",
  "id": "string"
}'
```

### DELETE `/cloud/v2/universes/{universe_id}/memory-store/sorted-maps/{sorted_map_id}/items/{item_id}` [STABLE]

Delete Memory Store Sorted Map Item

Deletes the specified item from the map.

**Auth:** API Key (`x-api-key` header)

**Scopes:** `memory-store.sorted-map:write`, `memory-store.sorted-map:write`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universe_id` | path | `string` | Yes | The universe ID. |
| `sorted_map_id` | path | `string` | Yes | The sorted-map ID. |
| `item_id` | path | `string` | Yes | The item ID. |

**Responses:**

- `200`: OK

**Rate Limits:** perApiKeyOwner: 1000000/minute

**Example:**
```bash
curl -X DELETE -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/cloud/v2/universes/{UNIVERSE_ID}/memory-store/sorted-maps/{SORTED_MAP_ID}/items/{ITEM_ID}"
```

### POST `/cloud/v2/universes/{universe_id}/memory-store:flush` [STABLE]

Flush Memory Store

Asynchronously flush all data structures in the universe.

Unlike some other endpoints, the flush response `path` already
includes the `cloud/v2` prefix. Poll the operation at
`https://apis.roblox.com/{path}` without adding another prefix.

**Auth:** API Key (`x-api-key` header)

**Scopes:** `memory-store:flush`, `memory-store:flush`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universe_id` | path | `string` | Yes | The universe ID. |
| `scope` | query | `LIVE \| TEST` | No | The scope of the memory store to flush.  Possible values:    \| Value \| Description \|   \| --- \| --- \|   \| LIVE \|  Flush the live memory store scope. This is the default. \|   \| TEST \| Flush the test memory store scope. \| Valid values: `LIVE`, `TEST` |

**Responses:**

- `200`: OK → `Operation`

**Response fields** (`Operation`)

See [Operation](#operation) in Models.

**Response example:**
```json
{
  "path": "string",
  "metadata": {
    "@type": "string"
  },
  "done": false,
  "error": {
    "code": 0,
    "message": "string",
    "details": [
      "..."
    ]
  },
  "response": {
    "@type": "string"
  }
}
```

**Rate Limits:** perApiKeyOwner: 1000000/minute

**Example:**
```bash
curl -X POST -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/cloud/v2/universes/{UNIVERSE_ID}/memory-store:flush"
```

### GET `/cloud/v2/universes/{universe_id}/ordered-data-stores/{ordered_data_store_id}/scopes/{scope_id}/entries` [STABLE]

List Ordered Data Store Entries

Returns a list of entries from an ordered data store.

**Auth:** API Key (`x-api-key` header)

**Scopes:** `universe.ordered-data-store.scope.entry:read`, `universe.ordered-data-store.scope.entry:read`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universe_id` | path | `string` | Yes | The universe ID. |
| `ordered_data_store_id` | path | `string` | Yes | The ordered-data-store ID. |
| `scope_id` | path | `string` | Yes | The scope ID. |
| `maxPageSize` | query | `integer` | No | The maximum number of ordered data store entries to return. The service might return fewer than this value. If unspecified, at most 10 ordered data store entries are returned. The maximum value is 100 and higher values are set to 100. |
| `pageToken` | query | `string` | No | A page token, received from a previous call, to retrieve a subsequent page.  When paginating, all other parameters provided to the subsequent call must match the call that provided the page token. |
| `orderBy` | query | `string` | No | If specified, results are ordered according to the specified fields.  Values must be a comma-separated list of fields, with an optional, per-field " desc" suffix to sort by descending rather than ascending values. You can access subfields with a `.` operator.  Results may be ordered by the following fields: value.  Example: "value desc" |
| `filter` | query | `string` | No | This field may be set in order to filter the resources returned.  We support two comparison operators for this operation: `<=` and `>=`.These comparison operators act as a minValue and maxValue for the values returned. If filtering is needed for a value between a minValue and maxValue the user can use the logical operator `&&`. All tokens in the filter expression must be separated by a single space.  Example filters: `entry <= 10`; `entry >= 10 && entry <= 30` |

**Responses:**

- `200`: OK → `ListOrderedDataStoreEntriesResponse`

**Response fields** (`ListOrderedDataStoreEntriesResponse`)

See [ListOrderedDataStoreEntriesResponse](#listordereddatastoreentriesresponse) in Models.

**Response example:**
```json
{
  "orderedDataStoreEntries": [
    {
      "path": "...",
      "value": "...",
      "id": "..."
    }
  ],
  "nextPageToken": "string"
}
```

**Rate Limits:** perApiKeyOwner: 1000000/minute
**Rate Limit Note:** Ordered data stores requests are subject to additional throttling limits described in the [Open Cloud guide for data stores](https://create.roblox.com/docs/cloud/guides/data-stores/throttling).

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/cloud/v2/universes/{UNIVERSE_ID}/ordered-data-stores/{ORDERED_DATA_STORE_ID}/scopes/{SCOPE_ID}/entries"
```

### POST `/cloud/v2/universes/{universe_id}/ordered-data-stores/{ordered_data_store_id}/scopes/{scope_id}/entries` [STABLE]

Create Ordered Data Store Entry

Creates an entry with the provided ID and value.

Returns a 400 Bad Request if the entry exists.

**Auth:** API Key (`x-api-key` header)

**Scopes:** `universe.ordered-data-store.scope.entry:write`, `universe.ordered-data-store.scope.entry:write`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universe_id` | path | `string` | Yes | The universe ID. |
| `ordered_data_store_id` | path | `string` | Yes | The ordered-data-store ID. |
| `scope_id` | path | `string` | Yes | The scope ID. |
| `id` | query | `string` | No | The ID to use for the ordered data store entry, which will become the final component of the ordered data store entry's resource path.  This value should be A 1-63 character string. We strongly recommend using only lowercase letters, numeric digits, and hyphens. |

**Request Body:** `application/json` — Type: `OrderedDataStoreEntry`

See [OrderedDataStoreEntry](#ordereddatastoreentry) in Models.

**Request example:**
```json
{
  "path": "string",
  "value": 0,
  "id": "string"
}
```

**Responses:**

- `200`: OK → `OrderedDataStoreEntry`

**Response fields** (`OrderedDataStoreEntry`)

See [OrderedDataStoreEntry](#ordereddatastoreentry) in Models.

**Response example:**
```json
{
  "path": "string",
  "value": 0,
  "id": "string"
}
```

**Rate Limits:** perApiKeyOwner: 1000000/minute
**Rate Limit Note:** Ordered data stores requests are subject to additional throttling limits described in the [Open Cloud guide for data stores](https://create.roblox.com/docs/cloud/guides/data-stores/throttling).

**Example:**
```bash
curl -X POST -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/cloud/v2/universes/{UNIVERSE_ID}/ordered-data-stores/{ORDERED_DATA_STORE_ID}/scopes/{SCOPE_ID}/entries" \
  -H "Content-Type: application/json" \
  -d '{
  "path": "string",
  "value": 0,
  "id": "string"
}'
```

### GET `/cloud/v2/universes/{universe_id}/ordered-data-stores/{ordered_data_store_id}/scopes/{scope_id}/entries/{entry_id}` [STABLE]

Get Ordered Data Store Entry

Gets the specified entry.

**Auth:** API Key (`x-api-key` header)

**Scopes:** `universe.ordered-data-store.scope.entry:read`, `universe.ordered-data-store.scope.entry:read`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universe_id` | path | `string` | Yes | The universe ID. |
| `ordered_data_store_id` | path | `string` | Yes | The ordered-data-store ID. |
| `scope_id` | path | `string` | Yes | The scope ID. |
| `entry_id` | path | `string` | Yes | The entry ID. |

**Responses:**

- `200`: OK → `OrderedDataStoreEntry`

**Response fields** (`OrderedDataStoreEntry`)

See [OrderedDataStoreEntry](#ordereddatastoreentry) in Models.

**Response example:**
```json
{
  "path": "string",
  "value": 0,
  "id": "string"
}
```

**Rate Limits:** perApiKeyOwner: 1000000/minute
**Rate Limit Note:** Ordered data stores requests are subject to additional throttling limits described in the [Open Cloud guide for data stores](https://create.roblox.com/docs/cloud/guides/data-stores/throttling).

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/cloud/v2/universes/{UNIVERSE_ID}/ordered-data-stores/{ORDERED_DATA_STORE_ID}/scopes/{SCOPE_ID}/entries/{ENTRY_ID}"
```

### PATCH `/cloud/v2/universes/{universe_id}/ordered-data-stores/{ordered_data_store_id}/scopes/{scope_id}/entries/{entry_id}` [STABLE]

Update Ordered Data Store Entry

Updates the value of an entry.

**Auth:** API Key (`x-api-key` header)

**Scopes:** `universe.ordered-data-store.scope.entry:write`, `universe.ordered-data-store.scope.entry:write`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universe_id` | path | `string` | Yes | The universe ID. |
| `ordered_data_store_id` | path | `string` | Yes | The ordered-data-store ID. |
| `scope_id` | path | `string` | Yes | The scope ID. |
| `entry_id` | path | `string` | Yes | The entry ID. |
| `allowMissing` | query | `boolean` | No | If set to true, and the ordered data store entry is not found, a ordered data store entry is created. |

**Request Body:** `application/json` — Type: `OrderedDataStoreEntry`

See [OrderedDataStoreEntry](#ordereddatastoreentry) in Models.

**Request example:**
```json
{
  "path": "string",
  "value": 0,
  "id": "string"
}
```

**Responses:**

- `200`: OK → `OrderedDataStoreEntry`

**Response fields** (`OrderedDataStoreEntry`)

See [OrderedDataStoreEntry](#ordereddatastoreentry) in Models.

**Response example:**
```json
{
  "path": "string",
  "value": 0,
  "id": "string"
}
```

**Rate Limits:** perApiKeyOwner: 1000000/minute
**Rate Limit Note:** Ordered data stores requests are subject to additional throttling limits described in the [Open Cloud guide for data stores](https://create.roblox.com/docs/cloud/guides/data-stores/throttling).

**Example:**
```bash
curl -X PATCH -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/cloud/v2/universes/{UNIVERSE_ID}/ordered-data-stores/{ORDERED_DATA_STORE_ID}/scopes/{SCOPE_ID}/entries/{ENTRY_ID}" \
  -H "Content-Type: application/json" \
  -d '{
  "path": "string",
  "value": 0,
  "id": "string"
}'
```

### DELETE `/cloud/v2/universes/{universe_id}/ordered-data-stores/{ordered_data_store_id}/scopes/{scope_id}/entries/{entry_id}` [STABLE]

Delete Ordered Data Store Entry

Deletes the specified entry.

On success, returns 200 OK. If the entry doesn't exist, returns
404 Not Found.

**Auth:** API Key (`x-api-key` header)

**Scopes:** `universe.ordered-data-store.scope.entry:write`, `universe.ordered-data-store.scope.entry:write`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universe_id` | path | `string` | Yes | The universe ID. |
| `ordered_data_store_id` | path | `string` | Yes | The ordered-data-store ID. |
| `scope_id` | path | `string` | Yes | The scope ID. |
| `entry_id` | path | `string` | Yes | The entry ID. |

**Responses:**

- `200`: OK

**Rate Limits:** perApiKeyOwner: 1000000/minute
**Rate Limit Note:** Ordered data stores requests are subject to additional throttling limits described in the [Open Cloud guide for data stores](https://create.roblox.com/docs/cloud/guides/data-stores/throttling).

**Example:**
```bash
curl -X DELETE -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/cloud/v2/universes/{UNIVERSE_ID}/ordered-data-stores/{ORDERED_DATA_STORE_ID}/scopes/{SCOPE_ID}/entries/{ENTRY_ID}"
```

### POST `/cloud/v2/universes/{universe_id}/ordered-data-stores/{ordered_data_store_id}/scopes/{scope_id}/entries/{entry_id}:increment` [STABLE]

Increment Ordered Data Store Entry

Increments the value of the specified entry. Both the existing value and
the increment amount must be integers.

If the entry doesn't exist, creates an entry with the specified value.

Known issue: the value may be incremented past the valid range of  values.
When this happens, the returned value will be clamped to the valid range,
but the backend may persist the original value. This behavior is maintained
for backwards compatibility reasons, but may change in a future version of
this API.

**Auth:** API Key (`x-api-key` header)

**Scopes:** `universe.ordered-data-store.scope.entry:write`, `universe.ordered-data-store.scope.entry:write`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universe_id` | path | `string` | Yes | The universe ID. |
| `ordered_data_store_id` | path | `string` | Yes | The ordered-data-store ID. |
| `scope_id` | path | `string` | Yes | The scope ID. |
| `entry_id` | path | `string` | Yes | The entry ID. |

**Request Body:** `application/json` — Type: `IncrementOrderedDataStoreEntryRequest`

See [IncrementOrderedDataStoreEntryRequest](#incrementordereddatastoreentryrequest) in Models.

**Request example:**
```json
{
  "amount": 0
}
```

**Responses:**

- `200`: OK → `OrderedDataStoreEntry`

**Response fields** (`OrderedDataStoreEntry`)

See [OrderedDataStoreEntry](#ordereddatastoreentry) in Models.

**Response example:**
```json
{
  "path": "string",
  "value": 0,
  "id": "string"
}
```

**Rate Limits:** perApiKeyOwner: 1000000/minute
**Rate Limit Note:** Ordered data stores requests are subject to additional throttling limits described in the [Open Cloud guide for data stores](https://create.roblox.com/docs/cloud/guides/data-stores/throttling).

**Example:**
```bash
curl -X POST -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/cloud/v2/universes/{UNIVERSE_ID}/ordered-data-stores/{ORDERED_DATA_STORE_ID}/scopes/{SCOPE_ID}/entries/{ENTRY_ID}:increment" \
  -H "Content-Type: application/json" \
  -d '{
  "amount": 0
}'
```

### GET `/datastores/v1/universes/{universeId}/standard-datastores` [BETA]

List data stores in an experience

Returns a list of an experience's data stores.

**Auth:** API Key (`x-api-key` header)

**Scopes:** `universe-datastores.control:list`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer` | Yes | The identifier of the experience with data stores that you want to access. You can find your experience's universe ID on Creator Hub. |
| `cursor` | query | `string` | No | Provide to request the next set of data. |
| `limit` | query | `integer` | No | The maximum number of items to return. Each call only reads one partition, so it can return fewer than the given value when running out of objectives on one partition. |
| `prefix` | query | `string` | No | Provide to return only data stores with this prefix. |

**Responses:**

- `200`:  → `object`

**Response fields** (`object`)

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | `OCV1.DataStores.DataStore[]` | No | An array of data stores in the target experience. |
| `nextPageCursor` | `string` | No | Indicates that there is more data available in the requested result set. |

**Response example:**
```json
{
  "data": [
    {
      "name": "...",
      "createdTime": "..."
    }
  ],
  "nextPageCursor": "string"
}
```

**Rate Limits:** perApiKeyOwner: 5000/minute
**Rate Limit Note:** See [Throttling](/cloud/guides/data-stores/throttling.md).

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/datastores/v1/universes/{UNIVERSEID}/standard-datastores"
```

### GET `/datastores/v1/universes/{universeId}/standard-datastores/datastore/entries` [BETA]

List entries

Returns a list of entry keys within a data store.

 Entries marked deleted with a tombstone version are still included in the response if they have yet to be permanently deleted.

**Auth:** API Key (`x-api-key` header)

**Scopes:** `universe-datastores.objects:list`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer` | Yes | The identifier of the experience with data stores that you want to access. You can find your experience's universe ID on Creator Hub. |
| `datastoreName` | query | `string` | No | The name of the data store. |
| `scope` | query | `string` | No | The value is `global` by default. See [Scopes](/cloud-services/data-stores/index.md#scopes). |
| `allScopes` | query | `boolean` | No | Set to true to return keys from all scopes. |
| `prefix` | query | `string` | No | Provide to return only keys with this prefix. |
| `cursor` | query | `string` | No | Provide to request the next set of data. |
| `limit` | query | `integer` | No | The maximum number of items to return. Each call only reads one partition, so it can return fewer than the given value when running out of objectives on one partition. |

**Responses:**

- `200`:  → `object`

**Response fields** (`object`)

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `keys` | `string[]` | No | An array of entry keys within the target data store. |
| `nextPageCursor` | `string` | No | Indicates that there is more data available in the requested result set. |

**Response example:**
```json
{
  "keys": [
    "string"
  ],
  "nextPageCursor": "string"
}
```

**Rate Limits:** perApiKeyOwner: 5000/minute
**Rate Limit Note:** See [Throttling](/cloud/guides/data-stores/throttling.md).

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/datastores/v1/universes/{UNIVERSEID}/standard-datastores/datastore/entries"
```

### GET `/datastores/v1/universes/{universeId}/standard-datastores/datastore/entries/entry` [BETA]

Get entry.

Returns the value and metadata associated with an entry.

Entries marked deleted with a tombstone version will return 404 Not Found.

Metadata can be found in the response headers like the following:
```text
content-md5: zuYxEhwuySMv0i8CitXImw==
roblox-entry-version: 08D9E6A3F2188CFF.0000000001.08D9E6A3F2188CFF.01
roblox-entry-created-time: 2022-02-02T23:30:06.5388799+00:00
roblox-entry-version-created-time: 2022-02-02T23:30:06.5388799+00:00
roblox-entry-attributes: { "myAttribute": "myValue" }
roblox-entry-userids: [1, 2, 3]
```

| Header | Description |
|---|---| 
| `content-md5` | The base64-encoded MD5 checksum of the content. See [Content-MD5](/cloud/guides/data-stores/request-handling.md#content-md5). |
| `roblox-entry-version` | The version of the returned entry. |
| `roblox-entry-created-time` | The time at which the entry was created. |
| `roblox-entry-version-created-time` | The time at which this particular version was created. |
| `roblox-entry-attributes` | Attributes tagged with the entry. Serialized JSON map object. |
| `roblox-entry-userids` | Comma-separated list of Roblox user IDs tagged with the entry. |

**Auth:** API Key (`x-api-key` header)

**Scopes:** `universe-datastores.objects:read`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer` | Yes | The identifier of the experience with data stores that you want to access. You can find your experience's universe ID on Creator Hub. |
| `datastoreName` | query | `string` | No | The name of the data store. |
| `entryKey` | query | `string` | No | The key identifying the entry. |
| `scope` | query | `string` | No | The value is `global` by default. See [Scopes](/cloud-services/data-stores/index.md#scopes). |

**Responses:**

- `200`: Successfully retrieved the entry. → `object`
- `204`: The key is marked as deleted.

**Rate Limits:** perApiKeyOwner: 5000/minute
**Rate Limit Note:** See [Throttling](/cloud/guides/data-stores/throttling.md).

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/datastores/v1/universes/{UNIVERSEID}/standard-datastores/datastore/entries/entry"
```

### POST `/datastores/v1/universes/{universeId}/standard-datastores/datastore/entries/entry` [BETA]

Set entry.

Sets the value, metadata and user IDs associated with an entry.

**Auth:** API Key (`x-api-key` header)

**Scopes:** `universe-datastores.objects:update`, `universe-datastores.objects:create`, `universe-datastores.control:create`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer` | Yes | The identifier of the experience with data stores that you want to access. You can find your experience's universe ID on Creator Hub. |
| `datastoreName` | query | `string` | No | The name of the data store. |
| `entryKey` | query | `string` | No | The key identifying the entry. |
| `matchVersion` | query | `string` | No | Provide to update only if the current version matches this. |
| `exclusiveCreate` | query | `boolean` | No | Create the entry only if it does not exist. |
| `scope` | query | `string` | No | The value is `global` by default. See [Scopes](/cloud-services/data-stores/index.md#scopes). |
| `roblox-entry-attributes` | header | `string` | No | Attributes to be associated with new version of the entry. Serialized by JSON map objects. If not provided, existing attributes are cleared. |
| `roblox-entry-userids` | header | `string` | No | Comma-separated list of Roblox user IDs tagged with the entry. If not provided, existing user IDs are cleared. |
| `content-md5` | header | `string` | No | The base64-encoded MD5 checksum of the content. See [Content-MD5](/cloud/guides/data-stores/request-handling.md#content-md5). |

**Request Body:** `application/json` — Type: `string`

**Responses:**

- `200`:  → `EntryVersion`

**Response fields** (`EntryVersion`)

See [EntryVersion](#entryversion) in Models.

**Response example:**
```json
{
  "version": "string",
  "deleted": false,
  "contentLength": 0,
  "createdTime": "2024-01-01T00:00:00Z",
  "objectCreatedTime": "2024-01-01T00:00:00Z"
}
```

**Rate Limits:** perApiKeyOwner: 5000/minute
**Rate Limit Note:** See [Throttling](/cloud/guides/data-stores/throttling.md).

**Example:**
```bash
curl -X POST -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/datastores/v1/universes/{UNIVERSEID}/standard-datastores/datastore/entries/entry" \
  -H "Content-Type: application/json" \
  -d '"string"'
```

### DELETE `/datastores/v1/universes/{universeId}/standard-datastores/datastore/entries/entry` [BETA]

Delete entry.

Marks the entry as deleted by creating a tombstone version. Entries are deleted permanently after 30 days.

**Auth:** API Key (`x-api-key` header)

**Scopes:** `universe-datastores.objects:delete`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer` | Yes | The identifier of the experience with data stores that you want to access. You can find your experience's universe ID on Creator Hub. |
| `datastoreName` | query | `string` | No | The name of the data store. |
| `entryKey` | query | `string` | No | The key identifying the entry. |
| `scope` | query | `string` | No | The value is `global` by default. See [Scopes](/cloud-services/data-stores/index.md#scopes). |

**Responses:**

- `204`: The entry is deleted.

**Rate Limits:** perApiKeyOwner: 5000/minute
**Rate Limit Note:** See [Throttling](/cloud/guides/data-stores/throttling.md).

**Example:**
```bash
curl -X DELETE -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/datastores/v1/universes/{UNIVERSEID}/standard-datastores/datastore/entries/entry"
```

### POST `/datastores/v1/universes/{universeId}/standard-datastores/datastore/entries/entry/increment` [BETA]

Increment entry

Increments the value for an entry by a given amount, or create a new entry with that amount. Returns the entry and metadata.

Metadata can be found in the response headers like the following:
```text
content-md5: zuYxEhwuySMv0i8CitXImw==
roblox-entry-version: 08D9E6A3F2188CFF.0000000001.08D9E6A3F2188CFF.01
roblox-entry-created-time: 2022-02-02T23:30:06.5388799+00:00
roblox-entry-version-created-time: 2022-02-02T23:30:06.5388799+00:00
roblox-entry-attributes: { "myAttribute": "myValue" }
roblox-entry-userids: [1, 2, 3]
```

| Header | Description |
|---|---| 
| `content-md5` | The base64-encoded MD5 checksum of the content. See [Content-MD5](/cloud/guides/data-stores/request-handling.md#content-md5). |
| `roblox-entry-version` | The version of the returned entry. |
| `roblox-entry-created-time` | The time at which the entry was created. |
| `roblox-entry-version-created-time` | The time at which this particular version was created. |
| `roblox-entry-attributes` | Attributes tagged with the entry. Serialized JSON map object. |
| `roblox-entry-userids` | Comma-separated list of Roblox user IDs tagged with the entry. |

**Auth:** API Key (`x-api-key` header)

**Scopes:** `universe-datastores.objects:update`, `universe-datastores.objects:create`, `universe-datastores.control:create`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer` | Yes | The identifier of the experience with data stores that you want to access. You can find your experience's universe ID on Creator Hub. |
| `datastoreName` | query | `string` | No | The name of the data store. |
| `entryKey` | query | `string` | No | The key identifying the entry. |
| `incrementBy` | query | `integer` | No | The amount by which the entry should be incremented, or the starting value if it doesn't exist. |
| `scope` | query | `string` | No | The value is `global` by default. See [Scopes](/cloud-services/data-stores/index.md#scopes). |
| `roblox-entry-attributes` | header | `string` | No | Attributes to be associated with new version of the entry. Serialized by JSON map objects. If not provided, existing attributes are cleared. |
| `roblox-entry-userids` | header | `string` | No | A comma-separated list of Roblox user IDs that the entry is tagged with. If not provided, existing user IDs are cleared. |

**Responses:**

- `200`: Returns the latest version of the entry after it has been incremented. → `object`
- `204`: The key is marked as deleted.

**Rate Limits:** perApiKeyOwner: 5000/minute
**Rate Limit Note:** See [Throttling](/cloud/guides/data-stores/throttling.md).

**Example:**
```bash
curl -X POST -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/datastores/v1/universes/{UNIVERSEID}/standard-datastores/datastore/entries/entry/increment"
```

### GET `/datastores/v1/universes/{universeId}/standard-datastores/datastore/entries/entry/versions` [BETA]

List entry versions

Returns a list of versions for an entry.

**Auth:** API Key (`x-api-key` header)

**Scopes:** `universe-datastores.versions:list`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer` | Yes | The identifier of the experience with data stores that you want to access. You can find your experience's universe ID on Creator Hub. |
| `datastoreName` | query | `string` | No | The name of the data store. |
| `entryKey` | query | `string` | No | The key identifying the entry. |
| `scope` | query | `string` | No | The value is `global` by default. See [Scopes](/cloud-services/data-stores/index.md#scopes). |
| `cursor` | query | `string` | No | Provide to request the next set of data. |
| `startTime` | query | `string` | No | Provide to not include versions earlier than this timestamp. |
| `endTime` | query | `string` | No | Provide to not include versions later than this timestamp. |
| `sortOrder` | query | `string` | No | Either `Ascending` (earlier versions first) or `Descending` (later versions first). |
| `limit` | query | `integer` | No | The maximum number of items to return. Each call only reads one partition, so it can return fewer than the given value when running out of objectives on one partition. |

**Responses:**

- `200`:  → `EntryVersion`
- `400`: Invalid request / Invalid file content.
- `403`: Publish not allowed on place.
- `404`: The experience or data store was not found.
- `429`: Too Many Requests.

**Response fields** (`EntryVersion`)

See [EntryVersion](#entryversion) in Models.

**Response example:**
```json
{
  "version": "string",
  "deleted": false,
  "contentLength": 0,
  "createdTime": "2024-01-01T00:00:00Z",
  "objectCreatedTime": "2024-01-01T00:00:00Z"
}
```

**Error handling:** `429`: Retry with exponential backoff (start at 1s). `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 5000/minute
**Rate Limit Note:** See [Throttling](/cloud/guides/data-stores/throttling.md).

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/datastores/v1/universes/{UNIVERSEID}/standard-datastores/datastore/entries/entry/versions"
```

### GET `/datastores/v1/universes/{universeId}/standard-datastores/datastore/entries/entry/versions/version` [BETA]

Get entry version.

Returns the value and metadata of a specific version of an entry.

Metadata can be found in the response headers like the following:
```text
content-md5: zuYxEhwuySMv0i8CitXImw==
roblox-entry-version: 08D9E6A3F2188CFF.0000000001.08D9E6A3F2188CFF.01
roblox-entry-created-time: 2022-02-02T23:30:06.5388799+00:00
roblox-entry-version-created-time: 2022-02-02T23:30:06.5388799+00:00
roblox-entry-attributes: { "myAttribute": "myValue" }
roblox-entry-userids: [1, 2, 3]
```

| Header | Description |
|---|---| 
| `content-md5` | The base64-encoded MD5 checksum of the content. See [Content-MD5](/cloud/guides/data-stores/request-handling.md#content-md5). |
| `roblox-entry-version` | The version of the returned entry. |
| `roblox-entry-created-time` | The time at which the entry was created. |
| `roblox-entry-version-created-time` | The time at which this particular version was created. |
| `roblox-entry-attributes` | Attributes tagged with the entry. Serialized JSON map object. |
| `roblox-entry-userids` | Comma-separated list of Roblox user IDs tagged with the entry. |

**Auth:** API Key (`x-api-key` header)

**Scopes:** `universe-datastores.versions:read`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer` | Yes | The identifier of the experience with data stores that you want to access. You can find your experience's universe ID on Creator Hub. |
| `datastoreName` | query | `string` | No | The name of the data store. |
| `entryKey` | query | `string` | No | The key identifying the entry. |
| `versionId` | query | `string` | No | The version to inspect. |
| `scope` | query | `string` | No | The value is `global` by default. See [Scopes](/cloud-services/data-stores/index.md#scopes). |

**Responses:**

- `200`: Successfully retrieved the entry. → `object`

**Rate Limits:** perApiKeyOwner: 5000/minute
**Rate Limit Note:** See [Throttling](/cloud/guides/data-stores/throttling.md).

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/datastores/v1/universes/{UNIVERSEID}/standard-datastores/datastore/entries/entry/versions/version"
```

### GET `/ordered-data-stores/v1/universes/{universeId}/orderedDataStores/{orderedDataStore}/scopes/{scope}/entries` [BETA]

Returns a list of entries from an ordered data store.

**Auth:** API Key (`x-api-key` header)

**Scopes:** `universe.ordered-data-store.scope.entry:read`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `string` | Yes | The identifier of the experience with ordered data stores that you want to access. You can find your experience's universe ID on Creator Hub. |
| `orderedDataStore` | path | `string` | Yes | The name of the target ordered data store. |
| `scope` | path | `string` | Yes | The name of the data store scope. See [Scopes](/cloud/guides/data-stores/request-handling.md#scopes). |
| `max_page_size` | query | `integer` | No | The maximum number of entries to return. The service may return fewer than this value. The default value is `10`. The maximum value is `100`, and any input above 100 is coerced to `100`. |
| `page_token` | query | `string` | No | A page token received from a previous `List` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `List` must match the call providing the page token. |
| `order_by` | query | `string` | No | The enumeration direction. The order by default is ascending. Input a `desc` suffix for descending. |
| `filter` | query | `string` | No | The range of qualifying values of entries to return. See [Filters](/cloud/guides/data-stores/request-handling.md#filters). |

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

**Rate Limits:** perApiKeyOwner: 500/minute
**Rate Limit Note:** See [Throttling](/cloud/guides/data-stores/throttling.md).

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/ordered-data-stores/v1/universes/{UNIVERSEID}/orderedDataStores/{ORDEREDDATASTORE}/scopes/{SCOPE}/entries"
```

### POST `/ordered-data-stores/v1/universes/{universeId}/orderedDataStores/{orderedDataStore}/scopes/{scope}/entries` [BETA]

Creates a new entry with the content value provided.

**Auth:** API Key (`x-api-key` header)

**Scopes:** `universe.ordered-data-store.scope.entry:write`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `string` | Yes | The identifier of the experience with ordered data stores that you want to access. You can find your experience's universe ID on Creator Hub. |
| `orderedDataStore` | path | `string` | Yes | The name of the ordered data store. |
| `scope` | path | `string` | Yes | The name of the data store scope. See [Scopes](/cloud/guides/data-stores/request-handling.md#scopes). |
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

**Rate Limits:** perApiKeyOwner: 500/minute
**Rate Limit Note:** See [Throttling](/cloud/guides/data-stores/throttling.md).

**Example:**
```bash
curl -X POST -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/ordered-data-stores/v1/universes/{UNIVERSEID}/orderedDataStores/{ORDEREDDATASTORE}/scopes/{SCOPE}/entries?id={VALUE}" \
  -H "Content-Type: application/json" \
  -d '{
  "value": 0
}'
```

### GET `/ordered-data-stores/v1/universes/{universeId}/orderedDataStores/{orderedDataStore}/scopes/{scope}/entries/{entry}` [BETA]

Gets and returns the specified entry.

**Auth:** API Key (`x-api-key` header)

**Scopes:** `universe.ordered-data-store.scope.entry:read`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `string` | Yes | The identifier of the experience with ordered data stores that you want to access. You can find your experience's universe ID on Creator Hub. |
| `orderedDataStore` | path | `string` | Yes | The name of the ordered data store. |
| `scope` | path | `string` | Yes | The name of the data store scope. See [Scopes](/cloud/guides/data-stores/request-handling.md#scopes). |
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

**Rate Limits:** perApiKeyOwner: 500/minute
**Rate Limit Note:** See [Throttling](/cloud/guides/data-stores/throttling.md).

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/ordered-data-stores/v1/universes/{UNIVERSEID}/orderedDataStores/{ORDEREDDATASTORE}/scopes/{SCOPE}/entries/{ENTRY}"
```

### PATCH `/ordered-data-stores/v1/universes/{universeId}/orderedDataStores/{orderedDataStore}/scopes/{scope}/entries/{entry}` [BETA]

Updates an entry value and returns the updated entry.

**Auth:** API Key (`x-api-key` header)

**Scopes:** `universe.ordered-data-store.scope.entry:write`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `string` | Yes | The identifier of the experience with ordered data stores that you want to access. You can find your experience's universe ID on Creator Hub. |
| `orderedDataStore` | path | `string` | Yes | The name of the ordered data store. |
| `scope` | path | `string` | Yes | The name of the data store scope. See [Scopes](/cloud/guides/data-stores/request-handling.md#scopes). |
| `entry` | path | `string` | Yes | The entry ID. |
| `allow_missing` | query | `boolean` | No | The flag to allow the creation of an entry if the entry doesn't exist. See [Allow missing flags](/cloud/guides/data-stores/request-handling.md.md#allow-missing-flags). |

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

**Rate Limits:** perApiKeyOwner: 500/minute
**Rate Limit Note:** See [Throttling](/cloud/guides/data-stores/throttling.md).

**Example:**
```bash
curl -X PATCH -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/ordered-data-stores/v1/universes/{UNIVERSEID}/orderedDataStores/{ORDEREDDATASTORE}/scopes/{SCOPE}/entries/{ENTRY}" \
  -H "Content-Type: application/json" \
  -d '{
  "value": 0
}'
```

### DELETE `/ordered-data-stores/v1/universes/{universeId}/orderedDataStores/{orderedDataStore}/scopes/{scope}/entries/{entry}` [BETA]

Deletes the specified entry. Unlike standard data stores, which mark entries for deletion, ordered data store entries are deleted immediately.

**Auth:** API Key (`x-api-key` header)

**Scopes:** `universe.ordered-data-store.scope.entry:write`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `string` | Yes | The identifier of the experience with ordered data stores that you want to access. You can find your experience's universe ID on Creator Hub. |
| `orderedDataStore` | path | `string` | Yes | The name of the ordered data store. |
| `scope` | path | `string` | Yes | The name of the data store scope. See [Scopes](/cloud/guides/data-stores/request-handling.md#scopes). |
| `entry` | path | `string` | Yes | The entry ID. |

**Responses:**

- `200`: Success: the entry was successfully deleted or didn't exist.
- `400`: Bad Request: invalid orderedDataStore, scope or entry name or encoding.
- `403`: Forbidden: Studio access to APIs is not allowed, incorrect API key or scope.
- `404`: Not found.
- `429`: Too Many Requests.

**Error handling:** `429`: Retry with exponential backoff (start at 1s). `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 500/minute
**Rate Limit Note:** See [Throttling](/cloud/guides/data-stores/throttling.md).

**Example:**
```bash
curl -X DELETE -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/ordered-data-stores/v1/universes/{UNIVERSEID}/orderedDataStores/{ORDEREDDATASTORE}/scopes/{SCOPE}/entries/{ENTRY}"
```

### POST `/ordered-data-stores/v1/universes/{universeId}/orderedDataStores/{orderedDataStore}/scopes/{scope}/entries/{entry}:increment` [BETA]

Increments the value of the key by the provided amount and returns the updated entry.

Known issue: Entry values can increment past the valid range and this may persist in the backend. Returned values will clamp to the valid range.

**Auth:** API Key (`x-api-key` header)

**Scopes:** `universe.ordered-data-store.scope.entry:write`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `string` | Yes | The identifier of the experience with ordered data stores that you want to access. You can find your experience's universe ID on Creator Hub. |
| `orderedDataStore` | path | `string` | Yes | The name of the ordered data store. |
| `scope` | path | `string` | Yes | The name of the data store scope. See [Scopes](/cloud/guides/data-stores/request-handling.md#scopes). |
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

**Rate Limits:** perApiKeyOwner: 500/minute
**Rate Limit Note:** See [Throttling](/cloud/guides/data-stores/throttling.md).

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

### ListDataStoresResponse

A list of DataStores in the parent collection.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `dataStores` | `DataStore[]` | No | The DataStores from the specified Universe. |
| `nextPageToken` | `string` | No | A token that you can send as a `pageToken` parameter to retrieve the next page. If this field is omitted, there are no subsequent pages. |

### DataStore

Represents a data store.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `path` | `string` | No | The resource path of the data store.  Format: `universes/{universe_id}/data-stores/{data_store_id}` |
| `createTime` | `string` | No | The timestamp when the data store was created. |
| `expireTime` | `string` | No | The timestamp when the data store will expire (or did expire).  This field is set when the data store is soft-deleted and indicates when it will be permanently removed. |
| `state` | `STATE_UNSPECIFIED \| ACTIVE \| DELETED` | No | The state of the data store.  Possible values:    \| Value \| Description \|   \| --- \| --- \|   \| STATE_UNSPECIFIED \| The default value. This value is used if the state is omitted. \|   \| ACTIVE \| The data store is active. \|   \| DELETED \| The data store is deleted.  After the expiration time passes, it will be permanently deleted. \| |
| `id` | `string` | No | The ID of the data store. Matches the last segment of the path. |

### ListDataStoreEntriesResponse

A list of DataStoreEntries in the parent collection.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `dataStoreEntries` | `DataStoreEntry[]` | No | The DataStoreEntries from the specified DataStore or DataStoreScope. |
| `nextPageToken` | `string` | No | A token that you can send as a `pageToken` parameter to retrieve the next page. If this field is omitted, there are no subsequent pages. |

### DataStoreEntry

A key-value entry in a data store.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `path` | `string` | No | The resource path of the data store entry.  Formats: * `universes/{universe_id}/data-stores/{data_store_id}/entries/{data_store_entry_id}` * `universes/{universe_id}/data-stores/{data_store_id}/scopes/{data_store_scope_id}/entries/{data_store_entry_id}` |
| `createTime` | `string` | No | The timestamp when the data store entry was created. |
| `revisionId` | `string` | No |  *(immutable)* The revision ID of the data store entry.  A new revision is committed whenever the data store entry is changed in any way.  The format is an arbitrary string. Example: "foo" |
| `revisionCreateTime` | `string` | No | The timestamp when the revision was created. |
| `state` | `STATE_UNSPECIFIED \| ACTIVE \| DELETED` | No | The state of the data store entry.  Possible values:    \| Value \| Description \|   \| --- \| --- \|   \| STATE_UNSPECIFIED \| The default value. This value is used if the state is omitted. \|   \| ACTIVE \| The data store entry is active.  The default state of a newly created data store entry. \|   \| DELETED \| The data store entry is deleted.  At some point in the future, it will be permanently deleted. \| |
| `etag` | `string` | No | This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests (and potentially on certain custom methods) to ensure the client has an up-to-date value before proceeding. |
| `value` | `GoogleProtobufValue` | No | The value of the entry.  When a stored value contains a non-finite Luau number that JSON can't represent, Open Cloud responses replace the number with a tagged JSON object:  * Positive infinity: `{"m": null, "t": "numeric", "v": "inf"}` * Negative infinity: `{"m": null, "t": "numeric", "v": "-inf"}` * NaN: `{"m": null, "t": "numeric", "v": "nan"}` |
| `id` | `string` | No | The resource ID of the entry.  This matches the last segment of the resource path, and is provided only for convenience. |
| `users` | `string[]` | No | Users associated with the entry.  Each value must be a user resource path in the format `users/{user_id}`, not a bare user ID. |
| `attributes` | `object` | No | An arbitrary set of attributes associated with the entry. |

### IncrementDataStoreEntryRequest

Increments the entry value.

If the value is not numeric, this request fails.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `amount` | `number` | No | The amount by which to increment the entry value. Both the existing value and the increment amount must be integers. |
| `users` | `string[]` | No | Users associated with the entry.  Each value must be a user resource path in the format `users/{user_id}`, not a bare user ID.  If this is not provided, existing user IDs are cleared. |
| `attributes` | `object` | No | An arbitrary set of attributes associated with the entry.  If this is not provided, existing attributes are cleared. |

### ListDataStoreEntryRevisionsResponse

A list of revisions of a data store entry.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `dataStoreEntries` | `DataStoreEntry[]` | No | The revisions of the data_store_entry. |
| `nextPageToken` | `string` | No | A token that you send as a `pageToken` parameter to retrieve the next page. If this field is omitted, there are no subsequent pages. |

### UndeleteDataStoreRequest

Restore the data store

| Property | Type | Required | Description |
|----------|------|----------|-------------|

### SnapshotDataStoresRequest

Takes a new snapshot for the given experience.

| Property | Type | Required | Description |
|----------|------|----------|-------------|

### SnapshotDataStoresResponse

Returns whether a new snapshot was taken and the time of the latest snapshot
after the operation (regardless of whether a new snapshot was taken).

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `newSnapshotTaken` | `boolean` | No | Whether a new snapshot was taken by this operation. (Only one snapshot can be taken per experience per UTC day.) |
| `latestSnapshotTime` | `string` | No | The time of the latest snapshot after the operation (regardless of whether a new snapshot was created). This time is always returned in UTC. |

### OCV2.Operations.Operation

This resource represents a long-running operation that is the result of a
network API call.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `path` | `string` | No | The server-assigned path, which is only unique within the same service that originally returns it. If you use the default HTTP mapping, the `path` should be a resource path ending with `operations/{unique_id}`. |
| `metadata` | `GoogleProtobufAny` | No | Service-specific metadata associated with the operation.  It typically contains progress information and common metadata such as create time. Some services might not provide such metadata.  Any method that returns a long-running operation should document the metadata type, if any. |
| `done` | `boolean` | No | If the value is `false`, it means the operation is still in progress. If `true`, the operation is completed, and either `error` or `response` is available. |
| `error` | `Status` | No | The error result of the operation in case of failure or cancellation. |
| `response` | `GoogleProtobufAny` | No | The normal response of the operation in case of success.  If the original method returns no data on success, such as `Delete`, the response is `google.protobuf.Empty`.  If the original method is standard `Get`/`Create`/`Update`, the response should be the resource.  For other methods, the response should have the type `XxxResponse`, where `Xxx` is the original method name.  For example, if the original method name is `TakeSnapshot()`, the inferred response type is `TakeSnapshotResponse`. |

### MemoryStoreQueueItem

Represents an item within a queue structure.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `path` | `string` | No | The resource path of the memory store queue item.  Format: `cloud/v2/universes/{universe_id}/memory-store/queues/{memory_store_queue_id}/items/{memory_store_queue_item_id}` |
| `data` | `GoogleProtobufValue` | No | The value of the queue item. |
| `priority` | `number` | No | The priority of the queue item. |
| `ttl` | `string` | No | The TTL for the item. |
| `expireTime` | `string` | No | The expiration time of the item. |
| `id` | `string` | No | The name of the item. |

### DiscardMemoryStoreQueueItemsRequest

Discards read items from the front of the queue.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `readId` | `string` | No | The `readId` of the previous read operation for which to discard read items. |

### ReadMemoryStoreQueueItemsResponse

Returns the specified number of items at the front of the queue.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `readId` | `string` | No | An identifier of the read operation  This can be passed to `:discard` in order to mark the items as processed. |
| `items` | `MemoryStoreQueueItem[]` | No | The items read from the queue |

### ListMemoryStoreSortedMapItemsResponse

A list of MemoryStoreSortedMapItems in the parent collection.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `items` | `MemoryStoreSortedMapItem[]` | No | The MemoryStoreSortedMapItems from the specified MemoryStoreSortedMap. |
| `nextPageToken` | `string` | No | A token that you can send as a `pageToken` parameter to retrieve the next page. If this field is omitted, there are no subsequent pages. |

### MemoryStoreSortedMapItem

Represents an item within a sorted map structure.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `path` | `string` | No | The resource path of the memory store sorted map item.  Format: `cloud/v2/universes/{universe_id}/memory-store/sorted-maps/{memory_store_sorted_map_id}/items/{memory_store_sorted_map_item_id}` |
| `value` | `GoogleProtobufValue` | No | The value of the item. |
| `etag` | `string` | No | The server generated tag of an item. |
| `ttl` | `string` | No | The TTL for the item. |
| `expireTime` | `string` | No | The expiration time of the item. |
| `id` | `string` | No | The name of the item. |
| `stringSortKey` | `string` | No | The item will be sorted lexicographically according to this string. |
| `numericSortKey` | `number` | No | The item will be sorted according to this number. |

### Operation

This resource represents a long-running operation that is the result of a
network API call.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `path` | `string` | No | The server-assigned path, which is only unique within the same service that originally returns it. If you use the default HTTP mapping, the `path` should be a resource path ending with `operations/{unique_id}`. |
| `metadata` | `GoogleProtobufAny` | No | Service-specific metadata associated with the operation.  It typically contains progress information and common metadata such as create time. Some services might not provide such metadata.  Any method that returns a long-running operation should document the metadata type, if any. |
| `done` | `boolean` | No | If the value is `false`, it means the operation is still in progress. If `true`, the operation is completed, and either `error` or `response` is available. |
| `error` | `Status` | No | The error result of the operation in case of failure or cancellation. |
| `response` | `GoogleProtobufAny` | No | The normal response of the operation in case of success.  If the original method returns no data on success, such as `Delete`, the response is `google.protobuf.Empty`.  If the original method is standard `Get`/`Create`/`Update`, the response should be the resource.  For other methods, the response should have the type `XxxResponse`, where `Xxx` is the original method name.  For example, if the original method name is `TakeSnapshot()`, the inferred response type is `TakeSnapshotResponse`. |

### ListOrderedDataStoreEntriesResponse

A list of OrderedDataStoreEntries in the parent collection.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `orderedDataStoreEntries` | `OrderedDataStoreEntry[]` | No | The OrderedDataStoreEntries from the specified OrderedDataStoreScope. |
| `nextPageToken` | `string` | No | A token that you can send as a `pageToken` parameter to retrieve the next page. If this field is omitted, there are no subsequent pages. |

### OrderedDataStoreEntry

A key-value entry in an ordered data store.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `path` | `string` | No | The resource path of the ordered data store entry.  Format: `universes/{universe_id}/ordered-data-stores/{ordered_data_store_id}/scopes/{ordered_data_store_scope_id}/entries/{ordered_data_store_entry_id}` |
| `value` | `number` | No | The value of the entry.  Always rounded to the nearest integer. |
| `id` | `string` | No | The name of the entry. |

### IncrementOrderedDataStoreEntryRequest

Increments the entry value.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `amount` | `number` | No | The amount by which to increment the entry value. Both the existing value and the increment amount must be integers. |

### OCV1.DataStores.DataStore

The data store object with its name and created time.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | `string` | No | The name of your data store. |
| `createdTime` | `string` | No | The timestamp of when the data store was created in the ISO time format. |

### EntryVersion

The entry version object returned by the `List Entry Versions` method.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `version` | `string` | No | The version name of the qualifying entry. |
| `deleted` | `boolean` | No | Indicates whether the entry has been deleted. |
| `contentLength` | `number` | No | The length of the content. |
| `createdTime` | `string` | No | The timestamp of when the version was created in the ISO time format. |
| `objectCreatedTime` | `string` | No | The timestamp of when the data store was created in the ISO time format. |

### ListEntriesResponse

A list of Entries in the parent collection.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `entries` | `Entry[]` | No | The Entries from the specified Scope. |
| `nextPageToken` | `string` | No | A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages. |

### CreateEntryRequest

Creates a new entry with the value provided.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `value` | `integer` | Yes | The value to set the new entry. If the input value exceeds the maximum value supported by int64, which is 9,223,372,036,854,775,807, the request fails with a 400 Bad Request error. |

### Entry

Represents an entry.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `path` | `string` | No | The resource path of the request. |
| `id` | `string` | No | The name of the entry |
| `value` | `integer` | No | The value of the entry. |

### UpdateEntryRequest

Updates the entry provided with a new value.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `value` | `integer` | Yes | The value to update the entry. If the input value exceeds the maximum value supported by int64, which is 9,223,372,036,854,775,807, the request fails with a 400 Bad Request error. |

### IncrementEntryRequest

Increments entry value.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `amount` | `integer` | Yes | The amount to increment by the entry value. If the input value exceeds the maximum value supported by int64, which is 9,223,372,036,854,775,807, the request fails with a 400 Bad Request error. |