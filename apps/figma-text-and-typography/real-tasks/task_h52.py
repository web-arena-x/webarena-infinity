import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify: Create Code/Block style from Code Sample properties and apply it."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    text_layers = state.get("textLayers", [])
    text_styles = state.get("textStyles", [])
    errors = []

    # Code/Block style should exist
    cb_style = next((s for s in text_styles if s.get("name") == "Code/Block"), None)
    if not cb_style:
        return False, "Code/Block text style not found."

    # Check style properties match Code Sample's original properties
    if cb_style.get("fontFamily") != "JetBrains Mono":
        errors.append(f"Style fontFamily: expected 'JetBrains Mono', got '{cb_style.get('fontFamily')}'.")
    if cb_style.get("fontStyle") != "Regular":
        errors.append(f"Style fontStyle: expected 'Regular', got '{cb_style.get('fontStyle')}'.")
    if cb_style.get("fontSize") != 13:
        errors.append(f"Style fontSize: expected 13, got {cb_style.get('fontSize')}.")

    lh = cb_style.get("lineHeight", {})
    if lh.get("value") != 22 or lh.get("unit") != "px":
        errors.append(f"Style lineHeight: expected 22px, got {lh}.")

    # Code Sample should have the style applied
    layer = next((l for l in text_layers if l.get("name") == "Code Sample"), None)
    if not layer:
        return False, "Code Sample layer not found."

    if layer.get("textStyleId") != cb_style["id"]:
        errors.append(f"Code Sample: expected textStyleId '{cb_style['id']}', got '{layer.get('textStyleId')}'.")

    if errors:
        return False, "; ".join(errors)
    return True, "Code/Block style created from Code Sample properties and applied."
