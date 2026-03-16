import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify: Underline decoration added to every layer that has at least one link."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    text_layers = state.get("textLayers", [])
    errors = []

    # Layers with links in seed:
    # Body Text (tl_002): 1 link -> underline
    # Call to Action (tl_006): 1 link -> underline
    # Copyright Notice (tl_007): 2 links -> underline
    # Underlined Link Text (tl_015): 1 link -> underline (already underlined)
    should_underline = {"Body Text", "Call to Action", "Copyright Notice", "Underlined Link Text"}

    for layer in text_layers:
        name = layer.get("name")
        links = layer.get("links", [])
        if name in should_underline or len(links) > 0:
            if layer.get("textDecoration") != "underline":
                errors.append(f"'{name}' has links but textDecoration is '{layer.get('textDecoration')}', expected 'underline'.")

    if errors:
        return False, "; ".join(errors)
    return True, "All layers with links have underline decoration."
