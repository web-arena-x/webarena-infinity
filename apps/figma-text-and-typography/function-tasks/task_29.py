import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    layer = next((l for l in state["textLayers"] if l["name"] == "Step Instructions"), None)
    if not layer:
        return False, "Text layer 'Step Instructions' not found."

    if layer["listStyle"] != "bulleted":
        return False, f"Expected listStyle 'bulleted', got '{layer['listStyle']}'."

    return True, "Step Instructions list style changed to bulleted."
