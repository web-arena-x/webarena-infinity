import requests

def verify(server_url: str) -> tuple[bool, str]:
    """Verify 'Accent' color scheme renamed to 'Forest' with new background color."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    settings = next((ts for ts in state["themeSettings"] if ts.get("themeId") == 1), None)
    if not settings:
        return False, "Theme settings for Dawn not found."

    # The Accent scheme had id 3
    scheme = next((c for c in settings.get("colors", []) if c.get("id") == 3), None)
    if not scheme:
        return False, "Color scheme with id 3 not found."

    if scheme.get("name") != "Forest":
        return False, f"Scheme name is '{scheme.get('name')}', expected 'Forest'."

    if scheme.get("background") != "#1b4332":
        return False, f"Background is '{scheme.get('background')}', expected '#1b4332'."

    return True, "Color scheme renamed to 'Forest' with background '#1b4332'."
