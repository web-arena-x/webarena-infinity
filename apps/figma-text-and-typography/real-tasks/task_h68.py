import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify: Default font set to Montserrat 14 (matching the layer with widest letter spacing)."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    prefs = state.get("preferences", {})
    errors = []

    # The layer with the widest letter spacing is Small Caps Header (0.1em, Montserrat 14px)
    if prefs.get("defaultFontFamily") != "Montserrat":
        errors.append(f"defaultFontFamily: expected 'Montserrat', got '{prefs.get('defaultFontFamily')}'.")
    if prefs.get("defaultFontSize") != 14:
        errors.append(f"defaultFontSize: expected 14, got {prefs.get('defaultFontSize')}.")

    if errors:
        return False, "; ".join(errors)
    return True, "Default font set to Montserrat 14 (widest letter spacing layer)."
