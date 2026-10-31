---
name: "Matchmaking Api v1"
last_updated: 2026-10-30T19:56:08Z
type: legacy
api_base_url: "https://apis.roblox.com"
versions: [v1]
endpoints: 25
auth: [cookie]
---

# Matchmaking Api v1

> **Warning:** Legacy APIs with cookie authentication can incorporate breaking changes without notice. We don't recommend them for production applications.

**Base URL:** `https://apis.roblox.com`
**Versions:** v1

## Endpoints

### GET `/matchmaking-api/v1/client-status`

Get the client-status

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

### POST `/matchmaking-api/v1/client-status`

Set the client-status

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

### POST `/matchmaking-api/v1/game-instances/shutdown`

Shutdown game instances.

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
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://apis.roblox.com/matchmaking-api/v1/game-instances/shutdown" \
  -H "Content-Type: application/json" \
  -d '{
  "placeId": 0,
  "privateServerId": 0,
  "gameId": "string"
}'
```

### POST `/matchmaking-api/v1/game-instances/shutdown-all`

Shutdown all game instances.

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
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://apis.roblox.com/matchmaking-api/v1/game-instances/shutdown-all" \
  -F "PlaceId=0" \
  -F "ReplaceInstances=false"
```

### POST `/matchmaking-api/v1/matchmaking/player-attribute`

Create a PlayerAttributeDefinition.

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

### PATCH `/matchmaking-api/v1/matchmaking/player-attribute/{attributeId}`

Update the PlayerAttributeDefinition specified by attributeId.

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

### DELETE `/matchmaking-api/v1/matchmaking/player-attribute/{attributeId}`

Delete the PlayerAttributeDefinition specified by attributeId.

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

### GET `/matchmaking-api/v1/matchmaking/player-attributes/{universeId}`

List all PlayerAttributeDefinitions of a universe.

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

### POST `/matchmaking-api/v1/matchmaking/server-attribute`

Create a ServerAttributeDefinition.

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

### PATCH `/matchmaking-api/v1/matchmaking/server-attribute/{attributeId}`

Update the ServerAttributeDefinition specified by attributeId.

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

### DELETE `/matchmaking-api/v1/matchmaking/server-attribute/{attributeId}`

Delete the ServerAttributeDefinition specified by attributeId.

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

### GET `/matchmaking-api/v1/matchmaking/server-attributes/{universeId}`

List all ServerAttributeDefinitions of a universe.

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

### GET `/matchmaking-api/v1/matchmaking/universe/{universeId}/feature-flags`

Gets feature flags for a customized matchmaking for a given universe.

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
    "isMatchmakingCustomizationAllowed": false
  }
}
```

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://apis.roblox.com/matchmaking-api/v1/matchmaking/universe/{UNIVERSEID}/feature-flags"
```

### POST `/matchmaking-api/v1/matchmaking/scoring-configuration`

Creates a matchmaking scoring configuration.

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

### GET `/matchmaking-api/v1/matchmaking/scoring-configuration/{scoringConfigurationId}`

Updates a matchmaking scoring configuration.

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

### PATCH `/matchmaking-api/v1/matchmaking/scoring-configuration/{scoringConfigurationId}`

Updates a matchmaking scoring configuration.

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

### DELETE `/matchmaking-api/v1/matchmaking/scoring-configuration/{scoringConfigurationId}`

Deletes a matchmaking scoring configuration.

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

### POST `/matchmaking-api/v1/matchmaking/scoring-configuration/{scoringConfigurationId}/signals`

Creates a matchmaking scoring configuration signal.

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

### PATCH `/matchmaking-api/v1/matchmaking/scoring-configuration/{scoringConfigurationId}/signals/{signalName}`

Updates a matchmaking scoring configuration signal.

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

### DELETE `/matchmaking-api/v1/matchmaking/scoring-configuration/{scoringConfigurationId}/signals/{signalName}`

Deletes a matchmaking scoring configuration custom signal.

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

### POST `/matchmaking-api/v1/matchmaking/scoring-configuration/place`

Sets a matchmaking scoring configuration for a place.

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

### DELETE `/matchmaking-api/v1/matchmaking/scoring-configuration/place/{placeId}`

Removes the matchmaking scoring configuration for a place.

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

### GET `/matchmaking-api/v1/matchmaking/scoring-configurations/{universeId}`

List all matchmaking scoring configurations for a universe.

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

### GET `/matchmaking-api/v1/matchmaking/scoring-configurations/{universeId}/places`

List all places with a matchmaking scoring configuration for a universe.

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

### GET `/matchmaking-api/v1/matchmaking/scoring-configuration/default-weights`

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

### CustomSignalConfiguration

The custom signal configuration using a developer created attribute.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | `string` | No | The name of the signal. |
| `weight` | `number` | No | The weight of the signal. |
| `customSignalType` | `CustomSignalType` | No |  |
| `playerCategoricalSignalConfiguration` | `PlayerCategoricalSignalConfiguration` | No |  |
| `serverCategoricalSignalConfiguration` | `ServerCategoricalSignalConfiguration` | No |  |
| `serverNumericalSignalConfiguration` | `ServerNumericalSignalConfiguration` | No |  |
| `playerNumericalSignalConfiguration` | `PlayerNumericalSignalConfiguration` | No |  |

### DataStoreLocation

Describes where an attribute value exists in DataStore.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `dataStoreName` | `string` | No | The DataStore name. |
| `scope` | `string` | No | The scope of the key in DataStore. |
| `keyTemplate` | `string` | No | The key of a DataStore value, with {UserId} replaced by the player's actual ID when fetching values. |
| `valuePath` | `string` | No | A JSON path to a value if it lives in a JSON object. |

### DeleteCustomMatchmakingSignalResponse

Response to delete a custom matchmaking signal.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `scoringConfiguration` | `MatchmakingScoringConfiguration` | No |  |

### GetMatchmakingCustomizationFeatureFlagsResponse

Response to get matchmaking customization feature flags.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `featureFlags` | `MatchmakingCustomizationFeatureFlags` | No |  |

### GetMatchmakingScoringConfigurationResponse

Response to get the matchmaking scoring configuration.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `scoringConfiguration` | `MatchmakingScoringConfiguration` | No |  |

### GetMatchmakingScoringDefaultWeightsResponse

Response containing the weights of the current default matchmaking scoring weights

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `weights` | `object` | No | The weights of the current default matchmaking scoring weights. |

### ListMatchmakingPlayerAttributeDefinitionsResponse

The response for listing matchmaking player attribute definitions.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `playerAttributeSchema` | `MatchmakingPlayerAttributeDefinition[]` | No | All PlayerAttributeDefinitions for a universe. |

### ListMatchmakingScoringConfigurationsResponse

Response to list matchmaking scoring configurations in a universe.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `scoringConfigurations` | `MatchmakingScoringConfiguration[]` | No | The scoring configurations. |

### ListMatchmakingServerAttributeDefinitionsResponse

The response for listing matchmaking server attribute definitions.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `serverAttributeSchema` | `MatchmakingServerAttributeDefinition[]` | No | All ServerAttributeDefinitions for a universe. |

### ListPlaceMatchmakingScoringConfigurationsResponse

Response to list all places with scoring configuration in a universe.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `placeScoringConfigurations` | `object` | No | The scoring configurations for places. |

### MatchmakingAttributeAggregation

Matchmaking attribute aggregation object for matchmaking rules.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `aggregationFunction` | `AttributeAggregationFunction` | No |  |

### MatchmakingAttributeReference

Matchmaking attribute reference object for matchmaking rules.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | `string` | No | The id of the attribute. |

### MatchmakingAttributeValue

Matchmaking attribute value object for matchmaking rules.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `boolValue` | `boolean` | No | Bool value of the attribute. One of BoolValue, NumericValue, or StringValue must be set. |
| `numericValue` | `number` | No | Double value of the attribute. One of BoolValue, NumericValue, or StringValue must be set. |
| `stringValue` | `string` | No | String value of the attribute. One of BoolValue, NumericValue, or StringValue must be set. |
| `type` | `MatchmakingAttributeValueType` | No |  |

### MatchmakingAttributeValueLocation

Describes where an attribute value exists.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `locationCase` | `MatchmakingAttributeValueLocationCase` | No |  |
| `dataStoreLocation` | `DataStoreLocation` | No |  |

### MatchmakingCustomizationFeatureFlags

Matchmaking object for universe feature flags controlling matchmaking customization.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `isMatchmakingCustomizationAllowed` | `boolean` | No | If matchmaking customization is allowed for universe |

### MatchmakingPlayerAttributeDefinition

Describes a player attribute definition for matchmaking.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | `string` | No | The id of the attribute. |
| `universeId` | `integer` | No | The universe id of the attribute. |
| `name` | `string` | No | The name of the attribute. |
| `dataType` | `MatchmakingAttributeDataType` | No |  |
| `defaultValue` | `MatchmakingAttributeValue` | No |  |
| `attributeValueLocation` | `MatchmakingAttributeValueLocation` | No |  |
| `createdTime` | `string` | No | The aggregation function of the attribute. |
| `updatedTime` | `string` | No | The time the attribute was last updated. |

### MatchmakingScoringConfiguration

The custom scoring configuration for matchmaking.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | `string` | No | The id of the scoring configuration. |
| `name` | `string` | No | The name of the scoring configuration. It needs to be unique within a universe. |
| `signalWeights` | `object` | No | The signal weights for the scoring configuration. |
| `customSignals` | `object` | No | The custom signals part of this place's scoring configuration. |
| `createdTime` | `string` | No | The scoring configuration's created time. |
| `updatedTime` | `string` | No | The scoring configuration's updated time. |

### MatchmakingServerAttributeDefaultValue

Describes how the server attribute value should be derived

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `sourceCase` | `MatchmakingServerAttributeDefaultValueSourceCase` | No |  |
| `constant` | `MatchmakingAttributeValue` | No |  |
| `playerAttributeReference` | `MatchmakingAttributeReference` | No |  |

### MatchmakingServerAttributeDefinition

Describes a player attribute definition for matchmaking.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | `string` | No | The id of the attribute. |
| `universeId` | `integer` | No | The universe id of the attribute. |
| `name` | `string` | No | The name of the attribute. |
| `dataType` | `MatchmakingAttributeDataType` | No |  |
| `defaultValue` | `MatchmakingServerAttributeDefaultValue` | No |  |
| `createdTime` | `string` | No | The aggregation function of the attribute. |
| `updatedTime` | `string` | No | The time the attribute was last updated. |

### MatchmakingSignalWeightConfiguration

The signal weight configuration for matchmaking.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `weight` | `number` | No | Weight of signal. |
| `signalType` | `MatchmakingSignalType` | No |  |

### PlayerCategoricalSignalConfiguration

The player categorical signal configuration.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `playerAttribute` | `MatchmakingAttributeReference` | No |  |
| `curveType` | `MatchmakingSignalCurveType` | No |  |

### PlayerNumericalSignalConfiguration

The player numerical signal configuration.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `playerAttribute` | `MatchmakingAttributeReference` | No |  |
| `aggregation` | `MatchmakingAttributeAggregation` | No |  |
| `comparisonType` | `MatchmakingNumericalAttributeComparisonType` | No |  |
| `maxRelevantDifference` | `number` | No | The maximum relevant difference for this signal. |
| `constantValue` | `number` | No | The constant value for this signal to be compared to. |

### ServerCategoricalSignalConfiguration

The server categorical signal configuration.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `serverAttribute` | `MatchmakingAttributeReference` | No |  |
| `comparisonType` | `MatchmakingCategoricalAttributeComparisonType` | No |  |
| `playerAttribute` | `MatchmakingAttributeReference` | No |  |
| `constantValue` | `string` | No | The constant value for this signal to be compared to. |

### ServerNumericalSignalConfiguration

The server numerical signal configuration.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `serverAttribute` | `MatchmakingAttributeReference` | No |  |
| `comparisonType` | `MatchmakingNumericalAttributeComparisonType` | No |  |
| `maxRelevantDifference` | `number` | No | The maximum relevant difference for this signal. |
| `constantValue` | `number` | No | The constant value for this signal to be compared to. |
| `playerAttribute` | `MatchmakingAttributeReference` | No |  |

### SetMatchmakingScoringConfigurationResponse

Response to set the matchmaking scoring configuration.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `scoringConfiguration` | `MatchmakingScoringConfiguration` | No |  |

### SetPlaceMatchmakingScoringConfigurationRequest

Request to set the matchmaking scoring configuration for a place.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `placeId` | `integer` | No | The place ID of the desired scoring configuration to set. |
| `scoringConfigurationId` | `string` | No | The ID of the scoring configuration. |

### ShutdownAllGameInstancesResponse

Shutdown All Game Instances response.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `placeId` | `integer` | No | The place ID to shut down. |
| `replaceInstances` | `boolean` | No | Whether to replace instances or not. |

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