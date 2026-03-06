import requests


def verify(server_url: str) -> tuple[bool, str]:
    try:
        resp = requests.get(f"{server_url}/api/state")
        if resp.status_code != 200:
            return False, f"Failed to fetch state: HTTP {resp.status_code}"
        state = resp.json()
    except Exception as e:
        return False, f"Error fetching state: {e}"

    temporary_meds = state.get("temporaryMeds", [])
    if len(temporary_meds) > 0:
        remaining_names = [m.get("medicationName", "unknown") for m in temporary_meds]
        return False, f"temporaryMeds is not empty, still contains: {remaining_names}"

    discontinued_meds = state.get("discontinuedMeds", [])
    expected_meds = [
        "Amoxicillin 500mg capsule",
        "Prednisone 10mg tablet",
        "Ciprofloxacin 500mg tablet",
    ]

    for expected_name in expected_meds:
        found = None
        for med in discontinued_meds:
            if med.get("medicationName") == expected_name:
                found = med
                break
        if found is None:
            return False, f"'{expected_name}' not found in discontinuedMeds"
        if found.get("status") != "discontinued":
            return False, f"'{expected_name}' in discontinuedMeds has status '{found.get('status')}', expected 'discontinued'"

    return True, "All 3 temporary medications discontinued successfully"
