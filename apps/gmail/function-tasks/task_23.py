import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    density = state["settings"].get("density")
    if density != "compact":
        return False, f"Expected density 'compact', got '{density}'."

    return True, "Display density changed to compact."
