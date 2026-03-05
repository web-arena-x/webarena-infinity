"""Task E12: Disable keyboard shortcuts."""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    try:
        kbd_shortcuts = state["settings"]["general"]["keyboardShortcuts"]
    except (KeyError, TypeError) as e:
        return False, f"Could not read settings.general.keyboardShortcuts: {e}"

    if kbd_shortcuts is not False:
        return False, f"keyboardShortcuts is {kbd_shortcuts} — expected False"

    return True, "Keyboard shortcuts are disabled."
