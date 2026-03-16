import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    match = [l for l in state["textLayers"] if l["name"] == "Strikethrough Example"]
    if match:
        return False, "Text layer 'Strikethrough Example' still exists."

    return True, "Text layer 'Strikethrough Example' deleted."
