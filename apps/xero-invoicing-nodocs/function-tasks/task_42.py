import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    settings = state["settings"]
    if settings.get("companyName") != "Kiwi Consulting Group Ltd":
        return False, f"Expected 'Kiwi Consulting Group Ltd', got '{settings.get('companyName')}'"
    return True, "Company name updated correctly."
