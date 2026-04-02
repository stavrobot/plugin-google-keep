---
id: pg-3nx2
status: closed
deps: [pg-g53o]
links: []
created: 2026-04-02T21:19:11Z
type: task
priority: 2
assignee: Stavros Korokithakis
---
# Tool: update_note

Update an existing note. Parameters: note_id (string, required), title (string, optional), text (string, optional - replaces text for text notes), pinned (boolean, optional), add_items (string, optional - newline-separated items to add to a list), uncheck_items (string, optional - newline-separated item texts to uncheck), check_items (string, optional - newline-separated item texts to check), delete_items (string, optional - newline-separated item texts to remove). Syncs after changes.

## Acceptance Criteria

Can update title, text, pin status, and manage checklist items.

