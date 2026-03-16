"""
Task: Center-align the Section Header.
Verify: Layer named "Section Header" has horizontalAlign='center'.
"""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    layers = state.get("textLayers", [])
    match = [l for l in layers if l.get("name") == "Section Header"]
    if not match:
        return False, "Layer 'Section Header' not found."
    layer = match[0]

    if layer.get("horizontalAlign") != "center":
        return False, f"Expected 'horizontalAlign' to be 'center', got '{layer.get('horizontalAlign')}'."

    return True, "Section Header is center-aligned."
