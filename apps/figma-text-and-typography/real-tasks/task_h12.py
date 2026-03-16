"""
Task: Reduce the Caption/Small style's font size to 11 pixels.
Verify: Style named "Caption/Small" has fontSize=11 AND layer named "Copyright Notice"
(which uses this style) also has fontSize=11.
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

    # Check the Caption/Small style
    caption_style = next(
        (s for s in text_styles if s.get("name") == "Caption/Small"), None
    )
    if caption_style is None:
        errors.append("Text style 'Caption/Small' not found")
    else:
        if caption_style.get("fontSize") != 11:
            errors.append(
                f"Style 'Caption/Small' has fontSize={caption_style.get('fontSize')}, expected 11"
            )

    # Check the Copyright Notice layer
    layer = next(
        (l for l in text_layers if l.get("name") == "Copyright Notice"), None
    )
    if layer is None:
        errors.append("Layer 'Copyright Notice' not found")
    else:
        if layer.get("fontSize") != 11:
            errors.append(
                f"Layer 'Copyright Notice' has fontSize={layer.get('fontSize')}, expected 11"
            )

    if errors:
        return False, "; ".join(errors)

    return True, "Caption/Small style and Copyright Notice layer both have fontSize=11."
