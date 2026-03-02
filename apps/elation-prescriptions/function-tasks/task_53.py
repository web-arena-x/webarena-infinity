import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify the only active controlled substance was discontinued and cancel request sent."""
    try:
        resp = requests.get(f"{server_url}/api/state")
        if resp.status_code != 200:
            return False, f"Failed to fetch state: HTTP {resp.status_code}"
        state = resp.json()
    except Exception as e:
        return False, f"Error fetching state: {e}"

    errors = []

    # Check no controlled substance in any active med list
    active_lists = [
        ("permanentRxMeds", state.get("permanentRxMeds", [])),
        ("permanentOtcMeds", state.get("permanentOtcMeds", [])),
        ("temporaryMeds", state.get("temporaryMeds", [])),
    ]

    for list_name, meds in active_lists:
        controlled_in_list = [
            m.get("medicationName") for m in meds
            if m.get("isControlled") is True
        ]
        if controlled_in_list:
            errors.append(
                f"Controlled substance(s) still in {list_name}: {controlled_in_list}"
            )

    # Check Alprazolam is in discontinuedMeds
    discontinued_meds = state.get("discontinuedMeds", [])
    alprazolam_in_disc = [
        m for m in discontinued_meds
        if "Alprazolam" in m.get("medicationName", "")
    ]

    if not alprazolam_in_disc:
        disc_names = [m.get("medicationName", "") for m in discontinued_meds]
        errors.append(
            f"'Alprazolam 0.5mg tablet' not found in discontinuedMeds. "
            f"Current discontinuedMeds: {disc_names}"
        )

    # Check canceledScripts contains Alprazolam
    canceled_scripts = state.get("canceledScripts", [])
    alprazolam_canceled = [
        c for c in canceled_scripts
        if "Alprazolam" in c.get("medicationName", "")
    ]

    if not alprazolam_canceled:
        canceled_names = [c.get("medicationName", "") for c in canceled_scripts]
        errors.append(
            f"No cancel request for Alprazolam found in canceledScripts. "
            f"Current canceledScripts: {canceled_names}"
        )

    if errors:
        return False, (
            f"Controlled substance discontinuation issues: {'; '.join(errors)}"
        )

    return True, (
        f"Controlled substance (Alprazolam 0.5mg tablet) successfully discontinued and "
        f"cancel request sent. Found in discontinuedMeds and canceledScripts. "
        f"No controlled substances remain in active medication lists."
    )
