import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    layer = next((l for l in state["textLayers"] if l["name"] == "Body Text"), None)
    if not layer:
        return False, "Text layer 'Body Text' not found."

    lh = layer["lineHeight"]
    if lh.get("unit") != "px":
        return False, f"Expected lineHeight unit 'px', got '{lh.get('unit')}'."
    if lh.get("value") != 24:
        return False, f"Expected lineHeight value 24, got {lh.get('value')}."

    return True, "Body Text line height changed to 24 px."
