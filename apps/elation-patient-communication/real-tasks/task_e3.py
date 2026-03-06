import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify that Sophia Nguyen's thyroid check-up appointment is cancelled."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    appointments = state.get("appointments", [])
    appointment = None
    for appt in appointments:
        if appt.get("id") == "appt_2":
            appointment = appt
            break

    if appointment is None:
        return False, "Appointment appt_2 (Sophia Nguyen's thyroid check-up) not found"

    status = appointment.get("status", "")
    if status != "cancelled":
        return False, f"Appointment appt_2 status is '{status}', expected 'cancelled'"

    return True, "Sophia Nguyen's thyroid check-up appointment (appt_2) is cancelled"
