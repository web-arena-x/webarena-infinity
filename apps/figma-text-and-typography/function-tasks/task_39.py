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
    if not otf.get("ss01"):
        return False, f"Expected 'ss01' to be True, got {otf.get('ss01')}."

    return True, "Page Title 'ss01' OpenType feature enabled."
