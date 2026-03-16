import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify: Center-aligned layers -> justify+hangingPunctuation, right-aligned -> left+LTR."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    text_layers = state.get("textLayers", [])
    errors = []

    # In seed data, center-aligned layers: Call to Action (tl_006), Copyright Notice (tl_007)
    # They should now be justify + hangingPunctuation=true
    for name in ["Call to Action", "Copyright Notice"]:
        layer = next((l for l in text_layers if l.get("name") == name), None)
        if not layer:
            errors.append(f"{name} layer not found.")
            continue
        if layer.get("horizontalAlign") != "justify":
            errors.append(f"{name}: expected justify, got '{layer.get('horizontalAlign')}'.")
        if layer.get("hangingPunctuation") is not True:
            errors.append(f"{name}: expected hangingPunctuation=True.")

    # In seed data, right-aligned layers: Arabic Welcome (tl_008), Hebrew Body (tl_009)
    # They should now be left + textDirection=ltr
    for name in ["Arabic Welcome", "Hebrew Body"]:
        layer = next((l for l in text_layers if l.get("name") == name), None)
        if not layer:
            errors.append(f"{name} layer not found.")
            continue
        if layer.get("horizontalAlign") != "left":
            errors.append(f"{name}: expected left, got '{layer.get('horizontalAlign')}'.")
        if layer.get("textDirection") != "ltr":
            errors.append(f"{name}: expected textDirection 'ltr', got '{layer.get('textDirection')}'.")

    if errors:
        return False, "; ".join(errors)
    return True, "Center-aligned -> justify+hangingPunct, right-aligned -> left+LTR."
