import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    layer = next((l for l in state["textLayers"] if l["name"] == "Strikethrough Example"), None)
    if not layer:
        return False, "Text layer 'Strikethrough Example' not found."

    if layer["textDecoration"] != "none":
        return False, f"Expected textDecoration 'none', got '{layer['textDecoration']}'."

    return True, "Strikethrough Example decoration removed."
