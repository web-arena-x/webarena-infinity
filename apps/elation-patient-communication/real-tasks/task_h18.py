import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    appointments = state.get("appointments", [])

    # Check appointment for Emily Thompson (pat_2)
    emily_appts = [
        a for a in appointments
        if a.get("patientId") == "pat_2"
        and a.get("providerId") == "prov_1"
        and a.get("place") == "in_person"
        and "2026-03-15" in (a.get("date") or "")
        and "14:00" in (a.get("date") or "")
        and a.get("status") == "scheduled"
    ]

    if not emily_appts:
        return False, (
            "No matching appointment found for Emily Thompson (pat_2) with "
            "prov_1, in_person, 2026-03-15 at 14:00, status scheduled."
        )

    # Check appointment for Priya Sharma (pat_32)
    priya_appts = [
        a for a in appointments
        if a.get("patientId") == "pat_32"
        and a.get("providerId") == "prov_1"
        and a.get("place") == "in_person"
        and "2026-03-18" in (a.get("date") or "")
        and "10:00" in (a.get("date") or "")
        and a.get("status") == "scheduled"
    ]

    if not priya_appts:
        return False, (
            "No matching appointment found for Priya Sharma (pat_32) with "
            "prov_1, in_person, 2026-03-18 at 10:00, status scheduled."
        )

    return True, "Appointments scheduled for Emily Thompson and Priya Sharma."
