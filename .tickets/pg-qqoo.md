---
id: pg-qqoo
status: closed
deps: [pg-g53o]
links: []
created: 2026-04-02T21:19:08Z
type: task
priority: 2
assignee: Stavros Korokithakis
---
# Tool: create_note

Create a text note or checklist. Parameters: title (string, required), text (string, optional - for text notes), items (string, optional - newline-separated checklist items), labels (string, optional - comma-separated label names to apply), pinned (boolean, optional). If items is provided, create a List node; otherwise create a Note. Return the new note's id and title.

## Acceptance Criteria

Can create both text notes and checklists. Labels are applied if they exist.

