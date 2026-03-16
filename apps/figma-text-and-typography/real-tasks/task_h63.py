import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify: Every layer with a font family starting with 'Noto' is locked."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    text_layers = state.get("textLayers", [])
    errors = []

    noto_layers = [l for l in text_layers if l.get("fontFamily", "").startswith("Noto")]
    if len(noto_layers) < 3:
        return False, f"Expected at least 3 Noto layers, found {len(noto_layers)}."

    for layer in noto_layers:
        if layer.get("locked") is not True:
            errors.append(f"{layer.get('name')}: expected locked=True.")

    if errors:
        return False, "; ".join(errors)
    return True, f"All {len(noto_layers)} Noto layers are locked."
