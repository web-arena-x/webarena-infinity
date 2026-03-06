import requests


def verify(server_url: str) -> tuple[bool, str]:
    try:
        resp = requests.get(f"{server_url}/api/state")
        if resp.status_code != 200:
            return False, f"Failed to fetch state: HTTP {resp.status_code}"
        state = resp.json()
    except Exception as e:
        return False, f"Error fetching state: {e}"

    # Check Ciprofloxacin is NOT in temporaryMeds
    temporary_meds = state.get("temporaryMeds", [])
    for med in temporary_meds:
        if med.get("medicationName") == "Ciprofloxacin 500mg tablet":
            return False, "Ciprofloxacin 500mg tablet is still in temporaryMeds; expected it to be moved to permanentRxMeds"

    # Check Ciprofloxacin IS in permanentRxMeds
    permanent_rx_meds = state.get("permanentRxMeds", [])
    cipro_med = None
    for med in permanent_rx_meds:
        if med.get("medicationName") == "Ciprofloxacin 500mg tablet":
            cipro_med = med
            break

    if cipro_med is None:
        return False, "Ciprofloxacin 500mg tablet not found in permanentRxMeds"

    # Check classification is permanent_rx
    classification = cipro_med.get("classification", "")
    if classification != "permanent_rx":
        return False, f"Ciprofloxacin classification is '{classification}', expected 'permanent_rx'"

    return True, "Ciprofloxacin moved from temporary to permanent Rx successfully"
