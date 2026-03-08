import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Set default font to Playfair Display and size to 24, then create 'Hero Title' layer."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    prefs = state.get("preferences", {})
    text_layers = state.get("textLayers", [])
    errors = []

    # Check preferences updated
    if prefs.get("defaultFontFamily") != "Playfair Display":
        errors.append(f"defaultFontFamily: expected 'Playfair Display', got '{prefs.get('defaultFontFamily')}'")
    if prefs.get("defaultFontSize") != 24:
        errors.append(f"defaultFontSize: expected 24, got {prefs.get('defaultFontSize')}")

    # Check new layer exists with correct properties
    hero = next((l for l in text_layers if l.get("content") == "Hero Title"), None)
    if not hero:
        hero = next((l for l in text_layers if l.get("name") == "Hero Title"), None)

    if not hero:
        errors.append("Layer with text 'Hero Title' not found.")
    else:
        if hero.get("fontFamily") != "Playfair Display":
            errors.append(f"Hero Title fontFamily: expected 'Playfair Display', got '{hero.get('fontFamily')}'")
        if hero.get("fontSize") != 24:
            errors.append(f"Hero Title fontSize: expected 24, got {hero.get('fontSize')}")

    if errors:
        return False, "; ".join(errors)
    return True, "Defaults updated and 'Hero Title' layer created with Playfair Display at 24px."
