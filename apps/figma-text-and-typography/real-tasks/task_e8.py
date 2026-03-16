"""
Task: Underline the Page Title.
Verify: Layer named "Page Title" has textDecoration='underline'.
"""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    layers = state.get("textLayers", [])
    match = [l for l in layers if l.get("name") == "Page Title"]
    if not match:
        return False, "Layer 'Page Title' not found."
    layer = match[0]

    if layer.get("textDecoration") != "underline":
        return False, f"Expected 'textDecoration' to be 'underline', got '{layer.get('textDecoration')}'."

    return True, "Page Title is underlined."
