import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    con = next((c for c in state["contacts"] if c["name"] == "Summit Financial Advisors"), None)
    if not con:
        return False, "Contact 'Summit Financial Advisors' not found."
    if con.get("taxId") != "NZ-55-777-888":
        return False, f"Expected tax ID 'NZ-55-777-888', got '{con.get('taxId')}'"
    return True, "Summit Financial Advisors tax ID updated correctly."
