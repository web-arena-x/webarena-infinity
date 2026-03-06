import requests


def verify(server_url: str) -> tuple[bool, str]:
    try:
        resp = requests.get(f"{server_url}/api/state")
        if resp.status_code != 200:
            return False, f"Failed to fetch state: HTTP {resp.status_code}"
        state = resp.json()
    except Exception as e:
        return False, f"Error fetching state: {e}"

    # Find the Gabapentin sig clarification change request
    change_requests = state.get("changeRequests", [])
    gabapentin_request = None
    for req in change_requests:
        if req.get("medicationName") == "Gabapentin 300mg capsule":
            gabapentin_request = req
            break

    if gabapentin_request is None:
        return False, "Change request for medicationName 'Gabapentin 300mg capsule' not found in changeRequests"

    if gabapentin_request.get("status") != "denied":
        return False, f"Gabapentin change request status is '{gabapentin_request.get('status')}', expected 'denied'"

    if not gabapentin_request.get("processedBy"):
        return False, "Gabapentin change request processedBy is not set"

    if not gabapentin_request.get("processedDate"):
        return False, "Gabapentin change request processedDate is not set"

    deny_reason = gabapentin_request.get("denyReason", "")
    if not deny_reason or not str(deny_reason).strip():
        return False, "Gabapentin change request denyReason is not set or is empty"

    return True, "Gabapentin sig clarification change request denied successfully with reason provided"
