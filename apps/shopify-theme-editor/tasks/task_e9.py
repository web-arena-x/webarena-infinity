import requests

def verify(server_url: str) -> tuple[bool, str]:
    """Verify search suggestions are disabled for Dawn theme."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    settings = next((ts for ts in state["themeSettings"] if ts.get("themeId") == 1), None)
    if not settings:
        return False, "Theme settings for Dawn not found."

    enabled = settings.get("searchBehavior", {}).get("enableSuggestions")
    if enabled is not False:
        return False, f"Search suggestions are still enabled (value: {enabled})."

    return True, "Search suggestions disabled."
