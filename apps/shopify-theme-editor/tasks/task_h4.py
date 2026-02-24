import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify cart: type=Drawer, showVendor=true, enableCartNote=true, drawerCollection='Best Sellers'."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    cart = state.get("themeSettings", {}).get("cart", {})

    if cart.get("type") != "Drawer":
        return False, f"Expected cart type 'Drawer', got '{cart.get('type')}'."

    if cart.get("showVendor") is not True:
        return False, f"Expected showVendor=true, got {cart.get('showVendor')}."

    if cart.get("enableCartNote") is not True:
        return False, f"Expected enableCartNote=true, got {cart.get('enableCartNote')}."

    if cart.get("drawerCollection") != "Best Sellers":
        return False, f"Expected drawerCollection='Best Sellers', got '{cart.get('drawerCollection')}'."

    return True, "Cart settings: Drawer, showVendor, enableCartNote, drawerCollection='Best Sellers'."
