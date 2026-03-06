import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    themes = state.get("brandingThemes", [])

    simple = next((t for t in themes if t.get("id") == "theme_simple" or t.get("name") == "Simple Clean"), None)
    if simple is not None:
        return False, "Simple Clean branding theme still exists in state."

    return True, "Simple Clean branding theme has been deleted successfully."
