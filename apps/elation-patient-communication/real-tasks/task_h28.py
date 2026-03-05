import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Cancel pacemaker patient's virtual appointment and schedule in-person
    with same provider on March 22 at 2 PM. Patient: Howard Blackwell."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    appointments = state.get("appointments", [])

    # Check appt_9 (Howard Blackwell's virtual) is cancelled
    appt_9 = next((a for a in appointments if a.get("id") == "appt_9"), None)
    if appt_9 is None:
        return False, "Appointment appt_9 (Howard Blackwell virtual) not found."
    if appt_9.get("status") != "cancelled":
        return False, (
            f"Howard Blackwell's virtual appointment status is "
            f"'{appt_9.get('status')}', expected 'cancelled'."
        )

    # Check new in-person appointment for pat_27 with prov_4 on March 22
    new_appt = next(
        (
            a for a in appointments
            if a.get("patientId") == "pat_27"
            and a.get("providerId") == "prov_4"
            and a.get("place") == "in_person"
            and a.get("status") == "scheduled"
            and "2026-03-22" in (a.get("date") or "")
        ),
        None,
    )
    if new_appt is None:
        return False, (
            "No in-person appointment found for Howard Blackwell with "
            "Dr. Kim on March 22, 2026."
        )

    return True, (
        "Howard Blackwell's virtual appointment cancelled and new "
        "in-person appointment scheduled on March 22."
    )
