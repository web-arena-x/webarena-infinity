import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    layer = next((l for l in state["textLayers"] if l["name"] == "Arabic Welcome"), None)
    if not layer:
        return False, "Text layer 'Arabic Welcome' not found."

    if layer["textDirection"] != "ltr":
        return False, f"Expected textDirection 'ltr', got '{layer['textDirection']}'."

    return True, "Arabic Welcome text direction changed to LTR."
