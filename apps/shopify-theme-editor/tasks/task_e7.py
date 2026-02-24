import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify hover effect is 'Vertical lift'."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    val = state.get("themeSettings", {}).get("animations", {}).get("hoverEffect")
    if val != "Vertical lift":
        return False, f"Expected hoverEffect 'Vertical lift', got '{val}'."

    return True, "Hover effect is 'Vertical lift'."
