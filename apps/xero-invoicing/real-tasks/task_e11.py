import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    themes = state.get("brandingThemes", [])

    standard = next((t for t in themes if t.get("name") == "Standard" or t.get("id") == "theme_standard"), None)
    if standard is None:
        return False, "Standard branding theme not found."

    if standard.get("showTaxNumber") is not False:
        return False, f"Expected Standard theme showTaxNumber to be False, got {standard.get('showTaxNumber')}."

    return True, "Tax number display has been turned off on the Standard theme."
