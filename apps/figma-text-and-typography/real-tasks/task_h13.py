"""
Task: Rename the Call to Action to 'CTA Button', switch its font to DM Sans Bold,
and change it to auto-height resizing.
Verify: A layer named "CTA Button" exists with fontFamily='DM Sans', fontStyle='Bold',
and resizing='auto-height'. The original "Call to Action" layer should no longer exist.
"""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    text_layers = state.get("textLayers", [])

    errors = []

    # The renamed layer should exist
    cta_layer = next(
        (l for l in text_layers if l.get("name") == "CTA Button"), None
    )
    if cta_layer is None:
        errors.append("Layer 'CTA Button' not found (expected rename from 'Call to Action')")
    else:
        if cta_layer.get("fontFamily") != "DM Sans":
            errors.append(
                f"Layer 'CTA Button' has fontFamily='{cta_layer.get('fontFamily')}', expected 'DM Sans'"
            )
        if cta_layer.get("fontStyle") != "Bold":
            errors.append(
                f"Layer 'CTA Button' has fontStyle='{cta_layer.get('fontStyle')}', expected 'Bold'"
            )
        if cta_layer.get("resizing") != "auto-height":
            errors.append(
                f"Layer 'CTA Button' has resizing='{cta_layer.get('resizing')}', expected 'auto-height'"
            )

    if errors:
        return False, "; ".join(errors)

    return True, "Layer 'CTA Button' exists with DM Sans Bold and auto-height resizing."
