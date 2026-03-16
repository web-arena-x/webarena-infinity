"""
Task: Hide the Copyright Notice text layer.
Verify: Layer named "Copyright Notice" has visible=False.
"""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    layers = state.get("textLayers", [])
    match = [l for l in layers if l.get("name") == "Copyright Notice"]
    if not match:
        return False, "Layer 'Copyright Notice' not found."
    layer = match[0]

    if layer.get("visible") is not False:
        return False, f"Expected 'visible' to be False, got '{layer.get('visible')}'."

    return True, "Copyright Notice layer is hidden."
