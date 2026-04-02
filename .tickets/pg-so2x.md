---
id: pg-so2x
status: closed
deps: [pg-g53o]
links: []
created: 2026-04-02T21:19:12Z
type: task
priority: 2
assignee: Stavros Korokithakis
---
# Tool: delete_note

Trash or untrash a note. Parameters: note_id (string, required), restore (boolean, optional - if true, untrash instead). Calls note.trash() or note.untrash().

## Acceptance Criteria

Can trash and restore notes.

