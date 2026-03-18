import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    settings = state["settings"]
    expected_addr = "100 Victoria Street, Level 10, Auckland 1010, New Zealand"
    if settings.get("companyAddress") != expected_addr:
        return False, f"Wrong address: '{settings.get('companyAddress')}'"
    if settings.get("companyTaxId") != "NZ-98-765-432":
        return False, f"Wrong tax ID: '{settings.get('companyTaxId')}'"
    return True, "Company address and tax ID updated correctly."
