---
name: "Notifications Api v2"
last_updated: 2026-10-30T19:56:08Z
type: legacy
api_base_url: "https://notifications.roblox.com"
versions: [v2]
endpoints: 15
auth: [cookie]
---

# Notifications Api v2

> **Warning:** Legacy APIs with cookie authentication can incorporate breaking changes without notice. We don't recommend them for production applications.

**Base URL:** `https://notifications.roblox.com`
**Versions:** v2

## Endpoints

### GET `/v2/push-notifications/chrome-manifest`

Get Chrome Manifest to link GCM project to Chrome Browser

**Responses:**

- `200`: OK → `Roblox.Api.Notifications.Models.ChromeManifestModel`
- `401`: 0: Authorization has been denied for this request.

**Response fields** (`Roblox.Api.Notifications.Models.ChromeManifestModel`)

See [Roblox.Api.Notifications.Models.ChromeManifestModel](#roblox-api-notifications-models-chromemanifestmodel) in Models.

**Response example:**
```json
{
  "name": "string",
  "gcm_sender_id": "string"
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://notifications.roblox.com/v2/push-notifications/chrome-manifest"
```

### GET `/v2/push-notifications/get-current-device-destination`

Gets the current device destination

**Responses:**

- `200`: OK → `Roblox.Api.Notifications.Models.GetCurrentPushDestinationResponseModel`
- `401`: 0: Authorization has been denied for this request.

**Response fields** (`Roblox.Api.Notifications.Models.GetCurrentPushDestinationResponseModel`)

See [Roblox.Api.Notifications.Models.GetCurrentPushDestinationResponseModel](#roblox-api-notifications-models-getcurrentpushdestinationresponsemodel) in Models.

**Response example:**
```json
{
  "destination": {
    "user": {
      "name": "...",
      "userId": "..."
    },
    "name": "string",
    "notificationToken": "string",
    "supportsUpdateNotifications": false,
    "userPushNotificationDestinationId": 0,
    "application": "string"
  },
  "statusMessage": "string"
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://notifications.roblox.com/v2/push-notifications/get-current-device-destination"
```

### GET `/v2/push-notifications/get-destinations`

Gets valid destinations associated with the signed user

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
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://notifications.roblox.com/v2/push-notifications/get-destinations"
```

### GET `/v2/push-notifications/metadata`

Gets the corresponding metadata for the specified notification

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `notificationToken` | query | `string` | Yes | Token for the notification |
| `notificationId` | query | `string (uuid)` | Yes | Id of the specified notification |

**Responses:**

- `200`: OK → `Roblox.Api.Notifications.Models.GetMetadataResponseModel`
- `401`: 0: Authorization has been denied for this request.

**Response fields** (`Roblox.Api.Notifications.Models.GetMetadataResponseModel`)

See [Roblox.Api.Notifications.Models.GetMetadataResponseModel](#roblox-api-notifications-models-getmetadataresponsemodel) in Models.

**Response example:**
```json
{
  "metadata": {
    "notificationId": "string",
    "type": "string",
    "detail": "...",
    "fallbackDelivered": false
  },
  "statusMessage": "string"
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://notifications.roblox.com/v2/push-notifications/metadata?notificationToken={VALUE}&notificationId={VALUE}"
```

### GET `/v2/stream-notifications/get-latest-game-updates`

Get the latest non aggregated Game Updates sent to the logged in user

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeIds` | query | `array` | Yes | List of universe IDs |
| `sinceDateTime` | query | `string (date-time)` | No | For retrieving only updates that created after a time point. |

**Responses:**

- `200`: OK → `Roblox.Api.Notifications.Models.GameUpdateNotificationModel[]`
- `401`: 0: Authorization has been denied for this request.

**Response fields** (`Roblox.Api.Notifications.Models.GameUpdateNotificationModel[]`)

See [Roblox.Api.Notifications.Models.GameUpdateNotificationModel](#roblox-api-notifications-models-gameupdatenotificationmodel) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://notifications.roblox.com/v2/stream-notifications/get-latest-game-updates?universeIds={VALUE}"
```

### GET `/v2/stream-notifications/get-recent`

Gets the recent entries from the notification stream

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `startIndex` | query | `integer (int32)` | No | Index to start the entries from. (Optional : Defaults to 0 which means the most recent entry) |
| `maxRows` | query | `integer (int32)` | No | Number of entries to be returned. (Optional : Defaults to 10 entries) |

**Responses:**

- `200`: OK → `Roblox.Api.Notifications.Models.NotificationStreamEntriesModel[]`
- `401`: 0: Authorization has been denied for this request.

**Response fields** (`Roblox.Api.Notifications.Models.NotificationStreamEntriesModel[]`)

See [Roblox.Api.Notifications.Models.NotificationStreamEntriesModel](#roblox-api-notifications-models-notificationstreamentriesmodel) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://notifications.roblox.com/v2/stream-notifications/get-recent"
```

### GET `/v2/stream-notifications/metadata`

Get Notification Stream metadata.

**Responses:**

- `200`: OK → `Roblox.Api.Notifications.Models.ResponseModels.NotificationStreamMetadataResponse`
- `401`: 0: Authorization has been denied for this request.

**Response fields** (`Roblox.Api.Notifications.Models.ResponseModels.NotificationStreamMetadataResponse`)

See [Roblox.Api.Notifications.Models.ResponseModels.NotificationStreamMetadataResponse](#roblox-api-notifications-models-responsemodels-notificationstreammetadataresponse) in Models.

**Response example:**
```json
{
  "bannerDismissTimeSpan": 0,
  "signalRDisconnectionResponseInMilliseconds": 0,
  "canLaunchGameFromGameUpdate": false
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://notifications.roblox.com/v2/stream-notifications/metadata"
```

### GET `/v2/stream-notifications/unread-count`

Gets the count of unread Notification stream entries

**Responses:**

- `200`: OK → `Roblox.Api.Notifications.Models.UnreadStreamNotificationsModel`
- `401`: 0: Authorization has been denied for this request.

**Response fields** (`Roblox.Api.Notifications.Models.UnreadStreamNotificationsModel`)

See [Roblox.Api.Notifications.Models.UnreadStreamNotificationsModel](#roblox-api-notifications-models-unreadstreamnotificationsmodel) in Models.

**Response example:**
```json
{
  "unreadNotifications": 0,
  "statusMessage": "string"
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Example:**
```bash
curl -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://notifications.roblox.com/v2/stream-notifications/unread-count"
```

### POST `/v2/push-notifications/deregister-all-devices`

De-register all devices to disable push notifications

**Responses:**

- `200`: OK → `Roblox.Api.Notifications.Models.SuccessResponseModel`
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed

**Response fields** (`Roblox.Api.Notifications.Models.SuccessResponseModel`)

See [Roblox.Api.Notifications.Models.SuccessResponseModel](#roblox-api-notifications-models-successresponsemodel) in Models.

**Response example:**
```json
{
  "statusMessage": "string"
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://notifications.roblox.com/v2/push-notifications/deregister-all-devices"
```

### POST `/v2/push-notifications/deregister-current-device`

De-register current device to disable push notifications

**Responses:**

- `200`: OK → `Roblox.Api.Notifications.Models.SuccessResponseModel`
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed

**Response fields** (`Roblox.Api.Notifications.Models.SuccessResponseModel`)

See [Roblox.Api.Notifications.Models.SuccessResponseModel](#roblox-api-notifications-models-successresponsemodel) in Models.

**Response example:**
```json
{
  "statusMessage": "string"
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://notifications.roblox.com/v2/push-notifications/deregister-current-device"
```

### POST `/v2/push-notifications/deregister-current-device-ios-pushkit`

De-register current device to disable pushkit notifications

**Responses:**

- `200`: OK → `Roblox.Api.Notifications.Models.SuccessResponseModel`
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed

**Response fields** (`Roblox.Api.Notifications.Models.SuccessResponseModel`)

See [Roblox.Api.Notifications.Models.SuccessResponseModel](#roblox-api-notifications-models-successresponsemodel) in Models.

**Response example:**
```json
{
  "statusMessage": "string"
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://notifications.roblox.com/v2/push-notifications/deregister-current-device-ios-pushkit"
```

### POST `/v2/push-notifications/register-android-native`

Register Android Native for push notifications

**Request Body:** `application/json` — Type: `Roblox.Api.Notifications.Models.RegisterAndroidRequestModel`

See [Roblox.Api.Notifications.Models.RegisterAndroidRequestModel](#roblox-api-notifications-models-registerandroidrequestmodel) in Models.

**Request example:**
```json
{
  "notificationToken": "string",
  "authorizeForUser": false,
  "oldNotificationToken": "string",
  "deviceName": "string"
}
```

**Responses:**

- `200`: OK → `Roblox.Api.Notifications.Models.RegistrationResponseModel`
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed

**Response fields** (`Roblox.Api.Notifications.Models.RegistrationResponseModel`)

See [Roblox.Api.Notifications.Models.RegistrationResponseModel](#roblox-api-notifications-models-registrationresponsemodel) in Models.

**Response example:**
```json
{
  "registration": {
    "userPushNotificationDestinationId": 0,
    "name": "string",
    "notificationToken": "string",
    "application": "string",
    "platform": "ChromeOnDesktop"
  },
  "statusMessage": "string"
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://notifications.roblox.com/v2/push-notifications/register-android-native" \
  -H "Content-Type: application/json" \
  -d '{
  "notificationToken": "string",
  "authorizeForUser": false,
  "oldNotificationToken": "string",
  "deviceName": "string"
}'
```

### POST `/v2/push-notifications/register-ios-native`

Registers IOS device for push notifications

**Request Body:** `application/json` — Type: `Roblox.Api.Notifications.Models.RegisterIOSNativeRequestModel`

See [Roblox.Api.Notifications.Models.RegisterIOSNativeRequestModel](#roblox-api-notifications-models-registeriosnativerequestmodel) in Models.

**Request example:**
```json
{
  "notificationToken": "string",
  "destinationIdentifier": "string",
  "authorizeForUser": false,
  "oldNotificationToken": "string",
  "deviceName": "string",
  "isProvisional": false
}
```

**Responses:**

- `200`: OK → `Roblox.Api.Notifications.Models.RegistrationResponseModel`
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed

**Response fields** (`Roblox.Api.Notifications.Models.RegistrationResponseModel`)

See [Roblox.Api.Notifications.Models.RegistrationResponseModel](#roblox-api-notifications-models-registrationresponsemodel) in Models.

**Response example:**
```json
{
  "registration": {
    "userPushNotificationDestinationId": 0,
    "name": "string",
    "notificationToken": "string",
    "application": "string",
    "platform": "ChromeOnDesktop"
  },
  "statusMessage": "string"
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://notifications.roblox.com/v2/push-notifications/register-ios-native" \
  -H "Content-Type: application/json" \
  -d '{
  "notificationToken": "string",
  "destinationIdentifier": "string",
  "authorizeForUser": false,
  "oldNotificationToken": "string",
  "deviceName": "string",
  "isProvisional": false
}'
```

### POST `/v2/push-notifications/register-ios-pushkit`

Registers IOS device for pushkit notifications

**Request Body:** `application/json` — Type: `Roblox.Api.Notifications.Models.RegisterIOSPushKitRequestModel`

See [Roblox.Api.Notifications.Models.RegisterIOSPushKitRequestModel](#roblox-api-notifications-models-registeriospushkitrequestmodel) in Models.

**Request example:**
```json
{
  "notificationToken": "string",
  "destinationIdentifier": "string",
  "authorizeForUser": false,
  "oldNotificationToken": "string",
  "deviceName": "string"
}
```

**Responses:**

- `200`: OK → `Roblox.Api.Notifications.Models.RegistrationResponseModel`
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed

**Response fields** (`Roblox.Api.Notifications.Models.RegistrationResponseModel`)

See [Roblox.Api.Notifications.Models.RegistrationResponseModel](#roblox-api-notifications-models-registrationresponsemodel) in Models.

**Response example:**
```json
{
  "registration": {
    "userPushNotificationDestinationId": 0,
    "name": "string",
    "notificationToken": "string",
    "application": "string",
    "platform": "ChromeOnDesktop"
  },
  "statusMessage": "string"
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://notifications.roblox.com/v2/push-notifications/register-ios-pushkit" \
  -H "Content-Type: application/json" \
  -d '{
  "notificationToken": "string",
  "destinationIdentifier": "string",
  "authorizeForUser": false,
  "oldNotificationToken": "string",
  "deviceName": "string"
}'
```

### POST `/v2/stream-notifications/clear-unread`

Clears the unread Notification stream count

**Responses:**

- `200`: OK → `Roblox.Api.Notifications.Models.SuccessResponseModel`
- `401`: 0: Authorization has been denied for this request.
- `403`: 0: Token Validation Failed

**Response fields** (`Roblox.Api.Notifications.Models.SuccessResponseModel`)

See [Roblox.Api.Notifications.Models.SuccessResponseModel](#roblox-api-notifications-models-successresponsemodel) in Models.

**Response example:**
```json
{
  "statusMessage": "string"
}
```

**Error handling:** `401`: Check that your API key/token is valid and not expired. `403`: Verify your API key has the required scopes listed above. 

**Example:**
```bash
curl -X POST -H "Authorization: Bearer $ROBLOX_ACCESS_TOKEN" \
  "https://notifications.roblox.com/v2/stream-notifications/clear-unread"
```

## Models

### Roblox.Api.Notifications.Models.ChromeManifestModel

Chrome Manifest to link GCM project to Chrome browser

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | `string` | No |  |
| `gcm_sender_id` | `string` | No |  |

### Roblox.Api.Notifications.Models.GameUpdateNotificationModel

Model for a game update message to be displayed in notification stream.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `universeId` | `integer` | No | ID of the game. |
| `rootPlaceId` | `integer` | No | ID of the game. |
| `createdOn` | `string` | No | Creation date of the update message. |
| `createdOnKey` | `string` | No | Key of Creation date ticks (dynamo table sort key). |
| `content` | `string` | No | Content of the update message. |
| `universeName` | `string` | No | Name of the game. |

### Roblox.Api.Notifications.Models.GetCurrentPushDestinationResponseModel

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `destination` | `Roblox.Api.Notifications.Models.UserPushDestination` | No |  |
| `statusMessage` | `string` | No | Message for the success response |

### Roblox.Api.Notifications.Models.GetMetadataResponseModel

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `metadata` | `Roblox.Api.Notifications.Models.PushNotificationClientMetadata` | No |  |
| `statusMessage` | `string` | No | Message for the success response |

### Roblox.Api.Notifications.Models.GetPushDestinationsResponseModel

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `destinations` | `Roblox.Api.Notifications.Models.UserPushDestination[]` | No | List of destinations for the user push notification |
| `statusMessage` | `string` | No | Message for the success response |

### Roblox.Api.Notifications.Models.NotificationStreamEntriesModel

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | `string` | No | Id of the notification stream entry |
| `notificationSourceType` | `string enum (15 values)` | No | Type of the notification source ['Test' = 0, 'FriendRequestReceived' = 1, 'FriendRequestAccepted' = 2, 'PartyInviteReceived' = 3, 'PartyMemberJoined' = 4, 'ChatNewMessage' = 5, 'PrivateMessageReceived' = 6, 'UserAddedToPrivateServerWhiteList' = 7, 'ConversationUniverseChanged' = 8, 'TeamCreateInvite' = 9, 'GameUpdate' = 10, 'DeveloperMetricsAvailable' = 11, 'GroupJoinRequestAccepted' = 12, 'Sendr' = 13, 'ExperienceInvitation' = 14] Values: Test, FriendRequestReceived, FriendRequestAccepted, PartyInviteReceived, PartyMemberJoined, ChatNewMessage, PrivateMessageReceived, UserAddedToPrivateServerWhiteList, ConversationUniverseChanged, TeamCreateInvite, GameUpdate, DeveloperMetricsAvailable, GroupJoinRequestAccepted, Sendr, ExperienceInvitation |
| `eventDate` | `string` | No | Datetime when the notification stream entry event had occured |
| `timestamp` | `string` | No | Relative timestamp for sendr notification stream entry |
| `isInteracted` | `boolean` | No | Has the user interacted with the notification stream entry |
| `metadataCollection` | `any[]` | No | List of metadata objects showing more details related to the notification stream entry |
| `eventCount` | `integer` | No | Count of events corresponding to the group of notification stream entry |
| `content` | `any` | No | Content object for sendr notification stream entry |

### Roblox.Api.Notifications.Models.NotificationUser

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | `string` | No | Name of the user |
| `userId` | `integer` | No | Id of the user |

### Roblox.Api.Notifications.Models.PushNotificationClientMetadata

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `notificationId` | `string` | No | Id for the push client notification |
| `type` | `string` | No | Type of the push client notification |
| `detail` | `any` | No | Details corresponding to the notification |
| `fallbackDelivered` | `boolean` | No | Is fallback delivered for the notification metadata |

### Roblox.Api.Notifications.Models.PushNotificationRegistration

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `userPushNotificationDestinationId` | `integer` | No | Id of the push notification destination |
| `name` | `string` | No | Name of the push Notification destination |
| `notificationToken` | `string` | No | Notification token |
| `application` | `string` | No | Notification application Example : "Roblox" |
| `platform` | `string enum (8 values)` | No | Notification platform ['ChromeOnDesktop' = 0, 'AndroidNative' = 1, 'FirefoxOnDesktop' = 2, 'IOSNative' = 3, 'AndroidAmazon' = 4, 'IOSTencent' = 5, 'AndroidTencentService' = 6, 'IOSPushKit' = 7] Values: ChromeOnDesktop, AndroidNative, FirefoxOnDesktop, IOSNative, AndroidAmazon, IOSTencent, AndroidTencentService, IOSPushKit |

### Roblox.Api.Notifications.Models.RegisterAndroidRequestModel

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `notificationToken` | `string` | No | Token for notification |
| `authorizeForUser` | `boolean` | No | Is this call authorized for user |
| `oldNotificationToken` | `string` | No | Old notification token |
| `deviceName` | `string` | No | Name of the requesting device |

### Roblox.Api.Notifications.Models.RegisterIOSNativeRequestModel

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `notificationToken` | `string` | No | Token for notification |
| `destinationIdentifier` | `string` | No | Identifier string for the destination |
| `authorizeForUser` | `boolean` | No | Is call authorized for user |
| `oldNotificationToken` | `string` | No | Old notification token |
| `deviceName` | `string` | No | Name of the requesting device |
| `isProvisional` | `boolean` | No | True when the client granted iOS provisional authorization (silent, quiet-only) rather than full authorization. Absent/null is treated as not provisional. |

### Roblox.Api.Notifications.Models.RegisterIOSPushKitRequestModel

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `notificationToken` | `string` | No | Token for notification |
| `destinationIdentifier` | `string` | No | Identifier string for the destination |
| `authorizeForUser` | `boolean` | No | Is call authorized for user |
| `oldNotificationToken` | `string` | No | Old notification token |
| `deviceName` | `string` | No | Name of the requesting device |

### Roblox.Api.Notifications.Models.RegistrationResponseModel

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `registration` | `Roblox.Api.Notifications.Models.PushNotificationRegistration` | No |  |
| `statusMessage` | `string` | No | Message for the success response |

### Roblox.Api.Notifications.Models.ResponseModels.NotificationStreamMetadataResponse

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `bannerDismissTimeSpan` | `integer` | No |  |
| `signalRDisconnectionResponseInMilliseconds` | `integer` | No |  |
| `canLaunchGameFromGameUpdate` | `boolean` | No |  |

### Roblox.Api.Notifications.Models.SuccessResponseModel

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusMessage` | `string` | No | Message for the success response |

### Roblox.Api.Notifications.Models.UnreadStreamNotificationsModel

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `unreadNotifications` | `integer` | No | Count of unread notifications in the stream |
| `statusMessage` | `string` | No | Message for the success response |

### Roblox.Api.Notifications.Models.UserPushDestination

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `user` | `Roblox.Api.Notifications.Models.NotificationUser` | No |  |
| `name` | `string` | No | Name of the destination |
| `notificationToken` | `string` | No | Token for the corresponding notification |
| `supportsUpdateNotifications` | `boolean` | No | Is Update notification feature supported |
| `userPushNotificationDestinationId` | `integer` | No | Destination Id for the push notification |
| `application` | `string` | No | application for the corresponding notification Example : "Roblox" |
| `platform` | `string enum (8 values)` | No | Platform for the corresponding notification ['ChromeOnDesktop' = 0, 'AndroidNative' = 1, 'FirefoxOnDesktop' = 2, 'IOSNative' = 3, 'AndroidAmazon' = 4, 'IOSTencent' = 5, 'AndroidTencentService' = 6, 'IOSPushKit' = 7] Values: ChromeOnDesktop, AndroidNative, FirefoxOnDesktop, IOSNative, AndroidAmazon, IOSTencent, AndroidTencentService, IOSPushKit |