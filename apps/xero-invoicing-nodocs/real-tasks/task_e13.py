import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Update the company tax ID to NZ-98-765-432 in settings."""
    try:
        resp = requests.get(f"{server_url}/api/state")
        if resp.status_code != 200:
            return False, f"Failed to fetch state: HTTP {resp.status_code}"
        state = resp.json()
    except Exception as e:
        return False, f"Error fetching state: {e}"

    settings = state.get("settings", {})
    tax_id = settings.get("companyTaxId")

    if tax_id == "NZ-98-765-432":
        return True, "Company tax ID is set to 'NZ-98-765-432'"
    else:
        return False, f"settings.companyTaxId is '{tax_id}', expected 'NZ-98-765-432'"
