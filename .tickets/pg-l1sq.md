---
id: pg-l1sq
status: closed
deps: [pg-g53o]
links: []
created: 2026-04-02T21:19:14Z
type: task
priority: 2
assignee: Stavros Korokithakis
---
# Tool: manage_labels

List, create, or delete labels. Parameters: action (string, required - one of list/create/delete), name (string, optional - required for create/delete). For list: return all labels. For create: create label, error if exists. For delete: delete label, error if not found.

## Acceptance Criteria

All three actions work correctly.

