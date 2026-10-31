---
title: "Usage guide for assets"
url: /docs/en-us/cloud/guides/usage-assets
last_updated: 2026-10-30T19:55:39Z
description: "Explains how to use Open Cloud Web APIs for assets to support usage such as uploading and updating."
---

# Usage guide for assets

The [Assets API](/docs/en-us/reference/cloud/assets/v1.md) of Open Cloud allows you to upload and update assets with a single HTTP request rather than manually importing them to Studio. This API supports:

- Uploading new assets.
- Updating existing assets with version control.
- Updating asset metadata, including descriptions, display names, icons, and previews.
- Managing asset versions, such as rolling back to a specified previous version.
- Checking existing information of an asset, including metadata, versions, and any in-process updating operations.

> **Info:** This API contains beta endpoints that might be subject to changes for future releases.
## Supported asset types and limits

For endpoints that don't create a new asset or update the content of existing assets, there are no restrictions and limits. However, the asset content uploading functionality powered by the **Create Asset** and **Update Asset** endpoints only supports limited types of assets with restrictions. For each call, you can only create or update one asset with the file size up to 20 MB with the following limits:

> **Info:** Updating asset metadata using the **Update Asset** endpoint is not subject to the following limits.

| Asset type | Format | Content type | Restrictions |
| --- | --- | --- | --- |
| [Animation](/docs/en-us/animation.md) | <ul><li>`.rbxm`</li><li>`.rbxmx`</li></ul> | <ul><li>`model/x-rbxm`</li><li>`model/x-rbxm`</li></ul> | <ul><li>`.rbxm` or `.rbxmx` files edited outside of [Roblox Studio](/docs/en-us/studio/setup.md) might not upload or function.</li></ul> |
| [Audio](/docs/en-us/audio/assets.md) | <ul><li>`.mp3`</li><li>`.ogg`</li><li>`.wav`</li><li>`.flac`</li></ul> | <ul><li>`audio/mpeg`</li><li>`audio/ogg`</li><li>`audio/wav`</li><li>`audio/flac`</li></ul> | <ul><li>Up to 7 minutes of duration.</li><li>Up to 100 uploads per month if you're ID-verified.</li><li>Up to 10 total uploads per month if you aren't ID-verified.</li><li>Not available for updating.</li></ul> |
| [Decal, Image](/docs/en-us/parts/textures-decals.md) | <ul><li>`.png`</li><li>`.jpeg`</li><li>`.bmp`</li><li>`.tga`</li></ul> | <ul><li>`image/png`</li><li>`image/jpeg`</li><li>`image/bmp`</li><li>`image/tga`</li></ul> | <ul><li>Must be smaller than 8000x8000 pixels.</li><li>Not available for updating.</li></ul> |
| [Mesh](/docs/en-us/parts/meshes.md) | <ul>Roblox only</ul> | <ul><li>`model/x-file-mesh-data`</li></ul> | <ul><li>Only content downloaded from [Asset delivery API](/docs/en-us/cloud/reference/domains/assetdelivery.md) is accepted. If you are not trying to download and re-upload meshes, then use [Importer](/docs/en-us/studio/importer.md) to import meshes instead.</li><li>Not available for updating.</li></ul> |
| [Model](/docs/en-us/parts/models.md) | <ul><li>`.fbx`</li><li>`.gltf`</li><li>`.glb`</li><li>`.rbxm`</li><li>`.rbxmx`</li></ul> | <ul><li>`model/fbx`</li><li>`model/gltf+json`</li><li>`model/gltf-binary`</li><li>`model/x-rbxm`</li><li>`model/x-rbxm`</li></ul> | <ul><li>Imports custom 3D models as a `Class.Model` container containing one or more `Class.MeshPart` objects.</li><ul><li>Depending on your use-case, consider uploading custom 3D models manually using the [Importer](/docs/en-us/studio/importer.md).</li><li>The Importer provides a 3D preview, various error-checking, and many customizable import settings.</li></ul><li>`.rbxm` or `.rbxmx` files edited outside of [Roblox Studio](/docs/en-us/studio/setup.md) might not upload or function.</li><li>Will be uploaded as [packages](/docs/en-us/projects/assets/packages.md)</li></ul> |
| [Video](/docs/en-us/ui/video-frames.md) | <ul><li>`.mp4`</li><li>`.mov`</li></ul> | <ul><li>`video/mp4`</li><li>`video/mov`</li></ul> | <ul><li>Up to 5 minutes of duration.</li><li>Up to 4096x2160 resolution.</li><li>Up to 3.75 GB.</li><li>Up to 20 uploads per day if you're 13+ and ID-verified.</li><li>Not available for updating.</li></ul> |

## Security permissions

The API supports both first-party use with [API key authorization](/docs/en-us/cloud/auth/api-keys.md) and third-party use in [OAuth 2 applications](/docs/en-us/cloud/auth/oauth2-overview.md). Each way requires different security permission settings.

### API keys

To use the API in your own scripts or tools, you need to [create an API key](/docs/en-us/cloud/auth/api-keys.md#create-api-keys) for authorization and security.

> **Warning:** To create an API key for managing group assets, you must have the corresponding permissions. For more information on granting group permissions, see [Group roles and permissions](/docs/en-us/projects/groups.md#roles-and-permissions).

When creating an API key, make sure to add the following permissions:

1. Add **assets** to **Access Permissions**.
2. Add **Read** and **Write** operation permissions to your selected game, depending on the required scopes of the endpoints you plan to call.

Once you have the API key, copy it to the `x-api-key` request header. All endpoints require the `x-api-key` request header.

```bash
--header 'x-api-key: ${ApiKey}' \
```

### OAuth 2.0 apps

To use the API for a third-party OAuth 2.0 application, add the `asset:read` and `asset:write` permission scopes when [registering your app](/docs/en-us/cloud/auth/oauth2-registration.md#add-permissions). Choose these scopes based on the requirements of the endpoints you plan to use.

## Create a new asset

To upload a new asset by an HTTP request:

1. Copy the API key to the `x-api-key` request header of the [Create Asset](/docs/en-us/reference/cloud/assets/v1.md#POST-v1-assets) endpoint.
2. In your request:
  1. Specify the target [asset type](#supported-asset-types-and-limits).
  2. Add your asset name and description.
  3. Add the creator information.
    - If you want to create the asset **on your own behalf**, add your user ID. You can find your user ID on the URL of your Roblox profile. For example, for `https://www.roblox.com/users/1234567/profile`, your user ID is `1234567`.
    - If you want to create the asset **as a group asset**, add the group ID of your group. You can find the group ID on the URL of your group's page. For example, for `https://www.roblox.com/groups/7654321/example-group#!/`, the group ID is `7654321`.
  4. Add the file path and content type of your asset.```bash
curl --location 'https://apis.roblox.com/assets/v1/assets' \
--header 'x-api-key: ${ApiKey}' \
--form 'request="{
  \"assetType\": \"Model\",
  \"displayName\": \"Name\",
  \"description\": \"This is a description\",
  \"creationContext\": {
    \"creator\": {
      \"userId\": \"${userId}\" # Use groupId for creating a group asset
    }
  }
}"' \
--form 'fileContent=@"/filepath/model.fbx";type=model/fbx'
```

## Update an existing asset

> **Info:** Asset updating is powered by beta endpoints that might be subject to changes for future releases.

To update an existing asset by an HTTP request:

1. Copy the API key to the `x-api-key` request header of the [Update Asset](/docs/en-us/reference/cloud/assets/v1.md#PATCH-v1-assets-_asset_) endpoint.
2. Add the asset type and asset ID in your request. To copy your asset ID:
  1. Navigate to the [Creation](https://create.roblox.com/dashboard/creations) page of the **Creator Dashboard**.
  2. Select the **Development Items** category.
  3. Select the category of your asset and find the target asset.
  4. Hover over the thumbnail of the target asset and click the **⋯** button to display a list of options, then select **Copy Asset ID** from the list.

#### Asset Content

> **Warning:** Currently, you can only update the asset content for `.fbx` files. The update creates a new version.

```bash
curl --location --request PATCH 'https://apis.roblox.com/assets/v1/assets/{assetId}' \
--header 'x-api-key: {apiKey}' \
--form 'request={
    \"assetType\": \"{assetType}\",
    \"assetId\": \"{assetId}\",
    \"creationContext\": {
        \"creator\": {
            \"userId\": {userId}
        },
        \"expectedPrice\":{expectedPrice}
    },
}' \
--form 'fileContent=@"{file-path}"'
```

#### Metadata

```bash
curl --location --request PATCH 'https://apis.roblox.com/assets/v1/assets/{assetId}?updateMask=description%2CdisplayName' \
--header 'x-api-key;' \
--form 'request={
    \"assetType\": \"{assetType}\",
    \"assetId\": \"{assetId}\",
    \"displayName\": \"{new display name}\",
    \"description\": \"{new description}\"
}'
```

#### Content and Metadata

```bash
curl --location --request PATCH 'https://apis.roblox.com/assets/v1/assets/{assetId}?updateMask=description%2CdisplayName' \
--header 'x-api-key: {apiKey}' \
--form 'request={
    \"assetType\": \"{assetType}\",
    \"assetId\": \"{assetId}\",
    \"displayName\": \"{new display name}\",
    \"description\": \"{new description}\",
    \"creationContext\": {
        \"creator\": {
            \"userId\": {userId}
        },
        \"expectedPrice\":{expectedPrice}
    },
}' \
--form 'fileContent=@\"{file-path}\"'
```

## Retrieve asset operation status

If your request for creating a new asset or updating an existing asset succeeds, it returns an **Operation ID** in the format of `{ "path": "operations/${operationId}" }`. You can use it to check the status and result of your upload with the following steps:

1. Copy the API key to the `x-api-key` request header of the [Get Operation](/docs/en-us/reference/cloud/assets/v1.md#GET-v1-operations-_operationId_) method and send the request, like the following code sample:```bash
curl --location 'https://apis.roblox.com/assets/v1/operations/{operationId}' \
--header 'x-api-key: {$ApiKey}'
```
2. If your request succeeds, it returns an `Operation` object, either including a `response` representing the uploaded asset information or a `status` explaining why the asset upload fails as the following code sample shows:```json
{
  "path": "operations/{operationId}",
  "done": true,
  "response": {
    "@type": "type.googleapis.com/roblox.open_cloud.assets.v1.Asset",
    "path": "assets/2205400862",
    "revisionId": "1",
    "revisionCreateTime": "2023-03-02T22:27:04.062164400Z",
    "assetId": "2205400862",
    "displayName": "Name",
    "description": "This is a description",
    "assetType": "ASSET_TYPE_DECAL",
    "creationContext": {
      "creator": {
        "userId": "11112938575"
      }
    },
    "moderationResult": {
      "moderationState": "MODERATION_STATE_APPROVED"
    }
  }
}
```
3. **OPTIONAL** Check the created asset on your Roblox account.
  1. Navigate to the **Inventory** page of your [Roblox account](https://www.roblox.com/home).
  2. Select the **Category** of the asset that you want to check.
  3. Find the target asset and click its thumbnail to view the asset.

## Use uploaded assets in Studio

An asset that you upload belongs to the user or group in the `creationContext` of your request, so it's available in Studio like any other asset that creator owns:

- Insert it from the [Toolbox](/docs/en-us/projects/assets/toolbox.md) or the [Asset Manager](/docs/en-us/projects/assets/manager.md#inventory-sorting).
- Models upload as [packages](/docs/en-us/projects/assets/packages.md), so check **Inventory** ⟩ **My Packages** in the Toolbox (or **Creations** ⟩ **Group Packages** if a group owns them).
- To use an asset in a property, enter `rbxassetid://` followed by the `assetId` from the operation response in the [Properties](/docs/en-us/studio/properties.md) window. In a script, assign that string to a string property such as `Class.AudioPlayer.Asset`, or pass the `assetId` to `Datatype.Content.fromAssetId()` for a property of type `Datatype.Content`, such as `Class.Decal.ColorMapContent`. For more information, see [rbxassetid](/docs/en-us/projects/assets.md#rbxassetid).

## Add assets API to OAuth 2.0 apps

You can create [OAuth 2.0 applications](/docs/en-us/cloud/auth/oauth2-overview.md) supporting Assets API to allow your users to upload and update assets to Roblox.

> **Warning:** Third-Party app support through OAuth 2.0 is a Beta feature that might be subject to changes for future releases.

To use Assets API for your application and request permissions from your users, perform the following settings:

1. When [registering your application](/docs/en-us/cloud/auth/oauth2-registration.md#register-your-app), under **Permissions**, select **asset:read** and **asset:write** scopes.
2. When [implementing the authorization flow](/docs/en-us/cloud/auth/oauth2-overview.md#implement-authorization-flows), include `asset:read` and `asset:write` as the scope parameters of the authorization URL that redirects users back to your application, like the following example:```plain
https://apis.roblox.com/oauth/v1/authorize?client_id=819547628404595165403873012&redirect_uri=https://my-app.com/redirect&scope=asset:read+asset:write&response_type=Code&prompts=login+consent&nonce=12345&state=6789
```
3. When sending the request, include the access token in the authorization header and the form data of the asset content to create or update in the request URI in. The following example shows a sample request for uploading a new asset:```bash
curl --location --request POST 'https://apis.roblox.com/assets/v1/assets' \

--header 'Authorization: Bearer <access_token>' \

--header 'Content-Type: application/json' \

--form 'request="{

  \"assetType\": \"Decal\",

  \"displayName\": \"DecalDemo123\",

  \"description\": \"This is a description\",

  \"creationContext\": {

    \"creator\": {

    \"userId\": \"<user_id>\"

    }
  }

}"' \

--form 'fileContent=@"/filepath/p1.png"'
```