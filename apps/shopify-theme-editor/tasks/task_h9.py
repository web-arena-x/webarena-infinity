import requests

def verify(server_url: str) -> tuple[bool, str]:
    """Verify 'Impact' theme published and renamed to 'Impact Pro'."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    theme = next((t for t in state["themes"] if t.get("name") == "Impact Pro"), None)
    if not theme:
        return False, "Theme 'Impact Pro' not found."

    if theme.get("status") != "live":
        return False, f"Theme 'Impact Pro' status is '{theme.get('status')}', expected 'live'."

    # Dawn should no longer be live
    dawn = next((t for t in state["themes"] if t.get("name") == "Dawn"), None)
    if dawn and dawn.get("status") == "live":
        return False, "Theme 'Dawn' is still live."

    return True, "Theme 'Impact' published and renamed to 'Impact Pro'."
