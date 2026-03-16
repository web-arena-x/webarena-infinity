"""
Task: Create a text style named 'Heading/H4' with Inter Semi Bold at 20px and 28px
line height, then apply it to the Release Notes Header.
Verify: A style named "Heading/H4" exists with fontFamily='Inter', fontStyle='Semi Bold',
fontSize=20, lineHeight={value:28, unit:'px'}. AND layer named "Release Notes Header"
has textStyleId matching that style's id AND fontFamily='Inter' AND fontStyle='Semi Bold'
AND fontSize=20.
"""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    text_styles = state.get("textStyles", [])
    text_layers = state.get("textLayers", [])

    errors = []

    # Check the Heading/H4 style exists with correct properties
    h4_style = next(
        (s for s in text_styles if s.get("name") == "Heading/H4"), None
    )
    if h4_style is None:
        return False, "Text style 'Heading/H4' not found"

    h4_style_id = h4_style.get("id")

    if h4_style.get("fontFamily") != "Inter":
        errors.append(
            f"Style 'Heading/H4' fontFamily='{h4_style.get('fontFamily')}', expected 'Inter'"
        )
    if h4_style.get("fontStyle") != "Semi Bold":
        errors.append(
            f"Style 'Heading/H4' fontStyle='{h4_style.get('fontStyle')}', expected 'Semi Bold'"
        )
    if h4_style.get("fontSize") != 20:
        errors.append(
            f"Style 'Heading/H4' fontSize={h4_style.get('fontSize')}, expected 20"
        )

    line_height = h4_style.get("lineHeight", {})
    if line_height.get("value") != 28 or line_height.get("unit") != "px":
        errors.append(
            f"Style 'Heading/H4' lineHeight={line_height}, expected {{value:28, unit:'px'}}"
        )

    # Check the Release Notes Header layer
    layer = next(
        (l for l in text_layers if l.get("name") == "Release Notes Header"), None
    )
    if layer is None:
        errors.append("Layer 'Release Notes Header' not found")
    else:
        if layer.get("textStyleId") != h4_style_id:
            errors.append(
                f"Layer textStyleId='{layer.get('textStyleId')}', expected '{h4_style_id}'"
            )
        if layer.get("fontFamily") != "Inter":
            errors.append(
                f"Layer fontFamily='{layer.get('fontFamily')}', expected 'Inter'"
            )
        if layer.get("fontStyle") != "Semi Bold":
            errors.append(
                f"Layer fontStyle='{layer.get('fontStyle')}', expected 'Semi Bold'"
            )
        if layer.get("fontSize") != 20:
            errors.append(
                f"Layer fontSize={layer.get('fontSize')}, expected 20"
            )

    if errors:
        return False, "; ".join(errors)

    return True, "Heading/H4 style created and applied to Release Notes Header correctly."
