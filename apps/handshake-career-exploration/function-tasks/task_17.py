import requests

def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()
    evt = next((e for e in state["events"] if e["id"] == "evt_02"), None)
    if not evt:
        return False, "Event 'evt_02' not found."
    if not evt.get("rsvped"):
        return False, "Event not RSVPed."
    if evt["rsvpCount"] <= 234:
        return False, f"RSVP count not increased. Expected > 234, got {evt['rsvpCount']}."
    return True, "RSVPed to AI/ML Careers at Meta event successfully."
