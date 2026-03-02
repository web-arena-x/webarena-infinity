import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    meds = state.get("permanentRxMeds", [])

    match = [
        m for m in meds
        if "Levothyroxine" in m.get("medicationName", "")
        and "50mcg" in m.get("medicationName", "")
    ]

    if not match:
        return False, "No med found in permanentRxMeds with medicationName containing 'Levothyroxine' and '50mcg'."

    med = match[0]
    errors = []

    expected_sig = "Take 1 tablet by mouth once daily on empty stomach"
    if med.get("sig") != expected_sig:
        errors.append(f"sig: expected '{expected_sig}', got '{med.get('sig')}'")

    if med.get("qty") != 30:
        errors.append(f"qty: expected 30, got {med.get('qty')}")

    if med.get("refills") != 5:
        errors.append(f"refills: expected 5, got {med.get('refills')}")

    if med.get("daysSupply") != 30:
        errors.append(f"daysSupply: expected 30, got {med.get('daysSupply')}")

    if med.get("classification") != "permanent_rx":
        errors.append(f"classification: expected 'permanent_rx', got '{med.get('classification')}'")

    pharmacy_name = med.get("pharmacyName", "")
    if "CVS" not in pharmacy_name or "4521" not in pharmacy_name:
        errors.append(f"pharmacyName: expected to contain 'CVS' and '4521', got '{pharmacy_name}'")

    if errors:
        return False, f"Levothyroxine 50mcg found in permanentRxMeds but has incorrect fields: {'; '.join(errors)}"

    if len(meds) != 12:
        return False, f"Expected 12 permanentRxMeds after adding, found {len(meds)}."

    return True, "Levothyroxine 50mcg correctly prescribed as permanent Rx to CVS Pharmacy #4521 with correct sig, qty=30, refills=5, daysSupply=30."
