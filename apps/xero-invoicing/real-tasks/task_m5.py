import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()

    repeating = state.get("repeatingInvoices", [])
    rep = None
    for r in repeating:
        if r.get("id") == "rep_002":
            rep = r
            break

    if rep is None:
        return False, "Repeating invoice rep_002 (CloudNine Analytics) not found."

    frequency = rep.get("frequency", "")
    if frequency != "quarterly":
        return False, f"Repeating invoice rep_002 frequency is '{frequency}', expected 'quarterly'."

    return True, "CloudNine Analytics repeating invoice frequency changed to quarterly."
