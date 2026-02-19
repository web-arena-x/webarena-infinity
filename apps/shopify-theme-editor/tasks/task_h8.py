import requests

def verify(server_url: str) -> tuple[bool, str]:
    """Verify typography fonts and page width changed for Dawn theme."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    settings = next((ts for ts in state["themeSettings"] if ts.get("themeId") == 1), None)
    if not settings:
        return False, "Theme settings for Dawn not found."

    heading = settings.get("typography", {}).get("headingFont")
    if heading != "Playfair Display":
        return False, f"Heading font is '{heading}', expected 'Playfair Display'."

    body = settings.get("typography", {}).get("bodyFont")
    if body != "Lato":
        return False, f"Body font is '{body}', expected 'Lato'."

    width = settings.get("layout", {}).get("pageWidth")
    if width != 1400:
        return False, f"Page width is {width}, expected 1400."

    return True, "Fonts changed and page width set to 1400."
