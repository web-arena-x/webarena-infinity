import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    repeating = state.get("repeatingInvoices", [])

    summit = next((ri for ri in repeating if ri.get("id") == "rep_005"), None)
    if summit is not None:
        return False, f"Repeating invoice rep_005 (Summit Health Group) still exists in repeatingInvoices (status: {summit.get('status')})."

    return True, "Repeating invoice rep_005 (Summit Health Group) has been deleted successfully."
