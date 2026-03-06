import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify that an in-person appointment has been scheduled for Emily Thompson with Dr. Chen on March 15, 2026."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    # Find Emily Thompson's patient ID
    patients = state.get("patients", [])
    patient_id = None
    for pat in patients:
        if pat.get("firstName") == "Emily" and pat.get("lastName") == "Thompson":
            patient_id = pat.get("id")
            break

    if patient_id is None:
        return False, "Patient Emily Thompson not found"

    # Find the matching appointment
    appointments = state.get("appointments", [])
    matching = None
    for appt in appointments:
        if (appt.get("patientId") == patient_id
                and appt.get("providerId") == "prov_1"
                and appt.get("place") == "in_person"
                and appt.get("status") == "scheduled"):
            date_str = appt.get("date", "")
            if "2026-03-15" in date_str:
                matching = appt
                break

    if matching is None:
        return False, (
            "No scheduled in-person appointment found for Emily Thompson with Dr. Chen (prov_1) "
            "on 2026-03-15"
        )

    reason = (matching.get("reason") or "").lower()
    if "check" not in reason:
        return False, (
            f"Appointment reason is '{matching.get('reason')}', expected it to contain 'check' "
            f"(for general check-up)"
        )

    return True, "In-person appointment scheduled for Emily Thompson with Dr. Chen on March 15, 2026 for a check-up"
