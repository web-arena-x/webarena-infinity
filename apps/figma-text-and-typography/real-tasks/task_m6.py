"""
Task: Set the Body Text paragraph spacing to 24 and indent to 20.
Verify: Layer named "Body Text" has paragraphSpacing=24 and paragraphIndent=20.
"""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    layers = state.get("textLayers", [])
    match = [l for l in layers if l.get("name") == "Body Text"]
    if not match:
        return False, "Layer 'Body Text' not found."
    layer = match[0]

    para_spacing = layer.get("paragraphSpacing")
    if not isinstance(para_spacing, (int, float)) or abs(para_spacing - 24) > 0.001:
        return False, f"Expected paragraphSpacing=24, got '{para_spacing}'."

    para_indent = layer.get("paragraphIndent")
    if not isinstance(para_indent, (int, float)) or abs(para_indent - 20) > 0.001:
        return False, f"Expected paragraphIndent=20, got '{para_indent}'."

    return True, "Body Text paragraph spacing set to 24 and indent set to 20."
