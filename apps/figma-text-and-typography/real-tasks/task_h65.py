import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify: Heading/H2 updated to Playfair Display Semi Bold 28px/36px with onum, Section Header reflects."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    text_styles = state.get("textStyles", [])
    text_layers = state.get("textLayers", [])
    errors = []

    style = next((s for s in text_styles if s.get("name") == "Heading/H2"), None)
    if not style:
        return False, "Heading/H2 text style not found."

    if style.get("fontFamily") != "Playfair Display":
        errors.append(f"Style fontFamily: expected 'Playfair Display', got '{style.get('fontFamily')}'.")
    if style.get("fontStyle") != "Semi Bold":
        errors.append(f"Style fontStyle: expected 'Semi Bold', got '{style.get('fontStyle')}'.")
    if style.get("fontSize") != 28:
        errors.append(f"Style fontSize: expected 28, got {style.get('fontSize')}.")
    lh = style.get("lineHeight", {})
    if lh.get("value") != 36 or lh.get("unit") != "px":
        errors.append(f"Style lineHeight: expected 36px, got {lh}.")
    if style.get("openTypeFeatures", {}).get("onum") is not True:
        errors.append("Style: onum not enabled.")

    layer = next((l for l in text_layers if l.get("name") == "Section Header"), None)
    if not layer:
        return False, "Section Header layer not found."

    if layer.get("fontFamily") != "Playfair Display":
        errors.append(f"Section Header fontFamily: expected 'Playfair Display', got '{layer.get('fontFamily')}'.")
    if layer.get("fontSize") != 28:
        errors.append(f"Section Header fontSize: expected 28, got {layer.get('fontSize')}.")
    layer_lh = layer.get("lineHeight", {})
    if layer_lh.get("value") != 36 or layer_lh.get("unit") != "px":
        errors.append(f"Section Header lineHeight: expected 36px, got {layer_lh}.")

    if errors:
        return False, "; ".join(errors)
    return True, "Heading/H2 updated and Section Header reflects changes."
