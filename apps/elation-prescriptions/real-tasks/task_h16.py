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

    # Build lookup
    refill_by_id = {}
    refill_by_name = {}
    for req in refill_requests:
        refill_by_id[req.get("id")] = req
        refill_by_name[req.get("medicationName", "")] = req

    def find_refill(rr_id, med_name):
        return refill_by_id.get(rr_id) or refill_by_name.get(med_name)

    # Check approved refills
    approved_refills = {
        "rr_001": "Lisinopril 10mg tablet",
        "rr_002": "Atorvastatin 20mg tablet",
        "rr_007": "Sertraline 50mg tablet",
    }
    for rr_id, med_name in approved_refills.items():
        req = find_refill(rr_id, med_name)
        if req is None:
            return False, f"Refill request for {med_name} ({rr_id}) not found"
        if req.get("status") != "approved":
            return False, f"Refill for {med_name} status is '{req.get('status')}', expected 'approved'"
        if not req.get("processedBy"):
            return False, f"Refill for {med_name} processedBy is not set"
        if not req.get("processedDate"):
            return False, f"Refill for {med_name} processedDate is not set"

    # Check Gabapentin refill denied
    gabapentin_refill = find_refill("rr_003", "Gabapentin 300mg capsule")
    if gabapentin_refill is None:
        return False, "Gabapentin refill request (rr_003) not found"
    if gabapentin_refill.get("status") != "denied":
        return False, f"Gabapentin refill status is '{gabapentin_refill.get('status')}', expected 'denied'"
    if not gabapentin_refill.get("denyReason"):
        return False, "Gabapentin refill denyReason is empty, expected a reason (needs appointment)"

    return True, "Lisinopril, Atorvastatin, Sertraline refills approved; Gabapentin refill denied with reason"
