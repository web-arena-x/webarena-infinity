import requests


def verify(server_url: str) -> tuple[bool, str]:
    """End-of-day: approve William refill, deny David refill, hold Margaret Semaglutide, renew Sertraline 6."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    errors = []

    # rr_010: William's Furosemide refill approved
    rr_010 = next((r for r in state["refillRequests"] if r["id"] == "rr_010"), None)
    if not rr_010:
        errors.append("Refill request rr_010 not found.")
    elif rr_010.get("status") != "approved":
        errors.append(f"Expected rr_010 (Furosemide) status 'approved', got '{rr_010.get('status')}'.")

    # rr_005: David's Metoprolol refill denied
    rr_005 = next((r for r in state["refillRequests"] if r["id"] == "rr_005"), None)
    if not rr_005:
        errors.append("Refill request rr_005 not found.")
    elif rr_005.get("status") != "denied":
        errors.append(f"Expected rr_005 (Metoprolol) status 'denied', got '{rr_005.get('status')}'.")

    # rx_030: Margaret's Semaglutide on hold
    rx_030 = next((rx for rx in state["prescriptions"] if rx["id"] == "rx_030"), None)
    if not rx_030:
        errors.append("Prescription rx_030 (Semaglutide) not found.")
    elif rx_030.get("status") != "on-hold":
        errors.append(f"Expected rx_030 status 'on-hold', got '{rx_030.get('status')}'.")

    # rx_013: Margaret's Sertraline renewed with 6
    rx_013 = next((rx for rx in state["prescriptions"] if rx["id"] == "rx_013"), None)
    if not rx_013:
        errors.append("Prescription rx_013 (Sertraline) not found.")
    else:
        if rx_013.get("refillsRemaining", 0) < 6:
            errors.append(f"Expected rx_013 refillsRemaining >= 6, got {rx_013.get('refillsRemaining')}.")

    if errors:
        return False, " ".join(errors)
    return True, "End-of-day tasks completed: refills processed, Semaglutide on hold, Sertraline renewed."
