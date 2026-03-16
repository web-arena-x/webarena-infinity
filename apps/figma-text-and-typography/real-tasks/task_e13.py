"""
Task: Delete the Strikethrough Example layer.
Verify: No layer named "Strikethrough Example" exists.
"""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    layers = state.get("textLayers", [])
    match = [l for l in layers if l.get("name") == "Strikethrough Example"]
    if match:
        return False, "Layer 'Strikethrough Example' still exists."

    return True, "Strikethrough Example layer has been deleted."
