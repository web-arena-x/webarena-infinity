import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify: Percentage-based line heights changed to 24px."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    text_layers = state.get("textLayers", [])
    errors = []

    # Layers that had %-based line height in seed:
    # Body Text (tl_002): 150% -> 24px
    # Hebrew Body (tl_009): 150% -> 24px
    should_change = {"Body Text", "Hebrew Body"}

    for layer in text_layers:
        name = layer.get("name")
        if name in should_change:
            lh = layer.get("lineHeight", {})
            if lh.get("value") != 24:
                errors.append(f"'{name}': expected lineHeight value 24, got {lh.get('value')}.")
            if lh.get("unit") != "px":
                errors.append(f"'{name}': expected lineHeight unit 'px', got '{lh.get('unit')}'.")

    if errors:
        return False, "; ".join(errors)
    return True, "Percentage-based line heights changed to 24px on Body Text and Hebrew Body."
