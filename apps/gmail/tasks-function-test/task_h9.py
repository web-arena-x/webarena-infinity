import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    settings = state.get("settings", {})

    if settings.get("keyboardShortcutsEnabled") is not False:
        return False, f"settings.keyboardShortcutsEnabled is {settings.get('keyboardShortcutsEnabled')}, expected False."

    if settings.get("importanceMarkers") is not False:
        return False, f"settings.importanceMarkers is {settings.get('importanceMarkers')}, expected False."

    if settings.get("hoverActions") is not False:
        return False, f"settings.hoverActions is {settings.get('hoverActions')}, expected False."

    if settings.get("density") != "compact":
        return False, f"settings.density is '{settings.get('density')}', expected 'compact'."

    return True, "Task completed successfully."
