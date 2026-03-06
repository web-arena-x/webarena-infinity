import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify a bulk letter was sent to all geriatric patients with responses allowed."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    # Geriatric patients: pat_3, pat_10, pat_19, pat_24, pat_27, pat_33, pat_36, pat_43, pat_47, pat_50
    geriatric_ids = {
        "pat_3", "pat_10", "pat_19", "pat_24", "pat_27",
        "pat_33", "pat_36", "pat_43", "pat_47", "pat_50"
    }

    seed_bulk_ids = {"bulk_1", "bulk_2", "bulk_3"}

    bulk_letters = state.get("bulkLetters", [])

    # Find a new bulk letter (not in seed data)
    new_bulk = None
    for bl in bulk_letters:
        if bl.get("id") not in seed_bulk_ids:
            new_bulk = bl
            break

    if new_bulk is None:
        return False, "No new bulk letter found in state"

    # Check that responses are allowed
    if not new_bulk.get("allowResponse"):
        return False, (
            f"New bulk letter '{new_bulk.get('id')}' has allowResponse={new_bulk.get('allowResponse')}, "
            f"expected True"
        )

    # Check target count is at least 10 (number of geriatric patients)
    target_count = new_bulk.get("targetCount", 0)
    if target_count < 10:
        return False, (
            f"New bulk letter targetCount is {target_count}, expected at least 10 "
            f"(number of geriatric patients)"
        )

    # Also verify individual letters were created for geriatric patients
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

    # Check that new to_patient letters exist for geriatric patients
    patients_with_new_letter = set()
    for ltr in letters:
        if (ltr.get("id") not in seed_letter_ids
                and ltr.get("direction") == "to_patient"
                and not ltr.get("isDraft", False)
                and ltr.get("patientId") in geriatric_ids):
            patients_with_new_letter.add(ltr.get("patientId"))

    missing_patients = geriatric_ids - patients_with_new_letter
    if missing_patients:
        return False, (
            f"Bulk letter created but individual letters missing for geriatric patients: "
            f"{', '.join(sorted(missing_patients))}"
        )

    return True, (
        "Bulk letter sent to all 10 geriatric patients about annual wellness visit, "
        "with responses allowed"
    )
