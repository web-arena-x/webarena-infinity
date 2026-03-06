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
            return False, "Amoxicillin 500mg capsule is still in temporaryMeds; expected it to be removed"

    # Check Amoxicillin IS in discontinuedMeds with status "discontinued"
    discontinued_meds = state.get("discontinuedMeds", [])
    amox_discontinued = None
    for med in discontinued_meds:
        if med.get("medicationName") == "Amoxicillin 500mg capsule":
            amox_discontinued = med
            break

    if amox_discontinued is None:
        return False, "Amoxicillin 500mg capsule not found in discontinuedMeds"

    if amox_discontinued.get("status") != "discontinued":
        return False, f"Amoxicillin in discontinuedMeds has status '{amox_discontinued.get('status')}', expected 'discontinued'"

    # Check canceledScripts contains a new entry for Amoxicillin
    # Seed only has 2 canceled scripts: Azithromycin 250mg (cxl_001) and Lisinopril 20mg (cxl_002)
    canceled_scripts = state.get("canceledScripts", [])
    seed_canceled_ids = {"cxl_001", "cxl_002"}
    amox_canceled = None
    for script in canceled_scripts:
        if script.get("medicationName") == "Amoxicillin 500mg capsule":
            amox_canceled = script
            break

    if amox_canceled is None:
        return False, "No canceled script found for Amoxicillin 500mg capsule in canceledScripts"

    return True, "Amoxicillin discontinued and cancellation sent to pharmacy successfully"
