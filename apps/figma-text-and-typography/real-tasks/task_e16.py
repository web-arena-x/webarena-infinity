"""
Task: Switch the Arabic Welcome text direction to left-to-right.
Verify: Layer named "Arabic Welcome" has textDirection='ltr'.
"""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    layers = state.get("textLayers", [])
    match = [l for l in layers if l.get("name") == "Arabic Welcome"]
    if not match:
        return False, "Layer 'Arabic Welcome' not found."
    layer = match[0]

    val = layer.get("textDirection")
    if val != "ltr":
        return False, f"Expected 'textDirection' to be 'ltr', got '{val}'."

    return True, "Arabic Welcome text direction is set to left-to-right."
