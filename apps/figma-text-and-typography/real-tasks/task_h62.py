import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify: Heading/Display style halved to 32px, Crimson Text Bold, applied to Japanese Heading."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    text_styles = state.get("textStyles", [])
    text_layers = state.get("textLayers", [])
    errors = []

    style = next((s for s in text_styles if s.get("name") == "Heading/Display"), None)
    if not style:
        return False, "Heading/Display text style not found."

    if style.get("fontSize") != 32:
        errors.append(f"Style fontSize: expected 32, got {style.get('fontSize')}.")
    if style.get("fontFamily") != "Crimson Text":
        errors.append(f"Style fontFamily: expected 'Crimson Text', got '{style.get('fontFamily')}'.")
    if style.get("fontStyle") != "Bold":
        errors.append(f"Style fontStyle: expected 'Bold', got '{style.get('fontStyle')}'.")

    layer = next((l for l in text_layers if l.get("name") == "Japanese Heading"), None)
    if not layer:
        return False, "Japanese Heading layer not found."

    if layer.get("textStyleId") != style["id"]:
        errors.append(f"Japanese Heading: expected textStyleId '{style['id']}', got '{layer.get('textStyleId')}'.")
    if layer.get("fontFamily") != "Crimson Text":
        errors.append(f"Japanese Heading fontFamily: expected 'Crimson Text', got '{layer.get('fontFamily')}'.")
    if layer.get("fontSize") != 32:
        errors.append(f"Japanese Heading fontSize: expected 32, got {layer.get('fontSize')}.")

    if errors:
        return False, "; ".join(errors)
    return True, "Heading/Display halved to 32px Crimson Text Bold and applied to Japanese Heading."
