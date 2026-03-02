import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    appointments = state.get("appointments", [])
    for appointment in appointments:
        if appointment.get("id") == "appt_2":
            status = appointment.get("status")
            if status == "cancelled":
                return True, "Sophia Nguyen's telehealth appointment has been cancelled."
            else:
                return False, f"Appointment appt_2 found but status is '{status}', expected 'cancelled'."

    return False, "Appointment with id 'appt_2' not found in appointments."
