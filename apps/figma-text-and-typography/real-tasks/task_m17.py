"""
Task: Reduce the Section Header font size to 28 and widen its letter spacing to 0.05 em.
Verify: Layer named "Section Header" has fontSize == 28 AND letterSpacing.value approximately 0.05 AND letterSpacing.unit == 'em'.
"""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    text_layers = state.get("textLayers", [])
    layer = None
    for tl in text_layers:
        if tl.get("name") == "Section Header":
            layer = tl
            break

    if layer is None:
        return False, "Layer 'Section Header' not found in textLayers."

    errors = []

    font_size = layer.get("fontSize")
    if font_size != 28:
        errors.append(f"Expected fontSize == 28, got {font_size}.")

    letter_spacing = layer.get("letterSpacing", {})
    ls_value = letter_spacing.get("value")
    ls_unit = letter_spacing.get("unit")

    if ls_value is None:
        errors.append("letterSpacing.value is missing.")
    elif abs(ls_value - 0.05) >= 0.001:
        errors.append(f"Expected letterSpacing.value approximately 0.05, got {ls_value}.")

    if ls_unit != "em":
        errors.append(f"Expected letterSpacing.unit == 'em', got '{ls_unit}'.")

    if errors:
        return False, " ".join(errors)

    return True, "Section Header has fontSize 28 and letterSpacing 0.05 em."
