# Google Keep plugin for Stavrobot

A Stavrobot plugin for managing Google Keep notes, checklists, and labels. It can create, read, update, and delete notes; manage checklist items; apply and remove labels; pin notes; and search across your Keep library.

## Authentication setup

This plugin authenticates using an OAuth token obtained directly from Google's embedded login page. The init script exchanges it for a long-lived master token automatically.

1. Go to https://accounts.google.com/EmbeddedSetup
2. Log into your Google account.
3. Click "I agree" (ignore any loading screen that appears).
4. Open browser dev tools → Application (or Storage) → Cookies.
5. Copy the value of the `oauth_token` cookie.

For more details on this flow, see the [gpsoauth documentation](https://github.com/simon-weber/gpsoauth#alternative-flow).

## Installation

Tell Stavrobot to install the plugin from:

```
https://github.com/stavrobot/plugins-google-keep
```

Before the plugin can be used, configure two values:

- `email` — your Google account email address.
- `oauth_token` — the token obtained from the steps above.

Once both are set, the init script will run and exchange the `oauth_token` for a long-lived `master_token`. You do not need to touch `master_token` yourself.

## Available tools

| Tool | Description |
|------|-------------|
| `create_note` | Create a new text note or checklist, optionally with labels and pinning. |
| `get_note` | Get the full content of a note by ID. |
| `update_note` | Update a note's title, text, pin status, or checklist items (add, check, uncheck, delete). |
| `delete_note` | Trash or restore a note by ID. |
| `list_notes` | List and search notes, with optional filters for query text, label, pinned state, and trashed state. |
| `label_note` | Add or remove a label from a note. |
| `manage_labels` | List, create, or delete labels. |
