import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    layer = next((l for l in state["textLayers"] if l["name"] == "Call to Action"), None)
    if not layer:
        return False, "Text layer 'Call to Action' not found."

    if layer["height"] != 72:
        return False, f"Expected height 72, got {layer['height']}."

    return True, "Call to Action height changed to 72."
