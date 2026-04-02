#!/usr/bin/env -S uv run
# /// script
# dependencies = ["gpsoauth"]
# ///

import json
import sys
from pathlib import Path


def main() -> None:
    """Exchange an OAuth token for a master token and persist it to config.json."""
    import gpsoauth

    config_path = Path("config.json")
    config = json.loads(config_path.read_text())

    if config.get("master_token"):
        print("master_token already set, skipping init.")
        return

    email = config["email"]
    oauth_token = config["oauth_token"]

    response = gpsoauth.exchange_token(email, oauth_token, "0123456789abcdef")

    if "Token" not in response:
        print(response, file=sys.stderr)
        sys.exit(1)

    config["master_token"] = response["Token"]
    config_path.write_text(json.dumps(config, indent=2) + "\n")

    print("Google Keep init complete: master_token saved to config.json.")


main()
