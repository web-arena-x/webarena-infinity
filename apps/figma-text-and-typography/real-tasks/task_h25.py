import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Add paragraph indent of 24 to every layer with paragraph spacing > 0."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    text_layers = state.get("textLayers", [])
    errors = []

    # In seed data, layers with paragraphSpacing > 0:
    # Body Text (16), Hebrew Body (12), Indented Quote (8)
    expected_layers = {"Body Text", "Hebrew Body", "Indented Quote"}

    for layer in text_layers:
        name = layer.get("name")
        if name in expected_layers:
            if layer.get("paragraphIndent") != 24:
                errors.append(f"{name}: expected paragraphIndent=24, got {layer.get('paragraphIndent')}")

    if errors:
        return False, "; ".join(errors)
    return True, "Paragraph indent set to 24 on all layers with paragraph spacing > 0."
