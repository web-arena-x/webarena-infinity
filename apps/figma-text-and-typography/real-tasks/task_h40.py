import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Rename the DM Sans layer to 'New Features' and change its font to Open Sans Bold."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    text_layers = state.get("textLayers", [])
    errors = []

    # Release Notes Header (tl_019) is the only layer using DM Sans in seed data
    layer = next((l for l in text_layers if l.get("id") == "tl_019"), None)
    if not layer:
        return False, "Layer tl_019 (originally Release Notes Header) not found."

    if layer.get("name") != "New Features":
        errors.append(f"name: expected 'New Features', got '{layer.get('name')}'")
    if layer.get("fontFamily") != "Open Sans":
        errors.append(f"fontFamily: expected 'Open Sans', got '{layer.get('fontFamily')}'")
    if layer.get("fontStyle") != "Bold":
        errors.append(f"fontStyle: expected 'Bold', got '{layer.get('fontStyle')}'")

    if errors:
        return False, "; ".join(errors)
    return True, "DM Sans layer renamed to 'New Features' with font changed to Open Sans Bold."
