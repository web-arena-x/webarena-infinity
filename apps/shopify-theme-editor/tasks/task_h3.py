import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify theme style is 'Crave' and heading font is overridden to 'Bitter'."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    ts = state.get("themeSettings", {})

    style = ts.get("activeThemeStyle")
    if style != "crave":
        return False, f"Expected activeThemeStyle='crave', got '{style}'."

    font = ts.get("typography", {}).get("headingFont")
    if font != "Bitter":
        return False, f"Expected headingFont='Bitter', got '{font}'."

    return True, "Theme style is 'Crave' with heading font overridden to 'Bitter'."
