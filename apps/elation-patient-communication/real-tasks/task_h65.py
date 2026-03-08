import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify appointment scheduled for Linda Garcia (pat_6) who mentioned withdrawal effects."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    # Look for new appointment for pat_6 with prov_3
    seed_appt_ids = {f"appt_{i}" for i in range(1, 21)}

    found = False
    for appt in state.get("appointments", []):
        if appt.get("id") in seed_appt_ids:
            continue
        if (appt.get("patientId") == "pat_6"
                and appt.get("providerId") == "prov_3"
                and appt.get("place") == "in_person"
                and appt.get("status") == "scheduled"):
            # Check date
            date = appt.get("date", "")
            if "2026-03-25" in date:
                found = True
                break

    if not found:
        return False, (
            "No in-person appointment found for pat_6 (Linda Garcia) "
            "with prov_3 (Jessica Okafor) on March 25, 2026"
        )

    return True, "Appointment scheduled for Linda Garcia with Jessica Okafor on March 25, 2026"
