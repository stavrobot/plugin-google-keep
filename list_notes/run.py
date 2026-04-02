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


def summarise(note: gkeepapi.node.TopLevelNode) -> dict:
    """Build a concise summary dict for a single note."""
    note_type = "list" if isinstance(note, gkeepapi.node.List) else "note"
    label_names = [label.name for label in note.labels.all()]
    text_preview = note.text[:100]
    return {
        "id": note.id,
        "title": note.title,
        "type": note_type,
        "pinned": note.pinned,
        "labels": label_names,
        "text_preview": text_preview,
    }


def main() -> None:
    """List Google Keep notes, applying optional filters from stdin parameters."""
    params = json.load(sys.stdin)

    query = params.get("query")
    label_name = params.get("label")
    pinned = params.get("pinned")
    # Default trashed to False so we don't show trash unless explicitly requested.
    trashed = params.get("trashed", False)

    keep = authenticate()

    label_object = None
    if label_name is not None:
        label_object = keep.findLabel(label_name)
        if label_object is None:
            json.dump({"notes": [], "total_count": 0}, sys.stdout)
            return

    find_kwargs: dict = {"trashed": trashed}
    if query is not None:
        find_kwargs["query"] = query
    if label_object is not None:
        find_kwargs["labels"] = [label_object]
    if pinned is not None:
        find_kwargs["pinned"] = pinned

    all_matches = list(keep.find(**find_kwargs))
    total_count = len(all_matches)
    notes = [summarise(note) for note in all_matches[:50]]

    json.dump({"notes": notes, "total_count": total_count}, sys.stdout)


main()
