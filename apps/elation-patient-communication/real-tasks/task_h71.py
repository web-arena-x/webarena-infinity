import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify bulk letter sent to NP's patients and NP notification timeframe changed to 48h."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, f"Failed to fetch state: HTTP {resp.status_code}"
    state = resp.json()

    errors = []

    # Check notification timeframe for prov_3 (nurse practitioner)
    prov_3 = None
    for prov in state.get("providers", []):
        if prov.get("id") == "prov_3":
            prov_3 = prov
            break

    if not prov_3:
        errors.append("Provider prov_3 (Jessica Okafor) not found")
    else:
        tf = prov_3.get("notificationTimeframe")
        if tf != "48_hours":
            errors.append(f"prov_3 notification timeframe is '{tf}', expected '48_hours'")

    # Check bulk letter was sent
    seed_bulk_ids = {"bulk_1", "bulk_2", "bulk_3"}
    new_bulk = None
    for bl in state.get("bulkLetters", []):
        if bl.get("id") not in seed_bulk_ids:
            new_bulk = bl
            break

    if not new_bulk:
        errors.append("No new bulk letter found")
    else:
        target_count = new_bulk.get("targetCount", 0)
        if target_count < 7:
            errors.append(
                f"Bulk letter targetCount is {target_count}, expected at least 7 "
                f"(all patients assigned to the nurse practitioner)"
            )

    # Check individual letters sent to NP's patients
    np_patient_ids = {"pat_6", "pat_12", "pat_20", "pat_28", "pat_34", "pat_40", "pat_44"}
    seed_letter_ids = {f"ltr_{i}" for i in range(1, 48)}

    patients_with_letters = set()
    for ltr in state.get("patientLetters", []):
        if (ltr.get("id") not in seed_letter_ids
                and ltr.get("patientId") in np_patient_ids
                and ltr.get("direction") == "to_patient"
                and not ltr.get("isDraft", False)):
            patients_with_letters.add(ltr.get("patientId"))

    missing = np_patient_ids - patients_with_letters
    if missing:
        errors.append(f"NP patients missing bulk letters: {', '.join(sorted(missing))}")

    if errors:
        return False, "; ".join(errors)
    return True, "Bulk letter sent to all NP patients and notification timeframe set to 48 hours"
