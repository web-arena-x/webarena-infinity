import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."

    state = resp.json()
    settings = state.get("settings", {})

    default_pharmacy = settings.get("defaultPharmacy")
    if default_pharmacy != "pharm_002":
        return False, f"Default pharmacy is '{default_pharmacy}', expected 'pharm_002' (Walgreens)."

    return True, "Default pharmacy changed to Walgreens (pharm_002)."
