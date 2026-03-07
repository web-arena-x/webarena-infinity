import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    settings = state.get("settings", {})
    secondary_tz = settings.get("secondaryTimezone")

    if secondary_tz is None or secondary_tz == "" or str(secondary_tz).lower() == "none":
        return True, f"Secondary timezone set to None (value={secondary_tz!r})."

    return False, f"Expected secondaryTimezone to be None/empty/'none', got '{secondary_tz}'."
