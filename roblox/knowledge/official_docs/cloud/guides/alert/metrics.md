---
title: "Supported alert metrics and dimensions"
url: /docs/en-us/cloud/guides/alert/metrics
last_updated: 2026-10-30T19:55:38Z
description: "Lists supported metrics and dimensions for analytics alerts."
---

# Supported alert metrics and dimensions

Analytics alerts support the following metrics and dimensions. All values are case-sensitive.

## Supported metrics

### Alert

See [Alert](/docs/en-us/production/analytics/alerts.md).

| Name | Metric | Supported dimensions |
| --- | --- | --- |
| Client CPU time | `ClientCpuTimeAvg`<br><br>**Granularities:** OneMinute, HalfHour, OneHour, OneDay<br>**Data retention:** 28 days | <ul><li>`ClientCpuTimeCategory`</li><li>`ClientCpuTimeSubCategory`</li><li>`MemoryGroup`</li><li>`OperatingSystem`</li><li>`Place` (filter only)</li><li>`Platform`</li></ul> |
| Client crash count | `ClientCrashCount`<br><br>**Granularities:** OneMinute, HalfHour, OneHour, OneDay<br>**Data retention:** 28 days | <ul><li>`MemoryGroup`</li><li>`OperatingSystem`</li><li>`Place` (filter only)</li><li>`Platform`</li></ul> |
| Client crash rate | `ClientCrashRate15m`<br><br>**Granularities:** OneMinute, HalfHour, OneHour, OneDay<br>**Data retention:** 28 days | <ul><li>`MemoryGroup`</li><li>`OperatingSystem`</li><li>`Place` (filter only)</li><li>`Platform`</li></ul> |
| Client frame rate | `ClientFpsAvg`<br>`ClientFpsP10`<br>`ClientFpsP50`<br>`ClientFpsP90`<br><br>**Granularities:** OneMinute, HalfHour, OneHour, OneDay<br>**Data retention:** 28 days | <ul><li>`MemoryGroup`</li><li>`OperatingSystem`</li><li>`Place` (filter only)</li><li>`Platform`</li></ul> |
| Client memory usage | `ClientMemoryUsageAvg`<br>`ClientMemoryUsageP10`<br>`ClientMemoryUsageP50`<br>`ClientMemoryUsageP90`<br><br>**Granularities:** OneMinute, HalfHour, OneHour, OneDay<br>**Data retention:** 28 days | <ul><li>`MemoryGroup`</li><li>`OperatingSystem`</li><li>`Place` (filter only)</li><li>`Platform`</li></ul> |
| Client memory usage percentage | `ClientMemoryUsagePercentageAvg`<br>`ClientMemoryUsagePercentageP10`<br>`ClientMemoryUsagePercentageP50`<br>`ClientMemoryUsagePercentageP90`<br><br>**Granularities:** OneMinute, HalfHour, OneHour, OneDay<br>**Data retention:** 28 days | <ul><li>`MemoryGroup`</li><li>`OperatingSystem`</li><li>`Place` (filter only)</li><li>`Platform`</li></ul> |
| Cross-server messaging fanout ratio | `CsmFanoutRatio`<br><br>**Granularities:** OneMinute, HalfHour, OneHour, OneDay<br>**Data retention:** 28 days | |
| Cross-server messaging connected game servers | `CsmGameServersConnectedCount`<br><br>**Granularities:** OneMinute, HalfHour, OneHour, OneDay<br>**Data retention:** 28 days | |
| Cross-server messaging message size | `CsmMessageSizeBytes`<br><br>**Granularities:** OneMinute, HalfHour, OneHour, OneDay<br>**Data retention:** 28 days | |
| Cross-server messaging published messages | `CsmPublishedMessagesCount`<br><br>**Granularities:** OneMinute, HalfHour, OneHour, OneDay<br>**Data retention:** 28 days | |
| Cross-server messaging received messages | `CsmReceivedMessagesCount`<br><br>**Granularities:** OneMinute, HalfHour, OneHour, OneDay<br>**Data retention:** 28 days | |
| List request quota consumption | `DataStoreConsumedListRequests`<br><br>**Granularities:** OneMinute, HalfHour, OneHour, OneDay<br>**Data retention:** 28 days | <ul><li>`DataStoreRequestSource`</li><li>`DataStoreTypeV2`</li></ul> |
| Read request quota consumption | `DataStoreConsumedReadRequests`<br><br>**Granularities:** OneMinute, HalfHour, OneHour, OneDay<br>**Data retention:** 28 days | <ul><li>`DataStoreRequestSource`</li><li>`DataStoreTypeV2`</li></ul> |
| Remove request quota consumption | `DataStoreConsumedRemoveRequests`<br><br>**Granularities:** OneMinute, HalfHour, OneHour, OneDay<br>**Data retention:** 28 days | <ul><li>`DataStoreRequestSource`</li><li>`DataStoreTypeV2`</li></ul> |
| Write request quota consumption | `DataStoreConsumedWriteRequests`<br><br>**Granularities:** OneMinute, HalfHour, OneHour, OneDay<br>**Data retention:** 28 days | <ul><li>`DataStoreRequestSource`</li><li>`DataStoreTypeV2`</li></ul> |
| Request count by API and status | `DataStoreRequests`<br><br>**Granularities:** OneMinute, HalfHour, OneHour, OneDay<br>**Data retention:** 28 days | <ul><li>`DataStoreOperation`</li><li>`DataStoreStatus`</li><li>`DataStoreTypeV2`</li></ul> |
| HTTP service request count | `HttpServiceRequestsCount`<br><br>**Granularities:** OneMinute, HalfHour, OneHour, OneDay<br>**Data retention:** 28 days | <ul><li>`HttpServiceDomains` (filter only)</li><li>`HttpServiceMethod`</li><li>`HttpServiceStatus`</li><li>`Place` (filter only)</li></ul> |
| HTTP service response time | `HttpServiceResponseTimeAvg`<br>`HttpServiceResponseTimeP10`<br>`HttpServiceResponseTimeP50`<br>`HttpServiceResponseTimeP90`<br><br>**Granularities:** OneMinute, HalfHour, OneHour, OneDay<br>**Data retention:** 28 days | <ul><li>`HttpServiceDomains` (filter only)</li><li>`HttpServiceMethod`</li><li>`Place` (filter only)</li></ul> |
| Memory Store request count by API and status | `MemoryStoreRequests`<br><br>**Granularities:** OneMinute, HalfHour, OneHour, OneDay<br>**Data retention:** 28 days | <ul><li>`MemoryStoreOperation`</li><li>`MemoryStoreStatus`</li></ul> |
| Unexpected out of memory exits | `OomUnexpectedExits`<br><br>**Granularities:** OneMinute, HalfHour, OneHour, OneDay<br>**Data retention:** 28 days | <ul><li>`MemoryGroup`</li><li>`OperatingSystem`</li><li>`Place` (filter only)</li><li>`Platform`</li></ul> |
| Peak concurrent players | `PeakConcurrentPlayers`<br><br>**Granularities:** OneMinute, HalfHour, OneHour, OneDay<br>**Data retention:** 28 days | <ul><li>`MemoryGroup`</li><li>`OperatingSystem`</li><li>`Place` (filter only)</li><li>`Platform`</li></ul> |
| Server CPU time | `CpuTimeAvg`<br>`CpuTimeP10`<br>`CpuTimeP50`<br>`CpuTimeP90`<br><br>**Granularities:** OneMinute, HalfHour, OneHour, OneDay<br>**Data retention:** 28 days | <ul><li>`CpuTimeCategory`</li><li>`CpuTimeSubCategory`</li><li>`Place` (filter only)</li></ul> |
| Server frame rate | `ServerFrameRateAvg`<br>`ServerFrameRateP10`<br>`ServerFrameRateP50`<br>`ServerFrameRateP90`<br><br>**Granularities:** OneMinute, HalfHour, OneHour, OneDay<br>**Data retention:** 28 days | <ul><li>`Place` (filter only)</li></ul> |
| Server memory usage by age | `MemoryUsageAvg`<br>`MemoryUsageP10`<br>`MemoryUsageP50`<br>`MemoryUsageP90`<br><br>**Granularities:** OneMinute, HalfHour, OneHour, OneDay, None<br>**Data retention:** 28 days | <ul><li>`MemoryUsageCategory`</li><li>`MemoryUsageSubCategory`</li><li>`Place` (filter only)</li></ul> |
| Server memory usage | `MemoryUsageAvg`<br>`MemoryUsageP10`<br>`MemoryUsageP50`<br>`MemoryUsageP90`<br><br>**Granularities:** OneMinute, HalfHour, OneHour, OneDay, None<br>**Data retention:** 28 days | <ul><li>`MemoryUsageCategory`</li><li>`MemoryUsageSubCategory`</li><li>`Place` (filter only)</li></ul> |
| Session time | `SessionDurationSecondsAvg`<br>`SessionDurationSecondsP10`<br>`SessionDurationSecondsP50`<br>`SessionDurationSecondsP90`<br><br>**Granularities:** OneMinute, HalfHour, OneHour, OneDay<br>**Data retention:** 28 days | <ul><li>`MemoryGroup`</li><li>`OperatingSystem`</li><li>`Place` (filter only)</li><li>`Platform`</li></ul> |
