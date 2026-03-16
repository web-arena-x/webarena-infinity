import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify: Enable oldstyle figures and lining figures on the layer quoting Spiekermann."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    text_layers = state.get("textLayers", [])
    errors = []

    # The layer quoting Spiekermann is Indented Quote (tl_016)
    layer = next((l for l in text_layers if l.get("name") == "Indented Quote"), None)
    if not layer:
        return False, "Indented Quote layer not found."

    features = layer.get("openTypeFeatures", {})

    if features.get("onum") is not True:
        errors.append(f"Expected onum=true, got {features.get('onum')}.")

    if features.get("lnum") is not True:
        errors.append(f"Expected lnum=true, got {features.get('lnum')}.")

    if errors:
        return False, "; ".join(errors)
    return True, "Oldstyle figures and lining figures enabled on Indented Quote (Spiekermann layer)."
