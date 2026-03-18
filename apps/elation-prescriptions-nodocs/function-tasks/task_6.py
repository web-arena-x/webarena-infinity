import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    prescriptions = state.get("prescriptions", [])

    seed_ids = {f"rx_{str(i).zfill(3)}" for i in range(1, 31)}

    matches = [
        rx for rx in prescriptions
        if rx.get("patientId") == "pat_001"
        and "dulaglutide" in rx.get("drugName", "").lower()
        and rx.get("id") not in seed_ids
    ]

    if not matches:
        return False, "No new Dulaglutide prescription found for pat_001."

    rx = matches[0]
    errors = []

    if rx.get("route") != "Subcutaneous":
        errors.append(f"route should be 'Subcutaneous', got '{rx.get('route')}'")

    if rx.get("frequency") != "Once weekly":
        errors.append(f"frequency should be 'Once weekly', got '{rx.get('frequency')}'")

    if rx.get("quantity") != 4:
        errors.append(f"quantity should be 4, got {rx.get('quantity')}")

    if rx.get("daysSupply") != 28:
        errors.append(f"daysSupply should be 28, got {rx.get('daysSupply')}")

    if rx.get("refillsTotal") != 2:
        errors.append(f"refillsTotal should be 2, got {rx.get('refillsTotal')}")

    if rx.get("pharmacyId") != "pharm_010":
        errors.append(f"pharmacyId should be 'pharm_010' (BioPlus Specialty), got '{rx.get('pharmacyId')}'")

    if rx.get("status") != "active":
        errors.append(f"status should be 'active', got '{rx.get('status')}'")

    if errors:
        return False, "New Dulaglutide prescription found but has issues: " + "; ".join(errors)

    return True, "New Dulaglutide injectable prescription for pat_001 is correct."
