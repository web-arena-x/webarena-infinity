import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify showSecondImageOnHover and showVendor are enabled in product cards."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    pc = state.get("themeSettings", {}).get("productCards", {})

    if pc.get("showSecondImageOnHover") is not True:
        return False, f"Expected showSecondImageOnHover=true, got {pc.get('showSecondImageOnHover')}."

    if pc.get("showVendor") is not True:
        return False, f"Expected showVendor=true, got {pc.get('showVendor')}."

    return True, "Show second image on hover and show vendor are both enabled."
