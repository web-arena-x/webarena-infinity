import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Enable fractions OpenType feature on both Montserrat layers."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    text_layers = state.get("textLayers", [])
    errors = []

    # Montserrat layers: Section Header, Small Caps Header
    montserrat_layers = [l for l in text_layers if l.get("fontFamily") == "Montserrat"]
    if len(montserrat_layers) < 2:
        return False, f"Expected at least 2 Montserrat layers, found {len(montserrat_layers)}."

    for layer in montserrat_layers:
        otf = layer.get("openTypeFeatures", {})
        if otf.get("frac") is not True:
            errors.append(f"{layer.get('name')}: fractions (frac) not enabled")

    if errors:
        return False, "; ".join(errors)
    return True, "Fractions enabled on all Montserrat layers (Section Header, Small Caps Header)."
