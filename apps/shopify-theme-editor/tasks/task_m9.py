import requests

def verify(server_url: str) -> tuple[bool, str]:
    """Verify button style changed to 'pill' for Dawn theme."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    settings = next((ts for ts in state["themeSettings"] if ts.get("themeId") == 1), None)
    if not settings:
        return False, "Theme settings for Dawn not found."

    style = settings.get("buttons", {}).get("style")
    if style != "pill":
        return False, f"Button style is '{style}', expected 'pill'."

    return True, "Button style changed to 'pill'."
