import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify the refill request with urgent pharmacy notes was approved."""
    try:
        resp = requests.get(f"{server_url}/api/state")
        if resp.status_code != 200:
            return False, f"Failed to fetch state: HTTP {resp.status_code}"
        state = resp.json()
    except Exception as e:
        return False, f"Error fetching state: {e}"

    refill_requests = state.get("refillRequests", [])

    # Find the refill request with notes containing 'running low' or 'urgently'
    # This is the Gabapentin refill request (rr_003 in seed)
    urgent_refill = None
    for rr in refill_requests:
        notes = (rr.get("notes") or "").lower()
        if "running low" in notes or "urgently" in notes:
            urgent_refill = rr
            break

    if urgent_refill is None:
        all_notes = [(rr.get("medicationName", ""), rr.get("notes", "")) for rr in refill_requests]
        return False, (
            f"No refill request found with notes containing 'running low' or 'urgently'. "
            f"Refill requests and notes: {all_notes}"
        )

    # Check status is approved
    actual_status = urgent_refill.get("status")
    if actual_status != "approved":
        return False, (
            f"Refill request for '{urgent_refill.get('medicationName')}' with urgent notes "
            f"has status '{actual_status}', expected 'approved'"
        )

    return True, (
        f"Urgent refill request for '{urgent_refill.get('medicationName')}' "
        f"approved successfully. status='{actual_status}', "
        f"notes='{urgent_refill.get('notes')}'."
    )
