import requests


def verify(server_url: str) -> tuple[bool, str]:
    try:
        resp = requests.get(f"{server_url}/api/state")
        if resp.status_code != 200:
            return False, f"Failed to fetch state: HTTP {resp.status_code}"
        state = resp.json()
    except Exception as e:
        return False, f"Error fetching state: {e}"

    # Check Gabapentin refill request is approved
    refill_requests = state.get("refillRequests", [])
    gabapentin_refill = None
    for req in refill_requests:
        if req.get("medicationName") == "Gabapentin 300mg capsule":
            gabapentin_refill = req
            break

    if gabapentin_refill is None:
        return False, "Gabapentin 300mg capsule refill request not found in refillRequests"

    if gabapentin_refill.get("status") != "approved":
        return False, f"Gabapentin refill status is '{gabapentin_refill.get('status')}', expected 'approved'"

    if not gabapentin_refill.get("processedBy"):
        return False, "Gabapentin refill processedBy is not set"

    if not gabapentin_refill.get("processedDate"):
        return False, "Gabapentin refill processedDate is not set"

    # Check modifications has sig containing "twice daily"
    modifications = gabapentin_refill.get("modifications", {})
    if not modifications:
        return False, "Gabapentin refill has no modifications recorded"

    mod_sig = modifications.get("sig", "")
    if "twice daily" not in mod_sig.lower():
        return False, f"Gabapentin refill modification sig is '{mod_sig}', expected it to contain 'twice daily'"

    # Check permanentRxMeds Gabapentin sig was updated to contain "twice daily"
    permanent_rx_meds = state.get("permanentRxMeds", [])
    gabapentin_med = None
    for med in permanent_rx_meds:
        if med.get("medicationName") == "Gabapentin 300mg capsule":
            gabapentin_med = med
            break

    if gabapentin_med is None:
        return False, "Gabapentin 300mg capsule not found in permanentRxMeds"

    med_sig = gabapentin_med.get("sig", "")
    if "twice daily" not in med_sig.lower():
        return False, f"Gabapentin in permanentRxMeds has sig '{med_sig}', expected it to contain 'twice daily'"

    return True, "Gabapentin refill approved with sig changed to twice daily"
