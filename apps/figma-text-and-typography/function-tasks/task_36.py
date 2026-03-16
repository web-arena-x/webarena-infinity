import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    layer = next((l for l in state["textLayers"] if l["name"] == "Variable Font Demo"), None)
    if not layer:
        return False, "Text layer 'Variable Font Demo' not found."

    if layer["verticalTrim"]:
        return False, "Vertical trim is still enabled."

    return True, "Variable Font Demo vertical trim disabled."
