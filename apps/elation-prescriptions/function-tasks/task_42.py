import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    meds = state.get("temporaryMeds", [])

    match = [
        m for m in meds
        if "Doxycycline" in m.get("medicationName", "")
        and "100mg" in m.get("medicationName", "")
    ]

    if not match:
        return False, "No med found in temporaryMeds with medicationName containing 'Doxycycline' and '100mg'."

    med = match[0]
    errors = []

    sig = med.get("sig", "")
    if "twice daily" not in sig:
        errors.append(f"sig: expected to contain 'twice daily', got '{sig}'")
    if "14 days" not in sig:
        errors.append(f"sig: expected to contain '14 days', got '{sig}'")

    if med.get("qty") != 28:
        errors.append(f"qty: expected 28, got {med.get('qty')}")

    if med.get("refills") != 0:
        errors.append(f"refills: expected 0, got {med.get('refills')}")

    if med.get("daysSupply") != 14:
        errors.append(f"daysSupply: expected 14, got {med.get('daysSupply')}")

    if med.get("classification") != "temporary":
        errors.append(f"classification: expected 'temporary', got '{med.get('classification')}'")

    pharmacy_name = med.get("pharmacyName", "")
    if "Walgreens" not in pharmacy_name or "7892" not in pharmacy_name:
        errors.append(f"pharmacyName: expected to contain 'Walgreens' and '7892', got '{pharmacy_name}'")

    if errors:
        return False, f"Doxycycline 100mg found in temporaryMeds but has incorrect fields: {'; '.join(errors)}"

    return True, "Doxycycline 100mg correctly prescribed as temporary med to Walgreens #7892 with correct sig, qty=28, refills=0, daysSupply=14."
