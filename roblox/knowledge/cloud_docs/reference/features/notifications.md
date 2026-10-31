---
name: "Notifications"
last_updated: 2026-10-30T19:56:08Z
type: feature
api_base_url: "https://apis.roblox.com"
endpoints: 11
auth: [api-key, oauth2, cookie]
description: "Send personalized notifications to re-engage players and keep them informed about your experience"
---

# Notifications

Send personalized notifications to re-engage players and keep them informed about your experience. Each user can receive one notification per day from a given experience. See the [Experience Notifications Guide](/cloud/guides/experience-notifications).

Common use cases include:

- Experience notifications: [Send targeted notifications](#Cloud_CreateUserNotification) to users about in-game events, rewards, or updates
- Personalized messages: Customize notifications with dynamic parameters like usernames and scores
- **Launch Data Integration**: Include launch data to route users to specific locations when they join

> **Getting started:** See [User notifications](/docs/en-us/cloud/guides/experience-notifications.md) for a complete walkthrough with working examples.

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

### POST `/cloud/v2/users/{user_id}/notifications` [STABLE]

Create User Notification

Sends a notification to a user.

**Auth:** API Key (`x-api-key` header) or OAuth 2.0 Bearer token

**Scopes:** `user.user-notification:write`, `user.user-notification:write`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `user_id` | path | `string` | Yes | The user ID. |

**Request Body:** `application/json` — Type: `UserNotification`

See [UserNotification](#usernotification) in Models.

**Request example:**
```json
{
  "path": "string",
  "id": "string",
  "source": {
    "universe": "string"
  },
  "payload": {
    "type": "TYPE_UNSPECIFIED",
    "messageId": "string",
    "parameters": "...",
    "joinExperience": {
      "launchData": "..."
    },
    "analyticsData": {
      "category": "..."
    }
  }
}
```

**Responses:**

- `200`: OK → `UserNotification`

**Response fields** (`UserNotification`)

See [UserNotification](#usernotification) in Models.

**Response example:**
```json
{
  "path": "string",
  "id": "string",
  "source": {
    "universe": "string"
  },
  "payload": {
    "type": "TYPE_UNSPECIFIED",
    "messageId": "string",
    "parameters": "...",
    "joinExperience": {
      "launchData": "..."
    },
    "analyticsData": {
      "category": "..."
    }
  }
}
```

**Rate Limits:** perApiKeyOwner: 4000/second, perOauth2Authorization: 4000/second

**Example:**
```bash
curl -X POST -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/cloud/v2/users/{USER_ID}/notifications" \
  -H "Content-Type: application/json" \
  -d '{
  "path": "string",
  "id": "string",
  "source": {
    "universe": "string"
  },
  "payload": {
    "type": "TYPE_UNSPECIFIED",
    "messageId": "string",
    "parameters": "...",
    "joinExperience": {
      "launchData": "..."
    },
    "analyticsData": {
      "category": "..."
    }
  }
}'
```

### POST `/v2/push-notifications/deregister-all-devices`

De-register all devices to disable push notifications

**Server:** `https://notifications.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

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
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://notifications.roblox.com/v2/push-notifications/deregister-all-devices"
```

### POST `/v2/push-notifications/deregister-current-device`

De-register current device to disable push notifications

**Server:** `https://notifications.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

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
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://notifications.roblox.com/v2/push-notifications/deregister-current-device"
```

### POST `/v2/push-notifications/deregister-current-device-ios-pushkit`

De-register current device to disable pushkit notifications

**Server:** `https://notifications.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

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
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://notifications.roblox.com/v2/push-notifications/deregister-current-device-ios-pushkit"
```

### POST `/v2/push-notifications/register-android-native`

Register Android Native for push notifications

**Server:** `https://notifications.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

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
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
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

**Server:** `https://notifications.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

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
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
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

**Server:** `https://notifications.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

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
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
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

### POST `/v2/stream-notifications/clear-unread` [EXPERIMENTAL]

Clears the unread Notification stream count

**Server:** `https://notifications.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

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
curl -X POST -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://notifications.roblox.com/v2/stream-notifications/clear-unread"
```

### GET `/v2/stream-notifications/get-latest-game-updates` [EXPERIMENTAL]

Get the latest non aggregated Game Updates sent to the logged in user

**Server:** `https://notifications.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universeIds` | query | `integer[]` | Yes | List of universe IDs |
| `sinceDateTime` | query | `string` | No | For retrieving only updates that created after a time point. |

**Responses:**

- `200`: OK → `Roblox.Api.Notifications.Models.GameUpdateNotificationModel[]`
- `401`: 0: Authorization has been denied for this request.

**Response fields** (`Roblox.Api.Notifications.Models.GameUpdateNotificationModel[]`)

See [Roblox.Api.Notifications.Models.GameUpdateNotificationModel](#roblox-api-notifications-models-gameupdatenotificationmodel) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://notifications.roblox.com/v2/stream-notifications/get-latest-game-updates?universeIds={VALUE}"
```

### GET `/v2/stream-notifications/get-recent` [EXPERIMENTAL]

Gets the recent entries from the notification stream

**Server:** `https://notifications.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `startIndex` | query | `integer` | No | Index to start the entries from. (Optional : Defaults to 0 which means the most recent entry) |
| `maxRows` | query | `integer` | No | Number of entries to be returned. (Optional : Defaults to 10 entries) |

**Responses:**

- `200`: OK → `Roblox.Api.Notifications.Models.NotificationStreamEntriesModel[]`
- `401`: 0: Authorization has been denied for this request.

**Response fields** (`Roblox.Api.Notifications.Models.NotificationStreamEntriesModel[]`)

See [Roblox.Api.Notifications.Models.NotificationStreamEntriesModel](#roblox-api-notifications-models-notificationstreamentriesmodel) in Models.

**Error handling:** `401`: Check that your API key/token is valid and not expired. 

**Example:**
```bash
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://notifications.roblox.com/v2/stream-notifications/get-recent"
```

### GET `/v2/stream-notifications/unread-count` [EXPERIMENTAL]

Gets the count of unread Notification stream entries

**Server:** `https://notifications.roblox.com`

**Auth:** Cookie (`.ROBLOSECURITY`)

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
curl -b ".ROBLOSECURITY=$ROBLOSECURITY" \
  "https://notifications.roblox.com/v2/stream-notifications/unread-count"
```

## Models

### UserNotification

Represents a notification sent to a user.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `path` | `string` | No | The resource path of the user notification.  Format: `users/{user_id}/notifications/{user_notification_id}` |
| `id` | `string` | No | A unique UUID of the user notification. |
| `source` | `UserNotification_Source` | No | The source of the notification. |
| `payload` | `UserNotification_Payload` | No | The notification payload. |

### Roblox.Api.Notifications.Models.SuccessResponseModel

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `statusMessage` | `string` | No | Message for the success response |

### Roblox.Api.Notifications.Models.RegisterAndroidRequestModel

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `notificationToken` | `string` | No | Token for notification |
| `authorizeForUser` | `boolean` | No | Is this call authorized for user |
| `oldNotificationToken` | `string` | No | Old notification token |
| `deviceName` | `string` | No | Name of the requesting device |

### Roblox.Api.Notifications.Models.RegistrationResponseModel

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `registration` | `Roblox.Api.Notifications.Models.PushNotificationRegistration` | No |  |
| `statusMessage` | `string` | No | Message for the success response |

### Roblox.Api.Notifications.Models.RegisterIOSNativeRequestModel

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `notificationToken` | `string` | No | Token for notification |
| `destinationIdentifier` | `string` | No | Identifier string for the destination |
| `authorizeForUser` | `boolean` | No | Is call authorized for user |
| `oldNotificationToken` | `string` | No | Old notification token |
| `deviceName` | `string` | No | Name of the requesting device |
| `isProvisional` | `boolean` | No | True when the client granted iOS provisional authorization (silent, quiet-only) rather than full authorization. Absent/null is treated as not provisional. |

### Roblox.Api.Notifications.Models.RegisterIOSPushKitRequestModel

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `notificationToken` | `string` | No | Token for notification |
| `destinationIdentifier` | `string` | No | Identifier string for the destination |
| `authorizeForUser` | `boolean` | No | Is call authorized for user |
| `oldNotificationToken` | `string` | No | Old notification token |
| `deviceName` | `string` | No | Name of the requesting device |

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

### Roblox.Api.Notifications.Models.UnreadStreamNotificationsModel

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `unreadNotifications` | `integer` | No | Count of unread notifications in the stream |
| `statusMessage` | `string` | No | Message for the success response |