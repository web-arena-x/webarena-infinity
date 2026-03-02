import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    meds = state.get("temporaryMeds", [])

    match = [
        m for m in meds
        if "Cyclobenzaprine" in m.get("medicationName", "")
        and "10mg" in m.get("medicationName", "")
    ]

    if not match:
        return False, "No med found in temporaryMeds with medicationName containing 'Cyclobenzaprine' and '10mg'."

    med = match[0]
    errors = []

    sig = med.get("sig", "")
    if "three times daily" not in sig:
        errors.append(f"sig: expected to contain 'three times daily', got '{sig}'")
    if "muscle spasm" not in sig:
        errors.append(f"sig: expected to contain 'muscle spasm', got '{sig}'")

    if med.get("qty") != 30:
        errors.append(f"qty: expected 30, got {med.get('qty')}")

    if med.get("refills") != 0:
        errors.append(f"refills: expected 0, got {med.get('refills')}")

    if med.get("daysSupply") != 10:
        errors.append(f"daysSupply: expected 10, got {med.get('daysSupply')}")

    if med.get("classification") != "temporary":
        errors.append(f"classification: expected 'temporary', got '{med.get('classification')}'")

    if errors:
        return False, f"Cyclobenzaprine 10mg found in temporaryMeds but has incorrect fields: {'; '.join(errors)}"

    if len(meds) != 4:
        return False, f"Expected 4 temporaryMeds after adding, found {len(meds)}."

    return True, "Cyclobenzaprine 10mg correctly prescribed as temporary med with correct sig, qty=30, refills=0, daysSupply=10."
