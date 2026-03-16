import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    layer = next((l for l in state["textLayers"] if l["name"] == "Body Text"), None)
    if not layer:
        return False, "Text layer 'Body Text' not found."

    if layer["textDecoration"] != "underline":
        return False, f"Expected textDecoration 'underline', got '{layer['textDecoration']}'."

    return True, "Body Text text decoration set to underline."
