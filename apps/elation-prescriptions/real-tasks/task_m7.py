import requests


def verify(server_url: str) -> tuple[bool, str]:
    try:
        resp = requests.get(f"{server_url}/api/state")
        if resp.status_code != 200:
            return False, f"Failed to fetch state: HTTP {resp.status_code}"
        state = resp.json()
    except Exception as e:
        return False, f"Error fetching state: {e}"

    # Find the Lisinopril refill request
    refill_requests = state.get("refillRequests", [])
    lisinopril_refill = None
    for req in refill_requests:
        if req.get("medicationName") == "Lisinopril 10mg tablet":
            lisinopril_refill = req
            break

    if lisinopril_refill is None:
        return False, "Lisinopril 10mg tablet refill request not found in refillRequests"

    if lisinopril_refill.get("status") != "denied":
        return False, f"Lisinopril refill status is '{lisinopril_refill.get('status')}', expected 'denied'"

    if not lisinopril_refill.get("processedBy"):
        return False, "Lisinopril refill processedBy is not set"

    if not lisinopril_refill.get("processedDate"):
        return False, "Lisinopril refill processedDate is not set"

    deny_reason = lisinopril_refill.get("denyReason", "")
    if not deny_reason:
        return False, "Lisinopril refill denyReason is empty or not set"

    return True, "Lisinopril refill denied successfully with reason provided"
