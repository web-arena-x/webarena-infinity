import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify: 'Sidebar Navigation' layer with Space Grotesk Bold 13px, uppercase, 0.08em, zero."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    text_layers = state.get("textLayers", [])
    errors = []

    layer = next((l for l in text_layers if l.get("name") == "Sidebar Navigation"), None)
    if not layer:
        return False, "Sidebar Navigation layer not found."

    if "Sidebar Navigation" not in layer.get("content", ""):
        errors.append(f"Content should contain 'Sidebar Navigation', got '{layer.get('content')}'.")
    if layer.get("fontFamily") != "Space Grotesk":
        errors.append(f"fontFamily: expected 'Space Grotesk', got '{layer.get('fontFamily')}'.")
    if layer.get("fontStyle") != "Bold":
        errors.append(f"fontStyle: expected 'Bold', got '{layer.get('fontStyle')}'.")
    if layer.get("fontSize") != 13:
        errors.append(f"fontSize: expected 13, got {layer.get('fontSize')}.")
    lh = layer.get("lineHeight", {})
    if lh.get("value") != 18 or lh.get("unit") != "px":
        errors.append(f"lineHeight: expected 18px, got {lh}.")
    if layer.get("letterCase") != "uppercase":
        errors.append(f"letterCase: expected 'uppercase', got '{layer.get('letterCase')}'.")
    ls = layer.get("letterSpacing", {})
    if ls.get("value") != 0.08 or ls.get("unit") != "em":
        errors.append(f"letterSpacing: expected 0.08em, got {ls}.")
    if layer.get("openTypeFeatures", {}).get("zero") is not True:
        errors.append("zero OpenType feature not enabled.")

    if errors:
        return False, "; ".join(errors)
    return True, "Sidebar Navigation layer created with correct properties."
