---
title: "Search ads"
url: /docs/en-us/production/promotion/search-ads
last_updated: 2026-10-30T19:55:50Z
description: "Search ads promote games in the search results of Roblox's game catalog."
---

# Search ads

**Search ads** enable creators and brands to promote their games to users searching for specific keywords on Roblox. This form of advertising allows developers to target their ads to users using search, increasing the likelihood of engagement.

When creating a search ad, advertisers select up to 10 keywords within an Ad Set relevant to their games. Once a successful search ad is applied and launched, your game displays as a search result if a user submits a search with an exact keyword match.

Search results populate in the following ways:

_ Search ads display at the top of search results._

_ For queries that directly match a game name, such as "Driving Empire", the exact match appears as the primary enlarged tile, and search ads display immediately after._

_ Search ads on desktop._

> **Warning:** All Roblox advertisers of games must abide by our [Community Standards](https://en.help.roblox.com/hc/en-us/articles/203313410-Roblox-Community-Standards). Roblox prevents surfacing games identified as clickbait or spam.
## Create search ads

Search ads are managed in the [Ads Manager](/docs/en-us/production/promotion/ads-manager.md) as a Visits campaign objective. Search ads also use a [modified bidding and auction](#bidding-and-auction) process to determine pricing and availability of individual keywords.

> **Warning:** Unlike other ad types, you can't modify brand suitability and audience targeting for search ads. Search ads reach audiences in all regions, all genders, ages 13 and over, and all eligible devices.

To create search ads:

1. Navigate to the [Ads Manager](https://advertise.roblox.com/landing). If it's your first time creating an ad campaign, you must first [create an account](/docs/en-us/production/promotion/ads-manager.md#create-an-ad-account) and [add a payment method](/docs/en-us/production/promotion/ads-manager.md#add-a-payment-method).
2. In **Manage Ads**, click **CREATE**.
3. In the Campaign page:
  1. Select your **Payment Method**.
  2. Set **Campaign Objective** to **Visits**.
  3. Set the **budget type**, **date range**, and **campaign name**.
  4. Click **NEXT**.
4. In the Ad Set page:
  1. Select **Search Experience**. The audience estimation shows the approximate number of Roblox user accounts your search ad might reach over a month. This number is based on the keywords you choose and the budget and bids you set when creating your ad.
  2. In **Keyword(s)**, choose up to 10 keywords for each Ad Set. Keywords populate after typing in the text field. You should group relevant keywords together within each Ad Set for clearer reporting on campaign performance.
  3. Click **NEXT**.
5. In the Ad page:
  1. Set your **Destination Experience**. This is the game that users are directed to after clicking on the search ad.
  2. Enter a name for this specific ad.
  3. Click **NEXT**.
6. In the Review Campaign page, review the final details of your advertisement and click **SUBMIT** to launch your campaign.

After launching your campaign, you can monitor the campaign's performance with [ads reporting](#reporting) and [billing](/docs/en-us/production/promotion/ads-manager.md#billing).

## Bidding and auction

Ads on Roblox work in a bidding system, where advertisers bid to have their ads shown to users through the available ad units placed in a game. Search ads differ from other ads in that they also calculate the relevance of the game to the user's query. **This means that games that are more relevant to a search query have a greater chance of displaying as ads**.

To maximize user experience and make the most of your ad spend, **you should bid on keywords that are most relevant to your game**. For instance, if you have a horror game and you bid on the keyword "obby", you could get some initial traffic from this ad, but the ad system will ultimately optimize for ads that are most relevant for your game.

The following is the [same bidding and auction information](/docs/en-us/production/promotion/ads-manager.md#bidding-and-auction) provided for other advertising formats with the specific differences for search ads bolded:

> All eligible ads participate in a second price auction. The ad with the highest bid wins the ad slot, but only charges the price of the second highest price, plus one cent. In principle, this looks like: 1. Advertisers submit their bids for ad space. 2. Roblox calculates an adjusted eCPM value for each Ad, based on the player, ad, **and query information. The adjusted eCPM accounts for the relevance of the Ad to the chosen keyword.**3. The ads are then placed into an auction. 4. The ad with the **highest adjusted eCPM** value wins the auction. 5. The winning ad is then displayed to the player. 6. The advertiser is charged its bid amount of the second highest price, plus one cent ($0.01). 7. The advertiser is charged the bid amount of the **second highest ranked ad, adjusted by how much better the ad scored in the auction relative to the next highest ranked ad**, plus one cent ($0.01).
>
> As an example: 1. An advertiser wants to display their ad. 2. The advertiser submits a bid of $10. 3. Another advertiser submits a bid of $12. 4. The second advertiser wins the auction and is charged $10.01, the price of the second highest bid, plus one cent.
## Reporting

You can review your ad campaign's performance using the Ad Manager's [ads reporting tool](/docs/en-us/production/promotion/ads-manager.md#reporting). At this time, you can't filter reports by keywords, but you can create ad sets with a single keyword to compare how an individual keyword performs for your campaign.

Search ad metrics also populate in the [Analytics Dashboard](/docs/en-us/production/analytics/acquisition.md#acquisition-sources) acquisition metrics. At this time, search ad and sponsored ad results are combined as a single Sponsored Ad metric on acquisition reports.
