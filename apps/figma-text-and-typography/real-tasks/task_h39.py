import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Disable vertical trim on layers that have it, and hanging punctuation on layers that have it."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    text_layers = state.get("textLayers", [])
    errors = []

    # In seed data:
    # verticalTrim=true: Variable Font Demo (tl_013), Release Notes Header (tl_019)
    # hangingPunctuation=true: Indented Quote (tl_016)

    vt_layers = {"tl_013": "Variable Font Demo", "tl_019": "Release Notes Header"}
    hp_layers = {"tl_016": "Indented Quote"}

    for layer in text_layers:
        lid = layer.get("id")
        name = layer.get("name", lid)
        if lid in vt_layers:
            if layer.get("verticalTrim") is not False:
                errors.append(f"{name}: verticalTrim should be False")
        if lid in hp_layers:
            if layer.get("hangingPunctuation") is not False:
                errors.append(f"{name}: hangingPunctuation should be False")

    if errors:
        return False, "; ".join(errors)
    return True, "Vertical trim disabled on 2 layers; hanging punctuation disabled on Indented Quote."
