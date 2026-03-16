import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify: Layer with hanging punctuation + indent changed to Merriweather Regular, spacing 16."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    text_layers = state.get("textLayers", [])
    errors = []

    # Indented Quote is the only layer with both hanging punctuation and paragraph indent > 0
    layer = next((l for l in text_layers if l.get("name") == "Indented Quote"), None)
    if not layer:
        return False, "Indented Quote layer not found."

    if layer.get("fontFamily") != "Merriweather":
        errors.append(f"fontFamily: expected 'Merriweather', got '{layer.get('fontFamily')}'.")
    if layer.get("fontStyle") != "Regular":
        errors.append(f"fontStyle: expected 'Regular', got '{layer.get('fontStyle')}'.")
    if layer.get("paragraphSpacing") != 16:
        errors.append(f"paragraphSpacing: expected 16, got {layer.get('paragraphSpacing')}.")

    if errors:
        return False, "; ".join(errors)
    return True, "Indented Quote changed to Merriweather Regular with paragraph spacing 16."
