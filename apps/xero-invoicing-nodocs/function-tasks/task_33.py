import requests


def verify(server_url: str) -> tuple[bool, str]:
    resp = requests.get(f"{server_url}/api/state")
    if resp.status_code != 200:
        return False, "Could not retrieve application state."
    state = resp.json()

    con = next((c for c in state["contacts"] if c["name"] == "Coastal Cafe Group"), None)
    if not con:
        return False, "Contact 'Coastal Cafe Group' not found."
    if con["email"] != "accounts@coastalcafe.co.nz":
        return False, f"Expected email 'accounts@coastalcafe.co.nz', got '{con['email']}'"
    return True, "Coastal Cafe Group email updated correctly."
