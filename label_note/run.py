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
    """Add or remove a label from a Google Keep note."""
    params = json.load(sys.stdin)

    note_id: str = params["note_id"]
    label_name: str = params["label"]
    remove: bool = params.get("remove", False)

    keep = authenticate()

    note = keep.get(note_id)
    if note is None:
        print(f"Note not found: {note_id}", file=sys.stderr)
        sys.exit(1)

    label_obj = keep.findLabel(label_name)
    if label_obj is None:
        print(f"Label not found: {label_name}", file=sys.stderr)
        sys.exit(1)

    if remove:
        note.labels.remove(label_obj)
        action = "removed"
    else:
        note.labels.add(label_obj)
        action = "added"

    keep.sync()

    json.dump({"note_id": note_id, "label": label_name, "action": action}, sys.stdout)


main()
