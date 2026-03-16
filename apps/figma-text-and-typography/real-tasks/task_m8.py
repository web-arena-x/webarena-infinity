"""
Task: Apply the Heading/H3 style to the Release Notes Header.
Verify: Layer named "Release Notes Header" has fontFamily='Inter', fontStyle='Semi Bold',
        fontSize=24, and textStyleId matches the id of the style named "Heading/H3".
"""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    # Find the Heading/H3 style
    styles = state.get("textStyles", [])
    style_match = [s for s in styles if s.get("name") == "Heading/H3"]
    if not style_match:
        return False, "Text style 'Heading/H3' not found."
    h3_style = style_match[0]
    h3_style_id = h3_style.get("id")

    # Find the Release Notes Header layer
    layers = state.get("textLayers", [])
    match = [l for l in layers if l.get("name") == "Release Notes Header"]
    if not match:
        return False, "Layer 'Release Notes Header' not found."
    layer = match[0]

    if layer.get("fontFamily") != "Inter":
        return False, f"Expected fontFamily='Inter', got '{layer.get('fontFamily')}'."

    if layer.get("fontStyle") != "Semi Bold":
        return False, f"Expected fontStyle='Semi Bold', got '{layer.get('fontStyle')}'."

    font_size = layer.get("fontSize")
    if not isinstance(font_size, (int, float)) or abs(font_size - 24) > 0.001:
        return False, f"Expected fontSize=24, got '{font_size}'."

    if layer.get("textStyleId") != h3_style_id:
        return False, (
            f"Expected textStyleId='{h3_style_id}' (Heading/H3), "
            f"got '{layer.get('textStyleId')}'."
        )

    return True, "Heading/H3 style applied to Release Notes Header."
