import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Remove all links from every text layer using auto-width resizing."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    text_layers = state.get("textLayers", [])
    errors = []

    # In seed data, auto-width layers that have links:
    # Copyright Notice (tl_007): 2 links, auto-width
    # Underlined Link Text (tl_015): 1 link, auto-width
    expected_cleared = {"tl_007", "tl_015"}

    for layer in text_layers:
        lid = layer.get("id")
        if lid in expected_cleared:
            links = layer.get("links", [])
            if len(links) != 0:
                errors.append(f"{layer.get('name')}: expected 0 links, still has {len(links)}")

    if errors:
        return False, "; ".join(errors)
    return True, "All links removed from auto-width layers (Copyright Notice, Underlined Link Text)."
