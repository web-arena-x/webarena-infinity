"""
Task: Switch the Call to Action to auto-width resizing.
Verify: Layer named "Call to Action" has resizing == 'auto-width'.
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
        if tl.get("name") == "Call to Action":
            layer = tl
            break

    if layer is None:
        return False, "Layer 'Call to Action' not found in textLayers."

    resizing = layer.get("resizing")
    if resizing != "auto-width":
        return False, f"Expected resizing == 'auto-width', got '{resizing}'."

    return True, "Call to Action resizing is correctly set to 'auto-width'."
