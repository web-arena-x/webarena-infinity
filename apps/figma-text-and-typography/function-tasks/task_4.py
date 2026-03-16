import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    match = [l for l in state["textLayers"] if l["name"] == "Main Body Copy"]
    if not match:
        return False, "Text layer 'Main Body Copy' not found."

    return True, "Text layer renamed to 'Main Body Copy'."
