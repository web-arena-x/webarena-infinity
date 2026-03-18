import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Differentiated refill processing: approve urgent, modify Metformin, deny Sertraline, leave Atorvastatin."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    errors = []

    # rr_003 (Pantoprazole, urgent) -> approved
    rr_003 = next((r for r in state["refillRequests"] if r["id"] == "rr_003"), None)
    if not rr_003:
        errors.append("Refill request rr_003 not found.")
    elif rr_003.get("status") != "approved":
        errors.append(f"Expected rr_003 (Pantoprazole, urgent) status 'approved', got '{rr_003.get('status')}'.")

    # rr_002 (Metformin) -> modified
    rr_002 = next((r for r in state["refillRequests"] if r["id"] == "rr_002"), None)
    if not rr_002:
        errors.append("Refill request rr_002 not found.")
    elif rr_002.get("status") != "modified":
        errors.append(f"Expected rr_002 (Metformin) status 'modified', got '{rr_002.get('status')}'.")
    elif not rr_002.get("modifiedDetails"):
        errors.append("Expected rr_002 to have modifiedDetails, but it is empty.")

    # rr_011 (Sertraline) -> denied
    rr_011 = next((r for r in state["refillRequests"] if r["id"] == "rr_011"), None)
    if not rr_011:
        errors.append("Refill request rr_011 not found.")
    elif rr_011.get("status") != "denied":
        errors.append(f"Expected rr_011 (Sertraline) status 'denied', got '{rr_011.get('status')}'.")

    # rr_001 (Atorvastatin) -> still pending
    rr_001 = next((r for r in state["refillRequests"] if r["id"] == "rr_001"), None)
    if not rr_001:
        errors.append("Refill request rr_001 not found.")
    elif rr_001.get("status") != "pending":
        errors.append(f"Expected rr_001 (Atorvastatin) status 'pending', got '{rr_001.get('status')}'.")

    if errors:
        return False, " ".join(errors)
    return True, "Refills processed correctly: urgent approved, Metformin modified, Sertraline denied, Atorvastatin left pending."
