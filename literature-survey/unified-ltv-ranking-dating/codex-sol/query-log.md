# NotebookLM Query Log — codex-sol

Notebook: `67046a44-7490-4fe5-b54a-3f39ef37fdd3` (`unified-ltv-ranking-dating`, 146 sources)

| # | Operation | Scope | Query / purpose | Result count | Outcome |
|---|---|---:|---|---:|---|
| 0 | `notebook_get` | full notebook | Verify existing notebook and enumerate sources. | 146 | success |
| 1 | `notebook_query` | sources 1–25 | Classify every scoped source by exact title, year, company/venue, source type, best D1–D9 direction, relevance, and include yes/no. | 25 | success; 25/25 lines returned |
| 2 | `notebook_query` | sources 26–50 | Same source-selection classification request. | null | timed out after more than 180 seconds; no result returned |
| 3 | `notebook_query` | sources 26–40 | Same source-selection classification request, reduced batch. | 15 | success; 15/15 lines returned |
| 4 | `notebook_query` | sources 41–55 | Same source-selection classification request, reduced batch. | 15 | success; 15/15 lines returned |
| 5 | `notebook_query` | sources 56–70 | Same source-selection classification request, reduced batch. | 15 | success; 15/15 lines returned |
| 6 | `notebook_query` | sources 71–85 | Same source-selection classification request, reduced batch. | 15 | success; 15/15 lines returned |
| 7 | `notebook_query` | sources 86–100 | Same source-selection classification request, reduced batch. | 13 | partial success; 13 lines returned, while the two identically titled Meta URL sources were omitted |
| 8 | `notebook_query` | sources 101–115 | Same source-selection classification request, reduced batch. | 15 | success; 15/15 lines returned |
| 9 | `notebook_query` | sources 116–130 | Same source-selection classification request, reduced batch. | 15 | success; 15/15 lines returned |
| 10 | `source_get_content` | one BatchRL-MTF source | Check indexed source text during metadata validation. | 1 | success |
| 11 | `source_describe` | one BatchRL-MTF source | Request an AI source summary. | null | failed: `Failed to get source summary.` |
| 12 | `source_get_content` | 31 selected uploaded-PDF sources | Extract source-header evidence and DOI/arXiv identifiers for URL verification. | 31 | success; 31/31 returned content |
| 13 | `source_get_content` | sources 131–146 | Verify titles, affiliations, and scope from source headers for metadata-only classification. | 16 | success; 16/16 returned content (one PDF was image-heavy) |
| 14 | `source_get_content` | xMTF | Verify conference, DOI, and Kuaishou affiliations. | 1 | success |

No NotebookLM query in this log searches for new sources; all calls are against the existing notebook. External title/URL verification was limited to direct paper, publisher, company-research, DBLP, DOI, and arXiv records.
