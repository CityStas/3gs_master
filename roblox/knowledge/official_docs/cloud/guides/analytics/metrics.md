---
title: "Supported metrics and dimensions"
url: /docs/en-us/cloud/guides/analytics/metrics
last_updated: 2026-10-30T19:55:39Z
description: "Lists supported metrics and dimensions for the Open Cloud Analytics API."
---

# Supported metrics and dimensions

The Analytics Query API supports numerous metrics and dimensions. Refer to the following tables for the comprehensive list. All values are case-sensitive.

## Supported metrics

### Retention

See [Retention](/docs/en-us/production/analytics/retention.md).

| Name | Metric | Supported dimensions |
| --- | --- | --- |
| Day 1 retention | `ForwardD1Retention`<br><br>**Granularities:** OneDay<br>**Data retention:** 1468 days | <ul><li>`AcquisitionSource`</li><li>`AgeGroupV2`</li><li>`Country`</li><li>`Gender`</li><li>`Locale`</li><li>`OperatingSystem`</li><li>`Platform`</li><li>`UserO18Eligibility`</li><li>`UserSegmentationAccountAge`</li><li>`UserSegmentationActivationStatus`</li><li>`UserSegmentationEngagementLevel`</li><li>`UserSegmentationPayerStatus`</li><li>`UserSegmentationPlatformActivationStatus`</li><li>`UserSegmentationPlatformSpenderStatus`</li></ul> |
| Day 7 retention | `ForwardD7Retention`<br><br>**Granularities:** OneDay<br>**Data retention:** 1468 days | <ul><li>`AcquisitionSource`</li><li>`AgeGroupV2`</li><li>`Country`</li><li>`Gender`</li><li>`Locale`</li><li>`OperatingSystem`</li><li>`Platform`</li><li>`UserO18Eligibility`</li><li>`UserSegmentationAccountAge`</li><li>`UserSegmentationActivationStatus`</li><li>`UserSegmentationEngagementLevel`</li><li>`UserSegmentationPayerStatus`</li><li>`UserSegmentationPlatformActivationStatus`</li><li>`UserSegmentationPlatformSpenderStatus`</li></ul> |
| Day 30 retention | `ForwardD30Retention`<br><br>**Granularities:** OneDay<br>**Data retention:** 1468 days | <ul><li>`AcquisitionSource`</li><li>`AgeGroupV2`</li><li>`Country`</li><li>`Gender`</li><li>`Locale`</li><li>`OperatingSystem`</li><li>`Platform`</li><li>`UserO18Eligibility`</li><li>`UserSegmentationAccountAge`</li><li>`UserSegmentationActivationStatus`</li><li>`UserSegmentationEngagementLevel`</li><li>`UserSegmentationPayerStatus`</li><li>`UserSegmentationPlatformActivationStatus`</li><li>`UserSegmentationPlatformSpenderStatus`</li></ul> |
| Daily cohort retention | `DailyCohortRetention`<br><br>**Granularities:** None, OneDay<br>**Data retention:** 1468 days | <ul><li>`AcquisitionSource`</li><li>`AgeGroupV2`</li><li>`CohortDay`</li><li>`Country`</li><li>`Gender`</li><li>`Locale`</li><li>`OperatingSystem`</li><li>`Platform`</li><li>`UserSegmentationAccountAge`</li><li>`UserSegmentationActivationStatus`</li><li>`UserSegmentationEngagementLevel`</li><li>`UserSegmentationPayerStatus`</li><li>`UserSegmentationPlatformActivationStatus`</li><li>`UserSegmentationPlatformSpenderStatus`</li></ul> |
| Weekly cohort retention | `WeeklyCohortRetention`<br><br>**Granularities:** None, OneWeek<br>**Data retention:** 1468 days | <ul><li>`AcquisitionSource`</li><li>`AgeGroupV2`</li><li>`CohortWeek`</li><li>`Country`</li><li>`Gender`</li><li>`Locale`</li><li>`OperatingSystem`</li><li>`Platform`</li><li>`UserSegmentationAccountAge`</li><li>`UserSegmentationActivationStatus`</li><li>`UserSegmentationEngagementLevel`</li><li>`UserSegmentationPayerStatus`</li><li>`UserSegmentationPlatformActivationStatus`</li><li>`UserSegmentationPlatformSpenderStatus`</li></ul> |
| Stickiness (DAU/MAU) | `DauMauStickiness`<br><br>**Granularities:** OneDay<br>**Data retention:** 1468 days | <ul><li>`AgeGroupV2`</li><li>`Country`</li><li>`Gender`</li><li>`Locale`</li><li>`OperatingSystem`</li><li>`Platform`</li><li>`UserO18Eligibility`</li><li>`UserSegmentationAccountAge`</li><li>`UserSegmentationActivationStatus`</li><li>`UserSegmentationEngagementLevel`</li><li>`UserSegmentationPayerStatus`</li><li>`UserSegmentationPlatformActivationStatus`</li><li>`UserSegmentationPlatformSpenderStatus`</li></ul> |

### Engagement

See [Engagement](/docs/en-us/production/analytics/engagement.md).

| Name | Metric | Supported dimensions |
| --- | --- | --- |
| Average playtime | `AveragePlayTimeMinutesPerDAU`<br><br>**Granularities:** OneDay, OneWeek, OneMonth, None<br>**Data retention:** 1468 days | <ul><li>`AgeGroupV2`</li><li>`Country`</li><li>`Gender`</li><li>`IsNewUser`</li><li>`Locale`</li><li>`OperatingSystem`</li><li>`Platform`</li><li>`UserO18Eligibility`</li><li>`UserSegmentationAccountAge`</li><li>`UserSegmentationActivationStatus`</li><li>`UserSegmentationEngagementLevel`</li><li>`UserSegmentationPayerStatus`</li><li>`UserSegmentationPlatformActivationStatus`</li><li>`UserSegmentationPlatformSpenderStatus`</li></ul> |
| Average session time | `AverageSessionLengthMinutes`<br><br>**Granularities:** OneDay, OneWeek, OneMonth, None<br>**Data retention:** 1468 days | <ul><li>`AgeGroupV2`</li><li>`Country`</li><li>`Gender`</li><li>`IsNewUser`</li><li>`Locale`</li><li>`OperatingSystem`</li><li>`Platform`</li><li>`UserO18Eligibility`</li><li>`UserSegmentationAccountAge`</li><li>`UserSegmentationActivationStatus`</li><li>`UserSegmentationEngagementLevel`</li><li>`UserSegmentationPayerStatus`</li><li>`UserSegmentationPlatformActivationStatus`</li><li>`UserSegmentationPlatformSpenderStatus`</li></ul> |
| Daily active users | `DailyActiveUsers`<br><br>**Granularities:** OneDay, OneWeek, OneMonth, None<br>**Data retention:** 1468 days | <ul><li>`AcquisitionSource`</li><li>`AgeGroupV2`</li><li>`Country`</li><li>`Gender`</li><li>`IsNewUser`</li><li>`Locale`</li><li>`OperatingSystem`</li><li>`Platform`</li><li>`UserO18Eligibility`</li><li>`UserSegmentationAccountAge`</li><li>`UserSegmentationActivationStatus`</li><li>`UserSegmentationEngagementLevel`</li><li>`UserSegmentationPayerStatus`</li><li>`UserSegmentationPlatformActivationStatus`</li><li>`UserSegmentationPlatformSpenderStatus`</li></ul> |
| Monthly active users | `MonthlyActiveUsers`<br><br>**Granularities:** OneDay<br>**Data retention:** 1468 days | <ul><li>`AgeGroupV2`</li><li>`Country`</li><li>`Gender`</li><li>`IsNewUser`</li><li>`Locale`</li><li>`OperatingSystem`</li><li>`Platform`</li><li>`UserO18Eligibility`</li><li>`UserSegmentationAccountAge`</li><li>`UserSegmentationActivationStatus`</li><li>`UserSegmentationEngagementLevel`</li><li>`UserSegmentationPayerStatus`</li><li>`UserSegmentationPlatformActivationStatus`</li><li>`UserSegmentationPlatformSpenderStatus`</li></ul> |
| Playtime | `TotalPlayTimeHours`<br><br>**Granularities:** OneDay, OneWeek, OneMonth, None<br>**Data retention:** 1468 days | <ul><li>`AgeGroupV2`</li><li>`Country`</li><li>`Gender`</li><li>`IsNewUser`</li><li>`Locale`</li><li>`OperatingSystem`</li><li>`Platform`</li><li>`UserO18Eligibility`</li><li>`UserSegmentationAccountAge`</li><li>`UserSegmentationActivationStatus`</li><li>`UserSegmentationEngagementLevel`</li><li>`UserSegmentationPayerStatus`</li><li>`UserSegmentationPlatformActivationStatus`</li><li>`UserSegmentationPlatformSpenderStatus`</li></ul> |
| New user first session retention | `TotalSessionsEndedInBucket`<br><br>**Granularities:** OneDay, OneWeek, OneMonth, None<br>**Data retention:** 1468 days | <ul><li>`AgeGroupV2`</li><li>`Gender`</li><li>`OperatingSystem`</li><li>`Platform`</li><li>`SessionTimeBucket`</li><li>`UserSegmentationAccountAge`</li><li>`UserSegmentationActivationStatus`</li><li>`UserSegmentationEngagementLevel`</li><li>`UserSegmentationPayerStatus`</li><li>`UserSegmentationPlatformActivationStatus`</li><li>`UserSegmentationPlatformSpenderStatus`</li></ul> |
| Sessions | `Visits`<br><br>**Granularities:** OneDay, OneWeek, OneMonth, None<br>**Data retention:** 1468 days | <ul><li>`AgeGroupV2`</li><li>`Country`</li><li>`Gender`</li><li>`IsNewUser`</li><li>`Locale`</li><li>`OperatingSystem`</li><li>`Platform`</li><li>`UserO18Eligibility`</li><li>`UserSegmentationAccountAge`</li><li>`UserSegmentationActivationStatus`</li><li>`UserSegmentationEngagementLevel`</li><li>`UserSegmentationPayerStatus`</li><li>`UserSegmentationPlatformActivationStatus`</li><li>`UserSegmentationPlatformSpenderStatus`</li></ul> |

### Monetization

See [Monetization](/docs/en-us/production/analytics/monetization.md).

| Name | Metric | Supported dimensions |
| --- | --- | --- |
| Average revenue per paying user (ARPPU) | `AverageRevenuePerPayingUser`<br><br>**Granularities:** OneDay, OneWeek, OneMonth, None<br>**Data retention:** 1468 days | <ul><li>`AgeGroupV2`</li><li>`Country`</li><li>`Gender`</li><li>`Locale`</li><li>`OperatingSystem`</li><li>`Platform`</li><li>`UserO18Eligibility`</li><li>`UserSegmentationAccountAge`</li><li>`UserSegmentationActivationStatus`</li><li>`UserSegmentationEngagementLevel`</li><li>`UserSegmentationPayerStatus`</li><li>`UserSegmentationPlatformActivationStatus`</li><li>`UserSegmentationPlatformSpenderStatus`</li></ul> |
| Average revenue per DAU (ARPDAU) | `AverageRevenuePerUser`<br><br>**Granularities:** OneDay, OneWeek, OneMonth, None<br>**Data retention:** 1468 days | <ul><li>`AgeGroupV2`</li><li>`Country`</li><li>`Gender`</li><li>`Locale`</li><li>`OperatingSystem`</li><li>`Platform`</li><li>`UserO18Eligibility`</li><li>`UserSegmentationAccountAge`</li><li>`UserSegmentationActivationStatus`</li><li>`UserSegmentationEngagementLevel`</li><li>`UserSegmentationPayerStatus`</li><li>`UserSegmentationPlatformActivationStatus`</li><li>`UserSegmentationPlatformSpenderStatus`</li></ul> |
| Revenue | `DailyRevenue`<br><br>**Granularities:** OneDay, OneWeek, OneMonth, None<br>**Data retention:** 1468 days | <ul><li>`AgeGroupV2`</li><li>`BalanceType`</li><li>`Country`</li><li>`Gender`</li><li>`Locale`</li><li>`OperatingSystem`</li><li>`Platform`</li><li>`RevenueSource`</li><li>`UserO18Eligibility`</li><li>`UserSegmentationAccountAge`</li><li>`UserSegmentationActivationStatus`</li><li>`UserSegmentationEngagementLevel`</li><li>`UserSegmentationPayerStatus`</li><li>`UserSegmentationPlatformActivationStatus`</li><li>`UserSegmentationPlatformSpenderStatus`</li></ul> |
| Robux Spent (Realtime) | `ItemMonetizationRevenue`<br><br>**Granularities:** OneHour, OneDay, None<br>**Data retention:** 1468 days | <ul><li>`CollectibleItemTargetType`</li><li>`CollectibleItemTargetTypeId`</li><li>`CollectibleItemType`</li><li>`ProductKey`</li><li>`ProductType`</li><li>`SalesLocation`</li></ul> |
| Paying users | `PayingUsers`<br><br>**Granularities:** OneDay, OneWeek, OneMonth, None<br>**Data retention:** 1468 days | <ul><li>`AgeGroupV2`</li><li>`Country`</li><li>`Gender`</li><li>`Locale`</li><li>`OperatingSystem`</li><li>`Platform`</li><li>`UserO18Eligibility`</li><li>`UserSegmentationAccountAge`</li><li>`UserSegmentationActivationStatus`</li><li>`UserSegmentationEngagementLevel`</li><li>`UserSegmentationPayerStatus`</li><li>`UserSegmentationPlatformActivationStatus`</li><li>`UserSegmentationPlatformSpenderStatus`</li></ul> |
| Payer conversion rate | `PayingUsersCVR`<br><br>**Granularities:** OneDay, OneWeek, OneMonth, None<br>**Data retention:** 1468 days | <ul><li>`AgeGroupV2`</li><li>`Country`</li><li>`Gender`</li><li>`Locale`</li><li>`OperatingSystem`</li><li>`Platform`</li><li>`UserO18Eligibility`</li><li>`UserSegmentationAccountAge`</li><li>`UserSegmentationActivationStatus`</li><li>`UserSegmentationEngagementLevel`</li><li>`UserSegmentationPayerStatus`</li><li>`UserSegmentationPlatformActivationStatus`</li><li>`UserSegmentationPlatformSpenderStatus`</li></ul> |

### Acquisition

See [Acquisition](/docs/en-us/production/analytics/acquisition.md).

| Name | Metric | Supported dimensions |
| --- | --- | --- |
| Users detail page CTR | `ClickCVR`<br><br>**Granularities:** OneDay, None<br>**Data retention:** 1468 days | <ul><li>`AcquisitionSource`</li><li>`AgeGroupV2`</li><li>`Gender`</li><li>`IsNewUser`</li><li>`OperatingSystem`</li><li>`Platform`</li><li>`UserSegmentationPlatformActivationStatus`</li><li>`UserSegmentationPlatformSpenderStatus`</li></ul> |
| Play rate per unique user | `EndToEndCVR`<br><br>**Granularities:** OneDay, None<br>**Data retention:** 1468 days | <ul><li>`AcquisitionSource`</li><li>`AgeGroupV2`</li><li>`Gender`</li><li>`IsNewUser`</li><li>`OperatingSystem`</li><li>`Platform`</li><li>`UserSegmentationPlatformActivationStatus`</li><li>`UserSegmentationPlatformSpenderStatus`</li></ul> |
| Users impression CTR | `ImpressionCVR`<br><br>**Granularities:** OneDay, None<br>**Data retention:** 1468 days | <ul><li>`AcquisitionSource`</li><li>`AgeGroupV2`</li><li>`Gender`</li><li>`IsNewUser`</li><li>`OperatingSystem`</li><li>`Platform`</li><li>`UserSegmentationPlatformActivationStatus`</li><li>`UserSegmentationPlatformSpenderStatus`</li></ul> |
| Qualified play through rate per user | `QualifiedEndToEndCVR`<br><br>**Granularities:** OneDay, None<br>**Data retention:** 1468 days | <ul><li>`AcquisitionSource`</li><li>`AgeGroupV2`</li><li>`Gender`</li><li>`IsNewUser`</li><li>`OperatingSystem`</li><li>`Platform`</li><li>`UserSegmentationPlatformActivationStatus`</li><li>`UserSegmentationPlatformSpenderStatus`</li></ul> |
| Unique users with qualified plays | `QualifiedUniqueUsersWithPlaySessions`<br><br>**Granularities:** OneDay, None, OneWeek<br>**Data retention:** 1468 days | <ul><li>`AcquisitionSource`</li><li>`AgeGroupV2`</li><li>`FunnelSource`</li><li>`Gender`</li><li>`IsNewUser`</li><li>`OperatingSystem`</li><li>`Platform`</li><li>`UserSegmentationPlatformActivationStatus`</li><li>`UserSegmentationPlatformSpenderStatus`</li></ul> |
| Users with detail page visits | `UniqueUsersWithClicks`<br><br>**Granularities:** OneDay, None<br>**Data retention:** 1468 days | <ul><li>`AcquisitionSource`</li><li>`AgeGroupV2`</li><li>`Gender`</li><li>`IsNewUser`</li><li>`OperatingSystem`</li><li>`Platform`</li><li>`UserSegmentationPlatformActivationStatus`</li><li>`UserSegmentationPlatformSpenderStatus`</li></ul> |
| Unique users with impressions | `UniqueUsersWithImpressions`<br><br>**Granularities:** OneDay, None<br>**Data retention:** 1468 days | <ul><li>`AcquisitionSource`</li><li>`AgeGroupV2`</li><li>`Gender`</li><li>`IsNewUser`</li><li>`OperatingSystem`</li><li>`Platform`</li><li>`UserSegmentationPlatformActivationStatus`</li><li>`UserSegmentationPlatformSpenderStatus`</li></ul> |
| Unique users with plays | `UniqueUsersWithPlaySessions`<br><br>**Granularities:** OneDay, None, OneWeek<br>**Data retention:** 1468 days | <ul><li>`AcquisitionSource`</li><li>`AgeGroupV2`</li><li>`FunnelSource`</li><li>`Gender`</li><li>`IsNewUser`</li><li>`OperatingSystem`</li><li>`Platform`</li><li>`UserSegmentationPlatformActivationStatus`</li><li>`UserSegmentationPlatformSpenderStatus`</li></ul> |

### Home recommendation signals

See [Discovery](/docs/en-us/discovery.md#understand-your-metrics-in-creator-analytics).

| Name | Metric | Supported dimensions |
| --- | --- | --- |
| Play through rate | `RFYPlayThroughRate`<br><br>**Granularities:** OneDay<br>**Data retention:** 1468 days | <ul><li>`AgeGroupV2`</li><li>`Gender`</li></ul> |
| First play bounce rate (0-60s) | `RFYDuration0To60`<br><br>**Granularities:** OneDay<br>**Data retention:** 1468 days | <ul><li>`AgeGroupV2`</li><li>`Gender`</li></ul> |
| First play bounce rate (61-180s) | `RFYDuration61To180`<br><br>**Granularities:** OneDay<br>**Data retention:** 1468 days | <ul><li>`AgeGroupV2`</li><li>`Gender`</li></ul> |
| Play days per user (days 2-7) | `RFYD2To7PlayDays`<br><br>**Granularities:** OneDay<br>**Data retention:** 1468 days | <ul><li>`AgeGroupV2`</li><li>`Gender`</li></ul> |
| Play days per user (days 8-28) | `RFYD8To28PlayDays`<br><br>**Granularities:** OneDay<br>**Data retention:** 1468 days | <ul><li>`AgeGroupV2`</li><li>`Gender`</li></ul> |
| Playtime per user (day 1) | `RFYD1Playtime`<br><br>**Granularities:** OneDay<br>**Data retention:** 1468 days | <ul><li>`AgeGroupV2`</li><li>`Gender`</li></ul> |
| Playtime per user (days 2-7) | `RFYD2To7Playtime`<br><br>**Granularities:** OneDay<br>**Data retention:** 1468 days | <ul><li>`AgeGroupV2`</li><li>`Gender`</li></ul> |
| Playtime per user (days 8-28) | `RFYD8To28Playtime`<br><br>**Granularities:** OneDay<br>**Data retention:** 1468 days | <ul><li>`AgeGroupV2`</li><li>`Gender`</li></ul> |
| Intentional co-play days per user (day 1) | `RFYD1CoplayDays`<br><br>**Granularities:** OneDay<br>**Data retention:** 1468 days | <ul><li>`AgeGroupV2`</li><li>`Gender`</li></ul> |
| Intentional co-play days per user (days 2-7) | `RFYD2To7CoplayDays`<br><br>**Granularities:** OneDay<br>**Data retention:** 1468 days | <ul><li>`AgeGroupV2`</li><li>`Gender`</li></ul> |
| Intentional co-play days per user (days 8-28) | `RFYD8To28CoplayDays`<br><br>**Granularities:** OneDay<br>**Data retention:** 1468 days | <ul><li>`AgeGroupV2`</li><li>`Gender`</li></ul> |
| Qualified play sessions per user (day 1) | `RFYD1QualifiedPlaySessions`<br><br>**Granularities:** OneDay<br>**Data retention:** 1468 days | <ul><li>`AgeGroupV2`</li><li>`Gender`</li></ul> |
| Qualified play sessions per user (days 2-7) | `RFYD2To7QualifiedPlaySessions`<br><br>**Granularities:** OneDay<br>**Data retention:** 1468 days | <ul><li>`AgeGroupV2`</li><li>`Gender`</li></ul> |
| Qualified play sessions per user (days 8-28) | `RFYD8To28QualifiedPlaySessions`<br><br>**Granularities:** OneDay<br>**Data retention:** 1468 days | <ul><li>`AgeGroupV2`</li><li>`Gender`</li></ul> |
| Spend days per user (day 1) | `RFYD1SpendDay`<br><br>**Granularities:** OneDay<br>**Data retention:** 1468 days | <ul><li>`AgeGroupV2`</li><li>`Gender`</li></ul> |
| Spend days per user (days 2-7) | `RFYD2To7SpendDays`<br><br>**Granularities:** OneDay<br>**Data retention:** 1468 days | <ul><li>`AgeGroupV2`</li><li>`Gender`</li></ul> |
| Spend days per user (days 8-28) | `RFYD8To28SpendDays`<br><br>**Granularities:** OneDay<br>**Data retention:** 1468 days | <ul><li>`AgeGroupV2`</li><li>`Gender`</li></ul> |
| Robux spent per user (day 1) | `RFYD1RobuxSpend`<br><br>**Granularities:** OneDay<br>**Data retention:** 1468 days | <ul><li>`AgeGroupV2`</li><li>`Gender`</li></ul> |
| Robux spent per user (days 2-7) | `RFYD2To7RobuxSpend`<br><br>**Granularities:** OneDay<br>**Data retention:** 1468 days | <ul><li>`AgeGroupV2`</li><li>`Gender`</li></ul> |
| Robux spent per user (days 8-28) | `RFYD8To28RobuxSpend`<br><br>**Granularities:** OneDay<br>**Data retention:** 1468 days | <ul><li>`AgeGroupV2`</li><li>`Gender`</li></ul> |

### Performance & Stability

See [Performance](/docs/en-us/production/analytics/performance.md).

| Name | Metric | Supported dimensions |
| --- | --- | --- |
| Client CPU time | `ClientCpuTimeAvg`<br><br>**Granularities:** OneMinute, HalfHour, OneHour, OneDay<br>**Data retention:** 28 days | <ul><li>`ClientCpuTimeCategory`</li><li>`ClientCpuTimeSubCategory`</li><li>`MemoryGroup`</li><li>`OperatingSystem`</li><li>`Place`</li><li>`PlaceVersion`</li><li>`Platform`</li></ul> |
| Client crash count | `ClientCrashCount`<br><br>**Granularities:** OneMinute, HalfHour, OneHour, OneDay<br>**Data retention:** 28 days | <ul><li>`MemoryGroup`</li><li>`OperatingSystem`</li><li>`Place`</li><li>`PlaceVersion`</li><li>`Platform`</li></ul> |
| Client crash rate | `ClientCrashRate15m`<br><br>**Granularities:** OneMinute, HalfHour, OneHour, OneDay<br>**Data retention:** 28 days | <ul><li>`MemoryGroup`</li><li>`OperatingSystem`</li><li>`Place`</li><li>`PlaceVersion`</li><li>`Platform`</li></ul> |
| Client frame rate | `ClientFpsAvg`<br>`ClientFpsP10`<br>`ClientFpsP50`<br>`ClientFpsP90`<br><br>**Granularities:** OneMinute, HalfHour, OneHour, OneDay<br>**Data retention:** 28 days | <ul><li>`MemoryGroup`</li><li>`OperatingSystem`</li><li>`Place`</li><li>`PlaceVersion`</li><li>`Platform`</li></ul> |
| Client memory usage | `ClientMemoryUsageAvg`<br>`ClientMemoryUsageP10`<br>`ClientMemoryUsageP50`<br>`ClientMemoryUsageP90`<br><br>**Granularities:** OneMinute, HalfHour, OneHour, OneDay<br>**Data retention:** 28 days | <ul><li>`MemoryGroup`</li><li>`OperatingSystem`</li><li>`Place`</li><li>`PlaceVersion`</li><li>`Platform`</li></ul> |
| Client memory usage percentage | `ClientMemoryUsagePercentageAvg`<br>`ClientMemoryUsagePercentageP10`<br>`ClientMemoryUsagePercentageP50`<br>`ClientMemoryUsagePercentageP90`<br><br>**Granularities:** OneMinute, HalfHour, OneHour, OneDay<br>**Data retention:** 28 days | <ul><li>`MemoryGroup`</li><li>`OperatingSystem`</li><li>`Place`</li><li>`PlaceVersion`</li><li>`Platform`</li></ul> |
| CPU core utilization | `CpuCoreUtilization`<br><br>**Granularities:** OneMinute, HalfHour, OneHour, OneDay<br>**Data retention:** 28 days | <ul><li>`Place`</li></ul> |
| Unexpected out of memory exits | `OomUnexpectedExits`<br><br>**Granularities:** OneMinute, HalfHour, OneHour, OneDay<br>**Data retention:** 28 days | <ul><li>`MemoryGroup`</li><li>`OperatingSystem`</li><li>`Place`</li><li>`PlaceVersion`</li><li>`Platform`</li></ul> |
| Peak concurrent players | `PeakConcurrentPlayers`<br><br>**Granularities:** OneMinute, HalfHour, OneHour, OneDay<br>**Data retention:** 28 days | <ul><li>`MemoryGroup`</li><li>`OperatingSystem`</li><li>`Place`</li><li>`PlaceVersion`</li><li>`Platform`</li></ul> |
| Client API calls in first 60s after join | `RotraceTotalCalls`<br><br>**Granularities:** OneDay, OneHour, None<br>**Data retention:** 365 days | <ul><li>`SimplifiedUrl`</li></ul> |
| Server CPU time | `CpuTimeAvg`<br>`CpuTimeP10`<br>`CpuTimeP50`<br>`CpuTimeP90`<br><br>**Granularities:** OneMinute, HalfHour, OneHour, OneDay<br>**Data retention:** 28 days | <ul><li>`CpuTimeCategory`</li><li>`CpuTimeSubCategory`</li><li>`Place`</li></ul> |
| Server crashes | `ServerCrashCount`<br><br>**Granularities:** OneMinute, HalfHour, OneHour, OneDay<br>**Data retention:** 28 days | <ul><li>`CrashType`</li><li>`Place`</li></ul> |
| Server frame rate | `ServerFrameRateAvg`<br>`ServerFrameRateP10`<br>`ServerFrameRateP50`<br>`ServerFrameRateP90`<br><br>**Granularities:** OneMinute, HalfHour, OneHour, OneDay<br>**Data retention:** 28 days | <ul><li>`Place`</li></ul> |
| Server memory usage by age | `MemoryUsageAvg`<br>`MemoryUsageP10`<br>`MemoryUsageP50`<br>`MemoryUsageP90`<br><br>**Granularities:** OneMinute, HalfHour, OneHour, OneDay, None<br>**Data retention:** 28 days | <ul><li>`MemoryUsageCategory`</li><li>`MemoryUsageSubCategory`</li><li>`Place`</li><li>`ServerAgeBucket`</li></ul> |
| Server memory usage | `MemoryUsageAvg`<br>`MemoryUsageP10`<br>`MemoryUsageP50`<br>`MemoryUsageP90`<br><br>**Granularities:** OneMinute, HalfHour, OneHour, OneDay, None<br>**Data retention:** 28 days | <ul><li>`MemoryUsageCategory`</li><li>`MemoryUsageSubCategory`</li><li>`Place`</li><li>`ServerAgeBucket`</li></ul> |
| Session time | `SessionDurationSecondsAvg`<br>`SessionDurationSecondsP10`<br>`SessionDurationSecondsP50`<br>`SessionDurationSecondsP90`<br><br>**Granularities:** OneMinute, HalfHour, OneHour, OneDay<br>**Data retention:** 28 days | <ul><li>`MemoryGroup`</li><li>`OperatingSystem`</li><li>`Place`</li><li>`PlaceVersion`</li><li>`Platform`</li></ul> |

### Economy

See [Economy](/docs/en-us/production/analytics/economy-events.md).

| Name | Metric | Supported dimensions |
| --- | --- | --- |
| Average wallet balance | `EconomyAverageWalletBalance`<br><br>**Granularities:** OneDay, OneHour, OneWeek, OneMonth, None<br>**Data retention:** 1468 days | <ul><li>`AgeGroup`</li><li>`CurrencyType`</li><li>`CustomField1`</li><li>`CustomField2`</li><li>`CustomField3`</li><li>`Gender`</li><li>`IsNewUser`</li><li>`OperatingSystem`</li><li>`PayerStatus`</li><li>`Platform`</li></ul> |
| Transaction amount | `EconomyTransactionAmount`<br><br>**Granularities:** OneDay, OneHour, OneWeek, OneMonth, None<br>**Data retention:** 1468 days | <ul><li>`AgeGroup`</li><li>`CurrencyType`</li><li>`CustomField1`</li><li>`CustomField2`</li><li>`CustomField3`</li><li>`FlowType`</li><li>`Gender`</li><li>`IsNewUser`</li><li>`ItemSku`</li><li>`OperatingSystem`</li><li>`PayerStatus`</li><li>`Platform`</li><li>`TransactionType`</li></ul> |
| Transactions | `EconomyTransactionCount`<br><br>**Granularities:** OneDay, OneHour, OneWeek, OneMonth, None<br>**Data retention:** 1468 days | <ul><li>`AgeGroup`</li><li>`CurrencyType`</li><li>`CustomField1`</li><li>`CustomField2`</li><li>`CustomField3`</li><li>`FlowType`</li><li>`Gender`</li><li>`IsNewUser`</li><li>`ItemSku`</li><li>`OperatingSystem`</li><li>`PayerStatus`</li><li>`Platform`</li><li>`TransactionType`</li></ul> |

### Funnels

See [Funnels](/docs/en-us/production/analytics/funnel-events.md).

| Name | Metric | Supported dimensions |
| --- | --- | --- |
| Cohort completion rate | `FunnelCohortCompletionRate`<br><br>**Granularities:** OneDay<br>**Data retention:** 1468 days | <ul><li>`AgeGroup`</li><li>`CustomField1`</li><li>`CustomField2`</li><li>`CustomField3`</li><li>`FunnelName`</li><li>`FunnelStep`</li><li>`Gender`</li><li>`IsNewUser`</li><li>`OperatingSystem`</li><li>`PayerStatus`</li><li>`Platform`</li></ul> |
| Session cohort completion rate | `FunnelCohortSessionCompletionRate`<br><br>**Granularities:** OneDay<br>**Data retention:** 1468 days | <ul><li>`AgeGroup`</li><li>`CustomField1`</li><li>`CustomField2`</li><li>`CustomField3`</li><li>`FunnelName`</li><li>`FunnelStep`</li><li>`Gender`</li><li>`IsNewUser`</li><li>`OperatingSystem`</li><li>`PayerStatus`</li><li>`Platform`</li></ul> |
| Churn | `FunnelStepChurnRate`<br><br>**Granularities:** None<br>**Data retention:** 1468 days | <ul><li>`AgeGroup`</li><li>`CustomField1`</li><li>`CustomField2`</li><li>`CustomField3`</li><li>`FunnelName`</li><li>`FunnelStep`</li><li>`Gender`</li><li>`IsNewUser`</li><li>`OperatingSystem`</li><li>`PayerStatus`</li><li>`Platform`</li></ul> |
| Step completion | `FunnelStepCompletionRate`<br><br>**Granularities:** None<br>**Data retention:** 1468 days | <ul><li>`AgeGroup`</li><li>`CustomField1`</li><li>`CustomField2`</li><li>`CustomField3`</li><li>`FunnelName`</li><li>`FunnelStep`</li><li>`Gender`</li><li>`IsNewUser`</li><li>`OperatingSystem`</li><li>`PayerStatus`</li><li>`Platform`</li></ul> |
| Total conversion | `FunnelStepOverallCompletionRate`<br><br>**Granularities:** None<br>**Data retention:** 1468 days | <ul><li>`AgeGroup`</li><li>`CustomField1`</li><li>`CustomField2`</li><li>`CustomField3`</li><li>`FunnelName`</li><li>`FunnelStep`</li><li>`Gender`</li><li>`IsNewUser`</li><li>`OperatingSystem`</li><li>`PayerStatus`</li><li>`Platform`</li></ul> |
| Total Sessions | `FunnelStepTotalCount`<br><br>**Granularities:** None<br>**Data retention:** 1468 days | <ul><li>`AgeGroup`</li><li>`CustomField1`</li><li>`CustomField2`</li><li>`CustomField3`</li><li>`FunnelName`</li><li>`FunnelStep`</li><li>`Gender`</li><li>`IsNewUser`</li><li>`OperatingSystem`</li><li>`PayerStatus`</li><li>`Platform`</li></ul> |
| Churn | `FunnelUserChurnRate`<br><br>**Granularities:** None<br>**Data retention:** 1468 days | <ul><li>`AgeGroup`</li><li>`CustomField1`</li><li>`CustomField2`</li><li>`CustomField3`</li><li>`FunnelName`</li><li>`FunnelStep`</li><li>`Gender`</li><li>`IsNewUser`</li><li>`OperatingSystem`</li><li>`PayerStatus`</li><li>`Platform`</li></ul> |
| Total conversion | `FunnelUserOverallCompletionRate`<br><br>**Granularities:** None<br>**Data retention:** 1468 days | <ul><li>`AgeGroup`</li><li>`CustomField1`</li><li>`CustomField2`</li><li>`CustomField3`</li><li>`FunnelName`</li><li>`FunnelStep`</li><li>`Gender`</li><li>`IsNewUser`</li><li>`OperatingSystem`</li><li>`PayerStatus`</li><li>`Platform`</li></ul> |
| Step completion | `FunnelUserStepCompletionRate`<br><br>**Granularities:** None<br>**Data retention:** 1468 days | <ul><li>`AgeGroup`</li><li>`CustomField1`</li><li>`CustomField2`</li><li>`CustomField3`</li><li>`FunnelName`</li><li>`FunnelStep`</li><li>`Gender`</li><li>`IsNewUser`</li><li>`OperatingSystem`</li><li>`PayerStatus`</li><li>`Platform`</li></ul> |
| Total users | `FunnelUserTotalCount`<br><br>**Granularities:** None<br>**Data retention:** 1468 days | <ul><li>`AgeGroup`</li><li>`CustomField1`</li><li>`CustomField2`</li><li>`CustomField3`</li><li>`FunnelName`</li><li>`FunnelStep`</li><li>`Gender`</li><li>`IsNewUser`</li><li>`OperatingSystem`</li><li>`PayerStatus`</li><li>`Platform`</li></ul> |

### Custom Events

See [Custom Events](/docs/en-us/production/analytics/custom-events.md).

| Name | Metric | Supported dimensions |
| --- | --- | --- |
| Custom events | `CustomEventAvgPerUserValue`<br>`CustomEventAvgValue`<br>`CustomEventCount`<br>`CustomEventCountUser`<br>`CustomEventMaxValue`<br>`CustomEventMinValue`<br>`CustomEventSumValue`<br><br>**Granularities:** OneDay, OneHour, OneWeek, OneMonth, None<br>**Data retention:** 1468 days | <ul><li>`AgeGroup`</li><li>`CustomEventName`</li><li>`CustomField1`</li><li>`CustomField2`</li><li>`CustomField3`</li><li>`Gender`</li><li>`IsNewUser`</li><li>`OperatingSystem`</li><li>`PayerStatus`</li><li>`Platform`</li></ul> |

### Thumbnails

See [Thumbnails](/docs/en-us/production/publishing/thumbnails.md).

| Name | Metric | Supported dimensions |
| --- | --- | --- |
| Average session length by thumbnail | `ThumbnailAverageSessionLengthMinutes`<br><br>**Granularities:** OneDay, OneHour, None<br>**Data retention:** 30 days | <ul><li>`ThumbnailAsset`</li><li>`ThumbnailList`</li></ul> |
| Impressions by thumbnail | `ThumbnailImpressions`<br><br>**Granularities:** OneDay, OneHour, None<br>**Data retention:** 30 days | <ul><li>`ThumbnailAsset`</li><li>`ThumbnailList`</li></ul> |
| 7D Qualified Play Through Rate by Thumbnail (Cumulative) | `ThumbnailL7QualifiedPTR`<br><br>**Granularities:** OneDay, OneHour, None<br>**Data retention:** 30 days | <ul><li>`ThumbnailAsset`</li><li>`ThumbnailList`</li></ul> |
| Qualified play through rate by thumbnail | `ThumbnailQualifiedPTR`<br><br>**Granularities:** OneDay, OneHour, None<br>**Data retention:** 30 days | <ul><li>`ThumbnailAsset`</li><li>`ThumbnailList`</li></ul> |
| Qualified plays by thumbnail | `ThumbnailQualifiedPlays`<br><br>**Granularities:** OneDay, OneHour, None<br>**Data retention:** 30 days | <ul><li>`ThumbnailAsset`</li><li>`ThumbnailList`</li></ul> |
| Winning segments by thumbnail | `ThumbnailWinningSegments`<br><br>**Granularities:** OneDay, OneHour, None<br>**Data retention:** 30 days | <ul><li>`ThumbnailAsset`</li><li>`ThumbnailList`</li></ul> |

### Speech-to-Text

See [Speech-to-Text](/docs/en-us/tutorials/use-case-tutorials/audio/speech-to-text.md).

| Name | Metric | Supported dimensions |
| --- | --- | --- |
| Audio transcription API responses by status | `SpeechToTextTranscriptionStatuses`<br><br>**Granularities:** OneMinute, HalfHour, OneHour, OneDay<br>**Data retention:** 28 days | <ul><li>`SpeechToTextTranscriptionStatus`</li></ul> |
| Audio transcription API usage | `SpeechToTextTranscriptionUsage`<br><br>**Granularities:** OneMinute, HalfHour, OneHour, OneDay<br>**Data retention:** 28 days | <ul><li>`SpeechToTextTranscriptionStatus`</li></ul> |

### Text-to-Speech

See [Text-to-Speech](/docs/en-us/tutorials/use-case-tutorials/audio/add-text-to-speech.md).

| Name | Metric | Supported dimensions |
| --- | --- | --- |
| Audio generation API asset generation successes | `TextToSpeechAssetSuccesses`<br><br>**Granularities:** OneMinute, HalfHour, OneHour, OneDay<br>**Data retention:** 28 days | |
| Audio generation API responses by status | `TextToSpeechRawAudioErrors`<br><br>**Granularities:** OneMinute, HalfHour, OneHour, OneDay<br>**Data retention:** 28 days | <ul><li>`TextToSpeechRawAudioStatus`</li></ul> |
| Audio generation API usage | `TextToSpeechRawAudioSuccesses`<br><br>**Granularities:** OneMinute, HalfHour, OneHour, OneDay<br>**Data retention:** 28 days | <ul><li>`TextToSpeechRawAudioStatus`</li></ul> |

### Matchmaking

See [Matchmaking](/docs/en-us/matchmaking/analytics.md).

| Name | Metric | Supported dimensions |
| --- | --- | --- |
| Categorical custom signal similarity ratio | `MatchmakingCategoricalCustomSignalsSimilarityRatioAvg`<br>`MatchmakingCategoricalCustomSignalsSimilarityRatioP10`<br>`MatchmakingCategoricalCustomSignalsSimilarityRatioP50`<br>`MatchmakingCategoricalCustomSignalsSimilarityRatioP90`<br><br>**Granularities:** OneHour, OneDay, None<br>**Data retention:** 90 days | <ul><li>`AgeGroup`</li><li>`Locale`</li><li>`MatchmakingCategoricalCustomSignal`</li><li>`Place`</li><li>`Platform`</li></ul> |
| Numerical custom signal difference | `MatchmakingNumericCustomSignalsDifferenceAvg`<br>`MatchmakingNumericCustomSignalsDifferenceP10`<br>`MatchmakingNumericCustomSignalsDifferenceP50`<br>`MatchmakingNumericCustomSignalsDifferenceP90`<br><br>**Granularities:** OneHour, OneDay, None<br>**Data retention:** 90 days | <ul><li>`AgeGroup`</li><li>`Locale`</li><li>`MatchmakingNumericCustomSignal`</li><li>`Place`</li><li>`Platform`</li></ul> |
| Age difference | `MatchmakingSignalsAgeDifferenceAvg`<br>`MatchmakingSignalsAgeDifferenceP10`<br>`MatchmakingSignalsAgeDifferenceP50`<br>`MatchmakingSignalsAgeDifferenceP90`<br><br>**Granularities:** OneHour, OneDay<br>**Data retention:** 90 days | <ul><li>`AgeGroup`</li><li>`Country`</li><li>`Locale`</li><li>`Place`</li><li>`Platform`</li></ul> |
| Common text chat ratio | `MatchmakingSignalsCommonChatGroupRatioAvg`<br>`MatchmakingSignalsCommonChatGroupRatioP10`<br>`MatchmakingSignalsCommonChatGroupRatioP50`<br>`MatchmakingSignalsCommonChatGroupRatioP90`<br><br>**Granularities:** OneHour, OneDay<br>**Data retention:** 90 days | <ul><li>`AgeGroup`</li><li>`Country`</li><li>`Locale`</li><li>`Place`</li><li>`Platform`</li></ul> |
| Common device ratio | `MatchmakingSignalsCommonDeviceTypeRatioAvg`<br>`MatchmakingSignalsCommonDeviceTypeRatioP10`<br>`MatchmakingSignalsCommonDeviceTypeRatioP50`<br>`MatchmakingSignalsCommonDeviceTypeRatioP90`<br><br>**Granularities:** OneHour, OneDay<br>**Data retention:** 90 days | <ul><li>`AgeGroup`</li><li>`Country`</li><li>`Locale`</li><li>`Place`</li><li>`Platform`</li></ul> |
| Common language ratio | `MatchmakingSignalsCommonLanguageRatioAvg`<br>`MatchmakingSignalsCommonLanguageRatioP10`<br>`MatchmakingSignalsCommonLanguageRatioP50`<br>`MatchmakingSignalsCommonLanguageRatioP90`<br><br>**Granularities:** OneHour, OneDay<br>**Data retention:** 90 days | <ul><li>`AgeGroup`</li><li>`Country`</li><li>`Locale`</li><li>`Place`</li><li>`Platform`</li></ul> |
| Estimated ping | `MatchmakingSignalsEstimatePingAvg`<br>`MatchmakingSignalsEstimatePingP10`<br>`MatchmakingSignalsEstimatePingP50`<br>`MatchmakingSignalsEstimatePingP90`<br><br>**Granularities:** OneHour, OneDay<br>**Data retention:** 90 days | <ul><li>`AgeGroup`</li><li>`Country`</li><li>`Locale`</li><li>`Place`</li><li>`Platform`</li></ul> |
| Occupancy ratio | `MatchmakingSignalsOccupancyRatioAvg`<br>`MatchmakingSignalsOccupancyRatioP10`<br>`MatchmakingSignalsOccupancyRatioP50`<br>`MatchmakingSignalsOccupancyRatioP90`<br><br>**Granularities:** OneHour, OneDay<br>**Data retention:** 90 days | <ul><li>`AgeGroup`</li><li>`Country`</li><li>`Locale`</li><li>`Place`</li><li>`Platform`</li></ul> |
| Play history difference | `MatchmakingSignalsPlayHistoryDifferenceAvg`<br>`MatchmakingSignalsPlayHistoryDifferenceP10`<br>`MatchmakingSignalsPlayHistoryDifferenceP50`<br>`MatchmakingSignalsPlayHistoryDifferenceP90`<br><br>**Granularities:** OneHour, OneDay<br>**Data retention:** 90 days | <ul><li>`AgeGroup`</li><li>`Country`</li><li>`Locale`</li><li>`Place`</li><li>`Platform`</li></ul> |
| Average friends match ratio | `MatchmakingSignalsPreferredPlayerMatchRatioAvg`<br><br>**Granularities:** OneHour, OneDay<br>**Data retention:** 90 days | <ul><li>`AgeGroup`</li><li>`Country`</li><li>`Locale`</li><li>`Place`</li><li>`Platform`</li></ul> |
| Voice chat ratio | `MatchmakingSignalsVoiceChatRatioAvg`<br>`MatchmakingSignalsVoiceChatRatioP10`<br>`MatchmakingSignalsVoiceChatRatioP50`<br>`MatchmakingSignalsVoiceChatRatioP90`<br><br>**Granularities:** OneHour, OneDay<br>**Data retention:** 90 days | <ul><li>`AgeGroup`</li><li>`Country`</li><li>`Locale`</li><li>`Place`</li><li>`Platform`</li></ul> |

### Data Store

See [Data Store](/docs/en-us/cloud-services/data-stores/observability.md).

| Name | Metric | Supported dimensions |
| --- | --- | --- |
| List request quota consumption | `DataStoreConsumedListRequests`<br><br>**Granularities:** OneMinute, HalfHour, OneHour, OneDay<br>**Data retention:** 28 days | <ul><li>`DataStoreRequestSource`</li><li>`DataStoreTypeV2`</li></ul> |
| Read request quota consumption | `DataStoreConsumedReadRequests`<br><br>**Granularities:** OneMinute, HalfHour, OneHour, OneDay<br>**Data retention:** 28 days | <ul><li>`DataStoreRequestSource`</li><li>`DataStoreTypeV2`</li></ul> |
| Remove request quota consumption | `DataStoreConsumedRemoveRequests`<br><br>**Granularities:** OneMinute, HalfHour, OneHour, OneDay<br>**Data retention:** 28 days | <ul><li>`DataStoreRequestSource`</li><li>`DataStoreTypeV2`</li></ul> |
| Write request quota consumption | `DataStoreConsumedWriteRequests`<br><br>**Granularities:** OneMinute, HalfHour, OneHour, OneDay<br>**Data retention:** 28 days | <ul><li>`DataStoreRequestSource`</li><li>`DataStoreTypeV2`</li></ul> |
| List quota usage | `DataStoreListRequests`<br><br>**Granularities:** OneMinute, HalfHour, OneHour, OneDay<br>**Data retention:** 28 days | <ul><li>`DataStoreTypeV2`</li></ul> |
| List quota usage | `DataStoreListRequestsByEndpoint`<br><br>**Granularities:** OneMinute, HalfHour, OneHour, OneDay<br>**Data retention:** 28 days | <ul><li>`DataStoreOperation`</li><li>`DataStoreTypeV2`</li></ul> |
| Read quota usage | `DataStoreReadRequests`<br><br>**Granularities:** OneMinute, HalfHour, OneHour, OneDay<br>**Data retention:** 28 days | <ul><li>`DataStoreTypeV2`</li></ul> |
| Read quota usage | `DataStoreReadRequestsByEndpoint`<br><br>**Granularities:** OneMinute, HalfHour, OneHour, OneDay<br>**Data retention:** 28 days | <ul><li>`DataStoreOperation`</li><li>`DataStoreTypeV2`</li></ul> |
| Remove quota usage | `DataStoreRemoveRequests`<br><br>**Granularities:** OneMinute, HalfHour, OneHour, OneDay<br>**Data retention:** 28 days | <ul><li>`DataStoreTypeV2`</li></ul> |
| Remove quota usage | `DataStoreRemoveRequestsByEndpoint`<br><br>**Granularities:** OneMinute, HalfHour, OneHour, OneDay<br>**Data retention:** 28 days | <ul><li>`DataStoreOperation`</li><li>`DataStoreTypeV2`</li></ul> |
| Request count by API and status | `DataStoreRequests`<br><br>**Granularities:** OneMinute, HalfHour, OneHour, OneDay<br>**Data retention:** 28 days | <ul><li>`DataStoreOperation`</li><li>`DataStoreStatus`</li><li>`DataStoreTypeV2`</li></ul> |
| Request count by API | `DataStoreRequestsByEndpoint`<br><br>**Granularities:** OneMinute, HalfHour, OneHour, OneDay<br>**Data retention:** 28 days | <ul><li>`DataStoreOperation`</li><li>`DataStoreTypeV2`</li></ul> |
| Request count by status | `DataStoreRequestsByStatus`<br><br>**Granularities:** OneMinute, HalfHour, OneHour, OneDay<br>**Data retention:** 28 days | <ul><li>`DataStoreStatus`</li><li>`DataStoreTypeV2`</li></ul> |
| Storage usage | `DataStoreStorageUsageBytes`<br><br>**Granularities:** OneMinute, HalfHour, OneHour, OneDay<br>**Data retention:** 28 days | |
| Write quota usage | `DataStoreWriteRequests`<br><br>**Granularities:** OneMinute, HalfHour, OneHour, OneDay<br>**Data retention:** 28 days | <ul><li>`DataStoreTypeV2`</li></ul> |
| Write quota usage | `DataStoreWriteRequestsByEndpoint`<br><br>**Granularities:** OneMinute, HalfHour, OneHour, OneDay<br>**Data retention:** 28 days | <ul><li>`DataStoreOperation`</li><li>`DataStoreTypeV2`</li></ul> |

### Memory Stores

See [Memory Stores](/docs/en-us/cloud-services/memory-stores/observability.md).

| Name | Metric | Supported dimensions |
| --- | --- | --- |
| Memory usage | `MemoryStoreMemoryUsageBytes`<br><br>**Granularities:** OneMinute, HalfHour, OneHour, OneDay<br>**Data retention:** 28 days | |
| API request units | `MemoryStoreRequestUnitsByEndpoint`<br><br>**Granularities:** OneMinute, HalfHour, OneHour, OneDay<br>**Data retention:** 28 days | <ul><li>`MemoryStoreOperation`</li></ul> |
| Request count by API and status | `MemoryStoreRequests`<br><br>**Granularities:** OneMinute, HalfHour, OneHour, OneDay<br>**Data retention:** 28 days | <ul><li>`MemoryStoreOperation`</li><li>`MemoryStoreStatus`</li></ul> |
| Request count by API | `MemoryStoreRequestsByEndpoint`<br><br>**Granularities:** OneMinute, HalfHour, OneHour, OneDay<br>**Data retention:** 28 days | <ul><li>`MemoryStoreOperation`</li></ul> |
| Request count by status | `MemoryStoreRequestsByStatus`<br><br>**Granularities:** OneMinute, HalfHour, OneHour, OneDay<br>**Data retention:** 28 days | <ul><li>`MemoryStoreStatus`</li></ul> |

### Safety

See [Safety](/docs/en-us/safety.md#understand-your-safety-analytics).

| Name | Metric | Supported dimensions |
| --- | --- | --- |
| Total abuse reports | `TotalAbuseReports`<br><br>**Granularities:** OneDay<br>**Data retention:** 1468 days | <ul><li>`AbuseCategory`</li><li>`AbuseChannel`</li></ul> |
| Abuse report submitters per 1000 playtime hours | `UniqueAbuseReportSubmittersPer1000PlaytimeHours`<br><br>**Granularities:** OneDay<br>**Data retention:** 1468 days | <ul><li>`AbuseCategory`</li><li>`AbuseChannel`</li></ul> |

### Advertising

See [Rewarded Video Ads](/docs/en-us/production/promotion/rewarded-video-ads.md#analytics).

| Name | Metric | Supported dimensions |
| --- | --- | --- |
| Impressions | `AdsPublisherReportingTotalImpressions`<br><br>**Granularities:** OneDay, OneHour, None<br>**Data retention:** 1468 days | <ul><li>`AdFormat`</li><li>`AdInstanceName`</li><li>`AdPlacementId`</li><li>`AdsPublisherReportingDataVersion`</li><li>`Country`</li><li>`Gender`</li><li>`OperatingSystem`</li><li>`Platform`</li></ul> |
| Total revenue | `AdsPublisherReportingTotalRevenueRobux`<br><br>**Granularities:** OneDay, OneHour, None<br>**Data retention:** 1468 days | <ul><li>`AdFormat`</li><li>`AdInstanceName`</li><li>`AdPlacementId`</li><li>`AdsPublisherReportingDataVersion`</li><li>`Country`</li><li>`Gender`</li><li>`OperatingSystem`</li><li>`Platform`</li></ul> |
| Rewarded video daily unique viewers | `AdsPublisherReportingVideo2DDailyUniqueViewer`<br><br>**Granularities:** OneDay, None<br>**Data retention:** 1468 days | <ul><li>`AdFormat`</li><li>`AdInstanceName`</li><li>`AdPlacementId`</li><li>`AdsPublisherReportingDataVersion`</li><li>`Country`</li><li>`Gender`</li><li>`OperatingSystem`</li><li>`PlacementType`</li><li>`Platform`</li></ul> |
| Rewarded video earnings per mille (EPM) | `AdsPublisherReportingVideo2DEpmNoUnvalidatedPc`<br><br>**Granularities:** OneDay, OneHour, None<br>**Data retention:** 1468 days | <ul><li>`AdFormat`</li><li>`AdInstanceName`</li><li>`AdPlacementId`</li><li>`AdRewardId`</li><li>`AdsPublisherReportingDataVersion`</li><li>`Country`</li><li>`Gender`</li><li>`OperatingSystem`</li><li>`PlacementType`</li><li>`Platform`</li></ul> |
| Rewarded video impressions | `AdsPublisherReportingVideo2DImpressions`<br><br>**Granularities:** OneDay, OneHour, None<br>**Data retention:** 1468 days | <ul><li>`AdFormat`</li><li>`AdInstanceName`</li><li>`AdPlacementId`</li><li>`AdRewardId`</li><li>`AdsPublisherReportingDataVersion`</li><li>`Country`</li><li>`Gender`</li><li>`OperatingSystem`</li><li>`PlacementType`</li><li>`Platform`</li></ul> |
| Rewarded video earnings | `AdsPublisherReportingVideo2DRevenueRobux`<br><br>**Granularities:** OneDay, OneHour, None<br>**Data retention:** 1468 days | <ul><li>`AdFormat`</li><li>`AdInstanceName`</li><li>`AdPlacementId`</li><li>`AdRewardId`</li><li>`AdsPublisherReportingDataVersion`</li><li>`Country`</li><li>`Gender`</li><li>`OperatingSystem`</li><li>`PlacementType`</li><li>`Platform`</li></ul> |
