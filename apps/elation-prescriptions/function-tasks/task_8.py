import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify that the change request for Gabapentin sig clarification was denied with the correct reason."""
    try:
        resp = requests.get(f"{server_url}/api/state")
        if resp.status_code != 200:
            return False, f"Failed to fetch state: HTTP {resp.status_code}"
        state = resp.json()
    except Exception as e:
        return False, f"Error fetching state: {e}"

    # Check changeRequests for Gabapentin 300mg capsule
    change_requests = state.get("changeRequests", [])
    gabapentin_change = None
    for cr in change_requests:
        if cr.get("medicationName") == "Gabapentin 300mg capsule":
            gabapentin_change = cr
            break

    if gabapentin_change is None:
        return False, "No change request found with medicationName='Gabapentin 300mg capsule'"

    # Check status is denied
    status = gabapentin_change.get("status")
    if status != "denied":
        return False, f"Change request status is '{status}', expected 'denied'"

    # Check denyReason matches exactly
    expected_reason = "Current sig is correct as written"
    deny_reason = gabapentin_change.get("denyReason", "")
    if deny_reason != expected_reason:
        return False, f"denyReason is '{deny_reason}', expected '{expected_reason}'"

    return True, (
        f"Gabapentin sig clarification change request denied successfully with "
        f"denyReason='{deny_reason}'"
    )
