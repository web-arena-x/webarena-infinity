import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    presentations = state.get("presentations", [])
    for pres in presentations:
        if pres.get("title") == "Competitor Analysis Dashboard":
            return False, "Presentation 'Competitor Analysis Dashboard' still exists; it should have been deleted."

    return True, "Presentation 'Competitor Analysis Dashboard' has been successfully deleted."
