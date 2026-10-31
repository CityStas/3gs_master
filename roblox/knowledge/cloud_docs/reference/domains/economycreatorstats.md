---
name: "Roblox.EconomyCreatorStats.Api v1"
last_updated: 2026-10-30T19:56:08Z
type: legacy
api_base_url: "https://economycreatorstats.roblox.com"
versions: [v1]
endpoints: 1
auth: [cookie]
---

# Roblox.EconomyCreatorStats.Api v1

> **Warning:** Legacy APIs with cookie authentication can incorporate breaking changes without notice. We don't recommend them for production applications.

**Base URL:** `https://economycreatorstats.roblox.com`
**Versions:** v1

## Endpoints

### GET `/v1/universes/{universeId}/stats`

Get statistics data for a universe.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer (int64)` | Yes | The universe id. |
| `Type` | query | `string` | Yes | The type of a statistics dataset. ['PremiumUpsells' = 0, 'PremiumVisits' = 1] Valid values: `PremiumUpsells`, `PremiumVisits` |
| `StartTime` | query | `string (date-time)` | Yes |  |
| `EndTime` | query | `string (date-time)` | Yes |  |

**Responses:**

- `200`: OK → `Roblox.EconomyCreatorStats.Api.Models.StatisticsResponse`
- `400`: 1: The Universe is invalid. 3: Too many data points requested. 4: The requested data type is not known.
- `401`: 0: Authorization has been denied for this request. 2: Not authorized to perform this action.

**Response fields** (`Roblox.EconomyCreatorStats.Api.Models.StatisticsResponse`)

See [Roblox.EconomyCreatorStats.Api.Models.StatisticsResponse](#roblox-economycreatorstats-api-models-statisticsresponse) in Models.

**Response example:**
```json
{
  "dataGranularity": 0,
  "data": "..."
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://economycreatorstats.roblox.com/v1/universes/{UNIVERSEID}/stats?Type={VALUE}&StartTime={VALUE}&EndTime={VALUE}"
```

## Models

### Roblox.EconomyCreatorStats.Api.Models.StatisticsResponse

The response model

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `dataGranularity` | `0 \| 1 \| 2` | No | The Roblox.EconomyCreatorStats.Api.StatisticsDataGranularity. ['Hourly' = 0, 'Daily' = 1, 'Monthly' = 2] |
| `data` | `object` | No | The actual data. |