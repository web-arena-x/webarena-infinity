import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify that a virtual appointment has been scheduled for Andrew McIntyre with Dr. Torres on March 20, 2026."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    # Find Andrew McIntyre's patient ID
    patients = state.get("patients", [])
    patient_id = None
    for pat in patients:
        if pat.get("firstName") == "Andrew" and pat.get("lastName") == "McIntyre":
            patient_id = pat.get("id")
            break

    if patient_id is None:
        return False, "Patient Andrew McIntyre not found"

    # Find the matching appointment
    appointments = state.get("appointments", [])
    matching = None
    for appt in appointments:
        if (appt.get("patientId") == patient_id
                and appt.get("providerId") == "prov_2"
                and appt.get("place") == "virtual"
                and appt.get("status") == "scheduled"):
            date_str = appt.get("date", "")
            if "2026-03-20" in date_str:
                matching = appt
                break

    if matching is None:
        return False, (
            "No scheduled virtual appointment found for Andrew McIntyre with Dr. Torres (prov_2) "
            "on 2026-03-20"
        )

    return True, "Virtual appointment scheduled for Andrew McIntyre with Dr. Torres on March 20, 2026"
