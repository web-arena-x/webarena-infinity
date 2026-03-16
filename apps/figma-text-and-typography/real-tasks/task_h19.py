"""
Task: Change all auto-width layers to auto-height with a width of 400.
Verify: No layer has resizing='auto-width'. All 10 previously auto-width layers
should have resizing='auto-height' and width=400.
"""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    text_layers = state.get("textLayers", [])

    errors = []

    # IDs of the 10 layers that were originally auto-width
    originally_auto_width_ids = {
        "tl_001", "tl_003", "tl_007", "tl_008", "tl_010",
        "tl_014", "tl_015", "tl_017", "tl_018", "tl_019",
    }

    # Check no layer has auto-width
    auto_width_layers = [
        l for l in text_layers if l.get("resizing") == "auto-width"
    ]
    if auto_width_layers:
        names = [l.get("name", l.get("id")) for l in auto_width_layers]
        errors.append(
            f"Layers still using auto-width: {', '.join(names)}"
        )

    # Check each previously auto-width layer is now auto-height with width=400
    for layer in text_layers:
        if layer.get("id") in originally_auto_width_ids:
            layer_name = layer.get("name", layer.get("id"))
            if layer.get("resizing") != "auto-height":
                errors.append(
                    f"Layer '{layer_name}' has resizing='{layer.get('resizing')}', expected 'auto-height'"
                )
            if layer.get("width") != 400:
                errors.append(
                    f"Layer '{layer_name}' has width={layer.get('width')}, expected 400"
                )

    if errors:
        return False, "; ".join(errors)

    return True, "All previously auto-width layers are now auto-height with width=400."
