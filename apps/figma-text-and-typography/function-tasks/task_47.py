import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    layer = next((l for l in state["textLayers"] if l["name"] == "Indented Quote"), None)
    if not layer:
        return False, "Text layer 'Indented Quote' not found."

    if layer["fontFamily"] != "Georgia":
        return False, f"Expected fontFamily 'Georgia', got '{layer['fontFamily']}'."

    return True, "Indented Quote font changed to Georgia."
