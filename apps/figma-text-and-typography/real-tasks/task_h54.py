import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify: Update Body/Regular to 15px/22px line height, then detach from all layers."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    text_layers = state.get("textLayers", [])
    text_styles = state.get("textStyles", [])
    errors = []

    # Body/Regular style should be updated
    style = next((s for s in text_styles if s.get("name") == "Body/Regular"), None)
    if not style:
        return False, "Body/Regular text style not found."

    if style.get("fontSize") != 15:
        errors.append(f"Style fontSize: expected 15, got {style.get('fontSize')}.")

    lh = style.get("lineHeight", {})
    if lh.get("value") != 22 or lh.get("unit") != "px":
        errors.append(f"Style lineHeight: expected 22px, got {lh}.")

    # Body Text (tl_002) should have updated properties AND be detached
    body = next((l for l in text_layers if l.get("name") == "Body Text"), None)
    if not body:
        return False, "Body Text layer not found."

    if body.get("fontSize") != 15:
        errors.append(f"Body Text fontSize: expected 15, got {body.get('fontSize')}.")

    body_lh = body.get("lineHeight", {})
    if body_lh.get("value") != 22 or body_lh.get("unit") != "px":
        errors.append(f"Body Text lineHeight: expected 22px, got {body_lh}.")

    if body.get("textStyleId") is not None:
        errors.append(f"Body Text should be detached (textStyleId=null), got '{body.get('textStyleId')}'.")

    # No layer should reference Body/Regular
    for layer in text_layers:
        if layer.get("textStyleId") == style["id"]:
            errors.append(f"'{layer['name']}' still has Body/Regular applied — should be detached.")

    if errors:
        return False, "; ".join(errors)
    return True, "Body/Regular updated to 15px/22px and detached from all layers."
