"""
Task: On the Code Sample layer, turn off all OpenType features except standard
ligatures and kerning.
Verify: Layer named "Code Sample" has openTypeFeatures where liga=True, kern=True,
and calt is False (or absent), zero is False (or absent). Any other features should
be False or absent.
"""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    text_layers = state.get("textLayers", [])

    layer = next(
        (l for l in text_layers if l.get("name") == "Code Sample"), None
    )
    if layer is None:
        return False, "Layer 'Code Sample' not found"

    otf = layer.get("openTypeFeatures", {})
    errors = []

    # liga must be True
    if otf.get("liga") is not True:
        errors.append(f"liga={otf.get('liga')}, expected True")

    # kern must be True
    if otf.get("kern") is not True:
        errors.append(f"kern={otf.get('kern')}, expected True")

    # All other features must be False or absent
    allowed_true = {"liga", "kern"}
    for key, value in otf.items():
        if key not in allowed_true and value is True:
            errors.append(f"{key}=True, expected False or absent")

    if errors:
        return False, "Code Sample openTypeFeatures: " + "; ".join(errors)

    return True, "Code Sample has only liga and kern enabled in openTypeFeatures."
