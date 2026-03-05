import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Enable telehealth for Amanda Wright, then schedule virtual appointment
    for Sophia Nguyen with Amanda Wright on Mar 20 at 3 PM."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # Check Amanda Wright telehealth activated
    providers = state.get("providers", [])
    prov_5 = next((p for p in providers if p.get("id") == "prov_5"), None)
    if prov_5 is None:
        return False, "Provider prov_5 (Amanda Wright) not found."
    if not prov_5.get("virtualVisitActivated"):
        return False, "Amanda Wright's telehealth is not activated."

    expected_url = "https://zoom.us/j/wright789"
    instructions = prov_5.get("virtualVisitInstructions", "")
    if expected_url not in instructions:
        return False, (
            f"Amanda Wright's telehealth instructions do not contain "
            f"'{expected_url}'. Current: '{instructions[:100]}...'"
        )

    # Check virtual appointment for Sophia Nguyen with Amanda Wright on Mar 20
    appointments = state.get("appointments", [])
    appt = next(
        (
            a for a in appointments
            if a.get("patientId") == "pat_4"
            and a.get("providerId") == "prov_5"
            and a.get("place") == "virtual"
            and a.get("status") == "scheduled"
            and "2026-03-20" in (a.get("date") or "")
        ),
        None,
    )
    if appt is None:
        return False, (
            "No virtual appointment found for Sophia Nguyen with "
            "Amanda Wright on March 20, 2026."
        )

    return True, (
        "Telehealth enabled for Amanda Wright and virtual appointment "
        "scheduled for Sophia Nguyen."
    )
