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
        and "rosuvastatin" in rx.get("drugName", "").lower()
        and rx.get("id") not in seed_ids
    ]

    if not matches:
        return False, "No new Rosuvastatin prescription found for pat_001."

    rx = matches[0]
    errors = []

    if "10mg" not in rx.get("formStrength", ""):
        errors.append(f"formStrength should contain '10mg', got '{rx.get('formStrength')}'")

    if rx.get("priorAuth") is not True:
        errors.append(f"priorAuth should be True, got {rx.get('priorAuth')}")

    if rx.get("priorAuthNumber") != "PA-2026-99999":
        errors.append(f"priorAuthNumber should be 'PA-2026-99999', got '{rx.get('priorAuthNumber')}'")

    if rx.get("refillsTotal") != 2:
        errors.append(f"refillsTotal should be 2, got {rx.get('refillsTotal')}")

    if rx.get("status") != "active":
        errors.append(f"status should be 'active', got '{rx.get('status')}'")

    if errors:
        return False, "New Rosuvastatin prescription found but has issues: " + "; ".join(errors)

    return True, "New Rosuvastatin prescription for pat_001 with prior auth is correct."
