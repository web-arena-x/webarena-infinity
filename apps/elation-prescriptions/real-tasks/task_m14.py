import requests


def verify(server_url: str) -> tuple[bool, str]:
    try:
        resp = requests.get(f"{server_url}/api/state")
        if resp.status_code != 200:
            return False, f"Failed to fetch state: HTTP {resp.status_code}"
        state = resp.json()
    except Exception as e:
        return False, f"Error fetching state: {e}"

    # Check Prednisone is NOT in temporaryMeds
    temporary_meds = state.get("temporaryMeds", [])
    for med in temporary_meds:
        if med.get("medicationName") == "Prednisone 10mg tablet":
            return False, "Prednisone 10mg tablet is still in temporaryMeds; expected it to be removed"

    # Check Prednisone IS in discontinuedMeds with status "discontinued"
    discontinued_meds = state.get("discontinuedMeds", [])
    prednisone_discontinued = None
    for med in discontinued_meds:
        if med.get("medicationName") == "Prednisone 10mg tablet":
            prednisone_discontinued = med
            break

    if prednisone_discontinued is None:
        return False, "Prednisone 10mg tablet not found in discontinuedMeds"

    if prednisone_discontinued.get("status") != "discontinued":
        return False, f"Prednisone in discontinuedMeds has status '{prednisone_discontinued.get('status')}', expected 'discontinued'"

    return True, "Prednisone taper discontinued successfully"
