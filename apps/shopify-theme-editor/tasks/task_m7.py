import requests

def verify(server_url: str) -> tuple[bool, str]:
    """Verify a new color scheme was added to Dawn theme."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    settings = next((ts for ts in state["themeSettings"] if ts.get("themeId") == 1), None)
    if not settings:
        return False, "Theme settings for Dawn not found."

    colors = settings.get("colors", [])
    # Seed has 5 color schemes
    if len(colors) <= 5:
        return False, f"Expected more than 5 color schemes, found {len(colors)}."

    return True, f"New color scheme added. Total: {len(colors)}."
