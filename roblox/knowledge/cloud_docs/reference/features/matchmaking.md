---
name: "Matchmaking"
last_updated: 2026-10-30T19:56:08Z
type: feature
api_base_url: "https://apis.roblox.com"
endpoints: 33
auth: [api-key, oauth2, cookie]
description: "Configure and manage matchmaking for your experiences"
---

# Matchmaking

Configure and manage matchmaking for your experiences. Matchmaking APIs help you create fair, balanced matches by considering player skill, preferences, and latency.

Common use cases include:

- Player attributes: [Define](#post_matchmaking_api_v1_matchmaking_player_attribute) and [manage](#patch_matchmaking_api_v1_matchmaking_player_attribute__attributeId_) custom player attributes for matching (skill level, preferences, etc.)
- Scoring configuration: [Create](#post_matchmaking_api_v1_matchmaking_scoring_configuration) and [tune](#patch_matchmaking_api_v1_matchmaking_scoring_configuration__scoringConfigurationId_) scoring configurations that determine match quality
- Instance control: [Shut down game instances](#post_matchmaking_api_v1_game_instances_shutdown) for maintenance

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

### GET `/matchmaking-api/v1/client-status` [BETA]

Get the client-status

**Auth:** 

**Request Body:** `application/json-patch+json` — Type: `ClientStatusGetRequest`

See [ClientStatusGetRequest](#clientstatusgetrequest) in Models.

**Request example:**
```json
{
  "browserTrackerId": 0
}
```

**Responses:**

- `200`: Success

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://apis.roblox.com/matchmaking-api/v1/client-status" \
  -H "Content-Type: application/json" \
  -d '{
  "browserTrackerId": 0
}'
```

### POST `/matchmaking-api/v1/client-status` [BETA]

Set the client-status

**Auth:** 

**Request Body:** `application/json-patch+json` — Type: `ClientStatusSetRequest`

See [ClientStatusSetRequest](#clientstatussetrequest) in Models.

**Request example:**
```json
{
  "status": "string",
  "browserTrackerId": 0
}
```

**Responses:**

- `200`: Success

**Example:**
```bash
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://apis.roblox.com/matchmaking-api/v1/client-status" \
  -H "Content-Type: application/json" \
  -d '{
  "status": "string",
  "browserTrackerId": 0
}'
```

### POST `/matchmaking-api/v1/game-instances/forecast-update` [BETA]

Forecast the outcome of launching an update

**Auth:** 

**Request Body:** `application/json-patch+json` — Type: `ForecastUpdateRequest`

See [ForecastUpdateRequest](#forecastupdaterequest) in Models.

**Request example:**
```json
{
  "universeId": 0
}
```

**Responses:**

- `200`: Success → `ForecastUpdateResponse`

**Response fields** (`ForecastUpdateResponse`)

See [ForecastUpdateResponse](#forecastupdateresponse) in Models.

**Response example:**
```json
{
  "placeSummaries": [
    {
      "placeId": "...",
      "playersToBeKicked": "...",
      "totalPlayers": "...",
      "instancesToBeClosed": "...",
      "totalInstances": "...",
      "placeVersion": "..."
    }
  ]
}
```

**Example:**
```bash
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://apis.roblox.com/matchmaking-api/v1/game-instances/forecast-update" \
  -H "Content-Type: application/json" \
  -d '{
  "universeId": 0
}'
```

### GET `/matchmaking-api/v1/game-instances/get-update-status` [BETA]

Get the rollout status of an update

**Auth:** 

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | query | `integer` | No |  |

**Responses:**

- `200`: Success → `GetUpdateStatusResponse`

**Response fields** (`GetUpdateStatusResponse`)

See [GetUpdateStatusResponse](#getupdatestatusresponse) in Models.

**Response example:**
```json
{
  "updateStatusList": [
    {
      "id": "...",
      "universeId": "...",
      "startTime": "...",
      "closeOldVersionsOnly": "...",
      "bleedOffEndTime": "...",
      "placeUpdateStatuses": "..."
    }
  ]
}
```

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://apis.roblox.com/matchmaking-api/v1/game-instances/get-update-status"
```

### POST `/matchmaking-api/v1/game-instances/launch-update` [BETA]

Launch a game update

**Auth:** 

**Request Body:** `application/json-patch+json` — Type: `LaunchUpdateRequest`

See [LaunchUpdateRequest](#launchupdaterequest) in Models.

**Request example:**
```json
{
  "universeId": 0,
  "placeIds": [
    0
  ],
  "closeOldVersionsOnly": false,
  "bleedOffServers": false,
  "bleedOffDurationMinutes": 0,
  "placeIdToVersions": "..."
}
```

**Responses:**

- `200`: Success → `LaunchUpdateResponse`

**Response fields** (`LaunchUpdateResponse`)

See [LaunchUpdateResponse](#launchupdateresponse) in Models.

**Response example:**
```json
{
  "updateId": "string",
  "numPlayersToBeKicked": 0,
  "instancesToBeClosed": 0
}
```

**Example:**
```bash
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://apis.roblox.com/matchmaking-api/v1/game-instances/launch-update" \
  -H "Content-Type: application/json" \
  -d '{
  "universeId": 0,
  "placeIds": [
    0
  ],
  "closeOldVersionsOnly": false,
  "bleedOffServers": false,
  "bleedOffDurationMinutes": 0,
  "placeIdToVersions": "..."
}'
```

### POST `/matchmaking-api/v1/game-instances/shutdown` [BETA]

Shutdown game instances.

**Auth:** Cookie (`.ROBLOSECURITY`)

**Request Body:** `application/json-patch+json` — Type: `ShutdownGameInstancesRequest`

See [ShutdownGameInstancesRequest](#shutdowngameinstancesrequest) in Models.

**Request example:**
```json
{
  "placeId": 0,
  "privateServerId": 0,
  "gameId": "string"
}
```

**Responses:**

- `200`: Success → `ShutdownGameInstancesResponse`

**Response fields** (`ShutdownGameInstancesResponse`)

See [ShutdownGameInstancesResponse](#shutdowngameinstancesresponse) in Models.

**Response example:**
```json
{
  "placeId": 0,
  "privateServerId": 0,
  "gameId": "string"
}
```

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://apis.roblox.com/matchmaking-api/v1/game-instances/shutdown" \
  -H "Content-Type: application/json" \
  -d '{
  "placeId": 0,
  "privateServerId": 0,
  "gameId": "string"
}'
```

### POST `/matchmaking-api/v1/game-instances/shutdown-all` [BETA]

Shutdown all game instances.

**Auth:** Cookie (`.ROBLOSECURITY`)

**Request Body:** `multipart/form-data` — Type: `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `PlaceId` | `integer` | No | The place ID to shut down. |
| `ReplaceInstances` | `boolean` | No | Whether to replace instances or not. |

**Request example:**
```json
{
  "PlaceId": 0,
  "ReplaceInstances": false
}
```

**Responses:**

- `200`: Success → `ShutdownAllGameInstancesResponse`

**Response fields** (`ShutdownAllGameInstancesResponse`)

See [ShutdownAllGameInstancesResponse](#shutdownallgameinstancesresponse) in Models.

**Response example:**
```json
{
  "placeId": 0,
  "replaceInstances": false
}
```

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://apis.roblox.com/matchmaking-api/v1/game-instances/shutdown-all" \
  -F "PlaceId=0" \
  -F "ReplaceInstances=false"
```

### POST `/matchmaking-api/v1/matchmaking/player-attribute` [BETA]

Create a PlayerAttributeDefinition.

**Auth:** 

**Request Body:** `application/json-patch+json` — Type: `CreateMatchmakingPlayerAttributeDefinitionRequest`

See [CreateMatchmakingPlayerAttributeDefinitionRequest](#creatematchmakingplayerattributedefinitionrequest) in Models.

**Request example:**
```json
{
  "universeId": 0,
  "name": "string",
  "dataType": "Invalid",
  "defaultValue": {
    "boolValue": false,
    "numericValue": 0,
    "stringValue": "string",
    "type": "Invalid"
  },
  "attributeValueLocation": {
    "locationCase": "Invalid",
    "dataStoreLocation": {
      "dataStoreName": "...",
      "scope": "...",
      "keyTemplate": "...",
      "valuePath": "..."
    }
  }
}
```

**Responses:**

- `200`: Success → `CreateMatchmakingPlayerAttributeDefinitionResponse`

**Response fields** (`CreateMatchmakingPlayerAttributeDefinitionResponse`)

See [CreateMatchmakingPlayerAttributeDefinitionResponse](#creatematchmakingplayerattributedefinitionresponse) in Models.

**Response example:**
```json
{
  "playerAttributeDefinition": {
    "id": "string",
    "universeId": 0,
    "name": "string",
    "dataType": "Invalid",
    "defaultValue": {
      "boolValue": "...",
      "numericValue": "...",
      "stringValue": "...",
      "type": "..."
    },
    "attributeValueLocation": {
      "locationCase": "...",
      "dataStoreLocation": "..."
    }
  }
}
```

**Example:**
```bash
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://apis.roblox.com/matchmaking-api/v1/matchmaking/player-attribute" \
  -H "Content-Type: application/json" \
  -d '{"universeId":0,"name":"string","dataType":"Invalid","defaultValue":{"boolValue":false,"numericValue":0,"stringValue":"string","type":"Invalid"},"attributeValueLocation":{"locationCase":"Invalid","dataStoreLocation":{"dataStoreName":"...","scope":"...","keyTemplate":"...","valuePath":"..."}}}'
```

### PATCH `/matchmaking-api/v1/matchmaking/player-attribute/{attributeId}` [BETA]

Update the PlayerAttributeDefinition specified by attributeId.

**Auth:** 

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `attributeId` | path | `string` | Yes |  |

**Request Body:** `application/json-patch+json` — Type: `UpdateMatchmakingPlayerAttributeDefinitionRequest`

See [UpdateMatchmakingPlayerAttributeDefinitionRequest](#updatematchmakingplayerattributedefinitionrequest) in Models.

**Request example:**
```json
{
  "attributeId": "string",
  "defaultValue": {
    "boolValue": false,
    "numericValue": 0,
    "stringValue": "string",
    "type": "Invalid"
  },
  "attributeValueLocation": {
    "locationCase": "Invalid",
    "dataStoreLocation": {
      "dataStoreName": "...",
      "scope": "...",
      "keyTemplate": "...",
      "valuePath": "..."
    }
  }
}
```

**Responses:**

- `200`: Success → `UpdateMatchmakingPlayerAttributeDefinitionResponse`

**Response fields** (`UpdateMatchmakingPlayerAttributeDefinitionResponse`)

See [UpdateMatchmakingPlayerAttributeDefinitionResponse](#updatematchmakingplayerattributedefinitionresponse) in Models.

**Response example:**
```json
{
  "playerAttributeDefinition": {
    "id": "string",
    "universeId": 0,
    "name": "string",
    "dataType": "Invalid",
    "defaultValue": {
      "boolValue": "...",
      "numericValue": "...",
      "stringValue": "...",
      "type": "..."
    },
    "attributeValueLocation": {
      "locationCase": "...",
      "dataStoreLocation": "..."
    }
  }
}
```

**Example:**
```bash
curl -X PATCH -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://apis.roblox.com/matchmaking-api/v1/matchmaking/player-attribute/{ATTRIBUTEID}" \
  -H "Content-Type: application/json" \
  -d '{"attributeId":"string","defaultValue":{"boolValue":false,"numericValue":0,"stringValue":"string","type":"Invalid"},"attributeValueLocation":{"locationCase":"Invalid","dataStoreLocation":{"dataStoreName":"...","scope":"...","keyTemplate":"...","valuePath":"..."}}}'
```

### DELETE `/matchmaking-api/v1/matchmaking/player-attribute/{attributeId}` [BETA]

Delete the PlayerAttributeDefinition specified by attributeId.

**Auth:** 

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `attributeId` | path | `string` | Yes |  |

**Responses:**

- `200`: Success → `DeleteMatchmakingPlayerAttributeDefinitionResponse`

**Response fields** (`DeleteMatchmakingPlayerAttributeDefinitionResponse`)

See [DeleteMatchmakingPlayerAttributeDefinitionResponse](#deletematchmakingplayerattributedefinitionresponse) in Models.

**Example:**
```bash
curl -X DELETE -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://apis.roblox.com/matchmaking-api/v1/matchmaking/player-attribute/{ATTRIBUTEID}"
```

### GET `/matchmaking-api/v1/matchmaking/player-attributes/{universeId}` [BETA]

List all PlayerAttributeDefinitions of a universe.

**Auth:** 

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer` | Yes |  |

**Responses:**

- `200`: Success → `ListMatchmakingPlayerAttributeDefinitionsResponse`

**Response fields** (`ListMatchmakingPlayerAttributeDefinitionsResponse`)

See [ListMatchmakingPlayerAttributeDefinitionsResponse](#listmatchmakingplayerattributedefinitionsresponse) in Models.

**Response example:**
```json
{
  "playerAttributeSchema": [
    {
      "id": "...",
      "universeId": "...",
      "name": "...",
      "dataType": "...",
      "defaultValue": "...",
      "attributeValueLocation": "..."
    }
  ]
}
```

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://apis.roblox.com/matchmaking-api/v1/matchmaking/player-attributes/{UNIVERSEID}"
```

### POST `/matchmaking-api/v1/matchmaking/scoring-configuration` [BETA]

Creates a matchmaking scoring configuration.

**Auth:** 

**Request Body:** `application/json-patch+json` — Type: `CreateMatchmakingScoringConfigurationRequest`

See [CreateMatchmakingScoringConfigurationRequest](#creatematchmakingscoringconfigurationrequest) in Models.

**Request example:**
```json
{
  "universeId": 0,
  "name": "string",
  "matchmakingSignalWeights": {
    "Invalid": 0,
    "Occupancy": 0,
    "Age": 0,
    "Language": 0,
    "Latency": 0,
    "PreferredPlayers": 0
  },
  "customSignalWeights": "...",
  "template": "NotApplicable"
}
```

**Responses:**

- `200`: Success → `CreateMatchmakingScoringConfigurationResponse`

**Response fields** (`CreateMatchmakingScoringConfigurationResponse`)

See [CreateMatchmakingScoringConfigurationResponse](#creatematchmakingscoringconfigurationresponse) in Models.

**Response example:**
```json
{
  "scoringConfiguration": {
    "id": "string",
    "name": "string",
    "signalWeights": {
      "Invalid": "...",
      "Occupancy": "...",
      "Age": "...",
      "Language": "...",
      "Latency": "...",
      "PreferredPlayers": "..."
    },
    "customSignals": "...",
    "createdTime": "2024-01-01T00:00:00Z",
    "updatedTime": "2024-01-01T00:00:00Z"
  }
}
```

**Example:**
```bash
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://apis.roblox.com/matchmaking-api/v1/matchmaking/scoring-configuration" \
  -H "Content-Type: application/json" \
  -d '{
  "universeId": 0,
  "name": "string",
  "matchmakingSignalWeights": {
    "Invalid": 0,
    "Occupancy": 0,
    "Age": 0,
    "Language": 0,
    "Latency": 0,
    "PreferredPlayers": 0
  },
  "customSignalWeights": "...",
  "template": "NotApplicable"
}'
```

### GET `/matchmaking-api/v1/matchmaking/scoring-configuration/default-weights` [BETA]

**Auth:** 

**Responses:**

- `200`: Success → `GetMatchmakingScoringDefaultWeightsResponse`

**Response fields** (`GetMatchmakingScoringDefaultWeightsResponse`)

See [GetMatchmakingScoringDefaultWeightsResponse](#getmatchmakingscoringdefaultweightsresponse) in Models.

**Response example:**
```json
{
  "weights": {
    "Invalid": 0,
    "Occupancy": 0,
    "Age": 0,
    "Language": 0,
    "Latency": 0,
    "PreferredPlayers": 0
  }
}
```

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://apis.roblox.com/matchmaking-api/v1/matchmaking/scoring-configuration/default-weights"
```

### GET `/matchmaking-api/v1/matchmaking/scoring-configuration/generate-mock-servers` [BETA]

**Auth:** 

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `count` | query | `integer` | No |  |
| `capacity` | query | `integer` | No |  |
| `playerAge` | query | `integer` | No |  |
| `playerPlayHistory` | query | `number` | No |  |
| `isPlayerVoiceChatEnabled` | query | `boolean` | No |  |

**Responses:**

- `200`: Success → `GenerateMockServerSignalValuesResponse`

**Response fields** (`GenerateMockServerSignalValuesResponse`)

See [GenerateMockServerSignalValuesResponse](#generatemockserversignalvaluesresponse) in Models.

**Response example:**
```json
{
  "exampleGameSignalValues": [
    {
      "capacity": "...",
      "occupancy": "...",
      "hasPreferredPlayers": "...",
      "playerAge": "...",
      "serverAveragePlayerAge": "...",
      "commonLanguagePlayers": "..."
    }
  ]
}
```

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://apis.roblox.com/matchmaking-api/v1/matchmaking/scoring-configuration/generate-mock-servers"
```

### POST `/matchmaking-api/v1/matchmaking/scoring-configuration/place` [BETA]

Sets a matchmaking scoring configuration for a place.

**Auth:** 

**Request Body:** `application/json-patch+json` — Type: `SetPlaceMatchmakingScoringConfigurationRequest`

See [SetPlaceMatchmakingScoringConfigurationRequest](#setplacematchmakingscoringconfigurationrequest) in Models.

**Request example:**
```json
{
  "placeId": 0,
  "scoringConfigurationId": "string"
}
```

**Responses:**

- `200`: Success → `SetMatchmakingScoringConfigurationResponse`

**Response fields** (`SetMatchmakingScoringConfigurationResponse`)

See [SetMatchmakingScoringConfigurationResponse](#setmatchmakingscoringconfigurationresponse) in Models.

**Response example:**
```json
{
  "scoringConfiguration": {
    "id": "string",
    "name": "string",
    "signalWeights": {
      "Invalid": "...",
      "Occupancy": "...",
      "Age": "...",
      "Language": "...",
      "Latency": "...",
      "PreferredPlayers": "..."
    },
    "customSignals": "...",
    "createdTime": "2024-01-01T00:00:00Z",
    "updatedTime": "2024-01-01T00:00:00Z"
  }
}
```

**Example:**
```bash
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://apis.roblox.com/matchmaking-api/v1/matchmaking/scoring-configuration/place" \
  -H "Content-Type: application/json" \
  -d '{
  "placeId": 0,
  "scoringConfigurationId": "string"
}'
```

### DELETE `/matchmaking-api/v1/matchmaking/scoring-configuration/place/{placeId}` [BETA]

Removes the matchmaking scoring configuration for a place.

**Auth:** 

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `placeId` | path | `integer` | Yes |  |

**Responses:**

- `200`: Success → `RemovePlaceMatchmakingScoringConfigurationResponse`

**Response fields** (`RemovePlaceMatchmakingScoringConfigurationResponse`)

See [RemovePlaceMatchmakingScoringConfigurationResponse](#removeplacematchmakingscoringconfigurationresponse) in Models.

**Example:**
```bash
curl -X DELETE -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://apis.roblox.com/matchmaking-api/v1/matchmaking/scoring-configuration/place/{PLACEID}"
```

### GET `/matchmaking-api/v1/matchmaking/scoring-configuration/{scoringConfigurationId}` [BETA]

Updates a matchmaking scoring configuration.

**Auth:** 

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `scoringConfigurationId` | path | `string` | Yes |  |

**Responses:**

- `200`: Success → `GetMatchmakingScoringConfigurationResponse`

**Response fields** (`GetMatchmakingScoringConfigurationResponse`)

See [GetMatchmakingScoringConfigurationResponse](#getmatchmakingscoringconfigurationresponse) in Models.

**Response example:**
```json
{
  "scoringConfiguration": {
    "id": "string",
    "name": "string",
    "signalWeights": {
      "Invalid": "...",
      "Occupancy": "...",
      "Age": "...",
      "Language": "...",
      "Latency": "...",
      "PreferredPlayers": "..."
    },
    "customSignals": "...",
    "createdTime": "2024-01-01T00:00:00Z",
    "updatedTime": "2024-01-01T00:00:00Z"
  }
}
```

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://apis.roblox.com/matchmaking-api/v1/matchmaking/scoring-configuration/{SCORINGCONFIGURATIONID}"
```

### PATCH `/matchmaking-api/v1/matchmaking/scoring-configuration/{scoringConfigurationId}` [BETA]

Updates a matchmaking scoring configuration.

**Auth:** 

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `scoringConfigurationId` | path | `string` | Yes |  |

**Request Body:** `application/json-patch+json` — Type: `UpdateMatchmakingScoringConfigurationRequest`

See [UpdateMatchmakingScoringConfigurationRequest](#updatematchmakingscoringconfigurationrequest) in Models.

**Request example:**
```json
{
  "scoringConfigurationId": "string",
  "name": "string",
  "matchmakingSignalWeights": {
    "Invalid": 0,
    "Occupancy": 0,
    "Age": 0,
    "Language": 0,
    "Latency": 0,
    "PreferredPlayers": 0
  },
  "customSignalWeights": "..."
}
```

**Responses:**

- `200`: Success → `UpdateMatchmakingScoringConfigurationResponse`

**Response fields** (`UpdateMatchmakingScoringConfigurationResponse`)

See [UpdateMatchmakingScoringConfigurationResponse](#updatematchmakingscoringconfigurationresponse) in Models.

**Response example:**
```json
{
  "scoringConfiguration": {
    "id": "string",
    "name": "string",
    "signalWeights": {
      "Invalid": "...",
      "Occupancy": "...",
      "Age": "...",
      "Language": "...",
      "Latency": "...",
      "PreferredPlayers": "..."
    },
    "customSignals": "...",
    "createdTime": "2024-01-01T00:00:00Z",
    "updatedTime": "2024-01-01T00:00:00Z"
  }
}
```

**Example:**
```bash
curl -X PATCH -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://apis.roblox.com/matchmaking-api/v1/matchmaking/scoring-configuration/{SCORINGCONFIGURATIONID}" \
  -H "Content-Type: application/json" \
  -d '{
  "scoringConfigurationId": "string",
  "name": "string",
  "matchmakingSignalWeights": {
    "Invalid": 0,
    "Occupancy": 0,
    "Age": 0,
    "Language": 0,
    "Latency": 0,
    "PreferredPlayers": 0
  },
  "customSignalWeights": "..."
}'
```

### DELETE `/matchmaking-api/v1/matchmaking/scoring-configuration/{scoringConfigurationId}` [BETA]

Deletes a matchmaking scoring configuration.

**Auth:** 

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `scoringConfigurationId` | path | `string` | Yes |  |

**Responses:**

- `200`: Success → `DeleteMatchmakingScoringConfigurationResponse`

**Response fields** (`DeleteMatchmakingScoringConfigurationResponse`)

See [DeleteMatchmakingScoringConfigurationResponse](#deletematchmakingscoringconfigurationresponse) in Models.

**Example:**
```bash
curl -X DELETE -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://apis.roblox.com/matchmaking-api/v1/matchmaking/scoring-configuration/{SCORINGCONFIGURATIONID}"
```

### POST `/matchmaking-api/v1/matchmaking/scoring-configuration/{scoringConfigurationId}/signals` [BETA]

Creates a matchmaking scoring configuration signal.

**Auth:** 

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `scoringConfigurationId` | path | `string` | Yes |  |

**Request Body:** `application/json-patch+json` — Type: `CreateCustomMatchmakingSignalRequest`

See [CreateCustomMatchmakingSignalRequest](#createcustommatchmakingsignalrequest) in Models.

**Request example:**
```json
{
  "scoringConfigurationId": "string",
  "signalConfiguration": {
    "name": "string",
    "weight": 0,
    "customSignalType": "Invalid",
    "playerCategoricalSignalConfiguration": {
      "playerAttribute": "...",
      "curveType": "..."
    },
    "serverCategoricalSignalConfiguration": {
      "serverAttribute": "...",
      "comparisonType": "...",
      "playerAttribute": "...",
      "constantValue": "..."
    },
    "serverNumericalSignalConfiguration": {
      "serverAttribute": "...",
      "comparisonType": "...",
      "maxRelevantDifference": "...",
      "constantValue": "...",
      "playerAttribute": "..."
    }
  }
}
```

**Responses:**

- `200`: Success → `CreateCustomMatchmakingSignalResponse`

**Response fields** (`CreateCustomMatchmakingSignalResponse`)

See [CreateCustomMatchmakingSignalResponse](#createcustommatchmakingsignalresponse) in Models.

**Response example:**
```json
{
  "scoringConfiguration": {
    "id": "string",
    "name": "string",
    "signalWeights": {
      "Invalid": "...",
      "Occupancy": "...",
      "Age": "...",
      "Language": "...",
      "Latency": "...",
      "PreferredPlayers": "..."
    },
    "customSignals": "...",
    "createdTime": "2024-01-01T00:00:00Z",
    "updatedTime": "2024-01-01T00:00:00Z"
  }
}
```

**Example:**
```bash
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://apis.roblox.com/matchmaking-api/v1/matchmaking/scoring-configuration/{SCORINGCONFIGURATIONID}/signals" \
  -H "Content-Type: application/json" \
  -d '{"scoringConfigurationId":"string","signalConfiguration":{"name":"string","weight":0,"customSignalType":"Invalid","playerCategoricalSignalConfiguration":{"playerAttribute":"...","curveType":"..."},"serverCategoricalSignalConfiguration":{"serverAttribute":"...","comparisonType":"...","playerAttribute":"...","constantValue":"..."},"serverNumericalSignalConfiguration":{"serverAttribute":"...","comparisonType":"...","maxRelevantDifference":"...","constantValue":"...","playerAttribute":"..."}}}'
```

### PATCH `/matchmaking-api/v1/matchmaking/scoring-configuration/{scoringConfigurationId}/signals/{signalName}` [BETA]

Updates a matchmaking scoring configuration signal.

**Auth:** 

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `scoringConfigurationId` | path | `string` | Yes |  |
| `signalName` | path | `string` | Yes |  |

**Request Body:** `application/json-patch+json` — Type: `UpdateCustomMatchmakingSignalRequest`

See [UpdateCustomMatchmakingSignalRequest](#updatecustommatchmakingsignalrequest) in Models.

**Request example:**
```json
{
  "scoringConfigurationId": "string",
  "signalConfiguration": {
    "name": "string",
    "weight": 0,
    "customSignalType": "Invalid",
    "playerCategoricalSignalConfiguration": {
      "playerAttribute": "...",
      "curveType": "..."
    },
    "serverCategoricalSignalConfiguration": {
      "serverAttribute": "...",
      "comparisonType": "...",
      "playerAttribute": "...",
      "constantValue": "..."
    },
    "serverNumericalSignalConfiguration": {
      "serverAttribute": "...",
      "comparisonType": "...",
      "maxRelevantDifference": "...",
      "constantValue": "...",
      "playerAttribute": "..."
    }
  }
}
```

**Responses:**

- `200`: Success → `UpdateCustomMatchmakingSignalResponse`

**Response fields** (`UpdateCustomMatchmakingSignalResponse`)

See [UpdateCustomMatchmakingSignalResponse](#updatecustommatchmakingsignalresponse) in Models.

**Response example:**
```json
{
  "scoringConfiguration": {
    "id": "string",
    "name": "string",
    "signalWeights": {
      "Invalid": "...",
      "Occupancy": "...",
      "Age": "...",
      "Language": "...",
      "Latency": "...",
      "PreferredPlayers": "..."
    },
    "customSignals": "...",
    "createdTime": "2024-01-01T00:00:00Z",
    "updatedTime": "2024-01-01T00:00:00Z"
  }
}
```

**Example:**
```bash
curl -X PATCH -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://apis.roblox.com/matchmaking-api/v1/matchmaking/scoring-configuration/{SCORINGCONFIGURATIONID}/signals/{SIGNALNAME}" \
  -H "Content-Type: application/json" \
  -d '{"scoringConfigurationId":"string","signalConfiguration":{"name":"string","weight":0,"customSignalType":"Invalid","playerCategoricalSignalConfiguration":{"playerAttribute":"...","curveType":"..."},"serverCategoricalSignalConfiguration":{"serverAttribute":"...","comparisonType":"...","playerAttribute":"...","constantValue":"..."},"serverNumericalSignalConfiguration":{"serverAttribute":"...","comparisonType":"...","maxRelevantDifference":"...","constantValue":"...","playerAttribute":"..."}}}'
```

### DELETE `/matchmaking-api/v1/matchmaking/scoring-configuration/{scoringConfigurationId}/signals/{signalName}` [BETA]

Deletes a matchmaking scoring configuration custom signal.

**Auth:** 

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `scoringConfigurationId` | path | `string` | Yes |  |
| `signalName` | path | `string` | Yes |  |

**Responses:**

- `200`: Success → `DeleteCustomMatchmakingSignalResponse`

**Response fields** (`DeleteCustomMatchmakingSignalResponse`)

See [DeleteCustomMatchmakingSignalResponse](#deletecustommatchmakingsignalresponse) in Models.

**Response example:**
```json
{
  "scoringConfiguration": {
    "id": "string",
    "name": "string",
    "signalWeights": {
      "Invalid": "...",
      "Occupancy": "...",
      "Age": "...",
      "Language": "...",
      "Latency": "...",
      "PreferredPlayers": "..."
    },
    "customSignals": "...",
    "createdTime": "2024-01-01T00:00:00Z",
    "updatedTime": "2024-01-01T00:00:00Z"
  }
}
```

**Example:**
```bash
curl -X DELETE -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://apis.roblox.com/matchmaking-api/v1/matchmaking/scoring-configuration/{SCORINGCONFIGURATIONID}/signals/{SIGNALNAME}"
```

### GET `/matchmaking-api/v1/matchmaking/scoring-configurations/{universeId}` [BETA]

List all matchmaking scoring configurations for a universe.

**Auth:** 

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer` | Yes |  |

**Responses:**

- `200`: Success → `ListMatchmakingScoringConfigurationsResponse`

**Response fields** (`ListMatchmakingScoringConfigurationsResponse`)

See [ListMatchmakingScoringConfigurationsResponse](#listmatchmakingscoringconfigurationsresponse) in Models.

**Response example:**
```json
{
  "scoringConfigurations": [
    {
      "id": "...",
      "name": "...",
      "signalWeights": "...",
      "customSignals": "...",
      "createdTime": "...",
      "updatedTime": "..."
    }
  ]
}
```

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://apis.roblox.com/matchmaking-api/v1/matchmaking/scoring-configurations/{UNIVERSEID}"
```

### GET `/matchmaking-api/v1/matchmaking/scoring-configurations/{universeId}/places` [BETA]

List all places with a matchmaking scoring configuration for a universe.

**Auth:** 

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer` | Yes |  |

**Responses:**

- `200`: Success → `ListPlaceMatchmakingScoringConfigurationsResponse`

**Response fields** (`ListPlaceMatchmakingScoringConfigurationsResponse`)

See [ListPlaceMatchmakingScoringConfigurationsResponse](#listplacematchmakingscoringconfigurationsresponse) in Models.

**Response example:**
```json
{
  "placeScoringConfigurations": "..."
}
```

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://apis.roblox.com/matchmaking-api/v1/matchmaking/scoring-configurations/{UNIVERSEID}/places"
```

### POST `/matchmaking-api/v1/matchmaking/server-attribute` [BETA]

Create a ServerAttributeDefinition.

**Auth:** 

**Request Body:** `application/json-patch+json` — Type: `CreateMatchmakingServerAttributeDefinitionRequest`

See [CreateMatchmakingServerAttributeDefinitionRequest](#creatematchmakingserverattributedefinitionrequest) in Models.

**Request example:**
```json
{
  "universeId": 0,
  "name": "string",
  "dataType": "Invalid",
  "defaultValue": {
    "sourceCase": "Invalid",
    "constant": {
      "boolValue": "...",
      "numericValue": "...",
      "stringValue": "...",
      "type": "..."
    },
    "playerAttributeReference": {
      "id": "..."
    }
  }
}
```

**Responses:**

- `200`: Success → `CreateMatchmakingServerAttributeDefinitionResponse`

**Response fields** (`CreateMatchmakingServerAttributeDefinitionResponse`)

See [CreateMatchmakingServerAttributeDefinitionResponse](#creatematchmakingserverattributedefinitionresponse) in Models.

**Response example:**
```json
{
  "playerAttributeDefinition": {
    "id": "string",
    "universeId": 0,
    "name": "string",
    "dataType": "Invalid",
    "defaultValue": {
      "sourceCase": "...",
      "constant": "...",
      "playerAttributeReference": "..."
    },
    "createdTime": "2024-01-01T00:00:00Z"
  }
}
```

**Example:**
```bash
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://apis.roblox.com/matchmaking-api/v1/matchmaking/server-attribute" \
  -H "Content-Type: application/json" \
  -d '{"universeId":0,"name":"string","dataType":"Invalid","defaultValue":{"sourceCase":"Invalid","constant":{"boolValue":"...","numericValue":"...","stringValue":"...","type":"..."},"playerAttributeReference":{"id":"..."}}}'
```

### PATCH `/matchmaking-api/v1/matchmaking/server-attribute/{attributeId}` [BETA]

Update the ServerAttributeDefinition specified by attributeId.

**Auth:** 

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `attributeId` | path | `string` | Yes |  |

**Request Body:** `application/json-patch+json` — Type: `UpdateMatchmakingServerAttributeDefinitionRequest`

See [UpdateMatchmakingServerAttributeDefinitionRequest](#updatematchmakingserverattributedefinitionrequest) in Models.

**Request example:**
```json
{
  "attributeId": "string",
  "defaultValue": {
    "sourceCase": "Invalid",
    "constant": {
      "boolValue": "...",
      "numericValue": "...",
      "stringValue": "...",
      "type": "..."
    },
    "playerAttributeReference": {
      "id": "..."
    }
  }
}
```

**Responses:**

- `200`: Success → `UpdateMatchmakingServerAttributeDefinitionResponse`

**Response fields** (`UpdateMatchmakingServerAttributeDefinitionResponse`)

See [UpdateMatchmakingServerAttributeDefinitionResponse](#updatematchmakingserverattributedefinitionresponse) in Models.

**Response example:**
```json
{
  "playerAttributeDefinition": {
    "id": "string",
    "universeId": 0,
    "name": "string",
    "dataType": "Invalid",
    "defaultValue": {
      "sourceCase": "...",
      "constant": "...",
      "playerAttributeReference": "..."
    },
    "createdTime": "2024-01-01T00:00:00Z"
  }
}
```

**Example:**
```bash
curl -X PATCH -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://apis.roblox.com/matchmaking-api/v1/matchmaking/server-attribute/{ATTRIBUTEID}" \
  -H "Content-Type: application/json" \
  -d '{
  "attributeId": "string",
  "defaultValue": {
    "sourceCase": "Invalid",
    "constant": {
      "boolValue": "...",
      "numericValue": "...",
      "stringValue": "...",
      "type": "..."
    },
    "playerAttributeReference": {
      "id": "..."
    }
  }
}'
```

### DELETE `/matchmaking-api/v1/matchmaking/server-attribute/{attributeId}` [BETA]

Delete the ServerAttributeDefinition specified by attributeId.

**Auth:** 

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `attributeId` | path | `string` | Yes |  |

**Responses:**

- `200`: Success → `DeleteMatchmakingServerAttributeDefinitionResponse`

**Response fields** (`DeleteMatchmakingServerAttributeDefinitionResponse`)

See [DeleteMatchmakingServerAttributeDefinitionResponse](#deletematchmakingserverattributedefinitionresponse) in Models.

**Example:**
```bash
curl -X DELETE -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://apis.roblox.com/matchmaking-api/v1/matchmaking/server-attribute/{ATTRIBUTEID}"
```

### GET `/matchmaking-api/v1/matchmaking/server-attributes/{universeId}` [BETA]

List all ServerAttributeDefinitions of a universe.

**Auth:** 

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer` | Yes |  |

**Responses:**

- `200`: Success → `ListMatchmakingServerAttributeDefinitionsResponse`

**Response fields** (`ListMatchmakingServerAttributeDefinitionsResponse`)

See [ListMatchmakingServerAttributeDefinitionsResponse](#listmatchmakingserverattributedefinitionsresponse) in Models.

**Response example:**
```json
{
  "serverAttributeSchema": [
    {
      "id": "...",
      "universeId": "...",
      "name": "...",
      "dataType": "...",
      "defaultValue": "...",
      "createdTime": "..."
    }
  ]
}
```

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://apis.roblox.com/matchmaking-api/v1/matchmaking/server-attributes/{UNIVERSEID}"
```

### GET `/matchmaking-api/v1/matchmaking/universe/{universeId}/feature-flags` [BETA]

Gets feature flags for a customized matchmaking for a given universe.

**Auth:** 

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer` | Yes |  |

**Responses:**

- `200`: Success → `GetMatchmakingCustomizationFeatureFlagsResponse`

**Response fields** (`GetMatchmakingCustomizationFeatureFlagsResponse`)

See [GetMatchmakingCustomizationFeatureFlagsResponse](#getmatchmakingcustomizationfeatureflagsresponse) in Models.

**Response example:**
```json
{
  "featureFlags": {
    "isMatchmakingCustomizationAllowed": false,
    "isMatchmakingCustomizationExperimentsAllowed": false,
    "isMatchmakingTextChatSignalEnabled": false
  }
}
```

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://apis.roblox.com/matchmaking-api/v1/matchmaking/universe/{UNIVERSEID}/feature-flags"
```

### GET `/matchmaking-api/v1/matchmaking/universe/{universeId}/start-place` [BETA]

Gets the start place override for a universe.

**Auth:** 

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer` | Yes |  |

**Responses:**

- `200`: Success → `GetStartPlaceOverrideResponse`

**Response fields** (`GetStartPlaceOverrideResponse`)

See [GetStartPlaceOverrideResponse](#getstartplaceoverrideresponse) in Models.

**Response example:**
```json
{
  "dataStoreLocation": {
    "dataStoreName": "string",
    "scope": "string",
    "keyTemplate": "string",
    "valuePath": "string"
  }
}
```

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://apis.roblox.com/matchmaking-api/v1/matchmaking/universe/{UNIVERSEID}/start-place"
```

### POST `/matchmaking-api/v1/matchmaking/universe/{universeId}/start-place` [BETA]

Sets (creates or updates) the start place override for a universe.

**Auth:** 

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer` | Yes |  |

**Request Body:** `application/json-patch+json` — Type: `SetStartPlaceOverrideRequestBody`

See [SetStartPlaceOverrideRequestBody](#setstartplaceoverriderequestbody) in Models.

**Request example:**
```json
{
  "dataStoreLocation": {
    "dataStoreName": "string",
    "scope": "string",
    "keyTemplate": "string",
    "valuePath": "string"
  }
}
```

**Responses:**

- `200`: Success → `SetStartPlaceOverrideResponse`

**Response fields** (`SetStartPlaceOverrideResponse`)

See [SetStartPlaceOverrideResponse](#setstartplaceoverrideresponse) in Models.

**Example:**
```bash
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://apis.roblox.com/matchmaking-api/v1/matchmaking/universe/{UNIVERSEID}/start-place" \
  -H "Content-Type: application/json" \
  -d '{
  "dataStoreLocation": {
    "dataStoreName": "string",
    "scope": "string",
    "keyTemplate": "string",
    "valuePath": "string"
  }
}'
```

### DELETE `/matchmaking-api/v1/matchmaking/universe/{universeId}/start-place` [BETA]

Deletes the start place override for a universe.

**Auth:** 

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer` | Yes |  |

**Responses:**

- `200`: Success → `DeleteStartPlaceOverrideResponse`

**Response fields** (`DeleteStartPlaceOverrideResponse`)

See [DeleteStartPlaceOverrideResponse](#deletestartplaceoverrideresponse) in Models.

**Example:**
```bash
curl -X DELETE -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://apis.roblox.com/matchmaking-api/v1/matchmaking/universe/{UNIVERSEID}/start-place"
```

### GET `/matchmaking-api/v1/matchmaking/universe/{universeId}/start-place/test` [BETA]

Tests a user's saved start place in a universe against the place checks gamejoin makes.

**Auth:** 

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer` | Yes |  |
| `userId` | query | `integer` | No |  |

**Responses:**

- `200`: Success → `TestStartPlaceOverrideResponse`

**Response fields** (`TestStartPlaceOverrideResponse`)

See [TestStartPlaceOverrideResponse](#teststartplaceoverrideresponse) in Models.

**Response example:**
```json
{
  "result": "Invalid",
  "placeId": 0
}
```

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://apis.roblox.com/matchmaking-api/v1/matchmaking/universe/{UNIVERSEID}/start-place/test"
```

## Models

### ClientStatusGetRequest

Get Client Status request.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `browserTrackerId` | `integer` | No | The client's browser tracker id. |

### ClientStatusSetRequest

Set Client Status request.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `status` | `string` | No | The client's status to send. |
| `browserTrackerId` | `integer` | No | The client's browser tracker id. |

### ForecastUpdateRequest

ForecastUpdateRequest is used to request an update to the forecast of a Place in a Universe.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `universeId` | `integer` | No | The Universe ID to update. |

### ForecastUpdateResponse

ForecastUpdateResponse is used to return information about the forecasted update of a place.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `placeSummaries` | `PlaceSummaryForGameUpdate[]` | No |  |

### GetUpdateStatusResponse

Get Update Status response.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `updateStatusList` | `GameUpdateStatus[]` | No | The status of the game update. |

### LaunchUpdateRequest

Launch Update Request. Contains specification for how update should roll out

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `universeId` | `integer` | No | The Universe ID to update. |
| `placeIds` | `integer[]` | No | The place IDs to update. If none are specified, we will update all active Places in the Universe |
| `closeOldVersionsOnly` | `boolean` | No | If true (default in UI), we will only migrate players from servers running old PlaceVersions. If false, we will migrate all players |
| `bleedOffServers` | `boolean` | No | If true (default in UI), we will stop matchmaking to servers but keep them up before shutting them down, allowing  players to naturally migrate to the newer version. If false, we will immediately start shutting down servers |
| `bleedOffDurationMinutes` | `integer` | No | If BleedOffServers=true, how long will we allow old servers to stay up before shutting them down. Valid values: 1 - 60 minutes |
| `placeIdToVersions` | `object` | No | Optional. A mapping of PlaceId to the specific versions to restart/bleed off for that place. When set for a place, only servers running those exact versions will be affected. If a place is not in this dictionary or has an empty set, behavior falls back to CloseOldVersionsOnly logic. |
| `attributes` | `string` | No | Optional. Attributes string to include in the ServerLifecycleChanged CSM payload published to game servers. |

### LaunchUpdateResponse

Launch Update response.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `updateId` | `string` | No | An ID for UI to query status of this update |
| `numPlayersToBeKicked` | `integer` | No | How many players are playing in servers that will be shut down according to the update configuration |
| `instancesToBeClosed` | `integer` | No | How many game instances will be closed according to the update configuration |

### ShutdownGameInstancesRequest

Shutdown Game Instance request.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `placeId` | `integer` | No | The place ID to shut down. |
| `privateServerId` | `integer` | No | The private server ID. |
| `gameId` | `string` | No | The game ID. |

### ShutdownGameInstancesResponse

Shutdown Game Instance response.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `placeId` | `integer` | No | The place ID to shut down. |
| `privateServerId` | `integer` | No | The private server ID. |
| `gameId` | `string` | No | The game ID. |

### ShutdownAllGameInstancesResponse

Shutdown All Game Instances response.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `placeId` | `integer` | No | The place ID to shut down. |
| `replaceInstances` | `boolean` | No | Whether to replace instances or not. |

### CreateMatchmakingPlayerAttributeDefinitionRequest

Request to create a new MatchmakingPlayerAttributeDefinition.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `universeId` | `integer` | No | UniverseId for the new PlayerAttributeDefinition. |
| `name` | `string` | No | Name of the new rule. |
| `dataType` | `MatchmakingAttributeDataType` | No |  |
| `defaultValue` | `MatchmakingAttributeValue` | No |  |
| `attributeValueLocation` | `MatchmakingAttributeValueLocation` | No |  |

### CreateMatchmakingPlayerAttributeDefinitionResponse

The response for creating a matchmaking player attribute definition.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `playerAttributeDefinition` | `MatchmakingPlayerAttributeDefinition` | No |  |

### UpdateMatchmakingPlayerAttributeDefinitionRequest

Request model for updating a PlayerAttributeDefinition.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `attributeId` | `string` | No | Id of the attribute to update. |
| `defaultValue` | `MatchmakingAttributeValue` | No |  |
| `attributeValueLocation` | `MatchmakingAttributeValueLocation` | No |  |

### UpdateMatchmakingPlayerAttributeDefinitionResponse

The response for updating a matchmaking player attribute definition.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `playerAttributeDefinition` | `MatchmakingPlayerAttributeDefinition` | No |  |

### ListMatchmakingPlayerAttributeDefinitionsResponse

The response for listing matchmaking player attribute definitions.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `playerAttributeSchema` | `MatchmakingPlayerAttributeDefinition[]` | No | All PlayerAttributeDefinitions for a universe. |

### CreateMatchmakingScoringConfigurationRequest

Request to create a matchmaking scoring configuration.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `universeId` | `integer` | No | UniverseId for the new matchmaking scoring configuraiton. |
| `name` | `string` | No | Name of the scoring configuration. |
| `matchmakingSignalWeights` | `object` | No | The desired set of weights for each matchmaking signal. |
| `customSignalWeights` | `object` | No | The desired set of weights for custom signals. It is a map from custom signal name to its weight. |
| `template` | `MatchmakingScoringConfigurationTemplate` | No |  |

### CreateMatchmakingScoringConfigurationResponse

Response to create a matchmaking scoring configuration.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `scoringConfiguration` | `MatchmakingScoringConfiguration` | No |  |

### GetMatchmakingScoringDefaultWeightsResponse

Response containing the weights of the current default matchmaking scoring weights

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `weights` | `object` | No | The weights of the current default matchmaking scoring weights. |

### GenerateMockServerSignalValuesResponse

Response for generating mock server signal values.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `exampleGameSignalValues` | `MockServerSignalValues[]` | No | The mock server signal values. |

### SetPlaceMatchmakingScoringConfigurationRequest

Request to set the matchmaking scoring configuration for a place.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `placeId` | `integer` | No | The place ID of the desired scoring configuration to set. |
| `scoringConfigurationId` | `string` | No | The ID of the scoring configuration. |

### SetMatchmakingScoringConfigurationResponse

Response to set the matchmaking scoring configuration.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `scoringConfiguration` | `MatchmakingScoringConfiguration` | No |  |

### GetMatchmakingScoringConfigurationResponse

Response to get the matchmaking scoring configuration.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `scoringConfiguration` | `MatchmakingScoringConfiguration` | No |  |

### UpdateMatchmakingScoringConfigurationRequest

Request to update a custom matchmaking signal.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `scoringConfigurationId` | `string` | No | The ID of the scoring configuration to be updated. |
| `name` | `string` | No | Name of the scoring configuration. |
| `matchmakingSignalWeights` | `object` | No | The desired set of weights for each matchmaking signal. |
| `customSignalWeights` | `object` | No | The desired set of weights for custom signals. It is a map from custom signal name to its weight. |

### UpdateMatchmakingScoringConfigurationResponse

Response to update a matchmaking scoring configuration.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `scoringConfiguration` | `MatchmakingScoringConfiguration` | No |  |

### CreateCustomMatchmakingSignalRequest

Request to create a custom matchmaking signal.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `scoringConfigurationId` | `string` | No | The ID of the scoring configuration that has the signal to be created. |
| `signalConfiguration` | `CustomSignalConfiguration` | No |  |

### CreateCustomMatchmakingSignalResponse

Response to create a custom matchmaking signal.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `scoringConfiguration` | `MatchmakingScoringConfiguration` | No |  |

### UpdateCustomMatchmakingSignalRequest

Request to update a custom matchmaking signal.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `scoringConfigurationId` | `string` | No | The ID of the scoring configuration. |
| `signalConfiguration` | `CustomSignalConfiguration` | No |  |

### UpdateCustomMatchmakingSignalResponse

Response to update a custom matchmaking signal.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `scoringConfiguration` | `MatchmakingScoringConfiguration` | No |  |

### DeleteCustomMatchmakingSignalResponse

Response to delete a custom matchmaking signal.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `scoringConfiguration` | `MatchmakingScoringConfiguration` | No |  |

### ListMatchmakingScoringConfigurationsResponse

Response to list matchmaking scoring configurations in a universe.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `scoringConfigurations` | `MatchmakingScoringConfiguration[]` | No | The scoring configurations. |

### ListPlaceMatchmakingScoringConfigurationsResponse

Response to list all places with scoring configuration in a universe.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `placeScoringConfigurations` | `object` | No | The scoring configurations for places. |

### CreateMatchmakingServerAttributeDefinitionRequest

Request to create a new ServerAttributeDefinition.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `universeId` | `integer` | No | UniverseId for the new PlayerAttributeDefinition. |
| `name` | `string` | No | Name of the new rule. |
| `dataType` | `MatchmakingAttributeDataType` | No |  |
| `defaultValue` | `MatchmakingServerAttributeDefaultValue` | No |  |

### CreateMatchmakingServerAttributeDefinitionResponse

The response for creating a matchmaking server attribute definition.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `playerAttributeDefinition` | `MatchmakingServerAttributeDefinition` | No |  |

### UpdateMatchmakingServerAttributeDefinitionRequest

Request model to update an exising ServerAttributeDefinition.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `attributeId` | `string` | No | Id of the attribute to update. |
| `defaultValue` | `MatchmakingServerAttributeDefaultValue` | No |  |

### UpdateMatchmakingServerAttributeDefinitionResponse

The response for updating a matchmaking server attribute definition.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `playerAttributeDefinition` | `MatchmakingServerAttributeDefinition` | No |  |

### ListMatchmakingServerAttributeDefinitionsResponse

The response for listing matchmaking server attribute definitions.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `serverAttributeSchema` | `MatchmakingServerAttributeDefinition[]` | No | All ServerAttributeDefinitions for a universe. |

### GetMatchmakingCustomizationFeatureFlagsResponse

Response to get matchmaking customization feature flags.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `featureFlags` | `MatchmakingCustomizationFeatureFlags` | No |  |

### GetStartPlaceOverrideResponse

Response for getting the start place override for a universe.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `dataStoreLocation` | `DataStoreLocation` | No |  |

### SetStartPlaceOverrideRequestBody

Request body for setting the start place override for a universe. The universe is
identified by the route, so it is not part of the body.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `dataStoreLocation` | `DataStoreLocation` | No |  |

### TestStartPlaceOverrideResponse

Response for testing a user's saved start place in a universe.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `result` | `StartPlaceOverrideTestResult` | No |  |
| `placeId` | `integer` | No | The place id read from the user's data store entry. Null when no place id could be read. |