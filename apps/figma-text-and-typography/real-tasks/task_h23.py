import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Lock the text layer that contains the most hyperlinks."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    text_layers = state.get("textLayers", [])

    # Copyright Notice has 2 links (the most of any layer in seed data)
    target = next((l for l in text_layers if l.get("name") == "Copyright Notice"), None)
    if not target:
        return False, "Copyright Notice layer not found."

    if target.get("locked") is not True:
        return False, f"Copyright Notice should be locked (has most links), but locked={target.get('locked')}"

    return True, "Copyright Notice (layer with most links) is correctly locked."
