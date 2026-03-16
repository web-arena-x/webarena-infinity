"""
Task: Increase the truncation limit on the Truncated Preview to 5 lines.
Verify: Layer named "Truncated Preview" has truncation.enabled=True and truncation.maxLines=5.
"""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    layers = state.get("textLayers", [])
    match = [l for l in layers if l.get("name") == "Truncated Preview"]
    if not match:
        return False, "Layer 'Truncated Preview' not found."
    layer = match[0]

    truncation = layer.get("truncation", {})

    if truncation.get("enabled") is not True:
        return False, f"Expected truncation.enabled=True, got '{truncation.get('enabled')}'."

    max_lines = truncation.get("maxLines")
    if not isinstance(max_lines, (int, float)) or abs(max_lines - 5) > 0.001:
        return False, f"Expected truncation.maxLines=5, got '{max_lines}'."

    return True, "Truncated Preview truncation limit increased to 5 lines."
