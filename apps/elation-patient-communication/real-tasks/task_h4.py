import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    appointments = state.get("appointments", [])
    appt_map = {a["id"]: a for a in appointments}

    # Virtual March appointments that should be cancelled
    virtual_march_ids = ["appt_2", "appt_6", "appt_9", "appt_13", "appt_14"]

    for appt_id in virtual_march_ids:
        appt = appt_map.get(appt_id)
        if appt is None:
            return False, f"Appointment {appt_id} not found in state."
        if appt.get("status") != "cancelled":
            return False, (
                f"Appointment {appt_id} status is '{appt.get('status')}', "
                f"expected 'cancelled'."
            )

    # In-person March appointments that should NOT be cancelled
    in_person_march_ids = [
        "appt_1", "appt_3", "appt_4", "appt_5",
        "appt_7", "appt_10", "appt_11", "appt_12",
    ]

    for appt_id in in_person_march_ids:
        appt = appt_map.get(appt_id)
        if appt is None:
            continue  # May not exist, skip
        if appt.get("status") == "cancelled":
            return False, (
                f"In-person appointment {appt_id} was incorrectly cancelled."
            )

    return True, "All 5 virtual March appointments have been cancelled."
