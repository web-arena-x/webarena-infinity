"""
Task: Remove all links from the Copyright Notice.
Verify: Layer named 'Copyright Notice' has links == [] (empty array).
"""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    text_layers = state.get("textLayers", [])
    if not text_layers:
        return False, "No text layers found in state."

    copyright_layer = None
    for layer in text_layers:
        if layer.get("name") == "Copyright Notice":
            copyright_layer = layer
            break

    if copyright_layer is None:
        return False, "No layer named 'Copyright Notice' found in textLayers."

    links = copyright_layer.get("links", [])
    if links is None:
        links = []

    if len(links) != 0:
        return False, f"Layer 'Copyright Notice' still has {len(links)} link(s). Expected 0."

    return True, "Layer 'Copyright Notice' has no links."
