import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    layer = next((l for l in state["textLayers"] if l["name"] == "Page Title"), None)
    if not layer:
        return False, "Text layer 'Page Title' not found."

    if layer.get("textStyleId") is not None:
        return False, f"Expected textStyleId to be null, got '{layer.get('textStyleId')}'."

    return True, "Page Title text style detached."
