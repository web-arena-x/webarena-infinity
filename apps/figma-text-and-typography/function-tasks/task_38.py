import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    layer = next((l for l in state["textLayers"] if l["name"] == "Code Sample"), None)
    if not layer:
        return False, "Text layer 'Code Sample' not found."

    otf = layer.get("openTypeFeatures", {})
    if otf.get("zero") is not False:
        return False, f"Expected 'zero' to be False, got {otf.get('zero')}."

    return True, "Code Sample 'zero' OpenType feature disabled."
