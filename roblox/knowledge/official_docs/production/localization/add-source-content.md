---
title: "Add source content"
url: /docs/en-us/production/localization/add-source-content
last_updated: 2026-10-30T19:55:48Z
description: "Learn how to manually add, edit, and remove entries to your game's cloud localization table."
---

# Add source content

You must add source text to translate to the game's localization table before you or any collaborators add translations. You can use [Automatic Text Capture](#automatic-text-capture) to collect text strings automatically as your game is played by users or [manually add text sources](#manually-add-source-content).

See [Localizing images and sounds](/docs/en-us/production/localization/localize-with-scripting.md#localize-images-and-sounds) for instructions on localizing non-text content.

## Automatic Text Capture

The **Automatic Text Capture (ATC)** tool collects text strings that users encounter in your game through GUI objects, such as `Class.TextLabel|TextLabels` or `Class.BillboardGui` and is usually the fastest way to collect translatable text from your game. In many cases, the Automatic Text Capture tool is already enabled for [automatic translations](/docs/en-us/production/localization/automatic-translations.md#enable-automatic-text-capture).

## Manually add source content

You can also add content manually. This is recommended if your game contains text that doesn't appear during typical gameplay, like a complex conversation tree, which may take longer to collect via ATC. You can add entries to the table [in the localization page](#add-sources-with-localization-settings) or [with a `.csv` file upload](#add-sources-with-file-upload). It is recommended to use the `.csv` upload if you want to specify an entry's Key, Context, or Example fields.

> **Warning:** Entries in the localization table are case-sensitive.
>
> For example, when using "hello" as a source value on the localization table, Roblox does not apply translations for "Hello" or "HELLO".

You can manually add image and sound asset IDs to the localization table with a `.csv` upload. For more information see [Localize images and sounds](/docs/en-us/production/localization/localize-with-scripting.md#localize-images-and-sounds).

### Add sources with localization settings

You can add source content in the [localization page](/docs/en-us/production/localization.md#localization-settings). This is ideal for making quick additions to your localization table.

To add source content through the localization page:

1. In your game's localization page, click the **Translate** button on the top right.
2. Select the **Strings** tab.
3. Click **Add Entry**.
4. In the **Text to translate** field, input the source text and click **Save**.
5. If you are using key-based scripting to translate a string, input the key name in the **Key** field.
6. If the string has multiple meanings, such as a character's back and a back button, input the full path of the specific text object in the **Context** field.
7. Click **Save**.

### Add sources with file upload

You can add source content to your localization table with a `.csv` upload. You can use this option when making large numbers of updates to your localization table.

To add source content through the `.csv` upload:

1. In Studio, open **Localization Tools** from the **Window** ⟩ **Localization**
2. In the **Cloud Localization Table** section, select **Download** to save the `.csv`.
3. Open the `.csv` in your preferred spreadsheet editor.
4. Under the **Source** column, add source text and save. You can leave the other columns blank. | Key | Context | Example | Source |
| --- | --- | --- | --- | |  |  |  | Options | |  |  |  | Start |
5. In Studio, in the **Cloud Localization Table** section, select **Update** and upload the new `.csv` file.
6. Click **Confirm** on the **Confirm Upload** prompt to save the new entry to the cloud localization table.
