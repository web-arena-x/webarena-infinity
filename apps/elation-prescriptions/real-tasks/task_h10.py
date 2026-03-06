import requests


def verify(server_url: str) -> tuple[bool, str]:
    try:
        resp = requests.get(f"{server_url}/api/state")
        if resp.status_code != 200:
            return False, f"Failed to fetch state: HTTP {resp.status_code}"
        state = resp.json()
    except Exception as e:
        return False, f"Error fetching state: {e}"

    alprazolam_name = "Alprazolam 0.5mg tablet"

    # Check Alprazolam is NOT in permanentRxMeds
    permanent_rx_meds = state.get("permanentRxMeds", [])
    for med in permanent_rx_meds:
        if med.get("medicationName") == alprazolam_name:
            return False, f"'{alprazolam_name}' still found in permanentRxMeds, expected it to be discontinued"

    # Check Alprazolam IS in discontinuedMeds
    discontinued_meds = state.get("discontinuedMeds", [])
    alprazolam_disc = None
    for med in discontinued_meds:
        if med.get("medicationName") == alprazolam_name:
            alprazolam_disc = med
            break

    if alprazolam_disc is None:
        return False, f"'{alprazolam_name}' not found in discontinuedMeds"

    if alprazolam_disc.get("status") != "discontinued":
        return False, f"'{alprazolam_name}' in discontinuedMeds has status '{alprazolam_disc.get('status')}', expected 'discontinued'"

    # Check canceledScripts contains Alprazolam (seed has 2 canceled scripts: cxl_001 and cxl_002)
    canceled_scripts = state.get("canceledScripts", [])
    alprazolam_canceled = None
    for script in canceled_scripts:
        if script.get("medicationName") == alprazolam_name:
            alprazolam_canceled = script
            break

    if alprazolam_canceled is None:
        return False, f"'{alprazolam_name}' not found in canceledScripts, expected a cancellation to be sent to pharmacy"

    return True, "Alprazolam discontinued, moved to discontinuedMeds, and cancellation sent to pharmacy"
