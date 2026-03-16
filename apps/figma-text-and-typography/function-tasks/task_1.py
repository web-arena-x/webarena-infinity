import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    match = [l for l in state["textLayers"] if l["content"] == "Hello World"]
    if not match:
        return False, "No text layer with content 'Hello World' found."

    return True, "Text layer with content 'Hello World' created."
