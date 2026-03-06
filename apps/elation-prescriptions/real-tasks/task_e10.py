import requests


def verify(server_url: str) -> tuple[bool, str]:
    try:
        resp = requests.get(f"{server_url}/api/state")
        if resp.status_code != 200:
            return False, f"Failed to fetch state: HTTP {resp.status_code}"
        state = resp.json()
    except Exception as e:
        return False, f"Error fetching state: {e}"

    # Check Montelukast is NOT in permanentRxMeds
    permanent_rx_meds = state.get("permanentRxMeds", [])
    for med in permanent_rx_meds:
        if med.get("medicationName") == "Montelukast 10mg tablet":
            return False, "Montelukast 10mg tablet still present in permanentRxMeds"

    # Check Montelukast IS in temporaryMeds
    temporary_meds = state.get("temporaryMeds", [])
    montelukast_temp = None
    for med in temporary_meds:
        if med.get("medicationName") == "Montelukast 10mg tablet":
            montelukast_temp = med
            break

    if montelukast_temp is None:
        return False, "Montelukast 10mg tablet not found in temporaryMeds"

    if montelukast_temp.get("classification") != "temporary":
        return False, f"Montelukast classification is '{montelukast_temp.get('classification')}', expected 'temporary'"

    return True, "Montelukast 10mg tablet marked as temporary medication successfully"
