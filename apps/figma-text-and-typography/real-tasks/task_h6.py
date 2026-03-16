"""
Task: Lock all layers that have links in them.
Verify: All layers with a non-empty links array have locked=True.
        Expected layers: Body Text, Call to Action, Copyright Notice, Underlined Link Text.
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

    layers_with_links = [l for l in text_layers if l.get("links") and len(l.get("links", [])) > 0]

    if not layers_with_links:
        return False, "No layers with links found in state. Expected at least 4."

    not_locked = []
    for layer in layers_with_links:
        if layer.get("locked") is not True:
            not_locked.append(layer.get("name", layer.get("id", "unknown")))

    if not_locked:
        return False, f"Layer(s) with links not locked: {', '.join(not_locked)}"

    locked_names = [l.get("name", l.get("id", "unknown")) for l in layers_with_links]
    return True, f"All {len(layers_with_links)} layers with links are locked: {', '.join(locked_names)}."
