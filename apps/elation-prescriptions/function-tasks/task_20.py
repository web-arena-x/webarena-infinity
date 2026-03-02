import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    med_name = "Gabapentin 300mg capsule"

    # Check that the med is NOT in permanentRxMeds anymore
    permanent_rx_meds = state.get("permanentRxMeds", [])
    perm_match = [m for m in permanent_rx_meds if m.get("medicationName") == med_name]
    if perm_match:
        return False, f"'{med_name}' is still in permanentRxMeds. Expected it to be discontinued."

    # Check that the med IS in discontinuedMeds
    discontinued_meds = state.get("discontinuedMeds", [])
    disc_match = [m for m in discontinued_meds if m.get("medicationName") == med_name]
    if not disc_match:
        return False, f"'{med_name}' not found in discontinuedMeds."

    # Check that a cancel request was created in canceledScripts
    canceled_scripts = state.get("canceledScripts", [])
    cxl_match = [c for c in canceled_scripts if c.get("medicationName") == med_name]
    if not cxl_match:
        return False, f"No entry found in canceledScripts for '{med_name}'. Expected a cancel request to be sent."

    return True, f"'{med_name}' is discontinued and a cancel request was created in canceledScripts."
