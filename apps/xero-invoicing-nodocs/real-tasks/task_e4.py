import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Change the company name in settings to Kiwi Consulting Group."""
    try:
        resp = requests.get(f"{server_url}/api/state")
        if resp.status_code != 200:
            return False, f"Failed to fetch state: HTTP {resp.status_code}"
        state = resp.json()
    except Exception as e:
        return False, f"Error fetching state: {e}"

    settings = state.get("settings", {})
    company_name = settings.get("companyName")

    if company_name == "Kiwi Consulting Group":
        return True, "Company name has been updated to 'Kiwi Consulting Group'"
    else:
        return False, f"Company name is '{company_name}', expected 'Kiwi Consulting Group'"
