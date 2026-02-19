import requests

def verify(server_url: str) -> tuple[bool, str]:
    """Verify YouTube URL set for Dawn theme."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    settings = next((ts for ts in state["themeSettings"] if ts.get("themeId") == 1), None)
    if not settings:
        return False, "Theme settings for Dawn not found."

    youtube = settings.get("socialLinks", {}).get("youtube")
    if youtube != "https://youtube.com/@northwindtraders":
        return False, f"YouTube URL is '{youtube}', expected 'https://youtube.com/@northwindtraders'."

    return True, "YouTube URL set correctly."
