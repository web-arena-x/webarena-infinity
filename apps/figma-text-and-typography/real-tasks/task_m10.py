"""
Task: Switch the Indented Quote font to Georgia and turn off its hanging punctuation.
Verify: Layer named "Indented Quote" has fontFamily='Georgia' and hangingPunctuation=False.
"""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    layers = state.get("textLayers", [])
    match = [l for l in layers if l.get("name") == "Indented Quote"]
    if not match:
        return False, "Layer 'Indented Quote' not found."
    layer = match[0]

    if layer.get("fontFamily") != "Georgia":
        return False, f"Expected fontFamily='Georgia', got '{layer.get('fontFamily')}'."

    if layer.get("hangingPunctuation") is not False:
        return False, f"Expected hangingPunctuation=False, got '{layer.get('hangingPunctuation')}'."

    return True, "Indented Quote font switched to Georgia with hanging punctuation off."
