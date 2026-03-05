import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Cancel all Dr. Chen's upcoming in-person appointments, keep virtual."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    appointments = state.get("appointments", [])
    appt_map = {a["id"]: a for a in appointments}

    # Dr. Chen's in-person upcoming appointments that should be cancelled
    should_cancel = ["appt_1", "appt_4", "appt_7", "appt_11", "appt_12"]
    for appt_id in should_cancel:
        appt = appt_map.get(appt_id)
        if appt is None:
            return False, f"Appointment {appt_id} not found."
        if appt.get("status") != "cancelled":
            return False, (
                f"Appointment {appt_id} status is '{appt.get('status')}', "
                f"expected 'cancelled'."
            )

    # Virtual appointments should remain scheduled
    should_keep = ["appt_2", "appt_13"]
    for appt_id in should_keep:
        appt = appt_map.get(appt_id)
        if appt is None:
            return False, f"Appointment {appt_id} not found."
        if appt.get("status") != "scheduled":
            return False, (
                f"Virtual appointment {appt_id} status is "
                f"'{appt.get('status')}', expected 'scheduled' (should not "
                f"have been cancelled)."
            )

    return True, (
        "All 5 in-person appointments cancelled; 2 virtual appointments "
        "remain scheduled."
    )
