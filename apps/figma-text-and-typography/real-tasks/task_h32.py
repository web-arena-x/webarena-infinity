import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Apply Body/Regular style to Strikethrough Example, then change decoration to underline."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    text_layers = state.get("textLayers", [])
    text_styles = state.get("textStyles", [])
    errors = []

    # Find the Body/Regular style
    body_style = next((s for s in text_styles if s.get("name") == "Body/Regular"), None)
    if not body_style:
        return False, "Body/Regular text style not found."

    # Find the Strikethrough Example layer
    layer = next((l for l in text_layers if l.get("name") == "Strikethrough Example"), None)
    if not layer:
        return False, "Strikethrough Example layer not found."

    if layer.get("textStyleId") != body_style.get("id"):
        errors.append(f"textStyleId: expected '{body_style.get('id')}', got '{layer.get('textStyleId')}'")

    if layer.get("fontFamily") != body_style.get("fontFamily"):
        errors.append(f"fontFamily: expected '{body_style.get('fontFamily')}', got '{layer.get('fontFamily')}'")

    if layer.get("fontSize") != body_style.get("fontSize"):
        errors.append(f"fontSize: expected {body_style.get('fontSize')}, got {layer.get('fontSize')}")

    if layer.get("textDecoration") != "underline":
        errors.append(f"textDecoration: expected 'underline', got '{layer.get('textDecoration')}'")

    if errors:
        return False, "; ".join(errors)
    return True, "Body/Regular applied to Strikethrough Example with underline decoration."
