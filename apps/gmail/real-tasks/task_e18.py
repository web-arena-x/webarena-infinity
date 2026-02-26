"""
Task: Turn off keyboard shortcuts.
Verify: state["settings"]["keyboardShortcutsEnabled"] == False.
"""

import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"

    state = resp.json()
    settings = state.get("settings", {})

    shortcuts_enabled = settings.get("keyboardShortcutsEnabled")
    if shortcuts_enabled is not False:
        return False, (
            f"Keyboard shortcuts are not disabled. "
            f"keyboardShortcutsEnabled={shortcuts_enabled}"
        )

    return True, "Keyboard shortcuts are disabled (keyboardShortcutsEnabled=False)."
