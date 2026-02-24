import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify showCurrencyCodes is enabled."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    val = state.get("themeSettings", {}).get("currencyFormat", {}).get("showCurrencyCodes")
    if val is not True:
        return False, f"Expected showCurrencyCodes=true, got {val}."

    return True, "Show currency codes is enabled."
