"""
Task: Add 12 pixels of paragraph spacing to every layer that uses a list format.
Verify: Layers named "Feature List", "Pricing Tiers", and "Step Instructions"
all have paragraphSpacing=12.
"""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    text_layers = state.get("textLayers", [])

    list_layer_names = ["Feature List", "Pricing Tiers", "Step Instructions"]
    errors = []

    for name in list_layer_names:
        layer = next((l for l in text_layers if l.get("name") == name), None)
        if layer is None:
            errors.append(f"Layer '{name}' not found")
            continue
        spacing = layer.get("paragraphSpacing")
        if spacing != 12:
            errors.append(
                f"Layer '{name}' has paragraphSpacing={spacing}, expected 12"
            )

    if errors:
        return False, "; ".join(errors)

    return True, "All list layers have paragraphSpacing=12."
