import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify Instagram link is set."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    val = state.get("themeSettings", {}).get("socialMedia", {}).get("instagram")
    expected = "https://instagram.com/mystorefront"
    if val != expected:
        return False, f"Expected instagram='{expected}', got '{val}'."

    return True, "Instagram link is set correctly."
