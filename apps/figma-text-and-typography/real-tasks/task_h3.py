"""
Task: Detach the text style from every layer that has one applied.
Verify: Every layer in textLayers has textStyleId == None (null).
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

    layers_with_style = []
    for layer in text_layers:
        style_id = layer.get("textStyleId")
        if style_id is not None and style_id != "":
            layers_with_style.append(layer)

    if layers_with_style:
        names = [l.get("name", l.get("id", "unknown")) for l in layers_with_style]
        return False, f"Found {len(layers_with_style)} layer(s) still with a text style attached: {', '.join(names)}"

    return True, "All layers have been detached from their text styles."
