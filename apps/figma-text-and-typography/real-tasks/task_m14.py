"""
Task: Enable truncation on the Body Text and limit it to 4 lines.
Verify: Layer named "Body Text" has truncation.enabled == True AND truncation.maxLines == 4.
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
        if tl.get("name") == "Body Text":
            layer = tl
            break

    if layer is None:
        return False, "Layer 'Body Text' not found in textLayers."

    truncation = layer.get("truncation", {})
    enabled = truncation.get("enabled")
    max_lines = truncation.get("maxLines")

    errors = []
    if enabled is not True:
        errors.append(f"Expected truncation.enabled == True, got {enabled}.")
    if max_lines != 4:
        errors.append(f"Expected truncation.maxLines == 4, got {max_lines}.")

    if errors:
        return False, " ".join(errors)

    return True, "Body Text truncation is enabled with maxLines set to 4."
