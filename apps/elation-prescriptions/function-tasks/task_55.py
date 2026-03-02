import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify Sertraline 50mg tablet discontinued and cancel request sent."""
    try:
        resp = requests.get(f"{server_url}/api/state")
        if resp.status_code != 200:
            return False, f"Failed to fetch state: HTTP {resp.status_code}"
        state = resp.json()
    except Exception as e:
        return False, f"Error fetching state: {e}"

    target_name = "Sertraline 50mg tablet"
    errors = []

    # Check Sertraline 50mg is NOT in permanentRxMeds
    permanent_rx_meds = state.get("permanentRxMeds", [])
    sertraline_in_rx = [
        m for m in permanent_rx_meds
        if m.get("medicationName") == target_name
    ]

    if sertraline_in_rx:
        errors.append(
            f"'{target_name}' still exists in permanentRxMeds, expected it to be removed"
        )

    # Check Sertraline 50mg IS in discontinuedMeds
    discontinued_meds = state.get("discontinuedMeds", [])
    sertraline_in_disc = [
        m for m in discontinued_meds
        if m.get("medicationName") == target_name
    ]

    if not sertraline_in_disc:
        disc_names = [m.get("medicationName", "") for m in discontinued_meds]
        errors.append(
            f"'{target_name}' not found in discontinuedMeds. "
            f"Current discontinuedMeds: {disc_names}"
        )

    # Check canceledScripts contains Sertraline 50mg
    canceled_scripts = state.get("canceledScripts", [])
    sertraline_canceled = [
        c for c in canceled_scripts
        if c.get("medicationName") == target_name
    ]

    if not sertraline_canceled:
        canceled_names = [c.get("medicationName", "") for c in canceled_scripts]
        errors.append(
            f"'{target_name}' not found in canceledScripts. "
            f"Current canceledScripts: {canceled_names}"
        )

    if errors:
        return False, (
            f"Sertraline discontinuation issues: {'; '.join(errors)}"
        )

    return True, (
        f"'{target_name}' successfully discontinued and cancel request sent. "
        f"Removed from permanentRxMeds, present in discontinuedMeds and canceledScripts."
    )
