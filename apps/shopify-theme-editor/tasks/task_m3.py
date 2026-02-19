import requests

def verify(server_url: str) -> tuple[bool, str]:
    """Verify cart type changed to 'page' for Dawn theme."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    settings = next((ts for ts in state["themeSettings"] if ts.get("themeId") == 1), None)
    if not settings:
        return False, "Theme settings for Dawn not found."

    cart_type = settings.get("cart", {}).get("type")
    if cart_type != "page":
        return False, f"Cart type is '{cart_type}', expected 'page'."

    return True, "Cart type changed to 'page'."
