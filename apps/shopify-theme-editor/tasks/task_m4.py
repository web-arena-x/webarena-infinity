import requests

def verify(server_url: str) -> tuple[bool, str]:
    """Verify hover effect changed to '3d-lift' for Dawn theme."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    settings = next((ts for ts in state["themeSettings"] if ts.get("themeId") == 1), None)
    if not settings:
        return False, "Theme settings for Dawn not found."

    effect = settings.get("animations", {}).get("hoverEffect")
    if effect != "3d-lift":
        return False, f"Hover effect is '{effect}', expected '3d-lift'."

    return True, "Hover effect changed to '3D lift'."
