import requests

def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()
    evt = next((e for e in state["events"] if e["id"] == "evt_06"), None)
    if not evt:
        return False, "Event 'evt_06' not found."
    if not evt.get("rsvped"):
        return False, "Event not RSVPed."
    if evt["rsvpCount"] <= 198:
        return False, f"RSVP count not increased. Expected > 198, got {evt['rsvpCount']}."
    return True, "RSVPed to Anthropic Research Talk successfully."
