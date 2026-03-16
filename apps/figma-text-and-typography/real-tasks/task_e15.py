"""
Task: Detach the style from the Section Header.
Verify: Layer named "Section Header" has textStyleId as None/null.
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

    val = layer.get("textStyleId")
    if val is not None:
        return False, f"Expected 'textStyleId' to be None, got '{val}'."

    return True, "Style has been detached from Section Header."
