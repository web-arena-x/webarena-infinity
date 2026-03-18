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
        and "montelukast" in rx.get("drugName", "").lower()
        and rx.get("id") not in seed_ids
    ]

    if not matches:
        return False, "No new Montelukast prescription found for pat_001."

    rx = matches[0]
    errors = []

    if rx.get("pharmacyId") != "pharm_007":
        errors.append(f"pharmacyId should be 'pharm_007' (Alto Pharmacy), got '{rx.get('pharmacyId')}'")

    if rx.get("refillsTotal") != 5:
        errors.append(f"refillsTotal should be 5, got {rx.get('refillsTotal')}")

    if rx.get("status") != "active":
        errors.append(f"status should be 'active', got '{rx.get('status')}'")

    if errors:
        return False, "New Montelukast prescription found but has issues: " + "; ".join(errors)

    return True, "New Montelukast prescription for pat_001 sent to Alto Pharmacy is correct."
