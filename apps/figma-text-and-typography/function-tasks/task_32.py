import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    layer = next((l for l in state["textLayers"] if l["name"] == "Body Text"), None)
    if not layer:
        return False, "Text layer 'Body Text' not found."

    trunc = layer["truncation"]
    if not trunc.get("enabled"):
        return False, "Truncation is not enabled."
    if trunc.get("maxLines") != 5:
        return False, f"Expected maxLines 5, got {trunc.get('maxLines')}."

    return True, "Body Text truncation enabled with 5 max lines."
