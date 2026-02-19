import requests

def verify(server_url: str) -> tuple[bool, str]:
    """Verify sale badge position and shape changed for Dawn theme."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    settings = next((ts for ts in state["themeSettings"] if ts.get("themeId") == 1), None)
    if not settings:
        return False, "Theme settings for Dawn not found."

    badges = settings.get("badges", {})
    pos = badges.get("salePosition")
    shape = badges.get("saleShape")

    if pos != "top-right":
        return False, f"Sale badge position is '{pos}', expected 'top-right'."
    if shape != "circle":
        return False, f"Sale badge shape is '{shape}', expected 'circle'."

    return True, "Sale badge position changed to 'top-right' and shape to 'circle'."
