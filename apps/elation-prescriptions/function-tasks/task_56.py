import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify Metoprolol refill approved with modified sig."""
    try:
        resp = requests.get(f"{server_url}/api/state")
        if resp.status_code != 200:
            return False, f"Failed to fetch state: HTTP {resp.status_code}"
        state = resp.json()
    except Exception as e:
        return False, f"Error fetching state: {e}"

    target_name = "Metoprolol Succinate ER 50mg tablet"
    expected_sig = "Take 1 tablet by mouth once daily in the morning"
    errors = []

    # Check refillRequests entry for Metoprolol has status approved
    refill_requests = state.get("refillRequests", [])
    metoprolol_refill = None
    for rr in refill_requests:
        if rr.get("medicationName") == target_name:
            metoprolol_refill = rr
            break

    if metoprolol_refill is None:
        rr_names = [rr.get("medicationName", "") for rr in refill_requests]
        return False, (
            f"No refill request found for '{target_name}'. "
            f"Refill request medications: {rr_names}"
        )

    actual_status = metoprolol_refill.get("status")
    if actual_status != "approved":
        errors.append(
            f"Refill request status: expected 'approved', got '{actual_status}'"
        )

    # Check the medication in permanentRxMeds has the updated sig
    permanent_rx_meds = state.get("permanentRxMeds", [])
    metoprolol_med = None
    for med in permanent_rx_meds:
        if med.get("medicationName") == target_name:
            metoprolol_med = med
            break

    if metoprolol_med is None:
        errors.append(
            f"'{target_name}' not found in permanentRxMeds"
        )
    else:
        actual_sig = metoprolol_med.get("sig")
        if actual_sig != expected_sig:
            errors.append(
                f"Medication sig: expected '{expected_sig}', got '{actual_sig}'"
            )

    if errors:
        return False, (
            f"Metoprolol refill approval with modified sig issues: {'; '.join(errors)}"
        )

    return True, (
        f"Metoprolol refill approved with modified sig. "
        f"Refill request status='approved', "
        f"medication sig updated to '{expected_sig}'."
    )
