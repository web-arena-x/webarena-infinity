import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify: Variable Font Demo weight set to max (900) and slant set to min (-10)."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    text_layers = state.get("textLayers", [])
    errors = []

    layer = next((l for l in text_layers if l.get("name") == "Variable Font Demo"), None)
    if not layer:
        return False, "Variable Font Demo layer not found."

    axes = layer.get("variableAxes", {})

    # Inter weight axis: min=100, max=900
    wght = axes.get("wght")
    if wght != 900:
        errors.append(f"Expected wght=900 (max), got wght={wght}.")

    # Inter slant axis: min=-10, max=0
    slnt = axes.get("slnt")
    if slnt != -10:
        errors.append(f"Expected slnt=-10 (min), got slnt={slnt}.")

    if errors:
        return False, "; ".join(errors)
    return True, "Variable Font Demo weight set to 900 (max) and slant set to -10 (min)."
