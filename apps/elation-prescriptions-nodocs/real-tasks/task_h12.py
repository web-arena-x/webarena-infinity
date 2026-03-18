import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    errors = []

    if state.get("currentPatientId") != "pat_005":
        errors.append(f"Expected currentPatientId 'pat_005' (Jessica Morales), got '{state.get('currentPatientId')}'.")

    prescriptions = state.get("prescriptions", [])

    # New Amlodipine prescription for Aisha Rahman (pat_003)
    seed_ids = {f"rx_{str(i).zfill(3)}" for i in range(1, 31)}
    matches = [
        rx for rx in prescriptions
        if rx["id"] not in seed_ids
        and rx.get("patientId") == "pat_003"
        and "amlodipine" in rx.get("drugName", "").lower()
    ]

    if not matches:
        errors.append("No new Amlodipine prescription found for Aisha Rahman (pat_003).")
    else:
        new_rx = matches[0]
        if "5mg" not in new_rx.get("formStrength", "").lower().replace(" ", ""):
            errors.append(f"Amlodipine: expected formStrength containing '5mg', got '{new_rx.get('formStrength')}'.")
        if new_rx.get("quantity") != 30:
            errors.append(f"Amlodipine: expected quantity 30, got {new_rx.get('quantity')}.")
        if new_rx.get("refillsTotal") != 5:
            errors.append(f"Amlodipine: expected refillsTotal 5, got {new_rx.get('refillsTotal')}.")
        if new_rx.get("pharmacyId") != "pharm_002":
            errors.append(f"Amlodipine: expected pharmacyId 'pharm_002' (Walgreens), got '{new_rx.get('pharmacyId')}'.")

    # rx_025 (Cephalexin, Jessica Morales) should be discontinued
    rx_025 = None
    for rx in prescriptions:
        if rx.get("id") == "rx_025":
            rx_025 = rx
            break

    if rx_025 is None:
        errors.append("Prescription rx_025 (Cephalexin) not found.")
    elif rx_025.get("status") != "discontinued":
        errors.append(f"Expected rx_025 (Cephalexin) status 'discontinued', got '{rx_025.get('status')}'.")

    if errors:
        return False, " ".join(errors)

    return True, "Amlodipine prescribed for Aisha Rahman and Cephalexin discontinued for Jessica Morales."
