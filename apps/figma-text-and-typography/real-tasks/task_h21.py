import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Create a 'Quote/Block' style with Playfair Display Regular 18px/28px line height, then apply it to Indented Quote."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    text_styles = state.get("textStyles", [])
    text_layers = state.get("textLayers", [])
    errors = []

    # Check the style exists
    qb_style = next((s for s in text_styles if s.get("name") == "Quote/Block"), None)
    if not qb_style:
        return False, "Text style 'Quote/Block' not found."

    if qb_style.get("fontFamily") != "Playfair Display":
        errors.append(f"Style fontFamily: expected 'Playfair Display', got '{qb_style.get('fontFamily')}'")
    if qb_style.get("fontStyle") != "Regular":
        errors.append(f"Style fontStyle: expected 'Regular', got '{qb_style.get('fontStyle')}'")
    if qb_style.get("fontSize") != 18:
        errors.append(f"Style fontSize: expected 18, got {qb_style.get('fontSize')}")
    lh = qb_style.get("lineHeight", {})
    if lh.get("value") != 28 or lh.get("unit") != "px":
        errors.append(f"Style lineHeight: expected 28px, got {lh}")

    # Check Indented Quote uses the style
    layer = next((l for l in text_layers if l.get("name") == "Indented Quote"), None)
    if not layer:
        errors.append("Text layer 'Indented Quote' not found.")
    elif layer.get("textStyleId") != qb_style.get("id"):
        errors.append(f"Indented Quote textStyleId: expected '{qb_style.get('id')}', got '{layer.get('textStyleId')}'")
    elif layer.get("fontFamily") != "Playfair Display":
        errors.append(f"Indented Quote fontFamily not updated to 'Playfair Display'")
    elif layer.get("fontSize") != 18:
        errors.append(f"Indented Quote fontSize: expected 18, got {layer.get('fontSize')}")

    if errors:
        return False, "; ".join(errors)
    return True, "Quote/Block style created and applied to Indented Quote correctly."
