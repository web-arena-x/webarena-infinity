import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Hold Gabapentin and nasal spray, approve Atorvastatin refill."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    errors = []

    # rx_007 Gabapentin -> on-hold
    rx_007 = next((r for r in state["prescriptions"] if r["id"] == "rx_007"), None)
    if not rx_007:
        errors.append("Prescription rx_007 (Gabapentin) not found.")
    else:
        if rx_007.get("status") != "on-hold":
            errors.append(f"Expected rx_007 (Gabapentin) status 'on-hold', got '{rx_007.get('status')}'.")

    # rx_008 Fluticasone Nasal -> on-hold
    rx_008 = next((r for r in state["prescriptions"] if r["id"] == "rx_008"), None)
    if not rx_008:
        errors.append("Prescription rx_008 (Fluticasone Nasal) not found.")
    else:
        if rx_008.get("status") != "on-hold":
            errors.append(f"Expected rx_008 (Fluticasone Nasal) status 'on-hold', got '{rx_008.get('status')}'.")

    # rr_001 Atorvastatin refill -> approved
    rr_001 = next((r for r in state["refillRequests"] if r["id"] == "rr_001"), None)
    if not rr_001:
        errors.append("Refill request rr_001 not found.")
    else:
        if rr_001.get("status") != "approved":
            errors.append(f"Expected rr_001 (Atorvastatin refill) status 'approved', got '{rr_001.get('status')}'.")

    if errors:
        return False, " ".join(errors)
    return True, "Gabapentin and nasal spray on hold, Atorvastatin refill approved."
