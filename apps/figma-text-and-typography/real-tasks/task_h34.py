import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Swap center-aligned and right-aligned layers."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    text_layers = state.get("textLayers", [])
    errors = []

    # In seed data:
    # Center-aligned: Call to Action (tl_006), Copyright Notice (tl_007) → should become right
    # Right-aligned: Arabic Welcome (tl_008), Hebrew Body (tl_009) → should become center
    expected = {
        "tl_006": ("Call to Action", "right"),
        "tl_007": ("Copyright Notice", "right"),
        "tl_008": ("Arabic Welcome", "center"),
        "tl_009": ("Hebrew Body", "center"),
    }

    for layer in text_layers:
        lid = layer.get("id")
        if lid in expected:
            name, expected_align = expected[lid]
            actual = layer.get("horizontalAlign")
            if actual != expected_align:
                errors.append(f"{name}: expected '{expected_align}', got '{actual}'")

    if errors:
        return False, "; ".join(errors)
    return True, "Center↔right alignment swap completed correctly on all 4 layers."
