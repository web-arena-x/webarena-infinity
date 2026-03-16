import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    layer = next((l for l in state["textLayers"] if l["name"] == "Small Caps Header"), None)
    if not layer:
        return False, "Text layer 'Small Caps Header' not found."

    if layer["letterCase"] != "lowercase":
        return False, f"Expected letterCase 'lowercase', got '{layer['letterCase']}'."

    return True, "Small Caps Header letter case changed to lowercase."
