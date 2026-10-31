---
title: "Rate limits and throttling"
url: /docs/en-us/cloud/guides/data-stores/throttling
last_updated: 2026-10-30T19:55:39Z
description: "Covers rate limits for the Open Cloud v2 Data Stores API."
---

# Rate limits and throttling

> **Info:** The below limits apply only to [Open Cloud v1](/docs/en-us/cloud/reference/features/storage.md#Datastores_ListDatastoresAsync) endpoints. For [Open Cloud v2](/docs/en-us/cloud/reference/features/storage.md#Cloud_ListDataStores) rate limits, see [Data store error codes and limits](/docs/en-us/cloud-services/data-stores/error-codes-and-limits.md#access-limits).

The [Data Stores API](/docs/en-us/cloud/reference/features/storage.md) enforces two types of throttling: **requests per minute** and **throughput**. Each game allows a certain number of requests per minute and a certain amount of data per minute. These limits are enforced for the universe (experience / game) regardless of the number of API keys used.

Unlike the Engine API, these limits do **not** scale based on user count. Exceeding either one causes the endpoint to return `429 Too Many Requests`.

## Legacy standard data stores throttling limits

These limits apply to the legacy `/datastores/v1/` endpoints.

| Request type | Method | Throttle limits |
| --- | --- | --- |
| Write | <ul><li>Create Data Store Entry</li><li>Delete Data Store Entry</li><li>Update Data Store Entry</li><li>Increment Data Store Entry</li></ul> | <ul><li>10 MB/minute/universe write throughput</li><li>300 requests/minute/universe</li></ul> |
| Read | <ul><li>List Data Stores</li><li>List Data Store Entries</li><li>Get Data Store Entry</li><li>List Data Store Entry Revisions</li></ul> | <ul><li>20 MB/minute/universe read throughput</li><li>300 requests/minute/universe</li></ul> |
| Delete | <ul><li>Delete Data Store</li><li>Undelete Data Store</li></ul> | <ul><li>300 requests/minute/universe</li></ul> |

## Legacy ordered data stores throttling limits

These limits apply to the legacy `/ordered-data-stores/v1/` endpoints.

| Request type | Method | Throttle limits |
| --- | --- | --- |
| Write | <ul><li>Create Ordered Data Store Entry</li><li>Delete Ordered Data Store Entry</li><li>Update Ordered Data Store Entry</li><li>Increment Ordered Data Store Entry</li></ul> | <ul><li>300 requests/minute/universe</li></ul> |
| Read | <ul><li>List Ordered Data Store Entries</li><li>Get Ordered Data Store Entry</li></ul> | <ul><li>300 requests/minute/universe</li></ul> |
