import requests


def verify(server_url: str) -> tuple[bool, str]:
    try:
        resp = requests.get(f"{server_url}/api/state")
        if resp.status_code != 200:
            return False, f"Failed to fetch state: HTTP {resp.status_code}"
        state = resp.json()
    except Exception as e:
        return False, f"Error fetching state: {e}"

    # Check Amoxicillin is NOT in temporaryMeds
    temporary_meds = state.get("temporaryMeds", [])
    for med in temporary_meds:
        if med.get("medicationName") == "Amoxicillin 500mg capsule":
            return False, "Amoxicillin 500mg capsule still present in temporaryMeds"

    # Check Amoxicillin IS in permanentRxMeds
    permanent_rx_meds = state.get("permanentRxMeds", [])
    amoxicillin_perm = None
    for med in permanent_rx_meds:
        if med.get("medicationName") == "Amoxicillin 500mg capsule":
            amoxicillin_perm = med
            break

    if amoxicillin_perm is None:
        return False, "Amoxicillin 500mg capsule not found in permanentRxMeds"

    if amoxicillin_perm.get("classification") != "permanent_rx":
        return False, f"Amoxicillin classification is '{amoxicillin_perm.get('classification')}', expected 'permanent_rx'"

    return True, "Amoxicillin 500mg capsule set to permanent medication successfully"
