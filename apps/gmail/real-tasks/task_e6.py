"""
Task: Switch to dark mode.
Verify: state["settings"]["theme"] == "dark".
"""

import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"

    state = resp.json()
    settings = state.get("settings", {})

    theme = settings.get("theme")
    if theme != "dark":
        return False, (
            f"Theme is not set to dark mode. "
            f"theme='{theme}' (expected 'dark')"
        )

    return True, "Theme is set to dark mode (theme='dark')."
