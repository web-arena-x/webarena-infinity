import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    layer = next((l for l in state["textLayers"] if l["name"] == "Page Title"), None)
    if not layer:
        return False, "Text layer 'Page Title' not found."

    if layer["letterCase"] != "uppercase":
        return False, f"Expected letterCase 'uppercase', got '{layer['letterCase']}'."

    return True, "Page Title letter case changed to uppercase."
