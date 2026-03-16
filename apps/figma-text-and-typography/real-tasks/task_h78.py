import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify: Heading/Hero style created and applied to Page Title."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    text_styles = state.get("textStyles", [])
    text_layers = state.get("textLayers", [])
    errors = []

    style = next((s for s in text_styles if s.get("name") == "Heading/Hero"), None)
    if not style:
        return False, "Heading/Hero text style not found."

    if style.get("fontFamily") != "Playfair Display":
        errors.append(f"Style fontFamily: expected 'Playfair Display', got '{style.get('fontFamily')}'.")
    if style.get("fontStyle") != "Bold":
        errors.append(f"Style fontStyle: expected 'Bold', got '{style.get('fontStyle')}'.")
    if style.get("fontSize") != 56:
        errors.append(f"Style fontSize: expected 56, got {style.get('fontSize')}.")
    lh = style.get("lineHeight", {})
    if lh.get("value") != 64 or lh.get("unit") != "px":
        errors.append(f"Style lineHeight: expected 64px, got {lh}.")
    ls = style.get("letterSpacing", {})
    if ls.get("value") != -0.03 or ls.get("unit") != "em":
        errors.append(f"Style letterSpacing: expected -0.03em, got {ls}.")
    if style.get("openTypeFeatures", {}).get("ss01") is not True:
        errors.append("Style: ss01 not enabled.")

    layer = next((l for l in text_layers if l.get("id") == "tl_001"), None)
    if not layer:
        return False, "Page Title layer not found."
    if layer.get("textStyleId") != style["id"]:
        errors.append(f"Page Title textStyleId: expected '{style['id']}', got '{layer.get('textStyleId')}'.")
    if layer.get("fontFamily") != "Playfair Display":
        errors.append(f"Page Title fontFamily: expected 'Playfair Display', got '{layer.get('fontFamily')}'.")
    if layer.get("fontSize") != 56:
        errors.append(f"Page Title fontSize: expected 56, got {layer.get('fontSize')}.")

    if errors:
        return False, "; ".join(errors)
    return True, "Heading/Hero style created and applied to Page Title."
