import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    theme = state["settings"].get("theme")
    if theme != "dark":
        return False, f"Expected theme 'dark', got '{theme}'."

    return True, "Theme changed to dark mode."
