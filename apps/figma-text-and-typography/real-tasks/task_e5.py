"""
Task: Remove the strikethrough from the deleted text.
Verify: Layer named "Strikethrough Example" has textDecoration='none'.
"""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    layers = state.get("textLayers", [])
    match = [l for l in layers if l.get("name") == "Strikethrough Example"]
    if not match:
        return False, "Layer 'Strikethrough Example' not found."
    layer = match[0]

    if layer.get("textDecoration") != "none":
        return False, f"Expected 'textDecoration' to be 'none', got '{layer.get('textDecoration')}'."

    return True, "Strikethrough has been removed."
