import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    quote = next((q for q in state.get("quotes", []) if q.get("number") == "QU-0026"), None)
    if quote is None:
        return False, "Quote QU-0026 not found in state (may have been fully removed)."

    if quote.get("status") != "deleted":
        return False, f"Expected quote QU-0026 status to be 'deleted', got '{quote.get('status')}'."

    return True, "Quote QU-0026 (Horizon Media) has been deleted successfully."
