import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify a reply was sent to Howard Blackwell and a virtual follow-up scheduled with Dr. Kim on April 1."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    letters = state.get("patientLetters", [])

    seed_letter_ids = {
        "ltr_1", "ltr_2", "ltr_3", "ltr_4", "ltr_5", "ltr_6", "ltr_7", "ltr_8",
        "ltr_9", "ltr_10", "ltr_11", "ltr_12", "ltr_13", "ltr_14", "ltr_15",
        "ltr_16", "ltr_17", "ltr_18", "ltr_19", "ltr_20", "ltr_21", "ltr_22",
        "ltr_23", "ltr_24", "ltr_25", "ltr_26", "ltr_27", "ltr_28", "ltr_29",
        "ltr_30", "ltr_31", "ltr_32", "ltr_33", "ltr_34", "ltr_35", "ltr_36",
        "ltr_37", "ltr_38", "ltr_39", "ltr_40", "ltr_41", "ltr_42", "ltr_43",
        "ltr_44", "ltr_45", "ltr_46", "ltr_47"
    }

    # Check for a reply in conv_24 (Howard Blackwell's conversation)
    conv_24_letters = [ltr for ltr in letters if ltr.get("conversationId") == "conv_24"]
    new_reply = None
    for ltr in conv_24_letters:
        if (ltr.get("id") not in seed_letter_ids
                and ltr.get("direction") == "to_patient"
                and not ltr.get("isDraft", False)):
            new_reply = ltr
            break

    if new_reply is None:
        return False, "No reply found in conv_24 for Howard Blackwell about gardening"

    # Check for a new virtual appointment for pat_27 with prov_4 on April 1, 2026
    appointments = state.get("appointments", [])
    seed_appt_ids = {
        "appt_1", "appt_2", "appt_3", "appt_4", "appt_5", "appt_6", "appt_7",
        "appt_8", "appt_9", "appt_10", "appt_11", "appt_12", "appt_13", "appt_14",
        "appt_15", "appt_16", "appt_17", "appt_18", "appt_19", "appt_20"
    }

    matching_appt = None
    for appt in appointments:
        if (appt.get("patientId") == "pat_27"
                and appt.get("providerId") == "prov_4"
                and appt.get("place") == "virtual"
                and appt.get("status") == "scheduled"):
            date_str = appt.get("date", "")
            if "2026-04-01" in date_str:
                matching_appt = appt
                break

    if matching_appt is None:
        return False, (
            "No scheduled virtual appointment found for Howard Blackwell (pat_27) "
            "with Dr. Kim (prov_4) on 2026-04-01"
        )

    # Check time is approximately 2:00 PM (14:00)
    date_str = matching_appt.get("date", "")
    if "14:00" not in date_str and "14:0" not in date_str:
        return False, (
            f"Appointment date is '{date_str}', expected time around 14:00 (2:00 PM)"
        )

    return True, (
        "Reply sent to Howard Blackwell about gardening being safe, and "
        "virtual follow-up scheduled with Dr. Kim on April 1, 2026 at 2:00 PM"
    )
