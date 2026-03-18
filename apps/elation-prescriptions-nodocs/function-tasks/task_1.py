import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    prescriptions = state.get("prescriptions", [])

    # Seed prescription IDs are rx_001 through rx_030. New prescriptions will have different IDs.
    seed_ids = {f"rx_{str(i).zfill(3)}" for i in range(1, 31)}

    # Find a new Ibuprofen prescription for pat_001
    matches = [
        rx for rx in prescriptions
        if rx.get("patientId") == "pat_001"
        and "ibuprofen" in rx.get("drugName", "").lower()
        and rx.get("id") not in seed_ids
    ]

    if not matches:
        return False, "No new Ibuprofen prescription found for pat_001."

    rx = matches[0]
    errors = []

    if "400mg" not in rx.get("formStrength", ""):
        errors.append(f"formStrength should contain '400mg', got '{rx.get('formStrength')}'")

    if rx.get("frequency") != "Twice daily":
        errors.append(f"frequency should be 'Twice daily', got '{rx.get('frequency')}'")

    if rx.get("route") != "Oral":
        errors.append(f"route should be 'Oral', got '{rx.get('route')}'")

    if rx.get("quantity") != 60:
        errors.append(f"quantity should be 60, got {rx.get('quantity')}")

    if rx.get("daysSupply") != 30:
        errors.append(f"daysSupply should be 30, got {rx.get('daysSupply')}")

    if rx.get("refillsTotal") != 2:
        errors.append(f"refillsTotal should be 2, got {rx.get('refillsTotal')}")

    if rx.get("pharmacyId") != "pharm_001":
        errors.append(f"pharmacyId should be 'pharm_001', got '{rx.get('pharmacyId')}'")

    if rx.get("status") != "active":
        errors.append(f"status should be 'active', got '{rx.get('status')}'")

    sig = rx.get("sig", "")
    if "every 6-8 hours" not in sig:
        errors.append(f"sig should contain 'every 6-8 hours', got '{sig}'")

    if errors:
        return False, "New Ibuprofen prescription found but has issues: " + "; ".join(errors)

    return True, "New Ibuprofen prescription for pat_001 is correct with all expected fields."
