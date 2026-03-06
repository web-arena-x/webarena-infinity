import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    quote = next((q for q in state.get("quotes", []) if q.get("number") == "QU-0028"), None)
    if quote is None:
        return False, "Quote QU-0028 not found."

    if quote.get("status") != "declined":
        return False, f"Expected quote QU-0028 status to be 'declined', got '{quote.get('status')}'."

    return True, "Quote QU-0028 (Metro Fabrication Works) has been declined successfully."
