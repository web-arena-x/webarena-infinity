import requests

def verify(server_url: str) -> tuple[bool, str]:
    """Verify that 'Sense' is now the live theme."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    sense = next((t for t in state["themes"] if t["name"] == "Sense"), None)
    if not sense:
        return False, "Theme 'Sense' not found."
    if sense.get("status") != "live":
        return False, f"Theme 'Sense' status is '{sense.get('status')}', expected 'live'."

    dawn = next((t for t in state["themes"] if t["name"] == "Dawn"), None)
    if dawn and dawn.get("status") == "live":
        return False, "Theme 'Dawn' is still live."

    return True, "Theme 'Sense' is now the live theme."
