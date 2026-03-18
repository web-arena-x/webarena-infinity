import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    refill_requests = state.get("refillRequests", [])

    rr = next((r for r in refill_requests if r["id"] == "rr_001"), None)
    if not rr:
        return False, "Refill request rr_001 not found."

    if rr.get("status") != "approved":
        return False, f"Refill request rr_001 status is '{rr.get('status')}', expected 'approved'."

    if rr.get("respondedBy") != "prov_001":
        return False, f"Refill request rr_001 respondedBy is '{rr.get('respondedBy')}', expected 'prov_001'."

    prescriptions = state.get("prescriptions", [])
    rx = next((p for p in prescriptions if p["id"] == "rx_001"), None)
    if not rx:
        return False, "Prescription rx_001 (Atorvastatin) not found."

    refills_remaining = rx.get("refillsRemaining")
    if refills_remaining != 1:
        return False, f"Prescription rx_001 refillsRemaining is {refills_remaining}, expected 1 (decremented from seed value 2)."

    fill_history = rx.get("fillHistory", [])
    # Seed has 2 fill history entries; after approval there should be at least 3
    if len(fill_history) < 3:
        return False, f"Prescription rx_001 fillHistory has {len(fill_history)} entries, expected at least 3 (a new entry after approval)."

    return True, "Refill request rr_001 is approved by prov_001, rx_001 refillsRemaining decremented to 1, and a new fill history entry exists."
