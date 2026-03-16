import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify: Montserrat disambiguation — smaller to Inter Semi Bold, larger to Playfair Display Bold."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    text_layers = state.get("textLayers", [])
    errors = []

    # Small Caps Header (14px, originally Montserrat) -> Inter Semi Bold
    small_caps = next((l for l in text_layers if l.get("name") == "Small Caps Header"), None)
    if not small_caps:
        return False, "Small Caps Header layer not found."

    if small_caps.get("fontFamily") != "Inter":
        errors.append(f"Small Caps Header: expected fontFamily 'Inter', got '{small_caps.get('fontFamily')}'.")
    if small_caps.get("fontStyle") != "Semi Bold":
        errors.append(f"Small Caps Header: expected fontStyle 'Semi Bold', got '{small_caps.get('fontStyle')}'.")

    # Section Header (32px, originally Montserrat) -> Playfair Display Bold
    section = next((l for l in text_layers if l.get("name") == "Section Header"), None)
    if not section:
        return False, "Section Header layer not found."

    if section.get("fontFamily") != "Playfair Display":
        errors.append(f"Section Header: expected fontFamily 'Playfair Display', got '{section.get('fontFamily')}'.")
    if section.get("fontStyle") != "Bold":
        errors.append(f"Section Header: expected fontStyle 'Bold', got '{section.get('fontStyle')}'.")

    if errors:
        return False, "; ".join(errors)
    return True, "Montserrat layers correctly reassigned: Small Caps→Inter Semi Bold, Section Header→Playfair Display Bold."
