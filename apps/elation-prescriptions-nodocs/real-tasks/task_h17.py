import requests


def verify(server_url: str) -> tuple[bool, str]:
    """All pending refills: approve urgent, deny routine."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    errors = []

    # Urgent pending -> approved
    for rr_id in ["rr_003", "rr_010"]:
        rr = next((r for r in state["refillRequests"] if r["id"] == rr_id), None)
        if not rr:
            errors.append(f"Refill request {rr_id} not found.")
        elif rr.get("status") != "approved":
            errors.append(f"Expected {rr_id} status 'approved', got '{rr.get('status')}'.")

    # Routine pending -> denied
    for rr_id in ["rr_001", "rr_002", "rr_005", "rr_007", "rr_011"]:
        rr = next((r for r in state["refillRequests"] if r["id"] == rr_id), None)
        if not rr:
            errors.append(f"Refill request {rr_id} not found.")
        elif rr.get("status") != "denied":
            errors.append(f"Expected {rr_id} status 'denied', got '{rr.get('status')}'.")

    if errors:
        return False, " ".join(errors)
    return True, "All pending refills processed: urgent approved, routine denied."
