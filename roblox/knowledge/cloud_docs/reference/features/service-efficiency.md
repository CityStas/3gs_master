---
name: "Service Efficiency"
last_updated: 2026-10-30T19:56:08Z
type: feature
api_base_url: "https://apis.roblox.com"
endpoints: 2
auth: [api-key, oauth2, cookie]
description: "Manage Service Efficiency accounts and billing for users and groups, and configure consumer settings for a universe"
---

# Service Efficiency

Manage Service Efficiency accounts and billing for users and groups, and configure consumer settings for a universe.

Common use cases include:

- Account management: [Retrieve](#ServiceEfficiencyApi_GetAccountForUser) or [update](#ServiceEfficiencyApi_UpdateAccountForUser) a user's account, or [retrieve](#ServiceEfficiencyApi_GetAccountForGroup) or [update](#ServiceEfficiencyApi_UpdateAccountForGroup) a group's account
- Billing: [Review billing activity](#ServiceEfficiencyApi_GetBillingActivitiesByUser) and [retrieve bills](#ServiceEfficiencyApi_GetBillByUser) for a user, or [review billing activity](#ServiceEfficiencyApi_GetBillingActivitiesByGroup) and [retrieve bills](#ServiceEfficiencyApi_GetBillByGroup) for a group
- Eligibility and access: [Check user](#ServiceEfficiencyApi_CheckEligibilityForUser) or [group](#ServiceEfficiencyApi_CheckEligibilityForGroup) eligibility, and [check access](#ServiceEfficiencyApi_IsAllowed) for the current user
- Payment profiles: [List](#ServiceEfficiencyApi_ListPaymentProfilesByUser), [create](#ServiceEfficiencyApi_CreatePaymentProfileForUser), or [delete](#ServiceEfficiencyApi_DeletePaymentProfileForUser) a user's payment profile
- Payment methods: [Retrieve](#ServiceEfficiencyApi_GetServiceEfficiencyPaymentMethodForUser) or [set](#ServiceEfficiencyApi_SetServiceEfficiencyPaymentMethodForUser) a user's payment method, or [retrieve](#ServiceEfficiencyApi_GetServiceEfficiencyPaymentMethodForGroup) or [set](#ServiceEfficiencyApi_SetServiceEfficiencyPaymentMethodForGroup) a group's payment method
- Manual payments: [Submit a payment for a user](#ServiceEfficiencyApi_SubmitManualPaymentForUser) or [group](#ServiceEfficiencyApi_SubmitManualPaymentForGroup)
- Universe configuration: [Retrieve](#ServiceEfficiencyApi_GetConsumerConfigurationsByUniverse) or [update](#ServiceEfficiencyApi_UpdateConsumerConfigurationsByUniverse) consumer configuration

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

### GET `/service-efficiency-api/v1/configurations/universes/{universeId}` [EXPERIMENTAL]

Operation to Get ConsumerConfiguration for a universe.

**Auth:** Cookie (`.ROBLOSECURITY`) or API Key (`x-api-key` header)

**Scopes:** `extended-services:read`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer` | Yes |  |

**Responses:**

- `200`: OK → `ConsumerConfigurationResponse`
- `400`: Bad Request
- `401`: Unauthorized
- `403`: Forbidden
- `404`: Not Found
- `500`: Internal Server Error
- `503`: Service Unavailable

**Response fields** (`ConsumerConfigurationResponse`)

See [ConsumerConfigurationResponse](#consumerconfigurationresponse) in Models.

**Response example:**
```json
{
  "accountState": "...",
  "accountInfoComplete": false,
  "serviceConfigurations": [
    {
      "serviceId": "...",
      "monthlyBudget": "...",
      "resourceConfigurations": "...",
      "budgetLevel": "..."
    }
  ]
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 5000/minute

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/service-efficiency-api/v1/configurations/universes/{UNIVERSEID}"
```

### PATCH `/service-efficiency-api/v1/configurations/universes/{universeId}` [EXPERIMENTAL]

Operation to Update ConsumerConfiguration for a universe.

**Auth:** Cookie (`.ROBLOSECURITY`) or API Key (`x-api-key` header)

**Scopes:** `extended-services:write`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | path | `integer` | Yes |  |

**Request Body:** `application/json-patch+json` — Type: `any`

**Responses:**

- `200`: OK → `ConsumerConfigurationResponse`
- `400`: Bad Request
- `401`: Unauthorized
- `403`: Forbidden
- `404`: Not Found
- `500`: Internal Server Error
- `503`: Service Unavailable

**Response fields** (`ConsumerConfigurationResponse`)

See [ConsumerConfigurationResponse](#consumerconfigurationresponse) in Models.

**Response example:**
```json
{
  "accountState": "...",
  "accountInfoComplete": false,
  "serviceConfigurations": [
    {
      "serviceId": "...",
      "monthlyBudget": "...",
      "resourceConfigurations": "...",
      "budgetLevel": "..."
    }
  ]
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 5000/minute

**Example:**
```bash
curl -X PATCH -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/service-efficiency-api/v1/configurations/universes/{UNIVERSEID}" \
  -H "Content-Type: application/json" \
  -d '"..."'
```

## Models

### ConsumerConfigurationResponse

Response object for consumer configuration.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `accountState` | `any` | No | Gets or sets the account state. |
| `accountInfoComplete` | `boolean` | No | Gets or sets a value indicating whether account information is complete. |
| `serviceConfigurations` | `ServiceConfiguration[]` | Yes | Gets or sets the service configuration lists. |