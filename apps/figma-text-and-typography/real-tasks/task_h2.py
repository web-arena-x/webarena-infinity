"""
Task: Hide all the right-to-left text layers.
Verify: All layers with textDirection == 'rtl' have visible == False.
"""
import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    text_layers = state.get("textLayers", [])
    if not text_layers:
        return False, "No text layers found in state."

    rtl_layers = [l for l in text_layers if l.get("textDirection") == "rtl"]
    if not rtl_layers:
        return False, "No RTL layers found in state. Expected at least 2 (Arabic Welcome, Hebrew Body)."

    still_visible = [l for l in rtl_layers if l.get("visible") is not False]
    if still_visible:
        names = [l.get("name", l.get("id", "unknown")) for l in still_visible]
        return False, f"RTL layer(s) still visible: {', '.join(names)}"

    return True, f"All {len(rtl_layers)} RTL layers are hidden."
