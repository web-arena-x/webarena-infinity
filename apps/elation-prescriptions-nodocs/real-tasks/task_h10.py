import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    errors = []

    if state.get("currentPatientId") != "pat_006":
        errors.append(f"Expected currentPatientId 'pat_006' (Robert Fitzgerald), got '{state.get('currentPatientId')}'.")

    prescriptions = state.get("prescriptions", [])
    seed_ids = {f"rx_{str(i).zfill(3)}" for i in range(1, 31)}
    matches = [
        rx for rx in prescriptions
        if rx["id"] not in seed_ids
        and rx.get("patientId") == "pat_006"
        and "sitagliptin" in rx.get("drugName", "").lower()
    ]

    if not matches:
        errors.append("No new Sitagliptin prescription found for Robert Fitzgerald (pat_006).")
    else:
        new_rx = matches[0]
        if "100mg" not in new_rx.get("formStrength", "").lower().replace(" ", ""):
            errors.append(f"Expected formStrength containing '100mg', got '{new_rx.get('formStrength')}'.")
        if new_rx.get("frequency") != "Once daily":
            errors.append(f"Expected frequency 'Once daily', got '{new_rx.get('frequency')}'.")
        if new_rx.get("quantity") != 30:
            errors.append(f"Expected quantity 30, got {new_rx.get('quantity')}.")
        if new_rx.get("refillsTotal") != 5:
            errors.append(f"Expected refillsTotal 5, got {new_rx.get('refillsTotal')}.")
        if new_rx.get("pharmacyId") != "pharm_004":
            errors.append(f"Expected pharmacyId 'pharm_004' (UCSF), got '{new_rx.get('pharmacyId')}'.")

    if errors:
        return False, " ".join(errors)

    return True, "Robert Fitzgerald selected and Sitagliptin 100mg prescribed correctly."
