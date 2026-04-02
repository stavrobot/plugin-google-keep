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
    """Update an existing Google Keep note by ID, applying whichever fields are provided."""
    params = json.load(sys.stdin)

    note_id: str = params["note_id"]
    keep = authenticate()

    note = keep.get(note_id)
    if note is None:
        print(f"Note not found: {note_id}", file=sys.stderr)
        sys.exit(1)

    if "title" in params:
        note.title = params["title"]

    if "text" in params:
        if not isinstance(note, gkeepapi.node.Note):
            print(f"Note {note_id} is not a text note; cannot set text", file=sys.stderr)
            sys.exit(1)
        note.text = params["text"]

    if "pinned" in params:
        note.pinned = params["pinned"]

    checklist_keys = {"add_items", "check_items", "uncheck_items", "delete_items"}
    if checklist_keys & params.keys():
        if not isinstance(note, gkeepapi.node.List):
            print(f"Note {note_id} is not a checklist; cannot perform checklist operations", file=sys.stderr)
            sys.exit(1)

    if "add_items" in params:
        for item_text in params["add_items"].split("\n"):
            item_text = item_text.strip()
            if item_text:
                note.add(item_text, False)

    if "check_items" in params:
        targets = {line.strip() for line in params["check_items"].split("\n") if line.strip()}
        for item in note.items:
            if item.text in targets:
                item.checked = True

    if "uncheck_items" in params:
        targets = {line.strip() for line in params["uncheck_items"].split("\n") if line.strip()}
        for item in note.items:
            if item.text in targets:
                item.checked = False

    if "delete_items" in params:
        targets = {line.strip() for line in params["delete_items"].split("\n") if line.strip()}
        for item in list(note.items):
            if item.text in targets:
                item.delete()

    keep.sync()

    note_type = "list" if isinstance(note, gkeepapi.node.List) else "note"
    json.dump(
        {
            "id": note.id,
            "title": note.title,
            "type": note_type,
            "pinned": note.pinned,
        },
        sys.stdout,
    )


main()
