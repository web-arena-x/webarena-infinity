"""
Task: Enable Stylistic Set 1 on the Page Title.
Verify: Layer named "Page Title" has openTypeFeatures.ss01 == True.
"""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    text_layers = state.get("textLayers", [])
    layer = None
    for tl in text_layers:
        if tl.get("name") == "Page Title":
            layer = tl
            break

    if layer is None:
        return False, "Layer 'Page Title' not found in textLayers."

    open_type_features = layer.get("openTypeFeatures", {})
    ss01 = open_type_features.get("ss01")

    if ss01 is not True:
        return False, f"Expected openTypeFeatures.ss01 == True, got {ss01}. Current openTypeFeatures: {open_type_features}"

    return True, "Stylistic Set 1 (ss01) is enabled on Page Title."
