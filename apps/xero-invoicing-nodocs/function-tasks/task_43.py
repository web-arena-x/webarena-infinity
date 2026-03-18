import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    settings = state["settings"]
    if settings.get("companyEmail") != "billing@kiwiconsulting.co.nz":
        return False, f"Expected email 'billing@kiwiconsulting.co.nz', got '{settings.get('companyEmail')}'"
    if settings.get("companyPhone") != "+64 21 555 0200":
        return False, f"Expected phone '+64 21 555 0200', got '{settings.get('companyPhone')}'"
    return True, "Company email and phone updated correctly."
