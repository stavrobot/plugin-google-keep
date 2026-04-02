import json
from pathlib import Path

import gpsoauth
import gkeepapi


def authenticate(config_path: Path | None = None) -> gkeepapi.Keep:
    """Read config.json, authenticate with Keep, and return the Keep object.

    Tools run from their own subdirectory (e.g. plugin-root/list_notes/), so the
    default config path walks two levels up from this file to reach the plugin root.
    Callers that live elsewhere can pass an explicit config_path.

    If master_token is already present it is used directly. Otherwise oauth_token is
    exchanged for a master_token via gpsoauth, which is then persisted back to
    config.json so subsequent calls skip the exchange.
    """
    if config_path is None:
        config_path = Path(__file__).resolve().parent.parent / "config.json"

    config = json.loads(config_path.read_text())
    email = config["email"]
    master_token = config.get("master_token")
    oauth_token = config.get("oauth_token")

    if master_token:
        pass
    elif oauth_token:
        response = gpsoauth.exchange_token(email, oauth_token, "0123456789abcdef")
        if "Token" not in response:
            raise RuntimeError(response)
        master_token = response["Token"]
        config["master_token"] = master_token
        config_path.write_text(json.dumps(config, indent=2) + "\n")
    else:
        raise RuntimeError("Both master_token and oauth_token are missing from config.json.")

    keep = gkeepapi.Keep()
    keep.authenticate(email, master_token)
    keep.sync()
    return keep
