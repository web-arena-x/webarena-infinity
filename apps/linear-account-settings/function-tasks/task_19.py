import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    val = state["preferences"]["interfaceAndTheme"]["fontSize"]
    if val != "large":
        return False, f"Expected font size 'large', got '{val}'."

    return True, "Font size set to 'large'."
