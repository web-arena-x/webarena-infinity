"""
Task: Add a link covering the full Japanese Heading text pointing to https://figma.com/japan.
Verify: Layer named "Japanese Heading" has at least one link with url == 'https://figma.com/japan'.
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
        if tl.get("name") == "Japanese Heading":
            layer = tl
            break

    if layer is None:
        return False, "Layer 'Japanese Heading' not found in textLayers."

    links = layer.get("links", [])
    if not links:
        return False, "Layer 'Japanese Heading' has no links."

    for link in links:
        if link.get("url") == "https://figma.com/japan":
            return True, "Japanese Heading has a link pointing to 'https://figma.com/japan'."

    urls_found = [link.get("url") for link in links]
    return False, f"No link with url 'https://figma.com/japan' found. Links found: {urls_found}"
