---
id: pg-g53o
status: closed
deps: []
links: []
created: 2026-04-02T21:18:55Z
type: task
priority: 2
assignee: Stavros Korokithakis
---
# Scaffold plugin: .gitignore, plugin manifest, and shared auth helper

Create .gitignore (config.json, __pycache__, *.pyc, .jj). Create plugin manifest.json with name google-keep, description, config entries for email/app_password/master_token. Create a shared Python module (lib/keep_auth.py or similar) that reads ../config.json (or ../../config.json depending on caller), authenticates with keep.resume(email, master_token), and returns the Keep object. Tools will import this. Use gkeepapi.

## Acceptance Criteria

manifest.json valid per PLUGIN.md spec. Auth helper works when master_token is present in config.

