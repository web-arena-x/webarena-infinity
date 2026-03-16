"""
Task: Remove the uppercase formatting from the Call to Action button text.
Verify: Layer named "Call to Action" has letterCase='none'.
"""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    layers = state.get("textLayers", [])
    match = [l for l in layers if l.get("name") == "Call to Action"]
    if not match:
        return False, "Layer 'Call to Action' not found."
    layer = match[0]

    if layer.get("letterCase") != "none":
        return False, f"Expected 'letterCase' to be 'none', got '{layer.get('letterCase')}'."

    return True, "Uppercase formatting removed from Call to Action."
