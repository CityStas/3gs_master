---
title: "Usage guide for place publishing"
url: /docs/en-us/cloud/guides/usage-place-publishing
last_updated: 2026-10-30T19:55:39Z
description: "Explains how to use Open Cloud Place Publishing API to publish places programmatically with version control."
---

# Usage guide for place publishing

The [place publishing API](/docs/en-us/reference/cloud/universes-api/v1.md) offers similar functionality to [publishing to Roblox](/docs/en-us/production/publishing/publish-games-and-places.md) in Studio, with extra permission control and automation in continuous release workflow. You can use this API to update existing places of a game to a new version, making it useful for automating your publishing workflow. For example, you can call this API from a GitHub action and have it automatically push a binary place file to Roblox after successful integration testing.

## Limitations

- This API only supports HTTPS requests.
- The place publishing API doesn't update certain instance types. If your game contains `Class.EditableImage`, `Class.EditableMesh`, `Class.PartOperation`, `Class.SurfaceAppearance`, or `Class.BaseWrap` instances, publish from Studio after modifying them.

## Places on Roblox

Games on Roblox can have multiple places, with one **starting place** as the user entry point of your game and optional other places that you can [teleport users between](/docs/en-us/projects/teleport.md). You can use the API to publish either the starting place or other places of your game with version control.

Before you can update an existing place of a game, you need the place's **Place ID** and the game's **Universe ID**. The **Place ID** identifies the place and the **Universe ID** identifies the game. Each is unique even if your game has only one place.

## Publish a place

To publish an existing place of a game with [Place Publishing API](/docs/en-us/reference/cloud/universes-api/v1.md):

1. [Create an API key](/docs/en-us/cloud/auth/api-keys.md#create-api-keys) on the **Creator Dashboard**. Make sure you perform the following settings:
  1. Add **universe-places** to **Access Permissions**.
  2. Add **Write** operation to your selected game.
2. Get the **Universe ID** of the game in which you want to publish the place.
  1. Navigate to the [Creator Dashboard](https://create.roblox.com/dashboard/creations).
  2. Find the game with the place that you want to update.
  3. Hover over the game's thumbnail, click the **⋯** button, and select **Copy Universe ID**.
3. Get the **Place ID** of the place that you want to update.
  1. Stay on the [Creations](https://create.roblox.com/dashboard/creations) page on **Creator Dashboard** and click the thumbnail of the target game.
  2. On the left navigation menu, click the **Places** tab.
  3. Find the place that you want to update and click its thumbnail.
  4. The **Place ID** is in the redirected URL. For example, in the URL `https://create.roblox.com/dashboard/creations/experiences/0000000/places/111111/configure`, the **Place ID** is `111111`.
4. Add the API Key in the **x-api-key** header of a `POST` request to the API. The following two example requests reference a Roblox XML place file (`.rbxlx`) and a binary place file (`.rbxl`).```bash
$ curl --verbose --location POST 'https://apis.roblox.com/universes/v1/{universeId}/places/{placeId}/versions?versionType=Published' \
--header 'x-api-key: <your-api-key>' \
--header 'Content-Type: application/xml' \
--data-binary @/home/placefiles/place1.rbxlx
``````bash
$ curl --verbose --location POST 'https://apis.roblox.com/universes/v1/{universeId}/places/{placeId}/versions?versionType=Published' \
--header 'x-api-key: <your-api-key>' \
--header 'Content-Type: application/octet-stream' \
--data-binary @/home/placefiles/place1.rbxl
``` To run the commands, replace `{universeId}` and `{placeId}` with the actual **Universe ID** and **Place ID** of the game and place that you want to publish.
5. If you send your request correctly, you receive a success response body with the place version number in the following format:```json
{ "versionNumber": 7 }
```
6. **OPTIONAL** Verify the upload in Studio or on [Creator Dashboard](https://create.roblox.com/dashboard/creations).