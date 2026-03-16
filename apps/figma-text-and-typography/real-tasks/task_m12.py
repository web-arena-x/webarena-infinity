"""
Task: Set the Variable Font Demo weight to 700.
Verify: Layer named "Variable Font Demo" has variableAxes.wght == 700.
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
        if tl.get("name") == "Variable Font Demo":
            layer = tl
            break

    if layer is None:
        return False, "Layer 'Variable Font Demo' not found in textLayers."

    variable_axes = layer.get("variableAxes", {})
    wght = variable_axes.get("wght")

    if wght is None:
        return False, f"Layer 'Variable Font Demo' has no 'wght' in variableAxes. Current variableAxes: {variable_axes}"

    if wght != 700:
        return False, f"Expected variableAxes.wght == 700, got {wght}."

    return True, "Variable Font Demo weight is correctly set to 700."
