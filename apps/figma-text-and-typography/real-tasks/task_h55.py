import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify: Create Serif/Quote style from the only serif layer and apply it."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    text_layers = state.get("textLayers", [])
    text_styles = state.get("textStyles", [])
    errors = []

    # Serif/Quote style should exist
    sq_style = next((s for s in text_styles if s.get("name") == "Serif/Quote"), None)
    if not sq_style:
        return False, "Serif/Quote text style not found."

    # Should match Indented Quote's original properties
    if sq_style.get("fontFamily") != "Playfair Display":
        errors.append(f"Style fontFamily: expected 'Playfair Display', got '{sq_style.get('fontFamily')}'.")
    if sq_style.get("fontStyle") != "Regular":
        errors.append(f"Style fontStyle: expected 'Regular', got '{sq_style.get('fontStyle')}'.")
    if sq_style.get("fontSize") != 22:
        errors.append(f"Style fontSize: expected 22, got {sq_style.get('fontSize')}.")

    lh = sq_style.get("lineHeight", {})
    if lh.get("value") != 32 or lh.get("unit") != "px":
        errors.append(f"Style lineHeight: expected 32px, got {lh}.")

    # Indented Quote should have the style applied
    layer = next((l for l in text_layers if l.get("name") == "Indented Quote"), None)
    if not layer:
        return False, "Indented Quote layer not found."

    if layer.get("textStyleId") != sq_style["id"]:
        errors.append(f"Indented Quote: expected textStyleId '{sq_style['id']}', got '{layer.get('textStyleId')}'.")

    if errors:
        return False, "; ".join(errors)
    return True, "Serif/Quote style created from Indented Quote (only serif layer) and applied."
