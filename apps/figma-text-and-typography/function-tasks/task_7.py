import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    layer = next((l for l in state["textLayers"] if l["name"] == "Section Header"), None)
    if not layer:
        return False, "Text layer 'Section Header' not found."

    if layer["fontFamily"] != "Roboto":
        return False, f"Expected fontFamily 'Roboto', got '{layer['fontFamily']}'."

    return True, "Section Header font changed to Roboto."
