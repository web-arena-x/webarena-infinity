import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    appointments = state.get("appointments", [])
    appt = None
    for a in appointments:
        if a.get("id") == "appt_10":
            appt = a
            break

    if appt is None:
        return False, "Appointment appt_10 not found."

    if appt.get("status") != "cancelled":
        return False, f"Appointment appt_10 status is '{appt.get('status')}', expected 'cancelled'."

    return True, "Rachel Steinberg's appointment has been cancelled."
