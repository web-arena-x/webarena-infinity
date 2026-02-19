import requests

def verify(server_url: str) -> tuple[bool, str]:
    """Verify currency codes are shown for Dawn theme."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    settings = next((ts for ts in state["themeSettings"] if ts.get("themeId") == 1), None)
    if not settings:
        return False, "Theme settings for Dawn not found."

    show_code = settings.get("currencyFormat", {}).get("showCurrencyCode")
    if show_code is not True:
        return False, f"Currency codes not enabled (value: {show_code})."

    return True, "Currency codes enabled."
