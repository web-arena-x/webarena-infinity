import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify: Every 14px layer has letter spacing 0.02em and line height 22px."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    text_layers = state.get("textLayers", [])
    errors = []

    targets = [l for l in text_layers if l.get("fontSize") == 14]
    if len(targets) < 5:
        return False, f"Expected at least 5 layers at 14px, found {len(targets)}."

    for layer in targets:
        name = layer.get("name", "?")
        ls = layer.get("letterSpacing", {})
        if ls.get("value") != 0.02 or ls.get("unit") != "em":
            errors.append(f"{name}: letterSpacing expected 0.02em, got {ls}.")
        lh = layer.get("lineHeight", {})
        if lh.get("value") != 22 or lh.get("unit") != "px":
            errors.append(f"{name}: lineHeight expected 22px, got {lh}.")

    if errors:
        return False, "; ".join(errors)
    return True, "All 14px layers have letter spacing 0.02em and line height 22px."
