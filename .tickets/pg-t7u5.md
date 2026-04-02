---
id: pg-t7u5
status: closed
deps: [pg-g53o]
links: []
created: 2026-04-02T21:19:00Z
type: task
priority: 2
assignee: Stavros Korokithakis
---
# Init script: login with app_password, save master_token

Create init.py at plugin root. Reads config.json, logs in with keep.login(email, app_password), calls keep.getMasterToken(), writes master_token back to config.json. Executable with uv shebang. Dependency: gkeepapi.

## Acceptance Criteria

Running init.py with valid email+app_password populates master_token in config.json.

