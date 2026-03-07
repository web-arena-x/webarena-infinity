import requests

def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()
    appt = next((a for a in state["appointments"] if a["id"] == "appt_08"), None)
    if not appt:
        return False, "Appointment 'appt_08' not found."
    if appt["status"] != "cancelled":
        return False, f"Appointment status is '{appt['status']}', expected 'cancelled'."
    return True, "Case Interview Prep appointment cancelled successfully."
