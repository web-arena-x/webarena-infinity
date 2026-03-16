import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    layer = next((l for l in state["textLayers"] if l["name"] == "Step Instructions"), None)
    if not layer:
        return False, "Text layer 'Step Instructions' not found."

    if layer["listSpacing"] != 10:
        return False, f"Expected listSpacing 10, got {layer['listSpacing']}."

    return True, "Step Instructions list spacing set to 10."
