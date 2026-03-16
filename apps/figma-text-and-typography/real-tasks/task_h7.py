"""
Task: Remove all list formatting from every layer.
Verify: Every layer in textLayers has listStyle='none'.
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

    layers_with_lists = []
    for layer in text_layers:
        list_style = layer.get("listStyle", "none")
        if list_style != "none":
            layers_with_lists.append(
                f"{layer.get('name', layer.get('id', 'unknown'))} (listStyle='{list_style}')"
            )

    if layers_with_lists:
        return False, f"Found {len(layers_with_lists)} layer(s) still with list formatting: {', '.join(layers_with_lists)}"

    return True, "All layers have listStyle='none'. List formatting has been removed."
