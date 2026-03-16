import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Enable oldstyle figures on every text layer using Inter."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    text_layers = state.get("textLayers", [])
    errors = []

    # In seed data, 10 layers use Inter:
    inter_layer_ids = {
        "tl_001", "tl_002", "tl_004", "tl_005", "tl_007",
        "tl_013", "tl_014", "tl_015", "tl_018", "tl_020"
    }

    inter_layers = [l for l in text_layers if l.get("id") in inter_layer_ids]
    if len(inter_layers) < 10:
        errors.append(f"Expected 10 Inter layers, found {len(inter_layers)}")

    for layer in inter_layers:
        otf = layer.get("openTypeFeatures", {})
        if otf.get("onum") is not True:
            errors.append(f"{layer.get('name')}: onum not enabled")

    if errors:
        return False, "; ".join(errors)
    return True, "Oldstyle figures (onum) enabled on all 10 Inter layers."
