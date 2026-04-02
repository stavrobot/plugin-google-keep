---
id: pg-i2n7
status: closed
deps: [pg-g53o]
links: []
created: 2026-04-02T21:19:04Z
type: task
priority: 2
assignee: Stavros Korokithakis
---
# Tool: list_notes

List/search notes. Parameters: query (string, optional - text search), label (string, optional - filter by label name), pinned (boolean, optional), trashed (boolean, optional, default false). Returns array of note summaries (id, title, note type, pinned, labels, truncated text). Limit results to avoid blowing up context - 50 max, return a count of total matches.

## Acceptance Criteria

Tool lists notes, filters work, output is concise.

