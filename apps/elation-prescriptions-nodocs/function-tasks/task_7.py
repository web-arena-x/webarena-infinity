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
        and "diltiazem" in rx.get("drugName", "").lower()
        and rx.get("id") not in seed_ids
    ]

    if not matches:
        return False, "No new Diltiazem prescription found for pat_001."

    rx = matches[0]
    errors = []

    if "120mg" not in rx.get("formStrength", ""):
        errors.append(f"formStrength should contain '120mg', got '{rx.get('formStrength')}'")

    if rx.get("refillsTotal") != 5:
        errors.append(f"refillsTotal should be 5, got {rx.get('refillsTotal')}")

    if rx.get("frequency") != "Once daily":
        errors.append(f"frequency should be 'Once daily', got '{rx.get('frequency')}'")

    if rx.get("status") != "active":
        errors.append(f"status should be 'active', got '{rx.get('status')}'")

    if errors:
        return False, "New Diltiazem prescription found but has issues: " + "; ".join(errors)

    return True, "New Diltiazem prescription for pat_001 with 5 refills is correct."
