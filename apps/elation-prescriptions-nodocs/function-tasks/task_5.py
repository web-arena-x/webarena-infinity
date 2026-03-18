import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    prescriptions = state.get("prescriptions", [])

    # Check that patient was switched to pat_002
    current_patient = state.get("currentPatientId")
    if current_patient != "pat_002":
        return False, f"currentPatientId should be 'pat_002', got '{current_patient}'."

    seed_ids = {f"rx_{str(i).zfill(3)}" for i in range(1, 31)}

    matches = [
        rx for rx in prescriptions
        if rx.get("patientId") == "pat_002"
        and "cephalexin" in rx.get("drugName", "").lower()
        and rx.get("id") not in seed_ids
    ]

    if not matches:
        return False, "No new Cephalexin prescription found for pat_002."

    rx = matches[0]
    errors = []

    if "500mg" not in rx.get("formStrength", ""):
        errors.append(f"formStrength should contain '500mg', got '{rx.get('formStrength')}'")

    if rx.get("frequency") != "Four times daily":
        errors.append(f"frequency should be 'Four times daily', got '{rx.get('frequency')}'")

    if rx.get("quantity") != 28:
        errors.append(f"quantity should be 28, got {rx.get('quantity')}")

    if rx.get("daysSupply") != 7:
        errors.append(f"daysSupply should be 7, got {rx.get('daysSupply')}")

    if rx.get("refillsTotal") != 0:
        errors.append(f"refillsTotal should be 0, got {rx.get('refillsTotal')}")

    if errors:
        return False, "New Cephalexin prescription found but has issues: " + "; ".join(errors)

    return True, "Patient switched to pat_002 and new Cephalexin prescription is correct."
