import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Create 'Navigation Menu' layer: Montserrat Medium 14px, small-caps, smcp enabled."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    text_layers = state.get("textLayers", [])
    errors = []

    # Find the new layer
    target = next((l for l in text_layers if l.get("content") == "Navigation Menu"), None)
    if not target:
        target = next((l for l in text_layers if l.get("name") == "Navigation Menu"), None)

    if not target:
        return False, "Layer with text 'Navigation Menu' not found."

    if target.get("fontFamily") != "Montserrat":
        errors.append(f"fontFamily: expected 'Montserrat', got '{target.get('fontFamily')}'")
    if target.get("fontStyle") != "Medium":
        errors.append(f"fontStyle: expected 'Medium', got '{target.get('fontStyle')}'")
    if target.get("fontSize") != 14:
        errors.append(f"fontSize: expected 14, got {target.get('fontSize')}")
    if target.get("letterCase") != "small-caps":
        errors.append(f"letterCase: expected 'small-caps', got '{target.get('letterCase')}'")

    otf = target.get("openTypeFeatures", {})
    if otf.get("smcp") is not True:
        errors.append("smcp OpenType feature not enabled")

    if errors:
        return False, "; ".join(errors)
    return True, "Navigation Menu layer created with Montserrat Medium 14px, small-caps, and smcp."
