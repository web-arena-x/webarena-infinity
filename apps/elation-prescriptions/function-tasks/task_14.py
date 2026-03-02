import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify that Amoxicillin 500mg capsule was moved from temporary to permanent Rx."""
    try:
        resp = requests.get(f"{server_url}/api/state")
        if resp.status_code != 200:
            return False, f"Failed to fetch state: HTTP {resp.status_code}"
        state = resp.json()
    except Exception as e:
        return False, f"Error fetching state: {e}"

    med_name = "Amoxicillin 500mg capsule"

    # Check that Amoxicillin is NOT in temporaryMeds
    temporary_meds = state.get("temporaryMeds", [])
    for med in temporary_meds:
        if med.get("medicationName") == med_name:
            return False, f"'{med_name}' still exists in temporaryMeds"

    # Check that Amoxicillin IS in permanentRxMeds
    permanent_rx_meds = state.get("permanentRxMeds", [])
    amoxicillin_perm = None
    for med in permanent_rx_meds:
        if med.get("medicationName") == med_name:
            amoxicillin_perm = med
            break

    if amoxicillin_perm is None:
        return False, f"'{med_name}' not found in permanentRxMeds"

    # Check classification is 'permanent_rx'
    classification = amoxicillin_perm.get("classification")
    if classification != "permanent_rx":
        return False, f"'{med_name}' classification in permanentRxMeds is '{classification}', expected 'permanent_rx'"

    return True, (
        f"'{med_name}' successfully moved from temporaryMeds to permanentRxMeds "
        f"with classification='{classification}'"
    )
