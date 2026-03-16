import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify: Layers with custom weight axis below 500 increased to 500."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    text_layers = state.get("textLayers", [])
    errors = []

    # Layers that had explicit wght < 500 in seed:
    # Truncated Preview (tl_011): wght=400 -> 500
    # Code Sample (tl_012): wght=400 -> 500
    # Variable Font Demo (tl_013): wght=450 -> 500
    # Indented Quote (tl_016): wght=400 -> 500
    should_be_500 = {
        "tl_011": "Truncated Preview",
        "tl_012": "Code Sample",
        "tl_013": "Variable Font Demo",
        "tl_016": "Indented Quote",
    }

    for layer in text_layers:
        lid = layer.get("id")
        if lid in should_be_500:
            axes = layer.get("variableAxes", {})
            wght = axes.get("wght")
            if wght != 500:
                errors.append(f"'{should_be_500[lid]}': expected wght=500, got wght={wght}.")

    # Layers that had wght >= 500 should be unchanged
    unchanged = {
        "tl_003": ("Section Header", 600),
        "tl_008": ("Arabic Welcome", 700),
        "tl_017": ("Small Caps Header", 500),
        "tl_019": ("Release Notes Header", 700),
    }
    for lid, (name, expected) in unchanged.items():
        layer = next((l for l in text_layers if l.get("id") == lid), None)
        if layer:
            wght = layer.get("variableAxes", {}).get("wght")
            if wght != expected:
                errors.append(f"'{name}': wght should remain {expected}, got {wght}.")

    if errors:
        return False, "; ".join(errors)
    return True, "All layers with custom weight below 500 increased to 500."
