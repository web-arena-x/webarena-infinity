import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    refill_requests = state.get("refillRequests", [])

    rr = next((r for r in refill_requests if r["id"] == "rr_010"), None)
    if not rr:
        return False, "Refill request rr_010 not found."

    if rr.get("status") != "approved":
        return False, f"Refill request rr_010 status is '{rr.get('status')}', expected 'approved'."

    prescriptions = state.get("prescriptions", [])
    rx = next((p for p in prescriptions if p["id"] == "rx_024"), None)
    if not rx:
        return False, "Prescription rx_024 (Furosemide) not found."

    refills_remaining = rx.get("refillsRemaining")
    if refills_remaining != 3:
        return False, f"Prescription rx_024 refillsRemaining is {refills_remaining}, expected 3 (decremented from seed value 4)."

    return True, "Refill request rr_010 is approved and rx_024 refillsRemaining decremented to 3."
