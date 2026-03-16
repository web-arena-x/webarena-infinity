"""
Task: Turn off vertical trim on the Release Notes Header.
Verify: Layer named "Release Notes Header" has verticalTrim=False.
"""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    layers = state.get("textLayers", [])
    match = [l for l in layers if l.get("name") == "Release Notes Header"]
    if not match:
        return False, "Layer 'Release Notes Header' not found."
    layer = match[0]

    if layer.get("verticalTrim") is not False:
        return False, f"Expected 'verticalTrim' to be False, got '{layer.get('verticalTrim')}'."

    return True, "Vertical trim is turned off on Release Notes Header."
