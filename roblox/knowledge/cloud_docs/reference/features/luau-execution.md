---
name: "Luau Execution"
last_updated: 2026-10-30T19:56:08Z
type: feature
api_base_url: "https://apis.roblox.com"
endpoints: 5
auth: [api-key, oauth2, cookie]
description: "Run Luau scripts headlessly in a Roblox place via Open Cloud for automated testing, game configuration, and procedural generation, with full DataModel and engine Luau API access"
---

# Luau Execution

Run Luau scripts headlessly in a Roblox place via Open Cloud for automated testing, game configuration, and procedural generation, with full DataModel and engine Luau API access. Tasks can run for up to 5 minutes, with a limit of 10 concurrent tasks per place. You can save changes using [`SavePlaceAsync`](/reference/engine/classes/AssetService#SavePlaceAsync), pass in large binary payloads, and use [`SerializationService`](/reference/engine/classes/SerializationService) to deserialize RBXM content. For a reference implementation, see [Roblox/place-ci-cd-demo](https://github.com/Roblox/place-ci-cd-demo) on GitHub.

Workflow:

1. [Create a task](#Cloud_CreateLuauExecutionSessionTask__Using_Universes) with your universeId, placeId, and the Luau script to run
2. A server launches, loads the place, and executes your code
3. [Poll for completion](#Cloud_GetLuauExecutionSessionTask) and receive the script's return values and [logs](#Cloud_ListLuauExecutionSessionTaskLogs)

Common use cases include:

- Automated testing: Run test scripts against specific place versions as part of a CI/CD pipeline
- Game configuration: Update pricing, stats, and balancing variables outside of Studio

> **Getting started:** See [Engine instances](/docs/en-us/cloud/guides/instance.md) for a complete walkthrough with working examples.

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

### POST `/cloud/v2/universes/{universe_id}/luau-execution-session-task-binary-inputs` [STABLE]

Create Luau Execution Session Task Binary Input

Create a new `LuauExecutionSessionTaskBinaryInput`.

**Auth:** API Key (`x-api-key` header)

**Scopes:** `universe.place.luau-execution-session:write`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universe_id` | path | `string` | Yes | The universe ID. |

**Request Body:** `application/json` — Type: `LuauExecutionSessionTaskBinaryInput`

See [LuauExecutionSessionTaskBinaryInput](#luauexecutionsessiontaskbinaryinput) in Models.

**Request example:**
```json
{
  "path": "string",
  "size": 0,
  "uploadUri": "string"
}
```

**Responses:**

- `200`: OK → `LuauExecutionSessionTaskBinaryInput`

**Response fields** (`LuauExecutionSessionTaskBinaryInput`)

See [LuauExecutionSessionTaskBinaryInput](#luauexecutionsessiontaskbinaryinput) in Models.

**Response example:**
```json
{
  "path": "string",
  "size": 0,
  "uploadUri": "string"
}
```

**Rate Limits:** perApiKeyOwner: 5/minute

**Example:**
```bash
curl -X POST -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/cloud/v2/universes/{UNIVERSE_ID}/luau-execution-session-task-binary-inputs" \
  -H "Content-Type: application/json" \
  -d '{
  "path": "string",
  "size": 0,
  "uploadUri": "string"
}'
```

### POST `/cloud/v2/universes/{universe_id}/places/{place_id}/luau-execution-session-tasks` [STABLE]

Create Luau Execution Session Task

Creates a task but does not wait for the task to complete.

To check whether a task has
completed, call the `GetLuauExecutionSessionTask` method and inspect the
`state` field of the returned resource.

**Auth:** API Key (`x-api-key` header)

**Scopes:** `universe.place.luau-execution-session:write`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universe_id` | path | `string` | Yes | The universe ID. |
| `place_id` | path | `string` | Yes | The place ID. |

**Request Body:** `application/json` — Type: `LuauExecutionSessionTask`

See [LuauExecutionSessionTask](#luauexecutionsessiontask) in Models.

**Request example:**
```json
{
  "path": "string",
  "createTime": "2024-01-01T00:00:00Z",
  "updateTime": "2024-01-01T00:00:00Z",
  "user": "string",
  "state": "STATE_UNSPECIFIED",
  "script": "string"
}
```

**Responses:**

- `200`: OK → `LuauExecutionSessionTask`

**Response fields** (`LuauExecutionSessionTask`)

See [LuauExecutionSessionTask](#luauexecutionsessiontask) in Models.

**Response example:**
```json
{
  "path": "string",
  "createTime": "2024-01-01T00:00:00Z",
  "updateTime": "2024-01-01T00:00:00Z",
  "user": "string",
  "state": "STATE_UNSPECIFIED",
  "script": "string"
}
```

**Rate Limits:** perApiKeyOwner: 5/minute

**Example:**
```bash
curl -X POST -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/cloud/v2/universes/{UNIVERSE_ID}/places/{PLACE_ID}/luau-execution-session-tasks" \
  -H "Content-Type: application/json" \
  -d '{
  "path": "string",
  "createTime": "2024-01-01T00:00:00Z",
  "updateTime": "2024-01-01T00:00:00Z",
  "user": "string",
  "state": "STATE_UNSPECIFIED",
  "script": "string"
}'
```

### POST `/cloud/v2/universes/{universe_id}/places/{place_id}/versions/{version_id}/luau-execution-session-tasks` [STABLE]

Create Luau Execution Session Task

Creates a task but does not wait for the task to complete.

To check whether a task has
completed, call the `GetLuauExecutionSessionTask` method and inspect the
`state` field of the returned resource.

**Auth:** API Key (`x-api-key` header)

**Scopes:** `universe.place.luau-execution-session:write`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universe_id` | path | `string` | Yes | The universe ID. |
| `place_id` | path | `string` | Yes | The place ID. |
| `version_id` | path | `string` | Yes | The version ID. |

**Request Body:** `application/json` — Type: `LuauExecutionSessionTask`

See [LuauExecutionSessionTask](#luauexecutionsessiontask) in Models.

**Request example:**
```json
{
  "path": "string",
  "createTime": "2024-01-01T00:00:00Z",
  "updateTime": "2024-01-01T00:00:00Z",
  "user": "string",
  "state": "STATE_UNSPECIFIED",
  "script": "string"
}
```

**Responses:**

- `200`: OK → `LuauExecutionSessionTask`

**Response fields** (`LuauExecutionSessionTask`)

See [LuauExecutionSessionTask](#luauexecutionsessiontask) in Models.

**Response example:**
```json
{
  "path": "string",
  "createTime": "2024-01-01T00:00:00Z",
  "updateTime": "2024-01-01T00:00:00Z",
  "user": "string",
  "state": "STATE_UNSPECIFIED",
  "script": "string"
}
```

**Rate Limits:** perApiKeyOwner: 5/minute

**Example:**
```bash
curl -X POST -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/cloud/v2/universes/{UNIVERSE_ID}/places/{PLACE_ID}/versions/{VERSION_ID}/luau-execution-session-tasks" \
  -H "Content-Type: application/json" \
  -d '{
  "path": "string",
  "createTime": "2024-01-01T00:00:00Z",
  "updateTime": "2024-01-01T00:00:00Z",
  "user": "string",
  "state": "STATE_UNSPECIFIED",
  "script": "string"
}'
```

### GET `/cloud/v2/universes/{universe_id}/places/{place_id}/versions/{version_id}/luau-execution-sessions/{luau_execution_session_id}/tasks/{task_id}` [STABLE]

Get Luau Execution Session Task

Gets information about a task.

**Auth:** API Key (`x-api-key` header)

**Scopes:** `universe.place.luau-execution-session:read`, `universe.place.luau-execution-session:write`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universe_id` | path | `string` | Yes | The universe ID. |
| `place_id` | path | `string` | Yes | The place ID. |
| `version_id` | path | `string` | Yes | The version ID. |
| `luau_execution_session_id` | path | `string` | Yes | The luau-execution-session ID. |
| `task_id` | path | `string` | Yes | The task ID. |
| `view` | query | `VIEW_UNSPECIFIED \| BASIC \| FULL` | No | The view in which to retrieve the luau execution session task.  Supports BASIC and FULL.  Defaults to BASIC.  Possible values:    \| Value \| Description \|   \| --- \| --- \|   \| VIEW_UNSPECIFIED \| The luau execution session task view is not specified; the default will be used. \|   \| BASIC \| Excludes the `script` field. \|   \| FULL \| Includes all fields. \| Valid values: `VIEW_UNSPECIFIED`, `BASIC`, `FULL` |

**Responses:**

- `200`: OK → `LuauExecutionSessionTask`

**Response fields** (`LuauExecutionSessionTask`)

See [LuauExecutionSessionTask](#luauexecutionsessiontask) in Models.

**Response example:**
```json
{
  "path": "string",
  "createTime": "2024-01-01T00:00:00Z",
  "updateTime": "2024-01-01T00:00:00Z",
  "user": "string",
  "state": "STATE_UNSPECIFIED",
  "script": "string"
}
```

**Rate Limits:** perApiKeyOwner: 200/minute

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/cloud/v2/universes/{UNIVERSE_ID}/places/{PLACE_ID}/versions/{VERSION_ID}/luau-execution-sessions/{LUAU_EXECUTION_SESSION_ID}/tasks/{TASK_ID}"
```

### GET `/cloud/v2/universes/{universe_id}/places/{place_id}/versions/{version_id}/luau-execution-sessions/{luau_execution_session_id}/tasks/{task_id}/logs` [STABLE]

List Luau Execution Session Task Logs

Lists log chunks generated by a `LuauExecutionSessionTask`.

**Auth:** API Key (`x-api-key` header)

**Scopes:** `universe.place.luau-execution-session:read`, `universe.place.luau-execution-session:write`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universe_id` | path | `string` | Yes | The universe ID. |
| `place_id` | path | `string` | Yes | The place ID. |
| `version_id` | path | `string` | Yes | The version ID. |
| `luau_execution_session_id` | path | `string` | Yes | The luau-execution-session ID. |
| `task_id` | path | `string` | Yes | The task ID. |
| `maxPageSize` | query | `integer` | No | The maximum number of luau execution session task logs to return. The service might return fewer than this value. If unspecified, at most 10000 luau execution session task logs are returned. The maximum value is 10000 and higher values are set to 10000. |
| `pageToken` | query | `string` | No | A page token, received from a previous call, to retrieve a subsequent page.  When paginating, all other parameters provided to the subsequent call must match the call that provided the page token. |
| `view` | query | `VIEW_UNSPECIFIED \| FLAT \| STRUCTURED` | No | The view in which to retrieve the luau execution session task log.  Supports FLAT and STRUCTURED.  Defaults to FLAT.  Possible values:    \| Value \| Description \|   \| --- \| --- \|   \| VIEW_UNSPECIFIED \| The luau execution session task log view is not specified; the default will be used. \|   \| FLAT \| If this view is selected, the `messages` field will be populated (and the `structuredMessages` field will not). Each entry of the `messages` array contains only the log message, without additional medata. This is the default. \|   \| STRUCTURED \| If this view is selected, the `structuredMessages` field will be populated (and the `messages` field will not). Each entry of the `structuredMessages` array contains the log message plus additional metadata (see `LogMessage` for details). \| Valid values: `VIEW_UNSPECIFIED`, `FLAT`, `STRUCTURED` |

**Responses:**

- `200`: OK → `ListLuauExecutionSessionTaskLogsResponse`

**Response fields** (`ListLuauExecutionSessionTaskLogsResponse`)

See [ListLuauExecutionSessionTaskLogsResponse](#listluauexecutionsessiontasklogsresponse) in Models.

**Response example:**
```json
{
  "luauExecutionSessionTaskLogs": [
    {
      "path": "...",
      "messages": "...",
      "structuredMessages": "..."
    }
  ],
  "nextPageToken": "string"
}
```

**Rate Limits:** perApiKeyOwner: 45/minute

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/cloud/v2/universes/{UNIVERSE_ID}/places/{PLACE_ID}/versions/{VERSION_ID}/luau-execution-sessions/{LUAU_EXECUTION_SESSION_ID}/tasks/{TASK_ID}/logs"
```

## Models

### LuauExecutionSessionTaskBinaryInput

Represents a large binary input that can be given to a
`LuauExecutionSessionTask`.

Each `LuauExecutionSessionTaskBinaryInput` is associated with a presigned URL
which can be used to upload an arbitrary object. After uploading the object,
the path of the `LuauExecutionSessionTaskBinaryInput` can be passed when
creating a `LuauExecutionSessionTask` to make the object available to the
task.

Within the task, the contents of the object are made available within a table
passed as the first argument to the script, with the key `BinaryInput`. The
following example demonstrates how to retrieve the data:

```
local taskInput: LuauExecutionTaskInput = ({...})[1]
local buf: buffer = taskInput.BinaryInput
```

Each `LuauExecutionSessionTaskBinaryInput` is valid for 15 minutes from the
time of creation. Within that time, in desired, you can use it to create
multiple tasks for the same universe.

The uploaded binary object must be no larger than 100 MiB.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `path` | `string` | No | The resource path of the luau execution session task binary input.  Format: `universes/{universe_id}/luau-execution-session-task-binary-inputs/{luau_execution_session_task_binary_input_id}` |
| `size` | `integer` | No |  *(immutable)* The size of the binary input object to be uploaded.  The maximum allowed size is 100 MiB. |
| `uploadUri` | `string` | No | Upload the binary input object using this URI. |

### LuauExecutionSessionTask

A `LuauExecutionSessionTask` ("task" for short) executes a given Luau script
in the context of a specific version of a place.

In a task, physics simulation does not run. Server and local scripts within
the place also do not automatically run.

The script may access and update the data model of the place, including
invoking any module scripts. However, data model changes are local to the
task and cannot be persisted.

The script can also invoke engine APIs that read and/or modify data stored in
the cloud, such as those for DataStores. Exercise caution when using these
APIs.

Scripts can be up to 4 MB in size and run for up to 5 minutes. Scripts that
run for longer than the time limit terminate with an error.

Scripts are executed as-is and do not need to be wrapped in a function.

Scripts can return values (using the Luau `return` keyword). Return values
are serialized to JSON and can be retrieved with the `Get
LuauExecutionSessionTask` API after the task completes. The total size of the
return values after JSON serialization must not exceed 4 MB. If the limit is
exceeded, the task terminates with an error.

If the script raises an unhandled error, the task terminates. The error
information can be retrieved with the `GetLuauExecutionSessionTask` API.

Standard output (generated by the Luau `print` function) can be retrieved
with the `ListLuauExecutionSessionTaskLogs` method after the task completes.
A maximum of 450 KB of logs are retained. If the amount of logs exceeds the
limit, older logs are discarded.

Information about a task is retained for 24 hours after task completion.

At most ten incomplete tasks are allowed per place. Attempting to create more
tasks while the first ten are incomplete results in a HTTP 429 response.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `path` | `string` | No | The resource path of the luau execution session task.  Formats: * `universes/{universe_id}/places/{place_id}/luau-execution-session-tasks/{luau_execution_session_task_id}` * `universes/{universe_id}/places/{place_id}/versions/{place_version_id}/luau-execution-session-tasks/{luau_execution_session_task_id}` * `universes/{universe_id}/places/{place_id}/luau-execution-sessions/{luau_execution_session_id}/tasks/{luau_execution_session_task_id}` * `universes/{universe_id}/places/{place_id}/versions/{place_version_id}/luau-execution-sessions/{luau_execution_session_id}/tasks/{luau_execution_session_task_id}` |
| `createTime` | `string` | No | Time when this task was created. |
| `updateTime` | `string` | No | Time when this task's state last changed. |
| `user` | `string` | No | The user that created the API key that was used to create this task. |
| `state` | `string enum (6 values)` | No | The task's state. See the State enum for information about each possible value.  Possible values:    \| Value \| Description \|   \| --- \| --- \|   \| STATE_UNSPECIFIED \| UNSPECIFIED \|   \| QUEUED \| The Task is waiting to be processed. \|   \| PROCESSING \| The Task has been picked up for processing. \|   \| CANCELLED \| The Task has been stopped by the user. \|   \| COMPLETE \| The Task has finished processing. The output field contains the output. \|   \| FAILED \| The Task failed. The error field contains details about the error. \| Values: STATE_UNSPECIFIED, QUEUED, PROCESSING, CANCELLED, COMPLETE, FAILED |
| `script` | `string` | No |  *(immutable)* The script to be run as part of this task.  For example:  ```luau local x = 3 local y = 4 return x + y ``` |
| `timeout` | `string` | No |  *(immutable)* Limit for how long the script can run.  The task fails if the script does not complete within the specified duration.  Defaults to 5 minutes. |
| `error` | `LuauExecutionSessionTask_Error` | No | Present when the task execution fails. Contains details about the error that caused the failure. |
| `output` | `LuauExecutionSessionTask_Output` | No | Present when the task execution succeeds. Contains the output of the execution. |
| `binaryInput` | `string` | No | Resource path of the binary input to this task. See the documentation for the `LuauExecutionSessionTaskBinaryInput` resource for usage details. |
| `enableBinaryOutput` | `boolean` | No |  *(immutable)* If set to true, allows the task to output a large binary object in addition to standard return values.  If `enable_binary_output` is set to true, the task script must return a `LuauExecutionTaskOutput` (or equivalent table) and no other return values.  Below is example code for doing so:  ```luau local buf: buffer = buffer.create(10) local result: LuauExecutionTaskOutput = {   BinaryOutput = buf,   ReturnValues = { "hello world", 123 } } return result ```  The `BinaryOutput` buffer must be no larger than 256 MiB in size.  The `ReturnValues` array, if given, will be serialized to JSON and made available in the `output` field of the `LuauExecutionSessionTask` resource, similar to regular return values when not using `enable_binary_output`.  The binary output can be fetched from the URI in the `binaryOutputUri` field after the task completes. The `binaryOutputUri` is valid for 15 minutes after task completion. |
| `binaryOutputUri` | `string` | No | URI for the binary output of this task. See the `enableBinaryOutput` field for usage details. |

### ListLuauExecutionSessionTaskLogsResponse

A list of LuauExecutionSessionTaskLogs in the parent collection.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `luauExecutionSessionTaskLogs` | `LuauExecutionSessionTaskLog[]` | No | The LuauExecutionSessionTaskLogs from the specified LuauExecutionSessionTask. |
| `nextPageToken` | `string` | No | A token that you can send as a `pageToken` parameter to retrieve the next page. If this field is omitted, there are no subsequent pages. |