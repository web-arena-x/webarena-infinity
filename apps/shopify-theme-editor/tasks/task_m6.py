import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify showVendor and showPrice are both enabled in Search behavior."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    sb = state.get("themeSettings", {}).get("searchBehavior", {})

    if sb.get("showVendor") is not True:
        return False, f"Expected showVendor=true, got {sb.get('showVendor')}."

    if sb.get("showPrice") is not True:
        return False, f"Expected showPrice=true, got {sb.get('showPrice')}."

    return True, "Show vendor and show price are both enabled in search behavior."
