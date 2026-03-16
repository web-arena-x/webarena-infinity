import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    layer = next((l for l in state["textLayers"] if l["name"] == "Variable Font Demo"), None)
    if not layer:
        return False, "Text layer 'Variable Font Demo' not found."

    axes = layer.get("variableAxes", {})
    if axes.get("wght") != 700:
        return False, f"Expected wght 700, got {axes.get('wght')}."

    return True, "Variable Font Demo wght axis set to 700."
