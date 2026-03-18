import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Process Margaret's pending refills: approve urgent, deny all routine."""
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    errors = []

    # rr_003 (Pantoprazole, urgent) -> approved
    rr_003 = next((r for r in state["refillRequests"] if r["id"] == "rr_003"), None)
    if not rr_003:
        errors.append("Refill request rr_003 not found.")
    else:
        if rr_003.get("status") != "approved":
            errors.append(f"Expected rr_003 (Pantoprazole, urgent) status 'approved', got '{rr_003.get('status')}'.")

    # rr_001 (Atorvastatin, routine) -> denied
    rr_001 = next((r for r in state["refillRequests"] if r["id"] == "rr_001"), None)
    if not rr_001:
        errors.append("Refill request rr_001 not found.")
    else:
        if rr_001.get("status") != "denied":
            errors.append(f"Expected rr_001 (Atorvastatin, routine) status 'denied', got '{rr_001.get('status')}'.")

    # rr_002 (Metformin, routine) -> denied
    rr_002 = next((r for r in state["refillRequests"] if r["id"] == "rr_002"), None)
    if not rr_002:
        errors.append("Refill request rr_002 not found.")
    else:
        if rr_002.get("status") != "denied":
            errors.append(f"Expected rr_002 (Metformin, routine) status 'denied', got '{rr_002.get('status')}'.")

    # rr_011 (Sertraline, routine) -> denied
    rr_011 = next((r for r in state["refillRequests"] if r["id"] == "rr_011"), None)
    if not rr_011:
        errors.append("Refill request rr_011 not found.")
    else:
        if rr_011.get("status") != "denied":
            errors.append(f"Expected rr_011 (Sertraline, routine) status 'denied', got '{rr_011.get('status')}'.")

    if errors:
        return False, " ".join(errors)
    return True, "All Margaret's pending refills processed: urgent approved, routine denied."
