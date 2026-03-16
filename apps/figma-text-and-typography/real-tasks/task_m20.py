"""
Task: Change the Small Caps Header to uppercase and increase its size to 16.
Verify: Layer named "Small Caps Header" has letterCase == 'uppercase' AND fontSize == 16.
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
        if tl.get("name") == "Small Caps Header":
            layer = tl
            break

    if layer is None:
        return False, "Layer 'Small Caps Header' not found in textLayers."

    errors = []

    letter_case = layer.get("letterCase")
    if letter_case != "uppercase":
        errors.append(f"Expected letterCase == 'uppercase', got '{letter_case}'.")

    font_size = layer.get("fontSize")
    if font_size != 16:
        errors.append(f"Expected fontSize == 16, got {font_size}.")

    if errors:
        return False, " ".join(errors)

    return True, "Small Caps Header has letterCase 'uppercase' and fontSize 16."
