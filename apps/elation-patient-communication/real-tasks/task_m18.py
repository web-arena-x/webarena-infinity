import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    appointments = state.get("appointments", [])
    matching = None
    for appt in appointments:
        if (
            appt.get("patientId") == "pat_29"
            and appt.get("providerId") == "prov_2"
            and appt.get("place") == "virtual"
            and "2026-03-20" in str(appt.get("date", ""))
            and "15:00" in str(appt.get("date", ""))
            and appt.get("status") == "scheduled"
        ):
            matching = appt
            break

    if matching is None:
        return False, "No matching virtual appointment found for Andrew McIntyre (pat_29) on March 20, 2026 at 15:00 with provider prov_2."

    return True, "Virtual appointment scheduled for Andrew McIntyre on March 20, 2026."
