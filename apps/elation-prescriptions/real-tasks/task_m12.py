import requests


def verify(server_url: str) -> tuple[bool, str]:
    try:
        resp = requests.get(f"{server_url}/api/state")
        if resp.status_code != 200:
            return False, f"Failed to fetch state: HTTP {resp.status_code}"
        state = resp.json()
    except Exception as e:
        return False, f"Error fetching state: {e}"

    # Find the Atorvastatin refill request
    refill_requests = state.get("refillRequests", [])
    atorvastatin_refill = None
    for req in refill_requests:
        if req.get("medicationName") == "Atorvastatin 20mg tablet":
            atorvastatin_refill = req
            break

    if atorvastatin_refill is None:
        return False, "Atorvastatin 20mg tablet refill request not found in refillRequests"

    if atorvastatin_refill.get("status") != "denied":
        return False, f"Atorvastatin refill status is '{atorvastatin_refill.get('status')}', expected 'denied'"

    if not atorvastatin_refill.get("processedBy"):
        return False, "Atorvastatin refill processedBy is not set"

    if not atorvastatin_refill.get("processedDate"):
        return False, "Atorvastatin refill processedDate is not set"

    deny_reason = atorvastatin_refill.get("denyReason", "")
    if not deny_reason:
        return False, "Atorvastatin refill denyReason is empty or not set"

    return True, "Atorvastatin refill denied successfully with reason provided"
