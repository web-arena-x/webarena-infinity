import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Turn on vertical trim for every layer that has a text style applied."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    text_layers = state.get("textLayers", [])
    errors = []

    # In seed data, layers with textStyleId set:
    # Page Title (ts_001), Body Text (ts_002), Section Header (ts_003),
    # Call to Action (ts_005), Copyright Notice (ts_006),
    # Code Sample (ts_007), Small Caps Header (ts_008)
    styled_layer_ids = {"tl_001", "tl_002", "tl_003", "tl_006", "tl_007", "tl_012", "tl_017"}

    for layer in text_layers:
        if layer.get("id") in styled_layer_ids:
            if layer.get("verticalTrim") is not True:
                errors.append(f"{layer.get('name')}: verticalTrim should be True")

    if errors:
        return False, "; ".join(errors)
    return True, "Vertical trim enabled on all 7 styled layers."
