"""
Task: Disable truncation on the Truncated Preview.
Verify: Layer named "Truncated Preview" has truncation.enabled=False.
"""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    layers = state.get("textLayers", [])
    match = [l for l in layers if l.get("name") == "Truncated Preview"]
    if not match:
        return False, "Layer 'Truncated Preview' not found."
    layer = match[0]

    truncation = layer.get("truncation", {})
    if not isinstance(truncation, dict):
        return False, f"Expected 'truncation' to be a dict, got '{type(truncation).__name__}'."

    val = truncation.get("enabled")
    if val is not False:
        return False, f"Expected 'truncation.enabled' to be False, got '{val}'."

    return True, "Truncation is disabled on Truncated Preview."
