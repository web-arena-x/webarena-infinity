import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify: Larger RTL layer hidden, smaller RTL layer locked."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    text_layers = state.get("textLayers", [])
    errors = []

    # Arabic Welcome (28px, RTL) should be hidden
    arabic = next((l for l in text_layers if l.get("name") == "Arabic Welcome"), None)
    if not arabic:
        return False, "Arabic Welcome layer not found."
    if arabic.get("visible") is not False:
        errors.append("Arabic Welcome (larger RTL): expected visible=False.")

    # Hebrew Body (16px, RTL) should be locked
    hebrew = next((l for l in text_layers if l.get("name") == "Hebrew Body"), None)
    if not hebrew:
        return False, "Hebrew Body layer not found."
    if hebrew.get("locked") is not True:
        errors.append("Hebrew Body (smaller RTL): expected locked=True.")

    if errors:
        return False, "; ".join(errors)
    return True, "Arabic Welcome hidden and Hebrew Body locked."
