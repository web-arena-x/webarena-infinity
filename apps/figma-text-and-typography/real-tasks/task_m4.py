"""
Task: Create a new text layer with the text 'Terms and Conditions'.
Verify: Any layer has content='Terms and Conditions'.
"""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    layers = state.get("textLayers", [])
    match = [l for l in layers if l.get("content") == "Terms and Conditions"]
    if not match:
        return False, "No layer found with content 'Terms and Conditions'."

    return True, "Layer with content 'Terms and Conditions' found."
