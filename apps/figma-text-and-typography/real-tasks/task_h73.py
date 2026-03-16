import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify: Second-largest font size layer has Caption/Small applied and truncation max 2."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    text_layers = state.get("textLayers", [])
    text_styles = state.get("textStyles", [])
    errors = []

    # The second-largest font size in seed data is Release Notes Header (36px)
    layer = next((l for l in text_layers if l.get("name") == "Release Notes Header"), None)
    if not layer:
        return False, "Release Notes Header layer not found."

    caption_style = next((s for s in text_styles if s.get("name") == "Caption/Small"), None)
    if not caption_style:
        return False, "Caption/Small style not found."

    if layer.get("textStyleId") != caption_style["id"]:
        errors.append(f"textStyleId: expected '{caption_style['id']}', got '{layer.get('textStyleId')}'.")
    if layer.get("fontFamily") != caption_style["fontFamily"]:
        errors.append(f"fontFamily: expected '{caption_style['fontFamily']}', got '{layer.get('fontFamily')}'.")
    if layer.get("fontSize") != caption_style["fontSize"]:
        errors.append(f"fontSize: expected {caption_style['fontSize']}, got {layer.get('fontSize')}.")

    trunc = layer.get("truncation", {})
    if trunc.get("enabled") is not True:
        errors.append("truncation not enabled.")
    if trunc.get("maxLines") != 2:
        errors.append(f"truncation maxLines: expected 2, got {trunc.get('maxLines')}.")

    if errors:
        return False, "; ".join(errors)
    return True, "Release Notes Header has Caption/Small style and truncation at 2 lines."
