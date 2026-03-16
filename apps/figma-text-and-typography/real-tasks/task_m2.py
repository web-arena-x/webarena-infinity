"""
Task: Switch the Page Title font to Montserrat Bold.
Verify: Layer named "Page Title" has fontFamily='Montserrat' and fontStyle='Bold'.
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

    if layer.get("fontFamily") != "Montserrat":
        return False, f"Expected fontFamily='Montserrat', got '{layer.get('fontFamily')}'."

    if layer.get("fontStyle") != "Bold":
        return False, f"Expected fontStyle='Bold', got '{layer.get('fontStyle')}'."

    return True, "Page Title font switched to Montserrat Bold."
