import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify: List-style layers have a link on first 10 chars to figma.com/list and list spacing 10."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    text_layers = state.get("textLayers", [])
    errors = []

    list_layers = [l for l in text_layers if l.get("listStyle") not in (None, "none")]
    if len(list_layers) < 3:
        return False, f"Expected at least 3 list-style layers, found {len(list_layers)}."

    for layer in list_layers:
        name = layer.get("name", "?")

        # Check list spacing
        if layer.get("listSpacing") != 10:
            errors.append(f"{name}: listSpacing expected 10, got {layer.get('listSpacing')}.")

        # Check for link on first 10 chars
        links = layer.get("links", [])
        matching = [lnk for lnk in links
                    if lnk.get("startIndex") == 0
                    and lnk.get("endIndex") == 10
                    and lnk.get("url") == "https://figma.com/list"]
        if not matching:
            errors.append(f"{name}: missing link on chars 0-10 to https://figma.com/list.")

    if errors:
        return False, "; ".join(errors)
    return True, "All list-style layers have link on first 10 chars and list spacing 10."
