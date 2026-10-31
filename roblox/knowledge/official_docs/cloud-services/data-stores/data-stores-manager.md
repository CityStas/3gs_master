---
title: "Data Stores Manager"
url: /docs/en-us/cloud-services/data-stores/data-stores-manager
last_updated: 2026-10-30T19:55:39Z
description: "The Data Stores Manager helps you monitor your data stores (DataStores) on Creator Hub."
---

# Data Stores Manager

With the Data Stores Manager, you can browse and monitor your data stores, their key entries, and their storage usage directly on the Creator Hub.

## Access the Data Stores Manager

> **Info:** If you're the owner of a game or the group owner of a group-owned game, you already have full access to the Data Stores Manager by default.
>
> To give members of your group access to the Data Stores Manager, you can [grant them one of the following permissions](/docs/en-us/projects/groups.md#roles-and-permissions): - ****lets them view the Data Stores Manager page in the Creator Hub. - ****lets them delete keys. - ****lets them delete data stores. - ****gives them full access to all of the functionality of the Data Stores Manager.

To access the Data Stores Manager:

1. Select a game on the [Creator Dashboard](https://create.roblox.com/dashboard/creations).
2. Go to **Configurations** > **Data stores manager**.

![Overview of Data Stores Manager page displaying the Summary section, the Data Stores list, and the Keys list.](./../../assets/data/data-store/Data-Stores-Manager-Page.png)

The **Summary** section of the Data Stores Manager page includes the **Total Size** and the **Storage Limit** of your data stores. Total Size is calculated by adding the number of bytes consumed by all existing keys in your game, and Storage Limit is calculated based on your game's lifetime user count. For more information about storage limits, see [Limits](/docs/en-us/cloud-services/data-stores/error-codes-and-limits.md#limits).

If your Total Size exceeds your Storage Limit, your **Est. Monthly Costs** will populate in your Summary and show an estimation of the impact of the usage that has gone over your quota. For tips on how to reduce your storage consumption, see [Best practices](/docs/en-us/cloud-services/data-stores/best-practices.md).

## View data stores and keys

> **Warning:** If your game has more than 100 data stores, the data store size and number of keys won't be available in the Data Stores list.

The **Data Stores** list displays the name, size, and number of keys for all data stores in your game. You can filter this list by entering a prefix in the search bar.

To further drill down into each specific data store, you can:

- Select a data store from the data store list to display a list of all keys in that data store.
- Enter a prefix in the search bar to filter the list of keys. The prefix must start with the scope name.
- Select a key entry to display that key's value, metadata, version history, status, and when it was last updated.
- Select both a key entry and a version, and click **Compare versions** to compare the current key entry version with the version you selected.
- Select a previous version of a key and click **Revert** to go back to that version. You must have Edit permissions to do this. Reverting to a previous version conditionally updates the list and writes a new version with the value of the version you have previously selected.

![Comparison of two key entries in a data store.](./../../assets/data/data-store/Data-Stores-Manager-Compare-Versions.png) ## Delete data stores and keys

> **Info:** When you schedule a data store for permanent deletion, that data store immediately becomes inaccessible. Any attempts to read or write to its entries will fail.

To schedule a data store or key for permanent deletion:

1. Select a game on the [Creator Dashboard](https://create.roblox.com/dashboard/creations).
2. In the left-hand navigation, go to **Configurations** > **Data stores manager**.
3. Click the **Action** menu next to the item you want to delete.
4. Click **Mark for Deletion**.

There is a cooldown period between when you delete a data store or key and when that item is actually deleted. During this cooldown period, you can undo the deletion and restore the item to its normal state.

To restore a data store, click the **Action** menu next to the data store you want to restore and then click **Restore**, or call the [`UndeleteDataStore`](/docs/en-us/cloud/reference/DataStore.md#Cloud_UndeleteDataStore) method from the Open Cloud API.

To restore a key, call the `Class.GlobalDataStore.UpdateAsync|UpdateAsync` method from the Engine API or the [`UpdateDataStoreEntry`](/docs/en-us/cloud/reference/DataStoreEntry.md#Cloud_UpdateDataStoreEntry__Using_Universes_DataStores) method from the Open Cloud API.
