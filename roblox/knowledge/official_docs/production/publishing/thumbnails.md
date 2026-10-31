---
title: "Thumbnails"
url: /docs/en-us/production/publishing/thumbnails
last_updated: 2026-10-30T19:55:51Z
description: "Thumbnail images and videos appear on the Roblox home page and at the top of a game's detail page to showcase features and share information."
---

# Thumbnails

Thumbnails appear on Roblox's [Home](https://www.roblox.com/home) page and at the top of your game's detail page, allowing you to showcase your game's features and announce updates or events.

You can feature up to 10 images or videos for each of your games' detail pages. All uploaded images and videos are moderated to make sure they adhere to the [Community Rules](https://en.help.roblox.com/hc/articles/203313410) and [Terms of Use](https://en.help.roblox.com/hc/articles/115004647846).

| Type | Description | Cost / Quota |
| --- | --- | --- |
| **Image** | An [uploaded image](#images) which supplements the game [icon](/docs/en-us/production/publishing/experience-icons.md) and helps players know what the game offers. | Free |
| **Uploaded Video** | An [uploaded authentic video](#videos), useful for displaying gameplay previews and other in-game features. | Free, with monthly quota of 3 uploads |
| **Auto‑Generated** | An auto‑generated image based on Studio's camera position for the most recent publish of the place. | Free |

## Manage thumbnails

Uploaded thumbnails appear in the **Experience Detail Page** tab where they can be reordered, deleted, or given "alt" text for improved [accessibility](/docs/en-us/production/publishing/accessibility.md).

![Thumbnails and related actions on the Creator Dashboard](../../assets/creator-dashboard/Manage-Thumbnails.png) ### Images

A thumbnail image should be **16:9 aspect ratio** and ideally **1920×1080 pixels** so that it always displays in high resolution across the Roblox site and app. Supported formats include `.jpg`, `.gif`, `.png`, `.tga`, or `.bmp`. See [best practices](#best-practices) for additional design recommendations.

To upload an image thumbnail for your game:

1. In the [Creator Dashboard](https://create.roblox.com/dashboard/creations), select the game you want to upload an image thumbnail for.
2. In the left-hand navigation, navigate to **Configurations** > **Places** and select a place.
3. Click **Thumbnails** in the left nav, then use the **Home Page** tab and the **Experience Detail Page** tab to customize your game's thumbnails for these two spaces.

### Videos

> **Warning:** Xbox , PlayStation, and VR headsets do not currently support video thumbnails.

To help users understand your game before they join, you can upload an authentic gameplay video. Once approved, the video will appear first on your game's detail page, and it can also be shown on the [Home](https://www.roblox.com/home) page.

To upload a video thumbnail for your game:

1. In the [Creator Dashboard](https://create.roblox.com/dashboard/creations), select the game you want to upload a video for.
2. In the left-hand navigation, navigate to **Configurations** > **Places** and select a place.
3. Click **Videos** in the left nav.

Video thumbnails should be **authentic** and [accurately portray in-game content](#video-accuracy) without misleading alterations. **All videos will be reviewed** to ensure they accurately reflect the game and do not violate the [Community Rules](https://en.help.roblox.com/hc/articles/203313410) or [Terms of Use](https://en.help.roblox.com/hc/articles/115004647846).

Certain modifications are acceptable, as long as they don't misrepresent the core game:

> **Success:****Camera Work** — Using varied camera angles for aesthetic or cinematic purposes is fine, as long as they showcase real gameplay. Studio's [free camera mode](/docs/en-us/workspace/camera/free-camera.md) is especially helpful for capturing different vantage points.
> **Success:****Minor Post-Processing** — Small adjustments like brightness, contrast, or minor visual effects are acceptable if they don't fundamentally alter the visual fidelity of the actual game. It's also acceptable to overlay your game's logo or branding in a video.
> **Success:****Curated Sequences** — You can showcase optimized or highlight-reel playthroughs. These sequences don't need to be strictly linear but they must display actual gameplay mechanics and interactions.
> **Success:****In-game UI Text** — Text that is part of your game's UI (character names, menus, notifications that appear to the player, etc.) is acceptable because it's part of the authentic game view.
> **Success:****Music Tracks** — Videos can contain music from Roblox's [catalog](https://create.roblox.com/store/audio) as governed by Roblox's internal licensing arrangements.

To prevent misleading players, please adhere to the following policies. Videos which do not adhere to these policies will be **rejected for distribution** and count against the monthly quota of 3 video uploads.

> **Error:****Misrepresented Gameplay** — Do not display gameplay mechanics, UI elements, or interactions that are not actually available in your game. For instance, a roleplay game should not be marketed as a racing game. Also ensure the video accurately reflects the core themes, for example a horror game should depict horror elements and not misrepresent its theme.
> **Error:****Artificial Visuals** — Graphics shown must be representative of the actual in-game visuals. Avoid artificially enhancing graphics beyond what a player will experience.
> **Error:****External Content & Overlays** — Don't include real-life footage of people, places, or any other content external to your game.
> **Error:****Spoken Audio** — Added voice-overs, narration, voice chat conversations, and music with lyrics is **not** permitted.
> **Error:****Text, Claims, and Advertisements** — Overlay text sparingly and only to describe gameplay contexts such as "Collect coins to boost jumps." Do not include any text, visuals, or audio that is an advertisement, promotion, or subjective claim, for example "50% off" or "Free UGC!".

## Free camera mode

The run-time **free camera mode** (freecam) allows you to manipulate the camera to vantage points which may not be possible through the default view camera, making it a useful tool for capturing cinematic screenshots and video. Press `Left Shift` + `P` during a solo playtest to toggle it on or off.

For the full list of controls, the config menu, and custom freecam post-processing effects, see [free camera mode](/docs/en-us/workspace/camera/free-camera.md).

## Home page personalization

**Thumbnail personalization** helps you attract more users to your game by showing the most relevant thumbnail to each user on their [Home](https://www.roblox.com/home) page. The goal of thumbnail personalization is to improve your qualified play through rate, which is the percentage of users that actively engage with your game for a significant amount of time.

> **Success:** During testing, games using thumbnail personalization had an average increase of +8.5% in their qualified play through rate. Some games had an increase of +50%.

Thumbnail personalization only starts when you activate 2 or more thumbnails. If only one of your thumbnails is active, all users see that thumbnail for your game on their home page.

After you set up and activate thumbnail personalization, its algorithm shows each thumbnail to a random set of users to get data on the qualified play through rate for each user group. It then gives more impressions to the winning thumbnail for each group, but still gives the other thumbnails minimal traffic to continue exploration.

### Set up thumbnail personalization

To set up thumbnail personalization:

1. In the **Home Page** tab, click **Edit active thumbnails**.
2. Upload new thumbnails or activate existing thumbnails.
  - To upload new thumbnails, click **Upload thumbnails** and select and confirm the images you want to use. Make sure to keep these images under 3 MB and 1920×1080 pixels.
  - To activate existing thumbnails, enable the **Active** checkbox next to 2-5 thumbnails.
3. Click **Save changes**.
4. In the **Start new thumbnail personalization?** dialog, click **Start**. The banner in the **Home Page** tab updates to indicate that thumbnail personalization is active.

![Example of the Home Page tab](../../assets/publishing/experience-metadata/Thumbnail-Home-Page-Tab.png) ### Keep multiple thumbnails active

> **Warning:** To get the most out of thumbnail personalization, make sure to **keep multiple thumbnails active** instead of choosing one winner, as this allows personalization to adapt to changing user trends.

For example, if you had removed the thumbnail associated with the green line in the chart below too early, you would have missed future additional impressions for what ended up becoming your second-best performing thumbnail.

![Example of the Impression by Thumbnail graph](../../assets/publishing/experience-metadata/Thumbnail-Impressions-Graph.png)

It's recommended to test multiple new thumbnails with any major game or content update, and then not make changes to your thumbnails until your game's next update.

### Analyze thumbnail personalization performance

After a few hours, the **Thumbnail Performance** table in the **Home Page** tab populates with statistics related to each of your active thumbnails:

| Title | Description |
| --- | --- |
| **Status** | Indicates if the thumbnail is active for personalization. |
| **Impressions** | Number of impressions from home page recommendations. |
| **Qualified Plays** | Number of qualified plays from home page recommendations. |
| **Average Playtime** | The average session time in minutes per qualified play. |
| **Qualified Play Through Rate** | The percentage of qualified plays divided by impressions from home page recommendations. |
| **Winning Segment** | The thumbnail with the highest play through rate during the current thumbnail personalization process. |

You can also use the **Impressions by thumbnail** and the **Qualified play through rate by thumbnail** graphs to further analyze the performance of your personalized thumbnails over time.

## Best practices

To create the most positive impact for players looking to play your game, consider the following best practices.

> **Warning:** In addition to the practices shown below, avoid placing any essential text or elements at the **bottom** of the thumbnail, as it may potentially be covered by metadata like the player count.
### Quality and aspect ratio

A thumbnail image should be **16:9** aspect ratio and ideally **1920×1080 pixels** so that it always displays in high resolution across the Roblox site and app. Displayed thumbnails will be stretched to 16:9 aspect ratio regardless of the upload's aspect ratio.

![High quality and sharp thumbnail](../../assets/publishing/experience-metadata/Thumbnail-High-Res.jpg)_> **Success:** High quality and sharp; upload in 16:9 aspect ratio_

![Non-16:9 thumbnail](../../assets/publishing/experience-metadata/Thumbnail-Not-16-9.jpg)_> **Error:** Upload not in 16:9 aspect ratio; displayed thumbnail stretched_

### Relevant content

A thumbnail will have a higher impact if it's unique and provides relevant imagery on what players should expect when they join the game. Thumbnails with ambiguous imagery or graphics may lead to unnecessary confusion.

![Thumbnail portraying a high-action urban racing game](../../assets/publishing/experience-metadata/Thumbnail-Urban-Rush.jpg)_> **Success:** Thumbnail portrays a high‑action urban racing game_

![Thumbnail with unclear imagery and an ambiguous graphic in the top-right corner](../../assets/publishing/experience-metadata/Thumbnail-Unclear.jpg)_> **Error:** Unclear imagery and ambiguous graphic in top‑right corner_

### Video accuracy

Video thumbnails should be authentic and portray actual in-game content without misleading alterations.

_> **Success:** Video presents actual gameplay which gives players an accurate and honest expectation of the game_

_> **Error:** Video presents an exaggerated version of the game and gameplay which is misleading to players_

### Theme and color

You can express your game's theme through overall theme and colors to help players decide if it's suitable and appealing to them.

![Thumbnail with a comical theme/character and bright colors](../../assets/publishing/experience-metadata/Thumbnail-Theme-Comical.jpg)_Comical theme/character with bright colors_

![Thumbnail with a dark and stormy theme for a horror game](../../assets/publishing/experience-metadata/Thumbnail-Theme-Horror.jpg)_Dark and stormy theme for a horror game_
