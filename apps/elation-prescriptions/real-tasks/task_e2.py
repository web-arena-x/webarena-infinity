import requests


def verify(server_url: str) -> tuple[bool, str]:
    try:
        resp = requests.get(f"{server_url}/api/state")
        if resp.status_code != 200:
            return False, f"Failed to fetch state: HTTP {resp.status_code}"
        state = resp.json()
    except Exception as e:
        return False, f"Error fetching state: {e}"

    # Find the Omeprazole refill request
    refill_requests = state.get("refillRequests", [])
    omeprazole_refill = None
    for req in refill_requests:
        if req.get("medicationName") == "Omeprazole 20mg capsule":
            omeprazole_refill = req
            break

    if omeprazole_refill is None:
        return False, "Omeprazole 20mg capsule refill request not found in refillRequests"

    if omeprazole_refill.get("status") != "denied":
        return False, f"Omeprazole refill status is '{omeprazole_refill.get('status')}', expected 'denied'"

    if not omeprazole_refill.get("processedBy"):
        return False, "Omeprazole refill processedBy is not set"

    if not omeprazole_refill.get("processedDate"):
        return False, "Omeprazole refill processedDate is not set"

    deny_reason = omeprazole_refill.get("denyReason", "")
    if not deny_reason or not str(deny_reason).strip():
        return False, "Omeprazole refill denyReason is not set or is empty"

    return True, "Omeprazole refill request denied successfully with reason provided"
