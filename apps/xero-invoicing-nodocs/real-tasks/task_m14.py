import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Update DataFlow Analytics Inc's tax ID to US-95-7654321."""
    try:
        resp = requests.get(f"{server_url}/api/state")
        if resp.status_code != 200:
            return False, f"Failed to fetch state: HTTP {resp.status_code}"
        state = resp.json()
    except Exception as e:
        return False, f"Error fetching state: {e}"

    contacts = state.get("contacts", [])
    target = None
    for c in contacts:
        if c.get("id") == "con_11" or c.get("name") == "DataFlow Analytics Inc":
            target = c
            break

    if target is None:
        return False, "Contact 'DataFlow Analytics Inc' not found in state"

    tax_id = target.get("taxId")
    if tax_id == "US-95-7654321":
        return True, "DataFlow Analytics Inc tax ID has been updated to US-95-7654321"
    else:
        return False, f"DataFlow Analytics Inc taxId is '{tax_id}', expected 'US-95-7654321'"
