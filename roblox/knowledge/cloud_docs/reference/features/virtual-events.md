---
name: "Game Events"
last_updated: 2026-10-30T19:56:08Z
type: feature
api_base_url: "https://apis.roblox.com"
endpoints: 5
auth: [api-key, oauth2, cookie]
description: "Create and manage scheduled game events for a universe — announce content"
---

# Game Events

Create and manage scheduled game events for a universe — announce content
updates, drops, and live moments, and let players discover and RSVP to them.

Common use cases include:

- **Create an event**: Publish a game event for a universe with a title, schedule, visibility, categories, and thumbnails
- **List and read events**: Page through a universe's game events or fetch a single event, using an optional `fields` mask to trim the payload
- **Update or cancel**: Patch event details or delete a game event

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

### GET `/virtual-events/v3/game-events/{eventId}` [EXPERIMENTAL]

Get a single game event by ID.
Use `?fields=` to request a subset of fields; unknown field names return 400.

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `universe.event:read`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `eventId` | path | `integer` | Yes | Game event ID (from path). |
| `fields` | query | `string` | No | Optional field mask (comma-separated; omit or use * for all fields). |

**Responses:**

- `200`: The requested game event. → `GameEventResponse`
- `400`: Malformed `?fields=` or invalid event ID. → `VirtualEventsApi.ProblemDetails`
- `404`: Event does not exist. → `VirtualEventsApi.ProblemDetails`

**Response fields** (`GameEventResponse`)

See [GameEventResponse](#gameeventresponse) in Models.

**Response example:**
```json
{
  "id": "string",
  "title": "string",
  "displayTitle": "string",
  "subtitle": "string",
  "displaySubtitle": "string",
  "description": "string"
}
```

**Rate Limits:** perApiKeyOwner: 100/minute, perOauth2Authorization: 100/minute

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/virtual-events/v3/game-events/{EVENTID}"
```

### PATCH `/virtual-events/v3/game-events/{eventId}` [EXPERIMENTAL]

Partially update a game event. Only fields present in the request body are changed; omitted or null fields are left
unchanged. Empty body is a no-op and returns the current game event resource.

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `universe.event:write`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `eventId` | path | `integer` | Yes | Game event ID from the route. |

**Request Body:** `application/json-patch+json` — Type: `any`

**Responses:**

- `200`: The updated game event resource. → `GameEventResponse`
- `400`: Validation failure or backend reject. → `VirtualEventsApi.ProblemDetails`
- `401`: Caller is not authenticated. → `VirtualEventsApi.ProblemDetails`
- `403`: Caller can read but lacks edit permission. → `VirtualEventsApi.ProblemDetails`
- `404`: Event not found. → `VirtualEventsApi.ProblemDetails`

**Response fields** (`GameEventResponse`)

See [GameEventResponse](#gameeventresponse) in Models.

**Response example:**
```json
{
  "id": "string",
  "title": "string",
  "displayTitle": "string",
  "subtitle": "string",
  "displaySubtitle": "string",
  "description": "string"
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 20/minute, perOauth2Authorization: 20/minute

**Example:**
```bash
curl -X PATCH -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/virtual-events/v3/game-events/{EVENTID}" \
  -H "Content-Type: application/json" \
  -d '"..."'
```

### DELETE `/virtual-events/v3/game-events/{eventId}` [EXPERIMENTAL]

Permanently delete an existing game event. Returns 204 No Content on success.
Permission is enforced via an explicit pre-check: callers that can read but not edit
receive 403; callers that cannot read receive 404.

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `universe.event:write`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `eventId` | path | `integer` | Yes | Game event ID to delete (from path). |

**Responses:**

- `204`: The event was deleted.
- `401`: Caller is not authenticated. → `VirtualEventsApi.ProblemDetails`
- `403`: Caller can read the event but lacks delete permission. → `VirtualEventsApi.ProblemDetails`
- `404`: Event does not exist or caller cannot see it. → `VirtualEventsApi.ProblemDetails`
- `500`: The backend rejected the delete after the permission pre-check passed. → `VirtualEventsApi.ProblemDetails`

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 20/minute, perOauth2Authorization: 20/minute

**Example:**
```bash
curl -X DELETE -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/virtual-events/v3/game-events/{EVENTID}"
```

### GET `/virtual-events/v3/universes/{universeId}/game-events` [EXPERIMENTAL]

List game events under a universe.
Use `?fields=` to trim the response payload.
Response is always 200 (empty list for unknown universe).

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `universe.event:read`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer` | Yes | Universe that owns the events (from path). |
| `pageSize` | query | `integer` | No | Requested page size. |
| `pageToken` | query | `string` | No | Continuation token from a prior page's `nextPageToken`. |
| `reverse` | query | `boolean` | No | When true, treats `pageToken` as a backward-pagination cursor. |
| `startsBefore` | query | `string` | No | Upper bound on event start time. |
| `startsAfter` | query | `string` | No | Lower bound on event start time. |
| `endsBefore` | query | `string` | No | Upper bound on event end time. |
| `endsAfter` | query | `string` | No | Lower bound on event end time. Defaults to now when neither bound is set. |
| `visibility` | query | `any` | No | Visibility filter. |
| `fields` | query | `string` | No | Field mask (comma-separated; omit or `*` for all fields). |

**Responses:**

- `200`: A page of game events. → `PaginatedGameEventsResponse`
- `400`: Invalid `?fields=`, out-of-range `pageSize`, or bad query parameter. → `VirtualEventsApi.ProblemDetails`

**Response fields** (`PaginatedGameEventsResponse`)

See [PaginatedGameEventsResponse](#paginatedgameeventsresponse) in Models.

**Response example:**
```json
{
  "gameEvents": [
    {
      "id": "...",
      "title": "...",
      "displayTitle": "...",
      "subtitle": "...",
      "displaySubtitle": "...",
      "description": "..."
    }
  ],
  "nextPageToken": "string",
  "previousPageToken": "string"
}
```

**Rate Limits:** perApiKeyOwner: 100/minute, perOauth2Authorization: 100/minute

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/virtual-events/v3/universes/{UNIVERSEID}/game-events"
```

### POST `/virtual-events/v3/universes/{universeId}/game-events` [EXPERIMENTAL]

Create a new game event. Returns the full resource on success.

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `universe.event:write`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer` | Yes | Universe that will own the new event (from path). |

**Request Body:** `application/json-patch+json` — Type: `any`

**Responses:**

- `200`: The newly-created game event resource. → `GameEventResponse`
- `400`: Validation failure or server-side reject (moderation, age requirement, ...). → `VirtualEventsApi.ProblemDetails`
- `401`: Caller is not authenticated. → `VirtualEventsApi.ProblemDetails`
- `403`: Caller lacks permission or quota is exhausted. → `VirtualEventsApi.ProblemDetails`

**Response fields** (`GameEventResponse`)

See [GameEventResponse](#gameeventresponse) in Models.

**Response example:**
```json
{
  "id": "string",
  "title": "string",
  "displayTitle": "string",
  "subtitle": "string",
  "displaySubtitle": "string",
  "description": "string"
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 20/minute, perOauth2Authorization: 20/minute

**Example:**
```bash
curl -X POST -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/virtual-events/v3/universes/{UNIVERSEID}/game-events" \
  -H "Content-Type: application/json" \
  -d '"..."'
```

## Models

### GameEventResponse

v3 game event response. All fields except VirtualEventsApi.Models.V3.Response.GameEventResponse.Id are gated by the `?fields=` mask.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | `string` | No | The unique id of the game event. Always populated. Serialized as a string to preserve precision for clients (event IDs exceed 2^53). |
| `title` | `string` | No |  |
| `displayTitle` | `string` | No | Localized title (caller's locale). Populated only when `displayTitle` is in the mask. |
| `subtitle` | `string` | No |  |
| `displaySubtitle` | `string` | No | Localized subtitle. Populated only when `displaySubtitle` is in the mask. |
| `description` | `string` | No |  |
| `displayDescription` | `string` | No | Localized description. Populated only when `displayDescription` is in the mask. |
| `startTime` | `string` | No |  |
| `endTime` | `string` | No |  |
| `universeId` | `integer` | No |  |
| `placeId` | `integer` | No |  |
| `host` | `any` | No | Host block. VirtualEventsApi.Models.V3.Response.HostResponse.HostName and VirtualEventsApi.Models.V3.Response.HostResponse.HasVerifiedBadge are omitted when host-details resolution failed. |
| `visibility` | `any` | No |  |
| `featuringStatus` | `any` | No |  |
| `tagline` | `string` | No | Tagline for featuring review; visible to curators only when featuring is opted into. |
| `categories` | `CategoryResponse[]` | No |  |
| `thumbnails` | `ThumbnailResponse[]` | No |  |
| `allThumbnailsCreated` | `boolean` | No | Whether all requested thumbnails were successfully persisted. Returned on Create/Update. |
| `userRsvpStatus` | `any` | No | Authenticated caller's RSVP status. Omitted for unauthenticated callers. |
| `createTime` | `string` | No |  |
| `updateTime` | `string` | No |  |

### VirtualEventsApi.ProblemDetails

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `type` | `string` | No |  |
| `title` | `string` | No |  |
| `status` | `integer` | No |  |
| `detail` | `string` | No |  |
| `instance` | `string` | No |  |

### PaginatedGameEventsResponse

Paginated response for v3 LIST. Page tokens are null at the collection boundaries.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `gameEvents` | `GameEventResponse[]` | No |  |
| `nextPageToken` | `string` | No |  |
| `previousPageToken` | `string` | No |  |