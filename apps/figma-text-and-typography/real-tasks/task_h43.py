import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify: Set spelling language to match the bold RTL layer's script, then hide that layer."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    text_layers = state.get("textLayers", [])
    preferences = state.get("preferences", {})
    errors = []

    # The only bold RTL layer is Arabic Welcome (Noto Sans Arabic, Bold, rtl)
    arabic_layer = next((l for l in text_layers if l.get("name") == "Arabic Welcome"), None)
    if not arabic_layer:
        return False, "Arabic Welcome layer not found."

    # Spelling language should be Arabic
    lang = preferences.get("spellingLanguage")
    if lang != "Arabic":
        errors.append(f"Expected spellingLanguage 'Arabic', got '{lang}'.")

    # Layer should be hidden
    if arabic_layer.get("visible") is not False:
        errors.append("Arabic Welcome layer should be hidden (visible=false).")

    if errors:
        return False, "; ".join(errors)
    return True, "Spelling language set to Arabic and Arabic Welcome layer hidden."
