import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    layer = next((l for l in state["textLayers"] if l["name"] == "Copyright Notice"), None)
    if not layer:
        return False, "Text layer 'Copyright Notice' not found."

    if layer["visible"]:
        return False, "Text layer 'Copyright Notice' is still visible."

    return True, "Text layer 'Copyright Notice' is hidden."
