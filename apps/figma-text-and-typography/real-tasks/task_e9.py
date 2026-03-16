"""
Task: Disable snap to grid.
Verify: preferences.snapToGrid is False.
"""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    preferences = state.get("preferences", {})
    snap_to_grid = preferences.get("snapToGrid")

    if snap_to_grid is not False:
        return False, f"Expected 'snapToGrid' to be False, got '{snap_to_grid}'."

    return True, "Snap to grid is disabled."
