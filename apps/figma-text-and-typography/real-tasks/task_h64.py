import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify: All font sizes clamped to range 14-32."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    text_layers = state.get("textLayers", [])
    errors = []

    for layer in text_layers:
        name = layer.get("name", "?")
        size = layer.get("fontSize")
        if size is None:
            continue
        if size < 14:
            errors.append(f"{name}: fontSize {size} is below 14.")
        if size > 32:
            errors.append(f"{name}: fontSize {size} is above 32.")

    # Verify specific layers were changed
    for layer in text_layers:
        name = layer.get("name", "?")
        if name == "Copyright Notice" and layer.get("fontSize") != 14:
            errors.append(f"Copyright Notice: expected 14, got {layer.get('fontSize')}.")
        if name == "Code Sample" and layer.get("fontSize") != 14:
            errors.append(f"Code Sample: expected 14, got {layer.get('fontSize')}.")
        if name == "Page Title" and layer.get("fontSize") != 32:
            errors.append(f"Page Title: expected 32, got {layer.get('fontSize')}.")
        if name == "Release Notes Header" and layer.get("fontSize") != 32:
            errors.append(f"Release Notes Header: expected 32, got {layer.get('fontSize')}.")

    if errors:
        return False, "; ".join(errors)
    return True, "All font sizes clamped to 14-32 range."
