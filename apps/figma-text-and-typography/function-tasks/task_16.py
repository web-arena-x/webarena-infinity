import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    layer = next((l for l in state["textLayers"] if l["name"] == "Call to Action"), None)
    if not layer:
        return False, "Text layer 'Call to Action' not found."

    if layer["verticalAlign"] != "bottom":
        return False, f"Expected verticalAlign 'bottom', got '{layer['verticalAlign']}'."

    return True, "Call to Action vertical alignment changed to bottom."
