---
name: "Accounts"
last_updated: 2026-10-30T19:56:08Z
type: feature
api_base_url: "https://apis.roblox.com"
endpoints: 198
auth: [api-key, oauth2, cookie]
description: "Access and manage Roblox account information, including Service Efficiency billing accounts"
---

# Accounts

Access and manage Roblox account information, including Service Efficiency billing accounts. [Retrieve](#ServiceEfficiencyApi_GetAccountForUser) and [update](#ServiceEfficiencyApi_UpdateAccountForUser) user accounts, or [retrieve](#ServiceEfficiencyApi_GetAccountForGroup) and [update](#ServiceEfficiencyApi_UpdateAccountForGroup) group accounts.

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

### GET `/service-efficiency-api/v1/accounts/groups/{groupId}` [EXPERIMENTAL]

Operation to Get an Account for a Group.

**Auth:** Cookie (`.ROBLOSECURITY`) or API Key (`x-api-key` header)

**Scopes:** `extended-services:read`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer` | Yes | Group id. |

**Responses:**

- `200`: OK → `GetAccountResponse`
- `400`: Bad Request
- `401`: Unauthorized
- `403`: Forbidden
- `404`: Not Found
- `500`: Internal Server Error
- `503`: Service Unavailable

**Response fields** (`GetAccountResponse`)

See [GetAccountResponse](#getaccountresponse) in Models.

**Response example:**
```json
{
  "account": "..."
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 100/minute

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/service-efficiency-api/v1/accounts/groups/{GROUPID}"
```

### PUT `/service-efficiency-api/v1/accounts/groups/{groupId}` [EXPERIMENTAL]

Operation to Update an Account for a Group.

**Auth:** Cookie (`.ROBLOSECURITY`) or API Key (`x-api-key` header)

**Scopes:** `extended-services:write`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer` | Yes | Group id. |

**Request Body:** `application/json-patch+json` — Type: `any`

**Responses:**

- `200`: OK → `UpdateAccountResponse`
- `400`: Bad Request
- `401`: Unauthorized
- `403`: Forbidden
- `404`: Not Found
- `500`: Internal Server Error
- `503`: Service Unavailable

**Response fields** (`UpdateAccountResponse`)

See [UpdateAccountResponse](#updateaccountresponse) in Models.

**Response example:**
```json
{
  "account": "..."
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 100/minute

**Example:**
```bash
curl -X PUT -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/service-efficiency-api/v1/accounts/groups/{GROUPID}" \
  -H "Content-Type: application/json" \
  -d '"..."'
```

### GET `/service-efficiency-api/v1/accounts/users/{userId}` [EXPERIMENTAL]

Operation to Get an Account for a User.

**Auth:** Cookie (`.ROBLOSECURITY`) or API Key (`x-api-key` header)

**Scopes:** `extended-services:read`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer` | Yes | User id. |

**Responses:**

- `200`: OK → `GetAccountResponse`
- `400`: Bad Request
- `401`: Unauthorized
- `403`: Forbidden
- `404`: Not Found
- `500`: Internal Server Error
- `503`: Service Unavailable

**Response fields** (`GetAccountResponse`)

See [GetAccountResponse](#getaccountresponse) in Models.

**Response example:**
```json
{
  "account": "..."
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 100/minute

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/service-efficiency-api/v1/accounts/users/{USERID}"
```

### PUT `/service-efficiency-api/v1/accounts/users/{userId}` [EXPERIMENTAL]

Operation to Update an Account for a User.

**Auth:** Cookie (`.ROBLOSECURITY`) or API Key (`x-api-key` header)

**Scopes:** `extended-services:write`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer` | Yes | User id. |

**Request Body:** `application/json-patch+json` — Type: `any`

**Responses:**

- `200`: OK → `UpdateAccountResponse`
- `400`: Bad Request
- `401`: Unauthorized
- `403`: Forbidden
- `404`: Not Found
- `500`: Internal Server Error
- `503`: Service Unavailable

**Response fields** (`UpdateAccountResponse`)

See [UpdateAccountResponse](#updateaccountresponse) in Models.

**Response example:**
```json
{
  "account": "..."
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 100/minute

**Example:**
```bash
curl -X PUT -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/service-efficiency-api/v1/accounts/users/{USERID}" \
  -H "Content-Type: application/json" \
  -d '"..."'
```

### GET `/service-efficiency-api/v1/billing_activities/groups/{groupId}` [EXPERIMENTAL]

Operation to Get Billing Activities

**Auth:** Cookie (`.ROBLOSECURITY`) or API Key (`x-api-key` header)

**Scopes:** `extended-services:read`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer` | Yes |  |
| `startYear` | query | `integer` | Yes |  |
| `startMonth` | query | `integer` | Yes |  |
| `endYear` | query | `integer` | Yes |  |
| `endMonth` | query | `integer` | Yes |  |

**Responses:**

- `200`: OK → `BillingActivitiesResponse`
- `400`: Bad Request
- `401`: Unauthorized
- `403`: Forbidden
- `404`: Not Found
- `500`: Internal Server Error
- `503`: Service Unavailable

**Response fields** (`BillingActivitiesResponse`)

See [BillingActivitiesResponse](#billingactivitiesresponse) in Models.

**Response example:**
```json
{
  "accountState": "...",
  "billSummaries": [
    {
      "timestamp": "...",
      "billId": "...",
      "billStatus": "...",
      "totalAmount": "..."
    }
  ],
  "currentBalance": "...",
  "monthToDateBalance": "...",
  "chargingThreshold": "..."
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 100/minute

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/service-efficiency-api/v1/billing_activities/groups/{GROUPID}?startYear={VALUE}&startMonth={VALUE}&endYear={VALUE}&endMonth={VALUE}"
```

### GET `/service-efficiency-api/v1/billing_activities/users/{userId}` [EXPERIMENTAL]

Operation to Get Billing Activities

**Auth:** Cookie (`.ROBLOSECURITY`) or API Key (`x-api-key` header)

**Scopes:** `extended-services:read`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer` | Yes |  |
| `startYear` | query | `integer` | Yes |  |
| `startMonth` | query | `integer` | Yes |  |
| `endYear` | query | `integer` | Yes |  |
| `endMonth` | query | `integer` | Yes |  |

**Responses:**

- `200`: OK → `BillingActivitiesResponse`
- `400`: Bad Request
- `401`: Unauthorized
- `403`: Forbidden
- `404`: Not Found
- `500`: Internal Server Error
- `503`: Service Unavailable

**Response fields** (`BillingActivitiesResponse`)

See [BillingActivitiesResponse](#billingactivitiesresponse) in Models.

**Response example:**
```json
{
  "accountState": "...",
  "billSummaries": [
    {
      "timestamp": "...",
      "billId": "...",
      "billStatus": "...",
      "totalAmount": "..."
    }
  ],
  "currentBalance": "...",
  "monthToDateBalance": "...",
  "chargingThreshold": "..."
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 100/minute

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/service-efficiency-api/v1/billing_activities/users/{USERID}?startYear={VALUE}&startMonth={VALUE}&endYear={VALUE}&endMonth={VALUE}"
```

### GET `/service-efficiency-api/v1/bills/groups/{groupId}` [EXPERIMENTAL]

Operation to Get Billing Statement for group owned account.

**Auth:** Cookie (`.ROBLOSECURITY`) or API Key (`x-api-key` header)

**Scopes:** `extended-services:read`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer` | Yes | Group id. |
| `billId` | query | `string` | No | Bill id. Takes precedence over date fields. |
| `year` | query | `integer` | No | Bill year. Ignored if bill id is provided. |
| `month` | query | `integer` | No | Bill month. Ignored if bill id is provided. |
| `date` | query | `integer` | No | Bill date. Ignored if bill id is provided. |
| `latest` | query | `boolean` | No | If true, we will return the most recent bill. |

**Responses:**

- `200`: OK → `BillDetailsResponse`
- `400`: Bad Request
- `401`: Unauthorized
- `403`: Forbidden
- `404`: Not Found
- `500`: Internal Server Error
- `503`: Service Unavailable

**Response fields** (`BillDetailsResponse`)

See [BillDetailsResponse](#billdetailsresponse) in Models.

**Response example:**
```json
{
  "accountState": "...",
  "billId": "string",
  "billStatus": "...",
  "usageAmount": "...",
  "taxAmount": "...",
  "totalAmount": "..."
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 100/minute

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/service-efficiency-api/v1/bills/groups/{GROUPID}"
```

### GET `/service-efficiency-api/v1/bills/users/{userId}` [EXPERIMENTAL]

Operation to Get Billing Statement for user owned account.

**Auth:** Cookie (`.ROBLOSECURITY`) or API Key (`x-api-key` header)

**Scopes:** `extended-services:read`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer` | Yes | User id. |
| `billId` | query | `string` | No | Bill id. Takes precedence over date fields. |
| `year` | query | `integer` | No | Bill year. Ignored if bill id is provided. |
| `month` | query | `integer` | No | Bill month. Ignored if bill id is provided. |
| `date` | query | `integer` | No | Bill date. Ignored if bill id is provided. |
| `latest` | query | `boolean` | No | If true, we will return the most recent bill. |

**Responses:**

- `200`: OK → `BillDetailsResponse`
- `400`: Bad Request
- `401`: Unauthorized
- `403`: Forbidden
- `404`: Not Found
- `500`: Internal Server Error
- `503`: Service Unavailable

**Response fields** (`BillDetailsResponse`)

See [BillDetailsResponse](#billdetailsresponse) in Models.

**Response example:**
```json
{
  "accountState": "...",
  "billId": "string",
  "billStatus": "...",
  "usageAmount": "...",
  "taxAmount": "...",
  "totalAmount": "..."
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 100/minute

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/service-efficiency-api/v1/bills/users/{USERID}"
```

### GET `/service-efficiency-api/v1/eligibility/groups/{groupId}` [EXPERIMENTAL]

Operation to Check the Eligibility of a Group.

**Auth:** Cookie (`.ROBLOSECURITY`) or API Key (`x-api-key` header)

**Scopes:** `extended-services:read`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer` | Yes | Group id. |

**Responses:**

- `200`: OK → `CheckEligibilityResponse`
- `400`: Bad Request
- `401`: Unauthorized
- `403`: Forbidden
- `404`: Not Found
- `500`: Internal Server Error
- `503`: Service Unavailable

**Response fields** (`CheckEligibilityResponse`)

See [CheckEligibilityResponse](#checkeligibilityresponse) in Models.

**Response example:**
```json
{
  "eligibilityRequirementResults": [
    {
      "eligibilityRequirement": "...",
      "eligible": "..."
    }
  ]
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 100/minute

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/service-efficiency-api/v1/eligibility/groups/{GROUPID}"
```

### GET `/service-efficiency-api/v1/eligibility/users/{userId}` [EXPERIMENTAL]

Operation to Check the Eligibility of a User.

**Auth:** Cookie (`.ROBLOSECURITY`) or API Key (`x-api-key` header)

**Scopes:** `extended-services:read`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer` | Yes | User id. |

**Responses:**

- `200`: OK → `CheckEligibilityResponse`
- `400`: Bad Request
- `401`: Unauthorized
- `403`: Forbidden
- `404`: Not Found
- `500`: Internal Server Error
- `503`: Service Unavailable

**Response fields** (`CheckEligibilityResponse`)

See [CheckEligibilityResponse](#checkeligibilityresponse) in Models.

**Response example:**
```json
{
  "eligibilityRequirementResults": [
    {
      "eligibilityRequirement": "...",
      "eligible": "..."
    }
  ]
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 100/second

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/service-efficiency-api/v1/eligibility/users/{USERID}"
```

### GET `/service-efficiency-api/v1/is_allowed` [EXPERIMENTAL]

Endpoint to return whether the current user can access the features in this API, optionally with a universe
ID.

**Auth:** Cookie (`.ROBLOSECURITY`) or API Key (`x-api-key` header)

**Scopes:** `extended-services:read`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeId` | query | `integer` | No | a universe the user may or may not be allowed to access |

**Responses:**

- `200`: OK → `boolean`
- `400`: Bad Request
- `401`: Unauthorized
- `500`: Internal Server Error
- `503`: Service Unavailable

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Rate Limits:** perApiKeyOwner: 5000/minute

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/service-efficiency-api/v1/is_allowed"
```

### GET `/service-efficiency-api/v1/payment_profiles/groups/{groupId}/service_efficiency` [EXPERIMENTAL]

Operation to Get the Service Efficiency Payment Method for a Group.

**Auth:** Cookie (`.ROBLOSECURITY`) or API Key (`x-api-key` header)

**Scopes:** `extended-services:read`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer` | Yes | Group id. |

**Responses:**

- `200`: OK → `GetServiceEfficiencyPaymentMethodResponse`
- `400`: Bad Request
- `401`: Unauthorized
- `403`: Forbidden
- `404`: Not Found
- `500`: Internal Server Error
- `503`: Service Unavailable

**Response fields** (`GetServiceEfficiencyPaymentMethodResponse`)

See [GetServiceEfficiencyPaymentMethodResponse](#getserviceefficiencypaymentmethodresponse) in Models.

**Response example:**
```json
{
  "paymentProfile": "..."
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 100/minute

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/service-efficiency-api/v1/payment_profiles/groups/{GROUPID}/service_efficiency"
```

### PUT `/service-efficiency-api/v1/payment_profiles/groups/{groupId}/service_efficiency` [EXPERIMENTAL]

Operation to Set the Service Efficiency Payment Method for a Group.

**Auth:** Cookie (`.ROBLOSECURITY`) or API Key (`x-api-key` header)

**Scopes:** `extended-services:write`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer` | Yes | Group id. |
| `paymentProfileId` | query | `string` | Yes | Payment profile id to set. |
| `paymentProfileOwnerType` | query | `string` | Yes | Payment profile owner type. GROUP or USER. |

**Responses:**

- `200`: OK → `SetServiceEfficiencyPaymentMethodResponse`
- `400`: Bad Request
- `401`: Unauthorized
- `403`: Forbidden
- `404`: Not Found
- `412`: Precondition Failed
- `500`: Internal Server Error
- `503`: Service Unavailable

**Response fields** (`SetServiceEfficiencyPaymentMethodResponse`)

See [SetServiceEfficiencyPaymentMethodResponse](#setserviceefficiencypaymentmethodresponse) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 100/minute

**Example:**
```bash
curl -X PUT -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/service-efficiency-api/v1/payment_profiles/groups/{GROUPID}/service_efficiency?paymentProfileId={VALUE}&paymentProfileOwnerType={VALUE}"
```

### GET `/service-efficiency-api/v1/payment_profiles/users/{userId}` [EXPERIMENTAL]

Operation to List Payment Profiles of a User.

**Auth:** Cookie (`.ROBLOSECURITY`) or API Key (`x-api-key` header)

**Scopes:** `extended-services:read`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer` | Yes | User id. |

**Responses:**

- `200`: OK → `ListPaymentProfilesResponse`
- `400`: Bad Request
- `401`: Unauthorized
- `403`: Forbidden
- `404`: Not Found
- `500`: Internal Server Error
- `503`: Service Unavailable

**Response fields** (`ListPaymentProfilesResponse`)

See [ListPaymentProfilesResponse](#listpaymentprofilesresponse) in Models.

**Response example:**
```json
{
  "paymentProfiles": [
    {
      "paymentProfileId": "...",
      "paymentProfileOwnerType": "...",
      "cardNetwork": "...",
      "last4Digits": "...",
      "expMonth": "...",
      "expYear": "..."
    }
  ]
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 100/minute

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/service-efficiency-api/v1/payment_profiles/users/{USERID}"
```

### POST `/service-efficiency-api/v1/payment_profiles/users/{userId}` [EXPERIMENTAL]

Operation to Create Payment Profile for a User.

**Auth:** Cookie (`.ROBLOSECURITY`) or API Key (`x-api-key` header)

**Scopes:** `extended-services:write`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer` | Yes | User id. |

**Responses:**

- `200`: OK → `CreatePaymentProfileResponse`
- `400`: Bad Request
- `401`: Unauthorized
- `403`: Forbidden
- `404`: Not Found
- `500`: Internal Server Error
- `503`: Service Unavailable

**Response fields** (`CreatePaymentProfileResponse`)

See [CreatePaymentProfileResponse](#createpaymentprofileresponse) in Models.

**Response example:**
```json
{
  "clientSecret": "string"
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 100/minute

**Example:**
```bash
curl -X POST -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/service-efficiency-api/v1/payment_profiles/users/{USERID}"
```

### DELETE `/service-efficiency-api/v1/payment_profiles/users/{userId}` [EXPERIMENTAL]

Operation to Delete a Payment Profile for a User.

**Auth:** Cookie (`.ROBLOSECURITY`) or API Key (`x-api-key` header)

**Scopes:** `extended-services:write`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer` | Yes | User id. |
| `paymentProfileId` | query | `string` | Yes | Payment profile id to delete. |

**Responses:**

- `200`: OK → `DeletePaymentProfileResponse`
- `400`: Bad Request
- `401`: Unauthorized
- `403`: Forbidden
- `404`: Not Found
- `500`: Internal Server Error
- `503`: Service Unavailable

**Response fields** (`DeletePaymentProfileResponse`)

See [DeletePaymentProfileResponse](#deletepaymentprofileresponse) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 100/minute

**Example:**
```bash
curl -X DELETE -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/service-efficiency-api/v1/payment_profiles/users/{USERID}?paymentProfileId={VALUE}"
```

### GET `/service-efficiency-api/v1/payment_profiles/users/{userId}/service_efficiency` [EXPERIMENTAL]

Operation to Get the Service Efficiency Payment Method for a User.

**Auth:** Cookie (`.ROBLOSECURITY`) or API Key (`x-api-key` header)

**Scopes:** `extended-services:read`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer` | Yes | User id. |

**Responses:**

- `200`: OK → `GetServiceEfficiencyPaymentMethodResponse`
- `400`: Bad Request
- `401`: Unauthorized
- `403`: Forbidden
- `404`: Not Found
- `500`: Internal Server Error
- `503`: Service Unavailable

**Response fields** (`GetServiceEfficiencyPaymentMethodResponse`)

See [GetServiceEfficiencyPaymentMethodResponse](#getserviceefficiencypaymentmethodresponse) in Models.

**Response example:**
```json
{
  "paymentProfile": "..."
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 100/minute

**Example:**
```bash
curl -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/service-efficiency-api/v1/payment_profiles/users/{USERID}/service_efficiency"
```

### PUT `/service-efficiency-api/v1/payment_profiles/users/{userId}/service_efficiency` [EXPERIMENTAL]

Operation to Set the Service Efficiency Payment Method for a User.

**Auth:** Cookie (`.ROBLOSECURITY`) or API Key (`x-api-key` header)

**Scopes:** `extended-services:write`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer` | Yes | User id. |
| `paymentProfileId` | query | `string` | Yes | Payment profile id to set. |
| `paymentProfileOwnerType` | query | `string` | Yes | Payment profile owner type. GROUP or USER. |

**Responses:**

- `200`: OK → `SetServiceEfficiencyPaymentMethodResponse`
- `400`: Bad Request
- `401`: Unauthorized
- `403`: Forbidden
- `404`: Not Found
- `412`: Precondition Failed
- `500`: Internal Server Error
- `503`: Service Unavailable

**Response fields** (`SetServiceEfficiencyPaymentMethodResponse`)

See [SetServiceEfficiencyPaymentMethodResponse](#setserviceefficiencypaymentmethodresponse) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 100/minute

**Example:**
```bash
curl -X PUT -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/service-efficiency-api/v1/payment_profiles/users/{USERID}/service_efficiency?paymentProfileId={VALUE}&paymentProfileOwnerType={VALUE}"
```

### POST `/service-efficiency-api/v1/payments/groups/{groupId}` [EXPERIMENTAL]

Operation to Submit a Manual Payment for a Group.

**Auth:** Cookie (`.ROBLOSECURITY`) or API Key (`x-api-key` header)

**Scopes:** `extended-services:write`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `groupId` | path | `integer` | Yes | Group id. |

**Request Body:** `application/json-patch+json` — Type: `any`

**Responses:**

- `200`: OK → `SubmitManualPaymentResponse`
- `400`: Bad Request
- `401`: Unauthorized
- `403`: Forbidden
- `404`: Not Found
- `500`: Internal Server Error
- `503`: Service Unavailable

**Response fields** (`SubmitManualPaymentResponse`)

See [SubmitManualPaymentResponse](#submitmanualpaymentresponse) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 100/minute

**Example:**
```bash
curl -X POST -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/service-efficiency-api/v1/payments/groups/{GROUPID}" \
  -H "Content-Type: application/json" \
  -d '"..."'
```

### POST `/service-efficiency-api/v1/payments/users/{userId}` [EXPERIMENTAL]

Operation to Submit a Manual Payment for a User.

**Auth:** Cookie (`.ROBLOSECURITY`) or API Key (`x-api-key` header)

**Scopes:** `extended-services:write`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer` | Yes | User id. |

**Request Body:** `application/json-patch+json` — Type: `any`

**Responses:**

- `200`: OK → `SubmitManualPaymentResponse`
- `400`: Bad Request
- `401`: Unauthorized
- `403`: Forbidden
- `404`: Not Found
- `500`: Internal Server Error
- `503`: Service Unavailable

**Response fields** (`SubmitManualPaymentResponse`)

See [SubmitManualPaymentResponse](#submitmanualpaymentresponse) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Rate Limits:** perApiKeyOwner: 100/minute

**Example:**
```bash
curl -X POST -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/service-efficiency-api/v1/payments/users/{USERID}" \
  -H "Content-Type: application/json" \
  -d '"..."'
```

### GET `/v1/account-creation/metadata`

Get metadata for adding auth methods.

**Server:** `https://auth.roblox.com`

**Auth:** 

**Responses:**

- `200`: OK → `Roblox.Authentication.Api.Models.AuthMethodsMetadataResponse`

**Response fields** (`Roblox.Authentication.Api.Models.AuthMethodsMetadataResponse`)

See [Roblox.Authentication.Api.Models.AuthMethodsMetadataResponse](#roblox-authentication-api-models-authmethodsmetadataresponse) in Models.

**Response example:**
```json
{
  "isEligibleForALSignup": false
}
```

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://auth.roblox.com/v1/account-creation/metadata"
```

### GET `/v1/account/pin`

Gets the account pin status.

**Server:** `https://auth.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Responses:**

- `200`: OK → `Roblox.Authentication.Api.Models.AccountPinStatusResponse`
- `401`: 0: Authorization has been denied for this request.

**Response fields** (`Roblox.Authentication.Api.Models.AccountPinStatusResponse`)

See [Roblox.Authentication.Api.Models.AccountPinStatusResponse](#roblox-authentication-api-models-accountpinstatusresponse) in Models.

**Response example:**
```json
{
  "isEnabled": false,
  "unlockedUntil": 0
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://auth.roblox.com/v1/account/pin"
```

### POST `/v1/account/pin`

Request to create the account pin.

**Server:** `https://auth.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Request Body:** `application/json` — Type: `Roblox.Authentication.Api.Models.AccountPinRequest`

See [Roblox.Authentication.Api.Models.AccountPinRequest](#roblox-authentication-api-models-accountpinrequest) in Models.

**Request example:**
```json
{
  "pin": "string",
  "reauthenticationToken": "string"
}
```

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiSuccessResponse`
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed

**Response fields** (`Roblox.Web.WebAPI.Models.ApiSuccessResponse`)

See [Roblox.Web.WebAPI.Models.ApiSuccessResponse](#roblox-web-webapi-models-apisuccessresponse) in Models.

**Response example:**
```json
{
  "success": false
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://auth.roblox.com/v1/account/pin" \
  -H "Content-Type: application/json" \
  -d '{
  "pin": "string",
  "reauthenticationToken": "string"
}'
```

### PATCH `/v1/account/pin`

Request made to update the account pin on the account.

**Server:** `https://auth.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Request Body:** `application/json` — Type: `Roblox.Authentication.Api.Models.AccountPinRequest`

See [Roblox.Authentication.Api.Models.AccountPinRequest](#roblox-authentication-api-models-accountpinrequest) in Models.

**Request example:**
```json
{
  "pin": "string",
  "reauthenticationToken": "string"
}
```

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiSuccessResponse`
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed

**Response fields** (`Roblox.Web.WebAPI.Models.ApiSuccessResponse`)

See [Roblox.Web.WebAPI.Models.ApiSuccessResponse](#roblox-web-webapi-models-apisuccessresponse) in Models.

**Response example:**
```json
{
  "success": false
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X PATCH -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://auth.roblox.com/v1/account/pin" \
  -H "Content-Type: application/json" \
  -d '{
  "pin": "string",
  "reauthenticationToken": "string"
}'
```

### DELETE `/v1/account/pin`

Request for deletes the account pin from the account.

**Server:** `https://auth.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Request Body:** `application/json` — Type: `Roblox.Authentication.Api.Models.AccountPinRequest`

See [Roblox.Authentication.Api.Models.AccountPinRequest](#roblox-authentication-api-models-accountpinrequest) in Models.

**Request example:**
```json
{
  "pin": "string",
  "reauthenticationToken": "string"
}
```

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiSuccessResponse`
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed

**Response fields** (`Roblox.Web.WebAPI.Models.ApiSuccessResponse`)

See [Roblox.Web.WebAPI.Models.ApiSuccessResponse](#roblox-web-webapi-models-apisuccessresponse) in Models.

**Response example:**
```json
{
  "success": false
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X DELETE -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://auth.roblox.com/v1/account/pin" \
  -H "Content-Type: application/json" \
  -d '{
  "pin": "string",
  "reauthenticationToken": "string"
}'
```

### POST `/v1/account/pin/lock`

Request to locks the account which has an account pin enabled.

**Server:** `https://auth.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiSuccessResponse`
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed

**Response fields** (`Roblox.Web.WebAPI.Models.ApiSuccessResponse`)

See [Roblox.Web.WebAPI.Models.ApiSuccessResponse](#roblox-web-webapi-models-apisuccessresponse) in Models.

**Response example:**
```json
{
  "success": false
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://auth.roblox.com/v1/account/pin/lock"
```

### POST `/v1/account/pin/unlock`

Requests to unlock the account pin.

**Server:** `https://auth.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Request Body:** `application/json` — Type: `Roblox.Authentication.Api.Models.AccountPinRequest`

See [Roblox.Authentication.Api.Models.AccountPinRequest](#roblox-authentication-api-models-accountpinrequest) in Models.

**Request example:**
```json
{
  "pin": "string",
  "reauthenticationToken": "string"
}
```

**Responses:**

- `200`: OK → `Roblox.Authentication.Api.Models.AccountPinResponse`
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed

**Response fields** (`Roblox.Authentication.Api.Models.AccountPinResponse`)

See [Roblox.Authentication.Api.Models.AccountPinResponse](#roblox-authentication-api-models-accountpinresponse) in Models.

**Response example:**
```json
{
  "unlockedUntil": 0
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://auth.roblox.com/v1/account/pin/unlock" \
  -H "Content-Type: application/json" \
  -d '{
  "pin": "string",
  "reauthenticationToken": "string"
}'
```

### GET `/v1/account/settings/account-country`

Get a user's current account country setting.

**Server:** `https://accountsettings.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Responses:**

- `200`: OK → `Roblox.AccountSettings.Api.Models.Response.AccountCountrySettingsResponse`
- `401`: 0: Authorization has been denied for this request.

**Response fields** (`Roblox.AccountSettings.Api.Models.Response.AccountCountrySettingsResponse`)

See [Roblox.AccountSettings.Api.Models.Response.AccountCountrySettingsResponse](#roblox-accountsettings-api-models-response-accountcountrysettingsresponse) in Models.

**Response example:**
```json
{
  "value": {
    "countryName": "string",
    "subdivisionIso": "string",
    "localizedSubdivision": "string",
    "localizedName": "string",
    "countryId": 0
  }
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://accountsettings.roblox.com/v1/account/settings/account-country"
```

### POST `/v1/account/settings/account-country`

Updates the user's account country.

**Server:** `https://accountsettings.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Request Body:** `application/json` — Type: `Roblox.AccountSettings.Api.UpdateAccountCountryRequest`

See [Roblox.AccountSettings.Api.UpdateAccountCountryRequest](#roblox-accountsettings-api-updateaccountcountryrequest) in Models.

**Request example:**
```json
{
  "targetCountryId": 0
}
```

**Responses:**

- `200`: OK → `Roblox.AccountSettings.Api.Models.Response.UpdateAccountCountryResponse`
- `400`: 1: InvalidRequest
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 2: OperationNotPermitted
- `404`: 2: OperationNotPermitted
- `500`: 0: Unknown

**Response fields** (`Roblox.AccountSettings.Api.Models.Response.UpdateAccountCountryResponse`)

See [Roblox.AccountSettings.Api.Models.Response.UpdateAccountCountryResponse](#roblox-accountsettings-api-models-response-updateaccountcountryresponse) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://accountsettings.roblox.com/v1/account/settings/account-country" \
  -H "Content-Type: application/json" \
  -d '{
  "targetCountryId": 0
}'
```

### GET `/v1/account/settings/metadata`

Returns metadata used by the account settings page

**Server:** `https://accountsettings.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Responses:**

- `200`: OK → `Roblox.AccountSettings.Api.Models.AccountsSettingsMetadataModel`
- `401`: 0: Authorization has been denied for this request.

**Response fields** (`Roblox.AccountSettings.Api.Models.AccountsSettingsMetadataModel`)

See [Roblox.AccountSettings.Api.Models.AccountsSettingsMetadataModel](#roblox-accountsettings-api-models-accountssettingsmetadatamodel) in Models.

**Response example:**
```json
{
  "IsAccountsRestrictionsSpamBugFixEnabled": false,
  "MaximumParentalControlsMonthlySpendLimitInUSD": 0,
  "IsParentalMonthlyLimitInUIEnabled": false,
  "IsParentalNotificationSettingsInUIEnabled": false,
  "IsContentControlsEnabled": false
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://accountsettings.roblox.com/v1/account/settings/metadata"
```

### POST `/v1/account/upgrade`

Attaches a sign-in credential to the calling account.

The caller is the account being upgraded, so the request carries no user ID and the
session is the authorization. The call is safe to retry: each field is compared against
the account first, and a field the account already holds is dropped rather than rewritten.

The moderation filter is bypassed because an account held by a birthday compliance
restriction is Suppressed and lifts that restriction through this call. Every upgrade type
still passes its own eligibility gate.

**Server:** `https://auth.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Request Body:** `application/json` — Type: `Roblox.Authentication.Api.Models.AccountUpgradeRequest`

See [Roblox.Authentication.Api.Models.AccountUpgradeRequest](#roblox-authentication-api-models-accountupgraderequest) in Models.

**Request example:**
```json
{
  "upgradeType": 0,
  "username": "string",
  "password": "string",
  "birthday": "2024-01-01T00:00:00Z",
  "email": "string",
  "gender": 1
}
```

**Responses:**

- `200`: OK → `Roblox.Authentication.Api.Models.AccountUpgradeResponse`
- `400`: 5: Account upgrade requires a password. 6: Invalid Birthday. 8: The upgrade type is missing, unknown, or not available. 9: A supplied field is not allowed for the declared upgrade type. 10: A birthday is required for this account. 11: Invalid username. 12: This username is already in use. 13: Invalid password. 14: Invalid email address. 15: Too many accounts use this email address. 17: Password is not complex enough. 18: Password is too similar to username.
- `401`: 0: Authorization has been denied for this request. 3: Not eligible for account upgrade.
- `403`: 0: Token Validation Failed 3: Not eligible for account upgrade. 16: This account already holds a sign-in credential.
- `429`: 4: Too many attempts. Please wait a bit.
- `500`: 1: Unknown Error 7: Account upgrade failed.
- `503`: 2: Account upgrade is disabled.

**Response fields** (`Roblox.Authentication.Api.Models.AccountUpgradeResponse`)

See [Roblox.Authentication.Api.Models.AccountUpgradeResponse](#roblox-authentication-api-models-accountupgraderesponse) in Models.

**Response example:**
```json
{
  "userId": 0,
  "username": "string"
}
```

**Error handling:** `429`: Retry with exponential backoff (start at 1s). `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://auth.roblox.com/v1/account/upgrade" \
  -H "Content-Type: application/json" \
  -d '{
  "upgradeType": 0,
  "username": "string",
  "password": "string",
  "birthday": "2024-01-01T00:00:00Z",
  "email": "string",
  "gender": 1
}'
```

### GET `/v1/announcements`

Migrate from RobloxWebsite project, return news notification for Private Message page

**Server:** `https://privatemessages.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Responses:**

- `200`: OK → `Roblox.PrivateMessages.Api.Models.GetAnnouncementsResponse`
- `400`: 2: Message does not exist or the current user is not authorized to view it.
- `401`: 0: Authorization has been denied for this request.

**Response fields** (`Roblox.PrivateMessages.Api.Models.GetAnnouncementsResponse`)

See [Roblox.PrivateMessages.Api.Models.GetAnnouncementsResponse](#roblox-privatemessages-api-models-getannouncementsresponse) in Models.

**Response example:**
```json
{
  "collection": [
    {
      "id": "...",
      "sender": "...",
      "subject": "...",
      "body": "...",
      "created": "...",
      "updated": "..."
    }
  ],
  "totalCollectionSize": 0
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://privatemessages.roblox.com/v1/announcements"
```

### GET `/v1/announcements/metadata`

**Server:** `https://privatemessages.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Responses:**

- `200`: OK → `Roblox.PrivateMessages.Api.Models.AnnouncementsMetadataResponse`
- `401`: 0: Authorization has been denied for this request.

**Response fields** (`Roblox.PrivateMessages.Api.Models.AnnouncementsMetadataResponse`)

See [Roblox.PrivateMessages.Api.Models.AnnouncementsMetadataResponse](#roblox-privatemessages-api-models-announcementsmetadataresponse) in Models.

**Response example:**
```json
{
  "numOfAnnouncements": 0
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://privatemessages.roblox.com/v1/announcements/metadata"
```

### GET `/v1/auth/metadata`

Gets Auth meta data

**Server:** `https://auth.roblox.com`

**Auth:** 

**Responses:**

- `200`: OK → `Roblox.Authentication.Api.Models.AuthMetaDataResponse`

**Response fields** (`Roblox.Authentication.Api.Models.AuthMetaDataResponse`)

See [Roblox.Authentication.Api.Models.AuthMetaDataResponse](#roblox-authentication-api-models-authmetadataresponse) in Models.

**Response example:**
```json
{
  "cookieLawNoticeTimeout": 0
}
```

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://auth.roblox.com/v1/auth/metadata"
```

### GET `/v1/birthdate` *(deprecated)*

Get the user's birthdate

Replaced by users.roblox.com/v1/birthdate

**Server:** `https://accountinformation.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Responses:**

- `200`: OK → `Roblox.AccountInformation.Api.Models.BirthdateResponse`
- `400`: 1: User not found.
- `401`: 0: Authorization has been denied for this request.

**Response fields** (`Roblox.AccountInformation.Api.Models.BirthdateResponse`)

See [Roblox.AccountInformation.Api.Models.BirthdateResponse](#roblox-accountinformation-api-models-birthdateresponse) in Models.

**Response example:**
```json
{
  "birthMonth": 0,
  "birthDay": 0,
  "birthYear": 0
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://accountinformation.roblox.com/v1/birthdate"
```

### POST `/v1/birthdate`

Update the user's birthdate

**Server:** `https://users.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Request Body:** `application/json` — Type: `Roblox.Users.Api.BirthdateRequest`

See [Roblox.Users.Api.BirthdateRequest](#roblox-users-api-birthdaterequest) in Models.

**Request example:**
```json
{
  "birthMonth": 0,
  "birthDay": 0,
  "birthYear": 0,
  "password": "string"
}
```

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: 1: User not found. 4: The birthdate provided is invalid. 8: Password is incorrect.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 2: PIN is locked. 5: Invalid birthdate change.
- `500`: 0: An unknown error occured. 5: Invalid birthdate change.

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://users.roblox.com/v1/birthdate" \
  -H "Content-Type: application/json" \
  -d '{
  "birthMonth": 0,
  "birthDay": 0,
  "birthYear": 0,
  "password": "string"
}'
```

### GET `/v1/birthdate#users.roblox.com`

Get the user's birthdate

**Server:** `https://users.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Responses:**

- `200`: OK → `Roblox.Users.Api.BirthdateResponse`
- `400`: 1: User not found.
- `401`: 0: Authorization has been denied for this request.

**Response fields** (`Roblox.Users.Api.BirthdateResponse`)

See [Roblox.Users.Api.BirthdateResponse](#roblox-users-api-birthdateresponse) in Models.

**Response example:**
```json
{
  "birthMonth": 0,
  "birthDay": 0,
  "birthYear": 0
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://users.roblox.com/v1/birthdate#users.roblox.com"
```

### GET `/v1/client-assertion`

Creates a client assertion to be used when generating an auth ticket.

**Server:** `https://auth.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Responses:**

- `200`: OK → `Roblox.Authentication.Api.Models.Response.GetClientAssertionResponse`
- `401`: 0: Authorization has been denied for this request.

**Response fields** (`Roblox.Authentication.Api.Models.Response.GetClientAssertionResponse`)

See [Roblox.Authentication.Api.Models.Response.GetClientAssertionResponse](#roblox-authentication-api-models-response-getclientassertionresponse) in Models.

**Response example:**
```json
{
  "clientAssertion": "string"
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://auth.roblox.com/v1/client-assertion"
```

### GET `/v1/description` *(deprecated)*

Get the user's description

Replaced by users.roblox.com/v1/description

**Server:** `https://accountinformation.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Responses:**

- `200`: OK → `Roblox.AccountInformation.Api.Models.DescriptionResponse`
- `400`: 1: User not found.
- `401`: 0: Authorization has been denied for this request.

**Response fields** (`Roblox.AccountInformation.Api.Models.DescriptionResponse`)

See [Roblox.AccountInformation.Api.Models.DescriptionResponse](#roblox-accountinformation-api-models-descriptionresponse) in Models.

**Response example:**
```json
{
  "description": "string"
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://accountinformation.roblox.com/v1/description"
```

### POST `/v1/description` *(deprecated)*

Update the user's description

Replaced by users.roblox.com/v1/description

**Server:** `https://accountinformation.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Request Body:** `application/json` — Type: `Roblox.AccountInformation.Api.Models.DescriptionRequest`

See [Roblox.AccountInformation.Api.Models.DescriptionRequest](#roblox-accountinformation-api-models-descriptionrequest) in Models.

**Request example:**
```json
{
  "description": "string"
}
```

**Responses:**

- `200`: OK → `Roblox.AccountInformation.Api.Models.DescriptionResponse`
- `400`: 1: User not found.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed
- `500`: 0: An unknown error occured.
- `503`: 3: This feature is currently disabled. Please try again later.

**Response fields** (`Roblox.AccountInformation.Api.Models.DescriptionResponse`)

See [Roblox.AccountInformation.Api.Models.DescriptionResponse](#roblox-accountinformation-api-models-descriptionresponse) in Models.

**Response example:**
```json
{
  "description": "string"
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://accountinformation.roblox.com/v1/description" \
  -H "Content-Type: application/json" \
  -d '{
  "description": "string"
}'
```

### GET `/v1/description#users.roblox.com`

Get the user's description

**Server:** `https://users.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Responses:**

- `200`: OK → `Roblox.Users.Api.DescriptionResponse`
- `400`: 1: User not found.
- `401`: 0: Authorization has been denied for this request.

**Response fields** (`Roblox.Users.Api.DescriptionResponse`)

See [Roblox.Users.Api.DescriptionResponse](#roblox-users-api-descriptionresponse) in Models.

**Response example:**
```json
{
  "description": "string"
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://users.roblox.com/v1/description#users.roblox.com"
```

### POST `/v1/description#users.roblox.com`

Update the user's description

**Server:** `https://users.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Request Body:** `application/json` — Type: `Roblox.Users.Api.DescriptionRequest`

See [Roblox.Users.Api.DescriptionRequest](#roblox-users-api-descriptionrequest) in Models.

**Request example:**
```json
{
  "description": "string"
}
```

**Responses:**

- `200`: OK → `Roblox.Users.Api.DescriptionResponse`
- `400`: 1: User not found.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 2: PIN is locked.
- `500`: 0: An unknown error occured.
- `503`: 3: This feature is currently disabled. Please try again later.

**Response fields** (`Roblox.Users.Api.DescriptionResponse`)

See [Roblox.Users.Api.DescriptionResponse](#roblox-users-api-descriptionresponse) in Models.

**Response example:**
```json
{
  "description": "string"
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://users.roblox.com/v1/description#users.roblox.com" \
  -H "Content-Type: application/json" \
  -d '{
  "description": "string"
}'
```

### GET `/v1/email`

Gets the authenticated user's email address and verified status

**Server:** `https://accountsettings.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Responses:**

- `200`: OK → `Roblox.AccountSettings.Api.EmailResponse`
- `401`: 0: Authorization has been denied for this request.

**Response fields** (`Roblox.AccountSettings.Api.EmailResponse`)

See [Roblox.AccountSettings.Api.EmailResponse](#roblox-accountsettings-api-emailresponse) in Models.

**Response example:**
```json
{
  "emailAddress": "string",
  "verified": false,
  "canBypassPasswordForEmailUpdate": false
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://accountsettings.roblox.com/v1/email"
```

### POST `/v1/email`

Updates the authenticated user's email address

**Server:** `https://accountsettings.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: 8: Password is incorrect. 9: Invalid email address.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 2: This feature is currently disabled. Please try again later. 3: There are too many accounts associated with this email address. 11: You must be on the Corporate network to log in.
- `409`: 4: This is already the current email.
- `429`: 6: Too many attempts to update email. Please try again later. 7: Too many attempts to send verification email. Please try again later.
- `503`: 2: This feature is currently disabled. Please try again later.

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `429`: Retry with exponential backoff (start at 1s). `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://accountsettings.roblox.com/v1/email" \
  -H "Content-Type: application/json" \
  -d '{"key": "value"}'
```

### PATCH `/v1/email`

Updates the authenticated user's email address

**Server:** `https://accountsettings.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: 8: Password is incorrect. 9: Invalid email address.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 2: This feature is currently disabled. Please try again later. 3: There are too many accounts associated with this email address. 11: You must be on the Corporate network to log in.
- `409`: 4: This is already the current email.
- `429`: 6: Too many attempts to update email. Please try again later. 7: Too many attempts to send verification email. Please try again later.
- `503`: 2: This feature is currently disabled. Please try again later.

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `429`: Retry with exponential backoff (start at 1s). `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X PATCH -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://accountsettings.roblox.com/v1/email" \
  -H "Content-Type: application/json" \
  -d '{"key": "value"}'
```

### POST `/v1/email/verify`

Verify the user's email address from token

**Server:** `https://accountinformation.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Request Body:** `application/json` — Type: `Roblox.AccountInformation.Api.Models.VerifyEmailRequest`

See [Roblox.AccountInformation.Api.Models.VerifyEmailRequest](#roblox-accountinformation-api-models-verifyemailrequest) in Models.

**Request example:**
```json
{
  "ticket": "string"
}
```

**Responses:**

- `200`: OK → `Roblox.AccountInformation.Api.Models.VerifyEmailResponse`
- `403`: 0: Token Validation Failed

**Response fields** (`Roblox.AccountInformation.Api.Models.VerifyEmailResponse`)

See [Roblox.AccountInformation.Api.Models.VerifyEmailResponse](#roblox-accountinformation-api-models-verifyemailresponse) in Models.

**Response example:**
```json
{
  "verifiedUserHatAssetId": 0
}
```

**Error handling:** `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://accountinformation.roblox.com/v1/email/verify" \
  -H "Content-Type: application/json" \
  -d '{
  "ticket": "string"
}'
```

### POST `/v1/email/verify#accountsettings.roblox.com`

Send verify email to the authenticated user's email address

**Server:** `https://accountsettings.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Request Body:** `application/json` — Type: `Roblox.AccountSettings.Api.SendVerifyEmailRequest`

See [Roblox.AccountSettings.Api.SendVerifyEmailRequest](#roblox-accountsettings-api-sendverifyemailrequest) in Models.

**Request example:**
```json
{
  "freeItem": false,
  "isAdsAccount": false
}
```

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: 10: No email address is associated with the account.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 2: This feature is currently disabled. Please try again later. 11: You must be on the Corporate network to log in.
- `409`: 5: The email is already verified.
- `429`: 7: Too many attempts to send verification email. Please try again later.
- `503`: 2: This feature is currently disabled. Please try again later.

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `429`: Retry with exponential backoff (start at 1s). `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://accountsettings.roblox.com/v1/email/verify#accountsettings.roblox.com" \
  -H "Content-Type: application/json" \
  -d '{
  "freeItem": false,
  "isAdsAccount": false
}'
```

### GET `/v1/emails`

Gets the authenticated user's verified email and pending (unverified) email if one exists

**Server:** `https://accountsettings.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Responses:**

- `200`: OK → `Roblox.AccountSettings.Api.CurrentEmailsResponse`
- `401`: 0: Authorization has been denied for this request.

**Response fields** (`Roblox.AccountSettings.Api.CurrentEmailsResponse`)

See [Roblox.AccountSettings.Api.CurrentEmailsResponse](#roblox-accountsettings-api-currentemailsresponse) in Models.

**Response example:**
```json
{
  "verifiedEmail": "string",
  "pendingEmail": "string"
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://accountsettings.roblox.com/v1/emails"
```

### POST `/v1/external/access`

Signs a user up for Roblox and links the account to the authenticated external provider ID.

**Server:** `https://auth.roblox.com`

**Auth:** 

**Request Body:** `application/json` — Type: `Roblox.Authentication.Api.Models.Request.ExternalAccessRequest`

See [Roblox.Authentication.Api.Models.Request.ExternalAccessRequest](#roblox-authentication-api-models-request-externalaccessrequest) in Models.

**Request example:**
```json
{
  "authenticationProof": "string",
  "identityProviderPlatformType": 0,
  "postAuthenticationIntentId": "string",
  "additionalInfoPayload": "..."
}
```

**Responses:**

- `200`: OK → `Roblox.Authentication.Api.Models.Response.ExternalIdentityGateway.ExternalIdentityAccessResponse`

**Response fields** (`Roblox.Authentication.Api.Models.Response.ExternalIdentityGateway.ExternalIdentityAccessResponse`)

See [Roblox.Authentication.Api.Models.Response.ExternalIdentityGateway.ExternalIdentityAccessResponse](#roblox-authentication-api-models-response-externalidentitygateway-externalidentityaccessresponse) in Models.

**Response example:**
```json
{
  "placeId": 0,
  "isolationContext": "string",
  "launchData": "string"
}
```

**Example:**
```bash
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://auth.roblox.com/v1/external/access" \
  -H "Content-Type: application/json" \
  -d '{
  "authenticationProof": "string",
  "identityProviderPlatformType": 0,
  "postAuthenticationIntentId": "string",
  "additionalInfoPayload": "..."
}'
```

### POST `/v1/external/login`

Logs in a user to Roblox based on the user's authenticated external provider session

**Server:** `https://auth.roblox.com`

**Auth:** 

**Request Body:** `application/json` — Type: `Roblox.Authentication.Api.Models.Request.ExternalLoginRequest`

See [Roblox.Authentication.Api.Models.Request.ExternalLoginRequest](#roblox-authentication-api-models-request-externalloginrequest) in Models.

**Request example:**
```json
{
  "identityProvider": 0,
  "additionalData": "...",
  "authenticationProof": "string"
}
```

**Responses:**

- `200`: OK → `Roblox.Authentication.Api.Models.Response.ExternalIdentityGateway.ExternalLoginResponse`
- `400`: 30: Platform is not supported for SSO login. 47: A platform identity proof is required for SSO login.
- `401`: 31: No linked account found for SSO login.
- `403`: 0: Token Validation Failed 44: Login is unavailable in your country.
- `500`: 0: An unexpected error occurred.
- `501`: 0: An unexpected error occurred.

**Response fields** (`Roblox.Authentication.Api.Models.Response.ExternalIdentityGateway.ExternalLoginResponse`)

See [Roblox.Authentication.Api.Models.Response.ExternalIdentityGateway.ExternalLoginResponse](#roblox-authentication-api-models-response-externalidentitygateway-externalloginresponse) in Models.

**Response example:**
```json
{
  "success": false
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://auth.roblox.com/v1/external/login" \
  -H "Content-Type: application/json" \
  -d '{
  "identityProvider": 0,
  "additionalData": "...",
  "authenticationProof": "string"
}'
```

### POST `/v1/external/loginAndLink`

Deprecated endpoint
Logins in a user to Roblox, then links the Roblox account to the external provider ID

**Server:** `https://auth.roblox.com`

**Auth:** 

**Request Body:** `application/json` — Type: `Roblox.Authentication.Api.Models.Request.ExternalLoginAndLinkRequest`

See [Roblox.Authentication.Api.Models.Request.ExternalLoginAndLinkRequest](#roblox-authentication-api-models-request-externalloginandlinkrequest) in Models.

**Request example:**
```json
{
  "ctype": 0,
  "cvalue": "string",
  "password": "string",
  "authenticationProof": "string",
  "IdentityProviderPlatformType": 0,
  "additionalInfoPayload": "..."
}
```

**Responses:**

- `200`: OK → `Roblox.Authentication.Api.Models.LoginResponse`
- `403`: 0: Token Validation Failed 44: Login is unavailable in your country.

**Response fields** (`Roblox.Authentication.Api.Models.LoginResponse`)

See [Roblox.Authentication.Api.Models.LoginResponse](#roblox-authentication-api-models-loginresponse) in Models.

**Response example:**
```json
{
  "user": {
    "id": 0,
    "name": "string",
    "displayName": "string"
  },
  "twoStepVerificationData": {
    "mediaType": 0,
    "ticket": "string"
  },
  "identityVerificationLoginTicket": "string",
  "isBanned": false,
  "accountBlob": "string",
  "shouldUpdateEmail": false
}
```

**Error handling:** `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://auth.roblox.com/v1/external/loginAndLink" \
  -H "Content-Type: application/json" \
  -d '{
  "ctype": 0,
  "cvalue": "string",
  "password": "string",
  "authenticationProof": "string",
  "IdentityProviderPlatformType": 0,
  "additionalInfoPayload": "..."
}'
```

### POST `/v1/external/signup`

Signs a user up for Roblox and links the account to the authenticated external provider ID

**Server:** `https://auth.roblox.com`

**Auth:** 

**Request Body:** `application/json` — Type: `Roblox.Authentication.Api.Models.Request.ExternalSignupRequest`

See [Roblox.Authentication.Api.Models.Request.ExternalSignupRequest](#roblox-authentication-api-models-request-externalsignuprequest) in Models.

**Request example:**
```json
{
  "username": "string",
  "password": "string",
  "birthday": "2024-01-01T00:00:00Z",
  "locale": "string",
  "authenticationProof": "string",
  "IdentityProviderPlatformType": 0
}
```

**Responses:**

- `200`: OK
- `403`: 0: Token Validation Failed 36: Password is not complex enough. 37: Password is too similar to username.

**Error handling:** `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://auth.roblox.com/v1/external/signup" \
  -H "Content-Type: application/json" \
  -d '{
  "username": "string",
  "password": "string",
  "birthday": "2024-01-01T00:00:00Z",
  "locale": "string",
  "authenticationProof": "string",
  "IdentityProviderPlatformType": 0
}'
```

### POST `/v1/external/unlink`

Unlink the logged in Roblox account from the current external provider ID

**Server:** `https://auth.roblox.com`

**Auth:** 

**Request Body:** `application/json` — Type: `Roblox.Authentication.Api.Models.Request.ExternalUnlinkRequest`

See [Roblox.Authentication.Api.Models.Request.ExternalUnlinkRequest](#roblox-authentication-api-models-request-externalunlinkrequest) in Models.

**Request example:**
```json
{
  "IdentityProviderPlatformType": 0,
  "additionalInfoPayload": "..."
}
```

**Responses:**

- `200`: OK
- `403`: 0: Token Validation Failed

**Error handling:** `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://auth.roblox.com/v1/external/unlink" \
  -H "Content-Type: application/json" \
  -d '{
  "IdentityProviderPlatformType": 0,
  "additionalInfoPayload": "..."
}'
```

### POST `/v1/external/{identityProviderId}/sso/native/nonce`

Reserves a nonce for a native SSO sign-in attempt.

The web flow gets its nonce from M:Roblox.Authentication.Api.Controllers.V1.ExternalIdentitiesGatewayController.OAuthInit(System.Int64,System.String,System.Threading.CancellationToken), which native clients never call
because they have no authorization redirect. They call this instead, pass the nonce to the
provider SDK, and post the resulting id_token to /access.
            
The client must pass this value to the SDK verbatim. Both providers treat the nonce as an
opaque string and echo it into the id_token unchanged, and redemption looks the value up as
issued. The SHA256(nonce) convention seen in Apple examples belongs to Firebase, which hashes
on its own side before comparing; hashing here would make the lookup miss.

**Server:** `https://auth.roblox.com`

**Auth:** 

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `identityProviderId` | path | `integer` | Yes |  |

**Responses:**

- `200`: OK → `Roblox.Authentication.Api.Models.Response.ExternalIdentityGateway.ExternalIdentityNonceResponse`

**Response fields** (`Roblox.Authentication.Api.Models.Response.ExternalIdentityGateway.ExternalIdentityNonceResponse`)

See [Roblox.Authentication.Api.Models.Response.ExternalIdentityGateway.ExternalIdentityNonceResponse](#roblox-authentication-api-models-response-externalidentitygateway-externalidentitynonceresponse) in Models.

**Response example:**
```json
{
  "nonce": "string"
}
```

**Example:**
```bash
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://auth.roblox.com/v1/external/{IDENTITYPROVIDERID}/sso/native/nonce"
```

### GET `/v1/external/{identityProviderId}/sso/oauth/callback`

OAuth callback for identity providers that return the authorization code on a GET redirect (Okta, Google).

**Server:** `https://auth.roblox.com`

**Auth:** 

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `identityProviderId` | path | `integer` | Yes |  |
| `code` | query | `string` | Yes |  |
| `state` | query | `string` | Yes |  |

**Responses:**

- `302`: Found

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://auth.roblox.com/v1/external/{IDENTITYPROVIDERID}/sso/oauth/callback?code={VALUE}&state={VALUE}"
```

### POST `/v1/external/{identityProviderId}/sso/oauth/callback`

OAuth callback for identity providers that POST the authorization code as form fields (Apple form_post).
Apple's first-auth `user` JSON is parsed and carried to identity storage; the form
`id_token` is ignored. Web login exchanges code via PKCE and does
not treat a form id_token as proof.

**Server:** `https://auth.roblox.com`

**Auth:** 

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `identityProviderId` | path | `integer` | Yes |  |

**Responses:**

- `302`: Found

**Example:**
```bash
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://auth.roblox.com/v1/external/{IDENTITYPROVIDERID}/sso/oauth/callback"
```

### GET `/v1/external/{identityProviderId}/sso/oauth/init`

Signs a user up for Roblox and links the account to the authenticated external provider ID via OAuth.

Stored with the PKCE secrets rather than accepted at the callback, where it would let anyone turn a
plain web login into a redirect carrying a live session.

**Server:** `https://auth.roblox.com`

**Auth:** 

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `identityProviderId` | path | `integer` | Yes | The identity provider to authenticate against. |
| `postAuthenticationIntentId` | query | `string` | Yes | Which post-authentication intent to carry out at the end of the handshake. Optional, and omitting it selects the provider's web redirect. |

**Responses:**

- `302`: Found

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://auth.roblox.com/v1/external/{IDENTITYPROVIDERID}/sso/oauth/init?postAuthenticationIntentId={VALUE}"
```

### POST `/v1/external/{identityProviderId}/sso/saml/assertion-consumer-service`

SAML Assertion Consumer Service endpoint that external identity provider calls post user authentication.

**Server:** `https://auth.roblox.com`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `identityProviderId` | path | `integer` | Yes |  |

**Request Body:** `multipart/form-data` — Type: `object`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `SAMLResponse` | `string` | No |  |
| `RelayState` | `string` | No |  |

**Request example:**
```json
{
  "SAMLResponse": "string",
  "RelayState": "string"
}
```

**Responses:**

- `302`: Found

**Example:**
```bash
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://auth.roblox.com/v1/external/{IDENTITYPROVIDERID}/sso/saml/assertion-consumer-service" \
  -F "SAMLResponse=string" \
  -F "RelayState=string"
```

### GET `/v1/games/multiget-playability-status` [EXPERIMENTAL]

Gets a list of universe playability statuses for the authenticated user

**Server:** `https://games.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeIds` | query | `integer[]` | Yes | A list of universe Ids. Cannot exceed a maximum of 50 IDs. |

**Responses:**

- `200`: OK → `Roblox.Games.Api.Models.Response.PlayabilityStatusResponse[]`
- `400`: 8: The universe IDs specified are invalid. 9: Too many universe IDs were requested.
- `429`: 4: Too many requests have been made.

**Response fields** (`Roblox.Games.Api.Models.Response.PlayabilityStatusResponse[]`)

See [Roblox.Games.Api.Models.Response.PlayabilityStatusResponse](#roblox-games-api-models-response-playabilitystatusresponse) in Models.

**Error handling:** `429`: Retry with exponential backoff (start at 1s). 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://games.roblox.com/v1/games/multiget-playability-status?universeIds={VALUE}"
```

### GET `/v1/gender` *(deprecated)*

Get the user's gender

Replaced by users.roblox.com/v1/gender

**Server:** `https://accountinformation.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Responses:**

- `200`: OK → `Roblox.AccountInformation.Api.Models.GenderResponse`
- `400`: 1: User not found.
- `401`: 0: Authorization has been denied for this request.

**Response fields** (`Roblox.AccountInformation.Api.Models.GenderResponse`)

See [Roblox.AccountInformation.Api.Models.GenderResponse](#roblox-accountinformation-api-models-genderresponse) in Models.

**Response example:**
```json
{
  "gender": 0
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://accountinformation.roblox.com/v1/gender"
```

### POST `/v1/gender` *(deprecated)*

Update the user's gender

Replaced by users.roblox.com/v1/gender

**Server:** `https://accountinformation.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Request Body:** `application/json` — Type: `Roblox.AccountInformation.Api.Models.GenderRequest`

See [Roblox.AccountInformation.Api.Models.GenderRequest](#roblox-accountinformation-api-models-genderrequest) in Models.

**Request example:**
```json
{
  "gender": "string"
}
```

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: 1: User not found. 6: The gender provided is invalid.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed
- `500`: 0: An unknown error occured.

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://accountinformation.roblox.com/v1/gender" \
  -H "Content-Type: application/json" \
  -d '{
  "gender": "string"
}'
```

### GET `/v1/gender#users.roblox.com`

Get the user's gender

**Server:** `https://users.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Responses:**

- `200`: OK → `Roblox.Users.Api.GenderResponse`
- `400`: 1: User not found.
- `401`: 0: Authorization has been denied for this request.

**Response fields** (`Roblox.Users.Api.GenderResponse`)

See [Roblox.Users.Api.GenderResponse](#roblox-users-api-genderresponse) in Models.

**Response example:**
```json
{
  "gender": 0
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://users.roblox.com/v1/gender#users.roblox.com"
```

### POST `/v1/gender#users.roblox.com`

Update the user's gender

**Server:** `https://users.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Request Body:** `application/json` — Type: `Roblox.Users.Api.GenderRequest`

See [Roblox.Users.Api.GenderRequest](#roblox-users-api-genderrequest) in Models.

**Request example:**
```json
{
  "gender": 1
}
```

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: 1: User not found. 6: The gender provided is invalid.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 2: PIN is locked.
- `500`: 0: An unknown error occured.

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://users.roblox.com/v1/gender#users.roblox.com" \
  -H "Content-Type: application/json" \
  -d '{
  "gender": 1
}'
```

### POST `/v1/identity-verification/login`

Endpoint for login with identity verification

**Server:** `https://auth.roblox.com`

**Auth:** 

**Request Body:** `application/json` — Type: `Roblox.Authentication.Api.Models.Request.IdentityVerificationLoginRequest`

See [Roblox.Authentication.Api.Models.Request.IdentityVerificationLoginRequest](#roblox-authentication-api-models-request-identityverificationloginrequest) in Models.

**Request example:**
```json
{
  "loginTicket": "string",
  "resultToken": "string"
}
```

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `403`: 0: Token Validation Failed 1: Invalid login ticket. 2: Invalid result token. 3: Invalid user. 4: Authentication failure. 44: Login is unavailable in your country.

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://auth.roblox.com/v1/identity-verification/login" \
  -H "Content-Type: application/json" \
  -d '{
  "loginTicket": "string",
  "resultToken": "string"
}'
```

### POST `/v1/identity/initialize-login`

Initiates identifier-first login flow by returning a list of login methods for user(s).

**Server:** `https://auth.roblox.com`

**Auth:** 

**Request Body:** `application/json` — Type: `Roblox.Authentication.Api.Models.Request.InitializeLoginRequest`

See [Roblox.Authentication.Api.Models.Request.InitializeLoginRequest](#roblox-authentication-api-models-request-initializeloginrequest) in Models.

**Request example:**
```json
{
  "ctype": 0,
  "cvalue": "string",
  "captchaId": "string",
  "captchaToken": "string",
  "captchaProvider": "string",
  "challengeId": "string"
}
```

**Responses:**

- `200`: OK → `Roblox.Authentication.Api.Models.Response.InitializeLoginResponse`
- `400`: 3: User identifier and type are required.
- `403`: 0: Token Validation Failed 2: Invalid user identifier. 4: No login methods available. Please use account recovery.
- `500`: 0: An unknown error occurred.
- `503`: 1: This feature is disabled.

**Response fields** (`Roblox.Authentication.Api.Models.Response.InitializeLoginResponse`)

See [Roblox.Authentication.Api.Models.Response.InitializeLoginResponse](#roblox-authentication-api-models-response-initializeloginresponse) in Models.

**Response example:**
```json
{
  "loginMethods": [
    {
      "method": "...",
      "priority": "..."
    }
  ]
}
```

**Error handling:** `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://auth.roblox.com/v1/identity/initialize-login" \
  -H "Content-Type: application/json" \
  -d '{
  "ctype": 0,
  "cvalue": "string",
  "captchaId": "string",
  "captchaToken": "string",
  "captchaProvider": "string",
  "challengeId": "string"
}'
```

### POST `/v1/login`

Authenticates a user.

**Server:** `https://auth.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Request Body:** `application/json` — Type: `Roblox.Authentication.Api.Models.LoginRequest`

See [Roblox.Authentication.Api.Models.LoginRequest](#roblox-authentication-api-models-loginrequest) in Models.

**Request example:**
```json
{
  "ctype": 0,
  "cvalue": "string",
  "password": "string",
  "userId": 0,
  "securityQuestionSessionId": "string",
  "securityQuestionRedemptionToken": "string"
}
```

**Responses:**

- `200`: Successfully logged in. → `Roblox.Authentication.Api.Models.LoginResponse`
- `400`: 0: An unexpected error occurred. 3: Username and Password are required. Please try again. 8: Login with received credential type is not supported.
- `403`: 0: Token Validation Failed 1: Incorrect username or password. Please try again. 2: You must pass the robot test before logging in. 4: Account has been locked. Please request a password reset. 5: Unable to login. Please use Social Network sign on. 6: Account issue. Please contact Support. 9: Unable to login with provided credentials. Default login is required. 10: Received credentials are unverified. 12: Existing login session found. Please log out first. 14: The account is unable to log in. Please log in to the LuoBu app. 15: Too many attempts. Please wait a bit. 27: The account is unable to login. Please log in with the VNG app. 44: Login is unavailable in your country.
- `429`: 7: Too many attempts. Please wait a bit.
- `503`: 11: Service unavailable. Please try again.

**Response fields** (`Roblox.Authentication.Api.Models.LoginResponse`)

See [Roblox.Authentication.Api.Models.LoginResponse](#roblox-authentication-api-models-loginresponse) in Models.

**Response example:**
```json
{
  "user": {
    "id": 0,
    "name": "string",
    "displayName": "string"
  },
  "twoStepVerificationData": {
    "mediaType": 0,
    "ticket": "string"
  },
  "identityVerificationLoginTicket": "string",
  "isBanned": false,
  "accountBlob": "string",
  "shouldUpdateEmail": false
}
```

**Error handling:** `429`: Retry with exponential backoff (start at 1s). `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://auth.roblox.com/v1/login" \
  -H "Content-Type: application/json" \
  -d '{
  "ctype": 0,
  "cvalue": "string",
  "password": "string",
  "userId": 0,
  "securityQuestionSessionId": "string",
  "securityQuestionRedemptionToken": "string"
}'
```

### POST `/v1/login/linked`

Endpoint for logging in a user, specifically for linked
authentication on PCGDK

**Server:** `https://auth.roblox.com`

**Auth:** 

**Request Body:** `application/json` — Type: `Roblox.Authentication.Api.Models.LoginRequest`

See [Roblox.Authentication.Api.Models.LoginRequest](#roblox-authentication-api-models-loginrequest) in Models.

**Request example:**
```json
{
  "ctype": 0,
  "cvalue": "string",
  "password": "string",
  "userId": 0,
  "securityQuestionSessionId": "string",
  "securityQuestionRedemptionToken": "string"
}
```

**Responses:**

- `200`: Successful login → `Roblox.Authentication.Api.Models.LoginResponse`
- `400`: 0: An unexpected error occurred. 3: Username and Password are required. Please try again. 8: Login with received credential type is not supported.
- `403`: 0: Token Validation Failed 1: Incorrect username or password. Please try again. 2: You must pass the robot test before logging in. 4: Account has been locked. Please request a password reset. 5: Unable to login. Please use Social Network sign on. 6: Account issue. Please contact Support. 9: Unable to login with provided credentials. Default login is required. 10: Received credentials are unverified. 12: Existing login session found. Please log out first. 14: The account is unable to log in. Please log in to the LuoBu app. 15: Too many attempts. Please wait a bit. 27: The account is unable to login. Please log in with the VNG app. 43: This account is not eligible for this platform. 44: Login is unavailable in your country.
- `429`: 7: Too many attempts. Please wait a bit.
- `503`: 11: Service unavailable. Please try again.

**Response fields** (`Roblox.Authentication.Api.Models.LoginResponse`)

See [Roblox.Authentication.Api.Models.LoginResponse](#roblox-authentication-api-models-loginresponse) in Models.

**Response example:**
```json
{
  "user": {
    "id": 0,
    "name": "string",
    "displayName": "string"
  },
  "twoStepVerificationData": {
    "mediaType": 0,
    "ticket": "string"
  },
  "identityVerificationLoginTicket": "string",
  "isBanned": false,
  "accountBlob": "string",
  "shouldUpdateEmail": false
}
```

**Error handling:** `429`: Retry with exponential backoff (start at 1s). `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://auth.roblox.com/v1/login/linked" \
  -H "Content-Type: application/json" \
  -d '{
  "ctype": 0,
  "cvalue": "string",
  "password": "string",
  "userId": 0,
  "securityQuestionSessionId": "string",
  "securityQuestionRedemptionToken": "string"
}'
```

### POST `/v1/logout`

Destroys the current authentication session.

**Server:** `https://auth.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://auth.roblox.com/v1/logout"
```

### POST `/v1/logoutfromallsessionsandreauthenticate`

Logs out user from all other sessions.

**Server:** `https://auth.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Request Body:** `application/json` — Type: `Roblox.Authentication.Api.Models.Request.LogoutFromAllSessionsAndReauthenticateRequest`

See [Roblox.Authentication.Api.Models.Request.LogoutFromAllSessionsAndReauthenticateRequest](#roblox-authentication-api-models-request-logoutfromallsessionsandreauthenticaterequest) in Models.

**Request example:**
```json
{
  "SecureAuthenticationIntent": {
    "clientPublicKey": "string",
    "clientEpochTimestamp": 0,
    "saiSignature": "string",
    "serverNonce": "string"
  }
}
```

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://auth.roblox.com/v1/logoutfromallsessionsandreauthenticate" \
  -H "Content-Type: application/json" \
  -d '{
  "SecureAuthenticationIntent": {
    "clientPublicKey": "string",
    "clientEpochTimestamp": 0,
    "saiSignature": "string",
    "serverNonce": "string"
  }
}'
```

### GET `/v1/messages`

Gets a user's messages.

**Server:** `https://privatemessages.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `pageNumber` | query | `integer` | No |  |
| `pageSize` | query | `integer` | No |  |
| `messageTab` | query | `Inbox \| Sent \| Archive` | No | Valid values: `Inbox`, `Sent`, `Archive` |

**Responses:**

- `200`: OK → `Roblox.PrivateMessages.Api.Models.GetMessagesResponse`
- `401`: 0: Authorization has been denied for this request.

**Response fields** (`Roblox.PrivateMessages.Api.Models.GetMessagesResponse`)

See [Roblox.PrivateMessages.Api.Models.GetMessagesResponse](#roblox-privatemessages-api-models-getmessagesresponse) in Models.

**Response example:**
```json
{
  "collection": [
    {
      "id": "...",
      "sender": "...",
      "recipient": "...",
      "subject": "...",
      "body": "...",
      "created": "..."
    }
  ],
  "totalCollectionSize": 0,
  "totalPages": 0,
  "pageNumber": 0
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://privatemessages.roblox.com/v1/messages"
```

### POST `/v1/messages/archive`

Archives a batch of messages.

**Server:** `https://privatemessages.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Responses:**

- `200`: OK → `Roblox.PrivateMessages.Api.Models.BatchMessagesResponse`
- `400`: 5: Too many ids in a batch request.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed

**Response fields** (`Roblox.PrivateMessages.Api.Models.BatchMessagesResponse`)

See [Roblox.PrivateMessages.Api.Models.BatchMessagesResponse](#roblox-privatemessages-api-models-batchmessagesresponse) in Models.

**Response example:**
```json
{
  "failedMessages": [
    {
      "messageId": "...",
      "errorMessage": "..."
    }
  ]
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://privatemessages.roblox.com/v1/messages/archive" \
  -H "Content-Type: application/json" \
  -d '{"key": "value"}'
```

### POST `/v1/messages/mark-read`

Marks a batch of messages as read.

**Server:** `https://privatemessages.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Responses:**

- `200`: OK → `Roblox.PrivateMessages.Api.Models.BatchMessagesResponse`
- `400`: 5: Too many ids in a batch request.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed

**Response fields** (`Roblox.PrivateMessages.Api.Models.BatchMessagesResponse`)

See [Roblox.PrivateMessages.Api.Models.BatchMessagesResponse](#roblox-privatemessages-api-models-batchmessagesresponse) in Models.

**Response example:**
```json
{
  "failedMessages": [
    {
      "messageId": "...",
      "errorMessage": "..."
    }
  ]
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://privatemessages.roblox.com/v1/messages/mark-read" \
  -H "Content-Type: application/json" \
  -d '{"key": "value"}'
```

### POST `/v1/messages/mark-unread`

Marks a batch of messages as unread.

**Server:** `https://privatemessages.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Responses:**

- `200`: OK → `Roblox.PrivateMessages.Api.Models.BatchMessagesResponse`
- `400`: 5: Too many ids in a batch request.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed

**Response fields** (`Roblox.PrivateMessages.Api.Models.BatchMessagesResponse`)

See [Roblox.PrivateMessages.Api.Models.BatchMessagesResponse](#roblox-privatemessages-api-models-batchmessagesresponse) in Models.

**Response example:**
```json
{
  "failedMessages": [
    {
      "messageId": "...",
      "errorMessage": "..."
    }
  ]
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://privatemessages.roblox.com/v1/messages/mark-unread" \
  -H "Content-Type: application/json" \
  -d '{"key": "value"}'
```

### POST `/v1/messages/unarchive`

Unarchives a batch of messages.

**Server:** `https://privatemessages.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Responses:**

- `200`: OK → `Roblox.PrivateMessages.Api.Models.BatchMessagesResponse`
- `400`: 5: Too many ids in a batch request.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed

**Response fields** (`Roblox.PrivateMessages.Api.Models.BatchMessagesResponse`)

See [Roblox.PrivateMessages.Api.Models.BatchMessagesResponse](#roblox-privatemessages-api-models-batchmessagesresponse) in Models.

**Response example:**
```json
{
  "failedMessages": [
    {
      "messageId": "...",
      "errorMessage": "..."
    }
  ]
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://privatemessages.roblox.com/v1/messages/unarchive" \
  -H "Content-Type: application/json" \
  -d '{"key": "value"}'
```

### GET `/v1/messages/unread/count`

Gets unread messages for the authenticated user.

**Server:** `https://privatemessages.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Responses:**

- `200`: OK → `Roblox.PrivateMessages.Api.Models.UnreadMessagesCountResponse`
- `401`: 0: Authorization has been denied for this request.

**Response fields** (`Roblox.PrivateMessages.Api.Models.UnreadMessagesCountResponse`)

See [Roblox.PrivateMessages.Api.Models.UnreadMessagesCountResponse](#roblox-privatemessages-api-models-unreadmessagescountresponse) in Models.

**Response example:**
```json
{
  "count": 0
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://privatemessages.roblox.com/v1/messages/unread/count"
```

### GET `/v1/messages/{messageId}`

Gets a message's details.

**Server:** `https://privatemessages.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `messageId` | path | `integer` | Yes |  |

**Responses:**

- `200`: OK → `Roblox.PrivateMessages.Api.Models.MessageDetailsResponse`
- `400`: 2: Message does not exist or the current user is not authorized to view it.
- `401`: 0: Authorization has been denied for this request.

**Response fields** (`Roblox.PrivateMessages.Api.Models.MessageDetailsResponse`)

See [Roblox.PrivateMessages.Api.Models.MessageDetailsResponse](#roblox-privatemessages-api-models-messagedetailsresponse) in Models.

**Response example:**
```json
{
  "id": 0,
  "sender": {
    "hasVerifiedBadge": false,
    "id": 0,
    "name": "string",
    "displayName": "string"
  },
  "recipient": {
    "hasVerifiedBadge": false,
    "id": 0,
    "name": "string",
    "displayName": "string"
  },
  "subject": "string",
  "body": "string",
  "created": "2024-01-01T00:00:00Z"
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://privatemessages.roblox.com/v1/messages/{MESSAGEID}"
```

### GET `/v1/metadata`

Get the metadata

**Server:** `https://accountinformation.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Responses:**

- `200`: OK → `Roblox.AccountInformation.Api.Models.MetadataResponse`

**Response fields** (`Roblox.AccountInformation.Api.Models.MetadataResponse`)

See [Roblox.AccountInformation.Api.Models.MetadataResponse](#roblox-accountinformation-api-models-metadataresponse) in Models.

**Response example:**
```json
{
  "isAllowedNotificationsEndpointDisabled": false,
  "isAccountSettingsPolicyEnabled": false,
  "isPhoneNumberEnabled": false,
  "MaxUserDescriptionLength": 0,
  "isUserDescriptionEnabled": false,
  "isUserBlockEndpointsUpdated": false
}
```

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://accountinformation.roblox.com/v1/metadata"
```

### GET `/v1/metadata#auth.roblox.com`

Get the metadata

**Server:** `https://auth.roblox.com`

**Auth:** 

**Responses:**

- `200`: OK → `Roblox.Authentication.Api.Models.MetadataResponse`

**Response fields** (`Roblox.Authentication.Api.Models.MetadataResponse`)

See [Roblox.Authentication.Api.Models.MetadataResponse](#roblox-authentication-api-models-metadataresponse) in Models.

**Response example:**
```json
{
  "isUpdateUsernameEnabled": false,
  "ftuxAvatarAssetMap": "string",
  "IsEmailUpsellAtLogoutEnabled": false,
  "ShouldFetchEmailUpsellIXPValuesAtLogout": false,
  "IsAccountRecoveryPromptEnabled": false,
  "IsContactMethodRequiredAtSignup": false
}
```

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://auth.roblox.com/v1/metadata#auth.roblox.com"
```

### GET `/v1/metadata#twostepverification.roblox.com`

Gets two step verification system metadata.

The metadata endpoint takes in optional request parameters to output additional context
for when the user is unauthenticated but attempting to login with two step verification.

When supplied, all three request parameters must be sent and match up.

**Server:** `https://twostepverification.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | query | `integer` | No | The user ID. |
| `challengeId` | query | `string` | No | The active two step verification challenge ID if there is one. |
| `actionType` | query | `integer enum (9 values)` | No | The Roblox.TwoStepVerification.Client.TwoStepVerificationActionType associated with the challenge. Valid values: `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8` |

**Responses:**

- `200`: OK → `Roblox.TwoStepVerification.Api.MetadataResponse`

**Response fields** (`Roblox.TwoStepVerification.Api.MetadataResponse`)

See [Roblox.TwoStepVerification.Api.MetadataResponse](#roblox-twostepverification-api-metadataresponse) in Models.

**Response example:**
```json
{
  "twoStepVerificationEnabled": false,
  "authenticatorQrCodeSize": "string",
  "emailCodeLength": 0,
  "authenticatorCodeLength": 0,
  "authenticatorHelpSiteAddress": "string",
  "isPasswordRequiredForEnablingAuthenticator": false
}
```

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://twostepverification.roblox.com/v1/metadata#twostepverification.roblox.com"
```

### POST `/v1/passkey/DeleteCredentialBatch`

Disables a batch of credentials for the specified user.

**Server:** `https://auth.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Request Body:** `application/json` — Type: `Roblox.Authentication.Api.Models.Request.DeletePasskeysRequest`

See [Roblox.Authentication.Api.Models.Request.DeletePasskeysRequest](#roblox-authentication-api-models-request-deletepasskeysrequest) in Models.

**Request example:**
```json
{
  "credentialIDs": [
    "string"
  ],
  "credentialNicknames": [
    "string"
  ]
}
```

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: 3: Invalid security key nickname.
- `401`: 0: Authorization has been denied for this request. 0: An unknown error occurred with the request.
- `403`: 0: Token Validation Failed
- `503`: 2: Feature disabled.

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://auth.roblox.com/v1/passkey/DeleteCredentialBatch" \
  -H "Content-Type: application/json" \
  -d '{
  "credentialIDs": [
    "string"
  ],
  "credentialNicknames": [
    "string"
  ]
}'
```

### POST `/v1/passkey/FinishRegistration`

Complete Passkey registration by providing credential creation options.

**Server:** `https://auth.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Request Body:** `application/json` — Type: `Roblox.Authentication.Api.Models.Request.FinishPasskeyRegistrationRequest`

See [Roblox.Authentication.Api.Models.Request.FinishPasskeyRegistrationRequest](#roblox-authentication-api-models-request-finishpasskeyregistrationrequest) in Models.

**Request example:**
```json
{
  "sessionId": "string",
  "credentialNickname": "string",
  "attestationResponse": "string",
  "source": "string"
}
```

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: 0: An unknown error occurred with the request. 3: Invalid security key nickname.
- `401`: 0: Authorization has been denied for this request. 0: An unknown error occurred with the request.
- `403`: 0: Token Validation Failed 3: Invalid security key nickname.
- `503`: 2: Feature disabled.

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://auth.roblox.com/v1/passkey/FinishRegistration" \
  -H "Content-Type: application/json" \
  -d '{
  "sessionId": "string",
  "credentialNickname": "string",
  "attestationResponse": "string",
  "source": "string"
}'
```

### POST `/v1/passkey/ListCredentials`

List a user's registered passkeys.

**Server:** `https://auth.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Request Body:** `application/json` — Type: `Roblox.Authentication.Api.Models.Request.ListPasskeysRequest`

See [Roblox.Authentication.Api.Models.Request.ListPasskeysRequest](#roblox-authentication-api-models-request-listpasskeysrequest) in Models.

**Request example:**
```json
{
  "all": false
}
```

**Responses:**

- `200`: OK → `Roblox.Authentication.Api.Models.Response.ListPasskeyCredentialResponse`
- `401`: 0: Authorization has been denied for this request. 0: An unknown error occurred with the request.
- `403`: 0: Token Validation Failed
- `503`: 2: Feature disabled.

**Response fields** (`Roblox.Authentication.Api.Models.Response.ListPasskeyCredentialResponse`)

See [Roblox.Authentication.Api.Models.Response.ListPasskeyCredentialResponse](#roblox-authentication-api-models-response-listpasskeycredentialresponse) in Models.

**Response example:**
```json
{
  "credentials": [
    {
      "nickname": "...",
      "credentialID": "..."
    }
  ]
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://auth.roblox.com/v1/passkey/ListCredentials" \
  -H "Content-Type: application/json" \
  -d '{
  "all": false
}'
```

### POST `/v1/passkey/RenameCredential`

Rename a credential for the specified user.

**Server:** `https://auth.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Request Body:** `application/json` — Type: `Roblox.Authentication.Api.Models.Request.RenamePasskeyRequest`

See [Roblox.Authentication.Api.Models.Request.RenamePasskeyRequest](#roblox-authentication-api-models-request-renamepasskeyrequest) in Models.

**Request example:**
```json
{
  "credentialID": "string",
  "newNickname": "string"
}
```

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: 3: Invalid security key nickname. 7: Invalid passkey ID.
- `401`: 0: Authorization has been denied for this request. 0: An unknown error occurred with the request.
- `403`: 0: Token Validation Failed 3: Invalid security key nickname.
- `503`: 2: Feature disabled.

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://auth.roblox.com/v1/passkey/RenameCredential" \
  -H "Content-Type: application/json" \
  -d '{
  "credentialID": "string",
  "newNickname": "string"
}'
```

### POST `/v1/passkey/StartAuthentication`

Provides a challenge for the Passkey to authenticate.

**Server:** `https://auth.roblox.com`

**Auth:** 

**Responses:**

- `200`: OK → `Roblox.Authentication.Api.Models.Response.StartAuthenticationResponse`
- `403`: 0: Token Validation Failed
- `503`: 2: Feature disabled.

**Response fields** (`Roblox.Authentication.Api.Models.Response.StartAuthenticationResponse`)

See [Roblox.Authentication.Api.Models.Response.StartAuthenticationResponse](#roblox-authentication-api-models-response-startauthenticationresponse) in Models.

**Response example:**
```json
{
  "authenticationOptions": "string",
  "sessionId": "string"
}
```

**Error handling:** `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://auth.roblox.com/v1/passkey/StartAuthentication"
```

### POST `/v1/passkey/StartRegistration`

Initiates Passkey registration by providing credential creation options.

**Server:** `https://auth.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `flow` | query | `string` | No |  |

**Request Body:** `application/json` — Type: `Roblox.Authentication.Api.Models.Request.StartPasskeyRegistrationRequest`

See [Roblox.Authentication.Api.Models.Request.StartPasskeyRegistrationRequest](#roblox-authentication-api-models-request-startpasskeyregistrationrequest) in Models.

**Request example:**
```json
{
  "isSilentUpgrade": false
}
```

**Responses:**

- `200`: OK → `Roblox.Authentication.Api.Models.Response.StartPasskeyRegistrationResponse`
- `401`: 0: Authorization has been denied for this request. 0: An unknown error occurred with the request.
- `403`: 0: Token Validation Failed 1: Reached limit of pass keys registered.
- `503`: 2: Feature disabled.

**Response fields** (`Roblox.Authentication.Api.Models.Response.StartPasskeyRegistrationResponse`)

See [Roblox.Authentication.Api.Models.Response.StartPasskeyRegistrationResponse](#roblox-authentication-api-models-response-startpasskeyregistrationresponse) in Models.

**Response example:**
```json
{
  "creationOptions": "string",
  "sessionId": "string"
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://auth.roblox.com/v1/passkey/StartRegistration" \
  -H "Content-Type: application/json" \
  -d '{
  "isSilentUpgrade": false
}'
```

### POST `/v1/passkey/finish-ar-preauth-registration`

Finishes account recovery pre-auth passkey registration by validating the recovery session,
deactivating the user's password, and completing passkey registration.

**Server:** `https://auth.roblox.com`

**Auth:** 

**Request Body:** `application/json` — Type: `Roblox.Authentication.Api.Models.Request.FinishARPreAuthPasskeyRegistrationRequest`

See [Roblox.Authentication.Api.Models.Request.FinishARPreAuthPasskeyRegistrationRequest](#roblox-authentication-api-models-request-finisharpreauthpasskeyregistrationrequest) in Models.

**Request example:**
```json
{
  "recoverySession": "string",
  "passkeySessionId": "string",
  "passkeyRegistrationResponse": "string",
  "userId": 0,
  "isPostRecovery": false,
  "source": "string"
}
```

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: 0: An unknown error occurred with the request.
- `401`: 0: An unknown error occurred with the request.
- `403`: 0: Token Validation Failed 1: Reached limit of pass keys registered.
- `500`: 0: An unknown error occurred with the request.
- `503`: 2: Feature disabled.

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://auth.roblox.com/v1/passkey/finish-ar-preauth-registration" \
  -H "Content-Type: application/json" \
  -d '{
  "recoverySession": "string",
  "passkeySessionId": "string",
  "passkeyRegistrationResponse": "string",
  "userId": 0,
  "isPostRecovery": false,
  "source": "string"
}'
```

### POST `/v1/passkey/finish-preauth-registration`

**Server:** `https://auth.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Request Body:** `application/json` — Type: `Roblox.Authentication.Api.Models.Request.FinishPasskeyPreauthRegistrationRequest`

See [Roblox.Authentication.Api.Models.Request.FinishPasskeyPreauthRegistrationRequest](#roblox-authentication-api-models-request-finishpasskeypreauthregistrationrequest) in Models.

**Request example:**
```json
{
  "sessionId": "string",
  "registrationResponse": "string",
  "source": "string"
}
```

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: 0: An unknown error occurred with the request.
- `401`: 0: Authorization has been denied for this request. 0: An unknown error occurred with the request.
- `403`: 0: Token Validation Failed 1: Reached limit of pass keys registered.
- `500`: 0: An unknown error occurred with the request.
- `503`: 2: Feature disabled.

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://auth.roblox.com/v1/passkey/finish-preauth-registration" \
  -H "Content-Type: application/json" \
  -d '{
  "sessionId": "string",
  "registrationResponse": "string",
  "source": "string"
}'
```

### POST `/v1/passkey/start-authentication-by-user`

Initializes passkey authentication for the user(s) corresponding to the identifier provided.

**Server:** `https://auth.roblox.com`

**Auth:** 

**Request Body:** `application/json` — Type: `Roblox.Authentication.Api.Models.Request.StartAuthenticationByUserRequest`

See [Roblox.Authentication.Api.Models.Request.StartAuthenticationByUserRequest](#roblox-authentication-api-models-request-startauthenticationbyuserrequest) in Models.

**Request example:**
```json
{
  "ctype": 0,
  "cvalue": "string"
}
```

**Responses:**

- `200`: OK → `Roblox.Authentication.Api.Models.Response.StartAuthenticationByUserResponse`
- `400`: 5: User identifier and type are required. 6: Multi-user passkey authentication is not supported for this credential type.
- `403`: 0: Token Validation Failed 4: No passkeys registered for any users found.
- `503`: 2: Feature disabled.

**Response fields** (`Roblox.Authentication.Api.Models.Response.StartAuthenticationByUserResponse`)

See [Roblox.Authentication.Api.Models.Response.StartAuthenticationByUserResponse](#roblox-authentication-api-models-response-startauthenticationbyuserresponse) in Models.

**Response example:**
```json
{
  "authenticationOptions": "string",
  "sessionId": "string"
}
```

**Error handling:** `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://auth.roblox.com/v1/passkey/start-authentication-by-user" \
  -H "Content-Type: application/json" \
  -d '{
  "ctype": 0,
  "cvalue": "string"
}'
```

### POST `/v1/passkey/start-preauth-registration`

Initiates  Passkey preauthenticated registration by providing credential creation options.

**Server:** `https://auth.roblox.com`

**Auth:** 

**Request Body:** `application/json` — Type: `Roblox.Authentication.Api.Models.Request.StartPasskeyPreauthRegistrationRequest`

See [Roblox.Authentication.Api.Models.Request.StartPasskeyPreauthRegistrationRequest](#roblox-authentication-api-models-request-startpasskeypreauthregistrationrequest) in Models.

**Request example:**
```json
{
  "username": "string"
}
```

**Responses:**

- `200`: OK → `Roblox.Authentication.Api.Models.Response.StartPasskeyPreauthRegistrationResponse`
- `403`: 0: Token Validation Failed
- `503`: 2: Feature disabled.

**Response fields** (`Roblox.Authentication.Api.Models.Response.StartPasskeyPreauthRegistrationResponse`)

See [Roblox.Authentication.Api.Models.Response.StartPasskeyPreauthRegistrationResponse](#roblox-authentication-api-models-response-startpasskeypreauthregistrationresponse) in Models.

**Response example:**
```json
{
  "creationOptions": "string",
  "sessionId": "string"
}
```

**Error handling:** `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://auth.roblox.com/v1/passkey/start-preauth-registration" \
  -H "Content-Type: application/json" \
  -d '{
  "username": "string"
}'
```

### GET `/v1/passkey/su-eligibility`

Checks whether the authenticated user is eligible for silent passkey upgrade.
Route and response are intentionally obfuscated ("su-eligibility" = "silent-upgrade-eligibility").

**Server:** `https://auth.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Responses:**

- `200`: OK → `Roblox.Authentication.Api.Models.Response.SilentUpgradeEligibilityResponse`
- `401`: 0: Authorization has been denied for this request. 0: An unknown error occurred with the request.
- `503`: 2: Feature disabled.

**Response fields** (`Roblox.Authentication.Api.Models.Response.SilentUpgradeEligibilityResponse`)

See [Roblox.Authentication.Api.Models.Response.SilentUpgradeEligibilityResponse](#roblox-authentication-api-models-response-silentupgradeeligibilityresponse) in Models.

**Response example:**
```json
{
  "suEligibility": false
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://auth.roblox.com/v1/passkey/su-eligibility"
```

### GET `/v1/passwords/validate`

Endpoint for checking if a password is valid.

**Server:** `https://auth.roblox.com`

**Auth:** 

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `Username` | query | `string` | Yes |  |
| `Password` | query | `string` | Yes |  |

**Responses:**

- `200`: Success → `Roblox.Authentication.Api.Models.PasswordValidationResponse`
- `400`: 1: Valid Username and Password are required. Please try again.

**Response fields** (`Roblox.Authentication.Api.Models.PasswordValidationResponse`)

See [Roblox.Authentication.Api.Models.PasswordValidationResponse](#roblox-authentication-api-models-passwordvalidationresponse) in Models.

**Response example:**
```json
{
  "code": 0,
  "message": "string"
}
```

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://auth.roblox.com/v1/passwords/validate?Username={VALUE}&Password={VALUE}"
```

### POST `/v1/passwords/validate`

Endpoint for checking if a password is valid.

**Server:** `https://auth.roblox.com`

**Auth:** 

**Request Body:** `application/json` — Type: `Roblox.Authentication.Api.Models.PasswordValidationModel`

See [Roblox.Authentication.Api.Models.PasswordValidationModel](#roblox-authentication-api-models-passwordvalidationmodel) in Models.

**Request example:**
```json
{
  "username": "string",
  "password": "string"
}
```

**Responses:**

- `200`: Success → `Roblox.Authentication.Api.Models.PasswordValidationResponse`
- `400`: 1: Valid Username and Password are required. Please try again.
- `403`: 0: Token Validation Failed

**Response fields** (`Roblox.Authentication.Api.Models.PasswordValidationResponse`)

See [Roblox.Authentication.Api.Models.PasswordValidationResponse](#roblox-authentication-api-models-passwordvalidationresponse) in Models.

**Response example:**
```json
{
  "code": 0,
  "message": "string"
}
```

**Error handling:** `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://auth.roblox.com/v1/passwords/validate" \
  -H "Content-Type: application/json" \
  -d '{
  "username": "string",
  "password": "string"
}'
```

### GET `/v1/phone`

Get Verified Phone Number

**Server:** `https://accountinformation.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Responses:**

- `200`: OK → `Roblox.AccountInformation.Api.Models.PhoneResponse`
- `401`: 0: Authorization has been denied for this request.
- `500`: 0: An unknown error occured.

**Response fields** (`Roblox.AccountInformation.Api.Models.PhoneResponse`)

See [Roblox.AccountInformation.Api.Models.PhoneResponse](#roblox-accountinformation-api-models-phoneresponse) in Models.

**Response example:**
```json
{
  "countryCode": "string",
  "prefix": "string",
  "phone": "string",
  "isVerified": false,
  "verificationCodeLength": 0,
  "canBypassPasswordForPhoneUpdate": false
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://accountinformation.roblox.com/v1/phone"
```

### POST `/v1/phone`

Set Phone Number

**Server:** `https://accountinformation.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Responses:**

- `200`: OK → `Roblox.Platform.UserPhoneNumberVerification.Models.PendingVerificationResponse`
- `400`: 2: Invalid Phone Number 3: Phone Number Already Associated 8: Invalid Phone Number Type
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 5: Incorrect Password 10:
- `429`: 6: Flooded
- `500`: 0: An unknown error occured.
- `503`: 1: This feature is currently disabled. Please try again later.

**Response fields** (`Roblox.Platform.UserPhoneNumberVerification.Models.PendingVerificationResponse`)

See [Roblox.Platform.UserPhoneNumberVerification.Models.PendingVerificationResponse](#roblox-platform-userphonenumberverification-models-pendingverificationresponse) in Models.

**Response example:**
```json
{
  "verificationChannel": "string",
  "data": "string"
}
```

**Error handling:** `429`: Retry with exponential backoff (start at 1s). `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://accountinformation.roblox.com/v1/phone" \
  -H "Content-Type: application/json" \
  -d '{"key": "value"}'
```

### POST `/v1/phone/delete`

Delete Phone

**Server:** `https://accountinformation.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 5: Incorrect Password
- `429`: 6: Flooded
- `500`: 0: An unknown error occured.
- `503`: 1: This feature is currently disabled. Please try again later.

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `429`: Retry with exponential backoff (start at 1s). `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://accountinformation.roblox.com/v1/phone/delete" \
  -H "Content-Type: application/json" \
  -d '{"key": "value"}'
```

### POST `/v1/phone/resend`

Resend Phone code

**Server:** `https://accountinformation.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Request Body:** `application/json` — Type: `Roblox.AccountInformation.Api.Models.EmptyRequest`

See [Roblox.AccountInformation.Api.Models.EmptyRequest](#roblox-accountinformation-api-models-emptyrequest) in Models.

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed
- `429`: 6: Flooded
- `500`: 0: An unknown error occured.
- `503`: 1: This feature is currently disabled. Please try again later.

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `429`: Retry with exponential backoff (start at 1s). `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://accountinformation.roblox.com/v1/phone/resend" \
  -H "Content-Type: application/json" \
  -d '"..."'
```

### POST `/v1/phone/verify`

Verify Phone

**Server:** `https://accountinformation.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Request Body:** `application/json` — Type: `Roblox.AccountInformation.Api.Models.VerifyPhoneRequest`

See [Roblox.AccountInformation.Api.Models.VerifyPhoneRequest](#roblox-accountinformation-api-models-verifyphonerequest) in Models.

**Request example:**
```json
{
  "code": "string"
}
```

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: 2: Invalid Phone Number 3: Phone Number Already Associated 7: Invalid Code
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed
- `429`: 6: Flooded
- `500`: 0: An unknown error occured.
- `503`: 1: This feature is currently disabled. Please try again later.

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `429`: Retry with exponential backoff (start at 1s). `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://accountinformation.roblox.com/v1/phone/verify" \
  -H "Content-Type: application/json" \
  -d '{
  "code": "string"
}'
```

### GET `/v1/promotion-channels`

Get the user's promotion channels

**Server:** `https://accountinformation.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `alwaysReturnUrls` | query | `boolean` | No | Whether all promotion channel links should be returned as full URLs. |
| `filterLink` | query | `boolean` | No | Whether all promotion channel links should be filtered. |
| `onlyShortenTwitter` | query | `boolean` | No | Whether all promotion channels links except for Twitter should be returned as full URLs. If false, all promotion channels will be shortened. |

**Responses:**

- `200`: OK → `Roblox.AccountInformation.Api.Models.PromotionChannelsResponse`
- `400`: 1: User not found.
- `401`: 0: Authorization has been denied for this request.

**Response fields** (`Roblox.AccountInformation.Api.Models.PromotionChannelsResponse`)

See [Roblox.AccountInformation.Api.Models.PromotionChannelsResponse](#roblox-accountinformation-api-models-promotionchannelsresponse) in Models.

**Response example:**
```json
{
  "promotionChannelsVisibilityPrivacy": "string",
  "facebook": "string",
  "twitter": "string",
  "youtube": "string",
  "twitch": "string"
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://accountinformation.roblox.com/v1/promotion-channels"
```

### POST `/v1/promotion-channels`

Update the user's promotion channels

**Server:** `https://accountinformation.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Request Body:** `application/json` — Type: `Roblox.AccountInformation.Api.Models.PromotionChannelsRequest`

See [Roblox.AccountInformation.Api.Models.PromotionChannelsRequest](#roblox-accountinformation-api-models-promotionchannelsrequest) in Models.

**Request example:**
```json
{
  "facebook": "string",
  "twitter": "string",
  "youtube": "string",
  "twitch": "string",
  "promotionChannelsVisibilityPrivacy": "string"
}
```

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: 2: The request was empty. 11: The Facebook profile url is invalid. 12: The Twitter handle is invalid. 13: The YouTube url is invalid. 14: The Twitch profile url is invalid.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 4: Only users who are over twelve years of age may edit social network channels.

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://accountinformation.roblox.com/v1/promotion-channels" \
  -H "Content-Type: application/json" \
  -d '{
  "facebook": "string",
  "twitter": "string",
  "youtube": "string",
  "twitch": "string",
  "promotionChannelsVisibilityPrivacy": "string"
}'
```

### GET `/v1/recovery/metadata`

Get metadata for forgot endpoints

**Server:** `https://auth.roblox.com`

**Auth:** 

**Responses:**

- `200`: OK → `Roblox.Authentication.Api.Models.RecoveryMetadataResponse`
- `503`: 7: The Roblox WeChat API is currently unavailable.

**Response fields** (`Roblox.Authentication.Api.Models.RecoveryMetadataResponse`)

See [Roblox.Authentication.Api.Models.RecoveryMetadataResponse](#roblox-authentication-api-models-recoverymetadataresponse) in Models.

**Response example:**
```json
{
  "isOnPhone": false,
  "codeLength": 0,
  "isPhoneFeatureEnabledForUsername": false,
  "isPhoneFeatureEnabledForPassword": false,
  "isBedev2CaptchaEnabledForPasswordReset": false,
  "isUsernameRecoveryDeprecated": false
}
```

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://auth.roblox.com/v1/recovery/metadata"
```

### GET `/v1/revert/account`

Get Revert Account ticket info

**Server:** `https://auth.roblox.com`

**Auth:** 

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `ticket` | query | `string` | Yes | Ticket Guid to revert account. |

**Responses:**

- `200`: OK → `Roblox.Authentication.Api.Models.RevertAccountInfoResponse`
- `400`: 2: The account revert ticket is not valid
- `403`: 13: Revert links are disabled for users in the Enhanced Protection Program.
- `503`: 1: This feature is disabled

**Response fields** (`Roblox.Authentication.Api.Models.RevertAccountInfoResponse`)

See [Roblox.Authentication.Api.Models.RevertAccountInfoResponse](#roblox-authentication-api-models-revertaccountinforesponse) in Models.

**Response example:**
```json
{
  "isTwoStepVerificationEnabled": false,
  "isEmailVerified": false,
  "isEmailChanged": false,
  "isPhoneVerified": false,
  "userId": 0,
  "username": "string"
}
```

**Error handling:** `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://auth.roblox.com/v1/revert/account?ticket={VALUE}"
```

### POST `/v1/revert/account`

Submit Revert Account Request

**Server:** `https://auth.roblox.com`

**Auth:** 

**Request Body:** `application/json` — Type: `Roblox.Authentication.Api.Models.RevertAccountSubmitRequest`

See [Roblox.Authentication.Api.Models.RevertAccountSubmitRequest](#roblox-authentication-api-models-revertaccountsubmitrequest) in Models.

**Request example:**
```json
{
  "UserId": 0,
  "NewPassword": "string",
  "NewPasswordRepeated": "string",
  "Ticket": "string",
  "TwoStepVerificationChallengeId": "string",
  "TwoStepVerificationToken": "string"
}
```

**Responses:**

- `200`: OK → `Roblox.Authentication.Api.Models.LoginResponse`
- `400`: 2: The account revert ticket is not valid 3: Password is not valid 4: Passwords do not match 5: Password cannot be used 8: The account security ticket is expired. 14: Password is not complex enough 15: Password is too similar to username
- `403`: 0: Token Validation Failed
- `503`: 0: Unknown 1: This feature is disabled

**Response fields** (`Roblox.Authentication.Api.Models.LoginResponse`)

See [Roblox.Authentication.Api.Models.LoginResponse](#roblox-authentication-api-models-loginresponse) in Models.

**Response example:**
```json
{
  "user": {
    "id": 0,
    "name": "string",
    "displayName": "string"
  },
  "twoStepVerificationData": {
    "mediaType": 0,
    "ticket": "string"
  },
  "identityVerificationLoginTicket": "string",
  "isBanned": false,
  "accountBlob": "string",
  "shouldUpdateEmail": false
}
```

**Error handling:** `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://auth.roblox.com/v1/revert/account" \
  -H "Content-Type: application/json" \
  -d '{
  "UserId": 0,
  "NewPassword": "string",
  "NewPasswordRepeated": "string",
  "Ticket": "string",
  "TwoStepVerificationChallengeId": "string",
  "TwoStepVerificationToken": "string"
}'
```

### POST `/v1/revert/invalidate-tickets`

Invalidates all account security tickets for the authenticated user.
This endpoint should be called before enrolling in EPP to ensure old revert links cannot be used.

**Server:** `https://auth.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Responses:**

- `200`: Successfully invalidated all tickets. → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed
- `503`: 1: This feature is disabled

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://auth.roblox.com/v1/revert/invalidate-tickets"
```

### POST `/v1/session/refresh`

Logs out user from the current session and create a new one.

**Server:** `https://auth.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://auth.roblox.com/v1/session/refresh"
```

### POST `/v1/signup`

Endpoint for signing up a new user

**Server:** `https://auth.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Responses:**

- `200`: Successful signup → `Roblox.Authentication.Api.Models.SignupResponse`
- `400`: Bad request
- `403`: 0: Token Validation Failed 2: Captcha Failed. 4: Invalid Birthday. 5: Invalid Username. 6: Username already taken. 7: Invalid Password. 8: Password and Username are same. 9: Password is too simple. 10: Email is invalid. 11: Asset is invalid. 12: Too many attempts. Please wait a bit. 17: One time Passcode session was not valid 22: Maximum logged in accounts limit reached. 36: Password is not complex enough. 37: Password is too similar to username. 44: Login is unavailable in your country.
- `429`: 3: Too many attempts. Please wait a bit.
- `500`: Internal server error
- `503`: Service unavailable

**Response fields** (`Roblox.Authentication.Api.Models.SignupResponse`)

See [Roblox.Authentication.Api.Models.SignupResponse](#roblox-authentication-api-models-signupresponse) in Models.

**Response example:**
```json
{
  "userId": 0,
  "starterPlaceId": 0,
  "returnUrl": "string",
  "accountBlob": "string"
}
```

**Error handling:** `429`: Retry with exponential backoff (start at 1s). `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://auth.roblox.com/v1/signup" \
  -H "Content-Type: application/json" \
  -d '{"key": "value"}'
```

### POST `/v1/signup/linked`

Endpoint for signing up a new user through linked authentication.

**Server:** `https://auth.roblox.com`

**Auth:** 

**Responses:**

- `200`: Successful signup → `Roblox.Authentication.Api.Models.SignupResponse`
- `400`: Bad request
- `403`: 0: Token Validation Failed 2: Captcha Failed. 4: Invalid Birthday. 5: Invalid Username. 6: Username already taken. 7: Invalid Password. 8: Password and Username are same. 9: Password is too simple. 10: Email is invalid. 11: Asset is invalid. 12: Too many attempts. Please wait a bit. 17: One time Passcode session was not valid 22: Maximum logged in accounts limit reached. 29: Account Linking already exists on this account 30: Account Linking required but failed 36: Password is not complex enough. 37: Password is too similar to username. 44: Login is unavailable in your country.
- `429`: 3: Too many attempts. Please wait a bit.
- `500`: Internal server error
- `503`: 30: Account Linking required but failed

**Response fields** (`Roblox.Authentication.Api.Models.SignupResponse`)

See [Roblox.Authentication.Api.Models.SignupResponse](#roblox-authentication-api-models-signupresponse) in Models.

**Response example:**
```json
{
  "userId": 0,
  "starterPlaceId": 0,
  "returnUrl": "string",
  "accountBlob": "string"
}
```

**Error handling:** `429`: Retry with exponential backoff (start at 1s). `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://auth.roblox.com/v1/signup/linked" \
  -H "Content-Type: application/json" \
  -d '{"key": "value"}'
```

### GET `/v1/social/connected-providers`

Get social network user information if the given social auth method is connected to current user.

**Server:** `https://auth.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Responses:**

- `200`: OK → `Roblox.Authentication.Api.Models.SocialProvidersResponse`
- `401`: 0: Authorization has been denied for this request.

**Response fields** (`Roblox.Authentication.Api.Models.SocialProvidersResponse`)

See [Roblox.Authentication.Api.Models.SocialProvidersResponse](#roblox-authentication-api-models-socialprovidersresponse) in Models.

**Response example:**
```json
{
  "providers": [
    {
      "provider": "...",
      "identifier": "..."
    }
  ]
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://auth.roblox.com/v1/social/connected-providers"
```

### POST `/v1/social/{provider}/disconnect`

Removes the given social authentication method from current Roblox user if it is connected.

**Server:** `https://auth.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `provider` | path | `string` | Yes | The social authentication provider, e.g. Facebook |

**Request Body:** `application/json` — Type: `Roblox.Authentication.Api.Models.SocialAuthenticationDisconnectRequest`

See [Roblox.Authentication.Api.Models.SocialAuthenticationDisconnectRequest](#roblox-authentication-api-models-socialauthenticationdisconnectrequest) in Models.

**Request example:**
```json
{
  "Password": "string"
}
```

**Responses:**

- `200`: Successfully disconnected the authentication provider, if it was connected → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: Bad request
- `401`: 0: Authorization has been denied for this request.
- `403`: Forbidden
- `500`: Internal server error

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://auth.roblox.com/v1/social/{PROVIDER}/disconnect" \
  -H "Content-Type: application/json" \
  -d '{
  "Password": "string"
}'
```

### GET `/v1/themes/types`

returns all the enabled theme types.

**Server:** `https://accountsettings.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiArrayResponse_System.String_`

**Response fields** (`Roblox.Web.WebAPI.Models.ApiArrayResponse_System.String_`)

See [Roblox.Web.WebAPI.Models.ApiArrayResponse_System.String_](#roblox-web-webapi-models-apiarrayresponse-system-string-) in Models.

**Response example:**
```json
{
  "data": [
    "string"
  ]
}
```

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://accountsettings.roblox.com/v1/themes/types"
```

### GET `/v1/themes/{consumerType}/{consumerId}`

returns the theme type for a specific consumer.

**Server:** `https://accountsettings.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `consumerType` | path | `1` | Yes | The consumer type Valid values: `1` |
| `consumerId` | path | `string` | Yes | The consumer's theme configuration to get. If the consumerType is User always return the AuthenticatedUser's theme type. |

**Responses:**

- `200`: OK → `Roblox.AccountSettings.Api.ThemeConfigurationResponse`
- `400`: 3: Invalid consumer type.
- `401`: 0: Authorization has been denied for this request.

**Response fields** (`Roblox.AccountSettings.Api.ThemeConfigurationResponse`)

See [Roblox.AccountSettings.Api.ThemeConfigurationResponse](#roblox-accountsettings-api-themeconfigurationresponse) in Models.

**Response example:**
```json
{
  "themeType": "string"
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://accountsettings.roblox.com/v1/themes/{CONSUMERTYPE}/{CONSUMERID}"
```

### PATCH `/v1/themes/{consumerType}/{consumerId}`

Modify the theme type for consumer.

**Server:** `https://accountsettings.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `consumerType` | path | `1` | Yes | The consumer type Valid values: `1` |
| `consumerId` | path | `integer` | Yes | The consumer's theme configuration to modify. If the consumerType is User always modify the AuthenticatedUser's theme type. |

**Request Body:** `application/json` — Type: `Roblox.AccountSettings.Api.ThemeConfigurationRequest`

See [Roblox.AccountSettings.Api.ThemeConfigurationRequest](#roblox-accountsettings-api-themeconfigurationrequest) in Models.

**Request example:**
```json
{
  "themeType": "string"
}
```

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: 2: Invalid theme type.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X PATCH -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://accountsettings.roblox.com/v1/themes/{CONSUMERTYPE}/{CONSUMERID}" \
  -H "Content-Type: application/json" \
  -d '{
  "themeType": "string"
}'
```

### GET `/v1/trade-privacy`

Get a user's trade privacy setting

**Server:** `https://accountsettings.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Responses:**

- `200`: OK → `Roblox.AccountSettings.Api.TradePrivacyResponse`
- `401`: 0: Authorization has been denied for this request.

**Response fields** (`Roblox.AccountSettings.Api.TradePrivacyResponse`)

See [Roblox.AccountSettings.Api.TradePrivacyResponse](#roblox-accountsettings-api-tradeprivacyresponse) in Models.

**Response example:**
```json
{
  "tradePrivacy": "string"
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://accountsettings.roblox.com/v1/trade-privacy"
```

### POST `/v1/trade-privacy`

Updates a user's trade privacy setting

**Server:** `https://accountsettings.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Request Body:** `application/json` — Type: `Roblox.AccountSettings.Api.UpdateTradePrivacyRequest`

See [Roblox.AccountSettings.Api.UpdateTradePrivacyRequest](#roblox-accountsettings-api-updatetradeprivacyrequest) in Models.

**Request example:**
```json
{
  "tradePrivacy": 0
}
```

**Responses:**

- `200`: OK → `Roblox.AccountSettings.Api.TradePrivacyUpdateResponse`
- `400`: Roblox.AccountSettings.Api.ResponseEnums.TradeSettingsErrors.InvalidTradePrivacy
- `401`: 0: Authorization has been denied for this request.
- `403`: Roblox.AccountSettings.Api.ResponseEnums.TradeSettingsErrors.AccountLocked             OR             Roblox.AccountSettings.Api.ResponseEnums.TradeSettingsErrors.UserCannotTrade 0: Token Validation Failed

**Response fields** (`Roblox.AccountSettings.Api.TradePrivacyUpdateResponse`)

See [Roblox.AccountSettings.Api.TradePrivacyUpdateResponse](#roblox-accountsettings-api-tradeprivacyupdateresponse) in Models.

**Response example:**
```json
{
  "tradePrivacy": 0,
  "inventoryPrivacy": 1,
  "privacySettingResponse": 0
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://accountsettings.roblox.com/v1/trade-privacy" \
  -H "Content-Type: application/json" \
  -d '{
  "tradePrivacy": 0
}'
```

### GET `/v1/trade-value`

Get a user's trade quality filter setting

**Server:** `https://accountsettings.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Responses:**

- `200`: OK → `Roblox.AccountSettings.Api.TradeValueResponse`
- `401`: 0: Authorization has been denied for this request.

**Response fields** (`Roblox.AccountSettings.Api.TradeValueResponse`)

See [Roblox.AccountSettings.Api.TradeValueResponse](#roblox-accountsettings-api-tradevalueresponse) in Models.

**Response example:**
```json
{
  "tradeValue": "string"
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://accountsettings.roblox.com/v1/trade-value"
```

### POST `/v1/trade-value`

Updates a user's trade quality filter setting

**Server:** `https://accountsettings.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Request Body:** `application/json` — Type: `Roblox.AccountSettings.Api.TradeValueRequest`

See [Roblox.AccountSettings.Api.TradeValueRequest](#roblox-accountsettings-api-tradevaluerequest) in Models.

**Request example:**
```json
{
  "tradeValue": 0
}
```

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: Roblox.AccountSettings.Api.ResponseEnums.TradeSettingsErrors.InvalidTradeValue
- `401`: 0: Authorization has been denied for this request.
- `403`: Roblox.AccountSettings.Api.ResponseEnums.TradeSettingsErrors.AccountLocked             OR             Roblox.AccountSettings.Api.ResponseEnums.TradeSettingsErrors.UserCannotTrade 0: Token Validation Failed

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://accountsettings.roblox.com/v1/trade-value" \
  -H "Content-Type: application/json" \
  -d '{
  "tradeValue": 0
}'
```

### POST `/v1/user/passwords/change`

Changes the password for the authenticated user.

The current password is needed for verification that the password can be changed.

**Server:** `https://auth.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Request Body:** `application/json` — Type: `Roblox.Authentication.Api.Models.PasswordChangeModel`

See [Roblox.Authentication.Api.Models.PasswordChangeModel](#roblox-authentication-api-models-passwordchangemodel) in Models.

**Request example:**
```json
{
  "currentPassword": "string",
  "newPassword": "string",
  "secureAuthenticationIntent": {
    "clientPublicKey": "string",
    "clientEpochTimestamp": 0,
    "saiSignature": "string",
    "serverNonce": "string"
  }
}
```

**Responses:**

- `200`: Password successfully changed. → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: Roblox.Web.Authentication.Passwords.PasswordResponseCodes.InvalidCurrentPassword             OR             Roblox.Web.Authentication.Passwords.PasswordResponseCodes.InvalidPassword             OR             Roblox.Web.Authentication.Passwords.PasswordResponseCodes.PasswordLowComplexity             OR             Roblox.Web.Authentication.Passwords.PasswordResponseCodes.PasswordTooSimilarToUsername
- `401`: 0: Authorization has been denied for this request.
- `403`: Roblox.Web.Authentication.Passwords.PasswordResponseCodes.PinLocked
- `429`: Roblox.Web.Authentication.Passwords.PasswordResponseCodes.Flooded

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `429`: Retry with exponential backoff (start at 1s). `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://auth.roblox.com/v1/user/passwords/change" \
  -H "Content-Type: application/json" \
  -d '{
  "currentPassword": "string",
  "newPassword": "string",
  "secureAuthenticationIntent": {
    "clientPublicKey": "string",
    "clientEpochTimestamp": 0,
    "saiSignature": "string",
    "serverNonce": "string"
  }
}'
```

### POST `/v1/username`

Change the user's username

**Server:** `https://auth.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Request Body:** `application/json` — Type: `Roblox.Authentication.Api.Models.UsernameChangeRequest`

See [Roblox.Authentication.Api.Models.UsernameChangeRequest](#roblox-authentication-api-models-usernamechangerequest) in Models.

**Request example:**
```json
{
  "username": "string",
  "password": "string"
}
```

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: 5: You don't have enough Robux to change your username. 10: This username is already in use 11: Username not appropriate for Roblox 12: Usernames can be 3 to 20 characters long 13: Usernames can’t start or end with _ and can have at most one _ 14: Only a-z, A-Z, 0-9, and _ are allowed 15: Username is null 16: Username might contain private information 17: This username is not available 18: Username is same as current
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 1: PIN is locked. 2: A verified email is missing 3: Your password is incorrect. 100: Unknown birthday
- `500`: 0: An unknown error occured. 5: You don't have enough Robux to change your username.
- `503`: 4: The feature is currently not available. Please try again later.

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://auth.roblox.com/v1/username" \
  -H "Content-Type: application/json" \
  -d '{
  "username": "string",
  "password": "string"
}'
```

### GET `/v1/username/change/price`

Get the current price for a username change

**Server:** `https://auth.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Responses:**

- `200`: OK → `Roblox.Authentication.Api.Models.UsernameChangePriceResponse`
- `401`: 0: Authorization has been denied for this request.

**Response fields** (`Roblox.Authentication.Api.Models.UsernameChangePriceResponse`)

See [Roblox.Authentication.Api.Models.UsernameChangePriceResponse](#roblox-authentication-api-models-usernamechangepriceresponse) in Models.

**Response example:**
```json
{
  "priceInRobux": 0,
  "basePriceInRobux": 0,
  "isFreeUsernameChange": false
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://auth.roblox.com/v1/username/change/price"
```

### GET `/v1/usernames`

Gets a list of existing usernames on Roblox based on the query parameters

This endpoint can be expanded in the future to include other query parameters such as "startsWith"

**Server:** `https://auth.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `username` | query | `string` | Yes | The username |

**Responses:**

- `200`: OK → `Roblox.Authentication.Api.Models.UsernamesResponse`

**Response fields** (`Roblox.Authentication.Api.Models.UsernamesResponse`)

See [Roblox.Authentication.Api.Models.UsernamesResponse](#roblox-authentication-api-models-usernamesresponse) in Models.

**Response example:**
```json
{
  "usernames": [
    "string"
  ]
}
```

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://auth.roblox.com/v1/usernames?username={VALUE}"
```

### POST `/v1/usernames/recover`

Sends an email of all accounts belonging to an email

**Server:** `https://auth.roblox.com`

**Auth:** 

**Request Body:** `application/json` — Type: `Roblox.Authentication.Api.Models.RecoverUsernameRequest`

See [Roblox.Authentication.Api.Models.RecoverUsernameRequest](#roblox-authentication-api-models-recoverusernamerequest) in Models.

**Request example:**
```json
{
  "targetType": 0,
  "target": "string"
}
```

**Responses:**

- `200`: OK → `Roblox.Authentication.Api.Models.RecoverUsernameResponse`
- `400`: 20: Invalid Email 21: Invalid Phone 23: No Account Found
- `403`: 0: Token Validation Failed 11: Too many attempts. Please wait a bit.
- `500`: 0: An unexpected error occurred.

**Response fields** (`Roblox.Authentication.Api.Models.RecoverUsernameResponse`)

See [Roblox.Authentication.Api.Models.RecoverUsernameResponse](#roblox-authentication-api-models-recoverusernameresponse) in Models.

**Response example:**
```json
{
  "transmissionType": 0
}
```

**Error handling:** `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://auth.roblox.com/v1/usernames/recover" \
  -H "Content-Type: application/json" \
  -d '{
  "targetType": 0,
  "target": "string"
}'
```

### GET `/v1/usernames/validate`

Checks if a username is valid.

**Server:** `https://auth.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `Username` | query | `string` | Yes |  |
| `Birthday` | query | `string` | Yes |  |
| `Context` | query | `0 \| 1 \| 2` | Yes | Valid values: `0`, `1`, `2` |

**Responses:**

- `200`: Success → `Roblox.Authentication.Api.Models.UsernameValidationResponse`
- `400`: 1: A valid username is required. 2: A valid birthday or authenticated user is required.

**Response fields** (`Roblox.Authentication.Api.Models.UsernameValidationResponse`)

See [Roblox.Authentication.Api.Models.UsernameValidationResponse](#roblox-authentication-api-models-usernamevalidationresponse) in Models.

**Response example:**
```json
{
  "code": 0,
  "message": "string"
}
```

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://auth.roblox.com/v1/usernames/validate?Username={VALUE}&Birthday={VALUE}&Context={VALUE}"
```

### POST `/v1/usernames/validate`

Checks if a username is valid.

**Server:** `https://auth.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Request Body:** `application/json` — Type: `Roblox.Authentication.Api.Models.UsernameValidationRequest`

See [Roblox.Authentication.Api.Models.UsernameValidationRequest](#roblox-authentication-api-models-usernamevalidationrequest) in Models.

**Request example:**
```json
{
  "username": "string",
  "birthday": "2024-01-01T00:00:00Z",
  "context": 0
}
```

**Responses:**

- `200`: Success → `Roblox.Authentication.Api.Models.UsernameValidationResponse`
- `400`: 1: A valid username is required. 2: A valid birthday or authenticated user is required.
- `403`: 0: Token Validation Failed

**Response fields** (`Roblox.Authentication.Api.Models.UsernameValidationResponse`)

See [Roblox.Authentication.Api.Models.UsernameValidationResponse](#roblox-authentication-api-models-usernamevalidationresponse) in Models.

**Response example:**
```json
{
  "code": 0,
  "message": "string"
}
```

**Error handling:** `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://auth.roblox.com/v1/usernames/validate" \
  -H "Content-Type: application/json" \
  -d '{
  "username": "string",
  "birthday": "2024-01-01T00:00:00Z",
  "context": 0
}'
```

### GET `/v1/users/authenticated`

Gets the minimal authenticated user.

**Server:** `https://users.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Responses:**

- `200`: OK → `Roblox.Users.Api.AuthenticatedGetUserResponse`
- `401`: 0: Authorization has been denied for this request.

**Response fields** (`Roblox.Users.Api.AuthenticatedGetUserResponse`)

See [Roblox.Users.Api.AuthenticatedGetUserResponse](#roblox-users-api-authenticatedgetuserresponse) in Models.

**Response example:**
```json
{
  "id": 0,
  "name": "string",
  "displayName": "string"
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://users.roblox.com/v1/users/authenticated"
```

### GET `/v1/users/authenticated/age-bracket`

Gets the age bracket of the authenticated user.

**Server:** `https://users.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Responses:**

- `200`: OK → `Roblox.Users.Api.UserAgeBracketResponse`
- `401`: 0: Authorization has been denied for this request.

**Response fields** (`Roblox.Users.Api.UserAgeBracketResponse`)

See [Roblox.Users.Api.UserAgeBracketResponse](#roblox-users-api-useragebracketresponse) in Models.

**Response example:**
```json
{
  "ageBracket": 0
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://users.roblox.com/v1/users/authenticated/age-bracket"
```

### GET `/v1/users/authenticated/country-code`

Gets the country code of the authenticated user.

**Server:** `https://users.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Responses:**

- `200`: OK → `Roblox.Users.Api.UserCountryCodeResponse`
- `401`: 0: Authorization has been denied for this request.

**Response fields** (`Roblox.Users.Api.UserCountryCodeResponse`)

See [Roblox.Users.Api.UserCountryCodeResponse](#roblox-users-api-usercountrycoderesponse) in Models.

**Response example:**
```json
{
  "countryCode": "string"
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://users.roblox.com/v1/users/authenticated/country-code"
```

### GET `/v1/users/authenticated/roles`

Gets the (public) roles of the authenticated user, such as `"Soothsayer"` and `"BetaTester"`.

**Server:** `https://users.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Responses:**

- `200`: OK → `Roblox.Users.Api.UserRolesResponse`
- `401`: 0: Authorization has been denied for this request.

**Response fields** (`Roblox.Users.Api.UserRolesResponse`)

See [Roblox.Users.Api.UserRolesResponse](#roblox-users-api-userrolesresponse) in Models.

**Response example:**
```json
{
  "roles": [
    "string"
  ]
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://users.roblox.com/v1/users/authenticated/roles"
```

### GET `/v1/users/{userId}/can-view-inventory`

Gets whether the specified user's inventory can be viewed.

**Server:** `https://inventory.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer` | Yes | The user identifier. |

**Responses:**

- `200`: OK → `Roblox.Inventory.Api.Models.CanViewInventoryResponse`
- `400`: 1: The specified user does not exist!

**Response fields** (`Roblox.Inventory.Api.Models.CanViewInventoryResponse`)

See [Roblox.Inventory.Api.Models.CanViewInventoryResponse](#roblox-inventory-api-models-canviewinventoryresponse) in Models.

**Response example:**
```json
{
  "canView": false
}
```

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://inventory.roblox.com/v1/users/{USERID}/can-view-inventory"
```

### POST `/v1/users/{userId}/challenges/authenticator/verify`

Verifies a two step verification challenge code via authenticator app.

**Server:** `https://twostepverification.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer` | Yes | The user ID. |

**Responses:**

- `200`: OK → `Roblox.TwoStepVerification.Api.VerifyCodeResponse`
- `400`: 1: Invalid challenge ID. 2: The user ID is invalid. 10: The two step verification challenge code is invalid.
- `403`: 0: Token Validation Failed
- `429`: 5: Too many requests.
- `503`: 7: Two step verification is currently under maintenance.

**Response fields** (`Roblox.TwoStepVerification.Api.VerifyCodeResponse`)

See [Roblox.TwoStepVerification.Api.VerifyCodeResponse](#roblox-twostepverification-api-verifycoderesponse) in Models.

**Response example:**
```json
{
  "verificationToken": "string"
}
```

**Error handling:** `429`: Retry with exponential backoff (start at 1s). `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://twostepverification.roblox.com/v1/users/{USERID}/challenges/authenticator/verify" \
  -H "Content-Type: application/json" \
  -d '{"key": "value"}'
```

### POST `/v1/users/{userId}/challenges/cross-device/retract`

Reverts a user's dialog state from ACTIVE to PENDING.

**Server:** `https://twostepverification.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer` | Yes | The user ID. |

**Request Body:** `application/json` — Type: `Roblox.TwoStepVerification.Api.RetractDialogRequest`

See [Roblox.TwoStepVerification.Api.RetractDialogRequest](#roblox-twostepverification-api-retractdialogrequest) in Models.

**Request example:**
```json
{
  "challengeId": "string",
  "actionType": 0
}
```

**Responses:**

- `200`: OK → `Roblox.TwoStepVerification.Api.RetractDialogResponse`
- `400`: 1: Invalid challenge ID. 2: The user ID is invalid.
- `403`: 0: Token Validation Failed 19: Challenge denied.
- `503`: 7: Two step verification is currently under maintenance.

**Response fields** (`Roblox.TwoStepVerification.Api.RetractDialogResponse`)

See [Roblox.TwoStepVerification.Api.RetractDialogResponse](#roblox-twostepverification-api-retractdialogresponse) in Models.

**Error handling:** `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://twostepverification.roblox.com/v1/users/{USERID}/challenges/cross-device/retract" \
  -H "Content-Type: application/json" \
  -d '{
  "challengeId": "string",
  "actionType": 0
}'
```

### POST `/v1/users/{userId}/challenges/cross-device/retry`

Retry a Cross Device two step verification approval.

**Server:** `https://twostepverification.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer` | Yes | The user ID. |

**Request Body:** `application/json` — Type: `Roblox.TwoStepVerification.Api.RetryApprovalRequest`

See [Roblox.TwoStepVerification.Api.RetryApprovalRequest](#roblox-twostepverification-api-retryapprovalrequest) in Models.

**Request example:**
```json
{
  "challengeId": "string",
  "actionType": 0
}
```

**Responses:**

- `200`: OK → `Roblox.TwoStepVerification.Api.RetryApprovalResponse`
- `400`: 1: Invalid challenge ID. 2: The user ID is invalid.
- `403`: 0: Token Validation Failed 19: Challenge denied.
- `503`: 7: Two step verification is currently under maintenance.

**Response fields** (`Roblox.TwoStepVerification.Api.RetryApprovalResponse`)

See [Roblox.TwoStepVerification.Api.RetryApprovalResponse](#roblox-twostepverification-api-retryapprovalresponse) in Models.

**Error handling:** `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://twostepverification.roblox.com/v1/users/{USERID}/challenges/cross-device/retry" \
  -H "Content-Type: application/json" \
  -d '{
  "challengeId": "string",
  "actionType": 0
}'
```

### POST `/v1/users/{userId}/challenges/cross-device/verify`

Verifies a two step verification approval via Cross Device. Cross Device approval does not use a verification code.

**Server:** `https://twostepverification.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer` | Yes | The user ID. |

**Request Body:** `application/json` — Type: `Roblox.TwoStepVerification.Api.VerifyApprovalRequest`

See [Roblox.TwoStepVerification.Api.VerifyApprovalRequest](#roblox-twostepverification-api-verifyapprovalrequest) in Models.

**Request example:**
```json
{
  "challengeId": "string",
  "actionType": 0
}
```

**Responses:**

- `200`: OK → `Roblox.TwoStepVerification.Api.VerifyApprovalResponse`
- `400`: 0: An unknown error occurred with the request. 1: Invalid challenge ID. 2: The user ID is invalid.
- `403`: 0: Token Validation Failed 19: Challenge denied.
- `503`: 7: Two step verification is currently under maintenance.

**Response fields** (`Roblox.TwoStepVerification.Api.VerifyApprovalResponse`)

See [Roblox.TwoStepVerification.Api.VerifyApprovalResponse](#roblox-twostepverification-api-verifyapprovalresponse) in Models.

**Response example:**
```json
{
  "verificationToken": "string"
}
```

**Error handling:** `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://twostepverification.roblox.com/v1/users/{USERID}/challenges/cross-device/verify" \
  -H "Content-Type: application/json" \
  -d '{
  "challengeId": "string",
  "actionType": 0
}'
```

### POST `/v1/users/{userId}/challenges/email/send-code`

Sends a two step verification challenge code via email.

**Server:** `https://twostepverification.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer` | Yes | The user ID. |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: 1: Invalid challenge ID.
- `403`: 0: Token Validation Failed 2: The user ID is invalid.
- `429`: 5: Too many requests.
- `503`: 7: Two step verification is currently under maintenance.

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `429`: Retry with exponential backoff (start at 1s). `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://twostepverification.roblox.com/v1/users/{USERID}/challenges/email/send-code" \
  -H "Content-Type: application/json" \
  -d '{"key": "value"}'
```

### POST `/v1/users/{userId}/challenges/email/verify`

Verifies a two step verification challenge with a code sent via email.

**Server:** `https://twostepverification.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer` | Yes | The user ID. |

**Responses:**

- `200`: OK → `Roblox.TwoStepVerification.Api.VerifyCodeResponse`
- `400`: 1: Invalid challenge ID. 10: The two step verification challenge code is invalid.
- `403`: 0: Token Validation Failed 2: The user ID is invalid.
- `429`: 5: Too many requests.
- `503`: 7: Two step verification is currently under maintenance.

**Response fields** (`Roblox.TwoStepVerification.Api.VerifyCodeResponse`)

See [Roblox.TwoStepVerification.Api.VerifyCodeResponse](#roblox-twostepverification-api-verifycoderesponse) in Models.

**Response example:**
```json
{
  "verificationToken": "string"
}
```

**Error handling:** `429`: Retry with exponential backoff (start at 1s). `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://twostepverification.roblox.com/v1/users/{USERID}/challenges/email/verify" \
  -H "Content-Type: application/json" \
  -d '{"key": "value"}'
```

### POST `/v1/users/{userId}/challenges/passkey/verify-finish`

Validates the assertion data returned by the passkey.

**Server:** `https://twostepverification.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer` | Yes | The user ID. |

**Responses:**

- `200`: OK → `Roblox.TwoStepVerification.Api.VerifyCodeResponse`
- `400`: 1: Invalid challenge ID. 2: The user ID is invalid. 10: The two step verification challenge code is invalid.
- `403`: 0: Token Validation Failed
- `503`: 7: Two step verification is currently under maintenance.

**Response fields** (`Roblox.TwoStepVerification.Api.VerifyCodeResponse`)

See [Roblox.TwoStepVerification.Api.VerifyCodeResponse](#roblox-twostepverification-api-verifycoderesponse) in Models.

**Response example:**
```json
{
  "verificationToken": "string"
}
```

**Error handling:** `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://twostepverification.roblox.com/v1/users/{USERID}/challenges/passkey/verify-finish" \
  -H "Content-Type: application/json" \
  -d '{"key": "value"}'
```

### POST `/v1/users/{userId}/challenges/passkey/verify-start`

Provides a challenge for the passkey to authenticate.

**Server:** `https://twostepverification.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer` | Yes | The user ID. |

**Responses:**

- `200`: OK → `Roblox.TwoStepVerification.Api.VerifyStartPasskeyResponse`
- `400`: 1: Invalid challenge ID. 2: The user ID is invalid.
- `403`: 0: Token Validation Failed 8: The user is not allowed to perform the requested action.
- `503`: 7: Two step verification is currently under maintenance.

**Response fields** (`Roblox.TwoStepVerification.Api.VerifyStartPasskeyResponse`)

See [Roblox.TwoStepVerification.Api.VerifyStartPasskeyResponse](#roblox-twostepverification-api-verifystartpasskeyresponse) in Models.

**Response example:**
```json
{
  "authenticationOptions": "string",
  "sessionId": "string"
}
```

**Error handling:** `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://twostepverification.roblox.com/v1/users/{USERID}/challenges/passkey/verify-start" \
  -H "Content-Type: application/json" \
  -d '{"key": "value"}'
```

### POST `/v1/users/{userId}/challenges/password/verify`

Verifies a two step verification challenge with a password (code).

**Server:** `https://twostepverification.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer` | Yes | The user ID. |

**Responses:**

- `200`: OK → `Roblox.TwoStepVerification.Api.VerifyCodeResponse`
- `400`: 1: Invalid challenge ID. 4: The password is invalid.
- `403`: 0: Token Validation Failed 2: The user ID is invalid.
- `429`: 5: Too many requests.
- `503`: 7: Two step verification is currently under maintenance.

**Response fields** (`Roblox.TwoStepVerification.Api.VerifyCodeResponse`)

See [Roblox.TwoStepVerification.Api.VerifyCodeResponse](#roblox-twostepverification-api-verifycoderesponse) in Models.

**Response example:**
```json
{
  "verificationToken": "string"
}
```

**Error handling:** `429`: Retry with exponential backoff (start at 1s). `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://twostepverification.roblox.com/v1/users/{USERID}/challenges/password/verify" \
  -H "Content-Type: application/json" \
  -d '{"key": "value"}'
```

### POST `/v1/users/{userId}/challenges/recovery-codes/verify`

Verifies a two step verification challenge via a recovery code.

Once a recovery code has been used to verify a challenge it cannot be used again.

**Server:** `https://twostepverification.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer` | Yes | The user ID. |

**Responses:**

- `200`: OK → `Roblox.TwoStepVerification.Api.VerifyCodeResponse`
- `400`: 1: Invalid challenge ID. 2: The user ID is invalid. 10: The two step verification challenge code is invalid.
- `403`: 0: Token Validation Failed
- `429`: 5: Too many requests.
- `503`: 7: Two step verification is currently under maintenance.

**Response fields** (`Roblox.TwoStepVerification.Api.VerifyCodeResponse`)

See [Roblox.TwoStepVerification.Api.VerifyCodeResponse](#roblox-twostepverification-api-verifycoderesponse) in Models.

**Response example:**
```json
{
  "verificationToken": "string"
}
```

**Error handling:** `429`: Retry with exponential backoff (start at 1s). `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://twostepverification.roblox.com/v1/users/{USERID}/challenges/recovery-codes/verify" \
  -H "Content-Type: application/json" \
  -d '{"key": "value"}'
```

### POST `/v1/users/{userId}/challenges/security-key/verify-finish`

Validates the assertion data returned by the security key.

**Server:** `https://twostepverification.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer` | Yes | The user ID. |

**Responses:**

- `200`: OK → `Roblox.TwoStepVerification.Api.VerifyCodeResponse`
- `400`: 1: Invalid challenge ID. 2: The user ID is invalid. 10: The two step verification challenge code is invalid.
- `403`: 0: Token Validation Failed
- `503`: 7: Two step verification is currently under maintenance.

**Response fields** (`Roblox.TwoStepVerification.Api.VerifyCodeResponse`)

See [Roblox.TwoStepVerification.Api.VerifyCodeResponse](#roblox-twostepverification-api-verifycoderesponse) in Models.

**Response example:**
```json
{
  "verificationToken": "string"
}
```

**Error handling:** `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://twostepverification.roblox.com/v1/users/{USERID}/challenges/security-key/verify-finish" \
  -H "Content-Type: application/json" \
  -d '{"key": "value"}'
```

### POST `/v1/users/{userId}/challenges/security-key/verify-start`

Provides a challenge for the security key to authenticate.

**Server:** `https://twostepverification.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer` | Yes | The user ID. |

**Responses:**

- `200`: OK → `Roblox.TwoStepVerification.Api.VerifyStartSecurityKeyResponse`
- `400`: 1: Invalid challenge ID. 2: The user ID is invalid.
- `403`: 0: Token Validation Failed 8: The user is not allowed to perform the requested action.
- `503`: 7: Two step verification is currently under maintenance.

**Response fields** (`Roblox.TwoStepVerification.Api.VerifyStartSecurityKeyResponse`)

See [Roblox.TwoStepVerification.Api.VerifyStartSecurityKeyResponse](#roblox-twostepverification-api-verifystartsecuritykeyresponse) in Models.

**Response example:**
```json
{
  "authenticationOptions": "string",
  "sessionId": "string"
}
```

**Error handling:** `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://twostepverification.roblox.com/v1/users/{USERID}/challenges/security-key/verify-start" \
  -H "Content-Type: application/json" \
  -d '{"key": "value"}'
```

### POST `/v1/users/{userId}/challenges/sms/send-code`

Sends a two step verification code via SMS for the specified user.

**Server:** `https://twostepverification.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer` | Yes | The user ID. |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: 1: Invalid challenge ID.
- `403`: 0: Token Validation Failed 2: The user ID is invalid.
- `429`: 5: Too many requests.
- `503`: 7: Two step verification is currently under maintenance.

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `429`: Retry with exponential backoff (start at 1s). `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://twostepverification.roblox.com/v1/users/{USERID}/challenges/sms/send-code" \
  -H "Content-Type: application/json" \
  -d '{"key": "value"}'
```

### POST `/v1/users/{userId}/challenges/sms/verify`

Verifies a two step verification challenge with a code sent via SMS.

**Server:** `https://twostepverification.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer` | Yes | The user ID. |

**Responses:**

- `200`: OK → `Roblox.TwoStepVerification.Api.VerifyCodeResponse`
- `400`: 1: Invalid challenge ID. 2: The user ID is invalid. 10: The two step verification challenge code is invalid.
- `403`: 0: Token Validation Failed
- `429`: 5: Too many requests.
- `503`: 7: Two step verification is currently under maintenance.

**Response fields** (`Roblox.TwoStepVerification.Api.VerifyCodeResponse`)

See [Roblox.TwoStepVerification.Api.VerifyCodeResponse](#roblox-twostepverification-api-verifycoderesponse) in Models.

**Response example:**
```json
{
  "verificationToken": "string"
}
```

**Error handling:** `429`: Retry with exponential backoff (start at 1s). `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://twostepverification.roblox.com/v1/users/{USERID}/challenges/sms/verify" \
  -H "Content-Type: application/json" \
  -d '{"key": "value"}'
```

### GET `/v1/users/{userId}/configuration`

Gets two step verification configuration for the specified user.

**Server:** `https://twostepverification.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer` | Yes | The Id of the user to get the configuration for. |
| `challengeId` | query | `string` | No | The active challenge for the user (as an alternative when the user is unauthenticated). |
| `actionType` | query | `integer enum (9 values)` | No | The action type the challengeId is associated with. Valid values: `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8` |

**Responses:**

- `200`: OK → `Roblox.TwoStepVerification.Api.UserConfiguration`
- `400`: 1: Invalid challenge ID.
- `403`: 2: The user ID is invalid.

**Response fields** (`Roblox.TwoStepVerification.Api.UserConfiguration`)

See [Roblox.TwoStepVerification.Api.UserConfiguration](#roblox-twostepverification-api-userconfiguration) in Models.

**Response example:**
```json
{
  "primaryMediaType": 0,
  "methods": [
    {
      "mediaType": "...",
      "enabled": "...",
      "updated": "..."
    }
  ]
}
```

**Error handling:** `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://twostepverification.roblox.com/v1/users/{USERID}/configuration"
```

### POST `/v1/users/{userId}/configuration/authenticator/disable`

Disables two step verification via authenticator for the specified user.

**Server:** `https://twostepverification.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer` | Yes | The user ID. |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: 2: The user ID is invalid. 4: The password is invalid.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 8: The user is not allowed to perform the requested action.
- `429`: 5: Too many requests.
- `503`: 7: Two step verification is currently under maintenance.

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `429`: Retry with exponential backoff (start at 1s). `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://twostepverification.roblox.com/v1/users/{USERID}/configuration/authenticator/disable" \
  -H "Content-Type: application/json" \
  -d '{"key": "value"}'
```

### POST `/v1/users/{userId}/configuration/authenticator/enable`

Initiates enabling authenticator-based two step verification for the specified user.

**Server:** `https://twostepverification.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer` | Yes | The user ID. |

**Request Body:** `application/json` — Type: `Roblox.TwoStepVerification.Api.EnableTwoStepVerificationRequest`

See [Roblox.TwoStepVerification.Api.EnableTwoStepVerificationRequest](#roblox-twostepverification-api-enabletwostepverificationrequest) in Models.

**Request example:**
```json
{
  "password": "string",
  "secureAuthenticationIntent": {
    "clientPublicKey": "string",
    "clientEpochTimestamp": 0,
    "saiSignature": "string",
    "serverNonce": "string"
  }
}
```

**Responses:**

- `200`: OK → `Roblox.TwoStepVerification.Api.EnableAuthenticatorResponse`
- `400`: 2: The user ID is invalid. 3: The email is invalid. 4: The password is invalid.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 11: The two step verification configuration is already enabled.
- `503`: 7: Two step verification is currently under maintenance.

**Response fields** (`Roblox.TwoStepVerification.Api.EnableAuthenticatorResponse`)

See [Roblox.TwoStepVerification.Api.EnableAuthenticatorResponse](#roblox-twostepverification-api-enableauthenticatorresponse) in Models.

**Response example:**
```json
{
  "setupToken": "string",
  "qrCodeImageUrl": "string",
  "manualEntryKey": "string"
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://twostepverification.roblox.com/v1/users/{USERID}/configuration/authenticator/enable" \
  -H "Content-Type: application/json" \
  -d '{
  "password": "string",
  "secureAuthenticationIntent": {
    "clientPublicKey": "string",
    "clientEpochTimestamp": 0,
    "saiSignature": "string",
    "serverNonce": "string"
  }
}'
```

### POST `/v1/users/{userId}/configuration/authenticator/enable-verify`

Finishes enabling authenticator-based two step verification for the specified user.

Enabling authenticator-based two step verification requires two parts to help ensure
the user has properly stored the authenticator key in their authenticator app.

**Server:** `https://twostepverification.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer` | Yes | The user ID. |

**Request Body:** `application/json` — Type: `Roblox.TwoStepVerification.Api.EnableVerifyAuthenticatorRequest`

See [Roblox.TwoStepVerification.Api.EnableVerifyAuthenticatorRequest](#roblox-twostepverification-api-enableverifyauthenticatorrequest) in Models.

**Request example:**
```json
{
  "setupToken": "string",
  "code": "string",
  "password": "string",
  "secureAuthenticationIntent": {
    "clientPublicKey": "string",
    "clientEpochTimestamp": 0,
    "saiSignature": "string",
    "serverNonce": "string"
  }
}
```

**Responses:**

- `200`: OK → `Roblox.TwoStepVerification.Api.EnableVerifyAuthenticatorResponse`
- `400`: 2: The user ID is invalid. 4: The password is invalid. 10: The two step verification challenge code is invalid. 12: Invalid setup token.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 11: The two step verification configuration is already enabled.
- `503`: 7: Two step verification is currently under maintenance.

**Response fields** (`Roblox.TwoStepVerification.Api.EnableVerifyAuthenticatorResponse`)

See [Roblox.TwoStepVerification.Api.EnableVerifyAuthenticatorResponse](#roblox-twostepverification-api-enableverifyauthenticatorresponse) in Models.

**Response example:**
```json
{
  "recoveryCodes": [
    "string"
  ]
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://twostepverification.roblox.com/v1/users/{USERID}/configuration/authenticator/enable-verify" \
  -H "Content-Type: application/json" \
  -d '{
  "setupToken": "string",
  "code": "string",
  "password": "string",
  "secureAuthenticationIntent": {
    "clientPublicKey": "string",
    "clientEpochTimestamp": 0,
    "saiSignature": "string",
    "serverNonce": "string"
  }
}'
```

### POST `/v1/users/{userId}/configuration/email/disable`

Disables two step verification via email for the specified user.

**Server:** `https://twostepverification.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer` | Yes | The user ID. |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: 4: The password is invalid.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 2: The user ID is invalid. 8: The user is not allowed to perform the requested action.
- `429`: 5: Too many requests.
- `503`: 7: Two step verification is currently under maintenance.

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `429`: Retry with exponential backoff (start at 1s). `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://twostepverification.roblox.com/v1/users/{USERID}/configuration/email/disable" \
  -H "Content-Type: application/json" \
  -d '{"key": "value"}'
```

### POST `/v1/users/{userId}/configuration/email/enable`

Enables two step verification via email for the specified user.

**Server:** `https://twostepverification.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer` | Yes | The user ID. |

**Request Body:** `application/json` — Type: `Roblox.TwoStepVerification.Api.EnableTwoStepVerificationRequest`

See [Roblox.TwoStepVerification.Api.EnableTwoStepVerificationRequest](#roblox-twostepverification-api-enabletwostepverificationrequest) in Models.

**Request example:**
```json
{
  "password": "string",
  "secureAuthenticationIntent": {
    "clientPublicKey": "string",
    "clientEpochTimestamp": 0,
    "saiSignature": "string",
    "serverNonce": "string"
  }
}
```

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: 3: The email is invalid. 4: The password is invalid.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 2: The user ID is invalid.
- `503`: 7: Two step verification is currently under maintenance.

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://twostepverification.roblox.com/v1/users/{USERID}/configuration/email/enable" \
  -H "Content-Type: application/json" \
  -d '{
  "password": "string",
  "secureAuthenticationIntent": {
    "clientPublicKey": "string",
    "clientEpochTimestamp": 0,
    "saiSignature": "string",
    "serverNonce": "string"
  }
}'
```

### POST `/v1/users/{userId}/configuration/security-key/disable`

Disables a batch of credentials for the specified user.

**Server:** `https://twostepverification.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer` | Yes | The user ID. |

**Request Body:** `application/json` — Type: `Roblox.TwoStepVerification.Api.DisableSecurityKeyRequest`

See [Roblox.TwoStepVerification.Api.DisableSecurityKeyRequest](#roblox-twostepverification-api-disablesecuritykeyrequest) in Models.

**Request example:**
```json
{
  "credentialNicknames": [
    "string"
  ],
  "credentialIDs": [
    "string"
  ]
}
```

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: 4: The password is invalid.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 8: The user is not allowed to perform the requested action.
- `503`: 7: Two step verification is currently under maintenance.

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://twostepverification.roblox.com/v1/users/{USERID}/configuration/security-key/disable" \
  -H "Content-Type: application/json" \
  -d '{
  "credentialNicknames": [
    "string"
  ],
  "credentialIDs": [
    "string"
  ]
}'
```

### POST `/v1/users/{userId}/configuration/security-key/enable`

Initiates security key registration by providing credential creation options.

**Server:** `https://twostepverification.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer` | Yes | The user ID. |

**Responses:**

- `200`: OK → `Roblox.TwoStepVerification.Api.EnableSecurityKeyResponse`
- `400`: 2: The user ID is invalid. 4: The password is invalid.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 9: The two step verification configuration is invalid for this action. 16: Reached limit of security keys registered.
- `503`: 7: Two step verification is currently under maintenance.

**Response fields** (`Roblox.TwoStepVerification.Api.EnableSecurityKeyResponse`)

See [Roblox.TwoStepVerification.Api.EnableSecurityKeyResponse](#roblox-twostepverification-api-enablesecuritykeyresponse) in Models.

**Response example:**
```json
{
  "creationOptions": "string",
  "sessionId": "string"
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://twostepverification.roblox.com/v1/users/{USERID}/configuration/security-key/enable" \
  -H "Content-Type: application/json" \
  -d '{"key": "value"}'
```

### POST `/v1/users/{userId}/configuration/security-key/enable-verify`

Finishes security key registration and stores credential. Enables security key as a 2sv media type if it is a user's first key.

**Server:** `https://twostepverification.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer` | Yes | The user ID. |

**Request Body:** `application/json` — Type: `Roblox.TwoStepVerification.Api.EnableVerifySecurityKeyRequest`

See [Roblox.TwoStepVerification.Api.EnableVerifySecurityKeyRequest](#roblox-twostepverification-api-enableverifysecuritykeyrequest) in Models.

**Request example:**
```json
{
  "sessionId": "string",
  "credentialNickname": "string",
  "attestationResponse": "string"
}
```

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: 2: The user ID is invalid. 17: Invalid security key nickname.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 17: Invalid security key nickname.
- `503`: 7: Two step verification is currently under maintenance.

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://twostepverification.roblox.com/v1/users/{USERID}/configuration/security-key/enable-verify" \
  -H "Content-Type: application/json" \
  -d '{
  "sessionId": "string",
  "credentialNickname": "string",
  "attestationResponse": "string"
}'
```

### POST `/v1/users/{userId}/configuration/security-key/list`

List a user's registered security keys.

**Server:** `https://twostepverification.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer` | Yes | The user ID. |

**Responses:**

- `200`: OK → `Roblox.TwoStepVerification.Api.ListSecurityKeyResponse`
- `400`: 2: The user ID is invalid.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed
- `503`: 7: Two step verification is currently under maintenance.

**Response fields** (`Roblox.TwoStepVerification.Api.ListSecurityKeyResponse`)

See [Roblox.TwoStepVerification.Api.ListSecurityKeyResponse](#roblox-twostepverification-api-listsecuritykeyresponse) in Models.

**Response example:**
```json
{
  "credentials": [
    {
      "nickname": "...",
      "credentialID": "..."
    }
  ]
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://twostepverification.roblox.com/v1/users/{USERID}/configuration/security-key/list"
```

### POST `/v1/users/{userId}/configuration/sms/disable`

Disables two step verification via SMS for the specified user.

**Server:** `https://twostepverification.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer` | Yes | The user ID. |

**Request Body:** `application/json` — Type: `Roblox.TwoStepVerification.Api.DisableTwoStepVerificationRequest`

See [Roblox.TwoStepVerification.Api.DisableTwoStepVerificationRequest](#roblox-twostepverification-api-disabletwostepverificationrequest) in Models.

**Request example:**
```json
{
  "password": "string",
  "reauthenticationToken": "string"
}
```

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: 4: The password is invalid.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 2: The user ID is invalid. 8: The user is not allowed to perform the requested action.
- `429`: 5: Too many requests.
- `503`: 7: Two step verification is currently under maintenance.

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `429`: Retry with exponential backoff (start at 1s). `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://twostepverification.roblox.com/v1/users/{USERID}/configuration/sms/disable" \
  -H "Content-Type: application/json" \
  -d '{
  "password": "string",
  "reauthenticationToken": "string"
}'
```

### POST `/v1/users/{userId}/configuration/sms/enable`

Enables two step verification via SMS for the specified user.

**Server:** `https://twostepverification.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer` | Yes | The user ID. |

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: 4: The password is invalid. 15: The phone number is invalid.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 2: The user ID is invalid.
- `503`: 7: Two step verification is currently under maintenance. 8: The user is not allowed to perform the requested action.

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://twostepverification.roblox.com/v1/users/{USERID}/configuration/sms/enable" \
  -H "Content-Type: application/json" \
  -d '{"key": "value"}'
```

### GET `/v1/users/{userId}/promotion-channels`

Get promotion channels for a given user ID

**Server:** `https://accountinformation.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer` | Yes | The ID of the user to fetch the promotion channels for. |
| `alwaysReturnUrls` | query | `boolean` | No | Whether all promotion channel links should be returned as full URLs. |
| `filterLink` | query | `boolean` | No | Whether all promotion channel links should be filtered. |

**Responses:**

- `200`: OK → `Roblox.AccountInformation.Api.Models.PromotionChannelsByUserIdResponse`
- `400`: 1: User not found.

**Response fields** (`Roblox.AccountInformation.Api.Models.PromotionChannelsByUserIdResponse`)

See [Roblox.AccountInformation.Api.Models.PromotionChannelsByUserIdResponse](#roblox-accountinformation-api-models-promotionchannelsbyuseridresponse) in Models.

**Response example:**
```json
{
  "facebook": "string",
  "twitter": "string",
  "youtube": "string",
  "twitch": "string"
}
```

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://accountinformation.roblox.com/v1/users/{USERID}/promotion-channels"
```

### GET `/v1/users/{userId}/recovery-codes`

Gets the current status of recovery codes for a user.

**Server:** `https://twostepverification.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer` | Yes | The user ID. |

**Responses:**

- `200`: OK → `Roblox.TwoStepVerification.Api.RecoveryCodesStatusResponse`
- `400`: 2: The user ID is invalid.
- `401`: 0: Authorization has been denied for this request.
- `503`: 7: Two step verification is currently under maintenance.

**Response fields** (`Roblox.TwoStepVerification.Api.RecoveryCodesStatusResponse`)

See [Roblox.TwoStepVerification.Api.RecoveryCodesStatusResponse](#roblox-twostepverification-api-recoverycodesstatusresponse) in Models.

**Response example:**
```json
{
  "activeCount": 0,
  "created": "2024-01-01T00:00:00Z"
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://twostepverification.roblox.com/v1/users/{USERID}/recovery-codes"
```

### POST `/v1/users/{userId}/recovery-codes/clear`

Clears any existing recovery codes for the user.

Clearing recovery codes voids any recovery codes previously generated for the user.
New recovery codes will have to be generated to pass two step verification via recovery code.

**Server:** `https://twostepverification.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer` | Yes | The user ID. |

**Request Body:** `application/json` — Type: `Roblox.TwoStepVerification.Api.ClearRecoveryCodesRequest`

See [Roblox.TwoStepVerification.Api.ClearRecoveryCodesRequest](#roblox-twostepverification-api-clearrecoverycodesrequest) in Models.

**Request example:**
```json
{
  "password": "string"
}
```

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: 2: The user ID is invalid. 4: The password is invalid.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed
- `429`: 5: Too many requests.
- `503`: 7: Two step verification is currently under maintenance.

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `429`: Retry with exponential backoff (start at 1s). `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://twostepverification.roblox.com/v1/users/{USERID}/recovery-codes/clear" \
  -H "Content-Type: application/json" \
  -d '{
  "password": "string"
}'
```

### POST `/v1/users/{userId}/recovery-codes/regenerate`

Clears any existing recovery codes and generates a new batch of recovery codes.

Two step verification recovery codes do not enforce that two step verification must be passed when logging in.
At least one two step verification media type must be enabled to trigger the two step verification flow.
Recovery codes are intended to be used to pass two step verification when the enabled media type is unavailable.

Recovery codes generated by this endpoint do not have an expiration.

Once a recovery code generated by this endpoint has been used it cannot be used again.

**Server:** `https://twostepverification.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer` | Yes | The user ID to generate recovery codes for. |

**Request Body:** `application/json` — Type: `Roblox.TwoStepVerification.Api.RegenerateRecoveryCodesRequest`

See [Roblox.TwoStepVerification.Api.RegenerateRecoveryCodesRequest](#roblox-twostepverification-api-regeneraterecoverycodesrequest) in Models.

**Request example:**
```json
{
  "password": "string"
}
```

**Responses:**

- `200`: OK → `Roblox.TwoStepVerification.Api.RegenerateRecoveryCodesResponse`
- `400`: 2: The user ID is invalid. 4: The password is invalid.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed
- `429`: 5: Too many requests.
- `503`: 7: Two step verification is currently under maintenance.

**Response fields** (`Roblox.TwoStepVerification.Api.RegenerateRecoveryCodesResponse`)

See [Roblox.TwoStepVerification.Api.RegenerateRecoveryCodesResponse](#roblox-twostepverification-api-regeneraterecoverycodesresponse) in Models.

**Response example:**
```json
{
  "recoveryCodes": [
    "string"
  ]
}
```

**Error handling:** `429`: Retry with exponential backoff (start at 1s). `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://twostepverification.roblox.com/v1/users/{USERID}/recovery-codes/regenerate" \
  -H "Content-Type: application/json" \
  -d '{
  "password": "string"
}'
```

### GET `/v1/users/{userId}/roblox-badges`

Returns a list of Roblox badges belonging to a user.

**Server:** `https://accountinformation.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer` | Yes |  |

**Responses:**

- `200`: OK → `Roblox.AccountInformation.Api.RobloxBadgeResponse[]`

**Response fields** (`Roblox.AccountInformation.Api.RobloxBadgeResponse[]`)

See [Roblox.AccountInformation.Api.RobloxBadgeResponse](#roblox-accountinformation-api-robloxbadgeresponse) in Models.

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://accountinformation.roblox.com/v1/users/{USERID}/roblox-badges"
```

### GET `/v1/validators/email`

Tries to check if an email is valid

**Server:** `https://auth.roblox.com`

**Auth:** 

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `Email` | query | `string` | Yes |  |

**Responses:**

- `200`: OK → `Roblox.Authentication.Api.Models.EmailValidationResponse`

**Response fields** (`Roblox.Authentication.Api.Models.EmailValidationResponse`)

See [Roblox.Authentication.Api.Models.EmailValidationResponse](#roblox-authentication-api-models-emailvalidationresponse) in Models.

**Response example:**
```json
{
  "isEmailValid": false
}
```

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://auth.roblox.com/v1/validators/email?Email={VALUE}"
```

### GET `/v1/validators/recommendedUsernameFromDisplayName`

Validates the given display name, and if valid, will convert it to a valid username and return suggested username(s) if available.

**Server:** `https://auth.roblox.com`

**Auth:** 

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `DisplayName` | query | `string` | Yes |  |
| `BirthDay` | query | `string` | Yes |  |

**Responses:**

- `200`: OK → `Roblox.Authentication.Api.Models.RecommendedUsernameResponse`

**Response fields** (`Roblox.Authentication.Api.Models.RecommendedUsernameResponse`)

See [Roblox.Authentication.Api.Models.RecommendedUsernameResponse](#roblox-authentication-api-models-recommendedusernameresponse) in Models.

**Response example:**
```json
{
  "didGenerateNewUsername": false,
  "suggestedUsernames": [
    "string"
  ]
}
```

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://auth.roblox.com/v1/validators/recommendedUsernameFromDisplayName?DisplayName={VALUE}&BirthDay={VALUE}"
```

### POST `/v1/validators/recommendedUsernameFromDisplayName`

Validates the given display name, and if valid, will convert it to a valid username and return suggested username(s) if available.
            
This is a POST request and explicitly does not receive the parameter values from the query

**Server:** `https://auth.roblox.com`

**Auth:** 

**Request Body:** `application/json` — Type: `Roblox.Authentication.Api.Models.RecommendedUsernameFromDisplayNameRequest`

See [Roblox.Authentication.Api.Models.RecommendedUsernameFromDisplayNameRequest](#roblox-authentication-api-models-recommendedusernamefromdisplaynamerequest) in Models.

**Request example:**
```json
{
  "displayName": "string",
  "birthday": "2024-01-01T00:00:00Z"
}
```

**Responses:**

- `200`: OK → `Roblox.Authentication.Api.Models.RecommendedUsernameResponse`
- `403`: 0: Token Validation Failed

**Response fields** (`Roblox.Authentication.Api.Models.RecommendedUsernameResponse`)

See [Roblox.Authentication.Api.Models.RecommendedUsernameResponse](#roblox-authentication-api-models-recommendedusernameresponse) in Models.

**Response example:**
```json
{
  "didGenerateNewUsername": false,
  "suggestedUsernames": [
    "string"
  ]
}
```

**Error handling:** `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://auth.roblox.com/v1/validators/recommendedUsernameFromDisplayName" \
  -H "Content-Type: application/json" \
  -d '{
  "displayName": "string",
  "birthday": "2024-01-01T00:00:00Z"
}'
```

### GET `/v1/validators/username`

Tries to get a valid username if the current username is taken

**Server:** `https://auth.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `Username` | query | `string` | Yes |  |
| `BirthDay` | query | `string` | Yes |  |

**Responses:**

- `200`: OK → `Roblox.Authentication.Api.Models.RecommendedUsernameResponse`

**Response fields** (`Roblox.Authentication.Api.Models.RecommendedUsernameResponse`)

See [Roblox.Authentication.Api.Models.RecommendedUsernameResponse](#roblox-authentication-api-models-recommendedusernameresponse) in Models.

**Response example:**
```json
{
  "didGenerateNewUsername": false,
  "suggestedUsernames": [
    "string"
  ]
}
```

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://auth.roblox.com/v1/validators/username?Username={VALUE}&BirthDay={VALUE}"
```

### POST `/v1/validators/username`

Tries to get a valid username if the current username is taken
This is a POST request and explicitly does not receive the parameter values from the query

**Server:** `https://auth.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Request Body:** `application/json` — Type: `Roblox.Authentication.Api.Models.RecommendedUsernameRequest`

See [Roblox.Authentication.Api.Models.RecommendedUsernameRequest](#roblox-authentication-api-models-recommendedusernamerequest) in Models.

**Request example:**
```json
{
  "username": "string",
  "birthday": "2024-01-01T00:00:00Z"
}
```

**Responses:**

- `200`: OK → `Roblox.Authentication.Api.Models.RecommendedUsernameResponse`
- `403`: 0: Token Validation Failed

**Response fields** (`Roblox.Authentication.Api.Models.RecommendedUsernameResponse`)

See [Roblox.Authentication.Api.Models.RecommendedUsernameResponse](#roblox-authentication-api-models-recommendedusernameresponse) in Models.

**Response example:**
```json
{
  "didGenerateNewUsername": false,
  "suggestedUsernames": [
    "string"
  ]
}
```

**Error handling:** `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://auth.roblox.com/v1/validators/username" \
  -H "Content-Type: application/json" \
  -d '{
  "username": "string",
  "birthday": "2024-01-01T00:00:00Z"
}'
```

### GET `/v1/xbox/connection`

Check if the current user has an Xbox connected.
Also returns the gamertag of the Xbox account if connected.

**Server:** `https://auth.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Responses:**

- `200`:  → `Roblox.Authentication.Api.Models.XboxConnectionModel`
- `401`: 0: Authorization has been denied for this request.
- `403`: 

**Response fields** (`Roblox.Authentication.Api.Models.XboxConnectionModel`)

See [Roblox.Authentication.Api.Models.XboxConnectionModel](#roblox-authentication-api-models-xboxconnectionmodel) in Models.

**Response example:**
```json
{
  "hasConnectedXboxAccount": false,
  "gamertag": "string"
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://auth.roblox.com/v1/xbox/connection"
```

### POST `/v1/xbox/disconnect`

Unlink the current ROBLOX account from the Xbox live account.

**Server:** `https://auth.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Responses:**

- `200`: Account is successfully disconnected → `Roblox.Web.WebAPI.Models.ApiSuccessResponse`
- `401`: 0: Authorization has been denied for this request.
- `403`: Forbidden

**Response fields** (`Roblox.Web.WebAPI.Models.ApiSuccessResponse`)

See [Roblox.Web.WebAPI.Models.ApiSuccessResponse](#roblox-web-webapi-models-apisuccessresponse) in Models.

**Response example:**
```json
{
  "success": false
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://auth.roblox.com/v1/xbox/disconnect"
```

### GET `/v1/xbox/get-login-consecutive-days`

Get the consecutive days the xbox user has been logged in.

**Server:** `https://auth.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Responses:**

- `200`:  → `Roblox.Authentication.Api.Models.XboxLoginConsecutiveDaysResponse`
- `400`: 36: Invalid Xbox Live Account
- `401`: 0: Authorization has been denied for this request.
- `403`: 

**Response fields** (`Roblox.Authentication.Api.Models.XboxLoginConsecutiveDaysResponse`)

See [Roblox.Authentication.Api.Models.XboxLoginConsecutiveDaysResponse](#roblox-authentication-api-models-xboxloginconsecutivedaysresponse) in Models.

**Response example:**
```json
{
  "count": 0
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://auth.roblox.com/v1/xbox/get-login-consecutive-days"
```

### POST `/v1/xbox/translate`

Translate the xbox user to roblox user.

**Server:** `https://auth.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Request Body:** `application/json` — Type: `Roblox.Authentication.Api.Models.XboxTranslateRequest`

See [Roblox.Authentication.Api.Models.XboxTranslateRequest](#roblox-authentication-api-models-xboxtranslaterequest) in Models.

**Request example:**
```json
{
  "ids": [
    "string"
  ]
}
```

**Responses:**

- `200`:  → `Roblox.Authentication.Api.Models.XboxCollectionsOfUserResponse`
- `401`: 0: Authorization has been denied for this request.
- `403`: 

**Response fields** (`Roblox.Authentication.Api.Models.XboxCollectionsOfUserResponse`)

See [Roblox.Authentication.Api.Models.XboxCollectionsOfUserResponse](#roblox-authentication-api-models-xboxcollectionsofuserresponse) in Models.

**Response example:**
```json
{
  "Users": [
    {
      "Id": "...",
      "UserId": "...",
      "Username": "..."
    }
  ]
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://auth.roblox.com/v1/xbox/translate" \
  -H "Content-Type: application/json" \
  -d '{
  "ids": [
    "string"
  ]
}'
```

### GET `/v2/auth/metadata`

Gets Auth meta data

**Server:** `https://auth.roblox.com`

**Auth:** 

**Responses:**

- `200`: OK → `Roblox.Authentication.Api.Models.AuthMetaDataResponse`

**Response fields** (`Roblox.Authentication.Api.Models.AuthMetaDataResponse`)

See [Roblox.Authentication.Api.Models.AuthMetaDataResponse](#roblox-authentication-api-models-authmetadataresponse) in Models.

**Response example:**
```json
{
  "cookieLawNoticeTimeout": 0
}
```

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://auth.roblox.com/v2/auth/metadata"
```

### POST `/v2/identity-verification/login`

Endpoint for login with identity verification

**Server:** `https://auth.roblox.com`

**Auth:** 

**Request Body:** `application/json` — Type: `Roblox.Authentication.Api.Models.Request.IdentityVerificationLoginRequest`

See [Roblox.Authentication.Api.Models.Request.IdentityVerificationLoginRequest](#roblox-authentication-api-models-request-identityverificationloginrequest) in Models.

**Request example:**
```json
{
  "loginTicket": "string",
  "resultToken": "string"
}
```

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `403`: 0: Token Validation Failed 1: Invalid login ticket. 2: Invalid result token. 3: Invalid user. 4: Authentication failure. 44: Login is unavailable in your country.

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://auth.roblox.com/v2/identity-verification/login" \
  -H "Content-Type: application/json" \
  -d '{
  "loginTicket": "string",
  "resultToken": "string"
}'
```

### POST `/v2/login`

Authenticates a user.

**Server:** `https://auth.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Request Body:** `application/json` — Type: `Roblox.Authentication.Api.Models.LoginRequest`

See [Roblox.Authentication.Api.Models.LoginRequest](#roblox-authentication-api-models-loginrequest) in Models.

**Request example:**
```json
{
  "ctype": 0,
  "cvalue": "string",
  "password": "string",
  "userId": 0,
  "securityQuestionSessionId": "string",
  "securityQuestionRedemptionToken": "string"
}
```

**Responses:**

- `200`: Successfully logged in. → `Roblox.Authentication.Api.Models.LoginResponse`
- `400`: 0: An unexpected error occurred. 3: Username and Password are required. Please try again. 8: Login with received credential type is not supported.
- `403`: 0: Token Validation Failed 1: Incorrect username or password. Please try again. 2: You must pass the robot test before logging in. 4: Account has been locked. Please request a password reset. 5: Unable to login. Please use Social Network sign on. 6: Account issue. Please contact Support. 9: Unable to login with provided credentials. Default login is required. 10: Received credentials are unverified. 12: Existing login session found. Please log out first. 14: The account is unable to log in. Please log in to the LuoBu app. 15: Too many attempts. Please wait a bit. 27: The account is unable to login. Please log in with the VNG app. 44: Login is unavailable in your country.
- `429`: 7: Too many attempts. Please wait a bit.
- `503`: 11: Service unavailable. Please try again.

**Response fields** (`Roblox.Authentication.Api.Models.LoginResponse`)

See [Roblox.Authentication.Api.Models.LoginResponse](#roblox-authentication-api-models-loginresponse) in Models.

**Response example:**
```json
{
  "user": {
    "id": 0,
    "name": "string",
    "displayName": "string"
  },
  "twoStepVerificationData": {
    "mediaType": 0,
    "ticket": "string"
  },
  "identityVerificationLoginTicket": "string",
  "isBanned": false,
  "accountBlob": "string",
  "shouldUpdateEmail": false
}
```

**Error handling:** `429`: Retry with exponential backoff (start at 1s). `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://auth.roblox.com/v2/login" \
  -H "Content-Type: application/json" \
  -d '{
  "ctype": 0,
  "cvalue": "string",
  "password": "string",
  "userId": 0,
  "securityQuestionSessionId": "string",
  "securityQuestionRedemptionToken": "string"
}'
```

### POST `/v2/login/linked`

Endpoint for logging in a user, specifically for linked
authentication on PCGDK

**Server:** `https://auth.roblox.com`

**Auth:** 

**Request Body:** `application/json` — Type: `Roblox.Authentication.Api.Models.LoginRequest`

See [Roblox.Authentication.Api.Models.LoginRequest](#roblox-authentication-api-models-loginrequest) in Models.

**Request example:**
```json
{
  "ctype": 0,
  "cvalue": "string",
  "password": "string",
  "userId": 0,
  "securityQuestionSessionId": "string",
  "securityQuestionRedemptionToken": "string"
}
```

**Responses:**

- `200`: Successful login → `Roblox.Authentication.Api.Models.LoginResponse`
- `400`: 0: An unexpected error occurred. 3: Username and Password are required. Please try again. 8: Login with received credential type is not supported.
- `403`: 0: Token Validation Failed 1: Incorrect username or password. Please try again. 2: You must pass the robot test before logging in. 4: Account has been locked. Please request a password reset. 5: Unable to login. Please use Social Network sign on. 6: Account issue. Please contact Support. 9: Unable to login with provided credentials. Default login is required. 10: Received credentials are unverified. 12: Existing login session found. Please log out first. 14: The account is unable to log in. Please log in to the LuoBu app. 15: Too many attempts. Please wait a bit. 27: The account is unable to login. Please log in with the VNG app. 43: This account is not eligible for this platform. 44: Login is unavailable in your country.
- `429`: 7: Too many attempts. Please wait a bit.
- `503`: 11: Service unavailable. Please try again.

**Response fields** (`Roblox.Authentication.Api.Models.LoginResponse`)

See [Roblox.Authentication.Api.Models.LoginResponse](#roblox-authentication-api-models-loginresponse) in Models.

**Response example:**
```json
{
  "user": {
    "id": 0,
    "name": "string",
    "displayName": "string"
  },
  "twoStepVerificationData": {
    "mediaType": 0,
    "ticket": "string"
  },
  "identityVerificationLoginTicket": "string",
  "isBanned": false,
  "accountBlob": "string",
  "shouldUpdateEmail": false
}
```

**Error handling:** `429`: Retry with exponential backoff (start at 1s). `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://auth.roblox.com/v2/login/linked" \
  -H "Content-Type: application/json" \
  -d '{
  "ctype": 0,
  "cvalue": "string",
  "password": "string",
  "userId": 0,
  "securityQuestionSessionId": "string",
  "securityQuestionRedemptionToken": "string"
}'
```

### POST `/v2/logout`

Destroys the current authentication session.

**Server:** `https://auth.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://auth.roblox.com/v2/logout"
```

### POST `/v2/logoutfromallsessionsandreauthenticate`

Logs out user from all other sessions.

**Server:** `https://auth.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Request Body:** `application/json` — Type: `Roblox.Authentication.Api.Models.Request.LogoutFromAllSessionsAndReauthenticateRequest`

See [Roblox.Authentication.Api.Models.Request.LogoutFromAllSessionsAndReauthenticateRequest](#roblox-authentication-api-models-request-logoutfromallsessionsandreauthenticaterequest) in Models.

**Request example:**
```json
{
  "SecureAuthenticationIntent": {
    "clientPublicKey": "string",
    "clientEpochTimestamp": 0,
    "saiSignature": "string",
    "serverNonce": "string"
  }
}
```

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://auth.roblox.com/v2/logoutfromallsessionsandreauthenticate" \
  -H "Content-Type: application/json" \
  -d '{
  "SecureAuthenticationIntent": {
    "clientPublicKey": "string",
    "clientEpochTimestamp": 0,
    "saiSignature": "string",
    "serverNonce": "string"
  }
}'
```

### GET `/v2/metadata`

Get the metadata

**Server:** `https://auth.roblox.com`

**Auth:** 

**Responses:**

- `200`: OK → `Roblox.Authentication.Api.Models.MetadataResponse`

**Response fields** (`Roblox.Authentication.Api.Models.MetadataResponse`)

See [Roblox.Authentication.Api.Models.MetadataResponse](#roblox-authentication-api-models-metadataresponse) in Models.

**Response example:**
```json
{
  "isUpdateUsernameEnabled": false,
  "ftuxAvatarAssetMap": "string",
  "IsEmailUpsellAtLogoutEnabled": false,
  "ShouldFetchEmailUpsellIXPValuesAtLogout": false,
  "IsAccountRecoveryPromptEnabled": false,
  "IsContactMethodRequiredAtSignup": false
}
```

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://auth.roblox.com/v2/metadata"
```

### GET `/v2/passwords/current-status`

Returns password status for current user, asynchronously.

**Server:** `https://auth.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Responses:**

- `200`: OK → `Roblox.Authentication.Api.Models.PasswordStatusResponse`
- `401`: 0: Authorization has been denied for this request.

**Response fields** (`Roblox.Authentication.Api.Models.PasswordStatusResponse`)

See [Roblox.Authentication.Api.Models.PasswordStatusResponse](#roblox-authentication-api-models-passwordstatusresponse) in Models.

**Response example:**
```json
{
  "valid": false
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://auth.roblox.com/v2/passwords/current-status"
```

### GET `/v2/passwords/reset`

Gets metadata needed for the password reset view.

**Server:** `https://auth.roblox.com`

**Auth:** 

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `TargetType` | query | `0 \| 1 \| 2` | Yes | Valid values: `0`, `1`, `2` |
| `Ticket` | query | `string` | Yes |  |

**Responses:**

- `200`: OK → `Roblox.Authentication.Api.Models.PasswordResetMetadataResponse`
- `400`: 3: Request was empty. 9: The target type is invalid. 11: The password reset ticket is invalid. 14: The nonce is invalid.
- `403`: 11: The password reset ticket is invalid. 16: The ticket is expired.
- `500`: 0: Unknown error occured.
- `503`: 1: Feature temporarily disabled. Please try again later.

**Response fields** (`Roblox.Authentication.Api.Models.PasswordResetMetadataResponse`)

See [Roblox.Authentication.Api.Models.PasswordResetMetadataResponse](#roblox-authentication-api-models-passwordresetmetadataresponse) in Models.

**Response example:**
```json
{
  "users": [
    {
      "userId": "...",
      "username": "...",
      "displayName": "..."
    }
  ]
}
```

**Error handling:** `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://auth.roblox.com/v2/passwords/reset?TargetType={VALUE}&Ticket={VALUE}"
```

### POST `/v2/passwords/reset`

Resets a password for a user that belongs to the password reset ticket.

This will log the user out of all sessions and re-authenticate.

**Server:** `https://auth.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Request Body:** `application/json` — Type: `Roblox.Authentication.Api.Models.PasswordResetModel`

See [Roblox.Authentication.Api.Models.PasswordResetModel](#roblox-authentication-api-models-passwordresetmodel) in Models.

**Request example:**
```json
{
  "targetType": 0,
  "ticket": "string",
  "userId": 0,
  "password": "string",
  "passwordRepeated": "string",
  "twoStepVerificationChallengeId": "string"
}
```

**Responses:**

- `200`: The password was successfully reset. → `Roblox.Authentication.Api.Models.LoginResponse`
- `400`: 3: Request was empty. 11: The password reset ticket is invalid. 12: The user is invalid. 20: The password is invalid. 21: Passwords do not match. 27: The password is not complex enough. 28: The password is too similar to the username.
- `403`: 0: Token Validation Failed 16: The ticket is expired. 17: The nonce is expired. 44: Login is unavailable in your country.
- `500`: 0: Unknown error occured.
- `503`: 1: Feature temporarily disabled. Please try again later.

**Response fields** (`Roblox.Authentication.Api.Models.LoginResponse`)

See [Roblox.Authentication.Api.Models.LoginResponse](#roblox-authentication-api-models-loginresponse) in Models.

**Response example:**
```json
{
  "user": {
    "id": 0,
    "name": "string",
    "displayName": "string"
  },
  "twoStepVerificationData": {
    "mediaType": 0,
    "ticket": "string"
  },
  "identityVerificationLoginTicket": "string",
  "isBanned": false,
  "accountBlob": "string",
  "shouldUpdateEmail": false
}
```

**Error handling:** `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://auth.roblox.com/v2/passwords/reset" \
  -H "Content-Type: application/json" \
  -d '{
  "targetType": 0,
  "ticket": "string",
  "userId": 0,
  "password": "string",
  "passwordRepeated": "string",
  "twoStepVerificationChallengeId": "string"
}'
```

### POST `/v2/passwords/reset/send`

Sends a password reset email or challenge to the specified target.

Phone target must be a csv with 3 values: "internationalPrefixNumber,nationalNumber,countryCode"

**Server:** `https://auth.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Request Body:** `application/json` — Type: `Roblox.Authentication.Api.Models.SendResetPasswordRequest`

See [Roblox.Authentication.Api.Models.SendResetPasswordRequest](#roblox-authentication-api-models-sendresetpasswordrequest) in Models.

**Request example:**
```json
{
  "targetType": 0,
  "target": "string",
  "captchaId": "string",
  "captchaToken": "string",
  "captchaProvider": "string",
  "challengeId": "string"
}
```

**Responses:**

- `200`: The forgot password email successfully sent. → `Roblox.Authentication.Api.Models.SendResetPasswordResponse`
- `400`: 3: Request was empty. 9: The target type is invalid. 10: The target is invalid. 12: The user is invalid.
- `403`: 0: Token Validation Failed 18: Captcha is required. 23: Authenticate with Luobu instead.
- `429`: 2: Too many attempts. Please try again later.
- `500`: 0: Unknown error occured. 19: Message could not be sent.
- `503`: 1: Feature temporarily disabled. Please try again later.

**Response fields** (`Roblox.Authentication.Api.Models.SendResetPasswordResponse`)

See [Roblox.Authentication.Api.Models.SendResetPasswordResponse](#roblox-authentication-api-models-sendresetpasswordresponse) in Models.

**Response example:**
```json
{
  "nonce": "string",
  "transmissionType": 0
}
```

**Error handling:** `429`: Retry with exponential backoff (start at 1s). `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://auth.roblox.com/v2/passwords/reset/send" \
  -H "Content-Type: application/json" \
  -d '{
  "targetType": 0,
  "target": "string",
  "captchaId": "string",
  "captchaToken": "string",
  "captchaProvider": "string",
  "challengeId": "string"
}'
```

### POST `/v2/passwords/reset/verify`

Verifies a password reset challenge solution.

**Server:** `https://auth.roblox.com`

**Auth:** 

**Request Body:** `application/json` — Type: `Roblox.Authentication.Api.Models.PasswordResetVerificationRequest`

See [Roblox.Authentication.Api.Models.PasswordResetVerificationRequest](#roblox-authentication-api-models-passwordresetverificationrequest) in Models.

**Request example:**
```json
{
  "targetType": 0,
  "nonce": "string",
  "code": "string"
}
```

**Responses:**

- `200`: Verification succeeded. → `Roblox.Authentication.Api.Models.PasswordResetVerificationResponse`
- `400`: 3: Request was empty. 9: The target type is invalid. 14: The nonce is invalid.
- `403`: 0: Token Validation Failed 13: The code is invalid.
- `500`: 0: Unknown error occured.
- `503`: 1: Feature temporarily disabled. Please try again later.

**Response fields** (`Roblox.Authentication.Api.Models.PasswordResetVerificationResponse`)

See [Roblox.Authentication.Api.Models.PasswordResetVerificationResponse](#roblox-authentication-api-models-passwordresetverificationresponse) in Models.

**Response example:**
```json
{
  "userTickets": [
    {
      "user": "...",
      "ticket": "..."
    }
  ]
}
```

**Error handling:** `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://auth.roblox.com/v2/passwords/reset/verify" \
  -H "Content-Type: application/json" \
  -d '{
  "targetType": 0,
  "nonce": "string",
  "code": "string"
}'
```

### GET `/v2/passwords/validate`

Endpoint for checking if a password is valid.

**Server:** `https://auth.roblox.com`

**Auth:** 

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `Username` | query | `string` | Yes |  |
| `Password` | query | `string` | Yes |  |

**Responses:**

- `200`: Success → `Roblox.Authentication.Api.Models.PasswordValidationResponse`
- `400`: 1: Valid Username and Password are required. Please try again.

**Response fields** (`Roblox.Authentication.Api.Models.PasswordValidationResponse`)

See [Roblox.Authentication.Api.Models.PasswordValidationResponse](#roblox-authentication-api-models-passwordvalidationresponse) in Models.

**Response example:**
```json
{
  "code": 0,
  "message": "string"
}
```

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://auth.roblox.com/v2/passwords/validate?Username={VALUE}&Password={VALUE}"
```

### POST `/v2/passwords/validate`

Endpoint for checking if a password is valid.

**Server:** `https://auth.roblox.com`

**Auth:** 

**Request Body:** `application/json` — Type: `Roblox.Authentication.Api.Models.PasswordValidationModel`

See [Roblox.Authentication.Api.Models.PasswordValidationModel](#roblox-authentication-api-models-passwordvalidationmodel) in Models.

**Request example:**
```json
{
  "username": "string",
  "password": "string"
}
```

**Responses:**

- `200`: Success → `Roblox.Authentication.Api.Models.PasswordValidationResponse`
- `400`: 1: Valid Username and Password are required. Please try again.
- `403`: 0: Token Validation Failed

**Response fields** (`Roblox.Authentication.Api.Models.PasswordValidationResponse`)

See [Roblox.Authentication.Api.Models.PasswordValidationResponse](#roblox-authentication-api-models-passwordvalidationresponse) in Models.

**Response example:**
```json
{
  "code": 0,
  "message": "string"
}
```

**Error handling:** `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://auth.roblox.com/v2/passwords/validate" \
  -H "Content-Type: application/json" \
  -d '{
  "username": "string",
  "password": "string"
}'
```

### GET `/v2/push-notifications/get-destinations` [EXPERIMENTAL]

Gets valid destinations associated with the signed user

**Server:** `https://notifications.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Responses:**

- `200`: OK → `Roblox.Api.Notifications.Models.GetPushDestinationsResponseModel`
- `401`: 0: Authorization has been denied for this request.

**Response fields** (`Roblox.Api.Notifications.Models.GetPushDestinationsResponseModel`)

See [Roblox.Api.Notifications.Models.GetPushDestinationsResponseModel](#roblox-api-notifications-models-getpushdestinationsresponsemodel) in Models.

**Response example:**
```json
{
  "destinations": [
    {
      "user": "...",
      "name": "...",
      "notificationToken": "...",
      "supportsUpdateNotifications": "...",
      "userPushNotificationDestinationId": "...",
      "application": "..."
    }
  ],
  "statusMessage": "string"
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://notifications.roblox.com/v2/push-notifications/get-destinations"
```

### GET `/v2/recovery/metadata`

Get metadata for forgot endpoints

**Server:** `https://auth.roblox.com`

**Auth:** 

**Responses:**

- `200`: OK → `Roblox.Authentication.Api.Models.RecoveryMetadataResponse`
- `503`: 7: The Roblox WeChat API is currently unavailable.

**Response fields** (`Roblox.Authentication.Api.Models.RecoveryMetadataResponse`)

See [Roblox.Authentication.Api.Models.RecoveryMetadataResponse](#roblox-authentication-api-models-recoverymetadataresponse) in Models.

**Response example:**
```json
{
  "isOnPhone": false,
  "codeLength": 0,
  "isPhoneFeatureEnabledForUsername": false,
  "isPhoneFeatureEnabledForPassword": false,
  "isBedev2CaptchaEnabledForPasswordReset": false,
  "isUsernameRecoveryDeprecated": false
}
```

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://auth.roblox.com/v2/recovery/metadata"
```

### GET `/v2/revert/account`

Get Revert Account ticket info

**Server:** `https://auth.roblox.com`

**Auth:** 

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `ticket` | query | `string` | Yes | Ticket Guid to revert account. |

**Responses:**

- `200`: OK → `Roblox.Authentication.Api.Models.RevertAccountInfoResponse`
- `400`: 2: The account revert ticket is not valid
- `403`: 13: Revert links are disabled for users in the Enhanced Protection Program.
- `503`: 1: This feature is disabled

**Response fields** (`Roblox.Authentication.Api.Models.RevertAccountInfoResponse`)

See [Roblox.Authentication.Api.Models.RevertAccountInfoResponse](#roblox-authentication-api-models-revertaccountinforesponse) in Models.

**Response example:**
```json
{
  "isTwoStepVerificationEnabled": false,
  "isEmailVerified": false,
  "isEmailChanged": false,
  "isPhoneVerified": false,
  "userId": 0,
  "username": "string"
}
```

**Error handling:** `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://auth.roblox.com/v2/revert/account?ticket={VALUE}"
```

### POST `/v2/revert/account`

Submit Revert Account Request

**Server:** `https://auth.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Request Body:** `application/json` — Type: `Roblox.Authentication.Api.Models.RevertAccountSubmitRequest`

See [Roblox.Authentication.Api.Models.RevertAccountSubmitRequest](#roblox-authentication-api-models-revertaccountsubmitrequest) in Models.

**Request example:**
```json
{
  "UserId": 0,
  "NewPassword": "string",
  "NewPasswordRepeated": "string",
  "Ticket": "string",
  "TwoStepVerificationChallengeId": "string",
  "TwoStepVerificationToken": "string"
}
```

**Responses:**

- `200`: OK → `Roblox.Authentication.Api.Models.LoginResponse`
- `400`: 2: The account revert ticket is not valid 3: Password is not valid 4: Passwords do not match 5: Password cannot be used 8: The account security ticket is expired. 14: Password is not complex enough 15: Password is too similar to username
- `403`: 0: Token Validation Failed
- `503`: 0: Unknown 1: This feature is disabled

**Response fields** (`Roblox.Authentication.Api.Models.LoginResponse`)

See [Roblox.Authentication.Api.Models.LoginResponse](#roblox-authentication-api-models-loginresponse) in Models.

**Response example:**
```json
{
  "user": {
    "id": 0,
    "name": "string",
    "displayName": "string"
  },
  "twoStepVerificationData": {
    "mediaType": 0,
    "ticket": "string"
  },
  "identityVerificationLoginTicket": "string",
  "isBanned": false,
  "accountBlob": "string",
  "shouldUpdateEmail": false
}
```

**Error handling:** `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://auth.roblox.com/v2/revert/account" \
  -H "Content-Type: application/json" \
  -d '{
  "UserId": 0,
  "NewPassword": "string",
  "NewPasswordRepeated": "string",
  "Ticket": "string",
  "TwoStepVerificationChallengeId": "string",
  "TwoStepVerificationToken": "string"
}'
```

### POST `/v2/revert/invalidate-tickets`

Invalidates all account security tickets for the authenticated user.
This endpoint should be called before enrolling in EPP to ensure old revert links cannot be used.

**Server:** `https://auth.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Responses:**

- `200`: Successfully invalidated all tickets. → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed
- `503`: 1: This feature is disabled

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://auth.roblox.com/v2/revert/invalidate-tickets"
```

### POST `/v2/session/refresh`

Logs out user from the current session and create a new one.

**Server:** `https://auth.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://auth.roblox.com/v2/session/refresh"
```

### POST `/v2/signup`

Endpoint for signing up a new user

**Server:** `https://auth.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Responses:**

- `200`: Successful signup → `Roblox.Authentication.Api.Models.SignupResponse`
- `400`: Bad request
- `403`: 0: Token Validation Failed 2: Captcha Failed. 4: Invalid Birthday. 5: Invalid Username. 6: Username already taken. 7: Invalid Password. 8: Password and Username are same. 9: Password is too simple. 10: Email is invalid. 11: Asset is invalid. 12: Too many attempts. Please wait a bit. 17: One time Passcode session was not valid 22: Maximum logged in accounts limit reached. 36: Password is not complex enough. 37: Password is too similar to username. 44: Login is unavailable in your country.
- `429`: 3: Too many attempts. Please wait a bit.
- `500`: Internal server error
- `503`: Service unavailable

**Response fields** (`Roblox.Authentication.Api.Models.SignupResponse`)

See [Roblox.Authentication.Api.Models.SignupResponse](#roblox-authentication-api-models-signupresponse) in Models.

**Response example:**
```json
{
  "userId": 0,
  "starterPlaceId": 0,
  "returnUrl": "string",
  "accountBlob": "string"
}
```

**Error handling:** `429`: Retry with exponential backoff (start at 1s). `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://auth.roblox.com/v2/signup" \
  -H "Content-Type: application/json" \
  -d '{"key": "value"}'
```

### POST `/v2/signup/linked`

Endpoint for signing up a new user through linked authentication.

**Server:** `https://auth.roblox.com`

**Auth:** 

**Responses:**

- `200`: Successful signup → `Roblox.Authentication.Api.Models.SignupResponse`
- `400`: Bad request
- `403`: 0: Token Validation Failed 2: Captcha Failed. 4: Invalid Birthday. 5: Invalid Username. 6: Username already taken. 7: Invalid Password. 8: Password and Username are same. 9: Password is too simple. 10: Email is invalid. 11: Asset is invalid. 12: Too many attempts. Please wait a bit. 17: One time Passcode session was not valid 22: Maximum logged in accounts limit reached. 29: Account Linking already exists on this account 30: Account Linking required but failed 36: Password is not complex enough. 37: Password is too similar to username. 44: Login is unavailable in your country.
- `429`: 3: Too many attempts. Please wait a bit.
- `500`: Internal server error
- `503`: 30: Account Linking required but failed

**Response fields** (`Roblox.Authentication.Api.Models.SignupResponse`)

See [Roblox.Authentication.Api.Models.SignupResponse](#roblox-authentication-api-models-signupresponse) in Models.

**Response example:**
```json
{
  "userId": 0,
  "starterPlaceId": 0,
  "returnUrl": "string",
  "accountBlob": "string"
}
```

**Error handling:** `429`: Retry with exponential backoff (start at 1s). `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://auth.roblox.com/v2/signup/linked" \
  -H "Content-Type: application/json" \
  -d '{"key": "value"}'
```

### POST `/v2/user/passwords/change`

Changes the password for the authenticated user.

The current password is needed for verification that the password can be changed.

**Server:** `https://auth.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Request Body:** `application/json` — Type: `Roblox.Authentication.Api.Models.PasswordChangeModel`

See [Roblox.Authentication.Api.Models.PasswordChangeModel](#roblox-authentication-api-models-passwordchangemodel) in Models.

**Request example:**
```json
{
  "currentPassword": "string",
  "newPassword": "string",
  "secureAuthenticationIntent": {
    "clientPublicKey": "string",
    "clientEpochTimestamp": 0,
    "saiSignature": "string",
    "serverNonce": "string"
  }
}
```

**Responses:**

- `200`: Password successfully changed. → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: Roblox.Web.Authentication.Passwords.PasswordResponseCodes.InvalidCurrentPassword             OR             Roblox.Web.Authentication.Passwords.PasswordResponseCodes.InvalidPassword             OR             Roblox.Web.Authentication.Passwords.PasswordResponseCodes.PasswordLowComplexity             OR             Roblox.Web.Authentication.Passwords.PasswordResponseCodes.PasswordTooSimilarToUsername
- `401`: 0: Authorization has been denied for this request.
- `403`: Roblox.Web.Authentication.Passwords.PasswordResponseCodes.PinLocked
- `429`: Roblox.Web.Authentication.Passwords.PasswordResponseCodes.Flooded

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `429`: Retry with exponential backoff (start at 1s). `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://auth.roblox.com/v2/user/passwords/change" \
  -H "Content-Type: application/json" \
  -d '{
  "currentPassword": "string",
  "newPassword": "string",
  "secureAuthenticationIntent": {
    "clientPublicKey": "string",
    "clientEpochTimestamp": 0,
    "saiSignature": "string",
    "serverNonce": "string"
  }
}'
```

### POST `/v2/username`

Change the user's username

**Server:** `https://auth.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Request Body:** `application/json` — Type: `Roblox.Authentication.Api.Models.UsernameChangeRequest`

See [Roblox.Authentication.Api.Models.UsernameChangeRequest](#roblox-authentication-api-models-usernamechangerequest) in Models.

**Request example:**
```json
{
  "username": "string",
  "password": "string"
}
```

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: 5: You don't have enough Robux to change your username. 10: This username is already in use 11: Username not appropriate for Roblox 12: Usernames can be 3 to 20 characters long 13: Usernames can’t start or end with _ and can have at most one _ 14: Only a-z, A-Z, 0-9, and _ are allowed 15: Username is null 16: Username might contain private information 17: This username is not available 18: Username is same as current
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 1: PIN is locked. 2: A verified email is missing 3: Your password is incorrect. 100: Unknown birthday
- `500`: 0: An unknown error occured. 5: You don't have enough Robux to change your username.
- `503`: 4: The feature is currently not available. Please try again later.

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://auth.roblox.com/v2/username" \
  -H "Content-Type: application/json" \
  -d '{
  "username": "string",
  "password": "string"
}'
```

### GET `/v2/username/change/price`

Get the current price for a username change

**Server:** `https://auth.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Responses:**

- `200`: OK → `Roblox.Authentication.Api.Models.UsernameChangePriceResponse`
- `401`: 0: Authorization has been denied for this request.

**Response fields** (`Roblox.Authentication.Api.Models.UsernameChangePriceResponse`)

See [Roblox.Authentication.Api.Models.UsernameChangePriceResponse](#roblox-authentication-api-models-usernamechangepriceresponse) in Models.

**Response example:**
```json
{
  "priceInRobux": 0,
  "basePriceInRobux": 0,
  "isFreeUsernameChange": false
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://auth.roblox.com/v2/username/change/price"
```

### GET `/v2/usernames`

Gets a list of existing usernames on Roblox based on the query parameters

This endpoint can be expanded in the future to include other query parameters such as "startsWith"

**Server:** `https://auth.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `username` | query | `string` | Yes | The username |

**Responses:**

- `200`: OK → `Roblox.Authentication.Api.Models.UsernamesResponse`

**Response fields** (`Roblox.Authentication.Api.Models.UsernamesResponse`)

See [Roblox.Authentication.Api.Models.UsernamesResponse](#roblox-authentication-api-models-usernamesresponse) in Models.

**Response example:**
```json
{
  "usernames": [
    "string"
  ]
}
```

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://auth.roblox.com/v2/usernames?username={VALUE}"
```

### POST `/v2/usernames/recover`

Sends an email of all accounts belonging to an email

**Server:** `https://auth.roblox.com`

**Auth:** 

**Request Body:** `application/json` — Type: `Roblox.Authentication.Api.Models.RecoverUsernameRequest`

See [Roblox.Authentication.Api.Models.RecoverUsernameRequest](#roblox-authentication-api-models-recoverusernamerequest) in Models.

**Request example:**
```json
{
  "targetType": 0,
  "target": "string"
}
```

**Responses:**

- `200`: OK → `Roblox.Authentication.Api.Models.RecoverUsernameResponse`
- `400`: 20: Invalid Email 21: Invalid Phone 23: No Account Found
- `403`: 0: Token Validation Failed 11: Too many attempts. Please wait a bit.
- `500`: 0: An unexpected error occurred.

**Response fields** (`Roblox.Authentication.Api.Models.RecoverUsernameResponse`)

See [Roblox.Authentication.Api.Models.RecoverUsernameResponse](#roblox-authentication-api-models-recoverusernameresponse) in Models.

**Response example:**
```json
{
  "transmissionType": 0
}
```

**Error handling:** `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://auth.roblox.com/v2/usernames/recover" \
  -H "Content-Type: application/json" \
  -d '{
  "targetType": 0,
  "target": "string"
}'
```

### GET `/v2/usernames/validate`

Checks if a username is valid.

**Server:** `https://auth.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `Username` | query | `string` | Yes |  |
| `Birthday` | query | `string` | Yes |  |
| `Context` | query | `0 \| 1 \| 2` | Yes | Valid values: `0`, `1`, `2` |

**Responses:**

- `200`: Success → `Roblox.Authentication.Api.Models.UsernameValidationResponse`
- `400`: 1: A valid username is required. 2: A valid birthday or authenticated user is required.

**Response fields** (`Roblox.Authentication.Api.Models.UsernameValidationResponse`)

See [Roblox.Authentication.Api.Models.UsernameValidationResponse](#roblox-authentication-api-models-usernamevalidationresponse) in Models.

**Response example:**
```json
{
  "code": 0,
  "message": "string"
}
```

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://auth.roblox.com/v2/usernames/validate?Username={VALUE}&Birthday={VALUE}&Context={VALUE}"
```

### POST `/v2/usernames/validate`

Checks if a username is valid.

**Server:** `https://auth.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Request Body:** `application/json` — Type: `Roblox.Authentication.Api.Models.UsernameValidationRequest`

See [Roblox.Authentication.Api.Models.UsernameValidationRequest](#roblox-authentication-api-models-usernamevalidationrequest) in Models.

**Request example:**
```json
{
  "username": "string",
  "birthday": "2024-01-01T00:00:00Z",
  "context": 0
}
```

**Responses:**

- `200`: Success → `Roblox.Authentication.Api.Models.UsernameValidationResponse`
- `400`: 1: A valid username is required. 2: A valid birthday or authenticated user is required.
- `403`: 0: Token Validation Failed

**Response fields** (`Roblox.Authentication.Api.Models.UsernameValidationResponse`)

See [Roblox.Authentication.Api.Models.UsernameValidationResponse](#roblox-authentication-api-models-usernamevalidationresponse) in Models.

**Response example:**
```json
{
  "code": 0,
  "message": "string"
}
```

**Error handling:** `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://auth.roblox.com/v2/usernames/validate" \
  -H "Content-Type: application/json" \
  -d '{
  "username": "string",
  "birthday": "2024-01-01T00:00:00Z",
  "context": 0
}'
```

### POST `/v3/logout`

Destroys the current authentication session while reporting metrics like url and reason for logout.

**Server:** `https://auth.roblox.com`

**Auth:** 

**Request Body:** `application/json` — Type: `Roblox.Authentication.Api.Models.Request.LogoutV3Request`

See [Roblox.Authentication.Api.Models.Request.LogoutV3Request](#roblox-authentication-api-models-request-logoutv3request) in Models.

**Request example:**
```json
{
  "logoutReason": "string",
  "url": "string",
  "userId": "string"
}
```

**Responses:**

- `200`: Successfully logged out. → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `403`: 0: Token Validation Failed

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://auth.roblox.com/v3/logout" \
  -H "Content-Type: application/json" \
  -d '{
  "logoutReason": "string",
  "url": "string",
  "userId": "string"
}'
```

### POST `/v3/users/{userId}/two-step-verification/login`

Authenticates as a user given a two step verification verification token.

**Server:** `https://auth.roblox.com`

**Auth:** 

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer` | Yes | The user ID to authenticate as. |

**Request Body:** `application/json` — Type: `Roblox.Authentication.Api.TwoStepVerificationLoginRequest`

See [Roblox.Authentication.Api.TwoStepVerificationLoginRequest](#roblox-authentication-api-twostepverificationloginrequest) in Models.

**Request example:**
```json
{
  "challengeId": "string",
  "verificationToken": "string",
  "rememberDevice": false,
  "secureAuthenticationIntent": {
    "clientPublicKey": "string",
    "clientEpochTimestamp": 0,
    "saiSignature": "string",
    "serverNonce": "string"
  },
  "accountBlob": "string",
  "accountLinkParameters": {
    "LinkingPlatform": 0
  }
}
```

**Responses:**

- `200`: OK → `Roblox.Authentication.Api.Models.TwoStepVerificationV3LoginResponse`
- `400`: 1: User is invalid. 5: Invalid two step verification ticket. 10: Invalid verification token.
- `403`: 0: Token Validation Failed 11: Maxium logged in accounts limit reached. 44: Login is unavailable in your country.

**Response fields** (`Roblox.Authentication.Api.Models.TwoStepVerificationV3LoginResponse`)

See [Roblox.Authentication.Api.Models.TwoStepVerificationV3LoginResponse](#roblox-authentication-api-models-twostepverificationv3loginresponse) in Models.

**Response example:**
```json
{
  "identityVerificationLoginTicket": "string",
  "accountBlob": "string"
}
```

**Error handling:** `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://auth.roblox.com/v3/users/{USERID}/two-step-verification/login" \
  -H "Content-Type: application/json" \
  -d '{"challengeId":"string","verificationToken":"string","rememberDevice":false,"secureAuthenticationIntent":{"clientPublicKey":"string","clientEpochTimestamp":0,"saiSignature":"string","serverNonce":"string"},"accountBlob":"string","accountLinkParameters":{"LinkingPlatform":0}}'
```

## Models

### GetAccountResponse

Response structure for GetAccount endpoints.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `account` | `any` | Yes | Gets or sets the account settings. |

### UpdateAccountResponse

Response structure for UpdateAccount endpoints.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `account` | `any` | Yes | Gets or sets the account settings. |

### BillingActivitiesResponse

Response object for Billing Activities request.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `accountState` | `any` | No | Gets or sets the account state. |
| `billSummaries` | `BillSummary[]` | No | Gets or sets the list of account bill summaries. |
| `currentBalance` | `any` | Yes | Gets or sets the current account balance. |
| `monthToDateBalance` | `any` | Yes | Gets or sets the month to date balance |
| `chargingThreshold` | `any` | Yes | Gets or sets the charging threshold. |

### BillDetailsResponse

Response object for a billing statement.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `accountState` | `any` | No | Gets or sets the account state. |
| `billId` | `string` | No | Gets or sets the ID of the bill. |
| `billStatus` | `any` | Yes | Gets or sets the status of the bill. |
| `usageAmount` | `any` | Yes | Gets or sets the pre-tax bill amount. |
| `taxAmount` | `any` | Yes | Gets or sets the tax amount of the bill. |
| `totalAmount` | `any` | Yes | Gets or sets the total, tax-inclusive amount of the bill. This is Roblox.CloudPricing.ServiceEfficiencyApi.Models.BillDetailsResponse.UsageAmount + Roblox.CloudPricing.ServiceEfficiencyApi.Models.BillDetailsResponse.TaxAmount. |
| `usages` | `ConsumerUsage[]` | Yes | Gets or sets the list of consumer usages. |
| `billingAddress` | `any` | Yes | Gets or sets the billing address of this bill. |
| `robloxAddress` | `any` | Yes | Gets or sets the Roblox Company address associated with this bill. |
| `taxId` | `string` | No | Gets or sets the tax id used for this bill. |
| `taxIdType` | `any` | No | Gets or sets the type of the tax id used for this bill. |
| `payments` | `Payment[]` | Yes | Gets or sets the payments associated with this bill. |
| `conversionRate` | `number` | No | Gets or sets the USD-to-local-currency conversion rate at bill creation time, provided for reference only. Null if the payment method is in the US, the bill predates this feature, or for pending bills. -1 if the currency converter lookup failed. |

### CheckEligibilityResponse

Response object for Roblox.CloudPricing.ServiceEfficiencyApi.Operations.CheckEligibilityOperation

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `eligibilityRequirementResults` | `EligibilityRequirementResult[]` | No | Gets or sets the eligibility requirement results for the provided creator. |

### GetServiceEfficiencyPaymentMethodResponse

Response object for Roblox.CloudPricing.ServiceEfficiencyApi.Operations.GetServiceEfficiencyPaymentMethodOperation

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `paymentProfile` | `any` | No | Gets or sets the payment profile set for Service Efficiency use for the provided creator. |

### ListPaymentProfilesResponse

Response object for Roblox.CloudPricing.ServiceEfficiencyApi.Operations.ListPaymentProfilesOperation.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `paymentProfiles` | `PaymentProfile[]` | No | Gets or sets the payment profiles owned by the provided creator. |

### CreatePaymentProfileResponse

Response object for Roblox.CloudPricing.ServiceEfficiencyApi.Operations.CreatePaymentProfileOperation

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `clientSecret` | `string` | No | Gets or sets the client secret to complete payment profile creation. |

### Roblox.Authentication.Api.Models.AuthMethodsMetadataResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `isEligibleForALSignup` | `boolean` | No |  |

### Roblox.Authentication.Api.Models.AccountPinStatusResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `isEnabled` | `boolean` | No |  |
| `unlockedUntil` | `number` | No |  |

### Roblox.Authentication.Api.Models.AccountPinRequest

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `pin` | `string` | No |  |
| `reauthenticationToken` | `string` | No |  |

### Roblox.Web.WebAPI.Models.ApiSuccessResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | `boolean` | No |  |

### Roblox.Authentication.Api.Models.AccountPinResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `unlockedUntil` | `number` | No |  |

### Roblox.AccountSettings.Api.Models.Response.AccountCountrySettingsResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `value` | `Roblox.AccountSettings.Api.Models.Response.UserAccountCountry` | No |  |

### Roblox.AccountSettings.Api.UpdateAccountCountryRequest

Request Model for updating a user's account country

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `targetCountryId` | `integer` | No | The targetCountryId |

### Roblox.AccountSettings.Api.Models.AccountsSettingsMetadataModel

A model containing website metadata for avatars

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `IsAccountsRestrictionsSpamBugFixEnabled` | `boolean` | No | Whether or not account restrictions spam bug fix is enabled |
| `MaximumParentalControlsMonthlySpendLimitInUSD` | `integer` | No | The max amount a user can enter as their monthly spending limit in USD |
| `IsParentalMonthlyLimitInUIEnabled` | `boolean` | No | Enables/disables the section in the account parental controls page where you can set the monthly spend limit |
| `IsParentalNotificationSettingsInUIEnabled` | `boolean` | No | Enables/disables the section in the account parental controls page where you can set the parental notifications settings |
| `IsContentControlsEnabled` | `boolean` | No | Enables/disables the section in the account parental controls page where you can set the content control settings |

### Roblox.Authentication.Api.Models.AccountUpgradeRequest

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `upgradeType` | `0 \| 1 \| 2 \| 3 \| 4` | No | ['Unknown' = 0, 'Pioneer' = 1, 'OAuth' = 2, 'Guest' = 3, 'PioneerU13' = 4] |
| `username` | `string` | No |  |
| `password` | `string` | No |  |
| `birthday` | `string` | No |  |
| `email` | `string` | No |  |
| `gender` | `1 \| 2 \| 3` | No |  |

### Roblox.Authentication.Api.Models.AccountUpgradeResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `userId` | `integer` | No |  |
| `username` | `string` | No |  |

### Roblox.PrivateMessages.Api.Models.GetAnnouncementsResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `collection` | `Roblox.PrivateMessages.Api.Models.AnnouncementsDetailsResponse[]` | No |  |
| `totalCollectionSize` | `integer` | No |  |

### Roblox.PrivateMessages.Api.Models.AnnouncementsMetadataResponse

A message details response.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `numOfAnnouncements` | `integer` | No | Number of incoming news |

### Roblox.Authentication.Api.Models.AuthMetaDataResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `cookieLawNoticeTimeout` | `integer` | No |  |

### Roblox.AccountInformation.Api.Models.BirthdateResponse

The birthdate response

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `birthMonth` | `integer` | No | The birth month |
| `birthDay` | `integer` | No | The birth day |
| `birthYear` | `integer` | No | The birth year |

### Roblox.Users.Api.BirthdateRequest

The birthdate request

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `birthMonth` | `integer` | No | The birth month |
| `birthDay` | `integer` | No | The birth day |
| `birthYear` | `integer` | No | The birth year |
| `password` | `string` | No | Password |

### Roblox.Users.Api.BirthdateResponse

The birthdate response

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `birthMonth` | `integer` | No | The birth month |
| `birthDay` | `integer` | No | The birth day |
| `birthYear` | `integer` | No | The birth year |

### Roblox.Authentication.Api.Models.Response.GetClientAssertionResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `clientAssertion` | `string` | No |  |

### Roblox.AccountInformation.Api.Models.DescriptionResponse

The description response

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `description` | `string` | No | The description |

### Roblox.AccountInformation.Api.Models.DescriptionRequest

The description request

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `description` | `string` | No | The description |

### Roblox.Users.Api.DescriptionResponse

The description response

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `description` | `string` | No | The description |

### Roblox.Users.Api.DescriptionRequest

The description request

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `description` | `string` | No | The description |

### Roblox.AccountSettings.Api.EmailResponse

Response model for getting the user's email address and verified status

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `emailAddress` | `string` | No | The masked and formatted email address |
| `verified` | `boolean` | No | The verified status of the email |
| `canBypassPasswordForEmailUpdate` | `boolean` | No | Whether password is required for updating email |

### Roblox.AccountInformation.Api.Models.VerifyEmailRequest

Verify Email Request

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `ticket` | `string` | No | Ticket to verify email |

### Roblox.AccountInformation.Api.Models.VerifyEmailResponse

The verify email response

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `verifiedUserHatAssetId` | `integer` | No | Free item id after email verification |

### Roblox.AccountSettings.Api.SendVerifyEmailRequest

Request model for sending a verify email request

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `freeItem` | `boolean` | No | Whether the user will see messaging that they received a free item after verifying their email |
| `isAdsAccount` | `boolean` | No | Whether the request is coming from ads site |

### Roblox.AccountSettings.Api.CurrentEmailsResponse

Response model for getting the user's verified and pending email addresses

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `verifiedEmail` | `string` | No | The user's most recent verified email address (masked) |
| `pendingEmail` | `string` | No | The user's pending (unverified) email address if one exists (masked) |

### Roblox.Authentication.Api.Models.Request.ExternalAccessRequest

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `authenticationProof` | `string` | No |  |
| `identityProviderPlatformType` | `integer enum (8 values)` | No | ['Undefined' = 0, 'Xbox' = 1, 'Playstation' = 2, 'Web' = 3, 'Steam' = 4, 'Android' = 5, 'Ios' = 6, 'MacOs' = 7] Values: 0, 1, 2, 3, 4, 5, 6, 7 |
| `postAuthenticationIntentId` | `string` | No |  |
| `additionalInfoPayload` | `object` | No |  |

### Roblox.Authentication.Api.Models.Response.ExternalIdentityGateway.ExternalIdentityAccessResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `placeId` | `integer` | No |  |
| `isolationContext` | `string` | No |  |
| `launchData` | `string` | No |  |

### Roblox.Authentication.Api.Models.Request.ExternalLoginRequest

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `identityProvider` | `integer enum (11 values)` | No |  Values: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 999 |
| `additionalData` | `object` | No |  |
| `authenticationProof` | `string` | No |  |

### Roblox.Authentication.Api.Models.Response.ExternalIdentityGateway.ExternalLoginResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | `boolean` | No |  |

### Roblox.Authentication.Api.Models.Request.ExternalLoginAndLinkRequest

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `ctype` | `integer enum (11 values)` | No | ['Email' = 0, 'Username' = 1, 'PhoneNumber' = 2, 'EmailOtpSessionToken' = 3, 'AuthToken' = 4, 'Passkey' = 5, 'AsUser' = 6, 'TwoStepVerification' = 7, 'XboxLive' = 8, 'PlatformLive' = 9, 'MagicLink' = 10] Values: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 |
| `cvalue` | `string` | No |  |
| `password` | `string` | No |  |
| `authenticationProof` | `string` | No |  |
| `IdentityProviderPlatformType` | `integer enum (8 values)` | No | ['Undefined' = 0, 'Xbox' = 1, 'Playstation' = 2, 'Web' = 3, 'Steam' = 4, 'Android' = 5, 'Ios' = 6, 'MacOs' = 7] Values: 0, 1, 2, 3, 4, 5, 6, 7 |
| `additionalInfoPayload` | `object` | No |  |

### Roblox.Authentication.Api.Models.LoginResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `user` | `Roblox.Web.Responses.Users.SkinnyUserResponse` | No |  |
| `twoStepVerificationData` | `Roblox.Authentication.Api.Models.TwoStepVerificationSentResponse` | No |  |
| `identityVerificationLoginTicket` | `string` | No |  |
| `isBanned` | `boolean` | No |  |
| `accountBlob` | `string` | No |  |
| `shouldUpdateEmail` | `boolean` | No |  |
| `recoveryEmail` | `string` | No |  |
| `passkeyRegistrationSucceeded` | `boolean` | No |  |
| `shouldAutoLoginFromRecovery` | `boolean` | No |  |
| `shouldPrompt2svRemoval` | `boolean` | No |  |
| `shouldPromptPasskeyAddition` | `boolean` | No |  |
| `shouldPromptCredentialInvalidation` | `boolean` | No |  |

### Roblox.Authentication.Api.Models.Request.ExternalSignupRequest

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `username` | `string` | No |  |
| `password` | `string` | No |  |
| `birthday` | `string` | No |  |
| `locale` | `string` | No |  |
| `authenticationProof` | `string` | No |  |
| `IdentityProviderPlatformType` | `integer enum (8 values)` | No | ['Undefined' = 0, 'Xbox' = 1, 'Playstation' = 2, 'Web' = 3, 'Steam' = 4, 'Android' = 5, 'Ios' = 6, 'MacOs' = 7] Values: 0, 1, 2, 3, 4, 5, 6, 7 |
| `additionalInfoPayload` | `object` | No |  |

### Roblox.Authentication.Api.Models.Request.ExternalUnlinkRequest

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `IdentityProviderPlatformType` | `integer enum (8 values)` | No | ['Undefined' = 0, 'Xbox' = 1, 'Playstation' = 2, 'Web' = 3, 'Steam' = 4, 'Android' = 5, 'Ios' = 6, 'MacOs' = 7] Values: 0, 1, 2, 3, 4, 5, 6, 7 |
| `additionalInfoPayload` | `object` | No |  |

### Roblox.Authentication.Api.Models.Response.ExternalIdentityGateway.ExternalIdentityNonceResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `nonce` | `string` | No |  |

### Roblox.Games.Api.Models.Response.PlayabilityStatusResponse

Response model for getting a universe's playability status for a user

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `playabilityStatus` | `integer enum (34 values)` | No | The actual playability status of the universe including the reason if unplayable ['UnplayableOtherReason' = 0, 'Playable' = 1, 'GuestProhibited' = 2, 'GameUnapproved' = 3, 'IncorrectConfiguration' = 4, 'UniverseRootPlaceIsPrivate' = 5, 'InsufficientPermissionFriendsOnly' = 6, 'InsufficientPermissionGroupOnly' = 7, 'DeviceRestricted' = 8, 'UnderReview' = 9, 'PurchaseRequired' = 10, 'AccountRestricted' = 11, 'TemporarilyUnavailable' = 12, 'PlaceHasNoPublishedVersion' = 13, 'ComplianceBlocked' = 14, 'ContextualPlayabilityRegionalAvailability' = 15, 'ContextualPlayabilityRegionalCompliance' = 16, 'ContextualPlayabilityAgeRecommendationParentalControls' = 17, 'ContextualPlayabilityExperienceBlockedParentalControls' = 18, 'ContextualPlayabilityAgeGated' = 19, 'ContextualPlayabilityUnverifiedSeventeenPlusUser' = 20, 'FiatPurchaseRequired' = 21, 'FiatPurchaseDeviceRestricted' = 22, 'ContextualPlayabilityUnrated' = 23, 'ContextualPlayabilityAgeGatedByDescriptor' = 24, 'ContextualPlayabilityGeneral' = 25, 'ContextualPlayabilityAgeCheckRequired' = 26, 'ContextualPlayabilityRequireParentApproval' = 27, 'ContextualPlayabilityCoreGated' = 28, 'ContextualPlayabilityTrustedFriendRequired' = 29, 'PlusSubscriptionRequired' = 30, 'ContextualPlayabilityPlaytestDisabled' = 31, 'InsufficientPermissionEditorsOnly' = 32, 'InsufficientPermissionPlayTestersOnly' = 33] Values: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33 |
| `isPlayable` | `boolean` | No | Whether or not the universe is playable for the user |
| `universeId` | `integer` | No | The universeId of the requested universe to help with batching requests |
| `unplayableDisplayText` | `string` | No | Localized display text explaining why unplayable |
| `playableUxTreatment` | `Roblox.Games.Api.Models.Response.PlayableUxTreatment` | No |  |
| `upsellUxTreatment` | `Roblox.Games.Api.Models.Response.UpsellUxTreatment` | No |  |
| `demoModeAvailable` | `boolean` | No | Whether the game supports demo play for users who have not purchased it. Only set when PlayabilityStatus is PurchaseRequired or FiatPurchaseRequired. |
| `privatePlaytestInfo` | `Roblox.Games.Api.Models.Response.PrivatePlaytestInfoResponse` | No |  |

### Roblox.AccountInformation.Api.Models.GenderResponse

The gender response

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `gender` | `integer` | No | The gender |

### Roblox.AccountInformation.Api.Models.GenderRequest

The gender request

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `gender` | `string` | No | The gender |

### Roblox.Users.Api.GenderResponse

The gender response

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `gender` | `integer` | No | The gender |

### Roblox.Users.Api.GenderRequest

The gender request

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `gender` | `1 \| 2 \| 3` | No | The gender ['Unknown' = 1, 'Male' = 2, 'Female' = 3] |

### Roblox.Authentication.Api.Models.Request.IdentityVerificationLoginRequest

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `loginTicket` | `string` | No |  |
| `resultToken` | `string` | No |  |

### Roblox.Authentication.Api.Models.Request.InitializeLoginRequest

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `ctype` | `integer enum (11 values)` | Yes |  Values: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 |
| `cvalue` | `string` | Yes |  |
| `captchaId` | `string` | No |  |
| `captchaToken` | `string` | No |  |
| `captchaProvider` | `string` | No |  |
| `challengeId` | `string` | No |  |

### Roblox.Authentication.Api.Models.Response.InitializeLoginResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `loginMethods` | `Roblox.Authentication.Api.Models.LoginMethodModel[]` | No |  |

### Roblox.Authentication.Api.Models.LoginRequest

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `ctype` | `integer enum (11 values)` | No | ['Email' = 0, 'Username' = 1, 'PhoneNumber' = 2, 'EmailOtpSessionToken' = 3, 'AuthToken' = 4, 'Passkey' = 5, 'AsUser' = 6, 'TwoStepVerification' = 7, 'XboxLive' = 8, 'PlatformLive' = 9, 'MagicLink' = 10] Values: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 |
| `cvalue` | `string` | No |  |
| `password` | `string` | No |  |
| `userId` | `integer` | No |  |
| `securityQuestionSessionId` | `string` | No |  |
| `securityQuestionRedemptionToken` | `string` | No |  |
| `secureAuthenticationIntent` | `Roblox.Authentication.Api.Models.Request.SecureAuthenticationIntentModel` | No |  |
| `accountBlob` | `string` | No |  |
| `accountLinkParameters` | `Roblox.Authentication.Api.Models.AccountLinkParameters` | No |  |
| `captchaId` | `string` | No |  |
| `captchaToken` | `string` | No |  |
| `captchaProvider` | `string` | No |  |
| `challengeId` | `string` | No |  |

### Roblox.Authentication.Api.Models.Request.LogoutFromAllSessionsAndReauthenticateRequest

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `SecureAuthenticationIntent` | `Roblox.Authentication.Api.Models.Request.SecureAuthenticationIntentModel` | No |  |

### Roblox.PrivateMessages.Api.Models.GetMessagesResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `collection` | `Roblox.PrivateMessages.Api.Models.MessageDetailsResponse[]` | No |  |
| `totalCollectionSize` | `integer` | No |  |
| `totalPages` | `integer` | No |  |
| `pageNumber` | `integer` | No |  |

### Roblox.PrivateMessages.Api.Models.BatchMessagesResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `failedMessages` | `Roblox.PrivateMessages.Api.Models.FailedMessageResponse[]` | No |  |

### Roblox.PrivateMessages.Api.Models.UnreadMessagesCountResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `count` | `integer` | No |  |

### Roblox.PrivateMessages.Api.Models.MessageDetailsResponse

A message details response.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | `integer` | No | The message's ID. |
| `sender` | `Roblox.PrivateMessages.Api.Models.VerifiedSkinnyUserResponse` | No |  |
| `recipient` | `Roblox.PrivateMessages.Api.Models.VerifiedSkinnyUserResponse` | No |  |
| `subject` | `string` | No | The subject of the message. |
| `body` | `string` | No | The body of the message. |
| `created` | `string` | No | When the message was created. |
| `updated` | `string` | No | When the message was last updated. |
| `isRead` | `boolean` | No | Whether or not the message has been read. |
| `isSystemMessage` | `boolean` | No | Whether or not the message is a system message. |
| `isReportAbuseDisplayed` | `boolean` | No | Whether or not the abuse report link is displayed for the message. |

### Roblox.AccountInformation.Api.Models.MetadataResponse

The metadata response

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `isAllowedNotificationsEndpointDisabled` | `boolean` | No | Switch for account/settings/allowed-notification-destinations endpoint |
| `isAccountSettingsPolicyEnabled` | `boolean` | No | The account settings policy enabled setting |
| `isPhoneNumberEnabled` | `boolean` | No | Switch for phone endpoints |
| `MaxUserDescriptionLength` | `integer` | No | The limit on the length used for description |
| `isUserDescriptionEnabled` | `boolean` | No | Switch for determining if user description is enabled |
| `isUserBlockEndpointsUpdated` | `boolean` | No | Switch for determining block endpoints to use for the user |
| `shouldUsePersonaForIdVerification` | `boolean` | No | Whether to use Persona for ID verification. |
| `shouldDisplaySessionManagement` | `boolean` | No | Whether to display Session Management. |
| `isPasswordRequiredForAgingDown` | `boolean` | No | Switch for requiring password to change age below 13. |

### Roblox.Authentication.Api.Models.MetadataResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `isUpdateUsernameEnabled` | `boolean` | No |  |
| `ftuxAvatarAssetMap` | `string` | No |  |
| `IsEmailUpsellAtLogoutEnabled` | `boolean` | No |  |
| `ShouldFetchEmailUpsellIXPValuesAtLogout` | `boolean` | No |  |
| `IsAccountRecoveryPromptEnabled` | `boolean` | No |  |
| `IsContactMethodRequiredAtSignup` | `boolean` | No |  |
| `IsUserAgreementsSignupIntegrationEnabled` | `boolean` | No |  |
| `IsPasswordRequiredForUsernameChange` | `boolean` | No |  |
| `IsPasskeyFeatureEnabled` | `boolean` | No |  |
| `IsAltBrowserTracker` | `boolean` | No |  |
| `IsLoginRedirectPageEnabled` | `boolean` | No |  |

### Roblox.TwoStepVerification.Api.MetadataResponse

Two step verification system metadata.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `twoStepVerificationEnabled` | `boolean` | No | Whether or not two step verification is globally enabled. |
| `authenticatorQrCodeSize` | `string` | No | Authenticator QR code image dimensions. |
| `emailCodeLength` | `integer` | No | Number of characters in an email-based two step verification code. |
| `authenticatorCodeLength` | `integer` | No | Number of characters in an authenticator-based two step verification code. |
| `authenticatorHelpSiteAddress` | `string` | No | Address of the help site provided to users to help them with authenticator. |
| `isPasswordRequiredForEnablingAuthenticator` | `boolean` | No | Whether or not a password is required for enabling authenticator. |
| `isPasswordRequiredForEnablingEmailTwoStepVerification` | `boolean` | No | Whether or not a password is required for enabling email 2sv. |
| `isUsingTwoStepWebviewComponent` | `boolean` | No | Whether or not we're using the new 2sv webview component or the manual pop up |
| `isTwoStepEnabledRequiredForEmailPasswordRequirement` | `boolean` | No | Whether or not a 2sv method has to be enabled to require password when enabling email two step verification. |
| `isTwoStepEnabledRequiredForAuthenticatorPasswordRequirement` | `boolean` | No | Whether or not a 2sv method has to be enabled to require password when enabling authenticator. |
| `isSingleMethodEnforcementEnabled` | `boolean` | No | Whether or not the frontend should enforce single method logic. |
| `isSmsTwoStepVerificationAvailable` | `boolean` | No | Whether or not sms two step verification is available for the user. |
| `isSecurityKeyTwoStepVerificationAvailable` | `boolean` | No | Whether or not security key two step verification is available for the user. |
| `isAuthenticatorWithVerifiedPhoneEnabled` | `boolean` | No | Whether or not someone can enable authenticator with just a verified phone number. |
| `isPasswordRequiredForEnablingSecurityKey` | `boolean` | No | Whether or not a password is required for enabling Security Key 2SV. |
| `isPasswordRequiredForEnablingSms2SV` | `boolean` | No | Whether or not a password is required for enabling SMS 2SV. |
| `isPasswordRequiredForChangingRecoveryCodes` | `boolean` | No | Whether or not a password is required for making updates to recovery codes. |
| `isPasswordRequiredForDisablingAuthenticator` | `boolean` | No | Whether or not a password is required for disabling authenticator. |
| `isPasswordRequiredForDisablingEmailTwoStepVerification` | `boolean` | No | Whether or not a password is required for disabling email 2sv. |
| `isPasswordRequiredForDisablingSms2SV` | `boolean` | No | Whether or not a password is required for disabling SMS 2SV. |
| `isRecoveryCodeGenerationForAuthenticatorSetupEnabled` | `boolean` | No | Whether recovery code generation is attempted upon completion of authenticator setup. |
| `isSecurityKeyOnAllPlatformsEnabled` | `boolean` | No | Whether security keys on all platforms is enabled. |
| `receiveWarningsOnDisableTwoStep` | `boolean` | No | Whether users should receive additional warnings when disabling 2SV. |
| `isAndroidSecurityKeyEnabled` | `boolean` | No | Whether Android security keys is enabled. |
| `isSettingsTabRedesignEnabled` | `boolean` | No | Whether the settings tab redesign is enabled. |
| `twoStepCopyTextEnrollmentStatus` | `integer` | No | The enum representing which experiment group the user is in. |
| `isEppUIEnabled` | `boolean` | No | Whether the EPP UI is enabled. |
| `isEppRecoveryCodesEnabled` | `boolean` | No | Whether the EPP recovery codes UI is enabled. |
| `maskedUserEmail` | `string` | No | The masked email for the authenticated user. Typically used in Email 2SV challenges after the challenge has been verified to match the target user. |
| `isUserU13` | `boolean` | No | Whether the user is O13. |
| `isDelayedUiEnabled` | `boolean` | No | Whether the delayed UI is enabled. |
| `is2svRecoveryEnabled` | `boolean` | No | Whether to expose 2SV recovery through the 2SV challenge modal. |

### Roblox.Authentication.Api.Models.Request.DeletePasskeysRequest

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `credentialIDs` | `string[]` | No |  |
| `credentialNicknames` | `string[]` | No |  |

### Roblox.Authentication.Api.Models.Request.FinishPasskeyRegistrationRequest

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `sessionId` | `string` | No |  |
| `credentialNickname` | `string` | No |  |
| `attestationResponse` | `string` | No |  |
| `source` | `string` | No |  |

### Roblox.Authentication.Api.Models.Request.ListPasskeysRequest

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `all` | `boolean` | No |  |

### Roblox.Authentication.Api.Models.Response.ListPasskeyCredentialResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `credentials` | `Roblox.Authentication.Api.Models.Response.PasskeyCredential[]` | No |  |

### Roblox.Authentication.Api.Models.Request.RenamePasskeyRequest

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `credentialID` | `string` | No |  |
| `newNickname` | `string` | No |  |

### Roblox.Authentication.Api.Models.Response.StartAuthenticationResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `authenticationOptions` | `string` | No |  |
| `sessionId` | `string` | No |  |

### Roblox.Authentication.Api.Models.Request.StartPasskeyRegistrationRequest

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `isSilentUpgrade` | `boolean` | No |  |

### Roblox.Authentication.Api.Models.Response.StartPasskeyRegistrationResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `creationOptions` | `string` | No |  |
| `sessionId` | `string` | No |  |

### Roblox.Authentication.Api.Models.Request.FinishARPreAuthPasskeyRegistrationRequest

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `recoverySession` | `string` | No |  |
| `passkeySessionId` | `string` | No |  |
| `passkeyRegistrationResponse` | `string` | No |  |
| `userId` | `integer` | No |  |
| `isPostRecovery` | `boolean` | No |  |
| `source` | `string` | No |  |

### Roblox.Authentication.Api.Models.Request.FinishPasskeyPreauthRegistrationRequest

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `sessionId` | `string` | No |  |
| `registrationResponse` | `string` | No |  |
| `source` | `string` | No |  |

### Roblox.Authentication.Api.Models.Request.StartAuthenticationByUserRequest

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `ctype` | `integer enum (11 values)` | Yes |  Values: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 |
| `cvalue` | `string` | Yes |  |

### Roblox.Authentication.Api.Models.Response.StartAuthenticationByUserResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `authenticationOptions` | `string` | No |  |
| `sessionId` | `string` | No |  |

### Roblox.Authentication.Api.Models.Request.StartPasskeyPreauthRegistrationRequest

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `username` | `string` | No |  |

### Roblox.Authentication.Api.Models.Response.StartPasskeyPreauthRegistrationResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `creationOptions` | `string` | No |  |
| `sessionId` | `string` | No |  |

### Roblox.Authentication.Api.Models.Response.SilentUpgradeEligibilityResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `suEligibility` | `boolean` | No |  |

### Roblox.Authentication.Api.Models.PasswordValidationResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `code` | `integer enum (8 values)` | No | ['ValidPassword' = 0, 'WeakPasswordError' = 1, 'PasswordLengthError' = 2, 'PasswordSameAsUsernameError' = 3, 'ForbiddenPasswordError' = 4, 'DumbStringsError' = 5, 'PasswordLowComplexityError' = 6, 'PasswordTooSimilarToUsernameError' = 7] Values: 0, 1, 2, 3, 4, 5, 6, 7 |
| `message` | `string` | No |  |

### Roblox.Authentication.Api.Models.PasswordValidationModel

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `username` | `string` | No |  |
| `password` | `string` | No |  |

### Roblox.AccountInformation.Api.Models.PhoneResponse

The phone response

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `countryCode` | `string` | No | The country Code |
| `prefix` | `string` | No | The Phone Prefix |
| `phone` | `string` | No | The Phone number |
| `isVerified` | `boolean` | No | Is the phone verified |
| `verificationCodeLength` | `integer` | No | Verification Code Length |
| `canBypassPasswordForPhoneUpdate` | `boolean` | No | Whether user needs to provide password to update their phone numbers |

### Roblox.Platform.UserPhoneNumberVerification.Models.PendingVerificationResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `verificationChannel` | `string` | No |  |
| `data` | `string` | No |  |

### Roblox.AccountInformation.Api.Models.VerifyPhoneRequest

Verify Phone Request

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `code` | `string` | No | Code to verify phone |

### Roblox.AccountInformation.Api.Models.PromotionChannelsResponse

The promotion channels response

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `promotionChannelsVisibilityPrivacy` | `string` | No | The promotion channels visibility privacy level |
| `facebook` | `string` | No | The Facebook channel |
| `twitter` | `string` | No | The Twitter channel |
| `youtube` | `string` | No | The YouTube channel |
| `twitch` | `string` | No | The Twitch channel |

### Roblox.AccountInformation.Api.Models.PromotionChannelsRequest

The promotion channels request

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `facebook` | `string` | No | The Facebook channel |
| `twitter` | `string` | No | The Twitter channel |
| `youtube` | `string` | No | The YouTube channel |
| `twitch` | `string` | No | The Twitch channel |
| `promotionChannelsVisibilityPrivacy` | `string` | No | The promotion channels visibility privacy level |

### Roblox.Authentication.Api.Models.RecoveryMetadataResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `isOnPhone` | `boolean` | No |  |
| `codeLength` | `integer` | No |  |
| `isPhoneFeatureEnabledForUsername` | `boolean` | No |  |
| `isPhoneFeatureEnabledForPassword` | `boolean` | No |  |
| `isBedev2CaptchaEnabledForPasswordReset` | `boolean` | No |  |
| `isUsernameRecoveryDeprecated` | `boolean` | No |  |

### Roblox.Authentication.Api.Models.RevertAccountInfoResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `isTwoStepVerificationEnabled` | `boolean` | No |  |
| `isEmailVerified` | `boolean` | No |  |
| `isEmailChanged` | `boolean` | No |  |
| `isPhoneVerified` | `boolean` | No |  |
| `userId` | `integer` | No |  |
| `username` | `string` | No |  |
| `ticket` | `string` | No |  |

### Roblox.Authentication.Api.Models.RevertAccountSubmitRequest

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `UserId` | `integer` | No |  |
| `NewPassword` | `string` | No |  |
| `NewPasswordRepeated` | `string` | No |  |
| `Ticket` | `string` | No |  |
| `TwoStepVerificationChallengeId` | `string` | No |  |
| `TwoStepVerificationToken` | `string` | No |  |

### Roblox.Authentication.Api.Models.SignupResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `userId` | `integer` | No |  |
| `starterPlaceId` | `integer` | No |  |
| `returnUrl` | `string` | No |  |
| `accountBlob` | `string` | No |  |

### Roblox.Authentication.Api.Models.SocialProvidersResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `providers` | `Roblox.Authentication.Api.Models.ProviderInfoModel[]` | No |  |

### Roblox.Authentication.Api.Models.SocialAuthenticationDisconnectRequest

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `Password` | `string` | No |  |

### Roblox.Web.WebAPI.Models.ApiArrayResponse_System.String_

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `data` | `string[]` | No |  |

### Roblox.AccountSettings.Api.ThemeConfigurationResponse

Response model for get user's theme type

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `themeType` | `string` | No | theme Type |

### Roblox.AccountSettings.Api.ThemeConfigurationRequest

Response model for get user's theme type

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `themeType` | `string` | No | theme Type |

### Roblox.AccountSettings.Api.TradePrivacyResponse

Response model for getting the user's trade privacy settings

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `tradePrivacy` | `string` | No | The current trade privacy setting for the current user |

### Roblox.AccountSettings.Api.UpdateTradePrivacyRequest

Request model for trade privacy setting update

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `tradePrivacy` | `integer enum (8 values)` | No | The desired trade privacy setting for the active user ['Undefined' = 0, 'Disabled' = 1, 'NoOne' = 2, 'Friends' = 3, 'TopFriends' = 4, 'Following' = 5, 'Followers' = 6, 'All' = 7] Values: 0, 1, 2, 3, 4, 5, 6, 7 |

### Roblox.AccountSettings.Api.TradePrivacyUpdateResponse

Response model for updating the user's trade privacy settings

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `tradePrivacy` | `integer enum (8 values)` | No | The trade privacy setting after updating ['Undefined' = 0, 'Disabled' = 1, 'NoOne' = 2, 'Friends' = 3, 'TopFriends' = 4, 'Following' = 5, 'Followers' = 6, 'All' = 7] Values: 0, 1, 2, 3, 4, 5, 6, 7 |
| `inventoryPrivacy` | `integer enum (6 values)` | No | The inventory privacy setting after updating ['NoOne' = 1, 'Friends' = 2, 'FriendsAndFollowing' = 3, 'FriendsFollowingAndFollowers' = 4, 'AllAuthenticatedUsers' = 5, 'AllUsers' = 6] Values: 1, 2, 3, 4, 5, 6 |
| `privacySettingResponse` | `0 \| 1` | No | The response state after updating trade privacy ['Success' = 0, 'Conflict' = 1] |

### Roblox.AccountSettings.Api.TradeValueResponse

Response model for getting the user's trade value settings

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `tradeValue` | `string` | No | The current trade value setting for the current user |

### Roblox.AccountSettings.Api.TradeValueRequest

Request model for trade value setting update

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `tradeValue` | `0 \| 1 \| 2 \| 3 \| 4` | No | The desired trade value setting for the active user ['Undefined' = 0, 'None' = 1, 'Low' = 2, 'Medium' = 3, 'High' = 4] |

### Roblox.Authentication.Api.Models.PasswordChangeModel

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `currentPassword` | `string` | No |  |
| `newPassword` | `string` | No |  |
| `secureAuthenticationIntent` | `Roblox.Authentication.Api.Models.Request.SecureAuthenticationIntentModel` | No |  |

### Roblox.Authentication.Api.Models.UsernameChangeRequest

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `username` | `string` | No |  |
| `password` | `string` | No |  |

### Roblox.Authentication.Api.Models.UsernameChangePriceResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `priceInRobux` | `integer` | No |  |
| `basePriceInRobux` | `integer` | No |  |
| `isFreeUsernameChange` | `boolean` | No |  |

### Roblox.Authentication.Api.Models.UsernamesResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `usernames` | `string[]` | No |  |

### Roblox.Authentication.Api.Models.RecoverUsernameRequest

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `targetType` | `0 \| 1 \| 2` | No | ['Email' = 0, 'PhoneNumber' = 1, 'RecoverySessionID' = 2] |
| `target` | `string` | No |  |

### Roblox.Authentication.Api.Models.RecoverUsernameResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `transmissionType` | `0 \| 1` | No |  |

### Roblox.Authentication.Api.Models.UsernameValidationResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `code` | `integer enum (10 values)` | No | ['ValidUsername' = 0, 'AlreadyInUseError' = 1, 'ModerationError' = 2, 'InvalidLengthError' = 3, 'StartsOrEndsWithUnderscoreError' = 4, 'TooManyUnderscoresError' = 5, 'ContainsSpacesError' = 6, 'InvalidCharactersError' = 7, 'ContainsPiiError' = 10, 'ContainsReservedUsernameError' = 12] Values: 0, 1, 2, 3, 4, 5, 6, 7, 10, 12 |
| `message` | `string` | No |  |

### Roblox.Authentication.Api.Models.UsernameValidationRequest

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `username` | `string` | No |  |
| `birthday` | `string` | No |  |
| `context` | `0 \| 1 \| 2` | No |  |

### Roblox.Users.Api.AuthenticatedGetUserResponse

A response model representing absolute minimal authenticating user information.
No new attributes should be added to this response since it is in the critical path of app launch and we want to minimize dependencies.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | `integer` | No | The user Id. |
| `name` | `string` | No | The user name. |
| `displayName` | `string` | No | The user DisplayName. |

### Roblox.Users.Api.UserAgeBracketResponse

A user age bracket response model.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `ageBracket` | `integer` | No | The age bracket of the user. |

### Roblox.Users.Api.UserCountryCodeResponse

A user country code response model.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `countryCode` | `string` | No | The country code of the user. |

### Roblox.Users.Api.UserRolesResponse

A user roles response model.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `roles` | `string[]` | No | The roles of the user. |

### Roblox.Inventory.Api.Models.CanViewInventoryResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `canView` | `boolean` | No | Boolean describing if the user's inventory can be viewed |

### Roblox.TwoStepVerification.Api.VerifyCodeResponse

Result for a successful verification.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `verificationToken` | `string` | No | The verification token. |

### Roblox.TwoStepVerification.Api.RetractDialogRequest

Request parameters for retracting a Cross Device dialog from state ACTIVE to PENDING.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `challengeId` | `string` | No | The two step verification challenge ID. |
| `actionType` | `integer enum (9 values)` | No | The Roblox.TwoStepVerification.Client.TwoStepVerificationActionType associated with the challenge. Values: 0, 1, 2, 3, 4, 5, 6, 7, 8 |

### Roblox.TwoStepVerification.Api.RetryApprovalRequest

Request parameters for retrying a Cross Device two step verification approval.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `challengeId` | `string` | No | The two step verification challenge ID. |
| `actionType` | `integer enum (9 values)` | No | The Roblox.TwoStepVerification.Client.TwoStepVerificationActionType associated with the challenge. Values: 0, 1, 2, 3, 4, 5, 6, 7, 8 |

### Roblox.TwoStepVerification.Api.VerifyApprovalRequest

Request parameters for verifying a Cross Device two step verification approval. Does not use verification code.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `challengeId` | `string` | No | The two step verification challenge ID. |
| `actionType` | `integer enum (9 values)` | No | The Roblox.TwoStepVerification.Client.TwoStepVerificationActionType associated with the challenge. Values: 0, 1, 2, 3, 4, 5, 6, 7, 8 |

### Roblox.TwoStepVerification.Api.VerifyApprovalResponse

Result for a successful Cross Device approval verification.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `verificationToken` | `string` | No | The verification token. |

### Roblox.TwoStepVerification.Api.VerifyStartPasskeyResponse

Result for a successful verification.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `authenticationOptions` | `string` | No | The authentication options for the passkey. |
| `sessionId` | `string` | No | The session of the authentication attempt. |

### Roblox.TwoStepVerification.Api.VerifyStartSecurityKeyResponse

Result for a successful verification.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `authenticationOptions` | `string` | No | The authentication options for the hardware key. |
| `sessionId` | `string` | No | The session of the authentication attempt. |

### Roblox.TwoStepVerification.Api.UserConfiguration

The users two step verification configuration.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `primaryMediaType` | `integer enum (8 values)` | No | The preferred two step verification method for the user. Values: 0, 1, 2, 3, 4, 5, 6, 7 |
| `methods` | `Roblox.TwoStepVerification.Api.UserConfigurationMethod[]` | No | The two step verification methods associated with the user. |

### Roblox.TwoStepVerification.Api.EnableTwoStepVerificationRequest

Request parameters for enabling two step verification.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `password` | `string` | No | The user's password. |
| `secureAuthenticationIntent` | `Roblox.TwoStepVerification.Api.Models.Request.SecureAuthenticationIntentModel` | No |  |

### Roblox.TwoStepVerification.Api.EnableAuthenticatorResponse

Response parameters for initiating enabling authenticator-based two step verification.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `setupToken` | `string` | No | The setup token for turning on authenticator. |
| `qrCodeImageUrl` | `string` | No | The Url to the QR code image to scan into the authenticator app. |
| `manualEntryKey` | `string` | No | The manual entry key to input into the authenticator app. |

### Roblox.TwoStepVerification.Api.EnableVerifyAuthenticatorRequest

Request parameters for authenticator enabling-verify.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `setupToken` | `string` | No | The setup token from the enable authenticator request. |
| `code` | `string` | No | The code from the authenticator app. |
| `password` | `string` | No | The user's password. |
| `secureAuthenticationIntent` | `Roblox.TwoStepVerification.Api.Models.Request.SecureAuthenticationIntentModel` | No |  |

### Roblox.TwoStepVerification.Api.EnableVerifyAuthenticatorResponse

Response parameters for finishing enabling authenticator-based two-step verification.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `recoveryCodes` | `string[]` | No | Recovery codes automatically generated for the user (when applicable; the user should not already have a set of recovery codes). |

### Roblox.TwoStepVerification.Api.DisableSecurityKeyRequest

Request information needed to disable a list of security keys.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `credentialNicknames` | `string[]` | No | An array of nicknames of credentials to be deleted. |
| `credentialIDs` | `string[]` | No | An array of IDs of credentials to be deleted. Preferred over nicknames. |

### Roblox.TwoStepVerification.Api.EnableSecurityKeyResponse

Response parameters for initiating enabling security key-based two step verification.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `creationOptions` | `string` | No | The credential registration options for the hardware key. |
| `sessionId` | `string` | No | The session of the registration attempt. |

### Roblox.TwoStepVerification.Api.EnableVerifySecurityKeyRequest

Request information needed to complete the registration of a security key.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `sessionId` | `string` | No | The session of the registration attempt. |
| `credentialNickname` | `string` | No | The nickname of the new credential. |
| `attestationResponse` | `string` | No | The hardware key's response. |

### Roblox.TwoStepVerification.Api.ListSecurityKeyResponse

Response parameters for listing all credentials under a user.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `credentials` | `Roblox.TwoStepVerification.Api.SecurityKeyCredential[]` | No | An array of credentials for a user. |

### Roblox.TwoStepVerification.Api.DisableTwoStepVerificationRequest

Request information needed to disable two step verification.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `password` | `string` | No | The user's password. |
| `reauthenticationToken` | `string` | No | A re-authentication token redeemable for any password check. |

### Roblox.AccountInformation.Api.Models.PromotionChannelsByUserIdResponse

The promotion channels response

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `facebook` | `string` | No | The Facebook channel |
| `twitter` | `string` | No | The Twitter channel |
| `youtube` | `string` | No | The YouTube channel |
| `twitch` | `string` | No | The Twitch channel |

### Roblox.TwoStepVerification.Api.RecoveryCodesStatusResponse

The response for getting the status of recovery codes for a user.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `activeCount` | `integer` | No | The number of unused recovery codes the user has available. |
| `created` | `string` | No | The date time the recovery codes were generated at. |

### Roblox.TwoStepVerification.Api.ClearRecoveryCodesRequest

Request information needed to clear existing recovery codes.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `password` | `string` | No | The user's password. |

### Roblox.TwoStepVerification.Api.RegenerateRecoveryCodesRequest

Request information needed to regenerate recovery codes.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `password` | `string` | No | The user's password. |

### Roblox.TwoStepVerification.Api.RegenerateRecoveryCodesResponse

The response for regenerating recovery codes.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `recoveryCodes` | `string[]` | No | The collection of generated recovery codes. |

### Roblox.AccountInformation.Api.RobloxBadgeResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | `integer` | No | The ID belonging to this Roblox badge. |
| `name` | `string` | No | The name of this Roblox badge. |
| `description` | `string` | No | The description belonging to this Roblox badge. |
| `imageUrl` | `string` | No | The URL corresponding to the image which represents this Roblox badge. |

### Roblox.Authentication.Api.Models.EmailValidationResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `isEmailValid` | `boolean` | No |  |

### Roblox.Authentication.Api.Models.RecommendedUsernameResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `didGenerateNewUsername` | `boolean` | No |  |
| `suggestedUsernames` | `string[]` | No |  |

### Roblox.Authentication.Api.Models.RecommendedUsernameFromDisplayNameRequest

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `displayName` | `string` | No |  |
| `birthday` | `string` | No |  |

### Roblox.Authentication.Api.Models.RecommendedUsernameRequest

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `username` | `string` | No |  |
| `birthday` | `string` | No |  |

### Roblox.Authentication.Api.Models.XboxConnectionModel

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `hasConnectedXboxAccount` | `boolean` | No |  |
| `gamertag` | `string` | No |  |

### Roblox.Authentication.Api.Models.XboxLoginConsecutiveDaysResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `count` | `integer` | No |  |

### Roblox.Authentication.Api.Models.XboxTranslateRequest

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `ids` | `string[]` | No |  |

### Roblox.Authentication.Api.Models.XboxCollectionsOfUserResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `Users` | `Roblox.Authentication.Api.Models.XboxUserModel[]` | No |  |

### Roblox.Authentication.Api.Models.PasswordStatusResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `valid` | `boolean` | No |  |

### Roblox.Authentication.Api.Models.PasswordResetMetadataResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `users` | `Roblox.Web.Responses.Users.LegacyUserResponse[]` | No |  |

### Roblox.Authentication.Api.Models.PasswordResetModel

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `targetType` | `0 \| 1 \| 2` | No | ['Email' = 0, 'PhoneNumber' = 1, 'RecoverySessionID' = 2] |
| `ticket` | `string` | No |  |
| `userId` | `integer` | No |  |
| `password` | `string` | No |  |
| `passwordRepeated` | `string` | No |  |
| `twoStepVerificationChallengeId` | `string` | No |  |
| `twoStepVerificationToken` | `string` | No |  |
| `accountBlob` | `string` | No |  |
| `secureAuthenticationIntent` | `Roblox.Authentication.Api.Models.Request.SecureAuthenticationIntentModel` | No |  |
| `newEmail` | `string` | No |  |
| `passkeySessionId` | `string` | No |  |
| `passkeyRegistrationResponse` | `string` | No |  |

### Roblox.Authentication.Api.Models.SendResetPasswordRequest

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `targetType` | `0 \| 1 \| 2` | No | ['Email' = 0, 'PhoneNumber' = 1, 'RecoverySessionID' = 2] |
| `target` | `string` | No |  |
| `captchaId` | `string` | No |  |
| `captchaToken` | `string` | No |  |
| `captchaProvider` | `string` | No |  |
| `challengeId` | `string` | No |  |

### Roblox.Authentication.Api.Models.SendResetPasswordResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `nonce` | `string` | No |  |
| `transmissionType` | `0 \| 1` | No | ['Sms' = 0, 'Email' = 1] |

### Roblox.Authentication.Api.Models.PasswordResetVerificationRequest

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `targetType` | `0 \| 1 \| 2` | No | ['Email' = 0, 'PhoneNumber' = 1, 'RecoverySessionID' = 2] |
| `nonce` | `string` | No |  |
| `code` | `string` | No |  |

### Roblox.Authentication.Api.Models.PasswordResetVerificationResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `userTickets` | `Roblox.Authentication.Api.Models.ForgotPasswordUserResponse[]` | No |  |

### Roblox.Api.Notifications.Models.GetPushDestinationsResponseModel

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `destinations` | `Roblox.Api.Notifications.Models.UserPushDestination[]` | No | List of destinations for the user push notification |
| `statusMessage` | `string` | No | Message for the success response |

### Roblox.Authentication.Api.Models.Request.LogoutV3Request

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `logoutReason` | `string` | No |  |
| `url` | `string` | No |  |
| `userId` | `string` | No |  |

### Roblox.Authentication.Api.TwoStepVerificationLoginRequest

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `challengeId` | `string` | No |  |
| `verificationToken` | `string` | No |  |
| `rememberDevice` | `boolean` | No |  |
| `secureAuthenticationIntent` | `Roblox.Authentication.Api.Models.Request.SecureAuthenticationIntentModel` | No |  |
| `accountBlob` | `string` | No |  |
| `accountLinkParameters` | `Roblox.Authentication.Api.Models.AccountLinkParameters` | No |  |

### Roblox.Authentication.Api.Models.TwoStepVerificationV3LoginResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `identityVerificationLoginTicket` | `string` | No |  |
| `accountBlob` | `string` | No |  |