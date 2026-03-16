import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    layer = next((l for l in state["textLayers"] if l["name"] == "Page Title"), None)
    if not layer:
        return False, "Text layer 'Page Title' not found."

    if layer["fontStyle"] != "Extra Bold":
        return False, f"Expected fontStyle 'Extra Bold', got '{layer['fontStyle']}'."

    return True, "Page Title font style changed to Extra Bold."
