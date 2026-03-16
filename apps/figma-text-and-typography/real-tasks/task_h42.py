import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify: Apply the style with the widest letter spacing to Variable Font Demo."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    text_layers = state.get("textLayers", [])
    text_styles = state.get("textStyles", [])
    errors = []

    # The style with the widest letter spacing is Label/SmallCaps (0.1 em)
    target_style = next((s for s in text_styles if s.get("name") == "Label/SmallCaps"), None)
    if not target_style:
        return False, "Label/SmallCaps text style not found."

    layer = next((l for l in text_layers if l.get("name") == "Variable Font Demo"), None)
    if not layer:
        return False, "Variable Font Demo layer not found."

    if layer.get("textStyleId") != target_style["id"]:
        errors.append(f"Expected textStyleId '{target_style['id']}', got '{layer.get('textStyleId')}'.")

    if layer.get("fontFamily") != target_style["fontFamily"]:
        errors.append(f"Expected fontFamily '{target_style['fontFamily']}', got '{layer.get('fontFamily')}'.")

    if layer.get("fontStyle") != target_style["fontStyle"]:
        errors.append(f"Expected fontStyle '{target_style['fontStyle']}', got '{layer.get('fontStyle')}'.")

    if layer.get("fontSize") != target_style["fontSize"]:
        errors.append(f"Expected fontSize {target_style['fontSize']}, got {layer.get('fontSize')}.")

    ls = layer.get("letterSpacing", {})
    if ls.get("value") != 0.1 or ls.get("unit") != "em":
        errors.append(f"Expected letterSpacing 0.1 em, got {ls}.")

    if errors:
        return False, "; ".join(errors)
    return True, "Label/SmallCaps style (widest letter spacing) applied to Variable Font Demo."
