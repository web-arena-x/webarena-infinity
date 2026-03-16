"""
Task: Switch the Pricing Tiers to a bulleted list.
Verify: Layer named "Pricing Tiers" has listStyle='bulleted'.
"""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    layers = state.get("textLayers", [])
    match = [l for l in layers if l.get("name") == "Pricing Tiers"]
    if not match:
        return False, "Layer 'Pricing Tiers' not found."
    layer = match[0]

    if layer.get("listStyle") != "bulleted":
        return False, f"Expected 'listStyle' to be 'bulleted', got '{layer.get('listStyle')}'."

    return True, "Pricing Tiers is now a bulleted list."
