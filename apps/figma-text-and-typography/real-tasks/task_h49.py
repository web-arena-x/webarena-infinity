import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify: Styled layers — left-aligned→center, center-aligned→right."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    text_layers = state.get("textLayers", [])
    errors = []

    # Seed state styled layers that were left-aligned -> should now be center:
    # Page Title (ts_001), Body Text (ts_002), Section Header (ts_003),
    # Code Sample (ts_007), Small Caps Header (ts_008)
    should_be_center = {"Page Title", "Body Text", "Section Header", "Code Sample", "Small Caps Header"}

    # Seed state styled layers that were center-aligned -> should now be right:
    # Call to Action (ts_005), Copyright Notice (ts_006)
    should_be_right = {"Call to Action", "Copyright Notice"}

    for layer in text_layers:
        name = layer.get("name")
        align = layer.get("horizontalAlign")

        if name in should_be_center:
            if align != "center":
                errors.append(f"'{name}' (styled, was left): expected 'center', got '{align}'.")

        if name in should_be_right:
            if align != "right":
                errors.append(f"'{name}' (styled, was center): expected 'right', got '{align}'.")

    if errors:
        return False, "; ".join(errors)
    return True, "Styled layers alignment shifted: left→center, center→right."
