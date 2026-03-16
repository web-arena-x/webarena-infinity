import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify: Lock center/right-aligned layers, hide strikethrough layers."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    text_layers = state.get("textLayers", [])
    errors = []

    # These layers should be locked (center or right-aligned in seed):
    # Call to Action (center), Copyright Notice (center), Arabic Welcome (right), Hebrew Body (right)
    should_lock = {"Call to Action", "Copyright Notice", "Arabic Welcome", "Hebrew Body"}

    # These layers should be hidden (strikethrough in seed):
    # Strikethrough Example
    should_hide = {"Strikethrough Example"}

    for layer in text_layers:
        name = layer.get("name")
        if name in should_lock:
            if not layer.get("locked"):
                errors.append(f"'{name}' should be locked (center/right-aligned).")
        if name in should_hide:
            if layer.get("visible") is not False:
                errors.append(f"'{name}' should be hidden (strikethrough decoration).")

    if errors:
        return False, "; ".join(errors)
    return True, "Center/right-aligned layers locked and strikethrough layers hidden."
