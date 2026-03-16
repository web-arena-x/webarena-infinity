import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Switch all auto-height layers to fixed resizing with height 200, keeping widths."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    text_layers = state.get("textLayers", [])
    errors = []

    # In seed data, auto-height layers (with their original widths):
    originally_auto_height = {
        "tl_002": 560,   # Body Text
        "tl_004": 400,   # Feature List
        "tl_005": 350,   # Pricing Tiers
        "tl_009": 400,   # Hebrew Body
        "tl_012": 320,   # Code Sample
        "tl_013": 480,   # Variable Font Demo
        "tl_016": 480,   # Indented Quote
        "tl_020": 380,   # Step Instructions
    }

    for layer in text_layers:
        lid = layer.get("id")
        if lid in originally_auto_height:
            name = layer.get("name", lid)
            if layer.get("resizing") != "fixed":
                errors.append(f"{name}: expected resizing='fixed', got '{layer.get('resizing')}'")
            if layer.get("height") != 200:
                errors.append(f"{name}: expected height=200, got {layer.get('height')}")
            expected_w = originally_auto_height[lid]
            if layer.get("width") != expected_w:
                errors.append(f"{name}: expected width={expected_w}, got {layer.get('width')}")

    if errors:
        return False, "; ".join(errors)
    return True, "All 8 auto-height layers switched to fixed with height=200 and original widths preserved."
