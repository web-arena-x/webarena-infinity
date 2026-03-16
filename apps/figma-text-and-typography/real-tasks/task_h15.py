"""
Task: Apply the Label/Overline style to the Small Caps Header.
Verify: Layer named "Small Caps Header" has textStyleId matching the id of style
named "Label/Overline", fontFamily='Inter', fontStyle='Semi Bold', fontSize=11,
and letterCase='uppercase'.
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

    # Find the Label/Overline style
    overline_style = next(
        (s for s in text_styles if s.get("name") == "Label/Overline"), None
    )
    if overline_style is None:
        return False, "Text style 'Label/Overline' not found"

    overline_style_id = overline_style.get("id")

    # Find the Small Caps Header layer
    layer = next(
        (l for l in text_layers if l.get("name") == "Small Caps Header"), None
    )
    if layer is None:
        return False, "Layer 'Small Caps Header' not found"

    if layer.get("textStyleId") != overline_style_id:
        errors.append(
            f"textStyleId='{layer.get('textStyleId')}', expected '{overline_style_id}'"
        )
    if layer.get("fontFamily") != "Inter":
        errors.append(
            f"fontFamily='{layer.get('fontFamily')}', expected 'Inter'"
        )
    if layer.get("fontStyle") != "Semi Bold":
        errors.append(
            f"fontStyle='{layer.get('fontStyle')}', expected 'Semi Bold'"
        )
    if layer.get("fontSize") != 11:
        errors.append(
            f"fontSize={layer.get('fontSize')}, expected 11"
        )
    if layer.get("letterCase") != "uppercase":
        errors.append(
            f"letterCase='{layer.get('letterCase')}', expected 'uppercase'"
        )

    if errors:
        return False, "Small Caps Header: " + "; ".join(errors)

    return True, "Small Caps Header has Label/Overline style applied correctly."
