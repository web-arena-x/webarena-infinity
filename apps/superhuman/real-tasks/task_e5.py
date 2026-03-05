"""Task E5: Switch to light mode."""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    try:
        theme = state["settings"]["general"]["theme"]
    except (KeyError, TypeError) as e:
        return False, f"Could not read settings.general.theme: {e}"

    if theme != "light":
        return False, f"Theme is '{theme}' — expected 'light'"

    return True, "Theme is set to 'light'."
