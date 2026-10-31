---
name: "TwoStepVerification Api v1"
last_updated: 2026-10-30T19:56:08Z
type: legacy
api_base_url: "https://twostepverification.roblox.com"
versions: [v1]
endpoints: 31
auth: [cookie]
---

# TwoStepVerification Api v1

> **Warning:** Legacy APIs with cookie authentication can incorporate breaking changes without notice. We don't recommend them for production applications.

**Base URL:** `https://twostepverification.roblox.com`
**Versions:** v1

## Endpoints

### GET `/v1/metadata`

Gets two step verification system metadata.

The metadata endpoint takes in optional request parameters to output additional context
for when the user is unauthenticated but attempting to login with two step verification.

When supplied, all three request parameters must be sent and match up.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | query | `integer (int64)` | No | The user ID. |
| `challengeId` | query | `string` | No | The active two step verification challenge ID if there is one. |
| `actionType` | query | `integer (int32)` | No | The Roblox.TwoStepVerification.Client.TwoStepVerificationActionType associated with the challenge. Valid values: `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8` |

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
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://twostepverification.roblox.com/v1/metadata"
```

### GET `/v1/users/{userId}/configuration`

Gets two step verification configuration for the specified user.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer (int64)` | Yes | The Id of the user to get the configuration for. |
| `challengeId` | query | `string` | No | The active challenge for the user (as an alternative when the user is unauthenticated). |
| `actionType` | query | `integer (int32)` | No | The action type the challengeId is associated with. Valid values: `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8` |

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
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://twostepverification.roblox.com/v1/users/{USERID}/configuration"
```

### GET `/v1/users/{userId}/recovery-codes`

Gets the current status of recovery codes for a user.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer (int64)` | Yes | The user ID. |

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
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://twostepverification.roblox.com/v1/users/{USERID}/recovery-codes"
```

### POST `/v1/users/{userId}/challenges/authenticator/verify`

Verifies a two step verification challenge code via authenticator app.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer (int64)` | Yes | The user ID. |

**Request Body:** `application/json` — Type: `Roblox.TwoStepVerification.Api.VerifyCodeRequest`

See [Roblox.TwoStepVerification.Api.VerifyCodeRequest](#roblox-twostepverification-api-verifycoderequest) in Models.

**Request example:**
```json
{
  "challengeId": "string",
  "actionType": 0,
  "code": "string"
}
```

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
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://twostepverification.roblox.com/v1/users/{USERID}/challenges/authenticator/verify" \
  -H "Content-Type: application/json" \
  -d '{
  "challengeId": "string",
  "actionType": 0,
  "code": "string"
}'
```

### POST `/v1/users/{userId}/challenges/cross-device/retract`

Reverts a user's dialog state from ACTIVE to PENDING.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer (int64)` | Yes | The user ID. |

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
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://twostepverification.roblox.com/v1/users/{USERID}/challenges/cross-device/retract" \
  -H "Content-Type: application/json" \
  -d '{
  "challengeId": "string",
  "actionType": 0
}'
```

### POST `/v1/users/{userId}/challenges/cross-device/retry`

Retry a Cross Device two step verification approval.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer (int64)` | Yes | The user ID. |

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
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://twostepverification.roblox.com/v1/users/{USERID}/challenges/cross-device/retry" \
  -H "Content-Type: application/json" \
  -d '{
  "challengeId": "string",
  "actionType": 0
}'
```

### POST `/v1/users/{userId}/challenges/cross-device/verify`

Verifies a two step verification approval via Cross Device. Cross Device approval does not use a verification code.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer (int64)` | Yes | The user ID. |

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
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://twostepverification.roblox.com/v1/users/{USERID}/challenges/cross-device/verify" \
  -H "Content-Type: application/json" \
  -d '{
  "challengeId": "string",
  "actionType": 0
}'
```

### POST `/v1/users/{userId}/challenges/email/send-code`

Sends a two step verification challenge code via email.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer (int64)` | Yes | The user ID. |

**Request Body:** `application/json` — Type: `Roblox.TwoStepVerification.Api.SendCodeRequest`

See [Roblox.TwoStepVerification.Api.SendCodeRequest](#roblox-twostepverification-api-sendcoderequest) in Models.

**Request example:**
```json
{
  "challengeId": "string",
  "actionType": 0
}
```

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
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://twostepverification.roblox.com/v1/users/{USERID}/challenges/email/send-code" \
  -H "Content-Type: application/json" \
  -d '{
  "challengeId": "string",
  "actionType": 0
}'
```

### POST `/v1/users/{userId}/challenges/email/verify`

Verifies a two step verification challenge with a code sent via email.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer (int64)` | Yes | The user ID. |

**Request Body:** `application/json` — Type: `Roblox.TwoStepVerification.Api.VerifyCodeRequest`

See [Roblox.TwoStepVerification.Api.VerifyCodeRequest](#roblox-twostepverification-api-verifycoderequest) in Models.

**Request example:**
```json
{
  "challengeId": "string",
  "actionType": 0,
  "code": "string"
}
```

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
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://twostepverification.roblox.com/v1/users/{USERID}/challenges/email/verify" \
  -H "Content-Type: application/json" \
  -d '{
  "challengeId": "string",
  "actionType": 0,
  "code": "string"
}'
```

### POST `/v1/users/{userId}/challenges/passkey/verify-finish`

Validates the assertion data returned by the passkey.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer (int64)` | Yes | The user ID. |

**Request Body:** `application/json` — Type: `Roblox.TwoStepVerification.Api.VerifyCodeRequest`

See [Roblox.TwoStepVerification.Api.VerifyCodeRequest](#roblox-twostepverification-api-verifycoderequest) in Models.

**Request example:**
```json
{
  "challengeId": "string",
  "actionType": 0,
  "code": "string"
}
```

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
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://twostepverification.roblox.com/v1/users/{USERID}/challenges/passkey/verify-finish" \
  -H "Content-Type: application/json" \
  -d '{
  "challengeId": "string",
  "actionType": 0,
  "code": "string"
}'
```

### POST `/v1/users/{userId}/challenges/passkey/verify-start`

Provides a challenge for the passkey to authenticate.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer (int64)` | Yes | The user ID. |

**Request Body:** `application/json` — Type: `Roblox.TwoStepVerification.Api.SendCodeRequest`

See [Roblox.TwoStepVerification.Api.SendCodeRequest](#roblox-twostepverification-api-sendcoderequest) in Models.

**Request example:**
```json
{
  "challengeId": "string",
  "actionType": 0
}
```

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
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://twostepverification.roblox.com/v1/users/{USERID}/challenges/passkey/verify-start" \
  -H "Content-Type: application/json" \
  -d '{
  "challengeId": "string",
  "actionType": 0
}'
```

### POST `/v1/users/{userId}/challenges/password/verify`

Verifies a two step verification challenge with a password (code).

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer (int64)` | Yes | The user ID. |

**Request Body:** `application/json` — Type: `Roblox.TwoStepVerification.Api.VerifyCodeRequest`

See [Roblox.TwoStepVerification.Api.VerifyCodeRequest](#roblox-twostepverification-api-verifycoderequest) in Models.

**Request example:**
```json
{
  "challengeId": "string",
  "actionType": 0,
  "code": "string"
}
```

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
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://twostepverification.roblox.com/v1/users/{USERID}/challenges/password/verify" \
  -H "Content-Type: application/json" \
  -d '{
  "challengeId": "string",
  "actionType": 0,
  "code": "string"
}'
```

### POST `/v1/users/{userId}/challenges/recovery-codes/verify`

Verifies a two step verification challenge via a recovery code.

Once a recovery code has been used to verify a challenge it cannot be used again.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer (int64)` | Yes | The user ID. |

**Request Body:** `application/json` — Type: `Roblox.TwoStepVerification.Api.VerifyCodeRequest`

See [Roblox.TwoStepVerification.Api.VerifyCodeRequest](#roblox-twostepverification-api-verifycoderequest) in Models.

**Request example:**
```json
{
  "challengeId": "string",
  "actionType": 0,
  "code": "string"
}
```

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
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://twostepverification.roblox.com/v1/users/{USERID}/challenges/recovery-codes/verify" \
  -H "Content-Type: application/json" \
  -d '{
  "challengeId": "string",
  "actionType": 0,
  "code": "string"
}'
```

### POST `/v1/users/{userId}/challenges/security-key/verify-finish`

Validates the assertion data returned by the security key.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer (int64)` | Yes | The user ID. |

**Request Body:** `application/json` — Type: `Roblox.TwoStepVerification.Api.VerifyCodeRequest`

See [Roblox.TwoStepVerification.Api.VerifyCodeRequest](#roblox-twostepverification-api-verifycoderequest) in Models.

**Request example:**
```json
{
  "challengeId": "string",
  "actionType": 0,
  "code": "string"
}
```

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
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://twostepverification.roblox.com/v1/users/{USERID}/challenges/security-key/verify-finish" \
  -H "Content-Type: application/json" \
  -d '{
  "challengeId": "string",
  "actionType": 0,
  "code": "string"
}'
```

### POST `/v1/users/{userId}/challenges/security-key/verify-start`

Provides a challenge for the security key to authenticate.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer (int64)` | Yes | The user ID. |

**Request Body:** `application/json` — Type: `Roblox.TwoStepVerification.Api.SendCodeRequest`

See [Roblox.TwoStepVerification.Api.SendCodeRequest](#roblox-twostepverification-api-sendcoderequest) in Models.

**Request example:**
```json
{
  "challengeId": "string",
  "actionType": 0
}
```

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
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://twostepverification.roblox.com/v1/users/{USERID}/challenges/security-key/verify-start" \
  -H "Content-Type: application/json" \
  -d '{
  "challengeId": "string",
  "actionType": 0
}'
```

### POST `/v1/users/{userId}/challenges/sms/send-code`

Sends a two step verification code via SMS for the specified user.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer (int64)` | Yes | The user ID. |

**Request Body:** `application/json` — Type: `Roblox.TwoStepVerification.Api.SendCodeRequest`

See [Roblox.TwoStepVerification.Api.SendCodeRequest](#roblox-twostepverification-api-sendcoderequest) in Models.

**Request example:**
```json
{
  "challengeId": "string",
  "actionType": 0
}
```

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
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://twostepverification.roblox.com/v1/users/{USERID}/challenges/sms/send-code" \
  -H "Content-Type: application/json" \
  -d '{
  "challengeId": "string",
  "actionType": 0
}'
```

### POST `/v1/users/{userId}/challenges/sms/verify`

Verifies a two step verification challenge with a code sent via SMS.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer (int64)` | Yes | The user ID. |

**Request Body:** `application/json` — Type: `Roblox.TwoStepVerification.Api.VerifyCodeRequest`

See [Roblox.TwoStepVerification.Api.VerifyCodeRequest](#roblox-twostepverification-api-verifycoderequest) in Models.

**Request example:**
```json
{
  "challengeId": "string",
  "actionType": 0,
  "code": "string"
}
```

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
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://twostepverification.roblox.com/v1/users/{USERID}/challenges/sms/verify" \
  -H "Content-Type: application/json" \
  -d '{
  "challengeId": "string",
  "actionType": 0,
  "code": "string"
}'
```

### POST `/v1/users/{userId}/configuration/authenticator/disable`

Disables two step verification via authenticator for the specified user.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer (int64)` | Yes | The user ID. |

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
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://twostepverification.roblox.com/v1/users/{USERID}/configuration/authenticator/disable" \
  -H "Content-Type: application/json" \
  -d '{
  "password": "string",
  "reauthenticationToken": "string"
}'
```

### POST `/v1/users/{userId}/configuration/authenticator/enable`

Initiates enabling authenticator-based two step verification for the specified user.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer (int64)` | Yes | The user ID. |

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
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
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

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer (int64)` | Yes | The user ID. |

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
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
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

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer (int64)` | Yes | The user ID. |

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
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://twostepverification.roblox.com/v1/users/{USERID}/configuration/email/disable" \
  -H "Content-Type: application/json" \
  -d '{
  "password": "string",
  "reauthenticationToken": "string"
}'
```

### POST `/v1/users/{userId}/configuration/email/enable`

Enables two step verification via email for the specified user.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer (int64)` | Yes | The user ID. |

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
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
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

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer (int64)` | Yes | The user ID. |

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
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
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

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer (int64)` | Yes | The user ID. |

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
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://twostepverification.roblox.com/v1/users/{USERID}/configuration/security-key/enable" \
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

### POST `/v1/users/{userId}/configuration/security-key/enable-verify`

Finishes security key registration and stores credential. Enables security key as a 2sv media type if it is a user's first key.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer (int64)` | Yes | The user ID. |

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
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
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

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer (int64)` | Yes | The user ID. |

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
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://twostepverification.roblox.com/v1/users/{USERID}/configuration/security-key/list"
```

### POST `/v1/users/{userId}/configuration/security-key/rename`

Rename a user's security key.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer (int64)` | Yes | The user ID. |

**Request Body:** `application/json` — Type: `Roblox.TwoStepVerification.Api.RenameSecurityKeyRequest`

See [Roblox.TwoStepVerification.Api.RenameSecurityKeyRequest](#roblox-twostepverification-api-renamesecuritykeyrequest) in Models.

**Request example:**
```json
{
  "credentialID": "string",
  "newNickname": "string"
}
```

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: 2: The user ID is invalid. 17: Invalid security key nickname. 21: Invalid security key id.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed
- `503`: 7: Two step verification is currently under maintenance.

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://twostepverification.roblox.com/v1/users/{USERID}/configuration/security-key/rename" \
  -H "Content-Type: application/json" \
  -d '{
  "credentialID": "string",
  "newNickname": "string"
}'
```

### POST `/v1/users/{userId}/configuration/sms/disable`

Disables two step verification via SMS for the specified user.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer (int64)` | Yes | The user ID. |

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
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://twostepverification.roblox.com/v1/users/{USERID}/configuration/sms/disable" \
  -H "Content-Type: application/json" \
  -d '{
  "password": "string",
  "reauthenticationToken": "string"
}'
```

### POST `/v1/users/{userId}/configuration/sms/enable`

Enables two step verification via SMS for the specified user.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer (int64)` | Yes | The user ID. |

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
- `400`: 4: The password is invalid. 15: The phone number is invalid.
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed 2: The user ID is invalid.
- `503`: 7: Two step verification is currently under maintenance. 8: The user is not allowed to perform the requested action.

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://twostepverification.roblox.com/v1/users/{USERID}/configuration/sms/enable" \
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

### POST `/v1/users/{userId}/recovery-codes/clear`

Clears any existing recovery codes for the user.

Clearing recovery codes voids any recovery codes previously generated for the user.
New recovery codes will have to be generated to pass two step verification via recovery code.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer (int64)` | Yes | The user ID. |

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
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
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

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer (int64)` | Yes | The user ID to generate recovery codes for. |

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
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://twostepverification.roblox.com/v1/users/{USERID}/recovery-codes/regenerate" \
  -H "Content-Type: application/json" \
  -d '{
  "password": "string"
}'
```

## Models

### Roblox.TwoStepVerification.Api.ClearRecoveryCodesRequest

Request information needed to clear existing recovery codes.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `password` | `string` | No | The user's password. |

### Roblox.TwoStepVerification.Api.DisableSecurityKeyRequest

Request information needed to disable a list of security keys.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `credentialNicknames` | `string[]` | No | An array of nicknames of credentials to be deleted. |
| `credentialIDs` | `string[]` | No | An array of IDs of credentials to be deleted. Preferred over nicknames. |

### Roblox.TwoStepVerification.Api.DisableTwoStepVerificationRequest

Request information needed to disable two step verification.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `password` | `string` | No | The user's password. |
| `reauthenticationToken` | `string` | No | A re-authentication token redeemable for any password check. |

### Roblox.TwoStepVerification.Api.EnableAuthenticatorResponse

Response parameters for initiating enabling authenticator-based two step verification.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `setupToken` | `string` | No | The setup token for turning on authenticator. |
| `qrCodeImageUrl` | `string` | No | The Url to the QR code image to scan into the authenticator app. |
| `manualEntryKey` | `string` | No | The manual entry key to input into the authenticator app. |

### Roblox.TwoStepVerification.Api.EnableSecurityKeyResponse

Response parameters for initiating enabling security key-based two step verification.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `creationOptions` | `string` | No | The credential registration options for the hardware key. |
| `sessionId` | `string` | No | The session of the registration attempt. |

### Roblox.TwoStepVerification.Api.EnableTwoStepVerificationRequest

Request parameters for enabling two step verification.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `password` | `string` | No | The user's password. |
| `secureAuthenticationIntent` | `Roblox.TwoStepVerification.Api.Models.Request.SecureAuthenticationIntentModel` | No |  |

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

### Roblox.TwoStepVerification.Api.Models.Request.SecureAuthenticationIntentModel

Model describing secure auth intent.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `clientPublicKey` | `string` | No |  |
| `clientEpochTimestamp` | `integer` | No |  |
| `saiSignature` | `string` | No |  |
| `serverNonce` | `string` | No |  |

### Roblox.TwoStepVerification.Api.RecoveryCodesStatusResponse

The response for getting the status of recovery codes for a user.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `activeCount` | `integer` | No | The number of unused recovery codes the user has available. |
| `created` | `string` | No | The date time the recovery codes were generated at. |

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

### Roblox.TwoStepVerification.Api.RenameSecurityKeyRequest

Request information needed to rename two step verification.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `credentialID` | `string` | No | A credential ID to be renamed. |
| `newNickname` | `string` | No | The new nickname for the credential. |

### Roblox.TwoStepVerification.Api.RetractDialogRequest

Request parameters for retracting a Cross Device dialog from state ACTIVE to PENDING.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `challengeId` | `string` | No | The two step verification challenge ID. |
| `actionType` | `integer enum (9 values)` | No | The Roblox.TwoStepVerification.Client.TwoStepVerificationActionType associated with the challenge. ['Unknown' = 0, 'Login' = 1, 'RobuxSpend' = 2, 'ItemTrade' = 3, 'Resale' = 4, 'PasswordReset' = 5, 'RevertAccount' = 6, 'Generic' = 7, 'GenericWithRecoveryCodes' = 8] Values: 0, 1, 2, 3, 4, 5, 6, 7, 8 |

### Roblox.TwoStepVerification.Api.RetryApprovalRequest

Request parameters for retrying a Cross Device two step verification approval.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `challengeId` | `string` | No | The two step verification challenge ID. |
| `actionType` | `integer enum (9 values)` | No | The Roblox.TwoStepVerification.Client.TwoStepVerificationActionType associated with the challenge. ['Unknown' = 0, 'Login' = 1, 'RobuxSpend' = 2, 'ItemTrade' = 3, 'Resale' = 4, 'PasswordReset' = 5, 'RevertAccount' = 6, 'Generic' = 7, 'GenericWithRecoveryCodes' = 8] Values: 0, 1, 2, 3, 4, 5, 6, 7, 8 |

### Roblox.TwoStepVerification.Api.SecurityKeyCredential

Credential information that includes its nickname and any additional metadata.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `nickname` | `string` | No | Nickname the user has chosen for this credential. |
| `credentialID` | `string` | No | Foreign key reference for this credential in the security-key-credentials database |

### Roblox.TwoStepVerification.Api.SendCodeRequest

Request parameters for sending a two step verification code.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `challengeId` | `string` | No | The two step verification challenge ID. |
| `actionType` | `integer enum (9 values)` | No | The Roblox.TwoStepVerification.Client.TwoStepVerificationActionType associated with the challenge. ['Unknown' = 0, 'Login' = 1, 'RobuxSpend' = 2, 'ItemTrade' = 3, 'Resale' = 4, 'PasswordReset' = 5, 'RevertAccount' = 6, 'Generic' = 7, 'GenericWithRecoveryCodes' = 8] Values: 0, 1, 2, 3, 4, 5, 6, 7, 8 |

### Roblox.TwoStepVerification.Api.UserConfiguration

The users two step verification configuration.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `primaryMediaType` | `integer enum (8 values)` | No | The preferred two step verification method for the user. Values: 0, 1, 2, 3, 4, 5, 6, 7 |
| `methods` | `Roblox.TwoStepVerification.Api.UserConfigurationMethod[]` | No | The two step verification methods associated with the user. |

### Roblox.TwoStepVerification.Api.UserConfigurationMethod

A user configuration method option.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `mediaType` | `integer enum (8 values)` | No | The Roblox.TwoStepVerification.Client.TwoStepVerificationMediaType for the method. ['Email' = 0, 'SMS' = 1, 'Authenticator' = 2, 'RecoveryCode' = 3, 'SecurityKey' = 4, 'CrossDevice' = 5, 'Password' = 6, 'Passkey' = 7] Values: 0, 1, 2, 3, 4, 5, 6, 7 |
| `enabled` | `boolean` | No | Whether or not the method is enabled. |
| `updated` | `string` | No | The last time this method was updated for the user. |

### Roblox.TwoStepVerification.Api.VerifyApprovalRequest

Request parameters for verifying a Cross Device two step verification approval. Does not use verification code.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `challengeId` | `string` | No | The two step verification challenge ID. |
| `actionType` | `integer enum (9 values)` | No | The Roblox.TwoStepVerification.Client.TwoStepVerificationActionType associated with the challenge. ['Unknown' = 0, 'Login' = 1, 'RobuxSpend' = 2, 'ItemTrade' = 3, 'Resale' = 4, 'PasswordReset' = 5, 'RevertAccount' = 6, 'Generic' = 7, 'GenericWithRecoveryCodes' = 8] Values: 0, 1, 2, 3, 4, 5, 6, 7, 8 |

### Roblox.TwoStepVerification.Api.VerifyApprovalResponse

Result for a successful Cross Device approval verification.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `verificationToken` | `string` | No | The verification token. |

### Roblox.TwoStepVerification.Api.VerifyCodeRequest

Request parameters for verifying a two step verification code.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `challengeId` | `string` | No | The two step verification challenge ID. |
| `actionType` | `integer enum (9 values)` | No | The Roblox.TwoStepVerification.Client.TwoStepVerificationActionType associated with the challenge. ['Unknown' = 0, 'Login' = 1, 'RobuxSpend' = 2, 'ItemTrade' = 3, 'Resale' = 4, 'PasswordReset' = 5, 'RevertAccount' = 6, 'Generic' = 7, 'GenericWithRecoveryCodes' = 8] Values: 0, 1, 2, 3, 4, 5, 6, 7, 8 |
| `code` | `string` | No | The two step verification code. |

### Roblox.TwoStepVerification.Api.VerifyCodeResponse

Result for a successful verification.

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