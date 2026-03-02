import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify that the pending refill request for Sertraline 50mg tablet was denied with the correct reason."""
    try:
        resp = requests.get(f"{server_url}/api/state")
        if resp.status_code != 200:
            return False, f"Failed to fetch state: HTTP {resp.status_code}"
        state = resp.json()
    except Exception as e:
        return False, f"Error fetching state: {e}"

    # Check refillRequests for Sertraline 50mg tablet
    refill_requests = state.get("refillRequests", [])
    sertraline_refill = None
    for rr in refill_requests:
        if rr.get("medicationName") == "Sertraline 50mg tablet":
            sertraline_refill = rr
            break

    if sertraline_refill is None:
        return False, "No refill request found with medicationName='Sertraline 50mg tablet'"

    # Check status is denied
    status = sertraline_refill.get("status")
    if status != "denied":
        return False, f"Refill request status is '{status}', expected 'denied'"

    # Check denyReason matches exactly
    expected_reason = "Requires follow-up appointment"
    deny_reason = sertraline_refill.get("denyReason", "")
    if deny_reason != expected_reason:
        return False, f"denyReason is '{deny_reason}', expected '{expected_reason}'"

    return True, (
        f"Sertraline 50mg tablet refill request denied successfully with "
        f"denyReason='{deny_reason}'"
    )
