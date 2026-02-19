import requests

def verify(server_url):
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()
    dawn = next((t for t in state["themes"] if t["name"] == "Dawn"), None)
    if not dawn:
        return False, "Theme 'Dawn' not found."
    settings = dawn.get("settings", {})
    if settings.get("stickyHeader") != False:
        return False, f"Sticky header should be disabled (got {settings.get('stickyHeader')})."
    if settings.get("cartType") != "page":
        return False, f"Expected cart type 'page', got '{settings.get('cartType')}'."
    return True, "Dawn theme settings updated: sticky header disabled, cart type=page."
