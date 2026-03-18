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
        and "pregabalin" in rx.get("drugName", "").lower()
        and rx.get("id") not in seed_ids
    ]

    if not matches:
        return False, "No new Pregabalin prescription found for pat_001."

    rx = matches[0]
    errors = []

    if "75mg" not in rx.get("formStrength", ""):
        errors.append(f"formStrength should contain '75mg', got '{rx.get('formStrength')}'")

    if rx.get("frequency") != "Twice daily":
        errors.append(f"frequency should be 'Twice daily', got '{rx.get('frequency')}'")

    if rx.get("quantity") != 60:
        errors.append(f"quantity should be 60, got {rx.get('quantity')}")

    if rx.get("refillsTotal") != 1:
        errors.append(f"refillsTotal should be 1, got {rx.get('refillsTotal')}")

    if rx.get("status") != "active":
        errors.append(f"status should be 'active', got '{rx.get('status')}'")

    if errors:
        return False, "New Pregabalin prescription found but has issues: " + "; ".join(errors)

    return True, "New Pregabalin controlled substance prescription for pat_001 is correct."
