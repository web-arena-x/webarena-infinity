import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Margaret's Pantoprazole: deny urgent refill, put prescription on hold."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    errors = []

    # rr_003 Pantoprazole refill -> denied
    rr_003 = next((r for r in state["refillRequests"] if r["id"] == "rr_003"), None)
    if not rr_003:
        errors.append("Refill request rr_003 not found.")
    else:
        if rr_003.get("status") != "denied":
            errors.append(f"Expected rr_003 (Pantoprazole refill) status 'denied', got '{rr_003.get('status')}'.")
        elif "gi consult" not in rr_003.get("denyReason", "").lower():
            errors.append(f"Expected rr_003 denyReason to mention 'GI consult', got '{rr_003.get('denyReason')}'.")

    # rx_005 Pantoprazole -> on-hold
    rx_005 = next((r for r in state["prescriptions"] if r["id"] == "rx_005"), None)
    if not rx_005:
        errors.append("Prescription rx_005 (Pantoprazole) not found.")
    else:
        if rx_005.get("status") != "on-hold":
            errors.append(f"Expected rx_005 (Pantoprazole) status 'on-hold', got '{rx_005.get('status')}'.")

    if errors:
        return False, " ".join(errors)
    return True, "Pantoprazole refill denied and prescription placed on hold."
