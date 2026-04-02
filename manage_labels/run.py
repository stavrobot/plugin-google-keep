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
    """List, create, or delete a Google Keep label based on the action parameter."""
    params = json.load(sys.stdin)

    action: str = params["action"]
    name: str | None = params.get("name")

    keep = authenticate()

    if action == "list":
        labels = [{"name": label.name} for label in keep.labels()]
        json.dump({"labels": labels}, sys.stdout)

    elif action == "create":
        if name is None:
            print("name is required for create action", file=sys.stderr)
            sys.exit(1)
        if keep.findLabel(name) is not None:
            print(f"Label '{name}' already exists", file=sys.stderr)
            sys.exit(1)
        label = keep.createLabel(name)
        keep.sync()
        json.dump({"name": label.name}, sys.stdout)

    elif action == "delete":
        if name is None:
            print("name is required for delete action", file=sys.stderr)
            sys.exit(1)
        label = keep.findLabel(name)
        if label is None:
            print(f"Label '{name}' not found", file=sys.stderr)
            sys.exit(1)
        label.delete()
        keep.sync()
        json.dump({"deleted": name}, sys.stdout)

    else:
        print(f"Unknown action '{action}': must be one of list, create, delete", file=sys.stderr)
        sys.exit(1)


main()
