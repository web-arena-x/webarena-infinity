import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    meds = state.get("permanentRxMeds", [])

    match = [
        m for m in meds
        if "Famotidine" in m.get("medicationName", "")
        and "20mg" in m.get("medicationName", "")
    ]

    if not match:
        return False, "No med found in permanentRxMeds with medicationName containing 'Famotidine' and '20mg'."

    med = match[0]
    errors = []

    if med.get("dispenseAsWritten") is not True:
        errors.append(f"dispenseAsWritten: expected True, got {med.get('dispenseAsWritten')}")

    expected_sig = "Take 1 tablet by mouth twice daily"
    if med.get("sig") != expected_sig:
        errors.append(f"sig: expected '{expected_sig}', got '{med.get('sig')}'")

    if med.get("qty") != 60:
        errors.append(f"qty: expected 60, got {med.get('qty')}")

    if med.get("refills") != 3:
        errors.append(f"refills: expected 3, got {med.get('refills')}")

    if errors:
        return False, f"Famotidine 20mg found in permanentRxMeds but has incorrect fields: {'; '.join(errors)}"

    return True, "Famotidine 20mg correctly prescribed with dispenseAsWritten=True, sig='Take 1 tablet by mouth twice daily', qty=60, refills=3."
