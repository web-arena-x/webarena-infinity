import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify the therapeutic substitution change request was approved."""
    try:
        resp = requests.get(f"{server_url}/api/state")
        if resp.status_code != 200:
            return False, f"Failed to fetch state: HTTP {resp.status_code}"
        state = resp.json()
    except Exception as e:
        return False, f"Error fetching state: {e}"

    change_requests = state.get("changeRequests", [])

    # Find the change request proposing therapeutic substitution
    # This is cr_001: Atorvastatin -> Rosuvastatin
    # Look for one where reason contains 'substitution' OR where
    # requestedMedication differs from originalMedication
    substitution_cr = None
    for cr in change_requests:
        reason = (cr.get("reason") or "").lower()
        original = cr.get("originalMedication", "")
        requested = cr.get("requestedMedication", "")

        if "substitution" in reason or (original and requested and original != requested):
            substitution_cr = cr
            break

    if substitution_cr is None:
        all_crs = [
            {
                "reason": cr.get("reason", ""),
                "originalMedication": cr.get("originalMedication", ""),
                "requestedMedication": cr.get("requestedMedication", ""),
                "status": cr.get("status", ""),
            }
            for cr in change_requests
        ]
        return False, (
            f"No change request found with therapeutic substitution "
            f"(reason containing 'substitution' or different original/requested medication). "
            f"Change requests: {all_crs}"
        )

    # Check status is approved
    actual_status = substitution_cr.get("status")
    if actual_status != "approved":
        return False, (
            f"Therapeutic substitution change request "
            f"('{substitution_cr.get('originalMedication')}' -> "
            f"'{substitution_cr.get('requestedMedication')}') "
            f"has status '{actual_status}', expected 'approved'"
        )

    return True, (
        f"Therapeutic substitution change request approved. "
        f"'{substitution_cr.get('originalMedication')}' -> "
        f"'{substitution_cr.get('requestedMedication')}', "
        f"status='{actual_status}', reason='{substitution_cr.get('reason')}'."
    )
