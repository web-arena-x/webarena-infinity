import requests

def verify(server_url: str) -> tuple[bool, str]:
    """Verify heading font is 'Montserrat' for Dawn theme."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    settings = next((ts for ts in state["themeSettings"] if ts.get("themeId") == 1), None)
    if not settings:
        return False, "Theme settings for Dawn not found."

    heading_font = settings.get("typography", {}).get("headingFont")
    if heading_font != "Montserrat":
        return False, f"Heading font is '{heading_font}', expected 'Montserrat'."

    return True, "Heading font changed to 'Montserrat'."
