import requests


def verify(server_url: str) -> tuple[bool, str]:
    """Change the default tax rate to No GST (0%) in settings."""
    try:
        resp = requests.get(f"{server_url}/api/state")
        if resp.status_code != 200:
            return False, f"Failed to fetch state: HTTP {resp.status_code}"
        state = resp.json()
    except Exception as e:
        return False, f"Error fetching state: {e}"

    settings = state.get("settings", {})
    default_tax_rate_id = settings.get("defaultTaxRateId")

    if default_tax_rate_id == "tax_3":
        return True, "Default tax rate has been changed to 'No GST (0%)' (tax_3)"
    else:
        return False, f"defaultTaxRateId is '{default_tax_rate_id}', expected 'tax_3'"
