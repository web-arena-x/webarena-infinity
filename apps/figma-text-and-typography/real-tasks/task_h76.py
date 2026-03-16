import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify: 'Learn More' layer with Crimson Text Semi Bold 16px, underline, center, full link."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    text_layers = state.get("textLayers", [])
    errors = []

    layer = next((l for l in text_layers if l.get("name") == "Learn More"), None)
    if not layer:
        return False, "Learn More layer not found."

    if "Learn More" not in layer.get("content", ""):
        errors.append(f"Content should contain 'Learn More', got '{layer.get('content')}'.")
    if layer.get("fontFamily") != "Crimson Text":
        errors.append(f"fontFamily: expected 'Crimson Text', got '{layer.get('fontFamily')}'.")
    if layer.get("fontStyle") != "Semi Bold":
        errors.append(f"fontStyle: expected 'Semi Bold', got '{layer.get('fontStyle')}'.")
    if layer.get("fontSize") != 16:
        errors.append(f"fontSize: expected 16, got {layer.get('fontSize')}.")
    if layer.get("textDecoration") != "underline":
        errors.append(f"textDecoration: expected 'underline', got '{layer.get('textDecoration')}'.")
    if layer.get("horizontalAlign") != "center":
        errors.append(f"horizontalAlign: expected 'center', got '{layer.get('horizontalAlign')}'.")

    # Check link
    links = layer.get("links", [])
    content_len = len(layer.get("content", ""))
    matching = [lnk for lnk in links
                if lnk.get("startIndex") == 0
                and lnk.get("endIndex") == content_len
                and lnk.get("url") == "https://figma.com/learn"]
    if not matching:
        errors.append("Missing full-text link to https://figma.com/learn.")

    if errors:
        return False, "; ".join(errors)
    return True, "Learn More layer created with correct properties and link."
