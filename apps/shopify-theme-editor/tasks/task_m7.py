import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify cart type is 'Drawer' and enableCartNote is true."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    cart = state.get("themeSettings", {}).get("cart", {})

    if cart.get("type") != "Drawer":
        return False, f"Expected cart type 'Drawer', got '{cart.get('type')}'."

    if cart.get("enableCartNote") is not True:
        return False, f"Expected enableCartNote=true, got {cart.get('enableCartNote')}."

    return True, "Cart type is 'Drawer' and cart note is enabled."
