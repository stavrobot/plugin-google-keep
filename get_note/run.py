#!/usr/bin/env -S uv run
# /// script
# dependencies = ["gkeepapi"]
# ///

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "lib"))
from keep_auth import authenticate

import gkeepapi.node


def main() -> None:
    """Fetch a single Google Keep note by ID and return its full content."""
    params = json.load(sys.stdin)
    note_id = params["note_id"]

    keep = authenticate()
    note = keep.get(note_id)

    if note is None:
        print(f"Note not found: {note_id}", file=sys.stderr)
        sys.exit(1)

    note_type = "list" if isinstance(note, gkeepapi.node.List) else "note"

    result: dict = {
        "id": note.id,
        "title": note.title,
        "type": note_type,
        "labels": [label.name for label in note.labels.all()],
        "pinned": note.pinned,
        "trashed": note.trashed,
        "created": note.timestamps.created.isoformat(),
        "updated": note.timestamps.updated.isoformat(),
    }

    if note_type == "list":
        result["items"] = [
            {"text": item.text, "checked": item.checked}
            for item in note.items
        ]
    else:
        result["text"] = note.text

    json.dump(result, sys.stdout)


main()
