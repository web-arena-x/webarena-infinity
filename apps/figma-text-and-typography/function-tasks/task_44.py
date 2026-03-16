import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    style = next((s for s in state["textStyles"] if s["name"] == "Body/Regular"), None)
    if not style:
        return False, "Text style 'Body/Regular' not found."

    if style["fontSize"] != 18:
        return False, f"Expected fontSize 18, got {style['fontSize']}."

    # Check that layers using this style also updated
    for layer in state["textLayers"]:
        if layer.get("textStyleId") == style["id"]:
            if layer["fontSize"] != 18:
                return False, f"Layer '{layer['name']}' using style has fontSize {layer['fontSize']}, expected 18."

    return True, "Text style 'Body/Regular' fontSize changed to 18 and layers updated."
