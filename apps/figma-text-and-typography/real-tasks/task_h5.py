"""
Task: Update the Body/Regular style to use a font size of 18.
Verify: Style named 'Body/Regular' has fontSize=18 AND layer named 'Body Text'
        (which uses this style) also has fontSize=18.
"""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    text_styles = state.get("textStyles", [])
    text_layers = state.get("textLayers", [])

    # Check the style
    body_regular_style = None
    for style in text_styles:
        if style.get("name") == "Body/Regular":
            body_regular_style = style
            break

    if body_regular_style is None:
        return False, "No style named 'Body/Regular' found in textStyles."

    errors = []

    if body_regular_style.get("fontSize") != 18:
        errors.append(f"Style 'Body/Regular' fontSize is {body_regular_style.get('fontSize')}, expected 18")

    # Check the layer
    body_text_layer = None
    for layer in text_layers:
        if layer.get("name") == "Body Text":
            body_text_layer = layer
            break

    if body_text_layer is None:
        errors.append("No layer named 'Body Text' found in textLayers")
    else:
        if body_text_layer.get("fontSize") != 18:
            errors.append(f"Layer 'Body Text' fontSize is {body_text_layer.get('fontSize')}, expected 18")

    if errors:
        return False, "; ".join(errors)

    return True, "Style 'Body/Regular' and layer 'Body Text' both have fontSize=18."
