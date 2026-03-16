import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Change the letter case of the only layer using Playfair Display to capitalize."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    text_layers = state.get("textLayers", [])

    # Indented Quote is the only layer using Playfair Display
    layer = next((l for l in text_layers if l.get("name") == "Indented Quote"), None)
    if not layer:
        return False, "Indented Quote layer not found."

    if layer.get("fontFamily") != "Playfair Display":
        return False, f"Indented Quote fontFamily changed: expected 'Playfair Display', got '{layer.get('fontFamily')}'"

    if layer.get("letterCase") != "capitalize":
        return False, f"Indented Quote letterCase: expected 'capitalize', got '{layer.get('letterCase')}'"

    return True, "Indented Quote (only Playfair Display layer) letter case set to capitalize."
