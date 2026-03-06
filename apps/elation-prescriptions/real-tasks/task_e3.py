import requests


def verify(server_url: str) -> tuple[bool, str]:
    try:
        resp = requests.get(f"{server_url}/api/state")
        if resp.status_code != 200:
            return False, f"Failed to fetch state: HTTP {resp.status_code}"
        state = resp.json()
    except Exception as e:
        return False, f"Error fetching state: {e}"

    # Find the Atorvastatin-to-Rosuvastatin change request
    change_requests = state.get("changeRequests", [])
    atorvastatin_request = None
    for req in change_requests:
        if req.get("originalMedication") == "Atorvastatin 20mg tablet":
            atorvastatin_request = req
            break

    if atorvastatin_request is None:
        return False, "Change request for originalMedication 'Atorvastatin 20mg tablet' not found in changeRequests"

    if atorvastatin_request.get("status") != "approved":
        return False, f"Atorvastatin substitution request status is '{atorvastatin_request.get('status')}', expected 'approved'"

    if not atorvastatin_request.get("processedBy"):
        return False, "Atorvastatin substitution request processedBy is not set"

    if not atorvastatin_request.get("processedDate"):
        return False, "Atorvastatin substitution request processedDate is not set"

    return True, "Atorvastatin-to-Rosuvastatin substitution request approved successfully"
