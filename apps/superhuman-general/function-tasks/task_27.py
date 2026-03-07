import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    settings = state["settings"]

    theme = settings.get("theme")
    if theme == "dark":
        return True, "Theme has been changed to dark."
    return False, f"Theme is '{theme}', expected 'dark'."
