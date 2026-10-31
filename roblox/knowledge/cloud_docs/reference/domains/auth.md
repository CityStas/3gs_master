---
name: "Authentication Api v3"
last_updated: 2026-10-30T19:56:08Z
type: legacy
api_base_url: "https://auth.roblox.com"
versions: [v3, v2, v1]
endpoints: 95
auth: [cookie]
---

# Authentication Api v3

> **Warning:** Legacy APIs with cookie authentication can incorporate breaking changes without notice. We don't recommend them for production applications.

**Base URL:** `https://auth.roblox.com`
**Versions:** v3, v2, v1

## V3

### POST `/v3/logout`

Destroys the current authentication session while reporting metrics like url and reason for logout.

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

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
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

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer (int64)` | Yes | The user ID to authenticate as. |

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

### Roblox.Authentication.Api.Models.AccountLinkParameters

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `LinkingPlatform` | `integer enum (11 values)` | No | ['Invalid' = 0, 'Xbox' = 1, 'Qq' = 2, 'WeChat' = 3, 'Facebook' = 4, 'RobloxDeveloper' = 5, 'RobloxGroupCreator' = 6, 'Playstation' = 7, 'ExternalProvider' = 8, 'Steam' = 9, 'Example' = 999] Values: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 999 |

### Roblox.Authentication.Api.Models.Request.LogoutV3Request

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `logoutReason` | `string` | No |  |
| `url` | `string` | No |  |
| `userId` | `string` | No |  |

### Roblox.Authentication.Api.Models.Request.SecureAuthenticationIntentModel

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `clientPublicKey` | `string` | No |  |
| `clientEpochTimestamp` | `integer` | No |  |
| `saiSignature` | `string` | No |  |
| `serverNonce` | `string` | No |  |

### Roblox.Authentication.Api.Models.TwoStepVerificationV3LoginResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `identityVerificationLoginTicket` | `string` | No |  |
| `accountBlob` | `string` | No |  |

### Roblox.Authentication.Api.TwoStepVerificationLoginRequest

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `challengeId` | `string` | No |  |
| `verificationToken` | `string` | No |  |
| `rememberDevice` | `boolean` | No |  |
| `secureAuthenticationIntent` | `Roblox.Authentication.Api.Models.Request.SecureAuthenticationIntentModel` | No |  |
| `accountBlob` | `string` | No |  |
| `accountLinkParameters` | `Roblox.Authentication.Api.Models.AccountLinkParameters` | No |  |

## V2

### GET `/v2/auth/metadata`

Gets Auth meta data

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

### GET `/v2/metadata`

Get the metadata

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
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://auth.roblox.com/v2/passwords/current-status"
```

### GET `/v2/passwords/reset`

Gets metadata needed for the password reset view.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `TargetType` | query | `integer (int32)` | Yes | Valid values: `0`, `1`, `2` |
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

- `200`: OK → `Roblox.Authentication.Api.Models.LoginResponse`
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
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
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

### GET `/v2/passwords/validate`

Endpoint for checking if a password is valid.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `Username` | query | `string` | Yes |  |
| `Password` | query | `string` | Yes |  |

**Responses:**

- `200`: OK → `Roblox.Authentication.Api.Models.PasswordValidationResponse`
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

- `200`: OK → `Roblox.Authentication.Api.Models.PasswordValidationResponse`
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

### GET `/v2/recovery/metadata`

Get metadata for forgot endpoints

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

### GET `/v2/username/change/price`

Get the current price for a username change

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
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://auth.roblox.com/v2/username/change/price"
```

### GET `/v2/usernames`

Gets a list of existing usernames on Roblox based on the query parameters

This endpoint can be expanded in the future to include other query parameters such as "startsWith"

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
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://auth.roblox.com/v2/usernames?username={VALUE}"
```

### GET `/v2/usernames/validate`

Checks if a username is valid.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `Username` | query | `string` | Yes |  |
| `Birthday` | query | `string (date-time)` | Yes |  |
| `Context` | query | `integer (int32)` | Yes | Valid values: `0`, `1`, `2` |

**Responses:**

- `200`: OK → `Roblox.Authentication.Api.Models.UsernameValidationResponse`
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
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://auth.roblox.com/v2/usernames/validate?Username={VALUE}&Birthday={VALUE}&Context={VALUE}"
```

### POST `/v2/usernames/validate`

Checks if a username is valid.

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

- `200`: OK → `Roblox.Authentication.Api.Models.UsernameValidationResponse`
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
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://auth.roblox.com/v2/usernames/validate" \
  -H "Content-Type: application/json" \
  -d '{
  "username": "string",
  "birthday": "2024-01-01T00:00:00Z",
  "context": 0
}'
```

### POST `/v2/identity-verification/login`

Endpoint for login with identity verification

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

- `200`: OK → `Roblox.Authentication.Api.Models.LoginResponse`
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
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
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

- `200`: OK → `Roblox.Authentication.Api.Models.LoginResponse`
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

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://auth.roblox.com/v2/logout"
```

### POST `/v2/logoutfromallsessionsandreauthenticate`

Logs out user from all other sessions.

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
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
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

### POST `/v2/passwords/reset/send`

Sends a password reset email or challenge to the specified target.

Phone target must be a csv with 3 values: "internationalPrefixNumber,nationalNumber,countryCode"

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

- `200`: OK → `Roblox.Authentication.Api.Models.SendResetPasswordResponse`
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
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
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

- `200`: OK → `Roblox.Authentication.Api.Models.PasswordResetVerificationResponse`
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

### POST `/v2/revert/invalidate-tickets`

Invalidates all account security tickets for the authenticated user.
This endpoint should be called before enrolling in EPP to ensure old revert links cannot be used.

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed
- `503`: 1: This feature is disabled

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://auth.roblox.com/v2/revert/invalidate-tickets"
```

### POST `/v2/session/refresh`

Logs out user from the current session and create a new one.

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://auth.roblox.com/v2/session/refresh"
```

### POST `/v2/signup`

Endpoint for signing up a new user

**Request Body:** `application/json` — Type: `Roblox.Authentication.Api.Models.SignupRequest`

See [Roblox.Authentication.Api.Models.SignupRequest](#roblox-authentication-api-models-signuprequest) in Models.

**Request example:**
```json
{
  "username": "string",
  "password": "string",
  "gender": 1,
  "birthday": "2024-01-01T00:00:00Z",
  "displayName": "string",
  "isTosAgreementBoxChecked": false
}
```

**Responses:**

- `200`: OK → `Roblox.Authentication.Api.Models.SignupResponse`
- `400`: Bad request 16: User agreement ids are null. 21: Empty account switch blob required
- `403`: 0: Token Validation Failed 2: Captcha Failed. 4: Invalid Birthday. 5: Invalid Username. 6: Username already taken. 7: Invalid Password. 8: Password and Username are same. 9: Password is too simple. 10: Email is invalid. 11: Asset is invalid. 12: Too many attempts. Please wait a bit. 17: One time Passcode session was not valid 22: Maximum logged in accounts limit reached. 36: Password is not complex enough. 37: Password is too similar to username. 44: Login is unavailable in your country.
- `429`: 3: Too many attempts. Please wait a bit.
- `500`: Internal server error 15: Insert acceptances failed. 27: Pre-auth passkey registration failed
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
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://auth.roblox.com/v2/signup" \
  -H "Content-Type: application/json" \
  -d '{
  "username": "string",
  "password": "string",
  "gender": 1,
  "birthday": "2024-01-01T00:00:00Z",
  "displayName": "string",
  "isTosAgreementBoxChecked": false
}'
```

### POST `/v2/signup/linked`

Endpoint for signing up a new user through linked authentication.

**Request Body:** `application/json` — Type: `Roblox.Authentication.Api.Models.SignupRequest`

See [Roblox.Authentication.Api.Models.SignupRequest](#roblox-authentication-api-models-signuprequest) in Models.

**Request example:**
```json
{
  "username": "string",
  "password": "string",
  "gender": 1,
  "birthday": "2024-01-01T00:00:00Z",
  "displayName": "string",
  "isTosAgreementBoxChecked": false
}
```

**Responses:**

- `200`: OK → `Roblox.Authentication.Api.Models.SignupResponse`
- `400`: Bad request 16: User agreement ids are null. 21: Empty account switch blob required
- `403`: 0: Token Validation Failed 2: Captcha Failed. 4: Invalid Birthday. 5: Invalid Username. 6: Username already taken. 7: Invalid Password. 8: Password and Username are same. 9: Password is too simple. 10: Email is invalid. 11: Asset is invalid. 12: Too many attempts. Please wait a bit. 17: One time Passcode session was not valid 22: Maximum logged in accounts limit reached. 29: Account Linking already exists on this account 30: Account Linking required but failed 36: Password is not complex enough. 37: Password is too similar to username. 44: Login is unavailable in your country.
- `429`: 3: Too many attempts. Please wait a bit.
- `500`: Internal server error 15: Insert acceptances failed. 27: Pre-auth passkey registration failed 30: Account Linking required but failed
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
  -d '{
  "username": "string",
  "password": "string",
  "gender": 1,
  "birthday": "2024-01-01T00:00:00Z",
  "displayName": "string",
  "isTosAgreementBoxChecked": false
}'
```

### POST `/v2/user/passwords/change`

Changes the password for the authenticated user.

The current password is needed for verification that the password can be changed.

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

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: Roblox.Web.Authentication.Passwords.PasswordResponseCodes.InvalidCurrentPassword             OR             Roblox.Web.Authentication.Passwords.PasswordResponseCodes.InvalidPassword             OR             Roblox.Web.Authentication.Passwords.PasswordResponseCodes.PasswordLowComplexity             OR             Roblox.Web.Authentication.Passwords.PasswordResponseCodes.PasswordTooSimilarToUsername
- `401`: 0: Authorization has been denied for this request.
- `403`: Roblox.Web.Authentication.Passwords.PasswordResponseCodes.PinLocked 0: Token Validation Failed
- `429`: Roblox.Web.Authentication.Passwords.PasswordResponseCodes.Flooded

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `429`: Retry with exponential backoff (start at 1s). `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
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
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://auth.roblox.com/v2/username" \
  -H "Content-Type: application/json" \
  -d '{
  "username": "string",
  "password": "string"
}'
```

### POST `/v2/usernames/recover`

Sends an email of all accounts belonging to an email

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

## Models

### Roblox.Authentication.Api.Models.AccountLinkParameters

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `LinkingPlatform` | `integer enum (11 values)` | No | ['Invalid' = 0, 'Xbox' = 1, 'Qq' = 2, 'WeChat' = 3, 'Facebook' = 4, 'RobloxDeveloper' = 5, 'RobloxGroupCreator' = 6, 'Playstation' = 7, 'ExternalProvider' = 8, 'Steam' = 9, 'Example' = 999] Values: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 999 |

### Roblox.Authentication.Api.Models.AuthMetaDataResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `cookieLawNoticeTimeout` | `integer` | No |  |

### Roblox.Authentication.Api.Models.ForgotPasswordUserResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `user` | `Roblox.Web.Responses.Users.LegacyUserResponse` | No |  |
| `ticket` | `string` | No |  |

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

### Roblox.Authentication.Api.Models.PasswordChangeModel

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `currentPassword` | `string` | No |  |
| `newPassword` | `string` | No |  |
| `secureAuthenticationIntent` | `Roblox.Authentication.Api.Models.Request.SecureAuthenticationIntentModel` | No |  |

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

### Roblox.Authentication.Api.Models.PasswordStatusResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `valid` | `boolean` | No |  |

### Roblox.Authentication.Api.Models.PasswordValidationModel

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `username` | `string` | No |  |
| `password` | `string` | No |  |

### Roblox.Authentication.Api.Models.PasswordValidationResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `code` | `integer enum (8 values)` | No | ['ValidPassword' = 0, 'WeakPasswordError' = 1, 'PasswordLengthError' = 2, 'PasswordSameAsUsernameError' = 3, 'ForbiddenPasswordError' = 4, 'DumbStringsError' = 5, 'PasswordLowComplexityError' = 6, 'PasswordTooSimilarToUsernameError' = 7] Values: 0, 1, 2, 3, 4, 5, 6, 7 |
| `message` | `string` | No |  |

### Roblox.Authentication.Api.Models.RecoverUsernameRequest

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `targetType` | `0 \| 1 \| 2` | No | ['Email' = 0, 'PhoneNumber' = 1, 'RecoverySessionID' = 2] |
| `target` | `string` | No |  |

### Roblox.Authentication.Api.Models.RecoverUsernameResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `transmissionType` | `0 \| 1` | No |  |

### Roblox.Authentication.Api.Models.RecoveryMetadataResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `isOnPhone` | `boolean` | No |  |
| `codeLength` | `integer` | No |  |
| `isPhoneFeatureEnabledForUsername` | `boolean` | No |  |
| `isPhoneFeatureEnabledForPassword` | `boolean` | No |  |
| `isBedev2CaptchaEnabledForPasswordReset` | `boolean` | No |  |
| `isUsernameRecoveryDeprecated` | `boolean` | No |  |

### Roblox.Authentication.Api.Models.ReferralDataModel

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `acquisitionTime` | `string` | No |  |
| `acquisitionReferrer` | `string` | No |  |
| `medium` | `string` | No |  |
| `source` | `string` | No |  |
| `campaign` | `string` | No |  |
| `adGroup` | `string` | No |  |
| `keyword` | `string` | No |  |
| `matchType` | `string` | No |  |
| `sendInfo` | `boolean` | No |  |
| `requestSessionId` | `string` | No |  |
| `offerId` | `string` | No |  |

### Roblox.Authentication.Api.Models.Request.AuditContentValue

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `translationKey` | `string` | No |  |
| `translationNamespace` | `string` | No |  |
| `translatedSourceString` | `string` | No |  |
| `parameters` | `object` | No |  |

### Roblox.Authentication.Api.Models.Request.AuditSystemContent

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `capturedAuditContent` | `object` | No |  |
| `additionalAuditContent` | `object` | No |  |

### Roblox.Authentication.Api.Models.Request.IdentityVerificationLoginRequest

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `loginTicket` | `string` | No |  |
| `resultToken` | `string` | No |  |

### Roblox.Authentication.Api.Models.Request.LogoutFromAllSessionsAndReauthenticateRequest

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `SecureAuthenticationIntent` | `Roblox.Authentication.Api.Models.Request.SecureAuthenticationIntentModel` | No |  |

### Roblox.Authentication.Api.Models.Request.OtpSessionModel

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `otpSessionToken` | `string` | No |  |
| `otpContactType` | `1 \| 2` | No | ['Unset' = 1, 'Email' = 2] |

### Roblox.Authentication.Api.Models.Request.SecureAuthenticationIntentModel

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `clientPublicKey` | `string` | No |  |
| `clientEpochTimestamp` | `integer` | No |  |
| `saiSignature` | `string` | No |  |
| `serverNonce` | `string` | No |  |

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

### Roblox.Authentication.Api.Models.SignupRequest

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `username` | `string` | No |  |
| `password` | `string` | No |  |
| `gender` | `1 \| 2 \| 3` | No | ['Unknown' = 1, 'Male' = 2, 'Female' = 3] |
| `birthday` | `string` | No |  |
| `displayName` | `string` | No |  |
| `isTosAgreementBoxChecked` | `boolean` | No |  |
| `signupType` | `0 \| 1` | No | ['Regular' = 0, 'Express' = 1] |
| `email` | `string` | No |  |
| `locale` | `string` | No |  |
| `assetIds` | `integer[]` | No |  |
| `bodyColorId` | `integer` | No |  |
| `bodyTypeScale` | `number` | No |  |
| `headScale` | `number` | No |  |
| `heightScale` | `number` | No |  |
| `widthScale` | `number` | No |  |
| `proportionScale` | `number` | No |  |
| `referralData` | `Roblox.Authentication.Api.Models.ReferralDataModel` | No |  |
| `agreementIds` | `string[]` | No |  |
| `identityVerificationResultToken` | `string` | No |  |
| `secureAuthenticationIntent` | `Roblox.Authentication.Api.Models.Request.SecureAuthenticationIntentModel` | No |  |
| `otpSession` | `Roblox.Authentication.Api.Models.Request.OtpSessionModel` | No |  |
| `dataToken` | `string` | No |  |
| `accountBlob` | `string` | No |  |
| `passkeySessionId` | `string` | No |  |
| `passkeyRegistrationResponse` | `string` | No |  |
| `accountLinkParameters` | `Roblox.Authentication.Api.Models.AccountLinkParameters` | No |  |
| `auditSystemContent` | `Roblox.Authentication.Api.Models.Request.AuditSystemContent` | No |  |
| `captchaId` | `string` | No |  |
| `captchaToken` | `string` | No |  |
| `captchaProvider` | `string` | No |  |
| `challengeId` | `string` | No |  |

### Roblox.Authentication.Api.Models.SignupResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `userId` | `integer` | No |  |
| `starterPlaceId` | `integer` | No |  |
| `returnUrl` | `string` | No |  |
| `accountBlob` | `string` | No |  |

### Roblox.Authentication.Api.Models.TwoStepVerificationSentResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `mediaType` | `integer enum (8 values)` | No | ['Email' = 0, 'SMS' = 1, 'Authenticator' = 2, 'RecoveryCode' = 3, 'SecurityKey' = 4, 'CrossDevice' = 5, 'Password' = 6, 'Passkey' = 7] Values: 0, 1, 2, 3, 4, 5, 6, 7 |
| `ticket` | `string` | No |  |

### Roblox.Authentication.Api.Models.UsernameChangePriceResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `priceInRobux` | `integer` | No |  |
| `basePriceInRobux` | `integer` | No |  |
| `isFreeUsernameChange` | `boolean` | No |  |

### Roblox.Authentication.Api.Models.UsernameChangeRequest

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `username` | `string` | No |  |
| `password` | `string` | No |  |

### Roblox.Authentication.Api.Models.UsernameValidationRequest

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `username` | `string` | No |  |
| `birthday` | `string` | No |  |
| `context` | `0 \| 1 \| 2` | No |  |

### Roblox.Authentication.Api.Models.UsernameValidationResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `code` | `integer enum (10 values)` | No | ['ValidUsername' = 0, 'AlreadyInUseError' = 1, 'ModerationError' = 2, 'InvalidLengthError' = 3, 'StartsOrEndsWithUnderscoreError' = 4, 'TooManyUnderscoresError' = 5, 'ContainsSpacesError' = 6, 'InvalidCharactersError' = 7, 'ContainsPiiError' = 10, 'ContainsReservedUsernameError' = 12] Values: 0, 1, 2, 3, 4, 5, 6, 7, 10, 12 |
| `message` | `string` | No |  |

### Roblox.Authentication.Api.Models.UsernamesResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `usernames` | `string[]` | No |  |

### Roblox.Web.Responses.Users.LegacyUserResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `userId` | `integer` | No |  |
| `username` | `string` | No |  |
| `displayName` | `string` | No |  |

### Roblox.Web.Responses.Users.SkinnyUserResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | `integer` | No |  |
| `name` | `string` | No |  |
| `displayName` | `string` | No |  |

## V1

### GET `/v1/account-creation/metadata`

Get metadata for adding auth methods.

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
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://auth.roblox.com/v1/account/pin"
```

### POST `/v1/account/pin`

Request to create the account pin.

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
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://auth.roblox.com/v1/account/pin" \
  -H "Content-Type: application/json" \
  -d '{
  "pin": "string",
  "reauthenticationToken": "string"
}'
```

### PATCH `/v1/account/pin`

Request made to update the account pin on the account.

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
curl -X PATCH -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://auth.roblox.com/v1/account/pin" \
  -H "Content-Type: application/json" \
  -d '{
  "pin": "string",
  "reauthenticationToken": "string"
}'
```

### DELETE `/v1/account/pin`

Request for deletes the account pin from the account.

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
curl -X DELETE -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://auth.roblox.com/v1/account/pin" \
  -H "Content-Type: application/json" \
  -d '{
  "pin": "string",
  "reauthenticationToken": "string"
}'
```

### GET `/v1/auth/metadata`

Gets Auth meta data

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

### GET `/v1/client-assertion`

Creates a client assertion to be used when generating an auth ticket.

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
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://auth.roblox.com/v1/client-assertion"
```

### GET `/v1/external/{identityProviderId}/sso/oauth/callback`

OAuth callback for identity providers that return the authorization code on a GET redirect (Okta, Google).

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `identityProviderId` | path | `integer (int64)` | Yes |  |
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

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `identityProviderId` | path | `integer (int64)` | Yes |  |

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

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `identityProviderId` | path | `integer (int64)` | Yes | The identity provider to authenticate against. |
| `postAuthenticationIntentId` | query | `string` | Yes | Which post-authentication intent to carry out at the end of the handshake. Optional, and omitting it selects the provider's web redirect. |

**Responses:**

- `302`: Found

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://auth.roblox.com/v1/external/{IDENTITYPROVIDERID}/sso/oauth/init?postAuthenticationIntentId={VALUE}"
```

### GET `/v1/metadata`

Get the metadata

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
  "https://auth.roblox.com/v1/metadata"
```

### GET `/v1/passkey/su-eligibility`

Checks whether the authenticated user is eligible for silent passkey upgrade.
Route and response are intentionally obfuscated ("su-eligibility" = "silent-upgrade-eligibility").

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
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://auth.roblox.com/v1/passkey/su-eligibility"
```

### GET `/v1/passwords/validate`

Endpoint for checking if a password is valid.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `Username` | query | `string` | Yes |  |
| `Password` | query | `string` | Yes |  |

**Responses:**

- `200`: OK → `Roblox.Authentication.Api.Models.PasswordValidationResponse`
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

- `200`: OK → `Roblox.Authentication.Api.Models.PasswordValidationResponse`
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

### GET `/v1/recovery/metadata`

Get metadata for forgot endpoints

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

### GET `/v1/social/connected-providers`

Get social network user information if the given social auth method is connected to current user.

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
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://auth.roblox.com/v1/social/connected-providers"
```

### GET `/v1/username/change/price`

Get the current price for a username change

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
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://auth.roblox.com/v1/username/change/price"
```

### GET `/v1/usernames`

Gets a list of existing usernames on Roblox based on the query parameters

This endpoint can be expanded in the future to include other query parameters such as "startsWith"

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
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://auth.roblox.com/v1/usernames?username={VALUE}"
```

### GET `/v1/usernames/validate`

Checks if a username is valid.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `Username` | query | `string` | Yes |  |
| `Birthday` | query | `string (date-time)` | Yes |  |
| `Context` | query | `integer (int32)` | Yes | Valid values: `0`, `1`, `2` |

**Responses:**

- `200`: OK → `Roblox.Authentication.Api.Models.UsernameValidationResponse`
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
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://auth.roblox.com/v1/usernames/validate?Username={VALUE}&Birthday={VALUE}&Context={VALUE}"
```

### POST `/v1/usernames/validate`

Checks if a username is valid.

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

- `200`: OK → `Roblox.Authentication.Api.Models.UsernameValidationResponse`
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
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://auth.roblox.com/v1/usernames/validate" \
  -H "Content-Type: application/json" \
  -d '{
  "username": "string",
  "birthday": "2024-01-01T00:00:00Z",
  "context": 0
}'
```

### GET `/v1/validators/email`

Tries to check if an email is valid

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

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `DisplayName` | query | `string` | Yes |  |
| `BirthDay` | query | `string (date-time)` | Yes |  |

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

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `Username` | query | `string` | Yes |  |
| `BirthDay` | query | `string (date-time)` | Yes |  |

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
  "https://auth.roblox.com/v1/validators/username?Username={VALUE}&BirthDay={VALUE}"
```

### POST `/v1/validators/username`

Tries to get a valid username if the current username is taken
This is a POST request and explicitly does not receive the parameter values from the query

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
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
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

**Responses:**

- `200`: OK → `Roblox.Authentication.Api.Models.XboxConnectionModel`
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
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://auth.roblox.com/v1/xbox/connection"
```

### GET `/v1/xbox/get-login-consecutive-days`

Get the consecutive days the xbox user has been logged in.

**Responses:**

- `200`: OK → `Roblox.Authentication.Api.Models.XboxLoginConsecutiveDaysResponse`
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
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://auth.roblox.com/v1/xbox/get-login-consecutive-days"
```

### POST `/v1/account/pin/lock`

Request to locks the account which has an account pin enabled.

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
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://auth.roblox.com/v1/account/pin/lock"
```

### POST `/v1/account/pin/unlock`

Requests to unlock the account pin.

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
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://auth.roblox.com/v1/account/pin/unlock" \
  -H "Content-Type: application/json" \
  -d '{
  "pin": "string",
  "reauthenticationToken": "string"
}'
```

### POST `/v1/account/upgrade`

Attaches a sign-in credential to the calling account.

The caller is the account being upgraded, so the request carries no user ID and the
session is the authorization. The call is safe to retry: each field is compared against
the account first, and a field the account already holds is dropped rather than rewritten.

The moderation filter is bypassed because an account held by a birthday compliance
restriction is Suppressed and lifts that restriction through this call. Every upgrade type
still passes its own eligibility gate.

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
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
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

### POST `/v1/external/{identityProviderId}/sso/native/nonce`

Reserves a nonce for a native SSO sign-in attempt.

The web flow gets its nonce from M:Roblox.Authentication.Api.Controllers.V1.ExternalIdentitiesGatewayController.OAuthInit(System.Int64,System.String,System.Threading.CancellationToken), which native clients never call
because they have no authorization redirect. They call this instead, pass the nonce to the
provider SDK, and post the resulting id_token to /access.
            
The client must pass this value to the SDK verbatim. Both providers treat the nonce as an
opaque string and echo it into the id_token unchanged, and redemption looks the value up as
issued. The SHA256(nonce) convention seen in Apple examples belongs to Firebase, which hashes
on its own side before comparing; hashing here would make the lookup miss.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `identityProviderId` | path | `integer (int64)` | Yes |  |

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

### POST `/v1/external/{identityProviderId}/sso/saml/assertion-consumer-service`

SAML Assertion Consumer Service endpoint that external identity provider calls post user authentication.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `identityProviderId` | path | `integer (int64)` | Yes |  |
| `SAMLResponse` | formData | `string` | No |  |
| `RelayState` | formData | `string` | No |  |

**Responses:**

- `302`: Found

**Example:**
```bash
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://auth.roblox.com/v1/external/{IDENTITYPROVIDERID}/sso/saml/assertion-consumer-service"
```

### POST `/v1/external/access`

Signs a user up for Roblox and links the account to the authenticated external provider ID.

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
- `400`: 30: Platform is not supported for SSO login.
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

### POST `/v1/identity-verification/login`

Endpoint for login with identity verification

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

- `200`: OK → `Roblox.Authentication.Api.Models.LoginResponse`
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
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
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

- `200`: OK → `Roblox.Authentication.Api.Models.LoginResponse`
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

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://auth.roblox.com/v1/logout"
```

### POST `/v1/logoutfromallsessionsandreauthenticate`

Logs out user from all other sessions.

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
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
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

### POST `/v1/passkey/DeleteCredentialBatch`

Disables a batch of credentials for the specified user.

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
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
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

### POST `/v1/passkey/finish-ar-preauth-registration`

Finishes account recovery pre-auth passkey registration by validating the recovery session,
deactivating the user's password, and completing passkey registration.

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
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://auth.roblox.com/v1/passkey/finish-preauth-registration" \
  -H "Content-Type: application/json" \
  -d '{
  "sessionId": "string",
  "registrationResponse": "string",
  "source": "string"
}'
```

### POST `/v1/passkey/FinishRegistration`

Complete Passkey registration by providing credential creation options.

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
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
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
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://auth.roblox.com/v1/passkey/ListCredentials" \
  -H "Content-Type: application/json" \
  -d '{
  "all": false
}'
```

### POST `/v1/passkey/RenameCredential`

Rename a credential for the specified user.

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
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://auth.roblox.com/v1/passkey/RenameCredential" \
  -H "Content-Type: application/json" \
  -d '{
  "credentialID": "string",
  "newNickname": "string"
}'
```

### POST `/v1/passkey/start-authentication-by-user`

Initializes passkey authentication for the user(s) corresponding to the identifier provided.

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

### POST `/v1/passkey/StartAuthentication`

Provides a challenge for the Passkey to authenticate.

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
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://auth.roblox.com/v1/passkey/StartRegistration" \
  -H "Content-Type: application/json" \
  -d '{
  "isSilentUpgrade": false
}'
```

### POST `/v1/revert/invalidate-tickets`

Invalidates all account security tickets for the authenticated user.
This endpoint should be called before enrolling in EPP to ensure old revert links cannot be used.

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed
- `503`: 1: This feature is disabled

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://auth.roblox.com/v1/revert/invalidate-tickets"
```

### POST `/v1/session/refresh`

Logs out user from the current session and create a new one.

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://auth.roblox.com/v1/session/refresh"
```

### POST `/v1/signup`

Endpoint for signing up a new user

**Request Body:** `application/json` — Type: `Roblox.Authentication.Api.Models.SignupRequest`

See [Roblox.Authentication.Api.Models.SignupRequest](#roblox-authentication-api-models-signuprequest) in Models.

**Request example:**
```json
{
  "username": "string",
  "password": "string",
  "gender": 1,
  "birthday": "2024-01-01T00:00:00Z",
  "displayName": "string",
  "isTosAgreementBoxChecked": false
}
```

**Responses:**

- `200`: OK → `Roblox.Authentication.Api.Models.SignupResponse`
- `400`: Bad request 16: User agreement ids are null. 21: Empty account switch blob required
- `403`: 0: Token Validation Failed 2: Captcha Failed. 4: Invalid Birthday. 5: Invalid Username. 6: Username already taken. 7: Invalid Password. 8: Password and Username are same. 9: Password is too simple. 10: Email is invalid. 11: Asset is invalid. 12: Too many attempts. Please wait a bit. 17: One time Passcode session was not valid 22: Maximum logged in accounts limit reached. 36: Password is not complex enough. 37: Password is too similar to username. 44: Login is unavailable in your country.
- `429`: 3: Too many attempts. Please wait a bit.
- `500`: Internal server error 15: Insert acceptances failed. 27: Pre-auth passkey registration failed
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
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://auth.roblox.com/v1/signup" \
  -H "Content-Type: application/json" \
  -d '{
  "username": "string",
  "password": "string",
  "gender": 1,
  "birthday": "2024-01-01T00:00:00Z",
  "displayName": "string",
  "isTosAgreementBoxChecked": false
}'
```

### POST `/v1/signup/linked`

Endpoint for signing up a new user through linked authentication.

**Request Body:** `application/json` — Type: `Roblox.Authentication.Api.Models.SignupRequest`

See [Roblox.Authentication.Api.Models.SignupRequest](#roblox-authentication-api-models-signuprequest) in Models.

**Request example:**
```json
{
  "username": "string",
  "password": "string",
  "gender": 1,
  "birthday": "2024-01-01T00:00:00Z",
  "displayName": "string",
  "isTosAgreementBoxChecked": false
}
```

**Responses:**

- `200`: OK → `Roblox.Authentication.Api.Models.SignupResponse`
- `400`: Bad request 16: User agreement ids are null. 21: Empty account switch blob required
- `403`: 0: Token Validation Failed 2: Captcha Failed. 4: Invalid Birthday. 5: Invalid Username. 6: Username already taken. 7: Invalid Password. 8: Password and Username are same. 9: Password is too simple. 10: Email is invalid. 11: Asset is invalid. 12: Too many attempts. Please wait a bit. 17: One time Passcode session was not valid 22: Maximum logged in accounts limit reached. 29: Account Linking already exists on this account 30: Account Linking required but failed 36: Password is not complex enough. 37: Password is too similar to username. 44: Login is unavailable in your country.
- `429`: 3: Too many attempts. Please wait a bit.
- `500`: Internal server error 15: Insert acceptances failed. 27: Pre-auth passkey registration failed 30: Account Linking required but failed
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
  -d '{
  "username": "string",
  "password": "string",
  "gender": 1,
  "birthday": "2024-01-01T00:00:00Z",
  "displayName": "string",
  "isTosAgreementBoxChecked": false
}'
```

### POST `/v1/social/{provider}/disconnect`

Removes the given social authentication method from current Roblox user if it is connected.

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

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: Bad request 2: Unsupported social provider type.
- `401`: 0: Authorization has been denied for this request.
- `403`: Forbidden 0: Token Validation Failed 3: Cannot disconnect the only authentication method. Password on account is required. 4: The password provided is invalid.
- `500`: Internal server error

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://auth.roblox.com/v1/social/{PROVIDER}/disconnect" \
  -H "Content-Type: application/json" \
  -d '{
  "Password": "string"
}'
```

### POST `/v1/user/passwords/change`

Changes the password for the authenticated user.

The current password is needed for verification that the password can be changed.

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

- `200`: OK → `Roblox.Web.WebAPI.ApiEmptyResponseModel`
- `400`: Roblox.Web.Authentication.Passwords.PasswordResponseCodes.InvalidCurrentPassword             OR             Roblox.Web.Authentication.Passwords.PasswordResponseCodes.InvalidPassword             OR             Roblox.Web.Authentication.Passwords.PasswordResponseCodes.PasswordLowComplexity             OR             Roblox.Web.Authentication.Passwords.PasswordResponseCodes.PasswordTooSimilarToUsername
- `401`: 0: Authorization has been denied for this request.
- `403`: Roblox.Web.Authentication.Passwords.PasswordResponseCodes.PinLocked 0: Token Validation Failed
- `429`: Roblox.Web.Authentication.Passwords.PasswordResponseCodes.Flooded

**Response fields** (`Roblox.Web.WebAPI.ApiEmptyResponseModel`)

See [Roblox.Web.WebAPI.ApiEmptyResponseModel](#roblox-web-webapi-apiemptyresponsemodel) in Models.

**Error handling:** `429`: Retry with exponential backoff (start at 1s). `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
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
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://auth.roblox.com/v1/username" \
  -H "Content-Type: application/json" \
  -d '{
  "username": "string",
  "password": "string"
}'
```

### POST `/v1/usernames/recover`

Sends an email of all accounts belonging to an email

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

### POST `/v1/xbox/disconnect`

Unlink the current ROBLOX account from the Xbox live account.

**Responses:**

- `200`: OK → `Roblox.Web.WebAPI.Models.ApiSuccessResponse`
- `401`: 0: Authorization has been denied for this request.
- `403`: Forbidden 0: Token Validation Failed

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
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://auth.roblox.com/v1/xbox/disconnect"
```

### POST `/v1/xbox/translate`

Translate the xbox user to roblox user.

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

- `200`: OK → `Roblox.Authentication.Api.Models.XboxCollectionsOfUserResponse`
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed

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
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://auth.roblox.com/v1/xbox/translate" \
  -H "Content-Type: application/json" \
  -d '{
  "ids": [
    "string"
  ]
}'
```

## Models

### Roblox.Authentication.Api.Models.AccountLinkParameters

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `LinkingPlatform` | `integer enum (11 values)` | No | ['Invalid' = 0, 'Xbox' = 1, 'Qq' = 2, 'WeChat' = 3, 'Facebook' = 4, 'RobloxDeveloper' = 5, 'RobloxGroupCreator' = 6, 'Playstation' = 7, 'ExternalProvider' = 8, 'Steam' = 9, 'Example' = 999] Values: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 999 |

### Roblox.Authentication.Api.Models.AccountPinRequest

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `pin` | `string` | No |  |
| `reauthenticationToken` | `string` | No |  |

### Roblox.Authentication.Api.Models.AccountPinResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `unlockedUntil` | `number` | No |  |

### Roblox.Authentication.Api.Models.AccountPinStatusResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `isEnabled` | `boolean` | No |  |
| `unlockedUntil` | `number` | No |  |

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

### Roblox.Authentication.Api.Models.AuthMetaDataResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `cookieLawNoticeTimeout` | `integer` | No |  |

### Roblox.Authentication.Api.Models.AuthMethodsMetadataResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `isEligibleForALSignup` | `boolean` | No |  |

### Roblox.Authentication.Api.Models.EmailValidationResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `isEmailValid` | `boolean` | No |  |

### Roblox.Authentication.Api.Models.LoginMethodModel

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `method` | `0 \| 1 \| 2` | No | ['EmailOtp' = 0, 'Passkey' = 1, 'Password' = 2] |
| `priority` | `integer` | No |  |

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

### Roblox.Authentication.Api.Models.PasswordChangeModel

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `currentPassword` | `string` | No |  |
| `newPassword` | `string` | No |  |
| `secureAuthenticationIntent` | `Roblox.Authentication.Api.Models.Request.SecureAuthenticationIntentModel` | No |  |

### Roblox.Authentication.Api.Models.PasswordValidationModel

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `username` | `string` | No |  |
| `password` | `string` | No |  |

### Roblox.Authentication.Api.Models.PasswordValidationResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `code` | `integer enum (8 values)` | No | ['ValidPassword' = 0, 'WeakPasswordError' = 1, 'PasswordLengthError' = 2, 'PasswordSameAsUsernameError' = 3, 'ForbiddenPasswordError' = 4, 'DumbStringsError' = 5, 'PasswordLowComplexityError' = 6, 'PasswordTooSimilarToUsernameError' = 7] Values: 0, 1, 2, 3, 4, 5, 6, 7 |
| `message` | `string` | No |  |

### Roblox.Authentication.Api.Models.ProviderInfoModel

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `provider` | `string` | No |  |
| `identifier` | `string` | No |  |

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

### Roblox.Authentication.Api.Models.RecommendedUsernameResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `didGenerateNewUsername` | `boolean` | No |  |
| `suggestedUsernames` | `string[]` | No |  |

### Roblox.Authentication.Api.Models.RecoverUsernameRequest

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `targetType` | `0 \| 1 \| 2` | No | ['Email' = 0, 'PhoneNumber' = 1, 'RecoverySessionID' = 2] |
| `target` | `string` | No |  |

### Roblox.Authentication.Api.Models.RecoverUsernameResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `transmissionType` | `0 \| 1` | No |  |

### Roblox.Authentication.Api.Models.RecoveryMetadataResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `isOnPhone` | `boolean` | No |  |
| `codeLength` | `integer` | No |  |
| `isPhoneFeatureEnabledForUsername` | `boolean` | No |  |
| `isPhoneFeatureEnabledForPassword` | `boolean` | No |  |
| `isBedev2CaptchaEnabledForPasswordReset` | `boolean` | No |  |
| `isUsernameRecoveryDeprecated` | `boolean` | No |  |

### Roblox.Authentication.Api.Models.ReferralDataModel

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `acquisitionTime` | `string` | No |  |
| `acquisitionReferrer` | `string` | No |  |
| `medium` | `string` | No |  |
| `source` | `string` | No |  |
| `campaign` | `string` | No |  |
| `adGroup` | `string` | No |  |
| `keyword` | `string` | No |  |
| `matchType` | `string` | No |  |
| `sendInfo` | `boolean` | No |  |
| `requestSessionId` | `string` | No |  |
| `offerId` | `string` | No |  |

### Roblox.Authentication.Api.Models.Request.AuditContentValue

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `translationKey` | `string` | No |  |
| `translationNamespace` | `string` | No |  |
| `translatedSourceString` | `string` | No |  |
| `parameters` | `object` | No |  |

### Roblox.Authentication.Api.Models.Request.AuditSystemContent

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `capturedAuditContent` | `object` | No |  |
| `additionalAuditContent` | `object` | No |  |

### Roblox.Authentication.Api.Models.Request.DeletePasskeysRequest

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `credentialIDs` | `string[]` | No |  |
| `credentialNicknames` | `string[]` | No |  |

### Roblox.Authentication.Api.Models.Request.ExternalAccessRequest

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `authenticationProof` | `string` | No |  |
| `identityProviderPlatformType` | `integer enum (8 values)` | No | ['Undefined' = 0, 'Xbox' = 1, 'Playstation' = 2, 'Web' = 3, 'Steam' = 4, 'Android' = 5, 'Ios' = 6, 'MacOs' = 7] Values: 0, 1, 2, 3, 4, 5, 6, 7 |
| `postAuthenticationIntentId` | `string` | No |  |
| `additionalInfoPayload` | `object` | No |  |

### Roblox.Authentication.Api.Models.Request.ExternalLoginAndLinkRequest

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `ctype` | `integer enum (11 values)` | No | ['Email' = 0, 'Username' = 1, 'PhoneNumber' = 2, 'EmailOtpSessionToken' = 3, 'AuthToken' = 4, 'Passkey' = 5, 'AsUser' = 6, 'TwoStepVerification' = 7, 'XboxLive' = 8, 'PlatformLive' = 9, 'MagicLink' = 10] Values: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 |
| `cvalue` | `string` | No |  |
| `password` | `string` | No |  |
| `authenticationProof` | `string` | No |  |
| `IdentityProviderPlatformType` | `integer enum (8 values)` | No | ['Undefined' = 0, 'Xbox' = 1, 'Playstation' = 2, 'Web' = 3, 'Steam' = 4, 'Android' = 5, 'Ios' = 6, 'MacOs' = 7] Values: 0, 1, 2, 3, 4, 5, 6, 7 |
| `additionalInfoPayload` | `object` | No |  |

### Roblox.Authentication.Api.Models.Request.ExternalLoginRequest

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `identityProvider` | `integer enum (11 values)` | No |  Values: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 999 |
| `additionalData` | `object` | No |  |
| `authenticationProof` | `string` | No |  |

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

### Roblox.Authentication.Api.Models.Request.FinishPasskeyRegistrationRequest

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `sessionId` | `string` | No |  |
| `credentialNickname` | `string` | No |  |
| `attestationResponse` | `string` | No |  |
| `source` | `string` | No |  |

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

### Roblox.Authentication.Api.Models.Request.ListPasskeysRequest

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `all` | `boolean` | No |  |

### Roblox.Authentication.Api.Models.Request.LogoutFromAllSessionsAndReauthenticateRequest

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `SecureAuthenticationIntent` | `Roblox.Authentication.Api.Models.Request.SecureAuthenticationIntentModel` | No |  |

### Roblox.Authentication.Api.Models.Request.OtpSessionModel

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `otpSessionToken` | `string` | No |  |
| `otpContactType` | `1 \| 2` | No | ['Unset' = 1, 'Email' = 2] |

### Roblox.Authentication.Api.Models.Request.RenamePasskeyRequest

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `credentialID` | `string` | No |  |
| `newNickname` | `string` | No |  |

### Roblox.Authentication.Api.Models.Request.SecureAuthenticationIntentModel

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `clientPublicKey` | `string` | No |  |
| `clientEpochTimestamp` | `integer` | No |  |
| `saiSignature` | `string` | No |  |
| `serverNonce` | `string` | No |  |

### Roblox.Authentication.Api.Models.Request.StartAuthenticationByUserRequest

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `ctype` | `integer enum (11 values)` | Yes |  Values: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 |
| `cvalue` | `string` | Yes |  |

### Roblox.Authentication.Api.Models.Request.StartPasskeyPreauthRegistrationRequest

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `username` | `string` | No |  |

### Roblox.Authentication.Api.Models.Request.StartPasskeyRegistrationRequest

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `isSilentUpgrade` | `boolean` | No |  |

### Roblox.Authentication.Api.Models.Response.ExternalIdentityGateway.ExternalIdentityAccessResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `placeId` | `integer` | No |  |
| `isolationContext` | `string` | No |  |
| `launchData` | `string` | No |  |

### Roblox.Authentication.Api.Models.Response.ExternalIdentityGateway.ExternalIdentityNonceResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `nonce` | `string` | No |  |

### Roblox.Authentication.Api.Models.Response.ExternalIdentityGateway.ExternalLoginResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | `boolean` | No |  |

### Roblox.Authentication.Api.Models.Response.GetClientAssertionResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `clientAssertion` | `string` | No |  |

### Roblox.Authentication.Api.Models.Response.InitializeLoginResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `loginMethods` | `Roblox.Authentication.Api.Models.LoginMethodModel[]` | No |  |

### Roblox.Authentication.Api.Models.Response.ListPasskeyCredentialResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `credentials` | `Roblox.Authentication.Api.Models.Response.PasskeyCredential[]` | No |  |

### Roblox.Authentication.Api.Models.Response.PasskeyCredential

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `nickname` | `string` | No |  |
| `credentialID` | `string` | No |  |

### Roblox.Authentication.Api.Models.Response.SilentUpgradeEligibilityResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `suEligibility` | `boolean` | No |  |

### Roblox.Authentication.Api.Models.Response.StartAuthenticationByUserResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `authenticationOptions` | `string` | No |  |
| `sessionId` | `string` | No |  |

### Roblox.Authentication.Api.Models.Response.StartAuthenticationResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `authenticationOptions` | `string` | No |  |
| `sessionId` | `string` | No |  |

### Roblox.Authentication.Api.Models.Response.StartPasskeyPreauthRegistrationResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `creationOptions` | `string` | No |  |
| `sessionId` | `string` | No |  |

### Roblox.Authentication.Api.Models.Response.StartPasskeyRegistrationResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `creationOptions` | `string` | No |  |
| `sessionId` | `string` | No |  |

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

### Roblox.Authentication.Api.Models.SignupRequest

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `username` | `string` | No |  |
| `password` | `string` | No |  |
| `gender` | `1 \| 2 \| 3` | No | ['Unknown' = 1, 'Male' = 2, 'Female' = 3] |
| `birthday` | `string` | No |  |
| `displayName` | `string` | No |  |
| `isTosAgreementBoxChecked` | `boolean` | No |  |
| `signupType` | `0 \| 1` | No | ['Regular' = 0, 'Express' = 1] |
| `email` | `string` | No |  |
| `locale` | `string` | No |  |
| `assetIds` | `integer[]` | No |  |
| `bodyColorId` | `integer` | No |  |
| `bodyTypeScale` | `number` | No |  |
| `headScale` | `number` | No |  |
| `heightScale` | `number` | No |  |
| `widthScale` | `number` | No |  |
| `proportionScale` | `number` | No |  |
| `referralData` | `Roblox.Authentication.Api.Models.ReferralDataModel` | No |  |
| `agreementIds` | `string[]` | No |  |
| `identityVerificationResultToken` | `string` | No |  |
| `secureAuthenticationIntent` | `Roblox.Authentication.Api.Models.Request.SecureAuthenticationIntentModel` | No |  |
| `otpSession` | `Roblox.Authentication.Api.Models.Request.OtpSessionModel` | No |  |
| `dataToken` | `string` | No |  |
| `accountBlob` | `string` | No |  |
| `passkeySessionId` | `string` | No |  |
| `passkeyRegistrationResponse` | `string` | No |  |
| `accountLinkParameters` | `Roblox.Authentication.Api.Models.AccountLinkParameters` | No |  |
| `auditSystemContent` | `Roblox.Authentication.Api.Models.Request.AuditSystemContent` | No |  |
| `captchaId` | `string` | No |  |
| `captchaToken` | `string` | No |  |
| `captchaProvider` | `string` | No |  |
| `challengeId` | `string` | No |  |

### Roblox.Authentication.Api.Models.SignupResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `userId` | `integer` | No |  |
| `starterPlaceId` | `integer` | No |  |
| `returnUrl` | `string` | No |  |
| `accountBlob` | `string` | No |  |

### Roblox.Authentication.Api.Models.SocialAuthenticationDisconnectRequest

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `Password` | `string` | No |  |

### Roblox.Authentication.Api.Models.SocialProvidersResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `providers` | `Roblox.Authentication.Api.Models.ProviderInfoModel[]` | No |  |

### Roblox.Authentication.Api.Models.TwoStepVerificationSentResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `mediaType` | `integer enum (8 values)` | No | ['Email' = 0, 'SMS' = 1, 'Authenticator' = 2, 'RecoveryCode' = 3, 'SecurityKey' = 4, 'CrossDevice' = 5, 'Password' = 6, 'Passkey' = 7] Values: 0, 1, 2, 3, 4, 5, 6, 7 |
| `ticket` | `string` | No |  |

### Roblox.Authentication.Api.Models.UsernameChangePriceResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `priceInRobux` | `integer` | No |  |
| `basePriceInRobux` | `integer` | No |  |
| `isFreeUsernameChange` | `boolean` | No |  |

### Roblox.Authentication.Api.Models.UsernameChangeRequest

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `username` | `string` | No |  |
| `password` | `string` | No |  |

### Roblox.Authentication.Api.Models.UsernameValidationRequest

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `username` | `string` | No |  |
| `birthday` | `string` | No |  |
| `context` | `0 \| 1 \| 2` | No |  |

### Roblox.Authentication.Api.Models.UsernameValidationResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `code` | `integer enum (10 values)` | No | ['ValidUsername' = 0, 'AlreadyInUseError' = 1, 'ModerationError' = 2, 'InvalidLengthError' = 3, 'StartsOrEndsWithUnderscoreError' = 4, 'TooManyUnderscoresError' = 5, 'ContainsSpacesError' = 6, 'InvalidCharactersError' = 7, 'ContainsPiiError' = 10, 'ContainsReservedUsernameError' = 12] Values: 0, 1, 2, 3, 4, 5, 6, 7, 10, 12 |
| `message` | `string` | No |  |

### Roblox.Authentication.Api.Models.UsernamesResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `usernames` | `string[]` | No |  |

### Roblox.Authentication.Api.Models.XboxCollectionsOfUserResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `Users` | `Roblox.Authentication.Api.Models.XboxUserModel[]` | No |  |

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

### Roblox.Authentication.Api.Models.XboxUserModel

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `Id` | `string` | No |  |
| `UserId` | `integer` | No |  |
| `Username` | `string` | No |  |

### Roblox.Web.Responses.Users.SkinnyUserResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | `integer` | No |  |
| `name` | `string` | No |  |
| `displayName` | `string` | No |  |

### Roblox.Web.WebAPI.Models.ApiSuccessResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `success` | `boolean` | No |  |