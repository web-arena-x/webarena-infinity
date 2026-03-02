import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify that Montelukast 10mg tablet was moved from permanent Rx to temporary."""
    try:
        resp = requests.get(f"{server_url}/api/state")
        if resp.status_code != 200:
            return False, f"Failed to fetch state: HTTP {resp.status_code}"
        state = resp.json()
    except Exception as e:
        return False, f"Error fetching state: {e}"

    med_name = "Montelukast 10mg tablet"

    # Check that Montelukast is NOT in permanentRxMeds
    permanent_rx_meds = state.get("permanentRxMeds", [])
    for med in permanent_rx_meds:
        if med.get("medicationName") == med_name:
            return False, f"'{med_name}' still exists in permanentRxMeds"

    # Check that Montelukast IS in temporaryMeds
    temporary_meds = state.get("temporaryMeds", [])
    montelukast_temp = None
    for med in temporary_meds:
        if med.get("medicationName") == med_name:
            montelukast_temp = med
            break

    if montelukast_temp is None:
        return False, f"'{med_name}' not found in temporaryMeds"

    # Check classification is 'temporary'
    classification = montelukast_temp.get("classification")
    if classification != "temporary":
        return False, f"'{med_name}' classification in temporaryMeds is '{classification}', expected 'temporary'"

    return True, (
        f"'{med_name}' successfully moved from permanentRxMeds to temporaryMeds "
        f"with classification='{classification}'"
    )
