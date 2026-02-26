"""
Task: Switch to compact display density.
Verify: state["settings"]["density"] == "compact".
"""

import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"

    state = resp.json()
    settings = state.get("settings", {})

    density = settings.get("density")
    if density != "compact":
        return False, (
            f"Display density is not 'compact'. "
            f"density='{density}'"
        )

    return True, "Display density is set to 'compact'."
