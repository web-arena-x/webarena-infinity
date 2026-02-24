import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify heading font is 'Playfair Display'."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    font = state.get("themeSettings", {}).get("typography", {}).get("headingFont")
    if font != "Playfair Display":
        return False, f"Expected headingFont 'Playfair Display', got '{font}'."

    return True, "Heading font is 'Playfair Display'."
