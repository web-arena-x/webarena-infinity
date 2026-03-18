import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    refill_requests = state.get("refillRequests", [])

    rr = next((r for r in refill_requests if r["id"] == "rr_011"), None)
    if not rr:
        return False, "Refill request rr_011 not found."

    if rr.get("status") != "denied":
        return False, f"Refill request rr_011 status is '{rr.get('status')}', expected 'denied'."

    deny_reason = rr.get("denyReason") or ""
    if "Changed therapy" not in deny_reason:
        return False, f"Refill request rr_011 denyReason is '{deny_reason}', expected it to contain 'Changed therapy'."

    return True, "Refill request rr_011 is denied with reason containing 'Changed therapy'."
