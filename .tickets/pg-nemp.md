---
id: pg-nemp
status: closed
deps: [pg-g53o]
links: []
created: 2026-04-02T21:19:06Z
type: task
priority: 2
assignee: Stavros Korokithakis
---
# Tool: get_note

Get full content of a note by ID. Parameters: note_id (string, required). Returns id, title, text (for text notes), items with checked status (for lists), labels, pinned, trashed, timestamps.

## Acceptance Criteria

Returns full note content for both text and list notes.

