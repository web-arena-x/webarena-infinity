import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    settings = state.get("settings", {})
    general = settings.get("general", {})
    keyboard_shortcuts = general.get("keyboardShortcuts")

    if keyboard_shortcuts is False:
        return True, "Keyboard shortcuts successfully disabled."

    return False, (
        f"keyboardShortcuts is {keyboard_shortcuts}, expected False."
    )
