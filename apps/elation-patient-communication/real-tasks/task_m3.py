import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    appointments = state.get("appointments", [])
    target_patient_id = "pat_2"

    matching = None
    for appt in appointments:
        if (
            appt.get("patientId") == target_patient_id
            and appt.get("providerId") == "prov_1"
            and appt.get("place") == "in_person"
            and "2026-03-15" in str(appt.get("date", ""))
            and "14:00" in str(appt.get("date", ""))
            and appt.get("status") == "scheduled"
        ):
            matching = appt
            break

    if matching is None:
        return False, "No matching appointment found for Emily Thompson on March 15, 2026 at 2:00 PM with provider prov_1 in person."

    return True, "Appointment scheduled for Emily Thompson on March 15, 2026 at 2:00 PM."
