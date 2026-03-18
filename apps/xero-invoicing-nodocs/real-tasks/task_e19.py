import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Update the company email to finance@kiwiconsulting.co.nz in settings."""
    try:
        resp = requests.get(f"{server_url}/api/state")
        if resp.status_code != 200:
            return False, f"Failed to fetch state: HTTP {resp.status_code}"
        state = resp.json()
    except Exception as e:
        return False, f"Error fetching state: {e}"

    settings = state.get("settings", {})
    email = settings.get("companyEmail")

    if email == "finance@kiwiconsulting.co.nz":
        return True, "Company email is set to 'finance@kiwiconsulting.co.nz'"
    else:
        return False, f"settings.companyEmail is '{email}', expected 'finance@kiwiconsulting.co.nz'"
