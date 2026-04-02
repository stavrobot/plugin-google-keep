import json
from pathlib import Path

import gkeepapi


def authenticate(config_path: Path | None = None) -> gkeepapi.Keep:
    """Read config.json, resume a Keep session using the stored master token, and return the Keep object.

    Tools run from their own subdirectory (e.g. plugin-root/list_notes/), so the
    default config path walks two levels up from this file to reach the plugin root.
    Callers that live elsewhere can pass an explicit config_path.
    """
    if config_path is None:
        config_path = Path(__file__).resolve().parent.parent / "config.json"

    config = json.loads(config_path.read_text())

    master_token = config.get("master_token")
    if not master_token:
        raise RuntimeError(
            "master_token is not set in config.json. "
            "Run the plugin init script to obtain one."
        )

    email = config["email"]

    keep = gkeepapi.Keep()
    keep.authenticate(email, master_token)
    keep.sync()
    return keep
