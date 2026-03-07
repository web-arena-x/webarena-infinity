import requests

def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()
    evt = next((e for e in state["events"] if e["id"] == "evt_05"), None)
    if not evt:
        return False, "Event 'evt_05' not found."
    if not evt.get("rsvped"):
        return False, "Event not RSVPed."
    if evt["rsvpCount"] <= 45:
        return False, f"RSVP count not increased. Expected > 45, got {evt['rsvpCount']}."
    return True, "RSVPed to Resume Workshop successfully."
