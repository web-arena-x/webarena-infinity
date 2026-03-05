import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    settings = state.get("settings", {})
    general = settings.get("general", {})
    theme = general.get("theme")

    if theme == "light":
        return True, "Theme successfully changed to 'light'."

    return False, f"Theme is '{theme}', expected 'light'."
