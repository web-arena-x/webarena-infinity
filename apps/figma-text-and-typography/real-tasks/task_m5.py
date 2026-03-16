"""
Task: Switch the Code Sample font to Fira Code.
Verify: Layer named "Code Sample" has fontFamily='Fira Code'.
"""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    layers = state.get("textLayers", [])
    match = [l for l in layers if l.get("name") == "Code Sample"]
    if not match:
        return False, "Layer 'Code Sample' not found."
    layer = match[0]

    if layer.get("fontFamily") != "Fira Code":
        return False, f"Expected fontFamily='Fira Code', got '{layer.get('fontFamily')}'."

    return True, "Code Sample font switched to Fira Code."
