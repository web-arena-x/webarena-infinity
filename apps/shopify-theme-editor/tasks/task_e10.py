import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify search suggestions is disabled."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    val = state.get("themeSettings", {}).get("searchBehavior", {}).get("enableSuggestions")
    if val is not False:
        return False, f"Expected enableSuggestions=false, got {val}."

    return True, "Search suggestions is disabled."
