import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # Find Cruz matter
    cruz = None
    for m in state.get("matters", []):
        if "Cruz" in (m.get("description") or ""):
            cruz = m
            break

    if not cruz:
        return False, "Cruz bus accident matter not found."

    # Find Advanced Imaging provider (con_020)
    aia_provider = None
    for p in cruz.get("medicalProviders", []):
        if p.get("contactId") == "con_020":
            aia_provider = p
            break

    if not aia_provider:
        return False, "Advanced Imaging Associates provider (con_020) not found on Cruz case."

    errors = []

    # Check description
    desc = aia_provider.get("description", "")
    if "MRI" not in desc and "cervical" not in desc.lower():
        errors.append(f"Provider description is '{desc}', expected to mention MRI cervical spine")

    # Check record status
    if aia_provider.get("recordStatus") != "Requested":
        errors.append(
            f"Record status is '{aia_provider.get('recordStatus')}', expected 'Requested'"
        )

    # Check record request date
    if aia_provider.get("recordRequestDate") != "2026-03-01":
        errors.append(
            f"Record request date is '{aia_provider.get('recordRequestDate')}', "
            f"expected '2026-03-01'"
        )

    # Check medical record exists
    records = aia_provider.get("medicalRecords", [])
    target_record = [r for r in records if r.get("fileName") == "Cervical_MRI_Cruz.pdf"]
    if not target_record:
        errors.append("Medical record 'Cervical_MRI_Cruz.pdf' not found")
    else:
        rec = target_record[0]
        if rec.get("receivedDate") != "2026-03-15":
            errors.append(
                f"Record received date is '{rec.get('receivedDate')}', expected '2026-03-15'"
            )

    if errors:
        return False, "; ".join(errors)

    return True, "AIA provider added to Cruz with MRI description, Requested status, and medical record."
