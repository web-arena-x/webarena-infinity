import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    refill_requests = state.get("refillRequests", [])

    rr = next((r for r in refill_requests if r["id"] == "rr_003"), None)
    if not rr:
        return False, "Refill request rr_003 not found."

    if rr.get("status") != "modified":
        return False, f"Refill request rr_003 status is '{rr.get('status')}', expected 'modified'."

    modified_details = rr.get("modifiedDetails") or ""
    if "Changed to 20mg from 40mg" not in modified_details:
        return False, f"Refill request rr_003 modifiedDetails is '{modified_details}', expected it to contain 'Changed to 20mg from 40mg'."

    return True, "Refill request rr_003 is modified with details containing 'Changed to 20mg from 40mg'."
