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
    change_requests = state.get("changeRequests", [])

    # Build lookup for refill requests by id and name
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
        "rr_004": "Omeprazole 20mg capsule",
        "rr_007": "Sertraline 50mg tablet",
        "rr_008": "Metoprolol Succinate ER 50mg tablet",
    }
    for rr_id, med_name in approved_refills.items():
        req = find_refill(rr_id, med_name)
        if req is None:
            return False, f"Refill request for {med_name} ({rr_id}) not found"
        if req.get("status") != "approved":
            return False, f"Refill for {med_name} status is '{req.get('status')}', expected 'approved'"

    # Check denied refill: Gabapentin
    gabapentin_refill = find_refill("rr_003", "Gabapentin 300mg capsule")
    if gabapentin_refill is None:
        return False, "Gabapentin refill request (rr_003) not found"
    if gabapentin_refill.get("status") != "denied":
        return False, f"Gabapentin refill status is '{gabapentin_refill.get('status')}', expected 'denied'"

    # Check change requests
    cr_by_id = {}
    for cr in change_requests:
        cr_by_id[cr.get("id")] = cr

    # Atorvastatin substitution approved
    cr_001 = cr_by_id.get("cr_001")
    if cr_001 is None:
        # Try by originalMedication
        for cr in change_requests:
            if cr.get("originalMedication") == "Atorvastatin 20mg tablet":
                cr_001 = cr
                break
    if cr_001 is None:
        return False, "Atorvastatin change request (cr_001) not found"
    if cr_001.get("status") != "approved":
        return False, f"Atorvastatin change request status is '{cr_001.get('status')}', expected 'approved'"

    # Gabapentin clarification denied
    cr_002 = cr_by_id.get("cr_002")
    if cr_002 is None:
        for cr in change_requests:
            if cr.get("originalMedication") == "Gabapentin 300mg capsule":
                cr_002 = cr
                break
    if cr_002 is None:
        return False, "Gabapentin change request (cr_002) not found"
    if cr_002.get("status") != "denied":
        return False, f"Gabapentin change request status is '{cr_002.get('status')}', expected 'denied'"

    # Check no pending requests remain
    pending_refills = sum(1 for r in refill_requests if r.get("status") == "pending")
    pending_changes = sum(1 for c in change_requests if c.get("status") == "pending")
    if pending_refills > 0 or pending_changes > 0:
        return False, f"Still have {pending_refills} pending refill(s) and {pending_changes} pending change request(s), expected 0"

    return True, "All pending requests processed: 5 refills approved, Gabapentin refill denied, Atorvastatin substitution approved, Gabapentin clarification denied"
