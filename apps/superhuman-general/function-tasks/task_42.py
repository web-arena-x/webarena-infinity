import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    settings = state.get("settings", {})
    keyboard = settings.get("keyboard", {})
    shortcuts = keyboard.get("shortcuts")

    if shortcuts is not False:
        return False, f"Expected keyboard.shortcuts to be False, got {shortcuts}."

    return True, "Keyboard shortcuts are disabled."
