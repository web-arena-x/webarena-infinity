import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    themes = state.get("brandingThemes", [])

    # Find 'Government' theme
    gov_theme = next((t for t in themes if t.get("name") == "Government"), None)
    if gov_theme is None:
        return False, "Branding theme 'Government' not found."

    if gov_theme.get("showPaymentAdvice") is not False:
        return False, f"Expected showPaymentAdvice=False on Government theme, got {gov_theme.get('showPaymentAdvice')}."

    if gov_theme.get("isDefault") is not True:
        return False, "Government theme is not set as default."

    # Check all other themes are not default
    other_defaults = [t.get("name") for t in themes if t.get("name") != "Government" and t.get("isDefault") is True]
    if other_defaults:
        return False, f"Other themes still marked as default: {', '.join(other_defaults)}."

    return True, "Government branding theme created with payment advice disabled and set as default."
