import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify: Variable Font Demo changed to Source Code Pro, weight 700, ss01+zero, 0.05em, center."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    text_layers = state.get("textLayers", [])
    errors = []

    layer = next((l for l in text_layers if l.get("name") == "Variable Font Demo"), None)
    if not layer:
        return False, "Variable Font Demo layer not found."

    if layer.get("fontFamily") != "Source Code Pro":
        errors.append(f"fontFamily: expected 'Source Code Pro', got '{layer.get('fontFamily')}'.")
    axes = layer.get("variableAxes", {})
    if axes.get("wght") != 700:
        errors.append(f"variableAxes.wght: expected 700, got {axes.get('wght')}.")

    features = layer.get("openTypeFeatures", {})
    if features.get("ss01") is not True:
        errors.append("ss01 not enabled.")
    if features.get("zero") is not True:
        errors.append("zero not enabled.")

    ls = layer.get("letterSpacing", {})
    if ls.get("value") != 0.05 or ls.get("unit") != "em":
        errors.append(f"letterSpacing: expected 0.05em, got {ls}.")
    if layer.get("horizontalAlign") != "center":
        errors.append(f"horizontalAlign: expected 'center', got '{layer.get('horizontalAlign')}'.")

    if errors:
        return False, "; ".join(errors)
    return True, "Variable Font Demo updated to Source Code Pro with all properties correct."
