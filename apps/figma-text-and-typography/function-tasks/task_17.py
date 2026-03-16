import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    layer = next((l for l in state["textLayers"] if l["name"] == "Body Text"), None)
    if not layer:
        return False, "Text layer 'Body Text' not found."

    if layer["resizing"] != "fixed":
        return False, f"Expected resizing 'fixed', got '{layer['resizing']}'."
    if layer["width"] != 600:
        return False, f"Expected width 600, got {layer['width']}."
    if layer["height"] != 300:
        return False, f"Expected height 300, got {layer['height']}."

    return True, "Body Text resizing set to fixed with 600x300."
