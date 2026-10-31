---
title: "Acquisition"
url: /docs/en-us/production/analytics/acquisition
last_updated: 2026-10-30T19:55:47Z
description: "Explains how to interpret and improve acquisition metrics for your game."
---

# Acquisition

**Acquisition** measures where new and returning users are coming from and how well they convert.

When acquiring users to your game, such as announcing an in-game event or creating ad campaigns, make sure your game has good [retention](/docs/en-us/production/analytics/retention.md) and [engagement](/docs/en-us/production/analytics/engagement.md).

## View acquisition metrics

To view your game's acquisition analytics:

1. Navigate to your [Creations](https://create.roblox.com/dashboard/creations) page on **Creator Dashboard** and select your game.
2. In the **Analytics** menu on the left, select **Acquisition**.

You can view analytics for individual or group owned game. To view the latter, you need to have [group permissions for analytics](/docs/en-us/production/analytics/analytics-dashboard.md).

## Acquisition sources

On the acquisition dashboard, you'll see the following charts and tables:

- New users with play per source
- New users with impressions per source
- Returning users with plays per source
- Returning users with impressions per source
- Play through rate
- Cumulative new users funnel

Here's a list of all the available acquisition sources:

| Source | Description |
| --- | --- |
| Home recommendations | **Recommended Experiences** section on **Home** |
| Continue play | **Continue Play** on **Home** |
| Today's Picks | **Today's Picks** on **Home** |
| Home other | **Favorites** and all other traffic on **Home** |
| Friends | **Friend Activity** section on **Home** |
| Search | Organic traffic from **Search** results and **Recommended Experiences** on **Experience Details** page |
| Charts | **All sorts** on **Charts** |
| Sponsored ads | Acquisition from [sponsored experiences](/docs/en-us/production/promotion/ads-manager.md) and **Sponsored Takeovers** on **Home** |
| Search ads | Acquisition from [search ads](/docs/en-us/production/promotion/ads-manager.md) |
| Portal ads | Acquisition from [portal ads](/docs/en-us/production/monetization/immersive-ads.md#portal-ads) |
| Teleport | Traffic coming from another game through [teleporting](/docs/en-us/projects/teleport.md) |
| Other | All other traffic with unknown sources or can't be attributed, including the traffic from external sources |

> **Info:** If your game has [Exclude from Recommendations](/docs/en-us/production/publishing/publish-games-and-places.md#audience) enabled, all other analytics remain available, but **Home recommendations** metrics are zero; games excluded from recommendations aren't included in **Recommended For You**, so they can't receive any traffic from it.
## Acquisition attribution

You can view the acquisition dashboard by [acquisition source](#acquisition-sources) or by [share links](/docs/en-us/production/promotion/share-links.md). The dashboard categorizes results for both views as follows:

| Attribution | Description |
| --- | --- |
| Users with plays | Unique new users with plays on the game. |
| Conversion rate | Percent of new users who played your game after viewing an impression. |
| D7 retention | Percentage of new players acquired in the date range who played again on the 8th day (D8) after their first session ended. |
| 7D playtime per user (cumulative) | Cumulative playtime for new players acquired in the date range in their first 7 days divided by the number of new players acquired in the date range. |
| 30D payer conversion (cumulative) | Number of paying users from new players acquired in the date range in their first 30 days divided by the number of new players acquired in the date range. |
| 30D revenue per user (cumulative) | Cumulative revenue, excluding subscriptions, engagement payouts, and immersive ads, for new players acquired in the date range in their first 30 days divided by the number of new players acquired in the date range. |

![Chart indicating new users funnel by acquisition source.](../../assets/analytics/acquisition/New-Users-Funnel.png) ## Improve acquisition

To improve acquisition, you can run an acquisition funnel to identify sources that might drive more traffic or convert better, such as:

- The sources driving **the most number of new users** to your game.
- The sources with the best **end-to-end conversion rate**.

### Improve acquisition from Roblox sources

Among all Roblox sources, **Home** is usually where the vast majority of users find games. To improve your game's discovery on Home:

1. **Improve engagement and retention.** Get your [session time](/docs/en-us/production/analytics/engagement.md#improve-average-session-time) and [day 1 retention](/docs/en-us/production/analytics/retention.md#improve-day-1-retention) to be comparable or above your similar game benchmarks. The algorithm cares about these metrics because they signal how engaging and satisfying your game is for users.
2. **Optimize monetization.** Get your [payer conversion](/docs/en-us/production/analytics/monetization.md#improve-payer-conversion-rate) rate and [ARPPU](/docs/en-us/production/analytics/monetization.md#improve-average-revenue-per-paying-user-arppu) (average revenue per paying user) to be comparable or above your similar game benchmarks. The algorithm cares about these metrics because they measure how invested users are in your game.

![An example shows the statistics by unique users with impressions and unique users with plays by source.](../../assets/analytics/acquisition/Unique-Users-by-Source.png)

You can adopt the following strategies to improve the number of users visiting your game from Roblox sources, including **Home**, **Discover**, and **Search**:

1. **Improve your retention**: Day 1 retention signals how engaging and satisfying your game is for users. Games with high Day 1 retention are more likely to be featured in **Recommended Experiences**. For more information on improving Day 1 retention, see [Day 1 retention](/docs/en-us/production/analytics/retention.md#improve-day-1-retention).
2. **Grow your engagement**. Average session time measures how much time users spend in your game and signals how much users enjoy your content. Games with high average session time are more likely to be featured in **Recommended Experiences**.

For more information on Roblox sources and best practices on improving the discovery of your game, see [Discovery](/docs/en-us/discovery.md).

### Improve play through rate from Roblox sources

You can get more users to convert by making your game metadata engaging and accurate:

1. **Use a title, description, and icon** that's true and unique to your game.
2. **Add images and videos** to your game detail page to engage users.

## Improve acquisition from external sources

Here are some tips to get users to visit your game from external sources:

1. **Create social accounts and post regularly**: Add social accounts such as Twitter, YouTube, and Instagram to your Roblox Game Detail Page. Share regular updates, teasers, and screenshots to build buzz for your game. Reply to other large social accounts to grow your following.
2. **Create a user community**: Users in your community can share feedback, suggestions, bug reports, fan art, and more. Engage with your community regularly by hosting events and replying to comments and suggestions.
3. **Partner with other creators and influencers**: You can partner with other creators who make similar games to grow together. You can also reach out to influencers who have large followings on platforms like YouTube or Twitch to see if they're willing to use or review your game.
4. **Create [share links](/docs/en-us/production/promotion/share-links.md)**: Track your off-platform user acquisition and use the **New users funnel** table to understand:
  - **Users with qualified plays**: How many new users are joining from each link?
  - **7-day playtime per user**: Which links are bringing in users who engage the most?
  - **D7 retention**: Which platforms drive users that keep coming back?
  - **30-day revenue per user**: Which channels are attracting users who spend in-game?

![Chart indicating new users funnel by share links.](../../assets/analytics/acquisition/Share-Link-Acquisition-Dashboard.png)
