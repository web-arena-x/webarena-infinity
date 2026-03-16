import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    layer = next((l for l in state["textLayers"] if l["name"] == "Feature List"), None)
    if not layer:
        return False, "Text layer 'Feature List' not found."

    if layer["listStyle"] != "numbered":
        return False, f"Expected listStyle 'numbered', got '{layer['listStyle']}'."

    return True, "Feature List list style changed to numbered."
