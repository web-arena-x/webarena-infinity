import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    layer = next((l for l in state["textLayers"] if l["name"] == "Code Sample"), None)
    if not layer:
        return False, "Text layer 'Code Sample' not found."

    ls = layer["letterSpacing"]
    if ls.get("unit") != "px":
        return False, f"Expected letterSpacing unit 'px', got '{ls.get('unit')}'."
    if ls.get("value") != 1:
        return False, f"Expected letterSpacing value 1, got {ls.get('value')}."

    return True, "Code Sample letter spacing changed to 1 px."
