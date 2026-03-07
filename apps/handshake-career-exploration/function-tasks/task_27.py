import requests

def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()
    for appt in state["appointments"]:
        if (appt.get("category") == "Interview Preparation" and
            appt.get("type") == "Mock Interview - Behavioral" and
            appt.get("staffName") == "David Kim" and
            appt.get("date") == "2026-03-11" and
            appt.get("time") == "10:00 AM" and
            appt.get("medium") == "Virtual on Handshake" and
            appt.get("status") == "requested"):
            if "Amazon behavioral" in appt.get("details", ""):
                return True, "Appointment with David Kim scheduled successfully."
            return False, f"Appointment found but details don't match. Got: {appt.get('details', '')}"
    return False, "No matching appointment found."
