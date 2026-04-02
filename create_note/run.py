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
    """Create a Google Keep text note or checklist from the given parameters."""
    params = json.load(sys.stdin)

    title: str = params["title"]
    text: str = params.get("text", "")
    items: str | None = params.get("items")
    labels_param: str | None = params.get("labels")
    pinned: bool = params.get("pinned", False)

    keep = authenticate()

    if items is not None:
        note = keep.createList(title, [(item, False) for item in [i.strip() for i in items.split("\n") if i.strip()]])
        note_type = "list"
    else:
        note = keep.createNote(title, text)
        note_type = "note"

    if labels_param:
        for label_name in labels_param.split(","):
            label_name = label_name.strip()
            label = keep.findLabel(label_name)
            if label is not None:
                note.labels.add(label)

    note.pinned = pinned

    keep.sync()

    json.dump({"id": note.id, "title": note.title, "type": note_type}, sys.stdout)


main()
