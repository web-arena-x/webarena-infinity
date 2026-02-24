import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify cart type is 'Page'."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    val = state.get("themeSettings", {}).get("cart", {}).get("type")
    if val != "Page":
        return False, f"Expected cart type 'Page', got '{val}'."

    return True, "Cart type is 'Page'."
