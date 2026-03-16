import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify: Indented Quote has ss01 off, onum and smcp on, paragraph indent 40."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    text_layers = state.get("textLayers", [])
    errors = []

    layer = next((l for l in text_layers if l.get("name") == "Indented Quote"), None)
    if not layer:
        return False, "Indented Quote layer not found."

    features = layer.get("openTypeFeatures", {})
    if features.get("ss01") is not False:
        errors.append(f"ss01: expected False, got {features.get('ss01')}.")
    if features.get("onum") is not True:
        errors.append(f"onum: expected True, got {features.get('onum')}.")
    if features.get("smcp") is not True:
        errors.append(f"smcp: expected True, got {features.get('smcp')}.")
    if layer.get("paragraphIndent") != 40:
        errors.append(f"paragraphIndent: expected 40, got {layer.get('paragraphIndent')}.")

    if errors:
        return False, "; ".join(errors)
    return True, "Indented Quote: ss01 disabled, onum+smcp enabled, paragraph indent set to 40."
