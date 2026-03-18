import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    refill_requests = state.get("refillRequests", [])

    rr = next((r for r in refill_requests if r["id"] == "rr_005"), None)
    if not rr:
        return False, "Refill request rr_005 not found."

    if rr.get("status") != "approved":
        return False, f"Refill request rr_005 status is '{rr.get('status')}', expected 'approved'."

    if rr.get("respondedBy") != "prov_001":
        return False, f"Refill request rr_005 respondedBy is '{rr.get('respondedBy')}', expected 'prov_001'."

    prescriptions = state.get("prescriptions", [])
    rx = next((p for p in prescriptions if p["id"] == "rx_016"), None)
    if not rx:
        return False, "Prescription rx_016 (Metoprolol) not found."

    refills_remaining = rx.get("refillsRemaining")
    if refills_remaining != 2:
        return False, f"Prescription rx_016 refillsRemaining is {refills_remaining}, expected 2 (decremented from seed value 3)."

    return True, "Refill request rr_005 is approved by prov_001, and rx_016 refillsRemaining decremented to 2."
