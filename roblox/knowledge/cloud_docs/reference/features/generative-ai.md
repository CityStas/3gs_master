---
name: "Generative AI"
last_updated: 2026-10-30T19:56:08Z
type: feature
api_base_url: "https://apis.roblox.com"
endpoints: 1
auth: [api-key, oauth2, cookie]
description: "Access Roblox's generative AI capabilities for content creation and translation"
---

# Generative AI

Access Roblox's generative AI capabilities for content creation and translation. These APIs enable you to [translate in-game text](#Cloud_TranslateText) between supported languages and [generate speech audio assets](#Cloud_GenerateSpeechAsset) from text for NPC dialogue or narration.

**Base URL:** `https://apis.roblox.com`

    ## Authentication

    Each endpoint requires one of the following authentication methods:

    - **API Key**: Pass your key in the `x-api-key` HTTP header. Create keys at [Creator Dashboard](https://create.roblox.com/dashboard/credentials).
- **OAuth 2.0**: Use Bearer token in the `Authorization` header. Authorization URL: `https://apis.roblox.com/oauth/v1/authorize`, Token URL: `https://apis.roblox.com/oauth/v1/token`
- **Cookie** *(not recommended)*: `.ROBLOSECURITY` cookie. Do not use in production.

    ```
    # API Key example
    curl -H "x-api-key: YOUR_API_KEY" https://apis.roblox.com/...

    # OAuth 2.0 example
    curl -H "Authorization: Bearer YOUR_ACCESS_TOKEN" https://apis.roblox.com/...
    ```

## Endpoints

### POST `/cloud/v2/universes/{universe_id}:translateText` [BETA]

Translate Text

Translates the provided text from one language to another.

**Auth:** API Key (`x-api-key` header)

**Scopes:** `universe:write`

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `universe_id` | path | `string` | Yes | The universe ID. |

**Request Body:** `application/json` — Type: `TranslateTextRequest`

See [TranslateTextRequest](#translatetextrequest) in Models.

**Request example:**
```json
{
  "text": "string",
  "sourceLanguageCode": "string",
  "targetLanguageCodes": [
    "string"
  ]
}
```

**Responses:**

- `200`: OK → `TranslateTextResponse`

**Response fields** (`TranslateTextResponse`)

See [TranslateTextResponse](#translatetextresponse) in Models.

**Response example:**
```json
{
  "sourceLanguageCode": "string",
  "translations": "..."
}
```

**Rate Limits:** perApiKeyOwner: 10000/minute
**Rate Limit Note:** Text translation requests are subject to additional rate limits [documented here](https://create.roblox.com/docs/production/localization/auto-translate-dynamic-content#limits).

**Example:**
```bash
curl -X POST -H "x-api-key: $ROBLOX_API_KEY" \
  "https://apis.roblox.com/cloud/v2/universes/{UNIVERSE_ID}:translateText" \
  -H "Content-Type: application/json" \
  -d '{
  "text": "string",
  "sourceLanguageCode": "string",
  "targetLanguageCodes": [
    "string"
  ]
}'
```

## Models

### TranslateTextRequest

Contains the text to be translated, the source language (optional), and a
list of target languages for translation.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `text` | `string` | Yes | The text to be translated. |
| `sourceLanguageCode` | `string` | No | The IETF BCP-47 language code representing the language of the input text.  If not provided, the system automatically detects the source language.  Supported language codes include:  - English (en-us) - French (fr-fr) - Vietnamese (vi-vn) - Thai (th-th) - Turkish (tr-tr) - Russian (ru-ru) - Spanish (es-es) - Portuguese (pt-br) - Korean (ko-kr) - Japanese (ja-jp) - Chinese Simplified (zh-cn) - Chinese Traditional (zh-tw) - German (de-de) - Polish (pl-pl) - Italian (it-it) - Indonesian (id-id) |
| `targetLanguageCodes` | `string[]` | No | A list of target language codes in IETF BCP-47 format for translation.  Supported language codes include:  - English (en-us) - French (fr-fr) - Vietnamese (vi-vn) - Thai (th-th) - Turkish (tr-tr) - Russian (ru-ru) - Spanish (es-es) - Portuguese (pt-br) - Korean (ko-kr) - Japanese (ja-jp) - Chinese Simplified (zh-cn) - Chinese Traditional (zh-tw) - German (de-de) - Polish (pl-pl) - Italian (it-it) - Indonesian (id-id) |

### TranslateTextResponse

Contains the detected or specified source language code and a map of
requested translations, where each key is a language code and the value is
the translated text.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `sourceLanguageCode` | `string` | No | The IETF BCP-47 language code representing the detected or user-specified language of the source text. |
| `translations` | `object` | No | A map containing the requested translations. The key is the IETF BCP-47 language code, and the value is the translated text for that language. The map contains all requested translations. |