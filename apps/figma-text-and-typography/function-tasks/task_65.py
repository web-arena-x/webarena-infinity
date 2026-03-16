import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    layer = next((l for l in state["textLayers"] if l["name"] == "Pricing Tiers"), None)
    if not layer:
        return False, "Text layer 'Pricing Tiers' not found."

    if layer["listStyle"] != "bulleted":
        return False, f"Expected listStyle 'bulleted', got '{layer['listStyle']}'."

    return True, "Pricing Tiers list style changed to bulleted."
