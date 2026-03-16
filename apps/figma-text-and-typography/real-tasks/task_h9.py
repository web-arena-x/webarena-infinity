"""
Task: Change the Heading/H2 style to use Playfair Display Bold.
Verify: Style named 'Heading/H2' has fontFamily='Playfair Display', fontStyle='Bold'.
        Layer named 'Section Header' (which uses style ts_003) also has
        fontFamily='Playfair Display', fontStyle='Bold'.
"""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    text_styles = state.get("textStyles", [])
    text_layers = state.get("textLayers", [])

    # Check the style
    h2_style = None
    for style in text_styles:
        if style.get("name") == "Heading/H2":
            h2_style = style
            break

    if h2_style is None:
        return False, "No style named 'Heading/H2' found in textStyles."

    errors = []

    if h2_style.get("fontFamily") != "Playfair Display":
        errors.append(f"Style 'Heading/H2' fontFamily is '{h2_style.get('fontFamily')}', expected 'Playfair Display'")

    if h2_style.get("fontStyle") != "Bold":
        errors.append(f"Style 'Heading/H2' fontStyle is '{h2_style.get('fontStyle')}', expected 'Bold'")

    # Check the layer
    section_header = None
    for layer in text_layers:
        if layer.get("name") == "Section Header":
            section_header = layer
            break

    if section_header is None:
        errors.append("No layer named 'Section Header' found in textLayers")
    else:
        if section_header.get("fontFamily") != "Playfair Display":
            errors.append(f"Layer 'Section Header' fontFamily is '{section_header.get('fontFamily')}', expected 'Playfair Display'")
        if section_header.get("fontStyle") != "Bold":
            errors.append(f"Layer 'Section Header' fontStyle is '{section_header.get('fontStyle')}', expected 'Bold'")

    if errors:
        return False, "; ".join(errors)

    return True, "Style 'Heading/H2' and layer 'Section Header' both use Playfair Display Bold."
