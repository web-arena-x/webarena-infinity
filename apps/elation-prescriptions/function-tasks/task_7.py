import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Verify that the change request for Atorvastatin to Rosuvastatin substitution was approved."""
    try:
        resp = requests.get(f"{server_url}/api/state")
        if resp.status_code != 200:
            return False, f"Failed to fetch state: HTTP {resp.status_code}"
        state = resp.json()
    except Exception as e:
        return False, f"Error fetching state: {e}"

    # Check changeRequests for original medication Atorvastatin 20mg tablet
    change_requests = state.get("changeRequests", [])
    atorvastatin_change = None
    for cr in change_requests:
        if cr.get("originalMedication") == "Atorvastatin 20mg tablet":
            atorvastatin_change = cr
            break

    if atorvastatin_change is None:
        return False, "No change request found with originalMedication='Atorvastatin 20mg tablet'"

    # Check status is approved
    status = atorvastatin_change.get("status")
    if status != "approved":
        return False, f"Change request status is '{status}', expected 'approved'"

    # Check processedBy is set
    processed_by = atorvastatin_change.get("processedBy")
    if not processed_by:
        return False, "Change request processedBy is not set"

    return True, (
        f"Atorvastatin to Rosuvastatin change request approved successfully. "
        f"processedBy='{processed_by}'"
    )
