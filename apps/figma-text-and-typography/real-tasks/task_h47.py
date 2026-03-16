import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify: Serif layers → capitalize, monospace layers → lowercase."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    text_layers = state.get("textLayers", [])
    font_families = state.get("fontFamilies", [])
    errors = []

    # Build category lookup
    category_map = {f["name"]: f.get("category", "") for f in font_families}

    for layer in text_layers:
        font = layer.get("fontFamily", "")
        cat = category_map.get(font, "")
        lc = layer.get("letterCase")

        if cat == "serif":
            if lc != "capitalize":
                errors.append(f"'{layer['name']}' uses serif font '{font}': expected letterCase 'capitalize', got '{lc}'.")
        elif cat == "monospace":
            if lc != "lowercase":
                errors.append(f"'{layer['name']}' uses monospace font '{font}': expected letterCase 'lowercase', got '{lc}'.")

    if errors:
        return False, "; ".join(errors)
    return True, "Serif layers set to capitalize and monospace layers set to lowercase."
