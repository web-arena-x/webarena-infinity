import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify: Body/Regular style applied to all layers that had fontSize 14."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    text_layers = state.get("textLayers", [])
    text_styles = state.get("textStyles", [])
    errors = []

    body_regular = next((s for s in text_styles if s.get("name") == "Body/Regular"), None)
    if not body_regular:
        return False, "Body/Regular text style not found."

    # Layers that had fontSize 14 in seed:
    # Feature List (tl_004), Pricing Tiers (tl_005), Strikethrough Example (tl_014),
    # Underlined Link Text (tl_015), Small Caps Header (tl_017), Step Instructions (tl_020)
    expected_layers = {
        "tl_004": "Feature List",
        "tl_005": "Pricing Tiers",
        "tl_014": "Strikethrough Example",
        "tl_015": "Underlined Link Text",
        "tl_017": "Small Caps Header",
        "tl_020": "Step Instructions",
    }

    for layer in text_layers:
        lid = layer.get("id")
        if lid in expected_layers:
            name = expected_layers[lid]
            if layer.get("textStyleId") != body_regular["id"]:
                errors.append(f"'{name}': expected textStyleId '{body_regular['id']}', got '{layer.get('textStyleId')}'.")
            if layer.get("fontFamily") != body_regular["fontFamily"]:
                errors.append(f"'{name}': expected fontFamily '{body_regular['fontFamily']}', got '{layer.get('fontFamily')}'.")
            if layer.get("fontSize") != body_regular["fontSize"]:
                errors.append(f"'{name}': expected fontSize {body_regular['fontSize']}, got {layer.get('fontSize')}.")

    if errors:
        return False, "; ".join(errors)
    return True, "Body/Regular applied to all layers that originally had fontSize 14."
