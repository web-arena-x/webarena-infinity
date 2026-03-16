import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    layer = next((l for l in state["textLayers"] if l["name"] == "Page Title"), None)
    if not layer:
        return False, "Text layer 'Page Title' not found."

    otf = layer.get("openTypeFeatures", {})
    if otf.get("calt") is not False:
        return False, f"Expected 'calt' to be False, got {otf.get('calt')}."

    return True, "Page Title 'calt' OpenType feature disabled."
