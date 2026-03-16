"""
Task: Make the Feature List numbered and increase its list spacing to 8.
Verify: Layer named "Feature List" has listStyle='numbered' and listSpacing=8.
"""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    layers = state.get("textLayers", [])
    match = [l for l in layers if l.get("name") == "Feature List"]
    if not match:
        return False, "Layer 'Feature List' not found."
    layer = match[0]

    if layer.get("listStyle") != "numbered":
        return False, f"Expected listStyle='numbered', got '{layer.get('listStyle')}'."

    list_spacing = layer.get("listSpacing")
    if not isinstance(list_spacing, (int, float)) or abs(list_spacing - 8) > 0.001:
        return False, f"Expected listSpacing=8, got '{list_spacing}'."

    return True, "Feature List set to numbered with list spacing 8."
