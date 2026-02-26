"""Set auto-advance to go to the previous (older) conversation."""

import requests


def verify(server_url: str) -> tuple[bool, str]:
    response = requests.get(f"{server_url}/api/state")
    if response.status_code != 200:
        return False, f"Failed to fetch state: HTTP {response.status_code}"

    state = response.json()

    auto_advance = state.get("settings", {}).get("autoAdvance")
    if auto_advance == "older":
        return True, "Auto-advance is set to 'older'."
    return False, f"Expected autoAdvance to be 'older', got {auto_advance!r}."
