"""Task H5: Switch to light theme with spacious density, disable keyboard shortcuts, set undo send to 30s."""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    settings = state.get("settings", {})
    general = settings.get("general", {})

    failures = []

    theme = general.get("theme")
    if theme != "light":
        failures.append(f"theme is '{theme}', expected 'light'")

    density = general.get("density")
    if density != "spacious":
        failures.append(f"density is '{density}', expected 'spacious'")

    kbd = general.get("keyboardShortcuts")
    if kbd is not False:
        failures.append(f"keyboardShortcuts is {kbd}, expected False")

    undo = general.get("undoSendDelay")
    if undo != 30:
        failures.append(f"undoSendDelay is {undo}, expected 30")

    if failures:
        return False, "Settings not correct: " + "; ".join(failures)

    return True, "Theme=light, density=spacious, keyboardShortcuts=false, undoSendDelay=30."
