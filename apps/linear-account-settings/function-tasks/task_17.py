import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    val = state["preferences"]["interfaceAndTheme"]["theme"]
    if val != "dark":
        return False, f"Expected theme 'dark', got '{val}'."

    return True, "Theme set to 'dark'."
