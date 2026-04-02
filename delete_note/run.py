#!/usr/bin/env -S uv run
# /// script
# dependencies = ["gkeepapi"]
# ///

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "lib"))

from keep_auth import authenticate


def main() -> None:
    """Trash or restore a Google Keep note by ID."""
    params = json.load(sys.stdin)
    note_id = params["note_id"]
    restore = params.get("restore", False)

    keep = authenticate()

    note = keep.get(note_id)
    if note is None:
        print(f"Note not found: {note_id}", file=sys.stderr)
        sys.exit(1)

    if restore:
        note.untrash()
    else:
        note.trash()

    keep.sync()

    json.dump(
        {
            "id": note.id,
            "title": note.title,
            "trashed": note.trashed,
        },
        sys.stdout,
    )


main()
