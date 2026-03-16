"""
Task: Rename the Body Text layer to 'Introduction' and justify-align it.
Verify: Layer named "Introduction" exists with horizontalAlign='justify'.
"""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    layers = state.get("textLayers", [])
    match = [l for l in layers if l.get("name") == "Introduction"]
    if not match:
        return False, "Layer 'Introduction' not found. The 'Body Text' layer may not have been renamed."
    layer = match[0]

    if layer.get("horizontalAlign") != "justify":
        return False, f"Expected horizontalAlign='justify', got '{layer.get('horizontalAlign')}'."

    return True, "Body Text layer renamed to 'Introduction' and justify-aligned."
