# Knowledge Base Update Policy

## Why updates matter

Roblox APIs, Studio capabilities, policy requirements, monetization features and MCP tool schemas change. A curated RAG corpus becomes stale unless it is refreshed and checked.

## Suggested schedule

| Source group | Suggested check |
|---|---|
| Engine API Reference and docs indexes | Weekly or on demand before API-sensitive work |
| Studio MCP documentation/tool list | Weekly while actively using MCP; before changing client config |
| Luau docs and release notes | Monthly and when compiler/type behavior is relevant |
| Open Cloud APIs | Monthly and before production integrations |
| Monetization, policy and safety docs | Before implementing or changing those features |
| Third-party tools (Rojo/Rokit/Wally) | On project toolchain update; use pinned versions |
| Curated concept docs in this pack | Quarterly or when a relevant official page changes |

## Update process

1. Fetch the official docs indexes.
2. Compare URL inventory with the previous snapshot.
3. Re-fetch changed source pages.
4. Compute content hash and detect changed sections.
5. Re-chunk and re-embed only changed content.
6. Keep the old version in an archive or versioned collection for auditability.
7. Run the RAG evaluation set in `11_RAG_INGESTION.md`.
8. Flag API snippets that may now be deprecated or invalid.

## Version labels

Every chunk should carry:

- `retrieved_at` — when your pipeline fetched it;
- `source_last_modified` — only when the source explicitly exposes it;
- `content_hash` — content fingerprint;
- `status` — current, superseded, retired or needs_review.

Never fabricate source modification dates. The retrieval timestamp is not the publication date.
