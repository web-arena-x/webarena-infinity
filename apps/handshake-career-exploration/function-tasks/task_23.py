import requests

def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()
    for appt in state["appointments"]:
        if (appt.get("category") == "Career Counseling" and
            appt.get("type") == "General Career Advising" and
            appt.get("date") == "2026-03-10" and
            appt.get("time") == "9:00 AM" and
            appt.get("medium") == "In Person" and
            appt.get("status") == "requested"):
            if "choosing between tech and consulting" in appt.get("details", ""):
                return True, "Appointment scheduled successfully."
            return False, f"Appointment found but details don't match. Got: {appt.get('details', '')}"
    return False, "No matching appointment found."
