import requests


def verify(server_url: str) -> tuple[bool, str]:
    try:
        resp = requests.get(f"{server_url}/api/state")
        if resp.status_code != 200:
            return False, f"Failed to fetch state: HTTP {resp.status_code}"
        state = resp.json()
    except Exception as e:
        return False, f"Error fetching state: {e}"

    refill_requests = state.get("refillRequests", [])

    pending_refill_ids = ["rr_001", "rr_002", "rr_003", "rr_004", "rr_007", "rr_008"]
    pending_refill_names = {
        "rr_001": "Lisinopril 10mg tablet",
        "rr_002": "Atorvastatin 20mg tablet",
        "rr_003": "Gabapentin 300mg capsule",
        "rr_004": "Omeprazole 20mg capsule",
        "rr_007": "Sertraline 50mg tablet",
        "rr_008": "Metoprolol Succinate ER 50mg tablet",
    }

    for rr_id in pending_refill_ids:
        found = None
        for req in refill_requests:
            if req.get("id") == rr_id:
                found = req
                break
        if found is None:
            # Try matching by medication name
            name = pending_refill_names[rr_id]
            for req in refill_requests:
                if req.get("medicationName") == name:
                    found = req
                    break
        if found is None:
            return False, f"Refill request {rr_id} ({pending_refill_names[rr_id]}) not found in refillRequests"
        if found.get("status") != "approved":
            return False, f"Refill request {rr_id} ({pending_refill_names[rr_id]}) status is '{found.get('status')}', expected 'approved'"
        if not found.get("processedBy"):
            return False, f"Refill request {rr_id} ({pending_refill_names[rr_id]}) processedBy is not set"

    # Check no pending refill requests remain
    pending_count = sum(1 for req in refill_requests if req.get("status") == "pending")
    if pending_count > 0:
        return False, f"Found {pending_count} refill request(s) still with status 'pending', expected 0"

    return True, "All 6 pending refill requests approved successfully with no pending requests remaining"
