"""
Task: Convert the Step Instructions to a bulleted list.
Verify: Layer named "Step Instructions" has listStyle='bulleted'.
"""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    layers = state.get("textLayers", [])
    match = [l for l in layers if l.get("name") == "Step Instructions"]
    if not match:
        return False, "Layer 'Step Instructions' not found."
    layer = match[0]

    val = layer.get("listStyle")
    if val != "bulleted":
        return False, f"Expected 'listStyle' to be 'bulleted', got '{val}'."

    return True, "Step Instructions is set to a bulleted list."
