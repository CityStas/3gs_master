---
name: "Account Information Api v1"
last_updated: 2026-10-30T19:56:08Z
type: legacy
api_base_url: "https://accountinformation.roblox.com"
versions: [v1]
endpoints: 16
auth: [cookie]
---

# Account Information Api v1

> **Warning:** Legacy APIs with cookie authentication can incorporate breaking changes without notice. We don't recommend them for production applications.

**Base URL:** `https://accountinformation.roblox.com`
**Versions:** v1

## Endpoints

### GET `/v1/birthdate` *(deprecated)*

Get the user's birthdate

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
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://accountinformation.roblox.com/v1/birthdate"
```

### GET `/v1/description` *(deprecated)*

Get the user's description

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
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://accountinformation.roblox.com/v1/description"
```

### POST `/v1/description` *(deprecated)*

Update the user's description

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
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://accountinformation.roblox.com/v1/description" \
  -H "Content-Type: application/json" \
  -d '{
  "description": "string"
}'
```

### GET `/v1/gender` *(deprecated)*

Get the user's gender

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
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://accountinformation.roblox.com/v1/gender"
```

### POST `/v1/gender` *(deprecated)*

Update the user's gender

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
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://accountinformation.roblox.com/v1/gender" \
  -H "Content-Type: application/json" \
  -d '{
  "gender": "string"
}'
```

### GET `/v1/metadata`

Get the metadata

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
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://accountinformation.roblox.com/v1/metadata"
```

### GET `/v1/phone`

Get Verified Phone Number

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
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://accountinformation.roblox.com/v1/phone"
```

### POST `/v1/phone`

Set Phone Number

**Request Body:** `application/json` — Type: `Roblox.AccountInformation.Api.Models.PhoneRequest`

See [Roblox.AccountInformation.Api.Models.PhoneRequest](#roblox-accountinformation-api-models-phonerequest) in Models.

**Request example:**
```json
{
  "countryCode": "string",
  "prefix": "string",
  "phone": "string",
  "password": "string",
  "verificationChannel": "string"
}
```

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
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://accountinformation.roblox.com/v1/phone" \
  -H "Content-Type: application/json" \
  -d '{
  "countryCode": "string",
  "prefix": "string",
  "phone": "string",
  "password": "string",
  "verificationChannel": "string"
}'
```

### GET `/v1/promotion-channels`

Get the user's promotion channels

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
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://accountinformation.roblox.com/v1/promotion-channels"
```

### POST `/v1/promotion-channels`

Update the user's promotion channels

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
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
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

### GET `/v1/users/{userId}/promotion-channels`

Get promotion channels for a given user ID

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer (int64)` | Yes | The ID of the user to fetch the promotion channels for. |
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
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://accountinformation.roblox.com/v1/users/{USERID}/promotion-channels"
```

### GET `/v1/users/{userId}/roblox-badges`

Returns a list of Roblox badges belonging to a user.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `userId` | path | `integer (int64)` | Yes |  |

**Responses:**

- `200`: OK → `Roblox.AccountInformation.Api.RobloxBadgeResponse[]`

**Response fields** (`Roblox.AccountInformation.Api.RobloxBadgeResponse[]`)

See [Roblox.AccountInformation.Api.RobloxBadgeResponse](#roblox-accountinformation-api-robloxbadgeresponse) in Models.

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://accountinformation.roblox.com/v1/users/{USERID}/roblox-badges"
```

### POST `/v1/email/verify`

Verify the user's email address from token

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
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://accountinformation.roblox.com/v1/email/verify" \
  -H "Content-Type: application/json" \
  -d '{
  "ticket": "string"
}'
```

### POST `/v1/phone/delete`

Delete Phone

**Request Body:** `application/json` — Type: `Roblox.AccountInformation.Api.Models.PhoneRequest`

See [Roblox.AccountInformation.Api.Models.PhoneRequest](#roblox-accountinformation-api-models-phonerequest) in Models.

**Request example:**
```json
{
  "countryCode": "string",
  "prefix": "string",
  "phone": "string",
  "password": "string",
  "verificationChannel": "string"
}
```

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
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://accountinformation.roblox.com/v1/phone/delete" \
  -H "Content-Type: application/json" \
  -d '{
  "countryCode": "string",
  "prefix": "string",
  "phone": "string",
  "password": "string",
  "verificationChannel": "string"
}'
```

### POST `/v1/phone/resend`

Resend Phone code

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
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://accountinformation.roblox.com/v1/phone/resend" \
  -H "Content-Type: application/json" \
  -d '"..."'
```

### POST `/v1/phone/verify`

Verify Phone

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
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://accountinformation.roblox.com/v1/phone/verify" \
  -H "Content-Type: application/json" \
  -d '{
  "code": "string"
}'
```

## Models

### Roblox.AccountInformation.Api.Models.BirthdateResponse

The birthdate response

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `birthMonth` | `integer` | No | The birth month |
| `birthDay` | `integer` | No | The birth day |
| `birthYear` | `integer` | No | The birth year |

### Roblox.AccountInformation.Api.Models.DescriptionRequest

The description request

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `description` | `string` | No | The description |

### Roblox.AccountInformation.Api.Models.DescriptionResponse

The description response

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `description` | `string` | No | The description |

### Roblox.AccountInformation.Api.Models.GenderRequest

The gender request

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `gender` | `string` | No | The gender |

### Roblox.AccountInformation.Api.Models.GenderResponse

The gender response

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `gender` | `integer` | No | The gender |

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

### Roblox.AccountInformation.Api.Models.PhoneRequest

The phone request

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `countryCode` | `string` | No | The country Code |
| `prefix` | `string` | No | The Phone Prefix |
| `phone` | `string` | No | The Phone number |
| `password` | `string` | No | Password |
| `verificationChannel` | `string` | No | Verification Channel |

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

### Roblox.AccountInformation.Api.Models.PromotionChannelsByUserIdResponse

The promotion channels response

| Property | Type | Required | Description |
|----------|------|----------|-------------|
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

### Roblox.AccountInformation.Api.Models.PromotionChannelsResponse

The promotion channels response

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `promotionChannelsVisibilityPrivacy` | `string` | No | The promotion channels visibility privacy level |
| `facebook` | `string` | No | The Facebook channel |
| `twitter` | `string` | No | The Twitter channel |
| `youtube` | `string` | No | The YouTube channel |
| `twitch` | `string` | No | The Twitch channel |

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

### Roblox.AccountInformation.Api.Models.VerifyPhoneRequest

Verify Phone Request

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `code` | `string` | No | Code to verify phone |

### Roblox.AccountInformation.Api.RobloxBadgeResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | `integer` | No | The ID belonging to this Roblox badge. |
| `name` | `string` | No | The name of this Roblox badge. |
| `description` | `string` | No | The description belonging to this Roblox badge. |
| `imageUrl` | `string` | No | The URL corresponding to the image which represents this Roblox badge. |

### Roblox.Platform.UserPhoneNumberVerification.Models.PendingVerificationResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `verificationChannel` | `string` | No |  |
| `data` | `string` | No |  |