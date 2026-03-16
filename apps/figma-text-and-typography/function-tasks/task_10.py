import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    layer = next((l for l in state["textLayers"] if l["name"] == "Page Title"), None)
    if not layer:
        return False, "Text layer 'Page Title' not found."

    lh = layer["lineHeight"]
    if lh.get("value") != 64:
        return False, f"Expected lineHeight value 64, got {lh.get('value')}."
    if lh.get("unit") != "px":
        return False, f"Expected lineHeight unit 'px', got '{lh.get('unit')}'."

    return True, "Page Title line height set to 64 px."
