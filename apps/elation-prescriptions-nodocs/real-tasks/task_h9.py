import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    prescriptions = state.get("prescriptions", [])
    errors = []

    # Check rx_007 (Gabapentin) is discontinued
    rx_007 = None
    for rx in prescriptions:
        if rx.get("id") == "rx_007":
            rx_007 = rx
            break

    if rx_007 is None:
        errors.append("Prescription rx_007 (Gabapentin) not found.")
    elif rx_007.get("status") != "discontinued":
        errors.append(f"Expected rx_007 (Gabapentin) status 'discontinued', got '{rx_007.get('status')}'.")

    # Find new Pregabalin prescription for pat_001
    seed_ids = {f"rx_{str(i).zfill(3)}" for i in range(1, 31)}
    matches = [
        rx for rx in prescriptions
        if rx["id"] not in seed_ids
        and rx.get("patientId") == "pat_001"
        and "pregabalin" in rx.get("drugName", "").lower()
    ]

    if not matches:
        errors.append("No new Pregabalin prescription found for Margaret (pat_001).")
    else:
        new_rx = matches[0]
        if "75mg" not in new_rx.get("formStrength", "").lower().replace(" ", ""):
            errors.append(f"Pregabalin: expected formStrength to contain '75mg', got '{new_rx.get('formStrength')}'.")
        if new_rx.get("frequency") != "Twice daily":
            errors.append(f"Pregabalin: expected frequency 'Twice daily', got '{new_rx.get('frequency')}'.")
        if new_rx.get("quantity") != 60:
            errors.append(f"Pregabalin: expected quantity 60, got {new_rx.get('quantity')}.")
        if new_rx.get("daysSupply") != 30:
            errors.append(f"Pregabalin: expected daysSupply 30, got {new_rx.get('daysSupply')}.")
        if new_rx.get("refillsTotal") != 1:
            errors.append(f"Pregabalin: expected refillsTotal 1, got {new_rx.get('refillsTotal')}.")
        if new_rx.get("pharmacyId") != "pharm_001":
            errors.append(f"Pregabalin: expected pharmacyId 'pharm_001' (CVS), got '{new_rx.get('pharmacyId')}'.")

    if errors:
        return False, " ".join(errors)

    return True, "Gabapentin discontinued and Pregabalin 75mg prescribed correctly for Margaret."
