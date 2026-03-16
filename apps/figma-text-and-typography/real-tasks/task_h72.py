import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify: Code Sample switched to Fira Code Medium 15px/24px, ss01+zero, style detached."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    text_layers = state.get("textLayers", [])
    errors = []

    layer = next((l for l in text_layers if l.get("name") == "Code Sample"), None)
    if not layer:
        return False, "Code Sample layer not found."

    if layer.get("fontFamily") != "Fira Code":
        errors.append(f"fontFamily: expected 'Fira Code', got '{layer.get('fontFamily')}'.")
    if layer.get("fontStyle") != "Medium":
        errors.append(f"fontStyle: expected 'Medium', got '{layer.get('fontStyle')}'.")
    if layer.get("fontSize") != 15:
        errors.append(f"fontSize: expected 15, got {layer.get('fontSize')}.")
    lh = layer.get("lineHeight", {})
    if lh.get("value") != 24 or lh.get("unit") != "px":
        errors.append(f"lineHeight: expected 24px, got {lh}.")

    features = layer.get("openTypeFeatures", {})
    if features.get("ss01") is not True:
        errors.append("ss01 not enabled.")
    if features.get("zero") is not True:
        errors.append("zero not enabled.")

    if layer.get("textStyleId") is not None:
        errors.append(f"textStyleId: expected null, got '{layer.get('textStyleId')}'.")

    if errors:
        return False, "; ".join(errors)
    return True, "Code Sample updated to Fira Code Medium 15px/24px with ss01+zero, style detached."
