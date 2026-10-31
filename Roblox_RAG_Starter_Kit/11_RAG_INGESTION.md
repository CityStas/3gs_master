# RAG Ingestion and Retrieval Design

## 1. Recommended architecture

```text
Official Roblox docs (.md) ─┐
Luau docs / GitHub docs ─────┼─> Fetch -> Normalize -> Deduplicate -> Chunk -> Embed
Curated KB markdown ────────┤                                |
Project-specific docs ─────┘                                v
                                                 Vector + lexical index
                                                          |
User question -> query rewrite -> hybrid retrieval -> rerank -> grounded answer
                                                          |
                                          citations + API verification + uncertainty
```

Keep general Roblox knowledge separate from private project knowledge. Use separate collections or metadata filters, for example:

- `roblox_official_docs`
- `luau_official_docs`
- `roblox_tooling_docs`
- `curated_roblox_kb`
- `project_<project_slug>`

## 2. Initial source import

Start with these three official machine-readable indexes:

- `https://create.roblox.com/docs/llms.txt`
- `https://create.roblox.com/docs/reference/engine/llms.txt`
- `https://create.roblox.com/docs/cloud/llms.txt`

Then import selected Luau and tool documentation. Prefer official Markdown pages when available. Do not blindly mirror every page on day one; start from the subject areas listed in `01_SOURCE_CATALOG.md` and expand by query demand.

## 3. Normalize before chunking

- Preserve headings and heading hierarchy.
- Preserve code blocks exactly; do not strip comments or indentation.
- Preserve official API identifiers and signatures.
- Keep tables with their headers; split very large tables by logical group.
- Remove navigation, repeated footers, cookie banners and unrelated page chrome.
- Preserve page URL and anchor/section title for citations.
- Keep English API terminology; optional Russian explanation can be stored alongside it.
- Do not join two unrelated API classes into one chunk.

## 4. Chunking recommendations

These are starting heuristics, not fixed laws:

- Conceptual prose: about 450–850 tokens per chunk, 60–100 token overlap.
- API class pages: split by class section or coherent groups of properties/methods/events; keep each signature with its description and thread/security tags.
- Code examples: keep the complete example together with its explanation and required script context.
- Tutorials: split by task/step with prerequisite and outcome retained.
- Tables: preserve header row in every chunk.
- Glossary: one term/definition per record or small related group.

For API retrieval, use parent-child indexing: small precise child chunks for an API member, linked to a larger parent page/class section for context.

## 5. Metadata schema

Recommended metadata for each chunk:

```json
{
  "chunk_id": "stable-id",
  "document_id": "stable-source-id",
  "title": "Remote events and callbacks",
  "heading_path": ["Scripting", "Events", "Remote events and callbacks"],
  "source_url": "https://create.roblox.com/docs/scripting/events/remote",
  "source_type": "official_documentation",
  "publisher": "Roblox",
  "trust_level": "primary",
  "language": "en",
  "topic": ["networking", "remotes", "security"],
  "api_identifiers": ["RemoteEvent", "RemoteFunction", "UnreliableRemoteEvent"],
  "script_context": ["server", "client"],
  "retrieved_at": "YYYY-MM-DD",
  "source_last_modified": null,
  "content_hash": "sha256:...",
  "version_scope": "current platform; revalidate"
}
```

Add `experience_id`, `project_slug` and `visibility=private` only to project-specific content.

## 6. Retrieval strategy

Use **hybrid retrieval**:

1. Query normalization: preserve API identifiers, code fragments, error strings and exact class names.
2. Metadata filtering: narrow by topic, source type, language or API identifier.
3. Lexical/BM25 search: essential for exact identifiers such as `GetAsync`, `PlayerAdded`, `CFrame`, `Humanoid`.
4. Vector search: useful for conceptual requests such as "make enemies follow the player".
5. Reranker: rank by direct relevance, source authority, specificity and recency.
6. Context assembly: include the specific API member chunk plus parent section when needed.
7. Grounded generation: cite source URL and distinguish official guarantee from design advice.

A query about a specific API should prioritize the Engine API Reference above general tutorials.

## 7. Embeddings and storage

Choose based on the local stack and language mix. The important requirements are:

- Good English technical retrieval (API docs are mostly English).
- Adequate Russian/English multilingual retrieval if user questions are Russian.
- Persistent local vector storage if privacy/offline access matters.
- Metadata filtering and deletion/upsert support.
- A lexical index alongside vector search.

Possible storage choices include Qdrant, Chroma or PostgreSQL with pgvector. They are alternatives, not all required. Do not select a database solely because a tutorial uses it.

## 8. Freshness and deduplication

- Use canonical URL as the initial document key.
- Compute a content hash; skip re-embedding unchanged content.
- Re-fetch the docs indexes regularly and detect added/removed/changed URLs.
- Use shorter refresh intervals for release notes, API reference and Open Cloud; longer intervals for stable conceptual guides.
- Mark removed pages as retired, not silently deleted, so retrieval does not cite dead content.
- Record `retrieved_at` independently from page publication/modified date.

## 9. Answer citation format

For every technical answer, retain at least:

- source page title;
- exact source URL;
- relevant heading/API identifier;
- retrieval date.

If an answer describes a current API, the agent should link the official API page, not only this curated starter file.

## 10. Evaluation set

Create a small gold test set before scaling:

1. Where should a server-only script live?
2. Difference between Script, LocalScript and ModuleScript?
3. When should I use RemoteEvent vs RemoteFunction?
4. Why must the server validate a purchase request?
5. How should player data be loaded and saved safely?
6. How do I test a multiplayer mechanic with multiple clients?
7. What does `--!strict` do?
8. What is the current API contract for a named Engine API member?
9. What does the Studio MCP server allow an agent to do?
10. Which source is authoritative when a DevForum answer conflicts with the Engine API Reference?

Score retrieval separately from answer quality. A correct answer with the wrong or stale source is not a passing result.
