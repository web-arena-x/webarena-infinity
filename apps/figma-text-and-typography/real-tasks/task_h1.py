"""
Task: Switch all text layers currently using Inter to Roboto.
Verify: No layer in textLayers has fontFamily == 'Inter'. All 10 Inter layers should now be Roboto.
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

    inter_layers = [l for l in text_layers if l.get("fontFamily") == "Inter"]
    if inter_layers:
        names = [l.get("name", l.get("id", "unknown")) for l in inter_layers]
        return False, f"Found {len(inter_layers)} layer(s) still using Inter: {', '.join(names)}"

    roboto_layers = [l for l in text_layers if l.get("fontFamily") == "Roboto"]
    if len(roboto_layers) < 10:
        return False, f"Expected at least 10 layers switched to Roboto, but found {len(roboto_layers)}."

    return True, "All Inter layers have been switched to Roboto."
