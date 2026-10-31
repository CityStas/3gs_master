---
title: "Event types"
url: /docs/en-us/production/analytics/event-types
last_updated: 2026-10-30T19:55:47Z
description: "Overview of using event types to track user sources, sinks and milestones in your game."
---

# Event types

Event types help you identify opportunities to grow and monetize your game. They allow you to integrate event tracking into your game and visualize your in-game economy and player usage patterns on the Analytics dashboard

After you begin tracking these events from your game using `Class.AnalyticsService`, you unlock new [economy](/docs/en-us/production/analytics/economy-events.md), [funnel](/docs/en-us/production/analytics/funnel-events.md), and [custom](/docs/en-us/production/analytics/custom-events.md) dashboards under Analytics on the Creator Dashboard. You can use these dashboards to identify growth opportunities and segment users by age, gender, platform, OS and custom fields. All of these features are **free to use**.

![Economy and Funnels dashboard pages populated with data.](../../assets/analytics/event-types/Overview-Economy-Funnels.png) ## Event types

Roblox provides three sets of analytic dashboards you can use to track different aspects of your game:

1. **Economy events** let you track your in-game economy, such as:
  - **Top sinks** — What do users spend in-game resources on?
  - **Top sources** — Where do users earn resources?
  - **Average wallet balance** — How many resources are users holding?
2. **Funnel events** let you track your user's progress through key stages of your game, such as:
  - **Onboarding** — Where do users drop off when getting started with your game?
  - **Progression** — Where do users stop advancing through your game?
  - **Shop** — Where do users abandon purchases?
3. **Custom events** let you track metrics specific to your game, such as:
  - **Adoption** — How many users click on a specific UI component?
  - **User behavior** — What is the most frequently used ability on each map?
  - **Core loop** — How do kill/death ratios compare across different weapons?

For more information on setting up these dashboards, see [Economy events](/docs/en-us/production/analytics/economy-events.md), [Funnel events](/docs/en-us/production/analytics/funnel-events.md) and [Custom events](/docs/en-us/production/analytics/custom-events.md).

## Validate your event tracking

Once you add [economy](/docs/en-us/production/analytics/economy-events.md), [funnel](/docs/en-us/production/analytics/funnel-events.md), or [custom](/docs/en-us/production/analytics/custom-events.md) events to your game, charts on the respective pages typically take 24 hours to appear. In the meantime, you can check if events are set up correctly using the **View Events** tool:

1. Navigate to the **Economy**, **Funnel**, or **Custom** pages of your Analytics dashboard for your game.
2. Click the **View Events** button at the top of each page. A near real-time list of the most recent events displays.
3. Refresh the page to update the list.

![View events report displaying multiple event entries sortable by event type, user ID and keyword.](../../assets/analytics/event-types/Event-Tracking.png)

If you see more events than you were expecting, verify that your calls to the `Class.AnalyticsService` methods occur **after** a successful operation. For example, you should call `Class.AnalyticsService:LogEconomyEvent()|LogEconomyEvent()` after a successful purchase, not when the user attempts a purchase (which could fail due to lack of funds).

You can also visit your game's [error report](/docs/en-us/production/analytics/error-report.md) to see if there are any errors with your event tracking.

## Event tracking limitations

The following limitations apply when tracking your events with `Class.AnalyticsService`. Limitations reset daily. You will be able to send new events the next day once you stop sending previous events. Each event remains visible on the Creator Dashboard and automatically rolls off after 90 days from the last data received.

> **Warning:** You can leverage [custom fields](/docs/en-us/production/analytics/custom-fields.md) to additionally filter your analytic events.
>
> For example, instead of tracking `WarriorXP`, `MageXP`, `PaladinXP` as separate economy currencies, set `XP` as one currency and set `Warrior`, `Mage`, `Paladin`, `...`, as Custom Field 1. This allows you to break down these values on your dashboards and not use up your currency cardinality.

|  | **Limitation** | **Maximum value** | **Examples** |
| --- | --- | --- | --- |
| Global Rate Limit | Total `Class.AnalyticsService` requests per minute | 120 + (20 * CCU) | |
|  |  |  | |
| Economy, Funnel, and Custom events | Number of [custom fields](/docs/en-us/production/analytics/custom-fields.md) | 3 | Class, Level, Weapon |
| Unique values per [custom field](/docs/en-us/production/analytics/custom-fields.md) | Unlimited — After 8,000 combined values across all custom fields, values will be grouped as "Other" | Warrior, Mage, Archer |
| Economy only | Resource types | 10 | Coins, Gold, Credits |
| transactionTypes | Unlimited — After 20, values will be grouped as "Other" | IAP, Gameplay |
| itemSkus | Unlimited — After 100, values will be grouped as "Other" | |
| Funnel only | Number of funnels | 10 | Onboarding, Shop |
| Steps per funnel | 100 | Step 1, Step 2, Step 3 |
| Custom only | eventNames | 100 | MonsterDefeated, KillDeathRatio, PetAdoption |
