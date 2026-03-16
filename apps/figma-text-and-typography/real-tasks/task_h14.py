"""
Task: Disable contextual alternates on all layers that currently have them enabled.
Verify: No layer has openTypeFeatures.calt == True. The 6 layers that had calt=true
(tl_001, tl_002, tl_004, tl_008, tl_012, tl_013) should all have calt=false or calt absent.
"""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    text_layers = state.get("textLayers", [])

    # IDs of layers that originally had calt=true
    originally_calt_ids = {"tl_001", "tl_002", "tl_004", "tl_008", "tl_012", "tl_013"}

    errors = []

    for layer in text_layers:
        otf = layer.get("openTypeFeatures", {})
        if otf.get("calt") is True:
            errors.append(
                f"Layer '{layer.get('name')}' (id={layer.get('id')}) still has calt=true"
            )

    if errors:
        return False, "; ".join(errors)

    return True, "No layers have contextual alternates (calt) enabled."
