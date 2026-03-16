import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    layer = next((l for l in state["textLayers"] if l["name"] == "Section Header"), None)
    if not layer:
        return False, "Text layer 'Section Header' not found."

    ls = layer["letterSpacing"]
    if ls.get("unit") != "em":
        return False, f"Expected letterSpacing unit 'em', got '{ls.get('unit')}'."
    if abs(ls.get("value", 0) - 0.05) > 0.001:
        return False, f"Expected letterSpacing value 0.05, got {ls.get('value')}."

    return True, "Section Header letter spacing set to 0.05 em."
