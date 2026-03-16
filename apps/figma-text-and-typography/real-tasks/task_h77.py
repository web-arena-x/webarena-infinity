import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify: Body Text changed to Lato Regular, 24px lh, detached, indent 16, auto-width."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    text_layers = state.get("textLayers", [])
    errors = []

    layer = next((l for l in text_layers if l.get("name") == "Body Text"), None)
    if not layer:
        return False, "Body Text layer not found."

    if layer.get("fontFamily") != "Lato":
        errors.append(f"fontFamily: expected 'Lato', got '{layer.get('fontFamily')}'.")
    if layer.get("fontStyle") != "Regular":
        errors.append(f"fontStyle: expected 'Regular', got '{layer.get('fontStyle')}'.")
    lh = layer.get("lineHeight", {})
    if lh.get("value") != 24 or lh.get("unit") != "px":
        errors.append(f"lineHeight: expected 24px, got {lh}.")
    if layer.get("textStyleId") is not None:
        errors.append(f"textStyleId: expected null, got '{layer.get('textStyleId')}'.")
    if layer.get("paragraphIndent") != 16:
        errors.append(f"paragraphIndent: expected 16, got {layer.get('paragraphIndent')}.")
    if layer.get("resizing") != "auto-width":
        errors.append(f"resizing: expected 'auto-width', got '{layer.get('resizing')}'.")

    if errors:
        return False, "; ".join(errors)
    return True, "Body Text updated: Lato Regular, 24px lh, detached, indent 16, auto-width."
