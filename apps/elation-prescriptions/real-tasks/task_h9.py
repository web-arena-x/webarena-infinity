import requests


def verify(server_url: str) -> tuple[bool, str]:
    try:
        resp = requests.get(f"{server_url}/api/state")
        if resp.status_code != 200:
            return False, f"Failed to fetch state: HTTP {resp.status_code}"
        state = resp.json()
    except Exception as e:
        return False, f"Error fetching state: {e}"

    change_requests = state.get("changeRequests", [])

    # Find Atorvastatin change request (cr_001)
    cr_001 = None
    for cr in change_requests:
        if cr.get("id") == "cr_001" or cr.get("originalMedication") == "Atorvastatin 20mg tablet":
            cr_001 = cr
            break

    if cr_001 is None:
        return False, "Atorvastatin change request (cr_001) not found in changeRequests"

    if cr_001.get("status") != "denied":
        return False, f"Atorvastatin change request status is '{cr_001.get('status')}', expected 'denied'"

    deny_reason = cr_001.get("denyReason", "")
    if not deny_reason:
        return False, "Atorvastatin change request denyReason is empty, expected a reason for denial"

    if not cr_001.get("processedBy"):
        return False, "Atorvastatin change request processedBy is not set"

    if not cr_001.get("processedDate"):
        return False, "Atorvastatin change request processedDate is not set"

    # Find Gabapentin change request (cr_002)
    cr_002 = None
    for cr in change_requests:
        if cr.get("id") == "cr_002" or (cr.get("originalMedication") == "Gabapentin 300mg capsule" and cr != cr_001):
            cr_002 = cr
            break

    if cr_002 is None:
        return False, "Gabapentin change request (cr_002) not found in changeRequests"

    if cr_002.get("status") != "denied":
        return False, f"Gabapentin change request status is '{cr_002.get('status')}', expected 'denied'"

    deny_reason_2 = cr_002.get("denyReason", "")
    if not deny_reason_2:
        return False, "Gabapentin change request denyReason is empty, expected a reason for denial"

    if not cr_002.get("processedBy"):
        return False, "Gabapentin change request processedBy is not set"

    if not cr_002.get("processedDate"):
        return False, "Gabapentin change request processedDate is not set"

    return True, "Both change requests denied with reasons, processedBy, and processedDate set"
