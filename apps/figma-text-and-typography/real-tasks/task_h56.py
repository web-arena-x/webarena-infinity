import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify: Create 'Table of Contents' layer with numbered list, Open Sans Medium 15px, hanging list."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    text_layers = state.get("textLayers", [])
    errors = []

    layer = next((l for l in text_layers if l.get("content") == "Table of Contents"
                   or l.get("name") == "Table of Contents"), None)
    if not layer:
        return False, "Layer with text 'Table of Contents' not found."

    if layer.get("fontFamily") != "Open Sans":
        errors.append(f"Expected fontFamily 'Open Sans', got '{layer.get('fontFamily')}'.")
    if layer.get("fontStyle") != "Medium":
        errors.append(f"Expected fontStyle 'Medium', got '{layer.get('fontStyle')}'.")
    if layer.get("fontSize") != 15:
        errors.append(f"Expected fontSize 15, got {layer.get('fontSize')}.")

    lh = layer.get("lineHeight", {})
    if lh.get("value") != 22 or lh.get("unit") != "px":
        errors.append(f"Expected lineHeight 22px, got {lh}.")

    if layer.get("listStyle") != "numbered":
        errors.append(f"Expected listStyle 'numbered', got '{layer.get('listStyle')}'.")
    if layer.get("listSpacing") != 8:
        errors.append(f"Expected listSpacing 8, got {layer.get('listSpacing')}.")
    if layer.get("hangingList") is not True:
        errors.append(f"Expected hangingList true, got {layer.get('hangingList')}.")

    if errors:
        return False, "; ".join(errors)
    return True, "Table of Contents layer created with correct properties."
