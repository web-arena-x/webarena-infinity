import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    layer = next((l for l in state["textLayers"] if l["name"] == "Feature List"), None)
    if not layer:
        return False, "Text layer 'Feature List' not found."

    style = next((s for s in state["textStyles"] if s["name"] == "Body/Small"), None)
    if not style:
        return False, "Text style 'Body/Small' not found."

    if layer.get("textStyleId") != style["id"]:
        return False, f"Expected textStyleId '{style['id']}', got '{layer.get('textStyleId')}'."

    if layer["fontFamily"] != style["fontFamily"]:
        return False, f"Expected fontFamily '{style['fontFamily']}', got '{layer['fontFamily']}'."
    if layer["fontSize"] != style["fontSize"]:
        return False, f"Expected fontSize {style['fontSize']}, got {layer['fontSize']}."

    return True, "Feature List has 'Body/Small' text style applied."
