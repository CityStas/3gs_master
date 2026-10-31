---
name: "Economy Api v1"
last_updated: 2026-10-30T19:56:08Z
type: legacy
api_base_url: "https://economy.roblox.com"
versions: [v1]
endpoints: 1
auth: [cookie]
---

# Economy Api v1

> **Warning:** Legacy APIs with cookie authentication can incorporate breaking changes without notice. We don't recommend them for production applications.

**Base URL:** `https://economy.roblox.com`
**Versions:** v1

## Endpoints

### GET `/v1/user/currency`

Gets currency for the authenticated user.

Currency can only be retrieved for the authenticated user.

**Responses:**

- `200`: OK → `Roblox.Web.Responses.Economy.CurrencyResponse`
- `401`: 0: Authorization has been denied for this request.
- `403`: 1: The user is invalid.

**Response fields** (`Roblox.Web.Responses.Economy.CurrencyResponse`)

See [Roblox.Web.Responses.Economy.CurrencyResponse](#roblox-web-responses-economy-currencyresponse) in Models.

**Response example:**
```json
{
  "robux": 0
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://economy.roblox.com/v1/user/currency"
```

## Models

### Roblox.Web.Responses.Economy.CurrencyResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `robux` | `integer` | No |  |