import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    presentations = state.get("presentations", [])
    for pres in presentations:
        if pres.get("title") == "Q4 2025 Revenue Analysis":
            if pres.get("status") == "archived":
                return True, "Presentation 'Q4 2025 Revenue Analysis' status is 'archived'."
            else:
                return False, f"Presentation 'Q4 2025 Revenue Analysis' has status='{pres.get('status')}', expected 'archived'."

    return False, "No presentation with title 'Q4 2025 Revenue Analysis' found."
