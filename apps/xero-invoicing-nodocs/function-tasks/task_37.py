import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    settings = state["settings"]
    if str(settings.get("defaultDueDateTerms")) != "30":
        return False, f"Expected defaultDueDateTerms '30', got '{settings.get('defaultDueDateTerms')}'"
    return True, "Default due date terms changed to 30."
