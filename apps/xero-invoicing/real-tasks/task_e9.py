import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    themes = state.get("brandingThemes", [])
    if not themes:
        return False, "No branding themes found in state."

    professional = next((t for t in themes if t.get("name") == "Professional Services"), None)
    if professional is None:
        professional = next((t for t in themes if t.get("id") == "theme_professional"), None)
    if professional is None:
        return False, "Professional Services branding theme not found."

    if not professional.get("isDefault"):
        return False, "Professional Services theme is not set as default."

    others_with_default = [t for t in themes if t.get("id") != professional.get("id") and t.get("isDefault")]
    if others_with_default:
        names = ", ".join(t.get("name", t.get("id")) for t in others_with_default)
        return False, f"Other themes still have isDefault=True: {names}."

    return True, "Professional Services is now the default branding theme."
