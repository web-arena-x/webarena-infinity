import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    layer = next((l for l in state["textLayers"] if l["name"] == "Truncated Preview"), None)
    if not layer:
        return False, "Text layer 'Truncated Preview' not found."

    trunc = layer["truncation"]
    if trunc.get("enabled"):
        return False, "Truncation is still enabled."

    return True, "Truncated Preview truncation disabled."
