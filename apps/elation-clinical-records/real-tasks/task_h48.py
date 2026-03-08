import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Patient born in 1940s with Medicare → record PCV20 vaccine: Pfizer, IM, left deltoid, dose 1, 5yr recall, Medicare."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    # Find patient born in 1940s with Medicare
    target = None
    for p in state.get("patients", []):
        dob = p.get("dateOfBirth", "")
        insurance = (p.get("insurancePrimary") or "").lower()
        if dob.startswith("194") and "medicare" in insurance:
            target = p
            break
    if not target:
        return False, "No patient born in 1940s with Medicare found."

    last_name = target.get("lastName", "?")
    pid = target.get("id")

    # Check for PCV20 vaccination
    vaccinations = state.get("vaccinations", [])
    patient_vax = [v for v in vaccinations if v.get("patientId") == pid]

    pcv20 = None
    for v in patient_vax:
        name = (v.get("vaccineName") or "").lower()
        if "pneumococcal" in name and "20" in name:
            pcv20 = v
            break

    if not pcv20:
        return False, f"{last_name} has no Pneumococcal 20-valent vaccine recorded."

    errors = []
    mfg = (pcv20.get("manufacturer") or "").lower()
    if "pfizer" not in mfg:
        errors.append(f"Manufacturer is '{pcv20.get('manufacturer')}', expected Pfizer.")

    method = (pcv20.get("method") or "").lower()
    if "intramuscular" not in method:
        errors.append(f"Method is '{pcv20.get('method')}', expected Intramuscular.")

    site = (pcv20.get("site") or "").lower()
    if "left deltoid" not in site:
        errors.append(f"Site is '{pcv20.get('site')}', expected Left Deltoid.")

    series = str(pcv20.get("seriesNumber", "")).strip()
    if series != "1":
        errors.append(f"Series number is '{series}', expected '1'.")

    recall = (pcv20.get("recall") or "").lower()
    if "5 year" not in recall:
        errors.append(f"Recall is '{pcv20.get('recall')}', expected '5 years'.")

    funded = (pcv20.get("fundedBy") or "").lower()
    if "medicare" not in funded:
        errors.append(f"Funded by is '{pcv20.get('fundedBy')}', expected Medicare.")

    if errors:
        return False, " ".join(errors)
    return True, (
        f"{last_name} has PCV20 vaccine: Pfizer, IM left deltoid, dose 1, 5yr recall, Medicare funded."
    )
